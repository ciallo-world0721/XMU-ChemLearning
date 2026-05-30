from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "src" / "实验11 20260513+20260520"
IMG_DIR = ROOT / "src" / "img"


@dataclass(frozen=True)
class Trace:
    label: str
    path: Path
    times: list[float]
    signals: list[float]


def ensure_inputs(paths: Iterable[Path]) -> None:
    for path in paths:
        if not path.exists():
            raise FileNotFoundError(f"Missing input file: {path}")


def read_trace(path: Path, label: str) -> Trace:
    text = path.read_text(encoding="utf-16")
    rows: list[tuple[float, float]] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            raise ValueError(f"Unexpected row in {path}: {raw_line!r}")
        rows.append((float(parts[0]), float(parts[1])))
    if not rows:
        raise ValueError(f"No numeric rows parsed from {path}")
    return Trace(
        label=label,
        path=path,
        times=[t for t, _ in rows],
        signals=[y for _, y in rows],
    )


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


def peak_point(trace: Trace) -> tuple[float, float]:
    index = max(range(len(trace.signals)), key=trace.signals.__getitem__)
    return trace.times[index], trace.signals[index]


def annotate_peak(ax: plt.Axes, trace: Trace, color: str, text_prefix: str = "主峰") -> None:
    x, y = peak_point(trace)
    ax.scatter([x], [y], color=color, s=18, zorder=5)
    ax.annotate(
        f"{text_prefix} {x:.2f} min",
        xy=(x, y),
        xytext=(x + 0.45, y * 0.82 if y > 0 else y + 20),
        fontsize=8,
        color=color,
        arrowprops={"arrowstyle": "->", "color": color, "lw": 0.8},
    )


def trim_window(trace: Trace, start: float = 0.0, end: float = 30.0) -> Trace:
    pairs = [(t, y) for t, y in zip(trace.times, trace.signals) if start <= t <= end]
    return Trace(
        label=trace.label,
        path=trace.path,
        times=[t for t, _ in pairs],
        signals=[y for _, y in pairs],
    )


def save_crude_figure(trace: Trace) -> Path:
    out = IMG_DIR / "hplc_crude_6_2.png"
    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    ax.plot(trace.times, trace.signals, label="6-2 粗肽", color="#C06C84", lw=1.2)
    annotate_peak(ax, trace, "#C06C84", "主峰")
    ax.set_xlim(0, 30)
    ax.set_xlabel("保留时间 (min)")
    ax.set_ylabel("信号 (mAU, 214 nm)")
    ax.set_title("H3 N端酰肼六肽（6-2）粗肽 HPLC 图谱")
    ax.legend(frameon=True)
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    return out


def save_pure_figure(trace: Trace) -> Path:
    out = IMG_DIR / "hplc_pure_reference.png"
    fig, ax = plt.subplots(figsize=(7.5, 3.4))
    ax.plot(trace.times, trace.signals, color="#2A9D8F", lw=1.2)
    annotate_peak(ax, trace, "#2A9D8F")
    ax.set_xlim(0, 30)
    ax.set_xlabel("保留时间 (min)")
    ax.set_ylabel("信号 (mAU, 214 nm)")
    ax.set_title("H3 N端酰肼六肽纯肽标准 HPLC 图谱")
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    return out


def save_overlay_figure(crude: Trace, pure: Trace) -> Path:
    out = IMG_DIR / "hplc_overlay_crude_vs_pure.png"
    fig, ax = plt.subplots(figsize=(7.5, 3.8))
    ax.plot(crude.times, crude.signals, label="6-2 粗肽", color="#4C72B0", lw=1.15)
    ax.plot(pure.times, pure.signals, label="纯肽标准", color="#55A868", lw=1.15)
    annotate_peak(ax, crude, "#4C72B0", "粗肽")
    annotate_peak(ax, pure, "#55A868", "纯肽")
    ax.set_xlim(0, 30)
    ax.set_xlabel("保留时间 (min)")
    ax.set_ylabel("信号 (mAU, 214 nm)")
    ax.set_title("粗肽与纯肽 HPLC 叠加对比图谱")
    ax.legend(frameon=True)
    fig.tight_layout()
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    return out


def main() -> None:
    pure_path = DATA_DIR / "20260422-ARTKQT-纯肽.CSV"
    crude_62_path = DATA_DIR / "20250520" / "20260520-ARTKQT-2.CSV"

    ensure_inputs([pure_path, crude_62_path, IMG_DIR])
    setup_style()

    pure = trim_window(read_trace(pure_path, "纯肽标准"))
    crude_62 = trim_window(read_trace(crude_62_path, "6-2 粗肽"))

    outputs = [
        save_crude_figure(crude_62),
        save_pure_figure(pure),
        save_overlay_figure(crude_62, pure),
    ]
    for output in outputs:
        print(output)


if __name__ == "__main__":
    main()
