"""Datos de la Parte 3. Perfiles de ntaccounts.org, población de WPP 2024 y del motor nacional. Ver README.md."""
import csv, os, re, sys
import numpy as np, pandas as pd
ROOT = os.path.expanduser("~/Dalila")
WPP = f"{ROOT}/GrandPlan/DFD/outputs/public/2026-09_mexico_2050/data"
ENG = f"{ROOT}/GrandPlan/DFD/outputs/public/2026-10_population_mex_bra_usa"
OUT = os.path.dirname(os.path.abspath(__file__))
d = pd.read_csv(f"{OUT}/ntaccounts_perfiles.csv", low_memory=False)
ages = [f"Age{i}" for i in range(91)]
def prof(c, y, v):
    x = d[(d.Country == c) & (d.Year == y) & (d["Variable Name"] == v)]
    s = x[x.VarType == "Smooth Mean"]; x = s if len(s) else x
    return None if x.empty else np.nan_to_num(x.iloc[0][ages].astype(float).values)
def base(c, y): return prof(c, y, "Labor Income")[30:50].mean()
age = pd.read_csv(f"{WPP}/WPP2024_PopulationByAge5GroupSex_Medium.csv.gz", usecols=["Location", "Time", "AgeGrpStart", "PopFemale", "PopTotal"])

# 65+ por regiones, 1950-2100 (gráfico 2 del informe)
regs = {"lac": "Latin America and the Caribbean", "eur": "Europe", "asi": "Asia", "afr": "Africa", "nam": "Northern America", "mun": "World"}
t = None
for k, L in regs.items():
    x = age[age.Location == L]; s = (x[x.AgeGrpStart >= 65].groupby("Time").PopTotal.sum() / x.groupby("Time").PopTotal.sum() * 100).round(2)
    t = s.rename(k).to_frame() if t is None else t.join(s.rename(k))
t.reset_index().to_csv(f"{OUT}/p3_65mas_regiones.csv", index=False)
print(t.loc[[1950, 2024, 2050, 2100]].to_string())

# razón de sostenimiento con pesos fijos: verifica contra el informe y agrega México
def pesos_anio(L):
    x = age[age.Location == L]; yrs = sorted(x.Time.unique()); P = {}
    for y, g in x.groupby("Time"):
        w = np.zeros(91); g = g.set_index("AgeGrpStart").PopTotal
        for a in range(0, 90, 5): w[a:a + 5] = g.get(a, 0) / 5
        w[90] = g[g.index >= 90].sum(); P[y] = w
    return P
print("informe: Chile 2023, Brasil 2025, Costa Rica 2026, Perú 2036, Argentina 2038")
sr = {}
for c, y, L in [("Chile", 2018, "Chile"), ("Brazil", 2008, "Brazil"), ("Costa Rica", 2013, "Costa Rica"), ("Peru", 2014, "Peru"), ("Argentina", 2016, "Argentina"), ("Mexico", 2014, "Mexico"), ("Mexico", 2010, "Mexico")]:
    P = pesos_anio(L); C, Y = prof(c, y, "Consumption"), prof(c, y, "Labor Income")
    s = pd.Series({a: (Y * w).sum() / (C * w).sum() for a, w in P.items()}); s = s / s.iloc[0] if False else s
    sr[f"{c}{y}"] = s; print(c, y, "max", int(s.idxmax()), round(s.max(), 3), "2024", round(s[2024], 3), "2050", round(s[2050], 3), "caída 2024-50 %", round((s[2050] / s[2024] - 1) * 100, 1))

# motor nacional: población por edad
sys.path.insert(0, ENG); sys.argv = ["x"]
import projection_national as PN
eicp = {}
for r in csv.DictReader(open(os.path.join(PN.NOTA, "eic2025_emigrants_age_sex_grafica9.csv"))):
    a = int(re.match(r"(\d+)", r["band"]).group(1)); eicp[a] = (float(r["men_pct"]), float(r["women_pct"]))
s = sum(m + w for m, w in eicp.values()); pr = {}
for a, (m, w) in eicp.items():
    rng = range(a, a + 5) if a < 85 else range(85, PN.TOP + 1)
    for x in rng:
        pr[("M", x)] = pr.get(("M", x), 0) + m / s / len(rng); pr[("F", x)] = pr.get(("F", x), 0) + w / s / len(rng)
b0, k0 = PN.mex_base_and_k(); S = PN.mex_mort(k0); pat = PN.mex_pattern()
R = PN.project(b0, lambda y, s: S[(y, s)], PN.tfr_path(PN.TFR["MEX"], 0.0), lambda y: pat, PN.mex_mig, pr)
def pop(y):
    m, f = R[y]; v = np.array(m) + np.array(f); w = np.zeros(91); w[:90] = v[:90]; w[90] = v[90:].sum(); return w, np.array(f)
# razón con el motor (México, 2025-2050)
for yy in (2014, 2010):
    C, Y = prof("Mexico", yy, "Consumption"), prof("Mexico", yy, "Labor Income")
    q = {y: (Y * pop(y)[0]).sum() / (C * pop(y)[0]).sum() for y in range(2025, 2051)}
    print("Mex", yy, "motor: max", max(q, key=q.get), round(max(q.values()), 3), "2025", round(q[2025], 3), "2050", round(q[2050], 3), "caída %", round((q[2050] / q[2025] - 1) * 100, 1))

# aritmética de perfiles fijos: gasto público por uso como % del ingreso laboral total, México (perfiles 2004)
res = []
Y = prof("Mexico", 2004, "Labor Income")
for lab, y in (("2025", 2025), ("2050", 2050)):
    w, _ = pop(y); yl = (Y * w).sum(); row = {"anio": lab}
    for n, v in (("pensiones", "Public Transfers, Pensions, Inflows"), ("salud", "Public Transfers, Health, Inflows"), ("educacion", "Public Transfers, Education, Inflows")):
        row[n] = round((prof("Mexico", 2004, v) * w).sum() / yl * 100, 2)
    res.append(row)
print("perfiles México 2004, % ingreso laboral", res)
for c, yy, L in (("Costa Rica", 2013, "Costa Rica"), ("Uruguay", 2013, "Uruguay"), ("Brazil", 2008, "Brazil")):
    P = pesos_anio(L); Y = prof(c, yy, "Labor Income"); o = {}
    for a in (2024, 2050):
        o[a] = {n: round((prof(c, yy, v) * P[a]).sum() / (Y * P[a]).sum() * 100, 1) for n, v in (("pen", "Public Transfers, Pensions, Inflows"), ("sal", "Public Transfers, Health, Inflows"), ("edu", "Public Transfers, Education, Inflows"))}
    print(c, yy, o)
pd.DataFrame(res).to_csv(f"{OUT}/p3_aritmetica_mex.csv", index=False)

# a los 75 años
rows = []
for c, y, n in [("Mexico", 2004, "México, 2004"), ("Costa Rica", 2013, "Costa Rica, 2013"), ("Uruguay", 2013, "Uruguay, 2013"), ("Peru", 2014, "Perú, 2014"), ("Argentina", 2016, "Argentina, 2016"), ("Brazil", 2008, "Brasil, 2008")]:
    k = base(c, y); rows.append({"pais": n, "pen": round(prof(c, y, "Public Transfers, Pensions, Inflows")[75] / k, 2), "sal": round(prof(c, y, "Public Transfers, Health, Inflows")[75] / k, 2)})
pd.DataFrame(rows).to_csv(f"{OUT}/p3_a75.csv", index=False); print(rows)

# salud por edad, México 2014
k = base("Mexico", 2014); pu, pv = prof("Mexico", 2014, "Public Consumption, Health") / k, prof("Mexico", 2014, "Private Consumption, Health") / k
pd.DataFrame({"edad": range(91), "pub": pu.round(4), "pri": pv.round(4)}).to_csv(f"{OUT}/p3_salud_mex2014.csv", index=False)
print("salud 2014 a 5, 40, 75, 85", [(a, round(pu[a], 3), round(pv[a], 3)) for a in (5, 40, 75, 85)], "75 vs 40 total", round((pu[75] + pv[75]) / (pu[40] + pv[40]), 2))

# cuidadoras potenciales: mujeres de 45-64 por persona de 80+
x = age[age.Location == "Latin America and the Caribbean"]
def rc(y):
    g = x[x.Time == y]; return g[g.AgeGrpStart.between(45, 60)].PopFemale.sum() / g[g.AgeGrpStart >= 80].PopTotal.sum()
print("ALC mujeres 45-64 por 80+", round(rc(2024), 2), round(rc(2050), 2))
for y in (2025, 2050):
    w, f = pop(y); print("México motor", y, round(f[45:65].sum() / w[80:].sum(), 2), "80+ M", round(w[80:].sum() / 1e6, 2))
