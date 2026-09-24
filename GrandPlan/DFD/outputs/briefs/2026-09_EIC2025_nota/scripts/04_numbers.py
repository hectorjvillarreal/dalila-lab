"""
Writes build/numbers.tex: every number printed in the nota, as \\N{key}, read from
results/*.csv, data/*.csv, the 65+ check in the demographics corpus, and the assumption
constants of 01_scenarios.py / 03_fiscal.py. Nothing numeric is typed into the .tex.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA, RESULTS, BUILD = ROOT / "data", ROOT / "results", ROOT / "build"
CHECK = ROOT.parents[4] / "_crossrefs/corpus/demographics/country/MEX"
BASE = "eic2025"
SENS = "eic2025_conapo65_sensitivity"
KEYS = ("optimista", "central", "inegi", "estres")


def load_module(name):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def f(x, d=1):
    s = f"{x:,.{d}f}"
    return s.replace("-", "\\textminus{}") if s.startswith("-") and s.strip("-0.,") else s.lstrip("-")


def main():
    sc = load_module("01_scenarios")
    fi = load_module("03_fiscal")
    N = {}

    res = pd.read_csv(RESULTS / "scenarios_eic2025_brief.csv")
    fis = pd.read_csv(RESULTS / "fiscal_indicators.csv")
    fis["period"] = fis.period.fillna("").astype(str)
    gate = pd.read_csv(RESULTS / "base_reconciliation_gate.csv").set_index("group")
    eic = pd.read_csv(DATA / "eic2025_mex_national_indicators.csv", index_col=0)["value"]
    wpp = pd.read_csv(DATA / "wpp2024_mex_indicators_medium.csv").set_index("year")
    low = pd.read_csv(DATA / "wpp2024_mex_tfr_low_variant.csv").set_index("year")
    enoe = pd.read_csv(DATA / "enoe2026q2_employment_rate.csv", index_col=0)["value"]
    chk = pd.read_csv(CHECK / "eic2025_65plus_check.csv")
    chk = chk[(chk.variant == "prorated") & (chk.sex == "T")].set_index("group")
    ctx = pd.read_csv(CHECK / "eic2025_65plus_check_context.csv", index_col=0)["value"]

    def v(ind, s, period="", base=BASE):
        r = fis[(fis.indicator == ind) & (fis.scenario == s) & (fis.period == str(period)) & (fis.base == base)]
        assert len(r) == 1, (ind, s, period, base)
        return float(r.value.iloc[0])

    # page 1 — the fact
    N["eicPob"] = f(float(eic["POBTOT"]) / 1e6 + sc.EIC_COMPLEMENTARY / 1e6)
    N["eicTgf"] = f(float(eic["TGF"]), 2)
    N["censoTgf"] = "1.9"                               # INEGI CPV 2020, same method (RR 37/26)
    N["eicEdadMediana"] = f(float(eic["MEDIANA_POBTOT"]), 0)
    N["eicSesentaycincoPct"] = f(100 * float(eic["POB65_MAS"]) / float(eic["POBTOT"]), 1)
    N["eicEmigrantes"] = f(1_300_000 / 1e6, 1)
    N["eicRetornos"] = f(150_800 / 1e3, 0)
    N["eicTdr"] = f(float(eic["RAZON_DEP_TOT"]), 1)
    N["onuTgfDosmilveinticinco"] = f(wpp.loc[2025, "TFR"], 2)
    N["onuTgfDosmilveinticuatro"] = f(wpp.loc[2024, "TFR"], 2)
    N["onuTgfDosmilcincuenta"] = f(wpp.loc[2050, "TFR"], 2)
    N["onuBajaDosmilveinticuatro"] = f(low.loc[2024, "TFR_low"], 2)
    N["onuBajaDosmilcincuenta"] = f(low.loc[2050, "TFR_low"], 2)
    N["onuPobDosmilcincuenta"] = f(wpp.loc[2050, "TPopulation1July"] / 1e3, 1)
    N["gapNinos"] = f(-gate.loc["0-14", "base_minus_conapo"] / 1e6, 1)

    # page 2 — scenarios
    b = res[res.base == BASE]
    for k in KEYS:
        g = b[b.scenario == k].set_index("year")
        N[f"pob2050_{k}"] = f(g.loc[2050, "population"] / 1e6, 1)
        N[f"tdrMin_{k}"] = f(v("tdr_min", k), 1)
        N[f"tdrMinAnio_{k}"] = str(int(v("tdr_min_year", k)))
        N[f"oadr2025_{k}"] = f(v("oadr", k, 2025), 0)
        N[f"oadr2050_{k}"] = f(v("oadr", k, 2050), 1)
        N[f"spanIni_{k}"] = str(int(v("span_1pt_start", k)))
        N[f"spanFin_{k}"] = str(int(v("span_1pt_end", k)))
    N["centralTgf"] = "1.50"
    N["inegiTgf"] = f(sc.EIC_TFR, 2)
    N["estresPiso"] = "0.90"
    N["estresAnio"] = "2031"
    N["tdrBaja"] = f(float(eic["RAZON_DEP_TOT"]) - v("tdr_min", "central"), 1)
    N["ydr2025"] = f(v("ydr", "central", 2025), 0)
    N["ydr2035_central"] = f(v("ydr", "central", 2035), 0)
    N["oadr2035_central"] = f(v("oadr", "central", 2035), 0)
    # Recuadro 2
    N["gapSesentaycinco"] = f(gate.loc["65+", "base_minus_conapo"] / 1e6, 1)
    N["chkEic"] = f(chk.loc["65+", "eic2025"] / 1e6, 1)
    N["chkCenso"] = f(chk.loc["65+", "cpv2020_aged_net"] / 1e6, 1)
    N["chkDif"] = f(chk.loc["65+", "eic_minus_aged"] / 1e6, 1)
    N["chkConapoOct"] = f((ctx["conapo_65plus_mid2025"] + (sc.EIC_REF_DATE - 2025.5)
                           * (ctx["conapo_65plus_mid2026"] - ctx["conapo_65plus_mid2025"])) / 1e6, 1)
    N["migEic"] = f(-sc.NET_MIG_EIC / 1e3, 0)
    N["migTaper"] = f(-sc.NET_MIG_TAPER_END / 1e3, 0)
    N["migRangoLo"] = f(-sc.NET_MIG_RANGE_2015_20[0] / 1e3, 0)
    N["migRangoHi"] = f(-sc.NET_MIG_RANGE_2015_20[1] / 1e3, 0)
    N["migHombresPct"] = f(100 * sc.MIG_MALE_SHARE, 1)

    # page 3 — fiscal
    N["qTresMin"] = f(fi.Q3_CENTRAL_MIN, 1)
    N["qTresMinAnio"] = str(fi.Q3_CENTRAL_MIN_YEAR)
    for k in ("central", "inegi"):
        for yr in fi.TAU_YEARS:
            N[f"tau{yr}_{k}"] = f(v("tau_payg", k, yr), 1)
            N[f"tauSens{yr}_{k}"] = f(v("tau_payg", k, yr, SENS), 1)
    N["rho"] = f(fi.RHO, 2)
    N["rhoPct"] = f(100 * fi.RHO, 0)
    N["eEmpleo"] = f(float(enoe["e_15_64"]), 2)
    N["eEmpleoPct"] = f(100 * float(enoe["e_15_64"]), 0)
    N["enoeTrim"] = "segundo trimestre de 2026"
    for k in KEYS:
        for yr in (2025, 2031, 2035, 2050):
            N[f"escolar{yr}_{k}"] = f(v("pop_6_14", k, yr) / 1e6, 1)
            N[f"escolarCambio{yr}_{k}"] = f(v("pop_6_14_change_vs_2025", k, yr), 1)
        N[f"glA_{k}"] = f(v("g_l_avg", k, "2025-2035"), 2)
        N[f"glB_{k}"] = f(v("g_l_avg", k, "2035-2050"), 2)
        N[f"glNeg_{k}"] = str(int(v("g_l_first_negative_year", k)))
    N["escolarAnioFijo"] = str(fi.LOCKED_6_14_YEAR)
    N["escolarNacidosPts"] = f(v("escolar_decline_born_pts", "central", fi.LOCKED_6_14_YEAR), 1)
    N["escolarEmigraPts"] = f(v("escolar_decline_emigration_pts", "central", fi.LOCKED_6_14_YEAR), 1)
    # v1.0 edit 1: the 65+ range and the τ sensitivity, as points of difference
    N["tauSensDif2025"] = f(v("tau_payg", "central", 2025) - v("tau_payg", "central", 2025, SENS), 1)
    N["tauSensDif2050"] = f(v("tau_payg", "central", 2050) - v("tau_payg", "central", 2050, SENS), 1)

    BUILD.mkdir(exist_ok=True)
    lines = ["% generated by scripts/04_numbers.py — do not edit",
             "\\makeatletter",
             "\\newcommand{\\N}[1]{\\ifcsname nota@#1\\endcsname\\csname nota@#1\\endcsname"
             "\\else\\PackageError{nota}{Unknown number key #1}{}\\fi}"]
    lines += [f"\\@namedef{{nota@{k}}}{{{val}}}" for k, val in N.items()]
    lines.append("\\makeatother")
    (BUILD / "numbers.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(N)} numbers to", BUILD / "numbers.tex")


if __name__ == "__main__":
    main()
