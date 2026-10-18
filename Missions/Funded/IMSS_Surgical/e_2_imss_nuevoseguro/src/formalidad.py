"""Instrucción v1.2, sección 4: serie histórica 2005-2025 de puestos de trabajo afiliados al IMSS entre población ocupada
de la ENOE, con fuentes primarias, y empalme con la formalidad implícita del libro (34.0 % en 2025)."""

from __future__ import annotations

import hashlib
import io
import json
import zipfile

import openpyxl
import pandas as pd

from comun import PROJECT, record, table
from insumos import cargar

RAW = PROJECT / "data" / "raw"
MEMORIA = RAW / "imss_memoria" / "01-Asegurados.xlsx"     # Memoria Estadística 2025, capítulo I
ENOE = RAW / "enoe"
ANIOS = list(range(2005, 2026))
DESCARGAS = json.loads((RAW / "descargas.json").read_text()) if (RAW / "descargas.json").exists() else {}


def sha(p) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def puestos_imss() -> pd.Series:
    """Cuadro I.2, fila «Nacional»: puestos de trabajo afiliados al IMSS al 31 de diciembre de cada año."""
    ws = openpyxl.load_workbook(MEMORIA, read_only=True, data_only=True)["I.2"]
    rows = [[c for c in r] for r in ws.iter_rows(values_only=True)]
    hdr = next(r for r in rows if r and r[0] == "OOAD")
    anios = [int(str(v)) for v in hdr[1:] if v is not None]
    k = next(i for i, r in enumerate(rows) if r and r[0] == "Nacional")
    vals = next(r for r in rows[k:] if r and isinstance(r[1], (int, float)) or (r and str(r[1]).isdigit()))
    vals = [int(str(v)) for v in vals[1:1 + len(anios)]]
    return pd.Series(vals, index=anios, name="puestos_IMSS_dic")


def ocupados_enoe(anio: int) -> tuple[float, str]:
    """Población ocupada de 15 años o más, cuarto trimestre: SDEMT, r_def = 0, c_res ∈ {1, 3}, clase2 = 1, 15 ≤ eda ≤ 97,
    ponderada con fac (hasta 2019) o fac_tri (ENOE nueva, desde 2020)."""
    z = next(ENOE.glob(f"*{anio}*trim4*.zip"))
    with zipfile.ZipFile(z) as zf:
        nombre = next(n for n in zf.namelist() if "sdem" in n.lower() and n.lower().endswith(".csv"))
        with zf.open(nombre) as f:
            d = pd.read_csv(io.TextIOWrapper(f, encoding="latin-1"), usecols=lambda c: c.lower() in
                            {"r_def", "c_res", "clase2", "eda", "fac", "fac_tri"}, low_memory=False)
    d.columns = [c.lower() for c in d.columns]
    for c in d.columns:
        d[c] = pd.to_numeric(d[c], errors="coerce")
    w = "fac_tri" if "fac_tri" in d.columns else "fac"
    m = (d.r_def == 0) & d.c_res.isin([1, 3]) & (d.clase2 == 1) & d.eda.between(15, 97)
    return float(d.loc[m, w].sum()), f"{z.name}:{nombre} (peso {w})"


def serie() -> pd.DataFrame:
    p = puestos_imss()
    rows = []
    for a in ANIOS:
        try:
            oc, fuente = ocupados_enoe(a)
        except StopIteration:
            oc, fuente = float("nan"), "no descargado"
        rows.append({"anio": a, "puestos_IMSS_dic": p.get(a), "ocupados_ENOE_T4": oc,
                     "razon_pct": p.get(a) / oc * 100 if oc == oc else float("nan"), "fuente_ENOE": fuente})
    return pd.DataFrame(rows)


def main():
    s = serie()
    table(s, "formalidad_historica")
    ins = cargar()
    fl = float(ins.formalidad[2025]) * 100
    x = s.set_index("anio")
    falt = int(x.ocupados_ENOE_T4.isna().sum())
    record("form_hist_anios_faltantes", falt, "Años 2005-2025 sin dato de la ENOE")
    if not falt:
        r05, r25 = x.razon_pct[2005], x.razon_pct[2025]
        record("form_hist_2005", round(r05, 1), "Puestos de trabajo IMSS (31-dic) / ocupados ENOE T4, 15+ (%)")
        record("form_hist_2025", round(r25, 1), "Idem, 2025")
        record("form_hist_cambio_pts", round(r25 - r05, 1), "Cambio 2005-2025, puntos porcentuales")
        record("form_hist_max", round(x.razon_pct.max(), 1), "Máximo de la serie 2005-2025 (%)")
        record("form_hist_max_anio", int(x.razon_pct.idxmax()), "Año del máximo")
        record("form_libro_2025", round(fl, 1), "Formalidad implícita del libro: cotizantes / ocupados (CONAPO × ENIGH), 2025 (%)")
        record("form_hist_menos_libro_2025", round(r25 - fl, 1), "Serie histórica 2025 − formalidad implícita del libro (puntos)")
        record("form_proy_cambio_pts", round((float(ins.formalidad[2054]) - float(ins.formalidad[2025])) * 100, 1), "Cambio 2025-2054 en la proyección base (puntos)")
        for a in (2005, 2010, 2015, 2020, 2025):
            record(f"ENOE_ocupados_T4_{a}", round(x.ocupados_ENOE_T4[a]), "ENOE T4, ocupados de 15+ (INEGI, microdatos)")
            record(f"IMSS_puestos_dic_{a}", int(x.puestos_IMSS_dic[a]), "IMSS, Memoria Estadística 2025, Cuadro I.2, Nacional")
    record("fuente_memoria_sha256", sha(MEMORIA)[:16], f"01-Asegurados.xlsx, descargado {DESCARGAS.get('memoria', 's/f')}")
    record("fuente_enoe_descarga", DESCARGAS.get("enoe", "s/f"), "Microdatos ENOE T4 2005-2025, inegi.org.mx/contenidos/programas/enoe/15ymas/microdatos/")
    return {"8.5 serie de formalización: años sin fuente primaria": falt}


if __name__ == "__main__":
    print(main())
