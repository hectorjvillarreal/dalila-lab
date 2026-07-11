#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
stage2b_b6_repro_diff.py — Stage 2b condition B6 (band/base reproduction diff)

================================ PROTO-RAG-001 ================================
Purpose
    Anne B6: prove the Stage 2b composition reproduces the Stage 1.5 coupling
    identification series on overlapping (year, band) cells — same bands, same
    base, no accidental transformation. Mismatch beyond tolerance HALTS (raises),
    so this is a gate, not a report. Also logs the 20-39 base limitation.

Inputs
    outputs/stage2b/composition_panel_{CC}.csv   (Task A output; run apc script first)
    ../data/coupling/{CC}_coupling_annual.csv     (Stage 1.5 coupling series = source)

Outputs (outputs/stage2b/)
    b6_repro_diff_{CC}.csv   per-cell residuals (married, cohabiting, union_total).
    b6_repro_summary.csv     pass/fail + max residual per country & field.

Assumptions
    - Stage 1.5 series columns: year, age_band, married, cohabiting, union_total
      (fractions 0-1). 2b panel columns: share_married, share_cohab.
    - Direct-copy fields (married, cohabiting) must match to TOL_EXACT — they are
      read from the same source, so any gap signals a transformation bug.
    - union_total is reconstructed as share_married + share_cohab and compared to
      the source union_total with TOL_ROUND (source rounds each field to 4 dp
      independently, so the reconstruction carries up to ~1e-3 rounding noise).
    - Base limitation (logged, not an error): the 20-39 floor EXCLUDES the 15-19
      entry margin — the cascade vanguard — and is what leaves peer_younger
      undefined for the youngest band in Task C.

Dependencies
    python>=3.12, pandas, numpy. CPU-only.

Identification wall
    No TFR is read; only the coupling composition series and the 2b panel.
==============================================================================
"""
from __future__ import annotations

import os
import sys
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "outputs", "stage2b")
DATA_DIR = os.path.normpath(os.path.join(HERE, "..", "data", "coupling"))
PRIMARY = ("CRI", "COL")
SOURCE = {c: f"{c}_coupling_annual.csv" for c in PRIMARY}

TOL_EXACT = 1e-6   # direct-copy fields (married, cohabiting)
TOL_ROUND = 2e-3   # reconstructed union_total (independent 4-dp rounding in source)
BASE_NOTE = ("20-39 base EXCLUDES the 15-19 entry margin (cascade vanguard); this is "
             "also what leaves peer_younger undefined for the youngest band in Task C.")


def diff_country(country: str) -> dict:
    panel = pd.read_csv(os.path.join(OUT_DIR, f"composition_panel_{country}.csv"))
    src = pd.read_csv(os.path.join(DATA_DIR, SOURCE[country]))
    src = src[src["age_band"].isin(panel["age_band"].unique())]

    m = panel.merge(src[["year", "age_band", "married", "cohabiting", "union_total"]],
                    on=["year", "age_band"], how="inner", validate="one_to_one")
    m["resid_married"] = (m["share_married"] - m["married"]).abs()
    m["resid_cohab"] = (m["share_cohab"] - m["cohabiting"]).abs()
    m["resid_union"] = ((m["share_married"] + m["share_cohab"]) - m["union_total"]).abs()
    m[["country", "year", "age_band", "resid_married", "resid_cohab", "resid_union"]] \
        .to_csv(os.path.join(OUT_DIR, f"b6_repro_diff_{country}.csv"), index=False)

    max_m, max_c, max_u = (float(m["resid_married"].max()),
                           float(m["resid_cohab"].max()),
                           float(m["resid_union"].max()))
    ok = (max_m <= TOL_EXACT) and (max_c <= TOL_EXACT) and (max_u <= TOL_ROUND)
    return {"country": country, "n_cells": int(len(m)),
            "max_resid_married": max_m, "max_resid_cohab": max_c,
            "max_resid_union": max_u, "tol_exact": TOL_EXACT,
            "tol_round": TOL_ROUND, "pass": bool(ok)}


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    rows = []
    for country in PRIMARY:
        if not os.path.exists(os.path.join(OUT_DIR, f"composition_panel_{country}.csv")):
            print(f"[B6] {country}: SKIP — run stage2b_apc_composition.py first.")
            continue
        rows.append(diff_country(country))
    if not rows:
        print("[B6] nothing to check.")
        return
    summ = pd.DataFrame(rows)
    summ["base_limitation"] = BASE_NOTE
    summ.to_csv(os.path.join(OUT_DIR, "b6_repro_summary.csv"), index=False)
    print("[B6] reproduction diff vs Stage 1.5 coupling series:")
    print(summ.drop(columns="base_limitation").to_string(index=False))
    print(f"[B6] base limitation logged: {BASE_NOTE}")

    if not summ["pass"].all():
        failed = summ.loc[~summ["pass"], "country"].tolist()
        raise SystemExit(f"[B6] HALT — reproduction mismatch beyond tolerance: {failed}")
    print("[B6] PASS — 2b composition reproduces Stage 1.5 on all overlapping cells.")


if __name__ == "__main__":
    main()
