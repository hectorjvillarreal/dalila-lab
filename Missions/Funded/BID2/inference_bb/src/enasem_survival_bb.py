#!/usr/bin/env python3
"""Bayesian bootstrap of the two ENASEM survival targets (Draft-November, tab:targeted_moments).

    python -I src/enasem_survival_bb.py [--reps 4000] [--seed 20261108]

Sample: respondents interviewed alive in ENASEM 2018 (TIPENT_18 in 1-4), aged 50-64 in 2018,
with vital status observed in the 2021 master follow-up (FALLECIDO_21: 0 alive, 1-2 died).
Education from the 2018 constructed file (EDU_GRU: 4 = 10+ years of schooling = high).
Three-year survival p3 = 1 - weighted death share; five-year p5 = p3^(5/3).
Weights FACTORI_18; cluster UPM_DIS (2018 design). Draft SEs for the normal comparison:
0.004 (low), 0.006 (high).

This is a different wave pair from the draft (harmonized 2012-2021), so levels are not
expected to reproduce the targets; the interval width is the quantity of interest.
"""
import argparse
import glob
import json
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bb  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(os.path.dirname(ROOT), "motivation", "data", "enasem")
DRAFT = {"low": {"target": 0.951, "se": 0.004, "model": 0.995}, "high": {"target": 0.972, "se": 0.006, "model": 0.998}}


def load():
    m = pd.read_csv(glob.glob(os.path.join(DATA, "2021", "*master_follow_up*", "conjunto_de_datos", "*.csv"))[0],
                    usecols=["CUNICAH", "NP", "TIPENT_18", "FACTORI_18", "AGE_18", "FALLECIDO_21"], low_memory=False)
    c = pd.read_csv(glob.glob(os.path.join(DATA, "2018", "*variables_creadas*", "conjunto_de_datos", "*.csv"))[0],
                    usecols=["CUNICAH", "NP", "EDUCACION", "EDU_GRU", "UPM_DIS", "EST_DIS"], low_memory=False)
    for df in (m, c):
        for col in df.columns:
            if col not in ("CUNICAH", "NP"):
                df[col] = pd.to_numeric(df[col], errors="coerce")
    d = m.merge(c, on=["CUNICAH", "NP"], how="inner")
    d = d[d.TIPENT_18.isin([1, 2, 3, 4]) & d.AGE_18.between(50, 64) & d.FALLECIDO_21.notna() & d.EDU_GRU.notna()].copy()
    d["dead"] = d.FALLECIDO_21.isin([1, 2]).astype(float)
    return d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reps", type=int, default=4000)
    ap.add_argument("--seed", type=int, default=20261108)
    ap.add_argument("--high", default="edu_gru4", choices=["edu_gru4", "edu_gru3plus", "years12plus"])
    a = ap.parse_args()
    d = load()
    hi = {"edu_gru4": d.EDU_GRU == 4, "edu_gru3plus": d.EDU_GRU >= 3, "years12plus": d.EDUCACION >= 12}[a.high].values
    codes = bb.cluster_codes(d.UPM_DIS.values)
    base = d.FACTORI_18.values.astype(float)
    dead = d.dead.values
    rng = np.random.default_rng(a.seed)

    def p5(w, mask):
        p3 = 1 - (w * dead * mask).sum() / (w * mask).sum()
        return p3 ** (5 / 3)

    groups = {"low": ~hi, "high": hi}
    point = {k: p5(base, v) for k, v in groups.items()}
    draws = {k: np.empty(a.reps) for k in groups}
    for r, w in enumerate(bb.replicate_weights(rng, codes, base, a.reps)):
        for k, v in groups.items():
            draws[k][r] = p5(w, v)
    res = {"seed": a.seed, "replicates": a.reps, "high_definition": a.high, "wave_pair": "2018 -> 2021 (3 years, converted to 5)",
           "n": {k: int(v.sum()) for k, v in groups.items()}, "deaths": {k: int(dead[v].sum()) for k, v in groups.items()},
           "clusters": int(codes.max() + 1), "moments": {}}
    for k in groups:
        s = bb.summarize(draws[k], point[k], DRAFT[k]["se"])
        s["draft_target"] = DRAFT[k]["target"]
        s["draft_model"] = DRAFT[k]["model"]
        s["model_in_ci95"] = bool(s["ci95"][0] <= DRAFT[k]["model"] <= s["ci95"][1])
        res["moments"][f"surv5_{k}"] = s
    gap = draws["high"] - draws["low"]
    res["moments"]["surv5_gap_high_minus_low"] = bb.summarize(gap, point["high"] - point["low"])
    res["moments"]["surv5_gap_high_minus_low"]["draft_gap"] = round(DRAFT["high"]["target"] - DRAFT["low"]["target"], 4)
    pd.DataFrame({"surv5_low": draws["low"], "surv5_high": draws["high"]}).to_csv(os.path.join(ROOT, "outputs", "enasem_survival_bb_draws.csv"), index=False)
    json.dump(res, open(os.path.join(ROOT, "outputs", "enasem_survival_bb.json"), "w"), indent=1)
    for k, s in res["moments"].items():
        print(f"{k:28s} point {s['point']:.4f}  ci95 {s['ci95']}  sd {s['sd']:.4f}" + (f"  draft se {s['normal']['se']}  pp {s['normal']['pp_distance']}" if "normal" in s else ""))
    print("n", res["n"], "deaths", res["deaths"], "clusters", res["clusters"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
