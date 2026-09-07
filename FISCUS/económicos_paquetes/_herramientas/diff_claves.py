#!/usr/bin/env python3
"""Diff institucional entre dos ejercicios, por clave. Parametrizado.

Precarga §3.3 de INSTRUCCIONES_preparacion_2027.md.

    python diff_claves.py                      # 2025 -> 2026, proyecto contra proyecto
    python diff_claves.py --de 2026 --a 2027
    python diff_claves.py --casos              # solo los dos casos de prueba

REGLA DE LA CASA, y su corrección de 2026:
  «por clave, nunca por nombre» **no basta**. La clave completa tampoco es estable:
  la Pensión Mujeres Bienestar es U316 en 2025 y S316 en 2026 —cambió la modalidad,
  no el número—. El emparejamiento usa **número de programa dentro del ramo** y la
  modalidad se verifica contra el diff. Y los organismos cambian de ramo: el diff por
  unidad responsable se corre **dos veces**, dentro del ramo y a través de los ramos.

SIN ESTE DIFF, una comparación automática produce recortes y aumentos falsos. En el
paso de 2025 a 2026 fueron 271 claves nuevas y 358 desaparecidas.
"""
from __future__ import annotations
import argparse, sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fiscus import analitico, clave, cod_pp, num_pp, deflactor, real

SAL = Path(__file__).resolve().parent / "_salidas"

# Los dos casos que rompen una lectura ingenua. Se buscan POR NOMBRE porque hay que
# localizarlos; se MIDEN por clave. Localizar y medir son cosas distintas.
CASOS = {
    "IMSS-Bienestar": dict(
        patron=r"IMSS[- ]?Bienestar|Servicios de Salud del Instituto Mexicano del Seguro Social",
        porque="Ha cambiado de ubicación tres veces: Ramo 19 en 2024, Ramo 47 en 2025, "
               "Ramo 56 en 2026. Un diff por ramo lo lee como extinción y nacimiento."),
    "Guardia Nacional": dict(
        patron=r"Guardia Nacional",
        porque="Coexisten dos cosas: cambio de ramo y reducción propia. Atribuir toda la "
               "variación al cambio de ramo, o toda a la política, es falso en los dos casos."),
}


def marco(anio: int, etapa: str = "proyecto") -> pd.DataFrame:
    """Gobierno Federal y entidades en un solo marco, con las claves normalizadas."""
    gf = analitico(anio, "gf-ramo-programa-ur-objeto", etapa)
    ef = analitico(anio, "entidades-ramo-programa-ur-objeto", etapa)
    gf = gf.assign(RAMO_K=clave(gf["RAMO"]), PP_K=cod_pp(gf), PP_NUM=num_pp(gf),
                   MOD_K=gf["MOD"].astype(str).str.strip().str[0],
                   UR_K=clave(gf["UR"]),
                   NOMBRE_PP=gf["PP"].astype(str).str.strip(),
                   NOMBRE_UR=gf["UR"].astype(str).str.strip(),
                   NOMBRE_RAMO=gf["RAMO"].astype(str).str.strip(), AMBITO="GF")
    ef = ef.assign(RAMO_K=clave(ef["ENTIDAD"]),
                   PP_K=ef["PP"].astype(str).str.strip().str[:4],
                   PP_NUM=ef["PP"].astype(str).str.strip().str[1:4],
                   MOD_K=ef["PP"].astype(str).str.strip().str[0],
                   UR_K=clave(ef["ENTIDAD"]),
                   NOMBRE_PP=ef["PP"].astype(str).str.strip(),
                   NOMBRE_UR=ef["ENTIDAD"].astype(str).str.strip(),
                   NOMBRE_RAMO=ef["ENTIDAD"].astype(str).str.strip(), AMBITO="EFE")
    cols = ["RAMO_K", "PP_K", "PP_NUM", "MOD_K", "UR_K", "NOMBRE_RAMO", "NOMBRE_PP",
            "NOMBRE_UR", "AMBITO", "MDP"]
    return pd.concat([gf[cols], ef[cols]], ignore_index=True)


def diff(a, b, llaves, nombre, de, al, defl) -> pd.DataFrame:
    ga = a.groupby(llaves, as_index=False)["MDP"].sum().rename(columns={"MDP": f"mdp_{de}"})
    gb = b.groupby(llaves, as_index=False)["MDP"].sum().rename(columns={"MDP": f"mdp_{al}"})
    m = ga.merge(gb, on=llaves, how="outer").fillna({f"mdp_{de}": 0.0, f"mdp_{al}": 0.0})
    m["dif_nominal"] = m[f"mdp_{al}"] - m[f"mdp_{de}"]
    m["dif_real"] = m[f"mdp_{al}"] - m[f"mdp_{de}"] * defl
    m["var_real_pct"] = (m[f"mdp_{al}"] / (m[f"mdp_{de}"] * defl) - 1) * 100
    m["estado"] = "continúa"
    m.loc[m[f"mdp_{de}"] == 0, "estado"] = "aparece"
    m.loc[m[f"mdp_{al}"] == 0, "estado"] = "desaparece"
    m["nivel"] = nombre
    return m.sort_values("dif_nominal")


def rastrear(nombre: str, patron: str, porque: str, a, b, de, al, defl) -> None:
    """Localiza una entidad por nombre en los dos años y la mide por clave.

    Es el procedimiento para todo lo que se mueve: el nombre sirve para encontrar,
    nunca para agregar. Si el nombre cambia —«Pemex Consolidado» pasó a «Petróleos
    Mexicanos»— el patrón hay que ampliarlo, y eso también es un hallazgo."""
    print(f"\n--- CASO DE PRUEBA: {nombre}")
    print(f"    {porque}")
    for etq, m, anio in (("origen", a, de), ("destino", b, al)):
        s = m[m.NOMBRE_UR.str.contains(patron, case=False, regex=True, na=False)
              | m.NOMBRE_PP.str.contains(patron, case=False, regex=True, na=False)]
        if s.empty:
            print(f"    {anio}: NO APARECE con este patrón. Si el objeto existe, el nombre "
                  f"cambió: amplía el patrón y regístralo.")
            continue
        g = (s.groupby(["RAMO_K", "UR_K"], as_index=False)
              .agg(mdp=("MDP", "sum"), ramo=("NOMBRE_RAMO", "first"), ur=("NOMBRE_UR", "first")))
        for _, r in g.sort_values("mdp", ascending=False).iterrows():
            print(f"    {anio}  ramo {r.RAMO_K:>3} UR {r.UR_K:<5} {str(r.ur)[:44]:<44} "
                  f"{r.mdp:>13,.1f} mdp")
    ta = a[a.NOMBRE_UR.str.contains(patron, case=False, regex=True, na=False)
           | a.NOMBRE_PP.str.contains(patron, case=False, regex=True, na=False)].MDP.sum()
    tb = b[b.NOMBRE_UR.str.contains(patron, case=False, regex=True, na=False)
           | b.NOMBRE_PP.str.contains(patron, case=False, regex=True, na=False)].MDP.sum()
    n, r_, v = real(ta, tb, defl)
    ramos_a = set(a[a.NOMBRE_UR.str.contains(patron, case=False, regex=True, na=False)].RAMO_K)
    ramos_b = set(b[b.NOMBRE_UR.str.contains(patron, case=False, regex=True, na=False)].RAMO_K)
    print(f"    TOTAL a través de ramos: {ta:>13,.1f} -> {tb:>13,.1f}  "
          f"{n:+,.1f} nominal | {r_:+,.1f} real | {v:+.2f} % real")
    if ramos_a != ramos_b:
        print(f"    *** CAMBIO DE RAMO: {sorted(ramos_a)} -> {sorted(ramos_b)}. La variación "
              f"de CADA ramo por separado es contable, no presupuestal. La cifra que se "
              f"publica es la de esta línea, a través de ramos.")
    else:
        print(f"    sin cambio de ramo: la variación es presupuestal y se puede atribuir.")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--de", type=int, default=2025)
    ap.add_argument("--a", type=int, default=2026)
    ap.add_argument("--etapa", default="proyecto", choices=["proyecto", "pef"])
    ap.add_argument("--casos", action="store_true", help="solo los casos de prueba")
    o = ap.parse_args()
    de, al = o.de, o.a
    defl = deflactor(al)
    a, b = marco(de, o.etapa), marco(al, o.etapa)

    print(f"DIFF INSTITUCIONAL {de} -> {al} ({o.etapa}), deflactor {defl}")
    print(f"  bruto {de} = {a.MDP.sum():>15,.1f} mdp")
    print(f"  bruto {al} = {b.MDP.sum():>15,.1f} mdp")
    n, r, v = real(a.MDP.sum(), b.MDP.sum(), defl)
    print(f"  {n:+,.1f} nominal | {r:+,.1f} real | {v:+.2f} % real")

    if not o.casos:
        partes = []
        niveles = [
            (["RAMO_K"], "ramo"),
            (["RAMO_K", "PP_K"], "programa"),
            (["RAMO_K", "PP_NUM"], "programa_por_numero"),   # ve a través del cambio de modalidad
            (["RAMO_K", "UR_K"], "unidad_responsable"),
            (["UR_K"], "unidad_responsable_entre_ramos"),    # ve el cambio de ramo
        ]
        for llaves, nombre in niveles:
            d = diff(a, b, llaves, nombre, de, al, defl)
            partes.append(d)
            ap_, ds = d[d.estado == "aparece"], d[d.estado == "desaparece"]
            print(f"\n--- {nombre}: {len(d)} claves | {len(ap_)} aparecen "
                  f"({ap_[f'mdp_{al}'].sum():,.1f} mdp) | {len(ds)} desaparecen "
                  f"({ds[f'mdp_{de}'].sum():,.1f} mdp)")

        # cambio de modalidad conservando número: el caso U316 -> S316
        ma = a.groupby(["RAMO_K", "PP_NUM"])["MOD_K"].agg(lambda s: s.mode().iat[0])
        mb = b.groupby(["RAMO_K", "PP_NUM"])["MOD_K"].agg(lambda s: s.mode().iat[0])
        mod = pd.concat([ma.rename("mod_de"), mb.rename("mod_a")], axis=1).dropna()
        mod = mod[mod.mod_de != mod.mod_a]
        print(f"\n--- cambios de MODALIDAD conservando el número de programa: {len(mod)}")
        for (ramo, num), r_ in mod.iterrows():
            nom = b[(b.RAMO_K == ramo) & (b.PP_NUM == num)].NOMBRE_PP.iloc[0]
            print(f"    ramo {ramo:>3}  {r_.mod_de}{num} -> {r_.mod_a}{num}  {str(nom)[:56]}")

        # función y subfunción: la única agregación estable
        A = pd.concat([analitico(de, c, o.etapa) for c in
                       ("gf-ramo-funcion-ur-objeto", "entidades-ramo-funcion-ur-objeto")])
        B = pd.concat([analitico(al, c, o.etapa) for c in
                       ("gf-ramo-funcion-ur-objeto", "entidades-ramo-funcion-ur-objeto")])
        for X in (A, B):
            X["F_K"], X["FN_K"], X["SF_K"] = clave(X["F"]), clave(X["FN"]), clave(X["SF"])
            X["NOMBRE_FN"] = X["FN"].astype(str).str.strip()
        d = diff(A, B, ["F_K", "FN_K", "SF_K"], "subfuncion", de, al, defl)
        partes.append(d)
        ap_, ds = d[d.estado == "aparece"], d[d.estado == "desaparece"]
        print(f"\n--- subfuncion: {len(d)} claves | {len(ap_)} aparecen | {len(ds)} desaparecen")
        print("    (la función y la subfunción son catálogo nacional: es la ÚNICA agregación "
              "estable entre ejercicios. Todo perímetro de rubro se define aquí primero.)")

        SAL.mkdir(exist_ok=True)
        salida = SAL / f"diffs_{de}_{al}.csv"
        pd.concat(partes, ignore_index=True).to_csv(salida, index=False, float_format="%.1f")
        print(f"\nescrito {salida.relative_to(SAL.parent)}")

    print("\n" + "=" * 78)
    print("CASOS DE PRUEBA OBLIGATORIOS")
    print("=" * 78)
    for nombre, c in CASOS.items():
        rastrear(nombre, c["patron"], c["porque"], a, b, de, al, defl)
    return 0


if __name__ == "__main__":
    sys.exit(main())
