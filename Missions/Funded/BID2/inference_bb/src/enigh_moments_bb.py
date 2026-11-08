#!/usr/bin/env python3
"""Bayesian bootstrap of the seven ENIGH targets of Draft-November (tab:targeted_moments).

    python -I src/enigh_moments_bb.py [--reps 2000] [--seed 20261108] [--high prepa|prof]

Data: ENIGH nueva serie 2016 and 2018 (pooled, as in the draft), tables concentradohogar,
poblacion, ingresos, under ../motivation/data/enigh/<year>/. Definitions follow the draft's
Measurement paragraph; where it is silent the choice is recorded in DEFINITIONS below and
was selected to reproduce the draft's point targets.

Bootstrap: one Exp(1) weight per primary sampling unit (wave x upm), multiplied into the
expansion factor; households and persons of the same UPM share the draw. Each replicate
recomputes all seven moments jointly, so the output is a joint posterior sample.
"""
import argparse
import json
import os
import sys
import time

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bb  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(os.path.dirname(ROOT), "motivation", "data", "enigh")
FILES = {
    2016: {"con": "2016/bundle_concentradohogar/concentradohogar.csv", "pob": "2016/bundle_poblacion/poblacion.csv",
           "inc": "2016/bundle_ingresos/ingresos.csv"},
    2018: {"con": "2018/concentradohogar.csv", "pob": "2018/poblacion.csv",
           "inc": "2018/bundle/conjunto_de_datos_ingresos_enigh_2018_ns/conjunto_de_datos/conjunto_de_datos_ingresos_enigh_2018_ns.csv"},
}
_R = lambda a, b: [f"P{i:03d}" for i in range(a, b + 1)]
LABOR_CLAVES = _R(1, 9) + _R(11, 16) + _R(18, 20) + ["P022"] + _R(67, 81)
DEFINITIONS = {
    "unit": "household (concentradohogar), age = age of head; persons (poblacion + ingresos) for the skill premium",
    "shares": "expansion-weighted mean of salud/gasto_mon over households with gasto_mon > 0, head aged 25-34, 50-64, 65-79",
    "logslope": "OLS slope of log(weighted mean salud by five-year age band of head) on band index, bands 25-29 ... 75-79",
    "elasticity_pooled": "PPML of salud (levels, quarterly) on log ingtrab + 2018 dummy; heads 25-64 with ingtrab > 0; zeros kept",
    "elasticity_within_age": "same PPML by five-year band of head (25-29 ... 60-64); coefficients averaged with band expansion-weight totals",
    "skill_premium": "WLS of log person labor income on high-education dummy + 2018 dummy; household members (parentesco not 4xx/7xx) aged 25-34 with positive labor income; labor income = ing_tri over claves " + ",".join(LABOR_CLAVES[:3]) + "... (P001-P009, P011-P016, P018-P020, P022, P067-P081)",
    "high_education": {"prepa": "nivelaprob >= 4 (upper secondary or more)", "prof": "nivelaprob >= 7 (university or more)"},
    "clusters": "wave x upm (ENIGH primary sampling unit); est_dis not used (Bayesian bootstrap ignores stratification; conservative)",
}
DRAFT = {  # tab:targeted_moments and tab:moment_match_md, Draft-November.tex (2026-11-07)
    "elas_pooled":  {"target": 0.575,  "se": 0.029,  "model": 0.724},
    "elas_within":  {"target": 0.573,  "se": 0.029,  "model": 0.831},
    "share_25_34":  {"target": 0.0182, "se": 0.0004, "model": 0.0211},
    "share_50_64":  {"target": 0.0231, "se": 0.0004, "model": 0.0225},
    "share_65_79":  {"target": 0.0332, "se": 0.0009, "model": 0.0203},
    "logslope":     {"target": 0.0675, "se": 0.0082, "model": 0.0885},
    "skill_prem":   {"target": 0.659,  "se": 0.013,  "model": 0.717},
}
ORDER = list(DRAFT)


def load(high):
    hh, pp = [], []
    for y, f in FILES.items():
        con = pd.read_csv(os.path.join(DATA, f["con"]), usecols=["folioviv", "foliohog", "factor", "upm", "edad_jefe", "ingtrab", "gasto_mon", "salud"], low_memory=False)
        con["wave"] = y
        pob = pd.read_csv(os.path.join(DATA, f["pob"]), usecols=["folioviv", "foliohog", "numren", "parentesco", "edad", "nivelaprob"], low_memory=False)
        inc = pd.read_csv(os.path.join(DATA, f["inc"]), usecols=["folioviv", "foliohog", "numren", "clave", "ing_tri"], low_memory=False)
        pob["parentesco"] = pd.to_numeric(pob.parentesco, errors="coerce")
        pob["nivelaprob"] = pd.to_numeric(pob.nivelaprob, errors="coerce")
        pob = pob[~pob.parentesco.between(400, 499) & ~pob.parentesco.between(700, 799)]
        lab = inc[inc.clave.isin(LABOR_CLAVES)].groupby(["folioviv", "foliohog", "numren"], as_index=False).ing_tri.sum().rename(columns={"ing_tri": "ylab"})
        per = pob.merge(lab, on=["folioviv", "foliohog", "numren"], how="inner").merge(con[["folioviv", "foliohog", "factor", "upm"]], on=["folioviv", "foliohog"], how="inner")
        per = per[per.edad.between(25, 34) & (per.ylab > 0) & per.nivelaprob.notna()].copy()
        per["wave"] = y
        hh.append(con)
        pp.append(per)
    hh, pp = pd.concat(hh, ignore_index=True), pd.concat(pp, ignore_index=True)
    hh["cl"] = hh.wave.astype(str) + "_" + hh.upm.astype(str)
    pp["cl"] = pp.wave.astype(str) + "_" + pp.upm.astype(str)
    labels = np.unique(np.concatenate([hh.cl.values, pp.cl.values]))
    hh["code"] = np.searchsorted(labels, hh.cl.values)
    pp["code"] = np.searchsorted(labels, pp.cl.values)
    pp["high"] = (pp.nivelaprob >= (4 if high == "prepa" else 7)).astype(float)
    return hh, pp, len(labels)


def ppml(y, X, w, tol=1e-9, maxit=50):
    """Weighted Poisson pseudo-maximum likelihood by Newton's method (small design)."""
    b = np.zeros(X.shape[1])
    b[0] = np.log(np.average(y, weights=w))
    for _ in range(maxit):
        mu = np.exp(X @ b)
        g = X.T @ (w * (y - mu))
        H = X.T @ (X * (w * mu)[:, None])
        step = np.linalg.solve(H, g)
        b += step
        if np.abs(step).max() < tol:
            break
    return b


class Moments:
    def __init__(self, hh, pp):
        self.hh_pos = hh[hh.gasto_mon > 0].reset_index(drop=True)
        self.ratio = (self.hh_pos.salud / self.hh_pos.gasto_mon).values
        self.age = self.hh_pos.edad_jefe.values
        self.salud = self.hh_pos.salud.values
        self.masks = {k: (self.age >= lo) & (self.age <= hi) for k, (lo, hi) in {"share_25_34": (25, 34), "share_50_64": (50, 64), "share_65_79": (65, 79)}.items()}
        band = (self.age - 25) // 5
        self.slope_bands = [(band == b) for b in range(11)]  # 25-29 ... 75-79
        self.slope_x = np.arange(11, dtype=float)
        el = hh[hh.edad_jefe.between(25, 64) & (hh.ingtrab > 0)].reset_index(drop=True)
        self.el_y = el.salud.values.astype(float)
        self.el_X = np.column_stack([np.ones(len(el)), np.log(el.ingtrab.values), (el.wave.values == 2018).astype(float)])
        self.el_code = el.code.values
        self.el_band = ((el.edad_jefe.values - 25) // 5)
        self.hh_code = self.hh_pos.code.values
        self.sp_y = np.log(pp.ylab.values)
        self.sp_X = np.column_stack([np.ones(len(pp)), pp.high.values, (pp.wave.values == 2018).astype(float)])
        self.sp_code = pp.code.values
        self.base = {"hh": self.hh_pos.factor.values.astype(float), "el": el.factor.values.astype(float), "sp": pp.factor.values.astype(float)}

    def compute(self, draw):
        """draw: Exp(1) per cluster (or ones for the point estimate)."""
        w_hh = self.base["hh"] * draw[self.hh_code]
        w_el = self.base["el"] * draw[self.el_code]
        w_sp = self.base["sp"] * draw[self.sp_code]
        out = {}
        for k, m in self.masks.items():
            out[k] = np.average(self.ratio[m], weights=w_hh[m])
        means = np.array([np.average(self.salud[m], weights=w_hh[m]) for m in self.slope_bands])
        out["logslope"] = np.polyfit(self.slope_x, np.log(means), 1)[0]
        out["elas_pooled"] = ppml(self.el_y, self.el_X, w_el)[1]
        co, wt = [], []
        for b in range(8):
            m = self.el_band == b
            co.append(ppml(self.el_y[m], self.el_X[m], w_el[m])[1])
            wt.append(w_el[m].sum())
        out["elas_within"] = np.average(co, weights=wt)
        XtW = self.sp_X.T * w_sp
        out["skill_prem"] = np.linalg.solve(XtW @ self.sp_X, XtW @ self.sp_y)[1]
        return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reps", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=20261108)
    ap.add_argument("--high", default="prepa", choices=["prepa", "prof"])
    a = ap.parse_args()
    t0 = time.time()
    hh, pp, G = load(a.high)
    M = Moments(hh, pp)
    point = M.compute(np.ones(G))
    print("point:", {k: round(v, 4) for k, v in point.items()}, f"[{time.time()-t0:.0f}s]", flush=True)
    rng = np.random.default_rng(a.seed)
    draws = np.empty((a.reps, len(ORDER)))
    for r in range(a.reps):
        m = M.compute(rng.exponential(size=G))
        draws[r] = [m[k] for k in ORDER]
        if (r + 1) % 200 == 0:
            print(f"  {r+1}/{a.reps} replicates [{time.time()-t0:.0f}s]", flush=True)
    os.makedirs(os.path.join(ROOT, "outputs"), exist_ok=True)
    pd.DataFrame(draws, columns=ORDER).to_csv(os.path.join(ROOT, "outputs", "enigh_moments_bb_draws.csv"), index=False)
    res = {"seed": a.seed, "replicates": a.reps, "high_education": DEFINITIONS["high_education"][a.high], "definitions": DEFINITIONS,
           "n": {"households_pooled": int(len(hh)), "households_gasto_pos": int(len(M.hh_pos)), "elasticity_sample": int(len(M.el_y)),
                 "skill_premium_persons": int(len(M.sp_y)), "clusters": int(G)}, "moments": {}}
    for j, k in enumerate(ORDER):
        s = bb.summarize(draws[:, j], point[k], DRAFT[k]["se"])
        s.update({"draft_target": DRAFT[k]["target"], "draft_model": DRAFT[k]["model"],
                  "reproduction_gap": round(point[k] - DRAFT[k]["target"], 4),
                  "model_in_ci95": bool(s["ci95"][0] <= DRAFT[k]["model"] <= s["ci95"][1]),
                  "model_tail_prob": bb.tail_prob(draws[:, j], DRAFT[k]["model"])})
        res["moments"][k] = s
    res["joint"] = bb.mahalanobis_check(draws, np.array([DRAFT[k]["model"] for k in ORDER]))
    res["joint"]["note"] = "model moment vector (tab:moment_match_md) against the joint replicate cloud of the seven ENIGH moments"
    res["corr"] = pd.DataFrame(draws, columns=ORDER).corr().round(3).to_dict()
    res["seconds"] = round(time.time() - t0)
    json.dump(res, open(os.path.join(ROOT, "outputs", "enigh_moments_bb.json"), "w"), indent=1)
    for k in ORDER:
        s = res["moments"][k]
        print(f"{k:12s} point {s['point']:.4f} (draft {s['draft_target']})  ci95 {s['ci95']}  sd {s['sd']:.4f} vs se {s['normal']['se']}  pp {s['normal']['pp_distance']}  model {s['draft_model']} in CI: {s['model_in_ci95']}  tail {s['model_tail_prob']}")
    print("joint:", res["joint"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
