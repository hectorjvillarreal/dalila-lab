#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
_render_figures_3a.py — Stage 3a PNG renderer

================================ PROTO-RAG-001 ================================
Purpose
    Render the Stage 3a figures from the figdata CSVs written by
    make_figures_3a.jl. Performs no estimation, no simulation; reads figdata
    (and nothing else).
      fig1_{CC}.png   per-band sim-vs-obs composition trajectories (2 x 4)
      fig2_{CC}.png   calibrated kappa(b) vs Stage 2b APC married cohort effects
      fig3_period.png exogenous period multiplier pi(t), both countries
      fig4_{CC}.png   TFR overlay [COMPARISON ONLY — placeholder ASFR level]

Inputs   outputs/stage3a/figdata/*.csv
Outputs  outputs/stage3a/figures/*.png

Color
    Okabe-Ito palette (CVD-safe by construction; Okabe & Ito 2008): observed
    near-black #1A1A1A, simulated blue #0072B2, secondary vermillion #D55E00.
    <=3 series per panel; identity also carried by marker/linestyle, never
    color alone. (Palette validator unavailable on Dalila — no node runtime;
    Okabe-Ito used as the documented validated fallback.)

Identification wall
    fig4 is the only figure touching a TFR series — comparison overlay only.

Dependencies  python>=3.12, pandas, numpy, matplotlib (Agg, headless).
Build instruction: STAGE3a_sufficiency_instruction.md (Debb, 2026-07-11).
Author: Claude Code (Stage 3a sufficiency), DFD Core Team — 2026-07-11
==============================================================================
"""
from __future__ import annotations

import os

import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

HERE = os.path.dirname(os.path.abspath(__file__))
S3A = os.path.join(HERE, "outputs", "stage3a")
FIGDATA = os.path.join(S3A, "figdata")
FIGS = os.path.join(S3A, "figures")
os.makedirs(FIGS, exist_ok=True)

CODES = ("CRI", "COL")
BANDS = ("20-24", "25-29", "30-34", "35-39")

OBS = "#1A1A1A"      # observed — near-black ink
SIM = "#0072B2"      # simulated — Okabe-Ito blue
ACC = "#D55E00"      # secondary — Okabe-Ito vermillion

def _save(fig, stem: str) -> None:
    """PNG for quick viewing + vector PDF for the paper (Overleaf)."""
    fig.savefig(os.path.join(FIGS, stem + ".png"))
    fig.savefig(os.path.join(FIGS, stem + ".pdf"))


plt.rcParams.update({
    "figure.dpi": 150, "savefig.dpi": 300, "font.size": 9,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "axes.grid.axis": "y", "grid.color": "#DDDDDD",
    "grid.linewidth": 0.6, "axes.axisbelow": True,
})


def _style_obs_sim(ax):
    ax.margins(x=0.02)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=5))


# ---------------------------------------------------------------- fig 1 ----
def fig1(cc: str) -> None:
    df = pd.read_csv(os.path.join(FIGDATA, f"fig1_bands_{cc}.csv"))
    fig, axes = plt.subplots(2, 4, figsize=(11, 5), sharex=True, sharey="row")
    for j, band in enumerate(BANDS):
        d = df[df.age_band == band]
        for i, (sim_c, sd_c, obs_c, label) in enumerate((
            ("married_sim", "married_sim_sd", "married_obs", "married"),
            ("cohab_sim", "cohab_sim_sd", "cohab_obs", "cohabiting"),
        )):
            ax = axes[i, j]
            ax.fill_between(d.year, d[sim_c] - d[sd_c], d[sim_c] + d[sd_c],
                            color=SIM, alpha=0.18, linewidth=0)
            ax.plot(d.year, d[sim_c], color=SIM, lw=2, label="simulated (mean ±1 sd)")
            o = d.dropna(subset=[obs_c])
            ax.plot(o.year, o[obs_c], color=OBS, lw=1.2, marker="o", ms=3,
                    linestyle="--", label="observed")
            _style_obs_sim(ax)
            if i == 0:
                ax.set_title(band)
            if j == 0:
                ax.set_ylabel(f"{label} share")
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=2, frameon=False)
    fig.suptitle(f"{cc} — union composition by age band, women 20–39: "
                 "no-reflexivity model vs observed", y=0.98)
    fig.tight_layout(rect=(0, 0.05, 1, 0.96))
    _save(fig, f"fig1_{cc}")
    plt.close(fig)


# ---------------------------------------------------------------- fig 2 ----
def fig2(cc: str) -> None:
    prof = pd.read_csv(os.path.join(FIGDATA, f"fig2_cohort_profile_{cc}.csv"))
    apc = pd.read_csv(os.path.join(FIGDATA, f"fig2_cohort_{cc}.csv"))
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 5.5), sharex=True)

    ax1.plot(prof.birth_year, prof.kappa, color=SIM, lw=2, label="κ(b) marriage-entry multiplier")
    ax1.plot(prof.birth_year, prof.phi, color=SIM, lw=1.2, ls=":", label="φ(b) formation tilt")
    ax1.set_ylabel("calibrated multiplier")
    ax1.legend(frameon=False, loc="lower left")
    ax1.set_title(f"{cc} — calibrated cohort gradient vs Stage 2b APC cohort effects (married)")

    ax2.bar(apc.cohort_start + 2, apc.effect, width=3.6, color=ACC, alpha=0.85,
            label="2b APC cohort effect (married, 5-yr bins)")
    ax2.axhline(0, color="#999999", lw=0.8)
    ax2.set_ylabel("APC effect (share dev.)")
    ax2.set_xlabel("birth cohort")
    ax2.legend(frameon=False, loc="lower left")
    fig.text(0.01, 0.005,
             "Note: κ(b) is a hazard multiplier, APC effects are share-level deviations — "
             "the comparison is qualitative (shape/timing), not level.",
             fontsize=7, color="#555555")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    _save(fig, f"fig2_{cc}")
    plt.close(fig)


# ---------------------------------------------------------------- fig 3 ----
def fig3() -> None:
    df = pd.read_csv(os.path.join(FIGDATA, "fig3_period.csv"))
    fig, ax = plt.subplots(figsize=(6.5, 3.6))
    for cc, color in (("CRI", SIM), ("COL", ACC)):
        d = df[df.country == cc]
        ax.plot(d.year, d.pi, color=color, lw=2)
        ax.annotate(cc, (d.year.iloc[-1], d.pi.iloc[-1]),
                    xytext=(4, 0), textcoords="offset points",
                    color=color, fontweight="bold", va="center")
    ax.set_ylabel("π(t) marriage-entry multiplier")
    ax.set_xlabel("calendar year")
    ax.set_title("Exogenous period shock π(t), full-model ROBUSTNESS spec\n"
                 "(calendar-time only — no state dependence; headline spec is cohort-only, π ≡ 1)",
                 fontsize=9)
    fig.tight_layout()
    _save(fig, "fig3_period")
    plt.close(fig)


# ---------------------------------------------------------------- fig 4 ----
def fig4(cc: str) -> None:
    df = pd.read_csv(os.path.join(FIGDATA, f"fig4_tfr_{cc}.csv"))
    fig, ax = plt.subplots(figsize=(6.5, 3.8))
    sim = df.dropna(subset=["tfr_overlay_mean"])
    ax.fill_between(sim.year, sim.tfr_overlay_mean - sim.tfr_overlay_sd,
                    sim.tfr_overlay_mean + sim.tfr_overlay_sd,
                    color=SIM, alpha=0.18, linewidth=0)
    ax.plot(sim.year, sim.tfr_overlay_mean, color=SIM, lw=2,
            label="model overlay (placeholder ASFR)")
    o = df.dropna(subset=["tfr_observed"])
    ax.plot(o.year, o.tfr_observed, color=OBS, lw=0, marker="o", ms=4,
            label="observed TFR")
    ax.set_ylabel("period TFR")
    ax.set_xlabel("year")
    ax.legend(frameon=False)
    ax.set_title(f"{cc} — TFR overlay [COMPARISON ONLY]")
    fig.text(0.01, 0.005,
             "Identification wall: TFR never enters the loss; overlay level rides the "
             "placeholder MEX-shape ASFR — Stage 3a makes NO TFR claim (3b is ENDS-gated).",
             fontsize=7, color="#555555")
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    _save(fig, f"fig4_{cc}")
    plt.close(fig)


if __name__ == "__main__":
    for cc in CODES:
        fig1(cc)
        fig2(cc)
        fig4(cc)
    fig3()
    print("figures written to:", FIGS)
