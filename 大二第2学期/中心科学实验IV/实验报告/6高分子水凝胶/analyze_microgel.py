from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

ROOT = Path(__file__).resolve().parent
SRC_DIR = ROOT / "src"
IMG_DIR = SRC_DIR / "img"

ROOM_SUMMARY_FILE = SRC_DIR / "CHR" / "SUM.xls"
ROOM_MSD_FILE = SRC_DIR / "CHR" / "MSD.xls"
TEMP_SUMMARY_FILE = SRC_DIR / "SXB 变温" / "SUM 变温.xls"
TEMP_MSD_FILE = SRC_DIR / "SXB 变温" / "MSD 变温.xls"

UV_DATA = pd.DataFrame(
    {
        "temperature_c": [25, 30, 35, 40, 45, 50, 55, 60],
        "absorbance": [0.2604, 0.3264, 1.1778, 1.7564, 1.9928, 1.9158, 1.8282, 1.7429],
    }
)


@dataclass
class FitResult:
    name: str
    params: list[float]
    r2: float
    center: float


def boltzmann(x: np.ndarray, a1: float, a2: float, x0: float, dx: float) -> np.ndarray:
    return a2 + (a1 - a2) / (1.0 + np.exp((x - x0) / dx))


def boltzmann_derivative(
    x: np.ndarray, a1: float, a2: float, x0: float, dx: float
) -> np.ndarray:
    exp_term = np.exp((x - x0) / dx)
    return -((a1 - a2) * exp_term) / (dx * (1.0 + exp_term) ** 2)


def lorentz(
    x: np.ndarray, y0: float, area: float, x0: float, width: float
) -> np.ndarray:
    return y0 + (2.0 * area / np.pi) * (width / (4.0 * (x - x0) ** 2 + width**2))


def lorentz_derivative(
    x: np.ndarray, y0: float, area: float, x0: float, width: float
) -> np.ndarray:
    denom = (4.0 * (x - x0) ** 2 + width**2) ** 2
    return -(16.0 * area * width * (x - x0)) / (np.pi * denom)


def fit_curve(
    model_name: str,
    func,
    x: np.ndarray,
    y: np.ndarray,
    p0: list[float],
    bounds: tuple[list[float], list[float]] | None = None,
) -> FitResult:
    kwargs = {"maxfev": 100000}
    if bounds is not None:
        kwargs["bounds"] = bounds
    params, _ = curve_fit(func, x, y, p0=p0, **kwargs)
    pred = func(x, *params)
    ss_res = np.sum((y - pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r2 = 1.0 - ss_res / ss_tot
    center = float(params[2])
    return FitResult(model_name, [float(v) for v in params], float(r2), center)


def load_summary(path: Path) -> pd.DataFrame:
    df = pd.read_excel(path, header=4)
    df = df.dropna(how="all")
    df = df[df["Type"] == "DLS"].copy()
    return df


def load_distributions(path: Path, has_temperature: bool) -> pd.DataFrame:
    raw = pd.read_excel(path, header=None)
    records: list[dict[str, float | str | int]] = []
    for start in range(0, raw.shape[1], 3):
        sample = str(raw.iloc[0, start])
        diam = pd.to_numeric(raw.iloc[2:, start], errors="coerce")
        intensity = pd.to_numeric(raw.iloc[2:, start + 1], errors="coerce")
        volume = pd.to_numeric(raw.iloc[2:, start + 2], errors="coerce")
        block = pd.DataFrame(
            {
                "sample_id": sample,
                "diameter_nm": diam,
                "intensity_pct": intensity,
                "volume_pct": volume,
            }
        ).dropna()
        if has_temperature:
            match = re.search(r"@\s*([0-9.]+)", sample)
            if match:
                block["temperature_c"] = float(match.group(1))
        records.extend(block.to_dict("records"))
    return pd.DataFrame(records)


def build_room_summary() -> pd.DataFrame:
    room = load_summary(ROOM_SUMMARY_FILE)
    return room.loc[
        :, ["Sample ID", "Eff. Diam. (nm)", "Polydispersity", "Data Retained (%)"]
    ].rename(
        columns={
            "Sample ID": "sample_id",
            "Eff. Diam. (nm)": "effective_diameter_nm",
            "Polydispersity": "pdi",
            "Data Retained (%)": "data_retained_pct",
        }
    )


def build_temperature_summary() -> tuple[pd.DataFrame, pd.DataFrame]:
    temp = load_summary(TEMP_SUMMARY_FILE)
    temp["temperature_c"] = (
        temp["Sample ID"].str.extract(r"@\s*([0-9.]+)")[0].astype(float)
    )
    temp["is_outlier"] = temp["Polydispersity"] > 0.7

    grouped = (
        temp.groupby("temperature_c", as_index=False)
        .agg(
            mean_diameter_nm=("Eff. Diam. (nm)", "mean"),
            std_diameter_nm=("Eff. Diam. (nm)", "std"),
            mean_pdi=("Polydispersity", "mean"),
            n=("Eff. Diam. (nm)", "size"),
            outlier_count=("is_outlier", "sum"),
        )
        .sort_values("temperature_c")
    )

    filtered = temp[~temp["is_outlier"]].copy()
    filtered_grouped = (
        filtered.groupby("temperature_c", as_index=False)
        .agg(
            mean_diameter_nm=("Eff. Diam. (nm)", "mean"),
            std_diameter_nm=("Eff. Diam. (nm)", "std"),
            mean_pdi=("Polydispersity", "mean"),
            n=("Eff. Diam. (nm)", "size"),
        )
        .sort_values("temperature_c")
    )
    return grouped, filtered_grouped


def style_axes(ax: plt.Axes) -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(True, alpha=0.35)


def save_dls_raw_plot(temp_raw: pd.DataFrame, temp_filtered: pd.DataFrame) -> None:
    plt.style.use("bmh")
    fig, ax = plt.subplots(figsize=(7.2, 4.4), dpi=600)
    ax.errorbar(
        temp_raw["temperature_c"],
        temp_raw["mean_diameter_nm"],
        yerr=temp_raw["std_diameter_nm"],
        fmt="o-",
        linewidth=1,
        capsize=2,
        label="All replicates",
    )
    filtered_mask = temp_raw["outlier_count"] > 0
    if filtered_mask.any():
        ax.scatter(
            temp_raw.loc[filtered_mask, "temperature_c"],
            temp_raw.loc[filtered_mask, "mean_diameter_nm"],
            s=70,
            marker="D",
            label="Temperatures containing PDI outlier",
            zorder=4,
        )
    ax.plot(
        temp_filtered["temperature_c"],
        temp_filtered["mean_diameter_nm"],
        linestyle="--",
        linewidth=1.5,
        label="Outlier-filtered mean",
    )
    ax.set_xlabel("Temperature / degC")
    ax.set_ylabel("Effective diameter / nm")
    ax.set_title("Temperature-dependent DLS diameter")
    style_axes(ax)
    ax.legend(frameon=True, fontsize=8)
    fig.tight_layout()
    fig.savefig(IMG_DIR / "dls_temperature_raw.png", bbox_inches="tight")
    plt.close(fig)


def save_dls_dual_axis_plot(
    temp_filtered: pd.DataFrame, fit_result: FitResult, deriv_func
) -> None:
    """Create a dual-axis plot showing original fit and derivative."""
    x = temp_filtered["temperature_c"].to_numpy(dtype=float)
    y = temp_filtered["mean_diameter_nm"].to_numpy(dtype=float)
    x_dense = np.linspace(x.min(), x.max(), 400)
    y_fit = (
        fit_result.params[0]
        if fit_result.name == "boltzmann"
        else (
            fit_result.params[1]
            + (2.0 * fit_result.params[1] / np.pi)
            * (
                fit_result.params[3]
                / (
                    4.0 * (x_dense - fit_result.params[2]) ** 2
                    + fit_result.params[3] ** 2
                )
            )
        )
    )
    if fit_result.name == "boltzmann":
        y_fit = boltzmann(x_dense, *fit_result.params)
    else:
        y_fit = lorentz(x_dense, *fit_result.params)
    dydx = deriv_func(x_dense, *fit_result.params)

    plt.style.use("bmh")
    fig, ax1 = plt.subplots(figsize=(9, 4), dpi=600)

    # Original function and data on left y-axis (C0 color)
    ax1.scatter(x, y, s=55, label="Experimental data", zorder=3, color="C0")
    ax1.plot(
        x_dense,
        y_fit,
        linewidth=2.0,
        label=f"{fit_result.name.capitalize()} fit (R²={fit_result.r2:.3f})",
        color="C0",
    )
    ax1.axvline(fit_result.center, linestyle=":", linewidth=1.2, color="C0")
    ax1.set_xlabel("Temperature / degC")
    ax1.set_ylabel("Effective diameter / nm", color="C0")
    ax1.tick_params(axis="y", labelcolor="C0")
    style_axes(ax1)

    # Derivative on right y-axis (C1 color)
    ax2 = ax1.twinx()
    ax2.plot(x_dense, dydx, linewidth=2.0, label="First derivative", color="C1")
    ax2.set_ylabel("dD/dT", color="C1")
    ax2.tick_params(axis="y", labelcolor="C1")
    ax2.grid(True, alpha=0.35)

    # Combined legend at figure level so it renders above both axes
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    fig.legend(
        lines1 + lines2,
        labels1 + labels2,
        frameon=True,
        fontsize=7.5,
        loc="upper left",
        bbox_to_anchor=(0.01, 1.02),
        ncol=2,
    )

    fig.tight_layout(rect=[0, 0, 1, 0.95])
    return fig


def save_dls_boltzmann_dual_axis(temp_filtered: pd.DataFrame, boltz: FitResult) -> None:
    fig = save_dls_dual_axis_plot(temp_filtered, boltz, boltzmann_derivative)
    fig.savefig(IMG_DIR / "dls_boltzmann_dual_axis.png", bbox_inches="tight")
    plt.close(fig)


def save_dls_lorentz_dual_axis(temp_filtered: pd.DataFrame, lor: FitResult) -> None:
    fig = save_dls_dual_axis_plot(temp_filtered, lor, lorentz_derivative)
    fig.savefig(IMG_DIR / "dls_lorentz_dual_axis.png", bbox_inches="tight")
    plt.close(fig)


def save_uv_raw_plot(uv: pd.DataFrame) -> None:
    plt.style.use("bmh")
    fig, ax = plt.subplots(figsize=(7.2, 4.4), dpi=600)
    ax.plot(
        uv["temperature_c"],
        uv["absorbance"],
        marker="o",
        linewidth=2.0,
    )
    ax.set_xlabel("Temperature / degC")
    ax.set_ylabel("Absorbance at 500 nm")
    ax.set_title("Temperature-dependent UV-vis absorbance")
    style_axes(ax)
    fig.tight_layout()
    fig.savefig(IMG_DIR / "uv_temperature_raw.png", bbox_inches="tight")
    plt.close(fig)


def save_uv_dual_axis_plot(uv: pd.DataFrame, fit_result: FitResult, deriv_func) -> None:
    """Create a dual-axis plot showing original fit and derivative."""
    x = uv["temperature_c"].to_numpy(dtype=float)
    y = uv["absorbance"].to_numpy(dtype=float)
    x_dense = np.linspace(x.min(), x.max(), 400)
    if fit_result.name == "boltzmann":
        y_fit = boltzmann(x_dense, *fit_result.params)
    else:
        y_fit = lorentz(x_dense, *fit_result.params)
    dydx = deriv_func(x_dense, *fit_result.params)

    plt.style.use("bmh")
    fig, ax1 = plt.subplots(figsize=(9, 4), dpi=600)

    # Original function and data on left y-axis (C0 color)
    ax1.scatter(x, y, s=55, label="Experimental data", zorder=3, color="C0")
    ax1.plot(
        x_dense,
        y_fit,
        linewidth=2.0,
        label=f"{fit_result.name.capitalize()} fit (R²={fit_result.r2:.3f})",
        color="C0",
    )
    ax1.axvline(fit_result.center, linestyle=":", linewidth=1.2, color="C0")
    ax1.set_xlabel("Temperature / degC")
    ax1.set_ylabel("Absorbance at 500 nm", color="C0")
    ax1.tick_params(axis="y", labelcolor="C0")
    style_axes(ax1)

    # Derivative on right y-axis (C1 color)
    ax2 = ax1.twinx()
    ax2.plot(x_dense, dydx, linewidth=2.0, label="First derivative", color="C1")
    ax2.set_ylabel("dA/dT", color="C1")
    ax2.tick_params(axis="y", labelcolor="C1")
    ax2.grid(True, alpha=0.35)

    # Combined legend at figure level so it renders above both axes
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    fig.legend(
        lines1 + lines2,
        labels1 + labels2,
        frameon=True,
        fontsize=7.5,
        loc="upper left",
        bbox_to_anchor=(0.01, 1.02),
        ncol=2,
    )

    fig.tight_layout(rect=[0, 0, 1, 0.95])
    return fig


def save_uv_boltzmann_dual_axis(uv: pd.DataFrame, boltz: FitResult) -> None:
    fig = save_uv_dual_axis_plot(uv, boltz, boltzmann_derivative)
    fig.savefig(IMG_DIR / "uv_boltzmann_dual_axis.png", bbox_inches="tight")
    plt.close(fig)


def save_uv_lorentz_dual_axis(uv: pd.DataFrame, lor: FitResult) -> None:
    fig = save_uv_dual_axis_plot(uv, lor, lorentz_derivative)
    fig.savefig(IMG_DIR / "uv_lorentz_dual_axis.png", bbox_inches="tight")
    plt.close(fig)


def save_outputs() -> None:
    IMG_DIR.mkdir(exist_ok=True)
    room_summary = build_room_summary()
    room_dist = load_distributions(ROOM_MSD_FILE, has_temperature=False)
    temp_raw, temp_filtered = build_temperature_summary()
    temp_dist = load_distributions(TEMP_MSD_FILE, has_temperature=True)

    dls_boltz = fit_curve(
        "boltzmann",
        boltzmann,
        temp_filtered["temperature_c"].to_numpy(dtype=float),
        temp_filtered["mean_diameter_nm"].to_numpy(dtype=float),
        p0=[
            float(temp_filtered["mean_diameter_nm"].max()),
            float(temp_filtered["mean_diameter_nm"].min()),
            37.0,
            1.0,
        ],
    )
    dls_lorentz = fit_curve(
        "lorentz",
        lorentz,
        temp_filtered["temperature_c"].to_numpy(dtype=float),
        temp_filtered["mean_diameter_nm"].to_numpy(dtype=float),
        p0=[700.0, 10000.0, 38.0, 8.0],
    )
    uv_boltz = fit_curve(
        "boltzmann",
        boltzmann,
        UV_DATA["temperature_c"].to_numpy(dtype=float),
        UV_DATA["absorbance"].to_numpy(dtype=float),
        p0=[0.25, 1.9, 35.0, 2.0],
    )
    uv_lorentz = fit_curve(
        "lorentz",
        lorentz,
        UV_DATA["temperature_c"].to_numpy(dtype=float),
        UV_DATA["absorbance"].to_numpy(dtype=float),
        p0=[0.2, 50.0, 45.0, 20.0],
    )

    save_dls_raw_plot(temp_raw, temp_filtered)
    save_dls_boltzmann_dual_axis(temp_filtered, dls_boltz)
    save_dls_lorentz_dual_axis(temp_filtered, dls_lorentz)
    save_uv_raw_plot(UV_DATA)
    save_uv_boltzmann_dual_axis(UV_DATA, uv_boltz)
    save_uv_lorentz_dual_axis(UV_DATA, uv_lorentz)

    room_summary.to_csv(IMG_DIR / "room_dls_summary.csv", index=False)
    temp_raw.to_csv(IMG_DIR / "temperature_dls_summary_all.csv", index=False)
    temp_filtered.to_csv(IMG_DIR / "temperature_dls_summary_filtered.csv", index=False)
    UV_DATA.to_csv(IMG_DIR / "uv_absorbance_summary.csv", index=False)
    temp_dist.to_csv(IMG_DIR / "temperature_dls_distributions.csv", index=False)

    summary = {
        "room_temperature": {
            "mean_effective_diameter_nm": float(
                room_summary["effective_diameter_nm"].mean()
            ),
            "mean_pdi": float(room_summary["pdi"].mean()),
        },
        "dls_fit_filtered": {
            "boltzmann": dls_boltz.__dict__,
            "lorentz": dls_lorentz.__dict__,
        },
        "uv_fit": {
            "boltzmann": uv_boltz.__dict__,
            "lorentz": uv_lorentz.__dict__,
        },
        "outlier_rule": "temperature points with any replicate PDI > 0.7 are flagged; high-PDI replicates are excluded from Boltzmann fitting",
    }
    (IMG_DIR / "analysis_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


if __name__ == "__main__":
    save_outputs()
