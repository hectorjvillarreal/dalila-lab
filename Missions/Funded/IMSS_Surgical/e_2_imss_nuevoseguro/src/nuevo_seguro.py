"""Ingreso del nuevo seguro, uso 1 (déficit de GMP), reserva y remanente (K1 y K2), valor presente,
remanente por persona mayor y verificaciones 3.1 a 3.4."""

from __future__ import annotations

import re
import subprocess

import numpy as np
import pandas as pd

from comun import CFG, DERIVED, MDP, P, REP, YEARS, descuento, informe_pdf, record, table
from insumos import ANIOS_INF, Insumos2, cargar

import common as c1

ESC_MASA = ("base", "M2")


def simular(ins: Insumos2, esc: str) -> pd.DataFrame:
    masa = ins.masa_esc(esc)
    I = P["ns_tasa"] * masa
    D = ins.gmp_def.loc[YEARS]
    r = P["r"]
    rows = []
    R, W = 0.0, None
    for t in YEARS:
        exc = I[t] - D[t]
        # K1: el remanente anual se gasta en cuidados; el déficit que el ingreso no cubre queda como déficit no cubierto
        u1, f1 = max(0.0, exc), max(0.0, -exc)
        # K2: reserva hasta 2034; desde 2035, cuidados = remanente + 1/20 de la reserva de inicio de 2035 (monto fijo real)
        pre = R * (1 + r) + exc
        if t == P["k2_inicio"]:
            W = P["k2_fraccion"] * R
        if pre < 0:
            u2, f2 = 0.0, -pre
        else:
            u2 = min(max(0.0, exc) + W, pre) if t >= P["k2_inicio"] else 0.0
            f2 = 0.0
        R_fin = pre - u2 + f2
        rows.append({"escenario_masa": esc, "anio": t, "masa_tope25": masa[t], "ingreso_NS": I[t], "deficit_GMP": D[t],
                     "ingreso_GMP_informe": ins.gmp_ing[t], "k1_remanente_cuidados": u1, "k1_deficit_no_cubierto": f1,
                     "k1_reserva_fin": 0.0, "k2_reserva_inicio": R, "k2_cuidados": u2, "k2_deficit_no_cubierto": f2,
                     "k2_reserva_fin": R_fin, "reduccion_cuna_legal": P["reduccion_cuna"] * masa[t],
                     "infonavit_5pct_teorico": P["infonavit_tasa"] * masa[t], "ingresos_SEM_informe": ins.sem[t]})
        R = R_fin
    d = pd.DataFrame(rows)
    for col in ("ingreso_NS", "deficit_GMP", "k1_remanente_cuidados", "k1_deficit_no_cubierto", "k2_cuidados",
                "k2_deficit_no_cubierto", "k2_reserva_fin", "reduccion_cuna_legal"):
        d[f"{col}_pts_salario"] = d[col] / d.masa_tope25 * 100
        d[f"{col}_pct_ingresos_SEM"] = d[col] / d.ingresos_SEM_informe * 100
    return d


def identidad_reserva(d: pd.DataFrame) -> float:
    """3.4: R(t+1) = R(t)·(1 + r) + I − D − U (+ déficit no cubierto, que no sale de la reserva)."""
    r = P["r"]
    dev = []
    for k, Ri in (("k1", None), ("k2", "k2_reserva_inicio")):
        R0 = d[Ri] if Ri else 0.0
        rhs = R0 * (1 + r) + d.ingreso_NS - d.deficit_GMP - d[f"{k}_cuidados" if k == "k2" else "k1_remanente_cuidados"] \
            + d[f"{k}_deficit_no_cubierto"]
        dev.append(float((d[f"{k}_reserva_fin"] - rhs).abs().max()))
        if Ri:  # encadenamiento: la reserva de inicio es la de fin del año anterior
            dev.append(float(np.abs(d[Ri].iloc[1:].values - d[f"{k}_reserva_fin"].iloc[:-1].values).max()))
    return max(dev)


def valor_presente(ins: Insumos2, sims: dict) -> pd.DataFrame:
    df = descuento(YEARS)
    rows = []
    for esc, d in sims.items():
        x = d.set_index("anio")
        for col, nombre in (("masa_tope25", "Masa salarial con tope de 25 UMA (337 días)"), ("ingreso_NS", "Ingreso del nuevo seguro"),
                            ("deficit_GMP", "Déficit de GMP (Cuadro V.24 interpolado)"),
                            ("k1_remanente_cuidados", "K1: remanente para cuidados"), ("k1_deficit_no_cubierto", "K1: déficit no cubierto"),
                            ("k2_cuidados", "K2: cuidados"), ("k2_deficit_no_cubierto", "K2: déficit no cubierto"),
                            ("reduccion_cuna_legal", "Reducción de las contribuciones legales sobre la nómina (3 puntos)")):
            rows.append({"bloque": "Experimento 2027-2054", "escenario_masa": esc, "concepto": nombre,
                         "vp_mdp2026": float((x[col] * df).sum()), "fuente": "Cálculo propio; descuento al 3 % real a 2026"})
        rows.append({"bloque": "Experimento 2027-2054", "escenario_masa": esc, "concepto": "K2: reserva al cierre de 2054",
                     "vp_mdp2026": float(x.k2_reserva_fin.iloc[-1] * df.iloc[-1]), "fuente": "Saldo final descontado a 2026"})
    return pd.DataFrame(rows)


def contrastes(ins: Insumos2) -> tuple[pd.DataFrame, dict]:
    """Contrastes con el Informe sobre el mismo horizonte que sus valores presentes (30 años desde 2026)."""
    g, cg = CFG["gmp_v24"], CFG["contraste_gmp"]
    df = descuento(ANIOS_INF)
    vps = P["vol_salarios_vp"]
    masa_vp = float((ins.masa.masa_tope25.loc[ANIOS_INF] * df).sum())
    masa_vp_sin = float((ins.masa.masa_sin_tope.loc[ANIOS_INF] * df).sum())
    def_vp = float((ins.gmp_def.loc[ANIOS_INF] * df).sum())
    ing_vp = float((ins.gmp_ing.loc[ANIOS_INF] * df).sum())
    # convención alternativa: descuento a mitad de año
    def_vp_mid = float((ins.gmp_def.loc[ANIOS_INF] * df * (1 + P["r"]) ** -0.5).sum())
    brecha = (P["gmp_prima_eq"] - P["gmp_prima_fin"]) * vps
    eq_exacta = cg["v19_vp_gasto"] / vps
    fin_exacta = cg["v20_aportaciones"] / vps
    redondeo = brecha - (eq_exacta - fin_exacta) * vps
    v19_v24 = -cg["v19_vp_saldo"] + g["vp_saldo"]
    resto = brecha - redondeo - cg["v20_otros_ingresos"] - v19_v24 + g["vp_saldo"]
    H30 = "Informe: 30 años desde 2026"
    rows = [
        {"bloque": H30, "escenario_masa": "base", "concepto": "Volumen de salarios, Informe (Cuadro V.15)", "vp_mdp2026": vps, "fuente": "Informe, Cuadro V.15"},
        {"bloque": H30, "escenario_masa": "base", "concepto": "Masa salarial propia con tope de 25 UMA", "vp_mdp2026": masa_vp, "fuente": "Cálculo propio, mismo horizonte"},
        {"bloque": H30, "escenario_masa": "base", "concepto": "Masa salarial propia sin tope", "vp_mdp2026": masa_vp_sin, "fuente": "Cálculo propio, mismo horizonte"},
        {"bloque": H30, "escenario_masa": "base", "concepto": "2 % × volumen de salarios del Informe", "vp_mdp2026": P["ns_tasa"] * vps, "fuente": "Contraste obligatorio 1.1"},
        {"bloque": H30, "escenario_masa": "base", "concepto": "2 % × masa propia con tope", "vp_mdp2026": P["ns_tasa"] * masa_vp, "fuente": "Cálculo propio"},
        {"bloque": H30, "escenario_masa": "base", "concepto": "Déficit de GMP, Cuadro V.24 (publicado)", "vp_mdp2026": -g["vp_saldo"], "fuente": "Informe, Cuadro V.24"},
        {"bloque": H30, "escenario_masa": "base", "concepto": "Déficit de GMP, serie interpolada, descuento a fin de año", "vp_mdp2026": def_vp, "fuente": "Verificación de la interpolación"},
        {"bloque": H30, "escenario_masa": "base", "concepto": "Déficit de GMP, serie interpolada, descuento a mitad de año", "vp_mdp2026": def_vp_mid, "fuente": "Convención alternativa"},
        {"bloque": H30, "escenario_masa": "base", "concepto": "Ingresos de GMP, serie interpolada", "vp_mdp2026": ing_vp, "fuente": "Frente a 2,750,260 del Cuadro V.24"},
        {"bloque": H30, "escenario_masa": "base", "concepto": "Brecha de primas 1.6 puntos × volumen de salarios", "vp_mdp2026": brecha, "fuente": "Contraste 1.2 (Cuadro II.16)"},
        {"bloque": H30, "escenario_masa": "base", "concepto": "  menos: redondeo de las primas (3.1 − 1.5 frente a 3.053 − 1.500)", "vp_mdp2026": redondeo, "fuente": "Cuadros V.19 y V.20"},
        {"bloque": H30, "escenario_masa": "base", "concepto": "  menos: otros ingresos de GMP (fuera de la prima de financiamiento)", "vp_mdp2026": cg["v20_otros_ingresos"], "fuente": "Cuadro V.20"},
        {"bloque": H30, "escenario_masa": "base", "concepto": "  menos: diferencia entre Cuadro V.19 y Cuadro V.24 (escenario base)", "vp_mdp2026": v19_v24, "fuente": "Cuadros V.19 y V.24"},
        {"bloque": H30, "escenario_masa": "base", "concepto": "  residuo", "vp_mdp2026": resto, "fuente": "Debe ser ≈ 0"},
    ]
    info = {"masa_vp": masa_vp, "masa_vp_sin": masa_vp_sin, "def_vp": def_vp, "def_vp_mid": def_vp_mid, "ing_vp": ing_vp,
            "brecha": brecha, "redondeo": redondeo, "v19_v24": v19_v24, "resto": resto, "eq_exacta": eq_exacta, "fin_exacta": fin_exacta}
    return pd.DataFrame(rows), info


def por_mayor(ins: Insumos2, sims: dict) -> pd.DataFrame:
    rows = []
    for esc, d in sims.items():
        x = d.set_index("anio")
        for base, d65, d80 in (("DH_total", ins.dh65, ins.dh80), ("PAMF", ins.dh65_pamf, ins.dh80_pamf)):
            for t in REP:
                rows.append({"escenario_masa": esc, "denominador": base, "anio": t, "dh_65mas": d65[t], "dh_80mas": d80[t],
                             "k1_remanente_mdp": x.k1_remanente_cuidados[t], "k2_cuidados_mdp": x.k2_cuidados[t],
                             "k1_pesos_por_dh65": x.k1_remanente_cuidados[t] * MDP / d65[t],
                             "k1_pesos_por_dh80": x.k1_remanente_cuidados[t] * MDP / d80[t],
                             "k2_pesos_por_dh65": x.k2_cuidados[t] * MDP / d65[t],
                             "k2_pesos_por_dh80": x.k2_cuidados[t] * MDP / d80[t]})
    return pd.DataFrame(rows)


def v24_del_pdf() -> dict:
    """Lee el Cuadro V.24 del PDF del Informe para la verificación 3.2."""
    pg = str(CFG["gmp_v24"]["pagina_pdf"])
    txt = subprocess.run(["pdftotext", "-layout", "-f", pg, "-l", pg, str(informe_pdf()), "-"],
                         capture_output=True, text=True, check=True).stdout
    blk = txt[txt.index("Cuadro V.24.\n"):]
    blk = blk[:blk.index("Fuente:")]
    lineas = [ln for ln in blk.splitlines() if ln.strip().startswith("Escenario Base")]
    num = lambda ln: [float(v.replace(",", "")) for v in re.findall(r"-?\d[\d,]*", ln)]  # noqa: E731
    return {"ingresos": num(lineas[0]), "saldo": num(lineas[1])}


def verificaciones(ins: Insumos2, sims: dict, info: dict) -> dict:
    chk = {}
    g = CFG["gmp_v24"]
    # 3.1 masa: reproduce la base de la tasa D2 de la v1.2 (recaudación D2 / c)
    ind = c1.load("efecto_indexacion").set_index("anio")
    rep = ind.recaudacion_D2 / ins.c
    m = ins.masa.masa_tope25.loc[rep.index]
    chk["3.1 masa con tope = base de la tasa D2 de la v1.2 (máx. desviación relativa)"] = float((m / rep - 1).abs().max())
    chk["3.1 masa con tope / denominador en puntos de la v1.2, 2027 (razón)"] = float(ins.masa.masa_tope25[2027] / ins.masa.masa_v12_denominador[2027])
    chk["3.1 masa con tope / denominador en puntos de la v1.2, 2054 (razón)"] = float(ins.masa.masa_tope25[2054] / ins.masa.masa_v12_denominador[2054])
    chk["3.1 proporción de la masa por encima del tope, 2027 (%)"] = float(ins.masa.prop_sobre_tope[2027] * 100)
    chk["3.1 proporción de la masa por encima del tope, 2054 (%)"] = float(ins.masa.prop_sobre_tope[2054] * 100)
    # 3.2 transcripción e interpolación
    pdf = v24_del_pdf()
    cfg_ing = g["ingresos"] + [g["vp_ingresos"]]
    cfg_sal = g["saldo"] + [g["vp_saldo"]]
    chk["3.2 Cuadro V.24 transcrito = PDF (celdas distintas)"] = int(sum(a != b for a, b in zip(cfg_ing, pdf["ingresos"])) +
                                                               sum(a != b for a, b in zip(cfg_sal, pdf["saldo"])) +
                                                               abs(len(cfg_ing) - len(pdf["ingresos"])) + abs(len(cfg_sal) - len(pdf["saldo"])))
    chk["3.2 interpolación preserva los años ancla (máx. desviación, mdp)"] = float(max(
        abs(ins.gmp_def[a] + s) for a, s in zip(g["anios"], g["saldo"])))
    chk["3.2 VP del déficit interpolado frente al Cuadro V.24 (%)"] = float((info["def_vp"] / -g["vp_saldo"] - 1) * 100)
    # 3.3 valor presente del ingreso con masa propia frente al contraste del Informe, mismo horizonte
    chk["3.3 VP 2 % × masa propia frente a 2 % × volumen del Informe, mismo horizonte (%)"] = float((info["masa_vp"] / P["vol_salarios_vp"] - 1) * 100)
    # 3.4 identidad de la reserva
    chk["3.4 identidad de la reserva (máx. desviación, mdp)"] = max(identidad_reserva(d) for d in sims.values())
    return chk


def main():
    ins = cargar()
    sims = {e: simular(ins, e) for e in ESC_MASA}
    d = pd.concat(sims.values(), ignore_index=True)
    table(d, "ingreso_vs_GMP")
    d.to_parquet(DERIVED / "ingreso_vs_GMP.parquet", index=False)
    vp = valor_presente(ins, sims)
    con, info = contrastes(ins)
    table(pd.concat([vp, con], ignore_index=True), "valor_presente")
    pm = por_mayor(ins, sims)
    table(pm, "remanente_por_mayor")
    chk = verificaciones(ins, sims, info)

    # ---- registro de cifras ----
    mm = ins.masa
    for t in REP:
        record(f"masa25_{t}", round(mm.masa_tope25[t]), "Σ cotizantes × SBC (R1, tope 25 UMA, piso SM) × UMA × 337, mdp de 2026")
        record(f"cotizantes_{t}", round(mm.cotizantes[t]), "Libro de Finanzas, `Pob Emp & Nuevos` (modelo de cohortes de la v1.2)")
        record(f"sm_uma_{t}", round(mm.sm_uma[t], 3), "SM en veces la UMA (Sup_Fin; v1.2)")
        record(f"prop_sobre_tope_{t}", round(mm.prop_sobre_tope[t] * 100, 2), "% de la masa sin tope que rebasa 25 UMA (forma R1 sin tope)")
        record(f"M2_factor_{t}", round(float(ins.m2[t]), 4), "Formalidad implícita 2025 / formalidad implícita t (prueba C de la v1.2)")
        record(f"formalidad_implicita_{t}", round(float(ins.formalidad[t]), 4), "Cotizantes / ocupados (prueba C de la v1.2)")
        record(f"DH65_{t}", round(ins.dh65[t]), "0.166 × 79,178,109 × (CONAPO 65+ t / CONAPO 65+ 2025)")
        record(f"DH80_{t}", round(ins.dh80[t]), "DH65 × (CONAPO 80+ / CONAPO 65+)")
        record(f"SEM_ingresos_{t}", round(ins.sem[t]), "Informe, Cuadro V.13, interpolación lineal")
        record(f"GMP_deficit_{t}", round(ins.gmp_def[t]), "Informe, Cuadro V.24 (base), interpolación lineal")
        for e, x in sims.items():
            x = x.set_index("anio")
            for col in ("ingreso_NS", "k1_remanente_cuidados", "k1_deficit_no_cubierto", "k2_cuidados", "k2_reserva_fin",
                        "reduccion_cuna_legal", "infonavit_5pct_teorico"):
                record(f"{e}_{col}_{t}", round(x[col][t]), f"ingreso_vs_GMP.csv, {e}, mdp de 2026")
            for col in ("ingreso_NS", "deficit_GMP", "k1_remanente_cuidados", "k2_cuidados", "reduccion_cuna_legal"):
                record(f"{e}_{col}_pts_{t}", round(x[f"{col}_pts_salario"][t], 3), "Puntos del salario (masa con tope, 337 días)")
                record(f"{e}_{col}_sem_{t}", round(x[f"{col}_pct_ingresos_SEM"][t], 2), "% de los ingresos del SEM (Cuadro V.13)")
    record("DH65_2025", round(P["dh_65mas_pamf_2025"] * P["dh_total"]), "0.166 × 79,178,109")
    record("DH65_PAMF_2025", round(P["dh_65mas_pamf_2025"] * P["pamf_2025"]), "0.166 × 63,598,543 (adscripciones a médico familiar)")
    record("CONAPO_65mas_2025", round(ins.p65[2025]), "CONAPO 2023, población de 65 años o más, 2025")
    record("DH65_entre_CONAPO65_2025", round(P["dh_65mas_pamf_2025"] * P["dh_total"] / ins.p65[2025] * 100, 1), "DH65 (instrucción) / población nacional de 65+ (%)")
    record("DH65_PAMF_entre_CONAPO65_2025", round(P["dh_65mas_pamf_2025"] * P["pamf_2025"] / ins.p65[2025] * 100, 1), "DH65 con base PAMF / población nacional de 65+ (%)")
    for t in REP:
        record(f"DH65_PAMF_{t}", round(ins.dh65_pamf[t]), "0.166 × 63,598,543 × crecimiento CONAPO 65+")
        record(f"DH80_PAMF_{t}", round(ins.dh80_pamf[t]), "DH65_PAMF × CONAPO 80+/65+")
    for e, x in sims.items():
        k1 = x[x.k1_deficit_no_cubierto > 0].anio
        k2 = x[x.k2_deficit_no_cubierto > 0].anio
        record(f"{e}_k1_primer_anio_no_cubre", int(k1.min()) if len(k1) else "ninguno", "Primer año en que I < D (K1)")
        record(f"{e}_k1_anios_no_cubre", len(k1), "Años 2027-2054 con I < D")
        record(f"{e}_k2_primer_anio_no_cubre", int(k2.min()) if len(k2) else "ninguno", "Primer año con déficit no cubierto tras usar la reserva (K2)")
        record(f"{e}_k2_reserva_max", round(x.k2_reserva_fin.max()), "Reserva máxima K2 (mdp de 2026)")
        record(f"{e}_k2_reserva_max_anio", int(x.loc[x.k2_reserva_fin.idxmax(), "anio"]), "Año de la reserva máxima K2")
        record(f"{e}_k2_retiro_anual", round(P["k2_fraccion"] * x.set_index("anio").k2_reserva_inicio[P["k2_inicio"]]), "1/20 de la reserva al inicio de 2035 (mdp de 2026)")
        record(f"{e}_k2_reserva_inicio_2035", round(x.set_index("anio").k2_reserva_inicio[P["k2_inicio"]]), "Reserva K2 al inicio de 2035")
        holg = x.ingreso_NS - x.deficit_GMP
        record(f"{e}_holgura_min", round(holg.min()), "Mínimo de ingreso − déficit de GMP, 2027-2054 (mdp de 2026)")
        record(f"{e}_holgura_min_anio", int(x.loc[holg.idxmin(), "anio"]), "Año de la holgura mínima")
        record(f"{e}_holgura_min_pts", round(float((holg / x.masa_tope25 * 100).loc[holg.idxmin()]), 3), "Holgura mínima en puntos del salario")
        primer = x[x.ingreso_NS >= x.deficit_GMP].anio
        record(f"{e}_cubre_desde", int(primer.min()) if len(primer) else "nunca", "Primer año con I ≥ D")
        cruce = x[(x.anio > 2027) & (x.ingreso_NS < x.deficit_GMP)].anio
        record(f"{e}_deja_de_cubrir", int(cruce.min()) if len(cruce) else "no deja de cubrir", "Primer año posterior a 2027 con I < D")
    for _, r in vp.iterrows():
        k = {"Masa salarial con tope de 25 UMA (337 días)": "masa", "Ingreso del nuevo seguro": "ingreso", "Déficit de GMP (Cuadro V.24 interpolado)": "deficit",
             "K1: remanente para cuidados": "k1_remanente", "K1: déficit no cubierto": "k1_no_cubierto", "K2: cuidados": "k2_cuidados",
             "K2: déficit no cubierto": "k2_no_cubierto", "Reducción de las contribuciones legales sobre la nómina (3 puntos)": "reduccion",
             "K2: reserva al cierre de 2054": "k2_reserva_final"}[r.concepto]
        record(f"VP_{r.escenario_masa}_{k}", round(r.vp_mdp2026), "valor_presente.csv, 2027-2054, 3 % real, mdp de 2026")
    for k in ("masa_vp", "masa_vp_sin", "def_vp", "def_vp_mid", "ing_vp", "brecha", "redondeo", "v19_v24", "resto"):
        record(f"contraste_{k}", round(info[k]), "valor_presente.csv, horizonte del Informe (30 años desde 2026)")
    record("contraste_ns_informe", round(P["ns_tasa"] * P["vol_salarios_vp"]), "0.02 × 176,481,700")
    record("contraste_ns_propio", round(P["ns_tasa"] * info["masa_vp"]), "0.02 × masa propia, mismo horizonte")
    record("GMP_prima_eq_exacta", round(info["eq_exacta"] * 100, 3), "5,388,234 / 176,481,700 (Cuadros V.19 y V.15)")
    record("GMP_prima_fin_exacta", round(info["fin_exacta"] * 100, 3), "2,647,226 / 176,481,700 (Cuadros V.20 y V.15)")
    for _, r in pm.iterrows():
        for col in ("k1_pesos_por_dh65", "k1_pesos_por_dh80", "k2_pesos_por_dh65", "k2_pesos_por_dh80"):
            record(f"{r.escenario_masa}_{r.denominador}_{col}_{int(r.anio)}", round(r[col]), "remanente_por_mayor.csv, pesos de 2026 por persona al año")
    for i, (k, v) in enumerate(chk.items()):
        record(f"chk_{i:02d}_{k.split()[0]}", round(v, 6) if isinstance(v, float) else v, k)
    return chk


if __name__ == "__main__":
    import json
    print(json.dumps(main(), ensure_ascii=False, indent=1))
