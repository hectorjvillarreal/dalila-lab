#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
stage2c_individual_model.py — Stage 2c-i (the cascade-below-the-cell pivot)

================================ PROTO-RAG-001 ================================
Purpose
    The 2c-i individual-level look mandated by STAGE2c_col_individual_instruction.md.
    Stage 2b's β was ECOLOGICAL (Anne B7): Task C regressed a CELL composition
    *share* on a cell reference share, observing no individual union behavior.
    Ecological aggregation can mask — and in principle sign-flip — an individual
    relationship, so a within-cohort reflexive cascade could still hide BELOW the
    cell. This stage looks there, in COL (the only country with microdata), by
    moving the OUTCOME to the person while keeping the reference regressor a lagged
    distinct-group share (as in 2b). It can OVERTURN the 2b non-cascade verdict.

    It does NOT observe transitions (GEIH is a repeated cross-section): 2c-i is a
    union-STATUS model. The true individual union-formation hazard is 2c-ii on ENDS
    (gated; not attempted here). It does NOT apply closure — Anne's 9a ruling makes
    2c-i necessary-but-not-sufficient to close (B): it can only fail to reopen.

Why "grouped logit" is genuinely individual-level (not a re-aggregation)
    Persons sharing identical discrete covariates (year, single-year age, urban,
    education, outcome) are exchangeable given those covariates, so collapsing them
    to weighted counts is a SUFFICIENT STATISTIC: the grouped-binomial MLE equals
    the person-by-person logit MLE exactly. The ecological problem in 2b was that
    the OUTCOME was a share; here the outcome (married 0/1) stays at the person
    level. The collapse is a tractability device, not an aggregation of the LHS.

Design (mirrors 2b where the test must be comparable)
    - Outcome: married_i = 1[P6070==3]. (P6070: 1,2 cohab / 3 married / 4,5,6 single.)
    - Reference regressor: ReferenceShare_{g(i),t-lag} = lagged NOT-married share of
      the individual's reference group, same groups/specs as 2b state-dependence:
        peer_younger (primary), peer_older (clean), pop_all (robustness).
      Amplifying (self-reinforcing retreat) = P(married) DECLINES as the reference
      not-married share rises => β < 0 & significant. SAME sign convention as 2b.
    - FE backbone: C(age_band) + C(cohort_start) — mirrors 2b's
      `d_married ~ ref_lag + C(age) + C(cohort)` and avoids the APC collinearity
      trap (age = year - cohort). A year-FE variant is reported as robustness only.
    - Age floor extended to 15 (instruction §3): the 15-19 entry/ignition band —
      Anne's second deferred channel — is OBSERVED here, unlike 2b's 20-39 floor.
    - Inference: cluster-robust on band×year. ref_lag varies only at band×year, so
      that is the honest inferential level; it stops millions of person-rows from
      fake-inflating significance (~90-108 clusters).
    - Weights: GEIH expansion factor, normalized to sum to the SAMPLE person count
      so effective N is the sample, not the projected population (honest SEs).

Pre-registered decision rule (instruction §4) — applied in classify_reading():
    non-amplifying incl. 15-19            -> H_confirm     (B) deferred, AGGREGATION-CLEARED, pending ENDS
    amplifying & significant, robust      -> H_reopen      (B) reopened; reflexivity back to Stage 3
    amplifying only in 15-19              -> H_entry-margin (B) partially reopened for youngest band

Inputs
    ../data/coupling/_geih_cache/*.zip   (DANE GEIH person modules, 2007-2024, cached
                                          offline; read via _extract_geih_col_v2 helpers)
Outputs (outputs/stage2c/)
    person_cells_COL.csv.gz        PASS-1 collapsed person-cell cache (rebuildable).
    ref_shares_COL.csv             not-married reference share by band×year (incl 15-19).
    stage2c_individual_estimates.csv   β by reference spec × lag × {with,without 15-19}.
    stage2c_entry_margin_COL.csv   15-19-only and interaction read (H_entry-margin test).
    stage2c_multinomial_COL.csv    descriptive married/cohab vs single multinomial.
    stage2c_vs_2b_beta.csv         individual-level β beside the 2b cell-level β.
    stage2c_reading.json           classified reading (confirm/reopen/entry-margin).
    _assert_no_tfr.log             identification-wall trail (carried over from 2b).

Dependencies
    python>=3.12, pandas, numpy, statsmodels, pyarrow. CPU-only (Anne envelope).
    Reuses ../data/coupling/_extract_geih_col_v2.py reader helpers (DANE redesign
    breaks: sex P6020<->P3271, weight Fex_c_2011<->FEX_C18, cab+resto pooling).

Identification wall (Stage 1.5 gate of record)
    Period TFR is NEVER loaded or used. assert_no_tfr() guards every estimation
    frame and appends to _assert_no_tfr.log. data/national/ is never read; `w` /
    fertility intensity is NOT a 2c-i object (gated to ENDS with 2c-ii).
==============================================================================
"""
from __future__ import annotations

import argparse
import glob
import importlib.util
import os
import re
import sys

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

# --------------------------------------------------------------------------- #
# Paths & configuration
# --------------------------------------------------------------------------- #
HERE = os.path.dirname(os.path.abspath(__file__))
COUPLING_DIR = os.path.normpath(os.path.join(HERE, "..", "data", "coupling"))
CACHE = os.path.join(COUPLING_DIR, "_geih_cache")
OUT_DIR = os.path.join(HERE, "outputs", "stage2c")
CELLS_PATH = os.path.join(OUT_DIR, "person_cells_COL.csv.gz")
ASSERT_LOG = os.path.join(OUT_DIR, "_assert_no_tfr.log")
STAGE2B_SUMMARY = os.path.join(HERE, "outputs", "stage2b", "statedep_summary.csv")

# Bands now include the 15-19 entry margin (instruction §3) — NOT in 2b's 20-39 base.
BANDS = [("15-19", 15, 19), ("20-24", 20, 24), ("25-29", 25, 29),
         ("30-34", 30, 34), ("35-39", 35, 39)]
BAND_ORDER = [b for b, _, _ in BANDS]
BAND_LOWER = {b: lo for b, lo, _ in BANDS}
ENTRY_BAND = "15-19"
COHAB_CODES, MARRIED_CODES = {1, 2}, {3}
COHORT_BIN = 5

# Reference-group specs (Anne A1 roles carried from 2b state-dependence).
#   peer_younger : PRIMARY    — next-younger band; excludes focal; upward-diffusion referent.
#   peer_older   : clean      — next-older band; template-setter referent.
#   pop_all      : robustness — whole 15-39 (or 20-39) female pop; focal inside it.
BAND_NEXT_YOUNGER = {"20-24": "15-19", "25-29": "20-24", "30-34": "25-29", "35-39": "30-34"}
BAND_NEXT_OLDER = {"15-19": "20-24", "20-24": "25-29", "25-29": "30-34", "30-34": "35-39"}
SPEC_ROLE = {"peer_younger": "primary", "peer_older": "clean", "pop_all": "robustness"}
REFERENCE_SPECS = ("peer_younger", "peer_older", "pop_all")
LAGS = (1, 2)
AMPLIFY_P = 0.10  # significance threshold for "amplifying" (matches 2b)

# Education (P6210, pre-redesign only) coarsened; primary spec does NOT use it
# (post-2021 recoding break) — robustness covariate on the pre-2021 subsample.
EDUC3 = {1: "low", 2: "low", 3: "low", 4: "mid", 5: "mid", 6: "high"}

_ext = None  # lazily-imported _extract_geih_col_v2 module (PASS 1 only)


# --------------------------------------------------------------------------- #
# Identification-wall guard (carried over from 2b; appends to shared-style log)
# --------------------------------------------------------------------------- #
def assert_no_tfr(df: pd.DataFrame, where: str) -> None:
    def is_fertility(c: str) -> bool:
        lc = str(c).lower()
        if "cohort" in lc:  # birth_cohort, cohort_start — demographic labels, fine
            return False
        return bool(re.search(r"tfr|asfr|fertil|\bbirths?\b", lc))

    banned = [c for c in df.columns if is_fertility(c)]
    try:
        os.makedirs(OUT_DIR, exist_ok=True)
        with open(ASSERT_LOG, "a") as fh:
            fh.write(f"[2c] {where}: cols={list(df.columns)} -> "
                     f"{'PASS' if not banned else 'VIOLATION ' + str(banned)}\n")
    except OSError:
        pass
    if banned:
        raise RuntimeError(
            f"Identification wall violated in {where}: {banned} must never enter "
            f"Stage 2c estimation (Stage 1.5 gate)."
        )


def band_of(age: pd.Series) -> pd.Series:
    out = pd.Series(pd.NA, index=age.index, dtype="object")
    for b, lo, hi in BANDS:
        out[(age >= lo) & (age <= hi)] = b
    return out


# --------------------------------------------------------------------------- #
# PASS 1 — build the collapsed person-cell cache from cached GEIH zips (offline)
# --------------------------------------------------------------------------- #
def _load_extractor():
    global _ext
    if _ext is None:
        path = os.path.join(COUPLING_DIR, "_extract_geih_col_v2.py")
        spec = importlib.util.spec_from_file_location("_geih_ext", path)
        _ext = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_ext)
    return _ext


def _cached_months(year: int):
    """One zip per calendar month from the offline cache (dedup like select_monthly)."""
    ext = _load_extractor()
    by_month = {}
    for fn in sorted(glob.glob(os.path.join(CACHE, f"{year}_*"))):
        name = os.path.basename(fn)
        if ext.is_aggregate(name):
            continue
        m = ext.month_of(name)
        if m is None:
            continue
        cur = by_month.get(m)
        if cur is None or ext.fmt_rank(name) < ext.fmt_rank(os.path.basename(cur)):
            by_month[m] = fn
    return [by_month[m] for m in sorted(by_month)]


def _persons_from_frame(df: pd.DataFrame) -> pd.DataFrame | None:
    """Person rows: women 15-39, with union status, urban, education. NOT aggregated."""
    ext = _load_extractor()
    cu = ext.pick(df.columns, ext.UNION_CANDS)
    ca = ext.pick(df.columns, ext.AGE_CANDS)
    cs = ext.pick(df.columns, ext.SEX_CANDS)
    cw = ext.pick(df.columns, ext.WEIGHT_CANDS)
    cl = ext.pick(df.columns, ["clase"])
    ce = ext.pick(df.columns, ["p6210"])
    if not all([cu, ca, cs, cw]):
        return None
    cols = [cu, ca, cs, cw] + [c for c in (cl, ce) if c]
    d = df[cols].copy()
    for c in (cu, ca, cs):
        d[c] = pd.to_numeric(d[c], errors="coerce")
    d[cw] = pd.to_numeric(d[cw].astype(str).str.replace(",", ".", regex=False),
                          errors="coerce")
    d = d.dropna(subset=[cu, ca, cs, cw])
    d = d[(d[cs] == 2) & (d[ca] >= 15) & (d[ca] <= 39)]
    if d.empty:
        return None
    out = pd.DataFrame({
        "age": d[ca].astype(int),
        "weight": d[cw].astype(float),
        "married": (d[cu].isin(MARRIED_CODES)).astype(int),
        "cohab": (d[cu].isin(COHAB_CODES)).astype(int),
    })
    # status: married / cohabiting / single (single absorbs sep,div,widow,never — as 2b)
    out["status"] = np.where(out["married"] == 1, "married",
                             np.where(out["cohab"] == 1, "cohabiting", "single"))
    if cl is not None:
        clv = pd.to_numeric(d[cl], errors="coerce")
        out["urban"] = np.where(clv == 1, 1, np.where(clv == 2, 0, np.nan))
    else:
        out["urban"] = np.nan
    if ce is not None:
        ev = pd.to_numeric(d[ce], errors="coerce").map(EDUC3)
        out["educ3"] = ev.astype("object")
    else:
        out["educ3"] = pd.NA
    return out


def build_person_cells(years, max_months=None) -> pd.DataFrame:
    """Read cached GEIH person modules and collapse to weighted covariate cells.

    Collapsing to (year, age, urban, educ3, status) with summed weight + count is a
    sufficient statistic for the person-level logit (see module docstring).
    """
    ext = _load_extractor()
    parts = []
    for y in years:
        months = _cached_months(y)
        if max_months:
            months = months[:max_months]
        if not months:
            print(f"  {y}: no cached months found — SKIP", file=sys.stderr)
            continue
        n_frames, n_persons = 0, 0
        for fn in months:
            try:
                with __import__("zipfile").ZipFile(fn) as zf:
                    frames = ext.person_frames(zf)
            except Exception as e:  # noqa: BLE001 — bad zip / read error, log & continue
                print(f"    ! {os.path.basename(fn)}: {e}", file=sys.stderr)
                continue
            for _mem, df in frames:
                pr = _persons_from_frame(df)
                if pr is None or pr.empty:
                    continue
                pr["year"] = y
                parts.append(pr)
                n_frames += 1
                n_persons += len(pr)
        print(f"  {y}: {len(months)} months, {n_frames} frames, "
              f"{n_persons:,} women 15-39")
    if not parts:
        raise RuntimeError("no person records read from cache")
    allp = pd.concat(parts, ignore_index=True)
    allp["age_band"] = band_of(allp["age"])
    allp["birth_year"] = allp["year"] - allp["age"]
    allp["cohort_start"] = (np.floor(allp["birth_year"] / COHORT_BIN)
                            * COHORT_BIN).astype(int)
    allp["urban"] = allp["urban"]  # may contain NaN if CLASE absent
    allp["educ3"] = allp["educ3"].astype("object")
    # Collapse: one row per distinct covariate cell, summing weight & counting persons.
    grp = ["year", "age", "age_band", "cohort_start", "birth_year",
           "urban", "educ3", "status", "married"]
    cells = (allp.groupby(grp, dropna=False)
                 .agg(weight=("weight", "sum"), n=("weight", "size"))
                 .reset_index())
    return cells


def ensure_cells(years, max_months, rebuild) -> pd.DataFrame:
    if os.path.exists(CELLS_PATH) and not rebuild:
        print(f"[2c PASS1] using cached cells: {CELLS_PATH}")
        return pd.read_csv(CELLS_PATH)
    print("[2c PASS1] building person-cell cache from GEIH zips (offline)…")
    cells = build_person_cells(years, max_months)
    os.makedirs(OUT_DIR, exist_ok=True)
    cells.to_csv(CELLS_PATH, index=False)
    print(f"[2c PASS1] wrote {CELLS_PATH}  ({len(cells):,} cells, "
          f"{int(cells['n'].sum()):,} persons, "
          f"{cells['weight'].sum():,.0f} weighted)")
    return cells


# --------------------------------------------------------------------------- #
# PASS 2 — reference shares, estimation, decision rule
# --------------------------------------------------------------------------- #
def reference_shares(cells: pd.DataFrame) -> pd.DataFrame:
    """Weighted NOT-married share by band×year (the reference object), incl 15-19.

    not_married = 1 - married share = cohab+single mass (mirrors 2b ref construction).
    """
    g = (cells.groupby(["age_band", "year"])
              .apply(lambda d: pd.Series({
                  "married_share": np.average(d["married"], weights=d["weight"]),
                  "n_women_weighted": d["weight"].sum(),
              }), include_groups=False)
              .reset_index())
    g["not_married"] = 1.0 - g["married_share"]
    return g


def _pop_all_ref(ref: pd.DataFrame, include_1519: bool) -> pd.DataFrame:
    """Whole-population not-married share by year (weighted mean across bands)."""
    r = ref if include_1519 else ref[ref["age_band"] != ENTRY_BAND]
    pop = (r.groupby("year")
            .apply(lambda d: np.average(d["not_married"],
                                        weights=d["n_women_weighted"]),
                   include_groups=False)
            .rename("ref_now").reset_index())
    return pop


def attach_reference(cells: pd.DataFrame, ref: pd.DataFrame, spec: str,
                     lag: int, include_1519: bool) -> pd.DataFrame:
    """Attach ReferenceShare_{g,t-lag} to each person-cell by its band & year."""
    c = cells.copy()
    if not include_1519:
        c = c[c["age_band"] != ENTRY_BAND].copy()

    if spec in ("peer_younger", "peer_older"):
        nbr_map = BAND_NEXT_YOUNGER if spec == "peer_younger" else BAND_NEXT_OLDER
        src = ref[["age_band", "year", "not_married"]].rename(
            columns={"age_band": "nbr_band", "year": "year_src", "not_married": "ref_lag"})
        c["nbr_band"] = c["age_band"].map(nbr_map)
        c["year_src"] = c["year"] - lag
        c = c.merge(src, on=["nbr_band", "year_src"], how="left")
    elif spec == "pop_all":
        pop = _pop_all_ref(ref, include_1519)
        pop["year_src"] = pop["year"] + lag  # value at t-lag attached at t
        c = c.merge(pop[["year_src", "ref_now"]].rename(
            columns={"year_src": "year", "ref_now": "ref_lag"}), on="year", how="left")
    else:
        raise ValueError(spec)
    return c


def _cluster_id(df: pd.DataFrame) -> pd.Series:
    return df["age_band"].astype(str) + ":" + df["year"].astype(str)


def estimate_logit(cells, ref, spec, lag, include_1519, use_educ=False) -> dict:
    """Weighted binary logit P(married) ~ ref_lag + C(age_band) + C(cohort_start)
    [+ urban] [+ educ3]; cluster-robust on band×year. Grouped-binomial MLE == the
    person-level logit MLE (sufficient statistic; see docstring).
    """
    d = attach_reference(cells, ref, spec, lag, include_1519)
    cov = ["urban"]
    if use_educ:
        cov.append("educ3")
    need = ["married", "ref_lag", "age_band", "cohort_start", "weight"] + cov
    d = d.dropna(subset=[x for x in need if x != "educ3"]).copy()
    if use_educ:
        d = d.dropna(subset=["educ3"]).copy()
    assert_no_tfr(d, f"logit[{spec},lag{lag},1519={include_1519},educ={use_educ}]")
    if d.empty or d["age_band"].nunique() < 2:
        return {"spec": spec, "role": SPEC_ROLE[spec], "lag": lag,
                "with_1519": include_1519, "educ": use_educ, "n_cells": len(d),
                "n_persons": int(d["n"].sum()) if "n" in d else 0,
                "beta": np.nan, "se": np.nan, "ci_lo": np.nan, "ci_hi": np.nan,
                "pvalue": np.nan, "amplifying": False, "note": "insufficient variation"}

    # Normalize weights to sample N so effective nobs = sample (honest SEs).
    w = d["weight"].to_numpy(float)
    w = w * (d["n"].sum() / w.sum())
    d = d.assign(_fw=w)
    clusters = _cluster_id(d)

    terms = ["ref_lag", "C(age_band)", "C(cohort_start)", "urban"]
    if use_educ:
        terms.append("C(educ3)")
    formula = "married ~ " + " + ".join(terms)
    model = smf.glm(formula, data=d, family=sm.families.Binomial(),
                    freq_weights=d["_fw"]).fit(
        cov_type="cluster", cov_kwds={"groups": clusters})
    b = float(model.params["ref_lag"])
    p = float(model.pvalues["ref_lag"])
    ci = model.conf_int().loc["ref_lag"]
    return {
        "spec": spec, "role": SPEC_ROLE[spec], "lag": lag,
        "with_1519": include_1519, "educ": use_educ,
        "n_cells": int(len(d)), "n_persons": int(d["n"].sum()),
        "n_clusters": int(clusters.nunique()),
        "beta": b, "se": float(model.bse["ref_lag"]),
        "ci_lo": float(ci[0]), "ci_hi": float(ci[1]), "pvalue": p,
        # amplifying: not-married reference UP -> P(married) DOWN -> β<0 (2b convention)
        "amplifying": bool(b < 0 and p < AMPLIFY_P),
        "note": "",
    }


def entry_margin_test(cells, ref) -> pd.DataFrame:
    """H_entry-margin probe: is amplifying dependence concentrated in 15-19?

    (a) 15-19-only subsample logit (peer_older referent — peer_younger undefined
        for the youngest band). (b) full-sample ref_lag×is_1519 interaction.
    """
    rows = []
    # (a) 15-19-only, peer_older + pop_all referents
    only = cells[cells["age_band"] == ENTRY_BAND].copy()
    for spec in ("peer_older", "pop_all"):
        d = attach_reference(only, ref, spec, 1, include_1519=True)
        d = d.dropna(subset=["married", "ref_lag", "cohort_start", "weight"]).copy()
        assert_no_tfr(d, f"entry_only[{spec}]")
        if d.empty or d["cohort_start"].nunique() < 2:
            rows.append({"test": "1519_only", "spec": spec, "beta": np.nan,
                         "pvalue": np.nan, "amplifying": False, "n_persons": 0})
            continue
        w = d["weight"].to_numpy(float)
        d = d.assign(_fw=w * (d["n"].sum() / w.sum()))
        m = smf.glm("married ~ ref_lag + C(cohort_start)", data=d,
                    family=sm.families.Binomial(), freq_weights=d["_fw"]).fit(
            cov_type="cluster", cov_kwds={"groups": d["year"].astype(str)})
        b, p = float(m.params["ref_lag"]), float(m.pvalues["ref_lag"])
        rows.append({"test": "1519_only", "spec": spec, "beta": b, "pvalue": p,
                     "amplifying": bool(b < 0 and p < AMPLIFY_P),
                     "n_persons": int(d["n"].sum())})
    # (b) interaction ref_lag × 1[band==15-19], pop_all referent (defined for all bands)
    d = attach_reference(cells, ref, "pop_all", 1, include_1519=True)
    d = d.dropna(subset=["married", "ref_lag", "age_band", "cohort_start", "weight"]).copy()
    d["is_1519"] = (d["age_band"] == ENTRY_BAND).astype(int)
    assert_no_tfr(d, "entry_interaction")
    w = d["weight"].to_numpy(float)
    d = d.assign(_fw=w * (d["n"].sum() / w.sum()))
    m = smf.glm("married ~ ref_lag * is_1519 + C(age_band) + C(cohort_start)",
                data=d, family=sm.families.Binomial(), freq_weights=d["_fw"]).fit(
        cov_type="cluster", cov_kwds={"groups": _cluster_id(d)})
    inter = "ref_lag:is_1519"
    rows.append({"test": "interaction", "spec": "pop_all",
                 "beta": float(m.params[inter]), "pvalue": float(m.pvalues[inter]),
                 "amplifying": bool(m.params[inter] < 0 and m.pvalues[inter] < AMPLIFY_P),
                 "n_persons": int(d["n"].sum()),
                 "note": "coef on ref_lag×1[15-19]: extra amplification in entry band"})
    return pd.DataFrame(rows)


def multinomial_descriptive(cells, ref) -> pd.DataFrame:
    """Descriptive multinomial (single base; married & cohab vs single) on ref_lag.

    Not the headline (no cluster-robust MNLogit in statsmodels); reported for the
    full {single,cohabiting,married} composition. peer_younger, lag 1, with 15-19.
    """
    d = attach_reference(cells, ref, "peer_younger", 1, include_1519=True)
    d = d.dropna(subset=["ref_lag", "age_band", "cohort_start", "weight"]).copy()
    assert_no_tfr(d, "multinomial")
    if d.empty:
        return pd.DataFrame()
    # Expand to integer pseudo-counts for MNLogit (weights -> rounded sample counts).
    d["status"] = pd.Categorical(d["status"],
                                 categories=["single", "cohabiting", "married"])
    w = d["weight"].to_numpy(float)
    d["_fw"] = w * (d["n"].sum() / w.sum())
    X = sm.add_constant(pd.get_dummies(
        d[["ref_lag", "age_band", "cohort_start"]].astype(
            {"age_band": "category", "cohort_start": "category"}),
        drop_first=True, dtype=float))
    try:
        m = sm.MNLogit(d["status"].cat.codes, X, freq_weights=d["_fw"]).fit(disp=0)
        out = []
        for j, lvl in enumerate(["cohabiting", "married"]):  # base=single(code0)
            out.append({"outcome_vs_single": lvl,
                        "ref_lag_coef": float(m.params.loc["ref_lag", j]),
                        "ref_lag_p": float(m.pvalues.loc["ref_lag", j])})
        return pd.DataFrame(out)
    except Exception as e:  # noqa: BLE001
        return pd.DataFrame([{"outcome_vs_single": "ERROR", "ref_lag_coef": np.nan,
                              "ref_lag_p": np.nan, "note": str(e)[:120]}])


def compare_to_2b(est: pd.DataFrame) -> pd.DataFrame:
    """Place the individual-level β beside 2b's cell-level β (COL), matched spec×lag."""
    if not os.path.exists(STAGE2B_SUMMARY):
        return pd.DataFrame()
    b2 = pd.read_csv(STAGE2B_SUMMARY)
    b2 = b2[b2["country"] == "COL"].copy()
    # 2b spec names: peer_younger, peer_older, pop2039, own_lag. Map pop_all<->pop2039.
    name_map = {"peer_younger": "peer_younger", "peer_older": "peer_older",
                "pop_all": "pop2039"}
    rows = []
    ind = est[(est["with_1519"]) & (~est["educ"])]
    for _, r in ind.iterrows():
        b2name = name_map.get(r["spec"])
        m = b2[(b2["reference_spec"] == b2name) & (b2["lag"] == r["lag"])]
        cell_beta = float(m["beta"].iloc[0]) if len(m) else np.nan
        cell_amp = bool(m["amplifying"].iloc[0]) if len(m) else False
        rows.append({
            "spec": r["spec"], "role": r["role"], "lag": r["lag"],
            "indiv_beta": r["beta"], "indiv_p": r["pvalue"],
            "indiv_amplifying": r["amplifying"],
            "cell_beta_2b": cell_beta, "cell_amplifying_2b": cell_amp,
            "verdict": ("reveals amplifying" if r["amplifying"] and not cell_amp
                        else "confirms non-amplifying" if not r["amplifying"]
                        else "amplifying (both)"),
        })
    return pd.DataFrame(rows)


def classify_reading(est: pd.DataFrame, entry: pd.DataFrame) -> dict:
    """Apply instruction §4 pre-registered rule -> H_confirm / H_reopen / H_entry-margin.

    Anne 9a: H_confirm does NOT close (B); it downgrades to aggregation-cleared,
    pending the ENDS true-transition test (2c-ii).
    """
    primary = est[(est["spec"] == "peer_younger") & (est["with_1519"])
                  & (~est["educ"])]
    clean = est[(est["spec"] == "peer_older") & (est["with_1519"]) & (~est["educ"])]
    # robustness across the full reference-spec × lag grid (with 15-19, no educ)
    grid = est[(est["with_1519"]) & (~est["educ"])]
    amp_any = bool(grid["amplifying"].any())
    amp_robust = bool(grid["amplifying"].mean() >= 0.5) if len(grid) else False
    prim_amp = bool(primary["amplifying"].any())
    clean_amp = bool(clean["amplifying"].any())

    entry_amp = bool(entry[entry["test"] == "interaction"]["amplifying"].any()) or \
        bool(entry[entry["test"] == "1519_only"]["amplifying"].any())
    body_grid = est[(~est["with_1519"]) & (~est["educ"])]
    body_amp = bool(body_grid["amplifying"].any())

    if amp_robust and (prim_amp or clean_amp):
        reading = "H_reopen"
        ruling = ("(B) REOPENED for COL; reflexivity returns to Stage 3. The "
                  "ecological aggregation in 2b had masked an amplifying individual-"
                  "level dependence.")
    elif entry_amp and not body_amp:
        reading = "H_entry-margin"
        ruling = ("(B) PARTIALLY REOPENED for the 15-19 entry band only; cascade "
                  "ignites at entry and dissipates. The 20-39 floor was a blindfold "
                  "over the ignition zone. Flag for ENDS (2c-ii) confirmation.")
    else:
        reading = "H_confirm"
        ruling = ("(B) DEFERRED, AGGREGATION-CLEARED, pending ENDS — NOT closed "
                  "(Anne 9a). The individual-level status model does not reveal an "
                  "amplifying dependence the cell-level aggregation hid; the "
                  "aggregation concern (B7) is cleared. But a cascade is a process "
                  "in time, which only the ENDS true-transition test (2c-ii) "
                  "observes. Stage 3 sufficiency may proceed in parallel as a "
                  "no-reflexivity model.")
    return {"reading": reading, "ruling": ruling,
            "primary_amplifying": prim_amp, "clean_amplifying": clean_amp,
            "amplifying_any_spec": amp_any, "amplifying_robust": amp_robust,
            "entry_band_amplifying": entry_amp, "body_amplifying": body_amp}


# --------------------------------------------------------------------------- #
# Driver
# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--years", nargs="*", type=int,
                    default=list(range(2007, 2025)))
    ap.add_argument("--max-months", type=int, default=None,
                    help="cap months/year for a fast proxy build (PASS 1)")
    ap.add_argument("--rebuild", action="store_true",
                    help="force PASS 1 even if person_cells_COL.csv.gz exists")
    args = ap.parse_args()

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(ASSERT_LOG, "w") as fh:
        fh.write("# Stage 2c identification-wall assertion trail (assert_no_tfr)\n")

    # PASS 1 — person-cell cache
    cells = ensure_cells(args.years, args.max_months, args.rebuild)
    assert_no_tfr(cells, "person_cells")

    # Reference shares (band×year, incl 15-19)
    ref = reference_shares(cells)
    ref.to_csv(os.path.join(OUT_DIR, "ref_shares_COL.csv"), index=False)
    print("\n[2c PASS2] reference not-married shares by band×year:")
    print(ref.pivot(index="year", columns="age_band",
                    values="not_married").round(3).to_string())

    # PASS 2 — estimates across spec × lag × {with,without 15-19}; educ robustness
    rows = []
    for spec in REFERENCE_SPECS:
        for lag in LAGS:
            for inc in (True, False):
                rows.append(estimate_logit(cells, ref, spec, lag, inc))
    # education robustness (pre-2021 subsample), primary spec/lag, with 15-19
    cells_pre = cells[cells["year"] <= 2020].copy()
    ref_pre = reference_shares(cells_pre)
    rows.append(estimate_logit(cells_pre, ref_pre, "peer_younger", 1, True,
                               use_educ=True))
    est = pd.DataFrame(rows)
    est.insert(0, "country", "COL")
    est.to_csv(os.path.join(OUT_DIR, "stage2c_individual_estimates.csv"), index=False)

    entry = entry_margin_test(cells, ref)
    entry.to_csv(os.path.join(OUT_DIR, "stage2c_entry_margin_COL.csv"), index=False)

    mnl = multinomial_descriptive(cells, ref)
    mnl.to_csv(os.path.join(OUT_DIR, "stage2c_multinomial_COL.csv"), index=False)

    cmp = compare_to_2b(est)
    cmp.to_csv(os.path.join(OUT_DIR, "stage2c_vs_2b_beta.csv"), index=False)

    reading = classify_reading(est, entry)
    import json
    with open(os.path.join(OUT_DIR, "stage2c_reading.json"), "w") as fh:
        json.dump(reading, fh, indent=2)

    # Console read
    print("\n[2c] Individual-level β (married vs not; β<0 & p<.10 = amplifying):")
    show = ["spec", "role", "lag", "with_1519", "educ", "n_persons", "n_clusters",
            "beta", "se", "pvalue", "amplifying"]
    print(est[show].to_string(index=False))
    if not cmp.empty:
        print("\n[2c] Individual-level β vs 2b cell-level β (COL, with 15-19):")
        print(cmp.to_string(index=False))
    print("\n[2c] Entry-margin (15-19) probe:")
    print(entry.to_string(index=False))
    if not mnl.empty:
        print("\n[2c] Multinomial descriptive (vs single):")
        print(mnl.to_string(index=False))
    print(f"\n[2c] READING: {reading['reading']}")
    print(f"     {reading['ruling']}")
    print(f"\n[2c] artifacts -> {OUT_DIR}")


if __name__ == "__main__":
    main()
