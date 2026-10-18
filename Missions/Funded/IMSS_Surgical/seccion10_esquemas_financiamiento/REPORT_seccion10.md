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

---

# v1.1 — correcciones de fondo, figuras y paginación (18-10-2026)

Instrucción: `20261018_BDH_N13_seccion10-esquemas-financiamiento_build_v1.1` (Beth; revisión de Beth y Cath). La v1 se conserva.

| Archivo nuevo | Contenido |
|---|---|
| `N13_seccion10_esquemas_financiamiento_v1.1.md` / `.docx` | Texto y .docx de la v1.1 |
| `Nucleo13_Informe_Resultados_Oct2026 atendido JP_con_seccion10_v1.1.docx` | Copia de JP con la v1.1 al final (fuera de git) |
| `tablas/seccion10_cifras_v1.1.csv`, `data/verificaciones_v1.1.json` | Registro de cifras y verificaciones de la v1.1 |
| `figuras/` | F10a_2, F10b_2, F10b_3 y F10b_4 cambian; todas se redibujan a 5.4 in (85 % del ancho de texto). La v1 queda en git |
| `e_1…/src/seccion10_v11.py` (+ `.md`) | Cifras nuevas de 1.1, 1.3, 1.5 y 1.9; claves `s10v11_*` en `NUMBERS.md` del experimento 1; incluido en `run_all.py` |

Orden: `e_1…/src/seccion10_v11.py` → `cifras.main()` → `figuras.py` → `verificar.py v1.1` → `conciliacion.py` → `docx_seccion10.py v1.1`.

## 1. Cifras nuevas y su cálculo

| Punto | Cifra | Cálculo | Clave |
|---|---|---|---|
| 1.1 | 8,736 pesos; 8.3 % del ingreso laboral (mediana) | (1 − s) × 20.40 % × UMA 2026 × 365, más el excedente sobre 3 UMA con 337 días, igual que la serie de la cuota proporcional. Mismo subsidio y umbrales que la Figura 10.2. Por percentil: 0, 0, 3,190, 8,736, 9,072 y 10,618 pesos (P10 a P90). Con subsidio total en P10 y P20, ambas cuotas valen 0 | `s10v11_p{q}_fija_patronal`, `…_pctlab` |
| 1.5 | 4,921 pesos; 2.1 % del ingreso del hogar (hogar mediano, afiliación individual) | Cada integrante paga 3.467 % del ingreso por persona del hogar, con el subsidio por persona; más el excedente de quien trabaja. Mediana de los hogares con titular en ±2.5 percentiles de la mediana, 2026 | `s10v11_U2_pago_hogar_p50`, `…_pct_hogar_p50` |
| 1.3 | +12.0 % de costo por persona; saldo de 2030 de unos 105 mil millones | 79,178,109 / 70,690,000 − 1. El saldo 2030 (−80,962 mdp) menos el costo (197,237) × 0.120 = −104,645. Sin otra corrida | `s10v11_costo_pp_70M_dif_pct`, `s10v11_saldo_mdp_2030_70M` |
| 1.3.2 | 41.2 % → 63.9 % de la población con IMSS en 2030 | Tasa IMSS por edad y sexo de la ENIGH 2024 × CONAPO 2030 = 56.83 M, entre 138.03 M de población; con el esquema se suman 31.4 M (hogares sin seguridad social: no se traslapan) | `s10v11_DH_enigh_2030`, `s10v11_pct_pob_imss_2030_*` |
| 1.9 | 13.2 % (nota al pie) | −80,962 / 611,200 (Tabla 5 de JP; igual al libro, 611,178). También en `tablas/conciliacion_seccion10.csv` | `s10v11_saldo_pct_tabla5_2030` |

Verificación 5.2: en la mediana, 3,647 (cuota proporcional) < 8,736 (cuota fija patronal) < 15,087 (cuota fija completa). Cumple. La referencia de Beth era de unos 8,700 pesos y 8.3 %.

**Días.** La cuota proporcional de la Figura 10.2 usa 365 días para el ingreso anual y 337 días para el umbral del excedente (`asequibilidad` en `v12.py`). La nueva serie usa los mismos. La primera versión de `seccion10_v11.py` usaba 365 en los dos y movía 0.1 puntos en P70 y P90; se corrigió antes de redactar.

## 2. Derechohabientes y población con IMSS

- **El conteo sí interviene.** El costo por persona del SEM es el gasto en especie de 2026 (Cuadro V.13, 494,275 mdp) entre los 79,178,109 derechohabientes del Cuadro I.4: `e_1…/src/proyeccion.py`, línea 402 (`costo_per_capita_DH_2026`, `ins.c_bar`). Ese costo por persona entra al costo de los bloques A y C (`c_edad`, líneas 151 y 295).
- Por eso la frase «no cambia los resultados» se sustituyó por la redacción prevista en la instrucción: con 70.7 millones, el costo por persona sube 12.0 % y el saldo de 2030 llega a unos 105 mil millones. La marca **[REVISAR-JP: conciliación de derechohabientes]** se mantiene.
- **Cobertura:** con el conteo de la ENIGH, la población con IMSS pasaría de 41.2 % a 63.9 % de la población nacional en 2030.
- La nota de derechohabientes ahora dice qué conteo usa cada cifra.

## 3. Los 326 mil millones

Se quedan, con su fuente: CIEP, «PPEF 2027: Gasto en salud por subsistema», Cuadro 1. Es el PEF 2026: Secretaría de Salud, IMSS-Bienestar, FASSA y Bienestar, que suman 338,028 mdp de 2027 y equivalen a 325,591 mdp de 2026 con la inflación de 2027 del libro. Está en `NUMBERS.md` del experimento 1 (`PEF2026_*`). La oración pasa al párrafo «Saldo para el SEM», después del saldo, sin «alcanza» ni «puede reasignarse».

## 4. Provisiones

El Informe del IMSS solo las define con una nota al pie del Cuadro V.19 (pág. PDF 147): «Se refiere a las provisiones para la operación». La misma nota acompaña los Cuadros V.17 a V.20. La Tabla 10.2 dice ahora «recursos que el IMSS aparta para su operación, según la nota del Cuadro V.19 del Informe». **[REVISAR]** La nota es casi circular; si Beth prefiere, se cambia por «con provisiones (véase el Informe del IMSS, Cuadro V.19)».

## 5. Ritmo histórico

**6.5 puntos** en la sección 10 y en el anexo. Es la resta exacta 37.685 − 31.137 = 6.548 (`e_2…/tablas/formalidad_historica.csv`; `form_hist_cambio_pts` = 6.5). Se corrigió la limitación 7 de `ANEXO_experimento2_borrador_v4.md` (decía 6.6) y se dejó constancia en `e_2…/REPORT.md`. No cambia ninguna corrida.

## 6. Verificaciones

| # | Resultado |
|---|---|
| 5.1 | Cumple. El diff de la v1 a la v1.1 tiene 72 líneas: los cambios de las secciones 1 a 4. Se movieron dos figuras (sección 4, abajo); el texto no cambió de orden |
| 5.2 | Cumple: las cifras nuevas están en `NUMBERS.md` con su cálculo. 3,647 < 8,736 < 15,087 |
| 5.3 | Cumple: «cuota fija vigente» aparece 2 veces. Una es la frase que pide 1.1.1 («la parte patronal de la cuota fija vigente»); la otra, el status quo de los 3 millones de cotizantes, igual que en la Figura 10.4 |
| 5.4 | Cumple: fila nueva en la Tabla 10.1. La base usa `pi_m: 0.0` (`e_1…/config.yaml`, escenario `base_v12`) |
| 5.5 | Cumple: sección 2 de este apartado |
| 5.6 | Cumple: 0 apariciones de «el mismo método de la sección 4.2», «la base», «[REVISAR-Beth]» y «2,631 mil millones» |
| 5.7 | Cumple: 6.5 en los dos documentos |
| 5.8 | Cumple: 0 expresiones prohibidas, 0 «el trabajador paga» y 0 «el patrón paga». Además, «Hoy el patrón paga una cuota fija» pasó a «Hoy la ley pone a cargo del patrón una cuota fija» |
| 5.9 | Cumple. Texto corrido: 10a 8,213 caracteres (4.56 cuartillas), 10b 6,906 (3.84), introducción 697. Fernández Huerta: 86.5 (10a), 88.3 (10b), 91.0 (introducción). Promedio de palabras por oración: 17.1 y 17.3. Páginas en la copia de JP: 10a ≈ 5.6 (págs. 55-60) y 10b ≈ 6.4 (págs. 60-66) |
| 5.10 | 0 tablas partidas. Huecos: ver sección 4 abajo |
| 5.11 | Cumple: hash `3f4002b8…a8cf88` antes y después. La copia conserva sus 57 comentarios y 191 cambios con control. Su nota al pie pasa a ser la 1 y la de la sección, la 2 |
| v1.0 | 8.2: 163 cifras, 152 respaldadas en `NUMBERS.md` y 11 en `config.yaml`; 0 sin respaldo. 8.5 a 8.9 cumplen |

Oraciones de más de 40 palabras: la segunda oración de la frase de apertura de Beth (46 palabras, 1.8) y la frase obligatoria 1 de 10b (42). Las dos son textos dictados y se dejaron literales **[REVISAR]**. La oración de 1.3 (41 palabras con «;») se partió en dos.

### Paginación (sección 4 de la instrucción)

- **Tablas.** Ninguna fila se parte. Las tablas se conservan completas en una página y repiten el encabezado si cruzan de página. Las celdas tienen 50 twips de margen vertical, en lugar de los 100 de JP. Los anchos de columna se eligen para que la tabla quede lo más baja posible.
- **Figuras.** Van en línea, a 5.4 in, con la leyenda y la fuente pegadas. Los títulos también quedan pegados a lo que sigue. Los esquemas 10.1 y 10.5 y las Figuras 10.2, 10.3, 10.6 y 10.7 son un poco más bajos.
- **Dos figuras flotadas.** Las Figuras 10.3 y 10.7 no cabían al final de su página y dejaban huecos de 33 % y 45 %. Ahora van después del párrafo que les sigue («Más formalidad…» y «Lo que queda para cuidados»). El texto conserva su orden y la referencia «(Figura 10.x)» no cambia **[REVISAR]**.
- **Huecos que quedan.** Se midieron como la franja blanca más alta del área de texto, en PDF de LibreOffice:
  - Copia de JP: 33 % en la pág. 56 (la Tabla 10.1 no cabe después de 10a.3 y pasa entera a la 57) y 29 % en la pág. 64. Al final de 10b queda 45 %, lo que se permite.
  - .docx de la sección sola: 36 % en la pág. 2 por la misma Tabla 10.1, y 32 % en la pág. 10.
  - Para quitar el de la Tabla 10.1 habría que dejar que se parta (con encabezado repetido) o adelantarla a 10a.2. No se hizo ninguna de las dos **[REVISAR]**.
- Word pagina distinto que LibreOffice, así que los números de página y los huecos pueden moverse un poco.

**Nota de visualización.** El documento de JP tiene activado el control de cambios (`trackRevisions` en `settings.xml`). LibreOffice pinta de dorado, con barra al margen, tanto la sección 10 como su propio Anexo M. El XML de la sección no tiene marcas de inserción (`w:ins` = 0): en Word se ve como texto normal.

## 7. Diff resumido

- **10a.1:** primera oración directa (1.11), verificada contra la definición de `A_personas_objetivo_2024`. La cuota fija se describe como «a cargo del patrón por ley» (1.7).
- **10a.2:** cuarta viñeta en incidencia legal (1.7). En el ejemplo, la parte patronal de la cuota fija con el mismo subsidio: 8,736 pesos, 8.3 % (1.1).
- **10a.3:** fila «Costo de atención por persona» en la Tabla 10.1 (1.2).
- **10a.4:**
  - frase de apertura de Beth, sin marca (1.8);
  - «Cobertura» con 41.2 % → 63.9 % (1.3.2);
  - «Asequibilidad» con 8.3 % y la oración sobre el peso de cada cuota (1.1.2);
  - leyenda de la Figura 10.2 (1.1.3);
  - «Saldo para el SEM» con la nota al pie de la Tabla 5 (1.9), los 326 mil millones con su fuente (1.10) y la nueva causa del descenso en puntos (1.2.2);
  - «Más formalidad»: «con 2.9 derechohabientes por cotizante, incluido él» y «su cuota y el Gobierno Federal» (1.6);
  - efecto sobre los formales con las dos oraciones de 1.4.
- **10a.5:** afiliación individual en tres oraciones (1.5).
- **10a.7:** 31 millones, 80 mil millones y «Con el supuesto ilustrativo…» (1.8 y 1.6).
- **Nota de derechohabientes:** conteo usado y sensibilidad con 70.7 millones (1.3).
- **10b.1:** 2.6 billones (2.4.1).
- **10b.2:** el ejemplo usa «5.55 veces la UMA de ese año» (2.4.4).
- **10b.3:** las provisiones se definen con la nota del Cuadro V.19 (2.3).
- **10b.4:**
  - leyenda de la Figura 10.6 sobre la reserva (3.2);
  - método de las personas de 65+ y cota superior de los pesos por persona (2.1);
  - cuña con la oración sobre la cuota proporcional y la advertencia del escalón (2.2);
  - leyenda de la Figura 10.8: «no están a escala» (3.4).
- **10b.7:** «con la formalización de la proyección del IMSS» en lugar de «en la base» (2.4.3).
- **Figuras:**
  - 10.2: nueva serie y rótulo (3.1);
  - 10.6: anotaciones «el ingreso del año alcanza hasta 2032 / 2034» (3.2);
  - 10.7: líneas continuas, marcador cada 5 años y mismos colores que la 10.6 (3.3);
  - 10.8: anotación «lectura por UMA; criterio pendiente con el IMSS» (3.4).

## 8. Decisiones propias [REVISAR]

1. **Rango 0.2 a 0.4 en la afiliación individual.** Depende de cuántos beneficiarios por titular se supongan: 0.80 según la ENIGH y 1.07 según el Informe.
2. **Redondeo de la frase de Beth.** Se usan 31 millones y 80 mil millones en la frase de apertura y en 10a.7. El cuerpo conserva 31.4 millones y 81 mil millones (2030). El «80 al año» se respalda con el saldo de 2054 (80); el de 2030 es 81.
3. **Oración de 2.2, más precisa que la de la instrucción:** «Con la cuota proporcional, la cuña es menor que sin ella por debajo del salario promedio y mayor por encima». En la Figura 10.8, a 5.55 UMA, las dos líneas casi coinciden (26.2 frente a 26.5 en 2030).
4. **«Cota superior» se aplica a los pesos por persona**, no al número de personas (2.1).
5. **«La cuota proporcional, antes del subsidio, pesa lo mismo en todos los niveles» (1.1.2).** Se agregó «antes del subsidio» porque con subsidio pesa 0 % en los ingresos bajos.
6. **Primera oración de 10a.1:** la del ejemplo de la instrucción sustituye las dos oraciones de la v1, que eran redundantes.
7. **Ejemplo de 10b (2.4.4).** La cuña de 2026 se calcula a 5.55 UMA de 2026, la misma posición relativa del salario promedio de diciembre de 2025. Ese nivel se rotula «salario promedio», como en la Figura 10.8.
8. **Provisiones:** se definen con la nota del Informe (sección 4 de este apartado).
9. **Paginación:** dos figuras flotadas, celdas de tabla más compactas que en JP y un hueco de 33 % a 36 % que sigue en la página de la Tabla 10.1.
10. **Oraciones de más de 40 palabras:** quedan dos, ambas dictadas.

---

# v1.2 — sensibilidad a derechohabientes, composición del déficit de GMP y aportación federal con afiliación individual (18-10-2026)

Instrucción: `20261018_BDH_N13_seccion10-esquemas-financiamiento_build_v1.2` (Beth; revisión de Beth y Cath de la v1.1). La v1.1 se conserva.

**Salidas nuevas:**
- `N13_seccion10_esquemas_financiamiento_v1.2.md` y `.docx`.
- `…_con_seccion10_v1.2.docx` (fuera de git).
- `tablas/seccion10_cifras_v1.2.csv` y `data/verificaciones_v1.2.json`.
- En el experimento 1: `outputs/tables/seccion10_v12_saldo_por_conteo.csv` y las claves `s10v12_*`. Se calculan en la función `v12()` de `src/seccion10_v11.py`.
- En el experimento 2: las semillas `GMP_V19_componentes` y `GMP_V19_vs_V24` en `NUMBERS.md`, vía `src/salidas.py`.
- Las figuras no cambian.

## 1. Cifras nuevas y su cálculo

**Saldo con tres conteos de derechohabientes.** Se escala el costo por persona por 79,178,109 / conteo, sin otra corrida, con los conteos sin redondear. Los puntos del salario se escalan igual.

| Conteo | Factor | Saldo 2030 (mdp) | Puntos 2030 | Saldo 2054 (mdp) | Puntos 2054 |
|---|---|---|---|---|---|
| 79,178,109 (Informe) | 1.000 | −80,962 | −1.31 | −80,335 | −0.58 |
| 70,690,000 (este informe) | 1.120 | −104,645 | −1.69 | −106,952 | −0.78 |
| 54,630,948 (ENIGH × CONAPO) | 1.449 | −169,586 | −2.73 | −179,936 | −1.31 |

Verificación 5.2: el saldo con 70.7 millones es igual al de la v1.1 (−104,645), y con 54.6 millones es mayor. Coincide con la referencia de Cath: el costo sube 44.9 % y el saldo ronda 170.

**Composición del déficit de GMP.** Cuadro V.19, pág. PDF 147, transcrito celda por celda; mdp de 2026:

| Concepto | 2026 | Valor presente |
|---|---|---|
| Gastos de administración | 43,581 | 1,009,572 |
| Provisiones | 123 | 151,550 |
| Total del gasto | 157,897 | 5,388,234 |
| Déficit | −68,398 | −2,637,347 |

Coincide con la tabla de referencia de la instrucción. Las notas del cuadro dicen:
- **Nota 3:** el gasto de administración «se integra a partir de la proporción del gasto que se asigna a este seguro de los siguientes rubros: i) servicios de personal y pasivos laborales del IMSS en su carácter de patrón por jubilaciones y pensiones».
- **Nota 4:** las provisiones se refieren a «provisiones para la operación».

**Aportación federal con afiliación individual, 2030.** Viene de `sensibilidades_v12.csv`, columna `pagos_GF_2030` (aportación fija más subsidio); es una salida existente y no requirió otra corrida.

| Variante | Aportación federal | Saldo | Mejora frente a la base | Parte de la mejora que viene de la aportación federal |
|---|---|---|---|---|
| Por hogar (base) | 73,769 | −80,962 | — | — |
| Individual, 0.80 beneficiarios por titular (ENIGH) | 122,748 | −11,223 | 69,739 | 70.2 % |
| Individual, 1.07 (Informe) | 108,127 | −25,843 | 55,118 | 62.3 % |

El costo no cambia entre variantes. El resto de la mejora son pagos privados mayores. La oración dictada («la mejora viene sobre todo de una mayor aportación federal») se sostiene, así que no hay marca [REVISAR-Cath] por este punto.

## 2. Diferencias entre los Cuadros V.19 y V.24

El Cuadro V.24 (pág. PDF 161) es el escenario base del ejercicio de rebalanceo y solo trae ingresos y saldo; no desglosa el gasto. Por eso la Tabla 10.2 y el párrafo nuevo dicen «según el desglose del Cuadro V.19». El modelo sigue usando el V.24.

| Año | Ingresos V.19 | Ingresos V.24 | Saldo V.19 | Saldo V.24 |
|---|---|---|---|---|
| 2026 | 89,499 | 89,499 | −68,398 | −68,398 |
| 2031 | 104,386 | 104,369 | −97,653 | −97,760 |
| 2036 | 119,537 | 119,537 | −135,137 | −134,117 |
| 2041 | 142,886 | 142,886 | −138,282 | −138,282 |
| 2046 | 169,523 | 169,522 | −157,934 | −157,934 |
| 2051 | 197,736 | 197,734 | −180,930 | −180,930 |
| 2055 | 217,063 | 217,061 | −203,895 | −203,895 |
| Valor presente | 2,750,887 | 2,750,260 | −2,637,347 | −2,631,460 |

En 2036 los ingresos coinciden pero el saldo difiere en 1,020: el gasto de ese año tampoco es igual entre cuadros. En 2031 difieren ingresos (17) y saldo (107). En valor presente el déficit del V.19 es 5,887 mayor; los dos cuadros se citan como «unos 2.6 billones».

## 3. Marcas [REVISAR-Cath] (solo en este reporte)

1. **Oración nueva de 10a.5:** «El conteo del Informe probablemente sobrestima a los derechohabientes y el de la ENIGH probablemente los subestima; el saldo verdadero está dentro de ese rango.» Es lectura de Cath. Se apoya en dos hechos: el conteo máximo del Informe da 112.4 % de la población nacional de 65 años o más, y la ENIGH registra lo que declaran los hogares. Va en el texto sin marca.
2. La afiliación individual no necesitó marca (sección 1).

## 4. Verificaciones

| # | Resultado |
|---|---|
| 5.1 | Cumple: el diff de la v1.1 a la v1.2 abarca las secciones 1 a 4 (lista abajo). |
| 5.2 | Cumple (sección 1). |
| 5.3 | Cumple: el V.19 está transcrito contra la pág. PDF 147 y el V.24 contra la 161; las diferencias se reportan. |
| 5.4 | Cumple: aportación federal registrada con su fuente (`sensibilidades_v12.csv`, salida existente). |
| 5.5 | Cumple: cada figura va después de su primera mención. La 10.3 va justo después de «Saldo para el SEM» y su nota; la 10.4, después de «Más formalidad». La 10.7 sigue flotada después de «Lo que queda para cuidados», como en la v1.1. |
| 5.6 | Cumple: 0 expresiones prohibidas y 0 «paga(r) pensiones». El párrafo nuevo de 10b.1 describe lo que contiene el déficit. |
| 5.7 | Cumple. Texto corrido: 10a 8,808 caracteres (4.89 cuartillas), 10b 7,611 (4.23). Fernández Huerta: 86.2 y 87.5. Páginas en la copia de JP: 10a ≈ 6.3 (págs. 55-61), 10b ≈ 6.7 (págs. 61-67). 0 tablas partidas. |
| 5.8 | Cumple: hash `3f4002b8…a8cf88` antes y después; la copia conserva los 57 comentarios y los cambios con control. |
| v1.0 | 8.2: 171 cifras, 160 respaldadas en `NUMBERS.md` y 11 en `config.yaml`; 0 sin respaldo. 8.9: 0 términos sin definir (provisiones se define en 10b.1). |

**Oraciones de más de 40 palabras:** las mismas dos dictadas de la v1.1 (frase de apertura de 10a, 46 palabras; frase obligatoria 1 de 10b, 42). El párrafo nuevo de 10b.1 se dictó como una oración de 52 palabras, con «según el desglose del Cuadro V.19» y la cifra en mil millones. Se partió en tres oraciones sin cambiar su contenido **[REVISAR]**.

**Paginación (LibreOffice).** Huecos mayores a un tercio de página en la copia de JP:
- **Pág. 62: 46 %.** La Tabla 10.2 creció por la nueva definición del déficit (cerca de 6 in con título y fuente) y pasa entera a la pág. 63.
- **Pág. 56: 33 %.** La Tabla 10.1, como en la v1.1.

Al volver la Figura 10.3 a su lugar, la pág. 58 queda con 27 %. En el .docx de la sección sola hay huecos de 36 % en la pág. 2 y de 50 % en la pág. 8 (Tabla 10.2). Para quitarlos habría que dejar partirse las Tablas 10.1 y 10.2 con encabezado repetido, lo que contradice la verificación 5.7 **[REVISAR]**.

## 5. Diff resumido

- **10a.4, «Saldo para el SEM»:**
  - «unos 81 mil millones en 2030» (4.3);
  - la oración de los 326 mil millones va al final del párrafo (4.1);
  - la Figura 10.3 regresa justo después del párrafo y su nota, antes de «Más formalidad» (4.2).
- **10a.5:**
  - «Cuatro supuestos» y viñeta nueva «Conteo de derechohabientes», en primer lugar (1.2.1);
  - la afiliación individual explica de dónde viene la mejora (3).
- **10a.7:** el punto del saldo agrega «; depende del conteo de derechohabientes (sección 10a.5)» (1.2.3).
- **Nota sobre derechohabientes:** se acorta (1.2.2). Dice qué conteo usa cada cálculo, que la diferencia está en conciliación y remite a 10a.5; la marca se mantiene.
- **10b.1:** párrafo nuevo sobre la composición del déficit (2.2.2).
- **Tabla 10.2:** fila «Déficit de GMP» (2.2.1).
- **10b.5:** oración sobre el déficit completo como supuesto más exigente, en la viñeta de provisiones (2.2.4).
- **10b.6:** viñeta nueva sobre la atención médica, la administración y las pensiones del personal (2.2.3).
