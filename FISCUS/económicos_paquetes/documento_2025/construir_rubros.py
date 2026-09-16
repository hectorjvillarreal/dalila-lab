"""Construye los .csv de los capítulos por rubro, desde los analíticos del PEF
aprobado 2024 y 2025. Cada perímetro va declarado en el encabezado de su bloque.

Aprobado contra aprobado. Deflactor 1.043 (CGPE 2025, Anexo II.5, p. 81).
Toda diferencia en mdp se emite dos veces, nominal y real, nunca una sola.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fiscus import an, mdp, real, dif_real, dif_nominal, emitir

DEF = 1.043
ENC = ["concepto", "mdp_2024", "mdp_2025", "dif_nominal_mdp", "dif_real_mdp", "var_real_pct"]
BASE = {"documento": "Analiticos del PEF aprobado 2024 y 2025",
        "tier": "oficial_primaria"}

g24, g25 = an(2024, "gf_f"), an(2025, "gf_f")
p24, p25 = an(2024, "gf_pp"), an(2025, "gf_pp")
e24, e25 = an(2024, "ent_pp"), an(2025, "ent_pp")
ef24, ef25 = an(2024, "ent_f"), an(2025, "ent_f")


def comparar(s24, s25):
    filas = []
    for k in sorted(set(s24.index) | set(s25.index)):
        v24, v25 = float(s24.get(k, 0.0)), float(s25.get(k, 0.0))
        filas.append([k, mdp(v24), mdp(v25), mdp(dif_nominal(v25, v24)),
                      mdp(dif_real(v25, v24, DEF)), real(v25, v24, DEF) if v24 else ""])
    return sorted(filas, key=lambda r: -r[2])


def total(df, **cond):
    s = df
    for k, v in cond.items():
        s = s[s[k] == v] if not isinstance(v, (list, tuple)) else s[s[k].isin(v)]
    return s["IMPORTE"].sum()


# ============================================================== PENSIONES ====
# PERIMETRO, adjudicado contra la cifra oficial y no supuesto: pensiones y
# jubilaciones de la clasificacion economica = tipo de gasto 4 de las entidades de
# control directo MAS el tipo de gasto 4 del Gobierno Federal EXCLUYENDO la partida
# 45203 "Transferencias para el pago de pensiones y jubilaciones", que es
# precisamente el flujo del GF hacia las entidades y se contaria dos veces.
# Verificacion: 2024 da 1,499,038.6 mdp = 4.36 % del PIB y 2025 da 1,637,665.1 =
# 4.53 %, contra 4.4 y 4.5 que publica el CGPE 2025 Anexo III.2 (p. 85).
def pensiones_consolidado(gf, ent):
    directo = gf[(gf.TG == 4) & (~gf.PE.astype(str).str.startswith("45203"))]["IMPORTE"].sum()
    return directo + ent[ent.TG == 4]["IMPORTE"].sum()

filas = []
for etiq, s24, s25 in [
    ("Entidades de control directo (pago directo)",
     total(e24, TG=4), total(e25, TG=4)),
    ("Gobierno Federal, pago directo (sin 45203)",
     p24[(p24.TG == 4) & (~p24.PE.astype(str).str.startswith("45203"))]["IMPORTE"].sum(),
     p25[(p25.TG == 4) & (~p25.PE.astype(str).str.startswith("45203"))]["IMPORTE"].sum()),
    ("CONSOLIDADO (clasificacion economica)",
     pensiones_consolidado(p24, e24), pensiones_consolidado(p25, e25)),
    ("Partida informativa: transferencias del GF a las entidades (45203)",
     p24[p24.PE.astype(str).str.startswith("45203")]["IMPORTE"].sum(),
     p25[p25.PE.astype(str).str.startswith("45203")]["IMPORTE"].sum()),
]:
    filas.append([etiq, mdp(s24), mdp(s25), mdp(dif_nominal(s25, s24)),
                  mdp(dif_real(s25, s24, DEF)), real(s25, s24, DEF)])
for ent_nom in sorted(set(e25.ENTIDAD.dropna().unique()) | set(e24.ENTIDAD.dropna().unique())):
    v24 = e24[(e24.ENTIDAD == ent_nom) & (e24.TG == 4)]["IMPORTE"].sum()
    v25 = e25[(e25.ENTIDAD == ent_nom) & (e25.TG == 4)]["IMPORTE"].sum()
    if v24 or v25:
        filas.append([f"  ... {ent_nom}", mdp(v24), mdp(v25), mdp(dif_nominal(v25, v24)),
                      mdp(dif_real(v25, v24, DEF)), real(v25, v24, DEF) if v24 else ""])
emitir("pensiones_institucion.csv", filas, ENC, dict(BASE, cuadro="C5.1",
    ubicacion="tipo de gasto 4, GF y entidades; partida 45203 excluida del GF",
    nota="PEF aprobado, no proyecto. Perimetro adjudicado contra el 4.4 y 4.5 % del PIB "
         "que publica el CGPE 2025 Anexo III.2, no supuesto. dif_real en pesos de 2025."))

# ================================================================= SALUD ====
# PERIMETRO: funcion 2.3 Salud. El canonico de 2022 se ancla al cuadro de la
# exposicion de motivos del PPEF, que no existe para 2022-2026 (esta caida en el
# servidor). Se reconstruye desde los analiticos por funcion, en dos bloques
# etiquetados. DECLARADO: los analiticos son BRUTOS y aquel cuadro era NETO.
filas = []
gf_s24 = g24[(g24.F == 2) & (g24.FN == 3)]
gf_s25 = g25[(g25.F == 2) & (g25.FN == 3)]
en_s24 = ef24[(ef24.F == 2) & (ef24.FN == 3)]
en_s25 = ef25[(ef25.F == 2) & (ef25.FN == 3)]
filas.append(["TOTAL funcion Salud (GF + entidades, bruto)",
              mdp(gf_s24["IMPORTE"].sum() + en_s24["IMPORTE"].sum()),
              mdp(gf_s25["IMPORTE"].sum() + en_s25["IMPORTE"].sum()),
              mdp(dif_nominal(gf_s25["IMPORTE"].sum() + en_s25["IMPORTE"].sum(),
                              gf_s24["IMPORTE"].sum() + en_s24["IMPORTE"].sum())),
              mdp(dif_real(gf_s25["IMPORTE"].sum() + en_s25["IMPORTE"].sum(),
                           gf_s24["IMPORTE"].sum() + en_s24["IMPORTE"].sum(), DEF)),
              real(gf_s25["IMPORTE"].sum() + en_s25["IMPORTE"].sum(),
                   gf_s24["IMPORTE"].sum() + en_s24["IMPORTE"].sum(), DEF)])
filas.append(["-- Gobierno Federal, por ramo --", "", "", "", "", ""])
filas += comparar(gf_s24.groupby("RAMO")["IMPORTE"].sum(), gf_s25.groupby("RAMO")["IMPORTE"].sum())
filas.append(["-- Entidades de control directo --", "", "", "", "", ""])
filas += comparar(en_s24.groupby("ENTIDAD")["IMPORTE"].sum(), en_s25.groupby("ENTIDAD")["IMPORTE"].sum())
emitir("salud_subsistema.csv", filas, ENC, dict(BASE, cuadro="C6.1",
    ubicacion="finalidad 2, funcion 3 Salud, GF y entidades",
    nota="PEF aprobado, no proyecto. BRUTO: los analiticos no netean las aportaciones "
         "y transferencias que el cuadro de la exposicion de motivos si neteaba. La "
         "exposicion de motivos del PPEF no existe para 2022-2026, de ahi la sustitucion "
         "de fuente. dif_real en pesos de 2025."))

# ============================================================= EDUCACION ====
# PERIMETRO: funcion 2.5 Educacion del Gobierno Federal, bruta. Las entidades de
# control directo tienen cero en esta funcion (verificado en 2024).
ed24 = g24[(g24.F == 2) & (g24.FN == 5)]
ed25 = g25[(g25.F == 2) & (g25.FN == 5)]
filas = [["TOTAL funcion Educacion (GF, bruto)", mdp(ed24["IMPORTE"].sum()),
          mdp(ed25["IMPORTE"].sum()), mdp(dif_nominal(ed25["IMPORTE"].sum(), ed24["IMPORTE"].sum())),
          mdp(dif_real(ed25["IMPORTE"].sum(), ed24["IMPORTE"].sum(), DEF)),
          real(ed25["IMPORTE"].sum(), ed24["IMPORTE"].sum(), DEF)],
         ["-- por ramo --", "", "", "", "", ""]]
filas += comparar(ed24.groupby("RAMO")["IMPORTE"].sum(), ed25.groupby("RAMO")["IMPORTE"].sum())
filas.append(["-- por subfuncion --", "", "", "", "", ""])
s24 = ed24.groupby("SF")["IMPORTE"].sum().rename(index=lambda k: f"subfuncion {int(k)}")
s25 = ed25.groupby("SF")["IMPORTE"].sum().rename(index=lambda k: f"subfuncion {int(k)}")
filas += comparar(s24, s25)
emitir("educacion_ramo.csv", filas, ENC, dict(BASE, cuadro="C7.1 y C7.2",
    ubicacion="finalidad 2, funcion 5 Educacion, Gobierno Federal",
    nota="PEF aprobado, no proyecto. Bruto. Las entidades de control directo tienen "
         "cero en funcion Educacion. dif_real en pesos de 2025."))

# ==================================================== FONE POR ENTIDAD ====
fone24 = p24[p24.CLAVE_PP.isin(["I013", "I014", "I015", "I016"])]
fone25 = p25[p25.CLAVE_PP.isin(["I013", "I014", "I015", "I016"])]
filas = [["FONE TOTAL", mdp(fone24["IMPORTE"].sum()), mdp(fone25["IMPORTE"].sum()),
          mdp(dif_nominal(fone25["IMPORTE"].sum(), fone24["IMPORTE"].sum())),
          mdp(dif_real(fone25["IMPORTE"].sum(), fone24["IMPORTE"].sum(), DEF)),
          real(fone25["IMPORTE"].sum(), fone24["IMPORTE"].sum(), DEF)],
         ["-- por entidad federativa --", "", "", "", "", ""]]
filas += comparar(fone24.groupby("EF")["IMPORTE"].sum(), fone25.groupby("EF")["IMPORTE"].sum())
emitir("fone_entidad.csv", filas, ENC, dict(BASE, cuadro="C7.3",
    ubicacion="programas I013 a I016 del Ramo 33, columna EF del analitico",
    nota="PEF aprobado, no proyecto. La Ciudad de Mexico no recibe FONE: su educacion "
         "basica y normal va por el Ramo 25. dif_real en pesos de 2025."))

# ================================================================ ENERGIA ====
en24 = g24[(g24.F == 3) & (g24.FN == 3)]
en25 = g25[(g25.F == 3) & (g25.FN == 3)]
ene24 = ef24[(ef24.F == 3) & (ef24.FN == 3)]
ene25 = ef25[(ef25.F == 3) & (ef25.FN == 3)]
filas = [["TOTAL funcion Combustibles y Energia (GF + entidades, bruto)",
          mdp(en24["IMPORTE"].sum() + ene24["IMPORTE"].sum()),
          mdp(en25["IMPORTE"].sum() + ene25["IMPORTE"].sum()), "", "", ""],
         ["-- Gobierno Federal, por ramo --", "", "", "", "", ""]]
filas += comparar(en24.groupby("RAMO")["IMPORTE"].sum(), en25.groupby("RAMO")["IMPORTE"].sum())
filas.append(["-- Entidades --", "", "", "", "", ""])
filas += comparar(ene24.groupby("ENTIDAD")["IMPORTE"].sum(), ene25.groupby("ENTIDAD")["IMPORTE"].sum())
emitir("energia_gasto.csv", filas, ENC, dict(BASE, cuadro="C9.1",
    ubicacion="finalidad 3, funcion 3 Combustibles y Energia, GF y entidades",
    nota="PEF aprobado, no proyecto. Bruto. dif_real en pesos de 2025."))

# ============================================================== SEGURIDAD ====
# PERIMETRO de la casa, fijado en 2020: quince subfunciones de cinco funciones de
# la finalidad 1 Gobierno. Se enumeran para que el lector pueda rehacerlo.
SEG = {2: [1, 2, 3, 4], 3: [2, 3, 4, 5], 6: [1, 2, 3], 7: [1, 2, 3, 4], 8: [4, 5]}
def seg(d):
    m = False
    for fn, sfs in SEG.items():
        m = m | ((d.F == 1) & (d.FN == fn) & (d.SF.isin(sfs)))
    return d[m]
sg24, sg25 = seg(g24), seg(g25)
filas = [["TOTAL perimetro de seguridad (15 subfunciones)", mdp(sg24["IMPORTE"].sum()),
          mdp(sg25["IMPORTE"].sum()), mdp(dif_nominal(sg25["IMPORTE"].sum(), sg24["IMPORTE"].sum())),
          mdp(dif_real(sg25["IMPORTE"].sum(), sg24["IMPORTE"].sum(), DEF)),
          real(sg25["IMPORTE"].sum(), sg24["IMPORTE"].sum(), DEF)],
         ["-- por funcion y subfuncion --", "", "", "", "", ""]]
k = lambda d: d.apply(lambda r: f"1.{int(r.FN)}.{int(r.SF)} {r.FN_NOM[:34]}", axis=1)
filas += comparar(sg24.assign(K=k(sg24)).groupby("K")["IMPORTE"].sum(),
                  sg25.assign(K=k(sg25)).groupby("K")["IMPORTE"].sum())
filas.append(["-- por ramo --", "", "", "", "", ""])
filas += comparar(sg24.groupby("RAMO")["IMPORTE"].sum(), sg25.groupby("RAMO")["IMPORTE"].sum())
emitir("seguridad_subfuncion.csv", filas, ENC, dict(BASE, cuadro="C10.1",
    ubicacion="finalidad 1, funciones 2/3/6/7/8, quince subfunciones enumeradas en el archivo",
    nota="PEF aprobado, no proyecto. Perimetro propio de la casa, fijado en 2020 y "
         "enumerado para que sea reproducible. dif_real en pesos de 2025."))

# ========================================================== FEDERALIZADO ====
filas = []
for etiq, r in [("Ramo 28 Participaciones", "28"), ("Ramo 33 Aportaciones", "33"),
                ("Ramo 25 Previsiones y aportaciones", "25")]:
    v24 = p24[p24.RAMO.astype(str).str.startswith(r)]["IMPORTE"].sum()
    v25 = p25[p25.RAMO.astype(str).str.startswith(r)]["IMPORTE"].sum()
    filas.append([etiq, mdp(v24), mdp(v25), mdp(dif_nominal(v25, v24)),
                  mdp(dif_real(v25, v24, DEF)), real(v25, v24, DEF)])
filas.append(["-- Ramo 33 por fondo --", "", "", "", "", ""])
f33_24 = p24[p24.RAMO.astype(str).str.startswith("33")]
f33_25 = p25[p25.RAMO.astype(str).str.startswith("33")]
filas += comparar(f33_24.groupby("CLAVE_PP")["IMPORTE"].sum(),
                  f33_25.groupby("CLAVE_PP")["IMPORTE"].sum())
filas.append(["-- Ramos 28 y 33 por entidad federativa --", "", "", "", "", ""])
fe24 = p24[p24.RAMO.astype(str).str.startswith(("28", "33"))]
fe25 = p25[p25.RAMO.astype(str).str.startswith(("28", "33"))]
filas += comparar(fe24.groupby("EF")["IMPORTE"].sum(), fe25.groupby("EF")["IMPORTE"].sum())
emitir("federalizado.csv", filas, ENC, dict(BASE, cuadro="C11.1 y C11.2",
    ubicacion="ramos 25, 28 y 33 del analitico de Gobierno Federal, columna EF",
    nota="PEF aprobado, no proyecto. No incluye convenios de reasignacion, que viven "
         "en los ramos sectoriales. dif_real en pesos de 2025."))

# ============================================================== INVERSION ====
def cap(d, c):
    return d[d.PE.astype(str).str.startswith(c)]["IMPORTE"].sum()
filas = []
for etiq, c in [("Capitulo 6000 Inversion publica (obra)", "6"),
                ("Capitulo 5000 Bienes muebles e inmuebles", "5"),
                ("Capitulo 7000 Inversiones financieras y otras provisiones", "7")]:
    v24 = cap(p24, c) + cap(e24, c)
    v25 = cap(p25, c) + cap(e25, c)
    filas.append([etiq + " (GF + entidades)", mdp(v24), mdp(v25), mdp(dif_nominal(v25, v24)),
                  mdp(dif_real(v25, v24, DEF)), real(v25, v24, DEF)])
filas.append(["-- Capitulo 6000 por ramo (GF) --", "", "", "", "", ""])
o24 = p24[p24.PE.astype(str).str.startswith("6")]
o25 = p25[p25.PE.astype(str).str.startswith("6")]
filas += comparar(o24.groupby("RAMO")["IMPORTE"].sum(), o25.groupby("RAMO")["IMPORTE"].sum())
emitir("inversion.csv", filas, ENC, dict(BASE, cuadro="C8.1 y C8.2",
    ubicacion="capitulos 5000, 6000 y 7000 del objeto del gasto, GF y entidades",
    nota="PEF aprobado, no proyecto. Capitulo 6000 es obra publica DIRECTA; no incluye "
         "la infraestructura que se transfiere a estados por el capitulo 8000. "
         "dif_real en pesos de 2025."))

print("emitidos: pensiones_institucion, salud_subsistema, educacion_ramo, fone_entidad,")
print("          energia_gasto, seguridad_subfuncion, federalizado, inversion")
