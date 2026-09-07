"""fiscus.py — capa de datos del documento propio ITED, Paquete Económico 2025.

Regla del pacto §6: ninguna cifra se teclea en el cuerpo del texto. Todo cuadro y
toda figura salen de un .csv de datos/, y todo .csv tiene su fila en
datos/_fuentes.csv con documento, cuadro, página y tier.

Este módulo no escribe prosa. Carga los analíticos, aplica los perímetros
declarados en el pacto y emite los .csv.

Uso:
    from fiscus import an, mdp, real, emitir
"""
from __future__ import annotations
import csv, os, hashlib
import pandas as pd

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "datos")
CACHE = os.environ.get("FISCUS_CACHE", "/tmp/claude-1000/fiscus_cache")
os.makedirs(CACHE, exist_ok=True)
os.makedirs(DATOS, exist_ok=True)

# Los cuatro cortes del analítico. La hoja de datos es 'Hoja1'; la primera hoja
# es una carátula-resumen de 45 filas por ramo (trampa documentada en 2024).
CORTES = {
    "gf_pp":  "gf-ramo-programa-ur-objeto",
    "gf_f":   "gf-ramo-funcion-ur-objeto",
    "ent_pp": "entidades-ramo-programa-ur-objeto",
    "ent_f":  "entidades-ramo-funcion-ur-objeto",
}


def an(anio: int, corte: str = "gf_pp") -> pd.DataFrame:
    """Analítico del PEF aprobado. Cachea en pickle porque cada xlsx tarda ~40 s."""
    pk = os.path.join(CACHE, f"{anio}_{corte}.pkl")
    if os.path.exists(pk):
        return pd.read_pickle(pk)
    ruta = os.path.join(RAIZ, str(anio), f"{anio}_pef_analitico-{CORTES[corte]}.xlsx")
    d = pd.read_excel(ruta, sheet_name="Hoja1")
    d.columns = [str(c).strip() for c in d.columns]
    if "IMPORTE PEF" in d.columns:
        d["IMPORTE"] = pd.to_numeric(d["IMPORTE PEF"], errors="coerce").fillna(0.0)
    # Código de programa: la modalidad va en columna aparte (MOD), no en PP.
    if "MOD" in d.columns and "PP" in d.columns:
        d["CLAVE_PP"] = d["MOD"].astype(str).str[0] + d["PP"].astype(str).str[:3]
    # OJO: en los cortes por funcion (gf_f, ent_f) las columnas F y FN vienen como
    # texto con nombre ("2 Desarrollo Social", "5 Educacion"); en los cortes por
    # programa vienen como numero. Se normaliza a codigo numerico y se conserva el
    # nombre aparte. Coercionar a numero sin mirar destruye la etiqueta.
    for c in ("F", "FN", "SF", "TG", "AI", "FF"):
        if c not in d.columns:
            continue
        col = d[c]
        # pandas 3 devuelve dtype 'str', no 'object': preguntar por numerico.
        if not pd.api.types.is_numeric_dtype(col):
            txt = col.astype(str)
            d[c + "_NOM"] = txt.str.replace(r"^\s*\d+\s*", "", regex=True).str.strip()
            d[c] = pd.to_numeric(txt.str.extract(r"^\s*(\d+)")[0], errors="coerce")
        else:
            d[c] = pd.to_numeric(col, errors="coerce")
    d.to_pickle(pk)
    return d


def mdp(x) -> float:
    """Pesos -> millones de pesos, un decimal."""
    return round(float(x) / 1e6, 1)


def real(v_t: float, v_prev: float, deflactor: float) -> float:
    """Variación real en por ciento. v_prev en pesos corrientes de t-1."""
    base = v_prev * deflactor
    if base == 0:
        return float("nan")
    return round(100.0 * (v_t / base - 1.0), 1)


def dif_real(v_t: float, v_prev: float, deflactor: float) -> float:
    """Diferencia REAL en mdp, en pesos del año t. Se reporta siempre etiquetada
    como real, nunca como si fuera una diferencia de niveles (regla propia §7.9)."""
    return round(v_t - v_prev * deflactor, 1)


def dif_nominal(v_t: float, v_prev: float) -> float:
    return round(v_t - v_prev, 1)


# ---------------------------------------------------------------- registro ---

CAMPOS_FUENTE = ["archivo", "cuadro", "documento", "ubicacion", "tier", "nota"]


def emitir(nombre: str, filas, encabezado, fuente: dict) -> str:
    """Escribe datos/<nombre>.csv y registra su fila en datos/_fuentes.csv."""
    ruta = os.path.join(DATOS, nombre)
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(encabezado)
        for r in filas:
            w.writerow(r)
    _registrar(nombre, fuente)
    return ruta


def _registrar(archivo: str, fuente: dict) -> None:
    reg = os.path.join(DATOS, "_fuentes.csv")
    filas, visto = [], False
    if os.path.exists(reg):
        with open(reg, newline="", encoding="utf-8") as f:
            r = list(csv.DictReader(f))
        for row in r:
            if row["archivo"] == archivo:
                row.update({k: fuente.get(k, row.get(k, "")) for k in CAMPOS_FUENTE if k != "archivo"})
                visto = True
            filas.append(row)
    if not visto:
        nueva = {"archivo": archivo}
        nueva.update({k: fuente.get(k, "") for k in CAMPOS_FUENTE if k != "archivo"})
        filas.append(nueva)
    with open(reg, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS_FUENTE)
        w.writeheader()
        for row in filas:
            w.writerow({k: row.get(k, "") for k in CAMPOS_FUENTE})
