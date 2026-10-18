---
id: 20261018_BDH_N13_seccion10-esquemas-financiamiento_build_v1.0
title: "Instrucciones de construcción — Sección 10 del Núcleo 13: Esquemas de financiamiento alternativos (10a afiliación subsidiada; 10b seguro solidario de salud y cuidados)"
type: build_instruction
build_type: initial_scaffold     # verificar que el valor exista en la enumeración de PROTO-RAG-001; si no, usar el más cercano y reportarlo
project: BDH
mission: IMSS — Núcleo 13 (Sostenibilidad financiera de la atención quirúrgica)
version: v1.0
supersedes: null
date: 2026-10-18
language: es
corpus_affected:
  - Missions/Funded/IMSS_Surgical/   # documento del Núcleo 13 de Juan Pablo (localizar; sección 1.1). No se modifica el original.
  - Missions/Funded/IMSS_Surgical/e_1_imss_subsidiado/anexo_afiliacion_subsidiada/   # solo lectura
  - Missions/Funded/IMSS_Surgical/e_2_imss_nuevoseguro/                              # solo lectura
triggered_by:
  - "Decisión de Héctor, 18-10-2026: redactar una sección 10, «Esquemas de financiamiento alternativos», en el documento de Juan Pablo; 10a = experimento 1 y 10b = experimento 2; máximo ocho cuartillas cada una, lenguaje accesible, supuestos claros y gráficas"
  - "Aval de Beth y Cath a los resultados de modelo: experimento 1 (v1.2, borrador v3) y experimento 2 (v1.3, borrador v4)"
agents_involved: [Beth, Cath, Claude Code]
added_by: Beth
endorsed_by: []          # revisión pendiente: Cath (cifras y lectura fiscal) y Héctor (redacción)
protocol: PROTO-RAG-001
status: executed
executed: 2026-10-18   # Claude Code; Missions/Funded/IMSS_Surgical/seccion10_esquemas_financiamiento/ (REPORT_seccion10.md, .md, .docx de la sección, figuras, tablas). Opción (b) de Héctor: sección 10 al final, después de «9. Anexos». Verificaciones 8.1-8.11 cumplidas, con la frase obligatoria 1 (42 palabras) como excepción reportada. El .docx se generó con python-docx porque pandoc rompe listas y tablas con la plantilla de JP. Documento en Claude Docs: https://claude.ai/code/artifact/f9109443-800e-49d4-a182-99247635053e
executor: Claude Code (Dalila)
---

# Sección 10 del Núcleo 13: Esquemas de financiamiento alternativos

## 0. Propósito y alcance

Redactar la sección 10 del documento del Núcleo 13 que preparó Juan Pablo, con dos subsecciones:

- **10a. Afiliación subsidiada para trabajadores independientes y hogares de ingresos bajos y medios bajos** (experimento 1).
- **10b. De la aportación al Infonavit a un seguro solidario de salud y cuidados en la vejez** (experimento 2).

Los títulos son provisionales. Proponer, si hace falta, uno más corto y claro para cada subsección, y reportarlo.

**Es una traducción, no un experimento nuevo.** La sección 10 cuenta en lenguaje accesible lo que ya está en los anexos técnicos, sin cifras ni corridas nuevas.

- Fuente de 10a: experimento 1, v1.2 (borrador v3).
- Fuente de 10b: experimento 2, v1.3 (borrador v4).

Si una gráfica necesita una serie que no está guardada como tabla, se puede generar con el código existente y la configuración vigente. Nunca con supuestos nuevos.

**El original de Juan Pablo no se modifica.** Todo se entrega en archivos nuevos (sección 7).

**Los anexos técnicos siguen siendo el respaldo.** La sección 10 los cita como «Anexo X» para el detalle. Dónde van los anexos dentro del documento lo decide Héctor después; esta instrucción no los inserta.

---

## 1. Insumos

### 1.1 Documento de Juan Pablo

1. Buscar en `Missions/Funded/IMSS_Surgical/` y sus subcarpetas el documento más reciente del Núcleo 13 (.docx o .md) hecho por Juan Pablo.
2. Si hay varios candidatos, listarlos con fecha de modificación y autor (metadatos del .docx), elegir el más reciente y reportar la elección. Si no es claro, detenerse y reportar sin redactar.
3. **Leerlo completo antes de escribir** y registrar en `REPORT_seccion10.md`:
   - numeración de secciones y si ya existe una sección 10;
   - estilos de título, de cuadros y de figuras (numeración, leyenda, fuente al pie);
   - estilo de citas y de fuentes;
   - unidades (mdp, pesos de qué año, % del PIB o de la masa salarial);
   - separador decimal y de miles;
   - los términos que usa para las mismas cosas, en una tabla de términos (derechohabientes, cotizantes, SEM, GMP, déficit, prima, etc.).
4. **La sección 10 usa los términos de Juan Pablo.** Si un término de los anexos difiere, usar el suyo y anotar la equivalencia en la tabla. Si su término cambiaría el significado, conservar el de los anexos con una definición breve y marcarlo **[REVISAR-JP]**.

### 1.2 Experimento 1 (solo lectura)

`e_1_imss_subsidiado/anexo_afiliacion_subsidiada/`: `ANEXO_borrador_v3.md`, `NUMBERS.md`, `REPORT.md`, `outputs/tables/`.

### 1.3 Experimento 2 (solo lectura)

`e_2_imss_nuevoseguro/`: `ANEXO_experimento2_borrador_v4.md`, `NUMBERS.md`, `REPORT.md`, `tablas/`.

---

## 2. Coherencia con el documento de Juan Pablo

1. **Conciliación de cifras compartidas.** Identificar las cifras que aparecen en las dos partes: derechohabientes, cotizantes, ingresos y déficit del SEM y de GMP, población de 65+, salario promedio, UMA, salario mínimo. Guardarlas en `tablas/conciliacion_seccion10.csv` con el valor de Juan Pablo, el de los anexos, la fuente de cada uno y la diferencia.
2. **Derechohabientes (70.7 frente a 54.6 millones).** Es la discrepancia conocida y sigue abierta.
   - La sección 10 no cambia la cifra de Juan Pablo ni la adopta para los experimentos.
   - Donde la sección use derechohabientes, dice en una oración qué cifra usa y de dónde sale, y remite a una nota que explica la diferencia sin decir cuál es la correcta.
   - Marcar **[REVISAR-JP: conciliación de derechohabientes]**.
   - La integración final depende de esa conciliación.
3. **Cualquier otra diferencia mayor a 1 %** se reporta y se marca **[REVISAR-JP]**. No se corrige en ninguno de los dos lados.
4. **Lo que ya dice el documento.** Si sus secciones 1 a 9 ya explican algo que la sección 10 necesita (cómo se financia el SEM, qué es GMP, qué es la UMA), no repetirlo: remitir a esa sección («véase la sección N»). Así se ahorra espacio.

---

## 3. Extensión, lenguaje y forma

### 3.1 Extensión

- **Cada subsección (10a y 10b): máximo 8 páginas** en el formato del documento de Juan Pablo, con figuras, cuadros y notas.
- Para que quepan las figuras, el **texto corrido de cada subsección no pasa de 6 cuartillas**. Una cuartilla equivale a 1,800 caracteres con espacios (convención editorial; Héctor puede cambiarla). Es decir, 10,800 caracteres con espacios, con notas al pie y sin cuadros ni leyendas.
- **Introducción de la sección 10** (antes de 10a): máximo media cuartilla. No cuenta en las 8 páginas de cada subsección.
- Si algo no cabe, se queda en el anexo técnico y el texto remite a él. No se comprime el lenguaje para que quepa más.

### 3.2 Lenguaje humano

- Oraciones cortas: **promedio de 22 palabras o menos** y ninguna de más de 40. Voz activa. Un párrafo, una idea.
- **Ninguna fórmula ni símbolo en el texto** (nada de τ, ρ, μ, s(m), K1, K2, M2, M3). Los supuestos tienen nombre en palabras:

  | Símbolo del anexo | Nombre en la sección 10 |
  |---|---|
  | τ | proporción de hogares que se afilia |
  | ρ | proporción de las cuotas que efectivamente se cobra |
  | μ | sobrecosto de atención de quienes se afilian primero |
  | K2 | regla con reserva |
  | K1 | regla sin reserva |
  | Base | formalización de la proyección del IMSS |
  | M3 | mitad de esa formalización |
  | M2 | formalidad constante |
  | MH | ritmo histórico |
  | D2 | cuota proporcional al salario |

  Registrar la equivalencia en la tabla de términos.
- **Cada término técnico se define en palabras la primera vez que aparece**: UMA, SBC, cuota fija, GMP, cuña contributiva legal, valor presente, provisiones.
- **Un ejemplo con números en cada subsección**, con una persona o un hogar ilustrativo y valores de 2026 tomados de `NUMBERS.md`.
  - 10a: un hogar informal de ingreso bajo: cuánto pagaría al año, qué parte cubre el Gobierno Federal y qué recibe.
  - 10b: un trabajador de salario promedio: qué contribución legal desaparece, cuál se crea y a dónde va.
  - Rotular el ejemplo como ilustrativo.
- **Cifras para leer, no para auditar.** En el texto, montos en miles de millones de pesos de 2026 con cero decimales (por ejemplo, «unos 109 mil millones de pesos») y puntos del salario con un decimal. Las cifras exactas van en los cuadros y en el anexo. Documentar la regla de redondeo en `REPORT_seccion10.md`.
- **Indicador de legibilidad.** Calcular el índice de Fernández Huerta de cada subsección y reportarlo. Meta: 60 o más («normal» o más fácil). Si no se alcanza, simplificar oraciones, no quitar contenido.

### 3.3 Reglas de contenido que se mantienen de los anexos

1. **Incidencia legal únicamente** (Salanié). Se dice «tasa legal», «contribuciones a cargo del patrón por ley», «cuña contributiva legal». Están prohibidas las expresiones de la sección 6.
2. **Ejercicios de ITED.** Usan insumos del IMSS, pero no son proyecciones del IMSS, no sustituyen sus valuaciones y no son propuestas del IMSS ni del Gobierno. Se dice una vez en la introducción y una vez en cada subsección.
3. **Los resultados de 10a y 10b no se suman.** Solo la cuña combinada (columna c del experimento 2) aparece en 10b, y así se rotula.
4. **No hay juicios de sostenibilidad** («es sostenible», «se autofinancia», «cubre su costo»).
5. **Los supuestos ilustrativos se llaman así**, no estimaciones: adopción, cobro, sobrecosto, formalización.

---

## 4. Estructura

### 4.0 Introducción de la sección 10 (máximo media cuartilla)

- Por qué buscar esquemas alternativos: una o dos oraciones que conecten con el diagnóstico del documento; remitir a la sección que corresponda.
- Qué atiende cada subsección:
  - 10a: cómo ampliar la cobertura contributiva a quienes hoy no cotizan, con un pago que puedan sostener;
  - 10b: cómo financiar el gasto médico de los pensionados y los cuidados en la vejez con una contribución que ya existe.
- Rótulo de ITED, incidencia legal y «no se suman».

### 4.1 Plantilla común de 10a y 10b

Las dos subsecciones usan la misma estructura y los mismos encabezados.

| # | Apartado | Extensión orientativa | Contenido |
|---|---|---|---|
| 1 | El problema | ½ cuartilla | Qué hueco atiende, con una o dos cifras del documento o del Informe. |
| 2 | La idea | 1 cuartilla + figura del esquema | Cómo funciona, en palabras. Quién aporta qué, a dónde va el dinero y qué recibe cada quien. El ejemplo ilustrativo. |
| 3 | Supuestos | ½ cuartilla + cuadro | Cuadro de supuestos con cuatro columnas: supuesto, valor, por qué ese valor, qué pasa si cambia (remitir a la sensibilidad). |
| 4 | Resultados | 2 cuartillas + 2 o 3 figuras | Se abre con la frase obligatoria (4.2 y 4.3) y sigue con lo principal, en orden de importancia. |
| 5 | Qué tan robusto es | ½ a 1 cuartilla | Las sensibilidades que cambian la lectura, no todas. |
| 6 | Lo que el ejercicio no dice | ½ cuartilla | Limitaciones en una lista breve; las demás, en el anexo. |
| 7 | En resumen | 3 a 4 viñetas | Mensajes clave, cada uno con su cifra. Sin recomendaciones de política. |

### 4.2 Contenido específico de 10a (experimento 1)

**La idea:**

- La parte patronal de la cuota fija (20.40 % de la UMA por día) se convierte en una cuota proporcional al salario (3.467 %), igual para formales y para informales que se afilian.
- Los hogares de ingresos bajos y medios bajos reciben un subsidio que baja con el ingreso.
- El Gobierno Federal aporta como hoy.
- Nadie paga distinto por el mismo ingreso según sea formal o informal: es la regla de no arbitraje, dicha en palabras.

**Supuestos del cuadro:**

- proporción que se afilia: 50 %;
- proporción de cuotas que se cobra: 75 %;
- sobrecosto de atención de los nuevos afiliados: 10 %;
- 337 días cotizados;
- umbrales indexados;
- perfil de costos por edad.

Cada uno con su «por qué», tomado del anexo.

**Resultados, en este orden:**

1. Cuántas personas quedarían cubiertas y qué parte de la población estaría con el IMSS.
2. Cuánto pagaría un hogar como % de su ingreso, frente a su gasto de bolsillo en salud (asequibilidad).
3. El saldo del esquema para el SEM: ingresos determinados frente a cobrados, aportación federal, costo de atención y saldo, en miles de millones y en puntos del salario.
4. **El Bloque C frente al status quo.** Es la respuesta a la limitación de ingresos fijos del documento y va como resultado propio. Se rotula que la formalización de 3 millones de cotizantes a 2030 es un supuesto ilustrativo, no una estimación.
5. El efecto de indexación de los umbrales, **separado** del saldo.

**Frase de apertura de Resultados.** Proponer una frase de apertura equivalente a la de 10b: qué cubre el esquema, a qué costo para el SEM y para el Gobierno Federal, con los supuestos base. Marcarla **[REVISAR-Beth]**. Debe respetar las afirmaciones prohibidas del experimento 1, en particular no decir que «cubre su costo».

**Gasto no contributivo actual:** solo como contexto, sin decir que «alcanza» ni que «puede reasignarse».

### 4.3 Contenido específico de 10b (experimento 2)

**La idea:**

- Se elimina la aportación de 5 % al Infonavit.
- 2 % del salario financia un seguro nuevo, solidario: un fondo común, no una cuenta individual.
- La tasa legal sobre la nómina baja 3 puntos hasta 25 UMA.
- El seguro paga primero el déficit de gastos médicos de pensionados (GMP). Hasta 2034 guarda el excedente en una reserva. Desde 2035 destina a cuidados lo que sobra.
- El Infonavit conserva lo que ya tiene.

**Supuestos del cuadro:**

- inicio en 2027 y horizonte 2027-2054;
- déficit de GMP del Informe;
- tres escenarios de formalización con el mismo peso;
- rendimiento real de la reserva de 3 %;
- retiro fijo para cuidados desde 2035;
- gasto de GMP sin ajuste en los escenarios de menor formalización.

**Frase obligatoria de apertura de Resultados,** adaptada de la v1.3 a lenguaje de la sección y con las cifras de `NUMBERS.md`:

> «Con una reserva que se acumula hasta 2034, el 2 % alcanza para pagar el déficit de gastos médicos de pensionados en todo el periodo 2027-2054, tanto con la formalización que supone la proyección del IMSS como con la mitad de ella. Si la formalidad se queda como está hoy, alcanza hasta 2037.»

**Resultados, en este orden:**

1. La frase de apertura.
2. El papel de la reserva. Frase obligatoria: «La reserva no crea recursos: cambia cuándo y para qué se usan. En cada escenario, lo que se destina a cuidados más lo que queda en la reserva, menos lo que falta para GMP, vale lo mismo con reserva y sin ella.»
3. Cuánto queda para cuidados en el escenario base, por persona de 65+ y de 80+ con IMSS. Se rotula como recurso disponible, no como costo de cuidados.
4. La cuña legal por nivel de salario:
   - en 2026, la cuña es más alta en el salario mínimo;
   - en 2030, por el calendario de cesantía y vejez, ya no lo es;
   - el escalón justo arriba del salario mínimo, que ninguno de los dos experimentos modifica.

**Qué tan robusto es:**

- **Ritmo histórico:** «entre 2005 y 2025 la formalidad subió 6.6 puntos; la proyección supone 29 puntos en 29 años». Con ese ritmo y con reserva, alcanza hasta 2049.
- **Provisiones:** cómo mueven las fechas.
- **Masa salarial:** el libro de Finanzas y el Informe suponen trayectorias distintas; con la del Informe, la base sigue cubriendo todo el periodo.

Sin calificar el supuesto del IMSS.

**Lo que el ejercicio no dice:**

- incidencia y valoración;
- efectos en pensiones y en otros seguros;
- operación del Infonavit;
- factibilidad política.

---

## 5. Gráficas y cuadros

### 5.1 Cuántas y cuáles

**Por subsección:** de 3 a 4 figuras y de 1 a 2 cuadros, como máximo.

**10a**

| # | Figura o cuadro | Qué muestra |
|---|---|---|
| F10a.1 | Esquema | Diagrama de flujo: hogar informal, patrón (si lo hay), Gobierno Federal e IMSS; quién aporta qué y qué cubre el SEM. |
| F10a.2 | Asequibilidad | Pago anual como % del ingreso laboral por percentil (10, 20, 30, 50, 70, 90), con la cuota proporcional frente a la cuota fija vigente. Referencia horizontal: gasto de bolsillo en salud del hogar. |
| F10a.3 | Saldo para el SEM | Barras por año seleccionado (2026, 2030, 2040, 2054): ingresos cobrados, aportación federal y costo de atención, con el saldo marcado. Puntos del salario con el denominador común. |
| F10a.4 | Bloque C frente al status quo | 2030, 2040 y 2054, con la cuota proporcional y con la fija. |
| C10a.1 | Supuestos | Supuesto, valor, por qué, qué pasa si cambia. |

**10b**

| # | Figura o cuadro | Qué muestra |
|---|---|---|
| F10b.1 | Esquema | Del 5 % actual: 3 puntos que se dejan de cobrar y 2 puntos al nuevo seguro; dentro del seguro, primero GMP, luego reserva hasta 2034 y cuidados desde 2035. |
| F10b.2 | Ingreso frente a déficit de GMP | Líneas 2027-2054 para los tres escenarios. Ingreso en línea continua y déficit en punteada, mismo color por escenario. Marcar dónde el déficit rebasa el ingreso. |
| F10b.3 | Reserva | Saldo de la reserva 2027-2054 por escenario, con el agotamiento de M2 en 2038 señalado. |
| F10b.4 | Cuña legal por nivel de salario, 2030 | Del salario mínimo a 25 UMA: ley vigente, experimento 2 y experimento 2 con la cuota proporcional. El escalón en 1.01 SM, señalado. |
| C10b.1 | Supuestos | Supuesto, valor, por qué, qué pasa si cambia. |
| C10b.2 | Hasta qué año alcanza | Con reserva y sin ella, para los tres escenarios y el ritmo histórico, con y sin provisiones. Con las cifras del Cuadro X-2.3 de la v1.3. |

### 5.2 Reglas para todas las figuras

1. **Una idea por figura.** Título descriptivo en el estilo del documento. Debajo, una oración de «cómo leerla» en el texto o en la leyenda.
2. **Forma de los datos.** Pesos de 2026; ejes con unidades; etiquetas en español; separador decimal y de miles como en el documento de Juan Pablo. Ningún año después de 2054.
3. **Fuente al pie** en el formato del documento («Fuente: elaboración de ITED con base en …»).
4. **Colores por escenario**, iguales en todas las figuras de 10b: base, mitad, constante e histórico. Legibles en escala de grises (distinguir también por tipo de línea o marcador). En 10a, un color por componente y los mismos en F10a.3 y F10a.4.
5. **Que se lean en el documento.** Fuente de las etiquetas de 9 pt o más al tamaño de inserción. Nada de títulos dentro de la gráfica si el documento los pone en la leyenda.
6. **Archivos:** PNG a 300 ppp para el .docx, SVG para edición y el CSV de datos de cada figura, en `seccion10/figuras/`. Los esquemas (F10a.1 y F10b.1) pueden hacerse con matplotlib o Graphviz; deben ser sobrios y caber en media página.
7. **Revisión visual.** Renderizar cada figura y cada página del .docx como imagen y revisarlas: texto cortado, solapamientos, legibilidad. Reportar las correcciones.

---

## 6. Expresiones prohibidas

Buscar en el texto, las leyendas y las notas; deben aparecer 0 veces.

| Grupo | Expresiones |
|---|---|
| Incidencia | «costo para el patrón», «costo laboral», «costo de la formalidad», «abarata», «más barato contratar», «subsidio cruzado entre patrones», «quién paga en realidad», «lo pagan los trabajadores» |
| Sostenibilidad | «sostenible», «insostenible», «se autofinancia», «cubre su costo» |
| Autoría | «proyección del IMSS» aplicado a resultados de ITED (sí se puede decir «la proyección del IMSS supone…» sobre el supuesto de formalización); «propuesta del IMSS», «propuesta del Gobierno» |
| Causalidad | cualquier afirmación causal sobre la formalidad («aumentará la formalidad», «incentiva la formalización») |
| Supuestos | llamar estimación a un supuesto ilustrativo |
| Gasto no contributivo | «alcanza», «puede reasignarse» |
| Interno | rutas de Dalila, nombres de archivos de trabajo, «Claude», «agente», Beth, Cath o Debb, «v1.3», «K1», «K2», «M2», «M3», «D2» y demás claves internas |

---

## 7. Salidas

En una carpeta nueva, `Missions/Funded/IMSS_Surgical/seccion10_esquemas_financiamiento/`:

1. `N13_seccion10_esquemas_financiamiento_v1.md`: el texto fuente.
2. `N13_seccion10_esquemas_financiamiento_v1.docx`: con los estilos del documento de Juan Pablo. Usar su .docx como documento de referencia de estilos (por ejemplo, `pandoc --reference-doc`) y revisar que títulos, leyendas y numeración coincidan.
3. `<nombre del documento de Juan Pablo>_con_seccion10_v1.docx`: copia del documento con la sección 10 insertada en su lugar.
   - Si el documento tiene índice o referencias cruzadas, actualizarlos.
   - Si ya existía una sección 10 o la numeración no lo permite, no renumerar el documento: insertar como «10» provisional y reportarlo.
4. `seccion10/figuras/`: PNG, SVG y CSV de cada figura (5.2.6).
5. `tablas/conciliacion_seccion10.csv` (sección 2) y `tablas/seccion10_cifras.csv`. Esta última tiene una fila por cada cifra del texto, los cuadros y las figuras, con:
   - experimento;
   - identificador en `NUMBERS.md`;
   - valor exacto;
   - valor redondeado que aparece;
   - ubicación.
6. `REPORT_seccion10.md` (sección 9).

---

## 8. Verificaciones

| # | Verificación |
|---|---|
| 8.1 | Extensión: 10a y 10b con 8 páginas o menos en el formato del documento; texto corrido de 10,800 caracteres o menos cada una; introducción de 900 caracteres o menos. Reportar las cifras. |
| 8.2 | Toda cifra de la sección está en `tablas/seccion10_cifras.csv` y en el `NUMBERS.md` de su experimento; redondeos conforme a la regla de 3.2. 0 cifras sin respaldo. |
| 8.3 | Las cifras del texto, de los cuadros y de las figuras coinciden entre sí y con los anexos (v3 del experimento 1, v4 del experimento 2). |
| 8.4 | 0 apariciones de las expresiones de la sección 6. |
| 8.5 | 0 años después de 2054 en texto, figuras y datos de figuras. |
| 8.6 | Promedio de palabras por oración de 22 o menos y ninguna de más de 40; índice de Fernández Huerta reportado para cada subsección (meta: 60 o más). |
| 8.7 | 10a y 10b tienen los siete apartados de 4.1, con los mismos encabezados. |
| 8.8 | Las dos frases obligatorias de 10b aparecen y sus cifras coinciden con el Cuadro X-2.3 de la v1.3. |
| 8.9 | Cada término técnico está definido en su primera aparición (lista en el reporte). |
| 8.10 | Revisión visual de figuras y páginas hecha (5.2.7); 0 textos cortados o solapados. |
| 8.11 | El original de Juan Pablo no cambió (hash antes y después). |

---

## 9. Reporte

`REPORT_seccion10.md` con:

1. Documento de Juan Pablo elegido y por qué (1.1).
2. Tabla de términos y equivalencias (1.1 y 3.2).
3. Conciliación de cifras y marcas **[REVISAR-JP]** (sección 2).
4. Títulos propuestos para 10a y 10b, si cambian.
5. Frase de apertura propuesta para 10a, marcada **[REVISAR-Beth]**.
6. Regla de redondeo.
7. Extensión e indicadores de legibilidad.
8. Lo que no cupo y se dejó en el anexo.
9. Verificaciones de la sección 8.
10. Decisiones propias marcadas como **[REVISAR]**.

Crear un documento en Claude Docs titulado «N13 · Sección 10: Esquemas de financiamiento alternativos (v1)» con:

- una nota inicial de cinco líneas como máximo: qué es, marcas de revisión y extensión;
- el texto completo de 10a y 10b con figuras y cuadros;
- las marcas [REVISAR].

Hacer commit y archivar esta instrucción en `_crossrefs/_build_instructions/`.
