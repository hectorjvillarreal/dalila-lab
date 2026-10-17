"""Proyección 2026-2054 de los Bloques A, B y C para la malla mínima de escenarios (sección 5)."""

from __future__ import annotations

import json

import numpy as np
import pandas as pd

from common import (CFG, DERIVED, F_G, F_P, NUMBERS_JSON, P, P_STAR, YEARS, excedente, load, record,
                    save, subsidio, table)
from esquemas import crec_ingreso, sm_en_uma, umbrales

ESC = CFG["escenarios"]
GRUPOS = [15, 25, 35, 45, 55, 65, 200]
ETQ = ["15-24", "25-34", "35-44", "45-54", "55-64", "65+"]
MDP = 1e6


class Insumos:
    def __init__(self):
        reg = json.loads(NUMBERS_JSON.read_text())
        self.hb = reg["R2_h_b"]["valor"]
        self.hb_informe = reg["Informe_familiares_por_cotizante"]["valor"]
        self.th, _ = umbrales()
        self.G = crec_ingreso()
        self.k24 = 1 + P["sbc_crec_uma_2025"]
        self.sm = sm_en_uma()
        self.c2 = load("prueba_c_agregado").set_index("anio").factor_C2

        per = load("enigh_personas")
        es = load("enigh_edad_sexo")
        es["g"] = np.minimum(es.edad, 90)
        base = es.groupby(["g", "sexo"]).pob.sum()
        pop = load("conapo_pob")
        pop["g"] = np.minimum(pop.edad, 90)
        cp = pop.groupby(["anio", "g", "sexo"]).pob.sum()
        self.ratio = {t: (cp.loc[t] / base) for t in YEARS}

        obj = per[per.persona_objetivo].copy()
        obj["g"] = np.minimum(obj.edad, 90)
        self.obj = obj.reset_index(drop=True)
        tit = per[per.titular].copy()
        tit["g"] = np.minimum(tit.edad, 90)
        self.tit = tit.reset_index(drop=True)
        # índice de hogar para enlazar personas con su titular
        key = ["folioviv", "foliohog"]
        self.obj["hh"] = self.obj.set_index(key).index.map({k: i for i, k in enumerate(self.tit.set_index(key).index)})
        io = pd.MultiIndex.from_arrays([self.obj.g, self.obj.sexo])
        it = pd.MultiIndex.from_arrays([self.tit.g, self.tit.sexo])
        self.r_o = {t: self.ratio[t].reindex(io).values for t in YEARS}
        self.r_t = {t: self.ratio[t].reindex(it).values for t in YEARS}

        # costo per cápita: ancla de nivel (Cuadro V.13 / Cuadro I.4) y perfil por edad sobre la estructura IMSS de la ENIGH
        self.c_bar = P["especie_sem_2026"] * MDP / P["dh_total_informe"]
        self.imss_edad = es.groupby("edad").imss.sum()

        self.sem = (load("libro_ingresos").query("seguro in ['SEM-A', 'SEM-GMP']").groupby("anio").mdp2026.sum())
        cot = load("cotizantes_edad_sexo")
        self.cot_tot = cot.groupby("anio").cotizantes.sum()
        cot["grupo_edad"] = pd.cut(cot.edad, GRUPOS, right=False, labels=ETQ).astype(str)
        self.cot_g = cot.groupby(["anio", "grupo_edad", "sexo"]).cotizantes.sum()
        self.formales = self._formales()
        sbc_prom = self._sbc_promedio()
        self.masa = {t: self.cot_tot.loc[t] * sbc_prom * (1 + P["inflacion_2026"]) * self.G[t] * P["dias"] / MDP
                     for t in YEARS}

    def _sbc_promedio(self):
        s = load("libro_sbc_dic25")
        m = load("libro_matrices").query("anio == 2025").groupby(["grupo", "sexo", "generacion", "edad"]).personas.sum()
        s = s.join(m, on=["grupo", "sexo", "generacion", "edad"]).fillna({"personas": 0})
        a = s[s.grupo == "aseg"]
        prom = (a.sbc * a.personas).sum() / a.personas.sum()
        record("SBC_ponderado_libro_calc", round(prom, 2), "Sal SEM-Emp_dic25 × Mat_Aseg SEM_dic25 (asegurados; generaciones en transición y actual)")
        return prom

    def _formales(self):
        """Respaldo R1: forma ENIGH reescalada al SBC promedio del libro por grupo de edad y sexo."""
        s = load("libro_sbc_dic25")
        m = load("libro_matrices").query("anio == 2025").groupby(["grupo", "sexo", "generacion", "edad"]).personas.sum()
        s = s.join(m, on=["grupo", "sexo", "generacion", "edad"]).fillna({"personas": 0})
        s["grupo_edad"] = pd.cut(s.edad, GRUPOS, right=False, labels=ETQ).astype(str)
        prom = s.groupby(["grupo_edad", "sexo"]).apply(
            lambda d: (d.sbc * d.personas).sum() / d.personas.sum(), include_groups=False).rename("sbc_prom")
        f = load("r1_forma_sbc").join(prom, on=["grupo_edad", "sexo"])
        f["share"] = f.factor / f.groupby(["grupo_edad", "sexo"]).factor.transform("sum")
        sbc = f.ratio * f.sbc_prom
        f["m25"] = np.clip(sbc, P["sm_2025"], P["tope_sbc_uma"] * P["uma_dic2025"]) / P["uma_dic2025"]
        bajo = (f.share * (sbc < P["sm_2025"])).groupby([f.grupo_edad, f.sexo]).sum()
        return f[["grupo_edad", "sexo", "share", "m25"]], bajo


def correr(ins: Insumos, rid: str, ov: dict) -> pd.DataFrame:
    sc = {**ESC["base"], **ov}
    hb = ins.hb_informe if sc.get("hb") == "informe" else ins.hb
    m0, m1 = ins.th[("tit", sc["S"])]
    m0pc, m1pc = ins.th[("pc", sc["S"])]
    k65 = ESC["perfil"][sc["perfil"]]["razon_65"]
    r = np.where(np.arange(0, 120) >= 65, k65, 1.0)
    norm = (ins.imss_edad * r[ins.imss_edad.index]).sum() / ins.imss_edad.sum()
    c_edad = ins.c_bar * r / norm
    T = ESC["T"][sc["T"]]
    f1 = ESC["F"][sc["F"]]
    obj, tit = ins.obj, ins.tit
    formales, _ = ins.formales
    rows = []
    f_meta = None
    for t in YEARS:
        gm = ins.k24 * ins.G[t]
        w_o = obj.factor.values * ins.r_o[t]
        w_t = tit.factor.values * ins.r_t[t]
        if sc["C"] == "C2":
            w_o, w_t = w_o * ins.c2.loc[t], w_t * ins.c2.loc[t]
        # Bloque C: fracción f de los hogares objetivo pasa a cotizar
        if f1["cotizantes_2030"] > 0:
            if t <= f1["anio_meta"]:
                f = f1["cotizantes_2030"] * (t - 2025) / (f1["anio_meta"] - 2025) / w_t.sum()
                f_meta = f
            else:
                f = f_meta
        else:
            f = 0.0
        crec = (1 + sc["pi_m"]) ** (t - 2026)
        c_i = c_edad[obj.edad.values] * crec
        mt = tit.m_tit.values * gm
        s_t = subsidio(mt, m0, m1)
        s_h = s_t[obj.hh.values]

        # ---- Bloque A ----
        if sc["U"] == "U1":
            s_tau = s_h
        else:
            s_tau = subsidio(obj.m_pc.values * gm, m0pc, m1pc)
        if sc["T"] == "T1":
            tau_o = T["tau0"] + T["tau1"] * s_tau
            mu_o = 1 + T["mu1"] * (1 - s_tau)
        else:
            tau_o = np.full(len(obj), T["tau"])
            mu_o = np.full(len(obj), T["mu"])
        wa_o = w_o * (1 - f)
        if sc["U"] == "U1":
            tau_t = T["tau0"] + T["tau1"] * s_t if sc["T"] == "T1" else np.full(len(tit), T["tau"])
            wa_t = w_t * (1 - f) * tau_t
            e = excedente(mt)
            if sc["G"] == "G1":
                priv, gf = (1 - s_t) * P_STAR + e, s_t * P_STAR
            else:
                priv, gf = (1 - s_t) * F_P + e, F_G + s_t * F_P
            A_priv, A_gf = (wa_t * priv).sum(), (wa_t * gf).sum()
            A_tit = wa_t.sum()
        else:
            si = s_tau
            fijo = P_STAR / (1 + hb)
            if sc["G"] == "G1":
                priv, gf = (1 - si) * fijo, si * fijo
            else:
                priv, gf = (1 - si) * F_P / (1 + hb), (F_G + si * F_P) / (1 + hb)
            priv = priv + np.where(obj.trab_objetivo.values, excedente(obj.m.values * gm), 0.0)
            A_priv, A_gf = (wa_o * tau_o * priv).sum(), (wa_o * tau_o * gf).sum()
            A_tit = np.nan
        A_af = (wa_o * tau_o).sum()
        A_cost = (wa_o * tau_o * mu_o * c_i).sum()

        # ---- Bloque B (formales institucionales con m < m1) ----
        cg = ins.cot_g.loc[t]
        wf = formales.share.values * cg.reindex(list(zip(formales.grupo_edad, formales.sexo))).values
        mf = np.minimum(P["tope_sbc_uma"], np.maximum(formales.m25.values * ins.G[t], ins.sm[t]))
        sf = subsidio(mf, m0, m1)
        B_cost = (wf * sf * F_P).sum()
        B_n = (wf * (sf > 0)).sum()

        # ---- Bloque C ----
        if f > 0:
            wc_t = w_t * f
            mc = np.minimum(P["tope_sbc_uma"], np.maximum(mt, ins.sm[t]))
            sc_ = subsidio(mc, m0, m1)
            C_priv = (wc_t * ((1 - sc_) * F_P + excedente(mc))).sum()
            C_gf = (wc_t * (F_G + sc_ * F_P)).sum()
            C_af = (w_o * f).sum()
            C_cost = (w_o * f * c_i).sum()
            C_tit = wc_t.sum()
        else:
            C_priv = C_gf = C_af = C_cost = C_tit = 0.0

        for bloque, af, ti, pr, g, co in (("A", A_af, A_tit, A_priv, A_gf, A_cost),
                                          ("B", 0.0, B_n, -B_cost, B_cost, 0.0),
                                          ("C", C_af, C_tit, C_priv, C_gf, C_cost)):
            rows.append({"corrida": rid, "anio": t, "bloque": bloque, "personas_cubiertas": af, "titulares_o_formales": ti,
                         "pagos_privados": pr / MDP, "pagos_GF": g / MDP, "costo": co / MDP})
    d = pd.DataFrame(rows)
    d["ingreso"] = d.pagos_privados + d.pagos_GF
    d["saldo"] = d.ingreso - d.costo
    tot = d.groupby(["corrida", "anio"], as_index=False)[
        ["personas_cubiertas", "titulares_o_formales", "pagos_privados", "pagos_GF", "costo", "ingreso", "saldo"]].sum()
    tot["bloque"] = "Total"
    d = pd.concat([d, tot], ignore_index=True)
    d["masa_sbc"] = d.anio.map(ins.masa)
    d["ingreso_sem"] = d.anio.map(ins.sem)
    for c in ("pagos_privados", "pagos_GF", "costo", "ingreso", "saldo"):
        d[f"{c}_pts_sbc"] = d[c] / d.masa_sbc * 100
        d[f"{c}_pct_sem"] = d[c] / d.ingreso_sem * 100
        d[f"{c}_pct_pib_2026"] = np.where(d.anio == 2026, d[c] / P["pib_2026"] * 100, np.nan)
    return d


def verificaciones(res: pd.DataFrame) -> dict:
    chk = {}
    eps = 1e-6
    d = res[res.bloque != "Total"]
    chk["7.5 ingreso − costo = saldo (máx. desviación, mdp)"] = float(abs(d.ingreso - d.costo - d.saldo).max())
    s = d.groupby(["corrida", "anio"])[["ingreso", "costo", "saldo", "pagos_GF"]].sum()
    t = res[res.bloque == "Total"].set_index(["corrida", "anio"])[["ingreso", "costo", "saldo", "pagos_GF"]]
    chk["7.5 A + B + C = total (máx. desviación, mdp)"] = float(abs(s - t).max().max())
    a = res[res.bloque == "A"].set_index(["corrida", "anio"])
    pim = a.loc["base"].costo, a.loc["pim1"].costo, a.loc["pim2"].costo
    chk["7.7 π_m mayor ⇒ costo mayor (años que fallan)"] = int(((pim[1] < pim[0] - eps) | (pim[2] < pim[1] - eps)).sum())
    fis = res[res.bloque.isin(["A", "B"])].groupby(["corrida", "anio"]).pagos_GF.sum()
    chk["7.7 S3 > S1 > S2 en costo fiscal (años que fallan)"] = int(((fis.loc["S3"] <= fis.loc["base"]) | (fis.loc["base"] <= fis.loc["S2"])).sum())
    s_grid = np.linspace(0, 1, 101)
    tau = ESC["T"]["T1"]["tau0"] + ESC["T"]["T1"]["tau1"] * s_grid
    chk["7.7 T1: mayor subsidio ⇒ mayor adopción (violaciones en la malla de s)"] = int((np.diff(tau) <= 0).sum())
    chk["7.8 años 2055 en las salidas"] = int((res.anio >= 2055).sum())
    return chk


def main():
    ins = Insumos()
    out = [correr(ins, r["id"], {k: v for k, v in r.items() if k != "id"}) for r in CFG["malla"]]
    res = pd.concat(out, ignore_index=True)
    save(res, "resultados_malla", csv=True)
    chk = verificaciones(res)
    for i, (k, v) in enumerate(chk.items()):
        record(f"chk_{k.split()[0]}_{i}", v, k)
    (DERIVED / "checks_7_5_7_8.json").write_text(json.dumps(chk, ensure_ascii=False, indent=1))
    print(json.dumps(chk, ensure_ascii=False, indent=1))
    _, bajo = ins.formales
    record("R1_share_bajo_SM", round(float(bajo.mean()), 4), "Proporción media (grupos edad×sexo) de la forma ENIGH reescalada que queda bajo el SM 2025 y se trunca")
    record("costo_per_capita_DH_2026", round(ins.c_bar, 2), "Especie SEM 2026 (Cuadro V.13) / DH total (Cuadro I.4), pesos de 2026")


if __name__ == "__main__":
    main()
