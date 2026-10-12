# Reporte final — Consumo e impuestos verdes (12 y 13 de octubre de 2026)

Entregables, compilados con `latexmk -pdf`, sin errores:
`consumo_iva.pdf`, `consumo_iva_handout.pdf`, `consumo_verdes.pdf`, `consumo_verdes_handout.pdf`; fuentes `consumo_iva.tex`, `consumo_verdes.tex` (los `_handout.tex` solo pasan la opción `handout`).

## Diapositivas

**Parte 1, IVA (25):** 1 Portada · 2 Dos paradigmas · 3 México recauda muy poco. ¿Qué pasó? · 4 Objetivo de hoy · 5 IVA e impuesto a las ventas… · 6 Principio de destino · 7 Tasa cero no es lo mismo que exención · 8 Diamond y Mirrlees · 9 Cuánto cuesta gravar insumos · 10 La cascada no es, por sí sola, ineficiente · 11 Las exenciones deshacen el IVA · 12 Un IVA distorsiona en dos márgenes · 13 La regla de Ramsey · 14 La elasticidad inversa es un caso particular · 15 Atkinson y Stiglitz · 16 Redistribuir con tasas reducidas rinde poco · 17 ¿Quién paga el IVA? · 18 Cuánto se gana con un IVA · 19 IVA personalizado · 20 Brasil: tres innovaciones · 21 FMI y Barreix · 22 La oportunidad para México · 23 Riesgos y desafíos · 24 ¿Qué harían? · 25 El IVA es eficiente, pero en México se percibe injusto.

**Parte 2, impuestos verdes (15):** 1 Portada · 2 Cuando el triángulo es ganancia · 3 Derivación mínima · 4 Específico y sobre el uso · 5 Precio o cantidad · 6 Recaudar y corregir (Sandmo) · 7 ¿Doble dividendo? · 8 ¿Quién paga el impuesto verde? · 9 Internalidades · 10 IEPS a gasolinas y diésel · 11 IEPS a combustibles fósiles · 12 Impuestos verdes estatales · 13 Para discutir · 14 Ideas centrales · 15 Cierre de la sesión.

## Cifras verificadas y su fuente

| Cifra | Fuente |
|---|---|
| Diap. 3: impuestos generales al consumo (cat. 5110), % del PIB, 2021: Brasil 12.1, Chile 9.5, OCDE 7.1, Uruguay 7.0, Colombia 6.7, ALC 6.6, México 4.2 | Base OCDE *Revenue Statistics in LAC* (API SDMX, consulta del 12-10-2026) |
| Francia, 1954 | Barreix et al. (2025); fuentes secundarias |
| LIVA arts. 2-A, 9, 15, 20 | LIVA, Cámara de Diputados (última reforma DOF 12-11-2021) |
| Tasa cero 2026: 560,618 mdp = 1.50 % del PIB; alimentos 1.26 %; exenciones 78,083 mdp = 0.21 %; total 638.7 mil mdp = 1.7 % (suma propia); deciles VI–X reciben 58.5 % de la tasa cero en alimentos | SHCP, *Renuncias Recaudatorias 2026* (antes Presupuesto de Gastos Fiscales), cuadros 3.3.1–3.3.2, gráficas 28–29 |
| Región fronteriza 8 % vigente en 2026 | Decreto DOF 31-12-2025 (confirmado por fuentes secundarias) |
| Keen: 0.06 % del costo, 0.82 % de lo recaudado | FMI WP/25/165, fig. 1 |
| Auriol y Warlters 1.17/1.23; 0.72–0.9 % y 0.32–2.1 % del PIB | FMI WP/25/165, sec. 2.4 |
| Experiencias de IVA personalizado: Uruguay 2012, Ecuador 2017, Colombia 2020, Bolivia 2021, Argentina 2016 (15 %) | Barreix et al. (2022), IDB-DP-939, pp. 20–21 |
| Brasil: CBS/IBS, comité gestor, transición de 50 años (2029–2078), pago fraccionado, cashback (100 % CBS, 20 % IBS) | EC 132/2023; LC 214/2025, arts. 31–35, 113, 118 |
| IEPS gasolinas 2026: 6.7001 / 5.6579; diésel 7.3634 $/l | Acuerdo 179/2025, DOF 22-12-2025 |
| IEPS carbono 2026: gasolinas 17.7591, diésel 21.5491, combustóleo 22.9975 ¢/l; carbón mineral 47.1189 $/t | Acuerdo 179/2025, DOF 22-12-2025 |
| Precio implícito 3.9 USD/tCO₂e, 29 % de emisiones | Banco Mundial, *State and Trends of Carbon Pricing 2025* |
| IEPS bebidas 2026: 3.0818 y 1.50 $/l | LIEPS art. 2, I, G (DOF 07-11-2025) |
| CIEP: 26 entidades / 13 recaudan; 2,590.7 mdp; 3.5 %; 43.2 / 30.4 / 25.9 / 0.6 % | Nota del CIEP (PDF en la carpeta); datos de leyes de ingresos 2023 |
| Referencias de revistas (Diamond-Mirrlees, Keen 2014, Corlett-Hague, Atkinson-Stiglitz, Sah, Benedek et al., Auriol-Warlters, Weitzman, Sandmo, Bovenberg-de Mooij, Pearce, Dorband et al., Ohlendorf et al.) | Crossref y bibliografía del FMI |

## Cifras quitadas o no usadas por no poder verificarlas

- Valores del gráfico 1 de Barreix et al. tal como venían en CLAUDE.md: México 4.3, Uruguay 7.9, Brasil 12.5 y ALC 6.4 **no coinciden** con la base de la OCDE. Usé la base actual (cat. 5110) para todos. No pude abrir el PDF de la edición 2024. El código del agregado ALC (A9) no quedó resuelto al 100 %.
- «175 jurisdicciones»: no confirmado en la OCDE (403); se deja atribuido a Barreix et al., que citan a OCDE (2024).
- Esqueleto: «3.8 % del PIB», «4–6 % en AL», «0.5–2 % del PIB», «1–1.5 % del PIB», «+2–3 % del ingreso de hogares pobres» y Paraguay como caso de IVA personalizado. Paraguay no aparece en Barreix et al. (2022).
- Distribución por decil (decil I 4.8 % frente a decil X 13.1 %): está leída de etiquetas de gráfica. Solo usé el 58.5 % del texto.
- Estímulo semanal al IEPS de gasolinas en 2026 (porcentajes de octubre): solo se encontró en prensa. Quedó solo lo de 2022 («en varias semanas llegó a 100 %»), sin fecha DOF exacta.
- Participación de deciles altos en el subsidio a gasolinas (Fundar 62 %, SHCP 2020): la metodología o el original no se verificaron. Nunca entró a las diapositivas; también se quitó de la diap. 10 la frase cualitativa sobre la concentración del subsidio en los hogares de mayor ingreso.
- Cuotas 2025 de gasolinas (solo fuente secundaria). «El gas natural no paga el IEPS al carbono» (quitado).
- Costo social del carbono de la EPA (190 USD/t, 2 %): confirmado solo por fuentes secundarias. Quitado de la diap. 11 junto con «unas 50 veces menos»; en su lugar va una pregunta a la clase sin cifra.

## Desviaciones del esquema

- Babel: la opción `es-noaccentedoperators` no existe en esta versión. Se usa `\unaccentedoperators`, igual que en la plantilla.
- Diap. 3: la gráfica usa la cat. 5110 de la OCDE, no los valores leídos del blog. El título del eje y la nota lo dicen.
- Diap. 19: la cita correcta del BID es Barreix, Bès, Fonseca, Fonteñez, Morán, Pineda y Roca (2022), «El IVA personalizado revisado», IDB-DP-939. «Revisando el IVA personalizado» es el título de un CIATBlog de 2022.
- Diap. 20: 26.5 % aparece como tasa conjunta estimada, no fijada en ley (la fija el Senado; LC 214, art. 475).
- Diap. 22: la ganancia potencial se expresa como renuncia recaudatoria (1.7 % del PIB). Lleva la advertencia de que no todo se recaudaría.
- Parte 2, diap. 8: no se encontró una cifra mexicana verificada, así que va solo la evidencia internacional (Dorband et al., 2019; Ohlendorf et al., 2021).
- Parte 2, diap. 15: el temario del parcial solo dice «de teoría». Agregué que entra la parte de tasa uniforme (CLAUDE.md la marca como material del parcial).
- Sandmo (diap. 6) va en forma verbal (componente Ramsey + componente pigouviano), sin fórmula explícita.
