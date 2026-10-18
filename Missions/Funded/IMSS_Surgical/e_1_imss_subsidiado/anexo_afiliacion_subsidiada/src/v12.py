"""Salidas de la instrucción v1.2: asequibilidad, población excluida, Cuadro X.1 en tres paneles,
sensibilidades, efecto de indexación, Bloque C contra el status quo, referencias y figuras."""

from __future__ import annotations

import json

import matplotlib
import numpy as np
import pandas as pd

from common import FIGURES, NUMBERS_JSON, P, UMA, YEARS, load, record, subsidio, table, wquantile
from enigh import HH, _csv, _num
from proyeccion import Insumos, _esc, pago_formal, pago_informal, umbrales_t
from reporte import AQUA, AZUL, FUENTE, GRIS, NARANJA, TINTA, TINTA2, _estilo

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

REP = [2026, 2030, 2040, 2054]
D = P["dias_cotizados"]
NOMBRES = {"base": "Base v1.2 (D2·G2·S1·τ 0.50·ρ 0.75·μ 1.10)", "regresion_v11": "Regresión v1.1", "S2": "S2 focalizado",
           "S3": "S3 amplio", "G1": "G1 (el informal paga F_g)", "D1": "D1 precio plano en UMA", "tau30": "Adopción τ = 0.30",
           "tau70": "Adopción τ = 0.70", "tau90": "Adopción τ = 0.90 (solo con descuento automático)", "T1": "T1 voluntaria",
           "rho50": "Cobro ρ = 0.50", "rho100": "Cobro ρ = 1.00", "mu100": "Selección μ = 1.00", "mu130": "Selección μ = 1.30",
           "U2_enigh": "U2 individual (h_b ENIGH 0.80)", "U2_informe": "U2 individual (h_b Informe 1.07)",
           "pim1": "π_m = 1 %", "pim2": "π_m = 2 %", "C2": "C2 población ligada a la formalización", "F1": "F1 dentro del esquema",
           "plano": "Perfil plano", "estilizado_2": "Perfil 65+/20-64 = 2", "estilizado_4": "Perfil 65+/20-64 = 4",
           "umbral_fijo": "Umbrales fijos en UMA", "C2_pim1": "C2 con π_m = 1 %"}


def asequibilidad(ins):
    tit = ins.tit
    k = ins.k24 * ins.G[2026]
    hog = _csv("concentradohogar", HH + ["ing_cor", "salud"])
    for c in ("ing_cor", "salud"):
        hog[c] = _num(hog[c]).fillna(0.0)
    t = tit.merge(hog, on=HH, how="left")   # tit ya trae el decil del hogar
    t["m26"] = t.m_tit * k
    # ingreso del hogar en pesos de 2026, con el mismo factor de ingreso que el titular (múltiplos de UMA × k)
    t["ing_hogar_26"] = t.ing_cor / (365 / 4) / P["uma_2024"] * k * UMA * 365
    # gasto de bolsillo en salud: solo conversión de precios (UMA 2026 / UMA 2024)
    t["oop_26"] = t.salud * 4 * UMA / P["uma_2024"]
    sc_d2g2 = _esc({}, "base_v12")
    sc_d2g1 = _esc({"G": "G1"}, "base_v12")
    sc_d1g1 = _esc({"D": "D1", "G": "G1", "umbral": "fijo", "dias": 365}, "base_v12")
    m0, m1 = umbrales_t(ins, sc_d2g2, 2026, "tit")
    rows = []
    for q in (10, 20, 30, 50, 70, 90):
        mq = wquantile(t.m26, t.factor, q / 100)
        lo, hi = wquantile(t.m26, t.factor, max(0, q - 2.5) / 100), wquantile(t.m26, t.factor, min(100, q + 2.5) / 100)
        band = t[(t.m26 >= lo) & (t.m26 <= hi)]
        ing_h = wquantile(band.ing_hogar_26, band.factor, 0.5)
        s = float(subsidio(mq, m0, m1))
        y = mq * UMA * 365
        row = {"percentil": q, "m_UMA_2026": mq, "ingreso_laboral_anual": y, "ingreso_hogar_anual_mediana": ing_h}
        for lab, sc, dd in (("D2_G2", sc_d2g2, D), ("D2_G1", sc_d2g1, D), ("D1_G1", sc_d1g1, 365)):
            pr, _, _ = pago_informal(ins, sc, np.array([mq]), np.array([s]), dd)
            row[f"prima_{lab}"] = float(pr[0])
            row[f"pct_ingreso_laboral_{lab}"] = float(pr[0]) / y * 100 if y > 0 else np.nan
            row[f"pct_ingreso_hogar_{lab}"] = float(pr[0]) / ing_h * 100 if ing_h > 0 else np.nan
        rows.append(row)
    a = pd.DataFrame(rows)
    table(a, "asequibilidad")
    med = float(a.set_index("percentil").loc[50, "prima_D2_G2"])
    record("chk12_6.6_prima_mediana_dif_pct", round((med / 3700 - 1) * 100, 2), "6.6 prima de la mediana D2-G2 frente a ~3,700 pesos (tolerancia ±25 %)")
    for _, r in a.iterrows():
        q = int(r.percentil)
        record(f"aseq_p{q}_m", round(r.m_UMA_2026, 3), "Percentil del ingreso laboral del titular informal, UMA de 2026")
        for lab in ("D2_G2", "D2_G1", "D1_G1"):
            record(f"aseq_p{q}_prima_{lab}", round(r[f"prima_{lab}"]), f"Prima anual determinada, {lab}, S1, 2026 (pesos de 2026)")
            record(f"aseq_p{q}_pctlab_{lab}", round(r[f"pct_ingreso_laboral_{lab}"], 2), "Prima / ingreso laboral anual del titular (%)")
            record(f"aseq_p{q}_pcthog_{lab}", round(r[f"pct_ingreso_hogar_{lab}"], 2), "Prima / ingreso corriente anual del hogar, mediana de titulares en ±2.5 percentiles (%)")
    # por decil: prima D2-G2 frente al gasto de bolsillo en salud del hogar
    s_t = subsidio(t.m26.values, m0, m1)
    t["prima_D2G2"] = pago_informal(ins, sc_d2g2, t.m26.values, s_t, D)[0]
    dec = t.groupby("decil").apply(lambda g: pd.Series({
        "hogares": g.factor.sum(),
        "gasto_bolsillo_salud_anual": np.average(g.oop_26, weights=g.factor),
        "prima_D2_G2_anual": np.average(g.prima_D2G2, weights=g.factor)}), include_groups=False).reset_index()
    dec["prima_entre_gasto_bolsillo"] = dec.prima_D2_G2_anual / dec.gasto_bolsillo_salud_anual
    table(dec, "asequibilidad_por_decil")
    for _, r in dec.iterrows():
        record(f"aseq_decil{int(r.decil)}_oop", round(r.gasto_bolsillo_salud_anual), "ENIGH 2024, concentradohogar.salud (cuidados de la salud) × 4, pesos de 2026, hogares objetivo")
        record(f"aseq_decil{int(r.decil)}_prima", round(r.prima_D2_G2_anual), "Prima D2-G2 media de los hogares objetivo del decil, 2026")
    # referencia: cuota patronal de un formal de salario mínimo, 2026
    sm = ins.sm[2026]
    antes = P["cf_patron"] * UMA * D
    despues = ins.c * sm * UMA * D
    record("SM2026_cuota_patronal_vigente", round(antes), "0.2040 × UMA × 337, formal de salario mínimo 2026")
    record("SM2026_cuota_patronal_vigente_pct", round(P["cf_patron"] / sm * 100, 2), "Como % del salario")
    record("SM2026_cuota_D2", round(despues), "c × SM × 337")
    record("SM2026_cuota_D2_pct", round(ins.c * 100, 2), "c, como % del salario")
    return a, dec


def excluidos(ins):
    per = load("enigh_personas")
    x = per[~per.contrib & ~per.persona_objetivo].copy()
    x["g"] = np.minimum(x.edad, 90)
    record("excl_total_2024", round(x.factor.sum()), "ENIGH 2024; sin cobertura contributiva y fuera de hogares con ocupado sin cobertura")
    record("excl_65mas_2024", round(x.factor[x.edad >= 65].sum()), "Idem, 65 años o más")
    record("excl_65mas_pct", round(x.factor[x.edad >= 65].sum() / x.factor.sum() * 100, 1), "Idem, % del total")
    rows = []
    for t in YEARS:
        w = x.factor.values * ins.ratio[t].reindex(pd.MultiIndex.from_arrays([x.g, x.sexo])).values
        rows.append({"anio": t, "excluidos": w.sum(), "excluidos_65mas": w[x.edad.values >= 65].sum()})
    d = pd.DataFrame(rows)
    table(d, "poblacion_excluida")
    x["grupo_edad"] = pd.cut(x.edad, [0, 15, 25, 45, 65, 200], right=False, labels=["0-14", "15-24", "25-44", "45-64", "65+"])
    table(x.groupby("grupo_edad", observed=True).factor.sum().rename("personas").reset_index(), "poblacion_excluida_edad")
    for y in (2030, 2054):
        r = d.set_index("anio").loc[y]
        record(f"excl_{y}", round(r.excluidos), "Reponderado con CONAPO")
        record(f"excl_65mas_{y}", round(r.excluidos_65mas), "Idem, 65 años o más")


def cuadro_x1(r12):
    base = r12[(r12.corrida == "base")].set_index(["bloque", "anio"])
    c2 = r12[(r12.corrida == "C2")].set_index(["bloque", "anio"])
    p1 = r12[(r12.corrida == "pim1") & (r12.bloque == "Total")].set_index("anio")
    c2p1 = r12[(r12.corrida == "C2_pim1") & (r12.bloque == "Total")].set_index("anio")
    cols = [("C1", y) for y in REP] + [("C2", y) for y in (2040, 2054)]
    for panel, suf in (("mdp", ""), ("pts_sbc", "_pts_sbc"), ("pct_sem", "_pct_sem")):
        rows = []
        def fila(nombre, f):
            rows.append({"concepto": nombre, **{f"{c}_{y}": f(c, y) for c, y in cols}})
        src = {"C1": base, "C2": c2}
        fila("Personas cubiertas (millones)", lambda c, y: src[c].loc[("A", y), "personas_cubiertas"] / 1e6)
        fila("Pagos determinados", lambda c, y: src[c].loc[("A", y), f"pagos_determinados{suf}"])
        fila("Pagos cobrados", lambda c, y: src[c].loc[("A", y), f"pagos_privados{suf}"])
        fila("Prima no cobrada", lambda c, y: src[c].loc[("A", y), f"no_cobrado{suf}"])
        fila("GF: cuota fija F_g", lambda c, y: src[c].loc[("A", y), f"GF_cuota_fija{suf}"])
        fila("GF: subsidio", lambda c, y: src[c].loc[("A", y), f"GF_subsidio{suf}"])
        fila("GF: Bloque B", lambda c, y: src[c].loc[("B", y), f"GF_subsidio{suf}"])
        fila("Costo de atención", lambda c, y: src[c].loc[("Total", y), f"costo{suf}"])
        fila("Saldo sin fuente asignada (π_m = 0)", lambda c, y: src[c].loc[("Total", y), f"saldo{suf}"])
        fila("Saldo sin fuente asignada (π_m = 1 %)",
             lambda c, y: (p1 if c == "C1" else c2p1).loc[y, f"saldo{suf}"])
        table(pd.DataFrame(rows), f"cuadro_X1_{panel}")


def sensibilidades(r12):
    t = r12[r12.bloque == "Total"].set_index(["corrida", "anio"])
    rows = []
    for c in r12.corrida.unique():
        row = {"corrida": c, "descripcion": NOMBRES[c]}
        for y in (2030, 2054):
            for col in ("saldo", "saldo_pts_sbc", "pagos_GF", "personas_cubiertas", "costo"):
                row[f"{col}_{y}"] = t.loc[(c, y), col]
        rows.append(row)
    s = pd.DataFrame(rows)
    b = s.set_index("corrida").loc["base"]
    s["delta_saldo_pts_2054"] = s.saldo_pts_sbc_2054 - b.saldo_pts_sbc_2054
    s["orden"] = s[~s.corrida.isin(["base", "regresion_v11", "C2_pim1"])].delta_saldo_pts_2054.abs().rank(ascending=False, method="first")
    table(s, "sensibilidades_v12")
    for _, x in s.iterrows():
        for y in (2030, 2054):
            for col in ("saldo", "saldo_pts_sbc", "pagos_GF", "personas_cubiertas"):
                v = x[f"{col}_{y}"]
                record(f"v12_{x.corrida}_{col}_{y}", round(v, 3) if "pts" in col else round(v), "sensibilidades_v12.csv")
    return s


def registrar(r12, ind, bc):
    t = r12.set_index(["corrida", "bloque", "anio"])
    for y in REP:
        for bl in ("A", "B", "Total"):
            a = t.loc[("base", bl, y)]
            for c in ("personas_cubiertas", "titulares_o_formales", "pagos_determinados", "pagos_privados", "no_cobrado",
                      "GF_cuota_fija", "GF_subsidio", "pagos_GF", "costo", "saldo"):
                if c in ("personas_cubiertas", "titulares_o_formales"):
                    if bl == "A":
                        record(f"v12b_{bl}_{c}_{y}", round(a[c]), f"resultados_v12.csv, base, {bl}, {y}")
                    continue
                record(f"v12b_{bl}_{c}_mdp_{y}", round(a[c]), f"resultados_v12.csv, base, {bl}, {y}")
                record(f"v12b_{bl}_{c}_pts_{y}", round(a[f"{c}_pts_sbc"], 3), "Idem, puntos del SBC (337 días)")
                record(f"v12b_{bl}_{c}_sem_{y}", round(a[f"{c}_pct_sem"], 2), "Idem, % de los ingresos del SEM")
        cub = t.loc[("base", "A", y), "personas_cubiertas"]
        record(f"v12b_cubiertos_pct_DH_{y}", round(cub / P["dh_total_informe"] * 100, 1), "Personas cubiertas / 79,178,109 DH (Cuadro I.4)")
    a = t.loc[("base", "Total", 2026)]
    record("v12b_costo_pct_pib_2026", round(a.costo_pct_pib_2026, 3), "Costo 2026 / PIB 2026")
    record("v12b_GF_pct_pib_2026", round(a.pagos_GF_pct_pib_2026, 3), "Pagos federales 2026 / PIB 2026")
    record("v12b_saldo_pct_pib_2026", round(a.saldo_pct_pib_2026, 3), "Saldo 2026 / PIB 2026")
    for y in (2030, 2040, 2054):
        r = ind.set_index("anio").loc[y]
        record(f"v12_indexacion_mdp_{y}", round(r.diferencia), "efecto_indexacion.csv: recaudación D2 − cuota fija vigente, formales")
        record(f"v12_indexacion_pts_{y}", round(r.diferencia_pts_sbc, 3), "Idem, puntos del SBC")
        record(f"v12_indexacion_sem_{y}", round(r.diferencia_pct_sem, 2), "Idem, % ingresos SEM")
        for cuota in ("D2", "vigente"):
            x = bc[(bc.anio == y) & (bc.cuota == cuota)].iloc[0]
            src = f"bloque_C_vs_status_quo.csv, {cuota}, {y}"
            record(f"v12_C_{cuota}_ingresos_{y}", round(x.ingresos_SEM), src)
            record(f"v12_C_{cuota}_costo_{y}", round(x.costo), src)
            record(f"v12_C_{cuota}_neto_{y}", round(x.efecto_neto_SEM), src)
            record(f"v12_C_{cuota}_neto_pts_{y}", round(x.efecto_neto_pts_sbc, 3), src)
            record(f"v12_C_{cuota}_GF_{y}", round(x.GF), src)
            record(f"v12_C_dh_por_cot_{y}", round(x.dh_por_cotizante, 2), src)
    bB = r12[(r12.corrida == "S3") & (r12.bloque == "B")].set_index("anio")
    for y in (2026, 2030, 2054):
        record(f"v12_S3_B_mdp_{y}", round(bB.loc[y, "pagos_GF"]), "resultados_v12.csv, S3, Bloque B")
    record("v12_S1_B_total", round(float(r12[(r12.corrida == "base") & (r12.bloque == "B")].pagos_GF.sum()), 2), "Σ 2026-2054 del Bloque B en la base (S1)")


def referencias(ins):
    reg = json.loads(NUMBERS_JSON.read_text())
    pef = P["pef2026_salud_no_contrib_mdp2027"]
    tot = sum(pef.values())
    for k, v in pef.items():
        record(f"PEF2026_{k}_mdp2027", v, "CIEP, «PPEF 2027: Gasto en salud por subsistema», Cuadro 1 (PEF 2026 en mdp de 2027; proporcionado por Héctor 08-10-2026)")
    record("PEF2026_no_contrib_total_mdp2027", round(tot, 1), "Suma SSa + IMSS-Bienestar + FASSA + Bienestar")
    record("PEF2026_no_contrib_total_mdp2026", round(tot / (1 + P["inflacion_2027"]), 1), "Idem / (1 + 3.82 %, inflación 2027 de Sup_Fin)")
    record("SM_2024", P["sm_2024"], "Resolución del H. Consejo de Representantes de la CONASAMI, DOF 12/12/2023 (resto del país; ZLFN 374.89)")
    record("SM_2024_en_UMA2024", round(P["sm_2024"] / P["uma_2024"], 4), "248.93 / 108.57")
    record("m_tit_p50_vs_SM2024", round(reg["m_tit_p50"]["valor"] / (P["sm_2024"] / P["uma_2024"]), 4), "Mediana del titular informal / SM 2024, ambos en UMA de 2024")
    record("hb_informe_titulares", P["hb_informe_titulares"], "Informe Cuadro I.4: 40,980,786 familiares / 38,197,323 titulares")
    record("ocupacion_hosp_2o_nivel_2025", 75.7, "Informe, sección de capacidad (pág. PDF 115)")
    record("ocupacion_hosp_3er_nivel_2025", 83.7, "Informe, pág. PDF 115")
    for y in (2030, 2054):
        record(f"v11_saldo_pts_337_{y}", round(reg[f"sens_base_saldo_pts_sbc_{y}"]["valor"] * 365 / 337, 3),
               "Saldo base v1.1 en puntos del SBC con masa de 337 días (= 365-días × 365/337)")


def figuras(r12, s):
    FIGURES.mkdir(parents=True, exist_ok=True)
    a = r12[(r12.corrida == "base") & (r12.bloque == "Total")].set_index("anio")
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
    series = (("costo", NARANJA, "Costo de atención"), ("GF_cuota_fija", AQUA, "GF: cuota fija F_g"),
              ("pagos_privados", AZUL, "Pagos cobrados"), ("GF_subsidio", GRIS, "GF: subsidio"))
    for col, color, lab in series:
        y = a[col] / 1000
        ax[0].plot(a.index, y, color=color, lw=2, label=lab)
        ax[0].text(a.index[-1] + 0.4, y.iloc[-1], lab, color=TINTA2, fontsize=8, va="center")
    ax[0].set_title("Escenario base v1.2 (miles de millones de pesos de 2026)", fontsize=10, color=TINTA, loc="left")
    ax[0].set_xlim(2026, 2064)
    ax[0].set_ylim(0, None)
    ax[0].legend(fontsize=8, frameon=False, loc="center left")
    y = a.saldo_pts_sbc
    ax[1].bar(a.index, y, color=GRIS, width=0.8)
    ax[1].axhline(0, color=TINTA2, lw=0.8)
    ax[1].set_ylim(y.min() * 1.2, 0.05)
    ax[1].set_title("Saldo sin fuente asignada (puntos del SBC, 337 días)", fontsize=10, color=TINTA, loc="left")
    for yr in REP:
        ax[1].text(yr, y.loc[yr] - 0.04, f"{y.loc[yr]:.2f}", ha="center", va="top", fontsize=7.5, color=TINTA2)
    for x in ax:
        _estilo(x)
    fig.text(0.01, 0.01, FUENTE, fontsize=7, color=TINTA2)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(FIGURES / "v12_base.png", dpi=160)
    plt.close(fig)

    d = s[~s.corrida.isin(["regresion_v11", "C2_pim1"])].set_index("corrida").sort_values("saldo_pts_sbc_2054")
    fig, ax = plt.subplots(figsize=(8.8, 7))
    yy = np.arange(len(d))
    base = d.loc["base", "saldo_pts_sbc_2054"]
    ax.axvline(base, color=GRIS, lw=1, ls="--")
    ax.axvline(0, color=TINTA2, lw=0.8)
    ax.hlines(yy, base, d.saldo_pts_sbc_2054, color="#cde2fb", lw=2)
    ax.scatter(d.saldo_pts_sbc_2054, yy, color=[AZUL if i != "base" else TINTA for i in d.index], s=40, zorder=3)
    ax.set_yticks(yy, [NOMBRES[i] for i in d.index], fontsize=8)
    for i, v in zip(yy, d.saldo_pts_sbc_2054):
        ax.text(v + (0.04 if v >= base else -0.04), i, f"{v:+.2f}", va="center", ha="left" if v >= base else "right",
                fontsize=7.5, color=TINTA2)
    lo, hi = d.saldo_pts_sbc_2054.min(), d.saldo_pts_sbc_2054.max()
    ax.set_xlim(lo - 0.3, max(hi, 0) + 0.3)
    ax.set_xlabel("Saldo total sin fuente asignada en 2054 (puntos del SBC)", fontsize=8, color=TINTA2)
    ax.set_title("Sensibilidad del saldo de 2054, v1.2", fontsize=10, color=TINTA, loc="left")
    _estilo(ax)
    ax.grid(axis="x", color="#ebeae6", lw=0.8)
    ax.grid(axis="y", visible=False)
    fig.text(0.01, 0.01, FUENTE, fontsize=6.5, color=TINTA2)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(FIGURES / "v12_sensibilidades_2054.png", dpi=160)
    plt.close(fig)


def main():
    ins = Insumos()
    r12 = load("resultados_v12")
    ind = load("efecto_indexacion")
    bc = load("bloque_C_vs_status_quo")
    referencias(ins)
    asequibilidad(ins)
    excluidos(ins)
    cuadro_x1(r12)
    s = sensibilidades(r12)
    registrar(r12, ind, bc)
    figuras(r12, s)


if __name__ == "__main__":
    main()
