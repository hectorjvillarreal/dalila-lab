#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
stage2b_state_dependence.py — Stage 2b Task C (the sharp test)

================================ PROTO-RAG-001 ================================
Purpose
    Estimate the within-cohort state-dependence (reflexivity) signature that
    distinguishes H_cascade from H_shock/H_cohort. The cascade signature is a
    within-cohort marriage-share decline that is LARGER where the reference
    group's cohabiting+single share has already risen:

        Δ(marriage_share)_{c,a,t} = β · ReferenceShare_{t-1}
                                    + age FE + cohort FE + ε

    Sign/significance of β is the read:
        β amplifying & significant  -> H_cascade (state-dependent)
        β ≈ 0, period effect present -> H_shock
        β ≈ 0, period effect absent  -> H_cohort
    This script estimates β with robustness; it does NOT apply the §5 rule and
    does NOT touch the ABM.

Inputs
    outputs/stage2b/composition_panel_{CC}.csv   (Task A output of
        stage2b_apc_composition.py — run that first.)

Outputs (outputs/stage2b/)
    statedep_estimates_{CC}.csv   β, SE, CI, n by (reference-group spec × lag).
    statedep_period_test_{CC}.csv joint test of period FE (is a period effect
                                  present at all? — needed to read β≈0 cases).
    statedep_summary.csv          one row per country×spec for the memo.

Assumptions
    - LHS Δ is the within-pseudo-cohort year-over-year change in marriage share
      (a cohort tracked by cohort_start as it ages). Annual deltas.
    - ReferenceShare_{t-1} is a LAGGED, DISTINCT-GROUP cohab+single share, to
      avoid the mechanical identity Δmarriage ≡ -Δ(1-marriage) that an own-lag
      reference would induce. Reference-group specs (robustness knob):
        * "peer_younger" : cohab+single share of the next-younger band at t-1
        * "pop2039"      : cohab+single share of all women 20-39 at t-1
        * "own_lag"      : own cohort's cohab+single at t-1 — REPORTED ONLY as a
                           mechanically-contaminated comparator, flagged as such.
    - Clustering: by cohort_start (within-country). Lag length robustness: 1, 2.
    - age FE + cohort FE absorb the H_cohort mix-shift; β is the residual
      state-dependence net of that.

Dependencies
    python>=3.12, pandas, numpy, statsmodels. CPU-only.

Identification wall
    TFR is NEVER on the RHS and is never loaded (assert_no_tfr; data/national/
    is not read). `w` is not used.
==============================================================================
"""
from __future__ import annotations

import os
import re
import itertools
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "outputs", "stage2b")
PRIMARY = ("CRI", "COL")

BAND_ORDER = ["20-24", "25-29", "30-34", "35-39"]
BAND_NEXT_YOUNGER = {"25-29": "20-24", "30-34": "25-29", "35-39": "30-34"}
BAND_NEXT_OLDER = {"20-24": "25-29", "25-29": "30-34", "30-34": "35-39"}

# Anne A1 — reference-group specs and their adjudication roles (§5 amended rule).
#   peer_younger : PRIMARY     — excludes focal cohort; upward-diffusion referent.
#   peer_older   : clean       — template-setter referent; tests diffusion direction.
#   pop2039      : robustness  — focal cohort inside it (mild inclusion bias).
#   own_lag      : comparator  — mechanically contaminated; never decisive.
SPEC_ROLE = {"peer_younger": "primary", "peer_older": "clean",
             "pop2039": "robustness", "own_lag": "comparator"}
REFERENCE_SPECS = ("peer_younger", "peer_older", "pop2039", "own_lag")
LAGS = (1, 2)

ASSERT_LOG = os.path.join(OUT_DIR, "_assert_no_tfr.log")


def assert_no_tfr(df: pd.DataFrame, where: str) -> None:
    def is_fertility(c: str) -> bool:
        lc = c.lower()
        if "cohort" in lc:                       # birth_cohort, cohort_start — fine
            return False
        return bool(re.search(r"tfr|asfr|fertil|\bbirths?\b", lc))

    banned = [c for c in df.columns if is_fertility(c)]
    try:                                          # B5 audit trail (append; apc writes header)
        os.makedirs(OUT_DIR, exist_ok=True)
        with open(ASSERT_LOG, "a") as fh:
            fh.write(f"[statedep] {where}: cols={list(df.columns)} -> "
                     f"{'PASS' if not banned else 'VIOLATION ' + str(banned)}\n")
    except OSError:
        pass
    if banned:
        raise RuntimeError(f"Identification wall violated in {where}: {banned}")


# --------------------------------------------------------------------------- #
# Reference-share construction
# --------------------------------------------------------------------------- #
def _ref_share_not_married(df: pd.DataFrame) -> pd.Series:
    """cohab+single share = 1 - married share (the 'has not married' mass)."""
    return df["share_cohab"] + df["share_single"]


def build_reference(panel: pd.DataFrame, spec: str, lag: int) -> pd.DataFrame:
    """Attach ReferenceShare_{t-lag} to each (cohort, band, year) cell."""
    p = panel.copy()
    p["ref_now"] = _ref_share_not_married(p)

    if spec == "own_lag":
        ref = (p.groupby(["cohort_start", "age_band"])
                 .apply(lambda g: g.set_index("year")["ref_now"].shift(lag),
                        include_groups=False)
                 .rename("ref_lag").reset_index())
        p = p.merge(ref, on=["cohort_start", "age_band", "year"], how="left")

    elif spec in ("peer_younger", "peer_older"):
        # Reference = the adjacent band's not-married share at t-lag. peer_younger
        # is the upward-diffusion referent (excludes focal cohort, undefined for the
        # youngest band — see B6 20-39 floor); peer_older is the template-setter
        # referent (undefined for the oldest band).
        nbr_map = BAND_NEXT_YOUNGER if spec == "peer_younger" else BAND_NEXT_OLDER
        nbr = p[["year", "age_band", "ref_now"]].rename(
            columns={"age_band": "nbr_band", "ref_now": "ref_nbr", "year": "year_lag"})
        p["nbr_band"] = p["age_band"].map(nbr_map)
        p["year_lag"] = p["year"] - lag
        p = p.merge(nbr, on=["nbr_band", "year_lag"], how="left")
        p["ref_lag"] = p["ref_nbr"]

    elif spec == "pop2039":
        # Population 20-39 reference: n-weighted mean of ref_now across bands.
        pop = (p.groupby("year")
                 .apply(lambda g: np.average(g["ref_now"],
                                             weights=g["n_women_weighted"]),
                        include_groups=False)
                 .rename("ref_pop").reset_index())
        pop["year_lag"] = pop["year"] + lag  # value at t-lag attached at t
        ref = pop[["year_lag", "ref_pop"]].rename(columns={"year_lag": "year"})
        p = p.merge(ref, on="year", how="left")
        p["ref_lag"] = p["ref_pop"]
    else:
        raise ValueError(f"unknown reference spec {spec}")

    return p


# --------------------------------------------------------------------------- #
# LHS delta and estimation
# --------------------------------------------------------------------------- #
def add_within_cohort_delta(panel: pd.DataFrame) -> pd.DataFrame:
    """Δ(marriage_share) within pseudo-cohort, year over year."""
    p = panel.sort_values(["cohort_start", "age_band", "year"]).copy()
    p["d_married"] = (p.groupby(["cohort_start", "age_band"])["share_married"]
                        .diff())
    return p


def estimate(panel: pd.DataFrame, spec: str, lag: int) -> dict:
    df = build_reference(add_within_cohort_delta(panel), spec, lag)
    df = df.dropna(subset=["d_married", "ref_lag"]).copy()
    assert_no_tfr(df, f"estimate[{spec},lag{lag}]")
    if df["cohort_start"].nunique() < 3 or len(df) < 10:
        return {"reference_spec": spec, "role": SPEC_ROLE[spec], "lag": lag,
                "n": len(df), "beta": np.nan, "se": np.nan, "ci_lo": np.nan,
                "ci_hi": np.nan, "pvalue": np.nan, "amplifying": False,
                "note": "insufficient variation"}

    df["age"] = df["age_band"].astype("category")
    df["cohort"] = df["cohort_start"].astype("category")
    model = smf.ols("d_married ~ ref_lag + C(age) + C(cohort)", data=df).fit(
        cov_type="cluster", cov_kwds={"groups": df["cohort_start"]})
    ci = model.conf_int().loc["ref_lag"]
    return {
        "reference_spec": spec, "role": SPEC_ROLE[spec], "lag": lag,
        "n": int(len(df)),
        "beta": float(model.params["ref_lag"]),
        "se": float(model.bse["ref_lag"]),
        "ci_lo": float(ci[0]), "ci_hi": float(ci[1]),
        "pvalue": float(model.pvalues["ref_lag"]),
        # amplifying sign: not-married share UP -> marriage DOWN -> Δ<0 -> β<0
        "amplifying": bool(model.params["ref_lag"] < 0
                           and model.pvalues["ref_lag"] < 0.10),
        "note": "MECHANICAL own-lag — comparator only" if spec == "own_lag" else "",
    }


def period_effect_test(panel: pd.DataFrame) -> dict:
    """Is a period effect present at all? Joint F-test of year FE on Δmarriage.

    Needed to disambiguate the two β≈0 readings (H_shock vs H_cohort, §5).
    """
    df = add_within_cohort_delta(panel).dropna(subset=["d_married"]).copy()
    df["age"] = df["age_band"].astype("category")
    df["cohort"] = df["cohort_start"].astype("category")
    df["period"] = df["year"].astype("category")
    full = smf.ols("d_married ~ C(age) + C(cohort) + C(period)", data=df).fit()
    restr = smf.ols("d_married ~ C(age) + C(cohort)", data=df).fit()
    ft = full.compare_f_test(restr)
    return {"period_F": float(ft[0]), "period_p": float(ft[1]),
            "period_present": bool(ft[1] < 0.10)}


# --------------------------------------------------------------------------- #
# Driver
# --------------------------------------------------------------------------- #
# Anne B7 — estimator level. CORRECTION surfaced during implementation: Task C's
# LHS is a within-pseudo-cohort CELL composition change, so on repeated cross-
# sections BOTH countries' β are ECOLOGICAL (cell-level) — no individual union
# transitions are observed in either (the §8 pseudo-panel limitation). The CR/COL
# asymmetry is in how the CELLS are built, not the estimator level:
#   CR  — cells are REDATAM pre-tabulated aggregates (coarsest; not reweightable).
#   COL — cells computed from DANE microdata (finer; reweightable in principle).
# This deviates from Anne's B7 wording ("COL β is individual-level"); logged as a
# protocol note in the memo for Anne's confirmation, not silently absorbed.
ESTIMATOR_LEVEL = {
    "CRI": "ecological — REDATAM pre-tabulated cells",
    "COL": "ecological — cells from DANE microdata",
}


def run_country(country: str) -> pd.DataFrame:
    path = os.path.join(OUT_DIR, f"composition_panel_{country}.csv")
    panel = pd.read_csv(path)

    rows = [estimate(panel, spec, lag)
            for spec, lag in itertools.product(REFERENCE_SPECS, LAGS)]
    est = pd.DataFrame(rows)
    est.insert(0, "country", country)
    est["estimator_level"] = ESTIMATOR_LEVEL.get(country, "ecological")
    est.to_csv(os.path.join(OUT_DIR, f"statedep_estimates_{country}.csv"),
               index=False)

    ptest = period_effect_test(panel)  # keys already period_F/period_p/period_present
    pd.DataFrame([{"country": country, **ptest}]).to_csv(
        os.path.join(OUT_DIR, f"statedep_period_test_{country}.csv"), index=False)
    return est.assign(**ptest)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    summaries = []
    for country in PRIMARY:
        path = os.path.join(OUT_DIR, f"composition_panel_{country}.csv")
        if not os.path.exists(path):
            print(f"[2b-C] {country}: SKIP — run stage2b_apc_composition.py first.")
            continue
        s = run_country(country)
        summaries.append(s)
        print(f"[2b-C] {country}: β estimates + period test -> {OUT_DIR}")
    if summaries:
        allsum = pd.concat(summaries, ignore_index=True)
        allsum.to_csv(os.path.join(OUT_DIR, "statedep_summary.csv"), index=False)
        # Full β matrix (all specs × CR/COL × lags) — Anne A1 deliverable.
        matrix = allsum.pivot_table(index=["reference_spec", "role", "lag"],
                                    columns="country", values="beta")
        matrix.to_csv(os.path.join(OUT_DIR, "statedep_beta_matrix.csv"))
        print("\n[2b-C] State-dependence read (sign of β; NOT the §5 rule):")
        cols = ["country", "reference_spec", "role", "lag", "beta", "se",
                "pvalue", "amplifying", "period_present"]
        print(allsum[cols].to_string(index=False))
        print("\n[2b-C] Full β matrix (rows: spec×role×lag; cols: country):")
        print(matrix.to_string())


if __name__ == "__main__":
    main()
