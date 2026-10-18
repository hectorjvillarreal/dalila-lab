---
id: REPORT_seccion10_v1
title: "Reporte de ejecución — Sección 10 del Núcleo 13: Esquemas de financiamiento alternativos (v1)"
build_instruction: _crossrefs/_build_instructions/2026-10-18_BDH-N13_seccion10-esquemas-financiamiento_initial-scaffold_v1.0.md
date: 2026-10-18
executor: Claude Code (Dalila)
status: borrador para revisión (Beth, Cath, Héctor; conciliación con Juan Pablo)
---

# Reporte — Sección 10: Esquemas de financiamiento alternativos (v1)

Fuentes: experimento 1 v1.2 (borrador v3) para 10a; experimento 2 v1.3 (borrador v4) para 10b. Sin corridas ni supuestos
nuevos. Los dos experimentos se leyeron sin modificarse. El original de Juan Pablo no cambió (8.11).

## Salidas

| Archivo | Contenido |
|---|---|
| `N13_seccion10_esquemas_financiamiento_v1.md` | Texto fuente |
| `N13_seccion10_esquemas_financiamiento_v1.docx` | La sección sola, con la plantilla del documento de JP (12 páginas) |
| `Nucleo13_Informe_Resultados_Oct2026 atendido JP_con_seccion10_v1.docx` | Copia del documento de JP con la sección 10 al final (67 páginas; la sección ocupa las 55 a 67). Fuera de git, como el original de JP |
| `figuras/` | F10a_1 a F10b_4: PNG (300 ppp), SVG y CSV |
| `tablas/conciliacion_seccion10.csv` | Cifras compartidas con el documento de JP (sección 3 de este reporte) |
| `tablas/seccion10_cifras.csv` | 149 cifras de texto, tablas y figuras, con su respaldo |
| `data/verificaciones.json`, `data/hash_original_*.txt` | Resultados de 8.1 a 8.9 y hash del original |
| `src/` | `figuras.py`, `cifras_mapa.py`, `verificar.py`, `conciliacion.py`, `docx_seccion10.py` (ver `src/README.md`) |

Orden de ejecución: `figuras.py` → `verificar.py` → `conciliacion.py` → `docx_seccion10.py`.

**Sobre el .docx.** La instrucción sugería `pandoc --reference-doc`. Se instaló pandoc 3.12.1 en el entorno `dalila` y se
probó: con la plantilla de JP pierde las viñetas (el documento no tiene `numbering.xml`) y deja la Tabla 10.1 en una sola
columna angosta. Por eso los dos .docx se generan con python-docx, copiando del XML de JP el formato de cada elemento.

## 1. Documento de Juan Pablo

- **Único candidato:** `Missions/Funded/IMSS_Surgical/Nucleo13_Informe_Resultados_Oct2026 atendido JP.docx`.
  - Fecha en disco: 17-10-2026.
  - Metadatos: creador «ITED — Núcleo 13»; última modificación de Juan Pablo López Reynosa, 16-10-2026.
  - Contiene 57 comentarios y 191 cambios con control (131 inserciones, 60 eliminaciones); todos son de JP.
  - No está bajo control de versiones en git.
- **Numeración.** Secciones 2 a 9 con «Heading 1» (de «2. Resumen ejecutivo» a «9. Anexos»); subsecciones con
  «Heading 2» (hasta 9.13). No había sección 10. Se insertó como «10», al final, después de «9. Anexos» (opción b de
  Héctor), en página nueva. No se renumeró nada. El documento no tiene índice automático ni referencias cruzadas.
- **Estilos copiados del XML.**
  - Títulos: «Heading 1» (12 pt, negrita) y «Heading 2» (negrita). JP no usa «Heading 3».
  - Párrafo: justificado, 6 pt antes y después, interlineado 1.15, Noto Sans 12 pt.
  - Figuras: centradas; leyenda debajo («Figura N. …», negrita 9 pt); fuente al pie («Fuente: elaboración propia…»,
    cursiva gris 8 pt).
  - Tablas: título arriba («Tabla N. …», negrita 9 pt); ancho de texto completo; encabezado con fondo azul claro;
    bordes grises; texto de 8.5 pt.
  - JP no usa listas con numeración automática.
- **Unidades y separadores.** Miles de millones de pesos de 2026 en el texto y «MDP de 2026» en tablas. Punto decimal y
  coma de miles. Porcentaje con espacio («63.6 %»).
- **Citas.** Autor y año entre paréntesis («IMSS, 2025»; «Rechel et al., 2013»).

## 2. Tabla de términos y equivalencias

| Concepto | Término de JP | Término en los anexos | Término en la sección 10 |
|---|---|---|---|
| Población con derecho | derechohabientes | DH | derechohabientes |
| Personas con cotización | cotizantes | cotizantes | cotizantes |
| Seguro de Enfermedades y Maternidad | SEM | SEM | SEM (definido en la introducción) |
| Gastos médicos de pensionados | GMP | GMP | gastos médicos de pensionados (GMP) |
| Diferencia entre ingreso y gasto | brecha, balance | déficit, saldo | déficit (GMP, como el Informe del IMSS); saldo sin fuente de financiamiento asignada (10a) |
| Salario base de cotización | SBC | SBC | salario base de cotización (SBC), definido en 10a.2 |
| Unidad de Medida y Actualización | UMA | UMA | UMA, definida en 10a.1 |
| Numeración de cuadros | Tabla | Cuadro | **Tabla** (como JP); «Cuadro» solo para citar el Informe del IMSS |
| Gráficas | Figura | Figura | Figura |
| Fuente de las gráficas | «Fuente: elaboración propia» | — | «Fuente: elaboración de ITED» (pide la instrucción) **[REVISAR]** |
| Proyección institucional | proyección institucional | Informe al Ejecutivo; libro de la Dirección de Finanzas | proyección del IMSS; Informe del IMSS; libro de la Dirección de Finanzas |
| Formalidad | formalidad | formalización, formalidad | formalidad (nivel) y formalización (cambio) |
| Valor presente | — | VP | valor presente, definido en 10b.1 |
| Cuña contributiva legal | — | cuña legal | cuña contributiva legal, definida en 10b.1 |
| Provisiones | — | provisiones | definidas en la Tabla 10.2 |

Equivalencia de símbolos (3.2):

| Símbolo del anexo | Nombre en la sección 10 |
|---|---|
| τ | proporción de hogares que se afilia |
| ρ | proporción de las cuotas que efectivamente se cobra |
| μ | sobrecosto de atención de quienes se afilian primero |
| K2 | con reserva |
| K1 | sin reserva |
| Base | formalización de la proyección del IMSS |
| M3 | mitad de esa formalización |
| M2 | formalidad constante |
| MH | ritmo histórico |
| D2 | cuota proporcional al salario |

## 3. Conciliación con el documento de JP

Detalle en `tablas/conciliacion_seccion10.csv` (16 filas). Diferencias mayores a 1 %:

| Cifra | JP | Anexos | Diferencia | Tratamiento |
|---|---|---|---|---|
| Derechohabientes 2025 | 70.69 M (Tabla I.1) | 79.18 M (Informe, Cuadro I.4) | +12.0 % | **[REVISAR-JP: conciliación de derechohabientes]**. La sección dice qué cifra usa y remite a una nota que no dice cuál es la correcta |
| Derechohabientes 2025, mismo método de JP | 70.69 M | 54.63 M (ENIGH × CONAPO) | −22.7 % | Mismo caso; sigue abierto (N13 no se reproduce) |
| Ingresos del SEM 2030 | 611.2 (Tabla 5, libro) | 626.3 (Informe, Cuadro V.13) | +2.5 % | **[REVISAR-JP]** en el texto de 10a.4. Los porcentajes del SEM de la sección usan el Cuadro V.13 (denominador común de los anexos) |
| Gasto de bolsillo por hogar | 6,421 pesos (CIEP; promedio nacional; pesos de 2024) | 5,773 pesos (decil V de los hogares objetivo; pesos de 2026) | −10.1 % | No son comparables: la sección 10 usa solo la de la ENIGH y no las mezcla |

Coinciden (diferencia menor a 1 %): cotizantes 2025, 2030 y 2040; cotizantes del último año (46.69 en 2055 frente a
46.80 en 2054); ingresos del SEM del libro en 2030; ingresos del SEM en 2040; ingresos totales del IMSS de 2025 (851.3);
tasa efectiva del SEM (9.60 %); primas de equilibrio (12.9 frente a 12.94) y de financiamiento (8.9 frente a 8.93).
JP no publica la población de 65 años o más (reporta 60 o más); no hay cifra que conciliar.

## 4. Títulos propuestos

| Instrucción (provisional) | Propuesto | Razón |
|---|---|---|
| 10a. Afiliación subsidiada para trabajadores independientes y hogares de ingresos bajos y medios bajos | **10a. Afiliación subsidiada para hogares sin seguridad social** | Más corto; el ejercicio se define por hogar, no por tipo de trabajador |
| 10b. De la aportación al Infonavit a un seguro solidario de salud y cuidados en la vejez | **10b. Del Infonavit a un seguro de salud y cuidados en la vejez** | Más corto; «solidario» se explica en 10b.2 |

Los dos títulos usan «Heading 2», como las subsecciones de JP. Los apartados 10a.1–10b.7 también llevan «Heading 2».
Si Héctor prefiere un nivel más, el documento tiene «Heading 3», pero JP no lo usa y su formato es distinto (azul, sin
negrita).

## 5. Frase de apertura de 10a [REVISAR-Beth]

> Con los supuestos base, el esquema cubriría a unos 31.4 millones de personas en 2030 con un pago de 3.5 % del ingreso
> laboral en el hogar mediano. El costo de atención supera lo que aportan los hogares y el Gobierno Federal: queda un
> saldo sin fuente de financiamiento asignada de unos 81 mil millones de pesos al año, 1.3 puntos del salario en 2030.

Abre 10a.4, en negrita, como las dos frases obligatorias de 10b.4. Evita «cubre su costo» y todo juicio de
sostenibilidad.

## 6. Regla de redondeo

| Tipo de cifra | Texto | Tablas y figuras |
|---|---|---|
| Montos | miles de millones de pesos de 2026, 0 decimales, con «unos» | Igual, salvo etiquetas de figura con 0 decimales |
| Puntos del salario y % | 1 decimal | 1 decimal (cuña legal en la Figura 10.8: 1 decimal) |
| Personas | millones con 1 decimal | — |
| Pesos por hogar o por persona | pesos exactos, sin decimales | Igual |
| Parámetros legales | como en la ley (20.40 % y 14.83 % de la UMA; 3.467 % del salario) | — |

**Caso 6.6 frente a 6.5.** El anexo v4 dice que la formalidad subió «6.6 puntos» entre 2005 y 2025. Es la resta de los
extremos ya redondeados (37.7 − 31.1). La resta exacta es 6.548, que redondea a 6.5, y así está registrada en
`NUMBERS.md` (`form_hist_cambio_pts`). La sección 10 dice 6.5. Conviene corregir el anexo en su próxima versión
**[REVISAR]**: el experimento 2 era de solo lectura en esta tarea.

## 7. Extensión y legibilidad

| | Introducción | 10a | 10b | Límite |
|---|---|---|---|---|
| Caracteres de texto corrido | 697 | 6,805 | 6,239 | 900 / 10,800 / 10,800 |
| Cuartillas (1,800 caracteres) | 0.39 | 3.78 | 3.47 | 0.5 / 6 / 6 |
| Páginas en el formato de JP (con figuras y tablas) | 0.3 | 5.6 | 6.4 | — / 8 / 8 |
| Oraciones | 8 | 80 | 70 | — |
| Promedio de palabras por oración | 15.4 | 15.5 | 16.5 | 22 |
| Oración más larga (palabras) | 22 | 37 | 42 | 40 |
| Índice de Fernández Huerta | 91.0 | 84.3 | 88.0 | 60 o más |

Las páginas se contaron sobre el PDF de LibreOffice de la copia: la sección empieza en la página 55; 10b, en la 60; la
última es la 67. La única oración de más de 40 palabras es la frase obligatoria 1 de 10b (42 palabras). Se copió
literalmente de la instrucción y por eso no se partió **[REVISAR]**.

## 8. Lo que no cupo y se queda en los anexos

- **10a.**
  - Malla completa de sensibilidad: sobrecosto, umbrales y perfil de costo por edad.
  - Comparación de los anexos v1.1 y v1.2.
  - Saldos por bloque (hogares objetivo y efecto sobre los formales) año por año.
  - Cálculo individual completo (solo se da el resultado de 2030).
  - El efecto de la cuota proporcional sobre los formales aparece en un párrafo; su serie anual queda en el anexo.
- **10b.**
  - Columna (b) de la cuña legal (seguro solidario con cuota proporcional sin la reducción) y el desglose por rama.
  - Escenario base con el conteo máximo de mayores del Informe: 2,327 pesos por persona de 65 años o más en 2040,
    frente a 5,631 con la ENIGH. La sección usa la ENIGH, como la sección 4.2 de JP.
  - Resultados sin reserva, por persona y año.
  - Valor presente por escenario, salvo el de la base.
  - Serie histórica de formalidad año por año.
- **Figura 10.2.** La línea de referencia del gasto de bolsillo no se dibujó: está en pesos y la figura en % del ingreso.
  Se da como contexto en el texto (5,773 pesos en el decil V) **[REVISAR]**.

## 9. Verificaciones

| # | Resultado |
|---|---|
| 8.1 | Cumple: 10a ≈ 5.6 y 10b ≈ 6.4 páginas; texto corrido 6,805 y 6,239 caracteres; introducción 697 |
| 8.2 | Cumple: 149 cifras en `seccion10_cifras.csv`; 139 respaldadas en `NUMBERS.md` y 10 en `config.yaml` del experimento 1 (ver 10); 0 sin respaldo |
| 8.3 | Cumple: texto, tablas y figuras coinciden entre sí y con los registros de los anexos; única diferencia con el texto de un anexo: 6.6 frente a 6.5 (sección 6) |
| 8.4 | Cumple: 0 expresiones prohibidas |
| 8.5 | Cumple: 0 años después de 2054 en texto, figuras y CSV de figuras |
| 8.6 | Promedios 15.4 / 15.5 / 16.5; Fernández Huerta 91.0 / 84.3 / 88.0. Una oración de 42 palabras (la frase obligatoria 1) |
| 8.7 | Cumple: siete apartados en el mismo orden y con los mismos encabezados en 10a y 10b |
| 8.8 | Cumple: las dos frases obligatorias aparecen literalmente; sus cifras coinciden con el Cuadro X-2.3 de la v1.3 |
| 8.9 | Cumple: 0 términos sin definir en su primera aparición (UMA, SBC, cuota fija, GMP, cuña contributiva legal, valor presente, provisiones) |
| 8.10 | Hecha: las 8 figuras se revisaron una a una y se corrigieron solapes (etiquetas de los esquemas, leyendas de F10b.2 y F10b.3, ejes de F10a.4 y F10b.1). Las 12 páginas del .docx se revisaron en PDF: 0 textos cortados o solapados |
| 8.11 | Cumple: hash SHA-256 `3f4002b8…a8cf88` antes y después |

**Nota de visualización.** En el PDF de LibreOffice, el signo menos (−) del texto se ve como un cuadro. Pasa también
en el texto de JP (por ejemplo, la página 54): es la fuente Noto Sans incrustada y recortada del documento. En Word con
Noto Sans instalada se ve bien. Las figuras no tienen el problema.

## 10. Decisiones propias [REVISAR]

1. **Fuente de las figuras.** Se usa «Fuente: elaboración de ITED», como pide la instrucción. JP usa «elaboración
   propia».
2. **Parámetros del escenario.** 50 %, 75 %, 10 %, 70 %, 30 %, 2 %, 20 % y 3 millones están en `config.yaml` del
   experimento 1, no en su `NUMBERS.md`. Se respaldan contra `config.yaml`. Conviene registrarlos en `NUMBERS.md` en la
   próxima versión del experimento 1.
3. **6.5 en lugar de 6.6** (sección 6).
4. **Frase obligatoria 1 de 10b** con 42 palabras, sin partir.
5. **Línea del gasto de bolsillo** omitida en la Figura 10.2.
6. **Leyenda de figura debajo de la imagen y título de tabla arriba**, como en el documento de JP. El .md sigue el
   mismo orden.
7. **Viñetas** como párrafos con sangría y «•», porque el documento de JP no tiene listas numeradas.
8. **Marcas en el texto:** [REVISAR-Beth] en 10a.4; [REVISAR-JP: ingresos del SEM] en 10a.4; [REVISAR-JP:
   conciliación de derechohabientes] en la nota de 10a. En el .docx aparecen resaltadas en amarillo y se retiran al
   cerrar la redacción.
9. **«Anexo X»** se deja literal: Héctor decide después dónde van los anexos.
