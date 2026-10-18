"""Cifras que pide la sección 10 v1.1 del Núcleo 13 (instrucción 20261018_BDH_N13_seccion10…_build_v1.1). Sin supuestos
nuevos: usa la configuración base_v12 y las salidas ya calculadas. Registra en NUMBERS.md:

- 1.1  pago de la parte patronal de la cuota fija (20.40 % de la UMA), con el mismo subsidio, umbrales y días que la serie
       de la cuota proporcional de la Figura 10.2 (D1·G2 de `pago_informal`: cuota anual de 365 días y excedente con 337, como la Figura 10.2);
- 1.5  pago total del hogar mediano con afiliación individual (U2): cada integrante paga la cuota proporcional sobre el
       ingreso por persona del hogar, con el subsidio por persona; más el excedente de quien trabaja;
- 1.3  sensibilidad del costo por persona al conteo de derechohabientes (79.2 millones del Informe frente a 70.7 del
       Núcleo 13), escalando el costo sin otra corrida; y la proporción de la población con IMSS en 2030 (método ENIGH);
- 1.9  saldo de 2030 como % de los ingresos del SEM del libro (Tabla 5 del Núcleo 13).
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from common import P, UMA, load, record, subsidio, table, wquantile

D = P["dias_cotizados"]       # días del excedente en la serie de la Figura 10.2 (asequibilidad de v12.py)
from enigh import HH, _csv, _num
from proyeccion import Insumos, _esc, e_anual, pago_informal, umbrales_t

DH_INFORME = 79_178_109      # Informe, Cuadro I.4
DH_N13 = 70_690_000          # Núcleo 13, Anexo I, Tabla I.1 (70.69 millones)
SEM_TABLA5_2030 = 611_200    # Núcleo 13, Tabla 5 (mdp de 2026); igual al libro (611,178)


def cuota_fija_patronal(ins, t):
    """1.1: misma tabla que la Figura 10.2, con la parte patronal de la cuota fija y el mismo subsidio."""
    sc_d2 = _esc({}, "base_v12")
    sc_d1 = _esc({"D": "D1"}, "base_v12")          # G2: el Gobierno Federal paga su parte fija aparte
    m0, m1 = umbrales_t(ins, sc_d2, 2026, "tit")
    rows = []
    for q in (10, 20, 30, 50, 70, 90):
        mq = wquantile(t.m26, t.factor, q / 100)
        s = float(subsidio(mq, m0, m1))
        y = mq * UMA * 365
        prop = float(pago_informal(ins, sc_d2, np.array([mq]), np.array([s]), D)[0][0])
        fija = float(pago_informal(ins, sc_d1, np.array([mq]), np.array([s]), D)[0][0])
        rows.append({"percentil": q, "m_UMA_2026": mq, "subsidio": s, "ingreso_laboral_anual": y,
                     "prima_proporcional": prop, "pct_proporcional": prop / y * 100,
                     "prima_fija_patronal": fija, "pct_fija_patronal": fija / y * 100})
    a = pd.DataFrame(rows)
    table(a, "seccion10_v11_cuota_fija_patronal")
    for _, r in a.iterrows():
        q = int(r.percentil)
        src = "seccion10_v11_cuota_fija_patronal.csv: (1 − s) × 20.40 % × UMA 2026 × 365 + excedente, mismo subsidio que la Figura 10.2"
        record(f"s10v11_p{q}_fija_patronal", round(r.prima_fija_patronal), src)
        record(f"s10v11_p{q}_fija_patronal_pctlab", round(r.pct_fija_patronal, 3), src + "; % del ingreso laboral del titular")
    return a


def individual(ins, t):
    """1.5: pago total del hogar con afiliación individual (U2), hogares del ±2.5 % alrededor de la mediana."""
    sc = _esc({"U": "U2"}, "base_v12")
    m0pc, m1pc = umbrales_t(ins, sc, 2026, "pc")
    obj = ins.obj
    gm = ins.k24 * ins.G[2026]
    mpc = obj.m_pc.values * gm
    si = subsidio(mpc, m0pc, m1pc)
    priv = (1 - si) * ins.c * mpc * UMA * 365
    priv = priv + np.where(obj.trab_objetivo.values, e_anual(obj.m.values * gm * UMA * 365, D), 0.0)
    por_hogar = pd.Series(priv).groupby(obj.hh.values).sum()
    t = t.copy()
    t["pago_U2"] = t.index.map(por_hogar).fillna(0.0)
    lo, hi = wquantile(t.m26, t.factor, 0.475), wquantile(t.m26, t.factor, 0.525)
    band = t[(t.m26 >= lo) & (t.m26 <= hi)]
    pago = wquantile(band.pago_U2, band.factor, 0.5)
    pct = wquantile(band.pago_U2 / band.ing_hogar_26 * 100, band.factor, 0.5)
    src = "U2 (cada integrante paga 3.467 % del ingreso por persona del hogar, subsidio por persona), hogares con titular en ±2.5 percentiles de la mediana, 2026"
    record("s10v11_U2_pago_hogar_p50", round(pago), src + "; mediana del pago anual del hogar (pesos de 2026)")
    record("s10v11_U2_pct_hogar_p50", round(pct, 2), src + "; mediana del pago / ingreso corriente del hogar (%)")
    return pago, pct


def derechohabientes(ins):
    """1.3: costo por persona con otro conteo de derechohabientes; población con IMSS en 2030 (ENIGH × CONAPO)."""
    r = load("resultados_v12")
    b = r[(r.corrida == "base") & (r.bloque == "Total") & (r.anio == 2030)].iloc[0]
    k = DH_INFORME / DH_N13
    saldo_70 = b.saldo - b.costo * (k - 1)
    record("s10v11_costo_pp_70M_dif_pct", round((k - 1) * 100, 1), "Costo por persona del SEM con 70.69 M de DH (N13) frente a 79,178,109 (Cuadro I.4): (79.18 / 70.69 − 1) × 100")
    record("s10v11_saldo_mdp_2030_70M", round(saldo_70), "Saldo base 2030 con el costo por persona escalado por 79.18 / 70.69 (sin otra corrida), mdp de 2026")
    record("s10v11_saldo_pct_tabla5_2030", round(b.saldo / SEM_TABLA5_2030 * 100, 1), "Saldo base 2030 / ingresos del SEM de la Tabla 5 del Núcleo 13 (611.2 mil mdp) (%)")
    es = load("enigh_edad_sexo")
    es["g"] = np.minimum(es.edad, 90)
    e = es.groupby(["g", "sexo"])[["imss", "pob"]].sum()
    pop = load("conapo_pob").query("anio == 2030").copy()
    pop["g"] = np.minimum(pop.edad, 90)
    pg = pop.groupby(["g", "sexo"]).pob.sum()
    imss30 = (pg * e.imss / e.pob).sum()
    total30 = pop.pob.sum()
    cub = b.personas_cubiertas
    record("s10v11_DH_enigh_2030", round(imss30), "Tasa IMSS (inst_1) por edad y sexo de la ENIGH 2024 × CONAPO 2030")
    record("s10v11_pob_conapo_2030", round(total30), "CONAPO 2023, población total 2030")
    record("s10v11_pct_pob_imss_2030_sin", round(imss30 / total30 * 100, 1), "DH ENIGH 2030 / población CONAPO 2030 (%)")
    record("s10v11_pct_pob_imss_2030_con", round((imss30 + cub) / total30 * 100, 1), "(DH ENIGH 2030 + personas cubiertas por el esquema) / población CONAPO 2030 (%)")
    return b, saldo_70, imss30, total30


def main():
    ins = Insumos()
    tit = ins.tit
    k = ins.k24 * ins.G[2026]
    hog = _csv("concentradohogar", HH + ["ing_cor"])
    hog["ing_cor"] = _num(hog["ing_cor"]).fillna(0.0)
    t = tit.merge(hog, on=HH, how="left")
    t.index = tit.index
    t["m26"] = t.m_tit * k
    t["ing_hogar_26"] = t.ing_cor / (365 / 4) / P["uma_2024"] * k * UMA * 365
    a = cuota_fija_patronal(ins, t)
    pago, pct = individual(ins, t)
    b, s70, i30, p30 = derechohabientes(ins)
    print(a.round(2).to_string(index=False))
    print(f"U2 hogar mediano: {pago:,.0f} pesos, {pct:.2f} % del ingreso del hogar")
    print(f"saldo 2030 {b.saldo:,.0f}; con 70.69 M: {s70:,.0f}; % Tabla 5: {b.saldo / SEM_TABLA5_2030 * 100:.1f}")
    print(f"DH ENIGH 2030 {i30:,.0f} / {p30:,.0f} = {i30 / p30 * 100:.1f} %; con esquema {(i30 + b.personas_cubiertas) / p30 * 100:.1f} %")


if __name__ == "__main__":
    main()
