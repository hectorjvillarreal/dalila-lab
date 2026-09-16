"""Carga de analíticos y parámetros del ejercicio. Sirve a cualquier año.

Generaliza `documento_2026/fiscus26.py`, que tenía 2026 cableado. Aquí el ejercicio
es un argumento y los parámetros macro viven en `parametros_ejercicio.csv`, con su
fuente declarada renglón por renglón.

TRAMPAS QUE ESTE ARCHIVO YA RESUELVE, y que costaron corridas enteras:
  · Los datos están en la hoja «Hoja1», no en la primera, que es una carátula por ramo.
  · El encabezado no está en el renglón 0: se busca el primero con ocho columnas llenas.
  · El código de programa es MOD[0] + PP[:3]: la modalidad va en columna aparte.
  · En los cortes por función, F/FN/SF vienen como texto con nombre («2 Desarrollo
    Social»); en los cortes por programa, como número. `clave()` normaliza las dos.
  · El nombre del archivo cambió: hasta 2022 los cortes del Gobierno Federal no llevan
    el segmento «gf-».
"""
from __future__ import annotations
import csv
from pathlib import Path
import pandas as pd

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
CACHE = AQUI / "_cache"
CACHE.mkdir(exist_ok=True)

CORTES = ("gf-ramo-programa-ur-objeto", "gf-ramo-funcion-ur-objeto",
          "entidades-ramo-programa-ur-objeto", "entidades-ramo-funcion-ur-objeto")


def parametros(anio: int | None = None) -> dict | pd.DataFrame:
    """PIB, deflactor y añada, con su fuente. Sin esto no hay variación real."""
    df = pd.read_csv(AQUI / "parametros_ejercicio.csv")
    if anio is None:
        return df
    f = df[df.ejercicio == anio]
    if f.empty:
        raise KeyError(f"no hay parámetros para {anio}: añádelos a parametros_ejercicio.csv "
                       f"leyéndolos del CGPE {anio}, no de memoria")
    return f.iloc[0].to_dict()


def pib(anio: int, de: int | None = None) -> float:
    """PIB nominal en mdp del año `anio`, según la añada del CGPE `de` (por defecto, el suyo)."""
    p = parametros(de or anio)
    col = {0: "pib_t_mmp", -1: "pib_t_1_mmp"}[anio - (de or anio)]
    return float(p[col]) * 1000


def deflactor(anio: int) -> float:
    return float(parametros(anio)["deflactor"])


def _ruta(anio: int, corte: str, etapa: str) -> Path:
    pre = "ppef" if etapa == "proyecto" else "pef"
    d = RAIZ / str(anio)
    cand = [d / f"{anio}_{pre}_analitico-{corte}.xlsx"]
    if corte.startswith("gf-"):           # hasta 2022 el corte del GF no lleva «gf-»
        cand.append(d / f"{anio}_{pre}_analitico-{corte[3:]}.xlsx")
    for c in cand:
        if c.exists():
            return c
    raise FileNotFoundError(f"falta el analítico {etapa} {anio} {corte}. Probé: "
                            + ", ".join(str(c.name) for c in cand))


def analitico(anio: int, corte: str, etapa: str = "proyecto") -> pd.DataFrame:
    """corte ∈ CORTES · etapa ∈ {proyecto, pef}. Devuelve el marco con la columna MDP."""
    ck = CACHE / f"{'ppef' if etapa == 'proyecto' else 'pef'}{anio}_{corte}.pkl"
    if ck.exists():
        return pd.read_pickle(ck)
    f = _ruta(anio, corte, etapa)
    crudo = pd.read_excel(f, sheet_name="Hoja1", header=None)
    fila = next(i for i in range(len(crudo)) if crudo.iloc[i].notna().sum() >= 8)
    df = pd.read_excel(f, sheet_name="Hoja1", header=fila)
    df.columns = [str(c).strip() for c in df.columns]
    ci = [c for c in df.columns if "IMPORTE" in c.upper()][0]
    df["MDP"] = pd.to_numeric(df[ci], errors="coerce") / 1e6
    df = df.dropna(subset=["MDP"])
    df.to_pickle(ck)
    return df


def clave(s: pd.Series) -> pd.Series:
    """Primer token: la columna puede venir '5 Educación' o '5'."""
    return s.astype(str).str.strip().str.split().str[0]


def cod_pp(df: pd.DataFrame) -> pd.Series:
    """Código de programa = modalidad + tres dígitos. La modalidad va en su columna."""
    return (df["MOD"].astype(str).str.strip().str[0]
            + df["PP"].astype(str).str.strip().str.zfill(3).str[:3])


def num_pp(df: pd.DataFrame) -> pd.Series:
    """SOLO el número, sin modalidad. La Pensión Mujeres Bienestar es U316 en 2025 y
    S316 en 2026: cambió el prefijo, no el número. El emparejamiento estable usa
    número + ramo, y la modalidad se verifica contra el diff."""
    return df["PP"].astype(str).str.strip().str.zfill(3).str[:3]


def real(v_ant: float, v_act: float, defl: float) -> tuple[float, float, float]:
    """(diferencia nominal, diferencia real, variación real %). El deflactor es
    argumento obligatorio: no hay valor por omisión que se pueda usar sin pensarlo."""
    base = v_ant * defl
    return v_act - v_ant, v_act - base, (v_act / base - 1) * 100 if base else float("nan")
