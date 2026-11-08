#!/usr/bin/env python3
"""Nine-panel figure: Bayesian bootstrap posterior of each survey target, the normal
approximation implied by the draft's standard error, and the model moment at the estimates.

    python -I src/make_figure.py
"""
import json
import os

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "outputs")
SURFACE, INK, INK2, BLUE, ORANGE = "#fcfcfb", "#0b0b0b", "#52514e", "#2a78d6", "#eb6834"
TITLES = {"elas_pooled": "Income elasticity of m, pooled", "elas_within": "Income elasticity of m, within age",
          "share_25_34": "Spending share, head 25–34", "share_50_64": "Spending share, head 50–64",
          "share_65_79": "Spending share, head 65–79", "logslope": "Log-slope of mean m, 25–79",
          "skill_prem": "Skill premium, ages 25–34", "surv5_low": "Five-year survival, low educ. 50–64*",
          "surv5_high": "Five-year survival, high educ. 50–64*"}


def main():
    e = json.load(open(os.path.join(OUT, "enigh_moments_bb.json")))
    s = json.load(open(os.path.join(OUT, "enasem_survival_bb.json")))
    de = pd.read_csv(os.path.join(OUT, "enigh_moments_bb_draws.csv"))
    ds = pd.read_csv(os.path.join(OUT, "enasem_survival_bb_draws.csv"))
    panels = [(k, e["moments"][k], de[k].values) for k in de.columns] + [(k, s["moments"][k], ds[k].values) for k in ds.columns]
    fig, axes = plt.subplots(3, 3, figsize=(11, 8.6), facecolor=SURFACE)
    for ax, (k, r, x) in zip(axes.flat, panels):
        ax.set_facecolor(SURFACE)
        ax.hist(x, bins=35, density=True, color=BLUE, alpha=0.85, edgecolor=SURFACE, linewidth=0.5)
        se, pt = r["normal"]["se"], r["point"]
        g = np.linspace(min(x.min(), pt - 4 * se), max(x.max(), pt + 4 * se), 300)
        ax.plot(g, np.exp(-0.5 * ((g - pt) / se) ** 2) / (se * np.sqrt(2 * np.pi)), color=INK2, linestyle="--", linewidth=1.5)
        ax.axvline(pt, color=INK, linewidth=1.2)
        ax.axvline(r["draft_model"], color=ORANGE, linewidth=1.8)
        lo, hi = r["ci95"]
        ax.annotate("", xy=(lo, 0), xytext=(hi, 0), xycoords=("data", "axes fraction"),
                    arrowprops=dict(arrowstyle="|-|", color=INK, lw=1.2, shrinkA=0, shrinkB=0, mutation_scale=3))
        ax.set_title(TITLES[k], fontsize=9.5, color=INK, loc="left")
        ax.set_yticks([])
        for sp in ("top", "right", "left"):
            ax.spines[sp].set_visible(False)
        ax.spines["bottom"].set_color(INK2)
        ax.tick_params(colors=INK2, labelsize=8)
        ax.text(0.98, 0.95, f"p-p {r['normal']['pp_distance']:.2f}\nSD/SE {r['normal']['sd_ratio_bb_over_normal']:.1f}",
                transform=ax.transAxes, ha="right", va="top", fontsize=8, color=INK2)
    handles = [Patch(color=BLUE, label="Bayesian bootstrap posterior, PSU-clustered"),
               Line2D([], [], color=INK2, linestyle="--", label="Normal with the draft's standard error"),
               Line2D([], [], color=INK, label="Point estimate and 95% credible interval"),
               Line2D([], [], color=ORANGE, linewidth=1.8, label="Model moment at the estimates (tab:moment_match_md)")]
    fig.legend(handles=handles, loc="lower center", ncol=2, frameon=False, fontsize=8.5, labelcolor=INK)
    fig.suptitle("BID2 Draft-November targets: Bayesian bootstrap of the survey moments\n"
                 f"ENIGH 2016+2018, {e['replicates']:,} replicates; ENASEM 2018→2021, {s['replicates']:,} replicates",
                 fontsize=10.5, color=INK, x=0.01, ha="left")
    fig.text(0.01, 0.055, "* ENASEM panels use the 2018→2021 wave pair, not the draft's 2012–2021 panel; levels are not comparable, widths are.",
             fontsize=8, color=INK2)
    fig.tight_layout(rect=(0, 0.1, 1, 0.93))
    os.makedirs(os.path.join(ROOT, "figures"), exist_ok=True)
    fig.savefig(os.path.join(ROOT, "figures", "bb_targets.png"), dpi=160, facecolor=SURFACE)
    fig.savefig(os.path.join(ROOT, "figures", "bb_targets.pdf"), facecolor=SURFACE)
    print("wrote figures/bb_targets.png and .pdf")


if __name__ == "__main__":
    main()
