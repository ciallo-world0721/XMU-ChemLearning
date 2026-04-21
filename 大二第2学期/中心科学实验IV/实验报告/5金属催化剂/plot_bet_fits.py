from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


plt.style.use("bmh")


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"

BET_DATA = {
    "I 1# no NH3": {
        "x": np.array(
            [0.051771544, 0.131860419, 0.197926929, 0.273970484, 0.350313888]
        ),
        "V": np.array([74.9754, 92.5534, 103.0057, 114.1479, 125.7566]),
    },
    "II 1# NH3": {
        "x": np.array(
            [0.050852198, 0.131381217, 0.197568422, 0.273698277, 0.350033258]
        ),
        "V": np.array([77.7361, 95.8442, 106.6463, 118.1422, 130.2510]),
    },
    "III 2# no NH3": {
        "x": np.array(
            [0.052791631, 0.132126965, 0.197883929, 0.273981969, 0.350456410]
        ),
        "V": np.array([75.5250, 93.0670, 103.5897, 114.7023, 126.2069]),
    },
    "IV 2# NH3": {
        "x": np.array(
            [0.048008855, 0.119604056, 0.213753971, 0.274039241, 0.349864139]
        ),
        "V": np.array([77.4727, 94.6556, 110.4815, 119.7890, 131.9877]),
    },
}


def bet_transform(x_values: np.ndarray, volume: np.ndarray) -> np.ndarray:
    return x_values / (volume * (1.0 - x_values))


def main() -> None:
    fig, axes = plt.subplots(2, 2, figsize=(9.2, 7.0), sharex=True, sharey=True)
    x_fit = np.linspace(0.045, 0.355, 200)

    for ax, (label, values) in zip(axes.flat, BET_DATA.items()):
        x_values = values["x"]
        y_values = bet_transform(x_values, values["V"])
        k, b = np.polyfit(x_values, y_values, 1)
        R2 = 1 - np.sum((y_values - (k * x_values + b)) ** 2) / np.sum((y_values - np.mean(y_values)) ** 2)
        ax.scatter(x_values, y_values, s=18, color="#0072B2")
        ax.plot(x_fit, k * x_fit + b, color="#D55E00", lw=1.3)
        ax.set_title(label, fontsize=11)
        ax.set_xlabel(r"$P/P_0$")
        ax.set_ylabel(r"$P/[V(P_0-P)]$")
        ax.text(0.05, 0.95, rf"$R^2$ = {R2:.4f}", transform=ax.transAxes, fontsize=10)
        ax.grid(alpha=0.2)

    fig.tight_layout()
    fig.savefig(SRC / "BET拟合图.png", dpi=400, bbox_inches="tight")
    plt.close(fig)
    print(f"Created {SRC / 'BET拟合图.png'}")


if __name__ == "__main__":
    main()
