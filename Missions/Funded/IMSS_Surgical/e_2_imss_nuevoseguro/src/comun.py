"""Rutas, parámetros y registro de cifras del experimento 2; enlace con los módulos de la v1.2 del experimento 1."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

PROJECT = Path(__file__).resolve().parents[1]
CFG = yaml.safe_load((PROJECT / "config.yaml").read_text(encoding="utf8"))
DALILA = (PROJECT / CFG["dalila_root"]).resolve()
EXP1 = DALILA / CFG["exp1"]
DERIVED = PROJECT / "data" / "derived"
TABLAS = PROJECT / "tablas"
FIGURAS = PROJECT / "figuras"
NUMBERS_JSON = DERIVED / "numbers_computed.json"

P = CFG["parametros"]
H = CFG["horizonte"]
YEARS = list(range(H["anio_inicial"], H["anio_final"] + 1))
REP = H["anios_reporte"]
MDP = 1e6

# Los módulos de la v1.2 se importan tal cual (mismo nombre `common` que el experimento 1; este proyecto usa `comun`).
sys.path.insert(1, str(EXP1 / "src"))


def informe_pdf() -> Path:
    return DALILA / CFG["informe_pdf"]


def interpola(anclas: list[int], valores: list[float], anios) -> pd.Series:
    """Interpolación lineal entre años ancla (Cuadros V.13 y V.24); los años ancla se preservan."""
    return pd.Series(np.interp(list(anios), anclas, valores), index=list(anios), dtype=float)


def descuento(anios, base: int | None = None) -> pd.Series:
    base = H["vp_base"] if base is None else base
    a = np.asarray(list(anios))
    return pd.Series((1 + P["r"]) ** -(a - base), index=a)


def table(df: pd.DataFrame, name: str) -> None:
    TABLAS.mkdir(parents=True, exist_ok=True)
    df.to_csv(TABLAS / f"{name}.csv", index=False)


def record(key: str, value, source: str) -> None:
    """Registra una cifra calculada para NUMBERS.md (clave, valor, fuente)."""
    reg = json.loads(NUMBERS_JSON.read_text()) if NUMBERS_JSON.exists() else {}
    if isinstance(value, (np.floating, np.integer)):
        value = value.item()
    reg[key] = {"valor": value, "fuente": source}
    DERIVED.mkdir(parents=True, exist_ok=True)
    NUMBERS_JSON.write_text(json.dumps(reg, ensure_ascii=False, indent=1))
