from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parent
WORKBOOK = ROOT / "src" / "260522-6-1.xlsx"
IMG_DIR = ROOT / "src" / "img"
SHEET = "Sheet4"


@dataclass(frozen=True)
class BradfordResult:
    concentrations: np.ndarray
    a_std: np.ndarray
    c_std: np.ndarray
    mean_std: np.ndarray
    ac_err: np.ndarray
    slope_a: float
    slope_c: float
    slope_mean: float
    r2_a: float
    r2_c: float
    r2_mean: float
    a_measured: np.ndarray
    c_measured: np.ndarray
    mean_original: np.ndarray
    sample_std: np.ndarray
    selected_mean: float
    selected_std: float


def setup_style() -> None:
    plt.style.use("bmh")
    plt.rcParams.update(
        {
            "font.family": "Microsoft YaHei",
            "axes.unicode_minus": False,
            "figure.dpi": 200,
            "savefig.dpi": 600,
            "axes.labelsize": 10,
            "axes.titlesize": 11,
            "legend.fontsize": 9,
            "xtick.labelsize": 9,
            "ytick.labelsize": 9,
        }
    )


def fit_through_origin(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    slope = float((x @ y) / (x @ x))
    pred = slope * x
    r2 = float(1 - ((y - pred) ** 2).sum() / ((y - y.mean()) ** 2).sum())
    return slope, r2


def compute() -> BradfordResult:
    if not WORKBOOK.exists():
        raise FileNotFoundError(WORKBOOK)

    df = pd.read_excel(WORKBOOK, sheet_name=SHEET, header=None)
    a = df.iloc[25, 1:13].to_numpy(dtype=float)
    c = df.iloc[27, 1:13].to_numpy(dtype=float)

    concentrations = np.array([125, 250, 500, 750, 1000], dtype=float)
    water_a = a[0]
    water_c = c[0]
    water_mean = (water_a + water_c) / 2
    ref_a = a[6]
    ref_c = c[6]
    ref_mean = (ref_a + ref_c) / 2

    a_std = a[1:6] - water_a
    c_std = c[1:6] - water_c
    mean_std = ((a[1:6] - water_mean) + (c[1:6] - water_mean)) / 2
    ac_err = np.abs(a_std - c_std) / 2

    slope_a, r2_a = fit_through_origin(concentrations, a_std)
    slope_c, r2_c = fit_through_origin(concentrations, c_std)
    slope_mean, r2_mean = fit_through_origin(concentrations, mean_std)

    a_measured = (a[7:12] - ref_a) / slope_a
    c_measured = (c[7:12] - ref_c) / slope_c
    mean_measured = (a_measured + c_measured) / 2
    dilutions = np.array([5, 10, 20, 40, 80], dtype=float)
    mean_original = mean_measured * dilutions
    sample_std = np.abs(a_measured - c_measured) / 2 * dilutions

    selected = mean_original[[1, 2, 3]]
    return BradfordResult(
        concentrations=concentrations,
        a_std=a_std,
        c_std=c_std,
        mean_std=mean_std,
        ac_err=ac_err,
        slope_a=slope_a,
        slope_c=slope_c,
        slope_mean=slope_mean,
        r2_a=r2_a,
        r2_c=r2_c,
        r2_mean=r2_mean,
        a_measured=a_measured,
        c_measured=c_measured,
        mean_original=mean_original,
        sample_std=sample_std,
        selected_mean=float(selected.mean()),
        selected_std=float(selected.std(ddof=1)),
    )


def save_ab_compare(result: BradfordResult) -> Path:
    out = IMG_DIR / "bradford_curve_ab.png"
    fig, ax = plt.subplots(figsize=(8.0, 4.2))
    ax.errorbar(result.concentrations, result.a_std, yerr=result.ac_err,
                fmt="o", color="#3B82F6", ms=5, capsize=4, lw=0.9,
                label="A行校正值")
    ax.errorbar(result.concentrations, result.c_std, yerr=result.ac_err,
                fmt="s", color="#EF4444", ms=5, capsize=4, lw=0.9,
                label="C行校正值")
    x = np.linspace(0, 1050, 200)
    ax.plot(x, result.slope_a * x, "--", color="#3B82F6", lw=1.0, label=f"A行拟合: y={result.slope_a:.4f}x, R²={result.r2_a:.3f}")
    ax.plot(x, result.slope_c * x, "--", color="#EF4444", lw=1.0, label=f"C行拟合: y={result.slope_c:.4f}x, R²={result.r2_c:.3f}")
    ax.set_xlim(0, 1050)
    ax.set_ylim(0, max(result.a_std.max(), result.c_std.max()) * 1.15)
    ax.set_xlabel("BSA浓度 (μg/mL)")
    ax.set_ylabel("吸光度 (595 nm, 校正后)")
    ax.set_title("Bradford法 BSA 标准曲线（过原点，A行与C行对比）")
    ax.legend(frameon=True, loc="lower right")
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    return out


def save_mean_curve(result: BradfordResult) -> Path:
    out = IMG_DIR / "bradford_curve_mean.png"
    fig, ax = plt.subplots(figsize=(8.0, 4.2))
    ax.errorbar(result.concentrations, result.mean_std, yerr=result.ac_err,
                fmt="o", color="#2563EB", ms=6, capsize=4, lw=1.0,
                label="校正后BSA实测值 (A/C均值 ± 半间距)")
    x = np.linspace(0, 1050, 200)
    ax.plot(x, result.slope_mean * x, "--", color="#DC2626", lw=1.1, label=f"过原点拟合: y={result.slope_mean:.4f}x\nR² = {result.r2_mean:.3f}")
    ax.set_xlim(0, 1050)
    ax.set_ylim(0, result.mean_std.max() * 1.15)
    ax.set_xlabel("BSA浓度 (μg/mL)")
    ax.set_ylabel("吸光度 (595 nm, 校正后)")
    ax.set_title("Bradford法 BSA 标准曲线（过原点）")
    ax.legend(frameon=True, loc="lower right")
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    return out


def main() -> None:
    setup_style()
    result = compute()
    outputs = [save_ab_compare(result), save_mean_curve(result)]
    for output in outputs:
        print(output)
    for i, d in enumerate([5, 10, 20, 40, 80]):
        print(f"dilution_{d}x_mean={result.mean_original[i]:.1f} std={result.sample_std[i]:.1f}")
    print(f"selected_mean_ug_per_mL={result.selected_mean:.1f}")
    print(f"selected_std_ug_per_mL={result.selected_std:.1f}")


if __name__ == "__main__":
    main()
