# Anexo X. Ingresos y costos de esquemas de afiliación subsidiada al SEM: ejercicio preliminar (ITED)

> **Rótulo.** Este anexo es un ejercicio preliminar de ITED (Tecnológico de Monterrey). Usa insumos institucionales del IMSS, pero **no es una proyección del IMSS** ni sustituye a sus valuaciones. Los parámetros de adopción, de selección adversa y de formalización son supuestos ilustrativos, no estimaciones. El anexo no emite juicios sobre la sostenibilidad financiera de ningún esquema.

## X.1 Propósito

El informe del Núcleo 13 proyecta el costo de los procedimientos trazadores con los ingresos de la proyección institucional del SEM, que son los mismos en todos los escenarios demográficos y de formalidad. Por eso, en ese informe, más formalidad solo agrega costo. La contraparte del IMSS señaló esta limitación.

Este anexo da un primer paso para vincular el ingreso con la cobertura. Cuantifica los ingresos, los costos y la aportación federal de tres esquemas:

- **Bloque A.** Afiliación subsidiada a la cobertura en especie del SEM para hogares con personas ocupadas sin seguridad social contributiva.
- **Bloque B.** Reducción de la cuota fija para los formales de bajo salario, para que el esquema no premie la informalidad.
- **Bloque C.** Un escenario mecánico de formalización adicional.

El horizonte es 2026-2054, en pesos de 2026. El año 2055 no se reporta porque la proyección institucional cambia de régimen ese año.

## X.2 Diseño

**Una sola tabla de pago privado.** Formales e informales enfrentan la misma tabla por la cobertura en especie:

π(m) = (1 − s(m)) · F_p + E(m)

- *m* es el ingreso diario en múltiplos de la UMA.
- F_p = 8,736 pesos al año es la parte de la cuota fija que hoy paga el patrón (20.40 % de la UMA).
- E(m) es el excedente de 1.5 % sobre el ingreso que rebasa 3 UMA.
- s(m) es la tasa de subsidio: vale 1 hasta un umbral m0, baja en línea recta y vale 0 a partir de m1.
- La parte federal de la cuota fija es F_g = 6,351 pesos (14.83 % de la UMA).
- El precio completo es P* = F_p + F_g = 15,087 pesos por titular con cobertura familiar.

**Regla de no arbitraje.** En ningún nivel de ingreso el informal afiliado paga menos que el par trabajador–patrón formal con el mismo ingreso.

- En el escenario G1, el Gobierno Federal solo paga el subsidio. El informal paga además (1 − s)·F_g, que equivale a una prima deliberada a la formalidad.
- En G2, el Gobierno Federal paga F_g por todo afiliado y la tabla es idéntica para formales e informales.
- En ambos casos, lo que paga el afiliado más lo que paga el Gobierno Federal suma P* + E(m) por titular: el mismo ingreso que hoy genera un formal con igual *m*.
- El Bloque B reduce el pago del formal en s(m)·F_p solo donde s(m) > 0. El Gobierno Federal compensa esa reducción, así que el ingreso del SEM no cambia.

**Umbrales.** Se calculan con los percentiles del ingreso laboral del titular informal en la ENIGH 2024, llevados a 2026.

| Escenario | m0 (UMA) | m1 (UMA) |
|---|---|---|
| S1 (base): percentiles 20 y 50 | 1.20 | 2.46 |
| S2: percentiles 10 y 30 | 0.56 | 1.66 |
| S3: percentiles 40 y 70 | 2.06 | 3.29 |

**Costo.** El costo de los nuevos afiliados se mide con las prestaciones en especie del SEM. No se les cargan el Régimen de Jubilaciones y Pensiones ni los gastos de administración.

## X.3 Datos y respaldos

**Fuentes:**
- Informe al Ejecutivo Federal y al Congreso de la Unión sobre la Situación Financiera y los Riesgos del IMSS 2025-2026: cuotas, primas, gasto en especie y derechohabientes.
- Libro de la Dirección de Finanzas del 7 de septiembre de 2026: ingresos por seguro, cotizantes, salarios, matrices de asegurados y supuestos financieros. Sus ingresos de 2025 suman 851,311 mdp, frente a 831,033 del Cuadro II.14 del Informe. Se usa el libro por coherencia con el Núcleo 13.
- ENIGH 2024, ponderada con su factor de expansión.
- Proyecciones de población de CONAPO, la misma base del Núcleo 13 (133,367,428 habitantes en 2025).

**Población objetivo (ENIGH 2024).**
- Son los miembros sin cobertura contributiva (IMSS, ISSSTE, Pemex, Defensa o Marina) de hogares con al menos una persona ocupada sin esa cobertura.
- Suman 59,193,354 personas en 19,655,021 hogares, con 3.01 personas por titular.
- El titular es el perceptor principal informal del hogar.
- La falta de cobertura contributiva entre los ocupados baja de 92.2 % en el decil I a 26.3 % en el decil X.

**Respaldos para los datos que no se pidieron al IMSS:**

| | Dato | Aproximación |
|---|---|---|
| R1 | Distribución del salario base de cotización | Forma del ingreso de los asalariados con IMSS en la ENIGH, reescalada al promedio del libro (627.21 pesos diarios) por edad y sexo, con piso en el salario mínimo |
| R2 | Beneficiarios por titular | 0.80 en la ENIGH, frente a 1.83 familiares por cotizante en el Informe (79,178,109 derechohabientes, Cuadro I.4). La diferencia se reporta y se acota con una corrida adicional |
| R3 | Costo per cápita por edad | 6,242.57 pesos por derechohabiente en 2026 (494,275 mdp del Cuadro V.13 entre el total de derechohabientes), con un perfil estilizado en que el costo de las personas de 65 años o más triplica el de 20 a 64 años. No hay perfil de consumo público de salud de Cuentas Nacionales de Transferencias disponible |
| R4 | Antigüedad en las matrices | Se lee como años desde el primer registro; la retención es indicativa |

**Cotizantes por edad.** Se reconstruyen con un modelo de cohortes que reproduce la proyección institucional, con factores de calibración entre 0.9962 y 1.0041.

**Retención anual de asegurados (reconstrucción propia).** Entre 2024 y 2025 es de 0.941 en hombres y 0.921 en mujeres, y de 0.830 entre los 15 y 24 años. Por la advertencia R4, estas cifras no son tasas de desafiliación.

## X.4 Resultados del escenario base

El escenario base supone:
- subsidio S1 y aportación federal G1;
- afiliación por hogar e inscripción automática con adopción de 90 %;
- ninguna formalización adicional;
- costo per cápita constante en términos reales.

**Cuadro X.1. Bloque A, escenario base.** Puntos del SBC; porcentaje de los ingresos del SEM; mdp de 2026.

| | 2026 | 2030 | 2040 | 2054 |
|---|---|---|---|---|
| Personas cubiertas (millones) | 55.5 | 56.5 | 57.9 | 57.0 |
| Pagos de afiliados | 3.53; 35.8 %; 197,810 | 3.27; 34.6 %; 211,406 | 2.53; 28.7 %; 239,104 | 1.76; 21.4 %; 257,856 |
| Pagos del Gobierno Federal | 1.67; 16.9 %; 93,657 | 1.46; 15.5 %; 94,471 | 0.99; 11.3 %; 93,878 | 0.60; 7.3 %; 87,703 |
| Costo de atención | 5.56; 56.4 %; 311,913 | 5.00; 52.8 %; 322,752 | 3.66; 41.5 %; 345,576 | 2.47; 30.1 %; 362,727 |
| Saldo para el SEM | −0.36; −3.7 %; −20,447 | −0.26; −2.8 %; −16,875 | −0.13; −1.5 %; −12,594 | −0.12; −1.4 %; −17,167 |

Columna secundaria, solo para 2026: el costo de atención equivale a 0.81 % del PIB y los pagos federales a 0.24 %.

**Lectura del Cuadro X.1:**

1. **Con inscripción automática, el ingreso por titular cubre casi todo el costo.** El costo por persona cubierta es de 5,622 pesos en 2026, menor que el promedio institucional porque la población objetivo es más joven. El ingreso por hogar es de P* más el excedente. El saldo residual equivale a entre 0.12 y 0.36 puntos del SBC. El anexo no supone quién lo cubre.
2. **El peso relativo baja porque el denominador crece.** La proyección institucional de cotizantes, de 22.35 a 46.8 millones, eleva la masa salarial y los ingresos del SEM más rápido que la población cubierta.
3. **El Bloque B no tiene costo en el escenario base.** El salario mínimo equivale a 2.69 UMA en 2026 y a 3.65 en 2030, por encima de m1 = 2.46. Ningún formal tiene un salario en el tramo subsidiado. El salario mínimo ya cumple, por sí solo, la regla de no arbitraje.
   - Solo el esquema amplio S3 genera costo en el Bloque B: 14,319 mdp en 2026, 10,320 en 2027 y 4,819 en 2028, para unos 4.6 millones de formales. Desde 2029 el costo es nulo.
   - Sin reforma, la cuota fija ya baja de 14.3 % del salario mínimo en 2025 a 9.66 % en 2030 y a 8.57 % en 2054.

## X.5 Sensibilidades

**Cuadro X.2. Saldo total para el SEM (Bloques A + B + C) y pagos federales.**

| Escenario | Saldo 2030 (pts SBC) | Saldo 2054 (pts SBC) | Pagos federales 2054 (mdp) |
|---|---|---|---|
| Base | −0.26 | −0.12 | 87,703 |
| S2 focalizado | −0.26 | −0.12 | 53,575 |
| S3 amplio | −0.26 | −0.12 | 138,236 |
| G2 aportación federal universal | −0.26 | −0.12 | 186,103 |
| T1 afiliación voluntaria | −0.26 | −0.14 | 43,804 |
| U2 individual (beneficiarios de la ENIGH) | 2.58 | 0.96 | 106,121 |
| U2 individual (beneficiarios del Informe) | −0.10 | −0.23 | 67,394 |
| Costo per cápita +1 % real anual | −0.46 | −0.91 | 87,703 |
| Costo per cápita +2 % real anual | −0.67 | −1.95 | 87,703 |
| C2 población objetivo ligada a la formalización institucional | −0.25 | −0.07 | 50,147 |
| F1 +3 millones de cotizantes al 2030 | −0.26 | −0.11 | 96,471 |
| Perfil de costo plano | −0.73 | −0.07 | 87,703 |
| Perfil 65+/20-64 = 2 | −0.47 | −0.10 | 87,703 |
| Perfil 65+/20-64 = 4 | −0.09 | −0.13 | 87,703 |

**Lectura del Cuadro X.2:**

- **Con inscripción automática, el saldo del SEM no depende del esquema de subsidio ni de la regla de aportación federal.** Esos parámetros solo cambian quién paga. La aportación federal de 2054 va de 53,575 mdp (S2) a 186,103 (G2).
- **La afiliación voluntaria (T1) reduce la cobertura** a 14.0 millones de personas en 2030, con selección adversa supuesta.
  - Referencia de calibración: el Seguro de Salud para la Familia, voluntario, registró en 2025 ingresos de 3,724 mdp y gastos de 21,674 mdp (Cuadro VII.2).
- **El supuesto que más mueve el resultado es el crecimiento real del costo per cápita.** El Informe supone 3.8 % de crecimiento real del gasto médico total (Cuadro II.15), que incluye el volumen.
- **El segundo es la unidad de afiliación**, por la incertidumbre del número de beneficiarios por titular.

**Bloque C.** Con +3 millones de cotizantes al 2030, el efecto neto para el SEM es de 298 mdp en 2030 y 647 mdp en 2054. El costo federal adicional es de 5,832 y 8,767 mdp. Hay 2.93 derechohabientes por cotizante en 2030. Este es un escenario mecánico, no una respuesta estimada de la formalidad.

**Coherencia con la proyección institucional.** La proyección institucional de cotizantes implica una formalidad de 34.0 % de los ocupados en 2025 y de 63.1 % en 2054. En 2054, los cotizantes rebasan a los ocupados estimados en las mujeres de 24 a 37 años (896,273 personas), lo que confirma la tensión señalada en el Anexo I del Núcleo 13. Si la población objetivo se liga a esa formalización (C2), en 2054 baja a 57 % de la del escenario base.

## X.6 Limitaciones

1. El ingreso de la ENIGH no es el salario base de cotización (integración, subdeclaración). El excedente de los informales se calcula sobre su ingreso laboral declarado.
2. El número de beneficiarios por titular difiere entre la ENIGH (0.80) y el Informe (1.83 familiares por cotizante). Los resultados del esquema individual (U2) dependen de esa cifra.
3. El perfil de costo por edad es estilizado y no distingue por sexo. No incorpora la maternidad ni la atención infantil.
4. La adopción, la selección adversa y la formalización son supuestos. El ejercicio no estima respuestas de comportamiento ni efectos de equilibrio general.
5. La cuota de gastos médicos de pensionados (1.425 % del salario del formal) deja una brecha residual ligada a derechos de pensión, que el Bloque B no corrige. Se documenta para una fase posterior.
6. La retención se calcula con la antigüedad de las matrices, cuya definición no está documentada.
7. La derechohabiencia del Núcleo 13 (70.7 millones en 2025) no se reproduce con la variable de afiliación al IMSS de la ENIGH ponderada (54.6 millones con el mismo método). Esta diferencia debe conciliarse antes de integrar el anexo.

## X.7 Fuentes

- IMSS (2026). *Informe al Ejecutivo Federal y al Congreso de la Unión sobre la Situación Financiera y los Riesgos del Instituto Mexicano del Seguro Social 2025-2026*. Cuadros I.2, I.4, II.14, II.15, II.16, II.18, V.11, V.13, V.14, VII.2, A.3, A.4 y A.5.
- IMSS, Dirección de Finanzas (2026). *Req inf fin_Modelo de demanda quirúrgica*, versión del 7 de septiembre de 2026.
- INEGI (2025). *Encuesta Nacional de Ingresos y Gastos de los Hogares 2024*, nueva serie: microdatos.
- CONAPO (2023). *Conciliación demográfica de 1950 a 2019 y proyecciones de la población de México 2020 a 2070*.
- ITED (2026). *Informe de Resultados del Núcleo 13: Sostenibilidad financiera de la atención quirúrgica*, borrador.

*Elaboración propia. Registro de cifras: `NUMBERS.md`. Tablas de respaldo: `outputs/tables/`.*
