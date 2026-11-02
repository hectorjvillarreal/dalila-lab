"""Datos de la Parte 2: perfiles por edad de ntaccounts.org, normalizados por el ingreso laboral medio de 30-49 años."""
import os, numpy as np, pandas as pd
OUT = os.path.dirname(os.path.abspath(__file__))
d = pd.read_csv(f"{OUT}/ntaccounts_perfiles.csv", low_memory=False)
ages = [f"Age{i}" for i in range(91)]
def prof(c, y, v, t=None):
    x = d[(d.Country == c) & (d.Year == y) & (d["Variable Name"] == v)]
    if t: x = x[x.VarType == t]
    else:
        s = x[x.VarType == "Smooth Mean"]; x = s if len(s) else x
    return None if x.empty else x.iloc[0][ages].astype(float).values
def base(c, y): return np.nanmean(prof(c, y, "Labor Income")[30:50])
def lcd(c, y): return (prof(c, y, "Consumption") - prof(c, y, "Labor Income")) / base(c, y)

# diapositiva 2: Filipinas 1999 y Alemania 2003, como la fig. 1.1 del Manual
for c, y, n in [("Philippines", 1999, "fil1999"), ("Germany", 2003, "ale2003"), ("Mexico", 2014, "mex2014"), ("Mexico", 2010, "mex2010"), ("Mexico", 2004, "mex2004")]:
    C, Y = prof(c, y, "Consumption"), prof(c, y, "Labor Income"); k = base(c, y)
    pd.DataFrame({"edad": range(91), "C": (C / k).round(4), "YL": (Y / k).round(4)}).dropna().to_csv(f"{OUT}/p2_{n}.csv", index=False)
    s = np.where(Y > C)[0]; print(n, "superavit", (s.min(), s.max()) if len(s) else None, "C/k 40", round(C[40] / k, 2), "tipo", d[(d.Country == c) & (d.Year == y) & (d["Variable Name"] == "Consumption")].VarType.tolist())

# diapositiva 18: déficit por persona
paises = [("Mexico", 2014, "mex"), ("Brazil", 2008, "bra"), ("Chile", 2018, "chl"), ("Germany", 2008, "ale")]
t = pd.DataFrame({"edad": range(91)})
for c, y, n in paises: t[n] = np.round(lcd(c, y), 4)
t.dropna().to_csv(f"{OUT}/p2_deficit_paises.csv", index=False)
for c, y, n in paises + [("Costa Rica", 2013, "cri"), ("Colombia", 2014, "col"), ("Peru", 2014, "per"), ("Argentina", 2016, "arg"), ("Uruguay", 2013, "ury")]:
    L = lcd(c, y); print(c, y, "max superavit", round(-np.nanmin(L), 3), "en", int(np.nanargmin(L)), "deficit a 75", round(L[75], 2))

# Transferencias públicas recibidas por uso
for c, y in [("Mexico", 2004), ("Brazil", 2008), ("Costa Rica", 2013), ("Peru", 2014), ("Uruguay", 2013), ("Argentina", 2016)]:
    k = base(c, y); r = {}
    for v, n in [("Public Transfers, Education, Inflows", "edu"), ("Public Transfers, Health, Inflows", "sal"), ("Public Transfers, Pensions, Inflows", "pen"), ("Public Transfers, Other In-Kind, Inflows", "oes"), ("Public Transfers, Other Cash, Inflows", "oef"), ("Public Transfers, Inflows", "tot"), ("Public Transfers, Outflows", "pag")]:
        p = prof(c, y, v); r[n] = None if p is None else p / k
    print(c, y, {n: (None if v is None else (round(v[10], 2), round(v[45], 2), round(v[75], 2))) for n, v in r.items()})
    if c == "Mexico" or c == "Brazil":
        pd.DataFrame({"edad": range(91), **{n: np.round(v, 4) for n, v in r.items() if v is not None}}).dropna().to_csv(f"{OUT}/p2_publicas_{c[:3].lower()}{y}.csv", index=False)

# Cómo se financia el déficit de 65+, ponderado con población de WPP por grupos
WPP = os.path.expanduser("~/Dalila/GrandPlan/DFD/outputs/public/2026-09_mexico_2050/data/WPP2024_PopulationByAge5GroupSex_Medium.csv.gz")
age = pd.read_csv(WPP, usecols=["Location", "Time", "AgeGrpStart", "PopTotal"])
def pesos(L, y):
    x = age[(age.Location == L) & (age.Time == y)].set_index("AgeGrpStart").PopTotal
    w = np.zeros(91)
    for a in range(0, 90, 5): w[a:a + 5] = x.get(a, 0) / 5
    w[90] = x[x.index >= 90].sum()
    return w
for c, y, L in [("Mexico", 2004, "Mexico"), ("Costa Rica", 2013, "Costa Rica"), ("Peru", 2014, "Peru"), ("Japan", 2004, "Japan"), ("Germany", 2003, "Germany"), ("Sweden", 2005, "Sweden"), ("Philippines", 2015, "Philippines")]:
    w = pesos(L, y); s = lambda v: np.nansum(prof(c, y, v)[65:] * w[65:])
    try:
        D = s("LifeCycle Deficit"); pu, pr, a = s("Public Transfers"), s("Private Transfers"), s("Asset-based Reallocations")
        print(c, y, "65+ deficit: publicas %.0f%% privadas %.0f%% activos %.0f%% suma %.0f%%" % (pu / D * 100, pr / D * 100, a / D * 100, (pu + pr + a) / D * 100))
    except Exception as e: print(c, y, "sin dato", e)

# diapositiva 14: columnas de área apiladas
for f in ("mex2004", "bra2008"):
    t = pd.read_csv(f"{OUT}/p2_publicas_{f}.csv"); t["otros"] = (t.oes + t.get("oef", 0)).round(4)
    t.to_csv(f"{OUT}/p2_publicas_{f}.csv", index=False)
    v = t[t.edad == 75].iloc[0]; print(f, "75: salud+pensiones/total", round((v.sal + v.pen) / v.tot, 2))
