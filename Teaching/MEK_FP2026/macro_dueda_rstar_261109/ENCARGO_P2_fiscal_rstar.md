# Encargo: presentación Beamer — Fiscal r-star (Bolhuis, Koosakul y Shenai), segunda parte

## Contexto
Curso de Finanzas Públicas, Maestría en Economía Aplicada, Escuela de Gobierno y
Transformación Pública, Tec de Monterrey. Profesor: Héctor Juan Villarreal.
Sesión «La perspectiva macro». **Esta presentación es la segunda parte de la clase de hoy:
60 minutos, sin descanso.** Llega justo después de 90 minutos sobre el capítulo 4 de
Bénassy-Quéré et al. (multiplicadores, dinámica de la deuda, mercado de deuda pública,
equivalencia ricardiana y efectividad de la política fiscal), cuyo encargo es
`CLAUDE.md` en esta misma carpeta. Un solo PDF debe servir en presencial y en línea.

La primera parte termina con el balance primario que estabiliza la deuda,
$s^* = \frac{r-g}{1+g}\,b$, y con un anticipo de la interacción entre política fiscal y
monetaria. Esta segunda parte le da vuelta a la pregunta: **con el balance primario que hay,
¿qué tasa de interés real estabiliza la deuda, y es compatible con la tasa que necesita el
banco central?**

Lo que los alumnos ya vieron y aquí se retoma:
- La primera parte de hoy (dinámica de la deuda, $r - g$, mercado de deuda, dominancia
  fiscal anticipada).
- Cuentas Nacionales de Transferencia y envejecimiento (2–3 de noviembre): el
  envejecimiento presiona el balance primario por décadas.

## Entregables obligatorios
**El producto es el PDF compilado, no solo el .tex.** Al terminar deben existir, compilados
con `latexmk -pdf`, en la misma carpeta de la sesión que la primera parte:
- `politica_fiscal_p2.pdf` y `politica_fiscal_p2_handout.pdf`
  (`\documentclass[handout]{beamer}`).
- `politica_fiscal_p2.tex`, por si hay que corregir.

Si la compilación falla, corrige y vuelve a compilar; no entregues un .tex sin su PDF.

## Fases y tiempos
**Fase 1 (meta: 14:30) — esquema, y detente.** Lee el artículo completo y escribe
`esquema_politica_fiscal_p2.md`: lista numerada de diapositivas con título, una línea de
contenido y **la sección, ecuación o figura del artículo que la respalda**. Parte del esquema
provisional de abajo y corrígelo contra el texto. Si el esquema de la primera parte sigue
pendiente de aprobación, entrega los dos juntos para una sola revisión. Espera aprobación.

**Fase 2 (meta: 17:30) — construcción**, después de terminar la primera parte y solo
después de aprobar este esquema.

## Fuentes
- **Bolhuis, M. A., Koosakul, J. y Shenai, N. (2024), «Fiscal R-Star: Fiscal-Monetary
  Tensions and Implications for Policy», IMF Working Paper 24/174.** Fuente principal:
  conceptos, ecuaciones y notación salen de aquí. Busca en Dalila la versión disponible.
  Existe una versión posterior presentada en la conferencia anual del Reserve Bank of
  Australia (septiembre de 2025, revisada en noviembre de 2025), con un comentario de
  Rachael McCririck. Si Dalila tiene esa versión, úsala y anota en el reporte cuál usaste;
  si no, trabaja con el WP 24/174 y no cites cifras de la otra versión.
- Literatura que el artículo cite (por ejemplo, sobre política fiscal activa y pasiva, o
  sobre la tasa neutral). Úsala solo si el artículo remite a ella, y verifica cada
  referencia antes de ponerla al pie.
- **Datos de México para el ejercicio:** SHCP (Saldo Histórico de los Requerimientos
  Financieros del Sector Público y balance primario, del Paquete Económico más reciente y de
  las estadísticas oportunas), Banco de México (meta de inflación y estimaciones publicadas
  de la tasa neutral real) e INEGI (PIB). Cifras con año y fuente al pie.
- **Dalila:** si hay material del profesor sobre dominancia fiscal en México, revisa antes
  si tiene alguna restricción de circulación (README, pie de documento o portada con «No
  divulgar», «borrador» o similar). Úsalo solo si es público, y solo en las notas del
  presentador. Ante la duda, no lo cites y anótalo en el reporte. No presentes como resultado
  un trabajo en proceso.
- **Plantilla:** `politica_fiscal_p1.tex`, para que las dos partes se vean como una sola
  sesión.

Las fuentes son de consulta: no copies párrafos ni figuras. Las gráficas se redibujan con
los datos.

## Decisiones acordadas
- Portada: «Fiscal r-star: cuando la deuda y el banco central tiran en sentidos opuestos»,
  con el subtítulo «Bolhuis, Koosakul y Shenai (2024) · Segunda parte» y la fecha «Noviembre
  de 2026».
- Pie de página: «Política fiscal · Parte 2».
- **Términos:** «fiscal r-star» se queda en inglés, como en el artículo, con la traducción
  la primera vez («la tasa real que estabiliza la deuda»); «r-star monetaria» o «tasa
  neutral»; «brecha fiscal-monetaria» (*fiscal-monetary gap*, en inglés solo la primera
  vez); «política fiscal activa» y «pasiva»; «dominancia fiscal»; «represión financiera».
- **Notación:** la del artículo. En la diapositiva de la definición, una línea que la empate
  con la ecuación de la primera parte.

---

## Esquema provisional (≈17 diapositivas · 60 min)

### I. Puente (2) · 5 min
1. **Portada.**
2. **La misma ecuación, otra pregunta.** De la primera parte: dado $r$, ¿qué balance primario
   estabiliza la deuda? Ahora: dado el balance primario, ¿qué tasa la estabiliza? Una
   diapositiva que muestre las dos lecturas de la misma ecuación.

### II. El concepto (5) · 18 min
3. **Recordatorio: la r-star monetaria.** La tasa real con la que la producción está en su
   potencial y la inflación en su meta.
4. **Fiscal r-star: la definición.** La tasa real que estabiliza la razón de deuda a PIB con
   un balance primario dado, la producción en su potencial y la inflación en su meta.
   Derivación con overlays a partir de la ecuación de acumulación de deuda del artículo;
   resultado en bloque destacado. — sección del artículo que la define
5. **Cómo se lee.** Una fiscal r-star más alta significa más espacio fiscal: si está por
   encima de la tasa efectiva de la deuda, hay margen; si está por debajo, el margen se
   cierra. La ventaja del concepto: vive en el mismo espacio que la tasa neutral, así que
   se pueden comparar.
6. **La brecha fiscal-monetaria.** r-star monetaria menos fiscal r-star. Gráfica propia con
   las dos tasas y la brecha.
7. **Política fiscal activa y pasiva.** La función de reacción del balance primario a la
   deuda que estima el artículo; por qué, según los autores, la política fiscal se volvió
   más activa después de la crisis financiera global.

### III. Lo que pasa cuando la brecha es positiva (3) · 12 min
8. **Cuatro desenlaces posibles.** Los que el artículo derive, en sus términos, con la
   intuición de cada uno. Pregunta (último overlay): «¿Cuál les parece más probable en
   México?»
9. *(opcional)* **La descomposición formal.** La ecuación del artículo que relaciona la
   brecha con la acumulación de deuda, la inflación y el balance primario; lectura término
   por término, sin derivarla completa.
10. **Dominancia fiscal y represión financiera.** Cuando el banco central cede, o cuando la
    deuda se licúa con tasas reales negativas; los episodios históricos que el artículo
    destaque (por ejemplo, la posguerra).

### IV. La evidencia (2) · 7 min
11. **140 años de tensiones.** Lo que encuentran para 16 economías avanzadas entre 1878 y
    2020: cómo se mueven la fiscal r-star y la brecha, y por qué los autores concluyen que
    las tensiones están en máximos históricos. Gráfica redibujada solo si el artículo trae
    los datos en tablas; si no, una gráfica esquemática rotulada como tal.
12. **Límites.** Ninguna de las dos r-star se observa; el balance primario se toma como
    exógeno; la estimación es sensible a supuestos. Los que reconozca el artículo y, si se
    usa la versión de la conferencia, los del comentario.

### V. Ejercicio: la fiscal r-star de México (3) · 13 min
El artículo no estima México. Aquí se aplica su definición con datos públicos; rotula todo
como **ejercicio ilustrativo**, con escenarios y no con un solo número.
13. **El cálculo.** Con la definición del artículo y datos de SHCP, INEGI y Banxico: deuda a
    PIB, balance primario, crecimiento potencial y meta de inflación. Tabla con dos o tres
    escenarios (por ejemplo, crecimiento bajo, central y alto). Si la definición del
    artículo requiere supuestos, decláralos en la diapositiva.
14. **La comparación.** La fiscal r-star de cada escenario frente al rango de tasa neutral
    real que publica Banxico y frente a la tasa real efectiva de la deuda pública. Signo y
    tamaño de la brecha.
15. **Lo que cambia en una economía emergente.** Deuda en moneda extranjera, prima de riesgo,
    $r - g$ volátil, Pemex y un balance primario que el envejecimiento presionará. Autonomía
    del banco central y metas de inflación como ancla. Pregunta (último overlay): «Si la
    brecha fuera positiva y persistente, ¿qué tendría que moverse primero?»

### VI. Cierre (2) · 5 min
16. **Ideas para llevarse.** Tres, que integren las dos partes de la sesión.
17. **Puente a la próxima sesión (17 de noviembre): déficits estructurales y sostenibilidad
    de la deuda, ¿hay salida?**

Ritmo: intuición → gráfica → formalización → lectura → México.

---

## Construcción
- LaTeX Beamer 16:9 con el preámbulo de `politica_fiscal_p1.tex`.
- Gráficas en TikZ/pgfplots con el estilo común. Nada extraído de los PDF.
- Derivaciones paso a paso con overlays, una por diapositiva, máximo 4–5 líneas; resultado
  final en bloque destacado. Nada por debajo de `\small`.
- Preguntas a la clase como último overlay, nunca como diapositiva aparte.
- Al pie de cada diapositiva, la sección, ecuación o figura del artículo que la respalda.
- **Cifras:** verifica cada cifra contra su fuente. Lo que no logres verificar, **quítalo de
  la diapositiva** y anótalo en el reporte. No debe quedar ningún [VERIFICAR] en pantalla.
  En el ejercicio de México, muestra los insumos y la fórmula para que los alumnos puedan
  replicarlo.
- Marca como opcionales (distintivo discreto en gris) diapositivas que sumen unos 7 minutos.
- Entregables sin errores ni cajas desbordadas. Revisión visual: convierte las páginas a
  imágenes y corrige texto que se salga, elementos encimados o etiquetas ilegibles.

## Idioma: la voz del profesor
Igual que en la primera parte. Si existe `_crossrefs/style/VOZ-HJVP-001.md`, síguelo;
prevalece sobre esta sección.
- Oraciones completas y explicativas en el cuerpo, que unan causa y efecto; nada de
  fragmentos sin verbo. Títulos y etiquetas pueden ser breves y, cuando se pueda, decir el
  resultado.
- Abre cada bloque diciendo por qué importa, con una pregunta o corrigiendo una idea común.
- Cada cifra con un punto de comparación; si es dudosa o depende de supuestos, dilo.
- Concede antes de objetar; sin adversarios con nombre; sin catastrofismo: una brecha
  positiva es una tensión que se administra, no un desenlace escrito.
- Cierra cada bloque con un juicio sobrio, una pregunta abierta o una tarea.
- Evita abstracciones personificadas, interjecciones («Ojo»), metáforas de moda, frases de
  suspenso en dos tiempos y muletillas («es importante destacar», «cabe señalar», «en este
  sentido», «clave», «crucial», «fundamental», «robusto», «abordar», «explorar»,
  «profundizar»).
- **«Asumir» está prohibido en el sentido de «suponer»: usa «suponer».** Tampoco «rol»
  (usa «papel») ni «impactar» (usa «afectar» o «incidir»).
- Trato de «ustedes».

Al terminar, relee todo de corrido **solo** para revisar el idioma. En cada diapositiva,
pregúntate si así lo diría el profesor en voz alta; si no, reescríbela.

## Reporte final
Versión del artículo usada, lista de diapositivas con su respaldo en el artículo, insumos y
fuentes del ejercicio de México, cifras quitadas por no poder verificarlas, archivos de
Dalila consultados y su estado de circulación, y cualquier desviación del esquema aprobado.
