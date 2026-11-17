# Encargo: presentación Beamer — Deuda: OCDE, *Global Debt Report 2025* (primera parte)

## Contexto
Curso de Finanzas Públicas, Maestría en Economía Aplicada, Escuela de Gobierno y
Transformación Pública, Tec de Monterrey. Profesor: Héctor Juan Villarreal.
Sesión «Déficits estructurales y sostenibilidad de la deuda: ¿hay salida?». La clase tiene
dos partes con encargos separados en esta carpeta:
- **Parte 1 (este archivo): deuda, 75 minutos.**
- Parte 2 (`ENCARGO_P2_clima.md`): cambio climático en el análisis macroeconómico,
  75 minutos.

Un solo PDF por parte debe servir en presencial y en línea.

Lo que los alumnos ya vieron y aquí se retoma:
- Sesión anterior (La perspectiva macro): multiplicadores, la ecuación de la dinámica de la
  deuda, el balance primario que estabiliza la deuda, el mercado de la deuda pública, el
  «pecado original» y la fiscal r-star de Bolhuis, Koosakul y Shenai.
- Cuentas Nacionales de Transferencia y envejecimiento: el envejecimiento presiona el
  balance primario por décadas.
- Impuestos verdes (12–13 de octubre): IEPS a combustibles y al carbono.
- Próxima sesión (24 de noviembre): el sistema fiscal mexicano y el Paquete Económico 2027.

## Entregables obligatorios
**El producto es el PDF compilado, no solo el .tex.** Al terminar deben existir, compilados
con `latexmk -pdf`:
- `deuda_p1.pdf` y `deuda_p1_handout.pdf` (`\documentclass[handout]{beamer}`).
- `deuda_p1.tex`, por si hay que corregir.

Guarda todo en una carpeta nueva de la sesión dentro de `Teaching/MEK_FP2026/`, con la misma
convención de nombre que las sesiones anteriores. Si la compilación falla, corrige y vuelve a
compilar; no entregues un .tex sin su PDF.

## Fases y tiempos
**El informe es largo. No lo resumas completo.**

**Fase 1 (meta: 14:30) — mapa y esquema, y detente.**
1. Localiza el informe en Dalila; si no está, descárgalo de la OCDE (acceso abierto,
   doi 10.1787/8ee42b13-en) y guárdalo en la carpeta de la sesión.
2. Haz un mapa de sus capítulos y secciones con páginas. Según la página del informe, trae
   dos capítulos permanentes (perspectivas del endeudamiento soberano y mercados de deuda
   corporativa) y dos temáticos (mercados de bonos soberanos de economías emergentes y en
   desarrollo, y financiamiento con deuda de la transición climática). Confírmalo.
3. Lee completos el resumen ejecutivo, el capítulo de endeudamiento soberano y el de bonos
   soberanos de economías emergentes. Del capítulo climático, lo necesario para la
   diapositiva puente. Del capítulo corporativo, solo lo que sirva para una diapositiva
   opcional.
4. Escribe `esquema_deuda_p1.md`: lista numerada de diapositivas con título, una línea de
   contenido y **el capítulo, sección y página que la respalda**. Parte del esquema
   provisional de abajo y corrígelo contra el texto.

Entrega este esquema junto con el de la Parte 2, para una sola revisión. Espera aprobación.

**Fase 2 (meta: 16:30) — construcción**, solo después de aprobar el esquema. Después sigue
con la Parte 2.

## Fuentes
- **OCDE (2025), *Global Debt Report 2025: Financing Growth in a Challenging Debt Market
  Environment*, OECD Publishing, París.** Fuente principal: cifras, argumentos y gráficas
  salen de aquí. Las cifras del informe son de su fecha de publicación (marzo de 2025) y
  son proyecciones para 2025: rotúlalas así.
- **Datos de México:** SHCP (Plan Anual de Financiamiento, Saldo Histórico de los
  Requerimientos Financieros del Sector Público, Paquete Económico 2027), Banco de México
  (tenencia de valores gubernamentales por residentes en el extranjero) e INEGI (PIB).
  Cifras con año y fuente al pie.
- **Dalila:** antes de citar cualquier archivo, revisa si tiene alguna restricción de
  circulación (README, pie de documento o portada con «No divulgar», «borrador» o similar).
  Ante la duda, no lo cites y anótalo en el reporte. No presentes como resultado un trabajo
  en proceso.
- **Plantilla:** `politica_fiscal_p2.tex` (la sesión anterior). Hereda el preámbulo
  (incluido `\usepackage[spanish,es-nodecimaldot,es-noaccentedoperators]{babel}`), el
  tema, los colores, el estilo de las gráficas, los bloques y el formato de las preguntas.

Las fuentes son de consulta: no copies párrafos ni figuras. Las gráficas se redibujan con
los datos.

## Decisiones acordadas
- Portada: «Deuda cara, necesidades crecientes: ¿hay salida?», con el subtítulo «OCDE,
  *Global Debt Report 2025* · Primera parte» y la fecha «Noviembre de 2026».
- Pie de página: «Déficits y deuda · Parte 1».
- Términos: deuda negociable; emisión bruta y neta; costo de financiamiento; plazo promedio
  y riesgo de refinanciamiento; tenencia extranjera; deuda en moneda local y extranjera;
  bonos verdes, sociales y sostenibles (bonos temáticos); espacio fiscal.
- Remite a la sesión anterior así: «sesión del 10 de noviembre, diap. N».

---

## Esquema provisional (≈22 diapositivas · 75 min)

### I. La pregunta de la sesión (2) · 5 min
1. **Portada.**
2. **Del modelo a los mercados.** La sesión anterior dio la aritmética: el balance primario
   que estabiliza la deuda y la tasa que la estabiliza. Hoy, qué está pasando en los
   mercados donde esa deuda se financia, y si hay salida cuando los déficits son
   estructurales.

### II. El endeudamiento soberano en la OCDE (7) · 25 min
3. **Más deuda y más cara.** Emisión y saldo de deuda soberana de la OCDE, según el informe
   (por ejemplo, emisión récord proyectada para 2025). Gráfica con los datos del informe.
4. **El costo llega con rezago.** La deuda vigente se contrató en buena parte con tasas
   bajas; al refinanciarse a tasas de mercado, el costo de intereses sube. Lo que el
   informe documente sobre vencimientos próximos y costo de intereses frente a ingresos.
5. **Tasas largas que suben aunque bajen las tasas de política.** Lo que el informe
   encuentre sobre rendimientos soberanos y primas por plazo.
6. **Quién compra ahora.** Del banco central a inversionistas más sensibles al precio: el
   fin de las compras de los bancos centrales y el cambio en la base de inversionistas.
7. **Plazos y riesgo de refinanciamiento.** Plazo promedio, concentración de vencimientos.
8. **Enlace con la sesión anterior.** Qué implican estas tendencias para $r - g$ y para la
   fiscal r-star: si la tasa efectiva converge a la de mercado, se cierra el margen.
   Pregunta (último overlay): «¿Qué tendría que pasar con el balance primario?»
9. *(opcional)* **Deuda corporativa.** Una diapositiva con lo central del capítulo
   corporativo.

### III. Economías emergentes (6) · 20 min
10. **Más endeudamiento en mercado.** Lo que el informe documente sobre emisión soberana de
    economías emergentes y en desarrollo.
11. **Acceso desigual.** Diferenciales, calificaciones y emisores que pierden acceso.
12. **Moneda local frente a moneda extranjera.** Retoma el «pecado original» de la sesión
    anterior: lo que el informe muestre sobre la composición por moneda.
13. **Profundidad del mercado local.** Inversionistas institucionales locales, liquidez y
    tenencia extranjera.
14. **México en el mapa.** Saldo, composición por moneda, plazo y tenencia extranjera de la
    deuda del gobierno federal (SHCP, Banxico); lo que el informe diga de México, si lo
    menciona. Cifras verificadas, con año.
15. **¿Hay salida?** Las opciones que el informe discute, presentadas como del informe, y la
    lectura para México: ajuste del balance primario, crecimiento, gestión de pasivos.
    Pregunta (último overlay): «¿Cuál de estas salidas es políticamente viable en México?»

### IV. Puente al clima (3) · 15 min
16. **Las necesidades de inversión que vienen.** El capítulo temático: cuánto
    financiamiento requiere la transición climática según el informe.
17. **¿Deuda pública o privada?** Más financiamiento público eleva la deuda a PIB por
    décadas; más financiamiento privado requiere mercados de capital más profundos. Lo que
    el informe concluya para economías emergentes.
18. **Bonos temáticos.** Bonos verdes, sociales y sostenibles; México como emisor soberano
    de bonos sostenibles (verifica fechas y montos con SHCP).

### V. Cierre (4) · 10 min
19. **Déficits estructurales: lo que no se arregla con el ciclo.** Envejecimiento (sesión de
    NTA), intereses más altos y necesidades de inversión al mismo tiempo.
20. **Ideas para llevarse.**
21. *(opcional)* **Para el Paquete Económico 2027.** Qué mirar el 24 de noviembre: costo
    financiero, plan de financiamiento, balance primario.
22. **Puente a la segunda parte.** «Si el clima cambia las necesidades de financiamiento,
    también cambia el crecimiento, la recaudación y el riesgo: ¿cómo se mete eso en el
    análisis macroeconómico?»

Ritmo: pregunta → datos del informe → lectura con la aritmética de la sesión anterior →
México.

---

## Construcción
- LaTeX Beamer 16:9 con el preámbulo de la plantilla.
- Gráficas en TikZ/pgfplots con el estilo común, con los datos del informe y de las fuentes
  mexicanas. Nada extraído de los PDF.
- Esta parte es de datos más que de derivaciones: a lo sumo una ecuación (la de la dinámica
  de la deuda, como recordatorio). Nada por debajo de `\small`.
- Preguntas a la clase como último overlay, nunca como diapositiva aparte.
- Al pie de cada diapositiva, el capítulo y la página del informe que la respalda.
- **Cifras:** verifica cada cifra contra su fuente y rotula su año (o «proyección del
  informe para 2025»). Lo que no logres verificar, **quítalo de la diapositiva** y anótalo
  en el reporte. No debe quedar ningún [VERIFICAR] en pantalla.
- Marca como opcionales (distintivo discreto en gris) diapositivas que sumen unos 8 minutos.
- Entregables sin errores ni cajas desbordadas. Revisión visual: convierte las páginas a
  imágenes y corrige texto que se salga, elementos encimados o etiquetas ilegibles.

## Idioma: la voz del profesor
Escribe directamente en español académico de México, como lo diría el profesor frente a su
grupo; no traduzcas el informe frase por frase. Si existe
`_crossrefs/style/VOZ-HJVP-001.md`, síguelo; prevalece sobre esta sección.
- Oraciones completas y explicativas en el cuerpo, que unan causa y efecto; nada de
  fragmentos sin verbo. Títulos y etiquetas pueden ser breves y, cuando se pueda, decir el
  resultado.
- Abre cada bloque diciendo por qué importa, con una pregunta o corrigiendo una idea común.
- Cada cifra con un punto de comparación (otro año, otro grupo de países, un umbral); si es
  una proyección o es dudosa, dilo.
- Concede antes de objetar; sin adversarios con nombre; sin catastrofismo: la deuda alta es
  un problema que se administra, no una tragedia anunciada.
- Cierra cada bloque con un juicio sobrio, una pregunta abierta o una tarea.
- Evita abstracciones personificadas («los mercados castigan» como figura retórica),
  interjecciones («Ojo»), metáforas de moda, frases de suspenso en dos tiempos y muletillas
  («es importante destacar», «cabe señalar», «en este sentido», «clave», «crucial»,
  «fundamental», «robusto», «abordar», «explorar», «profundizar», «desafíos y
  oportunidades»).
- **«Asumir» está prohibido en el sentido de «suponer»: usa «suponer».** Tampoco «rol»
  (usa «papel») ni «impactar» (usa «afectar» o «incidir»).
- Trato de «ustedes».

Al terminar, relee todo de corrido **solo** para revisar el idioma. En cada diapositiva,
pregúntate si así lo diría el profesor en voz alta; si no, reescríbela.

## Reporte final
Mapa del informe con las secciones usadas y las que quedaron fuera, lista de diapositivas
con su respaldo, cifras verificadas con su fuente y año, lo que quitaste por no poder
verificarlo, archivos de Dalila consultados y su estado de circulación, y cualquier
desviación del esquema aprobado.
