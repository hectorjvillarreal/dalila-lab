#!/usr/bin/env python3
"""Series históricas de la casa, ex ante y aprobado, SEPARADAS.

Precarga §3.7 de INSTRUCCIONES_preparacion_2027.md. Generaliza
`documento_2025/construir_razones.py`, que tenía los años cableados y una sola etapa.

    python series_historicas.py

REGLA QUE MANDA SOBRE TODAS: **ninguna línea híbrida.** Ex ante con ex ante, aprobado
con aprobado, en columnas distintas de archivos distintos. Una razón que mezcle las dos
etapas mide el cambio de objeto y no el cambio del objeto.

LO QUE ESTA CORRIDA DESCONGELA: la serie ex ante de pensiones IMSS / cuotas IMSS estaba
detenida en 2021 porque se creía que hacía falta la exposición de motivos del PPEF, que
no se publica desde 2022. **No hacía falta**: el numerador sale del analítico del
PROYECTO ---tipo de gasto 4 del IMSS--- y esos analíticos existen para 2020-2026 en
`Analiticos_Historico/{t}/Proyecto/`. La serie pasa de dos puntos a siete.
"""
from __future__ import annotations
import csv, re, subprocess, sys
from pathlib import Path
import pandas as pd

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
sys.path.insert(0, str(AQUI))
from fiscus import analitico, clave, cod_pp, num_pp

SALIDA = RAIZ / "_aprendizaje"
NOCONTRIB = ("176", "286", "316")   # adultas mayores, discapacidad, mujeres. POR NÚMERO:
                                     # la clave cambia de prefijo (U316 -> S316) y el nombre
                                     # es «Personas ADULTAS Mayores», en femenino.


# ------------------------------------------------------------------ art. 1o.
def art1o(anio: int, etapa: str) -> dict:
    """Renglones de primer nivel del artículo 1o., leídos del PDF con capa de texto.

    ex ante -> iniciativa de Ley de Ingresos; aprobado -> Ley de Ingresos publicada.
    El PDF de la ILIF CONTIENE su exposición de motivos: el artículo 1o. va al final."""
    arch = (RAIZ / str(anio) /
            (f"{anio}_ilif_iniciativa.pdf" if etapa == "proyecto" else f"{anio}_lif_aprobada.pdf"))
    if not arch.exists():
        return {}
    t = subprocess.run(["pdftotext", "-layout", str(arch), "-"],
                       capture_output=True, text=True).stdout
    out = {}
    for m in re.finditer(r"^\s{0,6}(\d)\.?\s+([A-ZÍÓÁÉÚ][^\n]{6,90}?)[:.]?\s{2,}([\d,]+\.\d)\s*$",
                         t, re.M):
        num, nom, val = m.group(1), " ".join(m.group(2).split()), float(m.group(3).replace(",", ""))
        if num == "1" and nom.startswith("Impuestos"):
            out.setdefault("impuestos", val)
        elif num == "2" and nom.startswith("Cuotas"):
            out.setdefault("cuotas", val)
    return out


# -------------------------------------------------------------- analíticos
def agregados(anio: int, etapa: str) -> dict:
    """Los siete numeradores y denominadores que salen de los analíticos."""
    try:
        gf_pp = analitico(anio, "gf-ramo-programa-ur-objeto", etapa)
        en_pp = analitico(anio, "entidades-ramo-programa-ur-objeto", etapa)
        gf_f = analitico(anio, "gf-ramo-funcion-ur-objeto", etapa)
        en_f = analitico(anio, "entidades-ramo-funcion-ur-objeto", etapa)
    except FileNotFoundError:
        return {}
    v = {}
    # Pensiones de la clasificación económica: tipo de gasto 4 de entidades más el del
    # Gobierno Federal SIN la partida 45203. El Anexo 3 del decreto adjudica el perímetro.
    directo = gf_pp[(gf_pp.TG == 4) & (~gf_pp.PE.astype(str).str.startswith("45203"))]["MDP"].sum()
    v["pens_clasif"] = directo + en_pp[en_pp.TG == 4]["MDP"].sum()
    ent = lambda d, p: d[d.ENTIDAD.astype(str).str.startswith(p)]
    v["imss_pens"] = ent(en_pp, "GYR").loc[lambda s: s.TG == 4, "MDP"].sum()
    v["isss_pens"] = ent(en_pp, "GYN").loc[lambda s: s.TG == 4, "MDP"].sum()
    sal = lambda d, p: ent(d, p)[(clave(ent(d, p).F) == "2") & (clave(ent(d, p).FN) == "3")]["MDP"].sum()
    v["imss_salud"], v["isss_salud"] = sal(en_f, "GYR"), sal(en_f, "GYN")
    v["educacion"] = gf_f[(clave(gf_f.F) == "2") & (clave(gf_f.FN) == "5")]["MDP"].sum()
    r20 = gf_pp[gf_pp.RAMO.astype(str).str.zfill(2).str.startswith("20")]
    v["no_contrib"] = r20[num_pp(r20).isin(NOCONTRIB)]["MDP"].sum()
    return v


# ------------------------------------- escalares que NO salen de los analíticos
def documentales() -> pd.DataFrame:
    return pd.read_csv(AQUI / "agregados_documentales.csv")


RAZONES = [
    ("2",  "Impuestos / gastos obligatorios con pensiones",
     "art. 1o. numeral 1", "decreto, Anexo 3",
     lambda a, d: safe(a.get("impuestos"), d.get("oblig_con_pensiones"))),
    ("2",  "Impuestos + cuotas de seguridad social / gastos obligatorios con pensiones",
     "art. 1o. numerales 1 y 2", "decreto, Anexo 3",
     lambda a, d: safe(sumar(a.get("impuestos"), a.get("cuotas")), d.get("oblig_con_pensiones"))),
    ("4",  "Pensiones y jubilaciones + costo financiero / impuestos",
     "clasificación económica + CGPE", "art. 1o. numeral 1",
     lambda a, d: safe(sumar(a.get("pens_clasif"), d.get("costo_financiero")), a.get("impuestos"))),
    ("5",  "Pensiones IMSS / cuotas de seguridad social",
     "tipo de gasto 4 del IMSS", "art. 1o. numeral 2",
     lambda a, d: safe(a.get("imss_pens"), a.get("cuotas"))),
    ("6",  "Gasto en salud del IMSS / cuotas de seguridad social",
     "función 2.3 Salud del IMSS", "art. 1o. numeral 2",
     lambda a, d: safe(a.get("imss_salud"), a.get("cuotas"))),
    ("6",  "Pensiones IMSS+ISSSTE / salud IMSS+ISSSTE",
     "tipo de gasto 4 de IMSS e ISSSTE", "función 2.3 Salud de IMSS e ISSSTE",
     lambda a, d: safe(sumar(a.get("imss_pens"), a.get("isss_pens")),
                       sumar(a.get("imss_salud"), a.get("isss_salud")))),
    ("7",  "Función Educación / pensiones y jubilaciones",
     "función 2.5 Educación, GF bruto", "pensiones y jubilaciones, clasificación económica",
     lambda a, d: safe(a.get("educacion"), a.get("pens_clasif"))),
    ("7",  "Función Educación / pensiones totales (con no contributivas)",
     "función 2.5 Educación, GF bruto",
     "pensiones y jubilaciones + adultas mayores + discapacidad + mujeres",
     lambda a, d: safe(a.get("educacion"), sumar(a.get("pens_clasif"), a.get("no_contrib")))),
    ("12", "Costo financiero / impuestos",
     "CGPE, costo financiero del sector público", "art. 1o. numeral 1",
     lambda a, d: safe(d.get("costo_financiero"), a.get("impuestos"))),
    ("12", "SHRFSP / impuestos, en años de recaudación",
     "CGPE, SHRFSP", "art. 1o. numeral 1",
     lambda a, d: safe(d.get("shrfsp"), a.get("impuestos"), 2)),
]


def sumar(*xs):
    return None if any(x is None or pd.isna(x) for x in xs) else sum(xs)


def safe(a, b, n=3):
    if a is None or b is None or pd.isna(a) or pd.isna(b) or not b:
        return ""
    return round(a / b, n)


def correr(anios=range(2018, 2027)) -> None:
    doc = documentales()
    for etapa, nombre in (("proyecto", "ex_ante"), ("pef", "aprobado")):
        val, base = {}, {}
        for anio in anios:
            a = agregados(anio, etapa)
            a.update(art1o(anio, etapa))
            d = {r.concepto: r.valor_mdp for r in
                 doc[(doc.ejercicio == anio) & (doc.etapa == nombre)].itertuples()}
            base[anio] = (a, d)
        filas = []
        for cap, razon, num, den, f in RAZONES:
            fila = [cap, razon, num, den]
            for anio in anios:
                a, d = base[anio]
                try:
                    fila.append(f(a, d))
                except Exception:
                    fila.append("")
            filas.append(fila)
        cab = ["capitulo", "razon", "numerador", "denominador"] + [str(x) for x in anios]
        sal = SALIDA / f"series_historicas_{nombre}.csv"
        with sal.open("w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh); w.writerow(cab); w.writerows(filas)
        print(f"\n=== serie {nombre} ===")
        print(pd.DataFrame(filas, columns=cab).drop(columns=["numerador", "denominador"])
                .to_string(index=False))
        # insumos, para que cada razón sea auditable renglón por renglón
        ins = []
        for anio in anios:
            a, d = base[anio]
            for k, v in {**a, **d}.items():
                ins.append([nombre, anio, k, round(v, 1) if isinstance(v, float) else v])
        with (SALIDA / f"series_insumos_{nombre}.csv").open("w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh); w.writerow(["etapa", "ejercicio", "concepto", "mdp"]); w.writerows(ins)
        print(f"escrito {sal.name} y series_insumos_{nombre}.csv")


if __name__ == "__main__":
    correr()
