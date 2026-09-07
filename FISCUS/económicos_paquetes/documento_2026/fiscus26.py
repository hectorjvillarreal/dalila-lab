"""Utilidades de la corrida 2026. Carga de analíticos y del CSV del proyecto."""
from pathlib import Path
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
CACHE = Path(__file__).resolve().parent / "_cache"
CACHE.mkdir(exist_ok=True)

# CGPE 2026, Anexo III.1 (p. 86). Deflactor del PIB 2026.
DEFLACTOR = 1.048
PIB = {2024: 33_980.5, 2025: 36_125.5, 2026: 38_715.9}      # mmp, CGPE 2026 III.1
PIB_APROBADO = {2025: 36_166.4}                              # CGPE 2025, para la añada aprobada


def analitico(anio: int, corte: str, etapa: str = "proyecto") -> pd.DataFrame:
    """corte ∈ {gf-ramo-programa-ur-objeto, gf-ramo-funcion-ur-objeto, entidades-*}
    etapa ∈ {proyecto, pef}"""
    pre = "ppef" if etapa == "proyecto" else "pef"
    ck = CACHE / f"{pre}{anio}_{corte}.pkl"
    if ck.exists():
        return pd.read_pickle(ck)
    f = RAIZ / str(anio) / f"{anio}_{pre}_analitico-{corte}.xlsx"
    crudo = pd.read_excel(f, sheet_name="Hoja1", header=None)
    fila = next(i for i in range(len(crudo)) if crudo.iloc[i].notna().sum() >= 8)
    df = pd.read_excel(f, sheet_name="Hoja1", header=fila)
    df.columns = [str(c).strip() for c in df.columns]
    ci = [c for c in df.columns if "IMPORTE" in c.upper()][0]
    df["MDP"] = pd.to_numeric(df[ci], errors="coerce") / 1e6
    df = df.dropna(subset=["MDP"])
    df.to_pickle(ck)
    return df


def csv_proyecto(anio: int = 2026) -> pd.DataFrame:
    """El CSV del repositorio de datos abiertos: proyecto completo, GF y entidades."""
    ck = CACHE / f"csv{anio}.pkl"
    if ck.exists():
        return pd.read_pickle(ck)
    df = pd.read_csv(RAIZ / str(anio) / f"{anio}_ppef_analitico-claves.csv", low_memory=False)
    df["MDP"] = df["monto_proyecto"] / 1e6
    df.to_pickle(ck)
    return df


def clave(s: pd.Series) -> pd.Series:
    """Primer token: la columna puede venir '5 Educación' o '5'."""
    return s.astype(str).str.strip().str.split().str[0]


def cod_pp(df: pd.DataFrame) -> pd.Series:
    """Código de programa = modalidad + tres dígitos. La modalidad va en su columna."""
    return (df["MOD"].astype(str).str.strip().str[0]
            + df["PP"].astype(str).str.strip().str.zfill(3).str[:3])


def real(v_ant: float, v_act: float, defl: float = DEFLACTOR) -> tuple[float, float, float]:
    """Devuelve (diferencia nominal, diferencia real, variación real %)."""
    base = v_ant * defl
    return v_act - v_ant, v_act - base, (v_act / base - 1) * 100 if base else float("nan")
