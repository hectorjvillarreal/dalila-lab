"""
65+ gate check (Anne record 2026-09-23, Appendix B §2 of
_crossrefs/_build_instructions/2026-09-23_demographics_commit-endorsements_nota-v0.2.md, Step 4).

Ages the CPV 2020 population (single years, by sex, at 15 Mar 2020) to 15 Oct 2025 with
CONAPO 2023 conciliación death rates (m = deaths / mid-year population, by single age,
sex and calendar year), subtracts EIC-measured emigration at those ages (Gráfica 9 of
RR 37/26), and compares with EIC 2025 at 15 Oct 2025 (private dwellings + the 517,925
complementary population at CPV 2020 non-household shares).

Inputs live with the nota build (GrandPlan/DFD/outputs/briefs/2026-09_EIC2025_nota/data/),
provenance and sha256 in that folder's README.md. Output: printed tables + CSV beside this file.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
NOTA = HERE.parents[4] / "GrandPlan/DFD/outputs/briefs/2026-09_EIC2025_nota"
DATA = NOTA / "data"

T0 = 2020 + (pd.Timestamp("2020-03-15").dayofyear - 0.5) / 365.0     # CPV 2020 reference date
T1 = 2025 + (pd.Timestamp("2025-10-15").dayofyear - 0.5) / 365.0     # EIC 2025 reference date
EMIGRANTS = 1_300_000                                                  # Oct 2020 - Oct 2025, RR 37/26
COMPLEMENTARY = 517_925
A = 110
STEPS_PER_YEAR = 12
GROUPS = [("65-69", 65, 70), ("70-74", 70, 75), ("75+", 75, A), ("65+", 65, A)]
SEXES = {"M": "Hombres", "F": "Mujeres"}


def cpv_single_age():
    d = pd.read_excel(DATA / "raw/cpv2020_b_eum_01_poblacion.xlsx", sheet_name="03", header=None)
    d = d[d[0] == "Estados Unidos Mexicanos"].iloc[:, [1, 3, 4]]
    d.columns = ["age", "M", "F"]
    d = d[d.age != "Total"]
    unspecified = d[d.age == "No especificado"][["M", "F"]].astype(float).iloc[0]
    d = d[d.age != "No especificado"].copy()
    d["age"] = d.age.str.extract(r"(\d+)").astype(int)
    out = {}
    for s in ("M", "F"):
        v = np.zeros(A)
        for a, n in zip(d.age, d[s].astype(float)):
            v[min(a, A - 1)] += n
        out[s] = {"reported": v, "prorated": v * (1 + unspecified[s] / v.sum())}
    return out, unspecified


def conapo_rates():
    pop = pd.read_csv(DATA / "conapo2023_mex_pop_midyear.csv")
    dth = pd.read_csv(DATA / "conapo2023_mex_deaths.csv")
    m = dth.merge(pop, on=["year", "age", "sex"])
    m["m"] = m.deaths / m["pop"]
    return {(r.sex, r.year, r.age): r.m for r in m.itertuples()}, pop


def age_forward(v0: np.ndarray, sex: str, rates) -> np.ndarray:
    """Cohort at exact age a+0.5 on T0, survived to T1, redistributed to single ages at T1."""
    dur = T1 - T0
    n = int(round(dur * STEPS_PER_YEAR))
    dt = dur / n
    out = np.zeros(A + 8)
    for a in range(A):
        if v0[a] == 0:
            continue
        surv = 1.0
        for k in range(n):
            t = T0 + (k + 0.5) * dt
            age = min(int(a + 0.5 + (t - T0)), A - 1)
            surv *= np.exp(-rates[(sex, int(t), age)] * dt)
        lo = a + dur                                     # cohort now spans [a+dur, a+1+dur)
        w_hi = lo - np.floor(lo)
        out[int(np.floor(lo))] += v0[a] * surv * (1 - w_hi)
        out[int(np.floor(lo)) + 1] += v0[a] * surv * w_hi
    return out[:A] + np.r_[np.zeros(A - 1), out[A:].sum()]


def eic_groups():
    eic = pd.read_csv(DATA / "eic2025_mex_private_by_band_sex.csv")
    cpv = pd.read_csv(DATA / "cpv2020_mex_nonhousehold_by_band_sex.csv")
    cpv["lo"] = cpv.band.str[:2].astype(int)
    out = {}
    for s in ("M", "F"):
        e = eic[eic.sex == s].set_index("band")["count"]
        c = cpv[cpv.sex == s]
        comp = {g: COMPLEMENTARY * c[(c.lo >= lo) & (c.lo < hi)].share_within_residual.sum() for g, lo, hi in GROUPS}
        out[s] = {"65-69": e["65A69"] + comp["65-69"], "70-74": e["70A74"] + comp["70-74"],
                  "75+": e["75YMAS"] + comp["75+"]}
        out[s]["65+"] = out[s]["65-69"] + out[s]["70-74"] + out[s]["75+"]
    return out


def emigrants_groups():
    g9 = pd.read_csv(DATA / "eic2025_emigrants_age_sex_grafica9.csv")
    g9["lo"] = g9.band.str.extract(r"(\d+)").astype(int)
    out = {}
    for s, col in (("M", "men_pct"), ("F", "women_pct")):
        e = {g: EMIGRANTS * g9[(g9.lo >= lo) & (g9.lo < hi)][col].sum() / 100 for g, lo, hi in GROUPS}
        out[s] = e
    return out


def main():
    cpv, unspecified = cpv_single_age()
    rates, pop = conapo_rates()
    eic = eic_groups()
    emi = emigrants_groups()
    rows = []
    for variant in ("prorated", "reported"):
        for s in ("M", "F"):
            aged = age_forward(cpv[s][variant], s, rates)
            for g, lo, hi in GROUPS:
                a = aged[lo:hi].sum() - emi[s][g]
                rows.append({"variant": variant, "sex": s, "group": g, "cpv2020_aged_net": a, "eic2025": eic[s][g],
                             "eic_minus_aged": eic[s][g] - a, "pct": 100 * (eic[s][g] - a) / a,
                             "emigrants_subtracted": emi[s][g]})
    df = pd.DataFrame(rows)
    tot = df.groupby(["variant", "group"])[["cpv2020_aged_net", "eic2025", "eic_minus_aged", "emigrants_subtracted"]].sum().reset_index()
    tot["sex"] = "T"
    tot["pct"] = 100 * tot.eic_minus_aged / tot.cpv2020_aged_net
    df = pd.concat([df, tot], ignore_index=True)
    df.round(1).to_csv(HERE / "eic2025_65plus_check.csv", index=False)

    # context: CONAPO vs CPV in 2020, CONAPO 2025
    c = pop.groupby(["year", "sex"]).apply(lambda g: g[g.age >= 65]["pop"].sum())
    cpv65_2020 = {s: cpv[s]["prorated"][65:].sum() for s in ("M", "F")}
    ctx = {"cpv2020_65plus_mar2020_prorated": sum(cpv65_2020.values()),
           "conapo_65plus_mid2020": c.loc[2020].sum(),
           "conapo_65plus_mid2025": c.loc[2025].sum(), "conapo_65plus_mid2026": c.loc[2026].sum(),
           "cpv_unspecified_age": unspecified.sum()}
    # deaths CONAPO attributes to the cohorts that reach 65+ by T1 (mortality-sensitivity lever)
    zero = {k: 0.0 for k in rates}
    ctx["cohort_deaths_to_65plus_2020_2025"] = sum(
        age_forward(cpv[s]["prorated"], s, zero)[65:].sum() - age_forward(cpv[s]["prorated"], s, rates)[65:].sum()
        for s in ("M", "F"))
    ctx["conapo_deaths_2020"] = 1_194_524
    pd.Series(ctx).round(0).to_csv(HERE / "eic2025_65plus_check_context.csv", header=["value"])
    pd.set_option("display.width", 200)
    print(df[df.variant == "prorated"].round(1).to_string(index=False))
    print(df[(df.variant == "reported") & (df.sex == "T")].round(1).to_string(index=False))
    print(pd.Series(ctx).round(0).to_string())


if __name__ == "__main__":
    main()
