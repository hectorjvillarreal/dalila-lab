---
id: 20261018_BDH_N13_seccion10-esquemas-financiamiento_build_v1.1
title: "Instrucciones de construcción — Sección 10 del Núcleo 13 (v1.1): correcciones de fondo, figuras y paginación"
type: build_instruction
build_type: retrofit
project: BDH
mission: IMSS — Núcleo 13 (Sostenibilidad financiera de la atención quirúrgica)
version: v1.1
supersedes: 20261018_BDH_N13_seccion10-esquemas-financiamiento_build_v1.0   # parcialmente: ver la sección 0
date: 2026-10-18
language: es
corpus_affected:
  - Missions/Funded/IMSS_Surgical/seccion10_esquemas_financiamiento/
  - Missions/Funded/IMSS_Surgical/e_1_imss_subsidiado/anexo_afiliacion_subsidiada/   # solo lectura, salvo el cálculo de 1.1 y la verificación de 1.3
  - Missions/Funded/IMSS_Surgical/e_2_imss_nuevoseguro/                              # solo lectura
triggered_by:
  - "Revisión de Beth y Cath de la sección 10 v1 (Claude Docs y N13_seccion10_esquemas_financiamiento_v1.docx, 18-10-2026)"
  - "Decisión de Héctor, 18-10-2026: adelante con la v1.1"
agents_involved: [Beth, Cath, Claude Code]
added_by: Beth
endorsed_by: []          # revisión pendiente: Cath (cifras) y Héctor (redacción)
protocol: PROTO-RAG-001
status: executed
executed: 2026-10-18   # Claude Code; seccion10_esquemas_financiamiento/ (N13_seccion10_…_v1.1.md/.docx, copia _con_seccion10_v1.1.docx fuera de git, REPORT_seccion10.md § v1.1); cifras nuevas en e_1…/src/seccion10_v11.py (claves s10v11_*); anexo v4 del experimento 2: 6.6 → 6.5. Verificaciones 5.1-5.11 cumplidas; quedan dos oraciones dictadas de más de 40 palabras y un hueco de 33-36 % por la Tabla 10.1 [REVISAR]. Doc: https://claude.ai/code/artifact/f9109443-800e-49d4-a182-99247635053e (v1.1)
executor: Claude Code (Dalila)
---

# Sección 10, v1.1 — correcciones

## 0. Alcance

**Esta instrucción modifica la v1.0.** Siguen vigentes:

- estructura, extensión y metas de legibilidad;
- expresiones prohibidas;
- trazabilidad de cifras;
- regla de no modificar el original de Juan Pablo.

**Solo se cambia lo que se indica aquí.** El resto del texto se queda igual. La v1 se conserva y la nueva versión se guarda como `N13_seccion10_esquemas_financiamiento_v1.1` (.md y .docx), junto con la copia del documento de Juan Pablo con la sección insertada (`…_con_seccion10_v1.1.docx`).

**Cifras nuevas: solo dos.** Son las de la sección 1.1 (comparación con la cuota fija) y la sección 1.5 (pago total del hogar con afiliación individual). Si alguna ya existe en las salidas del experimento 1, se usa esa. Todas van a `NUMBERS.md` del experimento 1 con su cálculo.

---

## 1. Correcciones de fondo en 10a

### 1.1 Comparación con la cuota fija: mismo diseño, misma parte

**Problema.** La serie "Cuota fija vigente (precio único)" de la Figura 10.2 y los 15,087 pesos (14.3 %) del ejemplo y de "Asequibilidad" son el diseño anterior: la cuota fija completa, incluida la parte federal (20.40 % + 14.83 % de la UMA), con el mismo subsidio. Por eso marca 0.0 en los percentiles 10 y 20. Con la cuota proporcional, el Gobierno Federal sigue pagando su parte. La comparación justa es contra la **parte patronal** de la cuota fija, con el **mismo subsidio**.

**Cálculo nuevo.** Para los percentiles 10, 20, 30, 50, 70 y 90 del ingreso laboral del titular informal, en 2026:

```
pago_cuota_fija_patronal(m) = (1 − s(m)) × 0.2040 × UMA_2026 × 365
```

- Mismo subsidio s(m), mismos umbrales y mismos días que la serie de la cuota proporcional de la Figura 10.2.
- Reportar el pago en pesos y en % del ingreso laboral del titular.
- Referencia de Beth para verificar: en la mediana, unos 8,700 pesos, cerca de 8.3 %.
- Si la serie de la cuota proporcional de la Figura 10.2 no usa 365 días, usar los mismos días que ella y reportarlo.

**Cambios en el texto:**

1. **Ejemplo ilustrativo de 10a.2.** "Con la cuota fija vigente pagaría 15,087 pesos, 14.3 % de su ingreso laboral" → la cifra nueva, con esta redacción: "Si se le cobrara la parte patronal de la cuota fija vigente, con el mismo subsidio, pagaría [x] pesos, [y] % de su ingreso laboral."
2. **"Asequibilidad" de 10a.4.** "Con la cuota fija vigente llegaría a 14.3 % en la mediana" → la cifra nueva. Agregar una oración: la cuota fija pesa más en los ingresos bajos porque es la misma cantidad para todos; la cuota proporcional pesa lo mismo en todos los niveles.
3. **Figura 10.2.** Sustituir la serie gris por la nueva y rotularla "Parte patronal de la cuota fija, con el mismo subsidio". La leyenda dice que en los dos casos el Gobierno Federal paga su aportación fija.
4. **Etiquetas.** La etiqueta "Cuota fija vigente" queda reservada para la Figura 10.4, donde sí es el status quo. Revisar que no aparezca con otro significado en ninguna parte.
5. La comparación del diseño anterior (cuota completa a cargo del hogar) no aparece en la sección 10; queda en el anexo.

### 1.2 Costo por persona constante: por qué el saldo casi no cambia en pesos

1. **Agregar una fila a la Tabla 10.1:**

   | Supuesto | Valor | Por qué ese valor | Qué pasa si cambia |
   |---|---|---|---|
   | Costo de atención por persona | Constante en términos reales | No se proyecta un aumento del costo médico por persona por encima de la inflación | Si crece 2 % real al año, el saldo de 2054 sube de 0.6 a 1.8 puntos del salario |

2. **En "Saldo para el SEM"**, sustituir "porque la proyección del IMSS supone que la masa salarial crece mucho" por: "porque el costo por persona se supone constante en términos reales mientras la masa salarial crece".
3. Confirmar en `NUMBERS.md` que el escenario base usa crecimiento real del costo por persona de 0 %. Si no es así, detenerse y reportarlo.

### 1.3 Derechohabientes: verificar antes de afirmar

La nota dice: "la diferencia está en conciliación y no cambia los resultados de esta sección".

1. Verificar en el código del experimento 1 qué conteo de derechohabientes entra al cálculo del costo por persona del SEM (gasto entre derechohabientes, o el que sea).
   - **Si el conteo no interviene** en ningún resultado de 10a, la frase se queda y en `REPORT_seccion10.md` se documenta dónde se verificó.
   - **Si interviene**, la frase se sustituye por: "El costo por persona del SEM usa [conteo y fuente]; con los 70.7 millones de este informe, el costo por persona sería [x] % mayor, y el saldo de 2030, de unos [y] mil millones de pesos." Se calculan [x] y [y] escalando el costo por persona, sin otra corrida. La marca **[REVISAR-JP: conciliación de derechohabientes]** se mantiene.
2. **Cobertura.** Sustituir "equivalen a 39.7 % de los 79.2 millones de derechohabientes que reporta el Informe del IMSS" por el porcentaje de la población nacional con IMSS en 2030, sin el esquema y con él, con el método de la ENIGH del experimento 1. Si `NUMBERS.md` no lo tiene, calcularlo con las salidas existentes:
   ```
   (derechohabientes ENIGH proyectados + cubiertos por el esquema) / población CONAPO
   ```
   Registrarlo y agregar una oración en la nota de derechohabientes sobre qué conteo se usó.

### 1.4 Efecto de la cuota proporcional sobre los formales

Después de la oración con 12 mil millones (2030) y 99 mil millones (2054), agregar:

> "Esta recaudación adicional también se obtendría si la cuota fija se actualizara con el salario en lugar de con la inflación, sin el esquema de afiliación. Por eso no se suma al saldo del esquema."

### 1.5 Afiliación individual: explicar quién paga

En 10a.5, la oración "Si la afiliación fuera individual … el saldo de 2030 bajaría a 0.2 puntos" se amplía así:

1. Decir quién paga en esa variante (cada adulto, cada persona del hogar o la definición del anexo) y por qué baja el saldo.
2. Agregar el pago total del hogar mediano en esa variante, en pesos y en % del ingreso del hogar, junto al de la afiliación por hogar (1.7 %).
   - Si la cifra existe en las salidas, usarla.
   - Si no, calcularla con el código y la configuración vigentes; es la segunda cifra nueva permitida.
3. Máximo tres oraciones.

### 1.6 Tres millones de cotizantes más

- "Su atención cuesta más de lo que aporta su cuota" → "Su atención cuesta más de lo que aportan su cuota y el Gobierno Federal".
- "trae 2.9 derechohabientes" → "con 2.9 derechohabientes por cotizante, incluido él". Verificar en `NUMBERS.md` si el 2.9 incluye al cotizante y ajustar la redacción.
- En el último punto de 10a.7, empezar con "Con el supuesto ilustrativo de 3 millones de cotizantes más…".

### 1.7 Incidencia legal

- "Un trabajador formal con el mismo ingreso paga lo mismo. Nadie paga distinto por el mismo ingreso según sea formal o informal." → "Por un trabajador formal con el mismo salario se paga la misma cuota. La cuota por el mismo ingreso no depende de si el trabajo es formal o informal."
- Revisar 10a y 10b en busca de otras frases con el trabajador o el patrón como quien "paga" una cuota a cargo del otro por ley. Corregirlas con "a cargo de … por ley" o "se paga por …".

### 1.8 Frase de apertura de 10a

Sustituir la frase marcada **[REVISAR-Beth]** por esta y retirar la marca:

> «Con los supuestos base, el esquema cubriría a unos 31 millones de personas en 2030, con un pago de 3.5 % del ingreso laboral para el hogar mediano. Lo que aportarían los hogares y el Gobierno Federal no alcanza para el costo de su atención: queda un saldo sin fuente de financiamiento asignada de unos 80 mil millones de pesos al año, equivalente a 1.3 puntos del salario en 2030 y 0.6 en 2054.»

Ajustar 10a.7 para que use las mismas cifras redondeadas: 31 millones y unos 80 mil millones.

### 1.9 Ingresos del SEM

- Se mantiene el Cuadro V.13 como denominador (decisión de Héctor).
- La marca **[REVISAR-JP]** del texto se sustituye por una nota al pie: "Con los ingresos del SEM de la Tabla 5 de este informe, el saldo de 2030 equivaldría a [x] % de los ingresos del SEM."
- Calcular [x] con la Tabla 5 de Juan Pablo y registrarlo en `tablas/conciliacion_seccion10.csv`.

### 1.10 Gasto federal para la población sin seguridad social

- Los 326 mil millones de pesos van con su fuente (documento, ramo o programas incluidos, año del presupuesto).
- Se mueven al párrafo "Saldo para el SEM", como contexto, después del saldo.
- Redacción: "Como contexto, el gasto federal en salud para la población sin seguridad social es de unos 326 mil millones de pesos en el presupuesto de 2026 ([fuente])." Sin "alcanza" ni "puede reasignarse".
- Si la fuente no está en `NUMBERS.md`, quitar la oración y reportarlo.

### 1.11 Primera oración de 10a.1

Sustituir por una versión directa, por ejemplo: "Según la ENIGH 2024, 59.2 millones de personas viven en 19.7 millones de hogares donde al menos un integrante trabaja sin seguridad social, y no tienen cobertura contributiva." Verificar la definición contra `NUMBERS.md`.

---

## 2. Correcciones de fondo en 10b

### 2.1 Personas de 65+ con IMSS: no es el método de la sección 4.2

- Sustituir "se calculan con CONAPO y la ENIGH 2024, el mismo método de la sección 4.2" por: "se estiman con la proporción de personas de cada edad y sexo que la ENIGH 2024 registra como afiliadas al IMSS, aplicada a la población de CONAPO. Es el mismo método de la sección 10a (véase la nota sobre derechohabientes)."
- Agregar la advertencia que se perdió: "Las cifras de 2040 y 2054 son una cota superior, porque esa proporción se mantiene en su nivel de 2024 aunque la formalidad sube."

### 2.2 Advertencia del escalón

- En "La cuña legal por nivel de salario", después de "en 2030 es de 4.4 puntos con la ley vigente y de 4.5 con ambos cambios", agregar: "Esto vale si el tramo de cesantía y vejez se determina por el salario en UMA; el criterio que aplica el IMSS en este caso está por confirmarse."
- Agregar también una oración sobre lo que muestra la Figura 10.8: "Con la cuota proporcional, la cuña sube a partir del salario promedio, porque la cuota deja de ser una cantidad fija."

### 2.3 Provisiones

- La definición de la Tabla 10.2 ("montos que el IMSS separa para gastos de operación") se verifica contra el texto del Informe (Cuadro V.19 y su explicación). Se sustituye por la definición del Informe, en palabras simples, con la página o el cuadro.
- Si el Informe no la define, quitar el paréntesis y poner: "con provisiones (véase el Informe del IMSS, Cuadro V.19)".

### 2.4 Cifras y lenguaje interno

1. "unos 2,631 mil millones de pesos" → "unos 2.6 billones de pesos (2.6 millones de millones)".
2. **Ritmo histórico.** Unificar con el anexo. Calcular la diferencia con los extremos sin redondear de la serie y usar la misma cifra, con un decimal, en la sección 10 y en el anexo del experimento 2. Si cambia el anexo, registrarlo en su `NUMBERS.md` y en el reporte.
3. **10b.7:** "en la base, cuidados más reserva…" → "con la formalización de la proyección del IMSS, cuidados más reserva…". Buscar "la base" como término interno en toda la sección y sustituirlo.
4. **Ejemplo ilustrativo de 10b.2.** El salario (627.87 pesos, diciembre de 2025) se expresa con la UMA de 2025 y la cuña es de 2026. Fechar bien: "ganaba 627.87 pesos al día en diciembre de 2025, 5.55 veces la UMA de ese año". En el cuadro de la cuña, el nivel de 5.55 UMA se rotula como "salario promedio". Si la cuña de 2026 usa otro nivel en UMA de 2026, reportarlo y usar el que corresponde.

---

## 3. Figuras

### 3.1 Figura 10.2

Según 1.1.3: serie nueva, etiqueta "Parte patronal de la cuota fija, con el mismo subsidio" y leyenda sobre la aportación federal.

### 3.2 Figura 10.6 (ingreso frente a déficit)

- **Anotaciones con la convención acordada:** "formalidad constante: el ingreso del año alcanza hasta 2032" y "mitad de esa formalización: el ingreso del año alcanza hasta 2034".
- **Leyenda:** agregar "Con reserva, el faltante de cada año lo paga la reserva hasta donde alcanza (Figura 10.7)."
- Revisar que las anotaciones no tapen líneas.

### 3.3 Figura 10.7 (reserva)

- Todas las líneas continuas; los escenarios se distinguen por color y marcador (cada 5 años).
- Mismos colores que en la Figura 10.6.
- La línea punteada queda reservada para el déficit de GMP en la 10.6.

### 3.4 Figura 10.8 (cuña legal)

- La anotación del escalón agrega: "lectura por UMA; criterio pendiente con el IMSS".
- Nota en la leyenda: "Los niveles de salario no están a escala."

### 3.5 Las demás

Las Figuras 10.1, 10.3, 10.4 y 10.5 no cambian. Solo se revisa que sus etiquetas sigan siendo coherentes con 1.1.4.

---

## 4. Paginación

1. En el .docx, marcar las tablas 10.1, 10.2 y 10.3 para que no se partan filas entre páginas y para que el encabezado se repita si una tabla cruza de página.
2. **Figuras:** en línea con el texto, con la leyenda pegada a la figura ("conservar con el siguiente"), y tamaño de 80 a 90 % del ancho de texto, para no dejar huecos grandes.
3. Renderizar el .docx a PDF y revisar todas las páginas como imagen. Reportar:
   - el número de páginas de 10a y de 10b;
   - los huecos de más de un tercio de página;
   - las tablas partidas.

   Meta: ninguna tabla partida y ningún hueco de más de un tercio de página, salvo al final de una subsección.

---

## 5. Verificaciones

| # | Verificación |
|---|---|
| 5.1 | Fuera de lo indicado, el texto de la v1 no cambia (diff limitado a las secciones 1 a 4). |
| 5.2 | Las dos cifras nuevas (1.1 y 1.5) están en `NUMBERS.md` con su cálculo. En la mediana, la cuota fija patronal con subsidio es mayor que la cuota proporcional y menor que 15,087 pesos. |
| 5.3 | La etiqueta "Cuota fija vigente" solo aparece donde significa el status quo. |
| 5.4 | La fila del costo por persona está en la Tabla 10.1, y el escenario base confirma un crecimiento real de 0 %. |
| 5.5 | La verificación del conteo de derechohabientes (1.3) está documentada con archivo y línea. |
| 5.6 | 0 apariciones de "el mismo método de la sección 4.2", "la base" como término interno, "[REVISAR-Beth]" y "2,631 mil millones". |
| 5.7 | La cifra del ritmo histórico es igual en la sección 10 y en el anexo. |
| 5.8 | Expresiones prohibidas (sección 6 de la v1.0): 0 apariciones. Se agregan "el trabajador paga" y "el patrón paga" referidos a cuotas que la ley pone a cargo del otro. |
| 5.9 | Extensión: 10a y 10b con 8 páginas o menos en el formato de Juan Pablo; texto corrido de 10,800 caracteres o menos; índice de Fernández Huerta reportado. |
| 5.10 | Paginación (sección 4): 0 tablas partidas; huecos reportados. |
| 5.11 | El original de Juan Pablo no cambió (hash). |

---

## 6. Reporte

Agregar a `REPORT_seccion10.md` una sección "v1.1" con:

1. Las cifras nuevas y su cálculo.
2. El resultado de la verificación de derechohabientes y el porcentaje de la población con IMSS.
3. La fuente de los 326 mil millones o su retiro.
4. La definición de provisiones encontrada.
5. La cifra unificada del ritmo histórico.
6. Las verificaciones de la sección 5.
7. El diff resumido.
8. Las decisiones propias marcadas como **[REVISAR]**.

Actualizar el documento de Claude Docs "N13 · Sección 10: Esquemas de financiamiento alternativos". El título termina en "(v1.1)" y la nota inicial dice, en tres líneas, qué cambió y qué marcas quedan. Hacer commit y archivar esta instrucción en `_crossrefs/_build_instructions/`.
