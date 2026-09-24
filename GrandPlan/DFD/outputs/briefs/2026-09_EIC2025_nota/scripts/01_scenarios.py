"""
Step 1 of the EIC-2025 nota (v0.2): four fertility scenarios for Mexico, 2025-2050.

Build instructions:
  _crossrefs/_build_instructions/2026-09-23_DFD_nota-EIC2025_build-instruction.md (v0.1)
  _crossrefs/_build_instructions/2026-09-23_demographics_commit-endorsements_nota-v0.2.md (v0.2;
  rulings in _crossrefs/corpus/demographics/_pending/2026-09-23_nota-EIC2025-v0.1_Anne-Cath-review.md)
Inputs: ../data/*.csv, written by 00_prepare_inputs.py.

Two-sex cohort-component projection, single ages 0..99 + 100+, annual mid-year steps.
A brief-specific run; the corpus skeleton country/MEX/mex_scenarios_eic2025.py is untouched.

  Base      EIC 2025 private-dwelling age-sex structure (130,393,389) plus the 517,925
            complementary population at CPV 2020 non-household age-sex shares; 5-yr bands
            split to single years with CONAPO 2025 within-band proportions; reference moved
            from 15 Oct 2025 to 1 Jul 2025 by a pure time shift (v0.2, Anne §1 F1): each
            age-sex group is moved back 0.29 yr at its own annual rate of change under the
            observed 2025 components (TFR 1.23, net migration -229,840/yr, CONAPO 2025
            mortality). WPP enters nowhere in the base.
  Mortality CONAPO 2023 conciliación/proyección: m(x,s,t) = deaths / mid-year population.
  Migration -230 k/yr to 2030, linear taper to -135 k/yr by 2040, constant after (Central,
            INEGI directo); no taper (Estrés); WPP 2024 medium (Optimista). Age-sex profile:
            EIC 2025 emigrants by 5-yr age and sex (RR 37/26 Gráfica 9), in every scenario.
  Fertility CONAPO 2024 ASFR shape scaled to each scenario's TFR path.

Sensitivities (CSV only): base = CONAPO 65+ (ages 65+ of the base replaced by CONAPO's
mid-2025 single-age values; Anne §2), and base = WPP 2024 mid-2023 (projected 2023 -> 2025
on WPP TFR and migration, then the scenario paths).
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"
RESULTS = HERE.parent / "results"

A = 101                     # single ages 0..99 and the open group 100+
T0, T1 = 2025, 2050
SEXES = ("F", "M")

# EIC 2025 (Reporte de Resultados 37/26)
EIC_COMPLEMENTARY = 517_925
EIC_REF_DATE = 2025 + (pd.Timestamp("2025-10-15").dayofyear - 0.5) / 365.0
MID_2025 = 2025.5
EIC_TFR = 1.23
NET_MIG_EIC = -(1_300_000 - 150_800) / 5.0          # -229,840 per year, 2020-25 (lower bound)
NET_MIG_TAPER_END = -135_000.0                      # instruction value; midpoint of 107-161 k/yr is 134 k (CPV 2020, 2015-20)
NET_MIG_RANGE_2015_20 = (-107_000.0, -161_000.0)
MIG_MALE_SHARE = 0.704                              # RR 37/26 text; Gráfica 9 bars sum to 70.3
ASFR_SHAPE_YEAR = 2024
EIC_BANDS = [(5 * i, 5 * i + 4) for i in range(15)] + [(75, 100)]

SCENARIOS = [
    # key, name in the PDF
    ("optimista", "Optimista — ONU (variante media)"),
    ("central", "Central DFD"),
    ("inegi", "INEGI directo"),
    ("estres", "Estrés"),
]


# ------------------------------------------------------------------ inputs
def load():
    pop = pd.read_csv(DATA / "conapo2023_mex_pop_midyear.csv")
    dth = pd.read_csv(DATA / "conapo2023_mex_deaths.csv")
    for df in (pop, dth):
        df["age"] = df.age.clip(upper=A - 1)
    pop = pop.groupby(["year", "sex", "age"])["pop"].sum()
    dth = dth.groupby(["year", "sex", "age"])["deaths"].sum()
    asfr = pd.read_csv(DATA / "conapo2023_mex_asfr.csv")
    wpp = pd.read_csv(DATA / "wpp2024_mex_indicators_medium.csv").set_index("year")
    wpp23 = pd.read_csv(DATA / "wpp2024_mex_pop_single_age_2023.csv")
    eic = pd.read_csv(DATA / "eic2025_mex_private_by_band_sex.csv")
    cpv = pd.read_csv(DATA / "cpv2020_mex_nonhousehold_by_band_sex.csv")
    g9 = pd.read_csv(DATA / "eic2025_emigrants_age_sex_grafica9.csv")
    return pop, dth, asfr, wpp, wpp23, eic, cpv, g9


def vec(series_by_age) -> np.ndarray:
    v = np.zeros(A)
    for age, val in series_by_age.items():
        v[int(age)] += val
    return v


# --------------------------------------------------------------- mortality
def life_table_survival(m: np.ndarray, sex: str):
    """Single-decrement life table from m(x). Returns (S, s_birth, e0):
    S[x] carries age x at mid-year t to x+1 at t+1 (S[A-1] is the open group's
    retention, applied to 99 and 100+ together); s_birth = L0 / l0."""
    a = np.full(A, 0.5)
    if sex == "M":                                  # Coale-Demeny West a0
        a[0] = 0.045 + 2.684 * m[0] if m[0] < 0.107 else 0.330
    else:
        a[0] = 0.053 + 2.800 * m[0] if m[0] < 0.107 else 0.350
    q = np.minimum(m / (1 + (1 - a) * m), 1.0)
    q[-1] = 1.0
    l = np.ones(A)
    for x in range(1, A):
        l[x] = l[x - 1] * (1 - q[x - 1])
    d = l * q
    L = l - (1 - a) * d
    L[-1] = l[-1] / m[-1]
    T = L[::-1].cumsum()[::-1]
    S = np.zeros(A)
    S[:-2] = L[1:-1] / L[:-2]
    S[-2] = T[-1] / T[-2]          # 99 and 100+ -> 100+
    S[-1] = S[-2]
    return S, L[0], T[0]


def mortality(pop, dth):
    """Returns {(sex, year): (S, s_birth, e0)} for 2023..2050."""
    return {(s, y): life_table_survival(vec(dth.loc[(y, s)]) / vec(pop.loc[(y, s)]), s)
            for y in range(2023, T1 + 1) for s in SEXES}


# ---------------------------------------------------------------- fertility
def asfr_shape(asfr) -> np.ndarray:
    """Single-year ASFR for ages 0..100, CONAPO 2024 shape, normalised so that sum = 1 (TFR 1)."""
    f = np.zeros(A)
    for _, r in asfr[asfr.year == ASFR_SHAPE_YEAR].iterrows():
        lo, hi = (int(v) for v in r.age_group.split("-"))
        f[lo:hi + 1] = r.asfr_per_1000 / 1000.0
    return f / f.sum()


def tfr_path(key: str, wpp) -> dict[int, float]:
    yrs = range(2023, T1 + 1)
    if key == "optimista":
        return {y: float(wpp.loc[y, "TFR"]) for y in yrs}
    if key == "central":
        return {y: 1.50 for y in yrs}
    if key == "inegi":
        return {y: EIC_TFR for y in yrs}
    if key == "estres":
        return {y: max(0.90, round(1.50 - 0.10 * (y - 2025), 2)) if y >= 2025 else 1.50 for y in yrs}
    raise KeyError(key)


# ---------------------------------------------------------------- migration
def migration_path(key: str, wpp) -> dict[int, float]:
    out = {}
    for y in range(2023, T1 + 1):
        if key == "optimista":
            out[y] = float(wpp.loc[y, "NetMigrations"]) * 1000.0
        elif key == "estres" or y < 2030:
            out[y] = NET_MIG_EIC
        elif y < 2040:
            out[y] = NET_MIG_EIC + (NET_MIG_TAPER_END - NET_MIG_EIC) * (y - 2030) / 10.0
        else:
            out[y] = NET_MIG_TAPER_END
    return out


def migration_profile(g9) -> dict[str, np.ndarray]:
    """Share of the annual net flow by single age and sex (sums to 1 over both sexes):
    EIC 2025 emigrants by 5-yr age and sex (Gráfica 9), uniform within each band."""
    tot = g9.men_pct.sum() + g9.women_pct.sum()
    prof = {"M": np.zeros(A), "F": np.zeros(A)}
    for _, r in g9.iterrows():
        lo = int(r.band.split("-")[0].rstrip("+"))
        hi = lo + 4 if "-" in r.band else A - 1
        for s, col in (("M", "men_pct"), ("F", "women_pct")):
            prof[s][lo:hi + 1] = r[col] / tot / (hi - lo + 1)
    return prof


# --------------------------------------------------------------------- base
def split_bands(band_counts: dict[tuple[int, int], float], within: np.ndarray) -> np.ndarray:
    v = np.zeros(A)
    for (lo, hi), c in band_counts.items():
        w = within[lo:hi + 1]
        v[lo:hi + 1] = c * w / w.sum()
    return v


def band_of(label: str) -> tuple[int, int]:
    if label.endswith("YMAS"):
        return int(label[:-4]), 100
    lo, hi = label.split("A")
    return int(lo), int(hi)


def eic_oct2025(pop, eic, cpv):
    conapo25 = {s: vec(pop.loc[(2025, s)]) for s in SEXES}
    cpv = cpv.copy()
    cpv["lo"] = cpv.band.str[:2].astype(int)
    out = {}
    for s in SEXES:
        bands = {band_of(r.band): r["count"] for _, r in eic[eic.sex == s].iterrows()}
        for _, r in cpv[cpv.sex == s].iterrows():
            b = (75, 100) if r.lo >= 75 else (r.lo, r.lo + 4)
            bands[b] += EIC_COMPLEMENTARY * r.share_within_residual
        out[s] = split_bands(bands, conapo25[s])
    return out, conapo25


def time_shift(oct15, mort, fshape, prof, wpp):
    """Pure time shift, 15 Oct 2025 -> 1 Jul 2025: move each age-sex group back by dt at its
    own annual rate of change under the observed 2025 components."""
    dt = EIC_REF_DATE - MID_2025
    fwd, _ = step(oct15, 2025, EIC_TFR, NET_MIG_EIC, mort, fshape, prof, float(wpp.loc[2025, "SRB"]) / 100.0)
    out = {}
    for s in SEXES:
        g = np.where(oct15[s] > 0, fwd[s] / np.maximum(oct15[s], 1e-9), 1.0)
        out[s] = oct15[s] * g ** (-dt)
    return out, dt


def base_conapo65(p0, conapo25):
    return {s: np.concatenate([p0[s][:65], conapo25[s][65:]]) for s in SEXES}


def base_wpp23(wpp23):
    w = wpp23.set_index("age")
    return {"F": vec(w.PopFemale * 1000.0), "M": vec(w.PopMale * 1000.0)}


# ------------------------------------------------------------------ project
def step(p, y, tfr, net_mig, mort, fshape, prof, srb):
    """Mid-year y -> mid-year y+1. Rates for the step: average of calendar years y and y+1."""
    new = {}
    for s in SEXES:
        S = 0.5 * (mort[(s, y)][0] + mort[(s, y + 1)][0])
        q = np.zeros(A)
        q[1:] = p[s][:-1] * S[:-1]
        q[-1] += p[s][-1] * S[-1]
        new[s] = q
    women = 0.5 * (p["F"] + new["F"])
    births = float((fshape * tfr * women).sum())
    for s, share in (("F", 1 / (1 + srb)), ("M", srb / (1 + srb))):
        sb = 0.5 * (mort[(s, y)][1] + mort[(s, y + 1)][1])
        new[s][0] = births * share * sb
    for s in SEXES:
        new[s] = np.maximum(new[s] + net_mig * prof[s], 0.0)
    return new, births


def project(p0, y0, key, wpp, mort, fshape, prof, pre_paths=None):
    tfr, mig = tfr_path(key, wpp), migration_path(key, wpp)
    if pre_paths:                                  # WPP-base sensitivity: 2023-2025 on WPP paths
        tfr = {**tfr, **pre_paths[0]}
        mig = {**mig, **pre_paths[1]}
    p, traj, births = {s: v.copy() for s, v in p0.items()}, {y0: p0}, {}
    for y in range(y0, T1):
        srb = float(wpp.loc[y, "SRB"]) / 100.0
        p, b = step(p, y, 0.5 * (tfr[y] + tfr[y + 1]), 0.5 * (mig[y] + mig[y + 1]), mort, fshape, prof, srb)
        traj[y + 1], births[y] = p, b
    return traj, births, tfr, mig


# ------------------------------------------------------------------ outputs
def indicators(traj, births, tfr, mig):
    rows, prev_work = [], None
    for y in sorted(traj):
        if y < T0:
            continue
        F, M = traj[y]["F"], traj[y]["M"]
        t = F + M
        work = t[15:65].sum()
        rows.append({
            "year": y, "population": t.sum(), "pop_0_14": t[:15].sum(), "pop_6_14": t[6:15].sum(),
            "pop_15_64": work, "pop_65plus": t[65:].sum(), "pop_80plus": t[80:].sum(),
            "women_20_39": F[20:40].sum(),
            "tdr": 100 * (t[:15].sum() + t[65:].sum()) / work, "ydr": 100 * t[:15].sum() / work,
            "oadr": 100 * t[65:].sum() / work, "support_ratio": work / t[65:].sum(),
            "growth_15_64_pct": np.nan if prev_work is None else 100 * (work / prev_work - 1),
            "tfr": tfr[y], "net_migration": mig[y], "births_next_12m": births.get(y, np.nan),
        })
        prev_work = work
    return pd.DataFrame(rows)


def tdr_minimum(df):
    y, v = df.year.to_numpy(), df.tdr.to_numpy()
    i = int(np.argmin(v))
    if 0 < i < len(v) - 1:                         # parabola through the minimum and its neighbours
        a = 0.5 * (v[i - 1] + v[i + 1]) - v[i]
        b = 0.5 * (v[i + 1] - v[i - 1])
        yi, vi = (y[i] - b / (2 * a), v[i] - b * b / (4 * a)) if a > 0 else (float(y[i]), v[i])
    else:
        yi, vi = float(y[i]), v[i]
    within = df.year[df.tdr <= v[i] + 1.0]
    g = df[df.year % 5 == 0]
    j = int(np.argmin(g.tdr.to_numpy()))
    return {"tdr_min_year_annual": int(y[i]), "tdr_min_annual": v[i],
            "tdr_min_year_interp": yi, "tdr_min_interp": vi,
            "tdr_min_year_5yr_grid": int(g.year.iloc[j]), "tdr_min_5yr_grid": g.tdr.iloc[j],
            "span_within_1pt_start": int(within.min()), "span_within_1pt_end": int(within.max())}


def main():
    pop, dth, asfr, wpp, wpp23, eic, cpv, g9 = load()
    mort = mortality(pop, dth)
    fshape = asfr_shape(asfr)
    prof = migration_profile(g9)
    oct15, conapo25 = eic_oct2025(pop, eic, cpv)
    p0, dt = time_shift(oct15, mort, fshape, prof, wpp)
    p_c65 = base_conapo65(p0, conapo25)
    p23 = base_wpp23(wpp23)

    # ---- diagnostics: base and the 65+ gap
    t_oct = oct15["F"] + oct15["M"]
    t_mid = p0["F"] + p0["M"]
    t_con = conapo25["F"] + conapo25["M"]
    print(f"Base: EIC 15-Oct-2025 {t_oct.sum():,.0f} -> mid-2025 {t_mid.sum():,.0f} (pure time shift, dt = {dt:.3f} yr)")
    gate = []
    for lab, sl in (("0-14", slice(0, 15)), ("15-64", slice(15, 65)), ("65+", slice(65, A)), ("80+", slice(80, A))):
        e, m, c = t_oct[sl].sum(), t_mid[sl].sum(), t_con[sl].sum()
        gate.append({"group": lab, "eic_oct2025_incl_complementary": e, "base_mid2025": m,
                     "conapo2023_mid2025": c, "base_minus_conapo": m - c})
        print(f"      {lab:>6}: EIC {e/1e6:7.3f} M  base {m/1e6:7.3f} M  CONAPO {c/1e6:7.3f} M  gap {(m-c)/1e6:+.3f} M")
    tdr = lambda v: 100 * (v[:15].sum() + v[65:].sum()) / v[15:65].sum()
    print(f"      TDR: EIC-Oct {tdr(t_oct):.2f}  base-mid {tdr(t_mid):.2f}")
    e0 = {s: (mort[(s, 2025)][2], mort[(s, 2050)][2]) for s in SEXES}
    print(f"Life-table e0 from CONAPO rates: F {e0['F'][0]:.2f} -> {e0['F'][1]:.2f}, M {e0['M'][0]:.2f} -> {e0['M'][1]:.2f}")

    # ---- runs
    frames, minima = [], []
    pre = (tfr_path("optimista", wpp), migration_path("optimista", wpp))
    pre = ({y: pre[0][y] for y in (2023, 2024)}, {y: pre[1][y] for y in (2023, 2024)})
    for base_tag, start, y0, pre_paths in (("eic2025", p0, 2025, None),
                                           ("eic2025_conapo65_sensitivity", p_c65, 2025, None),
                                           ("wpp2023_sensitivity", p23, 2023, pre)):
        for key, name in SCENARIOS:
            traj, births, tfr, mig = project(start, y0, key, wpp, mort, fshape, prof, pre_paths)
            df = indicators(traj, births, tfr, mig)
            df.insert(0, "base", base_tag)
            df.insert(1, "scenario", key)
            df.insert(2, "scenario_name", name)
            frames.append(df)
            minima.append({"base": base_tag, "scenario": key, "scenario_name": name, **tdr_minimum(df),
                           "pop_2050": df.population.iloc[-1],
                           "first_year_15_64_declines": next((int(r.year) for r in df.itertuples()
                                                              if r.growth_15_64_pct < 0), None)})
    res = pd.concat(frames, ignore_index=True)
    mins = pd.DataFrame(minima)
    RESULTS.mkdir(exist_ok=True)
    res.round(4).to_csv(RESULTS / "scenarios_eic2025_brief.csv", index=False)
    mins.round(3).to_csv(RESULTS / "tdr_minima.csv", index=False)
    pd.DataFrame(gate).round(0).to_csv(RESULTS / "base_reconciliation_gate.csv", index=False)

    pd.set_option("display.width", 220)
    show = res[res.year.isin([2025, 2030, 2035, 2040, 2045, 2050])]
    for tag in ("eic2025", "eic2025_conapo65_sensitivity", "wpp2023_sensitivity"):
        print(f"\n== base: {tag} ==")
        for col, scale, lab in (("population", 1e6, "Population (M)"), ("tdr", 1, "TDR"), ("oadr", 1, "OADR")):
            s = show[show.base == tag].pivot(index="year", columns="scenario", values=col) / scale
            print(lab, "\n", s[[k for k, _ in SCENARIOS]].round(2).to_string())
    print("\n", mins.drop(columns="scenario_name").round(2).to_string())


if __name__ == "__main__":
    main()
