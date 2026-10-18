"""Ingreso del nuevo seguro, uso 1 (déficit de GMP), reserva y remanente (K1 y K2) por escenario de formalidad,
valor presente, remanente por persona mayor, verificaciones 3.1 a 3.4 y 7.1 a 7.3."""

from __future__ import annotations

import re
import subprocess

import numpy as np
import pandas as pd

from comun import CFG, DERIVED, MDP, P, PROJECT, REP, YEARS, descuento, informe_pdf, record, table
from insumos import ANIOS_INF, Insumos2, cargar

import common as c1

COLS_RAZON = ("ingreso_NS", "deficit_GMP", "k1_remanente_cuidados", "k1_deficit_no_cubierto", "k2_cuidados",
              "k2_deficit_no_cubierto", "k2_reserva_fin", "reduccion_cuna_legal")


def corrida(nombre: str | None = None) -> dict:
    return CFG["corridas"][nombre or CFG["corrida"]]


def simular(ins: Insumos2, esc: str, ajuste: bool, k2_regla: str = "v1.1", sin_prov: bool = False,
            s_masa: bool = False) -> pd.DataFrame:
    masa = ins.masa_esc(esc)
    razon = masa / ins.masa_esc("base")
    ing = ins.gmp_ing.loc[YEARS]
    if s_masa:
        # v1.2, S-masa: el ingreso crece al ritmo del ingreso de GMP del Informe, desde el nivel propio de 2027
        I = P["ns_tasa"] * ins.masa_esc("base")[YEARS[0]] * ing / ing[YEARS[0]] * razon
    else:
        I = P["ns_tasa"] * masa
    prov = ins.gmp_prov.loc[YEARS]
    D0 = ins.gmp_def.loc[YEARS] - (prov if sin_prov else 0.0)
    # v1.1: con menos cotizantes también baja lo que recauda GMP; su gasto no se ajusta (supuesto aprobado)
    D = D0 + ing * (1 - razon) if ajuste else D0
    r = P["r"]
    rows = []
    R, W = 0.0, None
    for t in YEARS:
        exc = I[t] - D[t]
        # K1: el remanente anual se gasta en cuidados; el déficit que el ingreso no cubre queda como déficit no cubierto
        u1, f1 = max(0.0, exc), max(0.0, -exc)
        if t == P["k2_inicio"]:
            W = P["k2_fraccion"] * R
        if k2_regla == "v1.1":
            # v1.1: desde 2035, cuidados = remanente + retiro fijo, acotado por lo disponible, aun con faltante de GMP
            pre = R * (1 + r) + exc
            if pre < 0:
                u2, f2 = 0.0, -pre
            else:
                u2 = min(max(0.0, exc) + W, pre) if t >= P["k2_inicio"] else 0.0
                f2 = 0.0
            R_fin = pre - u2 + f2
            extra = {}
        else:
            # v1.2 (regla de Beth): el ingreso cubre GMP; el faltante sale de la reserva; el retiro fijo para cuidados
            # solo en años sin faltante de GMP y hasta donde alcance la reserva
            interes = R * r
            disp = R + interes
            dep = max(0.0, exc) if t < P["k2_inicio"] else 0.0
            rem = max(0.0, exc) if t >= P["k2_inicio"] else 0.0
            ret_gmp = min(-exc, disp) if exc < 0 else 0.0
            f2 = -exc - ret_gmp if exc < 0 else 0.0
            ret_cui = min(W, disp) if (t >= P["k2_inicio"] and exc >= 0) else 0.0
            u2 = rem + ret_cui
            R_fin = R + interes + dep - ret_gmp - ret_cui
            extra = {"k2_intereses": interes, "k2_deposito": dep, "k2_retiro_gmp": ret_gmp, "k2_retiro_cuidados": ret_cui,
                     "k2_remanente_del_anio": rem}
        rows.append({"escenario_masa": esc, "anio": t, "masa_tope25": masa[t], "ingreso_NS": I[t], "deficit_GMP": D[t],
                     "ingreso_GMP_informe": ing[t], "k1_remanente_cuidados": u1, "k1_deficit_no_cubierto": f1,
                     "k1_reserva_fin": 0.0, "k2_reserva_inicio": R, "k2_cuidados": u2, "k2_deficit_no_cubierto": f2,
                     "k2_reserva_fin": R_fin, "reduccion_cuna_legal": P["reduccion_cuna"] * masa[t],
                     "infonavit_5pct_teorico": P["infonavit_tasa"] * masa[t], "ingresos_SEM_informe": ins.sem[t]})
        if ajuste:
            rows[-1].update({"razon_masa": razon[t], "deficit_GMP_institucional": ins.gmp_def[t], "ingreso_GMP_ajustado": ing[t] * razon[t],
                             "provisiones_GMP": prov[t], "margen_sin_provisiones": exc + (0.0 if sin_prov else prov[t])})
        rows[-1].update(extra)
        R = R_fin
    d = pd.DataFrame(rows)
    for col in COLS_RAZON:
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


VP_CONCEPTOS = (("masa_tope25", "Masa salarial con tope de 25 UMA (337 días)", "masa"), ("ingreso_NS", "Ingreso del nuevo seguro", "ingreso"),
                ("deficit_GMP", "Déficit de GMP (Cuadro V.24 interpolado)", "deficit"),
                ("k1_remanente_cuidados", "K1: remanente para cuidados", "k1_remanente"), ("k1_deficit_no_cubierto", "K1: déficit no cubierto", "k1_no_cubierto"),
                ("k2_cuidados", "K2: cuidados", "k2_cuidados"), ("k2_deficit_no_cubierto", "K2: déficit no cubierto", "k2_no_cubierto"),
                ("reduccion_cuna_legal", "Reducción de las contribuciones legales sobre la nómina (3 puntos)", "reduccion"))


def valor_presente(sims: dict) -> pd.DataFrame:
    df = descuento(YEARS)
    rows = []
    for esc, d in sims.items():
        x = d.set_index("anio")
        for col, nombre, _ in VP_CONCEPTOS:
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


def bases_personas(ins: Insumos2, nombres) -> list:
    todas = {"DH_total": (ins.dh65, ins.dh80), "Informe_max": (ins.dh65, ins.dh80),
             "PAMF": (ins.dh65_pamf, ins.dh80_pamf), "ENIGH": (ins.enigh65, ins.enigh80)}
    return [(n, *todas[n]) for n in nombres]


def por_mayor(ins: Insumos2, sims: dict, nombres) -> pd.DataFrame:
    rows = []
    for esc, d in sims.items():
        x = d.set_index("anio")
        for base, d65, d80 in bases_personas(ins, nombres):
            for t in REP:
                rows.append({"escenario_masa": esc, "denominador": base, "anio": t, "dh_65mas": d65[t], "dh_80mas": d80[t],
                             "k1_remanente_mdp": x.k1_remanente_cuidados[t], "k2_cuidados_mdp": x.k2_cuidados[t],
                             "k1_pesos_por_dh65": x.k1_remanente_cuidados[t] * MDP / d65[t],
                             "k1_pesos_por_dh80": x.k1_remanente_cuidados[t] * MDP / d80[t],
                             "k2_pesos_por_dh65": x.k2_cuidados[t] * MDP / d65[t],
                             "k2_pesos_por_dh80": x.k2_cuidados[t] * MDP / d80[t]})
    return pd.DataFrame(rows)


def resumen(sims: dict, ins: Insumos2) -> pd.DataFrame:
    """Sección 1.3 de la v1.1: por escenario, primer año sin cobertura (K1 y K2), déficit no cubierto y remanente."""
    df = descuento(YEARS)
    rows = []
    for esc, d in sims.items():
        x = d.set_index("anio")
        k1 = x.index[x.k1_deficit_no_cubierto > 0]
        k2 = x.index[x.k2_deficit_no_cubierto > 0]
        rows.append({"escenario_masa": esc,
                     "formalidad_2054_pct": ins.formalidad_esc[esc].loc[2054] * 100,
                     "k1_primer_anio_sin_cobertura": int(k1.min()) if len(k1) else None,
                     "k2_primer_anio_sin_cobertura": int(k2.min()) if len(k2) else None,
                     "k1_deficit_no_cubierto_2054": x.k1_deficit_no_cubierto.iloc[-1],
                     "k2_deficit_no_cubierto_2054": x.k2_deficit_no_cubierto.iloc[-1],
                     "vp_k1_deficit_no_cubierto": float((x.k1_deficit_no_cubierto * df).sum()),
                     "vp_k2_deficit_no_cubierto": float((x.k2_deficit_no_cubierto * df).sum()),
                     "vp_k1_remanente": float((x.k1_remanente_cuidados * df).sum()),
                     "vp_k2_cuidados": float((x.k2_cuidados * df).sum()),
                     "vp_ingreso": float((x.ingreso_NS * df).sum()), "vp_deficit_GMP": float((x.deficit_GMP * df).sum())})
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
    chk["3.1 masa con tope / denominador anterior de la v1.2, 2027 (razón)"] = float(ins.masa.masa_tope25[2027] / ins.masa.masa_v12_denominador[2027])
    chk["3.1 masa con tope / denominador anterior de la v1.2, 2054 (razón)"] = float(ins.masa.masa_tope25[2054] / ins.masa.masa_v12_denominador[2054])
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
    # 7.2 base sin ajuste y monotonicidad del déficit ajustado
    b = sims["base"].set_index("anio")
    chk["7.2 base: déficit ajustado = Cuadro V.24 (máx. desviación, mdp)"] = float((b.deficit_GMP - ins.gmp_def.loc[YEARS]).abs().max())
    if "M3" in sims and "M2" in sims:
        m3, m2 = sims["M3"].set_index("anio"), sims["M2"].set_index("anio")
        gana = ins.factor["M2"].loc[YEARS] < 1
        viol = ((m2.deficit_GMP <= m3.deficit_GMP) | (m3.deficit_GMP <= b.deficit_GMP)) & gana
        chk["7.2 déficit M2 > M3 > base en años con ganancia de formalización (años que fallan)"] = int(viol.sum())
    # 7.3 personas mayores con IMSS (ENIGH) ≤ población nacional
    chk["7.3 base ENIGH de 65+ / población nacional de 65+, máximo 2027-2054 (%)"] = float((ins.enigh65 / ins.p65).loc[YEARS].max() * 100)
    return chk


def calcular(nombre: str | None = None) -> dict:
    ins = cargar()
    cr = corrida(nombre)
    sims = {e: simular(ins, e, cr["ajuste_ingreso_gmp"], cr.get("k2_regla", "v1.1")) for e in cr["escenarios"]}
    con, info = contrastes(ins)
    return {"ins": ins, "sims": sims, "ingreso_vs_GMP": pd.concat(sims.values(), ignore_index=True),
            "valor_presente": pd.concat([valor_presente(sims), con], ignore_index=True),
            "remanente_por_mayor": por_mayor(ins, sims, cr["personas"]), "resumen": resumen(sims, ins), "info": info}


def _max_dif(a: pd.DataFrame, b: pd.DataFrame) -> float:
    """Máxima diferencia absoluta entre dos tablas con las mismas columnas (texto: 0 si iguales, inf si no)."""
    if list(a.columns) != list(b.columns) or len(a) != len(b):
        return float("inf")
    dev = 0.0
    for c in a.columns:
        if pd.api.types.is_numeric_dtype(a[c]) and pd.api.types.is_numeric_dtype(b[c]):
            dev = max(dev, float(np.nanmax(np.abs(a[c].values.astype(float) - b[c].values.astype(float)))))
        elif not (a[c].astype(str).values == b[c].astype(str).values).all():
            return float("inf")
    return dev


def regresion_v10() -> dict:
    """7.1: con la configuración v1.0 se reproducen las tablas de la corrida del 18-10 (data/v10/)."""
    r = calcular("v1.0")
    v10 = PROJECT / "data" / "v10"
    out = {}
    for name in ("ingreso_vs_GMP", "valor_presente", "remanente_por_mayor"):
        out[f"7.1 regresión v1.0: {name} (máx. desviación)"] = _max_dif(r[name], pd.read_csv(v10 / f"{name}.csv"))
    return out


def main():
    r = calcular()
    ins, sims, info = r["ins"], r["sims"], r["info"]
    d = r["ingreso_vs_GMP"]
    table(d, "ingreso_vs_GMP")
    d.to_parquet(DERIVED / "ingreso_vs_GMP.parquet", index=False)
    vp = r["valor_presente"]
    table(vp, "valor_presente")
    pm = r["remanente_por_mayor"]
    table(pm, "remanente_por_mayor")
    rs = r["resumen"]
    table(rs, "resumen_escenarios")
    chk = verificaciones(ins, sims, info)
    chk.update(regresion_v10())

    # ---- registro de cifras ----
    mm = ins.masa
    for t in REP:
        record(f"masa25_{t}", round(mm.masa_tope25[t]), "Σ cotizantes × SBC (R1, tope 25 UMA, piso SM) × UMA × 337, mdp de 2026")
        record(f"cotizantes_{t}", round(mm.cotizantes[t]), "Libro de Finanzas, `Pob Emp & Nuevos` (modelo de cohortes de la v1.2)")
        record(f"sm_uma_{t}", round(mm.sm_uma[t], 3), "SM en veces la UMA (Sup_Fin; v1.2)")
        record(f"prop_sobre_tope_{t}", round(mm.prop_sobre_tope[t] * 100, 2), "% de la masa sin tope que rebasa 25 UMA (forma R1 sin tope)")
        record(f"formalidad_implicita_{t}", round(float(ins.formalidad[t]), 4), "Cotizantes / ocupados (prueba C de la v1.2)")
        for e in sims:
            record(f"{e}_formalidad_{t}", round(float(ins.formalidad_esc[e][t]) * 100, 2), f"Formalidad implícita del escenario {e} (%)")
            record(f"{e}_factor_masa_{t}", round(float(ins.factor[e][t]), 4), f"Masa {e} / masa base")
        record(f"DH65_{t}", round(ins.dh65[t]), "Conteo máximo: 0.166 × 79,178,109 × (CONAPO 65+ t / CONAPO 65+ 2025)")
        record(f"DH80_{t}", round(ins.dh80[t]), "Conteo máximo: DH65 × (CONAPO 80+ / CONAPO 65+)")
        record(f"ENIGH65_{t}", round(ins.enigh65[t]), "Tasa IMSS (inst_1) de la ENIGH 2024 por grupo quinquenal y sexo × CONAPO, 65+")
        record(f"ENIGH80_{t}", round(ins.enigh80[t]), "Idem, 80+")
        record(f"ENIGH65_entre_CONAPO65_{t}", round(ins.enigh65[t] / ins.p65[t] * 100, 1), "Base ENIGH 65+ / población nacional de 65+ (%)")
        record(f"DH65_entre_CONAPO65_{t}", round(ins.dh65[t] / ins.p65[t] * 100, 1), "Conteo máximo 65+ / población nacional de 65+ (%)")
        record(f"SEM_ingresos_{t}", round(ins.sem[t]), "Informe, Cuadro V.13, interpolación lineal")
        record(f"SEM_ingresos_libro_{t}", round(ins.sem_libro[t]), "Libro de Finanzas, SEM-A + SEM-GMP")
        record(f"GMP_deficit_{t}", round(ins.gmp_def[t]), "Informe, Cuadro V.24 (base), interpolación lineal")
        record(f"GMP_ingresos_{t}", round(ins.gmp_ing[t]), "Informe, Cuadro V.24 (base), ingresos, interpolación lineal")
        record(f"GMP_provisiones_{t}", round(ins.gmp_prov[t]), "Informe, Cuadro V.19, provisiones, interpolación lineal")
        for e, x in sims.items():
            x = x.set_index("anio")
            for col in ("ingreso_NS", "deficit_GMP", "k1_remanente_cuidados", "k1_deficit_no_cubierto", "k2_cuidados", "k2_reserva_fin",
                        "reduccion_cuna_legal", "infonavit_5pct_teorico", "masa_tope25"):
                record(f"{e}_{col}_{t}", round(x[col][t]), f"ingreso_vs_GMP.csv, {e}, mdp de 2026")
            for col in ("ingreso_NS", "deficit_GMP", "k1_remanente_cuidados", "k1_deficit_no_cubierto", "k2_cuidados", "reduccion_cuna_legal"):
                record(f"{e}_{col}_pts_{t}", round(x[f"{col}_pts_salario"][t], 3), "Puntos del salario (masa del escenario con tope, 337 días)")
                record(f"{e}_{col}_sem_{t}", round(x[f"{col}_pct_ingresos_SEM"][t], 2), "% de los ingresos del SEM (Cuadro V.13)")
    record("DH65_2025", round(P["dh_65mas_pamf_2025"] * P["dh_total"]), "Conteo máximo: 0.166 × 79,178,109")
    record("CONAPO_65mas_2025", round(ins.p65[2025]), "CONAPO 2023, población de 65 años o más, 2025")
    record("DH65_entre_CONAPO65_2025", round(P["dh_65mas_pamf_2025"] * P["dh_total"] / ins.p65[2025] * 100, 1), "Conteo máximo / población nacional de 65+ (%)")
    record("ENIGH_tasa_IMSS_65mas", round(ins.enigh_tasa65 * 100, 2), "ENIGH 2024, % de 65+ con inst_1 = 1 (ponderado)")
    record("ENIGH_tasa_IMSS_80mas", round(ins.enigh_tasa80 * 100, 2), "ENIGH 2024, % de 80+ con inst_1 = 1 (ponderado)")
    record("ENIGH65_2025", round(ins.enigh65[2025]), "Base ENIGH, 65+, 2025")
    record("ENIGH_n_min_celda", int(ins.enigh_n.min()), "Observaciones mínimas por celda grupo × sexo (65+)")
    for (g_, s_), v in ins.enigh_tasa.items():
        record(f"ENIGH_tasa_{g_}_{s_}", round(v * 100, 2), "Tasa IMSS por grupo quinquenal (85 = 85 y más) y sexo, ENIGH 2024 (%)")
    for e, x in sims.items():
        xi = x.set_index("anio")
        k1 = x[x.k1_deficit_no_cubierto > 0].anio
        k2 = x[x.k2_deficit_no_cubierto > 0].anio
        record(f"{e}_k1_primer_anio_no_cubre", int(k1.min()) if len(k1) else "ninguno", "Primer año en que I < D (K1)")
        record(f"{e}_k1_cubre_hasta", int(k1.min()) - 1 if len(k1) else 2054, "Último año cubierto antes del primero sin cobertura (K1)")
        record(f"{e}_k1_anios_no_cubre", len(k1), "Años 2027-2054 con I < D")
        record(f"{e}_k2_primer_anio_no_cubre", int(k2.min()) if len(k2) else "ninguno", "Primer año con déficit no cubierto tras usar la reserva (K2)")
        record(f"{e}_k2_reserva_max", round(x.k2_reserva_fin.max()), "Reserva máxima K2 (mdp de 2026)")
        record(f"{e}_k2_reserva_max_anio", int(x.loc[x.k2_reserva_fin.idxmax(), "anio"]), "Año de la reserva máxima K2")
        record(f"{e}_k2_retiro_anual", round(P["k2_fraccion"] * xi.k2_reserva_inicio[P["k2_inicio"]]), "1/20 de la reserva al inicio de 2035 (mdp de 2026)")
        record(f"{e}_k2_reserva_inicio_2035", round(xi.k2_reserva_inicio[P["k2_inicio"]]), "Reserva K2 al inicio de 2035")
        holg = x.ingreso_NS - x.deficit_GMP
        record(f"{e}_holgura_min", round(holg.min()), "Mínimo de ingreso − déficit de GMP, 2027-2054 (mdp de 2026)")
        record(f"{e}_holgura_min_anio", int(x.loc[holg.idxmin(), "anio"]), "Año de la holgura mínima")
        record(f"{e}_holgura_min_pts", round(float((holg / x.masa_tope25 * 100).loc[holg.idxmin()]), 3), "Holgura mínima en puntos del salario")
        if "margen_sin_provisiones" in x:
            ms = x.margen_sin_provisiones
            record(f"{e}_margen_sin_prov_min", round(ms.min()), "Mínimo de ingreso − (déficit − provisiones de GMP), 2027-2054")
            record(f"{e}_margen_sin_prov_min_anio", int(x.loc[ms.idxmin(), "anio"]), "Año del margen mínimo sin provisiones")
            record(f"{e}_margen_sin_prov_2036", round(xi.margen_sin_provisiones[2036]), "Margen sin provisiones en 2036")
    for _, r_ in vp[vp.bloque == "Experimento 2027-2054"].iterrows():
        k = {n: c for _, n, c in VP_CONCEPTOS} | {"K2: reserva al cierre de 2054": "k2_reserva_final"}
        record(f"VP_{r_.escenario_masa}_{k[r_.concepto]}", round(r_.vp_mdp2026), "valor_presente.csv, 2027-2054, 3 % real, mdp de 2026")
    for k in ("masa_vp", "masa_vp_sin", "def_vp", "def_vp_mid", "ing_vp", "brecha", "redondeo", "v19_v24", "resto"):
        record(f"contraste_{k}", round(info[k]), "valor_presente.csv, horizonte del Informe (30 años desde 2026)")
    record("contraste_ns_informe", round(P["ns_tasa"] * P["vol_salarios_vp"]), "0.02 × 176,481,700")
    record("contraste_ns_propio", round(P["ns_tasa"] * info["masa_vp"]), "0.02 × masa propia, mismo horizonte")
    record("GMP_prima_eq_exacta", round(info["eq_exacta"] * 100, 3), "5,388,234 / 176,481,700 (Cuadros V.19 y V.15)")
    record("GMP_prima_fin_exacta", round(info["fin_exacta"] * 100, 3), "2,647,226 / 176,481,700 (Cuadros V.20 y V.15)")
    for _, r_ in pm.iterrows():
        for col in ("k1_pesos_por_dh65", "k1_pesos_por_dh80", "k2_pesos_por_dh65", "k2_pesos_por_dh80"):
            record(f"{r_.escenario_masa}_{r_.denominador}_{col}_{int(r_.anio)}", round(r_[col]), "remanente_por_mayor.csv, pesos de 2026 por persona al año")
    for i, (k, v) in enumerate(chk.items()):
        record(f"chk_{i:02d}_{k.split()[0]}", round(v, 6) if isinstance(v, float) else v, k)
    return chk


if __name__ == "__main__":
    import json
    print(json.dumps(main(), ensure_ascii=False, indent=1))
