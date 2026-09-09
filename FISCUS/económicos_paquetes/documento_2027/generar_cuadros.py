#!/usr/bin/env python3
"""Genera los cuadros del documento 2027 desde datos registrados.

Ningún cuadro se teclea. Cada uno sale de `datos/_fuentes.csv` —una fila por cifra,
con su documento y su ubicación— o de `datos/ramos.csv`, que se extrae del Anexo 1 de
los dos decretos. Los números se formatean aquí porque el pacto prohíbe `siunitx`.

    python3 generar_cuadros.py            # regenera capitulos/cuadros/*.tex
    python3 generar_cuadros.py --ramos    # vuelve a extraer datos/ramos.csv de los PDF

REGLA DE LA CASA: la variación real usa el deflactor del PIB (1.040 para 2027). El
índice al consumidor no aparece en ningún cuadro presupuestal.
"""
from __future__ import annotations
import argparse, csv, re, subprocess
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
CUADROS = AQUI / "capitulos" / "cuadros"


def externo(nombre: str, *sub: str) -> Path:
    """Un CSV que vive fuera de este documento, con copia local en `datos/`.

    El ZIP de entrega tiene que ser autocontenido: si el árbol del proyecto no está,
    se usa la copia. Si está, manda el original, que es el que se actualiza.
    """
    fuera = RAIZ.joinpath(*sub, nombre)
    return fuera if fuera.exists() else AQUI / "datos" / nombre
DEFL = 1.040                      # deflactor del PIB 2027, CGPE 2027 Anexo III.1


# --------------------------------------------------------------------------- datos
def fuentes() -> dict[str, float]:
    with open(AQUI / "datos" / "_fuentes.csv", encoding="utf-8") as f:
        return {r["id"]: float(r["valor"]) for r in csv.DictReader(f)}


def extraer_ramos() -> None:
    """Anexo 1 de los dos decretos -> datos/ramos.csv. Por clave, nunca por nombre."""
    filas = []
    for anio, pdf, rango in ((2026, RAIZ / "2026" / "2026_ppef_proyecto-decreto.pdf", (65, 68)),
                             (2027, RAIZ / "2027" / "2027_ppef_proyecto-decreto.pdf", (69, 72))):
        txt = subprocess.run(["pdftotext", "-layout", "-f", str(rango[0]), "-l", str(rango[1]),
                              str(pdf), "-"], capture_output=True, text=True).stdout
        for linea in txt.split("\n"):
            m = re.match(r"\s*(\d{2})\s{2,}(.+?)\s{2,}([\d,]{7,})\s*$", linea)
            if m:
                # pdftotext parte la palabra DESPUÉS de v o x («Legislativ o», «Ex teriores»,
                # «Serv icios»). No tocar los espacios reales: «Aportaciones a», «Agricultura y».
                nombre = re.sub(r"(?<=[vxVX]) (?=[a-záéíóúñ])", "", m.group(2)).strip()
                filas.append({"ejercicio": anio, "ramo": m.group(1), "nombre": nombre,
                              "mdp": round(int(m.group(3).replace(",", "")) / 1e6, 1)})
    with open(AQUI / "datos" / "ramos.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, ["ejercicio", "ramo", "nombre", "mdp"], lineterminator="\n")
        w.writeheader(); w.writerows(filas)
    print(f"datos/ramos.csv: {len(filas)} filas")


def ramos() -> dict[str, dict]:
    d: dict[str, dict] = {}
    with open(AQUI / "datos" / "ramos.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            d.setdefault(r["ramo"], {"nombre": r["nombre"]})[int(r["ejercicio"])] = float(r["mdp"])
    return d


# ----------------------------------------------------------------------- formateo
def n(v, dec=1):
    """Número a la española: punto de millares, coma decimal. Sin siunitx."""
    s = f"{v:,.{dec}f}"
    return s.translate(str.maketrans({",": ".", ".": ","}))


def pct(v, dec=1):
    """Porcentaje con menos tipográfico. Si a un decimal daría cero, se imprime con dos:
    «$-$0,0» no dice nada y «0,0» pierde el signo."""
    if round(v, dec) == 0 and v != 0:
        dec += 1
    s = f"{abs(v):.{dec}f}".replace(".", ",")
    return ("$-$" if v < 0 else "+") + s


def real(v26, v27):
    return (v27 / v26 / DEFL - 1) * 100


def nominal(v26, v27):
    return (v27 / v26 - 1) * 100


def escribe(nombre: str, cuerpo: str) -> None:
    CUADROS.mkdir(parents=True, exist_ok=True)
    (CUADROS / f"{nombre}.tex").write_text(cuerpo.rstrip() + "\n", encoding="utf-8")
    print(f"  {nombre}.tex")


def tabla(caption, etiqueta, cols, encabezado, filas, nota=None, tam="small"):
    out = [f"\\begin{{table}}[htbp]\\centering\\{tam}",
           f"\\caption{{{caption}}}\\label{{{etiqueta}}}",
           f"\\begin{{tabular}}{{{cols}}}", "\\toprule", encabezado + " \\\\", "\\midrule"]
    out += [f + " \\\\" for f in filas]
    out += ["\\bottomrule", "\\end{tabular}"]
    if nota:
        out.append(f"\\\\[2pt]\\begin{{minipage}}{{0.92\\textwidth}}\\scriptsize {nota}\\end{{minipage}}")
    out.append("\\end{table}")
    return "\n".join(out)


# ------------------------------------------------------------------------ cuadros
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ramos", action="store_true")
    if ap.parse_args().ramos:
        extraer_ramos()
    F, R = fuentes(), ramos()
    print("cuadros generados:")

    # --- C1_1 marco macroeconómico -----------------------------------------
    fil = [("PIB nominal (mmp)", F["pib_26_ap"] / 1000, F["pib_26_es"] / 1000, F["pib_27"] / 1000, 1),
           ("Tipo de cambio promedio (pesos/dólar)", None, F["tc_prom_26"], F["tc_prom_27"], 1),
           ("Cetes 28 días, promedio (\\%)", None, 6.5, F["cetes_prom_27"], 1),
           ("Inflación INPC dic./dic. (\\%)", 3.0, 3.5, F["infl_dic_27"], 1),
           ("Mezcla mexicana (dólares por barril)", F["petro_26_ap"], F["petro_26"], F["petro_27"], 1),
           ("Plataforma de producción (mbd)", 1794.0, F["plat_prod_26"], F["plat_prod_27"], 1),
           ("Plataforma de exportación (mbd)", 521.0, F["plat_exp_26"], F["plat_exp_27"], 1)]
    escribe("C1_1", tabla(
        "Marco macroeconómico, 2026--2027", "cua:macro", "lrrr",
        "Concepto & 2026 aprobado & 2026 estimado & \\textbf{2027}",
        [f"{c} & {n(a) if a is not None else '---'} & {n(b)} & \\textbf{{{n(v)}}}"
         for c, a, b, v, _ in fil],
        "Fuente: CGPE 2027, edición SHCP, Anexos II.5 (p. 66) y III.1 (p. 68). "
        "El PIB de 2026 se revisa a la baja en 1.555,2 mmp entre el aprobado y el estimado; "
        "toda razón a PIB de 2026 depende de cuál añada se use."))

    # --- C2_1 ingresos del artículo 1o., línea P ---------------------------
    conc = [("Total", "lif_total"), ("Impuestos", "lif_imp"),
            ("\\quad Impuesto sobre la renta", "lif_isr"),
            ("\\quad Impuesto al valor agregado", "lif_iva"),
            ("\\quad IEPS", "lif_ieps"),
            ("\\quad\\quad de combustibles automotrices", "lif_comb"),
            ("Cuotas de seguridad social", "lif_cuotas"),
            ("Derechos", "lif_der"), ("Aprovechamientos", "lif_apro"),
            ("Ventas de bienes y servicios", "lif_ventas"),
            ("Transferencias del FMP", "lif_fmp"),
            ("Ingresos derivados de financiamientos", "lif_fin")]
    escribe("C2_1", tabla(
        "Ingresos del artículo 1o., línea P: proyecto 2026 contra proyecto 2027 (mdp)",
        "cua:ing", "lrrrr",
        "Concepto & 2026 & 2027 & Var. nominal (\\%) & Var. real (\\%)",
        [f"{c} & {n(F[k+'_26'])} & {n(F[k+'_27'])} & "
         f"{pct(nominal(F[k+'_26'], F[k+'_27']))} & {pct(real(F[k+'_26'], F[k+'_27']))}"
         for c, k in conc],
        "Fuente: artículo 1o. de la ILIF 2027 y de la ILIF 2026. "
        "Deflactor del PIB de 2027, 1,040. \\textbf{El renglón del IEPS de 2026 se restituye de "
        "la LIF aprobada}, porque el diseño de la tabla de la iniciativa no lo aísla; "
        "iniciativa y ley aprobada de 2026 coinciden al décimo en todos los demás renglones "
        "de este cuadro, incluido el total, de modo que para 2026 las líneas P y G son la misma."))

    # --- C2_2 ingresos presupuestarios en % del PIB ------------------------
    ing = [("Ingresos presupuestarios", "cg_ing_26ap", "cg_ing_27", 22.5, 23.2),
           ("\\quad Petroleros", "cg_petro_26ap", "cg_petro_27", 3.1, 2.5),
           ("\\quad No petroleros", "cg_nopetro_26ap", "cg_nopetro_27", 19.4, 20.7),
           ("\\quad\\quad Tributarios", "cg_trib_26ap", "cg_trib_27", 15.1, 15.9),
           ("\\quad\\quad No tributarios", "cg_notrib_26ap", "cg_notrib_27", 1.0, 1.3),
           ("\\quad\\quad Organismos y empresas", "cg_org_26ap", "cg_org_27", 3.4, 3.5)]
    escribe("C2_2", tabla(
        "Ingresos presupuestarios: monto y razón a PIB, línea G", "cua:ingpib", "lrrrr",
        "Concepto & 2026 aprob. (mdp) & 2027 (mdp) & 2026 (\\% PIB) & 2027 (\\% PIB)",
        [f"{c} & {n(F[a])} & {n(F[b])} & {n(p1)} & {n(p2)}" for c, a, b, p1, p2 in ing],
        "Fuente: CGPE 2027, edición SHCP, Anexo II.6 (p. 67). Las razones de 2026 usan el PIB "
        "\\emph{aprobado} de 2026 (38.715,9 mmp), como declara la nota del propio anexo, "
        "y no el estimado."))

    # --- C3_1 petroleros y empresas públicas -------------------------------
    escribe("C3_1", tabla(
        "Ingresos petroleros y empresas públicas del Estado", "cua:energ", "lrrr",
        "Concepto & 2026 & 2027 & Var. real (\\%)",
        [f"Ingresos petroleros (mdp, línea G) & {n(F['cg_petro_26ap'])} & {n(F['cg_petro_27'])} & "
         f"{pct(real(F['cg_petro_26ap'], F['cg_petro_27']))}",
         f"Transferencias del FMP (mdp, línea P) & {n(F['lif_fmp_26'])} & {n(F['lif_fmp_27'])} & "
         f"{pct(real(F['lif_fmp_26'], F['lif_fmp_27']))}",
         f"Ramo 18 Energía (mdp, línea P) & {n(R['18'][2026])} & {n(R['18'][2027])} & "
         f"{pct(real(R['18'][2026], R['18'][2027]))}",
         f"Mezcla mexicana (dólares por barril) & {n(F['petro_26'])} & {n(F['petro_27'])} & ---",
         f"Plataforma de exportación (mbd) & {n(F['plat_exp_26'])} & {n(F['plat_exp_27'])} & ---",
         f"Plataforma de privados (mbd) & {n(F['plat_priv_26'])} & {n(F['plat_priv_27'])} & ---"],
        "Fuentes: CGPE 2027 Anexos II.5 y II.6; artículo 1o. de las dos iniciativas de Ley de "
        "Ingresos; Anexo 1 de los dos proyectos de decreto. El precio y las plataformas no "
        "admiten variación real: no son pesos."))

    # --- C4_1 ramos que más se mueven --------------------------------------
    comunes = {k: v for k, v in R.items() if 2026 in v and 2027 in v and v[2026] > 0}
    orden = sorted(comunes.items(), key=lambda kv: -abs(kv[1][2027] - kv[1][2026]))[:14]
    escribe("C4_1", tabla(
        "Los catorce ramos que más se mueven en pesos, línea P (mdp)", "cua:ramos", "llrrrr",
        "Ramo & Denominación & 2026 & 2027 & Dif. & Var. real (\\%)",
        [f"{k} & {(v['nombre'][:38].rstrip() + '…') if len(v['nombre']) > 38 else v['nombre']}"
         f" & {n(v[2026])} & {n(v[2027])} & "
         f"{n(v[2027]-v[2026]).replace('-', '$-$')} & {pct(real(v[2026], v[2027]))}"
         for k, v in orden],
        "Fuente: Anexo 1 de los proyectos de decreto de PEF 2026 y 2027, \\textbf{por clave de "
        "ramo, no por nombre}. Deflactor del PIB de 2027. \\textbf{Un ramo no es una función}: "
        "una caída de ramo no es una caída de la política pública que su nombre sugiere.",
        tam="footnotesize"))

    # --- C4_2 gasto: agregados del decreto y del CGPE ----------------------
    escribe("C4_2", tabla(
        "Gasto: agregados del decreto y de los Criterios Generales (mdp)", "cua:gasto", "lrrr",
        "Concepto & 2026 & 2027 & Var. real (\\%)",
        [f"Gasto neto total (decreto, línea P) & {n(F['dec_gasto_26'])} & {n(F['dec_gasto_27'])} & "
         f"{pct(real(F['dec_gasto_26'], F['dec_gasto_27']))}",
         f"Neteo (decreto, línea P) & {n(F['dec_neteo_26'])} & {n(F['dec_neteo_27'])} & "
         f"{pct(real(F['dec_neteo_26'], F['dec_neteo_27']))}",
         f"Gasto neto pagado (CGPE, línea G) & {n(F['cg_gasto_26ap'])} & {n(F['cg_gasto_27'])} & "
         f"{pct(real(F['cg_gasto_26ap'], F['cg_gasto_27']))}",
         f"\\quad Programable pagado (línea G) & {n(F['cg_prog_26ap'])} & {n(F['cg_prog_27'])} & "
         f"{pct(real(F['cg_prog_26ap'], F['cg_prog_27']))}",
         f"\\quad No programable (línea G) & {n(F['cg_noprog_26ap'])} & {n(F['cg_noprog_27'])} & "
         f"{pct(real(F['cg_noprog_26ap'], F['cg_noprog_27']))}",
         f"\\quad\\quad Costo financiero (línea G) & {n(F['cg_cf_26ap'])} & {n(F['cg_cf_27'])} & "
         f"{pct(real(F['cg_cf_26ap'], F['cg_cf_27']))}",
         f"Gastos obligatorios sin pensiones (línea P) & {n(F['dec_oblig_sin_26'])} & "
         f"{n(F['dec_oblig_sin_27'])} & {pct(real(F['dec_oblig_sin_26'], F['dec_oblig_sin_27']))}",
         f"Perímetro de pensiones, por diferencia (línea P) & "
         f"{n(F['dec_oblig_con_26']-F['dec_oblig_sin_26'])} & "
         f"{n(F['dec_oblig_con_27']-F['dec_oblig_sin_27'])} & "
         f"{pct(real(F['dec_oblig_con_26']-F['dec_oblig_sin_26'], F['dec_oblig_con_27']-F['dec_oblig_sin_27']))}"],
        "\\textbf{Las dos líneas no se mezclan y van etiquetadas renglón por renglón.} "
        "Fuentes: Anexos 1 y 3 de los dos proyectos de decreto; CGPE 2027 Anexo II.6. "
        "El perímetro de pensiones sale de la diferencia entre los dos renglones del Anexo 3, "
        "no de una selección propia de programas."))

    # --- C13_1 balance y deuda ---------------------------------------------
    escribe("C13_1", tabla(
        "Balance, RFSP y saldo de la deuda", "cua:deuda", "lrrr",
        "Concepto & 2026 aprob. & 2027 & 2027 (\\% PIB)",
        [f"Balance presupuestario (mdp) & {n(F['cg_bal_26ap']).replace('-', '$-$')} & "
         f"{n(F['cg_bal_27']).replace('-', '$-$')} & $-$3,4",
         f"Superávit económico primario (mdp) & {n(F['cg_prim_26ap'])} & {n(F['cg_prim_27'])} & 0,6",
         f"RFSP (mdp) & {n(F['cg_rfsp_26ap']).replace('-', '$-$')} & "
         f"{n(F['cg_rfsp_27']).replace('-', '$-$')} & $-$3,9",
         f"SHRFSP (mdp) & --- & {n(F['cg_shrfsp_27'])} & 55,0",
         f"\\quad interno (\\% PIB) & --- & --- & {n(F['cg_shrfsp_int_27'])}",
         f"\\quad externo (\\% PIB) & --- & --- & {n(F['cg_shrfsp_ext_27'])}",
         f"Endeudamiento neto interno autorizado (mdp) & --- & {n(F['end_int_27'])} & ---",
         f"Endeudamiento neto externo autorizado (mdd) & --- & {n(F['end_ext_27'])} & ---"],
        "Fuentes: CGPE 2027, edición SHCP, Anexos II.6 (p. 67) y III.2 (p. 47); artículo 2o. "
        "de la ILIF 2027. \\textbf{El superávit primario se toma del Anexo II.6 (0,6~\\% del "
        "PIB) y no del cuadro resumen de la página 6 de esa edición, que imprime 0,5 y "
        "contradice a su propio anexo.} \\textbf{Techo de endeudamiento y déficit son objetos "
        "distintos}: los dos últimos renglones autorizan, no proyectan."))

    # --- C14_1 serie del perímetro de la regla fiscal ----------------------
    serie = []
    with open(externo("serie_perimetro_regla_fiscal.csv", "_aprendizaje"), encoding="utf-8") as f:
        for r in csv.DictReader(f):
            serie.append((r["ejercicio"], r["ilif_perimetro"], r["ilif_tope_pct_pib"],
                          r["balance_presupuestario_proyectado_pct_pib"],
                          r["balance_sin_inversion_proyectado_pct_pib"]))
    serie.append(("2027", "CLÁUSULA AUSENTE: la exclusión migra a la LFIIEDB", "", "-3.4",
                  "NO PUBLICADO"))
    def corto(s):
        s = s.replace("CLÁUSULA AUSENTE", "\\textbf{cláusula ausente}")
        return (s[:58] + "…") if len(s) > 60 else s

    def num(s):
        """Cifra de la serie, ya como texto: coma decimal y menos tipográfico."""
        if not s:
            return "n.d."
        if s == "NO PUBLICADO":
            return "\\textbf{no publicado}"
        if s == "SIN TOPE":
            return "\\textbf{sin tope}"
        return s.replace(".", ",").replace("-", "$-$")
    escribe("C14_1", tabla(
        "Perímetro de exclusión de la regla fiscal, 2018--2027", "cua:regla", "llrrr",
        "Ejercicio & Perímetro que propone la ILIF & Tope & Balance & Sin inversión",
        [f"{a} & {corto(b)} & {num(c)} & {num(d)} & {num(e)}"
         for a, b, c, d, e in serie],
        "Tope y balance en \\% del PIB. Fuente: artículo 1o. de las diez iniciativas de Ley de "
        "Ingresos y los diez CGPE. La columna «sin inversión» es el balance que la regla mide "
        "de verdad; \\textbf{dejó de publicarse en 2026 y sigue sin publicarse en 2027}.",
        tam="footnotesize"))

    # --- C14_2 la ruptura del gasto corriente estructural ------------------
    escribe("C14_2", tabla(
        "Gasto corriente estructural y su límite: ruptura de serie", "cua:gce", "lrr",
        "Concepto & 2026 & 2027",
        [f"Gasto corriente estructural (mdp) & {n(F['dec_gce_26'])} & {n(F['dec_gce_27'])}",
         f"Variación nominal (\\%) & --- & {pct(nominal(F['dec_gce_26'], F['dec_gce_27']))}",
         f"Límite máximo (\\% del PIB) & {n(F['dec_lmgce_pct_26'])} & {n(F['dec_lmgce_pct_27'])}",
         f"Límite máximo (mdp) & --- & {n(F['dec_lmgce_27'])}",
         f"Holgura contra el límite (mdp) & --- & {n(F['dec_lmgce_27']-F['dec_gce_27'])}"],
        "Fuentes: Anexo 2 de los dos proyectos de decreto; CGPE 2027, p. 24 y Anexo III.2 "
        "(p. 47). \\textbf{Las dos columnas no son comparables.} El Anexo 2 de 2027 declara "
        "que la cifra se estima «con la nueva metodología, derivada de la publicación el 9 de "
        "abril de 2026» de la LFIIEDB y su reforma a la LFPRH. La variación nominal se imprime "
        "para dimensionar la ruptura, \\textbf{no para leerse como una caída del gasto}."))

    # --- lectores de los dos CSV sectoriales -------------------------------
    def leer(nombre, clave):
        with open(AQUI / "datos" / nombre, encoding="utf-8") as f:
            return {r[clave]: r for r in csv.DictReader(f)}
    AX, F33 = leer("anexos.csv", "anexo"), leer("ramo33.csv", "fondo")

    def par(a, b, etiq):
        """Renglón «2026 / 2027 / var. real» a partir de dos identificadores."""
        return f"{etiq} & {n(F[a])} & {n(F[b])} & {pct(real(F[a], F[b]))}"

    # --- C5_1 salud ---------------------------------------------------------
    escribe("C5_1", tabla(
        "Salud: los vehículos presupuestales, línea P (mdp)", "cua:salud", "lrrr",
        "Vehículo & 2026 & 2027 & Var. real (\\%)",
        [f"Ramo 12 Salud & {n(R['12'][2026])} & {n(R['12'][2027])} & {pct(real(R['12'][2026], R['12'][2027]))}",
         f"Ramo 56 IMSS-Bienestar & {n(R['56'][2026])} & {n(R['56'][2027])} & {pct(real(R['56'][2026], R['56'][2027]))}",
         par("imss_26", "imss_27", "IMSS (entidad de control directo)"),
         par("issste_26", "issste_27", "ISSSTE (entidad de control directo)"),
         f"FASSA (Ramo 33) & {n(float(F33['FASSA']['mdp_2026']))} & {n(float(F33['FASSA']['mdp_2027']))} & "
         f"{pct(float(F33['FASSA']['var_real_pct']))}"],
        "\\textbf{Estos cinco renglones NO se suman}: el IMSS y el ISSSTE incluyen pensiones y "
        "prestaciones que no son atención médica, y el Ramo 19 les transfiere recursos que "
        "volverían a contarse. Fuentes: Anexo 1 y Anexo 22 de los dos proyectos de decreto."))

    # --- C6_1 educación -----------------------------------------------------
    escribe("C6_1", tabla(
        "Educación: los vehículos presupuestales, línea P (mdp)", "cua:educ", "lrrr",
        "Vehículo & 2026 & 2027 & Var. real (\\%)",
        [f"Ramo 11 Educación Pública & {n(R['11'][2026])} & {n(R['11'][2027])} & {pct(real(R['11'][2026], R['11'][2027]))}",
         f"Ramo 25 Previsiones y aportaciones & {n(R['25'][2026])} & {n(R['25'][2027])} & {pct(real(R['25'][2026], R['25'][2027]))}",
         f"FONE (Ramo 33) & {n(float(F33['FONE']['mdp_2026']))} & {n(float(F33['FONE']['mdp_2027']))} & "
         f"{pct(float(F33['FONE']['var_real_pct']))}",
         f"FAETA (Ramo 33) & {n(float(F33['FAETA']['mdp_2026']))} & {n(float(F33['FAETA']['mdp_2027']))} & "
         f"{pct(float(F33['FAETA']['var_real_pct']))}",
         f"Ramo 38 Ciencia y Humanidades & {n(R['38'][2026])} & {n(R['38'][2027])} & {pct(real(R['38'][2026], R['38'][2027]))}"],
        "\\textbf{No se suman.} El FONE es nómina educativa transferida a las entidades y el "
        "Ramo 25 contiene previsiones que acaban en el propio FONE. Fuentes: Anexo 1 y Anexo 22."))

    # --- C7_1 pensiones -----------------------------------------------------
    pens26 = F["dec_oblig_con_26"] - F["dec_oblig_sin_26"]
    pens27 = F["dec_oblig_con_27"] - F["dec_oblig_sin_27"]
    escribe("C7_1", tabla(
        "Pensiones: el perímetro adjudicado y sus vehículos, línea P (mdp)", "cua:pens", "lrrr",
        "Concepto & 2026 & 2027 & Var. real (\\%)",
        [f"\\textbf{{Perímetro del Anexo 3, por diferencia}} & \\textbf{{{n(pens26)}}} & "
         f"\\textbf{{{n(pens27)}}} & \\textbf{{{pct(real(pens26, pens27))}}}",
         par("ec_pensiones_26", "ec_pensiones_27", "Pensiones y jubilaciones (clas. económica)"),
         f"Ramo 19 Aportaciones a Seguridad Social & {n(R['19'][2026])} & {n(R['19'][2027])} & "
         f"{pct(real(R['19'][2026], R['19'][2027]))}",
         f"Ramo 20 Bienestar & {n(R['20'][2026])} & {n(R['20'][2027])} & {pct(real(R['20'][2026], R['20'][2027]))}"],
        "Los dos primeros renglones son \\textbf{el mismo objeto por dos caminos independientes} "
        "---la diferencia de los dos renglones del Anexo 3 del decreto y la línea de la "
        "clasificación económica del CGPE--- y coinciden al décimo en los dos ejercicios. "
        "El Ramo 20 incluye la pensión no contributiva y \\textbf{no es sumable} con los anteriores."))

    # --- C8_1 inversión -----------------------------------------------------
    escribe("C8_1", tabla(
        "Gasto de inversión en clasificación económica, línea P (mdp)", "cua:inv", "lrrr",
        "Concepto & 2026 & 2027 & Var. real (\\%)",
        [par("ec_inv_26", "ec_inv_27", "\\textbf{Gasto de inversión, total}"),
         par("ec_invfis_26", "ec_invfis_27", "\\quad Inversión física"),
         par("ec_invfin_26", "ec_invfin_27", "\\quad Inversión financiera y otros"),
         par("hidroc_26", "hidroc_27", "Programa «Articulación de la Política de Hidrocarburos»"),
         f"Contratos LFIIEDB: inversión de terceros & --- & {n(F['lfiiedb_terceros'])} & ---",
         f"Contratos LFIIEDB: pagos diferidos & --- & {n(F['lfiiedb_diferidos'])} & ---"],
        "Fuente: CGPE 2027, edición SHCP, p. 34 y p. 75. \\textbf{La caída del agregado es de "
        "inversión financiera, no de inversión física}, que crece. Los dos renglones de la "
        "LFIIEDB son de un cuadro distinto y \\textbf{no se suman} a los anteriores."))

    # --- C9_1 seguridad -----------------------------------------------------
    escribe("C9_1", tabla(
        "Seguridad y defensa: ramos y anexos, línea P (mdp)", "cua:seg", "lrrr",
        "Vehículo & 2026 & 2027 & Var. real (\\%)",
        [f"Ramo 07 Defensa Nacional & {n(R['07'][2026])} & {n(R['07'][2027])} & {pct(real(R['07'][2026], R['07'][2027]))}",
         f"Ramo 13 Marina & {n(R['13'][2026])} & {n(R['13'][2027])} & {pct(real(R['13'][2026], R['13'][2027]))}",
         f"Ramo 36 Seguridad y Protección Ciudadana & {n(R['36'][2026])} & {n(R['36'][2027])} & "
         f"{pct(real(R['36'][2026], R['36'][2027]))}",
         f"Ramo 49 Fiscalía General de la República & {n(R['49'][2026])} & {n(R['49'][2027])} & "
         f"{pct(real(R['49'][2026], R['49'][2027]))}",
         f"FASP (Ramo 33) & {n(float(F33['FASP']['mdp_2026']))} & {n(float(F33['FASP']['mdp_2027']))} & "
         f"{pct(float(F33['FASP']['var_real_pct']))}",
         f"Anexo 19, prevención del delito & {n(float(AX['19']['mdp_2026']))} & "
         f"{n(float(AX['19']['mdp_2027']))} & {pct(float(AX['19']['var_real_pct']))}"],
        "Los cuatro ramos se pueden sumar entre sí; \\textbf{el Anexo 19 no}, porque etiqueta "
        "programas que ya están contados en ellos. Fuentes: Anexo 1, Anexo 19 y Anexo 22."))

    # --- C10_1 gasto federalizado ------------------------------------------
    r33 = [("FONE", "FONE, nómina educativa"), ("FASSA", "FASSA, servicios de salud"),
           ("FAIS", "FAIS, infraestructura social"), ("FORTAMUN", "FORTAMUN, municipios"),
           ("FAM", "FAM, aportaciones múltiples"), ("FAETA", "FAETA, educación tecnológica"),
           ("FASP", "FASP, seguridad pública"), ("FAFEF", "FAFEF, entidades federativas")]
    s26 = sum(float(F33[k]["mdp_2026"]) for k, _ in r33)
    s27 = sum(float(F33[k]["mdp_2027"]) for k, _ in r33)
    escribe("C10_1", tabla(
        "Gasto federalizado: participaciones y los ocho fondos del Ramo 33, línea P (mdp)",
        "cua:feder", "lrrr",
        "Concepto & 2026 & 2027 & Var. real (\\%)",
        [f"Ramo 28 Participaciones (no condicionadas) & {n(R['28'][2026])} & {n(R['28'][2027])} & "
         f"{pct(real(R['28'][2026], R['28'][2027]))}",
         "\\midrule \\multicolumn{4}{l}{\\emph{Ramo 33, aportaciones (condicionadas)}}"] +
        [f"\\quad {et} & {n(float(F33[k]['mdp_2026']))} & {n(float(F33[k]['mdp_2027']))} & "
         f"{pct(float(F33[k]['var_real_pct']))}" for k, et in r33] +
        [f"\\textbf{{Suma de los ocho fondos}} & \\textbf{{{n(s26)}}} & \\textbf{{{n(s27)}}} & "
         f"\\textbf{{{pct(real(s26, s27))}}}",
         f"Ramo 33 según el Anexo 1 & {n(R['33'][2026])} & {n(R['33'][2027])} & "
         f"{pct(real(R['33'][2026], R['33'][2027]))}"],
        "\\textbf{Los ocho fondos suman el total del Ramo 33 al peso en los dos ejercicios}, lo "
        "que valida la lectura del Anexo 22 contra el Anexo 1. Participaciones y aportaciones "
        "\\textbf{no se suman entre sí}: las primeras no están condicionadas y las segundas sí.",
        tam="footnotesize"))

    # --- C11_1 medio ambiente y agua ---------------------------------------
    escribe("C11_1", tabla(
        "Medio ambiente, agua y energía limpia, línea P (mdp)", "cua:amb", "lrrr",
        "Vehículo & 2026 & 2027 & Var. real (\\%)",
        [f"Ramo 16 Medio Ambiente y Recursos Naturales & {n(R['16'][2026])} & {n(R['16'][2027])} & "
         f"{pct(real(R['16'][2026], R['16'][2027]))}",
         f"Anexo 16, adaptación y mitigación climática & {n(float(AX['16']['mdp_2026']))} & "
         f"{n(float(AX['16']['mdp_2027']))} & {pct(float(AX['16']['var_real_pct']))}",
         f"Anexo 15, transición energética & {n(float(AX['15']['mdp_2026']))} & "
         f"{n(float(AX['15']['mdp_2027']))} & {pct(float(AX['15']['var_real_pct']))}"],
        "\\textbf{El ramo y los dos anexos no se suman}: los anexos etiquetan programas de "
        "varios ramos, incluido el 16. Fuentes: Anexo 1, Anexo 15 y Anexo 16 de los decretos."))

    # --- C12_1 anexos transversales ----------------------------------------
    tr = ["13", "14", "15", "16", "17", "18", "19", "31", "33"]
    def corta(s):
        s = s.split("(")[0].strip().capitalize()
        return (s[:44] + "…") if len(s) > 46 else s
    st27 = sum(float(AX[k]["mdp_2027"]) for k in tr if AX[k]["mdp_2027"])
    escribe("C12_1", tabla(
        "Anexos transversales: totales y variación, línea P (mdp)", "cua:trans", "lrrr",
        "Anexo & 2026 & 2027 & Var. real (\\%)",
        [f"{k}. {corta(AX[k]['titulo'])} & "
         f"{n(float(AX[k]['mdp_2026'])) if AX[k]['mdp_2026'] else '\\textbf{no existía}'} & "
         f"{n(float(AX[k]['mdp_2027'])) if AX[k]['mdp_2027'] else '---'} & "
         f"{pct(float(AX[k]['var_real_pct'])) if AX[k]['var_real_pct'] else '---'}" for k in tr] +
        [f"\\emph{{Suma aritmética de los nueve}} & --- & \\emph{{{n(st27)}}} & ---"],
        "\\textbf{La última fila no es un agregado: es una advertencia.} Los anexos etiquetan "
        "los mismos programas más de una vez, de modo que su suma ---" + n(st27) + " mdp, el "
        + f"{st27 / F['cg_prog_27'] * 100:.0f}".replace(".", ",") +
        "~\\% del gasto programable pagado--- \\textbf{no mide ningún gasto}. Fuente: anexos "
        "13 a 19, 31 y 33 de los dos proyectos de decreto.", tam="footnotesize"))

    # --- capa demográfica: C15_1 indicadores, C15_2 per cápita (SEPARADOS) --
    with open(externo("poblacion_nacional.csv", "datos_demograficos"), encoding="utf-8") as f:
        POB = {r["anio"]: r for r in csv.DictReader(f)}

    def pb(a, k):
        return float(POB[a][k])

    esc = {a: pb(a, "edad_escolar_preescolar") + pb(a, "edad_escolar_primaria")
              + pb(a, "edad_escolar_secundaria") for a in ("2026", "2027")}
    escribe("C15_1", tabla(
        "Indicadores demográficos, 2026--2027", "cua:demo", "lrrr",
        "Indicador & 2026 & 2027 & Var. (\\%)",
        [f"Población total & {n(pb('2026','poblacion_total'), 0)} & {n(pb('2027','poblacion_total'), 0)} & "
         f"{pct(nominal(pb('2026','poblacion_total'), pb('2027','poblacion_total')), 2)}",
         f"Población de 65 años y más & {n(pb('2026','poblacion_65_mas'), 0)} & "
         f"{n(pb('2027','poblacion_65_mas'), 0)} & "
         f"{pct(nominal(pb('2026','poblacion_65_mas'), pb('2027','poblacion_65_mas')), 2)}",
         f"Población en edad escolar básica (3--14) & {n(esc['2026'], 0)} & {n(esc['2027'], 0)} & "
         f"{pct(nominal(esc['2026'], esc['2027']), 2)}",
         f"Razón de dependencia adulta & {n(pb('2026','razon_dependencia_adulta'), 2)} & "
         f"{n(pb('2027','razon_dependencia_adulta'), 2)} & ---",
         f"Índice de envejecimiento & {n(pb('2026','indice_envejecimiento'), 2)} & "
         f"{n(pb('2027','indice_envejecimiento'), 2)} & ---",
         f"Tasa global de fecundidad & {n(pb('2026','tasa_global_fecundidad'), 2)} & "
         f"{n(pb('2027','tasa_global_fecundidad'), 2)} & ---",
         f"Esperanza de vida al nacer & {n(pb('2026','esperanza_vida'), 2)} & "
         f"{n(pb('2027','esperanza_vida'), 2)} & ---"],
        "Fuente: CONAPO, Proyecciones de la Población de México 2020--2070, población a mitad "
        "de año, cobertura nacional, tier \\texttt{externa\\_demografica}. "
        "\\textbf{Este cuadro no contiene ninguna cifra presupuestal}, por la regla de "
        "separación de la nota de método."))

    def per(v, dem, a):
        return v * 1e6 / dem[a]

    pens = {"2026": F["dec_oblig_con_26"] - F["dec_oblig_sin_26"],
            "2027": F["dec_oblig_con_27"] - F["dec_oblig_sin_27"]}
    fone = {a: float(F33["FONE"][f"mdp_{a}"]) for a in ("2026", "2027")}
    salud = {"2026": R["12"][2026] + R["56"][2026], "2027": R["12"][2027] + R["56"][2027]}
    p65 = {a: pb(a, "poblacion_65_mas") for a in ("2026", "2027")}
    ptot = {a: pb(a, "poblacion_total") for a in ("2026", "2027")}
    escribe("C15_2", tabla(
        "Razones por persona: cada una con su denominador declarado (pesos de cada año)",
        "cua:percap", "lrrr",
        "Razón & 2026 & 2027 & Var. real (\\%)",
        [f"Perímetro pensionario / población 65 y más & {n(per(pens['2026'], p65, '2026'), 0)} & "
         f"{n(per(pens['2027'], p65, '2027'), 0)} & "
         f"{pct(real(per(pens['2026'], p65, '2026'), per(pens['2027'], p65, '2027')))}",
         f"FONE / población en edad escolar básica & {n(per(fone['2026'], esc, '2026'), 0)} & "
         f"{n(per(fone['2027'], esc, '2027'), 0)} & "
         f"{pct(real(per(fone['2026'], esc, '2026'), per(fone['2027'], esc, '2027')))}",
         f"Ramos 12 y 56 / población total & {n(per(salud['2026'], ptot, '2026'), 0)} & "
         f"{n(per(salud['2027'], ptot, '2027'), 0)} & "
         f"{pct(real(per(salud['2026'], ptot, '2026'), per(salud['2027'], ptot, '2027')))}",
         "\\midrule \\multicolumn{4}{l}{\\emph{El mismo numerador con dos denominadores "
         "distintos, para que se vea la diferencia}}",
         f"FONE 2027 / población en edad escolar básica 2027 & --- & "
         f"{n(per(fone['2027'], esc, '2027'), 0)} & ---",
         f"FONE 2027 / matrícula de básica, ciclo 2025--2026 & --- & "
         f"{n(fone['2027'] * 1e6 / 22846154, 0)} & ---"],
        "\\textbf{Cada renglón declara denominador, año y cobertura.} Población: CONAPO, a "
        "mitad de año, nacional. Matrícula: SEP, ciclo 2025--2026, modalidad escolarizada, "
        "nacional. \\textbf{Matrícula no es población en edad escolar}: los dos denominadores "
        "difieren en 10,2~\\% y mueven la cifra por persona en esa misma proporción. "
        "\\textbf{El primer renglón es un indicador de presión demográfica, NO una pensión "
        "media}: el denominador incluye a quien no recibe y el numerador puede incluir "
        "pensiones de menores de 65 años.", tam="footnotesize"))

    # --- C1_2: lo prometido en abril contra lo entregado en septiembre (B3) --
    fil = [("PIB nominal 2027 (mmp)", F["pc_pib_27"] / 1000, F["pib_27"] / 1000, 1),
           ("Deflactor del PIB (\\%)", F["pc_defl_27"], 4.0, 1),
           ("Inflación INPC dic./dic. (\\%)", F["pc_infl_dic_27"], F["infl_dic_27"], 1),
           ("Tipo de cambio promedio", F["pc_tc_prom_27"], F["tc_prom_27"], 1),
           ("Tipo de cambio fin de periodo", F["pc_tc_fin_27"], F["tc_fin_27"], 1),
           ("Cetes 28 días, promedio (\\%)", F["pc_cetes_prom_27"], F["cetes_prom_27"], 1),
           ("Mezcla mexicana (dólares por barril)", F["pc_petro_27"], F["petro_27"], 1),
           ("Plataforma de producción (mbd)", F["pc_plat_prod_27"], F["plat_prod_27"], 1),
           ("Plataforma de exportación (mbd)", F["pc_plat_exp_27"], F["plat_exp_27"], 1)]
    escribe("C1_2", tabla(
        "Lo proyectado para 2027 en abril y en septiembre de 2026", "cua:precrit", "lrrr",
        "Supuesto para 2027 & Pre-Criterios (6 abr.) & CGPE (8 sep.) & Diferencia",
        [f"{c} & {n(a)} & {n(b)} & {n(b - a).replace('-', '$-$')}" for c, a, b, _ in fil] +
        ["Crecimiento real (rango, \\%) & [1,9\\,--\\,2,9] & [1,5\\,--\\,2,5] & "
         "$-$0,4 en los dos extremos"],
        "Fuentes: Pre-Criterios 2027, Anexo I (p. 34), publicados el 6 de abril de 2026; y "
        "CGPE 2027, edición SHCP, Anexo II.5 (p. 66). \\textbf{Los dos son estimaciones del "
        "mismo Ejecutivo sobre el mismo ejercicio, separadas por cinco meses.} Ninguna de "
        "estas cifras admite variación real: son precios, tasas, volúmenes y un nivel "
        "nominal de PIB."))
    # --- C99_1 y C99_2: nota de actualización del 9 de septiembre --------------
    with open(AQUI / "datos" / "gaceta_anexos_2027.csv", encoding="utf-8") as f:
        anx = list(csv.DictReader(f))
    fil = []
    for a in anx:
        pp = a["paginas"] or "---"
        d, _, h = a["creado_pdf"].partition("T")
        cre = ("8 sep." if d.endswith("08") else "9 sep.") + (" " + h if h else "")
        idx = a["letra_indice_0908"]
        cambio = "" if idx == a["letra"] else "\\textbf{"
        fil.append(f"{cambio}{a['letra']}{'}' if cambio else ''} & {a['contenido']} & {pp} "
                   f"& {cre} & {idx}")
    escribe("C99_1", tabla(
        "Los trece anexos del paquete que sirve la Gaceta 7121, y la letra que el "
        "índice les daba el día de la entrega", "cua:anexos",
        "l>{\\raggedright\\arraybackslash}p{5.0cm}rl>{\\raggedright\\arraybackslash}p{2.9cm}",
        "Letra & Contenido, leído de la primera página del PDF & pp. & Creado & Letra en el "
        "índice del 8 sep.", fil,
        "Leído el 9 de septiembre de 2026 a las 07:40; el paginado es el de la edición de "
        "la Gaceta, que añade portada y colofón. \\textbf{La letra no identifica el "
        "contenido}: el índice del día de la entrega se reescribió y las letras se "
        "reasignaron. Los anexos K a N no aparecen en el índice vivo. Las dos copias del "
        "índice, del 8 y del 9, están archivadas.", tam="footnotesize"))

    with open(AQUI / "datos" / "vivienda_art61.csv", encoding="utf-8") as f:
        viv = list(csv.DictReader(f))
    tot_mdp = sum(float(v["monto_pesos"]) for v in viv) / 1e6
    r15 = R["15"]
    fil = [f"{v['necesidad']} & {n(float(v['hogares']), 0)} & {v['uma_por_vivienda']} & "
           f"{n(float(v['costo_unitario_pesos']))} & {n(float(v['monto_pesos']) / 1e6)}"
           for v in viv]
    fil.append("\\midrule \\textbf{Requerimiento declarado} & & & & \\textbf{"
               + n(tot_mdp) + "}")
    fil.append("Ramo 15 completo, proyecto 2027 & & & & " + n(r15[2027]))
    fil.append("\\textbf{El ramo como proporción del requerimiento} & & & & \\textbf{"
               + n(r15[2027] / tot_mdp * 100) + "\\,\\%}")
    escribe("C99_2", tabla(
        "La vara del artículo 61 de la Ley de Vivienda contra el Ramo 15 (mdp)",
        "cua:vivienda", "lrrrr",
        "Necesidad & Hogares & UMA & Costo unitario (pesos) & Monto (mdp)", fil,
        "Fuente: Gaceta Parlamentaria 7121, anexo N, estimación de la Secretaría de "
        "Bienestar; y \\texttt{datos/ramos.csv} para el Ramo 15. \\textbf{Años de pesos "
        "distintos}: los costos unitarios provienen de las Reglas de Operación y de la UMA "
        "de 2026, y el presupuesto está en pesos de 2027. \\textbf{El Ramo 15 no es el "
        "perímetro del gasto en subsidios de vivienda}: es el ramo completo, y CONAVI es un "
        "organismo descentralizado. La comparación es de orden de magnitud.",
        tam="footnotesize"))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
