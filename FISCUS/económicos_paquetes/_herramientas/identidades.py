#!/usr/bin/env python3
"""Identidades contables y de coherencia entre anexos. Parametrizadas por ejercicio.

Precarga §3.4 de INSTRUCCIONES_preparacion_2027.md. Generaliza `documento_2026/verificar.py`,
que tenía las cifras de 2026 dentro del código.

    python identidades.py                  # ejercicio 2026, el que ya cerró
    python identidades.py --ejercicio 2027

SEPARACIÓN QUE HACE ESTO REUTILIZABLE: **las pruebas son permanentes, las cifras son
datos.** Cada ejercicio trae su `restituciones/{año}.json` con las cifras copiadas de su
documento y la ubicación de cada una. Para correr contra 2027 no se toca este archivo:
se escribe el JSON.

Se corren ANTES de escribir una línea y DESPUÉS de cada cambio en los datos. Validan por
identidad, no por relectura: un dígito mal leído rompe una suma.

**Cuando una identidad no cierra, la primera hipótesis es de OBJETO, no de aritmética.**
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fiscus import analitico, parametros

AQUI = Path(__file__).resolve().parent
TOL_MDP, TOL_PP = 1.0, 0.1


class Tablero:
    def __init__(self):
        self.ok = self.fallo = 0
        self.fallas: list[str] = []

    def prueba(self, nombre, a, b, tol=TOL_MDP, unidad="mdp"):
        d = a - b
        bien = abs(d) <= tol
        self.ok += bien
        self.fallo += not bien
        if not bien:
            self.fallas.append(nombre)
        print(f"  [{'OK ' if bien else 'FALLA'}] {nombre:<62} {a:>16,.1f} vs {b:>16,.1f}"
              f"  dif {d:>+12,.3f} {unidad}")
        return bien

    def nota(self, texto):
        print(f"  [NOTA ] {texto}")


def correr(anio: int) -> int:
    r = json.loads((AQUI / "restituciones" / f"{anio}.json").read_text(encoding="utf-8"))
    D, DA, I, C, CA = (r["decreto"], r["decreto_anterior"], r["ilif"], r["cgpe"],
                       r["cgpe_anterior_estimado"])
    PUB = r["razones_pib_publicadas"]
    etapa = r.get("etapa", "proyecto")
    p = parametros(anio)
    PIB = float(p["pib_t_mmp"]) * 1000
    t = Tablero()

    print("=" * 130)
    print(f"IDENTIDADES DEL PAQUETE {anio} — {etapa}")
    print(f"PIB {anio} = {PIB:,.1f} mdp ({p['fuente']})")
    print("=" * 130)

    print("\n1. El decreto consigo mismo")
    bruto = (sum(D[k] for k in ("autonomos", "administrativos", "generales", "entidades",
                                "empresas"))
             + sum(D["fuera_de_subtotal"].values()))
    t.nota(f"ramos fuera del subtotal sumados: "
           f"{', '.join(D['fuera_de_subtotal'])} = {sum(D['fuera_de_subtotal'].values()):,.1f} mdp")
    t.prueba("Anexo 1: ramos + los que van fuera del subtotal - neteo = gasto neto",
             bruto - D["neteo"], D["gasto_neto"])
    pens = D["oblig_con_pensiones"] - D["oblig_sin_pensiones"]
    t.prueba("Anexo 3: obligatorios con pensiones - sin pensiones = agregado pensionario",
             D["oblig_sin_pensiones"] + pens, D["oblig_con_pensiones"])
    t.nota(f"el Anexo 3 adjudica el perímetro pensionario: {pens:,.1f} mdp")

    print("\n2. El decreto contra los analíticos")
    # Ruta B: si los analíticos del ejercicio no están en carpeta, este bloque no se puede
    # correr. NO se aborta la corrida: se declara y siguen las identidades documentales.
    try:
        gf = analitico(anio, "gf-ramo-programa-ur-objeto", etapa)["MDP"].sum()
        ef = analitico(anio, "entidades-ramo-programa-ur-objeto", etapa)["MDP"].sum()
        t.prueba("analíticos GF + entidades = bruto del Anexo 1", gf + ef, bruto)
        gff = analitico(anio, "gf-ramo-funcion-ur-objeto", etapa)["MDP"].sum()
        eff = analitico(anio, "entidades-ramo-funcion-ur-objeto", etapa)["MDP"].sum()
        t.prueba("corte por función = corte por programa (GF)", gff, gf)
        t.prueba("corte por función = corte por programa (entidades)", eff, ef)
        csv_p = AQUI.parent / str(anio) / f"{anio}_ppef_analitico-claves.csv"
        if csv_p.exists():
            import pandas as pd
            d = pd.read_csv(csv_p, low_memory=False)
            col = next(c for c in d.columns if "monto" in c.lower())
            t.prueba("base de datos abiertos = analíticos xlsx", d[col].sum() / 1e6, gf + ef)
        else:
            t.nota(f"no hay base de datos abiertos en carpeta para {anio}: la validación "
                   f"cruzada más barata que existe se queda sin correr")
    except FileNotFoundError as ex:
        t.nota(f"RUTA B: sin analíticos de {anio} en carpeta, el bloque 2 completo no corre "
               f"({ex}). Cuatro pruebas quedan sin correr; no cuentan como aprobadas.")

    print("\n3. La Ley de Ingresos contra el decreto")
    t.prueba("total del art. 1o. = gasto neto total", I["total"], D["gasto_neto"])

    print("\n4. Los Criterios Generales consigo mismos")
    t.prueba("balance presupuestario = ingresos presupuestarios - gasto neto pagado",
             C["ing_presup"] - C["gasto_pagado"], C["balance_presup"])
    t.prueba("RFSP = balance presupuestario + extrapresupuestario",
             C["balance_presup"] + C["extrapresup"], C["rfsp"])
    t.prueba("no programable = costo financiero + participaciones + Adefas",
             C["costo_financiero"] + C["participaciones"] + C["adefas"], C["no_programable"])
    t.prueba("gasto pagado = programable pagado + no programable",
             C["programable_pagado"] + C["no_programable"], C["gasto_pagado"])
    t.prueba("programable devengado = programable pagado - diferimiento",
             C["programable_pagado"] - C["diferimiento"], C["programable_devengado"])
    t.prueba("primario = balance presupuestario + no presupuestario + costo financiero",
             C["balance_presup"] + C["no_presupuestario"] + C["costo_financiero"], C["primario"])
    t.prueba("la misma identidad en la columna del año anterior del mismo cuadro",
             CA["balance_presup"] + C["no_presupuestario"] + CA["costo_financiero"],
             CA["primario"])
    if "primario" in r.get("notas", {}):
        t.nota(r["notas"]["primario"])
    t.prueba("no petroleros = Gobierno Federal + organismos y empresas",
             C["gf_no_petro"] + C["organismos"], C["no_petroleros"])
    t.prueba("Gobierno Federal no petrolero = tributarios + no tributarios",
             C["tributarios"] + C["no_tributarios"], C["gf_no_petro"])
    t.prueba("ingresos presupuestarios = petroleros + no petroleros",
             C["petroleros"] + C["no_petroleros"], C["ing_presup"])

    print("\n5. Puentes entre documentos")
    t.prueba("participaciones del CGPE = Ramo 28 del Anexo 1",
             C["participaciones"], D["ramo28_participaciones"])
    t.prueba("Adefas del CGPE = Ramo 30 del Anexo 1", C["adefas"], D["ramo30_adefas"])
    t.prueba("gasto neto total - financiamientos = ingresos presupuestarios",
             D["gasto_neto"] - I["financiamientos"], C["ing_presup"])
    t.prueba("gasto neto pagado = gasto neto total - diferimiento",
             D["gasto_neto"] + C["diferimiento"], C["gasto_pagado"])
    d = C["tributarios"] - I["impuestos"]
    t.nota(f"reconciliación tributarios CGPE - impuestos ILIF: {d:+,.1f} mdp "
           f"({d / C['tributarios'] * 100:+.4f} %) — residuo a nombrar en el capítulo de ingresos")

    print("\n6. Razones a PIB, contra las publicadas")
    for k, nom in (("rfsp", "RFSP"), ("balance_presup", "balance presupuestario"),
                   ("ing_presup", "ingresos presupuestarios"), ("tributarios", "tributarios"),
                   ("gasto_pagado", "gasto neto pagado"),
                   ("costo_financiero", "costo financiero"), ("shrfsp", "SHRFSP")):
        t.prueba(f"{nom} en % del PIB", C[k] / PIB * 100, PUB[k], tol=TOL_PP, unidad="pp")
    t.prueba("pensiones y jubilaciones del Anexo 3 en % del PIB", pens / PIB * 100,
             PUB["pensiones_anexo3"], tol=TOL_PP, unidad="pp")
    t.prueba("SHRFSP = interno + externo (% PIB)",
             C["shrfsp_interno_pct"] + C["shrfsp_externo_pct"], C["shrfsp_pct"],
             tol=TOL_PP, unidad="pp")
    holgura = D["gce_limite"] - D["gce"]
    t.prueba("gasto corriente estructural POR DEBAJO de su límite máximo (holgura ≥ 0)",
             min(holgura, 0.0), 0.0)
    t.nota(f"holgura {holgura:,.1f} mdp = {holgura / PIB * 100:.3f} pp del PIB. El límite que "
           f"publica el CGPE ({D['gce_limite']:,.1f}) no es exactamente el "
           f"{C['lmgce_pct']} % del PIB que declara ({C['lmgce_pct']/100*PIB:,.1f}): "
           f"la diferencia es el redondeo del porcentaje, no un error.")

    print("\n7. Flujo contra acervo")
    d_acervo = C["shrfsp"] - CA["shrfsp"]
    fx_pp = C["shrfsp_externo_pct_t_1"] * (C["tipo_cambio_t"] / C["tipo_cambio_t_1"] - 1)
    fx = fx_pp / 100 * PIB
    residuo = d_acervo - (-C["rfsp"]) - fx
    print(f"  Δ acervo {d_acervo:>14,.1f} | RFSP {-C['rfsp']:>14,.1f} | "
          f"tipo de cambio {fx:>12,.1f} ({fx_pp:+.3f} pp)")
    t.prueba("identidad flujo-acervo cierra dentro de 0.3 pp del PIB",
             abs(residuo) / PIB * 100, 0.0, tol=0.3, unidad="pp")

    print("\n8. La línea primaria: el ejercicio anterior")
    try:
        g1 = analitico(anio - 1, "gf-ramo-programa-ur-objeto", etapa)["MDP"].sum()
        e1 = analitico(anio - 1, "entidades-ramo-programa-ur-objeto", etapa)["MDP"].sum()
        t.prueba(f"analíticos {anio-1} - neteo {anio-1} = gasto neto total {anio-1}",
                 g1 + e1 - DA["neteo"], DA["gasto_neto"])
    except FileNotFoundError as ex:
        t.nota(f"sin analíticos de {anio-1} en carpeta: {ex}")

    G = r.get("gaceta_cola")
    if G is None:
        t.nota("sin bloque «gaceta_cola» en la restitución: no se corren las identidades "
               "de los anexos de la cola del paquete.")
    else:
        print("\n9. Anexos de la cola: vivienda (art. 61 LV) y ZAP")
        F = G["vivienda_filas"]
        for f in F:
            t.prueba(f"vivienda: hogares x costo unitario = monto ({f['necesidad'].lower()})",
                     f["hogares"] * f["costo_unitario"] / 1e6, f["monto"] / 1e6)
            t.prueba(f"vivienda: urbano + rural = hogares ({f['necesidad'].lower()})",
                     f["urbano"] + f["rural"], f["hogares"], tol=0.0, unidad="hogares")
            t.prueba(f"vivienda: costo unitario / UMA = UMA mensual ({f['necesidad'].lower()})",
                     f["costo_unitario"] / f["uma"], G["vivienda_uma_mensual_2026"],
                     tol=0.005, unidad="pesos")
        t.prueba("vivienda: suma de los tres montos = total declarado",
                 sum(f["monto"] for f in F) / 1e6,
                 G["vivienda_total_pesos_declarado"] / 1e6)
        t.prueba("vivienda: suma de hogares x UMA = total en UMA declarado",
                 sum(f["hogares"] * f["uma"] for f in F), G["vivienda_total_uma_declarado"],
                 tol=0.0, unidad="UMA")
        t.prueba("ZAP: municipios rurales = universo menos los que pasan a la lista urbana",
                 G["zap_rurales_antes_de_pasar_urbanos"] - G["zap_rurales_pasados_a_urbanos"],
                 G["zap_rurales_municipios"], tol=0.0, unidad="municipios")
        req = G["vivienda_total_pesos_declarado"] / 1e6
        t.nota(f"requerimiento de vivienda {req:,.1f} mdp = {req / PIB * 100:.3f} % del PIB; "
               f"Ramo 15 completo {G['ramo15_mdp']:,.1f} mdp = "
               f"{G['ramo15_mdp'] / PIB * 100:.3f} % del PIB, esto es el "
               f"{G['ramo15_mdp'] / req * 100:.1f} % del requerimiento. "
               f"AÑOS DE PESOS DISTINTOS: el requerimiento está en pesos de 2026 (UMA y "
               f"Reglas de Operación de 2026) y el presupuesto en pesos de 2027.")

        Z = G.get("zap_urbanas_microdatos")
        if Z is None:
            t.nota("sin bloque «zap_urbanas_microdatos»: no se verifican las 43.636 AGEB "
                   "contra el archivo de variables.")
        else:
            ruta = AQUI.parent / Z["archivo"]
            if not ruta.exists():
                t.nota(f"no está en carpeta {Z['archivo']}: la declaratoria urbana queda "
                       "verificada sólo por el PDF.")
            else:
                print("\n10. ZAP urbanas: la declaratoria contra el archivo de variables")
                import pandas as pd, zipfile
                with zipfile.ZipFile(ruta) as z:
                    interno = [n for n in z.namelist() if n.lower().endswith(".xlsx")][0]
                    with z.open(interno) as fh:
                        m = pd.read_excel(fh, header=Z["encabezado_en_renglon"], dtype=str)
                m = m.dropna(how="all")
                col = list(m.columns)
                ent, mun, loc, ageb, actual = (col[i] for i in Z["columnas"])
                t.prueba("ZAP urbana: renglones del archivo = AGEB declaradas",
                         len(m), G["zap_urbanas_agebs"], tol=0.0, unidad="AGEB")
                t.prueba("ZAP urbana: AGEB sin repetir = renglones",
                         m[ageb].nunique(), len(m), tol=0.0, unidad="AGEB")
                t.prueba("ZAP urbana: entidades = 32",
                         m[ent].nunique(), 32, tol=0.0, unidad="entidades")
                # LA CLAVE QUE CUENTA ES LA ACTUALIZADA. Sobre la clave que el propio
                # archivo trae en sus columnas, los dos conteos NO cierran: ver la nota.
                t.prueba("ZAP urbana: municipios (clave actual) = declarados",
                         m[actual].str[:5].nunique(), G["zap_urbanas_municipios"],
                         tol=0.0, unidad="municipios")
                t.prueba("ZAP urbana: localidades (clave actual) = declaradas",
                         m[actual].nunique(), G["zap_urbanas_localidades"],
                         tol=0.0, unidad="localidades")
                mv, lv = m[mun].nunique(), m[loc].nunique()
                reasignados = int((m[loc] != m[actual]).sum())
                nuevos = sorted(set(m[actual].str[:5]) - set(m[mun]))
                t.nota(f"sobre la clave que el archivo trae en sus columnas serían {mv:,} "
                       f"municipios y {lv:,} localidades, no {G['zap_urbanas_municipios']:,} "
                       f"y {G['zap_urbanas_localidades']:,}. La declaratoria cuenta sobre la "
                       f"CLAVE ACTUAL A JUNIO DE 2026: {reasignados} AGEB están reasignadas y "
                       f"aparecen {len(nuevos)} municipios que la clave vieja no tiene "
                       f"({', '.join(nuevos)}), los de creación reciente.")
                t.prueba("ZAP urbana: la columna del traslape rural parte el universo",
                         int(m[col[Z['columna_traslape_rural']]].isin(["SI", "NO"]).sum()),
                         len(m), tol=0.0, unidad="AGEB")
                tr = int((m[col[Z['columna_traslape_rural']]] == "SI").sum())
                t.nota(f"{tr:,} de las {len(m):,} AGEB urbanas ({tr / len(m) * 100:.1f} %) "
                       f"caen dentro de los {G['zap_rurales_municipios']:,} municipios ZAP "
                       "rurales: las dos listas se traslapan, no son disjuntas.")

    print("\n" + "=" * 130)
    print(f"RESULTADO: {t.ok} pruebas cierran, {t.fallo} fallan")
    for f in t.fallas:
        print(f"  FALLA -> {f}")
    print("=" * 130)
    return t.fallo


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--ejercicio", type=int, default=2026)
    sys.exit(1 if correr(ap.parse_args().ejercicio) else 0)
