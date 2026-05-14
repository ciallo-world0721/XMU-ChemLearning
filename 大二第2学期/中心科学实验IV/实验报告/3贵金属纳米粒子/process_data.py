from __future__ import annotations

import re
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from scipy.signal import find_peaks, savgol_filter


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "src" / "img"
SEM_DIR = OUT / "20260429-SEM"
RAMAN_APP_DIR = ROOT / "src" / "Raman_2026-05-08"
RAMAN_EC_DIR = ROOT / "src" / "Raman_100ms_531.81nm"
UVVIS_DIR = ROOT / "src" / "4.29 SYB"


plt.style.use("bmh")
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "Arial", "DejaVu Sans", "Liberation Sans", "Noto Sans CJK SC", "Apple LiGothic Medium", "sans-serif"]


def read_raman(path: Path) -> pd.DataFrame:
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    header_idx = next(i for i, line in enumerate(lines) if line.startswith("pixel"))
    rows = []
    for line in lines[header_idx + 1 :]:
        if not line.strip():
            continue
        parts = re.split(r"\s+", line.strip())
        if len(parts) < 5:
            continue
        rows.append([float(parts[0]), float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4])])
    return pd.DataFrame(rows, columns=["pixel", "wavelength", "wavenumber", "shift", "intensity"])


def read_uvvis(path: Path) -> pd.DataFrame:
    rows = []
    for line in path.read_text(errors="replace").splitlines()[2:]:
        parts = [part.strip().strip('"') for part in line.split(",")]
        if len(parts) < 2:
            continue
        try:
            rows.append((float(parts[0]), float(parts[1])))
        except ValueError:
            continue
    return pd.DataFrame(rows, columns=["wavelength", "absorbance"])


def uvvis_label_and_kind(path: Path) -> tuple[str, str]:
    stem = path.stem.replace("Group", "group")
    kind = "Au" if "Au" in stem else "Ag"
    match = re.search(r"group[-_]?([56])[-_]?([12])", stem, flags=re.IGNORECASE)
    amount_match = re.search(r"(?:Au|Ag)[-_]?(\d+)$", stem, flags=re.IGNORECASE)
    amount = amount_match.group(1) if amount_match else ""
    if match:
        label = f"{kind} G{match.group(1)}-{match.group(2)} {amount}".strip()
    else:
        label = f"{kind} {path.stem}"
    return kind, label


def smooth(y: np.ndarray) -> np.ndarray:
    if len(y) < 21:
        return y
    window = min(31, len(y) - (1 - len(y) % 2))
    if window % 2 == 0:
        window -= 1
    return savgol_filter(y, window, 3)


def norm_intensity(y: pd.Series | np.ndarray) -> np.ndarray:
    arr = np.asarray(y, dtype=float)
    arr = arr - np.nanpercentile(arr, 5)
    denom = np.nanpercentile(arr, 99)
    if denom <= 0:
        denom = np.nanmax(arr) or 1.0
    return arr / denom


def top_peaks(df: pd.DataFrame, low: float = 100, high: float = 1800, n: int = 5) -> list[tuple[float, float]]:
    sub = df[(df["shift"] >= low) & (df["shift"] <= high)].copy()
    y = smooth(sub["intensity"].to_numpy())
    prominence = max(np.nanstd(y) * 0.8, 1.0)
    peaks, props = find_peaks(y, prominence=prominence, distance=20)
    values = []
    for idx, prom in zip(peaks, props.get("prominences", np.zeros_like(peaks))):
        values.append((float(sub.iloc[idx]["shift"]), float(prom)))
    return sorted(values, key=lambda item: item[1], reverse=True)[:n]


def make_sem_montage() -> None:
    files = sorted(SEM_DIR.glob("2-*.jpg"))
    thumbs = []
    for path in files:
        img = Image.open(path).convert("RGB")
        img.thumbnail((420, 315), Image.Resampling.LANCZOS)
        canvas = Image.new("RGB", (440, 365), "white")
        canvas.paste(img, ((440 - img.width) // 2, 10))
        draw = ImageDraw.Draw(canvas)
        try:
            font = ImageFont.truetype("arial.ttf", 20)
        except OSError:
            font = ImageFont.load_default()
        draw.text((14, 330), path.stem, fill="black", font=font)
        thumbs.append(canvas)

    cols = 2
    rows = int(np.ceil(len(thumbs) / cols))
    montage = Image.new("RGB", (cols * 440, rows * 365), "white")
    for i, img in enumerate(thumbs):
        montage.paste(img, ((i % cols) * 440, (i // cols) * 365))
    montage.save(OUT / "sem_overview.png", dpi=(300, 300))


def plot_gem_raman(summary: list[str]) -> None:
    samples = [
        ("真钻石", "真钻石.txt"),
        ("假钻石", "假钻石.txt"),
        ("真翡翠", "真翡翠曝光1s.txt"),
        ("假翡翠", "假翡翠曝光1s.txt"),
    ]
    fig, axes = plt.subplots(2, 1, figsize=(10.2, 7.0), sharex=True)
    for ax, group in zip(axes, [samples[:2], samples[2:]]):
        for label, filename in group:
            df = read_raman(RAMAN_APP_DIR / filename)
            sub = df[(df["shift"] >= 100) & (df["shift"] <= 1800)]
            y = norm_intensity(smooth(sub["intensity"].to_numpy()))
            ax.plot(sub["shift"], y, lw=1.2, label=label)
            peaks = top_peaks(df, n=4)
            summary.append(f"{filename}: " + ", ".join(f"{p:.0f} cm^-1" for p, _ in peaks))
        ax.set_ylabel("归一化强度")
        ax.legend(loc="upper right", fontsize=9)
    axes[-1].set_xlabel("拉曼位移 / cm$^{-1}$")
    fig.tight_layout()
    fig.savefig(OUT / "raman_gem_comparison.png", dpi=600)
    plt.close(fig)


def plot_uvvis_reference(summary: list[str]) -> None:
    fig, axes = plt.subplots(2, 1, figsize=(7.2, 6.0), sharex=True, sharey=True)
    grouped: dict[str, list[tuple[str, Path]]] = {"Au": [], "Ag": []}
    for path in sorted(UVVIS_DIR.glob("*.txt")):
        if path.name.lower() == "group_6_2_au_600.txt":
            summary.append(f"{path.name}: excluded because this saved curve duplicates another Au spectrum")
            continue
        kind, label = uvvis_label_and_kind(path)
        grouped[kind].append((label, path))
    for ax, kind in zip(axes, ["Au", "Ag"]):
        for label, path in grouped[kind]:
            df = read_uvvis(path)
            sub = df[(df["wavelength"] >= 350) & (df["wavelength"] <= 750)]
            peak_row = sub.loc[sub["absorbance"].idxmax()]
            peak = float(peak_row["wavelength"])
            ax.plot(df["wavelength"], df["absorbance"], lw=1.3, label=f"{label}: {peak:.0f} nm")
            summary.append(f"{path.name}: UV-Vis peak {peak:.0f} nm, absorbance {float(peak_row['absorbance']):.3f}")
    for ax, title in zip(axes, ["Au 纳米粒子", "Ag 纳米粒子"]):
        ax.set_title(title)
        ax.set_xlabel("波长 / nm")
        ax.legend(fontsize=7)
    axes[0].set_ylabel("吸光度")
    axes[1].set_ylabel("吸光度")
    fig.tight_layout()
    fig.savefig(OUT / "uvvis_au_ag_reference.png", dpi=600)
    plt.close(fig)


def plot_malachite_sers(summary: list[str]) -> None:
    concentrations = ["0.1ppm", "1ppm", "10ppm", "100ppm"]
    treatments = [
        ("MG", "孔雀石绿曝光1s.txt"),
        ("MG + Ag", "孔雀石绿+Ag曝光1s.txt"),
        ("MG + Ag + NaI", "孔雀石绿+Ag+NaI曝光1s.txt"),
    ]
    fig, axes = plt.subplots(len(concentrations), 1, figsize=(7.2, 9.2), sharex=True)
    for row, conc in enumerate(concentrations):
        ax = axes[row]
        for label, suffix in treatments:
            filename = conc + suffix
            df = read_raman(RAMAN_APP_DIR / filename)
            sub = df[(df["shift"] >= 200) & (df["shift"] <= 1800)]
            y = norm_intensity(smooth(sub["intensity"].to_numpy()))
            ax.plot(sub["shift"], y, lw=1.0, label=label)
            if label.endswith("NaI"):
                peaks = top_peaks(df, low=300, high=1700, n=5)
                summary.append(f"{filename}: " + ", ".join(f"{p:.0f} cm^-1" for p, _ in peaks))
        ax.set_ylabel(conc)
        if row == 0:
            ax.legend(loc="upper right", fontsize=8, ncol=3)
    axes[-1].set_xlabel("拉曼位移 / cm$^{-1}$")
    fig.text(0.02, 0.5, "归一化强度", rotation="vertical", va="center")
    fig.tight_layout(rect=(0.04, 0.02, 1, 1))
    fig.savefig(OUT / "sers_malachite_green.png", dpi=600)
    plt.close(fig)


def plot_ec_sers(summary: list[str]) -> None:
    selected = []
    for path in sorted(RAMAN_EC_DIR.glob("*.txt")):
        match = re.search(r"v(-?\d+\.\d+)", path.stem)
        if match:
            selected.append((float(match.group(1)), path))
    fig, axes = plt.subplots(2, 1, figsize=(10, 6.8), sharex=True, sharey=True)
    for plotted, (potential, path) in enumerate(selected):
        df = read_raman(path)
        sub = df[(df["shift"] >= 400) & (df["shift"] <= 1800)]
        y = norm_intensity(smooth(sub["intensity"].to_numpy()))
        direction = "down" if plotted <= 7 else "return"
        ax = axes[0] if direction == "down" else axes[1]
        ax.plot(sub["shift"], y, lw=0.9, label=f"{potential:.1f} V")
        peaks = top_peaks(df, low=400, high=1800, n=3)
        summary.append(f"{path.name}: " + ", ".join(f"{p:.0f} cm^-1" for p, _ in peaks))
    for ax, title in zip(axes, ["向下扫描", "回程扫描"]):
        ax.set_title(title)
        ax.set_xlabel("拉曼位移 / cm$^{-1}$")
        ax.legend(title="电位", fontsize=7)
    axes[0].set_ylabel("归一化强度")
    fig.tight_layout()
    fig.savefig(OUT / "ec_sers_potential_series.png", dpi=600)
    plt.close(fig)


def peak_height_near(df: pd.DataFrame, target: float, window: float = 18) -> float:
    sub = df[(df["shift"] >= target - window) & (df["shift"] <= target + window)]
    base_region = df[(df["shift"] >= target - 90) & (df["shift"] <= target + 90)]
    if sub.empty or base_region.empty:
        return float("nan")
    baseline = float(np.nanpercentile(base_region["intensity"], 10))
    return float(sub["intensity"].max() - baseline)


def plot_ec_peak_trend(summary: list[str]) -> None:
    order = []
    for path in sorted(RAMAN_EC_DIR.glob("*.txt")):
        match = re.search(r"v(-?\d+\.\d+)", path.stem)
        if match:
            order.append((float(match.group(1)), path))
    potentials = [item[0] for item in order]
    x = np.arange(1, len(order) + 1)
    peaks = {"~588 cm$^{-1}$": [], "~1618 cm$^{-1}$": []}
    for _, path in order:
        df = read_raman(path)
        peaks["~588 cm$^{-1}$"].append(peak_height_near(df, 588))
        peaks["~1618 cm$^{-1}$"].append(peak_height_near(df, 1618))
    fig, ax = plt.subplots(figsize=(14, 4.2))
    for label, values in peaks.items():
        arr = np.asarray(values, dtype=float)
        arr = arr / np.nanmax(arr)
        ax.plot(x, arr, marker="o", lw=1.3, label=label)
    ax.axvline(8, color="0.35", ls="--", lw=1.0, label="拐点")
    ax.set_xticks(x)
    ax.set_xticklabels([f"{p:.1f}" for p in potentials], rotation=45, ha="right", fontsize=8)
    ax.set_xlabel("采集顺序下的施加电位 / V")
    ax.set_ylabel("归一化峰高")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(OUT / "ec_sers_peak_trend.png", dpi=600)
    plt.close(fig)
    summary.append("EC-SERS peak trend plotted for ca. 588 and 1618 cm^-1 over the full down-and-return sequence")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    summary: list[str] = []
    make_sem_montage()
    plot_uvvis_reference(summary)
    plot_gem_raman(summary)
    plot_malachite_sers(summary)
    plot_ec_sers(summary)
    plot_ec_peak_trend(summary)
    (ROOT / "analysis_summary.txt").write_text("\n".join(summary) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
