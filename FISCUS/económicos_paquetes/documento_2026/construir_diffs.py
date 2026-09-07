#!/usr/bin/env python3
"""Diffs por clave, proyecto 2025 -> proyecto 2026. Se anticipan, no se descubren.

Regla de la casa: toda agrupación por entidad presupuestaria se hace por CLAVE,
nunca por nombre. Un código que aparece, desaparece o se renumera produce una
variación contable que no es presupuestal.
"""
import sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fiscus26 import analitico, clave, cod_pp, real, DEFLACTOR

SAL = Path(__file__).resolve().parent / "datos"
SAL.mkdir(exist_ok=True)


def marco(anio: int) -> pd.DataFrame:
    """Une Gobierno Federal y entidades en un solo marco por clave."""
    gf = analitico(anio, "gf-ramo-programa-ur-objeto")
    ef = analitico(anio, "entidades-ramo-programa-ur-objeto")
    gf = gf.assign(RAMO_K=clave(gf["RAMO"]), PP_K=cod_pp(gf),
                   UR_K=gf["UR"].astype(str).str.strip().str.split().str[0],
                   NOMBRE_PP=gf["PP"].astype(str).str.strip(),
                   NOMBRE_UR=gf["UR"].astype(str).str.strip(),
                   NOMBRE_RAMO=gf["RAMO"].astype(str).str.strip(), AMBITO="GF")
    ef = ef.assign(RAMO_K=ef["ENTIDAD"].astype(str).str.strip().str.split().str[0],
                   PP_K=ef["PP"].astype(str).str.strip().str[:4],
                   UR_K=ef["ENTIDAD"].astype(str).str.strip().str.split().str[0],
                   NOMBRE_PP=ef["PP"].astype(str).str.strip(),
                   NOMBRE_UR=ef["ENTIDAD"].astype(str).str.strip(),
                   NOMBRE_RAMO=ef["ENTIDAD"].astype(str).str.strip(), AMBITO="EFE")
    cols = ["RAMO_K", "PP_K", "UR_K", "NOMBRE_RAMO", "NOMBRE_PP", "NOMBRE_UR", "AMBITO", "MDP"]
    return pd.concat([gf[cols], ef[cols]], ignore_index=True)


def diff(a: pd.DataFrame, b: pd.DataFrame, llaves: list[str], nombre: str) -> pd.DataFrame:
    ga = a.groupby(llaves, as_index=False)["MDP"].sum().rename(columns={"MDP": "mdp_2025"})
    gb = b.groupby(llaves, as_index=False)["MDP"].sum().rename(columns={"MDP": "mdp_2026"})
    m = ga.merge(gb, on=llaves, how="outer").fillna({"mdp_2025": 0.0, "mdp_2026": 0.0})
    m["dif_nominal"] = m.mdp_2026 - m.mdp_2025
    m["dif_real"] = m.mdp_2026 - m.mdp_2025 * DEFLACTOR
    m["var_real_pct"] = (m.mdp_2026 / (m.mdp_2025 * DEFLACTOR) - 1) * 100
    m["estado"] = "continúa"
    m.loc[m.mdp_2025 == 0, "estado"] = "aparece"
    m.loc[m.mdp_2026 == 0, "estado"] = "desaparece"
    m["nivel"] = nombre
    return m.sort_values("dif_nominal")


def main():
    a, b = marco(2025), marco(2026)
    print(f"proyecto 2025 = {a.MDP.sum():>14,.1f} mdp")
    print(f"proyecto 2026 = {b.MDP.sum():>14,.1f} mdp")
    n, r, v = real(a.MDP.sum(), b.MDP.sum())
    print(f"  bruto: {n:+,.1f} nominal | {r:+,.1f} real | {v:+.2f} % real\n")

    partes = []
    for llaves, nombre in ((["RAMO_K"], "ramo"),
                           (["RAMO_K", "PP_K"], "programa"),
                           (["RAMO_K", "UR_K"], "unidad_responsable")):
        d = diff(a, b, llaves, nombre)
        # nombres, del año donde exista
        nm = (pd.concat([a, b]).drop_duplicates(subset=llaves, keep="last")
                .set_index(llaves)[["NOMBRE_RAMO", "NOMBRE_PP", "NOMBRE_UR"]])
        d = d.join(nm, on=llaves)
        partes.append(d)
        apar = d[d.estado == "aparece"]; desa = d[d.estado == "desaparece"]
        print(f"--- {nombre}: {len(d)} claves | {len(apar)} aparecen "
              f"({apar.mdp_2026.sum():,.1f} mdp) | {len(desa)} desaparecen "
              f"({desa.mdp_2025.sum():,.1f} mdp)")
        for etq, sub, col in (("APARECEN", apar.nlargest(6, "mdp_2026"), "mdp_2026"),
                              ("DESAPARECEN", desa.nlargest(6, "mdp_2025"), "mdp_2025")):
            if len(sub) == 0:
                continue
            print(f"    {etq} (mayores):")
            for _, r_ in sub.iterrows():
                et = " ".join(str(r_[c]) for c in llaves)
                nb = r_.NOMBRE_PP if nombre == "programa" else (
                     r_.NOMBRE_UR if nombre == "unidad_responsable" else r_.NOMBRE_RAMO)
                print(f"      {et:<10} {str(nb)[:58]:<58} {r_[col]:>12,.1f}")
        mov = d[(d.estado == "continúa") & (d.dif_nominal.abs() > 20000)]
        if len(mov):
            print(f"    MOVIMIENTOS > 20,000 mdp nominales entre claves que continúan:")
            for _, r_ in mov.sort_values("dif_nominal").iterrows():
                et = " ".join(str(r_[c]) for c in llaves)
                nb = r_.NOMBRE_PP if nombre == "programa" else (
                     r_.NOMBRE_UR if nombre == "unidad_responsable" else r_.NOMBRE_RAMO)
                print(f"      {et:<10} {str(nb)[:50]:<50} {r_.mdp_2025:>12,.1f} ->"
                      f" {r_.mdp_2026:>12,.1f} {r_.var_real_pct:>+8.1f} %")
        print()

    # subfunción
    af = analitico(2025, "gf-ramo-funcion-ur-objeto"); bf = analitico(2026, "gf-ramo-funcion-ur-objeto")
    aef = analitico(2025, "entidades-ramo-funcion-ur-objeto"); bef = analitico(2026, "entidades-ramo-funcion-ur-objeto")
    def sf(x):
        return x.assign(F_K=clave(x["F"]), FN_K=clave(x["FN"]), SF_K=clave(x["SF"]),
                        NOMBRE_FN=x["FN"].astype(str).str.strip())
    A = pd.concat([sf(af), sf(aef)]); B = pd.concat([sf(bf), sf(bef)])
    d = diff(A, B, ["F_K", "FN_K", "SF_K"], "subfuncion")
    nm = pd.concat([A, B]).drop_duplicates(subset=["F_K","FN_K","SF_K"], keep="last") \
           .set_index(["F_K","FN_K","SF_K"])[["NOMBRE_FN"]]
    d = d.join(nm, on=["F_K","FN_K","SF_K"])
    partes.append(d)
    print(f"--- subfuncion: {len(d)} claves")
    print("    los diez movimientos mayores en nominal:")
    for _, r_ in pd.concat([d.nsmallest(5,"dif_nominal"), d.nlargest(5,"dif_nominal")]).iterrows():
        print(f"      {r_.F_K}.{r_.FN_K}.{r_.SF_K:<4} {str(r_.NOMBRE_FN)[:44]:<44}"
              f" {r_.mdp_2025:>12,.1f} -> {r_.mdp_2026:>12,.1f} {r_.dif_nominal:>+12,.1f}")

    todo = pd.concat(partes, ignore_index=True)
    todo.to_csv(SAL / "diffs_2025_2026.csv", index=False, float_format="%.1f")
    print(f"\nescrito datos/diffs_2025_2026.csv con {len(todo)} filas")


if __name__ == "__main__":
    main()
