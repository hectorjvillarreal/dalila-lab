# Encargo: dos presentaciones Beamer — Consumo e impuestos verdes

## Contexto
Curso de Finanzas Públicas, Maestría en Economía Aplicada, Escuela de Gobierno y
Transformación Pública, Tec de Monterrey. Profesor: Héctor Juan Villarreal.
Sesión «Consumo e impuestos verdes», 150 minutos. **La misma sesión se imparte dos veces:
hoy (12 de octubre, 18:30, presencial) y mañana (13 de octubre, en línea).** Un solo juego
de PDF sirve para los dos formatos.

Los alumnos manejan microeconomía al nivel de Varian y ya vieron incidencia y carga
excesiva (sesión del 26 de septiembre). Primer parcial, de teoría: 20 de octubre.

## Entregables obligatorios
**El producto son los PDF compilados, no solo los .tex.** Al terminar deben existir en la
carpeta, compilados con `latexmk -pdf` y abiertos para revisarlos:
- `consumo_iva.pdf` y `consumo_iva_handout.pdf`
- `consumo_verdes.pdf` y `consumo_verdes_handout.pdf`
- Los .tex fuente (`consumo_iva.tex`, `consumo_verdes.tex`), por si hay que corregir.

Si la compilación falla, corrige y vuelve a compilar; no entregues un .tex sin su PDF.

## Tiempo y prioridades
La clase es hoy a las 18:30. **No te detengas a pedir aprobación del esquema:** el esquema
de abajo ya está aprobado. Construye en este orden:
1. Presentación del IVA completa, compilada y revisada (meta: 15:30).
2. Presentación de impuestos verdes completa, compilada y revisada (meta: 17:00).
3. Versiones para repartir de las dos.

Si el tiempo aprieta, prioriza que las dos presentaciones existan completas sobre el pulido.

## Fuentes (en esta carpeta)
- **de Mooij, Hebous y Keen (2025)**, «Efficiency Aspects of the Value Added Tax», IMF
  WP/25/165 (`wpiea2025165-source-pdf.pdf`). Columna teórica del IVA. Secciones citadas
  abajo como «FMI 2.1», etc.
- **Barreix, Rocha y Tostes Neto**, «Tres innovaciones en la reforma del impuesto sobre el
  valor agregado en Brasil», CIATBlog, 25 de julio de 2025 (versión publicada; cítala así).
  La nota larga en .docx («Los tres ejes innovadores de IVA…», mayo de 2025) trae el
  Cuadro 1 y los apéndices: úsala para detalles.
- **Salanié**, *The Economics of Taxation*: regla de Ramsey (cap. 3, sec. 3.1); localiza
  Atkinson-Stiglitz y revisa el cap. 10, que el programa asigna a esta sesión, y úsalo donde
  aplique.
- **Gruber**, *Public Finance and Public Policy*: localiza los dos capítulos de
  externalidades (problemas y soluciones; aplicación a medio ambiente y salud).
- **CIEP (2023)**, Emilio Sánchez Salazar, «Impuestos verdes: una oportunidad para
  fortalecer la recaudación subnacional», 25-10-2023:
  https://ciep.mx/impuestos-verdes-una-oportunidad-para-fortalecer-la-recaudacion-subnacional/
  Peso menor: una diapositiva de datos y una de discusión.
- **`clase_1001.pptx`**: esqueleto del profesor, sin desarrollo. Da el hilo y el tono de la
  presentación del IVA (ver abajo). Sus cifras no tienen fuente: no las copies sin
  verificarlas.
- **`clase03_incidencia.tex`**: plantilla. Hereda el preámbulo, el tema, los colores, el
  estilo de las gráficas, los bloques y el formato de las preguntas a la clase.

Las fuentes son de consulta: no copies párrafos ni figuras. Las gráficas se redibujan.

## Decisiones acordadas
- Dos archivos: `consumo_iva.tex` y `consumo_verdes.tex`. No numeres la sesión («Clase N»).
  Pie de página: «Consumo e impuestos verdes · IVA» y «Consumo e impuestos verdes ·
  Impuestos verdes». Fecha en la portada: «Octubre de 2026».
- Notación y términos de la sesión del 26 de septiembre: **carga excesiva** (término
  único), $e_D, e_S$ en valor absoluto, $t$ ad valorem, $\tau$ específico.
- Remite a la sesión anterior cuando aplique («sesión del 26 de septiembre, diap. N»).
- Se queda fuera el uso macro del IVA (FMI 3.1, devaluación fiscal): llega el 10 de
  noviembre.

---

## Presentación 1: IVA (25 diapositivas · 85 min)

El hilo lo da el esqueleto del profesor (`clase_1001.pptx`): **tender un puente entre la
evidencia internacional sobre eficiencia (FMI) y las propuestas de equidad de América
Latina (Barreix), y llevarlo a la reforma fiscal en México.** Los bloques teóricos dan el
sustento; el arranque y el cierre son de política. Toma los títulos coloquiales del
esqueleto cuando funcionen («México recauda muy poco. ¿Qué pasó?»).

### I. Motivación (4)
1. **Portada.** «IVA en México: eficiencia, equidad y lecciones internacionales». Subtítulo:
   «Consumo e impuestos verdes · Parte 1».
2. **Dos paradigmas.** Viejo: eficiencia contra equidad; en los ochenta y noventa, «recauda
   con eficiencia y redistribuye con el gasto». Nuevo: la equidad sí importa en el diseño
   del impuesto. Al pie, en una línea: impuestos directos (ISR, predial) e indirectos (IVA,
   IEPS); las cuotas de seguridad social son la tercera pieza (sesión del 26 de septiembre).
   Pregunta (último overlay): «¿Qué cambió?». Esta diapositiva anuncia el bloque IV.
3. **México recauda muy poco. ¿Qué pasó?** El IVA existe en 175 jurisdicciones (OCDE,
   2024; Francia lo aplicó en 1954) y es la principal fuente de recaudación en países en
   desarrollo. Gráfica de barras redibujada del Gráfico 1 de Barreix et al. (IVA en % del
   PIB, 2021); valores leídos del gráfico: Brasil 12.5 (tres niveles de gobierno), Chile
   9.5, Uruguay 7.9, Colombia 5.9, México 4.3, ALC 6.4, OCDE 6.9. Verifícalos contra
   *Estadísticas tributarias en América Latina y el Caribe* (OCDE, BID, CEPAL y CIAT,
   2024). **Ojo:** el esqueleto dice «3.8 % del PIB» para México y «4–6 % en AL»; usa una
   sola fuente y un solo año, y no digas que ALC recauda 4–6 % (su promedio está arriba de
   México). Pregunta: ¿por qué tan poco con una tasa de 16 %?
4. **Objetivo de hoy.** Puente entre el FMI (eficiencia) y Barreix (equidad); por qué
   importa para la reforma fiscal en México.

### II. Mecánica (3)
5. **IVA e impuesto a las ventas: los dos gravan el consumo, solo que…** Cadena de tres
   etapas (insumos → fabricante → minorista → consumidor) con números: débito menos
   crédito; la recaudación total es $t$ × venta final. Cobro fraccionado y huella
   documental: el riesgo de evasión se reparte. Contraste en una línea con el impuesto a
   los ingresos brutos y su cascada. — FMI 2.3
6. **Principio de destino.** Exportaciones a tasa cero, importaciones gravadas: neutral al
   comercio, «el impuesto interno del libre comercio». Gancho a Brasil (transición de
   origen a destino). — FMI 2.3; Barreix et al.
7. **Tasa cero frente a exención.** Tabla: con tasa cero no se cobra y se acredita; con
   exención no se cobra y no se acredita, y el IVA de los insumos se vuelve impuesto a los
   insumos. Ejemplo numérico: exentar una etapa intermedia **sube** la recaudación y el
   precio final. México: alimentos y medicinas a tasa cero (LIVA, art. 2-A) y principales
   exenciones (arts. 9, 15 y 20); verifica contra la LIVA vigente.

### III. Eficiencia en la producción (4)
8. **No gravar insumos: Diamond y Mirrlees (1971).** Gravar insumos reduce la producción sin
   lograr nada que no se logre gravando el consumo. Eficiencia significa no alterar la
   organización productiva. Supuestos: competencia, rentas gravables, sin restricciones
   para gravar el consumo. — FMI 2.1 y nota 4
9. **Cuánto cuesta gravar insumos.** Keen (2014): carga excesiva (% del costo)
   $= \tfrac12\,\alpha(1-\alpha)\,\sigma\,t^2$, con $\alpha$ la participación de insumos
   gravados y $\sigma$ la sustitución entre insumos. Parentesco con $\tfrac12 t^2 \varepsilon$
   de la sesión anterior. Lectura de $\alpha(1-\alpha)$: la pérdida es chica si se grava
   casi ningún insumo o casi todos (los precios relativos no cambian). Ejemplo del FMI:
   $\sigma=2$, $\alpha=0.5$, $t=5\%$ → 0.06 % del costo y 0.82 % de lo recaudado. Gráfica
   pgfplots de la carga excesiva contra $\alpha$ para $\sigma = 1$ y $2$. — FMI 2.1, fig. 1
10. **La cascada no es, por sí sola, ineficiente.** Con coeficientes técnicos fijos no hay
    carga excesiva; el costo viene de la sustitución, de la integración vertical y de la
    opacidad (5 % sobre 5 % = 10.25 %). Contraste con el «efecto cascada» de Barreix et al.
    — FMI 2.1, notas 7–8
11. **Las exenciones deshacen el IVA.** Distorsionan, empujan al autosuministro y vuelven
    opacas las tasas efectivas; las importaciones, exentas de IVA en origen, ganan ventaja.
    Política industrial vía IVA: una tasa reducida a un insumo vendido a contribuyentes no
    tiene efecto; una exención es contraproducente. Pregunta (último overlay): «Si exentamos
    un insumo que compran empresas registradas, ¿el precio final baja o sube?»
    — FMI 2.3 y 3.3

### IV. ¿Tasa uniforme? (5) — material del parcial
12. **Dos distorsiones.** Entre bienes y entre consumo y ocio. El ocio no se grava: un IVA
    uniforme es un impuesto al trabajo (equivalencia de Harberger, sesión del 26 de
    septiembre, diap. 19). — FMI 2.2
13. **La regla de Ramsey.** Minimizar la carga excesiva sujeto a la recaudación: las
    demandas compensadas caen en la misma proporción. Derivación corta con overlays. —
    Salanié, cap. 3, sec. 3.1
14. **La elasticidad inversa es un caso particular.** Con demandas independientes,
    $t_i/(1+t_i) \propto 1/e_i$. Lectura del FMI: baja elasticidad = alta
    complementariedad con el ocio. Corlett y Hague: gravar menos lo que acompaña al
    trabajo (guarderías, transporte) y más lo que acompaña al ocio. Pregunta (último
    overlay): «¿Qué bien gravarían más y cuál menos?» — Salanié; FMI 2.2
15. **Atkinson y Stiglitz.** Con impuesto óptimo al ingreso y separabilidad débil entre
    consumo y ocio, la tasa uniforme es óptima: es la versión formal del viejo paradigma de
    la diapositiva 2. Cuanto más ricos los instrumentos redistributivos, más débil el caso
    para diferenciar. FMI: no hay un resultado universal de uniformidad, pero apartarse
    exige razones contundentes. — Salanié; FMI 2.2
16. **Redistribuir con tasas reducidas rinde poco.** Los ricos también comen; lo que importa
    es qué tan distintas son las canastas (Sah, 1983). México: costo de la tasa cero y de
    las exenciones, y su distribución por decil (SHCP, Presupuesto de Gastos Fiscales;
    «Distribución del pago de impuestos y recepción del gasto público»); verifica cifras y
    año.

### V. Incidencia y ganancias (2)
17. **¿Quién paga el IVA?** Traslado casi completo con la tasa general (zona euro
    1999–2013, Benedek et al., 2020; Alemania); alrededor de 30 % en tasas reducidas de la
    zona euro; restaurantes en Francia y Suecia, 14–25 %. Lectura con la fórmula de la
    sesión anterior: base amplia, poca sustitución, más traslado. Casi no hay evidencia para
    países en desarrollo; la informalidad podría reducir el traslado (sesión del 26 de
    septiembre, diap. 14). — FMI 2.5
18. **Cuánto se gana con un IVA.** Ganancia ≈ caída del costo marginal de los fondos
    públicos × recaudación inicial. Auriol y Warlters (2012), 38 países africanos: mediana
    de 1.17 con IVA y 1.23 sin IVA (comparación entre países, no una caída medida en el
    tiempo). Con recaudación de 12–15 % del PIB, unos 0.7–0.9 % del PIB al año; con el
    segundo método del FMI, entre 0.3 y 2.1 %. Dilo con la cautela del FMI («supuesto
    heroico»). **No uses** el «0.5–2 %» del esqueleto. Enlace con $\eta/(1-\eta)$ de la
    sesión anterior. — FMI 2.4

### VI. Barreix: el puente hacia la equidad (3)
19. **IVA personalizado.** Base amplia y tasa uniforme, con devolución focalizada del IVA a
    hogares pobres, por transferencias electrónicas y padrones sociales. El FMI lo cita como
    alternativa a las tasas reducidas (nota 28). Es Atkinson-Stiglitz llevado a la práctica.
    Experiencias en América Latina: **verifícalas en Barreix et al. (2022), «Revisando el
    IVA personalizado» (BID, doi 10.18235/0004147)** antes de citarlas. El esqueleto menciona
    Uruguay, Paraguay y Colombia y un efecto de «+2–3 % del ingreso de hogares pobres»; cita
    solo los países, diseños y cifras que confirmes ahí (Colombia, por ejemplo, ya aplica la
    compensación del IVA desde 2020, no solo la debate).
20. **Brasil: tres innovaciones.** (i) IVA dual: CBS federal e IBS estatal y municipal, con un
    comité gestor que recauda y reparte el IBS según el destino; transición de origen a
    destino en 50 años. (ii) Pago fraccionado inteligente: diagrama con el ejemplo de
    Barreix et al. (venta de 100 + 26.5 de IBS/CBS; la entidad de pago consulta al fisco y,
    si el proveedor no tiene créditos, separa los 26.5). (iii) Cashback: hogares de hasta
    medio salario mínimo per cápita; 100 % de la CBS y 20 % del IBS en gas, electricidad,
    agua, alcantarillado y telecomunicaciones; 20 % en otros bienes. Antecedente: Devolve
    ICMS, Rio Grande do Sul (2021). — Barreix, Rocha y Tostes Neto (2025)
21. **FMI y Barreix: ¿visiones complementarias?** Coinciden en la uniformidad y en rechazar
    exenciones amplias; el FMI pone la eficiencia y Barreix la equidad vía devoluciones.
    Lectura crítica: (i) la reforma brasileña no es uniforme (tasas reducidas en 30 %, 60 %
    y a cero; Zona Franca de Manaos; Simples Nacional); ¿cashback y tasas reducidas se
    duplican? (ii) El Cuadro 1 de Barreix et al. dice que la informalidad vuelve
    «invisibles» a los deciles bajos, pero el cashback también exige identificarlos.

### VII. México (3)
22. **La oportunidad para México.** Base erosionada (tasa cero, exenciones, región
    fronteriza), informalidad, recaudación baja frente a pares. Ganancia potencial de
    ampliar la base: usa el gasto fiscal del IVA según el Presupuesto de Gastos Fiscales
    más reciente; **no uses** el «1–1.5 % del PIB» del esqueleto sin fuente. Digitalización:
    factura electrónica y transferencias sociales.
23. **Riesgos y desafíos.** Capacidad administrativa y padrones confiables; resistencia
    política a gravar alimentos y medicinas; liquidez para devolver a tiempo; transparencia
    para sostener la confianza. La informalidad del lado del hogar: ¿a quién se le devuelve?
24. **Para la reforma fiscal: ¿qué harían?** Del esqueleto, como propuestas para discutir y
    no como conclusiones: avanzar a la tasa única con un plan gradual; un piloto de IVA
    personalizado; fortalecer la administración tributaria y la factura electrónica;
    comunicar con claridad la protección a hogares vulnerables. Pregunta (último overlay):
    «¿Por dónde empezarían y qué dejarían para después?»

### VIII. Puente (1)
25. **El IVA es eficiente, pero en México se percibe injusto.** Un IVA amplio y uniforme, con
    devoluciones focalizadas, puede ser eficiente y justo a la vez. Pero recaudar no es
    corregir: si el objetivo es corregir un daño, la herramienta no es una tasa diferenciada
    de IVA sino un impuesto específico. Entrada a la segunda parte. — FMI 3.3

---

## Presentación 2: Impuestos verdes (15 diapositivas · 50 min + 5 de cierre)

Entre las dos presentaciones: descanso de 10 minutos.

### I. Teoría (8)
1. **Portada.** «Consumo e impuestos verdes. Parte 2: impuestos correctivos».
2. **Cuando el triángulo es ganancia.** Externalidad: costo marginal privado y social.
   Impuesto pigouviano = daño marginal en el óptimo. Gráfica propia. — Gruber
3. **Derivación mínima.** Bienestar = beneficio − costo − daño $D(E)$; condición privada
   frente a social; $\tau^* = D'(E^*)$. Overlays.
4. **Específico y sobre el uso, no tasa diferenciada de IVA.** El daño depende de la
   cantidad, no del precio. El daño es el mismo en consumo final que como insumo: gravar
   el combustible de una fábrica es la excepción a Diamond-Mirrlees, no su violación. El
   IVA se aplica sobre el precio que ya incluye el impuesto específico. — FMI 3.3
5. **Precio o cantidad.** Weitzman (1974): con incertidumbre en el costo de abatimiento,
   conviene el impuesto si el daño marginal es plano (CO₂, contaminante de acervo) y la
   cuota de emisiones si es empinado (umbrales). Dos paneles. — Gruber
6. **Con impuestos distorsionantes.** Sandmo (1975): el impuesto óptimo suma un componente
   Ramsey (recaudar) y uno pigouviano (corregir). — FMI 3.3, nota 84
7. **¿Doble dividendo?** Débil: reciclar la recaudación es mejor que devolverla de suma
   fija. Fuerte: mejorar también la eficiencia no ambiental. Bovenberg y de Mooij (1994,
   *AER*): el efecto interacción (el impuesto verde reduce el salario real y agrava la
   distorsión laboral) suele superar al reciclaje; el impuesto ambiental óptimo queda por
   debajo del pigouviano. Nota: de Mooij es coautor del artículo del FMI.
8. **Incidencia distributiva.** En países ricos suele ser regresivo; en países de ingreso
   medio, donde el consumo de combustibles se concentra arriba, puede ser progresivo. El
   uso de la recaudación decide. Verifica la referencia empírica antes de citarla.
9. **Internalidades.** El IEPS a bebidas azucaradas (sesión del 26 de septiembre,
   diap. 37). Aquí el argumento a favor del impuesto específico es menos claro. — FMI 3.3

### II. México (4)
10. **IEPS a combustibles automotrices.** Cuota por litro, actualizada por inflación; cuotas
    de 2026 y estímulos fiscales (en 2022 anularon la cuota); verifica todo contra el DOF.
    ¿Pigouviano o recaudatorio? Un estímulo es un subsidio que va contra Pigou, y beneficia
    más a los deciles altos.
11. **IEPS a combustibles fósiles («impuesto al carbono», desde 2014).** Cuota según el
    contenido de carbono; precio implícito por tonelada de CO₂ frente a estimaciones del
    costo social del carbono. Verifica cuotas y precio implícito.
12. **Impuestos verdes estatales.** CIEP (2023): 26 entidades los contemplan en su ley de
    ingresos y solo 13 recaudan; 2,590.7 millones de pesos, en promedio 3.5 % de sus
    ingresos por impuestos; composición: extracción de materiales 43.2 %, emisiones a la
    atmósfera 30.4 %, contaminantes al suelo y agua 25.9 %, residuos 0.6 %. Rotula los
    datos como de 2023. No cites el número de entidades sin impuestos verdes (la nota se
    contradice).
13. **Para discutir: ¿qué está bien y qué no?** Dos afirmaciones de la nota del CIEP:
    (i) el doble dividendo como hecho (Pearce, 1991); (ii) «gravar la producción final, no
    los insumos». Contraste con las diapositivas 4 y 7. Mención breve: rediseñar la tenencia
    según el motor. Pregunta como último overlay.

### III. Cierre (2)
14. **Ideas centrales: impuestos verdes.** Corregir pide un impuesto específico, sobre la
    emisión donde ocurra; con impuestos distorsionantes, el óptimo queda por debajo de
    Pigou; la distribución depende del reciclaje.
15. **Cierre de la sesión.** El IVA recauda con eficiencia (base amplia, tasa uniforme, sin
    gravar insumos); los impuestos verdes corrigen (específicos, aun sobre insumos); la
    redistribución se hace mejor con transferencias. Parcial: 20 de octubre. Próxima
    sesión, 27 de octubre: marco unitario (Kaplow) y digitalización; el pago fraccionado y
    la factura electrónica como puente.

---

## Construcción
- LaTeX Beamer 16:9, preámbulo de `clase03_incidencia.tex`. Asegúrate de tener
  `\usepackage[spanish,es-nodecimaldot,es-noaccentedoperators]{babel}` («max», «min» sin
  acento; decimales con punto). `\usetikzlibrary{babel}` con TikZ.
- Gráficas en TikZ/pgfplots con el estilo común. Nada extraído de los PDF.
- Derivaciones paso a paso con overlays, una por diapositiva, máximo 4–5 líneas; resultado
  final en bloque destacado. Nada por debajo de `\small`.
- Preguntas a la clase como último overlay, nunca como diapositiva aparte.
- Referencias completas al pie (autor, año, revista) solo cuando las hayas verificado.
- **Cifras:** verifica en la web cada cifra mexicana y brasileña. Lo que no logres verificar,
  **quítalo de la diapositiva** y anótalo en el reporte final. No debe quedar ningún
  [VERIFICAR] en pantalla.
- Entregables: `consumo_iva.pdf`, `consumo_verdes.pdf` y sus versiones
  `\documentclass[handout]{beamer}` (`consumo_iva_handout.pdf`,
  `consumo_verdes_handout.pdf`). Sin errores ni cajas desbordadas.
- Revisión visual: convierte las páginas a imágenes y corrige textos que se salgan,
  elementos encimados, etiquetas ilegibles o etiquetas que una curva atraviese.

## Idioma: que suene a persona, no a máquina (importa tanto como el contenido)
El texto debe sonar como lo diría un profesor mexicano de economía frente a su grupo, no
como un resumen generado. Escribe directamente en español; no redactes en inglés para
traducir.

Cómo se ve el lenguaje humano en una diapositiva:
- **Frases cortas y concretas, con sujeto y verbo.** «Los ricos también comen» en lugar de
  «Se observa que los beneficios de la tasa cero se concentran en los deciles superiores».
- **Títulos que dicen el resultado**, como en la sesión anterior: «La cascada no es, por sí
  sola, ineficiente»; «Recaudar no es corregir».
- **Ejemplos cotidianos antes que abstracciones:** la tortilla con tasa cero, el litro de
  gasolina, el restaurante, la factura electrónica.
- **Voz activa y verbos directos:** «el fisco devuelve», «la empresa acredita», no «es
  devuelto por» ni «se procede a acreditar».
- **Algún giro coloquial cuando ayude**, sin perder el registro académico (en la sesión
  anterior funcionaron «Da lo mismo de qué lado se cobre» y «Carga más quien tiene menos
  opciones para responder»).

Lo que delata texto de máquina, y hay que evitar:
- Muletillas: «es importante destacar», «cabe señalar», «en este sentido», «en el marco
  de», «clave», «crucial», «fundamental», «robusto», «integral», «abordar», «explorar»,
  «profundizar», «potenciar», «en resumen» al abrir una diapositiva.
- Series de tres adjetivos o tres sustantivos por costumbre («eficiente, equitativo y
  transparente»).
- Viñetas que empiezan todas igual o que tienen exactamente la misma longitud.
- Frases de transición vacías («Veamos ahora…», «A continuación analizaremos…»).
- Calcos del inglés: «suponer», no «asumir»; «papel», no «rol»; «afectar», no «impactar»;
  «a la larga», no «eventualmente»; «tasa», no «rata».

Términos: tasa cero, exención, acreditamiento, traslado, cobro fraccionado, pago
fraccionado (split payment, en inglés solo la primera vez), cashback (devolución del IVA),
impuesto pigouviano, doble dividendo, carga excesiva. Trato de «ustedes».

Al terminar, relee todo de corrido **solo** para revisar el idioma. Pregúntate en cada
diapositiva si así lo diría el profesor en voz alta. Si no, reescríbela.

## Reporte final
Lista de diapositivas por presentación, cifras verificadas con su fuente, cifras que
quitaste por no poder verificarlas y cualquier desviación del esquema.
