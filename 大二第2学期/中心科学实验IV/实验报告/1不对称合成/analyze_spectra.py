from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parent
SRC_DIR = ROOT / "src"
UV_DIR = SRC_DIR / "uv"
CD1_DIR = SRC_DIR / "cd" / "1"
CD2_DIR = SRC_DIR / "cd" / "2"
IMG_DIR = SRC_DIR / "img"

PURE_DELTA_E = 0.336


def sample_label(file_path: Path) -> str:
    suffix = file_path.stem.split("-")[-1]
    return f"Sample {suffix}"


@dataclass
class UVSpectrum:
    sample: str
    wavelength: list[float]
    absorbance: list[float]

    def nearest(self, target_nm: float) -> tuple[float, float]:
        return min(
            zip(self.wavelength, self.absorbance),
            key=lambda item: abs(item[0] - target_nm),
        )


@dataclass
class CDSpectrum:
    sample: str
    y_units: str
    delta_x: float
    wavelength: list[float]
    signal: list[float]

    def nearest(self, target_nm: float) -> tuple[float, float]:
        return min(
            zip(self.wavelength, self.signal), key=lambda item: abs(item[0] - target_nm)
        )


def configure_plot_style() -> None:
    plt.style.use("bmh")
    plt.rcParams["font.family"] = ["Times New Roman", "SimSun", "DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False
    plt.rcParams["figure.dpi"] = 150
    plt.rcParams["savefig.dpi"] = 300


def parse_uv_file(file_path: Path) -> UVSpectrum:
    lines = file_path.read_text(encoding="gb18030", errors="ignore").splitlines()
    rows: list[tuple[float, float]] = []
    for line in lines:
        parts = [part.strip() for part in line.split(",")]
        if len(parts) < 2:
            continue
        try:
            wavelength = float(parts[0])
            absorbance = float(parts[1])
        except ValueError:
            continue
        rows.append((wavelength, absorbance))
    if not rows:
        raise ValueError(f"No numeric UV data found in {file_path}")
    return UVSpectrum(
        sample=sample_label(file_path),
        wavelength=[row[0] for row in rows],
        absorbance=[row[1] for row in rows],
    )


def parse_cd_file(file_path: Path) -> CDSpectrum:
    lines = file_path.read_text(encoding="utf-8", errors="ignore").splitlines()
    meta: dict[str, str] = {}
    for line in lines[:20]:
        parts = line.split("\t")
        if len(parts) >= 2:
            meta[parts[0].strip()] = parts[1].strip()
    try:
        start_index = lines.index("XYDATA") + 1
    except ValueError as exc:
        raise ValueError(f"Missing XYDATA marker in {file_path}") from exc

    rows: list[tuple[float, float]] = []
    for line in lines[start_index:]:
        parts = [part for part in line.split("\t") if part != ""]
        if len(parts) < 2:
            continue
        try:
            wavelength = float(parts[0])
            signal = float(parts[1])
        except ValueError:
            continue
        rows.append((wavelength, signal))
    if not rows:
        raise ValueError(f"No numeric CD data found in {file_path}")

    return CDSpectrum(
        sample=sample_label(file_path),
        y_units=meta.get("YUNITS", ""),
        delta_x=float(meta.get("DELTAX", "0") or 0),
        wavelength=[row[0] for row in rows],
        signal=[row[1] for row in rows],
    )


def load_uv_spectra() -> list[UVSpectrum]:
    return [parse_uv_file(path) for path in sorted(UV_DIR.glob("*.csv"))]


def load_cd_spectra(directory: Path) -> list[CDSpectrum]:
    return [parse_cd_file(path) for path in sorted(directory.glob("*.txt"))]


def save_figure(base_name: str) -> None:
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(IMG_DIR / f"{base_name}.pdf")
    plt.savefig(IMG_DIR / f"{base_name}.png")
    plt.close()


def plot_uv_overlay(spectra: Iterable[UVSpectrum]) -> None:
    plt.figure(figsize=(8.2, 5.0))
    for spectrum in spectra:
        plt.plot(
            spectrum.wavelength,
            spectrum.absorbance,
            linewidth=1.8,
            label=spectrum.sample,
        )
    plt.xlabel("波长 / nm")
    plt.ylabel("吸光度")
    plt.title("结晶后样品的 UV-Vis 光谱")
    plt.xlim(350, 700)
    plt.legend(frameon=True)
    save_figure("uv_vis_overlay")


def plot_uv_visible_zoom(spectra: Iterable[UVSpectrum]) -> None:
    plt.figure(figsize=(8.2, 5.0))
    for spectrum in spectra:
        plt.plot(
            spectrum.wavelength,
            spectrum.absorbance,
            linewidth=1.8,
            label=spectrum.sample,
        )
        peak_x, peak_y = spectrum.nearest(542.0)
        plt.scatter([peak_x], [peak_y], s=24)
    plt.xlabel("波长 / nm")
    plt.ylabel("吸光度")
    plt.title("结晶后样品在可见区的 UV-Vis 光谱")
    plt.xlim(500, 590)
    plt.ylim(0.1, 0.24)
    plt.legend(frameon=True)
    save_figure("uv_vis_peak_zoom")


def plot_cd_overlay(
    spectra: Iterable[CDSpectrum],
    title: str,
    ylabel: str,
    base_name: str,
    xlim: tuple[float, float] = (350, 680),
) -> None:
    plt.figure(figsize=(8.2, 5.0))
    for spectrum in spectra:
        plt.plot(
            spectrum.wavelength, spectrum.signal, linewidth=1.6, label=spectrum.sample
        )
    plt.axhline(0, color="black", linewidth=0.8)
    plt.xlabel("波长 / nm")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xlim(*xlim)
    plt.legend(frameon=True)
    save_figure(base_name)


def build_summary(
    uv_spectra: list[UVSpectrum], cd2_spectra: list[CDSpectrum]
) -> list[dict[str, float | str]]:
    uv_by_sample = {spectrum.sample: spectrum for spectrum in uv_spectra}
    summary: list[dict[str, float | str]] = []
    for spectrum in cd2_spectra:
        uv = uv_by_sample[spectrum.sample]
        _, a_542 = uv.nearest(542.0)
        _, delta_e_560 = spectrum.nearest(560.0)
        approx_ee = abs(delta_e_560) / PURE_DELTA_E * 100
        summary.append(
            {
                "sample": spectrum.sample,
                "a_542": round(a_542, 6),
                "delta_e_560": round(delta_e_560, 6),
                "approx_ee_pct": round(approx_ee, 1),
            }
        )
    return summary


def main() -> None:
    configure_plot_style()
    uv_spectra = load_uv_spectra()
    cd1_spectra = load_cd_spectra(CD1_DIR)
    cd2_spectra = load_cd_spectra(CD2_DIR)

    plot_uv_overlay(uv_spectra)
    plot_uv_visible_zoom(uv_spectra)
    plot_cd_overlay(
        cd1_spectra,
        "前期上清液的 CD 光谱（原始 mdeg 数据）",
        "CD / mdeg",
        "cd_week1_overlay",
    )
    plot_cd_overlay(
        cd2_spectra,
        "结晶后样品的 CD 光谱（Molar CD）",
        r"$\Delta\varepsilon$ / (L mol$^{-1}$ cm$^{-1}$)",
        "cd_week2_overlay",
    )
    plot_cd_overlay(
        cd2_spectra,
        "结晶后样品在可见区的 CD 光谱",
        r"$\Delta\varepsilon$ / (L mol$^{-1}$ cm$^{-1}$)",
        "cd_week2_visible_zoom",
        xlim=(450, 620),
    )

    summary = build_summary(uv_spectra, cd2_spectra)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
