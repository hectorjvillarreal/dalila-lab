#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
stage2b_figures.py — Stage 2b figure-data emitter

================================ PROTO-RAG-001 ================================
Purpose
    Emit figure data (and optional PNGs) for the Stage 2b read:
      1. Pseudo-panel cohort lines over calendar time (the §4 Task B eye-test).
      2. APC curvature (identified second differences, period vs cohort).
      3. State-dependence β with CI by reference-group spec (Task C).
    A period-TFR overlay is produced ONLY on figure 1, and ONLY for visual
    comparison — see identification-wall note below.

Inputs
    outputs/stage2b/composition_panel_{CC}.csv     (Task A)
    outputs/stage2b/apc_*_effects_{CC}_*.csv        (Task B)
    outputs/stage2b/statedep_estimates_{CC}.csv     (Task C)
    [comparison-only] ../data/national/{CC}_tfr_*.csv  (overlay on fig 1)

Outputs (outputs/stage2b/figdata/  and  outputs/stage2b/figures/)
    fig1_cohortlines_{CC}.csv / .png
    fig2_apc_curvature_{CC}.csv / .png
    fig3_beta_ci_{CC}.csv / .png

Assumptions
    - Reads only artifacts produced by the two estimation scripts; performs no
      estimation of its own.
    - PNG rendering uses the Agg backend (headless Dalila). If matplotlib is
      unavailable, figure-data CSVs are still written and PNGs are skipped.

Dependencies
    python>=3.12, pandas, numpy; matplotlib optional (for PNGs).

Identification wall
    This is the ONLY Stage 2b script allowed to read a TFR series, and strictly
    for the fig-1 comparison overlay. TFR is loaded in load_tfr_overlay() alone,
    never merged into any estimation frame, never used to weight or tune. The
    estimation scripts (apc, state_dependence) never import this module.
==============================================================================
"""
from __future__ import annotations

import os
import glob
import numpy as np
import pandas as pd

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    HAVE_MPL = True
except Exception:  # pragma: no cover - figure-data still emitted
    HAVE_MPL = False

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "outputs", "stage2b")
FIGDATA = os.path.join(OUT_DIR, "figdata")
FIGS = os.path.join(OUT_DIR, "figures")
NATIONAL = os.path.normpath(os.path.join(HERE, "..", "data", "national"))
PRIMARY = ("CRI", "COL")


# --------------------------------------------------------------------------- #
# Figure 1 — pseudo-panel cohort lines (+ TFR overlay, comparison only)
# --------------------------------------------------------------------------- #
def load_tfr_overlay(country: str) -> pd.DataFrame | None:
    """COMPARISON-ONLY TFR series for the fig-1 overlay. Never returns to an
    estimation path. Picks the national TFR file if present."""
    for pat in (f"{country}_tfr_national.csv", f"{country}_tfr_implied.csv"):
        f = os.path.join(NATIONAL, pat)
        if os.path.exists(f):
            t = pd.read_csv(f)
            ycol = next((c for c in t.columns if c.lower() in ("year", "anio")), None)
            # national TFR files use a `year,value` schema; also accept a *tfr* col.
            vcol = next((c for c in t.columns if "tfr" in c.lower()), None) \
                or next((c for c in t.columns if c.lower() in ("value", "tfr_value")), None)
            if ycol and vcol:
                return t[[ycol, vcol]].rename(columns={ycol: "year", vcol: "tfr"})
    return None


def fig1_cohort_lines(country: str) -> None:
    panel = pd.read_csv(os.path.join(OUT_DIR, f"composition_panel_{country}.csv"))
    fig_df = panel.sort_values(["birth_cohort", "year"])
    fig_df.to_csv(os.path.join(FIGDATA, f"fig1_cohortlines_{country}.csv"),
                  index=False)
    if not HAVE_MPL:
        return
    fig, ax = plt.subplots(figsize=(8, 5))
    # Anne A2: within-band-SEGMENTED redraw. Draw each cohort's series broken at
    # band transitions so the cross-band 2012/2017/2022 sawtooth connector is not
    # rendered as if it were a within-cohort trend. One colour per cohort; the
    # legend entry is added once, the older-band segments share it (label=None).
    colours = {c: f"C{i}" for i, c in enumerate(sorted(fig_df["birth_cohort"].unique()))}
    for cohort, g in fig_df.groupby("birth_cohort"):
        first = True
        for _, seg in g.sort_values("year").groupby("age_band"):
            ax.plot(seg["year"], seg["share_married"], marker="o", ms=3,
                    color=colours[cohort], label=cohort if first else None)
            first = False
    ax.set_xlabel("calendar year")
    ax.set_ylabel("married share (within band)")
    ax.set_title(f"{country}: pseudo-cohort marriage-share lines "
                 f"(within-band segments; no cross-band connector)")
    tfr = load_tfr_overlay(country)
    if tfr is not None:
        ax2 = ax.twinx()
        ax2.plot(tfr["year"], tfr["tfr"], color="black", ls="--", lw=1.2,
                 label="period TFR (comparison only)")
        ax2.set_ylabel("period TFR (comparison only — not a regressor)")
    ax.legend(fontsize=6, ncol=2, title="birth cohort")
    fig.tight_layout()
    fig.savefig(os.path.join(FIGS, f"fig1_cohortlines_{country}.png"), dpi=140)
    plt.close(fig)


# --------------------------------------------------------------------------- #
# Figure 2 — APC curvature (period vs cohort second differences)
# --------------------------------------------------------------------------- #
def fig2_apc_curvature(country: str) -> None:
    rows = []
    for f in glob.glob(os.path.join(OUT_DIR, f"apc_period_effects_{country}_*.csv")):
        tag = os.path.basename(f).split("_")[-1].replace(".csv", "")
        d = pd.read_csv(f)
        d["dim"], d["share"], d["index"] = "period", tag, d["period"]
        rows.append(d[["dim", "share", "index", "second_diff"]])
    for f in glob.glob(os.path.join(OUT_DIR, f"apc_cohort_effects_{country}_*.csv")):
        tag = os.path.basename(f).split("_")[-1].replace(".csv", "")
        d = pd.read_csv(f)
        d["dim"], d["share"], d["index"] = "cohort", tag, d["cohort_start"]
        rows.append(d[["dim", "share", "index", "second_diff"]])
    if not rows:
        print(f"[2b-fig] {country}: no APC outputs — run apc script first.")
        return
    curv = pd.concat(rows, ignore_index=True)
    curv.to_csv(os.path.join(FIGDATA, f"fig2_apc_curvature_{country}.csv"),
                index=False)
    if not HAVE_MPL:
        return
    sub = curv[curv["share"] == "married"]
    fig, ax = plt.subplots(figsize=(8, 4))
    for dim, g in sub.groupby("dim"):
        ax.plot(g["index"], g["second_diff"], marker="s", ms=4, label=dim)
    ax.axhline(0, color="grey", lw=0.7)
    ax.set_title(f"{country}: identified APC curvature (2nd diff, married share)")
    ax.set_xlabel("period / cohort index")
    ax.set_ylabel("second difference of effect")
    ax.legend()
    fig.tight_layout()
    fig.savefig(os.path.join(FIGS, f"fig2_apc_curvature_{country}.png"), dpi=140)
    plt.close(fig)


# --------------------------------------------------------------------------- #
# Figure 3 — β with CI by reference-group spec
# --------------------------------------------------------------------------- #
def fig3_beta_ci(country: str) -> None:
    f = os.path.join(OUT_DIR, f"statedep_estimates_{country}.csv")
    if not os.path.exists(f):
        print(f"[2b-fig] {country}: no state-dep estimates — run Task C first.")
        return
    est = pd.read_csv(f)
    est.to_csv(os.path.join(FIGDATA, f"fig3_beta_ci_{country}.csv"), index=False)
    if not HAVE_MPL:
        return
    est = est.dropna(subset=["beta"]).reset_index(drop=True)
    est["label"] = est["reference_spec"] + " (lag" + est["lag"].astype(str) + ")"
    fig, ax = plt.subplots(figsize=(7, 4))
    y = np.arange(len(est))
    ax.errorbar(est["beta"], y,
                xerr=[est["beta"] - est["ci_lo"], est["ci_hi"] - est["beta"]],
                fmt="o", capsize=3)
    ax.axvline(0, color="red", lw=0.8, ls="--")
    ax.set_yticks(y)
    ax.set_yticklabels(est["label"], fontsize=7)
    ax.set_xlabel("β (amplifying if < 0 and significant)")
    ax.set_title(f"{country}: state-dependence β by reference-group spec")
    fig.tight_layout()
    fig.savefig(os.path.join(FIGS, f"fig3_beta_ci_{country}.png"), dpi=140)
    plt.close(fig)


def main():
    os.makedirs(FIGDATA, exist_ok=True)
    os.makedirs(FIGS, exist_ok=True)
    if not HAVE_MPL:
        print("[2b-fig] matplotlib unavailable — emitting figure-data CSVs only.")
    for country in PRIMARY:
        panel = os.path.join(OUT_DIR, f"composition_panel_{country}.csv")
        if not os.path.exists(panel):
            print(f"[2b-fig] {country}: SKIP — run estimation scripts first.")
            continue
        fig1_cohort_lines(country)
        fig2_apc_curvature(country)
        fig3_beta_ci(country)
        print(f"[2b-fig] {country}: figure data + PNGs -> {FIGDATA}, {FIGS}")


if __name__ == "__main__":
    main()
