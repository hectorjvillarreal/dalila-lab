#!/usr/bin/env python3
"""Genera todos los cuadros LaTeX del documento 2026 desde datos/."""
import sys
from pathlib import Path
import pandas as pd
sys.path.insert(0, str(Path(__file__).resolve().parent))
from tablas import cuadro, leer, SALIDA

hechos = []
def C(*a, **k): hechos.append(cuadro(*a, **k))

# --- 1 macro
m = leer("macro_marco.csv")
C("C1_1", "Marco macroeconómico: aprobado 2025, estimado 2025 y proyecto 2026", m,
  ["variable", "aprobado_2025", "estimado_2025", "proyecto_2026"],
  ["Variable", "Aprobado 2025", "Estimado 2025", "Proyecto 2026"], [1,1,1,1],
  "Fuente: CGPE 2026, Anexo II.5, p. 83. Elaborado por el ITED.")
mp = leer("macro_medianoplazo.csv")
C("C1_2", "Mediano plazo 2025--2031", mp,
  ["variable","e2025","p2026","2027","2028","2029","2030","2031"],
  ["Variable","2025 e","2026 p","2027","2028","2029","2030","2031"], [1]*8,
  "Fuente: CGPE 2026, Anexos III.1 p. 86 y III.2 p. 87. Elaborado por el ITED.")

# --- 2 ingresos
i = leer("ingresos_art1o.csv")
C("C2_1", "Ingresos por renglón del artículo 1o.: iniciativa 2025 contra iniciativa 2026 (línea P)", i,
  ["concepto","mdp_2025_ilif","mdp_2026_ilif","dif_nominal","dif_real","var_real_pct","pct_pib_2026"],
  ["Concepto","ILIF 2025","ILIF 2026","Dif. nominal","Dif. real","Var. real \\%","\\% PIB 2026"],
  [1,1,1,1,1,2,2],
  "Línea P: ex ante contra ex ante. Ambas columnas son iniciativa, no ley aprobada. Millones de pesos corrientes; "
  "la diferencia real usa el deflactor del PIB de 4.8 por ciento que declara el CGPE 2026. "
  "Fuente: ILIF 2026 e ILIF 2025, artículo 1o. Elaborado por el ITED.",
  align="p{5.4cm}rrrrrr")

# --- 3 finanzas publicas
f = leer("finanzas_publicas.csv")
C("C4_1", "Estimación de las finanzas públicas 2025--2026", f,
  ["concepto","mdp_2025_aprobado","mdp_2025_estimado","mdp_2026","pct_pib_2025_aprobado","pct_pib_2026"],
  ["Concepto","2025 aprob.","2025 estim.","2026","\\% PIB 25a","\\% PIB 26"], [1,1,1,1,1,1],
  "Fuente: CGPE 2026, Anexo II.6, p. 84. El renglón del primario está rotulado «económico» en 2026 y "
  "«presupuestario» en el CGPE 2025: difieren en 500.0 millones, que son el balance no presupuestario. "
  "Elaborado por el ITED.", align="lrrrrr")

# --- ramos
r = leer("gasto_ramos.csv")
r = r[r.mdp_2026 > 3000].copy()
C("C4_2", "Gasto bruto por ramo, líneas P y G (ramos con más de 3 mil millones en 2026)", r,
  ["nombre","mdp_2025_proyecto","mdp_2026","var_real_pct_P","mdp_2025_aprobado","var_real_pct_G"],
  ["Ramo","Proy. 2025","Proy. 2026","Var. real P","Aprob. 2025","Var. real G"], [1,1,1,1,1,1],
  "Línea P: proyecto 2026 contra proyecto 2025. Línea G: proyecto 2026 contra aprobado 2025. "
  "Nunca se mezclan en una misma columna. Bruto, antes del neteo del Anexo 1. "
  "Fuente: analíticos del proyecto 2025 y 2026 y del PEF aprobado 2025. Elaborado por el ITED.",
  align="p{4.9cm}rrrrr")

fu = leer("gasto_funcional.csv"); fu = fu[fu.mdp_2026 > 20000]
C("C4_3", "Gasto bruto por finalidad y función (línea P)", fu,
  ["nombre","mdp_2025_proyecto","mdp_2026","dif_nominal","dif_real","var_real_pct","pct_pib_2026"],
  ["Función","Proy. 2025","Proy. 2026","Dif. nom.","Dif. real","Var. real \\%","\\% PIB"],
  [1,1,1,1,1,2,2],
  "Fuente: analíticos del proyecto por función, 2025 y 2026. Elaborado por el ITED.",
  align="p{4.6cm}rrrrrr")

ob = leer("gasto_obligatorios.csv")
C("C4_4", "Gastos obligatorios con y sin pensiones, y el agregado que su diferencia adjudica", ob,
  ["concepto","mdp_2025_proyecto","mdp_2026","dif_nominal","dif_real","var_real_pct","pct_pib_2026"],
  ["Concepto","Proy. 2025","Proy. 2026","Dif. nom.","Dif. real","Var. real \\%","\\% PIB"],
  [1,1,1,1,1,2,2],
  "La diferencia entre los dos primeros renglones es el agregado de pensiones y jubilaciones de la "
  "clasificación económica. Es una fuente independiente que adjudica el perímetro y no una elección "
  "metodológica. Fuente: Anexo 3 del proyecto de decreto de 2026 y de 2025. Elaborado por el ITED.",
  align="p{5.2cm}rrrrrr")

g = leer("gce_limite.csv")
C("C4_5", "Gasto corriente estructural contra su límite máximo, 2026", g,
  ["concepto","mdp_2025","mdp_2026"], ["Concepto","2025","2026"], [1,1],
  "El límite máximo no es un porcentaje del PIB: se construye del gasto corriente estructural devengado "
  "de la Cuenta Pública de 2024 y de los deflactores, con un crecimiento real de 2.05 por ciento contra un "
  "PIB potencial de 2.11. El punto de 2025 exige el límite que propuso el CGPE de ese año y no se construye. "
  "Fuente: Anexo 2 del proyecto de decreto y CGPE 2026, p. 33. Elaborado por el ITED.",
  align="p{7.4cm}rr")

# --- rubros
for idc, arch, tit in (("C5_1","salud_ramo.csv","Función Salud por ramo y entidad, bruta (línea P)"),
                       ("C6_1","educacion_ramo.csv","Función Educación por ramo, bruta (línea P)")):
    d = leer(arch); d = d[d.mdp_2026.notna()]
    C(idc, tit, d, ["nombre","mdp_2025_proyecto","mdp_2026","dif_nominal","dif_real","var_real_pct"],
      ["Ramo o entidad","Proy. 2025","Proy. 2026","Dif. nom.","Dif. real","Var. real \\%"], [1,1,1,1,1,1],
      "Bruto, de los analíticos por función. Fuente: analíticos del proyecto 2025 y 2026. Elaborado por el ITED.",
      align="p{6.2cm}rrrrr")

p = leer("pensiones_no_contributivas.csv")
C("C7_1", "Pensiones no contributivas por número de programa (línea P)", p,
  ["nombre","clave","mdp_2025_proyecto","mdp_2026","var_real_pct"],
  ["Programa","Clave 25 → 26","Proy. 2025","Proy. 2026","Var. real \\%"], [1,1,1,1,1],
  "Se selecciona por el número de tres dígitos y no por el código completo: la Pensión Mujeres Bienestar "
  "pasa de U316 a S316 y un filtro por código completo la pierde. Fuente: analíticos del proyecto. "
  "Elaborado por el ITED.", align="p{5.8cm}p{2.2cm}rrr")

s = leer("seguridad_subfuncion.csv")
C("C9_1", "Perímetro de seguridad: quince subfunciones de cinco funciones (línea P)", s,
  ["clave","mdp_2025_proyecto","mdp_2026","dif_nominal","var_real_pct"],
  ["Subfunción","Proy. 2025","Proy. 2026","Dif. nominal","Var. real \\%"], [1,1,1,1,1],
  "En 2026 la Guardia Nacional pasa del Ramo 36 al Ramo 07 y con ella la subfunción 1.7.3. El perímetro "
  "la absorbe sin cambio; el reparto entre civil y militar no. Fuente: analíticos del proyecto. "
  "Elaborado por el ITED.")

a = leer("ambiente_agua.csv")
C("C11_1", "Perímetro de medio ambiente y agua, enumerable (línea P)", a,
  ["concepto","mdp_2025_proyecto","mdp_2026","dif_nominal","dif_real","var_real_pct","pct_pib_2026"],
  ["Concepto","Proy. 2025","Proy. 2026","Dif. nom.","Dif. real","Var. real \\%","\\% PIB"],
  [1,1,1,1,1,2,2],
  "El abastecimiento de agua NO está en la función de protección ambiental sino en la de vivienda y "
  "servicios a la comunidad. Las dos partes se presentan etiquetadas por separado y nunca como una sola "
  "función. Fuente: analíticos del proyecto por función. Elaborado por el ITED.",
  align="p{6.0cm}rrrrrr")

t = leer("transversales.csv")
C("C12_1", "Anexos transversales del proyecto 2026", t,
  ["transversal","MDP","pct_del_etiquetado","pct_programable"],
  ["Anexo","Millones","\\% del etiquetado","\\% del programable"], [1,1,1,1],
  "El total no es dinero adicional: es una suma de etiquetas, y 170 de los 288 programas etiquetados "
  "aparecen en más de un anexo. Fuente: base de anexos transversales del PPEF 2026, datos abiertos de la "
  "Secretaría. Elaborado por el ITED.", align="p{9.6cm}rrr")

ig = leer("transversal_igualdad.csv").head(12)
C("C12_2", "Composición del anexo de igualdad entre mujeres y hombres: los doce programas mayores", ig,
  ["desc_pp","PP_K","MDP","pct_del_anexo"],
  ["Programa","Clave","Millones","\\% del anexo"], [1,1,1,1],
  "El 48.1 por ciento del anexo son programas de pensión. Fuente: base de anexos transversales del PPEF 2026. "
  "Elaborado por el ITED.", align="p{7.6cm}p{1.4cm}rr")

fl = leer("flujos.csv")
C("C13_1", "Los tres flujos, con su nombre correcto", fl,
  ["flujo","mdp_2025_aprobado","mdp_2026","pct_pib_2025","pct_pib_2026"],
  ["Flujo","2025 aprob.","2026","\\% PIB 25","\\% PIB 26"], [1,1,1,1,1],
  "El balance no presupuestario se obtiene por diferencia y vale 500.0 millones en los dos años. "
  "Fuente: CGPE 2026, Anexos II.6 y III.2. Elaborado por el ITED.", align="p{6.0cm}rrrr")

ac = leer("acervos.csv")
C("C13_2", "Los tres acervos", ac,
  ["acervo","mdp_2025_aprobado","mdp_2026","pct_pib_2025_aprobado","pct_pib_2026"],
  ["Acervo","2025 aprob.","2026","\\% PIB 25","\\% PIB 26"], [1,1,1,1,1],
  "Fuente: CGPE 2026, Anexos II.6 y III.2. Elaborado por el ITED.", align="p{6.4cm}rrrr")

te = leer("techos.csv")
C("C13_3", "Techos de endeudamiento, y lo que no es un techo", te,
  ["concepto","fuente","monto","unidad"], ["Concepto","Fuente","Monto","Unidad"], [1,1,1,1],
  "Techo de endeudamiento, déficit y endeudamiento informativo son tres objetos distintos. El techo "
  "interno del Gobierno Federal supera al déficit presupuestario en 27.7 por ciento. "
  "Fuente: ILIF 2026, artículos 2o., 4o. y 6o.; CGPE 2026. Elaborado por el ITED.",
  align="p{7.0cm}p{2.6cm}rl")

de = leer("descomposicion.csv")
C("C13_4", "Descomposición del cambio de la razón SHRFSP a PIB en cuatro variables, con la compensación por inflación como rango", de,
  ["convencion","rfsp_pp","crecimiento_pp","denominador_inflacion_pp","tipo_de_cambio_pp","suma_del_marco_pp","compensacion_pp","inflacion_neta_pp"],
  ["Convención del pago","RFSP","Crecim.","Inflación den.","Tipo cambio","Suma","Compens.","Infl. neta"],
  [2,2,2,2,2,2,2,2],
  "Puntos del PIB. Las cuatro primeras columnas no dependen de la convención y suman el cambio del acervo. "
  "La compensación por inflación pagada NO es un término aditivo del marco: es una lectura del RFSP, y el "
  "paquete no identifica qué índice le corresponde. Se presenta como rango con su cota, nunca como punto. "
  "Elaborado por el ITED con datos del CGPE 2026, Anexos III.1 y III.2.",
  align="p{3.6cm}rrrrrrr")

pc = leer("percapita.csv")
C("C14_1", "Cifras por habitante y por denominador declarado", pc,
  ["indicador","denominador","pesos_2025","pesos_2026","var_real_pct"],
  ["Indicador","Denominador","Pesos 2025","Pesos 2026","Var. real \\%"], [1,1,1,1,1],
  "CUADRO SEPARADO de los presupuestales: ninguna cifra del paquete aparece aquí junto a un denominador "
  "externo sin marca. No se publica el gasto por afiliado a IMSS o ISSSTE ni por alumno matriculado: esos "
  "dos denominadores no se consiguieron. Tier externa demográfica. Fuente: CONAPO, proyecciones de "
  "población a mitad de año, y padrón de IMSS-Bienestar del segundo trimestre de 2025. Elaborado por el ITED.",
  align="p{5.0cm}p{4.4cm}rrr")

dm = leer("demografia_denominadores.csv")
C("C14_2", "Los denominadores demográficos", dm,
  ["denominador","personas_2025","personas_2026"], ["Denominador","2025","2026"], [1,0,0],
  "Fuente: CONAPO, proyecciones de población a mitad de año 1950--2070. Tier externa demográfica. "
  "Elaborado por el ITED.", align="p{7.0cm}rr")

print(f"{len(hechos)} cuadros escritos en capitulos/cuadros/: {', '.join(hechos)}")
