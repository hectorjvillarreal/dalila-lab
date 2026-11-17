# Encargo: presentación Beamer — Cambio climático en el análisis macroeconómico (FMI, 2025), segunda parte

## Contexto
Curso de Finanzas Públicas, Maestría en Economía Aplicada, Escuela de Gobierno y
Transformación Pública, Tec de Monterrey. Profesor: Héctor Juan Villarreal.
Sesión «Déficits estructurales y sostenibilidad de la deuda: ¿hay salida?». **Esta
presentación es la segunda parte de la clase de hoy: 75 minutos.** Llega después de 75
minutos sobre el *Global Debt Report 2025* de la OCDE (encargo en `CLAUDE.md`, en esta
misma carpeta), que termina con las necesidades de financiamiento de la transición
climática. Un solo PDF debe servir en presencial y en línea.

**La pregunta de esta parte:** si el clima cambia el crecimiento, la recaudación, el gasto y
el riesgo, ¿cómo se incorpora al análisis macroeconómico y, en particular, al análisis de
sostenibilidad de la deuda?

Lo que los alumnos ya vieron y aquí se retoma:
- La primera parte de hoy (deuda cara y necesidades de inversión para la transición).
- La dinámica de la deuda y la fiscal r-star (sesión del 10 de noviembre).
- Impuestos verdes (12–13 de octubre): Pigou, doble dividendo, IEPS a combustibles y al
  carbono, impuestos ecológicos estatales.

## Entregables obligatorios
**El producto es el PDF compilado, no solo el .tex.** Al terminar deben existir, compilados
con `latexmk -pdf`, en la misma carpeta de la sesión que la primera parte:
- `clima_p2.pdf` y `clima_p2_handout.pdf` (`\documentclass[handout]{beamer}`).
- `clima_p2.tex`, por si hay que corregir.

Si la compilación falla, corrige y vuelve a compilar; no entregues un .tex sin su PDF.

## Fases y tiempos
**Fase 1 (meta: 14:30) — esquema, y detente.** Lee el documento completo (unas 70 páginas)
y escribe `esquema_clima_p2.md`: lista numerada de diapositivas con título, una línea de
contenido y **la sección y página que la respalda**. Parte del esquema provisional de
abajo y corrígelo contra el texto. Entrégalo junto con el de la Parte 1, para una sola
revisión. Espera aprobación.

**Fase 2 (meta: 17:30) — construcción**, después de terminar la Parte 1 y solo después de
aprobar este esquema.

## Fuentes
- **Mitra, P., Raissi, M., Versailles, B. et al. (2025), «Integrating Climate Change into
  Macroeconomic Analysis: A Review of Impact Channels, Data, Models, and Scenarios», IMF
  Working Paper 25/170.** Fuente principal. Localízalo en Dalila; si no está, descárgalo
  del FMI (acceso abierto) y guárdalo en la carpeta de la sesión. Verifica la lista completa
  de autores en el PDF.
- Literatura que el documento cite (modelos de evaluación integrada, funciones de daño,
  escenarios de la NGFS o del IPCC). Úsala solo si el documento remite a ella, y verifica
  cada referencia antes de ponerla al pie.
- **Datos de México:** solo de fuentes oficiales o del propio documento (SHCP, INECC,
  CENAPRED, Banxico). Ejemplos posibles, a verificar: costos de desastres recientes (por
  ejemplo, el huracán Otis en 2023), instrumentos de transferencia de riesgo como los bonos
  catastróficos, la eliminación del FONDEN, el IEPS al carbono y la taxonomía sostenible.
  Cifras con año y fuente al pie.
- **Dalila:** antes de citar cualquier archivo, revisa si tiene alguna restricción de
  circulación. Ante la duda, no lo cites y anótalo en el reporte.
- **Plantilla:** `deuda_p1.tex`, para que las dos partes se vean como una sola sesión.

Las fuentes son de consulta: no copies párrafos ni figuras. Las gráficas y diagramas se
redibujan.

## Decisiones acordadas
- Portada: «El clima entra a la macroeconomía», con el subtítulo «FMI (2025), WP 25/170 ·
  Segunda parte» y la fecha «Noviembre de 2026».
- Pie de página: «Déficits y deuda · Parte 2».
- Términos: riesgos físicos (agudos y crónicos) y riesgos de transición; mitigación y
  adaptación; canales de transmisión; función de daño; modelos de evaluación integrada;
  escenarios climáticos; análisis de sostenibilidad de la deuda; pasivos contingentes;
  activos varados.

---

## Esquema provisional (≈22 diapositivas · 75 min)

### I. Por qué el clima es un tema macroeconómico (3) · 8 min
1. **Portada.**
2. **De las necesidades de inversión a la macroeconomía.** Puente con la primera parte: el
   clima no solo pide financiamiento, también cambia el crecimiento, la recaudación, el
   gasto y el riesgo de la deuda.
3. **Dos tipos de riesgo.** Físicos (agudos, como huracanes y sequías; crónicos, como el
   aumento de temperatura) y de transición (políticas, tecnología, precios relativos).
   Mitigación frente a adaptación. Diagrama propio.

### II. Canales de transmisión (7) · 25 min
El documento revisa los canales hacia los sectores real, fiscal, externo, monetario y
financiero, en distintos horizontes. Una diapositiva por sector, más una de síntesis.
4. **Sector real.** Productividad, oferta de trabajo, capital destruido, agricultura.
5. **Sector fiscal.** Ingresos que caen, gasto de reconstrucción, pasivos contingentes,
   costo de la adaptación; el efecto sobre el balance primario.
6. **Sector externo.** Exportaciones, turismo, remesas, términos de intercambio.
7. **Sector monetario.** Choques de oferta, inflación de alimentos y energía, tasa neutral.
8. **Sector financiero.** Aseguradoras, bancos y activos varados.
9. **Horizontes.** Qué pesa en el corto plazo y qué en el largo: tabla propia con canales y
   horizontes, según el documento.
10. **Enlace con impuestos verdes.** Los impuestos al carbono como política de transición:
    sus efectos macro y fiscales (sesión del 12–13 de octubre).

### III. Datos, modelos y escenarios (6) · 20 min
11. **Qué datos se usan.** Las fuentes que el documento revise (temperatura, desastres,
    exposición).
12. **Funciones de daño.** Cómo se traduce el clima en pérdida de producto; una ecuación
    sencilla, si el documento la presenta, con su lectura. Derivación o lectura con
    overlays.
13. **Familias de modelos.** Modelos de evaluación integrada, de equilibrio general,
    DSGE, macroeconométricos y otros que el documento compare: para qué sirve cada uno y
    sus límites. Tabla propia.
14. **Escenarios.** Qué son los escenarios climáticos (por ejemplo, los de la NGFS o del
    IPCC) y cómo se usan; un escenario no es un pronóstico.
15. **Incertidumbre y colas.** Puntos de inflexión, no linealidades, lo que los modelos no
    capturan bien.
16. *(opcional)* **Lo que recomienda el documento para el análisis por país.**

### IV. Clima y sostenibilidad de la deuda (4) · 15 min
17. **El clima en la ecuación de la deuda.** Cómo entra cada canal en $\Delta b$: menor $g$,
    mayor $r$ por la prima de riesgo, menor balance primario por gasto de reconstrucción y
    ajustes stock-flujo por pasivos contingentes. Diapositiva propia que conecta el
    documento con la ecuación de la sesión anterior.
18. **Un ejercicio ilustrativo.** Trayectoria de deuda de México con y sin un choque
    climático, con parámetros ilustrativos y rotulados como tales (por ejemplo, un desastre
    que reduce el crecimiento un año y eleva el gasto). Gráfica pgfplots. Muestra insumos y
    fórmula.
19. **México: exposición y protección.** Riesgos físicos relevantes y los instrumentos
    existentes (seguros y bonos catastróficos, presupuesto para desastres tras la
    eliminación del FONDEN). Solo cifras verificadas.
20. **Adaptar cuesta, no adaptar cuesta más.** La lectura fiscal de la adaptación, según el
    documento. Pregunta (último overlay): «¿Debería el Paquete Económico incluir un
    escenario climático?»

### V. Cierre (2) · 7 min
21. **Ideas para llevarse.** Tres, que integren las dos partes de la sesión.
22. **Puente a la próxima sesión (24 de noviembre): el sistema fiscal mexicano y el Paquete
    Económico 2027.**

Ritmo: pregunta → canal o herramienta → lectura con la aritmética de la deuda → México.

---

## Construcción
- LaTeX Beamer 16:9 con el preámbulo de `deuda_p1.tex`.
- Gráficas y diagramas en TikZ/pgfplots con el estilo común. Nada extraído de los PDF.
- A lo sumo dos ecuaciones (la función de daño, si el documento la trae, y la dinámica de la
  deuda con choque climático), con overlays y en 4–5 líneas. Nada por debajo de `\small`.
- Preguntas a la clase como último overlay, nunca como diapositiva aparte.
- Al pie de cada diapositiva, la sección del documento que la respalda.
- **Cifras:** verifica cada cifra contra su fuente. Lo que no logres verificar, **quítalo de
  la diapositiva** y anótalo en el reporte. No debe quedar ningún [VERIFICAR] en pantalla.
  El ejercicio de la diapositiva 18 va rotulado como ilustrativo.
- Marca como opcionales (distintivo discreto en gris) diapositivas que sumen unos 8 minutos.
- Entregables sin errores ni cajas desbordadas. Revisión visual: convierte las páginas a
  imágenes y corrige texto que se salga, elementos encimados o etiquetas ilegibles.

## Idioma: la voz del profesor
Igual que en la primera parte. Si existe `_crossrefs/style/VOZ-HJVP-001.md`, síguelo;
prevalece sobre esta sección.
- Oraciones completas y explicativas en el cuerpo, que unan causa y efecto; nada de
  fragmentos sin verbo. Títulos y etiquetas pueden ser breves y, cuando se pueda, decir el
  resultado.
- Abre cada bloque diciendo por qué importa, con una pregunta o corrigiendo una idea común.
- Cada cifra con un punto de comparación; si es una proyección, un escenario o es dudosa,
  dilo.
- Concede antes de objetar; sin adversarios con nombre; **sin catastrofismo**: el riesgo
  climático se mide y se administra; el tono es el de un análisis de riesgos, no el de una
  alarma.
- Cierra cada bloque con un juicio sobrio, una pregunta abierta o una tarea.
- Evita abstracciones personificadas, interjecciones («Ojo»), metáforas de moda, frases de
  suspenso en dos tiempos y muletillas («es importante destacar», «cabe señalar», «en este
  sentido», «clave», «crucial», «fundamental», «robusto», «abordar», «explorar»,
  «profundizar», «desafíos y oportunidades»).
- **«Asumir» está prohibido en el sentido de «suponer»: usa «suponer».** Tampoco «rol»
  (usa «papel») ni «impactar» (usa «afectar» o «incidir»).
- Trato de «ustedes».

Al terminar, relee todo de corrido **solo** para revisar el idioma. En cada diapositiva,
pregúntate si así lo diría el profesor en voz alta; si no, reescríbela.

## Reporte final
Lista de diapositivas con su respaldo en el documento, cifras verificadas con su fuente y
año, insumos del ejercicio ilustrativo, lo que quitaste por no poder verificarlo, archivos
de Dalila consultados y su estado de circulación, y cualquier desviación del esquema
aprobado.
