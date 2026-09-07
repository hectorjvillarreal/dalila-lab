#!/usr/bin/env python3
"""Construye datos/ para el documento 2026. Todo por CLAVE, nunca por nombre.

Línea P (primaria): proyecto 2026 contra proyecto 2025.
Línea G (del género): proyecto 2026 contra aprobado 2025.
Deflactor 1.048 (CGPE 2026, Anexo III.1).
"""
import sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fiscus26 import analitico, csv_proyecto, clave, cod_pp, DEFLACTOR, PIB

SAL = Path(__file__).resolve().parent / "datos"
SAL.mkdir(exist_ok=True)
F = []   # filas de _fuentes.csv


def fuente(archivo, concepto, doc, ubic, tier="oficial_primaria", nota=""):
    F.append(dict(archivo=archivo, concepto=concepto, documento=doc, ubicacion=ubic,
                  tier=tier, nota=nota))


def cmp3(v25p, v26, v25a=None):
    """Devuelve las columnas de comparación de las dos líneas."""
    d = dict(mdp_2025_proyecto=v25p, mdp_2026=v26,
             dif_nominal_P=v26 - v25p, dif_real_P=v26 - v25p * DEFLACTOR,
             var_real_pct_P=(v26 / (v25p * DEFLACTOR) - 1) * 100 if v25p else float("nan"))
    if v25a is not None:
        d.update(mdp_2025_aprobado=v25a, dif_nominal_G=v26 - v25a,
                 dif_real_G=v26 - v25a * DEFLACTOR,
                 var_real_pct_G=(v26 / (v25a * DEFLACTOR) - 1) * 100 if v25a else float("nan"))
    return d


def marco(anio, etapa, corte="gf-ramo-programa-ur-objeto"):
    gf = analitico(anio, corte, etapa)
    ef = analitico(anio, corte.replace("gf-", "entidades-"), etapa)
    if "funcion" in corte:
        for d in (gf, ef):
            d["F_K"], d["FN_K"], d["SF_K"] = clave(d["F"]), clave(d["FN"]), clave(d["SF"])
    else:
        gf["PP_K"] = cod_pp(gf); ef["PP_K"] = ef["PP"].astype(str).str.strip().str[:4]
    gf["RAMO_K"] = clave(gf["RAMO"]); gf["UR_K"] = gf["UR"].astype(str).str.strip().str.split().str[0]
    ef["RAMO_K"] = ef["ENTIDAD"].astype(str).str.strip().str.split().str[0]
    ef["UR_K"] = ef["RAMO_K"]
    gf["NOMBRE"] = gf["RAMO"].astype(str).str.strip(); ef["NOMBRE"] = ef["ENTIDAD"].astype(str).str.strip()
    return pd.concat([gf, ef], ignore_index=True)


def por(df, llaves):
    return df.groupby(llaves)["MDP"].sum()


# ---------------------------------------------------------------- 1. macro y finanzas
def macro():
    m = pd.DataFrame([
        ("PIB, crecimiento real (rango)", "[2.0,3.0]", "[0.5,1.5]", "[1.8,2.8]"),
        ("PIB nominal (miles de millones de pesos)", 36166.4, 36125.5, 38715.9),
        ("Deflactor del PIB (%)", 4.3, 5.2, 4.8),
        ("Inflación dic/dic (%)", 3.5, 3.8, 3.0),
        ("Inflación promedio (%)", 3.8, 4.2, 3.5),
        ("Tipo de cambio fin de periodo", 18.5, 19.9, 18.9),
        ("Tipo de cambio promedio", 18.7, 19.6, 19.3),
        ("Cetes 28 nominal fin de periodo (%)", 8.0, 7.3, 6.0),
        ("Cetes 28 nominal promedio (%)", 8.9, 8.4, 6.6),
        ("Cetes 28 real acumulada (%)", 5.6, 4.8, 3.6),
        ("Cuenta corriente (% del PIB)", -0.4, -0.3, -0.6),
        ("Petróleo, precio promedio (dls/barril)", 57.8, 62.0, 54.9),
        ("Plataforma de producción (mbd)", 1891.2, 1713.9, 1794.0),
        ("Plataforma de exportación (mbd)", 891.5, 616.4, 521.0),
        ("Plataforma de privados (mbd)", 74.0, 51.0, 119.0),
        ("Gas, precio promedio (dls/MMBtu)", 3.1, 3.5, 4.0),
    ], columns=["variable", "aprobado_2025", "estimado_2025", "proyecto_2026"])
    m.to_csv(SAL / "macro_marco.csv", index=False)
    fuente("macro_marco.csv", "marco macroeconómico", "CGPE 2026", "Anexo II.5, p. 83")

    mp = pd.DataFrame([
        ("PIB nominal (mmp)", 36125.5, 38715.9, 41185.1, 43712.6, 46377.1, 49203.5, 52213.8),
        ("Deflactor del PIB (%)", 5.2, 4.8, 4.2, 4.0, 4.0, 4.0, 4.0),
        ("RFSP (% PIB)", -4.3, -4.1, -3.5, -3.0, -3.0, -3.0, -3.0),
        ("Balance presupuestario (% PIB)", -3.6, -3.6, -3.0, -2.5, -2.5, -2.5, -2.5),
        ("Balance primario (% PIB)", 0.2, 0.5, 0.8, 0.8, 0.8, 0.8, 0.6),
        ("Ingresos presupuestarios (% PIB)", 21.9, 22.5, 22.4, 22.4, 22.4, 22.4, 22.4),
        ("Tributarios (% PIB)", 14.8, 15.1, 14.9, 14.9, 14.9, 14.9, 14.9),
        ("Gasto neto pagado (% PIB)", 25.5, 26.1, 25.4, 24.9, 24.9, 24.9, 24.9),
        ("Costo financiero (% PIB)", 3.8, 4.1, 3.8, 3.4, 3.3, 3.3, 3.1),
        ("Pensiones y jubilaciones (% PIB)", 4.5, 4.4, 4.5, 4.5, 4.6, 4.6, 4.7),
        ("Inversión física (% PIB)", 2.4, 2.5, 2.6, 2.4, 2.3, 2.3, 2.3),
        ("SHRFSP (% PIB)", 52.3, 52.3, 52.3, 52.3, 52.3, 52.3, 52.3),
        ("SHRFSP interno (% PIB)", 40.2, 41.3, 42.1, 42.5, 42.8, 43.2, 43.5),
        ("SHRFSP externo (% PIB)", 12.2, 11.0, 10.2, 9.8, 9.5, 9.1, 8.8),
        ("Límite máx. gasto corriente estructural (% PIB)", 10.9, 10.9, 10.9, 10.9, 10.9, 10.9, 10.9),
    ], columns=["variable", "e2025", "p2026", "2027", "2028", "2029", "2030", "2031"])
    mp.to_csv(SAL / "macro_medianoplazo.csv", index=False)
    fuente("macro_medianoplazo.csv", "mediano plazo 2025-2031", "CGPE 2026",
           "Anexos III.1 p. 86 y III.2 p. 87")

    fp = pd.DataFrame([
        ("RFSP", -1428348.1, -1559905.4, -1587349.9, -3.9, -4.3, -4.1),
        ("Requerimientos financieros extrapresupuestarios", -257781.7, -257781.7, -193579.3, -0.7, -0.7, -0.5),
        ("Balance presupuestario", -1170566.5, -1302123.7, -1393770.6, -3.2, -3.6, -3.6),
        ("Ingresos presupuestarios", 8055649.4, 7924967.5, 8721057.3, 22.3, 21.9, 22.5),
        ("Ingresos petroleros", 1142021.5, 966864.4, 1204277.7, 3.2, 2.7, 3.1),
        ("Ingresos no petroleros", 6913627.9, 6958103.0, 7516779.6, 19.1, 19.3, 19.4),
        ("Gobierno Federal (no petroleros)", 5670839.1, 5728867.9, 6215701.1, 15.7, 15.9, 16.1),
        ("Tributarios", 5296426.4, 5337702.5, 5838571.0, 14.6, 14.8, 15.1),
        ("No tributarios", 374412.7, 391165.4, 377130.1, 1.0, 1.1, 1.0),
        ("Organismos y empresas", 1242788.8, 1229235.2, 1301078.5, 3.4, 3.4, 3.4),
        ("Gasto neto pagado", 9226215.8, 9227091.2, 10114827.9, 25.5, 25.5, 26.1),
        ("Gasto programable pagado", 6451831.3, 6465235.1, 7015853.1, 17.8, 17.9, 18.1),
        ("Diferimiento de pagos", -75800.0, -75800.0, -78855.7, -0.2, -0.2, -0.2),
        ("Gasto programable devengado", 6527631.3, 6541035.1, 7094708.8, 18.0, 18.1, 18.3),
        ("Gasto no programable", 2774384.5, 2761856.1, 3098974.9, 7.7, 7.6, 8.0),
        ("Costo financiero", 1388373.6, 1375947.3, 1572073.3, 3.8, 3.8, 4.1),
        ("Participaciones", 1340210.9, 1350108.8, 1456045.9, 3.7, 3.7, 3.8),
        ("Adefas", 45800.0, 35800.0, 70855.7, 0.1, 0.1, 0.2),
        ("Superávit económico primario", 218307.2, 74323.6, 178802.6, 0.6, 0.2, 0.5),
        ("SHRFSP", 18591005.5, 18903594.9, 20259590.7, 51.4, 52.3, 52.3),
    ], columns=["concepto", "mdp_2025_aprobado", "mdp_2025_estimado", "mdp_2026",
                "pct_pib_2025_aprobado", "pct_pib_2025_estimado", "pct_pib_2026"])
    fp.to_csv(SAL / "finanzas_publicas.csv", index=False)
    fuente("finanzas_publicas.csv", "estimación de finanzas públicas 2025-2026", "CGPE 2026",
           "Anexo II.6, p. 84",
           nota="El renglón primario está rotulado «económico» en 2026 y «presupuestario» en el CGPE 2025; difieren en 500.0 mdp, el balance no presupuestario")


# ---------------------------------------------------------------- 2. gasto
def gasto():
    p25, p26 = marco(2025, "proyecto"), marco(2026, "proyecto")
    a25 = marco(2025, "pef")
    r = pd.DataFrame({"mdp_2025_proyecto": por(p25, "RAMO_K"), "mdp_2026": por(p26, "RAMO_K"),
                      "mdp_2025_aprobado": por(a25, "RAMO_K")}).fillna(0.0)
    nom = pd.concat([a25, p25, p26]).drop_duplicates("RAMO_K", keep="last").set_index("RAMO_K")["NOMBRE"]
    r["nombre"] = nom
    for ln, base in (("P", "mdp_2025_proyecto"), ("G", "mdp_2025_aprobado")):
        r[f"dif_nominal_{ln}"] = r.mdp_2026 - r[base]
        r[f"dif_real_{ln}"] = r.mdp_2026 - r[base] * DEFLACTOR
        r[f"var_real_pct_{ln}"] = (r.mdp_2026 / (r[base] * DEFLACTOR) - 1) * 100
    r.sort_values("mdp_2026", ascending=False).to_csv(SAL / "gasto_ramos.csv", float_format="%.1f")
    fuente("gasto_ramos.csv", "gasto bruto por ramo, líneas P y G", "analíticos del proyecto 2025 y 2026; PEF aprobado 2025",
           "cortes por programa, agregado por clave de ramo")

    f25, f26 = marco(2025, "proyecto", "gf-ramo-funcion-ur-objeto"), marco(2026, "proyecto", "gf-ramo-funcion-ur-objeto")
    fu = pd.DataFrame({"mdp_2025_proyecto": por(f25, ["F_K", "FN_K"]),
                       "mdp_2026": por(f26, ["F_K", "FN_K"])}).fillna(0.0)
    nm = pd.concat([f25, f26]).drop_duplicates(["F_K", "FN_K"], keep="last").set_index(["F_K", "FN_K"])["FN"]
    fu["nombre"] = nm.astype(str).str.strip()
    fu["dif_nominal"] = fu.mdp_2026 - fu.mdp_2025_proyecto
    fu["dif_real"] = fu.mdp_2026 - fu.mdp_2025_proyecto * DEFLACTOR
    fu["var_real_pct"] = (fu.mdp_2026 / (fu.mdp_2025_proyecto * DEFLACTOR) - 1) * 100
    fu["pct_pib_2026"] = fu.mdp_2026 / (PIB[2026] * 1000) * 100
    fu.sort_values("mdp_2026", ascending=False).to_csv(SAL / "gasto_funcional.csv", float_format="%.2f")
    fuente("gasto_funcional.csv", "gasto bruto por finalidad y función, línea P",
           "analíticos del proyecto 2025 y 2026", "cortes por función")

    sf = pd.DataFrame({"mdp_2025_proyecto": por(f25, ["F_K", "FN_K", "SF_K"]),
                       "mdp_2026": por(f26, ["F_K", "FN_K", "SF_K"])}).fillna(0.0)
    sf["dif_nominal"] = sf.mdp_2026 - sf.mdp_2025_proyecto
    sf["var_real_pct"] = (sf.mdp_2026 / (sf.mdp_2025_proyecto * DEFLACTOR) - 1) * 100
    sf.to_csv(SAL / "gasto_subfuncion.csv", float_format="%.2f")
    fuente("gasto_subfuncion.csv", "gasto bruto por subfunción, línea P",
           "analíticos del proyecto 2025 y 2026", "cortes por función")

    c = csv_proyecto()
    ec = c.groupby(["id_capitulo", "desc_capitulo"])["MDP"].sum().reset_index()
    ec["pct"] = ec.MDP / ec.MDP.sum() * 100
    ec.sort_values("MDP", ascending=False).to_csv(SAL / "gasto_capitulo.csv", index=False, float_format="%.1f")
    tg = c.groupby(["id_tipogasto", "desc_tipogasto"])["MDP"].sum().reset_index()
    tg.to_csv(SAL / "gasto_tipo.csv", index=False, float_format="%.1f")
    fuente("gasto_capitulo.csv", "gasto por capítulo del objeto del gasto, 2026",
           "CSV del proyecto (datos abiertos)", "columnas id_capitulo, monto_proyecto")
    fuente("gasto_tipo.csv", "gasto por tipo de gasto, 2026",
           "CSV del proyecto (datos abiertos)", "columnas id_tipogasto, monto_proyecto")

    ob = pd.DataFrame([
        ("Gastos obligatorios sin pensiones", 6046446.8, 6702281.0),
        ("Gastos obligatorios con pensiones y jubilaciones", 7684111.9, 8406440.2),
        ("Pensiones y jubilaciones (diferencia)", 1637665.1, 1704159.2),
    ], columns=["concepto", "mdp_2025_proyecto", "mdp_2026"])
    ob["dif_nominal"] = ob.mdp_2026 - ob.mdp_2025_proyecto
    ob["dif_real"] = ob.mdp_2026 - ob.mdp_2025_proyecto * DEFLACTOR
    ob["var_real_pct"] = (ob.mdp_2026 / (ob.mdp_2025_proyecto * DEFLACTOR) - 1) * 100
    ob["pct_pib_2026"] = ob.mdp_2026 / (PIB[2026] * 1000) * 100
    ob.to_csv(SAL / "gasto_obligatorios.csv", index=False, float_format="%.2f")
    fuente("gasto_obligatorios.csv", "gastos obligatorios con y sin pensiones",
           "Proyecto de Decreto de PEF 2026 y 2025", "Anexo 3",
           nota="La diferencia adjudica el perímetro de pensiones de la clasificación económica")

    # El LMGCE NO es un porcentaje del PIB: se construye del gasto corriente estructural
    # devengado de la Cuenta Publica de 2024 y de los deflactores, con un crecimiento real
    # de 2.05 % contra un PIB potencial de 2.11 %. El CGPE 2026 lo restituye: 4,225.3 mmp.
    # El punto de 2025 exige el LMGCE que propuso el CGPE 2025 y queda sin construir.
    gce = pd.DataFrame([
        ("Gasto corriente estructural (Anexo 2 del decreto)", 3603976.7, 3868319.9),
        ("Limite maximo del gasto corriente estructural", None, 4225300.0),
        ("Holgura", None, 4225300.0 - 3868319.9),
    ], columns=["concepto", "mdp_2025", "mdp_2026"])
    gce.to_csv(SAL / "gce_limite.csv", index=False, float_format="%.1f")
    fuente("gce_limite.csv", "gasto corriente estructural contra su límite máximo",
           "Decreto Anexo 2; CGPE 2026 p. 33", "Anexo 2 del decreto; texto del CGPE",
           nota="El LMGCE de 2026 es 4,225.3 mmp, restituido del texto del CGPE. NO se deriva del 10.9 % del PIB de la partida informativa de III.2: ese porcentaje es informativo y redondeado. El punto de 2025 exige el LMGCE del CGPE 2025 y no se construye")


# ---------------------------------------------------------------- 3. rubros
def rubros():
    f25, f26 = marco(2025, "proyecto", "gf-ramo-funcion-ur-objeto"), marco(2026, "proyecto", "gf-ramo-funcion-ur-objeto")
    p25, p26 = marco(2025, "proyecto"), marco(2026, "proyecto")

    def funcion(f, fn, cual):
        return {a: d[(d.F_K == f) & (d.FN_K == fn)] for a, d in cual.items()}

    for nombre, (f, fn) in (("salud", ("2", "3")), ("educacion", ("2", "5")),
                            ("ambiente", ("2", "1")), ("proteccion_social", ("2", "6"))):
        s25 = f25[(f25.F_K == f) & (f25.FN_K == fn)]
        s26 = f26[(f26.F_K == f) & (f26.FN_K == fn)]
        t = pd.DataFrame({"mdp_2025_proyecto": por(s25, "RAMO_K"), "mdp_2026": por(s26, "RAMO_K")}).fillna(0.0)
        nm = pd.concat([s25, s26]).drop_duplicates("RAMO_K", keep="last").set_index("RAMO_K")["NOMBRE"]
        t["nombre"] = nm
        t["dif_nominal"] = t.mdp_2026 - t.mdp_2025_proyecto
        t["dif_real"] = t.mdp_2026 - t.mdp_2025_proyecto * DEFLACTOR
        t["var_real_pct"] = (t.mdp_2026 / (t.mdp_2025_proyecto * DEFLACTOR) - 1) * 100
        t.loc["TOTAL"] = [t.mdp_2025_proyecto.sum(), t.mdp_2026.sum(), "",
                          t.dif_nominal.sum(), t.dif_real.sum(),
                          (t.mdp_2026.sum() / (t.mdp_2025_proyecto.sum() * DEFLACTOR) - 1) * 100]
        t.sort_values("mdp_2026", ascending=False).to_csv(SAL / f"{nombre}_ramo.csv", float_format="%.1f")
        fuente(f"{nombre}_ramo.csv", f"función {f}.{fn} por ramo, línea P",
               "analíticos del proyecto 2025 y 2026", "cortes por función, GF y entidades")
        sub = pd.DataFrame({"mdp_2025_proyecto": por(s25, "SF_K"), "mdp_2026": por(s26, "SF_K")}).fillna(0.0)
        sub["var_real_pct"] = (sub.mdp_2026 / (sub.mdp_2025_proyecto * DEFLACTOR) - 1) * 100
        sub.to_csv(SAL / f"{nombre}_subfuncion.csv", float_format="%.1f")

    # seguridad: quince subfunciones de cinco funciones
    PER = {("1","7"):["1","2","3","4"], ("1","3"):["2","3","4","5"], ("1","2"):["1","2","3","4"],
           ("1","8"):["4","5"], ("1","6"):["1","2","3"]}
    filas = []
    for (f, fn), sfs in PER.items():
        for sf in sfs:
            v25 = f25[(f25.F_K==f)&(f25.FN_K==fn)&(f25.SF_K==sf)]["MDP"].sum()
            v26 = f26[(f26.F_K==f)&(f26.FN_K==fn)&(f26.SF_K==sf)]["MDP"].sum()
            if max(v25, v26) > 0:
                filas.append(dict(clave=f"{f}.{fn}.{sf}", mdp_2025_proyecto=v25, mdp_2026=v26))
    sg = pd.DataFrame(filas)
    sg["dif_nominal"] = sg.mdp_2026 - sg.mdp_2025_proyecto
    sg["var_real_pct"] = (sg.mdp_2026/(sg.mdp_2025_proyecto*DEFLACTOR)-1)*100
    sg.loc[len(sg)] = ["TOTAL", sg.mdp_2025_proyecto.sum(), sg.mdp_2026.sum(),
                       sg.dif_nominal.sum(),
                       (sg.mdp_2026.sum()/(sg.mdp_2025_proyecto.sum()*DEFLACTOR)-1)*100]
    sg.to_csv(SAL / "seguridad_subfuncion.csv", index=False, float_format="%.1f")
    fuente("seguridad_subfuncion.csv", "perímetro de seguridad: quince subfunciones de cinco funciones",
           "analíticos del proyecto 2025 y 2026", "cortes por función",
           nota="En 2026 la Guardia Nacional pasa del Ramo 36 al Ramo 07, función 1.7: el perímetro no cambia, el reparto civil-militar sí")

    # pensiones: por institución, tipo de gasto 4
    def tg4(anio):
        ef = analitico(anio, "entidades-ramo-programa-ur-objeto", "proyecto")
        gf = analitico(anio, "gf-ramo-programa-ur-objeto", "proyecto")
        e = ef[clave(ef["TG"]) == "4"].groupby(ef["ENTIDAD"].astype(str).str.strip().str[:3])["MDP"].sum()
        g = gf[clave(gf["TG"]) == "4"].groupby(clave(gf["RAMO"]))["MDP"].sum()
        return pd.concat([e, g])
    pen = pd.DataFrame({"mdp_2025_proyecto": tg4(2025), "mdp_2026": tg4(2026)}).fillna(0.0)
    pen["var_real_pct"] = (pen.mdp_2026/(pen.mdp_2025_proyecto*DEFLACTOR)-1)*100
    pen.sort_values("mdp_2026", ascending=False).to_csv(SAL / "pensiones_tg4.csv", float_format="%.1f")
    fuente("pensiones_tg4.csv", "gasto de tipo 4 (pensiones) por institución y ramo",
           "analíticos del proyecto 2025 y 2026", "columna TG = 4",
           nota="BRUTO: el Ramo 19 y las entidades cuentan el mismo dinero dos veces; el perímetro se adjudica con el Anexo 3")

    # pensiones no contributivas, por clave
    # Se selecciona por el NUMERO de tres digitos, no por el codigo completo: la
    # modalidad cambia. La Pension Mujeres Bienestar es U316 en 2025 y S316 en 2026.
    NUMS = ["176", "286", "316"]
    filas = []
    for n in NUMS:
        a = p25[p25.PP_K.str[1:] == n]; b = p26[p26.PP_K.str[1:] == n]
        v25, v26 = a["MDP"].sum(), b["MDP"].sum()
        cl = f"{a.PP_K.iloc[0] if len(a) else '-'} -> {b.PP_K.iloc[0] if len(b) else '-'}"
        nb = pd.concat([a, b])["PP"].astype(str).str.strip()
        filas.append(dict(clave=cl, nombre=nb.iloc[-1] if len(nb) else "",
                          mdp_2025_proyecto=v25, mdp_2026=v26))
    nc = pd.DataFrame(filas)
    nc["var_real_pct"] = (nc.mdp_2026/(nc.mdp_2025_proyecto*DEFLACTOR)-1)*100
    nc.loc[len(nc)] = ["TOTAL", "", nc.mdp_2025_proyecto.sum(), nc.mdp_2026.sum(),
                       (nc.mdp_2026.sum()/(nc.mdp_2025_proyecto.sum()*DEFLACTOR)-1)*100]
    nc.to_csv(SAL / "pensiones_no_contributivas.csv", index=False, float_format="%.1f")
    fuente("pensiones_no_contributivas.csv", "pensiones no contributivas por clave de programa",
           "analíticos del proyecto 2025 y 2026", "claves S176, S286 y S316",
           nota="Seleccion por el NUMERO de programa, no por el codigo completo: la Pension Mujeres Bienestar pasa de U316 a S316 y un filtro por codigo completo la pierde")


# ---------------------------------------------------------------- 4. transversales
def transversales():
    d = pd.read_csv(Path(__file__).resolve().parent.parent / "2026" / "2026_ppef_anexos-transversales.csv",
                    low_memory=False)
    d["MDP"] = d.monto_ppef / 1e6
    t = d.groupby(["id_transversal", "transversal"])["MDP"].sum().reset_index()
    t["pct_del_etiquetado"] = t.MDP / t.MDP.sum() * 100
    t["pct_programable"] = t.MDP / 7_015_853.1 * 100
    t.sort_values("MDP", ascending=False).to_csv(SAL / "transversales.csv", index=False, float_format="%.1f")
    fuente("transversales.csv", "anexos transversales del proyecto, monto y participación",
           "CSV de anexos transversales del PPEF (datos abiertos)", "id_transversal, monto_ppef")

    ig = d[d.id_transversal == 4].copy()
    ig["PP_K"] = ig.id_modalidad.astype(str) + ig.id_pp.astype(str).str.zfill(3)
    g = ig.groupby(["PP_K", "desc_pp"])["MDP"].sum().reset_index().sort_values("MDP", ascending=False)
    g["pct_del_anexo"] = g.MDP / g.MDP.sum() * 100
    g["es_pension"] = g.desc_pp.str.contains("ensi", case=False, na=False)
    g.to_csv(SAL / "transversal_igualdad.csv", index=False, float_format="%.1f")
    fuente("transversal_igualdad.csv", "composición del anexo de igualdad entre mujeres y hombres",
           "CSV de anexos transversales del PPEF", "id_transversal = 4",
           nota=f"El {g[g.es_pension].MDP.sum()/g.MDP.sum()*100:.1f} % del anexo son programas de pensión")

    pr = d.groupby(["id_ramo", "id_modalidad", "id_pp", "desc_pp"]).agg(
        anexos=("id_transversal", "nunique"), mdp_sumado=("MDP", "sum")).reset_index()
    pr = pr.sort_values(["anexos", "mdp_sumado"], ascending=False)
    pr.to_csv(SAL / "transversales_traslape.csv", index=False, float_format="%.1f")
    fuente("transversales_traslape.csv", "programas que aparecen en más de un anexo transversal",
           "CSV de anexos transversales del PPEF", "conteo de id_transversal por programa",
           nota=f"{(pr.anexos>1).sum()} de {len(pr)} programas aparecen en más de un anexo")


# ---------------------------------------------------------------- 5. demografía
def demografia():
    ext = SAL / "_externas" / "conapo_pob_mitad_1950_2070.csv"
    d = pd.read_csv(ext, low_memory=False)
    x = d[d.ANIO.isin([2025, 2026])]
    nac = x.groupby("ANIO")["POBLACION"].sum()
    p65 = x[x.EDAD >= 65].groupby("ANIO")["POBLACION"].sum()
    esc = x[(x.EDAD >= 3) & (x.EDAD <= 14)].groupby("ANIO")["POBLACION"].sum()
    ent = x[x.ANIO == 2026].groupby(["CVE_GEO", "ENTIDAD"])["POBLACION"].sum().reset_index()
    dem = pd.DataFrame({"denominador": ["Población total", "Población de 65 años y más",
                                        "Población de 3 a 14 años"],
                        "personas_2025": [nac[2025], p65[2025], esc[2025]],
                        "personas_2026": [nac[2026], p65[2026], esc[2026]]})
    dem.to_csv(SAL / "demografia_denominadores.csv", index=False, float_format="%.0f")
    ent.to_csv(SAL / "demografia_entidades.csv", index=False, float_format="%.0f")
    fuente("demografia_denominadores.csv", "denominadores demográficos nacionales",
           "CONAPO, proyecciones de población a mitad de año 1950-2070",
           "00_Pob_Mitad_1950_2070.csv", tier="externa_demografica",
           nota="Cuadros presupuestales y per cápita van separados; toda cifra per cápita declara su denominador")
    fuente("demografia_entidades.csv", "población por entidad federativa, 2026",
           "CONAPO, proyecciones de población a mitad de año", "00_Pob_Mitad_1950_2070.csv",
           tier="externa_demografica")
    return dem




# ---------------------------------------------------------------- 6. ingresos y deuda
def ingresos():
    # Restitucion linea por linea del articulo 1o. de cada iniciativa. NINGUNA cifra
    # tecleada de memoria: las de 2025 se cotejaron contra el PDF el 2026-09-07 y cuatro
    # de las primeras seis que se habian escrito de memoria estaban mal (bitacora, fase 2).
    ing = pd.DataFrame([
        ("1. Impuestos", 5297812.9, 5838541.1),
        ("   11.01 Impuesto sobre la renta", 2859575.1, 3070149.1),
        ("   13.01 Impuesto al valor agregado", 1463279.9, 1589069.0),
        ("   13.02 Impuesto especial sobre produccion y servicios", 713844.0, 761501.9),
        ("   14 Impuestos al comercio exterior", 151789.7, 254756.8),
        ("   17 Accesorios de impuestos", 81497.4, 135769.4),
        ("2. Cuotas y aportaciones de seguridad social", 603077.9, 641782.1),
        ("4. Derechos", 137500.5, 157081.7),
        ("5. Productos", None, 16488.3),
        ("6. Aprovechamientos", 223166.3, 203520.5),
        ("7. Ingresos por ventas de bienes y prestacion de servicios", 1500579.0, 1630973.6),
        ("9.97 Transferencias del Fondo Mexicano del Petroleo", 279766.8, 232630.4),
        ("0. Ingresos derivados de financiamientos", 1246366.5, 1472626.4),
        ("TOTAL", 9302015.8, 10193683.7),
    ], columns=["concepto", "mdp_2025_ilif", "mdp_2026_ilif"])
    ing["dif_nominal"] = ing.mdp_2026_ilif - ing.mdp_2025_ilif
    ing["dif_real"] = ing.mdp_2026_ilif - ing.mdp_2025_ilif * DEFLACTOR
    ing["var_real_pct"] = (ing.mdp_2026_ilif / (ing.mdp_2025_ilif * DEFLACTOR) - 1) * 100
    ing["pct_pib_2026"] = ing.mdp_2026_ilif / (PIB[2026] * 1000) * 100
    ing.to_csv(SAL / "ingresos_art1o.csv", index=False, float_format="%.2f")
    fuente("ingresos_art1o.csv", "ingresos por renglon del articulo 1o., linea P",
           "ILIF 2026 e ILIF 2025", "articulo 1o. de cada iniciativa",
           nota="Ex ante contra ex ante: las dos columnas son iniciativa, no ley aprobada. Cotejadas linea por linea contra los dos PDF el 2026-09-07")
    fin = pd.DataFrame([("Financiamiento por cada 100 pesos de ingreso total",
                         1246366.5/9302015.8*100, 1472626.4/10193683.7*100)],
                       columns=["concepto", "p2025", "p2026"])
    fin.to_csv(SAL / "ingresos_financiamiento.csv", index=False, float_format="%.2f")
    fuente("ingresos_financiamiento.csv", "pesos de cada 100 que provienen de financiamiento",
           "ILIF 2026 y 2025", "numeral 0 sobre el total del articulo 1o.")


def deuda():
    fl = pd.DataFrame([
        ("Balance presupuestario", -1170566.5, -1393770.6, -3.2, -3.6),
        ("Balance no presupuestario (implicito)", 500.0, 500.0, 0.0, 0.0),
        ("RFSP", -1428348.1, -1587349.9, -3.9, -4.1),
        ("Balance primario economico", 218307.2, 178802.6, 0.6, 0.5),
    ], columns=["flujo", "mdp_2025_aprobado", "mdp_2026", "pct_pib_2025", "pct_pib_2026"])
    fl.to_csv(SAL / "flujos.csv", index=False, float_format="%.1f")
    ac = pd.DataFrame([
        ("SHRFSP", 18591005.5, 20259590.7, 51.4, 52.3),
        ("SHRFSP interno", None, None, 39.8, 41.3),
        ("SHRFSP externo", None, None, 11.6, 11.0),
        ("Deuda neta del sector publico", None, None, 50.9, 52.8),
        ("Saldo historico de la deuda bruta del SPNF", None, None, 54.9, 57.4),
    ], columns=["acervo", "mdp_2025_aprobado", "mdp_2026", "pct_pib_2025_aprobado", "pct_pib_2026"])
    ac.to_csv(SAL / "acervos.csv", index=False, float_format="%.1f")
    fuente("flujos.csv", "los tres flujos con su nombre correcto", "CGPE 2026",
           "Anexos II.6 p. 84 y III.2 p. 87",
           nota="El primario esta rotulado economico en 2026 y presupuestario en 2025: 500.0 mdp de diferencia, que es el balance no presupuestario")
    fuente("acervos.csv", "los tres acervos", "CGPE 2026", "Anexos II.6 y III.2")

    d25, pib25, pib26 = 52.3, PIB[2025], PIB[2026]
    n = pib26 / pib25 - 1
    defl = 0.048
    g = (1 + n) / (1 + defl) - 1
    ext25, tc25, tc26 = 12.2, 19.9, 18.9
    e_crec = -d25 * g / (1 + n)
    e_infl = -d25 * defl * (1 + g) / (1 + n)
    e_fx = ext25 * (tc26 / tc25 - 1)
    rfsp = 4.1
    filas = []
    for nom, pi in (("deflactor del PIB, 4.8", 0.048), ("INPC promedio, 3.5", 0.035),
                    ("INPC dic/dic, 3.0", 0.030),
                    ("solo lo identificable: adecuaciones, 0.3 % del PIB", None)):
        comp = 0.3 if pi is None else d25 * pi / (1 + n)
        filas.append(dict(convencion=nom, compensacion_pp=comp, inflacion_neta_pp=e_infl + comp))
    desc = pd.DataFrame(filas)
    desc["crecimiento_pp"] = e_crec
    desc["denominador_inflacion_pp"] = e_infl
    desc["tipo_de_cambio_pp"] = e_fx
    desc["rfsp_pp"] = rfsp
    desc["suma_del_marco_pp"] = rfsp + e_crec + e_infl + e_fx
    desc["cambio_observado_pp"] = 52.3 - 52.3
    desc.to_csv(SAL / "descomposicion.csv", index=False, float_format="%.3f")
    fuente("descomposicion.csv", "descomposicion del cambio de SHRFSP/PIB en cuatro variables",
           "CGPE 2026 Anexos III.1 y III.2", "calculo propio", tier="autoral_ited",
           nota="Convencion 17 del pacto: la compensacion por inflacion se presenta como RANGO con su cota declarada, nunca como punto")


def inversion_federalizado():
    c = csv_proyecto()
    inv = c[c.id_capitulo.isin([6000, 7000])].groupby(["id_capitulo", "desc_capitulo"])["MDP"].sum().reset_index()
    inv.to_csv(SAL / "inversion_agregados.csv", index=False, float_format="%.1f")
    cart = c[c.id_clave_cartera != 0].groupby("id_clave_cartera")["MDP"].sum().nlargest(40).reset_index()
    cart.to_csv(SAL / "inversion_cartera.csv", index=False, float_format="%.1f")
    fuente("inversion_agregados.csv", "inversion por capitulo del objeto del gasto",
           "CSV del proyecto (datos abiertos)", "id_capitulo 6000 y 7000")
    fuente("inversion_cartera.csv", "los cuarenta proyectos mayores de la cartera de inversion",
           "CSV del proyecto (datos abiertos)", "id_clave_cartera",
           nota="Ruta que sustituye al Tomo VIII, que no esta en carpeta")
    ef = c[c.id_entidad_federativa != 0].groupby(["id_entidad_federativa", "entidad_federativa"])["MDP"].sum().reset_index()
    ef.to_csv(SAL / "federalizado_entidad.csv", index=False, float_format="%.1f")
    fuente("federalizado_entidad.csv", "gasto identificado por entidad federativa, 2026",
           "CSV del proyecto (datos abiertos)", "id_entidad_federativa",
           nota="No es todo el gasto federalizado: solo el que el proyecto identifica territorialmente")




# ---------------------------------------------------------------- 7. techos y per capita
def techos():
    t = pd.DataFrame([
        ("Gobierno Federal, endeudamiento neto interno", "ILIF art. 2o.", 1780000.0, "mdp"),
        ("Gobierno Federal, endeudamiento neto externo", "ILIF art. 2o.", 15500.0, "mdd"),
        ("Petroleos Mexicanos, interno", "ILIF art. 4o.", 160619.6, "mdp"),
        ("Petroleos Mexicanos, externo", "ILIF art. 4o.", 5342.1, "mdd"),
        ("Comision Federal de Electricidad, interno", "ILIF art. 4o.", 8764.2, "mdp"),
        ("Comision Federal de Electricidad, externo", "ILIF art. 4o.", 969.0, "mdd"),
        ("Ciudad de Mexico", "ILIF art. 6o.", 3500.0, "mdp"),
        ("--- para contraste, NO son techos ---", "", None, ""),
        ("Deficit presupuestario (DEC art. 2 / CGPE II.6)", "CGPE 2026", 1393770.6, "mdp"),
        ("Ingresos derivados de financiamientos (informativo)", "ILIF art. 1o. numeral 0", 1472626.4, "mdp"),
    ], columns=["concepto", "fuente", "monto", "unidad"])
    t.to_csv(SAL / "techos.csv", index=False, float_format="%.1f")
    fuente("techos.csv", "techos de endeudamiento y su distincion del deficit",
           "ILIF 2026", "articulos 2o., 4o. y 6o.",
           nota="Techo, deficit y endeudamiento informativo son TRES objetos distintos. El techo interno del GF supera al deficit en 27.6 %")


def percapita():
    dem = pd.read_csv(SAL / "demografia_denominadores.csv")
    pob26 = float(dem.loc[dem.denominador == "Poblacion total", "personas_2026"].iloc[0]) if False else float(dem.personas_2026.iloc[0])
    pob25 = float(dem.personas_2025.iloc[0])
    p65_26, p65_25 = float(dem.personas_2026.iloc[1]), float(dem.personas_2025.iloc[1])
    esc26, esc25 = float(dem.personas_2026.iloc[2]), float(dem.personas_2025.iloc[2])
    padron = 35772760.0     # IMSS-Bienestar, padron del 2o trimestre de 2025, 23 entidades

    sal = pd.read_csv(SAL / "salud_ramo.csv")
    edu = pd.read_csv(SAL / "educacion_ramo.csv")
    salud26 = float(sal.loc[sal.RAMO_K == "TOTAL", "mdp_2026"].iloc[0])
    salud25 = float(sal.loc[sal.RAMO_K == "TOTAL", "mdp_2025_proyecto"].iloc[0])
    edu26 = float(edu.loc[edu.RAMO_K == "TOTAL", "mdp_2026"].iloc[0])
    edu25 = float(edu.loc[edu.RAMO_K == "TOTAL", "mdp_2025_proyecto"].iloc[0])
    pens26, pens25 = 1704159.2, 1637665.1
    amb = pd.read_csv(SAL / "ambiente_ramo.csv")
    amb26 = float(amb.loc[amb.RAMO_K == "TOTAL", "mdp_2026"].iloc[0])
    amb25 = float(amb.loc[amb.RAMO_K == "TOTAL", "mdp_2025_proyecto"].iloc[0])

    filas = [
        ("Salud, por habitante", "poblacion total (CONAPO)", salud25*1e6/pob25, salud26*1e6/pob26),
        ("Educacion, por habitante", "poblacion total (CONAPO)", edu25*1e6/pob25, edu26*1e6/pob26),
        ("Educacion, por persona de 3 a 14 anios", "poblacion en edad escolar basica (CONAPO)",
         edu25*1e6/esc25, edu26*1e6/esc26),
        ("Pensiones y jubilaciones, por persona de 65 y mas", "poblacion 65+ (CONAPO)",
         pens25*1e6/p65_25, pens26*1e6/p65_26),
        ("Ambiente y agua, por habitante", "poblacion total (CONAPO)", amb25*1e6/pob25, amb26*1e6/pob26),
        ("IMSS-Bienestar, por persona del padron", "padron IMSS-Bienestar 2T2025, 23 entidades",
         None, 172085.2*1e6/padron),
    ]
    pc = pd.DataFrame(filas, columns=["indicador", "denominador", "pesos_2025", "pesos_2026"])
    pc["var_real_pct"] = (pc.pesos_2026 / (pc.pesos_2025 * DEFLACTOR) - 1) * 100
    pc.to_csv(SAL / "percapita.csv", index=False, float_format="%.1f")
    fuente("percapita.csv", "cifras por habitante y por denominador declarado",
           "cuadros presupuestales de datos/ mas denominadores de CONAPO e IMSS-Bienestar",
           "calculo propio", tier="externa_demografica",
           nota="CUADRO SEPARADO de los presupuestales. NO se publica gasto por afiliado a IMSS o ISSSTE ni por alumno matriculado: esos dos denominadores no se consiguieron (dos intentos, registrados en la bitacora)")
    dem2 = pd.DataFrame([
        ("Padron de personas sin seguridad social, IMSS-Bienestar", padron,
         "2o trimestre de 2025, 23 entidades federativas"),
    ], columns=["denominador", "personas", "nota"])
    dem2.to_csv(SAL / "demografia_padron.csv", index=False, float_format="%.0f")
    fuente("demografia_padron.csv", "padron de personas sin seguridad social",
           "IMSS-Bienestar, datos abiertos", "padron_sin_seguridad_social_2do_trimestre_2025.csv",
           tier="externa_demografica",
           nota="Se usa el 2o trimestre y NO el 4o, que existe: el 4o se publico despues de la entrega del paquete y no habria estado disponible en una lectura en vivo")




def ambiente_agua():
    """Perimetro del capitulo 11, enumerable: funcion 2.1 completa mas la subfuncion 2.2.3.
    El agua NO vive en la funcion de proteccion ambiental sino en la de vivienda y
    servicios a la comunidad. Se declara y las dos partes van etiquetadas por separado."""
    f25 = marco(2025, "proyecto", "gf-ramo-funcion-ur-objeto")
    f26 = marco(2026, "proyecto", "gf-ramo-funcion-ur-objeto")
    filas = []
    for etq, cond in (("2.1 Proteccion Ambiental (completa)", lambda d: (d.F_K=="2")&(d.FN_K=="1")),
                      ("  2.1.2 Ordenacion de aguas residuales", lambda d: (d.F_K=="2")&(d.FN_K=="1")&(d.SF_K=="2")),
                      ("  2.1.3 Reduccion de la contaminacion", lambda d: (d.F_K=="2")&(d.FN_K=="1")&(d.SF_K=="3")),
                      ("  2.1.5 Proteccion de la diversidad biologica", lambda d: (d.F_K=="2")&(d.FN_K=="1")&(d.SF_K=="5")),
                      ("  2.1.6 Otros de proteccion ambiental", lambda d: (d.F_K=="2")&(d.FN_K=="1")&(d.SF_K=="6")),
                      ("2.2.3 Abastecimiento de agua", lambda d: (d.F_K=="2")&(d.FN_K=="2")&(d.SF_K=="3")),
                      ("PERIMETRO (2.1 + 2.2.3)", lambda d: ((d.F_K=="2")&(d.FN_K=="1"))|((d.F_K=="2")&(d.FN_K=="2")&(d.SF_K=="3")))):
        v25, v26 = f25[cond(f25)]["MDP"].sum(), f26[cond(f26)]["MDP"].sum()
        filas.append(dict(concepto=etq, mdp_2025_proyecto=v25, mdp_2026=v26,
                          dif_nominal=v26-v25, dif_real=v26-v25*DEFLACTOR,
                          var_real_pct=(v26/(v25*DEFLACTOR)-1)*100 if v25 else float("nan")))
    a = pd.DataFrame(filas)
    a["pct_pib_2026"] = a.mdp_2026 / (PIB[2026]*1000) * 100
    a.to_csv(SAL / "ambiente_agua.csv", index=False, float_format="%.2f")
    fuente("ambiente_agua.csv", "perimetro de medio ambiente y agua, enumerable",
           "analiticos del proyecto 2025 y 2026", "funcion 2.1 completa mas subfuncion 2.2.3",
           nota="El agua NO esta en la funcion de proteccion ambiental sino en la 2.2 Vivienda y Servicios a la Comunidad. Las dos partes van etiquetadas por separado y nunca se presentan como una sola funcion")


def main():
    macro(); gasto(); rubros(); transversales(); ingresos(); deuda()
    inversion_federalizado(); techos(); ambiente_agua(); dem = demografia(); percapita()
    pd.DataFrame(F).to_csv(SAL / "_fuentes.csv", index=False)
    print(f"escritos {len(list(SAL.glob('*.csv')))} archivos en datos/")
    print(f"_fuentes.csv con {len(F)} filas")
    print("\nDenominadores demográficos:"); print(dem.to_string(index=False))


if __name__ == "__main__":
    main()
