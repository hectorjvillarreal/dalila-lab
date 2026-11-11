"""Series demográficas de México con la proyección propia (solo datos del INEGI), 2025-2050.
Motor: GrandPlan/DFD/outputs/public/2026-10_population_mex_bra_usa/projection_national.py (escenario central).
Misma llamada que Teaching/MEK_FP2026/demografia_nta_envejecimiento_261102/datos/prep_p3.py.
Salida: l3_nacional.csv (millones y % por grupo de edad). Referencia ONU: l5_ventana.csv (WPP 2024)."""
import csv, os, re, sys
import numpy as np, pandas as pd
ROOT = os.path.expanduser("~/Dalila")
ENG = f"{ROOT}/GrandPlan/DFD/outputs/public/2026-10_population_mex_bra_usa"
OUT = os.path.dirname(os.path.abspath(__file__))
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
rows = []
for y in range(2025, 2051):
    m, f = R[y]; v = np.array(m) + np.array(f); t = v.sum()
    rows.append({"anio": y, "total": round(t / 1e6, 3), "p014": round(v[:15].sum() / 1e6, 3), "p65": round(v[65:].sum() / 1e6, 3),
                 "p80": round(v[80:].sum() / 1e6, 3), "pet": round(v[15:65].sum() / t * 100, 2), "s65": round(v[65:].sum() / t * 100, 2)})
d = pd.DataFrame(rows); d.to_csv(f"{OUT}/l3_nacional.csv", index=False)
print(d[d.anio.isin([2025, 2026, 2030, 2035, 2040, 2045, 2050])].to_string(index=False))
print("cruce 65+ > 0-14:", int(d[d.p65 > d.p014].anio.min()), "| máximo 15-64:", int(d.loc[d.pet.idxmax(), "anio"]), d.pet.max())
print(d[["anio", "pet", "p014", "p65"]].iloc[:14].to_string(index=False))
