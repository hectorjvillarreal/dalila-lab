# Encargo: presentación Beamer — Política fiscal (Bénassy-Quéré et al., cap. 4), primera parte

## Contexto
Curso de Finanzas Públicas, Maestría en Economía Aplicada, Escuela de Gobierno y
Transformación Pública, Tec de Monterrey. Profesor: Héctor Juan Villarreal.
Sesión «La perspectiva macro». **Esta presentación es la primera parte de la clase de hoy:
90 minutos.** La segunda parte (60 minutos, encargo aparte) trata el concepto de fiscal
r-star de Bolhuis, Koosakul y Shenai. Un solo PDF
debe servir en presencial y en línea.

Temas de esta primera parte, en este orden:
1. Multiplicadores fiscales.
2. Dinámica de la deuda.
3. El mercado de la deuda pública.
4. Equivalencia ricardiana.
5. Efectividad de la política fiscal.

Lo que los alumnos ya vieron y aquí se retoma:
- Carga excesiva y costo por peso recaudado, $\eta/(1-\eta)$ (26 de septiembre).
- Kaplow: un modelo estático, sin tiempo ni generaciones (26–27 de octubre).
- Cuentas Nacionales de Transferencia y envejecimiento (2–3 de noviembre): el ciclo de vida
  económico y las presiones de pensiones, salud y cuidados. Es el puente natural hacia la
  dinámica de la deuda y la equivalencia ricardiana, que depende de cómo se relacionan las
  generaciones.

## Entregables obligatorios
**El producto es el PDF compilado, no solo el .tex.** Al terminar deben existir, compilados
con `latexmk -pdf`:
- `politica_fiscal_p1.pdf` y `politica_fiscal_p1_handout.pdf`
  (`\documentclass[handout]{beamer}`).
- `politica_fiscal_p1.tex`, por si hay que corregir.

Guarda todo en una carpeta nueva de la sesión dentro de `Teaching/MEK_FP2026/`, con la misma
convención de nombre que las sesiones anteriores. Si la compilación falla, corrige y vuelve a
compilar; no entregues un .tex sin su PDF.

## Fases y tiempos
**El capítulo es muy largo. No lo resumas completo.**

**Fase 1 (meta: 14:00) — mapa y esquema, y detente.**
1. Localiza el capítulo 4 en Dalila y anota edición, año y número de páginas.
2. Haz un mapa de sus secciones (título y páginas) y marca cuáles corresponden a los cinco
   temas de esta primera parte. Lee esas secciones completas; del resto, solo lo necesario
   para el mapa.
3. Escribe `esquema_politica_fiscal_p1.md`: lista numerada de diapositivas con título, una
   línea de contenido y **la sección y página del capítulo que la respalda**. Parte del
   esquema provisional de abajo y corrígelo contra el texto: se armó sin el libro a la mano.
4. Al final del esquema, lista las secciones del capítulo que quedan fuera de esta primera
   parte (por ejemplo, reglas fiscales, consejos fiscales o coordinación en uniones
   monetarias, si el capítulo las trae), como candidatas para otra sesión.

Espera aprobación.

**Fase 2 (meta: 17:00) — construcción**, solo después de aprobar el esquema.

## Fuentes
- **Bénassy-Quéré, A., Cœuré, B., Jacquet, P. y Pisani-Ferry, J., *Economic Policy: Theory
  and Practice*, Oxford University Press, capítulo 4.** Está en Dalila. Fuente principal:
  conceptos, argumentos y notación salen de aquí. Verifica en el PDF la edición y los datos
  bibliográficos.
- Literatura que el capítulo cite sobre cada tema. Úsala si el capítulo remite a ella, y
  verifica cada referencia antes de ponerla al pie. Candidatas probables, solo si las
  encuentras citadas o las verificas: Barro (1974) sobre equivalencia ricardiana; Blanchard
  (1985) sobre horizontes finitos; Ilzetzki, Mendoza y Végh (2013) sobre multiplicadores
  según régimen cambiario, apertura y deuda; Blanchard y Leigh (2013) sobre multiplicadores
  en crisis; Ramey (2019) como panorama de la evidencia; Blanchard (2019) sobre $r < g$;
  Calvo (1988) sobre equilibrios múltiples en deuda; Eichengreen y Hausmann sobre el
  «pecado original».
- **Datos de México:** SHCP (Saldo Histórico de los Requerimientos Financieros del Sector
  Público, balance primario, Paquete Económico más reciente), Banco de México (tenencia de
  valores gubernamentales por residentes en el extranjero) e INEGI (PIB). Cifras con año y
  fuente al pie.
- **Dalila:** si hay material del profesor sobre dominancia fiscal o sostenibilidad de la
  deuda en México, úsalo solo si su circulación es pública. Antes de citar cualquier archivo
  de Dalila, revisa si tiene alguna restricción (un README, un pie de documento o una
  portada que diga «No divulgar», «borrador» o similar). Ante la duda, no lo cites y
  anótalo en el reporte. No presentes como resultado un trabajo en proceso.
- **Plantilla:** la presentación más reciente del curso (`nta_p*.tex`) o
  `kaplow_marco_unitario.tex`. Hereda el preámbulo (incluido
  `\usepackage[spanish,es-nodecimaldot,es-noaccentedoperators]{babel}`), el tema, los
  colores, el estilo de las gráficas, los bloques y el formato de las preguntas a la clase.

Las fuentes son de consulta: no copies párrafos ni figuras. Las gráficas se redibujan con
los datos.

## Decisiones acordadas
- Portada: «Política fiscal: multiplicadores, deuda y efectividad», con el subtítulo
  «Bénassy-Quéré et al., cap. 4 · Primera parte» y la fecha «Noviembre de 2026».
- Pie de página: «Política fiscal · Parte 1».
- Notación: la del capítulo. En la diapositiva de dinámica de la deuda, una línea que la
  empate con la notación habitual: $b$ deuda/PIB, $s$ balance primario/PIB, $r$ tasa de
  interés real, $g$ crecimiento real.
- Términos: multiplicador fiscal (de impacto y acumulado); efecto desplazamiento (*crowding
  out*, en inglés solo la primera vez); balance primario; efecto «bola de nieve»; ajuste
  stock-flujo; prima de riesgo soberano; riesgo de refinanciamiento; «pecado original»;
  equivalencia ricardiana; estabilizadores automáticos; espacio fiscal; dominancia fiscal.
- Remite a sesiones anteriores así: «sesión del 26 de septiembre, diap. 34».

---

## Esquema provisional (≈28 diapositivas · 90 min)

### I. Motivación (2) · 5 min
1. **Portada.**
2. **Por qué la política fiscal volvió al centro.** La pandemia, los niveles de deuda y el
   costo de financiarla. México: déficit y deuda recientes, y lo que plantea el Paquete
   Económico más reciente (verifica cifras con SHCP). Las cinco preguntas de hoy.

### II. Multiplicadores fiscales (6) · 20 min
3. **Qué es un multiplicador.** De impacto y acumulado; de gasto y de impuestos; por qué la
   distinción importa.
4. **El multiplicador keynesiano y sus fugas.** Derivación corta con overlays en la notación
   del capítulo; impuestos e importaciones como fugas. Lectura: en una economía abierta como
   la mexicana, una parte del estímulo se va en importaciones.
5. **Cuando responde la política monetaria.** Efecto desplazamiento; con tipo de cambio
   flexible frente a fijo (Mundell-Fleming, si el capítulo lo usa). Gráfica.
6. **Lo que dice la evidencia.** Rango de estimaciones según el capítulo; por qué varían
   (método, país, momento del ciclo).
7. **El multiplicador depende de las condiciones.** Régimen cambiario, apertura, nivel de
   deuda, tasa de interés en su límite inferior, holgura de la economía. Evidencia de
   Ilzetzki, Mendoza y Végh (2013) para economías emergentes, si la verificas.
8. **¿Y en México?** Qué implican esas condiciones para México. Pregunta (último overlay):
   «Con tipo de cambio flexible y una economía muy abierta, ¿qué tamaño de multiplicador
   esperarían?»

### III. Dinámica de la deuda (6) · 20 min
9. **La restricción presupuestaria del gobierno.** Del déficit a la deuda.
10. **La ecuación de la dinámica de la deuda.** $\Delta b = \frac{r-g}{1+g}\,b - s$,
    derivada con overlays en la notación del capítulo; resultado en bloque destacado.
11. **El balance primario que estabiliza la deuda.** $s^* = \frac{r-g}{1+g}\,b$. Ejercicio
    numérico en clase con valores cercanos a los de México (rotulados como ilustrativos).
12. **Cuando $r < g$.** El debate reciente (Blanchard, 2019, si el capítulo lo trata): la
    deuda puede bajar con déficit primario, y por qué eso no es un almuerzo gratis en
    economías emergentes, donde $r - g$ es volátil.
13. **Lo que la ecuación no ve.** Ajustes stock-flujo: tipo de cambio sobre la deuda en
    moneda extranjera, pasivos contingentes, empresas públicas. En México, el caso de Pemex
    (verifica cómo se contabiliza en los RFSP).
14. **La deuda de México en cifras.** Trayectoria del SHRFSP, balance primario y $r - g$
    (SHCP, INEGI; verifica). Enlace con la sesión anterior: el envejecimiento presiona el
    balance primario a lo largo de décadas. Pregunta (último overlay).

### IV. El mercado de la deuda pública (5) · 15 min
15. **Quién compra deuda pública y por qué.** El activo seguro; residentes y no residentes;
    bancos, fondos de pensiones y bancos centrales. En México, el papel de las Afores.
16. **Prima de riesgo y diferenciales.** Qué la mueve: fundamentales, liquidez, apetito
    global por riesgo.
17. **Equilibrios múltiples y riesgo de refinanciamiento.** Si los inversionistas esperan
    impago, exigen tasas más altas que hacen más probable el impago (Calvo, 1988, si lo
    verificas). Gráfica propia de los dos equilibrios.
18. **El «pecado original» y la deuda en moneda local.** Por qué importa endeudarse en la
    propia moneda; México como caso de transición hacia deuda en pesos y la caída posterior
    de la tenencia extranjera (verifica con Banxico).
19. **Cuando la deuda condiciona al banco central.** Una sola diapositiva de anticipo: qué
    dice el capítulo sobre la interacción entre política fiscal y monetaria. La dominancia
    fiscal se desarrolla en la segunda parte (fiscal r-star); no la repitas aquí.

### V. Equivalencia ricardiana (4) · 15 min
20. **El argumento.** Con un horizonte de dos periodos: bajar impuestos hoy y subirlos
    mañana no cambia la riqueza de los hogares, así que no cambia el consumo. Derivación con
    overlays; resultado en bloque destacado. — Barro (1974)
21. **Los supuestos.** Horizontes infinitos o altruismo entre generaciones, mercados de
    crédito perfectos, impuestos de suma fija, previsión perfecta.
22. **Por qué falla.** Restricciones de liquidez, horizontes finitos (Blanchard, 1985),
    miopía, impuestos distorsionantes. Enlace directo con la sesión de NTA: con generaciones
    traslapadas, posponer impuestos traslada la carga a otras cohortes.
23. **Lo que dice la evidencia.** Según el capítulo: el ahorro privado compensa en parte,
    no en todo. Pregunta (último overlay): «¿Qué hogares mexicanos se comportarían de forma
    ricardiana?»

### VI. Efectividad de la política fiscal (3) · 10 min
24. **Cuándo funciona.** Síntesis: holgura, tasa en su límite inferior, tipo de cambio,
    espacio fiscal y credibilidad.
25. **Estabilizadores automáticos frente a medidas discrecionales.** Rezagos de decisión y
    de ejecución; economía política. En México, estabilizadores débiles y la evidencia de
    política fiscal procíclica en América Latina, si el capítulo la trata o la verificas.
26. **Lo que no conviene olvidar.** Las tres sesiones de microeconomía también importan
    aquí: cada peso de estímulo se financia con impuestos que tienen carga excesiva
    (sesión del 26 de septiembre, diap. 34).

### VII. Cierre (2) · 5 min
27. **Ideas para llevarse.** Una por tema.
28. **Puente a la segunda parte.** «Hasta ahora preguntamos qué balance primario estabiliza
    la deuda con una tasa dada. Ahora damos vuelta a la pregunta: con el balance primario que
    hay, ¿qué tasa de interés real estabiliza la deuda, y es compatible con la que necesita
    el banco central?» Entrada a fiscal r-star.

Ritmo de cada bloque: intuición → gráfica o ejemplo → formalización → lectura del
resultado → caso de México.

---

## Construcción
- LaTeX Beamer 16:9 con el preámbulo de la plantilla.
- Gráficas en TikZ/pgfplots con el estilo común: trayectorias de deuda con distintos
  $r - g$ y balances primarios, los dos equilibrios del mercado de deuda, series de México.
  Nada extraído de los PDF.
- Derivaciones paso a paso con overlays, una por diapositiva, máximo 4–5 líneas; resultado
  final en bloque destacado. Nada por debajo de `\small`.
- Preguntas a la clase como último overlay, nunca como diapositiva aparte.
- Al pie de cada diapositiva, la sección del capítulo que la respalda.
- **Cifras:** verifica cada cifra contra su fuente. Lo que no logres verificar, **quítalo de
  la diapositiva** y anótalo en el reporte. No debe quedar ningún [VERIFICAR] en pantalla.
- Marca como opcionales (distintivo discreto en gris) diapositivas que sumen unos 10
  minutos, por si el tiempo aprieta.
- Entregables sin errores ni cajas desbordadas. Revisión visual: convierte las páginas a
  imágenes y corrige texto que se salga, elementos encimados o etiquetas ilegibles.

## Idioma: la voz del profesor
Escribe directamente en español académico de México, como lo diría el profesor frente a su
grupo; no traduzcas el capítulo frase por frase. Si existe
`_crossrefs/style/VOZ-HJVP-001.md`, síguelo; prevalece sobre esta sección.

- **Oraciones completas y explicativas** en el cuerpo de las diapositivas, que unan causa y
  efecto («Si el banco central sube la tasa para contener la inflación, parte del estímulo
  se pierde»). Nada de fragmentos sin verbo. Los títulos y las etiquetas sí pueden ser
  breves; cuando se pueda, que el título diga el resultado.
- Abre cada bloque diciendo por qué importa, con una pregunta que luego se responde o
  corrigiendo una idea común equivocada.
- Cada cifra lleva un punto de comparación (otro país, otro año, un umbral). Si una cifra es
  dudosa o depende del método, dilo.
- Concede antes de objetar y no nombres adversarios. Evita el catastrofismo: la deuda alta
  es un problema que se administra, no una tragedia anunciada.
- Cierra cada bloque con un juicio sobrio, una pregunta abierta o una tarea.
- Evita: abstracciones personificadas («la deuda exige», «los mercados castigan» como
  figura retórica), interjecciones («Ojo»), metáforas de moda, frases de suspenso en dos
  tiempos y muletillas («es importante destacar», «cabe señalar», «en este sentido»,
  «clave», «crucial», «fundamental», «robusto», «abordar», «explorar», «profundizar»).
- **«Asumir» está prohibido en el sentido de «suponer»: usa «suponer».** Tampoco «rol»
  (usa «papel») ni «impactar» (usa «afectar» o «incidir»).
- Trato de «ustedes».

Al terminar, relee todo de corrido **solo** para revisar el idioma. En cada diapositiva,
pregúntate si así lo diría el profesor en voz alta; si no, reescríbela.

## Reporte final
Mapa del capítulo con las secciones usadas y las que quedaron fuera, lista de diapositivas
con su sección, referencias externas verificadas, cifras verificadas con su fuente, lo que
quitaste por no poder verificarlo, archivos de Dalila consultados y su estado de
circulación, y cualquier desviación del esquema aprobado.
