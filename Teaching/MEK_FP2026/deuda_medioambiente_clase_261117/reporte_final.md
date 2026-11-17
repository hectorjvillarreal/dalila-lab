# Reporte final — sesión del 17 de noviembre de 2026
«Déficits estructurales y sostenibilidad de la deuda: ¿hay salida?» · Parte 1 (deuda) y Parte 2 (clima)

## Entregables

| Archivo | Estado |
|---|---|
| `deuda_p1.tex` / `deuda_p1.pdf` (88 pp. con overlays) / `deuda_p1_handout.pdf` (23 diaps.) | Compilados con `latexmk -pdf`, sin errores ni cajas desbordadas |
| `clima_p2.tex` / `clima_p2.pdf` (89 pp. con overlays) / `clima_p2_handout.pdf` (22 diaps.) | Compilados con `latexmk -pdf`, sin errores ni cajas desbordadas |
| `deuda_p1_handout.tex`, `clima_p2_handout.tex` | Envoltorios con la opción `handout` (mismo esquema que la sesión del 10 de noviembre) |
| `esquema_deuda_p1.md`, `esquema_clima_p2.md` | Esquemas aprobados hoy |
| `fuentes/oecd_gdr2025.pdf`, `fuentes/imf_wp25170.pdf` | Fuentes principales |

Revisión visual: las páginas de los dos handouts se convirtieron a imágenes y se corrigieron textos encimados, gráficas más anchas que su columna, leyendas ilegibles y títulos que chocaban con el distintivo «opcional». No queda ningún [VERIFICAR] en pantalla. Preámbulo heredado de `politica_fiscal_p2.tex`; la opción de babel `es-noaccentedoperators` no existe en esta versión y se usa `\unaccentedoperators`, igual que en la sesión anterior. No existe `_crossrefs/style/VOZ-HJVP-001.md`; se siguió la sección de idioma de los encargos. Relectura de idioma hecha al final sobre el texto en pantalla de los dos handouts.

---

## Parte 1 · OCDE (2025), *Global Debt Report 2025*

### Mapa del informe: secciones usadas y fuera
Páginas impresas (= página del PDF − 2).

| Capítulo / sección | pp. | Uso |
|---|---|---|
| Resumen ejecutivo e infografía | 12–15 | Diaps. 2–7, 15, 17–18, 21 |
| Cap. 1 · Necesidades de financiamiento y saldo | 19–22 | Diap. 3 |
| Cap. 1 · Estrategias de emisión, letras, plazo | 23–29 | Diaps. 7, 14 |
| Cap. 1 · Costo por plazo, tasas reales, neutral | 29–33 | Diap. 5 |
| Cap. 1 · Intereses y dinámica de la deuda (recuadro 1.3) | 33–39 | Diaps. 4, 8, 15 |
| Cap. 1 · Base de inversionistas y QT (recuadro 1.4) | 40–46 | Diap. 6 |
| Cap. 1 · Liquidez y operadores (recuadro 1.5) | 46–50 | **Fuera** |
| Cap. 1 · Anexos | 56–63 | Solo p. 59 (México fuera de la descomposición) |
| Cap. 2 · Deuda corporativa | 69–107 | Solo hallazgos de p. 70 (diap. 9, opcional) |
| Cap. 3 · Emisión, moneda, plazo (recuadro 3.1) | 111–116 | Diaps. 10, 12, 13 |
| Cap. 3 · Costo y acceso (recuadro 3.2) | 116–123 | Diaps. 11, 12 |
| Cap. 3 · Calificaciones (recuadros 3.3, 3.4) | 123–127 | Diaps. 11, 16 (15b) |
| Cap. 3 · Refinanciamiento e implicaciones | 128–131 | Diaps. 13, 15 |
| Cap. 4 · Introducción, consideraciones, inversiones | 140–143 | Diap. 17 (16 del esquema) |
| Cap. 4 · Fuentes de financiamiento recientes | 148–153 | **Fuera**, salvo pp. 140 y 153 |
| Cap. 4 · Escenarios | 153–162 | Diap. 18 (17 del esquema) |
| Anexo 4.B · Bonos sostenibles | 173–175 | Diap. 19 (18 del esquema) |

### Diapositivas y respaldo
En el PDF la 15b es la diapositiva 16, así que de ahí en adelante la numeración es la del esquema + 1.

| PDF | Esquema | Título | Respaldo |
|---|---|---|---|
| 1 | 1 | Portada | — |
| 2 | 2 | Del modelo a los mercados | Resumen ejecutivo, p. 12; sesión del 10-nov |
| 3 | 3 | Más deuda, y casi toda para refinanciar | Cap. 1, pp. 18–20 |
| 4 | 4 | El costo de la deuda llega con rezago | Cap. 1, pp. 33–35, fig. 1.13; p. 13 |
| 5 | 5 | Bajan las tasas de política, no las largas | Cap. 1, pp. 30–33, 43 |
| 6 | 6 | Se retiran los bancos centrales | Cap. 1, pp. 40–45 |
| 7 | 7 | Más letras de corto plazo | Cap. 1, pp. 23–25, 29, 35 |
| 8 | 8 | La tasa real ya juega en contra (pregunta) | Cap. 1, pp. 33–37, fig. 1.14 |
| 9 | 9 | Las empresas refinanciarán más caro (opcional, 3 min) | Cap. 2, p. 70 |
| 10 | 10 | Emergentes: más endeudamiento en mercado | Cap. 3, pp. 110–112, 117 |
| 11 | 11 | Acceso desigual | Cap. 3, pp. 118–125 |
| 12 | 12 | «Pecado original» | Cap. 3, pp. 112–115, recuadro 3.2 |
| 13 | 13 | Mercado local profundo | Cap. 3, pp. 115–116, 128–131 |
| 14 | 14 | México en el mapa | CGPE 2027, pp. 41, 47, 52; Banxico SIE; GDR pp. 29, 130, 174 |
| 15 | 15 | ¿Hay salida? (pregunta) | p. 14; recuadro 1.3; pp. 129–131 |
| 16 | 15b | Sin salida ordenada (opcional, 3 min) | Recuadros 3.3 y 3.4 |
| 17 | 16 | Necesidades de inversión | Cap. 4, pp. 140–143, 155–156 |
| 18 | 17 | ¿Deuda pública o privada? | Cap. 4, pp. 140–142, 153–162 |
| 19 | 18 | Bonos temáticos | Anexo 4.B; SHCP Comunicado 071; CGPE pp. 39–40 |
| 20 | 19 | Déficits estructurales | Cap. 1, p. 19; cap. 4, pp. 154, 157 |
| 21 | 20 | Cuatro ideas | Resumen ejecutivo |
| 22 | 21 | Para el Paquete Económico 2027 (opcional, 2 min) | CGPE 2027, pp. 39, 47 |
| 23 | 22 | Puente a la segunda parte | — |

### Cifras verificadas (Parte 1)
Todas las del informe se cotejaron contra el texto (no contra figuras). Las de 2024 son estimaciones y las de 2025 proyecciones del informe, hechas en diciembre de 2024, y así se rotulan en pantalla.

- **OCDE, cap. 1**: emisión bruta 12 (2022), > 14 (2023), ≈ 16 (2024), 17 (2025) billones de dólares; refinanciamiento ≈ 13 (≈ 80 %); neta ≈ 3, doble del promedio prepandemia; deuda negociable 82/84/85 % del PIB (2023/2024/2025), pp. 18–20. Intereses 2.7 (2015–19), 3.0 (2023), 3.3 (2024) % del PIB, más que defensa; ⅓ de la deuda fija vence antes de 2027, 60 % emitido ≤ 2021 (≈ 9 billones), rendimiento < 2 % frente a 3.6 % proyectado; +0.2 pp del PIB promedio, +0.4 en FRA/ESP/GBR/USA; deuda < 1 %: 40/30/17 % y > 4 %: 5/13/20 % (2022–23/2024/2030), pp. 33–35. Tasas: −50 pb a 2 años, < −20 pb a 10 años, pendiente +60 pb (≈ 100 en 2015–19), reales de [−1, 1] a [1, 2] %, excepción Italia, pp. 30–33. Bancos centrales ≈ 16 → 12 billones, −1 en 2025; > 3 billones a absorber; 1 → 1.75 billones por punto; tenencias 29→19, 5→11, 29→34 %, pp. 40–45. Letras 49 % frente a 36 %; 8 % del saldo y 60 % del refinanciamiento; plazo 7.7 → 8.1 años; ≈ 10 % vence cada año; ≈ 45 % vence antes de 2027, pp. 13, 23–29, 35.
- **OCDE, cap. 2**: 35 / 25 / 1.6 billones; 63 % y 74 %; 12.9 y 8.4 billones; 72 % y 9 %; 151 → 784 mil millones, p. 70 y pp. 12–13.
- **OCDE, cap. 3**: saldo < 4 → ≈ 12 billones (≈ 20 → 30 % del PIB); emisión ≈ 1 → > 3; China 45 % (17 % en 2007–14); deuda 35 % (2007) → 64 % (2021), pp. 110–117. Dólares ≈ 4 → > 6 %, > 8 % en alto riesgo; emisores externos 40–50 → 29 → 42; alto riesgo 20 → 9 → 13; 10 países en riesgo muy alto o en impago; 52 mejoras y 21 bajas; ≈ 80 % de la deuda con grado de inversión y 22 % de los países, pp. 118–125. Moneda extranjera 6 % OCDE, ≈ 20 % emergentes sin China ni India, ≈ 40 % en los pequeños; < 10 % con PIB > 1 billón; cinco veces, pp. 112–115, 119. Plazos 3–5 / 5–6 / > 7 años; 4.5 billones (≈ 40 %), pp. 115–116, 128. Impagos 530 frente a 230 mil millones; Club de París 15 %, China ≈ 9 %, privados ≈ ½; canjes desde 1987, ≈ 713 millones de promedio en los 2020, recuadros 3.3–3.4.
- **OCDE, cap. 4 y anexo 4.B**: 2 billones (2024) frente a 1.2 (2019), 10 % anual; 4.1 billones al año en 2026–30; quintuplicar en 2035; 2028 / 2041 / faltante de 10 billones; 115→139, 90→131, 59→75 (2040); 1.6 billones; 17 % y 12 %; 0.5 → 4.9 billones; bonos 12 % frente a 30 %, pp. 140–162. Bonos soberanos sostenibles 170 frente a 132 mil millones; saldo 600; 64 emisores; emergentes ¼; México ≈ 3 % y desde 2020, p. 174.
- **México (SHCP, CGPE 2027, 8-sep-2026)**: deuda neta interna 84.3 %, valores a tasa fija y largo plazo 80.0 %, plazo 7.9 / 16.5 años, revisa tasa 28.4 % (2025), p. 41; SHRFSP 52.6 (2025, p. 52), 54.0 (2026e) y 55.0 (2027); costo financiero 3.7 (2026e) y 4.0 (2027) % del PIB; balance primario 0.5 % en 2027, p. 47; techos ILIF 2027 de 1,700 mil millones de pesos y 13.5 mil millones de dólares, p. 39; Bondes G, Bonos S y Taxonomía, pp. 39–40.
- **México (Banxico, SIE, cuadro CA138)**: tenencia de no residentes = SF65218 / SF65219: **10.97 % al 30-oct-2026**; 11.44 % al 31-dic-2025; 38.90 % el 26-ene-2015 (máximo de la serie descargada, 2013–2026). Cálculo propio, cotejado contra el CSV descargado del SIE el 17-nov-2026.
- **México (SHCP, Comunicado 071, 14-sep-2020)**: primer bono soberano vinculado a los ODS, 750 millones de euros, 7 años (vence en septiembre de 2027), cupón 1.350 %, rendimiento 1.603 %, demanda de 6.4 veces. Cotejado contra el PDF del comunicado.

### Quitado por no poder verificarlo (Parte 1)
Nada quedó pendiente. Lo que no tiene valor en el texto del informe (las series completas de sus figuras) no se graficó: las gráficas usan solo las cifras del texto, redondeadas y marcadas con ≈.

### Desviaciones del esquema aprobado (Parte 1)
1. Numeración: la 15b es la diapositiva 16 del PDF; de ahí en adelante, la numeración es la del esquema + 1.
2. Diap. 14: se añadió la tenencia de no residentes, ya verificada. La comparación del plazo de 7.9 años contra 8.1 de la OCDE pasó a la nota del presentador, por espacio.
3. Diap. 19 (18 del esquema): se añadieron los datos de la primera emisión ODS de 2020, ya verificados.
4. Diap. 22 (21 del esquema): además del costo financiero de 2026 (3.7 %) se pone el de 2027 (4.0 %), de la misma página del CGPE.
5. Títulos de las opcionales acortados para no chocar con el distintivo «opcional».

---

## Parte 2 · Mitra et al. (2025), IMF WP/25/170

### Diapositivas y respaldo
La página impresa coincide con la del PDF.

| # | Título | Respaldo |
|---|---|---|
| 1 | Portada | Portada y p. 2 (16 autores) |
| 2 | El clima mueve la economía que paga | Secc. 1, pp. 5–6; GDR p. 143 |
| 3 | Dos tipos de riesgo y dos respuestas | p. 5 y nota 5; recuadro 1, p. 7; pp. 9–10, 14 |
| 4 | Sector real | pp. 9–11, fig. 3; p. 22 |
| 5 | Sector fiscal | pp. 11–12, tabla 2; p. 14 |
| 6 | Sector externo | pp. 11–13, tabla 1 |
| 7 | Sector monetario (opcional, 3 min) | pp. 11, 14; anexo 2, pp. 54–55 |
| 8 | Sector financiero | pp. 11, 13–14, fig. 4; recuadro 3, pp. 26–27 |
| 9 | Corto y largo plazo (opcional, 2 min) | p. 5, nota 3; pp. 7–10; p. 35, fig. 12 |
| 10 | Impuestos verdes | pp. 13–14; tabla 5, pp. 29–30; DOF 22-12-2025 |
| 11 | Qué datos se usan | pp. 22–25, tabla 3, fig. 10 |
| 12 | Nivel o crecimiento | pp. 20–22, figs. 7–9, nota 22 |
| 13 | Familias de modelos | pp. 19–34, tablas 5–8; anexo 1 |
| 14 | Escenarios | pp. 15–18, recuadro 2, fig. 5 |
| 15 | Incertidumbre y colas | p. 5, nota 4; pp. 20–21, 27 |
| 16 | Recomendaciones por país (opcional, 3 min) | pp. 35–43 |
| 17 | El clima en la ecuación de la deuda | pp. 12, 14, 20–21, 32–33; recuadro 5, p. 38 |
| 18 | Ejercicio ilustrativo | CGPE 2027, p. 47; recuadro 5, p. 38; CENAPRED |
| 19 | México: exposición y protección | pp. 16, 28, 34; CENAPRED; SHCP; DOF; PEF 2026 |
| 20 | Adaptar cuesta; no adaptar cuesta más (pregunta) | pp. 27, 33; recuadro 6, p. 42 |
| 21 | Tres ideas | Las dos fuentes |
| 22 | Puente al 24 de noviembre | CGPE 2027, p. 51 |

### Cifras verificadas (Parte 2)
- **FMI WP/25/170**: un tercio por capital y dos tercios por actividad (p. 22); escenario base SSP2-4.5 de 2.7 °C, rango 2.1–3.5, con SSP1-2.6 y SSP3-7.0 como alternativos (p. 16); NGFS con siete escenarios en cuatro grupos (pp. 15, 18); Burke et al.: máximo a 13 °C y −23 % para 2100 (p. 21 y nota 22); Mohaddes y Raissi: hasta −24 % (p. 21); Basilea III revisado en abril de 2024, sin cargos por clima (p. 27); razones beneficio-costo de 100–900 %, costo de adaptar de 0.25–0.6 % del PIB al año, no reduce los daños más de la mitad (p. 27); prueba de estrés con dos desastres en tres años y ≥ 5 % del PIB, módulos a 30 años, supuesto de que la adaptación cancela el daño (p. 38); Costa Rica: daños de 0.5–0.7 % del PIB (1998–2018), 0.4 % adicional, +3 % de PIB, ganancia neta de 0.1 % (p. 42); horizontes de 5/20/30 años (p. 35); FSAP de México: ciclones, inundaciones de 1 en 100 años, escenarios de 2 °C y transición tardía (pp. 16, 28, 34); CPAT e IMF-ENV aplicados a México en el Artículo IV (tabla 5, p. 30).
- **IEPS al carbono 2026**: 17.7591 ¢/l en gasolinas y 21.5491 ¢/l en diésel (Acuerdo 179/2025, DOF 22-12-2025), ya verificado en la sesión del 12–13 de octubre (`iva_verdes_clase_261012/reporte_final.md`).
- **CGPE 2027**: pérdidas esperadas de 20.3 / 22.3 / 62.1 mil millones de pesos (pp. 51, 60); seguro paramétrico de 10 mil millones de pesos, el doble que en 2025 (p. 60); bonos catastróficos por 595 millones de dólares, A 225 / B 70 / C 125 / D 175, vía el BIRF (p. 60).
- **Otis**: daños y pérdidas por **84,207 millones de pesos**, cifra preliminar de CENAPRED, *Impacto socioeconómico de los principales desastres ocurridos en México. Resumen ejecutivo 2023*, tabla 1.2 (cotejado en el PDF). Plan federal de atención por **61,313 millones**, SHCP, Comunicado 73, 1-nov-2023: es un plan de apoyo, no una estimación de daños, y en pantalla se distinguen los dos.
- **FONDEN**: decreto en el DOF del 6-nov-2020 (reforma de la LFPRH y otras leyes); transitorio décimo noveno: desde el 1-ene-2021 el fideicomiso no contrae compromisos adicionales; el artículo 37 de la LFPRH reformado pide previsiones presupuestarias para atender daños por fenómenos naturales.
- **PEF 2026, anexo 20** (DOF 21-nov-2025): renglón «Fondo de Desastres Naturales (FONDEN)» por 19,430,107,735 pesos (cotejado en el PDF), más 246.7 millones para el FOPREDEN. En pantalla se dice «previsión anual en el presupuesto», no «fondo».

Los datos de Banxico, la SHCP (comunicados), CENAPRED, el DOF y el PEF los localizó un agente de apoyo en fuentes oficiales. Yo los cotejé después contra los archivos descargados: el CSV del SIE, el PDF del Comunicado 071, la tabla 1.2 de CENAPRED y el anexo 20 del PEF.

### Insumos del ejercicio ilustrativo (diap. 18)
Ecuación: $b_t = \frac{1+r}{1+g_t}\,b_{t-1} - (s_t - c_t)$, en términos reales, de 2027 a 2036.

| Insumo | Valor | Fuente |
|---|---|---|
| $b_{2026}$ | 54.0 % del PIB | CGPE 2027, p. 47 (SHRFSP 2026e) |
| $r$ | 3.4 % real | Tasa nominal implícita 7.4 % (4.0/54) menos deflactor 4.0; cálculo de la sesión del 10-nov |
| $g$ | 2.1 % real | Crecimiento nominal de 2027, 6.1 % (39,419.4/37,160.7 − 1), menos 4.0; cálculo de la sesión del 10-nov |
| $s_t$ | 0.5 (2027–29), 0.7 (2030), 0.9 (2031), 1.0 (2032 en adelante) | CGPE 2027, p. 47 |
| Choque | 2028: $g$ − 1 pp y $c$ = 0.5 % del PIB | **Ilustrativo** |
| Variante | además, $g$ − 0.1 pp cada año desde 2029 | **Ilustrativo** |

Resultados: sin choque, 54.2 (2027) → 52.8 (2036). Con el desastre, 55.4 en 2028 (+1.0 frente a 54.4) y 53.9 en 2036 (+1.1). Con la variante, 54.4 en 2036 (+1.6). La trayectoria base no reproduce la de la SHCP (55.0 en 2027) porque la ecuación no incluye ajustes stock-flujo; está dicho en la nota del presentador.

### Quitado por no poder verificarlo (Parte 2)
- **Fig. 10 (p. 23)**: las barras no tienen valores en el texto. Va como frase cualitativa («más daño como proporción del PIB y más muertes por habitante»), sin gráfica.
- **Otis como % del PIB y «0.3 % del PIB» de CENAPRED**: el resumen de CENAPRED atribuye en el texto 88,910 millones a Otis y en la tabla 84,207; uso solo la cifra de la tabla y no calculo la proporción del PIB.
- **La comparación «62.1 mil millones ≈ 0.16 % del PIB»** del esquema salió de la diap. 18 por espacio, no por falta de verificación; las pérdidas esperadas quedaron en la diap. 19.

### Desviaciones del esquema aprobado (Parte 2)
1. Diap. 6: la pregunta sobre México va como línea final y no como bloque, por espacio.
2. Diap. 11: sin gráfica (ver arriba); en su lugar, una tabla propia de fuentes y límites.
3. Diap. 18: para dimensionar el choque se usan el umbral del FMI y los daños de Otis; Costa Rica pasó a la diap. 20.
4. Diap. 19: incluye Otis, FONDEN y el PEF 2026, ya verificados.
5. Diap. 22: se añadió una tarea (ubicar en el CGPE cada término de la ecuación de la diap. 17).

---

## Archivos de Dalila consultados y estado de circulación

| Archivo | Estado |
|---|---|
| `FISCUS/económicos_paquetes/2027/2027_cgpe_criterios-generales.pdf` | Documento oficial público de la SHCP; sin README ni aviso de restricción. Citado. |
| `Teaching/MEK_FP2026/macro_dueda_rstar_261109/` (decks, esquemas, `reporte_final.md`) | Material propio del curso; numeración de diapositivas e insumos del CGPE ya verificados. Plantilla `politica_fiscal_p2.tex`. |
| `Teaching/MEK_FP2026/iva_verdes_clase_261012/reporte_final.md` | Material propio; solo las cuotas del IEPS al carbono 2026. |
| `fuentes/imf_wp25170.pdf` (puesto por Héctor) | IMF Working Paper público, con la leyenda de «research in progress». Citado como documento de trabajo. |

No se citó ningún archivo con restricción de circulación.

## Pendiente
- Confirmado en un commit local en `p4-revision-final`, **sin push**. El repositorio `dalila-lab` es público; antes de empujar, revisar `git log origin/<rama>..HEAD`.
- Las descargas de verificación (CSV del SIE, PDF de CENAPRED, comunicados, DOF, PEF) están en `fuentes/verificacion/`, con un `LEEME.md` que dice qué verifica cada una.
