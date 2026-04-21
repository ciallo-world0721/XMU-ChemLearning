from pathlib import Path
import csv

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


plt.style.use("bmh")


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
TPR_DIR = SRC / "第6组TPR（程序升温还原）_data" / "第六大组"
OUTPUT = SRC / "TPR图谱.png"

SAMPLES = {
    "1": {"title": "I 1# no NH3", "room_temp": 14.0},
    "2": {"title": "II 1# NH3", "room_temp": 19.0},
    "3": {"title": "III 2# no NH3", "room_temp": 16.0},
    "4": {"title": "IV 2# NH3", "room_temp": 16.0},
}


def load_channel_csv(path: Path) -> tuple[np.ndarray, np.ndarray]:
    times: list[float] = []
    signals: list[float] = []
    with path.open("r", encoding="utf-8", errors="ignore", newline="") as handle:
        reader = csv.reader(handle)
        next(reader, None)
        for row in reader:
            if len(row) < 2:
                continue
            try:
                times.append(float(row[0]))
                signals.append(float(row[1]))
            except ValueError:
                continue
    return np.asarray(times), np.asarray(signals)


def b_signal_to_temperature(b_signal: np.ndarray, room_temp: float) -> np.ndarray:
    return b_signal * 23.946 / 1000.0 + 15.423 + room_temp


def baseline_correct(signal: np.ndarray, points: int = 300) -> np.ndarray:
    baseline = float(np.mean(signal[:points]))
    return signal - baseline


def moving_average(y_values: np.ndarray, window: int = 41) -> np.ndarray:
    window = max(5, window | 1)
    pad = window // 2
    padded = np.pad(y_values, (pad, pad), mode="edge")
    kernel = np.ones(window) / window
    return np.convolve(padded, kernel, mode="valid")


def is_end_drift(x_values: np.ndarray, y_values: np.ndarray) -> bool:
    peak_index = int(np.argmax(y_values))
    if peak_index < int(0.95 * len(y_values)):
        return False
    correlation = float(np.corrcoef(x_values, y_values)[0, 1])
    return correlation > 0.98


def load_all_samples() -> dict[str, tuple[np.ndarray, np.ndarray]]:
    spectra: dict[str, tuple[np.ndarray, np.ndarray]] = {}
    for sample_id, meta in SAMPLES.items():
        sample_dir = TPR_DIR / f"第六组 催化剂{sample_id}#"
        a_matches = sorted(sample_dir.glob("通道A*--信号文件.CSV"))
        b_matches = sorted(sample_dir.glob("通道B*--信号文件.CSV"))
        if not a_matches or not b_matches:
            raise FileNotFoundError(f"Missing TPR CSV for sample {sample_id}")
        a_time, a_signal = load_channel_csv(a_matches[0])
        b_time, b_signal = load_channel_csv(b_matches[0])
        if len(a_time) != len(b_time) or not np.allclose(a_time, b_time, atol=1e-9):
            raise ValueError(f"A/B channels are not aligned for sample {sample_id}")
        temperature = b_signal_to_temperature(b_signal, meta["room_temp"])
        response = moving_average(baseline_correct(a_signal))
        spectra[sample_id] = (temperature, response)
    return spectra


def main() -> None:
    spectra = load_all_samples()
    fig, axes = plt.subplots(2, 2, figsize=(9.6, 7.0), sharex=False, sharey=False)

    for ax, sample_id in zip(axes.flat, ("1", "2", "3", "4")):
        x_values, y_values = spectra[sample_id]
        drift = is_end_drift(x_values, y_values)
        color = "#6c757d" if drift else "#0072B2"
        ax.plot(x_values, y_values, lw=1.4, color=color)
        ax.set_title(SAMPLES[sample_id]["title"], fontsize=11)
        ax.set_xlabel("Converted temperature / degC")
        ax.set_ylabel("Baseline-subtracted signal / a.u.")
        ax.grid(alpha=0.2)

        if drift:
            ax.text(
                0.04,
                0.88,
                "No resolved peak\nend-segment drift",
                transform=ax.transAxes,
                fontsize=8.5,
                color="#444444",
            )
        else:
            peak_index = int(np.argmax(y_values))
            peak_x = float(x_values[peak_index])
            peak_y = float(y_values[peak_index])
            ax.scatter([peak_x], [peak_y], s=14, color="#D62728", zorder=3)
            ax.text(
                0.04,
                0.90,
                f"Peak ~ {peak_x:.1f}",
                transform=ax.transAxes,
                fontsize=8.5,
            )

    fig.tight_layout()
    fig.savefig(OUTPUT, dpi=400, bbox_inches="tight")
    plt.close(fig)
    print(f"Created {OUTPUT}")


if __name__ == "__main__":
    main()
