"""Sección 4 de la v1.1: tablas de cambios del experimento 1 (v1.2) por el denominador común y la fuente única de
ingresos del SEM, verificación 7.4 (los montos en mdp no cambian) y contraste del Cuadro V.13 con el libro."""

from __future__ import annotations

import io
import json
import re
import subprocess

import numpy as np
import pandas as pd

from comun import DALILA, EXP1, PROJECT, REP, record, table
from insumos import cargar

ANTES = PROJECT / "data" / "v10" / "exp1_numbers_computed_v12.json"   # registro de la v1.2 al commit 2253249
COMMIT_ANTES = "2253249"
ES_RAZON = re.compile(r"pts|sem|pct")


def cambios() -> pd.DataFrame:
    a = json.loads(ANTES.read_text())
    b = json.loads((EXP1 / "data" / "derived" / "numbers_computed.json").read_text())
    rows = []
    # solo cifras que ya existían en la v1.2: las claves que el experimento 1 agregó después (v1.3: X1_*, chk13_*) no son cambios
    for k in sorted(a):
        va, vb = a.get(k, {}).get("valor"), b.get(k, {}).get("valor")
        if va != vb:
            dif = vb - va if isinstance(va, (int, float)) and isinstance(vb, (int, float)) else np.nan
            rows.append({"clave": k, "antes": va, "despues": vb, "diferencia": dif,
                         "tipo": "puntos del salario" if "pts" in k else ("% ingresos del SEM" if re.search("sem|pct", k) else "otro"),
                         "fuente_despues": b.get(k, {}).get("fuente", "")})
    return pd.DataFrame(rows)


def montos_sin_cambio() -> float:
    """7.4: máxima diferencia en las columnas de montos de resultados_v12 frente al commit anterior."""
    rel = (EXP1 / "outputs" / "tables" / "resultados_v12.csv").relative_to(DALILA)
    txt = subprocess.run(["git", "-C", str(DALILA), "show", f"{COMMIT_ANTES}:{rel}"], capture_output=True, text=True, check=True).stdout
    o = pd.read_csv(io.StringIO(txt))
    n = pd.read_csv(EXP1 / "outputs" / "tables" / "resultados_v12.csv")
    cols = [c for c in o.columns if pd.api.types.is_numeric_dtype(o[c]) and not pd.api.types.is_bool_dtype(o[c])
            and not re.search(r"pts|pct|sem|masa", c)]
    return float((o[cols] - n[cols]).abs().max().max())


def contraste_sem() -> pd.DataFrame:
    ins = cargar()
    rows = [{"anio": t, "ingresos_SEM_V13": ins.sem[t], "ingresos_SEM_libro": ins.sem_libro[t],
             "diferencia": ins.sem[t] - ins.sem_libro[t], "diferencia_pct": (ins.sem[t] / ins.sem_libro[t] - 1) * 100}
            for t in [2026] + REP[1:]]
    return pd.DataFrame(rows)


def main():
    c = cambios()
    table(c, "exp1_cambios_denominador")
    cs = contraste_sem()
    table(cs, "contraste_ingresos_SEM_V13_libro")
    from nuevo_seguro import _max_dif
    chk = {"7.4 experimento 1: montos en mdp de resultados_v12 sin cambio (máx. desviación)": montos_sin_cambio(),
           "8.1 regresión v1.1: exp1_cambios_denominador (máx. desviación)": _max_dif(c, pd.read_csv(PROJECT / "data" / "v11" / "exp1_cambios_denominador.csv")),
           "7.4 experimento 1: cifras cambiadas que no son puntos ni % del SEM": int((c.tipo == "otro").sum())}
    record("exp1_cifras_cambiadas", len(c), "Cifras del registro del experimento 1 que cambian por el denominador común")
    record("exp1_cifras_cambiadas_pts", int((c.tipo == "puntos del salario").sum()), "Idem, puntos del salario")
    record("exp1_cifras_cambiadas_sem", int((c.tipo == "% ingresos del SEM").sum()), "Idem, % de los ingresos del SEM")
    for _, r in cs.iterrows():
        record(f"SEM_V13_menos_libro_{int(r.anio)}", round(r.diferencia), "Ingresos del SEM: Cuadro V.13 − libro (SEM-A + SEM-GMP), mdp")
        record(f"SEM_V13_menos_libro_pct_{int(r.anio)}", round(r.diferencia_pct, 2), "Idem, % del libro")
    for i, (k, v) in enumerate(chk.items()):
        record(f"chk_exp1_{i}", v, k)
    return chk


if __name__ == "__main__":
    print(json.dumps(main(), ensure_ascii=False, indent=1))
