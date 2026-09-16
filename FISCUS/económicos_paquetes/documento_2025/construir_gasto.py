"""Construye los .csv de los agregados de gasto, desde los analíticos del PEF
aprobado 2024 y 2025 (Gobierno Federal y entidades de control directo).

OBJETO: aprobado contra aprobado. El PEF aprobado 2025 contra el PEF aprobado
2024, deflactor del PIB de 2025 declarado por el CGPE, 1.043.

Regla propia del documento: toda diferencia en mdp lleva su etiqueta. Se emiten
las dos columnas, `dif_nominal` y `dif_real`, nunca una sola sin nombre.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fiscus import an, mdp, real, dif_real, dif_nominal, emitir

DEF = 1.043  # deflactor del PIB 2025, CGPE 2025 Anexo II.5 p. 81 (4.3 %)
FUENTE = {"documento": "Analiticos del PEF aprobado 2024 y 2025",
          "ubicacion": "ac01_ra_pp_ur_og / ac01_ra_f_ur_og y sus versiones _efe, hoja Hoja1",
          "tier": "oficial_primaria",
          "nota": "PEF aprobado, no proyecto. Deflactor 1.043 (CGPE 2025 Anexo II.5). "
                  "dif_real en pesos de 2025."}

a24, a25 = an(2024, "gf_pp"), an(2025, "gf_pp")
e24, e25 = an(2024, "ent_pp"), an(2025, "ent_pp")


def comparar(s24, s25, etiqueta="concepto"):
    """Une dos series indexadas y devuelve filas con las dos diferencias."""
    claves = sorted(set(s24.index) | set(s25.index))
    filas = []
    for k in claves:
        v24, v25 = float(s24.get(k, 0.0)), float(s25.get(k, 0.0))
        filas.append([k, mdp(v24), mdp(v25),
                      mdp(dif_nominal(v25, v24)),
                      mdp(dif_real(v25, v24, DEF)),
                      real(v25, v24, DEF) if v24 else ""])
    filas.sort(key=lambda r: -r[2])
    return filas

ENC = ["concepto", "mdp_2024", "mdp_2025", "dif_nominal_mdp", "dif_real_mdp", "var_real_pct"]

# ------------------------------------------------------- C4.2 por ramo (GF) ---
# OJO: se agrupa por NUMERO de ramo y no por su nombre completo. El Ramo 38 se
# llamaba "Humanidades, Ciencias, Tecnologias e Innovacion" en 2024 y "Ciencia,
# Humanidades, Tecnologia e Innovacion" en 2025. Agrupar por nombre lo parte en dos
# y produce un ramo que desaparece con 33,170.7 y otro que aparece con 33,295.9:
# una variacion contable de 100 % que no existe. Es exactamente el error de
# perimetro que este proyecto le senala al genero desde 2020, cometido por nuestra
# propia herramienta.
n24 = a24.RAMO.astype(str).str[:2]
n25 = a25.RAMO.astype(str).str[:2]
etiqueta = {**dict(zip(n24, a24.RAMO.astype(str))), **dict(zip(n25, a25.RAMO.astype(str)))}
s24 = a24.assign(N=n24).groupby("N")["IMPORTE"].sum().rename(index=lambda k: etiqueta[k])
s25 = a25.assign(N=n25).groupby("N")["IMPORTE"].sum().rename(index=lambda k: etiqueta[k])
filas = comparar(s24, s25)
emitir("gasto_ramos.csv", filas, ENC, dict(FUENTE, cuadro="C4.2",
       nota=FUENTE["nota"] + " Agrupado por NUMERO de ramo, no por nombre: el Ramo 38 "
            "cambia de nombre entre 2024 y 2025 y agruparlo por nombre inventa una "
            "variacion de 100 % que no existe."))

# ------------------------------------------- por entidad de control directo ---
filas = comparar(e24.groupby("ENTIDAD")["IMPORTE"].sum(), e25.groupby("ENTIDAD")["IMPORTE"].sum())
emitir("gasto_entidades.csv", filas, ENC, dict(FUENTE, cuadro="C4.2b"))

# ------------------------------- C4.3 clasificacion economica: tipo de gasto ---
# Las etiquetas de TG se ADJUDICARON CONTRA LOS DATOS, no se asumieron: para cada
# codigo se leyeron sus partidas especificas dominantes. El hallazgo que importa es
# que TG 4 es pensiones y jubilaciones (partidas 45201 pago de pensiones y 45203
# transferencias para el pago de pensiones), no TG 2 como se habia supuesto.
TG = {0: "aportaciones a fideicomisos", 1: "gasto corriente",
      2: "capital e inversion financiera", 3: "inversion fisica y provisiones",
      4: "PENSIONES Y JUBILACIONES", 5: "participaciones",
      7: "subsidios", 9: "aportaciones a fideicomisos (otros)"}
def por_tg(d):
    s = d.groupby("TG")["IMPORTE"].sum()
    return s.rename(index=lambda k: f"TG {int(k)} {TG.get(int(k), '')}".strip())
filas = comparar(por_tg(a24), por_tg(a25))
emitir("gasto_tipo.csv", filas, ENC, dict(FUENTE, cuadro="C4.3a",
       nota=FUENTE["nota"] + " Etiquetas de TG adjudicadas contra las partidas especificas dominantes de cada codigo, no supuestas. Solo Gobierno Federal."))

# ------------------------------- C4.3 clasificacion economica: capitulo 1000-9000 ---
def por_cap(d):
    cap = d["PE"].astype(str).str.strip().str[0] + "000"
    return d.assign(CAP=cap).groupby("CAP")["IMPORTE"].sum()
filas = comparar(por_cap(a24), por_cap(a25))
emitir("gasto_capitulo.csv", filas, ENC, dict(FUENTE, cuadro="C4.3b",
       nota=FUENTE["nota"] + " Capitulo = primer digital de la partida especifica (PE). Solo GF."))

# ------------------------------------- C4.4 clasificacion funcional (GF + ent) ---
FIN = {1: "Gobierno", 2: "Desarrollo social", 3: "Desarrollo economico",
       4: "Otras no clasificadas"}
def por_fn(d):
    if "F" not in d.columns:
        return None
    et = d.apply(lambda r: f"{int(r['F'])}.{int(r['FN'])}"
                 if r["F"] == r["F"] and r["FN"] == r["FN"] else "sin clasificar", axis=1)
    return d.assign(K=et).groupby("K")["IMPORTE"].sum()
f24 = an(2024, "gf_f"); f25 = an(2025, "gf_f")
filas = comparar(por_fn(f24), por_fn(f25))
emitir("gasto_funcional.csv", filas, ENC, dict(FUENTE, cuadro="C4.4",
       nota=FUENTE["nota"] + " Clave = finalidad.funcion. Solo Gobierno Federal, bruto."))

# --------------------------------------------- C4.6 diffs de codigos 2024-2025 ---
def claves(d, col):
    return set(d[col].dropna().astype(str).unique())
dif = []
for etiqueta, col, dd24, dd25 in [("ramo", "RAMO", a24, a25),
                                  ("programa presupuestario", "CLAVE_PP", a24, a25),
                                  ("unidad responsable", "UR", a24, a25)]:
    s24, s25 = claves(dd24, col), claves(dd25, col)
    for k in sorted(s25 - s24):
        v = mdp(dd25[dd25[col].astype(str) == k]["IMPORTE"].sum())
        dif.append([etiqueta, "aparece en 2025", k, "", v])
    for k in sorted(s24 - s25):
        v = mdp(dd24[dd24[col].astype(str) == k]["IMPORTE"].sum())
        dif.append([etiqueta, "desaparece en 2025", k, v, ""])
emitir("diffs_2024_2025.csv", dif,
       ["nivel", "cambio", "clave", "mdp_2024", "mdp_2025"],
       dict(FUENTE, cuadro="C4.6",
            nota=FUENTE["nota"] + " Se anticipan, no se descubren: un codigo que aparece o "
                 "desaparece produce una variacion contable que no es presupuestal."))

print("emitidos: gasto_ramos, gasto_entidades, gasto_tipo, gasto_capitulo, gasto_funcional, diffs_2024_2025")
