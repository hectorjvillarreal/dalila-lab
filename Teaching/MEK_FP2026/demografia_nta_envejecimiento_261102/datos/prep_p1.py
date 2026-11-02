"""Datos de la Parte 1. Escribe CSV y fragmentos TikZ en esta carpeta. Ver README.md."""
import csv, os, re, sys
import pandas as pd
ROOT = os.path.expanduser("~/Dalila")
WPP = f"{ROOT}/GrandPlan/DFD/outputs/public/2026-09_mexico_2050/data"
ENG = f"{ROOT}/GrandPlan/DFD/outputs/public/2026-10_population_mex_bra_usa"
OUT = os.path.dirname(os.path.abspath(__file__))

ind = pd.read_csv(f"{WPP}/WPP2024_Demographic_Indicators_Medium.csv.gz", usecols=["Location", "Time", "TFR", "CBR", "CDR", "Variant"], low_memory=False)
ind = ind.drop_duplicates(["Location", "Time"])
mx = ind[(ind.Location == "Mexico") & (ind.Time <= 2023)].sort_values("Time")
mx[["Time", "CBR", "CDR", "TFR"]].round(2).to_csv(f"{OUT}/p1_tasas_mex.csv", index=False)
print("MEX", mx[mx.Time.isin([1950, 1960, 1970, 1980, 1990, 2000, 2010, 2023])][["Time", "CBR", "CDR", "TFR"]].round(2).to_string(index=False))
print("TFR<2.1 desde", int(mx[mx.TFR < 2.1].Time.min()))
print("LAC TFR 2024", ind[(ind.Location == "Latin America and the Caribbean") & (ind.Time == 2024)].TFR.round(2).tolist())

age = pd.read_csv(f"{WPP}/WPP2024_PopulationByAge5GroupSex_Medium.csv.gz", usecols=["Location", "Time", "AgeGrpStart", "PopMale", "PopFemale", "PopTotal"])

def dep(L):
    x = age[age.Location == L]
    t = x.groupby("Time").PopTotal.sum()
    wa = x[(x.AgeGrpStart >= 15) & (x.AgeGrpStart < 65)].groupby("Time").PopTotal.sum()
    return ((t - wa) / wa * 100)
dl, dm = dep("Latin America and the Caribbean"), dep("Mexico")
d = pd.DataFrame({"Time": dl.index, "LAC": dl.values.round(2), "MEX": dm.values.round(2)})
d = d[(d.Time <= 2050)]
d.to_csv(f"{OUT}/p1_dependencia.csv", index=False)
print("dep LAC max/min", d.loc[d.LAC.idxmax()].to_dict(), d.loc[d.LAC.idxmin()].to_dict(), "MEX min", d.loc[d.MEX.idxmin()].to_dict(), "LAC 2023-2030", d[d.Time.between(2024, 2032)].LAC.tolist())

# pirámides: % de la población total por grupo quinquenal, 85+ abierto
BANDS = list(range(0, 85, 5)) + [85]
def wpp_pyr(year):
    x = age[(age.Location == "Mexico") & (age.Time == year)].copy()
    x["b"] = x.AgeGrpStart.clip(upper=85)
    g = x.groupby("b")[["PopMale", "PopFemale"]].sum()
    t = g.values.sum()
    return (g.PopMale / t * 100).tolist(), (g.PopFemale / t * 100).tolist()

def single_pyr(M, F):
    t = sum(M) + sum(F); rm, rf = [0.0] * 18, [0.0] * 18
    for a, (m, f) in enumerate(zip(M, F)):
        i = min(a // 5, 17); rm[i] += m / t * 100; rf[i] += f / t * 100
    return rm, rf

c = pd.read_csv(f"{ENG}/data/inegi_cpv2020_single_age_prorated.csv")
print("CPV total M", round((c.M.sum() + c.F.sum()) / 1e6, 3), "edad max", c.age.max())
p20 = single_pyr(c.M.tolist(), c.F.tolist())
p70 = wpp_pyr(1970)

# 2050: el motor nacional, escenario central, sin tocar sus resultados
sys.path.insert(0, ENG)
sys.argv = ["x"]
import projection_national as P
eicp = {}
for r in csv.DictReader(open(os.path.join(P.NOTA, "eic2025_emigrants_age_sex_grafica9.csv"))):
    a = int(re.match(r"(\d+)", r["band"]).group(1)); eicp[a] = (float(r["men_pct"]), float(r["women_pct"]))
s = sum(m + w for m, w in eicp.values()); prof = {}
for a, (m, w) in eicp.items():
    ages = range(a, a + 5) if a < 85 else range(85, P.TOP + 1)
    for x in ages:
        prof[("M", x)] = prof.get(("M", x), 0) + m / s / len(ages)
        prof[("F", x)] = prof.get(("F", x), 0) + w / s / len(ages)
base, k = P.mex_base_and_k(); S = P.mex_mort(k); pat = P.mex_pattern()
r = P.project(base, lambda y, s: S[(y, s)], P.tfr_path(P.TFR["MEX"], 0.0), lambda y: pat, P.mex_mig, prof)
print("motor 2050 M", round(P.tot(r[2050]) / 1e6, 1), "65+", round(P.share65(r[2050]), 1), "TGF", P.TFR["MEX"])
p50 = single_pyr(*r[2050])

rows = []
for i, b in enumerate(BANDS):
    rows.append({"grupo": b, "H1970": p70[0][i], "M1970": p70[1][i], "H2020": p20[0][i], "M2020": p20[1][i], "H2050": p50[0][i], "M2050": p50[1][i]})
pd.DataFrame(rows).round(3).to_csv(f"{OUT}/p1_piramides.csv", index=False)
def sh(p, lo, hi): return round(sum(p[0][i] + p[1][i] for i in range(18) if lo <= BANDS[i] < hi), 1)
res = {"1970": p70, "2020": p20, "2050": p50}
for y, p in res.items(): print(y, "0-14", sh(p, 0, 15), "15-64", sh(p, 15, 65), "65+", sh(p, 65, 200))

def tikz(p, name):
    H = 0.215; S = 0.135   # cm por banda; cm por punto porcentual
    L = [f"% {name}: generado por prep_p1.py"]
    for i, b in enumerate(BANDS):
        y = i * H
        col = "cImpuesto!70" if b >= 65 else ("cRecauda!70" if b < 15 else "cOferta!70")
        L.append(f"\\fill[{col}] ({-p[0][i]*S:.3f},{y:.3f}) rectangle (-0.06,{y+H-0.03:.3f});")
        L.append(f"\\fill[{col}] (0.06,{y:.3f}) rectangle ({p[1][i]*S:.3f},{y+H-0.03:.3f});")
    open(f"{OUT}/p1_piramide_{name}.tex", "w").write("\n".join(L) + "\n")
for y, p in res.items(): tikz(p, y)
print("max banda", {y: round(max(max(p[0]), max(p[1])), 2) for y, p in res.items()})

# velocidad 10 % a 20 % de 65+
out = []
for L, n in [("Republic of Korea", "Corea"), ("Japan", "Japón"), ("Costa Rica", "Costa Rica"), ("Brazil", "Brasil"), ("Colombia", "Colombia"), ("Chile", "Chile"), ("Mexico", "México"), ("Latin America and the Caribbean", "América Latina y el Caribe"), ("Spain", "España"), ("Germany", "Alemania"), ("Europe", "Europa"), ("France", "Francia"), ("Sweden", "Suecia")]:
    x = age[age.Location == L]; t = x.groupby("Time").PopTotal.sum(); o = x[x.AgeGrpStart >= 65].groupby("Time").PopTotal.sum(); s6 = o / t * 100
    a, b = int(s6[s6 >= 10].index[0]), int(s6[s6 >= 20].index[0])
    out.append({"pais": n, "y10": a, "y20": b, "dur": b - a, "s1950": round(s6.iloc[0], 1)})
pd.DataFrame(out).to_csv(f"{OUT}/p1_velocidad.csv", index=False)
print(pd.DataFrame(out).to_string(index=False))
n = pd.read_csv(f"{ENG}/results/projections_national.csv"); n = n[(n.country == "Mexico") & (n.scenario == "central")]
print("motor 65+>=20 en", int(n[n.share_65plus_pct >= 20].year.min()), "pico pob", n.loc[n.pop_millions.idxmax()][["year", "pop_millions"]].tolist())
