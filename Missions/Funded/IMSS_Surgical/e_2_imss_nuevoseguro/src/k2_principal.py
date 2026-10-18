"""Instrucción v1.3: K2 como regla principal (cuadro principal, resumen K2 y K1 lado a lado, personas mayores con K2),
escenario de ritmo histórico MH en sensibilidades, convención «último año con cobertura completa» y verificaciones 6.1-6.4."""

from __future__ import annotations

import json

import numpy as np
import pandas as pd

from comun import MDP, P, PROJECT, REP, YEARS, descuento, record, table
from insumos import cargar
from nuevo_seguro import _max_dif, calcular, simular
from sensibilidades_v12 import grilla, reserva_k2

ESC3 = ("base", "M3", "M2")
ESC4 = ("base", "M3", "MH", "M2")
COMBOS = ((False, False, "con provisiones, masa del libro"), (True, False, "sin provisiones, masa del libro"),
          (False, True, "con provisiones, S-masa"), (True, True, "sin provisiones, S-masa"))


def ultimo_anio(x: pd.DataFrame, col: str) -> int:
    """Último año con cobertura completa de GMP: el anterior al primer año con déficit no cubierto (2054 si no hay)."""
    k = x.index[x[col] > 0]
    return int(k.min()) - 1 if len(k) else YEARS[-1]


def cuadro_principal(sims: dict) -> pd.DataFrame:
    rows = []
    for e in ESC3:
        x = sims[e].set_index("anio")
        mov = x.k2_deposito - x.k2_retiro_gmp
        for nombre, serie in (("Ingreso del nuevo seguro (2 %)", x.ingreso_NS), ("Déficit de GMP", x.deficit_GMP),
                              ("Depósito a la reserva (+) o retiro para GMP (−)", mov),
                              ("Gasto en cuidados", x.k2_cuidados), ("Déficit no cubierto", x.k2_deficit_no_cubierto)):
            for t in REP:
                rows.append({"escenario_masa": e, "concepto": nombre, "anio": t, "mdp": float(serie[t]),
                             "pts_salario": float(serie[t] / x.masa_tope25[t] * 100)})
    return pd.DataFrame(rows)


def resumen_k2_k1(sims: dict) -> pd.DataFrame:
    df = descuento(YEARS)
    rows = []
    for e in ESC3:
        x = sims[e].set_index("anio")
        for regla, nc, cu in (("K2", "k2_deficit_no_cubierto", "k2_cuidados"), ("K1", "k1_deficit_no_cubierto", "k1_remanente_cuidados")):
            res = float(x.k2_reserva_fin[YEARS[-1]] * df.iloc[-1]) if regla == "K2" else 0.0
            vpc = float((x[cu] * df).sum())
            rows.append({"escenario_masa": e, "regla": regla, "ultimo_anio_cobertura_completa": ultimo_anio(x, nc),
                         "deficit_no_cubierto_2054": float(x[nc][YEARS[-1]]), "vp_deficit_no_cubierto": float((x[nc] * df).sum()),
                         "vp_cuidados": vpc, "vp_reserva_final": res, "vp_cuidados_mas_reserva": vpc + res})
    return pd.DataFrame(rows)


def sensibilidad_v13(ins) -> tuple[pd.DataFrame, dict]:
    rows, sims = [], {}
    for e in ESC4:
        for sp, sm, et in COMBOS:
            d = simular(ins, e, True, "v1.2", sin_prov=sp, s_masa=sm)
            sims[(e, sp, sm)] = d
            x = d.set_index("anio")
            for regla, col in (("K2", "k2_deficit_no_cubierto"), ("K1", "k1_deficit_no_cubierto")):
                rows.append({"escenario_masa": e, "regla": regla, "variante": et, "ultimo_anio_cobertura_completa": ultimo_anio(x, col)})
    t = pd.DataFrame(rows).pivot_table(index=["regla", "escenario_masa"], columns="variante", values="ultimo_anio_cobertura_completa",
                                       sort=False).reset_index()
    return t[["regla", "escenario_masa"] + [c for _, _, c in COMBOS]], sims


def verificaciones(ins, sims: dict, rs: pd.DataFrame, sv: pd.DataFrame, sims_s: dict) -> dict:
    chk = {}
    v12 = PROJECT / "data" / "v12"
    r = calcular("v1.2")
    for name in ("ingreso_vs_GMP", "valor_presente", "remanente_por_mayor", "resumen"):
        f = "resumen_escenarios" if name == "resumen" else name
        chk[f"6.1 regresión v1.2: {f} (máx. desviación)"] = _max_dif(r[name], pd.read_csv(v12 / f"{f}.csv"))
    g, gs = grilla(ins)
    chk["6.1 regresión v1.2: sensibilidad_provisiones_masa (máx. desviación)"] = _max_dif(g, pd.read_csv(v12 / "sensibilidad_provisiones_masa.csv"))
    chk["6.1 regresión v1.2: reserva_K2 (máx. desviación)"] = _max_dif(reserva_k2(gs), pd.read_csv(v12 / "reserva_K2.csv"))
    # 6.2: el resumen coincide con la v1.2
    old = pd.read_csv(v12 / "resumen_escenarios.csv").set_index("escenario_masa")
    dev, fechas = 0.0, 0
    for _, x in rs.iterrows():
        o = old.loc[x.escenario_masa]
        k = "k2" if x.regla == "K2" else "k1"
        dev = max(dev, abs(x.vp_deficit_no_cubierto - o[f"vp_{k}_deficit_no_cubierto"]),
                  abs(x.vp_cuidados - (o.vp_k2_cuidados if k == "k2" else o.vp_k1_remanente)),
                  abs(x.deficit_no_cubierto_2054 - o[f"{k}_deficit_no_cubierto_2054"]))
        p = o[f"{k}_primer_anio_sin_cobertura"]
        fechas += int(x.ultimo_anio_cobertura_completa != (YEARS[-1] if pd.isna(p) else int(p) - 1))
    chk["6.2 resumen K2/K1 frente a la v1.2 (máx. desviación, mdp)"] = float(dev)
    chk["6.2 fechas que no corresponden a la v1.2 (primer año sin cobertura − 1)"] = fechas
    # 6.3: MH
    fe = ins.formalidad_esc
    yrs = range(2026, 2055)
    post = range(2035, 2055)
    chk["6.3 MH ≤ base en todos los años (años que fallan)"] = int(sum(fe["MH"][t] > fe["base"][t] + 1e-12 for t in yrs))
    chk["6.3 MH entre M2 y M3, 2035-2054: formalidad (años que fallan)"] = int(sum(not (fe["M2"][t] <= fe["MH"][t] <= fe["M3"][t]) for t in post))
    chk["6.3 MH por encima de M3, 2026-2034 (años; informativo)"] = int(sum(fe["MH"][t] > fe["M3"][t] for t in range(2026, 2035)))
    m = {e: sims_s[(e, False, False)].set_index("anio") for e in ("M2", "MH", "M3")}
    chk["6.3 MH entre M2 y M3, 2035-2054: masa y déficit ajustado (años que fallan)"] = int(sum(
        not (m["M2"].masa_tope25[t] <= m["MH"].masa_tope25[t] <= m["M3"].masa_tope25[t]) or
        not (m["M3"].deficit_GMP[t] <= m["MH"].deficit_GMP[t] <= m["M2"].deficit_GMP[t]) for t in post))
    sx = sv.set_index(["regla", "escenario_masa"])
    malas = 0
    for regla in ("K2", "K1"):
        for _, _, c in COMBOS:
            a, b, h = sx.loc[(regla, "M2"), c], sx.loc[(regla, "M3"), c], sx.loc[(regla, "MH"), c]
            malas += int(not (min(a, b) <= h <= max(a, b)))
    chk["6.3 último año con cobertura de MH entre M2 y M3 (columnas que fallan)"] = malas
    # 6.4: reserva final = inicio de 2054 + movimiento de 2054, descontada a 2026; K1 = 0
    df = descuento(YEARS)
    dev = 0.0
    for e in ESC3:
        x = sims[e].set_index("anio")
        cierre = x.k2_reserva_inicio[2054] + x.k2_intereses[2054] + x.k2_deposito[2054] - x.k2_retiro_gmp[2054] - x.k2_retiro_cuidados[2054]
        v = rs[(rs.escenario_masa == e) & (rs.regla == "K2")].vp_reserva_final.iloc[0]
        dev = max(dev, abs(cierre * df.iloc[-1] - v))
    chk["6.4 reserva final en VP = (inicio 2054 + movimiento 2054) descontada a 2026 (máx. desviación)"] = float(dev)
    chk["6.4 reserva final en K1 (máximo)"] = float(rs[rs.regla == "K1"].vp_reserva_final.max())
    return chk


def main():
    ins = cargar()
    sims = {e: simular(ins, e, True, "v1.2") for e in ESC3}
    cp = cuadro_principal(sims)
    table(cp, "cuadro_principal_K2")
    rs = resumen_k2_k1(sims)
    table(rs, "resumen_K2_K1")
    sv, sims_s = sensibilidad_v13(ins)
    table(sv, "sensibilidad_v13")
    chk = verificaciones(ins, sims, rs, sv, sims_s)

    # ---- registro ----
    for _, r in cp.iterrows():
        k = {"Ingreso del nuevo seguro (2 %)": "ingreso", "Déficit de GMP": "deficit", "Depósito a la reserva (+) o retiro para GMP (−)": "mov_reserva",
             "Gasto en cuidados": "cuidados", "Déficit no cubierto": "no_cubierto"}[r.concepto]
        record(f"k2p_{r.escenario_masa}_{k}_{r.anio}", round(r.mdp), "cuadro_principal_K2.csv, mdp de 2026")
        record(f"k2p_{r.escenario_masa}_{k}_pts_{r.anio}", round(r.pts_salario, 3), "cuadro_principal_K2.csv, puntos del salario")
    for _, r in rs.iterrows():
        k = f"res_{r.escenario_masa}_{r.regla}"
        record(f"{k}_ultimo", int(r.ultimo_anio_cobertura_completa), "resumen_K2_K1.csv: último año con cobertura completa de GMP")
        for c in ("deficit_no_cubierto_2054", "vp_deficit_no_cubierto", "vp_cuidados", "vp_reserva_final", "vp_cuidados_mas_reserva"):
            record(f"{k}_{c}", round(r[c]), "resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026")
    for _, r in sv.iterrows():
        for i, (_, _, c) in enumerate(COMBOS):
            record(f"sens13_{r.regla}_{r.escenario_masa}_{i}", int(r[c]), f"sensibilidad_v13.csv, último año con cobertura completa, {c}")
    fe = ins.formalidad_esc
    record("MH_paso_pts_anio", round(ins.paso_historico * 100, 4), "(razón 2025 − razón 2005) / 20, serie histórica de la v1.2")
    record("MH_formalidad_2054", round(float(fe["MH"][2054]) * 100, 2), "Formalidad de MH en 2054 (%)")
    record("MH_sin_tope_2026", round(float(ins.formalidad_mh_sin_tope[2026]) * 100, 2), "MH sin tope, 2026 (%)")
    record("base_formalidad_2026", round(float(fe["base"][2026]) * 100, 2), "Formalidad base, 2026 (%)")
    record("MH_anios_con_tope", int(sum(ins.formalidad_mh_sin_tope[t] > fe["base"][t] for t in range(2026, 2055))), "Años en que el tope en la base es activo")
    for t in (2030, 2035):
        record(f"MH_formalidad_{t}", round(float(fe["MH"][t]) * 100, 2), f"Formalidad MH {t} (%)")
        record(f"M3_formalidad_{t}", round(float(fe["M3"][t]) * 100, 2), f"Formalidad M3 {t} (%)")
    pm = pd.read_csv(PROJECT / "tablas" / "remanente_por_mayor.csv")
    b = pm[(pm.escenario_masa == "base") & (pm.denominador == "ENIGH")].set_index("anio")
    for t in (2040, 2054):
        for g in ("65", "80"):
            record(f"k2_pesos_por_dh{g}_{t}", round(b[f"k2_pesos_por_dh{g}"][t]), "Base, K2, base ENIGH, pesos de 2026 por persona al año")
    for i, (k, v) in enumerate(chk.items()):
        record(f"chk13_{i:02d}", round(v, 9) if isinstance(v, float) else v, k)
    return chk


if __name__ == "__main__":
    print(json.dumps(main(), ensure_ascii=False, indent=1))
