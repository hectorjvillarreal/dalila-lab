"""Construye los .csv del marco macroeconómico y de las finanzas públicas.

Fuente: CGPE 2025, anexos II.5 (p. 81), II.6 (p. 82), III.1 (p. 84) y III.2 (p. 85).

PROVENIENCIA, IMPORTANTE: el CGPE 2025 se publicó SIN CAPA DE TEXTO. 90 de sus 91
páginas son imagen; solo la 34 tiene texto, y son las fórmulas del PIB potencial.
Las cifras de este archivo se leyeron de la página renderizada a 150 dpi. Queda
declarado en la columna `nota` de _fuentes.csv y en la nota de método del
documento. No es una restitución de texto: es una lectura de imagen.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fiscus import emitir

IMG = ("Leído de página renderizada a 150 dpi: el CGPE 2025 no tiene capa de texto "
       "(90 de 91 páginas son imagen).")

# --------------------------------------------------------- C1.1 marco macro ---
# CGPE 2025, Anexo II.5, p. 81. Tres columnas: 2024 aprobado, 2024 estimado, 2025.
marco = [
    ("PIB, crecimiento real (rango)",            "[2.5,3.5]", "[1.5,2.5]", "[2.0,3.0]"),
    ("PIB nominal (miles de millones de pesos)", "34374",     "33927.7",   "36166.4"),
    ("Deflactor del PIB (%)",                    "4.8",       "4.6",       "4.3"),
    ("Inflacion dic/dic (%)",                    "3.8",       "4.3",       "3.5"),
    ("Inflacion promedio (%)",                   "4.5",       "4.7",       "3.8"),
    ("Tipo de cambio fin de periodo",            "17.6",      "19.7",      "18.5"),
    ("Tipo de cambio promedio",                  "17.1",      "18.2",      "18.7"),
    ("Cetes 28 nominal fin de periodo (%)",      "9.5",       "10.0",      "8.0"),
    ("Cetes 28 nominal promedio (%)",            "10.3",      "10.7",      "8.9"),
    ("Cetes 28 real acumulada (%)",              "6.7",       "6.7",       "5.6"),
    ("Cuenta corriente (millones de dolares)",   "-14954",    "-7097.5",   "-7941.0"),
    ("Cuenta corriente (% del PIB)",             "-0.7",      "-0.4",      "-0.4"),
    ("PIB EE.UU., crecimiento real (%)",         "1.8",       "2.7",       "2.2"),
    ("Produccion industrial EE.UU. (%)",         "2.0",       "0.5",       "2.0"),
    ("Inflacion EE.UU. promedio (%)",            "2.4",       "2.9",       "2.2"),
    ("SOFR 3 meses promedio (%)",                "4.3",       "5.0",       "3.3"),
    ("Fed Funds Rate promedio (%)",              "4.5",       "5.3",       "3.8"),
    ("Petroleo, precio promedio (dls/barril)",   "56.7",      "70.7",      "57.8"),
    ("Plataforma de produccion (mbd)",           "1983",      "1877",      "1891"),
    ("Plataforma de exportacion (mbd)",          "994",       "900",       "892"),
    ("Plataforma de privados (mbd)",             "86",        "67",        "74"),
    ("Gas, precio promedio (dls/MMBtu)",         "3.5",       "2.2",       "3.1"),
]
emitir("macro_marco.csv", marco,
       ["variable", "aprobado_2024", "estimado_2024", "proyecto_2025"],
       {"cuadro": "C1.1", "documento": "CGPE 2025", "ubicacion": "Anexo II.5, p. 81",
        "tier": "oficial_primaria", "nota": IMG})

# --------------------------------------- C1.2 marco macro de mediano plazo ---
# CGPE 2025, Anexo III.1, p. 84. 2023 observado; 2024-2030 estimado.
ANIOS = ["2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"]
mp = [
    ("PIB, crecimiento real (rango)", "3.2", "[1.5,2.5]", "[2.0,3.0]", "[2.0,3.0]", "[2.0,3.0]", "[2.0,3.0]", "[2.0,3.0]", "[2.0,3.0]"),
    ("PIB nominal (miles de millones de pesos)", "31772.4", "33927.7", "36166.4", "38348.3", "40682.5", "43152.6", "45789.6", "48574.0"),
    ("Deflactor del PIB promedio (%)", "4.5", "4.6", "4.3", "3.5", "3.5", "3.5", "3.5", "3.5"),
    ("Inflacion dic/dic (%)", "4.7", "4.3", "3.5", "3.0", "3.0", "3.0", "3.0", "3.0"),
    ("Inflacion promedio (%)", "5.5", "4.7", "3.8", "3.2", "3.0", "3.0", "3.0", "3.0"),
    ("Tipo de cambio fin de periodo", "16.9", "19.7", "18.5", "18.0", "18.1", "18.3", "18.5", "18.7"),
    ("Tipo de cambio promedio", "17.8", "18.2", "18.7", "18.5", "18.7", "18.9", "19.1", "19.3"),
    ("Cetes 28 nominal fin de periodo (%)", "11.3", "10.0", "8.0", "7.0", "5.5", "5.5", "5.5", "5.5"),
    ("Cetes 28 nominal promedio (%)", "11.1", "10.7", "8.9", "7.4", "6.2", "5.5", "5.5", "5.5"),
    ("Cetes 28 real acumulada (%)", "6.7", "6.7", "5.6", "4.6", "3.2", "2.6", "2.6", "2.6"),
    ("Cetes 28 real fin de periodo (%)", "6.3", "5.4", "4.4", "3.9", "2.4", "2.4", "2.4", "2.4"),
    ("Cetes 28 real promedio (%)", "5.3", "5.7", "4.9", "4.1", "3.1", "2.4", "2.4", "2.4"),
    ("Cuenta corriente (millones de dolares)", "-5476.7", "-7097.5", "-7941.0", "-10359.3", "-10853.3", "-11395.5", "-11974.6", "-12579.2"),
    ("Cuenta corriente (% del PIB)", "-0.3", "-0.4", "-0.4", "-0.5", "-0.5", "-0.5", "-0.5", "-0.5"),
    ("Petroleo, precio promedio (dls/barril)", "70.9", "70.7", "57.8", "61.7", "60.9", "60.5", "60.2", "60.0"),
    ("Plataforma de produccion (mbd)", "1942", "1877", "1891", "1902", "1911", "1921", "1930", "1941"),
    ("Plataforma de exportacion (mbd)", "1032", "900", "892", "883", "875", "866", "858", "850"),
    ("Gas, precio promedio (dls/MMBtu)", "2.5", "2.2", "3.1", "3.6", "3.6", "3.6", "3.4", "3.4"),
]
emitir("macro_medianoplazo.csv", mp, ["variable"] + ANIOS,
       {"cuadro": "C1.2", "documento": "CGPE 2025", "ubicacion": "Anexo III.1, p. 84",
        "tier": "oficial_primaria", "nota": IMG + " 2023 son datos observados."})

# ------------------------------- C4.1 / C12.1 estimacion de finanzas publicas ---
# CGPE 2025, Anexo II.6, p. 82. Millones de pesos y % del PIB, dos bases de 2024.
# La variacion real 2025 vs 2024 la publica el propio cuadro, contra las dos bases.
ff = [
    ("RFSP", "-1864872.3", "-1989921.3", "-1428348.1", "-5.4", "-5.9", "-3.9", "-26.5", "-31.1"),
    ("Recursos financieros extrapresupuestarios", "-171872.3", "-296921.3", "-257781.7", "-0.5", "-0.9", "-0.7", "43.9", "-16.7"),
    ("Balance presupuestario", "-1693000.0", "-1693000.0", "-1170566.5", "-4.9", "-5.0", "-3.2", "-33.7", "-33.7"),
    ("Ingresos presupuestarios", "7328995.2", "7483225.4", "8055649.4", "21.3", "22.1", "22.3", "5.4", "3.3"),
    ("Ingresos petroleros", "1048069.4", "1050436.5", "1142021.5", "3.0", "3.1", "3.2", "4.5", "4.3"),
    ("Ingresos no petroleros", "6280925.8", "6432789.0", "6913627.9", "18.3", "19.0", "19.1", "5.6", "3.1"),
    ("Gobierno Federal (no petroleros)", "5203187.3", "5256295.9", "5670839.1", "15.1", "15.5", "15.7", "4.5", "3.5"),
    ("Tributarios", "4941540.8", "4931100.0", "5296426.4", "14.4", "14.5", "14.6", "2.8", "3.0"),
    ("No tributarios", "261646.5", "325195.9", "374412.7", "0.8", "1.0", "1.0", "37.3", "10.4"),
    ("Organismos y empresas", "1077738.5", "1176493.1", "1242788.8", "3.1", "3.5", "3.4", "10.6", "1.3"),
    ("Gasto neto pagado", "9021995.2", "9176225.4", "9226215.8", "26.2", "27.0", "25.5", "-1.9", "-3.6"),
    ("Gasto programable pagado", "6451161.3", "6676688.8", "6451831.3", "18.8", "19.7", "17.8", "-4.1", "-7.3"),
    ("Diferimiento de pagos", "-44050.6", "-44050.6", "-75800.0", "-0.1", "-0.1", "-0.2", "65.1", "65.1"),
    ("Gasto programable devengado", "6495211.9", "6720739.4", "6527631.3", "18.9", "19.8", "18.0", "-3.6", "-6.8"),
    ("Gasto no programable", "2570833.8", "2499536.6", "2774384.5", "7.5", "7.4", "7.7", "3.5", "6.5"),
    ("Costo financiero", "1263994.1", "1227881.6", "1388373.6", "3.7", "3.6", "3.8", "5.4", "8.5"),
    ("Participaciones", "1262789.1", "1239604.3", "1340210.9", "3.7", "3.7", "3.7", "1.8", "3.7"),
    ("Adefas", "44050.6", "32050.6", "45800.0", "0.1", "0.1", "0.1", "-0.3", "37.1"),
    ("Balance primario presupuestario", "-429005.9", "-465118.3", "217807.2", "-1.2", "-1.4", "0.6", "", ""),
    ("SHRFSP", "16787906.1", "17440245.8", "18591005.5", "48.8", "51.4", "51.4", "6.2", "2.3"),
]
emitir("finanzas_publicas.csv", ff,
       ["concepto", "mdp_2024_aprobado", "mdp_2024_estimado", "mdp_2025",
        "pib_2024_aprobado", "pib_2024_estimado", "pib_2025",
        "var_real_vs_aprobado", "var_real_vs_estimado"],
       {"cuadro": "C4.1 y C12.1", "documento": "CGPE 2025", "ubicacion": "Anexo II.6, p. 82",
        "tier": "oficial_primaria",
        "nota": IMG + " La columna % del PIB de 2024 aprobado usa el PIB estimado en el CGPE 2024."})

# --------------------------- C12.2 perspectivas de finanzas publicas 2024-2030 ---
# CGPE 2025, Anexo III.2, p. 85. Todo en % del PIB. Dos bases para 2024.
COLS = ["2024_aprobado", "2024_estimado", "2025", "2026", "2027", "2028", "2029", "2030", "dif_2025_2030"]
pf = [
    ("I. RFSP", "-5.4", "-5.9", "-3.9", "-3.2", "-2.9", "-2.9", "-2.9", "-2.9", "1.1"),
    ("II. Necesidades de financiamiento fuera del presupuesto", "-0.5", "-0.9", "-0.7", "-0.5", "-0.5", "-0.5", "-0.5", "-0.5", "0.2"),
    ("Pidiregas", "-0.1", "0.0", "-0.1", "-0.1", "-0.1", "-0.1", "-0.1", "-0.1", "0.0"),
    ("Requerimientos financieros del IPAB", "-0.1", "0.0", "-0.1", "-0.1", "-0.1", "-0.1", "-0.1", "-0.1", "0.0"),
    ("Requerimientos financieros del Fonadin", "-0.1", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.0", "0.1"),
    ("Adecuaciones a registros presupuestarios", "-0.2", "-0.8", "-0.4", "-0.3", "-0.3", "-0.3", "-0.3", "-0.3", "0.1"),
    ("III. Balance presupuestario", "-4.9", "-5.0", "-3.2", "-2.7", "-2.4", "-2.4", "-2.4", "-2.4", "0.9"),
    ("III.A Ingresos presupuestarios", "21.3", "22.1", "22.3", "22.2", "22.1", "22.0", "21.9", "21.8", "-0.5"),
    ("Petroleros", "3.0", "3.1", "3.2", "3.1", "3.1", "3.0", "3.0", "3.0", "-0.2"),
    ("Petroleros, Gobierno Federal", "0.8", "0.6", "0.8", "0.9", "0.9", "0.9", "0.9", "0.9", "0.1"),
    ("Petroleros, Pemex", "2.2", "2.5", "2.4", "2.2", "2.1", "2.1", "2.1", "2.1", "-0.3"),
    ("No petroleros", "18.3", "19.0", "19.1", "19.1", "19.0", "18.9", "18.9", "18.8", "-0.3"),
    ("No petroleros, Gobierno Federal", "15.1", "15.5", "15.7", "15.7", "15.6", "15.5", "15.5", "15.4", "-0.3"),
    ("Tributarios", "14.4", "14.5", "14.6", "14.6", "14.6", "14.5", "14.5", "14.4", "-0.2"),
    ("No tributarios", "0.8", "1.0", "1.0", "1.0", "1.0", "1.0", "1.0", "1.0", "0.0"),
    ("Organismos y empresas", "3.1", "3.5", "3.4", "3.4", "3.4", "3.4", "3.4", "3.4", "0.0"),
    ("IMSS e ISSSTE", "1.8", "2.0", "1.9", "1.9", "1.9", "1.9", "1.9", "1.9", "0.0"),
    ("CFE", "1.3", "1.5", "1.5", "1.5", "1.5", "1.5", "1.5", "1.5", "0.0"),
    ("III.B Gasto neto pagado", "26.2", "27.0", "25.5", "24.9", "24.4", "24.3", "24.2", "24.1", "-1.4"),
    ("Gasto programable pagado", "18.8", "19.7", "17.8", "18.0", "18.0", "17.9", "17.9", "17.8", "0.0"),
    ("Diferimiento de pagos", "-0.1", "-0.1", "-0.2", "-0.1", "-0.1", "-0.1", "-0.1", "-0.1", "0.1"),
    ("Gasto programable devengado", "18.9", "19.8", "18.0", "18.1", "18.1", "18.0", "18.0", "17.9", "-0.1"),
    ("Gasto de operacion", "15.7", "16.1", "15.3", "15.4", "15.7", "15.6", "15.6", "15.6", "0.3"),
    ("Servicios personales", "5.1", "5.1", "4.7", "4.7", "4.7", "4.7", "4.7", "4.7", "0.0"),
    ("Otros de operacion", "3.5", "3.9", "3.0", "2.6", "2.6", "2.5", "2.5", "2.5", "-0.5"),
    ("Subsidios", "2.7", "2.7", "3.0", "3.5", "3.7", "3.7", "3.6", "3.5", "0.5"),
    ("Pensiones y jubilaciones", "4.4", "4.4", "4.5", "4.6", "4.6", "4.7", "4.8", "4.8", "0.3"),
    ("Gasto de capital", "3.2", "3.7", "2.8", "2.7", "2.4", "2.4", "2.4", "2.4", "-0.4"),
    ("Inversion fisica", "2.7", "3.0", "2.3", "2.4", "2.0", "2.1", "2.0", "2.0", "-0.3"),
    ("Inversion financiera", "0.5", "0.7", "0.4", "0.3", "0.3", "0.3", "0.3", "0.3", "-0.1"),
    ("Gasto no programable", "7.5", "7.4", "7.7", "6.9", "6.5", "6.5", "6.3", "6.3", "-1.4"),
    ("Costo financiero", "3.7", "3.6", "3.8", "3.2", "2.8", "2.8", "2.7", "2.7", "-1.1"),
    ("Participaciones", "3.7", "3.7", "3.7", "3.5", "3.5", "3.5", "3.5", "3.5", "-0.2"),
    ("Adefas", "0.1", "0.1", "0.1", "0.1", "0.1", "0.1", "0.1", "0.1", "0.0"),
    ("IV. Balance primario", "-1.2", "-1.4", "0.6", "0.5", "0.5", "0.4", "0.4", "0.4", "-0.2"),
    ("SHRFSP", "48.8", "51.4", "51.4", "51.4", "51.4", "51.4", "51.4", "51.4", "0.0"),
    ("SHRFSP interno", "37.4", "38.5", "39.8", "40.5", "40.8", "41.1", "41.4", "41.7", "1.9"),
    ("SHRFSP externo", "11.4", "12.9", "11.6", "10.9", "10.6", "10.3", "10.0", "9.7", "-1.9"),
    ("Deuda neta del Sector Publico", "48.7", "51.0", "50.9", "50.9", "50.9", "50.9", "50.9", "50.9", "0.0"),
    ("Deuda neta interna", "37.1", "37.9", "39.2", "40.0", "40.4", "40.8", "41.1", "41.5", "2.3"),
    ("Deuda neta externa", "11.5", "13.1", "11.7", "10.9", "10.5", "10.1", "9.8", "9.4", "-2.2"),
    ("Saldo historico de la deuda bruta del SPNF", "52.9", "54.9", "54.9", "54.9", "54.9", "54.9", "54.9", "54.9", "0.0"),
    ("Limite maximo de gasto corriente estructural", "9.8", "10.1", "10.1", "10.1", "10.1", "10.1", "10.1", "10.1", "0.0"),
]
emitir("perspectivas_2024_2030.csv", pf, ["concepto"] + COLS,
       {"cuadro": "C1.2 y C12.2", "documento": "CGPE 2025", "ubicacion": "Anexo III.2, p. 85",
        "tier": "oficial_primaria",
        "nota": IMG + " Todo en % del PIB. Signo (+) superavit, (-) deficit."})

print("emitidos: macro_marco, macro_medianoplazo, finanzas_publicas, perspectivas_2024_2030")
