"""Plot MATLAB-computed MSD data using matplotlib's bmh style.

This script does not recalculate trajectory statistics.  It only visualizes
the CSV files produced by process_data.m.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


plt.style.use("bmh")
plt.rcParams.update({
    "font.size": 8,
    "axes.titlesize": 9,
    "axes.labelsize": 8,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 7,
})

summary = pd.read_csv("data_summary.csv", encoding="utf-8")
msd = pd.read_csv("msd_results.csv", encoding="utf-8")
# Report-facing comparison excludes Group 3 and Group 4 per current report requirements.
selected_samples = ["第一组", "第二组", "第三组-2", "第四组-2"]
summary = summary[summary["Sample"].isin(selected_samples)].copy()
summary["_order"] = summary["Sample"].map({s: i for i, s in enumerate(selected_samples)})
summary = summary.sort_values("_order").drop(columns="_order")
msd = msd[msd["Sample"].isin(selected_samples)].copy()

name_map = {
    "第一组": "Group 1",
    "第二组": "Group 2",
    "第三组": "Group 3",
    "第三组-2": "Group 3-2",
    "第四组": "Group 4",
    "第四组-2": "Group 4-2",
}

out_dir = Path("src") / "img"
out_dir.mkdir(parents=True, exist_ok=True)

fig, axes = plt.subplots(2, 2, figsize=(8, 6), sharex=True)
for ax, (_, row) in zip(axes.ravel(), summary.iterrows()):
    sample = row["Sample"]
    data = msd[msd["Sample"] == sample]
    t = data["t_s"]
    y = data["MSD_nm2"]
    fit_y = 4 * row["D_nm2_per_s_alpha"] * (t ** row["Alpha"])
    ax.scatter(t, y, s=8, label="MSD data")
    ax.plot(t, fit_y, linewidth=1.5, label="power-law fit")
    ax.set_title(f"{name_map.get(sample, sample)}: α={row['Alpha']:.3f}")
    ax.set_xlabel("t / s")
    ax.set_ylabel("MSD / nm$^2$")
    ax.legend()
fig.tight_layout()
fig.savefig(out_dir / "msd_bmh.png", dpi=300)
plt.close(fig)

fig, ax1 = plt.subplots(figsize=(8, 4.5))
x = range(len(summary))
labels = [name_map.get(s, s) for s in summary["Sample"]]
ax1.bar(x, summary["D_nm2_per_s_alpha"] / 1e4, width=0.65, alpha=0.8, label="$D$")
ax1.set_ylabel("$D$ / $10^4$ nm$^2$ s$^{-\\alpha}$")
ax1.set_xticks(list(x))
ax1.set_xticklabels(labels, rotation=25, ha="right")
ax2 = ax1.twinx()
ax2.plot(list(x), summary["Alpha"], marker="o", color="#d62728", label="$\\alpha$")
ax2.set_ylabel("$\\alpha$")
ax2.set_ylim(0, 1.05)
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper right")
fig.tight_layout()
fig.savefig(out_dir / "diffusion_alpha_bmh.png", dpi=300)
plt.close(fig)
