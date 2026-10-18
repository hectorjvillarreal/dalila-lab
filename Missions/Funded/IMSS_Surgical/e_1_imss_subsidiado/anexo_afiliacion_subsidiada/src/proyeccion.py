"""Proyección 2026-2054 de los Bloques A, B y C para la malla mínima de escenarios (sección 5)."""

from __future__ import annotations

import json

import numpy as np
import pandas as pd

from common import (CFG, DERIVED, F_G, F_P, NUMBERS_JSON, P, P_STAR, UMA, YEARS, load, record, save,
                    subsidio, table)
from esquemas import crec_ingreso, sm_en_uma, umbrales

ESC = CFG["escenarios"]
GRUPOS = [15, 25, 35, 45, 55, 65, 200]
ETQ = ["15-24", "25-34", "35-44", "45-54", "55-64", "65+"]
MDP = 1e6


class Insumos:
    def __init__(self):
        reg = json.loads(NUMBERS_JSON.read_text())
        self.hb = reg["R2_h_b"]["valor"]
        self.hb_opts = {"enigh": reg["R2_h_b"]["valor"],
                        "informe_cotizantes": reg["Informe_familiares_por_cotizante"]["valor"],
                        "informe_titulares": P["hb_informe_titulares"]}
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
        # masa salarial por día cotizado; se multiplica por los días del escenario
        self.masa_dia = {t: self.cot_tot.loc[t] * sbc_prom * (1 + P["inflacion_2026"]) * self.G[t] / MDP for t in YEARS}
        self.masa = {t: v * P["dias"] for t, v in self.masa_dia.items()}
        # D2: tasa proporcional neutral en recaudación (2026), con la distribución R1 de los formales
        f, _ = self.formales
        self.wf = {t: f.share.values * self.cot_g.loc[t].reindex(list(zip(f.grupo_edad, f.sexo))).values for t in YEARS}
        self.mf = {t: np.minimum(P["tope_sbc_uma"], np.maximum(f.m25.values * self.G[t], self.sm[t])) for t in YEARS}
        self.c = P["cf_patron"] * self.wf[2026].sum() / (self.wf[2026] * self.mf[2026]).sum()

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


def _esc(ov: dict, base: str = "base") -> dict:
    return {**ESC["defaults"], **ESC[base], **ov}


def e_anual(y, d):
    """Excedente anual sobre el ingreso anual y (pesos): 1.5 % de lo que rebasa 3 UMA × d días."""
    return P["excedente"] * np.maximum(0.0, np.asarray(y, dtype=float) - P["umbral_excedente_uma"] * UMA * d)


def umbrales_t(ins, sc, t, clave):
    m0, m1 = ins.th[(clave, sc["S"])]
    if sc["umbral"] == "indexado":
        k = ins.G[t] / ins.G[2026]
        return m0 * k, m1 * k
    return m0, m1


def pago_informal(ins, sc, m, s, d):
    """Pago anual de un titular informal con ingreso diario m (UMA): (privado determinado, GF cuota fija, GF subsidio)."""
    y = m * UMA * 365
    e = e_anual(y, d)
    if sc["D"] == "D1":
        if sc["G"] == "G1":
            return (1 - s) * P_STAR + e, 0.0 * s, s * P_STAR
        return (1 - s) * F_P + e, F_G + 0.0 * s, s * F_P
    prop = ins.c * y
    if sc["G"] == "G1":
        return (1 - s) * (prop + F_G) + e, 0.0 * s, s * (prop + F_G)
    return (1 - s) * prop + e, F_G + 0.0 * s, s * prop


def pago_formal(ins, sc, m, s, d):
    """Pago anual de un formal con SBC diario m (UMA) y d días: (privado, GF cuota fija, GF subsidio/Bloque B)."""
    y = m * UMA * d
    fg = P["cf_gf"] * UMA * d
    base = P["cf_patron"] * UMA * d if sc["D"] == "D1" else ins.c * y
    return (1 - s) * base + e_anual(y, d), fg + 0.0 * s, s * base


def correr(ins: Insumos, rid: str, ov: dict, base: str = "base") -> pd.DataFrame:
    sc = _esc(ov, base)
    d_f = P["dias_cotizados"] if sc["dias"] == 337 else 365
    hb = ins.hb_opts[sc["hb"]]
    k65 = ESC["perfil"][sc["perfil"]]["razon_65"]
    r = np.where(np.arange(0, 120) >= 65, k65, 1.0)
    norm = (ins.imss_edad * r[ins.imss_edad.index]).sum() / ins.imss_edad.sum()
    c_edad = ins.c_bar * r / norm
    T = ESC["T"][sc["T"]]
    f1 = ESC["F"][sc["F"]]
    obj, tit = ins.obj, ins.tit
    rows = []
    f_meta = None
    for t in YEARS:
        m0, m1 = umbrales_t(ins, sc, t, "tit")
        m0pc, m1pc = umbrales_t(ins, sc, t, "pc")
        gm = ins.k24 * ins.G[t]
        w_o = obj.factor.values * ins.r_o[t]
        w_t = tit.factor.values * ins.r_t[t]
        if sc["C"] == "C2":
            w_o, w_t = w_o * ins.c2.loc[t], w_t * ins.c2.loc[t]
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
        s_tau = s_h if sc["U"] == "U1" else subsidio(obj.m_pc.values * gm, m0pc, m1pc)
        if sc["T"] == "T1":
            tau_o = T["tau0"] + T["tau1"] * s_tau
            mu_o = 1 + T["mu1"] * (1 - s_tau)
        else:
            tau_, mu_ = (T["tau"], T["mu"]) if sc["T"] == "T2" else (sc["tau"], sc["mu"])
            tau_o = np.full(len(obj), tau_)
            mu_o = np.full(len(obj), mu_)
        wa_o = w_o * (1 - f)
        if sc["U"] == "U1":
            if sc["T"] == "T1":
                tau_t = T["tau0"] + T["tau1"] * s_t
            else:
                tau_t = np.full(len(tit), T["tau"] if sc["T"] == "T2" else sc["tau"])
            wa_t = w_t * (1 - f) * tau_t
            priv, gfa, gfs = pago_informal(ins, sc, mt, s_t, d_f)
            A_det, A_fg, A_sub = (wa_t * priv).sum(), (wa_t * gfa).sum(), (wa_t * gfs).sum()
            A_tit = wa_t.sum()
        else:
            si = s_tau
            mpc = obj.m_pc.values * gm
            if sc["D"] == "D1":
                fijo = P_STAR / (1 + hb)
                if sc["G"] == "G1":
                    priv, gfa, gfs = (1 - si) * fijo, 0.0 * si, si * fijo
                else:
                    priv, gfa, gfs = (1 - si) * F_P / (1 + hb), F_G / (1 + hb) + 0.0 * si, si * F_P / (1 + hb)
            else:
                prop = ins.c * mpc * UMA * 365
                fg = F_G / (1 + hb)
                if sc["G"] == "G1":
                    priv, gfa, gfs = (1 - si) * (prop + fg), 0.0 * si, si * (prop + fg)
                else:
                    priv, gfa, gfs = (1 - si) * prop, fg + 0.0 * si, si * prop
            priv = priv + np.where(obj.trab_objetivo.values, e_anual(obj.m.values * gm * UMA * 365, d_f), 0.0)
            ww = wa_o * tau_o
            A_det, A_fg, A_sub = (ww * priv).sum(), (ww * gfa).sum(), (ww * gfs).sum()
            A_tit = np.nan
        A_af = (wa_o * tau_o).sum()
        A_cost = (wa_o * tau_o * mu_o * c_i).sum()

        # ---- Bloque B (formales institucionales en el tramo subsidiado) ----
        wf, mf = ins.wf[t], ins.mf[t]
        sf = subsidio(mf * d_f / 365, m0, m1)
        _, _, b_sub = pago_formal(ins, sc, mf, sf, d_f)
        B_cost = (wf * b_sub).sum()
        B_n = (wf * (sf > 0)).sum()

        # ---- Bloque C (F1 dentro del esquema) ----
        if f > 0:
            wc_t = w_t * f
            mc = np.minimum(P["tope_sbc_uma"], np.maximum(mt, ins.sm[t]))
            sc_ = subsidio(mc * d_f / 365, m0, m1)
            cpriv, cfg, csub = pago_formal(ins, sc, mc, sc_, d_f)
            C_det, C_fg, C_sub = (wc_t * cpriv).sum(), (wc_t * cfg).sum(), (wc_t * csub).sum()
            C_af = (w_o * f).sum()
            C_cost = (w_o * f * c_i).sum()
            C_tit = wc_t.sum()
        else:
            C_det = C_fg = C_sub = C_af = C_cost = C_tit = 0.0

        rho = sc["rho"]
        for bloque, af, ti, det, cob, fg, sub, co in (
                ("A", A_af, A_tit, A_det, rho * A_det, A_fg, A_sub, A_cost),
                ("B", 0.0, B_n, -B_cost, -B_cost, 0.0, B_cost, 0.0),
                ("C", C_af, C_tit, C_det, C_det, C_fg, C_sub, C_cost)):
            rows.append({"corrida": rid, "anio": t, "bloque": bloque, "personas_cubiertas": af, "titulares_o_formales": ti,
                         "pagos_determinados": det / MDP, "pagos_privados": cob / MDP, "no_cobrado": (det - cob) / MDP,
                         "GF_cuota_fija": fg / MDP, "GF_subsidio": sub / MDP, "pagos_GF": (fg + sub) / MDP, "costo": co / MDP})
    d = pd.DataFrame(rows)
    d["ingreso"] = d.pagos_privados + d.pagos_GF
    d["saldo"] = d.ingreso - d.costo
    num = ["personas_cubiertas", "titulares_o_formales", "pagos_determinados", "pagos_privados", "no_cobrado",
           "GF_cuota_fija", "GF_subsidio", "pagos_GF", "costo", "ingreso", "saldo"]
    tot = d.groupby(["corrida", "anio"], as_index=False)[num].sum()
    tot["bloque"] = "Total"
    d = pd.concat([d, tot], ignore_index=True)
    d["masa_sbc"] = d.anio.map(ins.masa_dia) * d_f
    d["ingreso_sem"] = d.anio.map(ins.sem)
    for c in ("pagos_determinados", "pagos_privados", "no_cobrado", "GF_cuota_fija", "GF_subsidio", "pagos_GF",
              "costo", "ingreso", "saldo"):
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


def bloque_c_status_quo(ins: Insumos) -> pd.DataFrame:
    """F1 sin Bloque A: los hogares que se formalizan pasan de no tener cobertura contributiva a cotizar (v1.2, 3.2)."""
    f1 = ESC["F"]["F1"]
    sc0 = _esc({}, "base_v12")
    d_f = P["dias_cotizados"]
    k65 = ESC["perfil"][sc0["perfil"]]["razon_65"]
    r = np.where(np.arange(0, 120) >= 65, k65, 1.0)
    c_edad = ins.c_bar * r / ((ins.imss_edad * r[ins.imss_edad.index]).sum() / ins.imss_edad.sum())
    rows, f_meta = [], None
    for t in YEARS:
        w_o = ins.obj.factor.values * ins.r_o[t]
        w_t = ins.tit.factor.values * ins.r_t[t]
        if t <= f1["anio_meta"]:
            f = f1["cotizantes_2030"] * (t - 2025) / (f1["anio_meta"] - 2025) / w_t.sum()
            f_meta = f
        else:
            f = f_meta
        m0, m1 = umbrales_t(ins, sc0, t, "tit")
        mc = np.minimum(P["tope_sbc_uma"], np.maximum(ins.tit.m_tit.values * ins.k24 * ins.G[t], ins.sm[t]))
        costo = (w_o * f * c_edad[ins.obj.edad.values]).sum()
        dh = (w_o * f).sum()
        cot = (w_t * f).sum()
        for cuota, D in (("D2", "D2"), ("vigente", "D1")):
            sc = {**sc0, "D": D}
            s_ = subsidio(mc * d_f / 365, m0, m1) if D == "D2" else 0.0 * mc
            priv, fg, sub = pago_formal(ins, sc, mc, s_, d_f)
            ing = (w_t * f * (priv + fg + sub)).sum()
            rows.append({"anio": t, "cuota": cuota, "cotizantes": cot, "derechohabientes": dh,
                         "dh_por_cotizante": dh / cot, "cuotas_privadas": (w_t * f * priv).sum() / MDP,
                         "GF": (w_t * f * (fg + sub)).sum() / MDP, "ingresos_SEM": ing / MDP, "costo": costo / MDP,
                         "efecto_neto_SEM": (ing - costo) / MDP})
    d = pd.DataFrame(rows)
    d["efecto_neto_pts_sbc"] = d.efecto_neto_SEM / (d.anio.map(ins.masa_dia) * d_f) * 100
    d["efecto_neto_pct_sem"] = d.efecto_neto_SEM / d.anio.map(ins.sem) * 100
    return d


def efecto_indexacion(ins: Insumos) -> pd.DataFrame:
    """Recaudación de los formales con D2 frente a la cuota fija vigente (v1.2, 1.4); fuera del saldo de informales."""
    d_f = P["dias_cotizados"]
    rows = []
    for t in YEARS:
        wf, mf = ins.wf[t], ins.mf[t]
        d2 = ins.c * UMA * d_f * (wf * mf).sum() / MDP
        sq = P["cf_patron"] * UMA * d_f * wf.sum() / MDP
        rows.append({"anio": t, "recaudacion_D2": d2, "recaudacion_vigente": sq, "diferencia": d2 - sq})
    d = pd.DataFrame(rows)
    d["diferencia_pts_sbc"] = d.diferencia / (d.anio.map(ins.masa_dia) * d_f) * 100
    d["diferencia_pct_sem"] = d.diferencia / d.anio.map(ins.sem) * 100
    return d


def no_arbitraje_d2(ins: Insumos) -> dict:
    m = np.round(np.arange(0, 25.0001, 0.1), 1)
    d_f = P["dias_cotizados"]
    n_eq = n_ge = n_b = 0
    for s_id in ESC["S"]:
        for G in ("G1", "G2"):
            for t in (2026, 2054):
                sc = _esc({"S": s_id, "G": G}, "base_v12")
                m0, m1 = umbrales_t(ins, sc, t, "tit")
                s = subsidio(m, m0, m1)
                pi_i, _, _ = pago_informal(ins, sc, m, s, d_f)
                w = m * 365 / d_f                      # mismo ingreso anual
                pi_f, _, b = pago_formal(ins, sc, w, s, d_f)
                if G == "G2":
                    n_eq += int((abs(pi_i - pi_f) > 1).sum())
                n_ge += int((pi_i < pi_f - 1e-6).sum())
                n_b += int((b > s * ins.c * w * UMA * d_f + 1e-6).sum())
    return {"6.3.1 igualdad ±1 peso en G2 (casos fuera)": n_eq, "6.3.2 π_I ≥ π_F (violaciones)": n_ge,
            "6.3.3 subsidio B ≤ s·c·w·d (violaciones)": n_b}


def verificaciones_v12(ins, res, v11, ind):
    chk = {}
    money = ["pagos_determinados", "pagos_privados", "pagos_GF", "costo", "saldo"]
    a = res[res.corrida == "regresion_v11"].set_index(["anio", "bloque"])
    b = v11[v11.corrida == "base"].set_index(["anio", "bloque"])
    cols = ["pagos_privados", "pagos_GF", "costo", "saldo", "personas_cubiertas"]
    chk["6.1 regresión v1.1 (máx. desviación, mdp o personas)"] = float((a[cols] - b[cols]).abs().max().max())
    r0 = ind.set_index("anio").loc[2026]
    chk["6.2 neutralidad de c en 2026 (diferencia %)"] = float(r0.diferencia / r0.recaudacion_vigente * 100)
    chk.update(no_arbitraje_d2(ins))
    d = res[res.bloque != "Total"]
    chk["6.4 determinados = cobrados + no cobrados (máx. desviación)"] = float(abs(d.pagos_determinados - d.pagos_privados - d.no_cobrado).max())
    chk["6.4 ingreso − costo = saldo (máx. desviación)"] = float(abs(d.ingreso - d.costo - d.saldo).max())
    s = d.groupby(["corrida", "anio"])[money].sum()
    t = res[res.bloque == "Total"].set_index(["corrida", "anio"])[money]
    chk["6.4 A + B + C = total (máx. desviación)"] = float(abs(s - t).max().max())
    T = res[res.bloque == "Total"].set_index(["corrida", "anio"])
    p = lambda r, c: T.loc[r][c]  # noqa: E731
    chk["6.5 τ mayor ⇒ más cobertura (años que fallan)"] = int(((p("tau30", "personas_cubiertas") >= p("base", "personas_cubiertas")) |
        (p("base", "personas_cubiertas") >= p("tau70", "personas_cubiertas")) | (p("tau70", "personas_cubiertas") >= p("tau90", "personas_cubiertas"))).sum())
    chk["6.5 ρ menor ⇒ peor saldo (años que fallan)"] = int(((p("rho50", "saldo") >= p("base", "saldo")) | (p("base", "saldo") >= p("rho100", "saldo"))).sum())
    chk["6.5 μ mayor ⇒ más costo (años que fallan)"] = int(((p("mu100", "costo") >= p("base", "costo")) | (p("base", "costo") >= p("mu130", "costo"))).sum())
    chk["7.7 π_m mayor ⇒ costo mayor (años que fallan)"] = int(((p("pim1", "costo") < p("base", "costo") - 1e-6) | (p("pim2", "costo") < p("pim1", "costo") - 1e-6)).sum())
    fis = res[res.bloque.isin(["A", "B"])].groupby(["corrida", "anio"]).pagos_GF.sum()
    chk["7.7 S3 > S1 > S2 en costo fiscal (años que fallan)"] = int(((fis.loc["S3"] <= fis.loc["base"]) | (fis.loc["base"] <= fis.loc["S2"])).sum())
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

    # ---- v1.2 ----
    record("v12_c", round(ins.c, 5), "D2: 0.2040 × Σ formales / Σ (formales × SBC en UMA), 2026, distribución R1 × cotizantes del libro")
    out = [correr(ins, r["id"], {k: v for k, v in r.items() if k != "id"}, "base_v12") for r in CFG["malla_v12"]]
    r12 = pd.concat(out, ignore_index=True)
    save(r12, "resultados_v12", csv=True)
    ind = efecto_indexacion(ins)
    table(ind, "efecto_indexacion")
    save(ind, "efecto_indexacion")
    bc = bloque_c_status_quo(ins)
    table(bc, "bloque_C_vs_status_quo")
    save(bc, "bloque_C_vs_status_quo")
    chk = verificaciones_v12(ins, r12, res, ind)
    for i, (k, v) in enumerate(chk.items()):
        record(f"chk12_{i:02d}_{k.split()[0]}", v, k)
    (DERIVED / "checks_v12.json").write_text(json.dumps(chk, ensure_ascii=False, indent=1))
    print(json.dumps(chk, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
