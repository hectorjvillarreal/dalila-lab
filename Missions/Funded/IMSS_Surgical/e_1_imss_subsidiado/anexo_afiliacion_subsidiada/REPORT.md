# REPORT — Anexo preliminar del Núcleo 13: afiliación subsidiada al SEM

**Instrucción:** `20261017_BDH_N13_anexo-afiliacion-subsidiada_build_v1.1` (Beth). **Ejecutó:** Claude Code, 2026-10-17, autorizado por Héctor.
**Rótulo:** ejercicio preliminar de ITED; usa insumos institucionales, pero no es una proyección del IMSS. Las conclusiones de sostenibilidad corresponden a Cath.
**Reproducir:** `conda activate dalila && python src/run_all.py` (unos 70 s). Todas las cifras están en `NUMBERS.md`.

---

# v1.3 — Borrador con el denominador común (2026-10-18)

**Instrucción:** `20261018_BDH_N13_anexo-afiliacion-subsidiada_build_v1.3` (Beth; revisión pendiente de Cath). Archivada en `_crossrefs/_build_instructions/2026-10-18_BDH-N13_anexo-afiliacion-subsidiada_retrofit_v1.3.md`. Producto: `ANEXO_borrador_v3.md`; el v2 se conserva. Lo genera `src/borrador_v3.py`, dentro de `run_all.py`.

- **Cifras sustituidas:** el borrador tiene 169 cifras en puntos del salario o en % de los ingresos del SEM (166 claves). **112 cambian de texto**; las otras 57 quedan iguales con el redondeo del v2.
  - Por sección: Cuadro X.1 (b) 37 de 54; Cuadro X.1 (c) 26 de 54; Cuadro X.2 41 de 46; X.4 texto 2 de 2; X.5 2 de 6; X.6 3 de 6; X.7 texto 1 de 1.
  - Ejemplo: en 2030, «1.36 puntos del SBC y 13.2 % de los ingresos del SEM» pasa a «1.30 puntos del SBC y 12.9 %». El valor es −1.3047; el REPORT de la v1.1 del experimento 2 lo cita como −1.305.
- **Oración nueva (X.3):** sustituye a la oración anterior sobre el denominador. Dice que los puntos se miden sobre la masa R1 con tope de 25 UMA y piso en el mínimo (337 días), que el % del SEM usa el Cuadro V.13 y que el libro se usa para cotizantes, salarios y supuestos.
- **Oraciones marcadas [REVISAR]:** ninguna. Se revisaron todas las afirmaciones comparativas y siguen siendo ciertas con las cifras nuevas:
  - el costo per cápita sigue siendo la sensibilidad que más mueve el saldo de 2054 (−1.195 puntos frente a la base);
  - el saldo sigue bajando en puntos;
  - el esquema individual sigue mejorando el saldo.
- **Trazabilidad:** `outputs/tables/exp1_borrador_v2_a_v3.csv`, una fila por cifra con clave en `NUMBERS.md`, texto anterior, texto nuevo, sección y si cambia.
- **Registro nuevo:** cada celda de los paneles (b) y (c) del Cuadro X.1 (claves `X1_*`). Las columnas C2 y algunos años no tenían clave antes.

**Verificaciones (sección 3):**

| # | Resultado | Estado |
|---|---|---|
| 3.1 | Montos en mdp que cambian del v2 al v3: 0 | ✓ |
| 3.2 | Cifras sustituidas sin registro o con valor distinto en `NUMBERS.md`: 0. Además, antes de sustituir, cada celda del v2 se comparó con el valor anterior (commit `2253249`): 0 discrepancias | ✓ |
| 3.3 | De las 112 cifras que cambian (109 claves distintas), 83 claves están entre las 186 de `exp1_cambios_denominador.csv`. Las otras 26 son celdas del Cuadro X.1 que no tenían clave antes de la v1.3 (columnas C2 y años sin registro previo) y ahora están registradas | ✓, con esa salvedad |
| 3.4 | Líneas que cambian fuera de las cifras y de la oración del denominador: 0 | ✓ |
| 3.5 | Sin 2055 en el borrador fuera de la oración del v2 que explica que no se reporta, que se conserva porque el diff no puede tocar la redacción | ✓ |

**Diff resumido:**

- 1 oración sustituida (X.3).
- 2 cifras en el texto de X.4 y 1 en el texto de X.7.
- 63 celdas del Cuadro X.1, 41 del Cuadro X.2, 2 de X.5 y 3 de X.6.
- Nada más.

---

# Experimento 2 — Cuota del Infonavit a un nuevo seguro solidario de salud y cuidados (2026-10-18)

Por decisión de Héctor, el experimento 2 vive en su propia carpeta: `../../e_2_imss_nuevoseguro/`. Ahí están su reporte (`REPORT.md`, sección «Experimento 2»), su registro de cifras (`NUMBERS.md`, sección «Experimento 2») y su borrador (`ANEXO_experimento2_borrador.md`). Reutiliza los módulos y derivados de esta v1.2 sin escribir en ellos. La única combinación permitida con este experimento es la columna (c) de su tabla de cuña contributiva legal, que usa la tasa D2 (3.467 %).

**Denominador común (instrucción v1.1 del experimento 2, sección 4).** Desde el 18-10-2026, las salidas v1.2 de este anexo usan dos referencias nuevas. Los puntos del salario se miden sobre la masa R1 con tope y piso (337 días), la misma base de la tasa D2. El % de los ingresos del SEM se mide sobre el Cuadro V.13 del Informe. El libro de Finanzas se sigue usando para cotizantes, salarios y supuestos. Los montos en mdp no cambian. Cambian 186 cifras del registro (123 en puntos y 63 en %); la tabla de cambios está en `../../e_2_imss_nuevoseguro/tablas/exp1_cambios_denominador.csv`. Por ejemplo, el saldo total de 2030 pasa de −1.357 a −1.305 puntos y de −13.25 % a −12.93 % de los ingresos del SEM. **`ANEXO_borrador_v2.md` sigue citando las cifras anteriores** y se actualiza cuando Beth lo indique. Las tablas de las secciones v1.2.1 a v1.2.4 de este reporte también tienen los valores anteriores en puntos y en %; los vigentes están en `NUMBERS.md`.

---

# v1.2 — Tasa proporcional única y pago creíble (2026-10-17)

**Instrucción:** `20261017_BDH_N13_anexo-afiliacion-subsidiada_build_v1.2` (Beth y Cath). Producto para el anexo: `ANEXO_borrador_v2.md`. Lo que sigue a esta sección es el reporte de la v1.1, que se conserva: la prueba de regresión 6.1 la reproduce exactamente.

## v1.2.1 Escenario base

D2 · G2 · S1 con umbrales indexados · U1 · τ = 0.50 · ρ = 0.75 · μ = 1.10 · C1 · F0 · π_m = 0 · perfil 3.0 · 337 días.

Montos en mdp de 2026.

| | 2026 | 2030 | 2040 | 2054 |
|---|---|---|---|---|
| Personas cubiertas | 30.8 M | 31.4 M | 32.2 M | 31.7 M |
| Pagos determinados | 52,137 | 56,676 | 67,181 | 77,796 |
| Pagos cobrados | 39,103 | 42,507 | 50,386 | 58,347 |
| Pagos federales (F_g + subsidio) | 70,332 | 73,769 | 80,153 | 82,984 |
| Costo de atención | 190,614 | 197,237 | 211,185 | 221,667 |
| **Saldo sin fuente asignada** | **−81,179** | **−80,962** | **−80,647** | **−80,335** |
| Saldo en puntos del SBC | −1.57 | −1.36 | −0.93 | −0.59 |
| Saldo en % de los ingresos del SEM | −14.7 | −13.2 | −9.7 | −6.7 |

- **Tasa neutral:** c = **0.03467** (3.467 %; Beth esperaba alrededor de 3.5 %).
- **Prima de la mediana (D2-G2):** **3,647 pesos al año**, 3.5 % del ingreso laboral del titular y 1.7 % del ingreso del hogar. Con D1-G1 (v1.1) era de 15,087 pesos, 14.3 % del ingreso laboral.
- **Bloque B en la base:** 0 en todos los años (S1).
- **Población excluida:** 8,195,479 personas (19.5 % de 65 años o más). En 2054 serían 10.1 M, con 3.8 M de 65 años o más.
- **Cobertura frente a la derechohabiencia actual:** la población cubierta equivale a 39.7 % de los derechohabientes de 2030.

## v1.2.2 Efecto de indexación (fuera del saldo del esquema de informales)

| | 2030 | 2040 | 2054 |
|---|---|---|---|
| Recaudación D2 − cuota fija vigente, formales (mdp) | 11,611 | 35,589 | 98,909 |
| Puntos del SBC | 0.19 | 0.41 | 0.73 |
| % de los ingresos del SEM | 1.9 | 4.3 | 8.2 |

## v1.2.3 Bloque C contra el status quo: el número que regresa al Núcleo 13

Escenario: +3 M de cotizantes al 2030, sin Bloque A, solo cobertura en especie.

| | 2030 | 2054 |
|---|---|---|
| Efecto neto para el SEM con D2 | −11,512 mdp (−0.19 pts) | −9,098 mdp (−0.07 pts) |
| Efecto neto para el SEM con la cuota vigente | −5,755 mdp (−0.10 pts) | −5,947 mdp (−0.04 pts) |
| Costo federal (F_g) | 17,591 mdp | 19,426 mdp |
| Derechohabientes por cotizante | 2.93 | 2.68 |

**Lectura para Cath:** con solo la cobertura en especie, formalizar a estos hogares **no** alivia el SEM. Los nuevos cotizantes ganan cerca del salario mínimo y cada uno trae casi 3 derechohabientes.

## v1.2.4 Las sensibilidades que más mueven el saldo de 2054

Base: −0.59 puntos del SBC.

| # | Sensibilidad | Saldo 2054 (pts SBC) |
|---|---|---|
| 1 | Costo per cápita +2 % real anual | −1.80 |
| 2 | Costo per cápita +1 % real anual | −1.12 |
| 3 | U2 con h_b de la ENIGH (0.80) | −0.09 |
| 4 | Adopción 0.90 (solo con descuento automático) | −1.07 |

En 2030 el orden cambia y la adopción domina: con 0.90, el saldo es −2.44 puntos.

## v1.2.5 Verificaciones 6.1 a 6.6, además de las de la sección 7 de la v1.1

| # | Verificación | Resultado | ¿Pasa? |
|---|---|---|---|
| 6.1 | Regresión: D1·G1·τ 0.90·ρ 1·μ 1·umbrales fijos·365 días reproduce la v1.1 | Desviación máxima 0 (saldo 2030 = −16,875; pagos federales 2054 = 87,703) | sí |
| 6.2 | Neutralidad de c en 2026 (±0.1 %) | 0.0000 % | sí |
| 6.3.1 | Igualdad ±1 peso en G2, malla 0-25 UMA × S × G, años 2026 y 2054 | 0 casos fuera | sí |
| 6.3.2 | π_I ≥ π_F | 0 violaciones | sí |
| 6.3.3 | Subsidio B ≤ s·c·w·d | 0 violaciones | sí |
| 6.4 | Determinados = cobrados + no cobrados; ingreso − costo = saldo; A + B + C = total; indexación fuera del saldo | Desviación 0 en todas | sí |
| 6.5 | τ ↑ ⇒ más cobertura; ρ ↓ ⇒ peor saldo; μ ↑ ⇒ más costo | 0 años fallan en cada una | sí |
| 6.6 | Prima de la mediana D2-G2 ≈ 3,700 (±25 %) | 3,647 (−1.4 %) | sí |
| 7.7 / 7.8 | Monotonicidad π_m y S; sin año 2055 | 0 / 0 | sí |

## v1.2.6 Correcciones de datos

- **4.1 Beneficiarios por titular del Informe:** 40,980,786 / 38,197,323 = 1.0729. U2 se rehizo con ese valor (se quitó el de 1.83).
  - Los 3.54 derechohabientes por cotizante incluyen a pensionados y sus familias. La calibración del Núcleo 13 («unos 3 derechohabientes por cotizante») puede estar inflada por ese motivo.
  - **[REVISAR]** Los 38.2 M de titulares incluyen 8.4 M del Seguro Facultativo, casi todos estudiantes sin beneficiarios. El 1.07 probablemente **subestima** los beneficiarios por trabajador; el valor verdadero estaría entre 1.07 y 1.83.
- **4.2 Diferencia de derechohabientes con el Núcleo 13 (54.6 frente a 70.7 M): NO RESUELTO.**
  - Los cuadernos `Ingresos_borrador.ipynb` y `reporte_final_borrador.ipynb` no están en Dalila. Busqué en todo el directorio personal; el Anexo B del Núcleo 13 dice que se entregaron en archivo aparte.
  - Sigue siendo bloqueante para integrar el anexo. Se necesita que Juan Pablo los comparta.
- **4.3 Salario mínimo 2024:** 248.93 pesos diarios (resto del país; 374.89 en la Zona Libre de la Frontera Norte), según la Resolución del H. Consejo de Representantes de la CONASAMI, DOF 12/12/2023 (verificado en dof.gob.mx). Equivale a 2.2928 UMA de 2024; la mediana del titular informal es 2.2979, es decir, 1.002 veces el salario mínimo.
- **1.5 Días:** con masa de 337 días, el saldo base de la v1.1 pasa de −0.26 a −0.28 puntos del SBC en 2030, y de −0.12 a −0.13 en 2054.
- **3.4 Gasto no contributivo, PEF 2026 (CIEP, Cuadro 1):** 338,028.3 mdp de 2027, que equivalen a 325,590.7 mdp de 2026 (÷ 1.0382). Solo es contexto: se cita para decir que los pagos federales son brutos.

## v1.2.7 Decisiones propias (para revisión de Héctor)

1. **[REVISAR] c con la distribución R1:** usa el SBC de la distribución R1 de 2026, con piso en el salario mínimo, multiplicado por los cotizantes del libro, no el promedio del libro sin piso. La indexación (1.4) usa la misma masa, así que incluye el efecto de que el salario mínimo suba más rápido que la UMA.
2. **[REVISAR] Comparación «mismo ingreso anual»:** el subsidio se evalúa con el ingreso anualizado m̃ = w·d/365 para los formales. El excedente usa el umbral anual de 3 UMA × 337 días para formales e informales. Sin esto, la igualdad de 6.3.1 falla por diferencias de días.
3. **[REVISAR] U2 en D2:** cada miembro paga c sobre el ingreso corriente per cápita del hogar. F_g se reparte entre (1 + h_b).
4. **[REVISAR] El cobro ρ se aplica a toda la prima determinada, incluido el excedente.** Los formales del Bloque C pagan completo.
5. **[REVISAR] Asequibilidad:**
   - El ingreso del hogar es la mediana de los titulares en ±2.5 percentiles alrededor de cada percentil.
   - El gasto de bolsillo es `concentradohogar.salud` (cuidados de la salud) × 4, solo con conversión de precios (UMA 2026 / UMA 2024). El ingreso lleva además el crecimiento real a 2026.
6. **[REVISAR] Umbrales indexados con el crecimiento real del SBC.** Después de 2030 crecen más rápido que el salario mínimo (+0.5 %). Por eso, en S3, el costo del Bloque B vuelve a crecer: 10,162 mdp en 2026, 1,104 en 2030 y 15,243 en 2054.
7. **[REVISAR] Bloque C contra el status quo:**
   - Solo cobertura en especie, sin prestaciones en dinero, GMP ni otros seguros.
   - SBC = max(ingreso, salario mínimo), con cobertura completa del hogar (μ = 1).
   - Mismos hogares y misma trayectoria que el F1 de la v1.1.
8. **Frontmatter:** `build_type: revision` no existe en PROTO-RAG-001. Se archivó como `retrofit`, el valor más cercano.
9. **PEF:** las cifras del cuadro del CIEP se rotulan como PEF 2026 en mdp de 2027, según confirmó Héctor.
10. La configuración v1.1 se conserva íntegra en `config.yaml` (`base`, `malla`). La v1.2 está en `base_v12` y `malla_v12`.

---

# v1.1 — Reporte original

## 1. Resumen

### Escenario base (S1 · G1 · U1 · T2 · C1 · F0 · π_m = 0 · perfil 65+/20-64 = 3.0)

Montos en mdp de 2026. Entre paréntesis: puntos del SBC; % de los ingresos del SEM.

| | 2030 | 2040 | 2054 |
|---|---|---|---|
| Personas cubiertas (Bloque A) | 56.5 M | 57.9 M | 57.0 M |
| Titulares afiliados | 19.3 M | 20.8 M | 21.3 M |
| Pagos de afiliados | 211,406 (3.27; 34.6 %) | 239,104 (2.53; 28.7 %) | 257,856 (1.76; 21.4 %) |
| Pagos federales del Bloque A | 94,471 (1.46; 15.5 %) | 93,878 (0.99; 11.3 %) | 87,703 (0.60; 7.3 %) |
| Costo del Bloque B | 0 | 0 | 0 |
| Costo de atención | 322,752 (5.00; 52.8 %) | 345,576 (3.66; 41.5 %) | 362,727 (2.47; 30.1 %) |
| Saldo para el SEM | −16,875 (−0.26; −2.8 %) | −12,594 (−0.13; −1.5 %) | −17,167 (−0.12; −1.4 %) |

En 2026, el costo de atención del Bloque A equivale a 0.81 % del PIB y los pagos federales a 0.24 %. Es la única columna en % del PIB, porque el Informe solo da el PIB de 2026.

### Lo que hay que saber antes de leer las cifras

1. **El Bloque B no tiene costo en S1 ni en S2.** La razón es el salario mínimo.
   - Ningún formal cotiza por debajo del salario mínimo, que equivale a 2.46 UMA en 2025, 2.69 en 2026 y 3.65 en 2030.
   - El umbral m1 de S1 es 2.46 UMA de 2026 (percentil 50 del titular informal) y el de S2 es 1.66.
   - Solo S3 (m1 = 3.29) tiene costo: 14,319 mdp en 2026, 10,320 en 2027 y 4,819 en 2028, para unos 4.6 millones de formales. Desde 2029 el salario mínimo rebasa m1 y el costo es cero.
   - **La regla de no arbitraje la cumple el salario mínimo antes que el Bloque B.**
2. **Con T2, el saldo no depende de S ni de G.** La v1.1 fija que afiliado + Gobierno Federal = P* + E(m) por titular, y con adopción fija el ingreso total del SEM no cambia. S y G solo mueven quién paga.
   - En 2054, los pagos federales totales van de 53,575 mdp (S2) a 138,236 (S3) y 186,103 (G2), frente a 87,703 en la base.
3. **El costo crece con la población cubierta y los ingresos del SEM crecen con la formalización institucional.** El costo del Bloque A pasa de 56.4 % a 30.1 % de los ingresos del SEM entre 2026 y 2054. La caída se debe a que el denominador crece (cotizantes de 22.35 a 46.8 millones), no a que el Bloque A se abarate.

### Las tres sensibilidades que más mueven el saldo de 2054

En puntos del SBC; la base es −0.12.

| # | Sensibilidad | Saldo 2054 | Por qué |
|---|---|---|---|
| 1 | Crecimiento real del costo per cápita π_m = 2 % | −1.95 (−285,957 mdp) | El costo se acumula 28 años; el ingreso por titular no se indexa al costo |
| 2 | U2 individual con h_b de la ENIGH | +0.96 (+140,919 mdp) | La ENIGH da 0.80 beneficiarios por titular. El precio por persona, P*/1.80, cobra más de un P* por hogar de 3 personas. **Es un artefacto de R2:** con la razón del Informe (1.83 familiares por cotizante) el saldo es −0.23 |
| 3 | π_m = 1 % | −0.91 (−133,708 mdp) | Igual que el punto 1 |

---

## 2. Verificaciones de la sección 7

| # | Verificación | Resultado | ¿Pasa? |
|---|---|---|---|
| 7.1 | Asegurados dic. 2025: 21,800,692 (H 13,102,667; M 8,698,025) | Idéntico | sí |
| 7.1 | TIMSS dic. 2025: 551,894 | Idéntico | sí |
| 7.1 | Total 22,352,586 = stock 2025 de `Pob Emp & Nuevos` | Idéntico | sí |
| 7.1 | SBC promedio ponderado 627.21 | 627.21 (627.2063) | sí |
| 7.1 | Aportación federal SEM-A 2025 reconstruida, a menos de 3 % de 146,457 | 144,610 (−1.26 %) | sí |
| 7.2 | Libro de Finanzas frente al Cuadro II.14 | Cuotas +8,822; GF −1,055; otros +12,511; total 851,311 frente a 831,033 (+20,278). Se usa el libro | reportado |
| 7.3 | Retención de hombres ≈ 0.94 | 0.941 | sí |
| 7.3 | Retención de mujeres ≈ 0.92 | 0.921 | sí |
| 7.3 | Retención de 15 a 24 años: 0.81 a 0.85 | 0.830 (H 0.845, M 0.806) | sí |
| 7.3 | Antigüedad cero en 2025 ≈ 1.69 M | 1,689,393 | sí |
| 7.4 | Población ENIGH expandida / con IMSS | 130,325,969 / 53,630,567 | reportado |
| 7.4 | Contraste con los 70.7 M del Núcleo 13 y los 79.2 M del Informe | El método del Anexo I (tasa IMSS por edad y sexo × CONAPO 2025) da **54.6 M**, no 70.7 M. Ver sección 6 | **discrepancia** |
| 7.4 | Proporción de ocupados sin cobertura contributiva, por decil de hogares | Decil I 92.2 % … decil X 26.3 % (`enigh_informalidad_por_decil.csv`) | reportado |
| 7.5 | Ingreso − costo = saldo, en cada escenario y año | Desviación máxima 0 | sí |
| 7.5 | A + B + C = total | Desviación máxima 0 | sí |
| 7.6.1 | π_I ≥ π_F en toda la malla 0–25 UMA (paso 0.1) × S × G × U | 0 violaciones | sí |
| 7.6.2 | Diferencia = 0 en G2 y (1 − s)·F_g en G1, ±1 peso | 0 casos fuera | sí |
| 7.6.3 | Costo_B = 0 si m ≥ m1; Costo_B ≤ F_p | 0 / 0 casos | sí |
| 7.6.4 | Afiliado + Gobierno Federal = P* + E(m) | 0 casos | sí |
| 7.6.5 | Pago vigente frente a π_I antes de la reforma | 213 puntos de la malla con π_I < π_F^vig. Es el arbitraje que crearía el subsidio sin Bloque B; en la práctica casi todos quedan bajo el salario mínimo | documentado |
| 7.6.6 | Brecha GMP | `brecha_GMP.csv`: 0.01425 · m · UMA · 365 por titular. No se corrige con el Bloque B | documentado |
| 7.7 | π_m mayor ⇒ costo mayor | 0 años fallan | sí |
| 7.7 | T1: más subsidio ⇒ más adopción | 0 violaciones | sí |
| 7.7 | Costo fiscal S3 > S1 > S2 | 0 años fallan | sí |
| 7.8 | Ningún año 2055 en las salidas | 0 (las tablas van de 2025 o 2026 a 2054) | sí |
| 7.9 | Todo en pesos de 2026 | Pesos de dic. 2025 × 1.037 (inflación 2026 de `Sup_Fin`). La ENIGH se usa en múltiplos de la UMA de 2024, así que no necesita deflactor | sí |

**Prueba C (sección 4.5)**

| | 2030 | 2040 | 2054 |
|---|---|---|---|
| Formalidad implícita (cotizantes / ocupados) | 36.5 % | 46.0 % | 63.1 % |
| Edades con más cotizantes que ocupados | ninguna | ninguna | mujeres de 24 a 37 años, exceso de 896,273 |

La formalidad implícita en 2025 es 34.0 %. Esto confirma la tensión del Anexo I del Núcleo 13 con un método independiente (ocupados en vez de derechohabientes). En C2, la población objetivo baja a 0.96 (2030), 0.81 (2040) y 0.57 (2054) de la de C1.

---

## 3. Respaldos y dirección probable del sesgo

| Respaldo | Qué se hizo | Sesgo probable |
|---|---|---|
| R1 — distribución del SBC | Forma del ingreso subordinado principal (P001-P009) de asalariados con IMSS por prestación en la ENIGH (45,754 obs.), reescalada al SBC promedio del libro por grupo de edad y sexo; piso en el salario mínimo (12.3 % de la masa de la forma queda debajo y se trunca); tope 25 UMA | Subestima la cola baja del SBC porque los trabajadores con salario mínimo se apilan en el piso; **el costo del Bloque B en S3 es una cota inferior** |
| R2 — beneficiarios por titular | h_b = 0.80 en la ENIGH, contra 1.83 familiares por cotizante y 3.54 derechohabientes por cotizante en el Informe | La ENIGH subestima beneficiarios porque no ve a los de otros hogares ni a los no adscritos. **U2 con h_b de la ENIGH sobrestima el ingreso**; la corrida con h_b del Informe lo acota |
| R3 — perfil de costo | Sin perfil NTA. Ancla de nivel: 494,275 mdp / 79,178,109 DH = 6,242.57 pesos por derechohabiente; forma escalonada 65+/20-64 = 3 (sensibilidades 1, 2 y 4), normalizada sobre la estructura por edad de los afiliados al IMSS en la ENIGH; sin diferencia por sexo | La población objetivo es más joven: 5,622 pesos por persona cubierta en 2026. Un perfil con costos altos en la infancia y por sexo (maternidad) podría elevarlo |
| R4 — antigüedad | Se lee como años desde el primer registro | Hay 85,615 personas con antigüedad cero y 50 años o más, lo que es compatible con reingresos o con tiempo cotizado. **La retención es indicativa, no una tasa de desafiliación** |

---

## 4. Decisiones que tomé por mi cuenta (para revisión de Héctor)

1. **[REVISAR] Pesos de 2026:** la UMA de 2026 se toma como 113.14 × 1.037 = 117.33. Con eso, F_p = 8,736, F_g = 6,351 y P* = 15,087 pesos. La instrucción ilustra con pesos de dic. 2025 (8,424; 6,124; 14,549).
2. **[REVISAR] Umbrales m0 y m1:** son los percentiles de la ENIGH llevados a 2026 con un factor de 1.0689 (2.6 % de crecimiento del SBC en UMA en 2025, según el Informe, por el crecimiento real del SBC de 2026 en `Sup_Inc`). Después quedan **fijos en UMA**. Como los ingresos crecen, el subsidio se reduce con el tiempo.
3. **[REVISAR] Crecimiento del ingreso informal y formal:** columna «Total» del crecimiento real del SBC en `Sup_Inc_Aseg&Sal`.
4. **[REVISAR] Ingreso laboral de la ENIGH:** claves P001-P022 (sin P010 ni P017, que no existen) más los ingresos de negocios agropecuarios y no agropecuarios por persona. Suma 2.9 % más que `ingtrab` de `concentradohogar`.
5. **[REVISAR] Cobertura contributiva:** `inst_1` a `inst_4` (IMSS, ISSSTE, ISSSTE estatal, Pemex/Defensa/Marina) por cualquier motivo de afiliación. Ocupado es quien tiene registro en `trabajos`. El titular es el ocupado sin cobertura con mayor ingreso laboral y al menos 15 años.
6. **[REVISAR] Proyección de la población objetivo:** se reponderan los microdatos con CONAPO(edad, sexo, t) / ENIGH(edad, sexo), con 90+ agrupado. La estructura del hogar no se reconstruye año con año.
7. **[REVISAR] U2:** los umbrales se recalculan como los mismos percentiles del **ingreso per cápita** de las personas objetivo. Usar los del titular subsidiaría casi a todos.
8. **[REVISAR] C2 como índice:** C2 se iguala con C1 en 2025 y sigue la dinámica de max(0, ocupados − cotizantes). La resta literal da 43.4 M en 2025 frente a 32.5 M informales de C1, porque incluye a ocupados con ISSSTE y a beneficiarios.
9. **[REVISAR] F1:** cada año se mueve una fracción uniforme de todos los hogares objetivo (con sus miembros sin cobertura), con cobertura completa (τ = 1, μ = 1). El SBC de los nuevos cotizantes es max(m, salario mínimo). Después de 2030 la fracción se mantiene constante. Resultado: 2.93 derechohabientes por cotizante en 2030, coherente con la calibración del Núcleo 13.
10. **[REVISAR] Cotizantes por edad:** se replica el modelo de cohortes del Anexo H del Núcleo 13 sumando todas las causas de salida de las bases biométricas. El factor de calibración queda entre 0.9962 y 1.0041 (el Núcleo 13 reporta entre 0.9955 y 1.0042).
11. **[REVISAR] Masa salarial para los puntos del SBC:** cotizantes del libro × 627.21 × 1.037 × crecimiento real × 365 días. El IMSS usa 337 días cotizados; con 337 días los puntos subirían alrededor de 8 %.
12. **Sensibilidad añadida:** `U2_hInforme` (h_b = 1.83) para acotar el artefacto de R2.
13. **% del PIB:** solo para 2026, porque el Informe no trae el PIB de otros años.
14. **Documentación:** cada módulo de `src/` tiene su `.md` companion.

---

## 5. Hallazgos que van más allá de la instrucción

- **Lo que dice la v1.1 sobre E(m) no se cumple en S3.** La sección 4.2 dice que E(m) opera «muy por arriba de m1 en todos los escenarios S», pero el m1 de S3 es 3.29 UMA, arriba del umbral de 3. El efecto es menor: E(m) es muy pequeño entre 3 y 3.29.
- **El Bloque B es casi vacío por construcción.** Ver el resumen. Para Beth: el instrumento relevante contra el arbitraje es el salto del informal subsidiado al primer empleo formal **en el salario mínimo** (8,736 pesos de cuota patronal fija en 2026), no la comparación al mismo m. Esa brecha cae sola: la cuota fija baja de 14.3 % del salario mínimo en 2025 a 9.66 % en 2030 y 8.57 % en 2054.
- **Discrepancia con el Núcleo 13 (7.4).** Con `inst_1` ponderado, la tasa IMSS de la ENIGH es 41.2 % y da 54.6 M de derechohabientes en 2025, no 70.7 M. El Anexo I habla de tasas de 44 % a 59 % por rango. Probé `inst_1 | inst_5` (IMSS-Bienestar): 44.7 %, tampoco cuadra. **Hay que revisarlo con Juan Pablo antes de anexar:** si el Núcleo 13 usó otra variable, su derechohabiencia está sobrestimada alrededor de 30 %.

---

## 6. Pendientes que requieren datos del IMSS en una fase posterior

- Distribución del SBC por tramo de ingreso (sustituye a R1; decide el costo del Bloque B en S3).
- Derechohabientes por titular, por edad y sexo del titular (sustituye a R2; decide U2).
- Perfiles de gasto del SEM por edad y sexo (sustituye a R3).
- Definición de antigüedad en las matrices (R4).
- Vigencia de las bases biométricas: la nota de la hoja de salidas dice que se usaron en el Informe 2022-2023 (probabilidades dinámicas 2023-2025, la última constante). Confirmar si aplican a la valuación 2025-2026.

## 7. Productos

- `config.yaml` — escenarios y malla.
- `src/` — un módulo por bloque, cada uno con su `.md`.
- `outputs/F0_inventario.md`.
- `outputs/tables/` — 15 CSV.
- `outputs/figures/` — 3 PNG.
- `NUMBERS.md`.
- `ANEXO_borrador.md`.
- `data/derived/` — parquet; la ENIGH no se versiona en crudo.
