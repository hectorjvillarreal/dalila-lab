---
type: briefing
to: Cath, Anne, Debb
from: Claude (for Héctor)
date: 2026-11-10
subject: "CEESP: la instrucción pedía proyecciones de Naciones Unidas; Héctor las cambió por la proyección propia"
note: GrandPlan/RF/foros_talleres/CEESP_2026-11-11/Villarreal_CEESP_2026-11-11.pdf
related: _crossrefs/_build_instructions/20261111_CEESP_BUILD_beamer-salud-formalizacion_v1.md
commit_at_send: b05a1d5
---

# Core Team — proyecciones de población en presentaciones públicas

**Qué pasó.** La instrucción BUILD-20261111-CEESP-BEAMER v1 pedía dejar sin cambios las láminas 3 y 4 de la base del 22 de septiembre y construir la lámina 5 con «la misma fuente y variante» (WPP 2024, variante media). Así lo construí. Héctor preguntó por qué usar las proyecciones de Naciones Unidas si tenemos mejores, y pidió avisarles. Su regla del 24 de octubre es que las proyecciones salen de datos nacionales y que Naciones Unidas aparece solo como referencia en gris. La instrucción no la recogía y yo no señalé el choque antes de construir.

**Qué se cambió.** Las láminas 3 a 6 y las fuentes usan ahora la proyección propia de México, hecha solo con datos del INEGI (motor `GrandPlan/DFD/outputs/public/2026-10_population_mex_bra_usa/projection_national.py`, escenario central, fecundidad fija en 1.23). Las series están en `datos/l3_nacional.csv` y se generan con `datos/prep_demografia_nacional.py`. El motor reproduce sus totales publicados: 130.9 millones en 2025 y 129.4 en 2050.

| Cifra en pantalla | Antes (Naciones Unidas) | Ahora (proyección propia) |
|---|---|---|
| Población de 65 y más | 10.8 millones en 2024, 25.3 en 2050 | 13.2 millones en 2025, 29.3 en 2050 |
| Año en que hay más personas de 65 y más que menores de 15 | 2051 | 2036 |
| Población de 80 y más | 2.1 a 6.5 millones | 2.7 a 9.1 millones |
| Máximo de la población de 15 a 64 años | 67.9 % en 2030 | 70.1 % en 2034 |
| Población de 15 a 64 años en 2050 | 65.6 % | 64.7 % |
| Población total en 2050 | 148.9 millones | 129.4 millones |
| Horizonte de las gráficas | hasta 2100 | hasta 2050 |

La lámina 4 conserva las cifras de Naciones Unidas (1.91 en 2023, mínimo de 1.66) como contraste, agrega el 1.23 del INEGI para 2024 y quita el 1.44 de zonas urbanas.

## Qué se les pide

**Cath.** Decide cómo queda la instrucción: una v2 que recoja el cambio, o la v1 con esta nota como desviación registrada. Sigue con `endorsed_by` vacío. En las próximas instrucciones, la fuente por defecto para proyecciones de México debería ser la proyección propia.

**Anne.** Revisa las cifras de la tabla antes de que se reutilicen; mañana se muestran en público. Dos puntos para tu criterio:

1. La proyección mantiene la fecundidad en 1.23 hasta 2050. Con ese supuesto, el máximo de la población de 15 a 64 años llega más tarde y más alto que con Naciones Unidas, porque nacen menos niños. La lámina 5 lo dice así.
2. La mortalidad usa el patrón por edad del IBGE ajustado a las defunciones registradas por el INEGI. La lámina de fuentes lo declara. Anclar en la tasa de 65 y más movería la proporción de 2050 alrededor de un punto.

**Debb.** Decide dónde debe vivir la regla para que la vean quienes escriben instrucciones. Hoy solo está en la memoria de trabajo de Claude Code, no en un protocolo ni en `CLAUDE.md`.

## Otras desviaciones de esta construcción

- La base no tiene `.tex` en Dalila. Se reconstruyó a partir del PDF en un solo archivo que compila directo.
- La lámina «Qué mueve la decisión» se omitió: el trabajo para el IMSS no tiene un modelo estimado de elección entre empleo formal e informal.
- La presentación CISS v2 y el artículo de logit condicional con la ENIGH 2022 no están en Dalila.
- La lámina 8 entra por decisión de Héctor, en % del ingreso laboral y con perfil de 2004, no en % del PIB.
- En Infonavit, Héctor resolvió que los 3 puntos se dejan de cobrar, sin la variante en que permanecen en el Instituto.
- Las láminas 13 y 15 llevan la etiqueta del PEF con cifras de CIEP sobre el proyecto; no hay copia del dictamen en Dalila.

La página de revisión con las 39 láminas está en https://claude.ai/artifact/3ePP6JNg3suwAJQ5tGxdKE (privada, de Héctor).
