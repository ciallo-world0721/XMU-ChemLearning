from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


plt.style.use("bmh")

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
XPS_DIR = SRC / "DATE-XPS"
LEIS_DIR = SRC / "LEIS"
TPR_DIR = SRC / "第6组TPR（程序升温还原）_data" / "第六大组"

SAMPLE_LABELS = {
    "1": "I",
    "2": "II",
    "3": "III",
    "4": "IV",
}

# COLORS = {
#     "I": "#1f77b4",
#     "II": "#d62728",
#     "III": "#2ca02c",
#     "IV": "#ff7f0e",
# }


def load_two_column_data(
    path: Path, header_marker: str | None = None
) -> tuple[np.ndarray, np.ndarray]:
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    start = 0
    if header_marker is not None:
        for idx, line in enumerate(lines):
            if line.strip() == header_marker:
                start = idx + 1
                break
    x_values: list[float] = []
    y_values: list[float] = []
    for line in lines[start:]:
        parts = line.strip().split()
        if len(parts) != 2:
            continue
        try:
            x_values.append(float(parts[0]))
            y_values.append(float(parts[1]))
        except ValueError:
            continue
    return np.asarray(x_values), np.asarray(y_values)


def load_xps_region(path: Path, region_note: str) -> tuple[np.ndarray, np.ndarray]:
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    i = 0
    while i < len(lines):
        if lines[i].startswith("Region\tEnabled\tDataFlag"):
            if i + 1 >= len(lines):
                break
            region_parts = lines[i + 1].split("\t")
            note = region_parts[12].strip() if len(region_parts) > 12 else ""
            j = i + 2
            while j < len(lines) and lines[j].strip() != "Energy\tCounts":
                j += 1
            if note == region_note and j < len(lines):
                x_values: list[float] = []
                y_values: list[float] = []
                for line in lines[j + 1 :]:
                    if line.startswith("Region\tEnabled\tDataFlag"):
                        break
                    parts = line.strip().split()
                    if len(parts) != 2:
                        continue
                    try:
                        x_values.append(float(parts[0]))
                        y_values.append(float(parts[1]))
                    except ValueError:
                        continue
                return np.asarray(x_values), np.asarray(y_values)
        i += 1
    raise ValueError(f"Region {region_note!r} not found in {path}")


def normalize(y_values: np.ndarray) -> np.ndarray:
    max_value = float(np.max(y_values))
    if max_value <= 0:
        return y_values
    return y_values / max_value


def parse_xps_files() -> dict[str, dict[str, tuple[np.ndarray, np.ndarray]]]:
    spectra: dict[str, dict[str, tuple[np.ndarray, np.ndarray]]] = {"RT": {}, "H2": {}}
    for path in sorted(XPS_DIR.glob("*.txt")):
        sample_id = path.name.split("-", 1)[0]
        label = SAMPLE_LABELS.get(sample_id)
        if label is None:
            continue
        condition = "H2" if "500-H2" in path.name else "RT"
        energy, counts = load_xps_region(path, region_note="Ni")
        spectra[condition][label] = (energy, normalize(counts))
    return spectra


def parse_properties(path: Path) -> tuple[str, str]:
    species = ""
    energy = ""
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        if line.startswith("Instrument.PrimaryGun.Species\t"):
            species = line.split("\t", 1)[1].strip()
        elif line.startswith("Instrument.PrimaryGun.ParticleEnergy\t"):
            energy = line.split("\t", 1)[1].strip()
    species = "He" if "He" in species else species
    return species, energy


def parse_leis_files() -> dict[
    tuple[str, str], dict[str, tuple[np.ndarray, np.ndarray]]
]:
    grouped: dict[tuple[str, str], dict[str, tuple[np.ndarray, np.ndarray]]] = {}
    for path in sorted(LEIS_DIR.glob("*.txt")):
        if path.name.endswith(".properties.txt"):
            continue
        parts = path.stem.split("-")
        if len(parts) < 2:
            continue
        label = SAMPLE_LABELS.get(parts[1])
        if label is None:
            continue
        species, energy = parse_properties(
            path.with_name(path.stem + ".properties.txt")
        )
        key = (species, energy)
        x_values, y_values = load_two_column_data(path)
        grouped.setdefault(key, {})[label] = (x_values, normalize(y_values))
    return grouped


def load_tpr_csv(path: Path) -> tuple[np.ndarray, np.ndarray]:
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    x_values: list[float] = []
    y_values: list[float] = []
    for line in lines[1:]:
        parts = [part.strip() for part in line.split(",")]
        if len(parts) < 4:
            continue
        try:
            x_values.append(float(parts[2]))
            y_values.append(float(parts[3]))
        except ValueError:
            continue
    return np.asarray(x_values), np.asarray(y_values)


def baseline_correct(y_values: np.ndarray, points: int = 300) -> np.ndarray:
    baseline = float(np.mean(y_values[:points]))
    return y_values - baseline


def parse_tpr_files() -> dict[str, tuple[np.ndarray, np.ndarray]]:
    spectra: dict[str, tuple[np.ndarray, np.ndarray]] = {}
    for sample_id, label in SAMPLE_LABELS.items():
        sample_dir = TPR_DIR / f"第六组 催化剂{sample_id}#"
        matches = sorted(sample_dir.glob("通道B*--信号文件.CSV"))
        if not matches:
            continue
        temperature, signal = load_tpr_csv(matches[0])
        spectra[label] = (temperature, baseline_correct(signal))
    return spectra


def is_end_drift(x_values: np.ndarray, y_values: np.ndarray) -> bool:
    peak_index = int(np.argmax(y_values))
    if peak_index < int(0.95 * len(y_values)):
        return False
    correlation = float(np.corrcoef(x_values, y_values)[0, 1])
    return correlation > 0.98


def save_tpr_plot() -> None:
    spectra = parse_tpr_files()
    fig, axes = plt.subplots(2, 2, figsize=(9.6, 7.2), sharex=False, sharey=False)
    panel_titles = {
        "I": "I 1# no NH3",
        "II": "II 1# NH3",
        "III": "III 2# no NH3",
        "IV": "IV 2# NH3",
    }
    for ax, label in zip(axes.flat, ("I", "II", "III", "IV")):
        x_values, y_values = spectra[label]
        ax.plot(x_values, y_values, lw=1.1)
        ax.set_title(panel_titles[label], fontsize=11)
        ax.set_xlabel("Instrument temperature signal")
        ax.set_ylabel("Baseline-corrected signal / a.u.")
        ax.grid(alpha=0.18)
        if is_end_drift(x_values, y_values):
            ax.text(
                0.04,
                0.90,
                "No resolved peak\nend-segment drift",
                transform=ax.transAxes,
                fontsize=8.5,
                color="#444444",
            )
        else:
            peak_index = int(np.argmax(y_values))
            peak_x = x_values[peak_index]
            peak_y = y_values[peak_index]
            ax.scatter([peak_x], [peak_y], color="red", s=12, zorder=3)
            ax.text(
                0.04,
                0.90,
                f"Peak ~ {peak_x:.1f}",
                transform=ax.transAxes,
                fontsize=8.5,
            )
    fig.tight_layout()
    fig.savefig(SRC / "TPR图谱.png", dpi=400, bbox_inches="tight")
    plt.close(fig)


def save_xps_plot() -> None:
    spectra = parse_xps_files()
    fig, axes = plt.subplots(2, 1, figsize=(8.2, 8.0), sharex=True, sharey=True)
    panels = [
        ("RT", "Room temperature"),
        ("H2", "500 C H2-treated"),
    ]
    for ax, (key, title) in zip(axes, panels):
        for label in ("I", "II", "III", "IV"):
            energy, intensity = spectra[key][label]
            ax.plot(energy, intensity, lw=1, label=label)
        ax.set_xlim(890, 845)
        ax.set_ylim(0.6, 1.08)
        ax.set_ylabel("Normalized intensity / a.u.")
        ax.set_title(title, fontsize=11)
        ax.grid(alpha=0.18)
        ax.legend(ncol=4, frameon=False, fontsize=9, loc="upper left")
    axes[-1].set_xlabel("Binding energy / eV")
    fig.suptitle("XPS Ni 2p comparison", fontsize=13)
    fig.tight_layout()
    fig.savefig(SRC / "xps_ni2p_comparison.png", dpi=400, bbox_inches="tight")
    plt.close(fig)


def save_leis_plot() -> None:
    grouped = parse_leis_files()
    fig, axes = plt.subplots(2, 1, figsize=(8.2, 8.0), sharex=False, sharey=True)
    panels = [
        (("He", "3000"), "LEIS comparison under He+ 3 keV"),
        (("Ne", "5000"), "LEIS comparison under Ne+ 5 keV"),
    ]
    for ax, (key, title) in zip(axes, panels):
        spectra = grouped[key]
        for label in ("I", "II", "III", "IV"):
            x_values, intensity = spectra[label]
            ax.plot(x_values, intensity, lw=1, label=label)
        ax.set_ylabel("Normalized intensity / a.u.")
        ax.set_title(title, fontsize=11)
        ax.grid(alpha=0.18)
        ax.legend(ncol=4, frameon=False, fontsize=9, loc="upper right")
    axes[-1].set_xlabel("Scattered ion energy / eV")
    fig.suptitle("LEIS spectra under matched beam conditions", fontsize=13)
    fig.tight_layout()
    fig.savefig(SRC / "leis_comparison.png", dpi=400, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    save_tpr_plot()
    save_xps_plot()
    save_leis_plot()
    print("Created src/TPR图谱.png")
    print("Created src/xps_ni2p_comparison.png")
    print("Created src/leis_comparison.png")


if __name__ == "__main__":
    main()
