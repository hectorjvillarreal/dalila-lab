"""Masa salarial con tope de 25 UMA y 337 días (cotizantes del libro × distribución R1, como en la v1.2),
sensibilidad M2, derechohabientes de 65+ y 80+, e ingresos del SEM y déficit de GMP del Informe interpolados."""

from __future__ import annotations

from functools import cache

import numpy as np
import pandas as pd

from comun import CFG, MDP, P, YEARS, interpola

import common as c1          # experimento 1 (v1.2)
import proyeccion as pr1

# Insumos() registra una cifra de la v1.2 al construirse; aquí no se toca el registro del experimento 1.
pr1.record = lambda *a, **k: None

INF = CFG["horizonte"]["informe"]
ANIOS_INF = list(range(INF[0], INF[1] + 1))


class Insumos2:
    def __init__(self):
        ins = pr1.Insumos()
        self.v12 = ins
        self.uma = c1.UMA                       # UMA de dic. 2025 en pesos de 2026
        self.c = ins.c
        d = P["dias"]

        # forma R1 sin el tope superior, en el mismo orden que ins.formales (para la proporción por encima del tope)
        s = c1.load("libro_sbc_dic25")
        m = c1.load("libro_matrices").query("anio == 2025").groupby(["grupo", "sexo", "generacion", "edad"]).personas.sum()
        s = s.join(m, on=["grupo", "sexo", "generacion", "edad"]).fillna({"personas": 0})
        s["grupo_edad"] = pd.cut(s.edad, pr1.GRUPOS, right=False, labels=pr1.ETQ).astype(str)
        prom = s.groupby(["grupo_edad", "sexo"]).apply(
            lambda x: (x.sbc * x.personas).sum() / x.personas.sum(), include_groups=False).rename("sbc_prom")
        f = c1.load("r1_forma_sbc").join(prom, on=["grupo_edad", "sexo"])
        m25_sin_tope = np.maximum(f.ratio * f.sbc_prom, c1.P["sm_2025"]).values / c1.P["uma_dic2025"]

        # 2055 se extiende un año solo para el contraste de valor presente con horizonte igual al del Informe (3.3)
        pe = c1.load("libro_pob_emp").set_index("anio")
        cot55 = pe.loc[2055, ["aseg_H", "aseg_M", "timss_H", "timss_M"]].sum()
        g55 = c1.load("libro_sup_inc").set_index("anio").crec_sbc_total.loc[2055]
        sm55 = c1.load("libro_sup_fin").set_index("anio").sm_real.loc[2055]
        G = dict(ins.G)
        G[2055] = G[2054] * (1 + g55)
        self.sm = dict(ins.sm)
        self.sm[2055] = self.sm[2054] * (1 + sm55)
        wf = dict(ins.wf)
        wf[2055] = wf[2054] * cot55 / ins.cot_tot.loc[2054]
        self.cot = {t: wf[t].sum() for t in wf}
        f0 = ins.formales[0]
        mf = dict(ins.mf)
        mf[2055] = np.minimum(c1.P["tope_sbc_uma"], np.maximum(f0.m25.values * G[2055], self.sm[2055]))

        rows = []
        for t in range(2026, 2056):
            sin_tope = np.maximum(m25_sin_tope * G[t], self.sm[t])
            rows.append({"anio": t, "cotizantes": wf[t].sum(),
                         "masa_tope25": (wf[t] * mf[t]).sum() * self.uma * d / MDP,
                         "masa_sin_tope": (wf[t] * sin_tope).sum() * self.uma * d / MDP,
                         "masa_v12_denominador": ins.masa_dia[t] * d if t in ins.masa_dia else np.nan,
                         "sm_uma": self.sm[t]})
        self.masa = pd.DataFrame(rows).set_index("anio")
        self.masa["prop_sobre_tope"] = 1 - self.masa.masa_tope25 / self.masa.masa_sin_tope

        # M2: cotizantes al ritmo de los ocupados (formalidad implícita de 2025 constante), con la prueba C de la v1.2
        pc = c1.load("prueba_c_agregado").set_index("anio")
        fm = pc.formalidad_implicita
        self.m2 = (fm.loc[2025] / fm).reindex(range(2026, 2055))
        self.formalidad = fm

        # derechohabientes de 65+ y 80+: 16.6 % de 65+ (Gráfica I.31) × DH totales (Cuadro I.4), proyectados con CONAPO
        pop = c1.load("conapo_pob")
        p65 = pop[pop.edad >= 65].groupby("anio").pob.sum()
        p80 = pop[pop.edad >= 80].groupby("anio").pob.sum()
        dh65_25 = P["dh_65mas_pamf_2025"] * P["dh_total"]
        self.dh65 = dh65_25 * p65 / p65.loc[2025]
        self.dh80 = self.dh65 * p80 / p65
        # sensibilidad: la proporción de la Gráfica I.31 aplicada a su propia base (adscripciones a médico familiar)
        self.dh65_pamf = P["dh_65mas_pamf_2025"] * P["pamf_2025"] * p65 / p65.loc[2025]
        self.dh80_pamf = self.dh65_pamf * p80 / p65
        self.p65, self.p80 = p65, p80

        g = CFG["gmp_v24"]
        self.gmp_ing = interpola(g["anios"], g["ingresos"], ANIOS_INF)
        self.gmp_def = -interpola(g["anios"], g["saldo"], ANIOS_INF)       # déficit en positivo
        v = CFG["sem_v13"]
        self.sem = interpola(v["anios"], v["ingresos"], ANIOS_INF)

    def masa_esc(self, esc: str) -> pd.Series:
        b = self.masa.masa_tope25.loc[YEARS]
        return b if esc == "base" else b * self.m2.loc[YEARS]


@cache
def cargar() -> Insumos2:
    """Una sola construcción por proceso (la de la v1.2 carga la ENIGH)."""
    return Insumos2()
