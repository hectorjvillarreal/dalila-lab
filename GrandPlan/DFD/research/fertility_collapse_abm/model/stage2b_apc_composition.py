#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
stage2b_apc_composition.py — Stage 2b Tasks A & B

================================ PROTO-RAG-001 ================================
Purpose
    Demographic-measurement leg of question (A): build the pseudo-cohort
    composition panel (Task A) and run the curvature-focused Age-Period-Cohort
    decomposition (Task B) that asks whether the marriage-share acceleration
    localizes in PERIODS (all live bands bend together at the same calendar time)
    or in COHORTS (successive entry cohorts step down). Does NOT apply the §5
    decision rule and does NOT touch the ABM.

Inputs
    ../data/coupling/CRI_coupling_annual.csv   (ENAHO 2010-2024, REDATAM aggregates)
    ../data/coupling/COL_coupling_annual.csv   (GEIH 2007-2024, DANE microdata-derived)
    ../data/coupling/MEX_coupling_annual.csv   (ENOE, comparator only)
    Columns used: year, age_band, married, cohabiting, n_women_weighted.

Outputs (outputs/stage2b/)
    composition_panel_{CC}.csv     Task A tidy panel (birth-year-bin cohorts).
    apc_period_effects_{CC}_*.csv  Task B period effects + identified 2nd diffs.
    apc_cohort_effects_{CC}_*.csv  Task B cohort effects + identified 2nd diffs.
    lexis_curvature_{CC}_*.csv     within-fixed-band 2nd diffs over year (the
                                   object whose curvature CANNOT contain the
                                   cross-band plotting sawtooth — see A2).
    apc_localization_{CC}.csv      period (2015-24 & 2018-24) vs cohort (birth>=1990).
    _assert_no_tfr.log             identification-wall assertion trail (B5/Cond 5).

Assumptions
    - Band/base inherited from Stage 1.5: women, 5-year bands 20-24..35-39,
      composition simplex {single, cohabiting, married}; single = 1 - cohab - married.
      Bands are NOT re-derived. NOTE the 20-39 base excludes the 15-19 entry margin
      (the cascade vanguard) — logged per Anne B6; it is also what breaks the
      peer_younger reference for the youngest band in Task C.
    - PSEUDO-COHORT (Anne A2): birth_cohort = 5-year bin of (year - band_LOWER age),
      i.e. a birth-year bin from (age, survey year) — NOT year - band_midpoint.
      A cohort is tracked across bands at 5-year aging steps; the band-LOWER anchor
      keeps the canonical 5-year cohort boundaries aligned across bands.
    - APC linear trend is UNIDENTIFIED (cohort = period - age). Only curvature
      (second differences) is reported; sum-to-zero coding fixes a normalization
      whose linear split is arbitrary and is deliberately not interpreted.
    - Task B curvature is taken (i) from the APC regression's period/cohort effects,
      which are net of the age=band fixed effect, and (ii) within fixed bands (Lexis
      table). Neither sees the cross-band calendar-connected cohort series, so the
      2012/2017/2022 fig-1 sawtooth cannot leak into curvature (Anne A2).
    - WLS weight = n_women_weighted (band sampling mass).

Dependencies
    python>=3.12, pandas, numpy, statsmodels. CPU-only (Anne compute envelope).

Identification wall (Stage 1.5 gate of record)
    Period TFR is NEVER loaded or used here. Enforced by assert_no_tfr() (which
    also writes an audit trail to _assert_no_tfr.log, B5) and by never reading
    data/national/. `w` is not an object of 2b.
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

SOURCES = {
    "CRI": "CRI_coupling_annual.csv",
    "COL": "COL_coupling_annual.csv",
    "MEX": "MEX_coupling_annual.csv",  # comparator only; biennial/coarse
}
PRIMARY = ("CRI", "COL")

# Stage 1.5 bands — do NOT re-derive (§1). Bounds drive cohort + age FE.
BAND_BOUNDS = {"20-24": (20, 24), "25-29": (25, 29),
               "30-34": (30, 34), "35-39": (35, 39)}
BAND_LOWER = {b: lo for b, (lo, _) in BAND_BOUNDS.items()}
BAND_MIDPOINT = {b: (lo + hi) / 2 for b, (lo, hi) in BAND_BOUNDS.items()}  # age-FE label only
COHORT_BIN = 5

# Anne A4 — substantive cuts (replace the mechanical youngest-third / single box).
PERIOD_WINDOWS = {"2015_2024": (2015, 2024), "2018_2024": (2018, 2024)}
ENTRY_COHORT_MIN = 1990  # entry cohorts = birth-year >= 1990

ASSERT_LOG = os.path.join(OUT_DIR, "_assert_no_tfr.log")


# --------------------------------------------------------------------------- #
# Identification-wall guard (+ B5 audit trail)
# --------------------------------------------------------------------------- #
def assert_no_tfr(df: pd.DataFrame, where: str) -> None:
    """Hard stop if any fertility/TFR column leaks into an estimation frame.

    Word-aware: catches tfr/asfr/fertility/births columns but NOT demographic
    cohort labels like `birth_cohort`. Every call appends a line to
    _assert_no_tfr.log so the wall verification is part of the artifact set (B5).
    """
    def is_fertility(c: str) -> bool:
        lc = c.lower()
        if "cohort" in lc:                       # birth_cohort, cohort_start — fine
            return False
        return bool(re.search(r"tfr|asfr|fertil|\bbirths?\b", lc))

    banned = [c for c in df.columns if is_fertility(c)]
    try:
        os.makedirs(OUT_DIR, exist_ok=True)
        with open(ASSERT_LOG, "a") as fh:
            fh.write(f"[apc] {where}: cols={list(df.columns)} -> "
                     f"{'PASS' if not banned else 'VIOLATION ' + str(banned)}\n")
    except OSError:
        pass
    if banned:
        raise RuntimeError(
            f"Identification wall violated in {where}: TFR/fertility columns "
            f"{banned} must never enter Stage 2b estimation (Stage 1.5 gate)."
        )


# --------------------------------------------------------------------------- #
# Task A — pseudo-cohort construction (Anne A2: birth-year bin)
# --------------------------------------------------------------------------- #
def load_composition(country: str) -> pd.DataFrame:
    """Load one country's coupling series and derive the composition simplex."""
    path = os.path.join(DATA_DIR, SOURCES[country])
    df = pd.read_csv(path)
    df = df[df["age_band"].isin(BAND_BOUNDS)].copy()
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
    """Task A (Anne A2): assign each (year, band) cell to a 5-year birth cohort
    using birth-year = year - band_LOWER age (NOT year - band_midpoint).

    The band-lower anchor differs from successive bands by exactly 5 years, so a
    given 5-year birth cohort maps consistently as it ages through the bands;
    binning to canonical 5-year boundaries gives the tracked pseudo-cohort.
    """
    comp = comp.copy()
    lower = comp["age_band"].map(BAND_LOWER).astype(int)
    comp["birth_year_anchor"] = comp["year"] - lower
    lo = (np.floor(comp["birth_year_anchor"] / COHORT_BIN) * COHORT_BIN).astype(int)
    comp["cohort_start"] = lo
    comp["birth_cohort"] = [f"{a}-{a + COHORT_BIN - 1}" for a in lo]
    return comp


# --------------------------------------------------------------------------- #
# Task B — curvature within fixed bands (Lexis) — sawtooth cannot enter here
# --------------------------------------------------------------------------- #
def lexis_within_band_curvature(panel: pd.DataFrame, share_col: str) -> pd.DataFrame:
    """Second differences of the share over calendar year, taken WITHIN each
    fixed band. By construction these never cross a band boundary, so the
    cross-band plotting sawtooth (2012/2017/2022) cannot contaminate them (A2).

    Returns long: age_band, year, second_diff, n_women_weighted.
    """
    rows = []
    for band, g in panel.sort_values("year").groupby("age_band"):
        s = g.set_index("year")[share_col]
        d2 = s.shift(-1) - 2.0 * s + s.shift(1)
        w = g.set_index("year")["n_women_weighted"]
        rows.append(pd.DataFrame({"age_band": band, "year": s.index,
                                  "second_diff": d2.values,
                                  "n_women_weighted": w.values}))
    return pd.concat(rows, ignore_index=True)


# --------------------------------------------------------------------------- #
# Task B — APC regression (separator of period vs cohort, net of age=band FE)
# --------------------------------------------------------------------------- #
def _second_differences(effects: pd.Series) -> pd.Series:
    e = effects.sort_index()
    return e.shift(-1) - 2.0 * e + e.shift(1)


def apc_decompose(panel: pd.DataFrame, share_col: str = "share_married"):
    """Fit sum-to-zero WLS APC; return period & cohort effects with identified
    second differences. age=band enters as a fixed effect, so the regression
    operates on (band, period, cohort) CELLS — it never sees the calendar-
    connected cohort series, hence is immune to the fig-1 sawtooth (A2).
    """
    d = panel.dropna(subset=[share_col, "n_women_weighted"]).copy()
    d["age"] = d["age_band"].astype("category")
    d["period"] = d["year"].astype("category")
    d["cohort"] = d["cohort_start"].astype("category")
    assert_no_tfr(d, "apc_decompose")

    formula = f"{share_col} ~ C(age, Sum) + C(period, Sum) + C(cohort, Sum)"
    model = smf.wls(formula, data=d, weights=d["n_women_weighted"]).fit()

    def _marginals(values, prefix):
        levels = sorted(values.unique())
        eff = {}
        for lv in levels:
            key = [p for p in model.params.index
                   if p.startswith(prefix) and f"[S.{lv}]" in p]
            eff[lv] = model.params[key[0]] if key else np.nan
        s = pd.Series(eff)
        return s.fillna(-s.sum(skipna=True))  # recover dropped (sum-to-zero) level

    period_eff = _marginals(d["year"], "C(period, Sum)")
    cohort_eff = _marginals(d["cohort_start"], "C(cohort, Sum)")
    period_tab = pd.DataFrame({"period": period_eff.index, "effect": period_eff.values})
    period_tab["second_diff"] = _second_differences(period_eff).values
    cohort_tab = pd.DataFrame({"cohort_start": cohort_eff.index, "effect": cohort_eff.values})
    cohort_tab["second_diff"] = _second_differences(cohort_eff).values
    return model, period_tab, cohort_tab


def localization_summary(period_tab, cohort_tab, country, share_col):
    """Period (over 2015-24 AND 2018-24 windows) vs cohort (birth-year >= 1990)
    curvature, RMS of identified second differences. Descriptive read, NOT §5.
    """
    cmask = cohort_tab["cohort_start"] >= ENTRY_COHORT_MIN
    cohort_curv = np.sqrt(np.nanmean(cohort_tab.loc[cmask, "second_diff"] ** 2))
    out = []
    for tag, (lo, hi) in PERIOD_WINDOWS.items():
        pmask = period_tab["period"].between(lo, hi)
        period_curv = np.sqrt(np.nanmean(period_tab.loc[pmask, "second_diff"] ** 2))
        total = period_curv + cohort_curv
        out.append({
            "country": country, "share": share_col, "period_window": tag,
            "period_curvature_rms": period_curv,
            "cohort_curvature_rms_birth_ge_1990": cohort_curv,
            "period_share_of_curvature": period_curv / total if total else np.nan,
            "leaning": "period" if period_curv > cohort_curv else "cohort",
            "normalization": "sum-to-zero; linear trend NOT identified/reported",
        })
    return pd.DataFrame(out)


# --------------------------------------------------------------------------- #
# Driver
# --------------------------------------------------------------------------- #
def run_country(country: str) -> pd.DataFrame:
    comp = load_composition(country)
    panel = build_pseudo_cohorts(comp)

    tidy = panel[["country", "birth_cohort", "cohort_start", "age_band", "year",
                  "share_single", "share_cohab", "share_married",
                  "n_women_weighted"]]
    tidy.to_csv(os.path.join(OUT_DIR, f"composition_panel_{country}.csv"), index=False)

    loc_rows = []
    for share_col in ("share_married", "share_cohab"):
        tag = share_col.replace("share_", "")
        _, period_tab, cohort_tab = apc_decompose(panel, share_col)
        period_tab.to_csv(os.path.join(OUT_DIR, f"apc_period_effects_{country}_{tag}.csv"), index=False)
        cohort_tab.to_csv(os.path.join(OUT_DIR, f"apc_cohort_effects_{country}_{tag}.csv"), index=False)
        lexis_within_band_curvature(panel, share_col).to_csv(
            os.path.join(OUT_DIR, f"lexis_curvature_{country}_{tag}.csv"), index=False)
        loc_rows.append(localization_summary(period_tab, cohort_tab, country, share_col))
    loc = pd.concat(loc_rows, ignore_index=True)
    loc.to_csv(os.path.join(OUT_DIR, f"apc_localization_{country}.csv"), index=False)
    return loc


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    # Fresh assertion log per run (B5 artifact).
    with open(ASSERT_LOG, "w") as fh:
        fh.write("# Stage 2b identification-wall assertion trail (assert_no_tfr)\n")
    summaries = []
    for country in SOURCES:
        if country not in PRIMARY:
            print(f"[2b] {country}: comparator — pseudo-panel only (coarse/biennial).")
        try:
            summaries.append(run_country(country))
            print(f"[2b] {country}: panel + APC + Lexis curvature -> {OUT_DIR}")
        except FileNotFoundError as e:
            print(f"[2b] {country}: SKIP (missing input) — {e}")
    if summaries:
        allsum = pd.concat(summaries, ignore_index=True)
        allsum.to_csv(os.path.join(OUT_DIR, "apc_localization_ALL.csv"), index=False)
        print("\n[2b] Curvature-localization read (descriptive, NOT the §5 rule):")
        print(allsum.to_string(index=False))


if __name__ == "__main__":
    main()
