#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
stage2b_apc_composition.py — Stage 2b Tasks A & B

================================ PROTO-RAG-001 ================================
Purpose
    Demographic-measurement leg of question (A): build the pseudo-cohort
    composition panel (Task A) and run the curvature-focused Age-Period-Cohort
    decomposition (Task B) that asks whether the 2018-2024 marriage-share
    acceleration localizes in PERIODS (all live cohorts bend together) or in
    COHORTS (successive entry cohorts step down). This script does NOT apply the
    §5 decision rule and does NOT touch the ABM — it emits a read for the memo.

Inputs
    ../data/coupling/CRI_coupling_annual.csv   (ENAHO 2010-2024, REDATAM aggregates)
    ../data/coupling/COL_coupling_annual.csv   (GEIH 2007-2024, DANE microdata-derived)
    ../data/coupling/MEX_coupling_annual.csv   (ENOE, comparator only)
    Columns used: year, age_band, married, cohabiting, n_women_weighted.

Outputs (outputs/stage2b/)
    composition_panel_{CC}.csv   Task A tidy panel: country, birth_cohort,
                                 age_band, year, share_single/cohab/married.
    apc_period_effects_{CC}.csv  Task B period effects + identified 2nd differences.
    apc_cohort_effects_{CC}.csv  Task B cohort effects + identified 2nd differences.
    apc_localization_{CC}.csv    Curvature-localization summary (period vs cohort).

Assumptions
    - Band/base inherited from Stage 1.5: women, 5-year bands 20-24..35-39,
      co-residential union composition simplex {single, cohabiting, married};
      single = 1 - cohabiting - married.  Bands are NOT re-derived here.
    - Pseudo-cohort label = year - band_midpoint, binned to 5-year groups; this
      tracks a birth cohort across bands as it ages (Task A construction choice).
    - APC linear trend is UNIDENTIFIED (cohort = period - age). Only curvature
      (second differences) is reported; sum-to-zero coding fixes a normalization
      whose linear split is arbitrary and is deliberately not interpreted.
    - WLS weight = n_women_weighted (band sampling mass).

Dependencies
    python>=3.12, pandas, numpy, statsmodels. CPU-only (Anne compute envelope).

Identification wall (Stage 1.5 gate of record)
    Period TFR is NEVER loaded or used here — not as regressor, weight, or tuner.
    Enforced by assert_no_tfr() and by never reading data/national/. `w` (the
    cohabiting-to-married fertility-intensity ratio) is not an object of 2b.
==============================================================================
"""
from __future__ import annotations

import os
import re
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #
HERE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.normpath(os.path.join(HERE, "..", "data", "coupling"))
OUT_DIR = os.path.join(HERE, "outputs", "stage2b")

# Identification countries (primary) + MEX comparator (§3).
SOURCES = {
    "CRI": "CRI_coupling_annual.csv",
    "COL": "COL_coupling_annual.csv",
    "MEX": "MEX_coupling_annual.csv",  # comparator only; biennial/coarse
}
PRIMARY = ("CRI", "COL")

# Stage 1.5 bands — do NOT re-derive (§1 band/base consistency).
BAND_MIDPOINT = {"20-24": 22, "25-29": 27, "30-34": 32, "35-39": 37}
COHORT_BIN = 5  # 5-year birth-cohort groups
ACCEL_WINDOW = (2018, 2024)  # §4 acceleration window of interest


# --------------------------------------------------------------------------- #
# Identification-wall guard
# --------------------------------------------------------------------------- #
def assert_no_tfr(df: pd.DataFrame, where: str) -> None:
    """Hard stop if any fertility/TFR column leaks into an estimation frame.

    Word-aware: catches tfr/asfr/fertility/births columns but NOT demographic
    cohort labels like `birth_cohort` (a legitimate Task A construct).
    """
    def is_fertility(c: str) -> bool:
        lc = c.lower()
        if "cohort" in lc:                       # birth_cohort, cohort_start — fine
            return False
        return bool(re.search(r"tfr|asfr|fertil|\bbirths?\b", lc))

    banned = [c for c in df.columns if is_fertility(c)]
    if banned:
        raise RuntimeError(
            f"Identification wall violated in {where}: TFR/fertility columns "
            f"{banned} must never enter Stage 2b estimation (Stage 1.5 gate)."
        )


# --------------------------------------------------------------------------- #
# Task A — pseudo-cohort construction
# --------------------------------------------------------------------------- #
def load_composition(country: str) -> pd.DataFrame:
    """Load one country's coupling series and derive the composition simplex."""
    path = os.path.join(DATA_DIR, SOURCES[country])
    df = pd.read_csv(path)
    df = df[df["age_band"].isin(BAND_MIDPOINT)].copy()
    df["share_married"] = df["married"].astype(float)
    df["share_cohab"] = df["cohabiting"].astype(float)
    df["share_single"] = 1.0 - df["share_cohab"] - df["share_married"]
    df["country"] = country
    keep = ["country", "year", "age_band", "share_single", "share_cohab",
            "share_married", "n_women_weighted"]
    out = df[keep].sort_values(["year", "age_band"]).reset_index(drop=True)
    assert_no_tfr(out, f"load_composition[{country}]")
    return out


def build_pseudo_cohorts(comp: pd.DataFrame) -> pd.DataFrame:
    """Task A: assign each (year, band) cell to a 5-year synthetic birth cohort.

    central_cohort = year - band_midpoint tracks a cohort across bands; binning
    to 5-year groups yields the pseudo-cohort that the eye-test plot follows.
    """
    comp = comp.copy()
    mid = comp["age_band"].map(BAND_MIDPOINT)
    comp["central_cohort"] = comp["year"] - mid
    lo = (np.floor(comp["central_cohort"] / COHORT_BIN) * COHORT_BIN).astype(int)
    comp["birth_cohort"] = [f"{a}-{a + COHORT_BIN - 1}" for a in lo]
    comp["cohort_start"] = lo
    return comp


# --------------------------------------------------------------------------- #
# Task B — curvature-focused APC
# --------------------------------------------------------------------------- #
def _second_differences(effects: pd.Series) -> pd.Series:
    """Δ²e_k = e_{k+1} - 2 e_k + e_{k-1}; identified (trend-invariant)."""
    e = effects.sort_index()
    return e.shift(-1) - 2.0 * e + e.shift(1)


def apc_decompose(panel: pd.DataFrame, share_col: str = "share_married"):
    """Fit sum-to-zero WLS APC and return identified second differences.

    Linear component is unidentified (cohort = period - age) and is NOT
    interpreted; only the curvature (second differences) is reported, with the
    normalization stated in the output. age has 4 levels, so its curvature has
    limited resolution — period/cohort curvature carries the localization read.
    """
    d = panel.dropna(subset=[share_col, "n_women_weighted"]).copy()
    d["age"] = d["age_band"].astype("category")
    d["period"] = d["year"].astype("category")
    d["cohort"] = d["cohort_start"].astype("category")
    assert_no_tfr(d, "apc_decompose")

    formula = (f"{share_col} ~ C(age, Sum) + C(period, Sum) + C(cohort, Sum)")
    model = smf.wls(formula, data=d, weights=d["n_women_weighted"]).fit()

    def _marginals(dim_values, prefix):
        # Reconstruct sum-to-zero effects: dropped level = -sum(others).
        levels = sorted(dim_values.unique())
        eff = {}
        for lv in levels:
            key = [p for p in model.params.index
                   if p.startswith(prefix) and f"[S.{lv}]" in p]
            eff[lv] = model.params[key[0]] if key else np.nan
        s = pd.Series(eff)
        s = s.fillna(-s.sum(skipna=True))  # recover the reference level
        return s

    period_eff = _marginals(d["year"], "C(period, Sum)")
    cohort_eff = _marginals(d["cohort_start"], "C(cohort, Sum)")

    period_tab = pd.DataFrame({"period": period_eff.index,
                               "effect": period_eff.values})
    period_tab["second_diff"] = _second_differences(period_eff).values
    cohort_tab = pd.DataFrame({"cohort_start": cohort_eff.index,
                               "effect": cohort_eff.values})
    cohort_tab["second_diff"] = _second_differences(cohort_eff).values
    return model, period_tab, cohort_tab


def localization_summary(period_tab, cohort_tab, country, share_col):
    """Compare curvature concentrated in the 2018-2024 periods vs entry cohorts.

    NOTE: this is a descriptive read, NOT the §5 decision rule. The rule is
    applied in the memo (Task D) after the Task C state-dependence result.
    """
    lo, hi = ACCEL_WINDOW
    pmask = period_tab["period"].between(lo, hi)
    period_curv = np.sqrt(np.nanmean(period_tab.loc[pmask, "second_diff"] ** 2))
    # Entry cohorts = the youngest third of cohort groups (most recent entrants).
    cuts = cohort_tab["cohort_start"].quantile(2 / 3)
    cmask = cohort_tab["cohort_start"] >= cuts
    cohort_curv = np.sqrt(np.nanmean(cohort_tab.loc[cmask, "second_diff"] ** 2))
    total = period_curv + cohort_curv
    return pd.DataFrame([{
        "country": country,
        "share": share_col,
        "period_curvature_rms_2018_2024": period_curv,
        "cohort_curvature_rms_entry": cohort_curv,
        "period_share_of_curvature": period_curv / total if total else np.nan,
        "leaning": ("period" if period_curv > cohort_curv else "cohort"),
        "normalization": "sum-to-zero (Deviation) coding; linear trend NOT identified/reported",
    }])


# --------------------------------------------------------------------------- #
# Driver
# --------------------------------------------------------------------------- #
def run_country(country: str) -> pd.DataFrame:
    comp = load_composition(country)
    panel = build_pseudo_cohorts(comp)

    tidy = panel[["country", "birth_cohort", "cohort_start", "age_band", "year",
                  "share_single", "share_cohab", "share_married",
                  "n_women_weighted"]]
    tidy.to_csv(os.path.join(OUT_DIR, f"composition_panel_{country}.csv"),
                index=False)

    loc_rows = []
    for share_col in ("share_married", "share_cohab"):
        _, period_tab, cohort_tab = apc_decompose(panel, share_col)
        tag = share_col.replace("share_", "")
        period_tab.to_csv(
            os.path.join(OUT_DIR, f"apc_period_effects_{country}_{tag}.csv"),
            index=False)
        cohort_tab.to_csv(
            os.path.join(OUT_DIR, f"apc_cohort_effects_{country}_{tag}.csv"),
            index=False)
        loc_rows.append(localization_summary(period_tab, cohort_tab,
                                             country, share_col))
    loc = pd.concat(loc_rows, ignore_index=True)
    loc.to_csv(os.path.join(OUT_DIR, f"apc_localization_{country}.csv"),
               index=False)
    return loc


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    summaries = []
    for country in SOURCES:
        if country not in PRIMARY:
            print(f"[2b] {country}: comparator — pseudo-panel only "
                  f"(coarse/biennial; APC localization read not relied upon).")
        try:
            summaries.append(run_country(country))
            print(f"[2b] {country}: panel + APC written to {OUT_DIR}")
        except FileNotFoundError as e:
            print(f"[2b] {country}: SKIP (missing input) — {e}")
    if summaries:
        allsum = pd.concat(summaries, ignore_index=True)
        allsum.to_csv(os.path.join(OUT_DIR, "apc_localization_ALL.csv"),
                      index=False)
        print("\n[2b] Curvature-localization read (descriptive, NOT the §5 rule):")
        print(allsum.to_string(index=False))


if __name__ == "__main__":
    main()
