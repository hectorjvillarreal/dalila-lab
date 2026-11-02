# REPORT — Evaluación de los informes del Núcleo 13 (v1)

Instrucción: `20261101_BDH_N13_evaluacion-informes_build_v1.0` (archivada en `_crossrefs/_build_instructions/`).
Ejecutor: Claude Code (Dalila). Fecha: 2026-11-01. Carpeta de insumos indicada por Héctor: `Missions/Funded/IMSS_Surgical/entrega_finales_versiones/`.

## 1. Insumos usados

| Insumo | Ruta | Uso |
|---|---|---|
| Informe de Resultados | `entrega_finales_versiones/Nucleo13_Informe_Resultados_Oct2026_LIMPIO.docx` | Lectura completa (22,044 palabras, 68 pp. en PDF, 35 figuras, 26 tablas) |
| Informe de Recomendaciones | `entrega_finales_versiones/Nucleo13_Informe_Recomendaciones-4.docx` | Lectura completa (4,875 palabras, 15 pp., sin figuras ni tablas) |
| Cuaderno del Núcleo 13 | `entrega_finales_versiones/reporte_final_28oct.ipynb` (353 celdas) | Contraste de la Tabla 5 (celda 16.6: coincide al peso) y del método de balance (`METODO_GASTO_BALANCE = "pct"`) |
| Informe al Ejecutivo Federal 2025-2026 (IMSS) | `e_1_imss_subsidiado/_informe-situacion-financiera_imss.pdf` (338 pp.) | Cuadros A.3, A.4, I.4, II.14, II.18, IV.3, V.11, V.13, V.19, V.24, C.1 |
| Anexo técnico ITED, experimento 1 | `e_1_imss_subsidiado/anexo_afiliacion_subsidiada/ANEXO_borrador_v3.md`, `NUMBERS.md` | Contraste de 6a |
| Anexo técnico ITED, experimento 2 | `e_2_imss_nuevoseguro/ANEXO_experimento2_borrador_v4.md`, `REPORT.md`, `NUMBERS.md`, `tablas/*.csv` | Contraste de 6b |
| Sección 10 de ITED | `seccion10_esquemas_financiamiento/N13_seccion10_esquemas_financiamiento_v1.2.md` | Referencia de qué cifras siguió ITED |
| Fuentes externas (referencias) | Crossref, PubMed, OUP, CEPAL, dcp-3.org, who.int, gob.mx/conapo, imss.gob.mx, ciep.mx | Verificación de las 22 referencias y 4 citas sin entrada |

Los dos documentos no tienen cambios controlados (`w:ins`/`w:del` = 0) ni comentarios (`comments.xml` ausente); `pandoc --track-changes=accept` y `=all` producen el mismo texto. `tablas/comentarios.csv` queda sólo con cabecera.

## 2. Herramientas y versiones

pandoc 3.12.1 (env `dalila`) · LibreOffice 24.2.7.2 (render a PDF) · poppler 24.02 (`pdftoppm` 90 dpi, `pdftotext -layout` por página) · Python 3.12.13 · python-docx 1.2.0 (comentarios de Word) · tres subagentes de Claude Code (referencias con WebSearch/WebFetch; revisión visual de las 83 páginas y los 35 archivos de `word/media`; contraste con el Informe del IMSS y los anexos de ITED). Reportes completos de los subagentes en `respaldo/`.

## 3. Salidas

- `EVALUACION_N13.md` — veredicto, calificaciones, estado de los 33 problemas conocidos, 33 problemas nuevos, evaluación por sección, coherencia entre documentos, ruta para cerrar.
- `tablas/hallazgos.csv` — 66 filas (33 conocidos + 33 nuevos); columnas de la instrucción más `decide` y `cambia_resumen`. Severidad: 21 mayores, 36 menores, 9 editoriales; ningún bloqueante.
- `tablas/cifras.csv` — 2,533 cifras extraídas automáticamente de los dos documentos (oración, sección, página aproximada, valor, unidad, año, magnitud por palabra clave). `tablas/cifras_clave.csv` — 20 magnitudes clave con sus valores en cada documento y el contraste con el Informe del IMSS y los anexos de ITED.
- `tablas/referencias.csv` — 26 filas (14 + 8 de las listas, 4 citas sin entrada) con estado de verificación y URL.
- `tablas/figuras_tablas.csv` — 35 figuras y 26 tablas de Resultados (citada, citada antes, fuente, unidades, legibilidad, coincidencia, duplicados).
- `tablas/comentarios.csv` — vacío (sin comentarios en los archivos).
- `Nucleo13_Informe_Resultados_Oct2026_LIMPIO_evaluacion_comentado.docx` (9 comentarios) y `Nucleo13_Informe_Recomendaciones-4_evaluacion_comentado.docx` (12 comentarios): un comentario de Word por hallazgo mayor, anclado en la cita textual, con el ID. Los originales no se tocaron.
- Documento en Claude Docs «N13 · Evaluación del Informe de Resultados y del Informe de Recomendaciones (v1)» (sin rutas de Dalila).
- `respaldo/` — reportes de los subagentes (visual, contraste, referencias) y las tablas intermedias (legibilidad, siglas, lenguaje).

## 4. Lo que no se pudo verificar y por qué

- **Plantilla de la Comisión**: no hay plantilla en la carpeta; D9 se infirió de la estructura de los dos documentos y del Anexo B («conforme a los requisitos del protocolo de la Comisión»).
- **Comentario de Mónica Montano sobre la lista de autores (R16)**: el archivo no tiene comentarios; se evaluó la lista por comparación entre los dos documentos.
- **Cifras internas del IMSS** (1,410,605 cirugías, 10,536 / 21,259, 27 % de subregistro, 187 quirófanos, $8,715, 1.42 % y 3.4 % del PIB): sin documento citado; marcadas como no verificadas.
- **INEGI, «gasto real en salud +5 % anual»**: sin serie ni periodo.
- **Referencias internas** (Coordinación de Asesores 2024; Síntesis de las Mesas 2026): no verificables públicamente.
- **Capítulo de proyecciones de Health at a Glance 2019**: oecd.org devolvió 403; el juicio sobre la atribución se basó en el Working Paper 110 que lo sustenta.
- **Cuaderno de ingresos**: no está en la carpeta de entrega; los ingresos del SEM sólo pudieron cotejarse con la salida del cuaderno de reporte (coincide) y con el Informe del IMSS (perímetro distinto).
- **Signo menos como cuadro vacío**: es un efecto del render de LibreOffice (U+2212 sin glifo en la fuente); no se comprobó en Word [REVISAR].
- **Página aproximada**: corresponde al PDF de LibreOffice; en Word puede desplazarse una o dos páginas.
- **`tablas/cifras.csv`**: la extracción es automática por expresión regular y la columna `magnitud` es una etiqueta por palabra clave; sirve para localizar, no para contar. El agrupamiento por magnitud se hizo a mano en `cifras_clave.csv`.

## 5. Verificaciones de la sección 7 de la instrucción

| # | Verificación | Resultado |
|---|---|---|
| 7.1 | Hash de los originales igual antes y después | **Cumplida.** sha256 Resultados `f5f0b711d2f43f4f1c16a823b52c6799c33b6c0cf5f96be84bf3982a63828bcc`; Recomendaciones `913a73fc663ae38c2a41d91cb9b567406c3843949431aafdf91c20002c039aad`; iguales al cierre. |
| 7.2 | Los 33 problemas de la sección 3 tienen estado y evidencia | **Cumplida.** 16 R + 17 C en `hallazgos.csv` con `estado` ∈ {conocido-resuelto 5, conocido-parcial 10, conocido-pendiente 18} y `evidencia_textual`. |
| 7.3 | Cada calificación tiene al menos una evidencia citada | **Cumplida.** Tabla de la sección 2 de `EVALUACION_N13.md`. |
| 7.4 | Todas las referencias de la lista están en `referencias.csv` con estado | **Cumplida.** 14 + 8 entradas, más 4 citas sin entrada. |
| 7.5 | Todas las figuras y tablas en `figuras_tablas.csv` | **Cumplida.** 35 figuras y 26 tablas de Resultados; Recomendaciones no tiene. |
| 7.6 | El veredicto cabe en una página y nombra el nivel global de cada documento | **Cumplida.** Sección 1 de `EVALUACION_N13.md` (≈ 560 palabras). |

## 6. Decisiones propias [REVISAR]

- **[REVISAR] Severidad sin «bloqueante».** Ningún hallazgo invalida por sí solo un resultado central; los tres mayores de método (N-R20, R4/R5, R6) juntos cambian las cifras del resumen. Si el equipo decide que una referencia inexistente en la justificación de una recomendación la invalida, N-C10 pasaría a bloqueante.
- **[REVISAR] D5 = 1 en los dos documentos.** Se calificó la dimensión como «no apta» por las cuatro referencias no localizadas; D5 no entra en el mínimo del nivel global, por lo que el global queda en 2.
- **[REVISAR] D1 = 3 en Resultados** pese a las Figuras 5 y 10: las leyendas erradas no alteran ninguna cifra del texto; se trató como figura a regenerar (N-R17, mayor).
- **[REVISAR] N-R20 (6a/6b frente a los anexos de ITED) se registró como hallazgo nuevo** aunque la instrucción no lo pedía expresamente; el §1.4 pedía usar los anexos como contraste y la diferencia es de 2 a 4 veces en las cifras del resumen.
- **[REVISAR] El «déficit institucional ≈74 mil millones en 2027» de la instrucción (R4)** no está en el Informe del IMSS (cuadros quinquenales); es la interpolación del anexo de ITED del Cuadro V.24 (74,270 en 2027). Se usó así en la evidencia.
- **[REVISAR] `build_type: initial_scaffold`** existe en la enumeración de PROTO-RAG-001 (línea 74); se dejó.
- **[REVISAR] Carpeta de insumos**: `entrega_finales_versiones/` indicada por Héctor; contiene exactamente los dos .docx y el cuaderno.
- Los comentarios de Word se limitaron a los hallazgos mayores (21) para no saturar los archivos; los menores y editoriales están en `hallazgos.csv`.
- Las páginas de `hallazgos.csv` se obtuvieron buscando la primera cita textual de cada evidencia en el texto por página del PDF; donde no hubo coincidencia se dejó en blanco y vale la sección.
