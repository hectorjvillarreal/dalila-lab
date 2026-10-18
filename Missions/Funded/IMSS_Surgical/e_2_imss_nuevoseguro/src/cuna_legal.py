"""Cuña contributiva legal por nivel de salario (sección 1.5): ley vigente (a), experimento 2 (b) y
experimento 2 + tasa proporcional D2 del experimento 1 (c). Incidencia legal; no mide incidencia económica."""

from __future__ import annotations

import numpy as np
import pandas as pd

from comun import CFG, P, PROJECT, record, table
from insumos import Insumos2, cargar

K = CFG["cuna"]
LIM = K["cyv_limite_uma"]
# Art. 168, fr. II, inciso a) de la LSS vigente (texto del DOF 16-12-2020): tasas que rigen desde 2030
ART168 = [3.150, 4.202, 6.552, 7.962, 8.902, 9.573, 10.077, 11.875]


def tramo(w: float, sm: float, lectura: str = "uma") -> int:
    """Índice del tramo de cesantía y vejez y de cuota social para un SBC de w UMA.
    lectura 'uma': tramos por UMA (un salario de 1.01 SM cae donde su valor en UMA lo ubique);
    lectura 'primer': un salario apenas arriba del mínimo cae en el tramo «1.01 SM a 1.50 UMA»."""
    if abs(w - sm) < 1e-9:
        return 0
    if lectura == "primer":
        return 1
    for i in range(1, 7):
        if w <= LIM[i] + 1e-9:
            return i
    return 7


def componentes(w: float, sm: float, anio: int, col: str, lectura: str = "uma", rt: float = 1.9078) -> dict:
    i = tramo(w, sm, lectura)
    pa, ob, fe = K["patron"], K["obrera"], K["federal"]
    exc = max(0.0, w - 3.0) / w
    d = {"SEM cuota fija": pa["cf_uma"] / w if col != "c" else P["c_d2"] * 100,
         "SEM excedente": pa["excedente"] * exc, "SEM prestaciones en dinero": pa["pd"], "SEM GMP": pa["gmp"],
         "Invalidez y Vida": pa["iv"], "Riesgos de Trabajo (prima promedio)": rt,
         "Guarderías y Prestaciones Sociales": pa["gps"], "Retiro": pa["retiro"],
         "Cesantía y vejez": K["cyv"][anio][i],
         "Infonavit": P["infonavit_tasa"] * 100 if col == "a" else 0.0,
         "Nuevo seguro": P["ns_tasa"] * 100 if col != "a" else 0.0}
    obrera = ob["excedente"] * exc + ob["pd"] + ob["gmp"] + ob["iv"] + ob["cyv"]
    # LSS art. 36: con salario mínimo, el patrón cubre íntegramente la cuota de la persona trabajadora
    en_sm = i == 0
    d["Cuota obrera a cargo del patrón (art. 36 LSS)"] = obrera if en_sm else 0.0
    patron = sum(d.values())
    cs = K["cuota_social_dic2025"][i] / K["uma_dic2025"] * 100 / w
    federal = fe["cf_uma"] / w + fe["pd"] + fe["gmp"] + fe["iv"] + cs
    d.update({"Total a cargo del patrón (incidencia legal)": patron, "Cuotas obreras": 0.0 if en_sm else obrera,
              "Aportación federal (incluye cuota social)": federal})
    d["Cuña legal total"] = patron + d["Cuotas obreras"] + federal
    return d


def tabla(ins: Insumos2, rt: float) -> pd.DataFrame:
    rows = []
    for anio in K["anios"]:
        sm = ins.sm[anio]
        niveles = [("Salario mínimo", sm, "uma"), ("1.01 SM, lectura por UMA", 1.01 * sm, "uma"),
                   ("1.01 SM, primer tramo tras el mínimo", 1.01 * sm, "primer")]
        niveles += [(f"{w:g} UMA", float(w), "uma") for w in K["niveles_uma"]]
        for nombre, w, lect in niveles:
            cols = {c: componentes(w, sm, anio, c, lect, rt) for c in ("a", "b", "c")}
            for comp in cols["a"]:
                rows.append({"anio": anio, "nivel": nombre, "sbc_uma": round(w, 4), "debajo_del_SM": w < sm - 1e-9,
                             "tramo_cyv": K["cyv_tramos"][tramo(w, sm, lect)], "componente": comp,
                             "a_ley_vigente": cols["a"][comp], "b_experimento2": cols["b"][comp],
                             "c_experimento2_mas_D2": cols["c"][comp]})
    return pd.DataFrame(rows)


def verificar(t: pd.DataFrame) -> dict:
    tot = t[t.componente == "Total a cargo del patrón (incidencia legal)"]
    chk = {"3.5 (b) = (a) − 3 puntos en todo nivel hasta 25 UMA (máx. desviación, puntos)":
           float((tot.b_experimento2 - (tot.a_ley_vigente - 3)).abs().max())}
    cyv = t[t.componente == "Cesantía y vejez"]
    malos = 0
    for _, r in cyv.iterrows():
        malos += int(r.a_ley_vigente not in K["cyv"][r.anio])
    chk["3.5 tasas de cesantía y vejez fuera de la tabla de 1.5 (casos)"] = malos
    chk["3.5 tabla 2030 = art. 168 fr. II a) del DOF 16-12-2020 (celdas distintas)"] = int(sum(a != b for a, b in zip(K["cyv"][2030], ART168)))
    return chk


def main():
    ins = cargar()
    t = tabla(ins, CFG["corridas"][CFG["corrida"]]["rt_cuna"])
    table(t, "cuna_legal_por_salario")
    chk = verificar(t)
    # 7.1: con la prima de RT de la v1.0 (1.80) se reproduce la tabla de la corrida del 18-10
    from nuevo_seguro import _max_dif
    v10 = tabla(ins, CFG["corridas"]["v1.0"]["rt_cuna"])
    chk["7.1 regresión v1.0: cuna_legal_por_salario (máx. desviación)"] = _max_dif(v10, pd.read_csv(PROJECT / "data" / "v10" / "cuna_legal_por_salario.csv"))
    chk = {k.replace("3.5 (b)", "3.5/7.5 (b)"): v for k, v in chk.items()}
    piv = t.set_index(["anio", "nivel", "componente"])
    for anio in K["anios"]:
        record(f"cuna_sm_uma_{anio}", round(ins.sm[anio], 3), "SM en veces la UMA (Sup_Fin)")
        for nivel in t[t.anio == anio].nivel.unique():
            for comp, key in (("Total a cargo del patrón (incidencia legal)", "patron"), ("Cuña legal total", "total"),
                              ("Cesantía y vejez", "cyv"), ("Cuotas obreras", "obrera"), ("Aportación federal (incluye cuota social)", "federal")):
                for c in ("a_ley_vigente", "b_experimento2", "c_experimento2_mas_D2"):
                    record(f"cuna_{anio}_{nivel}_{key}_{c[0]}", round(float(piv.loc[(anio, nivel, comp), c]), 3),
                           "cuna_legal_por_salario.csv, % del SBC")
        sm_p = piv.loc[(anio, "Salario mínimo", "Total a cargo del patrón (incidencia legal)"), "a_ley_vigente"]
        for lect in ("1.01 SM, lectura por UMA", "1.01 SM, primer tramo tras el mínimo"):
            p = piv.loc[(anio, lect, "Total a cargo del patrón (incidencia legal)"), "a_ley_vigente"]
            cy = piv.loc[(anio, lect, "Cesantía y vejez"), "a_ley_vigente"]
            k = "uma" if "UMA" in lect else "primer"
            record(f"escalon_{anio}_{k}_cyv", round(float(cy), 3), f"Tasa patronal de cesantía y vejez a 1.01 SM, {lect}")
            record(f"escalon_{anio}_{k}_cyv_salto", round(float(cy - 3.150), 3), "Salto frente a 3.150 % del salario mínimo (puntos)")
            record(f"escalon_{anio}_{k}_patron_salto", round(float(p - sm_p), 3),
                   "Salto del total a cargo del patrón entre SM y 1.01 SM, ley vigente (puntos; neto del fin del art. 36)")
    for nivel, key in (("Salario mínimo", "sm"), ("5.55 UMA", "prom"), ("25 UMA", "25uma")):
        for anio in K["anios"]:
            x = piv.loc[(anio, nivel, "Total a cargo del patrón (incidencia legal)")]
            record(f"cuna_{anio}_{key}_c_menos_a", round(float(x.c_experimento2_mas_D2 - x.a_ley_vigente), 3),
                   "Cambio de la cuña legal a cargo del patrón, (c) − (a), puntos del SBC")
    record("RT_prima_cuna", CFG["corridas"][CFG["corrida"]]["rt_cuna"], "Prima de RT en el Cuadro X-2.2 (Informe, Cuadro A.3)")
    for i, (k, v) in enumerate(chk.items()):
        record(f"chk_cuna_{i}", round(v, 9) if isinstance(v, float) else v, k)
    return chk


if __name__ == "__main__":
    import json
    print(json.dumps(main(), ensure_ascii=False, indent=1))
