"""Cotizantes del SEM por edad y sexo, 2025-2054 (modelo de cohortes del Anexo H del Núcleo 13),
prueba de coherencia C y descriptivo de rotación (verificación 7.3)."""

from __future__ import annotations

import numpy as np
import pandas as pd

from common import YEARS, load, record, save, table

AGES = np.arange(15, 101)


def cohortes():
    mat = load("libro_matrices")
    q = load("libro_salidas")
    vec = load("libro_vector_nuevos")
    pe = load("libro_pob_emp").set_index("anio")
    out, ks = [], []
    for grupo in ("aseg", "timss"):
        for sexo in ("H", "M"):
            s = (mat[(mat.anio == 2025) & (mat.grupo == grupo) & (mat.sexo == sexo)]
                 .groupby("edad").personas.sum().reindex(AGES, fill_value=0.0).values)
            qs = q[(q.grupo == grupo) & (q.sexo == sexo)].set_index("edad").q_salida.reindex(AGES).values
            v = vec[(vec.grupo == grupo) & (vec.sexo == sexo)].set_index("edad").share.reindex(AGES, fill_value=0.0).values
            out += [(2025, grupo, sexo, int(a), x) for a, x in zip(AGES, s)]
            for t in YEARS:
                surv = s * (1 - qs)
                n = np.zeros_like(s)
                n[1:] = surv[:-1]
                n[-1] += surv[-1]
                n += pe.loc[t, f"nvo_{grupo}_{sexo}"] * v
                k = pe.loc[t, f"{grupo}_{sexo}"] / n.sum()
                ks.append(k)
                s = n * k
                out += [(t, grupo, sexo, int(a), x) for a, x in zip(AGES, s)]
    df = pd.DataFrame(out, columns=["anio", "grupo", "sexo", "edad", "cotizantes"])
    save(df, "cotizantes_edad_sexo")
    record("cohortes_k_min", round(min(ks), 4), "Factor de calibración del modelo de cohortes (total del libro / total simulado)")
    record("cohortes_k_max", round(max(ks), 4), "Idem")
    return df


def prueba_c(cot):
    e = load("enigh_edad_sexo")
    e["g"] = np.minimum(e.edad, 90)
    r = e.groupby(["g", "sexo"])[["pob", "ocupados", "trab_objetivo"]].sum()
    r = (r[["ocupados", "trab_objetivo"]].div(r.pob, axis=0)).rename(columns={"ocupados": "t_ocup", "trab_objetivo": "t_inf"})
    pop = load("conapo_pob")
    pop["g"] = np.minimum(pop.edad, 90)
    pop = pop.join(r, on=["g", "sexo"])
    pop["ocupados"] = pop.pob * pop.t_ocup
    pop["informal_C1"] = pop.pob * pop.t_inf
    c = cot.groupby(["anio", "sexo", "edad"]).cotizantes.sum()
    pop = pop.join(c, on=["anio", "sexo", "edad"]).fillna({"cotizantes": 0.0})
    pop["residuo_C2"] = np.maximum(0.0, pop.ocupados - pop.cotizantes)
    pop = pop[pop.anio >= 2025]
    agg = pop.groupby("anio")[["ocupados", "cotizantes", "informal_C1", "residuo_C2"]].sum()
    agg["formalidad_implicita"] = agg.cotizantes / agg.ocupados
    # C2 como índice: igual a C1 en 2025 y sigue la dinámica del residuo ocupados − cotizantes
    agg["factor_C2"] = (agg.residuo_C2 / agg.residuo_C2.loc[2025]) / (agg.informal_C1 / agg.informal_C1.loc[2025])
    save(agg.reset_index(), "prueba_c_agregado")
    table(agg.reset_index(), "prueba_c_agregado")
    exc = []
    for t in (2030, 2040, 2054):
        for sexo in ("H", "M"):
            d = pop[(pop.anio == t) & (pop.sexo == sexo) & (pop.cotizantes > pop.ocupados)]
            exc.append({"anio": t, "sexo": sexo, "n_edades": len(d),
                        "edades": ",".join(str(a) for a in d.edad), "exceso_personas": (d.cotizantes - d.ocupados).sum()})
        a = agg.loc[t]
        record(f"C_formalidad_implicita_{t}", round(float(a.formalidad_implicita), 4), "Cotizantes (modelo de cohortes) / ocupados (CONAPO × tasa de ocupación ENIGH 2024)")
        record(f"C_factor_C2_{t}", round(float(a.factor_C2), 4), "Escala de la población objetivo en C2 respecto de C1 (índice 2025 = 1)")
    record("C_formalidad_implicita_2025", round(float(agg.loc[2025].formalidad_implicita), 4), "Idem, 2025")
    exc = pd.DataFrame(exc)
    table(exc, "prueba_c_edades_exceso")
    for _, x in exc.iterrows():
        record(f"C_exceso_{x.anio}_{x.sexo}_n_edades", int(x.n_edades), f"Edades simples con cotizantes > ocupados estimados; edades: {x.edades or 'ninguna'}")
        record(f"C_exceso_{x.anio}_{x.sexo}_personas", round(float(x.exceso_personas)), "Σ (cotizantes − ocupados) en esas edades")
    return agg


def rotacion():
    mat = load("libro_matrices")
    m = mat[mat.grupo == "aseg"].groupby(["anio", "sexo", "antiguedad", "edad"]).personas.sum()
    m24, m25 = m.loc[2024], m.loc[2025]
    rows = []
    for (sexo, ant, edad), n in m24.items():
        if ant < 50 and edad < 100:
            rows.append((sexo, ant, edad, n, m25.get((sexo, ant + 1, edad + 1), 0.0)))
    r = pd.DataFrame(rows, columns=["sexo", "antiguedad", "edad", "n2024", "n2025"])
    r["grupo_edad"] = pd.cut(r.edad, [15, 20, 25, 35, 45, 55, 65, 101], right=False,
                             labels=["15-19", "20-24", "25-34", "35-44", "45-54", "55-64", "65+"])
    t = r.groupby(["sexo", "grupo_edad"], observed=True)[["n2024", "n2025"]].sum()
    t["retencion"] = t.n2025 / t.n2024
    table(t.reset_index(), "rotacion_retencion_edad_sexo")
    for sexo in ("H", "M"):
        d = r[r.sexo == sexo]
        record(f"Ret_{sexo}_total", round(d.n2025.sum() / d.n2024.sum(), 4), "Reconstrucción propia: Mat_Aseg dic25 (edad+1, ant+1) / dic24 (edad, ant); advertencia R4")
    d = r[(r.edad >= 15) & (r.edad <= 24)]
    record("Ret_15_24", round(d.n2025.sum() / d.n2024.sum(), 4), "Idem, 15 a 24 años en 2024, ambos sexos")
    for sexo in ("H", "M"):
        d = r[(r.edad <= 24) & (r.sexo == sexo)]
        record(f"Ret_15_24_{sexo}", round(d.n2025.sum() / d.n2024.sum(), 4), "Idem, por sexo")
    a0 = mat[(mat.grupo == "aseg") & (mat.anio == 2025) & (mat.antiguedad == 0)].personas.sum()
    record("Ant0_2025", round(a0), "Mat_Aseg dic25, antigüedad 0, ambos sexos")
    # evidencia interna para R4: antigüedad 0 a edades altas y cohortes cuya antigüedad no crece
    old0 = mat[(mat.grupo == "aseg") & (mat.anio == 2025) & (mat.antiguedad == 0) & (mat.edad >= 50)].personas.sum()
    record("Ant0_2025_50mas", round(old0), "Mat_Aseg dic25, antigüedad 0 y edad ≥ 50 (indicio para R4)")


def main():
    cot = cohortes()
    prueba_c(cot)
    rotacion()


if __name__ == "__main__":
    main()
