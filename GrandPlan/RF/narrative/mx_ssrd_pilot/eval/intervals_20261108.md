# MX-SSRD Fase 0: intervalos de credibilidad para las métricas

8 de noviembre de 2026. Addendum a `report_20261031.md`. Bootstrap bayesiano (Rubin 1981; Andrews, Moon y Shapiro 2026) con el documento como unidad de muestreo: 10 documentos evaluados, 4000 réplicas, semilla 20261108. Cada documento recibe un peso Exp(1) por réplica; ningún documento se descarta. Intervalos: cuantiles 2.5 y 97.5 %. Figura: `eval/figures/bb_metrics.png`. Código: `src/bootstrap_eval.py`.

## Métricas principales

| Medida | Puntual | IC 95 % bayesiano | IC 80 % | Normal ingenua (episodios independientes) | Distancia p-p |
|---|---|---|---|---|---|
| Exhaustividad, todos | 0.28 | [0.17, 0.42] | [0.21, 0.38] | [0.14, 0.42] | 0.06 |
| Exhaustividad, núcleo | 0.38 | [0.23, 0.60] | [0.27, 0.52] | [0.20, 0.56] | 0.07 |
| Precisión | 1.00 | degenerado | degenerado |  |  |
| Exactitud por campo, todos | 0.65 | [0.62, 0.69] | [0.63, 0.67] |  |  |
| Exactitud por campo, con contenido | 0.60 | [0.55, 0.67] | [0.56, 0.64] |  |  |
| Citas que fallan la verificación | 0.35 | [0.25, 0.46] | [0.28, 0.42] | [0.29, 0.41] | 0.32 |
| Registros con campos sin cita ni marca | 0.75 | [0.51, 0.92] | [0.59, 0.87] | [0.54, 0.96] | 0.04 |

La distancia p-p es la de Andrews y Shapiro (2026): suma de la mayor desviación positiva y la mayor negativa entre la función de distribución del bootstrap y la de la aproximación normal; 0 es coincidencia exacta.

## Chequeo de réplicas suficientes (regla de mitades del artículo)

| Medida | IC 95 %, primera mitad | IC 95 %, segunda mitad |
|---|---|---|
| Exhaustividad, todos | [0.17, 0.42] | [0.17, 0.43] |
| Exhaustividad, núcleo | [0.23, 0.60] | [0.22, 0.60] |
| Exactitud por campo, con contenido | [0.55, 0.67] | [0.55, 0.68] |
| Citas que fallan la verificación | [0.25, 0.46] | [0.25, 0.46] |

## Tamaño de la Fase 1

Documentos necesarios para que la semianchura del IC 95 % baje al valor indicado, si los documentos nuevos dispersan como estos diez. La regla es la escala 1/√D de la varianza posterior; es una aproximación y, como el prompt de Etapa 1 se ajustó dentro de muestra, es optimista.

| Medida | Semianchura hoy | D para ±0.10 | D para ±0.05 |
|---|---|---|---|
| Exhaustividad, todos | ±0.12 | 16 | 63 |
| Exhaustividad, núcleo | ±0.19 | 35 | 140 |
| Exactitud por campo, con contenido | ±0.06 | 4 | 16 |

## Por campo, casos con contenido en *silver*

| Campo | n | Puntual | IC 95 % bayesiano |
|---|---|---|---|
| `coverage_change` | 1 | 0.00 | degenerado |
| `implicit_liability_direction` | 8 | 0.12 | [0.01, 0.26] |
| `benefit_change` | 4 | 0.25 | [0.01, 0.69] |
| `Is the legislated pension reform minor or major?` | 11 | 0.27 | [0.07, 0.56] |
| `instrument_type` | 11 | 0.36 | [0.09, 0.72] |
| `regime_affected` | 11 | 0.39 | [0.15, 0.74] |
| `implementation_date` | 11 | 0.46 | [0.21, 0.77] |
| `Pension Reform Types` | 11 | 0.50 | [0.29, 0.70] |
| `reason_reform` | 2 | 0.50 | degenerado |
| `insurance_branch` | 11 | 0.50 | [0.27, 0.70] |
| `Reform_category` | 10 | 0.60 | [0.24, 0.87] |
| `reform_coverage` | 11 | 0.64 | [0.39, 0.84] |
| `Social_insurance_change` | 9 | 0.89 | [0.60, 1.00] |
| `legislation_date` | 11 | 0.91 | [0.73, 1.00] |
| `entry_into_force_date` | 11 | 0.91 | [0.67, 1.00] |
| `Status of Pension Reform` | 11 | 0.95 | [0.83, 1.00] |
| `Contribution_rate_change` | 1 | 1.00 | degenerado |
| `financing_indexation_change` | 1 | 1.00 | degenerado |
| `dof_publication_date` | 11 | 1.00 | degenerado |
| `indexation_change` | 0 | | |
| `retirement_age_change` | 0 | | |
| `Planned_date` | 0 | | |
| `announcement_date` | 0 | | |
| `reversal_date` | 0 | | |

## Lectura

- **La exhaustividad no está medida, está acotada.** Con diez documentos el IC 95 % de la exhaustividad va de 0.17 a 0.42 (núcleo: 0.23 a 0.60). El intervalo normal que trata los 39 episodios como independientes casi coincide (distancia p-p 0.06); la diferencia es la forma: la posterior es asimétrica a la derecha y su piso es más alto. Aquí el conglomerado por documento no ensancha, pero tampoco había razón para esperar que lo hiciera: la variación entre documentos (de 0 de 4 en el 09 a 1 de 1 en el 05) ya es la que domina.
- **Donde la normal sí engaña: las citas.** La proporción de citas que fallan la verificación literal es 0.35 con IC bayesiano [0.25, 0.46]; la normal sobre 270 citas independientes da [0.29, 0.41] y la distancia p-p es 0.32. Las citas fallan por documento, no por cita: las elisiones se concentran en unos pocos registros largos. Es el caso del ejemplo A del artículo, en el que el intervalo que se debe reportar es el del bootstrap.
- **Lo que sí sobrevive al intervalo.** Ni el límite superior de la exhaustividad (0.42) ni el de la exactitud por campo con contenido (0.67) alcanzan un nivel útil para construir la base; la cota inferior de citas que fallan (0.25) sigue por encima del límite de paro de 0.10. La recomendación «ajustar» se sostiene con incertidumbre explícita; «parar» no se puede descartar ni afirmar con esta muestra.
- **Precisión 1.00 es degenerada, no precisa.** Cada episodio del modelo emparejó con alguno de *silver* en todos los documentos, así que el bootstrap no puede moverla. Es el aviso del artículo: el bootstrap cuantifica el muestreo, no el diseño del emparejamiento, que ya el reporte llamó generoso.
- **Los campos de juicio no tienen muestra.** Dirección del pasivo, cobertura y beneficios tienen entre 1 y 8 casos con contenido; sus intervalos cubren casi todo el rango o son degenerados. Las cifras 0.13, 0.00 y 0.25 del reporte son ilustrativas, no estimaciones.
- **Tamaño de la Fase 1.** Para que la exhaustividad tenga una semianchura de ±0.10 hacen falta del orden de 16 documentos; para ±0.05, 63. Eso dimensiona el *silver* fuera de muestra que piden Beth y Héctor en el punto 4 de «Qué ajustar».
