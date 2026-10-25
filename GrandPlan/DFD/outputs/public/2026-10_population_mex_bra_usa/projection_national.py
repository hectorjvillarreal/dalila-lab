"""
projection_national.py — Total population and share aged 65+ in Mexico, Brazil and the United States,
2025–2050, from national data only (no UN WPP input). Single engine behind every chart in this folder.

Method
    Cohort-component projection by single year of age (0-89, 90+ open) and sex, annual steps from
    mid-2025 to mid-2050. Every input is national:
      base population   MEX INEGI EIC 2025 (5-yr bands + complementary population), split to single
                        ages by following each INEGI CPV 2020 cohort (smoothed for age heaping) five years forward (0-4 uniform);
                        BRA IBGE 2024 projection revision, 2025 by single age; USA Census Bureau
                        Vintage 2025 by single age
      mortality         MEX no national life table usable without CONAPO (which is excluded): IBGE
                        2025 age pattern (assumption) rescaled by sex with two INEGI death-count anchors
                        on the EIC 2025 structure: 2024 registered deaths at 65+ (57.9 % of the total)
                        and in total (scales blended linearly over ages 60-70); then falling 1 % a year; BRA IBGE projection life tables, its year-by-year path; USA CDC/NCHS
                        2024 life tables, death rates falling 1 % a year (assumption)
      fertility pattern MEX INEGI ENR 2025 mothers' ages over EIC 2025 women by age; BRA IBGE 2025
                        TEF; USA CDC 2025 rates; held fixed
      fertility level   latest observed TFR held flat (MEX 1.23, BRA 1.48, USA 1.576); low/high
                        -0.2/+0.2 phased in 2025 -> 2035
      net migration     MEX INEGI EIC rule (-230k to 2030, taper to -134k by 2040) with the EIC age-sex
                        profile; BRA the net migration implied by IBGE's projection (population change
                        minus births plus deaths); USA 321k a year (Census Bureau 2026 figure). BRA and
                        USA use a young-adult profile (assumption, MIGPROF below)
Validation
    With each agency's own inputs (base, TFR path, mortality, migration) the engine must reproduce the
    agency's 2050 total within 1 % and its 2050 65+ share within 0.3 points: IBGE for Brazil. Mexico
    gets plausibility checks against INEGI instead (CONAPO excluded at Héctor's request, 2026-10-24);
    there is no national US projection on file.
Outputs
    results/projections_national.csv (country, scenario, year, pop_millions, share_65plus_pct; scenarios central,
    low, high, central_mig_1M for the US, plus reference paths un_medium, ibge_2024),
    results/validation.txt, results/inputs_sha256.txt, results/assumptions.json
    The UN medium totals are carried only as a reference line, read from data/un_extract_mex_bra_usa.json.
Authors: Claude (code), for Héctor, Oct 2026.
"""
import csv, hashlib, json, os, re, sys
from functools import lru_cache

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
DATA, RES = os.path.join(HERE, "data"), os.path.join(HERE, "results")
NOTA = os.path.join(HERE, "..", "..", "briefs", "2026-09_EIC2025_nota", "data")
IBGE = os.path.join(DATA, "ibge_2024")
NVSR = os.path.join(DATA, "cdc", "nvsr75-05.txt")
US_AGESEX = os.path.join(DATA, "census_nc-est2025-agesex-res.csv")
TOP = 90                      # open age group 90+
AGES = range(TOP + 1)
SRB = 1.05
Y0, Y1 = 2025, 2050
MIGPROF = {0: .03, 5: .03, 10: .03, 15: .10, 20: .20, 25: .20, 30: .14, 35: .10, 40: .07, 45: .04,
           50: .03, 55: .02, 60: .01}   # young-adult net-migration profile by 5-yr group (assumption)
TFR = {"MEX": 1.23, "BRA": 1.48, "USA": 1.576}
US_MORT_DECLINE = 0.01
MEX_MORT_DECLINE = 0.01
INEGI_65_RATE_2024 = {"M": 0.04783, "F": 0.04169}   # INEGI EDR 2024 definitive results report: deaths per person 65+
INEGI_SHARE_65_DEATHS_2024 = 0.579                  # same report: 65+ share of registered deaths
ENR_MOTHER_AGE_2025 = {10: 0.4, 15: 11.8, 20: 22.3, 25: 21.9, 30: 17.0, 35: 8.8, 40: 2.2, 45: 0.2}  # INEGI ENR 2025,
# RR 38/26 Gráfica 10, % of registered births (15.4 % age not specified, excluded = prorated)
INEGI_DEATHS_2024 = 819_672                          # INEGI EDR 2024 definitive (Comunicado 142/25)
INEGI_DEATHS_2024_SEX = {"M": 819_672 * 0.559 / 0.999, "F": 819_672 * 0.440 / 0.999}  # 55.9 % men, 44.0 % women, 0.1 % n.s.


def band_to_single(shares5, sexsplit):
    """5-yr profile {start: share} -> single-age {(sex, age): share}."""
    out = {}
    for a, p in shares5.items():
        for s, w in sexsplit.items():
            for x in range(a, a + 5): out[(s, x)] = out.get((s, x), 0) + p * w / 5
    return out


# ------------------------------------------------------------ life tables
def survival_from_m(m, a0=0.1):
    """Single-age death rates m[0..TOP] (TOP open) -> (S[x] for x=0..TOP-1 plus open, L0 per birth)."""
    l, L = [1.0], []
    for x in range(TOP):
        q = m[x] / (1 + (1 - (a0 if x == 0 else 0.5)) * m[x]); q = min(q, 1.0)
        d = l[-1] * q
        L.append(l[-1] - (1 - (a0 if x == 0 else 0.5)) * d); l.append(l[-1] - d)
    Lopen = l[TOP] / m[TOP]
    S = [L[x + 1] / L[x] for x in range(TOP - 1)]
    S.append(Lopen / (L[TOP - 1] + Lopen))       # (89 and 90+) -> 90+
    return S, L[0]


def lx_from_m(m, a0=0.1, upto=106):
    l = [1.0]
    for x in range(upto):
        mx = m[min(x, TOP)]; ax = a0 if x == 0 else 0.5
        l.append(l[-1] * (1 - min(1.0, mx / (1 + (1 - ax) * mx))))
    return l


@lru_cache(None)
def _bra_lt():
    lt = pd.read_excel(os.path.join(IBGE, "projecoes_2024_tab5_tabuas_mortalidade.xlsx"), header=5)
    return lt[(lt["SIGLA"] == "BR") & (lt["SEXO"].isin(["Homens", "Mulheres"]))]


@lru_cache(None)
def bra_m(year, sex):
    lt = _bra_lt(); sub = lt[(lt["ANO"] == year) & (lt["SEXO"] == ("Homens" if sex == "M" else "Mulheres"))]
    grp = dict(zip(sub["IDADE"], sub["nMx"])); starts = sorted(grp)
    m = [float(grp[max(a for a in starts if a <= x)]) for x in AGES]
    return tuple(m), float(sub[sub["IDADE"] == 0]["nAx"].iloc[0])


def bra_mort():
    return {(y, s): survival_from_m(list(bra_m(y, s)[0]), bra_m(y, s)[1]) for y in range(2024, Y1 + 1) for s in "MF"}


def blend(x): return min(1.0, max(0.0, (x - 60) / 10))


def mex_m(k, s):
    """Mexico 2024 single-age death rates: IBGE 2025 pattern times kY below 60, k65 above 70, blended between."""
    m, a0 = bra_m(2025, s); kY, k65 = k[s]
    return [v * (kY * (1 - blend(x)) + k65 * blend(x)) for x, v in zip(AGES, m)], a0


def mex_mort(k):
    out = {}
    for s in "MF":
        m, a0 = mex_m(k, s)
        for y in range(2024, Y1 + 1):
            f = (1 - MEX_MORT_DECLINE) ** (y - 2024)
            out[(y, s)] = survival_from_m([v * f for v in m], a0)
    return out


def us_mort():
    txt = open(NVSR, encoding="utf-8", errors="replace").read().splitlines()
    tables = {}
    for tab, sex in (("Table 2.", "M"), ("Table 3.", "F")):
        rows = {}; on = False
        for line in txt:
            if line.startswith(tab): on = True; continue
            if on and re.match(r"^Table \d+\.", line) and not line.startswith(tab): break
            if not on: continue
            mm = re.match(r"^(\d+)[–-]\d+\.[ .]*\s+([\d.]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)", line)
            mo = re.match(r"^100 and older[ .]*\s+([\d.]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)", line)
            num = lambda v: float(v.replace(",", ""))
            if mm: rows[int(mm.group(1))] = (num(mm.group(2)), num(mm.group(3)), num(mm.group(6)))
            elif mo: rows[100] = (1.0, num(mo.group(2)), num(mo.group(5)))
        assert len(rows) == 101, (sex, len(rows))
        tables[sex] = rows
    base = {}
    for s, r in tables.items():
        m = [r[x][0] / (1 - 0.5 * r[x][0]) for x in range(TOP)]
        m.append(r[TOP][1] / r[TOP][2])          # l90 / T90 for the open group
        base[s] = m
    out = {}
    for y in range(2024, Y1 + 1):
        f = (1 - US_MORT_DECLINE) ** (y - 2024)
        for s in "MF": out[(y, s)] = survival_from_m([v * f for v in base[s]], a0=0.1)
    return out


# ------------------------------------------------------------ bases
def cpv2020():
    """INEGI CPV 2020 by single age (0..100+), smoothed with a centred 5-year moving average (ages 2-97) to
    remove digit preference (heaping on ages ending in 0 and 5) before it is used as within-band weights."""
    d = pd.read_csv(os.path.join(DATA, "inegi_cpv2020_single_age_prorated.csv"))
    out = {}
    for s in "MF":
        v = d[s].astype(float).tolist()
        out[s] = [sum(v[x - 2:x + 3]) / 5 if 2 <= x <= 97 else v[x] for x in range(len(v))]
    return out


def mex_bands():
    """INEGI EIC 2025 private dwellings + 517,925 complementary (CPV 2020 non-household shares), 5-yr bands, 75+ open."""
    eic = pd.read_csv(os.path.join(NOTA, "eic2025_mex_private_by_band_sex.csv"))
    comp = pd.read_csv(os.path.join(NOTA, "cpv2020_mex_nonhousehold_by_band_sex.csv"))
    out = {}
    for s in "MF":
        bands = {}
        for _, r in eic[eic.sex == s].iterrows():
            a = min(int(re.match(r"(\d+)", r["band"]).group(1)), 75); bands[a] = bands.get(a, 0) + r["count"]
        for _, r in comp[comp.sex == s].iterrows():
            a = min(int(re.match(r"(\d+)", r["band"]).group(1)), 75); bands[a] = bands.get(a, 0) + 517_925 * r["share_within_residual"]
        out[s] = bands
    return out


def split_bands(bands, cpv, l=None):
    """Split 5-yr bands to single ages with the CPV 2020 cohorts five years younger (0-4 uniform); in 75+ the
    cohorts are weighted by 5-year survival from lx l when given."""
    v = [0.0] * (TOP + 1)
    for a, n in bands.items():
        if a == 0: w = {x: 1.0 for x in range(5)}
        elif a < 75: w = {x: cpv[x - 5] for x in range(a, a + 5)}
        else:
            w = {}
            for x in range(75, 106):
                sv = l[x] / l[x - 5] if l else 1.0
                w[min(x, TOP)] = w.get(min(x, TOP), 0) + cpv[min(x - 5, 100)] * (1.0 if x - 5 < 100 else 0.0) * sv
        tw = sum(w.values())
        for x, wx in w.items(): v[x] += n * wx / tw
    return v


def mex_base_and_k():
    """EIC base split to single ages and the IBGE-pattern scale k fitted to INEGI's 2024 65+ death rate (two passes)."""
    bands, cpv = mex_bands(), cpv2020()
    base = {s: split_bands(bands[s], cpv[s]) for s in "MF"}
    k = {s: (1.0, 1.0) for s in "MF"}
    for _ in range(3):
        # 65+ deaths by sex: INEGI's 65+ share of deaths, split by sex with INEGI's 65+ rates on the EIC sex mix
        w = {s: INEGI_65_RATE_2024[s] * sum(base[s][65:]) for s in "MF"}
        d65 = {s: INEGI_SHARE_65_DEATHS_2024 * INEGI_DEATHS_2024 * w[s] / (w["M"] + w["F"]) for s in "MF"}
        for s in "MF":
            m, _a0 = bra_m(2025, s); pop = base[s]
            for _it in range(50):          # alternate the two anchors until both hold
                kY, k65 = k[s]
                ms = [v * (kY * (1 - blend(x)) + k65 * blend(x)) for x, v in zip(AGES, m)]
                k65 *= d65[s] / sum(a * b for a, b in zip(ms[65:], pop[65:]))
                ms = [v * (kY * (1 - blend(x)) + k65 * blend(x)) for x, v in zip(AGES, m)]
                young = sum(a * b for a, b in zip(ms[:65], pop[:65]))
                kY *= (INEGI_DEATHS_2024_SEX[s] - sum(a * b for a, b in zip(ms[65:], pop[65:]))) / young
                k[s] = (kY, k65)
        base = {s: split_bands(bands[s], cpv[s], lx_from_m(*mex_m(k, s))) for s in "MF"}
    return base, k


@lru_cache(None)
def _bra_pop():
    p = pd.read_excel(os.path.join(IBGE, "projecoes_2024_tab1_idade_simples.xlsx"), header=5)
    return p[(p["SIGLA"] == "BR") & (p["SEXO"].isin(["Homens", "Mulheres"]))]


def bra_single(year):
    p = _bra_pop()
    out = {}
    for sx, s in (("Homens", "M"), ("Mulheres", "F")):
        sub = p[p.SEXO == sx].copy(); sub["age"] = sub["IDADE"].astype(str).str.extract(r"(\d+)")[0].astype(int).clip(upper=TOP)
        out[s] = sub.groupby("age")[year].sum().reindex(AGES).astype(float).tolist()
    return out


def us_base():
    v = {"M": [0.0] * (TOP + 1), "F": [0.0] * (TOP + 1)}
    for r in csv.DictReader(open(US_AGESEX)):
        a = int(r["AGE"])
        if a == 999 or r["SEX"] == "0": continue
        v["M" if r["SEX"] == "1" else "F"][min(a, TOP)] += float(r["POPESTIMATE2025"])
    return v


# ------------------------------------------------------------ fertility patterns (single-age, sum 1)
def pattern_from_groups(groups):
    tot = sum(groups.values()); pat = [0.0] * (TOP + 1)
    for a, r in groups.items():
        for x in range(a, a + 5): pat[x] = r                      # group rate applies to each single age
    s = sum(pat); return [p / s for p in pat]


def mex_pattern():
    """INEGI ENR 2025 mothers' age distribution divided by EIC 2025 women per band -> relative ASFR."""
    women = mex_bands()["F"]
    return pattern_from_groups({a: sh / women[a] for a, sh in ENR_MOTHER_AGE_2025.items()})


def bra_ind():
    ind = pd.read_excel(os.path.join(IBGE, "projecoes_2024_tab4_indicadores.xlsx"), header=6)
    return ind[ind["SIGLA"] == "BR"].set_index("ANO")


def bra_pattern(ind, year=2025):
    cols = {a: f"TEF_{a}-{a+4}" for a in range(10, 50, 5)}
    return pattern_from_groups({a: float(ind.loc[year, c]) for a, c in cols.items()})


US_ASFR_2025 = {10: 0.1, 15: 11.7, 20: 52.3, 25: 85.7, 30: 96.3, 35: 55.2, 40: 12.8, 45: 1.1}  # CDC Data Brief 571


# ------------------------------------------------------------ engine
def project(base, surv, tfr_fn, pat_fn, mig_fn, prof):
    M, F = list(base["M"]), list(base["F"])
    out = {Y0: (list(M), list(F))}
    for y in range(Y0, Y1):
        SM, L0M = surv(y, "M"); SF, L0F = surv(y, "F")
        nM = [0.0] * (TOP + 1); nF = [0.0] * (TOP + 1)
        for x in range(TOP - 1): nM[x + 1] = M[x] * SM[x]; nF[x + 1] = F[x] * SF[x]
        nM[TOP] = (M[TOP - 1] + M[TOP]) * SM[TOP - 1]; nF[TOP] = (F[TOP - 1] + F[TOP]) * SF[TOP - 1]
        tfr, pat = tfr_fn(y), pat_fn(y)
        B = sum(tfr * pat[x] * (F[x] + nF[x]) / 2 for x in range(10, 55))
        nM[0] = B * SRB / (1 + SRB) * L0M; nF[0] = B / (1 + SRB) * L0F
        N = mig_fn(y)
        for (s, x), p in prof.items():
            (nM if s == "M" else nF)[min(x, TOP)] += N * p
        M, F = nM, nF; out[y + 1] = (list(M), list(F))
    return out


def tot(mf): return sum(mf[0]) + sum(mf[1])
def share65(mf): return 100 * (sum(mf[0][65:]) + sum(mf[1][65:])) / tot(mf)


def tfr_path(level, delta): return lambda y: level + delta * min(1.0, max(0.0, (y - 2025) / 10))


def mex_mig(y):
    if y < 2030: return -230_000.0
    if y >= 2040: return -134_000.0
    return -230_000.0 + (y - 2030) * 9_600.0


def main():
    os.makedirs(RES, exist_ok=True)
    files = [os.path.join(IBGE, f) for f in sorted(os.listdir(IBGE))] + [NVSR, US_AGESEX] + \
            [os.path.join(DATA, "inegi_cpv2020_single_age_prorated.csv")] + \
            [os.path.join(NOTA, f) for f in ("eic2025_mex_private_by_band_sex.csv", "cpv2020_mex_nonhousehold_by_band_sex.csv",
                                            "eic2025_emigrants_age_sex_grafica9.csv")]
    open(os.path.join(RES, "inputs_sha256.txt"), "w").write(
        "\n".join(f"{hashlib.sha256(open(f, 'rb').read()).hexdigest()}  {os.path.relpath(f, HERE)}" for f in files) + "\n")

    generic = band_to_single(MIGPROF, {"M": 0.55, "F": 0.45})
    eicp = {}
    for r in csv.DictReader(open(os.path.join(NOTA, "eic2025_emigrants_age_sex_grafica9.csv"))):
        a = int(re.match(r"(\d+)", r["band"]).group(1))
        eicp[a] = (float(r["men_pct"]), float(r["women_pct"]))
    s = sum(m + w for m, w in eicp.values())
    eic_prof = {}
    for a, (m, w) in eicp.items():
        ages = range(a, a + 5) if a < 85 else range(85, TOP + 1)
        for x in ages:
            eic_prof[("M", x)] = eic_prof.get(("M", x), 0) + m / s / len(ages)
            eic_prof[("F", x)] = eic_prof.get(("F", x), 0) + w / s / len(ages)

    mex_base, k = mex_base_and_k()
    mexS, braS, usS = mex_mort(k), bra_mort(), us_mort()
    ind = bra_ind()
    val, rows = [], []

    # validation: Brazil with IBGE's own inputs
    bra_nm = lambda y: float(ind.loc[y + 1, "POP_T"] - ind.loc[y, "POP_T"]
                             - (ind.loc[y, "NASC_T"] + ind.loc[y + 1, "NASC_T"]) / 2 + (ind.loc[y, "OBT_T"] + ind.loc[y + 1, "OBT_T"]) / 2)
    v = project(bra_single(2025), lambda y, s: braS[(y, s)], lambda y: float(ind.loc[y, "TFT"]),
                lambda y: bra_pattern(ind, y), bra_nm, generic)
    ib = bra_single(2050); ib_t = sum(ib["M"]) + sum(ib["F"]); ib_65 = 100 * (sum(ib["M"][65:]) + sum(ib["F"][65:])) / ib_t
    val.append(f"Brazil, IBGE inputs: 2050 total {tot(v[2050])/1e6:.2f} M vs IBGE {ib_t/1e6:.2f} M; 65+ {share65(v[2050]):.2f} % vs IBGE {ib_65:.2f} %")
    ok = abs(tot(v[2050]) / ib_t - 1) < 0.01 and abs(share65(v[2050]) - ib_65) < 0.3
    # plausibility: Mexico against INEGI (no agency projection used)
    e0, deaths = {}, 0.0
    for sx in "MF":
        m, a0 = mex_m(k, sx); l = lx_from_m(m, a0, upto=130)
        e0[sx] = sum((l[x] + l[x + 1]) / 2 for x in range(129))
        deaths += sum(a * b for a, b in zip(m, mex_base[sx]))
    val.append(f"Mexico, INEGI anchors: IBGE-pattern scales (below 60 / above 70) M {k['M'][0]:.3f}/{k['M'][1]:.3f}, "
               f"F {k['F'][0]:.3f}/{k['F'][1]:.3f}; deaths at 2024 rates on the 2025 base {deaths/1e3:.0f}k vs INEGI registered 2024 "
               f"{INEGI_DEATHS_2024/1e3:.0f}k; implied e0 2024 M {e0['M']:.1f} F {e0['F']:.1f}")
    open(os.path.join(RES, "validation.txt"), "w").write("\n".join(val) + "\n")
    print("\n".join(val))
    if not ok: sys.exit("VALIDATION FAILED")

    setups = {
        "Mexico": (mex_base, lambda y, s: mexS[(y, s)], (lambda pat: lambda y: pat)(mex_pattern()), mex_mig, eic_prof, TFR["MEX"]),
        "Brazil": (bra_single(2025), lambda y, s: braS[(y, s)], lambda y: bra_pattern(ind, 2025), bra_nm, generic, TFR["BRA"]),
        "United States": (us_base(), lambda y, s: usS[(y, s)], lambda y: pattern_from_groups(US_ASFR_2025),
                          lambda y: 321_000.0, generic, TFR["USA"]),
    }
    row = lambda c, sc, y, mf: rows.append([c, sc, y, f"{tot(mf)/1e6:.3f}", f"{share65(mf):.3f}"])
    for name, (base, surv, pat, mig, prof, level) in setups.items():
        scen = [("central", 0.0, mig), ("low", -0.2, mig), ("high", 0.2, mig)]
        if name == "United States": scen.append(("central_mig_1M", 0.0, lambda y: 1_000_000.0))
        for sc, d, mg in scen:
            r = project(base, surv, tfr_path(level, d), pat, mg, prof)
            for y, mf in r.items(): row(name, sc, y, mf)
            print(f"{name:14s} {sc:15s} pop 2050 {tot(r[2050])/1e6:6.1f} M  65+ 2025 {share65(r[2025]):.1f} %  2050 {share65(r[2050]):.1f} %")
    # reference paths: national agencies and UN medium (reference only, never an input)
    for y in range(Y0, Y1 + 1):
        p = bra_single(y); row("Brazil", "ibge_2024", y, (p["M"], p["F"]))
    un = json.load(open(os.path.join(DATA, "un_extract_mex_bra_usa.json")))
    for iso, name in (("MEX", "Mexico"), ("BRA", "Brazil"), ("USA", "United States")):
        for r in un[iso]["tot"]:
            if Y0 <= int(r["Time"]) <= Y1: rows.append([name, "un_medium", int(r["Time"]), f"{float(r['PopTotal'])/1000:.3f}", ""])
    with open(os.path.join(RES, "projections_national.csv"), "w", newline="") as h:
        w = csv.writer(h); w.writerow(["country", "scenario", "year", "pop_millions", "share_65plus_pct"]); w.writerows(rows)
    assume = {}
    for name, (base, surv, *_rest) in setups.items():
        lvl = setups[name][5]
        e0s = {}
        for s_ in "MF":
            S, L0 = surv(2025, s_)
            e = L0
            # rebuild person-years from survival ratios: L(x+1) = L(x) * S(x)
            Lx = L0
            for x in range(TOP - 1): Lx *= S[x]; e += Lx
            e0s[s_] = round(e + Lx * S[TOP - 1] / (1 - S[TOP - 1]), 2)
        assume[name] = {"base_2025_millions": round((sum(base["M"]) + sum(base["F"])) / 1e6, 3), "tfr_central": lvl,
                        "tfr_range": [round(lvl - 0.2, 3), round(lvl + 0.2, 3)], "e0_2025_male": e0s["M"], "e0_2025_female": e0s["F"]}
    json.dump(assume, open(os.path.join(RES, "assumptions.json"), "w"), indent=2, ensure_ascii=False)
    print(assume)


if __name__ == "__main__":
    main()
