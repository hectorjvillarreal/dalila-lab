---
id: 20261017_BDH_N13_anexo-afiliacion-subsidiada_build_v1
title: "Instrucciones de construcción — Anexo preliminar: ingresos y costos de esquemas de afiliación subsidiada al SEM"
type: build_instruction
project: BDH
mission: IMSS — Núcleo 13 (Sostenibilidad financiera de la atención quirúrgica)
version: v1
date: 2026-10-17
language: es
added_by: Beth
endorsed_by: ""          # pendiente: Cath (prueba fiscal) y Héctor
protocol: PROTO-RAG-001  # verificar el esquema vigente en _crossrefs/protocols/PROTO-RAG-001.md y ajustar estos campos
status: superseded
superseded_by: 20261017_BDH_N13_anexo-afiliacion-subsidiada_build_v1.1
executor: Claude Code (Dalila)
---

# Anexo preliminar del Núcleo 13 — Ingresos y costos de esquemas de afiliación subsidiada al SEM

## 0. Propósito

Construir, con la información disponible **hoy**, un modelo preliminar de ingresos, costos y subsidio implícito de una **formalización subsidiada** para personas de ingresos bajos y medio-bajos. El resultado se anexará al *Informe de Resultados del Núcleo 13* (IMSS / ITED).

El modelo responde a dos comentarios de la contraparte del IMSS sobre el borrador del Núcleo 13. Ambos señalan que ese informe proyecta costos con ingresos fijos y no vincula el ingreso a los escenarios demográficos ni de formalidad.

**No se solicitarán datos adicionales al IMSS.** Todo lo que falte se sustituye con aproximaciones documentadas (sección 4.6).

El anexo es **trabajo preliminar de ITED**, no una proyección institucional del IMSS. Así debe rotularse en todos los productos.

---

## 1. Alcance

### 1.1 Dentro del alcance

1. **Bloque A — Afiliación subsidiada de informales:** prima graduada por ingreso, subsidio federal, adopción, costo esperado de la atención por edad y sexo.
2. **Bloque B — Formalización subsidiada:** reducción graduada de la cuota fija del SEM para formales de bajo salario, de modo que se cumpla la **regla de no arbitraje** (sección 3.1).
3. **Bloque C — Escenario mecánico de formalización:** +5 pp de formalidad al 2030, coherente con los escenarios E2/E4/E6 del Núcleo 13.
4. **Descriptivo de rotación:** retención anual por edad y sexo a partir de las matrices de asegurados a diciembre de 2024 y diciembre de 2025.
5. Horizonte **2026–2054**, en **pesos de 2026**.

### 1.2 Fuera del alcance

- Equilibrio general.
- Respuesta conductual estimada. El Bloque C es un escenario, no una estimación.
- Prestaciones en dinero para informales.
- Pensiones.
- Conclusiones de sostenibilidad fiscal. Las emite Cath, no este anexo.

---

## 2. Insumos

### 2.1 Fase F0: inventario

Localizar en Dalila cada insumo, reportar su ruta, versión y estado, y **continuar con los respaldos** de la sección 4.6 si algo falta.

**Detenerse solo si falta un insumo crítico (C) y no puede obtenerse.**

| # | Insumo | Crítico | Dónde buscar / cómo obtener |
|---|---|---|---|
| I1 | *Informe al Ejecutivo Federal y al Congreso de la Unión sobre la Situación Financiera y los Riesgos del IMSS 2025-2026* (PDF, 338 pp.) | C | Descargar de `https://www.senado.gob.mx/66/gaceta_del_senado/documento/160639`. El sitio puede entrar en un bucle de redirecciones: reintentar con cookies o sesión, o buscar el enlace al PDF en la página del documento. Si falla, buscar la copia local en Dalila (`_informe-situacion-financiera_imss.pdf`) o pedirla a Héctor. Validar con `pdfinfo` (338 páginas; título 2025-2026). |
| I2 | Tablas de la Dirección de Finanzas: `Req inf fin_Modelo de demanda quirúrgica_070926.xlsx` | C | Carpetas del Núcleo 13 o de Juan Pablo López Reynosa. **Usar solo la versión 07/09/2026.** La del 03/09 está superada: su matriz de trabajadores del IMSS (TIMSS) tiene contenido numérico de más y le faltan los años observados 2024-2025. |
| I3 | Proyecciones de población CONAPO 2022-2070, por edad simple, sexo y año | C | Módulo demográfico de DFD (Anne), `_baseline.md` o carpetas del Núcleo 13 (Juan Pablo las usó). Debe ser la misma base que usa el Núcleo 13. |
| I4 | ENIGH 2024 (microdatos: tablas de población, trabajos, ingresos y hogares) | C | Dalila (`ENIGH` en datos). Si no está, descargarla del sitio de INEGI. Usar el factor de expansión. Si se reportan errores estándar, usar el diseño muestral (UPM y estrato), **no** pesos de frecuencia (lección del paper de formalidad). |
| I5 | Perfiles por edad del consumo público de salud (NTA México) | No | Repositorio `NTA_tesis` (misión NTA). Si no existe o no está listo, usar el respaldo R3 (sección 4.6). |
| I6 | Cuadernos e insumos del Núcleo 13 (`Ingresos_borrador.ipynb`, `reporte_final_borrador.ipynb`) | No | Para garantizar coherencia de población derechohabiente, deflactores y escenarios. |

**Producto de F0:** `outputs/F0_inventario.md` con rutas, versiones, sumas de control (sección 7.1) y decisiones de respaldo.

---

## 3. Restricciones de diseño (no negociables)

### 3.1 Regla de no arbitraje

Para cada nivel de ingreso *m*, el pago neto anual por la cobertura en especie de un informal afiliado **nunca puede ser menor** que el pago del par trabajador–patrón formal con el mismo ingreso. Si lo fuera, el esquema subsidiaría la informalidad.

El modelo debe:

1. Mostrar en una tabla las violaciones de la regla **antes** del Bloque B.
2. Construir el Bloque B para que no quede **ninguna violación** después de aplicarlo.

### 3.2 Una sola tabla de pago neto

Formales e informales enfrentan la misma función de pago neto π(*m*) por la cobertura en especie del SEM. Las diferencias de política se expresan solo a través de quién paga cada parte: afiliado, patrón o Gobierno Federal.

### 3.3 Invariancia de métrica

Los resultados se reportan primero en **puntos del salario base de cotización (SBC)** o como **porcentaje de los ingresos del SEM**, y después en millones de pesos de 2026.

El % del PIB va en una columna secundaria. Nunca se compara un valor presente con el PIB de un año como cifra principal.

### 3.4 Separar costo sanitario de pasivo laboral

El costo de la atención de los nuevos afiliados se mide con las prestaciones en especie. No se le cargan el RJP ni los gastos de administración del Instituto.

### 3.5 Horizonte

La proyección institucional cambia de régimen en 2055: los nuevos ingresantes caen de 1.525 a 0.695 millones y el crecimiento del empleo se vuelve negativo.

**No reportar ni interpretar 2055.** El último año reportado es 2054.

### 3.6 Coherencia con el Núcleo 13

Usar la misma base CONAPO, los mismos pesos de 2026 y la misma calibración del escenario de formalidad (+5 pp al 2030; alrededor de 3 millones de cotizantes; unos 3 derechohabientes por cotizante).

### 3.7 Trazabilidad

**Ninguna cifra aparece en el anexo si no está en `NUMBERS.md`**, con su fuente: cuadro y página del Informe, hoja del libro de Finanzas, o tabla y variable de la ENIGH.

---

## 4. Modelo

### 4.1 Notación

| Símbolo | Definición |
|---|---|
| *m* | Ingreso diario del titular en múltiplos de la UMA. La UMA se indexa a la inflación, así que *m* es aproximadamente invariante en términos reales. |
| UMA | 113.14 pesos diarios (diciembre de 2025). |
| P* | Precio completo anual de la cobertura en especie por titular, con cobertura familiar: P* = 0.3523 × UMA × 365. Es la cuota fija vigente: 20.40% patrón + 14.83% Gobierno Federal. |
| s(*m*) | Tasa de subsidio, entre 0 y 1. |
| π(*m*) | Pago neto común. |
| c(a, x, t) | Costo anual per cápita de la atención en especie por edad *a* y sexo *x*. |
| τ | Tasa de adopción. |
| μ | Multiplicador de selección adversa. |

### 4.2 Bloque A — Afiliación subsidiada de informales

**Población objetivo (ENIGH 2024).** Personas ocupadas sin acceso a servicios médicos como prestación laboral y sin cobertura contributiva de ningún tipo (IMSS, ISSSTE, Pemex, Sedena, Semar), más los miembros de su hogar sin cobertura contributiva.

- Identificar las variables en el descriptor de la ENIGH 2024 y documentarlas en `NUMBERS.md`.
- Seguir el criterio de "acceso a la seguridad social" de la medición multidimensional de la pobreza.

**Ingreso del titular.** Ingreso laboral mensual del perceptor principal informal del hogar, convertido a pesos diarios y a múltiplos de la UMA de 2024 (UMA vigente en el periodo de levantamiento; registrar el valor).

**Proyección.** Proporciones por edad × sexo × tramo de *m* de la ENIGH 2024, aplicadas a CONAPO por año.

- Crecimiento real del ingreso de informales: el mismo que el del SBC de la proyección institucional (hoja `Sup_Inc_Aseg&Sal`).

**Esquema de subsidio (parámetros de escenario).**

```
s(m) = 1                    si m ≤ m0
s(m) = (m1 − m)/(m1 − m0)   si m0 < m < m1
s(m) = 0                    si m ≥ m1
```

| Escenario | m0 | m1 |
|---|---|---|
| **S1 (base)** | percentil 20 del ingreso del titular objetivo | percentil 50 |
| S2 (focalizado) | percentil 10 | percentil 30 |
| S3 (amplio) | percentil 40 | percentil 70 |

Los percentiles se calculan con la ENIGH ponderada y se convierten a múltiplos de la UMA.

**Pago neto del afiliado.**

```
π(m) = (1 − s(m)) · κ · P*
```

**Aportación federal (parámetro G).**

| Escenario | Regla | κ |
|---|---|---|
| **G1 (base)** | El Gobierno Federal paga solo el subsidio s·κ·P*. | κ = 1 |
| G2 | Aportación federal universal: el Gobierno Federal paga 14.83% de la UMA por todo afiliado, igual que hoy con los formales; el resto se gradúa. | κ = 20.40 / 35.23 |

**Unidad de afiliación (parámetro U).**

| Escenario | Regla |
|---|---|
| **U1 (base)** | Titular con cobertura familiar: todos los miembros del hogar sin cobertura contributiva. |
| U2 | Individual: precio por persona = P* / *h*, donde *h* es el número de derechohabientes por titular del IMSS estimado en la ENIGH (respaldo R2). *m* se mide con el ingreso per cápita del hogar. |

**Adopción y selección adversa (parámetro T).** Son supuestos ilustrativos del equipo, no estimaciones.

| Escenario | Adopción τ(s) | Multiplicador de costo μ |
|---|---|---|
| T1 (voluntario) | 0.10 + 0.40·s | 1.0 + 0.3·(1 − s) |
| **T2 (base; inscripción automática vía impuesto negativo)** | 0.90 | 1.0 |

Referencia de calibración que el anexo debe citar: el Seguro de Salud para la Familia, voluntario, cubrió en 2025 apenas 17% de su gasto (ingresos 3,724 mdp contra gastos 21,674 mdp; Informe, Cuadro VII.2).

**Costo de atención.**

```
Costo_A(t) = Σ_{a,x} N_afiliados(a,x,t) · c(a,x,2026) · (1+π_m)^(t−2026) · μ
```

- π_m ∈ {0, 1%, 2%} anual real **per cápita**.
- Referencia: el Informe supone un crecimiento real del gasto médico total de 3.8% anual (Cuadro II.15), que incluye volumen.

**Ingreso del SEM por el Bloque A.** Pagos de los afiliados + pagos federales: subsidio, más 14.83% de la UMA en G2.

**Saldo del Bloque A.** Ingreso − costo. Reportar por separado:

- (i) lo que pagan los afiliados,
- (ii) lo que paga el Gobierno Federal,
- (iii) el costo,
- (iv) el saldo residual para el SEM.

No suponer quién cubre el saldo residual.

### 4.3 Bloque B — Formalización subsidiada

**Pago vigente del par formal, solo componente en especie, base anual de 365 días:**

```
π_F(m) = [0.2040·UMA + 0.0150·max(0, m − 3)·UMA] · 365
```

Reportar aparte una variante que incluya la cuota de gastos médicos para pensionados (GMP): +0.01425·m·UMA·365 (patrón + trabajador).

**Reducción.** Donde π_F(*m*) > π(*m*), la cuota patronal fija se reduce para que el par formal pague π(*m*). El Gobierno Federal compensa la diferencia, de modo que el ingreso del SEM no cambia.

```
Costo_B(t) = Σ_formales max(0, π_F(m) − π(m))
```

**Distribución del SBC formal (respaldo R1).** El libro de Finanzas solo trae promedios de SBC por edad, sexo y generación.

- Tomar la **forma** de la distribución del ingreso laboral de los asalariados con IMSS por prestación laboral en la ENIGH 2024, por grupo de edad y sexo.
- Reescalarla para que el promedio coincida con la hoja `Sal SEM-Emp_dic25`, ponderada con `Mat_Aseg SEM_dic25`. El objetivo es 627.21 pesos diarios.
- Truncar por abajo en el salario mínimo (278.80 pesos diarios en 2025).
- Aplicarla a los cotizantes proyectados en `Pob Emp & Nuevos`.
- Documentar que el ingreso de la ENIGH no es el SBC (integración, subdeclaración).

**Trayectoria del salario mínimo.** Usar la hoja `Sup_Fin`: +8.97% real en 2026, alrededor de +8% real anual de 2027 a 2030 y +0.5% después; la UMA sigue a la inflación.

Reportar la cuota fija como porcentaje del salario mínimo de 2025 a 2054. Referencias: alrededor de 14.3% en 2025 y cerca de 9.7% en 2030 (la parte patronal, de 8.3% a 5.6%). Este cambio es la reducción automática de la regresividad de la cuota fija que ya ocurre sin reforma.

**Indicador de incentivos.** Cuota patronal del SEM en especie como porcentaje del salario, por tramo de *m*, antes y después del Bloque B. Es un componente del costo de formalizarse (FTR); no se calcula el FTR completo.

### 4.4 Bloque C — Escenario mecánico de formalización

| Escenario | Regla |
|---|---|
| **F0 (base)** | Sin formalización adicional. |
| F1 | +3 millones de cotizantes al 2030, con trayectoria lineal entre 2026 y 2030 y proporción constante después. Se extraen de la población objetivo del Bloque A según su distribución por edad, sexo y *m*. |

En F1, esas personas salen del Bloque A, cotizan con el esquema reformado (Bloques B y A) y sus familias generan costo de atención.

Reportar el **efecto neto para el SEM** y el **costo federal**. Rotularlo como escenario, no como respuesta estimada.

### 4.5 Coherencia con la proyección institucional (prueba C)

La proyección institucional de cotizantes pasa de 22.35 millones en 2025 a 46.8 millones en 2054, con crecimiento del empleo cercano a 2.9% anual hasta los 2040. Eso implica una formalización fuerte en el escenario base del IMSS.

| Escenario | Regla |
|---|---|
| **C1 (base)** | Proporciones de la ENIGH fijas. |
| C2 | Población informal objetivo = personas ocupadas (CONAPO × tasa de ocupación por edad y sexo de la ENIGH) − cotizantes institucionales, por edad y sexo, con piso en cero. |

Reportar en 2030, 2040 y 2054:

- la tasa de formalidad implícita,
- las edades donde los cotizantes institucionales exceden a los ocupados estimados.

Esto documenta la inconsistencia ya observada en el Anexo I del Núcleo 13.

### 4.6 Respaldos (datos que no se pedirán al IMSS)

| Código | Dato faltante | Respaldo |
|---|---|---|
| R1 | Distribución del SBC | Forma de la ENIGH 2024, reescalada al promedio del libro de Finanzas (sección 4.3). |
| R2 | Derechohabientes por titular | ENIGH 2024: personas con IMSS como beneficiarias por un familiar, entre titulares con IMSS por prestación laboral, por edad y sexo del titular. Contrastar con el total del Informe ("casi 80 millones de derechohabientes"; extraer la cifra exacta de la sección I.2.1) entre los 22.35 millones de cotizantes. Reportar la discrepancia. |
| R3 | Perfil de costo por edad y sexo | **Ancla de nivel:** prestaciones en especie del SEM en 2026, 494,275 mdp de 2026 (Informe, Cuadro V.13), entre la población derechohabiente total del Informe. **Forma:** perfil NTA de consumo público de salud (I5). Si no hay perfil NTA, usar un perfil plano como cota inferior y un perfil estilizado con razón 65+/20-64 = 3.0 como supuesto ilustrativo, con sensibilidad de 2.0 y 4.0. |
| R4 | Antigüedad en las matrices | Interpretarla como años desde el primer registro. Si la evidencia interna sugiere tiempo cotizado, reportar la retención como "indicativa" y explicar la doble lectura. |

---

## 5. Escenarios a correr

**Base:** S1 · G1 · U1 · T2 · C1 · F0 · π_m = 0 · R3 con NTA (o perfil estilizado de 3.0).

**Malla mínima** (no correr el producto cartesiano completo):

1. **Esquema:** S1, S2, S3 (con el resto en base).
2. **Adopción:** T1 frente a T2.
3. **Aportación federal:** G1 frente a G2.
4. **Unidad:** U1 frente a U2 (solo S1, T2).
5. **Costo:** π_m = 0, 1% y 2%.
6. **Coherencia:** C1 frente a C2.
7. **Formalización:** F0 frente a F1.
8. **Perfil de costo:** NTA, estilizado 2.0, 3.0 y 4.0 (o plano).

Todo debe quedar en `config.yaml`, con un escenario por bloque.

---

## 6. Fases y productos

| Fase | Contenido | Productos |
|---|---|---|
| F0 | Inventario (sección 2.1) | `outputs/F0_inventario.md` |
| F1 | Población objetivo y formales: ENIGH, R1, R2, CONAPO, prueba C | `data/derived/*.parquet`; tabla de población objetivo por edad, sexo y tramo de *m* |
| F2 | Esquemas y regla de no arbitraje | `outputs/tables/no_arbitraje_antes_despues.csv`; figura de π(*m*) y π_F(*m*) |
| F3 | Proyección 2026–2054 de los Bloques A, B y C, y descriptivo de rotación | `outputs/tables/*.csv`; `outputs/figures/*.png` |
| F4 | Registro de cifras, verificaciones y borrador del anexo | `NUMBERS.md`, `REPORT.md`, `ANEXO_borrador.md` |

### 6.1 Estructura de carpetas

Dentro de la carpeta de la misión del Núcleo 13 en `Missions/` (localizarla; si no existe, crear `Missions/IMSS_N13/` y reportarlo):

```
anexo_afiliacion_subsidiada/
  config.yaml
  src/          # Python; un módulo por bloque; sin rutas absolutas en el código
  data/raw/     # no versionar microdatos de la ENIGH
  data/derived/
  outputs/tables/  outputs/figures/
  NUMBERS.md  REPORT.md  ANEXO_borrador.md
```

Archivar este archivo de instrucciones en `_crossrefs/_build_instructions/` conforme a PROTO-RAG-001. Hacer commit en Git con un mensaje descriptivo.

### 6.2 Contenido de `ANEXO_borrador.md`

Español institucional, de 4 a 6 páginas:

1. **Título y rótulo:** "Anexo X. Ingresos y costos de esquemas de afiliación subsidiada al SEM: ejercicio preliminar (ITED)".
2. **Propósito:** responde a la limitación de ingresos fijos del Núcleo 13.
3. **Diseño:** no arbitraje y tabla única de pago neto.
4. **Datos y respaldos:** declarar R1 a R4.
5. **Resultados del escenario base** en 2026, 2030, 2040 y 2054, en puntos del SBC, % del ingreso del SEM y mdp de 2026.
6. **Sensibilidades**, en una tabla.
7. **Limitaciones.**
8. **Fuentes.**

Sin conclusiones de sostenibilidad fiscal; esas se dejan a Cath.

---

## 7. Verificaciones obligatorias

Reportarlas en `REPORT.md` con el valor obtenido y si pasan o no.

### 7.1 Sumas de control del libro de Finanzas (07/09)

| Verificación | Valor esperado |
|---|---|
| Asegurados a diciembre de 2025 | 21,800,692 (hombres 13,102,667; mujeres 8,698,025) |
| Trabajadores del IMSS (TIMSS) a diciembre de 2025 | 551,894 |
| Total | 22,352,586 = stock de 2025 en `Pob Emp & Nuevos` |
| SBC promedio ponderado (diciembre de 2025) | 627.21 pesos diarios (el Informe reporta 627.87) |
| Aportación federal al SEM de asegurados (SEM-A) 2025 reconstruida | Cuota fija de 14.83% de la UMA por persona asegurada (incluido TIMSS) × 365 + 0.05% del SBC, llevada a pesos de 2026. Debe quedar a menos de 3% de 146,457 mdp (hoja `Ingresos IMSS`). |

### 7.2 Diferencias con el Informe

Reportar la diferencia entre los ingresos de 2025 del libro de Finanzas y el Cuadro II.14 del Informe:

| Concepto | Libro de Finanzas | Cuadro II.14 |
|---|---|---|
| Cuotas obrero-patronales | 634,265 | 625,443 |
| Otros ingresos | 59,154 | 46,643 |
| Total sin pensiones en curso de pago | 851.3 mil millones | 831.0 mil millones |

Declarar la fuente que se usa: el libro de Finanzas, por coherencia con el Núcleo 13.

### 7.3 Rotación

A partir de las matrices de diciembre de 2024 y diciembre de 2025, retención = asegurados en (edad + 1, antigüedad + 1) en 2025 entre asegurados en (edad, antigüedad) en 2024. Debe reproducir, aproximadamente:

| Grupo | Retención esperada |
|---|---|
| Hombres, total | 0.94 |
| Mujeres, total | 0.92 |
| 15 a 24 años | 0.81 a 0.85 |
| Antigüedad cero en 2025 | alrededor de 1.69 millones |

Reportar las cifras con la advertencia R4.

### 7.4 ENIGH

- Población total expandida y población con IMSS expandida.
- Contraste con los 70.7 millones de derechohabientes del Núcleo 13 (2025) y con el total del Informe.
- Proporción de informales por decil.

### 7.5 Identidades contables

En cada escenario y año: ingreso − costo = saldo. Además, Bloque A + Bloque B + Bloque C = total.

### 7.6 Regla de no arbitraje

Cero violaciones después del Bloque B en todos los tramos de *m* y en todos los escenarios S y G.

### 7.7 Monotonicidad

- Mayor π_m implica mayor costo.
- Mayor subsidio implica mayor adopción en T1.
- S3 cuesta más al fisco que S1, y S1 más que S2.

### 7.8 Horizonte

Ninguna salida contiene el año 2055.

### 7.9 Unidades

Todo en pesos de 2026. Documentar el deflactor usado para llevar la ENIGH 2024 a 2026: INPC de INEGI, o inflación de `Sup_Fin` para 2026.

---

## 8. Registro de cifras semilla (`NUMBERS.md`)

Estas cifras ya se verificaron contra las fuentes. Claude Code debe confirmarlas en I1 e I2, añadir página y cuadro exactos, e incorporar todas las nuevas que produzca.

| Clave | Valor | Fuente |
|---|---|---|
| UMA_dic2025 | 113.14 pesos/día | Informe, Cuadro A.3, nota 2; libro de Finanzas, hoja `Tasas de Contribución` |
| CF_patron | 20.40% UMA | Informe, Cuadro A.3 |
| CF_GF | 14.83% UMA (16.78 pesos/día, dic. 2025) | Informe, Cuadro A.3, nota 3 |
| CF_total | 35.23% UMA | Informe, Cuadro A.3 |
| Excedente | 1.10% patrón + 0.40% trabajador sobre (SBC − 3 UMA) | Informe, Cuadro A.3 |
| Prest_dinero | 0.70 / 0.25 / 0.05% SBC | Informe, Cuadro A.3 |
| GMP | 1.05 / 0.375 / 0.075% SBC (total 1.50) | Informe, Cuadro A.3 |
| Tasa_efectiva_SEM | 9.60% SBC (patrón 5.97, trabajador 0.82, GF 2.81) | Informe, Cuadro A.4 |
| Tasa_efectiva_SEM-A | 8.10% SBC (4.92 / 0.44 / 2.74) | Informe, Cuadro A.4 |
| Prima_eq_SEM / Prima_fin_SEM | 12.94% / 8.9% SBC (2026-2055) | Informe, Cuadros V.13 y V.14 |
| Prima_eq / fin SEM-A | 9.9% / 7.4% | Informe, Cuadro II.16 |
| Prima_eq / fin GMP | 3.1% / 1.5% | Informe, Cuadro II.16 |
| SBC_prom_dic2025 | 627.87 pesos/día | Informe, sección I.1.3 |
| SM_2025 | 278.80 pesos/día (zona general) | Informe, sección I.1.3 |
| Dias_cotizados | 337 (base) / 324 (riesgo) | Informe, Cuadro II.18 |
| Especie_SEM_2026 | 494,275 mdp de 2026 | Informe, Cuadro V.13 |
| Crec_gasto_medico | 3.8% real anual (2026-2055) | Informe, Cuadro II.15 |
| SEM_resultado_2025 | −151,127 mdp corrientes; pensiones y jubilaciones cargadas al SEM: 164,456 | Informe, Cuadro V.11 |
| SSFAM_2025 | Ingresos 3,724; gastos 21,674; resultado −17,950 mdp | Informe, Cuadro VII.2 |
| SSFAM_cuotas | 8,900 a 21,300 pesos anuales por persona según edad (2025-2026) | Informe, Cuadro A.5 |
| PIB_2026 | 38,715,900 mdp | Informe, nota 51 (CGPE 2026) |
| DH_total | "casi 80 millones" (extraer la cifra exacta) | Informe, Introducción y sección I.2.1 |
| Aseg_dic2025 / TIMSS_dic2025 | 21,800,692 / 551,894 | Libro de Finanzas 07/09, matrices dic25 |
| SBC_ponderado_libro | 627.21 pesos/día | Cálculo propio con `Sal SEM-Emp_dic25` × `Mat_Aseg SEM_dic25` |
| GF_SEM-A_2025 | 146,457 mdp de 2026 | Libro de Finanzas, hoja `Ingresos IMSS` |
| Nuevos_2054 / Nuevos_2055 | 1.525 / 0.695 millones | Libro de Finanzas, hoja `Pob Emp & Nuevos` |
| Cotizantes_2054 | 46.8 millones | Libro de Finanzas, hoja `Pob Emp & Nuevos` |
| SM_real | +8.97% (2026); +7.97, 7.99, 7.92, 7.92% (2027-2030); +0.5% después | Libro de Finanzas, hoja `Sup_Fin` |
| Inflacion_2026 | 3.70% | Libro de Finanzas, hoja `Sup_Fin` |

Las desagregaciones de cuotas por seguro y las retenciones son **reconstrucciones propias** y deben citarse como tales.

---

## 9. Afirmaciones prohibidas

1. Llamar a cualquier resultado "proyección del IMSS" o "proyección institucional". Es un ejercicio preliminar de ITED que **usa** insumos institucionales.
2. Presentar los parámetros de adopción, selección adversa o formalización (T1, T2, F1) como estimaciones.
3. Afirmar que un esquema "es sostenible" o "no es sostenible". Esa prueba corresponde a Cath.
4. Afirmar efectos causales sobre la formalidad.
5. Usar el % del PIB como cifra principal, o comparar un valor presente con el PIB de un año.
6. Interpretar o reportar 2055.
7. Llamar "tasa de desafiliación" a la retención calculada con la antigüedad sin la advertencia R4.
8. Mezclar el RJP o los gastos de administración con el costo sanitario de los nuevos afiliados.
9. Usar cualquier cifra ausente de `NUMBERS.md`.
10. Atribuir al Seguro de Salud para la Familia una causa de su déficit distinta de lo que reporta el Informe. Se cita como referencia de calibración, no como diagnóstico.

---

## 10. Reporte final

Al terminar, `REPORT.md` debe contener:

1. Resumen de una página:
   - cifras del escenario base en 2030, 2040 y 2054: población cubierta, pagos de afiliados, pagos federales del Bloque A, costo del Bloque B, costo de atención y saldo;
   - las tres sensibilidades que más mueven el resultado.
2. Resultado de cada verificación de la sección 7.
3. Lista de respaldos usados y su efecto esperado en la dirección del sesgo.
4. Decisiones que Claude Code tomó por su cuenta. Cada una debe marcarse para revisión de Héctor.
5. Pendientes que requieren datos del IMSS en una fase posterior:
   - distribución del SBC,
   - derechohabientes por titular,
   - perfiles de gasto del SEM,
   - definición de antigüedad,
   - vigencia de las bases biométricas: la nota de la hoja de salidas indica que se usaron para el Informe 2022-2023; confirmar si aplican a la valuación 2025-2026.
