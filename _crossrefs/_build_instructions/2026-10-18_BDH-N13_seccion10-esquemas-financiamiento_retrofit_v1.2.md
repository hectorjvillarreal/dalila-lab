---
id: 20261018_BDH_N13_seccion10-esquemas-financiamiento_build_v1.2
title: "Instrucciones de construcción — Sección 10 del Núcleo 13 (v1.2): sensibilidad a derechohabientes, composición del déficit de GMP y aportación federal con afiliación individual"
type: build_instruction
build_type: retrofit
project: BDH
mission: IMSS — Núcleo 13 (Sostenibilidad financiera de la atención quirúrgica)
version: v1.2
supersedes: 20261018_BDH_N13_seccion10-esquemas-financiamiento_build_v1.1   # parcialmente: ver la sección 0
date: 2026-10-18
language: es
corpus_affected:
  - Missions/Funded/IMSS_Surgical/seccion10_esquemas_financiamiento/
  - Missions/Funded/IMSS_Surgical/e_1_imss_subsidiado/anexo_afiliacion_subsidiada/   # solo lectura, salvo el registro de las cifras de 1.1 y 3
  - Missions/Funded/IMSS_Surgical/e_2_imss_nuevoseguro/                              # solo lectura, salvo el registro de las cifras de 2
triggered_by:
  - "Revisión de Beth y Cath de la sección 10 v1.1 (18-10-2026)"
  - "Decisión de Héctor, 18-10-2026: hacer la v1.2"
agents_involved: [Beth, Cath, Claude Code]
added_by: Beth
endorsed_by: []          # revisión pendiente: Cath (cifras) y Héctor (redacción)
protocol: PROTO-RAG-001
status: executed
executed: 2026-10-18   # Claude Code; seccion10_esquemas_financiamiento/ (N13_seccion10_…_v1.2.md/.docx, copia _con_seccion10_v1.2.docx fuera de git, REPORT_seccion10.md § v1.2); cifras en e_1…/src/seccion10_v11.py (función v12, claves s10v12_*) y semillas GMP_V19_componentes / GMP_V19_vs_V24 en e_2…/NUMBERS.md. Verificaciones 5.1-5.8 cumplidas; huecos de 46 % (Tabla 10.2) y 33 % (Tabla 10.1) en la copia de JP, reportados [REVISAR]. Doc: https://claude.ai/code/artifact/f9109443-800e-49d4-a182-99247635053e (v1.2)
executor: Claude Code (Dalila)
---

# Sección 10, v1.2 — tres correcciones de fondo y tres de forma

## 0. Alcance

**Esta instrucción modifica la v1.1.** Todo lo demás sigue vigente: estructura, extensión, legibilidad, expresiones prohibidas, trazabilidad y no modificar el original de Juan Pablo.

- Solo se cambia lo que se indica aquí.
- La v1.1 se conserva. La nueva versión se guarda como `N13_seccion10_esquemas_financiamiento_v1.2` (.md y .docx), junto con la copia del documento de Juan Pablo con la sección insertada (`…_con_seccion10_v1.2.docx`).
- **No hay corridas nuevas.** Las cifras nuevas salen de escalar el costo por persona, como en la v1.1 (sección 1), de la transcripción del Cuadro V.19 (sección 2) y de las salidas existentes de la afiliación individual (sección 3). Cada una va al `NUMBERS.md` de su experimento con su cálculo.

---

## 1. 10a: el conteo de derechohabientes como sensibilidad principal

En la v1.1 se verificó que el costo por persona del SEM usa los 79.2 millones de derechohabientes del Informe, y que con los 70.7 millones de este informe el saldo de 2030 sube a unos 105 mil millones de pesos. Eso no es una nota de conciliación: cambia el tamaño del resultado principal de 10a.

### 1.1 Cifras

Con el mismo método de la v1.1 (escalar el costo por persona por la razón de conteos, sin otra corrida), calcular el saldo de 2030 y de 2054, en miles de millones de pesos y en puntos del salario, con tres conteos:

| Conteo | Fuente | Factor sobre el costo por persona |
|---|---|---|
| 79.2 millones (actual) | Informe del IMSS | 1.000 |
| 70.7 millones | este informe, sección 4.2 | 79.2 / 70.7 |
| 54.6 millones | ENIGH, variable de afiliación | 79.2 / 54.6 |

Usar los conteos sin redondear de `NUMBERS.md`. Referencias de Cath para verificar (2030, aproximadas):

- con 70.7 millones, saldo de unos 105 mil millones (ya calculado en la v1.1);
- con 54.6 millones, el costo sube cerca de 45 % y el saldo ronda 170 mil millones.

### 1.2 Texto

1. **Nueva viñeta en 10a.5 "Qué tan robusto es"**, la primera de la lista, y cambiar "Tres supuestos" por "Cuatro supuestos". Redacción base (ajustar las cifras):

   > «**Conteo de derechohabientes.** El costo por persona del SEM se obtiene dividiendo su gasto entre los derechohabientes. Con los 79.2 millones del Informe del IMSS, el saldo de 2030 es de unos 81 mil millones de pesos. Con los 70.7 millones de este informe sería de unos [x] mil millones, y con los 54.6 millones que registra la ENIGH, de unos [y] mil millones. El conteo del Informe probablemente sobrestima a los derechohabientes y el de la ENIGH probablemente los subestima; el saldo verdadero está dentro de ese rango.»

   La segunda oración de la cita es lectura de Cath, sustentada en la nota del conteo máximo (112.4 % de la población nacional de 65+ con el conteo del Informe) y en que la ENIGH registra lo que declaran los hogares. Marcarla **[REVISAR-Cath]** solo en `REPORT_seccion10.md`, no en el texto.

2. **Nota sobre derechohabientes.** Se acorta para que no repita la viñeta. Queda así:
   - qué conteo usa cada cálculo: costo por persona con el Informe y proporción de la población con IMSS con la ENIGH;
   - que la diferencia está en conciliación con este informe;
   - la remisión a 10a.5;
   - la marca **[REVISAR-JP: conciliación de derechohabientes]**, que se mantiene.
3. **Resumen (10a.7).** En el punto del saldo, agregar al final: «; depende del conteo de derechohabientes (sección 10a.5)».

---

## 2. 10b: qué incluye el déficit de GMP

Según las notas 3 y 4 del Cuadro V.19 del Informe:

- El gasto de GMP incluye **gastos de administración**. Se integran con la parte asignada a GMP de rubros que incluyen «servicios de personal y pasivos laborales del IMSS en su carácter de patrón por jubilaciones y pensiones».
- Las **provisiones** son «provisiones para la operación».

### 2.1 Cifras (transcribir del Cuadro V.19)

Registrar en el `NUMBERS.md` del experimento 2, en millones de pesos de 2026:

- gastos de administración en 2026 y en valor presente;
- provisiones en 2026 y en valor presente;
- gasto total en 2026 y en valor presente;
- déficit en valor presente.

Referencias para verificar:

| Concepto | 2026 | Valor presente |
|---|---|---|
| Administración | 43,581 | 1,009,572 |
| Provisiones | 123 | 151,550 |
| Gasto total | 157,897 | 5,388,234 |
| Déficit | — | −2,637,347 |

**Reportar en `REPORT_seccion10.md` las diferencias entre los Cuadros V.19 y V.24** en los años ancla. Por ejemplo, el déficit de 2036 es −135,137 en el V.19 y −134,117 en el V.24. No cambiar la fuente del modelo, que sigue siendo el V.24.

### 2.2 Texto

1. **Tabla 10.2, fila «Déficit de GMP», columna Valor.** Sustituir el paréntesis por: «El del Informe del IMSS (Cuadro V.24). Incluye la atención médica, los gastos de administración —entre ellos la parte que le corresponde de las pensiones de los trabajadores del IMSS— y las provisiones para la operación.»
2. **Párrafo nuevo en 10b.1 «El problema»**, después de la oración del valor presente:

   > «Ese déficit no es solo atención médica. Según el Informe, los gastos de administración —que incluyen la parte que corresponde a GMP de las pensiones de los trabajadores del IMSS— equivalen a unos [z] billones de pesos en valor presente, y las provisiones para la operación a unos [w] mil millones.»

   Redondear con la regla de la sección.
3. **Viñeta nueva en 10b.6 «Lo que el ejercicio no dice»:** «No separa la atención médica de los gastos de administración ni de las pensiones de los trabajadores del IMSS: el nuevo seguro paga el déficit de GMP completo, como lo reporta el Informe.»
4. **Una oración en 10b.5 «Qué tan robusto es»**, en la viñeta de provisiones o en una nueva:

   > «Usar el déficit completo, con administración y provisiones, es el supuesto más exigente para el nuevo seguro: si pagara solo la atención médica, alcanzaría por más tiempo.»

   No cuantificar: no hay una corrida sin gastos de administración, y no se hace en esta versión.

---

## 3. 10a: de dónde viene la mejora con afiliación individual

1. Tomar de las salidas existentes de la variante de afiliación individual del experimento 1 la **aportación federal de 2030** (aportación fija más subsidio), en miles de millones de pesos.
   - Si existen variantes con distinto número de beneficiarios por titular, reportar la que corresponde a cada extremo del rango de 0.2 a 0.4 puntos.
   - Si la cifra no existe en las salidas, calcularla con el código y la configuración vigentes de esa variante, sin cambiar supuestos, y reportarlo.
2. **En el párrafo de afiliación individual de 10a.5**, sustituir la oración que empieza «Como el pago se calcula sobre todo el ingreso del hogar…» por:

   > «El saldo de 2030 bajaría a entre 0.2 y 0.4 puntos del salario, según cuántos beneficiarios por titular se supongan. La mejora viene sobre todo de una mayor aportación federal: unos [a] mil millones de pesos en 2030, frente a unos 74 mil millones con la afiliación por hogar.»

   Si los datos muestran que la mejora no viene sobre todo de la aportación federal, decir de qué viene, con la cifra, y marcarlo **[REVISAR-Cath]** en el reporte.

---

## 4. Forma

1. **Gasto federal en salud para la población sin seguridad social.** La oración de los 326 mil millones de pesos se mueve al final del párrafo «Saldo para el SEM», después de la oración que termina en «(Figura 10.3)».
2. **Figura 10.3.** Va inmediatamente después del párrafo «Saldo para el SEM» y su nota al pie, antes de «Más formalidad frente a lo que hay hoy». La Figura 10.4 queda después de ese párrafo.
3. **Cifra del saldo.** Usar «unos 80 mil millones de pesos al año» solo cuando se hable del periodo y «unos 81 mil millones en 2030» cuando se hable de 2030:
   - la frase de apertura de 10a.4 dice «al año» y queda igual;
   - el párrafo «Saldo para el SEM» dice «en 2030»;
   - revisar el resto de la sección con la misma regla.

---

## 5. Verificaciones

| # | Verificación |
|---|---|
| 5.1 | Fuera de lo indicado, el texto de la v1.1 no cambia (diff limitado a las secciones 1 a 4). |
| 5.2 | Saldo con 70.7 millones igual al de la v1.1; con 54.6 millones, el saldo de 2030 es mayor que con 70.7. Cálculo registrado. |
| 5.3 | Las cifras del Cuadro V.19 coinciden con el Informe (transcripción verificada contra la página); diferencias V.19 contra V.24 reportadas. |
| 5.4 | Aportación federal con afiliación individual registrada con su fuente (salida existente o cálculo con la configuración vigente). |
| 5.5 | La Figura 10.3 aparece después del párrafo que la cita por primera vez; la Figura 10.4, después de la suya. |
| 5.6 | Expresiones prohibidas: 0 apariciones. Se revisa en especial que el párrafo nuevo de 10b.1 no diga ni sugiera que el seguro «paga pensiones» como propósito. Es una descripción de lo que contiene el déficit. |
| 5.7 | Extensión: 10a y 10b con 8 páginas o menos y texto corrido de 10,800 caracteres o menos cada una; índice de Fernández Huerta reportado; 0 tablas partidas. |
| 5.8 | El original de Juan Pablo no cambió (hash). |

---

## 6. Reporte

Agregar a `REPORT_seccion10.md` una sección «v1.2» con:

1. Las cifras nuevas y su cálculo (secciones 1, 2 y 3).
2. Las diferencias entre los Cuadros V.19 y V.24.
3. Las marcas [REVISAR-Cath].
4. Las verificaciones de la sección 5.
5. El diff resumido.

Actualizar el documento de Claude Docs. El título termina en «(v1.2)», y la nota inicial dice en tres líneas qué cambió y que la única marca en el texto es la de conciliación de derechohabientes. Hacer commit y archivar esta instrucción en `_crossrefs/_build_instructions/`.
