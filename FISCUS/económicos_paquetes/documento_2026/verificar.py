#!/usr/bin/env python3
"""Identidades contables y de coherencia entre anexos, paquete 2026.

Se corren ANTES de escribir una línea y DESPUÉS de cada cambio en los datos.
Validan por identidad, no por relectura. Un dígito mal leído rompe una suma.

Fuentes, todas del proyecto: DEC 2026 y 2025 (Anexos 1, 2, 3, 8); ILIF 2026 art. 1o.;
CGPE 2026 Anexos II.5, II.6, III.1, III.2; analíticos del proyecto 2025 y 2026;
CSV del proyecto 2026 del repositorio de datos abiertos.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fiscus26 import analitico, csv_proyecto, clave, PIB, DEFLACTOR

TOL_MDP = 1.0        # un millón de pesos
TOL_PP = 0.1         # una décima de punto porcentual
TOL_PCT = 0.5        # medio por ciento en niveles

# ---- restituciones, con documento y ubicación -------------------------------
DEC26 = dict(  # Proyecto de Decreto de PEF 2026, PDF pp. 65-67
    autonomos=149_220.238722, administrativos=2_445_888.923876, generales=5_696_382.292607,
    entidades=2_129_329.459009, empresas=1_310_768.382032,
    ramo40=11_807.5, ramo32=3_400.0,
    neteo=1_553_113.096246, gasto_neto=10_193_683.7,
    gce=3_868_319.904030 / 1000 * 1000,  # mdp
    oblig_sin=6_702_281.0, oblig_con=8_406_440.2,
)
DEC25 = dict(neteo=1_493_069.318581, gasto_neto=9_302_015.8,
             gce=3_603_976.680425, oblig_sin=6_046_446.8, oblig_con=7_684_111.9)
ILIF26 = dict(total=10_193_683.7, impuestos=5_838_541.1, cuotas=641_782.1,
              ventas=1_630_973.6, fmp=232_630.4, financiamientos=1_472_626.4)
CGPE26 = dict(  # Anexo II.6, p. 84
    rfsp=-1_587_349.9, balance_presup=-1_393_770.6, extrapresup=-193_579.3,
    ing_presup=8_721_057.3, petroleros=1_204_277.7, no_petroleros=7_516_779.6,
    gf_no_petro=6_215_701.1, tributarios=5_838_571.0, no_tributarios=377_130.1,
    organismos=1_301_078.5, gasto_pagado=10_114_827.9, programable_pagado=7_015_853.1,
    diferimiento=-78_855.7, programable_devengado=7_094_708.8, no_programable=3_098_974.9,
    costo_financiero=1_572_073.3, participaciones=1_456_045.9, adefas=70_855.7,
    primario=178_802.6, shrfsp=20_259_590.7,
    lmgce_pct=10.9, shrfsp_pct=52.3, shrfsp_interno_pct=41.3, shrfsp_externo_pct=11.0,
)
CGPE25E = dict(shrfsp=18_903_594.9, shrfsp_pct=52.3, rfsp=-1_559_905.4)

ok = fallo = 0
def prueba(nombre, a, b, tol=TOL_MDP, unidad="mdp"):
    global ok, fallo
    d = a - b
    bien = abs(d) <= tol
    globals().__setitem__("ok", ok + bien); globals().__setitem__("fallo", fallo + (not bien))
    print(f"  [{'OK ' if bien else 'FALLA'}] {nombre:<62} {a:>16,.1f} vs {b:>16,.1f}"
          f"  dif {d:>+12,.3f} {unidad}")
    return bien


def main():
    global ok, fallo
    print("=" * 130)
    print("IDENTIDADES DEL PAQUETE 2026 — proyecto")
    print("=" * 130)

    print("\n1. El decreto consigo mismo")
    bruto = sum(DEC26[k] for k in ("autonomos","administrativos","generales","entidades",
                                   "empresas","ramo40","ramo32"))
    prueba("Anexo 1: A+B+C+D+E + ramos 40 y 32 - neteo = gasto neto total",
           bruto - DEC26["neteo"], DEC26["gasto_neto"])
    prueba("Anexo 3: obligatorios con pensiones - sin pensiones > 0",
           DEC26["oblig_con"] - DEC26["oblig_sin"], 1_704_159.2)

    print("\n2. El decreto contra los analíticos del proyecto")
    gf = analitico(2026, "gf-ramo-programa-ur-objeto")["MDP"].sum()
    ef = analitico(2026, "entidades-ramo-programa-ur-objeto")["MDP"].sum()
    prueba("analíticos GF + entidades = bruto del Anexo 1", gf + ef, bruto, tol=1.0)
    prueba("CSV de datos abiertos = analíticos xlsx", csv_proyecto()["MDP"].sum(), gf + ef, tol=1.0)
    gff = analitico(2026, "gf-ramo-funcion-ur-objeto")["MDP"].sum()
    eff = analitico(2026, "entidades-ramo-funcion-ur-objeto")["MDP"].sum()
    prueba("corte por función = corte por programa (GF)", gff, gf, tol=1.0)
    prueba("corte por función = corte por programa (entidades)", eff, ef, tol=1.0)

    print("\n3. La Ley de Ingresos contra el decreto")
    prueba("total del art. 1o. = gasto neto total", ILIF26["total"], DEC26["gasto_neto"])

    print("\n4. Los Criterios Generales consigo mismos")
    prueba("balance presupuestario = ingresos presupuestarios - gasto neto pagado",
           CGPE26["ing_presup"] - CGPE26["gasto_pagado"], CGPE26["balance_presup"], tol=TOL_MDP)
    prueba("RFSP = balance presupuestario + extrapresupuestario",
           CGPE26["balance_presup"] + CGPE26["extrapresup"], CGPE26["rfsp"], tol=TOL_MDP)
    prueba("no programable = costo financiero + participaciones + Adefas",
           CGPE26["costo_financiero"] + CGPE26["participaciones"] + CGPE26["adefas"],
           CGPE26["no_programable"], tol=TOL_MDP)
    prueba("gasto pagado = programable pagado + no programable",
           CGPE26["programable_pagado"] + CGPE26["no_programable"], CGPE26["gasto_pagado"])
    prueba("programable devengado = programable pagado - diferimiento",
           CGPE26["programable_pagado"] - CGPE26["diferimiento"],
           CGPE26["programable_devengado"])
    # IDENTIDAD DE OBJETO. El CGPE 2026 rotula el renglón «Superávit ECONÓMICO primario»
    # donde el CGPE 2025 rotulaba «Superávit primario PRESUPUESTARIO». No cierra contra el
    # balance presupuestario por exactamente 500.0 mdp en LOS DOS años del cuadro, que es el
    # balance no presupuestario. Con el objeto bien nombrado, cierra al décimo.
    NO_PRESUP = 500.0
    prueba("primario económico = balance presupuestario + no presupuestario + costo financiero",
           CGPE26["balance_presup"] + NO_PRESUP + CGPE26["costo_financiero"],
           CGPE26["primario"], tol=TOL_MDP)
    prueba("la misma identidad en la columna 2025 del mismo cuadro",
           -1_170_566.5 + NO_PRESUP + 1_388_373.6, 218_307.2, tol=TOL_MDP)
    print("  [NOTA ] el CGPE 2025 publicaba 217,807.2 para esa misma celda, bajo el rótulo")
    print("          «Superávit primario PRESUPUESTARIO». Mismo año, dos rótulos, 500.0 mdp")
    print("          de diferencia: es el balance no presupuestario. Se declara una vez.")
    prueba("no petroleros = Gobierno Federal + organismos y empresas",
           CGPE26["gf_no_petro"] + CGPE26["organismos"], CGPE26["no_petroleros"])
    prueba("Gobierno Federal no petrolero = tributarios + no tributarios",
           CGPE26["tributarios"] + CGPE26["no_tributarios"], CGPE26["gf_no_petro"])
    prueba("ingresos presupuestarios = petroleros + no petroleros",
           CGPE26["petroleros"] + CGPE26["no_petroleros"], CGPE26["ing_presup"])

    print("\n5. Puentes entre documentos")
    prueba("participaciones del CGPE = Ramo 28 del Anexo 1",
           CGPE26["participaciones"], 1_456_045.894280, tol=TOL_MDP)
    prueba("Adefas del CGPE = Ramo 30 del Anexo 1", CGPE26["adefas"], 70_855.7)
    prueba("gasto neto total - financiamientos = ingresos presupuestarios",
           DEC26["gasto_neto"] - ILIF26["financiamientos"], CGPE26["ing_presup"], tol=TOL_MDP)
    prueba("gasto neto pagado = gasto neto total - diferimiento",
           DEC26["gasto_neto"] + CGPE26["diferimiento"], CGPE26["gasto_pagado"], tol=TOL_MDP)
    d = CGPE26["tributarios"] - ILIF26["impuestos"]
    print(f"  [NOTA ] reconciliación tributarios CGPE - impuestos ILIF: {d:+,.1f} mdp"
          f"  ({d/CGPE26['tributarios']*100:+.4f} %) — residuo a nombrar en C2.2")

    print("\n6. Razones a PIB, contra las publicadas")
    for nom, mdp, pub in (("RFSP", CGPE26["rfsp"], -4.1),
                          ("balance presupuestario", CGPE26["balance_presup"], -3.6),
                          ("ingresos presupuestarios", CGPE26["ing_presup"], 22.5),
                          ("tributarios", CGPE26["tributarios"], 15.1),
                          ("gasto neto pagado", CGPE26["gasto_pagado"], 26.1),
                          ("costo financiero", CGPE26["costo_financiero"], 4.1),
                          ("SHRFSP", CGPE26["shrfsp"], 52.3)):
        prueba(f"{nom} en % del PIB", mdp / (PIB[2026] * 1000) * 100, pub, tol=TOL_PP, unidad="pp")
    prueba("pensiones y jubilaciones del Anexo 3 en % del PIB",
           (DEC26["oblig_con"] - DEC26["oblig_sin"]) / (PIB[2026] * 1000) * 100, 4.4,
           tol=TOL_PP, unidad="pp")
    prueba("SHRFSP = interno + externo (% PIB)",
           CGPE26["shrfsp_interno_pct"] + CGPE26["shrfsp_externo_pct"], CGPE26["shrfsp_pct"],
           tol=TOL_PP, unidad="pp")
    prueba("gasto corriente estructural bajo su límite máximo (mdp)",
           CGPE26["lmgce_pct"] / 100 * PIB[2026] * 1000 - DEC26["gce"],
           4_220_033.1 - 3_868_319.9, tol=5000.0)

    print("\n7. Flujo contra acervo")
    d_acervo = CGPE26["shrfsp"] - CGPE25E["shrfsp"]
    tc25, tc26 = 19.9, 18.9          # CGPE III.1, fin de periodo
    ext25 = 12.2                      # SHRFSP externo % PIB 2025 estimado
    fx_pp = ext25 * (tc26 / tc25 - 1)
    fx_mdp = fx_pp / 100 * PIB[2026] * 1000
    print(f"  Δ acervo observado {d_acervo:>14,.1f} | RFSP {-CGPE26['rfsp']:>14,.1f}"
          f" | tipo de cambio {fx_mdp:>12,.1f} ({fx_pp:+.3f} pp)")
    residuo = d_acervo - (-CGPE26["rfsp"]) - fx_mdp
    print(f"  residuo {residuo:>+14,.1f} mdp = {residuo/(PIB[2026]*1000)*100:+.3f} % del PIB")
    prueba("identidad flujo-acervo cierra dentro de 0.3 pp del PIB",
           abs(residuo) / (PIB[2026] * 1000) * 100, 0.0, tol=0.3, unidad="pp")

    print("\n8. La línea primaria: proyecto 2025 contra proyecto 2026")
    gf25 = analitico(2025, "gf-ramo-programa-ur-objeto")["MDP"].sum()
    ef25 = analitico(2025, "entidades-ramo-programa-ur-objeto")["MDP"].sum()
    prueba("analíticos del proyecto 2025 - neteo 2025 = gasto neto total 2025",
           gf25 + ef25 - DEC25["neteo"], DEC25["gasto_neto"], tol=1.0)

    print("\n" + "=" * 130)
    print(f"RESULTADO: {ok} pruebas cierran, {fallo} fallan")
    print("=" * 130)
    return fallo


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
