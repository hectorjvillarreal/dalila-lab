# Esquema — Clase 3: Incidencia, distorsiones y pérdida de bienestar

Finanzas Públicas · Maestría en Economía Aplicada · 26 de septiembre de 2026
Sesión de **150 minutos, en línea**: la densidad matemática debe funcionar en pantalla compartida.

Fuentes:
- **Salanié**, *The Economics of Taxation*: cap. 1 (pp. 15–34) y cap. 2 (pp. 35–58).
- **Gruber**, *Public Finance and Public Policy*: cap. 19, «Tax Incidence» (pp. 557–588), y cap. 20, «Tax Inefficiencies and Their Implications for Optimal Taxation» (pp. 589 y siguientes).

Decisiones acordadas:
- Término único: **carga excesiva** (no «pérdida de peso muerto» ni «pérdida irrecuperable de eficiencia»).
- Notación de Salanié: elasticidades en valor absoluto $e_D, e_S > 0$; impuesto ad valorem $t$ e impuesto específico $\tau$ (diap. 24–25 y 35–37); en equilibrio general, notación de sombreros ($\hat z = dz/z$).
- Aplicación mexicana: IEPS a bebidas azucaradas; los combustibles se anuncian para el 13 de octubre. Cuotas del IEPS y estudios de traslado verificados el 2026-09-25; solo la cuota de 2025 sigue con [VERIFICAR].
- Mercado de trabajo: la reforma de pensiones de 2020 abre la sesión (cifras verificadas en el DOF); teoría (diap. 12), evidencia (diap. 13) e informalidad (diap. 14) en diapositivas separadas. Referencias verificadas el 2026-09-25.
- Derivaciones propias que se conservan: carga excesiva marginal por peso recaudado (diap. 34, versión de equilibrio parcial de Browning, 1976) y medición con la función de gasto (diap. 31, Salanié y Varian).
- Revisión aplicada: `revision_esquema.md` (2026-09-25).

Total: 39 diapositivas en el cuerpo, más 2 de apéndice.

---

## I. Motivación (3) · 10 min

1. **Portada.** Título de la sesión, curso, fecha. — *propia*
2. **La ley sube la cuota patronal; ¿quién la pagará?** Reforma de pensiones de 2020: la cuota patronal de cesantía en edad avanzada y vejez pasa de una tasa única de 3.150 % a una tabla por salario que va de 3.150 % (un salario mínimo) a 11.875 % (desde 4.01 UMA), de forma gradual entre 2023 y 2030; la cuota obrera se queda en 1.125 %. ¿Recaerá en las empresas, en los salarios o en el empleo formal? La tesis del papel matamoscas (flypaper): el impuesto se queda donde cae. — *DOF, 16-12-2020 (art. 168, fr. II, y transitorio segundo, LSS); Salanié (cap. 1, intro)*
3. **Tres preguntas para hoy.** ¿Quién carga con el impuesto? ¿Cuánto se pierde además de lo recaudado? ¿De qué depende? Mapa de la sesión. — *propia*

## II. Incidencia en equilibrio parcial (12) · 45 min

4. **La incidencia legal no es la incidencia económica.** Definiciones: incidencia legal (quién entera el impuesto) e incidencia económica (cómo cambian los recursos de cada agente). — *Gruber (19.1, regla 1); Salanié (1.1)*
5. **El impuesto abre una cuña entre dos precios.** Precio al consumidor $q = p(1+t)$ y precio al productor $p$. Gráfica de oferta y demanda con la cuña fiscal. — *Salanié (1.1.2); gráfica propia*
6. **Da lo mismo de qué lado se cobre.** Dos paneles: el impuesto desplaza la oferta o la demanda y los precios $q$, $p$ y la cantidad son iguales en ambos casos. Una línea sobre cuándo falla: en Grecia, la cuota patronal adicional la absorbieron los patrones y la obrera, los trabajadores: el lado legal sí importó (Saez, Matsaganis y Tsakloglou, 2012, *QJE*). — *Gruber (19.1, regla 2); Salanié (1.1.1)*
7. **Derivación: equilibrio con impuesto.** $D(p(1+t)) = S(p)$; diferenciar alrededor de $t=0$; despejar $dp$. — *Salanié (1.1.1)*
8. **El lado menos elástico carga con el impuesto.** $\partial \log q/\partial t = e_S/(e_S+e_D)$ y $\partial \log p/\partial t = -e_D/(e_S+e_D)$. Lectura de la fórmula. — *Salanié (1.1.1–1.1.2)*
9. **Lectura sobre la gráfica.** Dos paneles (demanda inelástica y elástica) con el mismo impuesto; el rectángulo de recaudación se divide entre consumidores y productores según las elasticidades. Pregunta a la clase (último overlay): «¿Quién carga con un impuesto a los cigarros? ¿Y a los boletos de avión de temporada baja?» — *Gruber (19.1); gráfica propia*
10. **Casos extremos.** $e_D = 0$ o $e_S = \infty$: traslado (pass-through) completo al consumidor. $e_S = 0$: el productor carga con todo. Caso de la tierra: capitalización fiscal. — *Salanié (1.1.2 y final del cap. 1); Gruber (19.1)*
11. **Cuanto más elásticos los dos lados, más cae la cantidad.** $\partial \log x/\partial t = -e_S e_D/(e_S+e_D)$, la mitad de la media armónica de las dos elasticidades. Adelanto: esta caída es la que genera la carga excesiva. — *Salanié (1.1.1)*
12. **La teoría: con oferta de trabajo inelástica, la cuota recae sobre el salario.** El salario neto absorbe casi toda la cuota. Con salario mínimo obligatorio, el salario neto no baja y la cuota se vuelve desempleo. Gráfica de dos paneles. — *Salanié (1.1.1, figs. 1.1–1.2); Gruber (19.2, mercados de factores)*
13. **En la práctica, la carga no siempre llega al salario.** (i) Suecia: la rebaja de la cuota patronal a jóvenes no movió su salario neto y subió su empleo; las empresas repartieron la ganancia entre toda su plantilla (Saez, Schoefer y Seim, 2019, *AER*). (ii) Vínculo contribución-beneficio: si el trabajador valora lo que compra la cuota, esa parte no es impuesto; la oferta se desplaza y el salario absorbe la cuota sin pérdida de empleo (Summers, 1989, *AER P&P* 79(2): 177–183). En la reforma de 2020, la cuota patronal va a la subcuenta de retiro, cesantía en edad avanzada y vejez de la cuenta individual (AFORE). (iii) Evidencia mexicana del vínculo: la reforma de 1997 ligó la pensión al salario declarado y redujo la subdeclaración ante el IMSS (Kumler, Verhoogen y Frías, 2020, *REStat*). — *literatura citada*
14. **La informalidad vuelve más elástica la oferta de trabajo formal.** Dos márgenes: empresas que no se registran y empresas formales que contratan sin registro (Ulyssea, 2018, *AER*; 2020, *Annual Review of Economics*). El Seguro Popular redujo el registro en el IMSS en empresas de hasta 50 trabajadores (Bosch y Campos-Vázquez, 2014, *AEJ: Policy*). Respuesta a la diapositiva 2, en tres líneas: la teoría (salario), la evidencia (la carga se queda donde cae) y la informalidad (el ajuste se va al empleo formal); el vínculo contribución-beneficio decide entre ellas. — *literatura citada; propia*
15. **Con poder de mercado, el traslado puede superar 100 %.** Fórmula de Lerner con impuesto; demanda lineal frente a elasticidad constante. Ad valorem frente a impuesto específico: con monopolio ya no son equivalentes. — *Salanié (1.1.2, caso monopolio); Gruber (19.2, competencia imperfecta)*

## III. Incidencia en equilibrio general (7) · 25 min

16. **Solo las personas cargan con impuestos.** Un impuesto municipal a comidas en restaurantes (municipio hipotético, sin cifras) con demanda perfectamente elástica: el restaurante «paga», pero la carga pasa a trabajadores, dueños de capital y dueños de la tierra. Analogía de las dos carreteras con peaje. — *Gruber (19.3); Salanié (1.2.3)*
17. **Modelo de Harberger: supuestos.** Dos bienes $X, Y$; dos factores $K, L$ con oferta fija y movilidad perfecta entre sectores; rendimientos constantes; preferencias idénticas y homotéticas. — *Salanié (1.2.1)*
18. **Equilibrio con impuestos.** Precios iguales a costos unitarios, mercados de factores y de bienes; seis ecuaciones, seis incógnitas, Ley de Walras. Impuestos $t_{KX}$ y $t_X$. — *Salanié (1.2.1–1.2.2)*
19. **Tres equivalencias.** (i) El rendimiento neto de cada factor se iguala entre sectores. (ii) Gravar $K$ y $L$ en $X$ a la misma tasa equivale a gravar el bien $X$. (iii) Un impuesto uniforme a un factor lo carga ese factor. Diagrama propio de equivalencias. — *Salanié (1.2.3)*
20. **Dos canales: sustitución de factores y efecto volumen.** En el cuerpo, solo planteamiento y resultado: $D(\hat w - \hat r) = (\sigma_X a_X - e_D \lambda^* s_{KX})\,dt_{KX} - e_D \lambda^* dt_X$, con $\lambda^*$ (intensidad relativa de capital), $\sigma_X, \sigma_Y$, $e_D$. El álgebra de sombreros completa va al apéndice A2. — *Salanié (1.2.4)*
21. **Gravar el capital en un sector puede recaer sobre todo el capital.** Casos: $X$ intensivo en capital; $e_D = 0$; el caso contraintuitivo en que el capital gana. Con $\sigma_X = \sigma_Y = e_D = 1$ (producción y preferencias Cobb-Douglas), los capitalistas cargan con todo el impuesto. Diagrama de flujo de los dos canales. Pregunta a la clase (último overlay): «Si $X$ usa mucho trabajo, ¿puede ganar el capital con el impuesto?» — *Salanié (1.2.4)*
22. **Un impuesto a un bien recae sobre el factor que ese bien usa con intensidad.** Solo opera el efecto volumen. Límites del modelo: sin efectos ingreso, economía cerrada (el capital móvil entre países carga menos), análisis estático (ciclo de vida). — *Salanié (1.2.4–1.2.5)*

*Descanso (10 min): nota del presentador al final de la diapositiva 22 o transición mínima fuera del conteo.*

## IV. Distorsiones y carga excesiva (12) · 45 min

23. **De quién paga a cuánto se pierde.** La incidencia reparte la carga; la carga excesiva mide lo que se pierde por encima de lo recaudado. Con impuesto, consumidores y productores ven precios distintos y la TMS deja de igualar la TMT. — *Salanié (cap. 2, intro); Gruber (20.1)*
24. **Un ejemplo con dos bienes.** $U = C_1 C_2$, tecnología $X_2 = X_1/c$, impuesto específico $\tau$ al bien 2 que se devuelve de suma fija. La TMS es $1/(c+\tau)$; la TMT sigue en $1/c$. — *Salanié (cap. 2, intro)*
25. **Devolver lo recaudado no elimina la pérdida.** $U^* - U(\tau) = \tau^2/[4c(2c+\tau)^2]$: pérdida de segundo orden en $\tau$. — *Salanié (cap. 2, intro)*
26. **El triángulo de Harberger.** Gráfica: pérdida de excedente del consumidor, pérdida de excedente del productor, recaudación; lo que sobra es el triángulo. — *Gruber (fig. 20-1); Salanié (fig. 2.3); gráfica propia*
27. **Derivación: carga excesiva $\approx \tfrac12\, t^2\, \varepsilon\, p x$.** Área del triángulo: $\tfrac12$ × cuña ($t\,p$) × caída de la cantidad; se sustituye la caída con la fórmula de la diapositiva 11; $\varepsilon = e_S e_D/(e_S+e_D)$. — *Salanié (2.2); Gruber (20.1 y apéndice)*
28. **La carga excesiva crece con el cuadrado de la tasa.** Razón carga excesiva/recaudación proporcional a $t$. Ejemplo de Salanié: IVA de 20 % con elasticidades unitarias da 5 % de lo recaudado; con oferta perfectamente elástica, 10 %. — *Salanié (2.2)*
29. **Más elasticidad, más carga excesiva.** Dos paneles (demanda inelástica y elástica) con el mismo impuesto y triángulos de tamaño distinto; contraste con la diapositiva 9: lo que protege de la incidencia genera carga excesiva. Pregunta a la clase (último overlay): «¿Qué bien preferirían gravar para minimizar la carga excesiva?» — *Gruber (fig. 20-2); gráfica propia*
30. **La carga excesiva depende solo del efecto sustitución.** Una transferencia de suma fija produce efecto ingreso sin distorsión; por eso la medida correcta usa la demanda compensada (hicksiana). — *Salanié (2.3); Gruber (20.1, apéndice)*
31. **Medir con la función de gasto.** Con oferta perfectamente elástica, carga excesiva $= -VE - T$, con $VE = e(p^0, V(p^1,R)) - R$. Por el lema de Shephard, $-VE$ es el área bajo la demanda hicksiana de la utilidad final; al restar lo recaudado queda un triángulo bajo la hicksiana. Gráfica: demanda marshalliana y hicksiana. La comparación con variación compensada y con el excedente de Dupuit-Marshall va al apéndice A1. — *Salanié (2.2); Varian (cap. 10); gráfica propia*
32. **Que la cantidad no cambie no significa que no haya carga excesiva.** Impuesto al ingreso laboral con Cobb-Douglas: efectos ingreso y sustitución se cancelan, la oferta de trabajo no se mueve, pero la elasticidad compensada es positiva y hay pérdida. Descomposición de Slutsky en una línea. — *Salanié (2.1.1 y 2.3)*
33. **La carga excesiva marginal es de primer orden.** Si ya existe $t>0$, subir la tasa en $dt$ agrega un trapecio de área $\approx t\,p\,dx$. Gráfica del trapecio. — *Salanié (fig. 2.4); Gruber (fig. 20-3); gráfica propia*
34. **Cada peso adicional cuesta más de un peso.** Con oferta perfectamente elástica y $p$ fijo: $R = t\,p\,x$, $dR = p\,x\,dt + t\,p\,dx$, $dCE = -t\,p\,dx$; con $\eta = -(t/x)(dx/dt)$, la carga excesiva marginal por peso recaudado es $\eta/(1-\eta)$. Lectura: con $\eta = 0.2$, 25 centavos por peso; con $\eta \to 1$ (máximo de la curva de Laffer), el costo se dispara. Implicaciones en una línea: bases amplias, tasas estables. Nota del presentador (`\note{}`): Browning (1976, *JPE* 84(2): 283–298) estima el costo marginal de los fondos públicos entre 1.09 y 1.16 por dólar para impuestos al trabajo en EUA; Salanié reporta 10–50 % en modelos de EGC. — *Salanié (2.2); Gruber (20.1); Browning (1976); derivación propia*

## V. Aplicación mexicana: IEPS a bebidas azucaradas (3) · 10 min

35. **El IEPS a bebidas azucaradas es un impuesto específico por litro.** En 2014, $\tau = 1.00$ peso por litro (DOF, 11-12-2013); se actualiza por inflación cada año desde 2018. Texto vigente en 2026: $3.0818 por litro con azúcares añadidos y $1.5000 por litro con edulcorantes (LIEPS, art. 2, fr. I, inciso G; última reforma DOF 07-11-2025). Cuota de 2025 (≈ $1.65) [VERIFICAR]. Qué predice la teoría: oferta muy elástica implica traslado cercano a 100 %; con poder de mercado, puede superarlo. — *DOF; LIEPS vigente; propia*
36. **En refrescos, el precio subió más que el impuesto.** Con la cuota de 1 peso por litro: Grogger (2017, *AJAE* 99(2): 481–498), precios del INPC y control sintético, los refrescos subieron más que el impuesto. Colchero et al. (2015, *PLOS ONE* 10(12): e0144408): traslado cercano a 1 peso por litro en promedio; más de 100 % en bebidas carbonatadas y menos en no carbonatadas; mayor en envases chicos. Campos-Vázquez y Medina-Cortina (2019, *Latin American Economic Review* 28): 1.12 pesos por litro en refrescos, y menos traslado donde hay más competencia entre tiendas. Lectura con las fórmulas de las diapositivas 8 y 15. Pregunta a la clase (último overlay): «Si el precio subió más que el impuesto, ¿qué nos dice sobre la competencia en el mercado?» — *literatura citada*
37. **Cuando el impuesto corrige una falla, el triángulo cambia de signo.** Respuesta de la cantidad: las calorías compradas de bebidas gravadas cayeron 2.7 % (Aguilar, Gutiérrez y Seira, 2021, *Journal of Health Economics* 77), con sustitución hacia alimentos no gravados. Carga excesiva frente al argumento correctivo (externalidades e internalidades de salud); incidencia distributiva: ¿es regresivo? Pregunta abierta: ¿qué traslado cabe esperar con la cuota de 2026? — *literatura citada; propia*

## VI. Cierre (2) · 5 min

38. **Ideas centrales.** (i) La ley no decide quién paga; las elasticidades sí. (ii) En equilibrio general, la carga viaja a los factores. (iii) La carga excesiva crece con la elasticidad compensada y con el cuadrado de la tasa. (iv) Lo que protege de la incidencia genera carga excesiva. — *propia*
39. **Próximas sesiones.** 6 de octubre: taller del Simulador Fiscal del CIEP; ahí se corren con el simulador los números del IEPS de las diapositivas 35–37. 13 de octubre: IVA e impuestos verdes. IVA uniforme equivale a gravar todos los factores (equivalencia de Harberger); ¿por qué tasas diferenciadas? Impuestos verdes: cuando el triángulo es ganancia y no pérdida; el IEPS a combustibles como caso. Anticipo de la regla de Ramsey (Salanié, cap. 3, sección 3.1). — *propia*

## Apéndice (después de `\appendix`, con `appendixnumberbeamer`)

- **A1. Variación compensada, variación equivalente y excedente de Dupuit-Marshall.** Con VC, el triángulo cae bajo la hicksiana de la utilidad inicial; las tres medidas coinciden solo con utilidad cuasilineal. — *Salanié (2.2); Varian (cap. 10)*
- **A2. Álgebra de sombreros completa del modelo de Harberger.** Pasos de las ecuaciones (1)–(4) de Salanié hasta $(\hat w - \hat r)$. — *Salanié (1.2.4)*

---

## Indicaciones para la Fase 2 (de `revision_esquema.md`)

- Derivaciones reveladas paso a paso con overlays (`\pause` u `\onslide`), una línea a la vez; el resultado final en un bloque destacado. Una derivación por diapositiva, como máximo.
- Tamaño mínimo: nada por debajo de `\small`, en texto ni en etiquetas de gráficas.
- Preguntas a la clase como último overlay de las diapositivas 9, 21, 29 y 36; no son diapositivas nuevas.
- Segunda versión con `\documentclass[handout]{beamer}` (sin overlays): `clase03_incidencia_handout.pdf`.
- Apéndice con `appendixnumberbeamer`, para que no altere la numeración principal.

## Conteo y tiempos

| Bloque | Diapositivas | Minutos |
|---|---|---|
| I. Motivación | 1–3 | 10 |
| II. Equilibrio parcial | 4–15 | 45 |
| III. Equilibrio general | 16–22 | 25 |
| Descanso | — | 10 |
| IV. Distorsiones y carga excesiva | 23–34 | 45 |
| V. IEPS a bebidas azucaradas | 35–37 | 10 |
| VI. Cierre | 38–39 | 5 |
| **Total** | **39 + 2 de apéndice** | **150** |
