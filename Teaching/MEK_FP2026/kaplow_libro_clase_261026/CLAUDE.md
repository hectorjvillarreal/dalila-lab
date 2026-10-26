# Encargo: presentación Beamer — Kaplow, capítulos 1 a 3

## Contexto
Curso de Finanzas Públicas, Maestría en Economía Aplicada, Escuela de Gobierno y
Transformación Pública, Tec de Monterrey. Profesor: Héctor Juan Villarreal.
Sesión «Buscando un marco unitario para el sistema fiscal». **Primera sección de la clase
de hoy: 90 minutos.** La segunda sección (digitalización de las finanzas públicas) es
aparte; esta presentación solo cierra con un puente hacia ella. Un solo PDF debe servir en
presencial y en línea.

Lo que los alumnos ya vieron y aquí se reinterpreta:
- Incidencia y carga excesiva (26 de septiembre), incluido el costo por peso recaudado
  $\eta/(1-\eta)$ (diap. 34).
- IVA (12–13 de octubre): Diamond-Mirrlees, Ramsey, Corlett-Hague, Atkinson-Stiglitz
  (diap. 15), costo marginal de los fondos públicos (diap. 18) y la diapositiva «Dos
  paradigmas»: el viejo, «recauda con eficiencia y redistribuye con el gasto», y el nuevo,
  «la equidad sí importa en el diseño del impuesto» (diap. 2).
- Impuestos verdes: Pigou, Sandmo, doble dividendo.

**Kaplow es la lectura más abstracta del curso.** La presentación tiene que hacerla
accesible sin rebajarla: cada idea formal llega después de su intuición y se amarra con
algo que los alumnos ya vieron.

## Entregables obligatorios
**El producto es el PDF compilado, no solo el .tex.** Al terminar deben existir, compilados
con `latexmk -pdf`:
- `kaplow_marco_unitario.pdf` y `kaplow_marco_unitario_handout.pdf`
  (`\documentclass[handout]{beamer}`).
- `kaplow_marco_unitario.tex`, por si hay que corregir.

Si la compilación falla, corrige y vuelve a compilar; no entregues un .tex sin su PDF.

## Fases y tiempos
**Fase 1 (meta: 12:30) — esquema, y detente.** Lee los capítulos 1 a 3 de Kaplow completos
y escribe `esquema_kaplow.md`: lista numerada de diapositivas con título, una línea de
contenido y **la sección y páginas de Kaplow que la respaldan**. Parte del esquema
provisional de abajo, pero corrígelo contra el texto: el esquema se armó sin el libro a la
mano y puede atribuir a estos capítulos ideas que Kaplow desarrolla en otros capítulos o en
artículos. Señala cada caso así. Espera aprobación.

**Fase 2 (meta: 16:00) — construcción**, solo después de aprobar el esquema.

## Fuentes (en esta carpeta)
- **Kaplow, L. (2008), *The Theory of Taxation and Public Economics*, Princeton University
  Press**: cap. 1, «Introduction» (pp. 1–10); Parte I, «Framework»: cap. 2, «An Integrated
  View» (pp. 13–34), y cap. 3, «The Social Objective» (pp. 35–50). Es la fuente principal:
  conceptos, argumentos y notación salen de aquí.
- **Salanié**, *The Economics of Taxation*: para conectar notación y resultados (Ramsey,
  Atkinson-Stiglitz, Mirrlees).
- Artículos de Kaplow que el capítulo 2 resume o cita. Úsalos solo si el libro remite a
  ellos, y verifica cada referencia antes de ponerla al pie:
  - Kaplow (1996), «The Optimal Supply of Public Goods and the Distortionary Cost of
    Taxation», *National Tax Journal* 49(4).
  - Kaplow y Shavell (1994), «Why the Legal System Is Less Efficient than the Income Tax in
    Redistributing Income», *Journal of Legal Studies* 23(2).
  - Kaplow y Shavell (2001), «Any Non-welfarist Method of Policy Assessment Violates the
    Pareto Principle», *Journal of Political Economy* 109(2).
  - Atkinson y Stiglitz (1976), *Journal of Public Economics* 6.
- **`consumo_iva.tex`**: plantilla. Hereda el preámbulo (incluido
  `\usepackage[spanish,es-nodecimaldot,es-noaccentedoperators]{babel}`), el tema, los
  colores, el estilo de las gráficas, los bloques y el formato de las preguntas a la clase.

Las fuentes son de consulta: no copies párrafos ni figuras. Las gráficas se redibujan.

## Decisiones acordadas
- Pie de página: «Marco unitario · Kaplow, caps. 1–3». Portada: «En busca de un marco
  unitario: Kaplow, capítulos 1 a 3», con la fecha «Octubre de 2026».
- **Notación:** la de Kaplow para el modelo de esta sesión. En la diapositiva del modelo,
  una línea que la empate con la de Salanié y con la de las sesiones anteriores.
- **Términos:** «reforma distributivamente neutral» para *distribution-neutral*;
  «bienestarismo» para *welfarism*; «función de bienestar social»; «principio de Pareto»;
  «carga excesiva» (como en todo el curso); «costo marginal de los fondos públicos».
- Remite a sesiones anteriores así: «sesión del IVA, diap. 15».
- Kaplow tiene una posición fuerte. La presentación la expone con fidelidad y con sus
  mejores argumentos, y deja espacio claro a las críticas (bloque IV). No la presenta como
  verdad establecida ni la caricaturiza.

---

## Esquema provisional (24 diapositivas · 90 min)

### I. Motivación (3) · 8 min
1. **Portada.**
2. **Una disciplina hecha pedazos.** Impuesto óptimo al ingreso, impuestos a bienes, bienes
   públicos, transferencias, externalidades: cada subcampo con su regla (Mirrlees, Ramsey,
   Samuelson, Pigou) y su manera de tratar la distribución. La pregunta de Kaplow: ¿qué pasa
   si se analizan juntos? — cap. 1
3. **Lo que ya vimos, con otra luz.** Atkinson-Stiglitz (sesión del IVA, diap. 15),
   $\eta/(1-\eta)$ (26 de septiembre, diap. 34), el costo marginal de los fondos públicos
   (sesión del IVA, diap. 18) y los dos paradigmas (sesión del IVA, diap. 2). Hoy esas
   piezas encajan, o chocan. — propia

### II. El marco integrado (12) · 50 min — cap. 2
4. **El problema del gobierno.** Personas que difieren en capacidad (salario); eligen
   consumo y trabajo; el gobierno solo observa el ingreso y elige un esquema de impuestos y
   transferencias sobre el ingreso, además de impuestos a bienes, bienes públicos y
   regulación. Modelo en notación de Kaplow, con la línea que lo empata con Salanié.
5. **La distorsión que importa es la del trabajo.** Todo instrumento que redistribuye
   condiciona en algo correlacionado con el ingreso y, por lo tanto, desalienta trabajar.
   Intuición con un ejemplo cotidiano.
6. **La reforma distributivamente neutral: la idea.** Se cambia una política (un bien
   público, un impuesto a un bien, una regla) y se ajusta el impuesto al ingreso para que
   cada nivel de ingreso quede igual que antes. Gráfica propia: beneficio neto de la reforma
   por nivel de ingreso y el ajuste del esquema que lo compensa.
7. **La reforma distributivamente neutral: el resultado.** Derivación con overlays, en la
   notación de Kaplow: con separabilidad débil entre trabajo y lo demás, el ajuste deja
   intacta la oferta de trabajo; si sobra recaudación, la reforma permite una mejora de
   Pareto. El resultado final, en un bloque destacado.
8. **Por qué funciona.** Con separabilidad, la decisión de trabajar depende solo del consumo
   que se alcanza con cada ingreso, y el ajuste lo mantiene. Separar el análisis no es
   ignorar la distribución: la distribución se decide al elegir el esquema del impuesto al
   ingreso.
9. **Primera consecuencia: impuestos a bienes.** Atkinson-Stiglitz como caso de reforma
   neutral; qué cambia sin separabilidad (Corlett-Hague, sesión del IVA, diap. 14).
10. **Segunda consecuencia: bienes públicos.** Si el financiamiento es distributivamente
    neutral, la regla de Samuelson no se ajusta por el costo de los fondos (Kaplow, 1996).
    Pregunta (último overlay): «Entonces, ¿el $\eta/(1-\eta)$ de la sesión del 26 de
    septiembre está mal?». La respuesta va en las notas del presentador: depende de cómo se
    financie el gasto.
11. **Tercera consecuencia: regulación y externalidades.** Pigou sin ajustes distributivos;
    redistribuir con reglas legales distorsiona dos veces, el trabajo y la actividad
    (Kaplow y Shavell, 1994).
12. **Cuarta consecuencia: transferencias.** El impuesto al ingreso y las transferencias son
    un solo esquema; se evalúan juntos.
13. **Lo que queda del viejo paradigma.** Vuelta a la diapositiva «Dos paradigmas»:
    Kaplow da la versión rigurosa de «recauda con eficiencia y redistribuye con el
    esquema del ingreso», y dice cuándo falla.
14. **Los supuestos que sostienen el marco.** Separabilidad (empírica), preferencias
    heterogéneas, que el ajuste compensatorio de verdad se haga (economía política) y
    capacidad administrativa.
15. **¿Y en México?** El marco supone un impuesto al ingreso potente y transferencias que
    llegan a todos. Con informalidad alta, un ISR de personas físicas débil y padrones
    incompletos, ese instrumento es débil. Enlace con el FMI (el caso para diferenciar
    tasas es más fuerte en países de menor ingreso) y con el IVA personalizado de Barreix.
    Pregunta (último overlay): «Si el instrumento redistributivo es débil, ¿qué queda del
    marco de Kaplow?»

### III. El objetivo social (6) · 25 min — cap. 3
16. **Bienestarismo.** La evaluación depende solo del bienestar de las personas:
    $W(u_1, \dots, u_n)$.
17. **Funciones de bienestar social.** Utilitarista, cóncava y el extremo rawlsiano. Dos
    razones distintas para redistribuir: la utilidad marginal decreciente del ingreso y la
    aversión a la desigualdad en utilidades. Gráfica de curvas de nivel.
18. **El principio de Pareto.** Qué pide y por qué casi nadie lo discute.
19. **Criterios que no son de bienestar.** Equidad horizontal, capacidad de pago, principio
    del beneficio, nociones de justicia. Argumento de Kaplow y Shavell (2001): todo método
    que no es de bienestar viola el principio de Pareto en algún caso. Pregunta (último
    overlay): «¿Qué criterio defenderían aunque costara bienestar a todos?»
20. **Medir el bienestar de cada persona.** Comparaciones interpersonales y preferencias
    heterogéneas: qué supone Kaplow y qué deja abierto.
21. **Lo que cambia en la práctica.** Las tablas distributivas de una reforma, el análisis
    costo-beneficio con ponderadores distributivos, el «costo de los fondos»: cómo se leen
    con este marco.

### IV. Cierre (3) · 7 min
22. **Tres ideas para llevarse.** Una sola distorsión central (el trabajo); la reforma
    neutral separa eficiencia y distribución sin borrar la distribución; el objetivo social
    es el bienestar de las personas.
23. **Las críticas.** El ajuste compensatorio rara vez ocurre (economía política); la
    separabilidad no siempre se cumple; la capacidad administrativa en países de ingreso
    medio; perspectivas que no son de bienestar (capacidades, derechos, contrato social;
    enlace con Shafik, lectura de la sesión del 22 de septiembre). Presentar cada crítica en
    su versión más fuerte.
24. **Puente.** A la segunda sección de hoy: en Mirrlees la restricción es de información, y
    la digitalización amplía los instrumentos que el marco de Kaplow da por hechos (factura
    electrónica, pago fraccionado, devoluciones focalizadas). A la sesión del 3 de
    noviembre: Kaplow es estático, y las cuentas nacionales de transferencia agregan la
    edad y el ciclo de vida.

Ritmo de cada bloque: intuición → gráfica o ejemplo → formalización → lectura del
resultado → amarre con una sesión anterior.

---

## Construcción
- LaTeX Beamer 16:9 con el preámbulo de `consumo_iva.tex`.
- Gráficas en TikZ/pgfplots con el estilo común. Nada extraído de los PDF.
- Derivaciones paso a paso con overlays, una por diapositiva, máximo 4–5 líneas; resultado
  final en bloque destacado. Nada por debajo de `\small`.
- **Densidad:** es la sesión más abstracta. Mejor una idea bien explicada que tres
  enunciadas. Si una diapositiva necesita más de 6 líneas, pártela o pasa detalle a
  `\note{}`.
- Preguntas a la clase como último overlay, nunca como diapositiva aparte.
- Al pie de cada diapositiva, la sección de Kaplow que la respalda (por ejemplo, «Kaplow,
  sec. 2.2»). Las referencias externas van completas y solo si las verificaste.
- Entregables sin errores ni cajas desbordadas. Revisión visual: convierte las páginas a
  imágenes y corrige texto que se salga, elementos encimados o etiquetas ilegibles.

## Idioma: que suene a persona, no a máquina (importa tanto como el contenido)
El texto debe sonar como lo diría un profesor mexicano de economía frente a su grupo.
Escribe directamente en español; no traduzcas a Kaplow frase por frase.
- Frases cortas, con sujeto y verbo; títulos que dicen el resultado («La distorsión que
  importa es la del trabajo»).
- Ejemplos cotidianos antes que abstracciones.
- Voz activa: «el gobierno ajusta el impuesto», no «se procede a ajustar».
- Sin muletillas: «es importante destacar», «cabe señalar», «en este sentido», «en el marco
  de», «clave», «crucial», «fundamental», «robusto», «integral», «abordar», «explorar»,
  «profundizar», «potenciar», «en resumen» al abrir una diapositiva.
- Sin series de tres adjetivos por costumbre, sin viñetas idénticas en forma y sin
  transiciones vacías («Veamos ahora…»).
- Sin calcos: «suponer», no «asumir»; «papel», no «rol»; «afectar», no «impactar»; «a la
  larga», no «eventualmente». *Welfare* es «bienestar», no «bienestar social» cuando se
  refiere a una persona.
- Trato de «ustedes».

Al terminar, relee todo de corrido **solo** para revisar el idioma. En cada diapositiva,
pregúntate si así lo diría el profesor en voz alta; si no, reescríbela.

## Reporte final
Lista de diapositivas con su sección de Kaplow, referencias externas verificadas, ideas
que no estaban en los capítulos 1 a 3 (y de dónde salieron) y cualquier desviación del
esquema aprobado.
