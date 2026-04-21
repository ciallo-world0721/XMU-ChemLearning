from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


plt.style.use("bmh")


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
XPS_DIR = SRC / "DATE-XPS"

SAMPLE_LABELS = {
    "1": "I",
    "2": "II",
    "3": "III",
    "4": "IV",
}

COLORS = {
    "I": "#1f77b4",
    "II": "#d62728",
    "III": "#2ca02c",
    "IV": "#ff7f0e",
}

REGIONS = [
    ("", "Survey", (1400, 0)),
    ("O", "O 1s", (545, 525)),
    ("c", "C 1s", (295, 275)),
    ("Si", "Si 2p", (110, 90)),
    ("Ni", "Ni 2p", (890, 840)),
    ("O V", "O V", (545, 525)),
]


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
                energy: list[float] = []
                counts: list[float] = []
                for line in lines[j + 1 :]:
                    if line.startswith("Region\tEnabled\tDataFlag"):
                        break
                    parts = line.strip().split()
                    if len(parts) != 2:
                        continue
                    try:
                        energy.append(float(parts[0]))
                        counts.append(float(parts[1]))
                    except ValueError:
                        continue
                return np.asarray(energy), np.asarray(counts)
        i += 1
    raise ValueError(f"Region {region_note!r} not found in {path}")


def normalize(counts: np.ndarray) -> np.ndarray:
    peak = float(np.max(counts))
    if peak <= 0:
        return counts
    return counts / peak


def parse_xps() -> dict[str, dict[str, dict[str, tuple[np.ndarray, np.ndarray]]]]:
    spectra: dict[str, dict[str, dict[str, tuple[np.ndarray, np.ndarray]]]] = {
        "RT": {note: {} for note, _, _ in REGIONS},
        "H2": {note: {} for note, _, _ in REGIONS},
    }
    for path in sorted(XPS_DIR.glob("*.txt")):
        sample_id = path.name.split("-", 1)[0]
        label = SAMPLE_LABELS.get(sample_id)
        if label is None:
            continue
        condition = "H2" if "500-H2" in path.name else "RT"
        for note, _, _ in REGIONS:
            energy, counts = load_xps_region(path, note)
            spectra[condition][note][label] = (energy, normalize(counts))
    return spectra


def plot_condition_grid(
    spectra: dict[str, dict[str, tuple[np.ndarray, np.ndarray]]],
    title: str,
    output_name: str,
) -> None:
    fig, axes = plt.subplots(2, 3, figsize=(12.8, 7.8), sharey=False)
    for ax, (note, label, xlim) in zip(axes.flat, REGIONS):
        for sample in ("I", "II", "III", "IV"):
            energy, intensity = spectra[note][sample]
            ax.plot(energy, intensity, lw=1.2, color=COLORS[sample], label=sample)
        ax.set_title(label, fontsize=11)
        ax.set_xlim(*xlim)
        ax.set_ylim(-0.02, 1.08)
        ax.set_xlabel("Binding energy / eV")
        ax.set_ylabel("Normalized intensity / a.u.")
        ax.grid(alpha=0.18)
    handles, labels = axes.flat[0].get_legend_handles_labels()
    fig.legend(
        handles,
        labels,
        ncol=4,
        frameon=False,
        loc="upper center",
        bbox_to_anchor=(0.5, 0.99),
    )
    fig.suptitle(title, fontsize=14, y=1.02)
    fig.tight_layout()
    fig.savefig(SRC / output_name, dpi=400, bbox_inches="tight")
    plt.close(fig)


def plot_ni_focus(
    spectra: dict[str, dict[str, dict[str, tuple[np.ndarray, np.ndarray]]]],
) -> None:
    fig, axes = plt.subplots(2, 1, figsize=(8.2, 8.0), sharex=True, sharey=True)
    for ax, condition, title in zip(
        axes,
        ("RT", "H2"),
        ("Room temperature", "500 C H2-treated"),
    ):
        for sample in ("I", "II", "III", "IV"):
            energy, intensity = spectra[condition]["Ni"][sample]
            ax.plot(energy, intensity, lw=1.2, color=COLORS[sample], label=sample)
        ax.set_xlim(890, 845)
        ax.set_ylim(0.0, 1.08)
        ax.set_ylabel("Normalized intensity / a.u.")
        ax.set_title(title, fontsize=11)
        ax.grid(alpha=0.18)
        ax.legend(ncol=4, frameon=False, fontsize=9, loc="upper left")
    axes[-1].set_xlabel("Binding energy / eV")
    fig.suptitle("XPS Ni 2p comparison", fontsize=13)
    fig.tight_layout()
    fig.savefig(SRC / "xps_ni2p_comparison.png", dpi=400, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    spectra = parse_xps()
    plot_condition_grid(
        spectra["RT"],
        "XPS full-region comparison at room temperature",
        "xps_full_regions_rt.png",
    )
    plot_condition_grid(
        spectra["H2"],
        "XPS full-region comparison after 500 C H2 treatment",
        "xps_full_regions_h2.png",
    )
    plot_ni_focus(spectra)
    print(f"Created {SRC / 'xps_full_regions_rt.png'}")
    print(f"Created {SRC / 'xps_full_regions_h2.png'}")
    print(f"Created {SRC / 'xps_ni2p_comparison.png'}")


if __name__ == "__main__":
    main()
