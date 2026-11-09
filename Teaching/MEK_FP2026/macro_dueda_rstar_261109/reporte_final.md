# Reporte final — sesión «La perspectiva macro» (9 de noviembre de 2026)

Dos presentaciones Beamer 16:9 compiladas con `latexmk -pdf`, cada una con su versión para repartir (`\PassOptionsToClass{handout}{beamer}` + `\input`, como en las sesiones anteriores):

| Archivo | Diapositivas | Páginas (con overlays) |
|---|---|---|
| `politica_fiscal_p1.pdf` / `politica_fiscal_p1_handout.pdf` | 28 (2 opcionales) | 92 / 28 |
| `politica_fiscal_p2.pdf` / `politica_fiscal_p2_handout.pdf` | 18 (17 + 1 opcional) | 60 / 18 |

Plantilla: preámbulo, tema, colores, estilo de gráficas, `\fuente`, `\opcional` y `alertblock{Pregunta}` heredados de `nta_p3_cepal.tex`. Único cambio: márgenes laterales de 0.7 cm (la plantilla usa el valor por omisión de 1 cm) para ganar una línea por diapositiva. Pie: «Política fiscal · Parte 1» y «Política fiscal · Parte 2». Nada por debajo de `\small`; las etiquetas de ejes de algunas gráficas van en `\footnotesize`, como en la plantilla.

Esquemas aprobados: `esquema_politica_fiscal_p1.md` y `esquema_politica_fiscal_p2.md` (aprobación: «Aprobado, aplica tus recomendaciones y arranca la fase 2»).

---

## 1. Mapa del capítulo 4 (Bénassy-Quéré et al., 2019, 2.ª ed., pp. 148–236)

| Sección | Páginas | Uso en la Parte 1 |
|---|---|---|
| Apertura | 148–149 | Diap. 2 (tamaño del Estado) |
| 4.1.1 What is it all about? | 150–165 | Diaps. 9–14, 16, 20, 26 (estabilizadores, balance estructural, deuda, recuadros 4.2–4.5) |
| 4.1.2 Lessons from history | 166–179 | Diaps. 17–18 (pp. 174–178: salidas de la deuda, solvencia/liquidez/sostenibilidad, recuadro 4.9, fig. 4.11). Pp. 166–173 solo para el mapa |
| 4.2.1 Demand-side effects | 179–192 | Diaps. 3–8, 21–25, 27 (recuadros 4.10–4.12, fig. 4.13, hallazgos 1–7) |
| 4.2.2 Public debt sustainability | 192–199 | Diaps. 12, 15, 19, 25 (recuadros 4.13–4.14, fig. 4.15) |
| 4.2.3 Open-economy dimensions | 200–205 | **Fuera** (Mundell-Fleming sacrificado por tiempo, decisión de Héctor) |
| 4.3.1 Fiscal rules and institutions | 206–215 | Fuera; candidata para el 17 de noviembre |
| 4.3.2 Sovereign debt crises resolution | 214–219 | Fuera |
| 4.3.3 Fiscal policy in the euro area | 216–227 | Fuera |
| 4.3.4 Conclusion | 228 | Diap. 28 |
| Notas y referencias | 228–236 | Verificación de citas |

Páginas leídas completas: 148–149, 154–165, 174–199, 228–231. El PDF del capítulo es fotográfico sin capa de texto (`benassy_quere_cap4_fiscal_261109/`); se leyó por imágenes. Las pp. 200–227 solo se hojearon para el mapa.

## 2. Versión del artículo usada (Parte 2)

Bolhuis, Koosakul y Shenai, «Fiscal R-Star: Fiscal-Monetary Tensions and Implications for Policy», **versión fechada marzo de 2025 presentada en la conferencia anual del Reserve Bank of Australia (Sídney, 4–5 de septiembre de 2025), 48 pp.**, con el comentario de Rachael McCririck (Tesoro de Australia, 4 pp.). Ambos en `fuentes/`. El WP 24/174 del FMI (agosto de 2024) no estaba en Dalila y `imf.org` niega la descarga a clientes automatizados («Access Denied»); no se cotejaron las dos versiones y **no se cita ninguna cifra del WP original**. La portada dice «(2024)» como pide el encargo y aclara al pie la versión usada. Todas las páginas citadas son de la versión del RBA.

## 3. Lista de diapositivas con su respaldo

### Parte 1

| # | Título corto | Respaldo |
|---|---|---|
| 1 | Portada | — |
| 2 | Por qué volvió al centro | pp. 148–149, 228; CGPE 2027 pp. 6, 55 |
| 3 | Qué es un multiplicador | p. 179; recuadro 4.12 (p. 189); p. 191 |
| 4 | Keynesiano y fugas (derivación) | recuadro 4.10, pp. 180–181 |
| 5 | Banco central responde (IS-LM redibujado) | pp. 181–183, fig. 4.13 |
| 6 | Evidencia (rangos de la fig. 4.14) | pp. 188–192, hallazgos 1 y 3, notas 22–23 |
| 7 | Depende de las condiciones | pp. 190–191, hallazgos 2, 4, 6, 7 |
| 8 | ¿Y en México? (pregunta) | lectura propia de pp. 180–181, 190–191 |
| 9 | Del déficit a la deuda | pp. 157–160, ecs. (4.1)–(4.2); CGPE p. 52 |
| 10 | Ecuación de la deuda (derivación) | recuadro 4.5, p. 164 |
| 11 | Balance primario estabilizador, tabla México | recuadro 4.5 (B4.5.6); p. 163; CGPE pp. 6, 47, 68 |
| 12 | Cuando r < g | p. 164; recuadro 4.13; p. 165 |
| 13 | Lo que la ecuación no ve: México 2027 (gráfica) | recuadro 4.5; p. 165; CGPE pp. 25, 47, 52, 55, 68 |
| 14 | Pasivos implícitos y trayectoria SHRFSP (gráfica, pregunta) | p. 165, tabla 4.1; CGPE pp. 47, 52, 55 |
| 15 | [opcional] Restricción intertemporal | recuadro 4.13, pp. 194–195; p. 193 |
| 16 | Quién compra deuda | recuadro 4.4, p. 161; p. 160; CGPE pp. 41, 47, 52 |
| 17 | Cinco salidas; solvencia/liquidez/sostenibilidad | pp. 174–175, fig. 4.10 |
| 18 | Prima de riesgo (derivación) | recuadro 4.9, p. 177; p. 178, fig. 4.11 |
| 19 | Dos equilibrios y espacio fiscal (fig. 4.15 redibujada) | pp. 196–197 |
| 20 | Pecado original y deuda en pesos | p. 161; p. 165 (nota 8); p. 183; CGPE pp. 41, 47 |
| 21 | Argumento ricardiano (derivación en dos periodos) | recuadro 4.11, pp. 184–185 |
| 22 | Supuestos | p. 186 |
| 23 | Por qué falla; enlace NTA | pp. 186–187 |
| 24 | [opcional] Evidencia (pregunta) | p. 186, nota 19 |
| 25 | Cuándo funciona | pp. 187, 192; recuadro 4.14, p. 199 |
| 26 | Estabilizadores frente a discreción | pp. 154–158, recuadros 4.2–4.3, figs. 4.3–4.4 |
| 27 | La micro dentro de la macro | pp. 186–187; sesiones anteriores |
| 28 | Ideas y puente | p. 228; recuadro 4.5 |

### Parte 2

| # | Título corto | Respaldo (versión RBA) |
|---|---|---|
| 1 | Portada | — |
| 2 | La misma ecuación, otra pregunta | pp. 3–4; ec. (1) p. 8; ec. (4) p. 10 |
| 3 | r-star monetaria | p. 3; ec. (10) p. 13; Banxico IT abr–jun 2024, Recuadro 7 |
| 4 | Fiscal r-star: definición (derivación) | ecs. (1), (6), pp. 8, 12; Anexo A.1 |
| 5 | Cómo se lee | ec. (7), p. 12 |
| 6 | Brecha fiscal-monetaria (fig. 3 redibujada) | pp. 15–16 |
| 7 | Activa y pasiva (fig. 2 / Annex Table 1 redibujadas) | ecs. (3)–(5), pp. 8–11; p. 46 |
| 8 | Cuatro desenlaces (pregunta) | p. 4; p. 14 |
| 9 | Descomposición formal, ec. (11) | pp. 13–14, nota 31 |
| 10 | Dominancia fiscal y represión | pp. 33–35, figs. 13–14, nota 44 |
| 10b | [opcional] Estáticas comparativas (fig. 4 redibujada) | pp. 16–18 |
| 11 | 140 años; proyecciones locales; WEO | pp. 19–31 |
| 12 | Límites | p. 19, p. 31, notas 29, 40; McCririck pp. 2, 4 |
| 13 | Cálculo para México (tabla) | ec. (6); CGPE pp. 6, 47, 68 |
| 14 | Comparación (gráfica) | ecs. (6)–(7); Banxico 2024; CGPE pp. 47, 55, 68 |
| 15 | Economía emergente (pregunta) | pp. 33–35; Anexo A.3 p. 47; nota 31 |
| 16 | Tres ideas | síntesis |
| 17 | Puente al 17 de noviembre; tarea | Anexo A.4 p. 48; cap. 4 pp. 206–215 |

## 4. Referencias externas verificadas

En la bibliografía del capítulo (pp. 230–231): Barro (1974), *JPE* 81(6), 1095–1117; Blanchard (1985), *JPE* 93(2), 223–247; Blanchard y Perotti (2002), *QJE* 117(4), 1329–1368; Bohn (1998), *QJE* 113(3), 949–963; Auerbach y Gorodnichenko (2012; 2017); Alesina et al. (2017); Batini et al. (2014). En el texto del capítulo: Mineshima et al. (2014), Coenen et al. (2012), Ghosh et al. (2011), Zheng (2014), Eichengreen, Hausmann y Panizza (2005, nota 8), de Mello et al. (2004, nota 19), Mankiw (2000), Greenspan y Kennedy (2007), Sutherland (1997), Mourre et al. (2013).

En las referencias del artículo (pp. 36–42 de la versión RBA): Leeper (1991), *JME* 27; Bohn (1998); Mauro et al. (2015); Laubach y Williams (2003); Reinhart y Sbrancia (2015), IMF WP 15/7; Romero (2013); Platzer et al. (2023); Blanchard (2019), *AER* 109(4).

**No están en el capítulo y van solo en notas del presentador** (decisión aplicada según el esquema): Ilzetzki, Mendoza y Végh (2013); Blanchard (2019) [sí en el artículo]; Calvo (1988); Ramey (2019) y Blanchard y Leigh (2013) no se usan. Gavin y Perotti (1997) y Frankel, Végh y Vuletin (2013) se mencionan en una nota como «no verificadas hoy».

## 5. Cifras verificadas y su fuente

Todas las cifras en pantalla tienen fuente al pie. Las de México salen del PDF del CGPE 2027 que está en Dalila (`FISCUS/económicos_paquetes/2027/2027_cgpe_criterios-generales.pdf`, SHCP, 8 de septiembre de 2026), páginas del PDF: cuadro resumen p. 6; indicadores de deuda del Gobierno Federal p. 41; RFSP y SHRFSP 2026–2032 p. 47; RFSP y SHRFSP 2020–2026 p. 52; ingresos y gasto 2020–2026 p. 55; resumen p. 61; marco macroeconómico 2025–2032 p. 68. Detalle en la tabla de insumos de `esquema_politica_fiscal_p2.md`.

Cálculos propios, rotulados así en pantalla: tasa nominal implícita de la deuda 2027 = 4.0/54 = 7.4 %; real = 7.4 − 4.0 (deflactor) = 3.4 %; crecimiento nominal 2027 = 39 419.4/37 160.7 − 1 = 6.1 %; descomposición de la diapositiva 13 (0.72 − 0.50 = 0.22 contra 1.0 de la SHCP; residuo 0.78); $s^*$ por escenario (1.0 / 0.75 / 0.5); fiscal r-star por escenario (tabla de la diap. 13 de la Parte 2); externo = 11.4/54.0 = 21 %.

Banxico: tasa neutral real 2.7 % (1.8–3.6), nominal 5.7 (4.8–6.6), Recuadro 7 del Informe Trimestral abril–junio 2024, verificado en el PDF (`fuentes/`). El índice de recuadros de Banxico hasta abril–junio 2026 no registra actualización posterior.

Del capítulo: 2 % → 40 % del PIB en EE. UU. y 45–55 % en Europa (p. 149); Japón 234/126 % (p. 159); Canadá 39–67 % (p. 160); 68/22.5/8.4 % (p. 160); 3 % = 5 % × 60 % (p. 163); elasticidad 0.5, 0.43, 0.65 (recuadro 4.2); Irlanda 2007 (fig. 4.4); diferenciales de 8 y 5 puntos (p. 179); 11 de 87 países y 3.5 % del FMI (p. 196); 0.9–1.3 (p. 190); 0 y 1.5 (p. 191); un tercio a medio punto (nota 19); 3 % del consumo (p. 186); 1.5 y 1.7 en el límite inferior (notas 22). Del artículo: $\rho_1$ = 0.031, −0.015, −0.035 y $\rho_2$ = 1.37, 0.49, 0.67 (Annex Table 1, p. 46); 1.5 pp, 2 %, 0.6 pp, 0.7–1.8 pp (pp. 25–26); 4 % → 1 % (p. 30).

**Lecturas aproximadas, declaradas como tales en el pie**: los rangos de la gráfica de la diapositiva 6 de la Parte 1 se leyeron de la fig. 4.14 del libro (no hay tabla); la gráfica esquemática de la fig. 4.15 y el diagrama de fases no están a escala.

## 6. Lo que se quitó por no poder verificarlo

- **Tenencia de valores gubernamentales en poder de no residentes** (≈ 39 % en enero de 2015, ≈ 11 % en 2026): solo la encontré en prensa especializada; el SIE de Banxico no se pudo consultar desde aquí. Se sustituyó, como recomendaba el esquema, por la composición interna/externa del SHRFSP (verificada en el CGPE). La cifra queda en la nota del presentador de la diapositiva 16 como «no verificada».
- **Prociclicidad de la política fiscal en América Latina**: no está en el capítulo; la frase quedó en nota del presentador con las referencias habituales sin verificar.
- **Multiplicadores de Ilzetzki, Mendoza y Végh (2013)** para emergentes: no citados en el capítulo; solo en notas.
- **Serie histórica de la fig. 5 del artículo (140 años)**: no se publican los datos; no se redibujó. Se sustituyó por la tabla de resultados de las proyecciones locales y por la gráfica de la función de reacción (fig. 2), que sí tiene cifras en el anexo.

## 7. Archivos de Dalila consultados y su circulación

| Archivo | Uso | Circulación |
|---|---|---|
| `Teaching/MEK_FP2026/benassy_quere_cap4_fiscal_261109/benassy_quere_cap4_fiscal_policy.pdf` | fuente principal P1 | ejemplar comprado, «No redistribuir»; se cita el libro, no el archivo |
| `FISCUS/económicos_paquetes/2027/2027_cgpe_criterios-generales.pdf` | cifras de México | documento público de la SHCP; se cita la SHCP |
| `Teaching/MEK_FP2026/demografia_nta_envejecimiento_261102/nta_p3_cepal.tex` | plantilla | propia |
| `…/20261102_TEACHING_briefing_debb_voice-adoption.md` y `…/20261102_RULING_debb_voice-provenance-circulation.md` | guía de voz (no existe `_crossrefs/style/VOZ-HJVP-001.md`) | internos; no se citan |
| Búsqueda de «dominancia fiscal» en `GrandPlan/`, `Missions/`, `_crossrefs/` | material del profesor | solo notas internas de DFD, Aurora y el corpus de desigualdad; **no se cita ninguno**; no encontré material público del profesor sobre dominancia fiscal en México |

Fuentes descargadas hoy, con procedencia, en `fuentes/LEEME.md`.

## 8. Desviaciones respecto a los esquemas aprobados

- Parte 1, diap. 4: la derivación pasó de 5 a 4 líneas (impuestos e importaciones en una sola) para que cupiera; la nota del presentador conserva el paso intermedio.
- Parte 1, diap. 28: se marcó también como opcional la 24, como proponía el esquema, para completar los 10 minutos de holgura (15 + 24 ≈ 8 min).
- Parte 2, diap. 10b (estáticas comparativas): se mantiene como opcional de 7 min entre la 10 y la 11, según el esquema.
- Parte 2, diap. 11: sin gráfica esquemática de 140 años (recomendación 3 del esquema, aplicada); la gráfica del bloque de evidencia es la de la función de reacción en la diap. 7.
- Títulos de varias diapositivas se acortaron para caber en una línea; el contenido no cambió.
- Margen lateral de 0.7 cm (la plantilla no lo fijaba).

## 9. Revisión visual y de idioma

- Las 46 páginas de los dos handouts se convirtieron a imagen; se corrigieron: etiquetas faltantes en la gráfica de barras (diap. 13 P1), solapamientos de pie y bloque (diaps. 10, 14, 23 P1), ejes y etiquetas del diagrama de fases y de la gráfica de barras (diaps. 6, 7 P2), etiquetas de la gráfica de comparación (diap. 14 P2). Desbordes residuales reportados por LaTeX: ≤ 6 pt (menos de medio renglón), sin texto fuera de la página.
- Lectura corrida para el idioma: oraciones completas, trato de «ustedes», sin «asumir», «rol», «impactar» ni las muletillas de la lista. «Impacto» aparece solo en el término «multiplicador de impacto».

## 10. Pendientes

- Verificar en vivo, si se quiere mostrar, la tenencia extranjera de valores gubernamentales (Banxico, SIE).
- Si Héctor tiene el WP 24/174 del FMI, cotejar las páginas citadas; la numeración de ecuaciones coincide en ambas versiones según el resumen de SUERF, pero no lo comprobé.
- La carpeta no está en git todavía; no se hizo commit porque no se pidió.
