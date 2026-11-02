---
id: 20261101_BDH_N13_evaluacion-informes_v1.0
title: "Evaluación del Informe de Resultados y del Informe de Recomendaciones del Núcleo 13"
type: evaluation
project: BDH
mission: IMSS — Núcleo 13
version: v1.0
date: 2026-11-01
language: es
build_instruction: 20261101_BDH_N13_evaluacion-informes_build_v1.0
inputs:
  - Nucleo13_Informe_Resultados_Oct2026_LIMPIO.docx (sha256 f5f0b711…828bcc)
  - Nucleo13_Informe_Recomendaciones-4.docx (sha256 913a73fc…039aad)
executor: Claude Code (Dalila)
added_by: Beth
endorsed_by: []
status: draft_for_review
---

# Evaluación de los informes del Núcleo 13 (v1)

Insumos: la carpeta `entrega_finales_versiones/` (dos .docx, sin cambios controlados ni comentarios de Word), el cuaderno `reporte_final_28oct.ipynb`, el Informe al Ejecutivo Federal 2025-2026 del IMSS y los anexos técnicos de ITED de los experimentos 1 y 2. Los originales no se modificaron (hash igual antes y después). Las tablas de respaldo están en `tablas/`.

---

## 1. Veredicto

**Informe de Resultados: nivel 2 (cambios mayores).** El modelo, las tablas y el hilo argumental están bien construidos y las cifras del cuerpo son internamente consistentes, pero tres decisiones de método sin cerrar mueven todos los saldos de la sección 6, la brecha Δ(t) se presenta con una trayectoria que el propio texto reconoce como artefacto, y la lista de referencias contiene cuatro obras que no existen.

**Informe de Recomendaciones: nivel 2 (cambios mayores), al borde del 1 en coherencia y fuentes.** Las seis recomendaciones tienen sus siete dimensiones y las 3 a 6 salen de conclusiones del Informe de Resultados, pero la descripción del método (2.2-2.3) corresponde a una versión anterior del modelo, la Recomendación 1 afirma más de lo que el análisis sostiene y descansa en una cita inexistente, y los seis instrumentos normativos siguen entre corchetes.

**Los cinco problemas que más pesan**

1. **Referencias inexistentes.** Arredondo & Aviles (2020), Castañeda-Orjuela & Arbelaez (2021), Lavín & Sosa (2019) y el capítulo de Reddy et al. (2015) en DCP3 no se localizan en ninguna base; sus volúmenes y páginas corresponden a otros artículos. Reddy es la única cita del Informe de Recomendaciones y sostiene la Recomendación 1. Además, 9 de 14 entradas de Resultados no se citan y tres fuentes citadas (CIEP 2025, Informe IMSS 2025-2026, INEGI) no están en la lista. [R14, N-R1, N-C10]
2. **La sección 6 no coincide con los anexos técnicos de ITED.** El saldo de la afiliación subsidiada es 288 mil millones en el informe y 81 mil millones en el anexo del experimento 1; el seguro solidario cubre hasta 2037/2033 en el informe y hasta 2054/2037 en el anexo del experimento 2. La diferencia viene del gasto base (545,271 millones atribuidos al SEM frente a 494,275 del Cuadro V.13), del conteo de derechohabientes (54.7 frente a 79.2 M) y del déficit de GMP (aproximación propia frente al Cuadro V.24). El Informe del IMSS da un déficit de GMP menor que la aproximación (≈74 frente a 89 mil millones en 2027; ≈198 frente a 272 en 2054), así que la frase de 6b.5 va en la dirección contraria. [N-R20, R4, R5, R6]
3. **La brecha Δ(t) proyectada es un artefacto declarado.** Desde 2028 el gasto es 63.55 % de los ingresos totales del IMSS; 5.6 advierte que la brecha negativa 2030-2040 «no debe interpretarse como un excedente», pero la Tabla 5 y la Figura 9 sólo muestran esa trayectoria y el cuaderno entregado se corrió sólo con ese método. [R3]
4. **El Informe de Recomendaciones describe otro modelo.** Horizonte 2024-2040, inflación médica variable, Δ(t) = CT(t) − F(t), seis escenarios y análisis tornado (2.2-2.3); la Recomendación 4 añade una opción no simulada (dejar 3 puntos en el Infonavit) y la 5 atribuye el 3.467 % a la ENIGH. Ninguna cifra que depende de los puntos 2 y 3 lleva rango. [C1-C5, C12, C13, C15]
5. **Restos de edición en los dos entregables.** «[año]», la nota «(Poner todos los títulos de figuras o tablas al final)», texto resaltado, cinco notas rojas «[precisar con la contraparte IMSS]», las Figuras 5 y 10 con leyendas de un esquema de escenarios anterior (E0-E6), el título de la Figura 10 duplicado, el Informe de Recomendaciones sin sección 1 ni números de página, y listas de autores distintas en los dos documentos. [R11, N-R17, N-C9, C17, R16]

**Qué falta para llegar al nivel 4, en orden**

1. Cerrar las tres decisiones de método de la sección 6 (gasto base, conteo, déficit de GMP) y alinear el informe con los anexos de ITED o explicar la diferencia; recalcular 6a, 6b, resumen, 7.1, 8 y las Recomendaciones 3-6.
2. Decidir cómo se presenta Δ(t): dos trayectorias en la Tabla 5 o advertencia en el resumen ejecutivo.
3. Rehacer las dos listas de referencias con sólo lo citado y verificado; quitar el umbral del 15 % y la cita de Reddy.
4. Reescribir 2.2-2.3 y la Recomendación 1 del Informe de Recomendaciones; añadir rangos y salvedades a las cifras que dependen de 1 y 2.
5. Resolver los seis corchetes de la sección 4 con la contraparte del IMSS y correr las fechas (piloto 2028, diseño del catálogo 2027).
6. Pase editorial: marcadores, figuras 5/10 y GIF, títulos huérfanos, siglas, sección 1, numeración, autores.

---

## 2. Tabla de calificaciones

Escala: 4 listo · 3 cambios menores · 2 cambios mayores · 1 no apto. Nivel global = mínimo de D1-D4, ajustable un nivel si el resto es 4.

### Informe de Resultados

| Dim. | Nivel | Justificación (evidencia) |
|---|---|---|
| D1 Coherencia interna de cifras | 3 | Las Tablas 1-6, K.2, J.2 y E.1 suman y los porcentajes se recalculan (89 %/11 %, 2.5 %/2.7 %, −4.0/+5.9 %, 47.2 %, 10.9 %); quedan las leyendas de las Figuras 5 y 10 con escenarios de otra versión, 54.6 frente a 53.63 M en la nota de 6a, «se cruzan alrededor de 2038» frente a «crece más lento a partir de 2028», y un 49.5 % que no se reproduce. |
| D2 Coherencia entre documentos | — | No aplica. |
| D3 Solidez metodológica y honestidad de límites | 2 | Supuestos explícitos y 7.2.1 completo, pero: «queda un saldo sin fuente […] de unos 288 mil millones» (6a.4) frente a 81 mil millones en el anexo ITED; «se atribuye completo al SEM» sin definir el agregado; «el déficit sería mayor y el seguro alcanzaría por menos tiempo» (6b.5) en la dirección contraria al Cuadro V.24; Tabla 5 con una sola trayectoria. |
| D4 Hilo argumental | 3 | Pregunta → método → hallazgos → discusión → conclusiones, con el cambio de objetivo explicado en 3.3 y cada conclusión ligada a un hallazgo («La presión estimada es un límite inferior»). La pregunta de 3.4 no se ajustó al objetivo modificado y 2.3 no recoge las limitaciones que importan. |
| D5 Fuentes y referencias | 1 | Cuatro referencias no localizadas; «Rechel, B., et al. (2009)» frente a «Rechel et al., 2013»; «(IMSS, [año], cuadro A.4)»; umbral del 15 % sin respaldo; cifras internas sin cita. El Cuadro A.4 y el CIEP sí respaldan lo que se les atribuye. |
| D6 Completitud editorial | 2 | «(Poner todos los títulos de figuras o tablas al final)» en la Figura 3; resaltado en 3.3; Figura 10 con dos títulos; Tabla 1, Tabla 6.2 y Figura 10 sin cita; títulos huérfanos (pp. 18, 21, 22); sin índice; dos estilos de tabla; referencias a la «sección 8». |
| D7 Lenguaje | 3 | Registro consistente y lenguaje de tasas legales correcto («Miden tasas legales, no quién paga en los hechos»); Fernández Huerta 68-89 por sección; siglas sin definir (CC/CCM, DIDT, CONAPO, CIEP, SEM-A/GMP); la oración del objetivo en 3.3. |
| D8 Calidad de las recomendaciones | — | No aplica. |
| D9 Requisitos de la Comisión | 3 | No se encontró plantilla en la carpeta. La estructura (introducción, resumen, antecedentes, método, hallazgos, discusión, conclusiones, referencias, anexos) y el Anexo B («conforme a los requisitos del protocolo de la Comisión») sugieren conformidad; falta el cuaderno de ingresos en la entrega. |
| **Global** | **2** | Mínimo de D1, D3 y D4 = 2 (D3). D5 y D6 también están por debajo de 3, así que no procede ajuste. |

### Informe de Recomendaciones

| Dim. | Nivel | Justificación (evidencia) |
|---|---|---|
| D1 Coherencia interna de cifras | 3 | Las cifras de 2.4 y de las justificaciones son consistentes entre sí (288, 47.2 %, 66 → 272, 113 → 280, 13 → 108, 52); la sección 4 dice «dos niveles» y enumera seis; el cronograma tiene una fecha pasada. |
| D2 Coherencia entre documentos | 2 | «horizonte 2024-2040», «distintos supuestos de inflación médica», «Δ(t) = CT(t)−F(t)», «seis escenarios», «tornado» (2.2-2.3); «o permanecerán en Infonavit» (3.4) no simulado; «3.467 % en 2026 con base en la ENIGH» (3.5); «R y Excel 365» (5.1). Las cifras cuantitativas sí coinciden con Resultados. |
| D3 Solidez metodológica | — | No aplica. |
| D4 Hilo argumental | 2 | Las Recomendaciones 3-6 salen de conclusiones de Resultados; la 1 afirma «subestimación del gasto quirúrgico proyectado derivada del uso de métodos de extrapolación sin ajuste demográfico», que Resultados no demuestra (el gasto en trazadores crece menos que los ingresos), y la justifica con Reddy et al. (2015), que no existe. 2.4 mezcla aprendizajes de la Mesa 2 con hallazgos. |
| D5 Fuentes y referencias | 1 | La única cita del texto (Reddy) es un capítulo inexistente; 7 de 8 entradas no se citan; la Síntesis de las Mesas no se cita donde se usa. |
| D6 Completitud editorial | 2 | Sin sección 1; sin números de página; cinco notas rojas «[precisar con la contraparte IMSS]»; título de 3.4 y «el Infonavit.» resaltados; «del seguro los seguros de salud»; 4.3-4.6 en cursiva; lista de autores distinta de Resultados. |
| D7 Lenguaje | 3 | Dos registros («continuo normativo-operativo» frente a «no se paga sola»); sección 4 con 44 palabras por oración; «sin que los patrones paguen más», «que no cueste proporcionalmente más» (incidencia); siglas sin definir (CMTR, PHEDS, MOCE, SIMOIQX, INDOQC, GRD, UMAE, SEM-GMP, ENSANUT). |
| D8 Calidad de las recomendaciones | 2 | Siete dimensiones completas en las seis; pero piloto en el «proceso presupuestal 2027» ya en curso; los seis instrumentos sin identificar; viabilidad por adjetivos; la Recomendación 4 sin su alcance (sin pensiones, IV, RT, Infonavit) y con un actor (Infonavit) ausente de 6.1. |
| D9 Requisitos de la Comisión | 2 | Sigue el esquema de siete dimensiones, instrumento normativo, viabilidad con cuatro criterios y brechas; pero empieza en la sección 2 y 6.1 cubre sólo dos recomendaciones. Plantilla no encontrada. |
| **Global** | **2** | Mínimo de D1, D2 y D4 = 2. D5 = 1 no entra en el mínimo, pero impide la entrega tal cual. |

---

## 3. Estado de los problemas ya identificados

Resumen: Resultados 5 resueltos, 7 parciales, 4 pendientes (16). Recomendaciones 0 resueltos, 3 parciales, 14 pendientes (17). Detalle con evidencia en `tablas/hallazgos.csv` (columna `estado`).

### 3.1 Informe de Resultados

| ID | Estado | Evidencia en la versión actual |
|---|---|---|
| R1 | Resuelto | Un solo conteo (54.7 M); los otros dos como sensibilidad en la Tabla I.3 y 6a.5. Falta el conteo «adscrito» de 63.6 M (N-R23). |
| R2 | Resuelto | Tabla 2 suma por fila; texto y tabla dicen 89.8. |
| R3 | Parcial | Advertencia en 5.6; Tabla 5 y Figura 9 con una sola trayectoria; cuaderno corrido con `METODO_GASTO_BALANCE = "pct"`; 5.6 dice «pendiente» y el Anexo M dice que ambas versiones «se guardan». |
| R4 | Pendiente | Aproximación declarada, sin contraste con V.24 (que da ≈74 mil millones en 2027 frente a 89). |
| R5 | Pendiente | «el déficit sería mayor y el seguro alcanzaría por menos tiempo» (6b.5); la dirección es la contraria. |
| R6 | Parcial | «se atribuye completo al SEM», sin decir qué incluye; V.13 da 494,275 de prestaciones en especie en 2026. |
| R7 | Parcial | Cada sección declara su supuesto; la diferencia no se nombra. |
| R8 | Pendiente | «(secciones 5.6 y 8)» y «La sección 8 señala…»; la 8 es Conclusiones. |
| R9 | Resuelto | 7 Discusión, 8 Conclusiones, un solo texto. |
| R10 | Resuelto | Sin duplicados; dos «27 %» distintos seguidos en 7.2.2 (N-R13). |
| R11 | Parcial | «[año]», nota de edición en la Figura 3, resaltado en 3.3, encabezado vacío al final. |
| R12 | Resuelto | 89/11 y 12.5 % consistentes y recalculables. |
| R13 | Parcial | Explicado en Anexos H y M; evitado en 6b; sin advertencia en Tabla 5, Tabla 6.4 ni conclusiones. |
| R14 | Pendiente | Rechel 2009/2013; cuatro referencias no localizadas; lista y citas no se corresponden. |
| R15 | Parcial | «Diego» desapareció; el resto sigue sin cita. |
| R16 | Parcial / no verificable | Sin comentarios en el archivo; listas de autores distintas; «Act. Luz María» sin apellido. |

### 3.2 Informe de Recomendaciones

| ID | Estado | Evidencia en la versión actual |
|---|---|---|
| C1 | Pendiente | «periodo 2024-2040» (2.2); «horizonte 2024-2040» (2.3). |
| C2 | Pendiente | «distintos supuestos de inflación médica» (2.2). |
| C3 | Pendiente | «Δ(t) = CT(t)−F(t)» (2.3). |
| C4 | Pendiente | «análisis de sensibilidad univariado y multivariado (tornado)» (2.3). |
| C5 | Pendiente | «seis escenarios paramétricos (3 variantes CONAPO × 2 trayectorias)» (2.3). |
| C6 | Pendiente | «El modelo opera en R y Excel 365» (5.1). |
| C7 | Pendiente | «fase piloto en el proceso presupuestal 2027» (3.1). |
| C8 | Pendiente | «sustituyendo el método actual de extrapolación lineal histórica»; Reddy; «Informes Actuariales» (3.1, 5.1). |
| C9 | Parcial | 4.3-4.6 añadidos (en cursiva); «en dos niveles» y «ambas recomendaciones» siguen; 6.1 sin actores de 3-6. |
| C10 | Pendiente | «Octubre 7, 2026» (6.4); «octubre-diciembre 2026» (3.2). |
| C11 | Parcial | 12.5 % ya coincide; 2054/2037/2033 sin advertencia sobre R4. |
| C12 | Parcial | «personas adultas mayores, quienes mayoritariamente pertenecen al SEM-GMP»; «sin que los patrones paguen más»; opción «o permanecerán en Infonavit» nueva y no simulada; alcance sin declarar. |
| C13 | Pendiente | «3.467 % en 2026 con base en la ENIGH»; «que no cueste proporcionalmente más»; «[Confirmar el artículo…]». |
| C14 | Pendiente | «del seguro los seguros de salud»; sin salvedad del costo promedio. |
| C15 | Pendiente | «unos 288 mil millones» (2.4, 3.6) sin el rango 162-288; «66 […] 272 mil millones» (3.4) sin advertencia. |
| C16 | Pendiente | Dos registros; sección 4 con 44 palabras por oración. |
| C17 | Pendiente | Primer encabezado «2. Contexto». |

---

## 4. Problemas nuevos, por severidad

Severidad: bloqueante (invalida un resultado central o una recomendación) · mayor (cambia una cifra o un mensaje) · menor (no cambia cifras ni mensajes) · editorial. No se encontró ninguno que, por sí solo, invalide un resultado central; los tres primeros «mayores» juntos sí cambian las cifras del resumen ejecutivo.

### Mayores

| ID | Documento | Dónde | Problema |
|---|---|---|---|
| N-R20 | Resultados | 6a, 6b, 2.4, 7.1 | Las cifras de 6a/6b no coinciden con los anexos técnicos de ITED (288 frente a 81 mil millones; 2037/2033 frente a 2054/2037; cuidados 20 → 10 frente a 54 → 90; VP 229 frente a 802) por tres elecciones de método no discutidas como alternativas (gasto base, conteo, déficit de GMP). |
| N-R1 | Resultados | 9, 3.2, 3.3 | Lista y citas no se corresponden: 9 de 14 entradas sin citar; CIEP 2025, Informe IMSS 2025-2026 e INEGI sin entrada. Cuatro entradas no existen (ver R14). |
| N-R17 | Resultados | Figuras 5 y 10 | Leyendas con un esquema de escenarios anterior (E0-E6, «Expansión») que no coincide con las Tablas 3 y 6 (E0-E9, «Afiliación»); faltan E7-E9. |
| N-R21 | Resultados | 7.1 | «el gasto en salud crece a una tasa superior al PIB cuando la proporción de adultos mayores supera el 15%» no está en Rechel 2013 ni en el material OCDE 2019 leído. |
| N-C10 | Recomendaciones | 3.1, 7 | La única cita del documento (Reddy et al. 2015, DCP3) no existe; la Recomendación 1 queda sin sustento externo. |
| N-C2 | Recomendaciones | 3.1, 4.1, 5.1 | La Recomendación 1 afirma una subestimación presupuestal que Resultados no demuestra; «horizonte de cinco años» y «la Dirección de Finanzas ha manifestado interés» sin fuente. |

### Menores

| ID | Documento | Dónde | Problema |
|---|---|---|---|
| N-R4 | Resultados | 5.5 / Anexo M | «se cruzan alrededor de 2038: antes el gasto crece más rápido» frente a «crece más lento a partir de 2028». |
| N-R5 | Resultados | Nota de 6a / Anexo I | 54.6 frente a 53.63 millones con IMSS en la ENIGH. |
| N-R6 | Resultados | Nota al pie 1 | La advertencia de que CONAPO subestima la transición (EIC 2025) va en una nota con error gramatical y sin sensibilidad asociada. |
| N-R7 | Resultados | 6a-6c | Horizontes 2054 (6a, 6b) y 2055 (6c, Tabla 6.4). |
| N-R8 | Resultados | 6a.2 / 6a.4 | La cuota fija vale 8,735 (365 días) y 8,065 (337 días) sin explicación. |
| N-R9 | Resultados | varias | Siglas sin definir: CC/CCM, DIDT, CONAPO, CIEP, CIE-9/10, SEM-A/GMP; SSFAM, ENIGH y GRD antes de su definición. |
| N-R11 | Resultados | 2.1, 3.1 | «discrepancia de 49.5%» no se reproduce con 10,536 / 21,259 (49.6 % o 50.4 %). |
| N-R12 | Resultados | 4.2 | La proyección institucional de ingresos 2024-2055 no tiene entrada como fuente. |
| N-R13 | Resultados | 3.1, 7.2.2 | Dos «27 %» distintos (subregistro; registros sin fecha) y dos atribuciones del subregistro (SIMOIQX / jefaturas). |
| N-R14 | Resultados | 2.3 | «Alcance y limitaciones» del resumen es genérico y omite las dos limitaciones que gobiernan la lectura. |
| N-R15 | Resultados | 3.3, 3.4 | Oración del objetivo difícil de seguir; la pregunta de 3.4 no se ajustó al objetivo modificado. |
| N-R16 | Resultados | Anexo B | El cuaderno de ingresos no está en la carpeta de entrega. |
| N-R18 | Resultados | figuras | Figura 3 ilegible; Figuras 4-11 en GIF con leyendas de 5-6 pt; Figura 1 sin fuente ni unidades; F.1/F.2 con leyenda sobre barra, «intenvención», «1e9», «escenario_y»; M.1/M.2 «millones» en el pie y «MMDP» en el eje; 4 = J.1 y 11 = L.1. |
| N-R22 | Resultados | 2.2, 3.1, 4.2, ref. 3 | «CONAPO 2022-2070» / CONAPO (2022); el producto es 2020-2070, publicado en 2023. |
| N-R23 | Resultados | 6a.5, Tabla I.3 | Falta el conteo adscrito (63.6 M) y la aclaración de que 79.2 M es población «potencial». |
| N-C1 | Recomendaciones | 7 | 7 de 8 referencias sin citar; la Síntesis de las Mesas no se cita donde se usa. |
| N-C3 | Recomendaciones | 3.2 | Atribución del 27 % distinta de Resultados 3.1. |
| N-C4 | Recomendaciones | 3.5 | 13 / 108 mil millones presentados como si la calibración del 3.467 % fuera exacta (N.2 dice que en 2026 ya hay 8 mil millones de diferencia). |
| N-C6 | Recomendaciones | 2.3, 3.2, 3.5, 6.2 | Siglas sin definir: CMTR, PHEDS, MOCE, SIMOIQX, INDOQC, GRD, UMAE, SEM-GMP, ENSANUT, CONAPO. |
| N-C7 | Recomendaciones | 5 | Viabilidad por adjetivos; una oración por criterio en 3-6. |
| N-C8 | Recomendaciones | 2.4 | Aprendizajes de la Mesa 2 presentados como hallazgos. |
| N-C9 | Recomendaciones | 4 | Cinco notas rojas de edición; sin números de página. |

### Editoriales

N-R2 (Tabla 1, Tabla 6.2 y Figura 10 sin cita; «Gráfica 2»; título duplicado), N-R3 (jerarquía de encabezados; títulos de figura antes y después), N-R10 (erratas: «FFuente», «Fuente;», «tercer de nivel», «INEGI..», «costosde», «Monroy ,», «se estos resultados»), N-R19 (títulos y encabezados huérfanos, Tabla 5 partida sin cabecera, páginas casi vacías, dos estilos de tabla, sin índice, signo menos como cuadro vacío en el render de LibreOffice [REVISAR en Word]), N-C5 (4.3-4.6 en cursiva, resaltados, «dicha institución .», autores).

---

## 5. Evaluación por sección

### 5.1 Informe de Resultados

| Sección | Evaluación |
|---|---|
| Portada | Dos listas (investigador y colaborador) que no coinciden con las de Recomendaciones; «Act. Luz María» sin apellido; espacio antes de la coma en «Monroy ,». |
| 1. Introducción | Clara y corta: dos presiones, dos partes, fuentes y advertencia de que no son pronósticos. Usa ENIGH, GRD y CONAPO antes de definirlos. |
| Resumen ejecutivo (2.1-2.5) | Los hallazgos cuantitativos están bien jerarquizados y coinciden con el cuerpo (89/11, 1,877 → 3,974, −4/+6 %, 288 mil millones, 2054/2037/2033). 2.3 «Alcance y limitaciones» es genérico. 2.5 no tiene estilo de título. 2.4 adelanta el seguro solidario y el SSFAM sin que el lector sepa aún qué son. |
| 3. Antecedentes | Contexto útil, con las cifras internas sin cita y los dos marcadores que quedan. La Figura 1 no tiene fuente ni unidades. 3.3 explica con honestidad el cambio de objetivo; la oración del objetivo es difícil de seguir. 3.4 formula la pregunta sobre «la atención quirúrgica» cuando la respuesta se da para el SEM completo. |
| 4. Metodología | La parte más sólida: fórmulas, fuentes, conteo de derechohabientes, π_m = 0 y «no se realizó sensibilidad» explícitos. Falta la proyección institucional de ingresos como fuente formal. 4.3.3 declara el supuesto de proporción fija, pero la consecuencia (el signo de Δ(t)) sólo se advierte en 5.6. La nota al pie 1 (EIC 2025) merece estar en el cuerpo. |
| 5. Hallazgos | Tablas 1-6 consistentes y recalculables. 5.5 y Anexo M dan lecturas distintas del cruce de curvas. 5.6 es el punto más delicado: la brecha negativa 2030-2040 se presenta en Tabla 5 y Figura 9 aunque el texto diga que es un artefacto. Las Figuras 5 y 10 llevan leyendas de otra versión del modelo; la 10 tiene el título duplicado y no se cita. |
| 6. Esquemas de financiamiento | Bien estructurada (problema, idea, supuestos, resultados, robustez, lo que no dice, resumen) y con el lenguaje de tasas legales correcto. Depende de tres decisiones de método sin cerrar (R6, R1/Tabla I.3, R4), con la frase de 6b.5 en la dirección contraria (R5), y sus cifras no coinciden con los anexos de ITED (N-R20). Horizontes mixtos y referencias a la «sección 8». |
| 7. Discusión | 7.1 integra bien la Mesa 2 y dice con claridad que las secciones 5 y 6 no están integradas; contiene el umbral del 15 % sin respaldo. 7.2.1 recoge las limitaciones que importan, pero no nombra la diferencia de crecimiento del gasto entre 5 y 6. 7.2.2: dos «27 %» distintos en párrafos consecutivos. |
| 8. Conclusiones | Cinco conclusiones, cada una ligada a un hallazgo; «La presión estimada es un límite inferior» y «El gasto y el ingreso del SEM deben proyectarse con la misma población» sostienen las Recomendaciones 3 y 6. Compara 2025-2055 sin advertir el efecto del último año de la proyección. |
| 9. Referencias | Cuatro entradas inexistentes; lista y citas no se corresponden; edición equivocada del Informe del IMSS. |
| 10. Anexos A-N | Detallados y trazables al cuaderno, con la Tabla I.3 como mejor pieza de transparencia. Las figuras de anexo repiten dos del cuerpo. El Anexo N.2 contiene una aclaración (la calibración del 3.467 % no es exacta) que debería estar en 6a. |

### 5.2 Informe de Recomendaciones

| Sección | Evaluación |
|---|---|
| Portada | Una sola lista de 11 autores, distinta de la de Resultados. |
| 2. Contexto | 2.1 correcto. 2.2 y 2.3 describen un modelo que ya no es el de Resultados. 2.4 mezcla aprendizajes de la Mesa 2 con hallazgos; los hallazgos cuantitativos sí coinciden con Resultados. |
| 3. Recomendaciones 1-2 | Siete dimensiones completas. La 1 excede lo que el análisis sostiene (metodología oficial del presupuesto, «extrapolación lineal», Reddy, piloto 2027) y afirma una subestimación que Resultados no demuestra. La 2 es la mejor fundamentada (Mesa 2, Núcleo 4), con fechas que ya corren. |
| 3. Recomendaciones 3-6 | Siete dimensiones completas y derivadas de conclusiones de Resultados. La 3 es la más directa. La 4 arrastra la aproximación de R4, mantiene lenguaje de incidencia, mezcla pensionados con adultos mayores y añade una opción no simulada. La 5 cita mal la base del 3.467 % y no identifica el artículo de ley. La 6 tiene errata en el título y le falta la salvedad del costo promedio. |
| 4. Instrumento normativo | Cubre las seis, pero la entrada sigue diciendo «dos niveles», 4.3-4.6 van en cursiva y los seis llevan corchetes: ningún instrumento está identificado. 4.1 introduce un «horizonte de cinco años» nuevo. Oraciones de 44 palabras en promedio. |
| 5. Viabilidad | Cuatro criterios por recomendación, con adjetivos y, en 3-6, una oración por criterio. «R y Excel 365» y «la Dirección de Finanzas ha manifestado interés» sin sustento. |
| 6. Brechas y próximos pasos | 6.2 es honesto y coincide con 7.2 de Resultados. 6.1 sólo cubre las recomendaciones 1 y 2. 6.3 bien planteado. 6.4 es el calendario de entrega del Núcleo (con una fecha pasada), no el de implementación. |
| 7. Referencias | Sólo una de ocho se cita en el texto, y no existe. |

---

## 6. Coherencia entre documentos

| Tema | Informe de Resultados | Informe de Recomendaciones | ID |
|---|---|---|---|
| Horizonte | 2025-2055 (4.1) | 2024-2040 (2.2, 2.3) | C1 |
| Inflación médica | π_m = 0 en todos los escenarios (4.3.1) | «distintos supuestos de inflación médica» (2.2) | C2 |
| Brecha | Δ(t) = G(t) − F(t), G = gasto corriente en salud (4.3.3) | Δ(t) = CT(t) − F(t) (2.3) | C3 |
| Sensibilidad | Denominador poblacional; «no se realizó» sobre costo, inflación ni tasas (4.5) | «univariado y multivariado (tornado)» (2.3) | C4 |
| Escenarios | Nueve (3 × 3) más base (4.4) | Seis (3 × 2) (2.3) | C5 |
| Herramientas | Cuadernos de Python, PostgreSQL (Anexo B) | «R y Excel 365» (5.1) | C6 |
| Seguro solidario, 3 puntos restantes | «se dejan de cobrar; la tasa legal baja 3 puntos» (6b.2) | «se dejarían de cobrar o permanecerán en Infonavit» (3.4) | C12 |
| Base del 3.467 % | Calibrado con los ingresos de GMP de la proyección institucional (N.2) | «con base en la ENIGH» (3.5) | C13 |
| Subregistro de 27 % | Comparación con SIMOIQX (3.1); «respecto a los reportes de jefaturas» (7.2.2) | «entre SIMOIQX y los reportes de jefaturas» (3.2) | N-C3 |
| Saldo de la afiliación subsidiada | 288 mil millones, con rango 162-288 según conteo (6a.5) | 288 sin rango (2.4, 3.6) | C15 |
| Déficit de GMP | Aproximación declarada (6b.1) | 66 → 272 sin advertencia (3.4, 5.4) | C15, C11 |
| Efecto de 3 M de cotizantes | «Solo considera la atención médica del SEM» (N.2) | Sin salvedad (3.6) | C14 |
| Recaudación de la cuota proporcional | Diferencia de 8 mil millones ya en 2026 (N.2) | «que recaude lo mismo en 2026» (3.5) | N-C4 |
| Horizonte de presupuestación | — | «cinco años» (4.1), no está en Resultados | N-C2 |
| Lenguaje | Tasas legales («Miden tasas legales, no quién paga en los hechos») | Incidencia («sin que los patrones paguen más», «que no cueste proporcionalmente más») | C12, C13 |
| Autores | 7 + 4 (dos listas) | 11 (una lista); «Dra. Judith S. Méndez M.» | R16 |
| Cifras que sí coinciden | 1,877 → 3,974; 89 %; 3.6 mil millones (0.7 %); 22.4 → 46.8 M; 41 → 67 %; 3.5 %; 47.2 %; 2054/2037/2033; 113/280; 66/272; 13/108; 7.6 %; 8.6 %; 29 %; 10.9 %; 52 | — |

### Magnitudes clave (resumen de `tablas/cifras.csv`)

| Magnitud | Valores encontrados | Consistente |
|---|---|---|
| Derechohabientes 2025 | 54.7 / 54.65 M (cuerpo, Tablas 3, I.2, I.3, J.2); 70.7 y 79.2 M como sensibilidad; ENIGH 53.63 M (Anexo I) frente a 54.6 M (nota 6a) | Sí, salvo la nota de 6a |
| Derechohabientes 2055 | 61.5 / 61.46 M; +12.5 % | Sí |
| Gasto en trazadores 2025 / 2055 | 1,877 / 3,974.1 M; 2.5 % anual; 2.1 veces | Sí (en los dos documentos) |
| Envejecimiento / tamaño | 89 % / 11 %; 1,864 / 234 M | Sí |
| Ingresos del SEM 2025 / 2055 | 541.6 / 1,215.3 mil millones; 2.7 % anual; 2.2 veces | Sí; no coincide con V.11 del Informe (538.0) por perímetro |
| Brecha 2025 | 3.6 mil millones (0.7 %); −3.6 en M.5 | Sí |
| Saldo de la afiliación subsidiada 2030 | 288 (47.2 %; 4.6 puntos); 196 / 162 por conteo; 404 / 173 por afiliación; 301 por cobro | Sí; anexo ITED: 81 |
| Años de cobertura del seguro solidario | 2054 / 2037 / 2033 con reserva; 2054 / 2032 / 2030 sin reserva | Sí; anexo ITED: 2054 / 2054 / 2037 |
| Déficit de GMP | 66 (2025), 89 (2027), 107 (2030), 272 (2054) | Sí; Informe IMSS V.19/V.24: 68.4 (2026) … 203.9 (2055) |
| Cotizantes 2025 / 2054 | 22.35 (22.4) / 46.8 M; 46.69 M en 2055 | Sí; el Informe no publica 46.8 (Gráfica C.1: 47.15) |
| Gasto corriente en salud 2025 | 545.3 mil millones / 545,271 M | Sí; V.13 prestaciones en especie 2026: 494,275 |
| Cuota fija patronal anual | 8,735 (365 días) / 8,065 (337 días) | Aclarar |
| Discrepancia INDOQC | 49.5 % con 10,536 / 21,259 | No se reproduce (49.6 / 50.4 %) |

---

## 7. Ruta para cerrar

| # | Acción | Quién decide | ¿Cambia cifras del resumen ejecutivo? |
|---|---|---|---|
| 1 | Fijar una sola base para la sección 6 y los anexos de ITED: gasto base (545,271 atribuido al SEM o 494,275 de V.13), conteo (54.7 / 63.6 / 79.2 M) y déficit de GMP (aproximación 60+ o Cuadro V.24); recalcular 6a, 6b, 6c o añadir la fila de sensibilidad con la otra base. Corregir 6b.5 (R5). | Héctor, Juan Pablo, Judy | Sí: 288, 2037/2033, cuidados, 47.2 % |
| 2 | Decidir la presentación de Δ(t): dos columnas en la Tabla 5 («proporción fija» y «demanda») o advertencia en 2.4; resolver la contradicción 5.6 / Anexo M; entregar el cuaderno de ingresos. | Equipo (método); Juan Pablo (cuaderno) | Sí: el hallazgo sobre Δ(t) |
| 3 | Rehacer las dos listas de referencias con sólo lo citado y verificado; retirar Arredondo, Castañeda-Orjuela, Lavín, Reddy y el «Informe Actuarial»; añadir CIEP 2025 (Méndez Méndez), IMSS 2026 (Informe 2025-2026), la proyección de Finanzas; corregir Rechel 2013 y CONAPO 2023 / 2020-2070; quitar el umbral del 15 %. | Equipo | No |
| 4 | Reescribir 2.2-2.3 del Informe de Recomendaciones con el método actual (2025-2055, π_m = 0, G(t) − F(t), nueve escenarios, sensibilidad real). | Equipo | No |
| 5 | Reformular la Recomendación 1: insumo complementario de proyección demográfica, piloto 2028 / formal 2029, sin «extrapolación lineal», sin Reddy, sin «subestimación» no demostrada; corregir «R y Excel 365». | Héctor y equipo | Sí (Recomendación 1) |
| 6 | Alinear la Recomendación 4 con 6b (déficit de GMP, tasas legales, los 3 puntos se dejan de cobrar o se simula la alternativa; alcance declarado) y la 5 con N.2 (base del 3.467 %, aproximación, artículo de la LSS con Jurídico); añadir rangos y salvedades (C11, C14, C15). | Equipo; IMSS (artículo) | Sí (Recomendación 4; 2.4 con rango) |
| 7 | Resolver los seis corchetes de la sección 4 y los actores de 6.1 con la contraparte del IMSS; separar el calendario de la Comisión de los pasos de cada recomendación; correr las fechas. | IMSS y equipo | No |
| 8 | Cerrar las decisiones menores de método: 2055 (nota o cierre en 2054), horizonte único en la sección 6, 8,735 / 8,065, nota al pie 1 al cuerpo, atribución del 27 %, 49.5 %. | Equipo | No |
| 9 | Pase editorial de Resultados: marcadores y resaltados, Figuras 5 y 10 regeneradas con E0-E9, figuras en PNG, pies de M.1/M.2 y F.1/F.2, títulos citados y no duplicados, jerarquía de encabezados, índice, estilo único de tabla, títulos huérfanos, siglas, erratas, referencias a 7.2.1. | Juan Pablo (figuras); equipo | No |
| 10 | Pase editorial de Recomendaciones: sección 1, números de página, notas rojas, resaltados, errata del título de la 6, cursivas de 4.3-4.6, registro único, siglas. | Equipo | No |
| 11 | Unificar la lista de autores en los dos informes y completar «Act. Luz María Álvarez Soto». | Héctor e IMSS | No |

Decisiones de método (puntos 1, 2, 6 y 8) frente a correcciones (3, 4, 5, 7, 9, 10, 11): las primeras las toma el equipo con el cuaderno; las segundas no cambian ningún número por sí mismas.
