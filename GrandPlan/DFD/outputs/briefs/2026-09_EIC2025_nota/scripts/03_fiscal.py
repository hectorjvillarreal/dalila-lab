"""
Step 3 of the EIC-2025 nota (v0.2): reduced-form fiscal indicators. Arithmetic on
results/scenarios_eic2025_brief.csv; IM-6 is not re-run (review record §3.5).

  τ_t = ρ · OADR_t / e     (review record §3.3: stylised PAYG in which beneficiary and
                            contributor coverage are equal in steady state, so coverage cancels)
  ρ = 0.50  IM-6 κ_rep, Missions/Funded/BID2/GE-now with Gender/ge_model_gender.jl:61 (commit 5368693);
            retirement j_R = 10 = age 65 (same file, line 50)
  e         employment / population at 15-64, INEGI ENOE 2026-Q2 microdata (data/enoe2026q2_employment_rate.csv),
            held constant

Writes results/fiscal_indicators.csv (long: base, indicator, scenario, period, value, unit).
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
RESULTS = HERE.parent / "results"
DATA = HERE.parent / "data"

RHO = 0.50
Q3_CENTRAL_MIN, Q3_CENTRAL_MIN_YEAR = 42.0, 2038
LOCKED_6_14_YEAR = 2031      # last year in which every 6-14 child was born before mid-2025
TAU_YEARS = (2025, 2035, 2050)


def employment_rate() -> float:
    e = pd.read_csv(DATA / "enoe2026q2_employment_rate.csv", index_col=0)["value"]
    return float(e["e_15_64"])


def main():
    e = employment_rate()
    res = pd.read_csv(RESULTS / "scenarios_eic2025_brief.csv")
    mins = pd.read_csv(RESULTS / "tdr_minima.csv").set_index(["base", "scenario"])
    rows = []

    def add(base, ind, sc, period, value, unit):
        rows.append({"base": base, "indicator": ind, "scenario": sc, "period": str(period), "value": value, "unit": unit})

    for (base, sc), g in res[res.base != "wpp2023_sensitivity"].groupby(["base", "scenario"]):
        g = g.set_index("year")
        m = mins.loc[(base, sc)]
        add(base, "tdr_min_year", sc, "", int(m.tdr_min_year_annual), "year")
        add(base, "tdr_min", sc, "", float(m.tdr_min_annual), "per 100 aged 15-64")
        add(base, "span_1pt_start", sc, "", int(m.span_within_1pt_start), "year")
        add(base, "span_1pt_end", sc, "", int(m.span_within_1pt_end), "year")
        for yr in (2025, 2035, 2050):
            add(base, "oadr", sc, yr, g.loc[yr, "oadr"], "per 100 aged 15-64")
            add(base, "tdr", sc, yr, g.loc[yr, "tdr"], "per 100 aged 15-64")
            add(base, "ydr", sc, yr, g.loc[yr, "ydr"], "per 100 aged 15-64")
        for yr in TAU_YEARS:
            add(base, "tau_payg", sc, yr, 100 * RHO * g.loc[yr, "oadr"] / 100 / e, "% of wage bill")
        for yr in (2025, LOCKED_6_14_YEAR, 2035, 2050):
            add(base, "pop_6_14", sc, yr, g.loc[yr, "pop_6_14"], "persons")
            add(base, "pop_6_14_change_vs_2025", sc, yr, 100 * (g.loc[yr, "pop_6_14"] / g.loc[2025, "pop_6_14"] - 1), "%")
        for a, b in ((2025, 2035), (2035, 2050)):
            gl = 100 * ((g.loc[b, "pop_15_64"] / g.loc[a, "pop_15_64"]) ** (1 / (b - a)) - 1)
            add(base, "g_l_avg", sc, f"{a}-{b}", gl, "% per year")
        neg = g.index[(g.growth_15_64_pct < 0)]
        add(base, "g_l_first_negative_year", sc, "", int(neg.min()) if len(neg) else np.nan, "year")

    add("q3", "q3_central_tdr_min", "central", "", Q3_CENTRAL_MIN, "per 100 aged 15-64")
    add("q3", "q3_central_tdr_min_year", "central", "", Q3_CENTRAL_MIN_YEAR, "year")
    add("param", "rho", "all", "", RHO, "share")
    add("param", "e_15_64", "all", "2026-Q2", e, "share")

    out = pd.DataFrame(rows)
    out.to_csv(RESULTS / "fiscal_indicators.csv", index=False)
    show = out[out.scenario.isin(["central", "inegi"]) & out.base.isin(["eic2025", "eic2025_conapo65_sensitivity"])]
    print(f"e(15-64) = {e:.4f}")
    print(show.pivot_table(index=["indicator", "period"], columns=["base", "scenario"], values="value", aggfunc="first").round(2).to_string())


if __name__ == "__main__":
    main()
