---
id: 20261017_BDH_N13_anexo-afiliacion-subsidiada_build_v1.2
title: "Instrucciones de construcción — Anexo preliminar: afiliación subsidiada al SEM (v1.2: tasa proporcional única y pago creíble)"
type: build_instruction
build_type: retrofit      # la instrucción decía «revision», que no está en la enumeración de PROTO-RAG-001; se usa el valor más cercano (REPORT.md v1.2.7)
project: BDH
mission: IMSS — Núcleo 13 (Sostenibilidad financiera de la atención quirúrgica)
version: v1.2
supersedes: 20261017_BDH_N13_anexo-afiliacion-subsidiada_build_v1.1   # parcialmente: ver la sección 0
date: 2026-10-17
language: es
corpus_affected:
  - Missions/Funded/IMSS_Surgical/e_1_imss_subsidiado/anexo_afiliacion_subsidiada/
triggered_by:
  - "Aclaración de Héctor, 17-10-2026: las cifras del cuadro del CIEP son el PEF 2026 en mdp de 2027"
  - "Revisión conjunta Beth y Cath de la corrida v1.1 (REPORT.md, NUMBERS.md y ANEXO_borrador.md, 17-10-2026)"
  - "Decisión de Héctor, 17-10-2026: el pago del informal debe ser sustancialmente menor; una adopción de 90 % no es creíble. Se adopta como base la tasa proporcional única."
agents_involved: [Beth, Cath, Claude Code]
added_by: Beth
endorsed_by: []          # revisión pendiente: Cath (lectura fiscal de los resultados)
protocol: PROTO-RAG-001
status: executed
executed: 2026-10-17   # Claude Code; ANEXO_borrador_v2.md y REPORT.md (sección v1.2). Pendiente 4.2 (cuadernos del Núcleo 13 no disponibles)
executor: Claude Code (Dalila)
---

# v1.2 — Tasa proporcional única, pago creíble y correcciones de la revisión

## 0. Alcance de esta versión

**Esta instrucción modifica la v1.1.** Todo lo que la v1.2 no cambie expresamente sigue vigente: insumos, restricciones 3.3 a 3.7, respaldos R1 a R4, verificaciones 7.1 a 7.9, afirmaciones prohibidas y estructura de carpetas.

**Reutilizar el código existente.** Agregar el nuevo diseño como opción de configuración, sin borrar el anterior. La configuración de la v1.1 debe poder reproducirse íntegra (prueba de regresión 6.1).

**Qué cambia y por qué:**

| # | Cambio | Motivo (revisión de Beth y Cath) |
|---|---|---|
| 1 | Nuevo diseño base D2: la parte privada de la cuota fija se convierte en una **tasa proporcional al salario**, neutral en recaudación, igual para formales e informales | El pago del informal en el diseño anterior (15,087 pesos al año; 14.3 % del ingreso en la mediana) no es creíble. Un tope al informal sin cambiar al formal rompe la regla de no arbitraje o es fiscalmente inviable. |
| 2 | Adopción base de 50 % (no 90 %); se distingue entre pagos **determinados** y pagos **cobrados** | Una adopción de 90 % no es creíble. |
| 3 | Tabla de asequibilidad | Hay que mostrar el peso del pago en el ingreso y contra el gasto de bolsillo. |
| 4 | Bloque C contra el status quo | F1 dentro del Bloque A sale neutro por construcción y no responde la pregunta del Núcleo 13. |
| 5 | Beneficiarios por titular del Informe = 1.07 | La v1.1 dividió los familiares entre cotizantes (1.83); los titulares del Cuadro I.4 incluyen pensionados. |
| 6 | C2 se presenta junto a la base | C1 cuenta dos veces a la población que la proyección institucional formaliza. |
| 7 | Umbrales indexados; D1 (precio plano en UMA) pasa a sensibilidad | Los umbrales fijos en UMA retiran el subsidio sin decisión explícita, y el precio plano en UMA reproduce el defecto de indexación del SEM. |
| 8 | Base de 337 días cotizados | Para que los puntos del SBC sean comparables con las primas del Informe. |
| 9 | Reescritura del anexo | La frase "el ingreso por titular cubre casi todo el costo", el Cuadro X.1, la lectura sobre el salario mínimo y las omisiones de capacidad y de población excluida. |

---

## 1. Nuevo diseño base: D2, tasa proporcional única

### 1.1 Tasa neutral en recaudación

Calcular, para **2026**, la tasa *c* que recauda de los formales lo mismo que hoy recauda la parte patronal de la cuota fija:

```
c = Σ_formales F_p,diaria × d  /  Σ_formales SBC_diario × d
F_p,diaria = 0.2040 × UMA_2026
d = 337 días cotizados (ver 1.5)
```

- Usar los cotizantes y el SBC de la proyección del libro (con la distribución R1).
- Valor esperado: alrededor de **3.5 %**.
- Registrar *c* en `NUMBERS.md` con cinco decimales.
- *c* queda **fija** a partir de 2026.

### 1.2 Pagos

**Formal, parte privada en especie (patrón y trabajador):**

```
π_F(w) = c × w × d + E(w)
```

- *w* es el SBC diario.
- E(·) no cambia.
- El ingreso del SEM por cuota fija **deja de estar indexado a la UMA** y crece con la masa salarial.

**Informal afiliado:**

```
π_I(m) = (1 − s(m)) × c × m × UMA × 365 + E(m)
```

- *m* es el ingreso laboral diario del titular en múltiplos de la UMA (ENIGH).
- El subsidio *s* se aplica **solo** sobre la parte proporcional.

**Gobierno Federal (G2, base en D2):**

- F_g por titular, formal o informal: 14.83 % de la UMA × 365, o × d para formales.
- Más s(m) × c × m × UMA × 365 por informal subsidiado.
- Más el Bloque B: formales con s(w) > 0 reciben s(w) × c × w × d. En S1 y S2 este monto debe ser nulo o casi nulo, porque m1 queda por debajo del salario mínimo; en S3 no.

**Sensibilidad G1:** el informal paga además (1 − s) × F_g. Sirve para mostrar el costo en asequibilidad.

### 1.3 Regla de no arbitraje

Con s = 0, π_I(m) = π_F(m) para el mismo ingreso anual. Con s > 0, el formal del mismo *m* recibe el mismo subsidio (Bloque B). La regla 3.1 se cumple por construcción.

**Verificación 7.6 ampliada:**

1. Igualdad ±1 peso con s = 0 en G2.
2. π_I ≥ π_F en todo el rango de *m*.
3. El subsidio del Bloque B nunca rebasa s × c × w × d.

### 1.4 Efecto de indexación (reportar por separado)

Para los formales, D2 recauda en 2026 lo mismo que el status quo. Después crece con el salario real, mientras la cuota fija vigente sigue a la UMA.

Reportar en una tabla propia, **fuera del saldo del esquema de informales**, la diferencia anual entre:

- la recaudación de D2 de los formales, y
- la recaudación con la cuota fija vigente,

en mdp, puntos del SBC y % de los ingresos del SEM, para 2030, 2040 y 2054.

Es el efecto de corregir la indexación a la UMA. Es parte del diseño, no del costo de afiliar informales.

### 1.5 Días

- Masa salarial y contribuciones de los formales: 337 días (Informe, Cuadro II.18).
- Informales: ingreso anual de la ENIGH (mensual × 12) y prima anual.
- Reportar el efecto del cambio de 365 a 337 días sobre los puntos del SBC del escenario base de la v1.1.

### 1.6 Umbrales

| Escenario | Regla |
|---|---|
| **Base** | m0 y m1 se indexan al crecimiento real del ingreso informal (el mismo de `Sup_Inc_Aseg&Sal` que ya se usa): la proporción de titulares subsidiados queda constante. |
| Sensibilidad | Umbrales fijos en UMA (comportamiento de la v1.1). |

---

## 2. Adopción, cobro y selección

### 2.1 Cobertura

| Escenario | Adopción τ | Uso |
|---|---|---|
| **Base** | 0.50 | |
| Sensibilidad | 0.30 | |
| Sensibilidad | 0.70 | |
| Sensibilidad | 0.90 | Rotular "solo con descuento automático vía impuesto negativo". |
| Sensibilidad T1 | v1.1, voluntaria | Se conserva. |

### 2.2 Cobro

La prima **determinada** de los afiliados no subsidiados del todo se cobra en proporción ρ:

| Escenario | ρ |
|---|---|
| **Base** | 0.75 |
| Sensibilidad | 0.50 |
| Sensibilidad | 1.00 |

- Para los titulares con s = 1 no hay prima privada.
- La prima no cobrada se reporta como renglón propio y **aumenta el saldo sin fuente de financiamiento asignada**.

### 2.3 Selección adversa

| Escenario | Multiplicador de costo μ |
|---|---|
| **Base (con τ < 0.9)** | 1.10 |
| Sensibilidad | 1.00 |
| Sensibilidad | 1.30 |

### 2.4 Rotulado

Todos son **supuestos ilustrativos**, no estimaciones (afirmación prohibida 2).

---

## 3. Salidas nuevas

### 3.1 Tabla de asequibilidad (`outputs/tables/asequibilidad.csv`)

Para los percentiles 10, 20, 30, 50, 70 y 90 del ingreso laboral del titular informal (2026), reportar en D2-G2 (base), D2-G1 y D1-G1 (v1.1):

- prima anual en pesos;
- prima como % del ingreso laboral del titular;
- prima como % del ingreso corriente del hogar;
- prima contra el gasto de bolsillo anual en salud **del hogar, por decil**, calculado directamente de la ENIGH 2024 (`concentradohogar`, rubro de salud; registrar la variable) para los hogares objetivo;
- como referencia, el costo de la cuota patronal para un formal de salario mínimo, antes y después de D2, en pesos y en % del salario.

### 3.2 Bloque C contra el status quo (`outputs/tables/bloque_C_vs_status_quo.csv`)

Escenario F1 (+3 millones de cotizantes al 2030, misma trayectoria y misma selección de hogares que en la v1.1), **sin Bloque A**: los hogares que se formalizan pasan de no tener cobertura contributiva a cotizar.

Reportar en 2030, 2040 y 2054, con dos versiones de la cuota (D2 y la cuota fija vigente):

| Concepto | Detalle |
|---|---|
| Ingresos al SEM | Cuotas privadas + F_g federal |
| Costo de atención | De sus derechohabientes |
| Efecto neto para el SEM | |
| Costo federal | F_g |
| Derechohabientes por cotizante | |

**Este es el número que regresa al Núcleo 13** como respuesta a la limitación de ingresos fijos. F1 dentro del Bloque A (v1.1) se conserva como sensibilidad.

### 3.3 Población excluida

Personas sin cobertura contributiva que **no** pertenecen a la población objetivo, porque en su hogar no hay ningún ocupado sin cobertura:

- total (esperado: unos 8.2 millones = 130.33 − 62.94 − 59.19 millones; verificar);
- estructura por edad (en particular, 65 años o más);
- proyección con CONAPO.

### 3.4 Referencia de gasto no contributivo (solo contexto, para Cath)

Registrar en `NUMBERS.md` el gasto en salud no contributivo del PEF 2026, tomado del cuadro del CIEP *"PPEF 2027: Gasto en salud por subsistema"* (Cuadro 1; mdp de 2027; lo proporcionó Héctor el 08-10-2026):

| Concepto | mdp de 2027 |
|---|---|
| SSa | 68,964.2 |
| IMSS-Bienestar | 177,591.9 |
| FASSA | 87,344.2 |
| Bienestar | 4,128.0 |
| **Total** | **338,028.3** |

- Convertir a pesos de 2026 con la inflación de 2027 de `Sup_Fin` (3.82 %) y registrar ambos valores.
- En el anexo se cita **solo** para decir que los pagos federales del esquema son brutos y no descuentan el gasto no contributivo que hoy atiende a esa población.
- **No** se concluye que sea una reasignación viable: esa lectura es de Cath.

---

## 4. Correcciones de datos

### 4.1 Beneficiarios por titular del Informe

h_b,Informe = familiares / titulares = 40,980,786 / 38,197,323 = **1.0729** (Cuadro I.4).

- Rehacer la sensibilidad U2 con este valor y quitar la de 1.83.
- Registrar además los 3.54 derechohabientes por cotizante como una razón que **incluye a pensionados y sus familias**.
- Anotar en `REPORT.md` que la calibración del Núcleo 13 ("unos 3 derechohabientes por cotizante") puede estar inflada por ese motivo.

### 4.2 Diferencia de derechohabientes con el Núcleo 13 (54.6 contra 70.7 millones)

- Revisar los cuadernos del Núcleo 13 (I6) para identificar qué variable de afiliación de la ENIGH usaron y cómo la ponderaron. Reportar el hallazgo con la celda o línea exacta.
- **No modificar el Núcleo 13.**
- La diferencia sigue siendo **bloqueante para integrar el anexo**, no para correr el modelo.

### 4.3 Salario mínimo frente a la mediana informal

Registrar el salario mínimo general de 2024 (esperado: 248.93 pesos diarios). Verificar la fuente:

- el Informe, si lo cita; si no,
- la resolución de la CONASAMI publicada en el DOF.

Calcular su equivalente en UMA de 2024 (esperado: unos 2.29) y compararlo con la mediana del ingreso laboral del titular informal (2.30 UMA de 2024).

---

## 5. Escenarios

**Base v1.2:** D2 · G2 · S1 (umbrales indexados) · U1 · τ = 0.50 · ρ = 0.75 · μ = 1.10 · C1 · F0 · π_m = 0 · perfil 65+/20-64 = 3.0 · 337 días.

**Malla:**

1. **Esquema:** S2, S3.
2. **Aportación federal:** G1.
3. **Precio:** D1 (precio plano en UMA, diseño de la v1.1).
4. **Adopción:** τ = 0.30, 0.70 y 0.90; T1.
5. **Cobro:** ρ = 0.50 y 1.00.
6. **Selección:** μ = 1.00 y 1.30.
7. **Unidad:** U2 con h_b de la ENIGH (0.80) y del Informe (1.07).
8. **Costo:** π_m = 1 % y 2 %.
9. **Coherencia:** C2.
10. **Formalización:** F1 (dentro de A) y F1 contra el status quo (3.2).
11. **Perfil de costo:** plano, 2 y 4.
12. **Umbrales:** fijos en UMA.

---

## 6. Verificaciones adicionales (además de las de la sección 7 de la v1.1)

| # | Verificación | Criterio |
|---|---|---|
| 6.1 | **Regresión** | Con D1 · G1 · τ = 0.90 · ρ = 1 · μ = 1 · umbrales fijos · 365 días, se reproducen exactamente las cifras de la v1.1 (por ejemplo, saldo base de 2030 = −16,875 mdp; pagos federales de 2054 = 87,703 mdp). |
| 6.2 | Neutralidad de *c* | La recaudación de D2 de los formales en 2026 es igual a la del status quo, ±0.1 %. |
| 6.3 | No arbitraje en D2 | Los criterios de 1.3, en toda la malla de *m* y en todos los escenarios. |
| 6.4 | Identidades contables | Pagos determinados = cobrados + no cobrados; ingreso − costo = saldo; A + B + C = total; el efecto de indexación (1.4) va fuera del saldo de informales y se suma solo en un renglón de "total del diseño", claramente separado. |
| 6.5 | Monotonicidad | Mayor τ implica más cobertura; menor ρ implica peor saldo; mayor μ implica más costo. |
| 6.6 | Asequibilidad | En D2-G2, la prima de la mediana debe quedar alrededor de 3,700 pesos al año (orden de magnitud estimado por Beth). Si se aleja más de 25 %, explicar por qué. |

---

## 7. Anexo: `ANEXO_borrador_v2.md`

Mismo formato institucional. El documento compartido lo actualizará Héctor o Beth.

### 7.1 Cambios obligatorios

1. **Título:** "Anexo X. Ingresos y costos de esquemas de afiliación subsidiada al SEM: ejercicio preliminar (ITED)".
2. **X.2 Diseño.** Explicar D2 en un párrafo:
   - la parte privada de la cuota fija se vuelve una tasa proporcional neutral en recaudación;
   - informales y formales pagan la misma tasa;
   - el Gobierno Federal mantiene F_g por titular y subsidia los deciles bajos;
   - resultado: no hay arbitraje y la cuota deja de erosionarse con la UMA.

   Mencionar que D1 se reporta como sensibilidad y por qué no funciona (asequibilidad).
3. **X.4. Primer párrafo nuevo, sin titular de "cubre el costo".** Reportar en este orden:
   - la prima de la mediana;
   - los pagos determinados y los cobrados;
   - los pagos federales, aclarando que son **brutos** y no descuentan el gasto no contributivo actual (3.4);
   - el costo;
   - el **saldo sin fuente de financiamiento asignada**.
4. **Cuadro X.1 en tres paneles:** (a) mdp de 2026, (b) puntos del SBC, (c) % de los ingresos del SEM. Una métrica por celda.
   - Incluir los renglones: cubiertos, pagos determinados, pagos cobrados, pagos federales (F_g, subsidio, Bloque B), costo y saldo.
   - Incluir el saldo con π_m = 0 y con π_m = 1 %.
   - Mostrar C1 y C2 lado a lado en 2040 y 2054.
5. **Lectura del salario mínimo.** Sustituir la frase "el salario mínimo cumple, por sí solo, la regla de no arbitraje" por el hallazgo:
   - la mediana del ingreso laboral del titular informal equivale aproximadamente a un salario mínimo (cifras de 4.3);
   - por eso el tramo subsidiado queda por debajo del mínimo;
   - el riesgo relevante es el salto al primer empleo formal en el salario mínimo, que D2 reduce: costo patronal antes y después.
6. **Tabla de asequibilidad** (3.1), resumida.
7. **Bloque C contra el status quo** (3.2), como respuesta explícita a la limitación de ingresos fijos del Núcleo 13.
8. **Efecto de indexación** (1.4), en un párrafo y una tabla corta, separado del esquema de informales.
9. **Limitaciones, agregar:**
   - el costo es **promedio, no marginal**: no incluye inversión en capacidad. La población cubierta equivale a X % de los 79.2 millones de derechohabientes actuales. Contexto de ocupación hospitalaria: 75.7 % en segundo nivel y 83.7 % en tercero (Informe; registrar cuadro y página);
   - la población excluida (3.3);
   - adopción, cobro y selección son supuestos;
   - la diferencia de derechohabientes con el Núcleo 13 (4.2).
10. **R2:** sustituir "1.83 familiares por cotizante" por "1.07 familiares por titular (Cuadro I.4)".
11. **Pie:** "Registro de cifras y verificaciones disponibles a solicitud (ITED)". Sin rutas de Dalila.

---

## 8. Afirmaciones prohibidas (además de las de la v1.1)

1. Decir o sugerir que el esquema "cubre su costo" o "se autofinancia".
2. Llamar a D2 propuesta del IMSS o del Gobierno. Es un diseño de análisis de ITED.
3. Concluir que el gasto no contributivo actual "alcanza" o "puede reasignarse". Esa lectura es de Cath.
4. Presentar la adopción, el cobro o la selección como estimaciones.
5. Sumar el efecto de indexación (1.4) al saldo del esquema de informales sin separarlo.

---

## 9. Reporte

Actualizar `REPORT.md` (sección nueva "v1.2") con:

1. Resumen del escenario base v1.2 en 2026, 2030, 2040 y 2054.
2. Prima de la mediana.
3. Efecto de indexación.
4. Bloque C contra el status quo.
5. Las tres sensibilidades que más mueven el saldo.
6. Resultado de la prueba de regresión y de las verificaciones 6.1 a 6.6.
7. Hallazgo sobre la variable de afiliación del Núcleo 13 (4.2).
8. Decisiones propias marcadas como **[REVISAR]**.

Hacer commit en Git y archivar esta instrucción en `_crossrefs/_build_instructions/`. Marcar la v1.1 como `superseded` solo en lo que esta versión modifica; anotarlo en el frontmatter de la v1.1 si el esquema lo permite.
