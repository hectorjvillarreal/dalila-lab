"""Coordenadas de las gráficas del deck CIJUF (20-nov-2026).

Fuentes (sin red, todo local):
  ../../nta_dem/profiles_2024_age_sex.csv   perfiles NTA_ITED 2024 por edad simple y sexo
                                             (corrida local de badcf23; pesos de 2024, anuales)
  ../../nta_dem/population_mex.csv          motor demográfico nacional DFD (solo INEGI), 2025-2050
  ../../nta_dem/projection_aggregates.csv   perfiles 2024 fijos x población proyectada
Salida: coordenadas.txt (se pegan en el .tex) y verificaciones impresas.
Unidades de las gráficas de perfiles: miles de pesos de 2024, trimestrales per cápita (anual / 4).
"""
from pathlib import Path
import pandas as pd

AQUI = Path(__file__).resolve().parent
DEM = AQUI.parents[1] / "nta_dem"
prof = pd.read_csv(DEM / "profiles_2024_age_sex.csv")
pop = pd.read_csv(DEM / "population_mex.csv")
agg = pd.read_csv(DEM / "projection_aggregates.csv")

FLUJOS = ["C", "YL", "tau_pub_in", "tau_pub_out", "tau_ext", "tau_priv", "YA_minus_S", "LCD"]
for f in FLUJOS:
    prof[f + "_t"] = prof[f] * prof["enigh_pop"]

def suave(serie):
    """Promedio móvil centrado de tres edades, solo para mostrar (atenúa el redondeo de edades)."""
    return serie.rolling(3, center=True, min_periods=1).mean()

def coords(xs, ys, nd=2):
    return "".join(f"({x},{y:.{nd}f})" for x, y in zip(xs, ys))

out = []
# A. Consumo e ingreso laboral por edad, ambos sexos
tot = prof.groupby("age")[[f + "_t" for f in FLUJOS] + ["enigh_pop"]].sum()
pc = tot[[f + "_t" for f in FLUJOS]].div(tot["enigh_pop"], axis=0) / 4 / 1000
pc.columns = FLUJOS
out.append("% A. C(a) ambos sexos, suavizado\n" + coords(pc.index, suave(pc["C"])))
out.append("% A. YL(a) ambos sexos, suavizado\n" + coords(pc.index, suave(pc["YL"])))
print("A: edades con YL > C (ambos sexos):", list(pc.index[pc["YL"] > pc["C"]]))

# B y C. Por sexo
for s in ["M", "F"]:
    p = prof[prof.sex == s].set_index("age")
    out.append(f"% B. YL(a) {s}, suavizado\n" + coords(p.index, suave(p["YL"] / 4000)))
    out.append(f"% C. LCD(a) {s}, suavizado\n" + coords(p.index, suave(p["LCD"] / 4000)))
    sup = list(p.index[p["LCD"] < 0])
    print(f"C: {s} edades con superávit:", (min(sup), max(sup)) if sup else "ninguna",
          "| mínimo LCD 25-59 = %.0f a %d" % (p.loc[25:59, "LCD"].min() / 4, p.loc[25:59, "LCD"].idxmin()))
print("C: participación femenina en LCD agregado = %.1f %%" %
      (100 * prof[prof.sex == "F"]["LCD_t"].sum() / prof["LCD_t"].sum()))

# D. Población 0-14 y 60+, escenario central
pc_ = pop[pop.scenario == "central"].copy()
g = pc_.assign(grupo=pd.cut(pc_.age, [-1, 14, 59, 200], labels=["0-14", "15-59", "60+"]))\
       .groupby(["year", "grupo"], observed=True)["population"].sum().unstack() / 1e6
anios = list(range(2025, 2051))
out.append("% D. 0-14 millones\n" + coords(anios, g.loc[anios, "0-14"], 1))
out.append("% D. 60+ millones\n" + coords(anios, g.loc[anios, "60+"], 1))
cruce = g.index[g["60+"] > g["0-14"]].min()
print("D: 0-14 y 60+ en 2025/2050:", g.loc[[2025, 2050], ["0-14", "60+"]].round(1).to_dict(),
      "| 60+ supera a 0-14 en", cruce, "| 60+ % 2025/2050:",
      (100 * g["60+"] / g.sum(axis=1)).loc[[2025, 2050]].round(1).tolist())

# E. Composición del financiamiento por grupo (participación en la suma de componentes)
def grupo(sub, lo, hi):
    q = sub[(sub.age >= lo) & (sub.age <= hi)]
    P = q["enigh_pop"].sum()
    r = {f: q[f + "_t"].sum() / P / 4 for f in FLUJOS}
    r["pub_neta"] = r["tau_pub_in"] - r["tau_pub_out"]
    return r
for lab, (lo, hi) in {"0-14": (0, 14), "60+": (60, 200)}.items():
    r = grupo(prof, lo, hi)
    comp = {k: r[k] for k in ["pub_neta", "tau_priv", "tau_ext", "YA_minus_S"]}
    s = sum(comp.values())
    print(f"E: {lab} participaciones %:", {k: round(100 * v / s, 1) for k, v in comp.items()},
          "| suma componentes / LCD = %.2f" % (s / r["LCD"]))

# F. Mayores de 60 por sexo (miles de pesos trimestrales per cápita)
for s in ["M", "F"]:
    r = grupo(prof[prof.sex == s], 60, 200)
    vals = [r["LCD"], r["pub_neta"], r["YA_minus_S"], r["tau_ext"], r["tau_priv"]]
    out.append(f"% F. 60+ {s}: LCD, pub neta, activos, exterior, privadas\n" +
               " ".join(f"{v/1000:.2f}" for v in vals))
    print(f"F: 60+ {s}", [round(v) for v in vals])

# G. Proyección: transferencias públicas netas y LCD (billones de pesos de 2024)
for esc in ["central", "low", "high"]:
    a = agg[agg.scenario == esc].set_index("year")
    out.append(f"% G. tau_pub_net {esc}\n" + coords(a.index, a["tau_pub_net"], 2))
a = agg[agg.scenario == "central"].set_index("year")
out.append("% G. LCD central\n" + coords(a.index, a["LCD"], 2))
print("G: central 2025/2050 tau_pub_net", a.loc[[2025, 2050], "tau_pub_net"].tolist(),
      "LCD", a.loc[[2025, 2050], "LCD"].tolist(), "razón de soporte", a.loc[[2025, 2050], "support_ratio"].tolist())
print("G: C agregado 2024 (billones) = %.2f" % (prof["C_t"].sum() / 1e12))

(AQUI / "coordenadas.txt").write_text("\n".join(out) + "\n")
