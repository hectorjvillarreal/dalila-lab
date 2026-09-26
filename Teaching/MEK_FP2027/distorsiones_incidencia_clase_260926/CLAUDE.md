# Encargo: presentación Beamer, clase 3 — Incidencia y distorsiones

## Contexto
Curso de Finanzas Públicas, Maestría en Economía Aplicada, Escuela de Gobierno y
Transformación Pública, Tec de Monterrey. Profesor: Héctor Juan Villarreal.
Sesión del 26 de septiembre de 2026: "Incidencia, distorsiones y pérdida de bienestar".
Los alumnos manejan microeconomía al nivel de Varian (Microeconomic Analysis) y
optimización con restricciones.

## Fuentes (en esta carpeta)
- Salanié, The Economics of Taxation, capítulos 1 y 2. Es el texto oficial del curso:
  la notación y los resultados formales salen de aquí.
- Gruber, Public Finance and Public Policy. Localiza los capítulos de incidencia fiscal
  y de ineficiencia de los impuestos; úsalos para la intuición y las gráficas.

Las fuentes son de consulta: no copies párrafos ni figuras. Todas las gráficas se redibujan.

## Fase 1: esquema (detente al terminar)
Escribe `esquema.md` con la lista numerada de diapositivas: título, una línea sobre el
contenido y la fuente (Salanié / Gruber / propia). Entre 30 y 40 diapositivas.
No escribas LaTeX todavía. Espera mi aprobación.

Distribución orientativa:
- Motivación y preguntas de la sesión (2–3)
- Incidencia en equilibrio parcial: incidencia legal y económica, cuña fiscal, fórmula
  con elasticidades, casos extremos (8–10)
- Incidencia en equilibrio general: modelo de Harberger de dos sectores (5–7)
- Distorsiones: carga excesiva, triángulo de Harberger, aproximación ½·t²·ε, demanda
  compensada frente a no compensada, carga excesiva marginal (10–12)
- Aplicación mexicana: IEPS a bebidas azucaradas o a combustibles, traslado a precios (2–3)
- Cierre: ideas centrales y próximas sesiones: taller del Simulador Fiscal del CIEP
  (6 de octubre) e IVA e impuestos verdes (13 de octubre) (2)

Estado: esquema aprobado el 2026-09-25 (`esquema.md`, 39 diapositivas + 2 de apéndice,
con la revisión de `revision_esquema.md` aplicada). Sesión de 150 minutos, en línea.
`esquema.md` es la referencia para la Fase 2, incluidas sus «Indicaciones para la Fase 2».

Ritmo de cada bloque: intuición → gráfica → derivación → lectura del resultado sobre la
misma gráfica.

## Fase 2: construcción (solo después de aprobar el esquema)
- LaTeX Beamer, formato 16:9, tema sobrio. Compila con `latexmk -pdf`.
- Preámbulo: `\usepackage[spanish,es-nodecimaldot]{babel}` y `\usepackage[T1]{fontenc}`.
  Con TikZ, carga `\usetikzlibrary{babel}` para evitar choques con los atajos de babel.
  Verifica que los decimales salgan con punto.
- Gráficas en TikZ/pgfplots con un estilo común (colores, grosor de línea, etiquetas).
  Nada de imágenes extraídas de los PDF.
- Derivaciones en pasos cortos: no más de 4–5 líneas de álgebra por diapositiva.
- Aplicación mexicana: no inventes cifras. Si citas un dato, márcalo con
  `\textcolor{red}{[VERIFICAR]}` junto con la fuente que crees que lo respalda.
- Entregables: `clase03_incidencia.tex` y `clase03_incidencia.pdf`, sin errores ni
  cajas desbordadas (overfull hbox/vbox).
- Revisión visual: convierte las páginas del PDF a imágenes, revisa cada diapositiva y
  corrige texto que se salga, elementos encimados o etiquetas ilegibles.

## Idioma (importa tanto como el contenido)
Escribe directamente en español académico de México, como lo haría un profesor de
economía mexicano. No redactes en inglés para luego traducir.
- Frases cortas; nada de párrafos. Títulos breves y, cuando se pueda, que afirmen el
  resultado ("El lado menos elástico carga con el impuesto").
- Evita muletillas: "es importante destacar", "cabe señalar", "en este sentido", "clave",
  "crucial", "fundamental", "robusto", "abordar", "explorar", "profundizar",
  "sumergirnos", "en resumen" al inicio de una diapositiva, series de tres adjetivos.
- Evita calcos del inglés: "suponer" (no "asumir") para los supuestos de un modelo;
  "papel" (no "rol"); "afectar" o "incidir" (no "impactar"); "a la larga" (no
  "eventualmente"); nada de pasivas innecesarias ("es pagado por").
- Terminología: incidencia legal y económica, cuña fiscal, traslado (pass-through; el
  término en inglés entre paréntesis solo la primera vez), excedente del consumidor y del
  productor, carga excesiva (o pérdida irrecuperable de eficiencia: elige uno y sé
  consistente), triángulo de Harberger, demanda compensada (hicksiana).
- Si hace falta dirigirse a los alumnos, trátalos de "ustedes".
- Al terminar, relee todo el texto de corrido solo para revisar el idioma y corrige lo
  que suene traducido.
