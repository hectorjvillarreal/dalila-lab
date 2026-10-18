---
id: 20261018_BDH_N13_experimento2-seguro-salud-cuidados_build_v1.0
title: "Instrucciones de construcción — Experimento 2 del anexo del Núcleo 13: cuota del Infonavit a un nuevo seguro solidario de salud y cuidados en la vejez"
type: build_instruction
build_type: initial_scaffold
project: BDH
mission: IMSS — Núcleo 13 (Sostenibilidad financiera de la atención quirúrgica)
version: v1.0
date: 2026-10-18
language: es
corpus_affected:
  - Missions/Funded/IMSS_Surgical/e_2_imss_nuevoseguro/   # decisión de Héctor, 18-10-2026 (en lugar de la subcarpeta del experimento 1)
triggered_by:
  - "Solicitud de Héctor, 18-10-2026: segundo experimento simple para el anexo del Núcleo 13. La versión completa (valoraciones, variantes individual y mixta, transición del Infonavit) queda para un artículo propio."
  - "Antecedente: H. Villarreal, 'El Infonavit, ¿qué sigue?', Arena Pública, 20-12-2022"
  - "Decisiones de Héctor, 18-10-2026, antes de ejecutar: salidas en e_2; K1 reporta déficit no cubierto; regla 1/20 de K2 a criterio de Claude Code; contraste 3.3 con horizontes iguales; % de ingresos del SEM con el Informe (Cuadro V.13); base de 79,178,109 DH aceptada"
agents_involved: [Beth, Cath, Claude Code]
added_by: Beth
endorsed_by: []          # revisión pendiente: Cath (lectura fiscal)
protocol: PROTO-RAG-001
status: executed
executed: 2026-10-18   # Claude Code; e_2_imss_nuevoseguro/ (REPORT.md, NUMBERS.md, ANEXO_experimento2_borrador.md). Verificaciones 3.1-3.7 cumplidas; recaudación efectiva del Infonavit omitida
executor: Claude Code (Dalila)
---

# Experimento 2 — De la cuota del Infonavit a un nuevo seguro solidario de salud y cuidados en la vejez

## 0. Propósito y alcance

Ejercicio **simple y mecánico** para el anexo del Núcleo 13. Es la segunda parte del mismo anexo, después del experimento de afiliación subsidiada (v1.2).

**La reforma que se simula:**

1. Se elimina la aportación patronal de 5 % del salario base de cotización al Infonavit (artículo 29 de la Ley del Infonavit; tope de 25 UMA).
2. El Infonavit conserva su patrimonio y sus obligaciones como **mutualidad**. Su operación posterior no se modela.
3. **2 % del salario** (misma base y mismo tope de 25 UMA) financia un **nuevo seguro solidario de salud y cuidados en la vejez** (en adelante, "el nuevo seguro"). Es un fondo común, no una cuenta individual.
4. La **tasa legal de contribuciones obligatorias sobre la nómina** baja **3 puntos del salario** para todo salario hasta 25 UMA.

**Regla de lenguaje (no negociable).** El ejercicio describe tasas legales, es decir, la incidencia legal o estatutaria. **No mide incidencia económica**: quién soporta en realidad la contribución, si el trabajador vía menor salario, el empleador vía menores ganancias o una combinación, depende de elasticidades que aquí no se estiman. Por eso nunca se dice "costo para el patrón", "costo laboral", "ahorro del patrón" ni "costo de la formalidad". Se dice:

- "tasa legal de contribución",
- "cuña contributiva legal sobre la nómina", o
- "contribuciones obligatorias a cargo del patrón (incidencia legal)".

**Usos del nuevo seguro, en este orden:**

1. Cerrar el déficit de la cobertura de Gastos Médicos para Pensionados (GMP) del SEM.
2. Lo que sobre, el **remanente**, se destina a cuidados de largo plazo de personas mayores derechohabientes.

**Fuera de alcance (van a limitaciones y al artículo futuro):**

- valoración de los trabajadores y efecto sobre el costo de formalizarse;
- variantes individual y mixta;
- liquidez y transición del Infonavit;
- política de vivienda;
- efectos sobre Invalidez y Vida y Riesgos de Trabajo por saldos de vivienda;
- pensión mínima garantizada;
- incidencia;
- estimación del costo de los cuidados.

**Reutilizar** los módulos ya construidos (masa salarial, distribución R1, cotizantes, deflactores). La reforma inicia en **2027**. Horizonte 2027–2054; 2055 no se reporta.

---

## 1. Modelo

### 1.1 Ingreso del nuevo seguro

```
I_NS(t) = 0.02 × Masa_SBC_tope25(t)
```

- Masa salarial con 337 días cotizados y tope de 25 UMA: cotizantes del libro de Finanzas × distribución R1, como en la v1.2.
- **Contraste obligatorio:** 0.02 × volumen de salarios en valor presente del Informe (176,481,700 mdp; Cuadro V.15, escenario base) = cerca de 3.53 billones en valor presente.

**Sensibilidad M2.** Masa salarial con formalidad constante: cotizantes que crecen al ritmo de los ocupados, sin la formalización implícita en la proyección institucional. Se construye con el índice C2 de la v1.2 aplicado a los cotizantes.

### 1.2 Uso 1: déficit de GMP

Usar las cifras del **Informe, Cuadro V.24 (escenario base)**, en mdp de 2026:

| Concepto | 2026 | 2031 | 2036 | 2041 | 2046 | 2051 | 2055 | VP 2026-2055 |
|---|---|---|---|---|---|---|---|---|
| Ingresos GMP | 89,499 | 104,369 | 119,537 | 142,886 | 169,522 | 197,734 | 217,061 | 2,750,260 |
| Superávit/déficit GMP | −68,398 | −97,760 | −134,117 | −138,282 | −157,934 | −180,930 | −203,895 | −2,631,460 |

- Interpolar linealmente los años intermedios. Documentarlo.
- 2055 solo sirve para interpolar 2052-2054; **no se reporta**.

**Contraste.** La brecha de primas de GMP es de 1.6 puntos del salario (prima de financiamiento 1.5 % y prima de equilibrio 3.1 %; Cuadro II.16) × 176.48 billones = cerca de 2.82 billones en valor presente. Reportar la diferencia frente a los 2.63 billones del Cuadro V.24 y explicarla (definición de ingresos y reserva).

### 1.3 Reserva y remanente

```
R(t+1) = R(t)·(1 + r) + I_NS(t) − D_GMP(t) − U_cuidados(t)
r = 3 % real (tasa de descuento del Informe, Cuadro II.16, nota 1)
```

**Regla de uso para cuidados (escenarios):**

| Escenario | Regla |
|---|---|
| **K1 (base)** | U_cuidados(t) = max(0, I_NS(t) − D_GMP(t)). El remanente anual se gasta en cuidados; no hay reserva. |
| K2 | Nada para cuidados antes de 2035; el excedente se acumula en reserva. Después, cuidados = remanente + 1/20 de la reserva por año. |

Reportar, en cualquiera de los dos:

- el primer año (si lo hay) en que el ingreso no cubre el déficit de GMP;
- el saldo de la reserva.

### 1.4 Remanente por persona mayor

Remanente anual entre derechohabientes de 65 años o más y de 80 años o más.

- **Derechohabientes por edad:** proporción de 65 años o más entre la población adscrita a médico familiar (Informe, Gráfica I.31: 16.6 % en 2025), aplicada a los 79,178,109 derechohabientes (Cuadro I.4).
- **Proyección:** con la estructura por edad de CONAPO.
- **80 años o más:** se toma de CONAPO dentro del grupo de 65 años o más.

**No estimar el costo de los cuidados.** El anexo reporta solo cuánto alcanza por persona mayor.

### 1.5 Cuña contributiva legal por nivel de salario

Tabla determinística por nivel de salario: salario mínimo; 2, 3, 4 y 5.55 UMA (promedio); 10 y 25 UMA. Años 2026 y 2030. Columnas:

| Columna | Descripción |
|---|---|
| (a) | Ley vigente |
| (b) | Experimento 2 |
| (c) | Experimento 2 + tasa proporcional D2 del experimento 1 |

Componentes a cargo del patrón por ley (incidencia legal), en % del salario. Reportar aparte la cuña legal total, sumando las cuotas obreras y la aportación federal, para que se vea la estructura completa:

- cuota fija del SEM (vigente: 20.40 % de la UMA por trabajador; D2: 3.467 %);
- excedente de 1.10 % sobre (salario − 3 UMA);
- prestaciones en dinero, 0.70 %;
- GMP, 1.05 %;
- Invalidez y Vida, 1.75 %;
- Riesgos de Trabajo, prima promedio de 1.80 %;
- Guarderías y Prestaciones Sociales, 1.00 %;
- Retiro, 2.00 %;
- **cesantía y vejez según el calendario de la reforma de 2020**;
- Infonavit: 5 % (vigente) o 0 (experimento);
- nuevo seguro: 0 (vigente) o 2 %.

**Calendario de la cuota patronal de cesantía y vejez** (verificar contra el DOF del 16-12-2020, transitorio de la reforma a la LSS; fuente secundaria: El Contribuyente, noviembre de 2025):

| Salario | 2025 | 2026 | 2030 |
|---|---|---|---|
| 1.00 SM | 3.150 | 3.150 | 3.150 |
| 1.01 SM a 1.50 UMA | 3.544 | 3.676 | 4.202 |
| 1.51 a 2.00 UMA | 4.426 | 4.851 | 6.552 |
| 2.01 a 2.50 UMA | 4.954 | 5.556 | 7.962 |
| 2.51 a 3.00 UMA | 5.307 | 6.026 | 8.902 |
| 3.01 a 3.50 UMA | 5.559 | 6.361 | 9.573 |
| 3.51 a 4.00 UMA | 5.747 | 6.613 | 10.077 |
| 4.01 UMA o más | 6.422 | 7.513 | 11.875 |

**Verificación del escalón arriba del salario mínimo.** Con la trayectoria de `Sup_Fin`, el salario mínimo equivale a unas 3.65 UMA en 2030, así que el tramo "1.01 SM a 1.50 UMA" queda vacío. Determinar en el texto legal qué tasa paga un salario de 1.01 SM cuando ese salario rebasa 1.50 UMA. Reportar las dos lecturas:

- la de la tabla por UMA (alrededor de 10 % en 2030);
- la del primer tramo después del mínimo.

Si hay escalón, cuantificarlo en la tabla.

**Total agregado.** Reducción de las contribuciones legales sobre la nómina, en mdp = 0.03 × masa salarial con tope de 25 UMA. Como contexto: recaudación teórica actual de 5 % para el Infonavit. Si Claude Code puede obtener los estados financieros del Infonavit 2024 o 2025, reportar la recaudación efectiva; si no, omitirla sin buscar alternativas.

---

## 2. Salidas

| Archivo | Contenido |
|---|---|
| `tablas/ingreso_vs_GMP.csv` | Anual 2027-2054: ingreso del nuevo seguro, déficit de GMP, remanente y reserva (K1 y K2), en mdp de 2026, puntos del salario y % de los ingresos del SEM. Con la sensibilidad M2. |
| `tablas/valor_presente.csv` | Ingreso del nuevo seguro, déficit de GMP y remanente en valor presente 2027-2054 al 3 % real. Contraste con el Cuadro V.24. |
| `tablas/remanente_por_mayor.csv` | Por derechohabiente de 65+ y de 80+ (2027, 2030, 2040, 2054). |
| `tablas/cuna_legal_por_salario.csv` | Sección 1.5. |
| `figuras/` | Una figura: ingreso del nuevo seguro frente a déficit de GMP, 2027-2054, con el remanente sombreado. |
| `ANEXO_experimento2_borrador.md` | 2 a 3 páginas, español institucional, misma estructura que el anexo de afiliación subsidiada. |

**Contenido del borrador del anexo:**

1. **Propósito.** Una contribución que hoy financia vivienda puede cerrar el hueco de financiamiento más grande del SEM, con una cuña contributiva legal menor.
2. **Diseño.**
3. **Resultados:**
   - el ingreso cubre o no el déficit de GMP, y desde cuándo;
   - remanente para cuidados por persona mayor;
   - tabla de cuña contributiva legal.
4. **Limitaciones** (sección 4).
5. **Fuentes.**

---

## 3. Verificaciones

| # | Verificación |
|---|---|
| 3.1 | La masa salarial con tope de 25 UMA y 337 días se reproduce de la corrida v1.2 (mismos cotizantes y misma distribución R1). Reportar la proporción de la masa por encima del tope. |
| 3.2 | Las cifras del Cuadro V.24 se transcriben exactamente. La interpolación preserva los años ancla. |
| 3.3 | El valor presente del ingreso del nuevo seguro calculado con la masa propia queda a menos de 10 % del contraste con el volumen de salarios del Informe (1.1). Si no, explicar. |
| 3.4 | Identidad de la reserva en todos los años: R(t+1) = R(t)·(1 + r) + I − D − U. |
| 3.5 | En la tabla de cuña contributiva legal, columna (b) = columna (a) − 3 puntos para todo nivel de salario hasta 25 UMA. Las tasas de cesantía y vejez coinciden con la tabla de 1.5 y con el texto del DOF. |
| 3.6 | No aparece 2055 en ninguna salida. |
| 3.7 | Todas las cifras están en `NUMBERS.md` (sección nueva "Experimento 2") con su fuente. |

---

## 4. Limitaciones que el anexo debe declarar

1. **Incidencia y valoración.** El ejercicio reporta tasas legales. No mide incidencia económica: quién soporta la cuña depende de las elasticidades de oferta y demanda de trabajo; en el largo plazo, buena parte de las contribuciones a cargo del patrón suele trasladarse al salario. Tampoco mide valoración: el trabajador deja de acumular 5 % de su salario en su subcuenta de vivienda y recibe a cambio un seguro solidario. El efecto sobre el incentivo a formalizarse depende de ambas cosas y no se estima aquí.
2. **Infonavit.** Se supone que conserva su patrimonio y sus obligaciones como mutualidad. No se modelan su liquidez, el pago de saldos al retiro ni el fin del financiamiento hipotecario con aportaciones.
3. **Efectos en otros seguros.** Al dejar de acumularse saldos de vivienda, baja con el tiempo la proporción de asegurados que se pensionan con saldo; el Informe supone 71.45 % en su escenario base (Cuadro II.18). Eso encarece las rentas vitalicias de Invalidez y Vida y de Riesgos de Trabajo. No se cuantifica.
4. **Pensiones.** Con la Ley 97, el saldo de vivienda no usado se suma a los recursos para la pensión. Sin la aportación, las pensiones de quienes no usan crédito serían menores y el gasto en pensión mínima garantizada podría aumentar. No se cuantifica.
5. **Cuidados.** El remanente es una cifra disponible, no un costo estimado de cuidados.
6. **Proyección del IMSS.** El déficit de GMP es el de la proyección institucional del IMSS (Cuadro V.24). El ingreso depende de la proyección institucional de cotizantes; la sensibilidad M2 acota ese supuesto.
7. **Factibilidad política.** La política de vivienda vigente se apoya en el Infonavit. El ejercicio no evalúa esa dimensión.

---

## 5. Afirmaciones prohibidas

1. Decir que el experimento "reduce el costo de la formalidad", "reduce el costo laboral" o "reduce el costo para el patrón". Debe decir "reduce en 3 puntos del salario la tasa legal de contribuciones obligatorias sobre la nómina". Cualquier afirmación sobre quién se beneficia de la reducción implica medir incidencia y queda fuera del alcance.
2. Afirmar efectos sobre el empleo formal, la vivienda o el Infonavit.
3. Presentar el remanente como suficiente o insuficiente para cubrir los cuidados.
4. Llamar al nuevo seguro propuesta del IMSS o del Gobierno. Es un diseño de análisis de ITED.
5. Juicios de sostenibilidad fiscal. Corresponden a Cath.
6. Sumar los resultados del experimento 2 a los del experimento 1 sin presentarlos por separado. La columna (c) de la tabla de cuña contributiva legal es la única combinación permitida.

---

## 6. Registro de cifras semilla (`NUMBERS.md`, sección "Experimento 2")

| Clave | Valor | Fuente |
|---|---|---|
| Infonavit_tasa | 5 % del SBC, tope 25 UMA | Ley del Infonavit, art. 29; Informe, nota 176 |
| NS_tasa | 2 % del SBC, tope 25 UMA | Supuesto del experimento |
| GMP_V24_base | Serie de la sección 1.2 | Informe, Cuadro V.24 |
| GMP_prima_fin / eq | 1.5 % / 3.1 % | Informe, Cuadro II.16 |
| Vol_salarios_VP_SEM | 176,481,700 mdp de 2026 | Informe, Cuadro V.15 (base) |
| Tasa_descuento | 3 % real | Informe, Cuadro II.16, nota 1 |
| DH_65mas_2025 | 16.6 % de la población adscrita a médico familiar | Informe, Gráfica I.31 |
| DH_total | 79,178,109 | Informe, Cuadro I.4 |
| Vivienda_al_pensionarse | 71.45 % (base) / 57.45 % (riesgo) | Informe, Cuadro II.18 |
| CyV_patronal_2025_2026_2030 | Tabla de la sección 1.5 | DOF 16-12-2020 (verificar); El Contribuyente, nov. 2025 |
| c_D2 | 3.467 % | Corrida v1.2 |
| Patronales SEM, SIV, SRT, SGPS, Retiro | Tasas de la sección 1.5 | Informe, Cuadro A.3; libro de Finanzas, hoja `Tasas de Contribución` |

---

## 7. Reporte

Agregar a `REPORT.md` una sección "Experimento 2" con:

1. Resumen de media página: ¿cubre el déficit de GMP?, remanente por persona mayor, reducción de la cuña contributiva legal.
2. Resultado de las verificaciones de la sección 3.
3. Hallazgo sobre el escalón de cesantía y vejez arriba del salario mínimo.
4. Decisiones propias marcadas como **[REVISAR]**.

Hacer commit y archivar esta instrucción en `_crossrefs/_build_instructions/`.
