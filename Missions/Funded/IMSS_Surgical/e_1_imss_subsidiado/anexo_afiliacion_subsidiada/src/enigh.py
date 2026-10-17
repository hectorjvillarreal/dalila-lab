"""ENIGH 2024: población objetivo del Bloque A, forma del ingreso formal (R1),
beneficiarios por titular (R2), tasas de ocupación (prueba C) y verificaciones 7.4."""

from __future__ import annotations

import numpy as np
import pandas as pd

from common import P, inp, record, save, table, wquantile

KEYS = ["folioviv", "foliohog", "numren"]
HH = ["folioviv", "foliohog"]
CLAVES_TRABAJO = [f"P{n:03d}" for n in range(1, 23) if n not in (10, 17)]
CLAVES_SUBOR_PRINCIPAL = [f"P{n:03d}" for n in range(1, 10)]
DIAS_TRIM = 365 / 4
GRUPOS = [15, 25, 35, 45, 55, 65, 200]
ETQ = ["15-24", "25-34", "35-44", "45-54", "55-64", "65+"]


def _csv(tabla, usecols=None):
    d = inp("enigh_bundle") / f"conjunto_de_datos_{tabla}_enigh2024_ns" / "conjunto_de_datos"
    return pd.read_csv(d / f"conjunto_de_datos_{tabla}_enigh2024_ns.csv", usecols=usecols,
                       dtype=str, keep_default_na=False)


def _num(s):
    return pd.to_numeric(s.replace({"": np.nan, " ": np.nan}), errors="coerce")


def personas():
    pob = _csv("poblacion", KEYS + ["parentesco", "sexo", "edad"] + [f"inst_{k}" for k in range(1, 10)]
               + [f"inscr_{k}" for k in range(1, 9)])
    pob["edad"] = _num(pob.edad).astype(int)
    pob["sexo"] = pob.sexo.map({"1": "H", "2": "M"})
    has = lambda c, v: pob[c].str.strip() == v  # noqa: E731
    pob["imss"] = has("inst_1", "1")
    # cobertura contributiva: IMSS, ISSSTE, ISSSTE estatal, Pemex/Defensa/Marina (cualquier motivo de afiliación)
    pob["contrib"] = has("inst_1", "1") | has("inst_2", "2") | has("inst_3", "3") | has("inst_4", "4")
    pob["imss_prest"] = pob.imss & has("inscr_1", "1")
    pob["imss_benef"] = pob.imss & has("inscr_3", "3") & ~has("inscr_1", "1")

    tra = _csv("trabajos", KEYS + ["id_trabajo", "subor"])
    ocup = tra.drop_duplicates(KEYS)[KEYS].assign(ocupado=True)
    princ = tra[tra.id_trabajo == "1"][KEYS + ["subor"]]
    pob = pob.merge(ocup, on=KEYS, how="left").merge(princ, on=KEYS, how="left")
    pob["ocupado"] = pob.ocupado.fillna(False).astype(bool)
    pob["asalariado"] = pob.subor == "1"

    ing = _csv("ingresos", KEYS + ["clave", "ing_tri"])
    ing["ing_tri"] = _num(ing.ing_tri).fillna(0.0)
    lab = ing[ing.clave.isin(CLAVES_TRABAJO)].groupby(KEYS).ing_tri.sum().rename("ing_trab_tri")
    sub = ing[ing.clave.isin(CLAVES_SUBOR_PRINCIPAL)].groupby(KEYS).ing_tri.sum().rename("ing_sub_tri")
    neg = []
    for t in ("noagro", "agro"):
        n = _csv(t, KEYS + ["ing_tri"])
        n["ing_tri"] = _num(n.ing_tri).fillna(0.0)
        neg.append(n.groupby(KEYS).ing_tri.sum())
    neg = pd.concat(neg).groupby(level=[0, 1, 2]).sum().rename("ing_neg_tri")
    pob = pob.join(lab, on=KEYS).join(sub, on=KEYS).join(neg, on=KEYS)
    for c in ("ing_trab_tri", "ing_sub_tri", "ing_neg_tri"):
        pob[c] = pob[c].fillna(0.0)
    pob["ing_lab_d"] = (pob.ing_trab_tri + pob.ing_neg_tri) / DIAS_TRIM
    pob["m"] = pob.ing_lab_d / P["uma_2024"]

    hog = _csv("concentradohogar", HH + ["factor", "upm", "est_dis", "ing_cor", "ingtrab", "tot_integ"])
    for c in ("factor", "ing_cor", "ingtrab", "tot_integ"):
        hog[c] = _num(hog[c])
    # deciles de hogares por ingreso corriente total, ponderados (criterio INEGI)
    o = hog.sort_values("ing_cor")
    cw = o.factor.cumsum() / o.factor.sum()
    hog.loc[o.index, "decil"] = np.minimum(10, np.floor(cw.values * 10 - 1e-12) + 1).astype(int)
    hog["m_pc"] = hog.ing_cor / hog.tot_integ / DIAS_TRIM / P["uma_2024"]
    pob = pob.merge(hog[HH + ["factor", "upm", "est_dis", "decil", "m_pc"]], on=HH, how="left")
    return pob, hog


def poblacion_objetivo(pob):
    pob["trab_objetivo"] = pob.ocupado & ~pob.contrib & (pob.edad >= P["edad_min_titular"])
    hh_obj = pob[pob.trab_objetivo].groupby(HH).size().rename("n_trab_obj")
    pob = pob.join(hh_obj, on=HH)
    pob["hogar_objetivo"] = pob.n_trab_obj.notna()
    pob["persona_objetivo"] = pob.hogar_objetivo & ~pob.contrib
    # titular: perceptor principal informal del hogar (mayor ingreso laboral; desempate por numren)
    tw = pob[pob.trab_objetivo].sort_values(HH + ["ing_lab_d", "numren"], ascending=[True, True, False, True])
    tit = tw.drop_duplicates(HH)[KEYS + ["m", "edad", "sexo"]]
    tit = tit.rename(columns={"m": "m_tit", "edad": "edad_tit", "sexo": "sexo_tit"})
    pob = pob.merge(tit.drop(columns="numren"), on=HH, how="left")
    pob["titular"] = pob.set_index(KEYS).index.isin(tit.set_index(KEYS).index)
    return pob


def verificaciones(pob, hog):
    w = pob.factor
    tot = w.sum()
    record("ENIGH_pob_total", round(tot), "ENIGH 2024, poblacion × factor (concentradohogar)")
    record("ENIGH_pob_IMSS", round(w[pob.imss].sum()), "ENIGH 2024, poblacion inst_1 = 1")
    record("ENIGH_pob_contrib", round(w[pob.contrib].sum()), "ENIGH 2024, poblacion inst_1..inst_4")
    record("ENIGH_ocupados", round(w[pob.ocupado].sum()), "ENIGH 2024, personas con registro en trabajos")
    record("ENIGH_ocupados_sin_contrib", round(w[pob.ocupado & ~pob.contrib].sum()), "ENIGH 2024, ocupados sin inst_1..inst_4")
    record("ENIGH_ingtrab_personas_vs_hogar", round(float((pob.ing_lab_d * w).sum() * DIAS_TRIM / (hog.ingtrab * hog.factor).sum()), 4),
           "Cociente Σ ingreso laboral por persona (P001-P022 sin P010/P017 + negocios) / Σ ingtrab de concentradohogar")
    oc = pob[pob.ocupado]
    dec = oc.groupby("decil").apply(lambda d: (d.factor * ~d.contrib).sum() / d.factor.sum(), include_groups=False)
    out = dec.rename("prop_ocupados_sin_contrib").reset_index()
    table(out, "enigh_informalidad_por_decil")
    for _, r in out.iterrows():
        record(f"ENIGH_informal_decil_{int(r.decil)}", round(float(r.prop_ocupados_sin_contrib), 4),
               "ENIGH 2024; ocupados sin cobertura contributiva / ocupados, deciles de hogares por ing_cor")


def objetivo_tablas(pob):
    po = pob[pob.persona_objetivo]
    tit = pob[pob.titular]
    w = po.factor
    record("A_personas_objetivo_2024", round(w.sum()), "ENIGH 2024; miembros sin cobertura contributiva de hogares con ≥1 ocupado sin cobertura")
    record("A_titulares_2024", round(tit.factor.sum()), "ENIGH 2024; perceptor principal ocupado sin cobertura por hogar objetivo")
    record("A_personas_por_titular", round(w.sum() / tit.factor.sum(), 3), "Cociente de las dos cifras anteriores")
    record("A_trab_objetivo_2024", round(pob.factor[pob.trab_objetivo].sum()), "ENIGH 2024; ocupados de 15+ sin cobertura contributiva")
    pct = {}
    for q in (10, 20, 30, 40, 50, 70):
        pct[q] = wquantile(tit.m_tit, tit.factor, q / 100)
        record(f"m_tit_p{q}", round(pct[q], 4), "ENIGH 2024; percentil ponderado del ingreso laboral diario del titular / UMA 2024")
    pc = {}
    for q in (10, 20, 30, 40, 50, 70):
        pc[q] = wquantile(po.m_pc, po.factor, q / 100)
        record(f"m_pc_p{q}", round(pc[q], 4), "ENIGH 2024; percentil ponderado del ingreso corriente per cápita (personas objetivo) / UMA 2024")
    bins = np.r_[np.arange(0, 5, 0.5), 25, np.inf]
    po = po.assign(tramo_m=pd.cut(po.m_tit, bins, right=False).astype(str),
                   grupo_edad=pd.cut(po.edad, [0, 15, 25, 35, 45, 55, 65, 200], right=False,
                                     labels=["0-14"] + ETQ).astype(str))
    t = po.groupby(["grupo_edad", "sexo", "tramo_m"], observed=True).factor.sum().rename("personas").reset_index()
    table(t, "A_poblacion_objetivo_edad_sexo_tramo")
    return pct, pc


def r2_beneficiarios(pob):
    hh = pob.groupby(HH).agg(n_tit=("imss_prest", "sum"), n_ben=("imss_benef", "sum"), factor=("factor", "first"))
    hh = hh[hh.n_tit > 0]
    hb = (hh.n_ben * hh.factor).sum() / (hh.n_tit * hh.factor).sum()
    record("R2_h_b", round(hb, 4), "ENIGH 2024; Σ beneficiarios IMSS por familiar en el hogar (inscr_3, sin inscr_1) / Σ titulares IMSS por prestación (inscr_1), hogares con titular")
    t = pob[pob.imss_prest].join(hh[["n_tit", "n_ben"]], on=HH)
    t["ben_por_tit"] = t.n_ben / t.n_tit
    t["grupo_edad"] = pd.cut(t.edad, GRUPOS, right=False, labels=ETQ)
    g = t.groupby(["grupo_edad", "sexo"], observed=True).apply(
        lambda d: (d.ben_por_tit * d.factor).sum() / d.factor.sum(), include_groups=False).rename("h_b").reset_index()
    table(g, "R2_beneficiarios_por_titular")
    dh_por_cot = P["dh_total_informe"] / 22352586
    record("Informe_DH_por_cotizante", round(dh_por_cot, 4), "Informe Cuadro I.4 (79,178,109) / cotizantes dic. 2025 del libro (22,352,586)")
    record("Informe_familiares_por_cotizante", round(40980786 / 22352586, 4), "Informe Cuadro I.4 familiares (40,980,786) / cotizantes del libro")
    return hb


def r1_forma_sbc(pob):
    a = pob[pob.imss_prest & pob.asalariado & (pob.ing_sub_tri > 0) & (pob.edad >= 15)].copy()
    a["inc"] = a.ing_sub_tri / DIAS_TRIM
    a["grupo_edad"] = pd.cut(a.edad, GRUPOS, right=False, labels=ETQ).astype(str)
    a["ratio"] = a.inc / a.groupby(["grupo_edad", "sexo"]).inc.transform(
        lambda s: np.average(s, weights=a.loc[s.index, "factor"]))
    record("R1_n_obs", int(len(a)), "ENIGH 2024; asalariados con IMSS por prestación e ingreso subordinado principal > 0 (P001-P009)")
    save(a[["grupo_edad", "sexo", "factor", "ratio"]].reset_index(drop=True), "r1_forma_sbc")


def ocupacion(pob):
    g = pob.groupby(["edad", "sexo"]).apply(lambda d: pd.Series({
        "pob": d.factor.sum(),
        "ocupados": d.factor[d.ocupado].sum(),
        "trab_objetivo": d.factor[d.trab_objetivo].sum(),
        "imss": d.factor[d.imss].sum()}), include_groups=False).reset_index()
    save(g, "enigh_edad_sexo")


def main():
    pob, hog = personas()
    pob = poblacion_objetivo(pob)
    verificaciones(pob, hog)
    objetivo_tablas(pob)
    r2_beneficiarios(pob)
    r1_forma_sbc(pob)
    ocupacion(pob)
    cols = ["folioviv", "foliohog", "numren", "factor", "upm", "est_dis", "edad", "sexo", "imss", "contrib",
            "ocupado", "trab_objetivo", "persona_objetivo", "titular", "m", "m_tit", "edad_tit", "sexo_tit",
            "m_pc", "decil"]
    save(pob[cols], "enigh_personas")


if __name__ == "__main__":
    main()
