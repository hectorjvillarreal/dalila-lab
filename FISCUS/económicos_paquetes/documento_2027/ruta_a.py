#!/usr/bin/env python3
"""Ruta A del ejercicio 2027: todo lo que exige los analíticos del proyecto.

Los analíticos del PPEF 2027 no estaban en la ruta conocida (…/PPEF2027/analiticosPresupuestarios/
Proyecto/, 404 del 8 al 10 de septiembre). Se localizaron el 12 de septiembre en el árbol
`ppef.hacienda.gob.mx/work/models/PP3F2709/PPEF2027/yik327fP/analiticosPresupuestarios/`, sin el
segmento `/Proyecto/`, a partir de las referencias del documento de CIEP. Descargados 2026-09-12 23:08.

    python ruta_a.py            # escribe datos/ruta_a/*.csv e imprime el resumen con sus pruebas

Línea P en todo: proyecto 2027 contra proyecto 2026. Deflactor del PIB 1,040 (CGPE 2027).
Nada aquí reescribe el documento: produce los insumos de una nota de actualización.
"""
from __future__ import annotations
import re, subprocess, sys
from pathlib import Path
import pandas as pd

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
sys.path.insert(0, str(RAIZ / "_herramientas"))
from fiscus import analitico, clave, cod_pp, deflactor  # noqa: E402

SAL = AQUI / "datos" / "ruta_a"
SAL.mkdir(parents=True, exist_ok=True)
BUILD = AQUI / "_build"
DE, AL = 2026, 2027
D = deflactor(AL)
FALLAS: list[str] = []


def prueba(nombre: str, ok: bool, detalle: str = "") -> None:
    print(f"  [{'ok' if ok else 'FALLA'}] {nombre} {detalle}")
    if not ok:
        FALLAS.append(nombre)


def var(a: float, b: float) -> float:
    return (b / (a * D) - 1) * 100 if a else float("nan")


def tabla(ga: pd.Series, gb: pd.Series, nombre: str) -> pd.DataFrame:
    t = pd.DataFrame({f"mdp_{DE}": ga, f"mdp_{AL}": gb}).fillna(0.0)
    t["dif_nominal"] = t[f"mdp_{AL}"] - t[f"mdp_{DE}"]
    t["var_real_pct"] = [var(a, b) for a, b in zip(t[f"mdp_{DE}"], t[f"mdp_{AL}"])]
    t.index.name = t.index.name or "clave"
    # tres decimales: los cuadros suman renglones, y sumar renglones redondeados al décimo deriva
    t.round(3).to_csv(SAL / f"{nombre}.csv", float_format="%.3f")
    return t


# ---------------------------------------------------------------- analíticos
def cortes(y: int):
    gp = analitico(y, "gf-ramo-programa-ur-objeto"); ep = analitico(y, "entidades-ramo-programa-ur-objeto")
    gf = analitico(y, "gf-ramo-funcion-ur-objeto"); ef = analitico(y, "entidades-ramo-funcion-ur-objeto")
    for X, col in ((gp, "RAMO"), (gf, "RAMO"), (ep, "ENTIDAD"), (ef, "ENTIDAD")):
        X["INST"] = clave(X[col]).str.zfill(2)
        X["TG_K"] = clave(X["TG"])
        X["OG"] = X["PE"].astype(str).str.strip().str[:5]
        X["CAP"] = X["OG"].str[0]
        X["FN_K"] = clave(X["F"]) + "." + clave(X["FN"])
        X["SF_K"] = X["FN_K"] + "." + clave(X["SF"])
    gp["K"] = gp.INST + "-" + cod_pp(gp)
    ep["K"] = ep.INST + "-" + ep["PP"].astype(str).str.strip().str[:4]
    return gp, ep, gf, ef


# ---------------------------------------------------------------- anexos transversales del decreto
NUMS = r"\d{1,3}(?:,\d{3})+"
P_AMT_ONLY = re.compile(rf"^\s*([A-Z]\d{{3}})\s+({NUMS})\s*$")
P_CODE_ONLY = re.compile(r"^\s*([A-Z]\d{3})\s*$")
P_FULL = re.compile(rf"^\s*([A-Z]\d{{3}})\s+(.*\S)\s+({NUMS}|\d{{1,3}})\s*$")
P_NAME = re.compile(r"^\s*([A-Z]\d{3})\s+(.*\S)\s*$")
NUM = re.compile(rf"^\s*({NUMS})\s*$")
OBJ = re.compile(r"^\s{0,4}\d+\.\s")
RAMO = re.compile(rf"^\s*(\d{{1,2}})\s+([^\d\s].*?)\s{{2,}}({NUMS}|\d{{1,3}})\s*$")
ENT = {"Instituto Mexicano del Seguro Social": "GYR",
       "Instituto de Seguridad y Servicios Sociales de los Trabajadores del Estado": "GYN",
       "Petróleos Mexicanos": "TYY", "Comisión Federal de Electricidad": "TVV"}
RUIDO = re.compile(r"^\s*(PRESIDENCIA DE LA REPÚBLICA|\d{1,3})\s*$")
ANEXOS = (13, 14, 15, 16, 17, 18, 19, 31, 32, 33)


def mdp(s: str) -> float:
    return int(s.replace(",", "")) / 1e6


def texto_decreto(y: int) -> list[str]:
    BUILD.mkdir(exist_ok=True)
    f = BUILD / f"decreto_{y}.txt"
    if not f.exists():
        subprocess.run(["pdftotext", "-layout", str(RAIZ / str(y) / f"{y}_ppef_proyecto-decreto.pdf"), str(f)],
                       check=True)
    return f.read_text().split("\n")


def bloques(t: list[str], y: int) -> dict[int, tuple[int, int]]:
    hs = [(i, int(m.group(1))) for i, l in enumerate(t) if (m := re.match(r"\s*ANEXO\s+(\d+)\.", l))]
    out = {}
    for k, (i, a) in enumerate(hs):
        if a in ANEXOS:
            out[a] = (i, hs[k + 1][0] if k + 1 < len(hs) else len(t))
    if y == 2027:
        # El Anexo 32 no trae encabezado ni «Total general» en el decreto: arranca a media tabla
        # (p. 242 del PDF). Empieza en el renglón de ramo previo a su primera acción visible.
        c = next(i for i, l in enumerate(t) if "Certificación de personas en materia de mov" in l)
        s = max(i for i in range(out[31][0], c) if re.match(rf"^\s*11 Educación Pública\s+{NUMS}\s*$", t[i]))
        out[31] = (out[31][0], s)
        out[32] = (s, out[33][0])
    return out


def ramo_de(l: str) -> str | None:
    if (m := RAMO.match(l)):
        return m.group(1).zfill(2)
    return ENT.get(re.sub(rf"\s{{2,}}{NUMS}\s*$", "", l.strip()))


def parse_anexos(y: int):
    t = texto_decreto(y)
    filas, totales, brechas = [], {}, []
    for a, (i, j) in sorted(bloques(t, y).items()):
        L = t[i:j]
        tg = [mdp(m.group(1)) for l in L if re.match(r"\s*Total( general)?\s", l) and (m := re.search(rf"({NUMS})\s*$", l))]
        totales[a] = tg[0] if tg else None
        ramo, r_amt, acc, prev = None, 0.0, 0.0, ""

        def cierra():
            if ramo and abs(r_amt - acc) > 0.05:
                brechas.append(dict(ejercicio=y, anexo=a, ramo=ramo, mdp_ramo=r_amt, mdp_programas=acc))
        for k, l in enumerate(L):
            if not l.strip() or RUIDO.match(l) or re.match(r"\s*Total", l) or "ANEXO" in l:
                continue
            if OBJ.match(l):
                cierra(); ramo, acc = None, 0.0; prev = l; continue
            code = nombre = amt = None
            if (m := P_AMT_ONLY.match(l)):
                code, amt, nombre = m.group(1), m.group(2), prev.strip()
            elif (m := P_CODE_ONLY.match(l)):
                code, nombre = m.group(1), prev.strip()
            elif (m := P_FULL.match(l)):
                code, nombre, amt = m.group(1), m.group(2), m.group(3)
            elif (m := P_NAME.match(l)):
                code, nombre = m.group(1), m.group(2)
            if code:
                if amt is None:
                    amt = next((mm.group(1) for q in L[k + 1:k + 3] if (mm := NUM.match(q))), None)
                if amt is not None:
                    v = mdp(amt); acc += v
                    filas.append(dict(ejercicio=y, anexo=a, ramo=ramo, pp=code,
                                      nombre=re.sub(r"\s+", " ", nombre or "")[:120], mdp=v))
                prev = l; continue
            r = ramo_de(l)
            if r:
                nxt = next((q for q in L[k + 1:k + 4] if q.strip() and not RUIDO.match(q)), "")
                cierra()
                ramo, r_amt, acc = r, mdp(re.search(rf"({NUMS}|\d{{1,3}})\s*$", l).group(1)), 0.0
                if ramo_de(nxt):          # encabezado de sector (p. ej. «47 Entidades no Sectorizadas»)
                    ramo = None
            prev = l
        cierra()
    df = pd.DataFrame(filas)
    df["K"] = df.ramo + "-" + df.pp
    return df, totales, pd.DataFrame(brechas)


# ---------------------------------------------------------------- CGPE y Pre-Criterios, extraídos del PDF
def _pdf(pieza: str, pag: int) -> list[str]:
    f = RAIZ / "2027" / pieza
    return subprocess.run(["pdftotext", "-layout", "-f", str(pag), "-l", str(pag), str(f), "-"],
                          capture_output=True, text=True, check=True).stdout.split("\n")


def _num(s: str) -> float:
    return float(s.replace(",", ""))


def extraer_cgpe_y_precriterios() -> None:
    """Tres tablas que estaban en carpeta desde el 8 de septiembre y el documento no usó.
    Se extraen del PDF, nunca se teclean; se escriben en datos/ y en _fuentes.csv."""
    cg, pc = "2027_cgpe_criterios-generales.pdf", "2027_precgpe_pre-criterios.pdf"
    # (a) CGPE p. 24: límite máximo del gasto corriente estructural, con la metodología nueva
    filas = []
    for l in _pdf(cg, 24):
        m = re.match(r"^\s*(A\)|B\)|C\)|D\)|\(\d+\)|Diferimiento de pagos|Actualización por precios|"
                     r"Crecimiento real propuesto)\s*(.*?)\s{2,}(-?[\d,]+\.\d)\s*$", l)
        if m:
            filas.append((m.group(1), re.sub(r"\d/$", "", (m.group(1) + " " + m.group(2)).strip()).strip(),
                          _num(m.group(3))))
    ren = []
    anio = None
    for k, (c, concepto, v) in enumerate(filas):
        if c in ("Actualización por precios", "Crecimiento real propuesto"):
            anio = 2026 if sum(1 for x in filas[:k] if x[0] == c) == 0 else 2027
            ren.append(dict(clave=f"{c[:4].lower()}_{anio}", concepto=f"{concepto} {anio}", valor=v, unidad="pct"))
        else:
            k_ = "Dife" if c.startswith("Diferimiento") else c.strip("()").replace(")", "")
            ren.append(dict(clave=k_, concepto=concepto, valor=v, unidad="mdp"))
    g = pd.DataFrame(ren)
    g.to_csv(AQUI / "datos" / "gce_limite_2027.csv", index=False, float_format="%.1f")
    V = dict(zip(g.clave, g.valor))
    exclus = sum(V[str(i)] for i in range(1, 11))
    # tolerancia 0,5: el cuadro publica once cifras redondeadas al décimo
    prueba("CGPE p. 24: A menos (1)…(10) = B", abs(V["A"] - exclus - V["B"]) < 0.5,
           f"({V['A'] - exclus:,.1f} vs {V['B']:,.1f})")
    prueba("CGPE p. 24: B + diferimiento = C", abs(V["B"] + V["Dife"] - V["C"]) < 0.2)
    D_ = V["C"] * (1 + V["actu_2026"] / 100) * (1 + V["crec_2026"] / 100) * (1 + V["actu_2027"] / 100) * (1 + V["crec_2027"] / 100)
    prueba("CGPE p. 24: C actualizada por precios y crecimiento = D (redondeo de tasas)",
           abs(D_ / V["D"] - 1) < 0.0005, f"({D_:,.1f} vs {V['D']:,.1f})")
    nuevos = sum(V[str(i)] for i in (7, 8, 9, 10))
    print(f"  rubros nuevos (7)–(10): {nuevos:,.1f} mdp de la CP 2025")

    # (b) CGPE p. 32: programas sociales prioritarios y prioridades de inversión (dos columnas)
    izq, der = [], []
    # la paginación impresa y la del PDF no coinciden: se localiza la página por su contenido
    pag = next(p for p in range(28, 40) if any("Prioridades de inversión" in l for l in _pdf(cg, p)))
    print(f"  tablas de programas prioritarios: página {pag} del PDF")
    for l in _pdf(cg, pag):
        m = re.match(r"^\s{3,10}(\S.*?)\s{2,}([\d,]+\.\d)\s{3,}(\S.*?)\s{2,}([\d,]+\.\d)\s*$", l)
        if m:
            izq.append((m.group(1).strip(), _num(m.group(2)))); der.append((m.group(3).strip(), _num(m.group(4))))
    t32 = pd.DataFrame([dict(tabla="programas_sociales", concepto=c, mdp=v) for c, v in izq]
                       + [dict(tabla="prioridades_inversion", concepto=re.sub(r"\s*\d/$", "", c), mdp=v) for c, v in der])
    t32.to_csv(AQUI / "datos" / "cgpe_p32_2027.csv", index=False, float_format="%.1f")
    S_ = dict(zip(t32[t32.tabla == "programas_sociales"].concepto, t32[t32.tabla == "programas_sociales"].mdp))
    I_ = t32[t32.tabla == "prioridades_inversion"]
    nc = S_["Pensión para Adultos Mayores"] + S_["Pensión Mujeres Bienestar"] + S_["Pensión Personas con Discapacidad"]
    prueba("CGPE p. 32: inversión, 12 renglones de primer nivel suman el total",
           abs(I_[I_.concepto.str.match(r"^\d+\. ")].mdp.sum() - I_[I_.concepto == "Total"].mdp.iat[0]) < 0.2)
    prueba("CGPE p. 32: tres pensiones no contributivas = 640,291.0 (CIEP)", abs(nc - 640291.0) < 0.1)

    # (c) Pre-Criterios p. 32: RFSP y SHRFSP para 2027
    pre = {}
    for l in _pdf(pc, 32):
        m = re.match(r"^\s*(RFSP|SHRFSP)\s+(-?[\d,]+\.\d)\s+(-?[\d,]+\.\d)\s+(-?[\d,]+\.\d)\s+(-?\d+\.\d)\s+(-?\d+\.\d)\s+(-?\d+\.\d)", l)
        if m:
            pre[m.group(1)] = (_num(m.group(4)), float(m.group(7)))
    prueba("Pre-Criterios p. 32: RFSP y SHRFSP 2027 extraídos", set(pre) == {"RFSP", "SHRFSP"}, str(pre))

    # (d) al registro de fuentes, sin duplicar
    f = AQUI / "datos" / "_fuentes.csv"
    fu = pd.read_csv(f, dtype=str)
    alta = [
        dict(id="pc_rfsp_27", concepto="RFSP", ejercicio="2027", etapa="pre-criterios", valor=pre["RFSP"][0], unidad="mdp", documento="Pre-Criterios 2027", ubicacion="p. 32"),
        dict(id="pc_rfsp_pct_27", concepto="RFSP", ejercicio="2027", etapa="pre-criterios", valor=pre["RFSP"][1], unidad="pct del PIB", documento="Pre-Criterios 2027", ubicacion="p. 32"),
        dict(id="pc_shrfsp_27", concepto="SHRFSP", ejercicio="2027", etapa="pre-criterios", valor=pre["SHRFSP"][0], unidad="mdp", documento="Pre-Criterios 2027", ubicacion="p. 32"),
        dict(id="pc_shrfsp_pct_27", concepto="SHRFSP", ejercicio="2027", etapa="pre-criterios", valor=pre["SHRFSP"][1], unidad="pct del PIB", documento="Pre-Criterios 2027", ubicacion="p. 32"),
        dict(id="cg_p32_pens_nc_27", concepto="Pensiones no contributivas (Adultos Mayores, Mujeres, Discapacidad)", ejercicio="2027", etapa="proyecto", valor=round(nc, 1), unidad="mdp", documento="CGPE 2027 (ed. SHCP)", ubicacion="p. 32, Programas sociales prioritarios"),
        dict(id="cg_p32_inv_total_27", concepto="Prioridades de inversion, total", ejercicio="2027", etapa="proyecto", valor=I_[I_.concepto == "Total"].mdp.iat[0], unidad="mdp", documento="CGPE 2027 (ed. SHCP)", ubicacion="p. 32, Prioridades de inversion"),
        dict(id="cg_gce_nuevos_rubros_cp25", concepto="Rubros (7) a (10) excluidos del gasto corriente estructural", ejercicio="2025", etapa="cuenta publica", valor=round(nuevos, 1), unidad="mdp", documento="CGPE 2027 (ed. SHCP)", ubicacion="p. 24"),
        dict(id="an_73903_27", concepto="Ramo 18 partida 73903 aportaciones de capital", ejercicio="2027", etapa="proyecto", valor=81103.0, unidad="mdp", documento="Analitico PPEF 2027 GF ramo-programa-UR-objeto", ubicacion="Hoja1, ramo 18, PE 73903"),
    ]
    fu = fu[~fu.id.isin([a["id"] for a in alta])]
    pd.concat([fu, pd.DataFrame(alta).astype(str)]).to_csv(f, index=False)
    print(f"  _fuentes.csv: {len(alta)} renglones de la tercera nota registrados")


# ================================================================ corrida
def main() -> int:
    A, B = cortes(DE), cortes(AL)
    print(f"RUTA A {AL} · línea P {DE}->{AL} · deflactor {D}")

    print("\n1. Identidades de los analíticos contra el Anexo 1 del decreto")
    r = pd.read_csv(AQUI / "datos" / "ramos.csv")
    for y, (gp, ep, _, _) in ((DE, A), (AL, B)):
        a1 = r[r.ejercicio == y].assign(k=lambda z: z.ramo.astype(str).str.zfill(2)).set_index("k").mdp
        g = gp.groupby("INST").MDP.sum()
        d = (g.reindex(a1.index) - a1).abs()
        prueba(f"{y}: {len(a1)} ramos del Anexo 1 = analítico GF", d.max() < 0.1, f"(máx {d.max():.2f} mdp)")
    ent27 = {"GYR": 1803009.1, "GYN": 571592.3, "TYY": 678662.7, "TVV": 575215.6}
    e = B[1].groupby("INST").MDP.sum()
    prueba("2027: IMSS, ISSSTE, Pemex, CFE = Anexo 1 / CIEP", all(abs(e[k] - v) < 0.2 for k, v in ent27.items()))

    print("\n2. Pensiones y jubilaciones (TG 4) por institución")
    ga = pd.concat([A[0][A[0].TG_K == "4"], A[1][A[1].TG_K == "4"]]).groupby("INST").MDP.sum()
    gb = pd.concat([B[0][B[0].TG_K == "4"], B[1][B[1].TG_K == "4"]]).groupby("INST").MDP.sum()
    pen = tabla(ga, gb, "pensiones_tg4_institucion")
    print(pen.round(1).to_string())
    gf = {DE: 1704159.2, AL: 1840746.1}      # perímetro Anexo 3, por diferencia
    for y, g in ((DE, ga), (AL, gb)):
        epe = g[["GYR", "GYN", "TYY", "TVV"]].sum()
        print(f"  {y}: Anexo 3 {gf[y]:,.1f} = entidades {epe:,.1f} + resto Gobierno Federal {gf[y]-epe:,.1f}")
    prueba("2027: pensiones contributivas IMSS 1,136,228 e ISSSTE 409,867 (CIEP)",
           abs(gb["GYR"] - 1136228) < 1 and abs(gb["GYN"] - 409867) < 1)
    r19 = B[0][B[0].INST == "19"]
    tr = r19[r19.UR.astype(str).str.startswith(("GYR", "GYN"))].MDP.sum()
    r19a = A[0][A[0].INST == "19"]
    tra = r19a[r19a.UR.astype(str).str.startswith(("GYR", "GYN"))].MDP.sum()
    print(f"  Ramo 19 transferido a IMSS e ISSSTE: {tra:,.1f} -> {tr:,.1f} (+{tr-tra:,.1f}); "
          f"Ramo 19 neto: {r19a.MDP.sum()-tra:,.1f} -> {r19.MDP.sum()-tr:,.1f}")
    prueba("Ramo 19 neto = cifra de CIEP (139,565.9 / 134,893.2)",
           abs(r19a.MDP.sum() - tra - 139565.9) < 0.2 and abs(r19.MDP.sum() - tr - 134893.2) < 0.2)
    tabla(r19a.groupby("K").MDP.sum(), r19.groupby("K").MDP.sum(), "ramo19_programas")
    pd.DataFrame([dict(concepto="Ramo 19 bruto", mdp_2026=r19a.MDP.sum(), mdp_2027=r19.MDP.sum()),
                  dict(concepto="transferido a IMSS e ISSSTE (UR GYR y GYN)", mdp_2026=tra, mdp_2027=tr),
                  dict(concepto="Ramo 19 neto de esas transferencias", mdp_2026=r19a.MDP.sum() - tra, mdp_2027=r19.MDP.sum() - tr)]
                 ).to_csv(SAL / "ramo19_transferencias.csv", index=False, float_format="%.1f")

    print("\n3. Entidades de control directo y empresas públicas por función")
    fa = A[3].groupby(["INST", "FN_K"]).MDP.sum(); fb = B[3].groupby(["INST", "FN_K"]).MDP.sum()
    print(tabla(fa, fb, "entidades_funcion").round(1).to_string())

    print("\n4. Función salud (2.3) y educación (2.5), GF + entidades, por subfunción e institución")
    FA, FB = pd.concat([A[2], A[3]]), pd.concat([B[2], B[3]])
    for fn, nom in (("2.3", "salud"), ("2.5", "educacion"), ("2.6", "proteccion_social")):
        s = tabla(FA[FA.FN_K == fn].groupby("SF_K").MDP.sum(), FB[FB.FN_K == fn].groupby("SF_K").MDP.sum(), f"{nom}_subfuncion")
        i = tabla(FA[FA.FN_K == fn].groupby(["SF_K", "INST"]).MDP.sum(), FB[FB.FN_K == fn].groupby(["SF_K", "INST"]).MDP.sum(), f"{nom}_subfuncion_institucion")
        tot_a, tot_b = s[f"mdp_{DE}"].sum(), s[f"mdp_{AL}"].sum()
        print(f"  {nom}: {tot_a:,.1f} -> {tot_b:,.1f}  {var(tot_a, tot_b):+.1f} % real")
    prueba("2026: función salud = 974,302.2 del documento 2026",
           abs(FA[FA.FN_K == "2.3"].MDP.sum() - 974302.2) < 0.2)

    print("\n5. Inversión: capítulos 6000 y 7000 por institución y partida")
    X7a = pd.concat([A[0], A[1]]); X7b = pd.concat([B[0], B[1]])
    c7 = tabla(X7a[X7a.CAP == "7"].groupby(["INST", "OG"]).MDP.sum(), X7b[X7b.CAP == "7"].groupby(["INST", "OG"]).MDP.sum(), "capitulo7000_institucion_partida")
    c6 = tabla(X7a[X7a.CAP == "6"].groupby("INST").MDP.sum(), X7b[X7b.CAP == "6"].groupby("INST").MDP.sum(), "capitulo6000_institucion")
    ap = c7.loc[("18", "73903")]
    print(f"  Ramo 18, partida 73903 (aportación de capital a Pemex): {ap[f'mdp_{DE}']:,.1f} -> {ap[f'mdp_{AL}']:,.1f}")
    prueba("partida 73903 2026 = 263,476.3 (documento 2026)", abs(ap[f"mdp_{DE}"] - 263476.3) < 0.1)
    for c, t in (("6000", c6), ("7000", c7)):
        print(f"  capítulo {c}: {t[f'mdp_{DE}'].sum():,.1f} -> {t[f'mdp_{AL}'].sum():,.1f}  {var(t[f'mdp_{DE}'].sum(), t[f'mdp_{AL}'].sum()):+.1f} % real")

    print("\n6. Empresas públicas: gasto que la reforma a la LFPRH saca del gasto corriente estructural")
    epe_ = []
    for y, ep in ((DE, A[1]), (AL, B[1])):
        x = ep[ep.INST.isin(["TYY", "TVV"])]
        corr = x[(x.TG_K == "1") & (x.CAP != "9")].MDP.sum()
        epe_.append(dict(ejercicio=y, total=x.MDP.sum(), corriente_sin_costo_financiero=corr,
                         costo_financiero=x[x.CAP == "9"].MDP.sum(), pensiones=x[x.TG_K == "4"].MDP.sum(),
                         inversion_tg2_tg3=x[x.TG_K.isin(["2", "3"])].MDP.sum()))
        pd.DataFrame(epe_).to_csv(SAL / "empresas_publicas_gasto.csv", index=False, float_format="%.3f")
        print(f"  {y}: total {x.MDP.sum():,.1f} | corriente sin costo financiero {corr:,.1f} | "
              f"costo financiero {x[x.CAP=='9'].MDP.sum():,.1f} | pensiones {x[x.TG_K=='4'].MDP.sum():,.1f} | "
              f"inversión (TG 2-3) {x[x.TG_K.isin(['2','3'])].MDP.sum():,.1f}")

    print("\n7. Ramo 33 por entidad federativa")
    tabla(A[0][A[0].INST == "33"].groupby("EF").MDP.sum(), B[0][B[0].INST == "33"].groupby("EF").MDP.sum(), "ramo33_entidad_federativa")

    print("\n8. Defensa por unidad responsable (Policía Militar, Guardia Nacional)")
    d7 = tabla(A[0][A[0].INST == "07"].groupby("UR").MDP.sum(), B[0][B[0].INST == "07"].groupby("UR").MDP.sum(), "defensa_ur")
    print(d7.sort_values("dif_nominal").round(1).head(4).to_string())
    print(d7.sort_values("dif_nominal").round(1).tail(5).to_string())

    print("\n9. Anexos transversales: auditoría de etiquetado (parser del decreto)")
    an = []
    for y in (DE, AL):
        df, tot, br = parse_anexos(y)
        an.append(df)
        g = df.groupby("anexo").mdp.sum()
        for a in g.index:
            t = tot.get(a)
            cob = g[a] / t * 100 if t else float("nan")
            print(f"  {y} anexo {a}: extraído {g[a]:,.1f} | total general {t if t else float('nan'):,.1f} | cobertura {cob:.2f} %")
        if len(br):
            print(f"  {y}: {len(br)} bloques de ramo con brecha, {(br.mdp_ramo-br.mdp_programas).sum():,.1f} mdp")
            br.to_csv(SAL / f"anexos_brechas_parser_{y}.csv", index=False, float_format="%.1f")
    an = pd.concat(an, ignore_index=True)
    an.to_csv(SAL / "anexos_programas.csv", index=False, float_format="%.3f")
    prueba("2027: Anexo 32 extraído = 175,045.5 (CIEP)", abs(an[(an.ejercicio == AL) & (an.anexo == 32)].mdp.sum() - 175045.5) < 0.1)

    presup = {DE: pd.concat([A[0], A[1]]).groupby("K").MDP.sum(), AL: pd.concat([B[0], B[1]]).groupby("K").MDP.sum()}
    aud = []
    for y in (DE, AL):
        for alcance, conj in (("anexos 13-19 y 31", (13, 14, 15, 16, 17, 18, 19, 31)), ("todos los anexos del ejercicio", ANEXOS)):
            d = an[(an.ejercicio == y) & an.anexo.isin(conj)]
            p = d.groupby("K").agg(anexos=("anexo", "nunique"), mdp=("mdp", "sum"))
            multi = p[p.anexos > 1]
            emp = p.index.intersection(presup[y].index)
            a13 = d[d.anexo == 13]
            pens = a13[a13.pp.isin(["S176", "S286", "S316"])].mdp.sum()
            aud.append(dict(ejercicio=y, alcance=alcance, programas=len(p), en_mas_de_un_anexo=len(multi),
                            pct_etiquetado_en_multiples=multi.mdp.sum() / p.mdp.sum() * 100,
                            suma_etiquetas=p.mdp.sum(),
                            programas_emparejados_analitico=len(emp),
                            presupuesto_completo_programas_etiquetados=presup[y].reindex(emp).sum(),
                            anexo13_pensiones_S176_S286_S316=pens,
                            anexo13_pct_pensiones=pens / a13.mdp.sum() * 100 if len(a13) else float("nan")))
    aud = pd.DataFrame(aud)
    aud.to_csv(SAL / "anexos_auditoria.csv", index=False, float_format="%.4f")
    print(aud.round(1).to_string())

    d27 = an[an.ejercicio == AL]
    nuevos_ = []
    for a in (32, 33):
        x = d27[d27.anexo == a]; otros = set(d27[d27.anexo != a].K)
        nuevos_.append(dict(anexo=a, programas=x.K.nunique(), ya_en_otro_anexo=len(set(x.K) & otros),
                            mdp_total=x.mdp.sum(), mdp_ya_en_otro_anexo=x[x.K.isin(otros)].mdp.sum()))
        print(f"  anexo {a}: {x.K.nunique()} programas; {len(set(x.K) & otros)} ya etiquetados en otro anexo "
              f"({x[x.K.isin(otros)].mdp.sum():,.1f} mdp de {x.mdp.sum():,.1f})")
    pd.DataFrame(nuevos_).to_csv(SAL / "anexos_nuevos_traslape.csv", index=False, float_format="%.1f")
    a16 = tabla(an[(an.ejercicio == DE) & (an.anexo == 16)].groupby("K").mdp.sum(),
                d27[d27.anexo == 16].groupby("K").mdp.sum(), "anexo16_programas")
    a16["presupuesto_2026_analitico"] = presup[DE].reindex(a16.index)
    a16["presupuesto_2027_analitico"] = presup[AL].reindex(a16.index)
    a16.round(3).to_csv(SAL / "anexo16_programas.csv", float_format="%.3f")
    print(a16.sort_values("dif_nominal").round(1).head(6).to_string())
    exced = a16[a16[f"mdp_{DE}"] > a16.presupuesto_2026_analitico + 0.5]
    print(f"  etiquetas 2026 del Anexo 16 mayores que el presupuesto del programa: {len(exced)}")
    if len(exced):
        print(exced[[f"mdp_{DE}", "presupuesto_2026_analitico"]].round(1).to_string())

    print("\n10. Lo que ya estaba en carpeta: CGPE pp. 24 y 32, Pre-Criterios p. 32")
    extraer_cgpe_y_precriterios()

    print("\n" + ("SIN FALLAS" if not FALLAS else f"FALLAS: {FALLAS}"))
    return 1 if FALLAS else 0


if __name__ == "__main__":
    sys.exit(main())
