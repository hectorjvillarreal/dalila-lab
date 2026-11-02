---
id: 20261101_BDH_N13_evaluacion-informes_build_v1.0
title: "Instrucciones de construcción — Evaluación del Informe de Resultados y del Informe de Recomendaciones del Núcleo 13"
type: build_instruction
build_type: initial_scaffold     # verificar que el valor exista en la enumeración de PROTO-RAG-001; si no, usar el más cercano y reportarlo
project: BDH
mission: IMSS — Núcleo 13 (Sostenibilidad financiera de la atención quirúrgica)
version: v1.0
supersedes: null
date: 2026-11-01
language: es
corpus_affected:
  - "<CARPETA>"   # carpeta que indica Héctor, con los dos .docx; solo lectura
  - Missions/Funded/IMSS_Surgical/evaluacion_informes_N13/   # salidas
triggered_by:
  - "Petición de Héctor, 01-11-2026: revisar la última versión del Informe de Resultados y del Informe de Recomendaciones y evaluar su nivel"
  - "Revisiones previas de Beth y Cath: Informe de Resultados (28-10-2026) e Informe de Recomendaciones (29-10-2026)"
agents_involved: [Beth, Cath, Claude Code]
added_by: Beth
endorsed_by: []          # revisión pendiente: Cath (cifras y lectura fiscal)
protocol: PROTO-RAG-001
status: pending_execution
executor: Claude Code (Dalila)
---

# Evaluación de los informes del Núcleo 13

## 0. Propósito y alcance

Evaluar el nivel de dos documentos Word del Núcleo 13, en su última versión:

1. **Informe de Resultados** («Sostenibilidad Financiera de la Atención Quirúrgica en el IMSS»).
2. **Informe de Recomendaciones.**

La pregunta que hay que contestar es: **¿qué tan cerca está cada documento de poder entregarse a la Comisión y a las áreas del IMSS, y qué falta para llegar?**

**Es una evaluación, no una corrección.**

- No se reescribe el texto. Se diagnostica, se cita la evidencia y se propone qué hacer.
- **Los originales no se modifican.** Se registra su hash antes y después.
- Todo se escribe en español.

**Carpeta de insumos:** `<CARPETA>` (Héctor la indica). Si no se indica, buscar en `Missions/Funded/IMSS_Surgical/` la carpeta más reciente con exactamente dos archivos .docx cuyos nombres correspondan a los dos informes. Reportar la elección; si hay duda, detenerse y preguntar.

---

## 1. Lectura

1. **Leer los dos documentos completos**, con sus cambios controlados y sus comentarios:
   - texto con los cambios aceptados: `pandoc --track-changes=accept`;
   - texto con los cambios visibles: `pandoc --track-changes=all`, para saber quién cambió qué;
   - comentarios con autor, fecha y texto, extraídos de `word/comments.xml`; guardarlos en `tablas/comentarios.csv` con el párrafo al que se refieren.
2. **Renderizar cada documento a PDF** con LibreOffice y revisar todas las páginas como imagen: figuras, tablas, numeración, saltos, páginas en blanco y tablas vacías.
3. **Extraer y revisar cada figura** (`word/media/`): legibilidad, etiquetas, unidades, fuente al pie y concordancia con el texto que la cita.
4. **Insumos de contraste, si están disponibles en Dalila** (no son obligatorios; reportar cuáles se usaron):
   - el Informe al Ejecutivo Federal y al Congreso de la Unión 2025-2026 del IMSS (Cuadros V.13, V.19, V.24, A.3 y A.4);
   - las salidas tabulares del cuaderno del Núcleo 13 (`reporte_final_*`), si están en la misma estructura de carpetas;
   - los anexos técnicos de ITED de los experimentos 1 y 2 (`e_1_imss_subsidiado/`, `e_2_imss_nuevoseguro/`).

---

## 2. Rúbrica

Evaluar cada documento en las dimensiones siguientes, con una escala de cuatro niveles:

| Nivel | Significado |
|---|---|
| 4 | Listo: solo detalles de forma |
| 3 | Cambios menores: no alteran cifras ni mensajes |
| 2 | Cambios mayores: hay cifras, métodos o mensajes que corregir |
| 1 | No apto: hay problemas que invalidan un resultado central o una recomendación |

Cada calificación va con **una a tres evidencias citadas textualmente**, con sección y página aproximada.

| # | Dimensión | Qué se revisa | Aplica a |
|---|---|---|---|
| D1 | Coherencia interna de cifras | Que la misma magnitud tenga el mismo valor en todo el documento; que las tablas sumen; que porcentajes y tasas de crecimiento se puedan recalcular con las cifras del propio documento | Ambos |
| D2 | Coherencia entre documentos | Que las cifras, definiciones, horizontes, escenarios y métodos del Informe de Recomendaciones coincidan con los del Informe de Resultados | Recomendaciones |
| D3 | Solidez metodológica y honestidad de límites | Que los supuestos estén explícitos; que los resultados no dependan de supuestos no declarados; que los límites se digan donde importan y no solo en la sección de limitaciones | Resultados |
| D4 | Hilo argumental | Pregunta → método → hallazgos → discusión → conclusiones → recomendaciones. Que cada conclusión salga de un hallazgo y cada recomendación de una conclusión; que nada se afirme más fuerte de lo que el análisis sostiene | Ambos |
| D5 | Fuentes y referencias | Que cada dato tenga fuente; que cada referencia de la lista se cite en el texto y viceversa; que cada referencia exista y diga lo que el texto le atribuye (sección 4) | Ambos |
| D6 | Completitud editorial | Marcadores sin llenar («[año]», «Completar», «por confirmar», notas para el equipo); párrafos o secciones duplicadas; numeración de secciones, tablas y figuras; referencias cruzadas; tablas vacías; títulos y fuentes de figuras | Ambos |
| D7 | Lenguaje | Claridad para un lector institucional no técnico; un registro consistente; definición de siglas y términos; reglas de la sección 5 | Ambos |
| D8 | Calidad de las recomendaciones | Las siete dimensiones de la Comisión completas (actor, acción, destinatario, temporalidad, frecuencia, resultado, justificación); actores correctos; fechas posibles; instrumento normativo identificable; viabilidad con argumentos y no solo con calificativos | Recomendaciones |
| D9 | Requisitos de la Comisión | Estructura y apartados que pide la Comisión (inferirlos de los dos documentos y de cualquier plantilla en la carpeta; reportar si no se encontró la plantilla) | Ambos |

**Veredicto global por documento.** El nivel global es el **mínimo** de D1, D2, D3 y D4, ajustado a lo más un nivel hacia arriba si el resto de las dimensiones es 4. Explicar en dos o tres oraciones.

---

## 3. Problemas ya identificados: verificar su estado

Las revisiones previas encontraron los problemas siguientes. Para cada uno, determinar si sigue **pendiente**, quedó **resuelto** o está **parcialmente resuelto**, con la evidencia de la versión actual. **No dar ninguno por resuelto sin comprobarlo en el texto.** No limitarse a esta lista: buscar problemas nuevos con la rúbrica.

### 3.1 Informe de Resultados

| ID | Problema | Dónde estaba |
|---|---|---|
| R1 | Dos conteos de derechohabientes: 54.7 millones (sección 4.2, Tabla 3, sección 6) y 70.69 millones (Anexo I, Tabla I.1, Tabla J.2 y tasas de utilización) | 4.2, 5, 6, Anexos I y J |
| R2 | En la Tabla 2, la columna «Total» no es la suma de los procedimientos (por ejemplo, 50-59 años: los componentes suman 69.1 y la tabla dice 91.4); el texto dice «89.8» de promedio y la tabla, 69.4 | 5.2 |
| R3 | La brecha Δ(t) proyectada depende del supuesto de gasto como proporción fija (63.55 %) de los ingresos totales del IMSS; con gasto ligado a la demanda la brecha es positiva todo el periodo. Revisar qué trayectoria se presenta como principal y si el resumen y las conclusiones la siguen | 4.3.3, 5.6, resumen, conclusiones |
| R4 | Déficit de GMP en 6b aproximado con el costo de todos los derechohabientes de 60 años o más, en lugar del Cuadro V.24 del Informe del IMSS. La aproximación (unos 89 mil millones en 2027) supera el déficit institucional total (unos 74 mil millones), aunque este incluye administración y provisiones | 6b |
| R5 | En 6b.5, la frase según la cual con administración y provisiones «el déficit sería mayor y el seguro alcanzaría por menos tiempo». Frente al dato institucional, la dirección es la contraria | 6b.5 |
| R6 | Definición del gasto corriente en salud de 545,271 millones que se divide entre los derechohabientes para el costo por persona: qué incluye (administración, pasivos laborales, Riesgos de Trabajo) y por qué se atribuye completo al SEM | 6, «Costo e ingreso en las simulaciones» |
| R7 | Supuestos distintos de crecimiento del gasto: proporción fija de ingresos en la sección 5 y crecimiento con el salario real en la sección 6. ¿Está declarado? | 4.3.3, 6 |
| R8 | Referencias cruzadas a la «sección 8» para las limitaciones; la 8 es Referencias | 6, 6a |
| R9 | Dos secciones numeradas «7» (Discusión y Conclusiones); dos versiones de conclusiones | 7 |
| R10 | Párrafos duplicados | 5.5, 5.6, 7.2.2 |
| R11 | Marcadores sin llenar: «[año]», «[año exacto por confirmar…]», «Completar», «(Poner todos los títulos…)», tablas vacías al final | Varias |
| R12 | Cifras que no coinciden entre secciones: 89 % frente a 90 %; 11 % frente a 10 %; «crece 12.5 %» frente a 70.69 → 78.36 millones (10.8 %) | 2.4, 2.5, 5.4, 7 |
| R13 | Año 2055: el Anexo M explica que los nuevos cotizantes de la proyección del IMSS caen a la mitad en 2055; las cifras de ese año (brecha, Tabla 6.4) están afectadas. ¿Se advierte? | 5, 6c, Anexo M |
| R14 | Referencias bibliográficas sin verificar. Por ejemplo, Rechel et al. aparece como 2009 en la lista y como 2013 en el texto; hay otras sin comprobar | Referencias |
| R15 | Datos internos sin citar: Diego, Finanzas, presentación de la Coordinación de Asesores, 27 % de subregistro | 2, 3, 7 |
| R16 | Lista de autores (comentario de Mónica Montano) | Portada |

### 3.2 Informe de Recomendaciones

| ID | Problema | Dónde estaba |
|---|---|---|
| C1 | Horizonte 2024-2040 (Resultados: 2025-2055) | 2.2, 2.3 |
| C2 | «Distintos supuestos de inflación médica» (Resultados: inflación médica real de cero en todos los escenarios) | 2.2 |
| C3 | Δ(t) = CT(t) − F(t) (Resultados: Δ(t) = G(t) − F(t)) | 2.3 |
| C4 | «Análisis de sensibilidad univariado y multivariado (tornado)», que Resultados dice que no se hizo | 2.3 |
| C5 | Número de escenarios distinto entre documentos | 2.3 |
| C6 | Recomendación 1: «el modelo opera en R y Excel 365» (son cuadernos de Python) | 5.1 |
| C7 | Recomendación 1: piloto en el presupuesto 2027, que ya existe | 3.1 |
| C8 | Recomendación 1: alcance excesivo (volver «metodología oficial» del presupuesto del SEM un modelo de cuatro procedimientos que suman 0.3 % del gasto); afirmación no sustentada sobre la «extrapolación lineal histórica» de Finanzas; citas a Reddy et al. (2015) y a los «Informes Actuariales» por verificar | 3.1, 5.1 |
| C9 | Sección 4 («dos niveles») y 6.1 («ambas recomendaciones») escritas para dos recomendaciones; faltan actores de las recomendaciones 3 a 6 | 4, 6.1 |
| C10 | Cronograma con fechas pasadas | 6.4 |
| C11 | Recomendación 3: «crecen 12.5 %»; fechas del seguro solidario que dependen de R4 | 3.3 |
| C12 | Recomendación 4: confunde pensionados (GMP) con personas mayores; lenguaje de incidencia («sin que los patrones paguen más»); alcance del estudio sin pensiones del personal del IMSS, pensión mínima garantizada, Invalidez y Vida, Riesgos de Trabajo, transición del Infonavit y valoración; cifras de la aproximación de R4 | 3.4, 4.4, 5.4 |
| C13 | Recomendación 5: «3.467 % … con base en la ENIGH» (se calibró con el libro de la Dirección de Finanzas); «que no cueste proporcionalmente más» (incidencia); el estudio no evalúa la cuña completa (calendario de cesantía y vejez, escalón arriba del salario mínimo); artículo de la ley por confirmar (art. 106, fracción I, de la LSS) | 3.5, 4.5, 5.5 |
| C14 | Recomendación 6: errata en el título; falta la salvedad de que el efecto de los 3 millones de cotizantes solo considera la atención médica del SEM y usa costo promedio | 3.6 |
| C15 | Cifras que dependen de puntos abiertos de Resultados (R1, R4) sin rango ni advertencia | 2.4, 3.3 a 3.6, 5 |
| C16 | Dos registros de lenguaje: recomendaciones 1 y 2 técnicas y densas; 3 a 6 casi coloquiales | Todo |
| C17 | El documento empieza en la sección 2 | Estructura |

---

## 4. Verificaciones específicas

### 4.1 Cifras

1. Extraer todas las cifras de los dos documentos (texto, tablas y leyendas) a `tablas/cifras.csv`, con:
   - documento, sección, página aproximada y oración;
   - magnitud, valor, unidad y año.
2. Agrupar por magnitud y marcar las que tienen más de un valor dentro de un documento o entre documentos. Algunos ejemplos: derechohabientes de 2025 y de 2055; gasto en trazadores de 2025 y de 2055; porcentaje de crecimiento atribuible al envejecimiento; ingresos del SEM; brecha de 2025; saldo de la afiliación subsidiada; años de cobertura del seguro solidario; cotizantes de 2025 y de 2054.
3. Recalcular sumas de tablas, porcentajes y tasas de crecimiento que puedan obtenerse con las cifras del propio documento. Reportar las diferencias mayores a la precisión publicada.
4. Si el Informe del IMSS está disponible, contrastar las cifras que dicen venir de él (por ejemplo, la prima de 9.60 % del Cuadro A.4; la prima de equilibrio de 12.9 % y la de financiamiento de 8.9 %; los derechohabientes).

### 4.2 Referencias

En `tablas/referencias.csv`, por cada referencia de la lista y cada cita del texto, registrar:

- si se cita en el texto y si está en la lista;
- si existe y cómo se verificó: DOI, Crossref, catálogo de la editorial o búsqueda en la web (si Dalila tiene acceso a red);
- si los datos bibliográficos coinciden: autores, año, revista, volumen y páginas;
- si el texto le atribuye algo que la obra no dice. Marcarlo solo si se pudo leer el resumen o el texto; si no, «no verificado».

**Ninguna referencia se da por existente sin verificarla.** Las que no se encuentren se marcan como «no localizada», sin especular si son correctas.

### 4.3 Lenguaje y reglas del equipo

Buscar y listar las apariciones de:

- **Lenguaje de incidencia económica:** «costo para el patrón», «costo laboral», «costo de la formalidad», «abarata», «sin que los patrones paguen más», «lo que pagan los patrones», «que no cueste más a…» y equivalentes. La regla es describir **tasas legales** («a cargo del patrón por ley», «cuña contributiva legal»).
- **Juicios no sustentados de sostenibilidad o de autofinanciamiento**, y afirmaciones causales sobre la formalidad que el análisis no estima.
- **Resultados de ITED presentados como proyección del IMSS** o como propuesta del IMSS o del Gobierno.
- **Siglas no definidas** en su primera aparición.
- **Legibilidad:** índice de Fernández Huerta por sección y longitud media de oración. Solo como referencia, no como calificación.

### 4.4 Figuras y tablas

Por cada figura y tabla, en `tablas/figuras_tablas.csv`, registrar:

- número y título;
- si se cita en el texto y si se cita antes de aparecer;
- fuente al pie;
- unidades;
- legibilidad;
- coincidencia con las cifras del texto;
- duplicados.

---

## 5. Salidas

En `Missions/Funded/IMSS_Surgical/evaluacion_informes_N13/`:

1. **`EVALUACION_N13.md`**, con esta estructura:
   1. **Veredicto** (máximo una página): nivel global de cada documento, en una oración cada uno; los cinco problemas que más pesan; qué falta para llegar al nivel 4, en orden.
   2. **Tabla de calificaciones**: dimensiones D1 a D9 por documento, con nivel y una línea de justificación.
   3. **Estado de los problemas ya identificados** (sección 3): ID, estado y evidencia.
   4. **Problemas nuevos**, por severidad.
   5. **Evaluación por sección** de cada documento: dos a cinco líneas por sección.
   6. **Coherencia entre documentos**: tabla de discrepancias.
   7. **Ruta para cerrar**: lista ordenada de acciones. Para cada una, quién decide (el equipo, Juan Pablo, Héctor, el IMSS) y si cambia cifras del resumen ejecutivo.
2. **`tablas/hallazgos.csv`**, con una fila por problema y estas columnas:

   | Columna | Contenido |
   |---|---|
   | `id` | |
   | `documento` | |
   | `seccion` | |
   | `pagina_aprox` | |
   | `dimension` | D1 a D9 |
   | `severidad` | bloqueante, mayor, menor o editorial |
   | `descripcion` | |
   | `evidencia_textual` | |
   | `propuesta` | |
   | `estado` | nuevo, conocido-pendiente, conocido-parcial o conocido-resuelto |

   Criterio de severidad:
   - **Bloqueante:** invalida un resultado central o una recomendación.
   - **Mayor:** cambia una cifra o un mensaje.
   - **Menor:** no cambia cifras ni mensajes.
   - **Editorial:** solo de forma.
3. **`tablas/cifras.csv`, `tablas/referencias.csv`, `tablas/figuras_tablas.csv` y `tablas/comentarios.csv`** (secciones 1 y 4).
4. **Opcional, si la biblioteca lo permite** (`python-docx` 1.2 o posterior admite comentarios): copias de los dos .docx con un comentario de Word en cada hallazgo bloqueante o mayor, con el ID del hallazgo. Se guardan como `…_evaluacion_comentado.docx`, **nunca sobre el original**. Si no se puede, omitirlo y reportarlo.
5. **Documento en Claude Docs** titulado «N13 · Evaluación del Informe de Resultados y del Informe de Recomendaciones (v1)», con el veredicto, la tabla de calificaciones, el estado de los problemas conocidos y la ruta para cerrar. Sin rutas de Dalila.

---

## 6. Reglas

1. **Evidencia o no se afirma.** Todo hallazgo lleva su cita textual y su ubicación. Si algo no se puede comprobar, se marca «no verificado».
2. **No reescribir.** Las propuestas dicen qué hacer, con una redacción sugerida solo cuando sea indispensable para entender el cambio (máximo dos oraciones).
3. **Separar decisiones de método y correcciones.** El conteo de derechohabientes y la trayectoria del gasto son decisiones del equipo; una suma mal hecha es una corrección. Marcar cuál es cuál.
4. **Tono.** Los documentos tienen varios autores. La evaluación describe problemas del texto, no de personas.
5. **Sin cifras propias nuevas.** Los recálculos de la sección 4.1 sirven para detectar inconsistencias, no para proponer cifras sustitutas. Las cifras correctas las decide el equipo con el cuaderno.

---

## 7. Verificaciones de la ejecución

| # | Verificación |
|---|---|
| 7.1 | Hash de los dos originales igual antes y después. |
| 7.2 | Los 33 problemas de la sección 3 (16 de Resultados y 17 de Recomendaciones) tienen estado y evidencia. |
| 7.3 | Cada calificación de la rúbrica tiene al menos una evidencia citada. |
| 7.4 | Todas las referencias de la lista están en `referencias.csv` con un estado de verificación. |
| 7.5 | Todas las figuras y tablas están en `figuras_tablas.csv`. |
| 7.6 | El veredicto cabe en una página y nombra el nivel global de cada documento. |

---

## 8. Reporte

Agregar a `REPORT.md` de la carpeta de salida:

- los insumos usados (incluidos los de contraste);
- las herramientas y versiones;
- lo que no se pudo verificar y por qué;
- las verificaciones de la sección 7;
- las decisiones propias, marcadas **[REVISAR]**.

Hacer commit y archivar esta instrucción en `_crossrefs/_build_instructions/`.
