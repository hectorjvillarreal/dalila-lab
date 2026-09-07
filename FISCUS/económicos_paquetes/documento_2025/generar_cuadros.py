"""Genera todos los cuadros y figuras del documento, en LaTeX y en Markdown,
desde datos/*.csv. Se corre antes de compilar. Ningún capítulo teclea una cifra.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tablas import cuadro, figura

CG = "elaboración propia del ITED con información de la SHCP, CGPE 2025"
AN = "elaboración propia del ITED con los analíticos del PEF aprobado 2024 y 2025"
LIF = "elaboración propia del ITED con la Ley de Ingresos aprobada de 2024 y 2025"
REAL = "Las diferencias en millones de pesos se reportan dos veces, nominal y real; la real está en pesos de 2025 con el deflactor de 4.3% que declara el CGPE."
IMG = "El CGPE 2025 se publicó sin capa de texto; las cifras se leyeron de la página renderizada y se validaron por identidad contable."

R = {"concepto": "Concepto", "mdp_2024": "2024", "mdp_2025": "2025",
     "dif_nominal_mdp": "Dif. nominal", "dif_real_mdp": "Dif. real",
     "var_real_pct": "Var. real \\%"}
COLS = ["concepto", "mdp_2024", "mdp_2025", "dif_nominal_mdp", "dif_real_mdp", "var_real_pct"]

# ------------------------------------------------------------------ cap. 1 ---
cuadro("C1_1", "macro_marco.csv",
       "Marco macroeconómico, 2024--2025", CG + ", Anexo II.5, p.~81",
       renombrar={"variable": "Variable", "aprobado_2024": "2024 aprobado",
                  "estimado_2024": "2024 estimado", "proyecto_2025": "2025"},
       alineacion="lccc", nota=IMG)
cuadro("C1_2", "macro_medianoplazo.csv",
       "Marco macroeconómico de mediano plazo, 2023--2030", CG + ", Anexo III.1, p.~84",
       renombrar={"variable": "Variable"}, alineacion="l" + "c" * 8, nota=IMG)

# ------------------------------------------------------------------ cap. 2 ---
cuadro("C2_1", "ingresos_art1o.csv",
       "Ingresos por renglón del artículo 1o., aprobado 2024 contra aprobado 2025 (mdp)",
       LIF,
       columnas=["clave", "concepto", "mdp_2024_aprobado", "mdp_2025_aprobado",
                 "dif_nominal_mdp", "dif_real_mdp", "var_real_pct", "cambio_de_la_camara_mdp"],
       renombrar={"clave": "Clave", "concepto": "Concepto",
                  "mdp_2024_aprobado": "2024", "mdp_2025_aprobado": "2025",
                  "dif_nominal_mdp": "Dif. nom.", "dif_real_mdp": "Dif. real",
                  "var_real_pct": "Var. real \\%",
                  "cambio_de_la_camara_mdp": "Cámara"},
       alineacion="llSSSSSS", nota=REAL)

# ------------------------------------------------------------------ cap. 3 ---
cuadro("C3_1", "energia_ingresos.csv",
       "El sector energético en el artículo 1o., por vía de entrada (mdp)", LIF,
       columnas=COLS, renombrar=R, nota=REAL)

# ------------------------------------------------------------------ cap. 4 ---
cuadro("C4_1", "finanzas_publicas.csv",
       "Estimación de las finanzas públicas, 2024--2025", CG + ", Anexo II.6, p.~82",
       columnas=["concepto", "mdp_2024_aprobado", "mdp_2025", "pib_2024_aprobado",
                 "pib_2025", "var_real_vs_aprobado"],
       renombrar={"concepto": "Concepto", "mdp_2024_aprobado": "2024 (mdp)",
                  "mdp_2025": "2025 (mdp)", "pib_2024_aprobado": "2024 \\% PIB",
                  "pib_2025": "2025 \\% PIB", "var_real_vs_aprobado": "Var. real \\%"},
       nota=IMG)
cuadro("C4_2", "gasto_ramos.csv",
       "Gasto por ramo del Gobierno Federal, aprobado contra aprobado (mdp)", AN,
       columnas=COLS, renombrar=R, limite=22, nota=REAL)
cuadro("C4_4", "gasto_funcional.csv",
       "Gasto del Gobierno Federal por finalidad y función (mdp)", AN,
       columnas=COLS, renombrar=R, limite=18, nota=REAL)

# ------------------------------------------------------------------ cap. 5 ---
cuadro("C5_1", "pensiones_institucion.csv",
       "Pensiones y jubilaciones por institución (mdp)", AN,
       columnas=COLS, renombrar=R, nota=REAL)

# ------------------------------------------------------------------ cap. 6 ---
cuadro("C6_1", "salud_subsistema.csv",
       "Función Salud por ramo y entidad, en bruto (mdp)", AN,
       columnas=COLS, renombrar=R, nota=REAL)

# ------------------------------------------------------------------ cap. 7 ---
cuadro("C7_1", "educacion_ramo.csv",
       "Función Educación por ramo y subfunción (mdp)", AN,
       columnas=COLS, renombrar=R, nota=REAL)
cuadro("C7_3", "fone_entidad.csv",
       "FONE por entidad federativa (mdp)", AN,
       columnas=COLS, renombrar=R, limite=36, nota=REAL)

# ------------------------------------------------------------ caps. 8 a 11 ---
cuadro("C8_1", "inversion.csv", "Inversión por capítulo de objeto del gasto (mdp)", AN,
       columnas=COLS, renombrar=R, limite=20, nota=REAL)
cuadro("C9_1", "energia_gasto.csv", "Función Combustibles y Energía (mdp)", AN,
       columnas=COLS, renombrar=R, nota=REAL)
cuadro("C9_2", "energia_empresas.csv",
       "Pemex y CFE: por dónde entra y en qué se va (mdp)", AN,
       columnas=COLS, renombrar=R, nota=REAL)
cuadro("C10_1", "seguridad_subfuncion.csv",
       "Perímetro de seguridad, quince subfunciones (mdp)", AN,
       columnas=COLS, renombrar=R, limite=30, nota=REAL)
cuadro("C11_1", "federalizado.csv",
       "Gasto federalizado por vía, fondo y entidad federativa (mdp)", AN,
       columnas=COLS, renombrar=R, limite=48, nota=REAL)

# ----------------------------------------------------------------- cap. 12 ---
cuadro("C12_2", "perspectivas_2024_2030.csv",
       "Perspectivas de finanzas públicas, 2024--2030 (\\% del PIB)",
       CG + ", Anexo III.2, p.~85",
       renombrar={"concepto": "Concepto", "2024_aprobado": "2024 apr.",
                  "2024_estimado": "2024 est.", "dif_2025_2030": "Dif. 25--30"},
       alineacion="l" + "c" * 9, nota=IMG)
cuadro("C12_3", "techos.csv",
       "Techos, endeudamiento y déficit: tres objetos distintos",
       "elaboración propia del ITED con la ILIF y la LIF aprobada, y los decretos",
       renombrar={"objeto": "Objeto", "mdp_2024": "2024", "mdp_2025": "2025",
                  "fuente": "Fuente", "que_es": "Qué es"},
       alineacion="lSSll",
       nota="El renglón externo está en millones de dólares y no se suma con los demás.")
cuadro("C12_4", "descomposicion.csv",
       "Descomposición del cambio de la razón SHRFSPF/PIB en cuatro variables (puntos del PIB)",
       "construcción propia del ITED con el CGPE 2025",
       columnas=["caso", "d_inicial", "d_final", "cambio_observado", "rfspf",
                 "efecto_crecimiento", "efecto_inflacion_denominador",
                 "compensacion_por_inflacion_pagada", "efecto_inflacion_neto",
                 "efecto_tipo_de_cambio", "suma_del_marco", "residuo"],
       renombrar={"caso": "Caso", "d_inicial": "$d_{t-1}$", "d_final": "$d_t$",
                  "cambio_observado": "Obs.", "rfspf": "RFSPF",
                  "efecto_crecimiento": "Crec.",
                  "efecto_inflacion_denominador": "Infl. denom.",
                  "compensacion_por_inflacion_pagada": "Compens.",
                  "efecto_inflacion_neto": "Infl. neta",
                  "efecto_tipo_de_cambio": "Tipo cambio",
                  "suma_del_marco": "Suma", "residuo": "Residuo"},
       nota="Los dos primeros renglones son la prueba de aceptación del marco sobre 2022, "
            "con las dos añadas que estaban en disputa.")

# ----------------------------------------------------------------- cap. 13 ---
cuadro("C13_1", "triada_nta.csv",
       "La tríada de cuentas de transferencias nacionales: los tres vértices",
       AN + " y el CGPE 2025",
       columnas=["vertice", "mdp_2025", "pct_pib_2025", "var_real_pct",
                 "direccion_demografica", "horizonte_en_el_paquete"],
       renombrar={"vertice": "Vértice", "mdp_2025": "2025 (mdp)",
                  "pct_pib_2025": "\\% PIB", "var_real_pct": "Var. real \\%",
                  "direccion_demografica": "Dirección demográfica",
                  "horizonte_en_el_paquete": "¿Horizonte en el paquete?"},
       alineacion="lSSSp{3.2cm}p{4.2cm}")

# --------------------------------------------------- razones estructurales ---
cuadro("CR_1", "razones_estructurales.csv",
       "Comparaciones estructurales del ITED, series con base consistente",
       "elaboración propia del ITED; numerador y denominador en las columnas correspondientes",
       columnas=["capitulo", "razon", "2021", "2022", "2023", "2024", "2025"],
       renombrar={"capitulo": "Cap.", "razon": "Razón"},
       alineacion="cp{5.6cm}ccccc",
       nota="Aprobado contra aprobado en toda la serie. Ninguna línea híbrida. "
            "El punto de 2023 de la razón del capítulo 4 se retira porque no se reproduce.")

print("cuadros generados en capitulos/cuadros/ y markdown/cuadros/")
print("archivos:", len(os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                               "capitulos", "cuadros"))))
