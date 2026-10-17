"""Rutas, parámetros y registro de cifras compartidos por todos los módulos."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

PROJECT = Path(__file__).resolve().parents[1]
CFG = yaml.safe_load((PROJECT / "config.yaml").read_text(encoding="utf8"))
DALILA = (PROJECT / CFG["dalila_root"]).resolve()
DERIVED = PROJECT / "data" / "derived"
TABLES = PROJECT / "outputs" / "tables"
FIGURES = PROJECT / "outputs" / "figures"
NUMBERS_JSON = DERIVED / "numbers_computed.json"

P = CFG["parametros"]
H = CFG["horizonte"]
YEARS = list(range(H["anio_inicial"], H["anio_final"] + 1))


def inp(key: str) -> Path:
    return DALILA / CFG["inputs"][key]


# --- Precios: todo en pesos de 2026 ---------------------------------------
# La UMA se indexa a la inflación: su valor real de 2026 es la UMA de dic. 2025
# llevada a pesos de 2026 con la inflación de Sup_Fin.
UMA = P["uma_dic2025"] * (1 + P["inflacion_2026"])
DIAS = P["dias"]
F_P = P["cf_patron"] * UMA * DIAS          # parte privada de la cuota fija, anual
F_G = P["cf_gf"] * UMA * DIAS              # parte federal de la cuota fija, anual
P_STAR = F_P + F_G
E_RATE = P["excedente"] * UMA * DIAS       # pesos por cada UMA de ingreso sobre 3


def excedente(m):
    return E_RATE * np.maximum(0.0, np.asarray(m, dtype=float) - P["umbral_excedente_uma"])


def subsidio(m, m0, m1):
    m = np.asarray(m, dtype=float)
    return np.clip((m1 - m) / (m1 - m0), 0.0, 1.0)


def save(df: pd.DataFrame, name: str, csv: bool = False) -> None:
    DERIVED.mkdir(parents=True, exist_ok=True)
    df.to_parquet(DERIVED / f"{name}.parquet", index=False)
    if csv:
        TABLES.mkdir(parents=True, exist_ok=True)
        df.to_csv(TABLES / f"{name}.csv", index=False)


def load(name: str) -> pd.DataFrame:
    return pd.read_parquet(DERIVED / f"{name}.parquet")


def table(df: pd.DataFrame, name: str) -> None:
    TABLES.mkdir(parents=True, exist_ok=True)
    df.to_csv(TABLES / f"{name}.csv", index=False)


def record(key: str, value, source: str) -> None:
    """Registra una cifra calculada para NUMBERS.md (clave, valor, fuente)."""
    reg = json.loads(NUMBERS_JSON.read_text()) if NUMBERS_JSON.exists() else {}
    if isinstance(value, (np.floating, np.integer)):
        value = value.item()
    reg[key] = {"valor": value, "fuente": source}
    DERIVED.mkdir(parents=True, exist_ok=True)
    NUMBERS_JSON.write_text(json.dumps(reg, ensure_ascii=False, indent=1))


def wquantile(x, w, q):
    """Cuantil ponderado (q en [0, 1])."""
    x = np.asarray(x, dtype=float)
    w = np.asarray(w, dtype=float)
    o = np.argsort(x)
    cw = np.cumsum(w[o])
    return float(np.interp(q * cw[-1], cw, x[o]))
