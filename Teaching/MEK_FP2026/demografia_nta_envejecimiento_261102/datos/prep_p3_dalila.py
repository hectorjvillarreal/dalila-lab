"""Datos de la Parte 3, segunda versión: material de Dalila sobre envejecimiento.

Motor nacional (INEGI, IBGE, Census/CDC), escenario de un hijo por mujer y BID2/motivation.
Sin insumos de ONU ni CONAPO en México y Brasil. Ver README.md de cada carpeta de origen.
"""
import csv, os, re, sys
import numpy as np, pandas as pd

ROOT = os.path.expanduser("~/Dalila")
ENG = f"{ROOT}/GrandPlan/DFD/outputs/public/2026-10_population_mex_bra_usa"
HIJO = f"{ROOT}/GrandPlan/DFD/outputs/public/2026-09_latam_un_hijo/results/lac_tfr1_aggregate.csv"
MOT = f"{ROOT}/Missions/Funded/BID2/motivation/output/tables"
OUT = os.path.dirname(os.path.abspath(__file__))

# 1. 65+ y razón de dependencia de la vejez: resultados guardados del motor
r = pd.read_csv(f"{ENG}/results/projections_national.csv")
r = r[r.scenario == "central"]
names = {"Mexico": "mex", "Brazil": "bra", "United States": "usa"}
for col, f in (("share_65plus_pct", "p3_65mas_nal.csv"), ("oadr", "p3_oadr_nal.csv")):
    t = r.pivot(index="year", columns="country", values=col).rename(columns=names)[["mex", "bra", "usa"]].round(2)
    t.reset_index().to_csv(f"{OUT}/{f}", index=False)
    print(f, t.loc[[2025, 2050]].to_string())

# 2. Un hijo por mujer
h = pd.read_csv(HIJO)
hh = pd.DataFrame({"anio": h.year, "onu": h.un_published.round(1), "esc": h.tfr1.round(1),
                   "menores": h.tfr1_0_14.round(1), "mayores": h.tfr1_65p.round(1)})
hh.to_csv(f"{OUT}/p3_unhijo.csv", index=False)
print(hh[hh.anio.isin([2025, 2035, 2040, 2050, 2100])].to_string(index=False))

# 3. Gasto de bolsillo por edad, 2024 (ENIGH + ENSANUT). Solo forma: índice, 15-29 = 1, promedio de ambos sexos
f = pd.read_csv(f"{MOT}/fig1_age_sex_profile_2024.csv")
for m, tag in (("nta_utilization", "nta"), ("regression", "reg")):
    x = f[f.method == m].pivot(index="age_grp", columns="sex", values="value")
    b = x.loc["15-29"].mean()
    print(tag, "base 15-29", round(b, 1), "85+", (x.loc["85+"] / b).round(2).to_dict(), "65-74", (x.loc["65-74"] / b).round(2).to_dict())
x = f[f.method == "nta_utilization"].pivot(index="age_grp", columns="sex", values="value")
order = ["15-29", "30-44", "45-59", "60-64", "65-74", "75-84", "85+"]
b = x.loc["15-29"].mean()
pd.DataFrame({"pos": range(len(order)), "grupo": order, "mujeres": (x.loc[order, "female"] / b).round(2).values,
              "hombres": (x.loc[order, "male"] / b).round(2).values}).to_csv(f"{OUT}/p3_bolsillo_edad.csv", index=False)

# 4. Salto de 2020 por decil
p = pd.read_csv(f"{MOT}/pandemic_jump_by_decile.csv")
q = pd.DataFrame({"decil": p.decile, "salud": (p.d_salud_pct * 100).round(1), "alimentos": (p.d_alim_pct * 100).round(1),
                  "sin_gasto_18": (p.p_zero_18 * 100).round(1), "sin_gasto_20": (p.p_zero_20 * 100).round(1)})
q.to_csv(f"{OUT}/p3_pandemia.csv", index=False); print(q.to_string(index=False))

# 5. Gasto catastrófico 2024 y necesidad no atendida
c = pd.read_csv(f"{MOT}/fig8_catastrophic_by_decile.csv"); c = c[c.year == 2024]
print("catastrófico 2024 (OMS, 40 %)", (c.set_index("decile").cat40ctp * 100).round(2).to_dict())
g = pd.read_csv(f"{MOT}/fig6_forgone_care.csv")
print(g[g.wave == 2024][["grp", "forgoneTRUE", "cost_forgoneTRUE"]].round(3).head(6).to_string(index=False))

# 6. Motor nacional por edad: México y Brasil
sys.path.insert(0, ENG); sys.argv = ["x"]
import projection_national as PN
eicp = {}
for row in csv.DictReader(open(os.path.join(PN.NOTA, "eic2025_emigrants_age_sex_grafica9.csv"))):
    a = int(re.match(r"(\d+)", row["band"]).group(1)); eicp[a] = (float(row["men_pct"]), float(row["women_pct"]))
s = sum(m + w for m, w in eicp.values()); pr = {}
for a, (m, w) in eicp.items():
    rng = range(a, a + 5) if a < 85 else range(85, PN.TOP + 1)
    for x_ in rng:
        pr[("M", x_)] = pr.get(("M", x_), 0) + m / s / len(rng); pr[("F", x_)] = pr.get(("F", x_), 0) + w / s / len(rng)
b0, k0 = PN.mex_base_and_k(); S = PN.mex_mort(k0); pat = PN.mex_pattern()
RM = PN.project(b0, lambda y, s_: S[(y, s_)], PN.tfr_path(PN.TFR["MEX"], 0.0), lambda y: pat, PN.mex_mig, pr)
ind = PN.bra_ind(); braS = PN.bra_mort(); gen = PN.band_to_single(PN.MIGPROF, {"M": 0.55, "F": 0.45})
bra_nm = lambda y: float(ind.loc[y + 1, "POP_T"] - ind.loc[y, "POP_T"] - (ind.loc[y, "NASC_T"] + ind.loc[y + 1, "NASC_T"]) / 2 + (ind.loc[y, "OBT_T"] + ind.loc[y + 1, "OBT_T"]) / 2)
RB = PN.project(PN.bra_single(2025), lambda y, s_: braS[(y, s_)], PN.tfr_path(PN.TFR["BRA"], 0.0), lambda y: PN.bra_pattern(ind, 2025), bra_nm, gen)
print("control: México 2050", round(PN.tot(RM[2050]) / 1e6, 1), "65+", round(PN.share65(RM[2050]), 1), "| Brasil 2050", round(PN.tot(RB[2050]) / 1e6, 1), "65+", round(PN.share65(RB[2050]), 1))


def pop(R, y):
    m, f_ = R[y]; v = np.array(m) + np.array(f_); w = np.zeros(91); w[:90] = v[:90]; w[90] = v[90:].sum()
    return w, np.array(f_)


def rd1564(R, y):
    w, _ = pop(R, y); return 100 * w[65:].sum() / w[15:65].sum()


fact = {}
for n, R in (("México", RM), ("Brasil", RB)):
    fact[n] = rd1564(R, 2050) / rd1564(R, 2025)
    print(n, "RD 65+/15-64", round(rd1564(R, 2025), 2), round(rd1564(R, 2050), 2), "factor", round(fact[n], 3))

# 7. Cuidadoras potenciales: mujeres de 45-64 por persona de 80+
cu = []
for n, R in (("México", RM), ("Brasil", RB)):
    for y in (2025, 2050):
        w, f_ = pop(R, y); cu.append((n, y, round(f_[45:65].sum() / w[80:].sum(), 2), round(w[80:].sum() / 1e6, 2)))
print("cuidadoras", cu)

# 8. Perfiles fijos NTA por población nacional
d = pd.read_csv(f"{OUT}/ntaccounts_perfiles.csv", low_memory=False)
ages = [f"Age{i}" for i in range(91)]


def prof(c_, y, v):
    x_ = d[(d.Country == c_) & (d.Year == y) & (d["Variable Name"] == v)]
    s_ = x_[x_.VarType == "Smooth Mean"]; x_ = s_ if len(s_) else x_
    return np.nan_to_num(x_.iloc[0][ages].astype(float).values)


rows = []
for n, c_, yy, R in (("México", "Mexico", 2004, RM), ("Brasil", "Brazil", 2008, RB)):
    Y = prof(c_, yy, "Labor Income"); o = {"pais": n, "perfil": yy}
    for a in (2025, 2050):
        w, _ = pop(R, a); yl = (Y * w).sum()
        for k_, v in (("pen", "Public Transfers, Pensions, Inflows"), ("sal", "Public Transfers, Health, Inflows"), ("edu", "Public Transfers, Education, Inflows")):
            o[f"{k_}{a}"] = round((prof(c_, yy, v) * w).sum() / yl * 100, 1)
    rows.append(o)
t = pd.DataFrame(rows); t.to_csv(f"{OUT}/p3_perfiles_nal.csv", index=False); print(t.to_string(index=False))

# 9. Cuenta ilustrativa de México con datos públicos: pensiones 4.7 % (CGPE 2027), salud 2.7 % (OMS, 2023)
m = t[t.pais == "México"].iloc[0]; fa = fact["México"]
print("con perfiles", round(4.7 * (m.pen2050 / m.pen2025 - 1), 1), round(2.7 * (m.sal2050 / m.sal2025 - 1), 1), "| estrés", round(4.7 * (fa - 1), 1), round(2.7 * (fa - 1), 1))
