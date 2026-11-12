---
type: briefing
to: Cath, Anne, Debb
from: Claude (for Héctor)
date: 2026-11-11
subject: "RIUSS: la instrucción pedía WPP 2024 para la región; Héctor eligió una proyección propia con la fecundidad observada"
note: GrandPlan/RF/foros_talleres/CIESS_2026-11-12/Villarreal_RIUSS_2026-11-12.pdf
related: _crossrefs/_build_instructions/20261112_RIUSS_BUILD_beamer-conferencia-magistral_v1.md
previous: _crossrefs/team/cath/20261110_RF_briefing_core-team_proyecciones-nacionales-ceesp.md
---

# Core Team — demografía regional en la conferencia de la RIUSS

**Qué pasó.** La instrucción BUILD-20261112-RIUSS-BEAMER v1 pedía el agregado regional de WPP 2024, variante media, para las láminas de demografía. Es el mismo choque que en la presentación del 11 de noviembre. Esta vez lo señalé antes de construir y Héctor decidió, el 11 de noviembre por la noche, usar una proyección propia de la región. La presentación es el 12 de noviembre a las 9:30.

**Qué se construyó.** `datos/prep_demografia_regional.py` corre el motor regional de `GrandPlan/DFD/outputs/public/2026-09_latam_un_hijo/lac_tfr1_projection.py` (49 países y territorios, grupos quinquenales, pasos de cinco años) con la fecundidad de cada país fija en su último valor observado: los 18 registros de la tabla de Fernández-Villaverde del 15 de septiembre (entrada endosada del corpus), México en 1.23 (INEGI, EIC 2025) y la estimación de Naciones Unidas para 2025 en los demás. La base de México es la EIC 2025. **Fuera de México, la población base, la mortalidad, la migración y el patrón de fecundidad por edad siguen siendo de WPP 2024**; la lámina de fuentes lo declara. Salidas: `datos/r3_region.csv`, `r4_fecundidad.csv`, `r5_ventana.csv`.

| Cifra en pantalla | Proyección propia | Mismo cálculo con la fecundidad de Naciones Unidas |
|---|---|---|
| 65 y más, 2025 y 2050 | 69.9 y 137.8 millones | 68.0 y 137.5 millones |
| Cruce de 65 y más con menores de 15 | hacia 2041 | hacia 2046 |
| 80 y más, 2025 y 2050 | 13.4 y 36.9 millones | 13.0 y 36.7 millones |
| 15 a 64 años, % del total | 67.9 (2025); máximo 68.5 hacia 2035; 65.1 (2050) | 67.7 (2025); 64.5 (2050) |
| Población total, 2050 | 698.6 millones | 729.0 millones (publicado: 730.1) |
| Fecundidad regional ponderada | 1.49 | 1.77 (2025) |
| Años de 10 % a 20 % de 65 y más | alrededor de 27 | 28 |

Héctor pidió además incluir un resultado del documento de trabajo sobre la caída de la fecundidad («Cohort Replacement, Not Cascade», borrador 2). La lámina 5 muestra Costa Rica 1.83 → 1.12 (2010–2024), Colombia 1.7 → 1.1, nacimientos −18 a −47 %, casadas de 20 a 39 años en Colombia 20.7 → 11.9 %, y la conclusión de reemplazo de generaciones. Se cita como documento de trabajo de Villarreal (2026).

## Qué se les pide

**Anne.** Revisa la tabla y el supuesto de fecundidad constante por país antes de que estas cifras se reutilicen. Tres puntos: (1) con pasos de cinco años, los años de cruce y de máximo salen de interpolar; (2) la tabla de registros da 0.99 para Chile y el documento de trabajo 1.03 para 2024, y la lámina 5 evita a Chile por eso; (3) el motor regional da para México un máximo de la población de 15 a 64 años hacia 2040, y el motor nacional lo da en 2034, por lo que México no aparece como línea en la lámina 6. La cautela sobre la TFR de Chile, Costa Rica y México se respetó: no se usó el archivo de línea base ni CELADE.

**Cath.** Decide si la instrucción pasa a v2 o queda la v1 con esta nota como desviación registrada. `endorsed_by` sigue vacío. Otras desviaciones: la presentación de CEPAL no trae cifras regionales de cobertura de pensiones ni fechas de reformas; la presentación en Colombia que hay es la de Cuentas Nacionales de Transferencia y no aportó nada; CISS v2 no está en Dalila. Héctor autorizó usar las fechas que lista la sección 2 sin fuente local. La banda de la lámina de Chile y Colombia no dice que ambas reformas «aumentan la contribución», porque no hay fuente local para el caso colombiano.

**Debb.** La regla sobre proyecciones sigue sin vivir en un protocolo. Con este segundo caso, conviene que la instrucción tipo para presentaciones la incluya. El documento de trabajo citado en pantalla lleva la leyenda «not for circulation»: falta definir cómo se cita en público.
