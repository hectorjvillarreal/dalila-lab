"""Demografía regional para la conferencia RIUSS (12-nov-2026).
Proyección propia de América Latina y el Caribe (49 países y territorios), 2025-2060, con la fecundidad
de cada país fija en su último valor observado (registros civiles, 18 países; México = INEGI, 1.23).
Motor: GrandPlan/DFD/outputs/public/2026-09_latam_un_hijo/lac_tfr1_projection.py (componentes, grupos
quinquenales, pasos de cinco años). Población base y mortalidad fuera de México, migración y patrón de
fecundidad por edad: Naciones Unidas, WPP 2024. Base de México: INEGI, Encuesta Intercensal 2025.
Referencia: misma maquinaria con la fecundidad de la variante media de Naciones Unidas.
Salidas: r3_region.csv, r4_fecundidad.csv, r5_ventana.csv."""
import os, pandas as pd
ROOT = os.path.expanduser("~/Dalila")
ENG = f"{ROOT}/GrandPlan/DFD/outputs/public/2026-09_latam_un_hijo/lac_tfr1_projection.py"
OUT = os.path.dirname(os.path.abspath(__file__))
src = open(ENG).read().split("rows = []; val = {}")[0]      # definiciones y carga; sin la corrida original
g = {"__file__": ENG}; exec(compile(src, ENG, "exec"), g)
names, ind, LT, PA, AGES, SRB, MIGPROF = (g[k] for k in ["names", "ind", "LT", "PA", "AGES", "SRB", "MIGPROF"])
base, eic_base, surv, t25, un_tfr = (g[k] for k in ["base", "eic_base", "surv", "t25", "un_tfr"])

def project(loc, tfr_fn, own, end=2060):
    m, f = eic_base(loc) if (own and names.ISO3_code[loc] == "MEX") else base(loc); y = 2025; res = {}
    def snap():
        v = {a: m[a] + f[a] for a in AGES}; t = sum(v.values())
        return dict(total=t, p014=sum(v[a] for a in (0, 5, 10)), p1564=sum(v[a] for a in AGES if 15 <= a < 65),
                    p65=sum(v[a] for a in AGES if a >= 65), p80=sum(v[a] for a in AGES if a >= 80))
    res[y] = snap()
    while y < end:
        t = min(y + 2, 2100); Sm, Sf = surv(LT[(loc, t, "Male")]), surv(LT[(loc, t, "Female")]); P = PA[(loc, t)]
        tfr = (tfr_fn(y) + tfr_fn(y + 5)) / 2
        nm = {a + 5: m[a] * Sm[a] for a in range(0, 95, 5)}; nf = {a + 5: f[a] * Sf[a] for a in range(0, 95, 5)}
        nm[100] = (m[95] + m[100]) * Sm[95]; nf[100] = (f[95] + f[100]) * Sf[95]
        B = sum(tfr * P[a] * (f[a] + nf.get(a, 0)) / 2 for a in P)
        nm[0] = B * SRB / (1 + SRB) * Sm["b"]; nf[0] = B / (1 + SRB) * Sf["b"]
        M = sum(ind.NetMigrations.get((loc, y + k), 0) for k in range(1, 6))
        for a, p in MIGPROF.items(): nm[a] = nm.get(a, 0) + M * p * .55; nf[a] = nf.get(a, 0) + M * p * .45
        m, f = nm, nf; y += 5; res[y] = snap()
    return res

rows = []
for loc in names.index:
    t0 = t25(loc)
    for esc, r in (("propia", project(loc, lambda y, t0=t0: t0, True)), ("onu", project(loc, un_tfr(loc), False))):
        for y, d in r.items(): rows.append(dict(iso=names.ISO3_code[loc], esc=esc, anio=y, **{k: v / 1000 for k, v in d.items()}))
R = pd.DataFrame(rows)
A = R.groupby(["esc", "anio"])[["total", "p014", "p1564", "p65", "p80"]].sum().reset_index()
def wide(D):
    W = D.pivot(index="anio", columns="esc", values=["total", "p014", "p1564", "p65", "p80"])
    W.columns = [f"{v}_{e}" for v, e in W.columns]
    for e in ("propia", "onu"):
        W[f"pet_{e}"] = W[f"p1564_{e}"] / W[f"total_{e}"] * 100; W[f"s65_{e}"] = W[f"p65_{e}"] / W[f"total_{e}"] * 100
    return W.round(3).reset_index()
W = wide(A); W.to_csv(f"{OUT}/r3_region.csv", index=False)
pd.set_option("display.width", 250); print(W.to_string(index=False))
# ventana: región y países (proyección propia), % de 15 a 64
V = pd.DataFrame({"anio": W.anio, "ALC": W.pet_propia})
for iso in ("BRA", "CHL", "COL", "MEX", "CRI", "ARG"):
    c = R[(R.iso == iso) & (R.esc == "propia")].set_index("anio"); V[iso] = (c.p1564 / c.total * 100).round(2).values
    c2 = c.assign(s65=c.p65 / c.total * 100); print(iso, c2[["total", "p014", "p65", "s65"]].round(2).to_dict("index"))
V.to_csv(f"{OUT}/r5_ventana.csv", index=False); print(V.to_string(index=False))
# fecundidad: observada frente a la estimación de Naciones Unidas para 2025
F = pd.DataFrame([dict(iso=names.ISO3_code[l], observada=t25(l), onu2025=round(float(ind.TFR[(l, 2025)]), 2),
                       onu2050=round(float(ind.TFR[(l, 2050)]), 2), pob2025=project(l, lambda y: 1, True, end=2025)[2025]["total"] / 1000) for l in names.index])
F["registro"] = F.iso.isin(g["OBS"]); F.to_csv(f"{OUT}/r4_fecundidad.csv", index=False)
print(F[F.registro].sort_values("observada").to_string(index=False))
w = F.pob2025 / F.pob2025.sum(); print("TGF regional ponderada: observada %.2f | ONU 2025 %.2f | ONU 2050 %.2f" % ((F.observada * w).sum(), (F.onu2025 * w).sum(), (F.onu2050 * w).sum()))
