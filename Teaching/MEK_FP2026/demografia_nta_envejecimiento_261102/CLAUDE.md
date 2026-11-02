# Encargo: tres presentaciones Beamer — Cuentas Nacionales de Transferencia y envejecimiento

## Contexto
Curso de Finanzas Públicas, Maestría en Economía Aplicada, Escuela de Gobierno y
Transformación Pública, Tec de Monterrey. Profesor: Héctor Juan Villarreal.
Sesión «Cuentas Nacionales de Transferencia y envejecimiento»: **lunes 2 de noviembre,
presencial, y martes 3 de noviembre, en línea.** Un solo juego de PDF sirve para los dos
formatos. Es la sesión del curso que más le importa al profesor: es su campo de
investigación.

Las tres presentaciones funcionan también como **notas del curso**: la versión para
repartir debe poder leerse sola, sin la exposición.

| Parte | Archivo | Tema | Duración |
|---|---|---|---|
| 1 | `nta_p1_demografia` | Transición demográfica y la investigación del equipo | 60 min |
| 2 | `nta_p2_manual` | Manual NTA, capítulos 1 y 2 | 60 min |
| 3 | `nta_p3_cepal` | CEPAL (2025): impactos económicos del envejecimiento | 60 min |

**Las tres suman 180 minutos y la sesión dura 150.** Calcula cada una para 60 minutos y
marca en cada presentación **diapositivas opcionales** que sumen unos 10 minutos: el
profesor decide en clase cuáles salta. Márcalas con un distintivo discreto (por ejemplo,
«opcional» en gris en la esquina) y lístalas en el reporte.

Lo que los alumnos ya vieron y aquí se retoma:
- Incidencia (26 de septiembre): cuotas de seguridad social y la reforma de pensiones de
  2020; informalidad.
- Kaplow (26–27 de octubre): un modelo estático. Las NTA agregan la edad y el ciclo de vida.
- Próxima sesión (10 de noviembre): la perspectiva macro y la sostenibilidad de la deuda.

## Entregables obligatorios
**El producto son los PDF compilados, no solo los .tex.** Al terminar deben existir,
compilados con `latexmk -pdf`, para cada parte:
- `nta_pN_<tema>.pdf` y `nta_pN_<tema>_handout.pdf` (`\documentclass[handout]{beamer}`).
- `nta_pN_<tema>.tex`, por si hay que corregir.

Si la compilación falla, corrige y vuelve a compilar; no entregues un .tex sin su PDF.

## Fases y tiempos
**Fase 1 — tres esquemas, y detente.** Lee las fuentes y escribe `esquema_nta.md` con las
tres partes: lista numerada de diapositivas con título, una línea de contenido, la fuente
exacta (capítulo y página, o ruta del archivo de Dalila) y la marca «opcional» donde
aplique. Parte de los esquemas provisionales de abajo, pero corrígelos contra las fuentes:
se armaron sin los documentos a la mano. Espera aprobación.

**Fase 2 — construcción**, solo después de aprobar los esquemas, en este orden: Parte 1,
Parte 2, Parte 3. Compila y revisa cada una antes de pasar a la siguiente.

## Fuentes

### Parte 1: archivos de Dalila (investigación propia)
Puedes leer todos los archivos de Dalila. Busca en:
- `GrandPlan/DFD/`: el laboratorio de simulación demográfico-fiscal (los cuatro módulos del
  motor: demográfico, salud y seguridad social, núcleo OLG/DSGE y capa de agentes), la
  revisión del modelo OLG, los escenarios de transición rápida de la fecundidad, la
  documentación de datos (CELADE, CONAPO, ONU) y las notas de corpus (por ejemplo, Acemoglu,
  Autor, Beirne y Scott, «Baby Busts and Growth Booms», NBER, 2026).
- `GrandPlan/BDH/`: seguridad social y economía de la salud (pensiones, financiamiento de
  la salud); úsalo para el bloque de pensiones, salud y cuidados de la Parte 3 y para las
  diapositivas 15 y 16 de la Parte 1.
- `Missions/`: la Misión NTA y equidad intergeneracional de ITED.
- `Research/`: trabajos publicados, enviados y en proceso; incluye la presentación para la
  CEPAL (XXXVIII Seminario Regional de Política Fiscal, mayo de 2026) sobre una nueva
  arquitectura de seguridad social y la presentación de pensiones para la CISS (trampa de
  formalización y arquitectura multipilar).
- `Teaching/` y `_crossrefs/`: materiales del curso y el mapa misión–proyecto.

Reglas para usar Dalila:
- Las entradas de corpus siguen PROTO-RAG-001. Prefiere las que tienen `endorsed_by`; si
  usas una con `endorsed_by` vacío, dilo en el reporte (revisión pendiente, no ausente).
- **No presentes como resultado lo que es agenda.** El motor DFD está en construcción:
  muéstralo como programa de investigación (preguntas, arquitectura, primeros pasos), no
  con cifras que no existan.
- **Fecundidad:** los valores de TGF en `_baseline.md` tienen una discrepancia abierta con
  el Observatorio Demográfico 2025 de CELADE para Chile, Costa Rica y México, y está
  pendiente distinguir valores observados de escenarios. **No uses esos valores.** Toma las
  cifras observadas directamente de CELADE (Observatorio Demográfico 2025) o de ONU (World
  Population Prospects 2024), con año y fuente al pie; rotula como «escenario» todo lo
  proyectado.
- Cita los archivos de Dalila en las notas del presentador (`\note{}`), no en pantalla.

### Parte 2: Manual NTA
- **Naciones Unidas (2013), *National Transfer Accounts Manual: Measuring and Analysing the
  Generational Economy*, Departamento de Asuntos Económicos y Sociales, División de
  Población.** **Capítulos 1 y 2**, como en el programa del curso. Según los catálogos:
  cap. 1, «The generational economy: foundations and applications», y cap. 2, «An overview
  of national transfer accounts» (pp. 25–54). Confírmalo en el PDF. Los capítulos
  siguientes (construcción de las cuentas) quedan fuera; a lo sumo, una diapositiva
  opcional que diga qué datos se necesitan.

### Parte 3: CEPAL
- **CEPAL (2025), *Impactos económicos del envejecimiento en América Latina y el Caribe:
  desafíos y oportunidades*.** Fuente única de esta parte. Verifica el título exacto, la
  serie y el año en el PDF.

### Plantilla
- `kaplow_marco_unitario.tex` o `consumo_iva.tex`: hereda el preámbulo (incluido
  `\usepackage[spanish,es-nodecimaldot,es-noaccentedoperators]{babel}`), el tema, los
  colores, el estilo de las gráficas, los bloques y el formato de las preguntas a la clase.

Las fuentes son de consulta: no copies párrafos ni figuras. Las gráficas se redibujan con
los datos.

## Decisiones acordadas
- Portadas: «Cuentas Nacionales de Transferencia y envejecimiento», con el subtítulo de
  cada parte («Parte 1: la transición demográfica», «Parte 2: la economía generacional»,
  «Parte 3: América Latina envejece») y la fecha «Noviembre de 2026».
- Pie de página: «NTA y envejecimiento · Parte N».
- **Términos:** tasa global de fecundidad (TGF); transición demográfica; bono o dividendo
  demográfico (elige uno y sé consistente; primer y segundo dividendo); ciclo de vida
  económico; déficit del ciclo de vida; ingreso laboral; reasignaciones por edad;
  transferencias públicas y privadas; reasignaciones basadas en activos; razón de
  sostén económico (*support ratio*, en inglés solo la primera vez). Usa los términos del
  español que usa CEPAL cuando existan.
- Los perfiles por edad se grafican con la edad en el eje horizontal (0–90+) y, cuando se
  comparan países o años, normalizados (por ejemplo, por el ingreso laboral medio de 30–49
  años, como en NTA).

---

## Parte 1: La transición demográfica y nuestra investigación (≈20 diapositivas · 60 min)

### I. El modelo de transición demográfica (≈9) · 25 min
1. **Portada.**
2. **Por qué empezar por la demografía.** Las finanzas públicas cobran a unas edades y
   gastan en otras; cuando cambia la estructura por edad, cambia todo el presupuesto.
3. **Las fases del modelo.** Gráfica esquemática de natalidad y mortalidad en el tiempo,
   con el crecimiento natural como área entre las curvas. Fase 1: natalidad y mortalidad
   altas. Fase 2: cae la mortalidad. Fase 3: cae la fecundidad. Fase 4: ambas bajas.
   Mención de la llamada «segunda transición» y de la fecundidad bajo el reemplazo.
4. **Fase 2: la mortalidad cae primero.** Por qué (salud pública, nutrición) y qué le hace a
   la pirámide: se ensancha la base.
5. **Fase 3: la fecundidad cae después.** Mecanismos (urbanización, educación de las
   mujeres, costo de los hijos). La velocidad importa.
6. **Fase 4 y lo que sigue.** Fecundidad bajo el reemplazo y envejecimiento.
7. **Las pirámides cuentan la historia.** Tres pirámides de México (por ejemplo, 1970,
   2020 y una proyección a 2050, rotulada como escenario), con datos de ONU o CONAPO.
8. **América Latina envejece más rápido.** Velocidad de la transición frente a Europa:
   años para pasar de 10 % a 20 % de población de 65 y más (verifica con ONU). «Envejecer
   antes de enriquecerse».
9. **El bono demográfico y su fin.** Primer dividendo (más población en edad de trabajar)
   y segundo dividendo (acumulación de activos para la vejez), en intuición. Puente a la
   Parte 2. — Mason y Lee; verifica la referencia.

### II. Lo que hemos investigado (≈9) · 30 min
Contenido tomado de los archivos de Dalila. Ajusta según lo que encuentres.
10. **Las preguntas de ITED.** La agenda: cómo la transición demográfica reordena las
    finanzas públicas en economías de ingreso medio con informalidad alta.
11. **Escenarios de fecundidad: cuando la transición se acelera.** La disciplina de
    escenarios de transición rápida; observado frente a escenario, rotulado así.
12. **El laboratorio DFD.** Arquitectura del motor de simulación en cuatro módulos;
    diagrama propio. Como programa de investigación, no como resultados.
13. **El núcleo: un modelo de generaciones traslapadas.** Estructura de ciclo de vida
    (entrada a los 20 años, retiro exógeno, horizonte de 100 años en periodos de cinco),
    historia contributiva y heterogeneidad de habilidades, según la revisión del modelo
    en Dalila. Una diapositiva, sin álgebra.
14. **Automatización y envejecimiento.** La nota de corpus sobre «Baby Busts and Growth
    Booms»: la pregunta del umbral de automatización en economías de ingreso medio con
    informalidad alta.
15. **Seguridad social para una población que envejece.** La presentación para la CEPAL
    (mayo de 2026): dos ejes de reforma, financiamiento de la salud y consolidación de
    transferencias en un impuesto negativo al ingreso.
16. **Pensiones: la trampa de la formalización.** La presentación para la CISS: el efecto
    escalón y la arquitectura multipilar («el cero se habla con el uno, el dos con el
    tres»).
17. **La Misión NTA y equidad intergeneracional.** Qué mide y para qué; puente directo a
    la Parte 2.
18. *(opcional)* **Cómo trabajamos.** El corpus con procedencia citada y el equipo de
    agentes como herramienta de investigación; enlace con la persona de investigación que
    construyen los alumnos en el curso.

### III. Cierre (2) · 5 min
19. **Tres ideas para llevarse.**
20. **Pregunta para la Parte 2.** «Si cada edad consume distinto de lo que produce, ¿quién
    paga la diferencia?»

---

## Parte 2: La economía generacional — Manual NTA, caps. 1 y 2 (≈20 diapositivas · 60 min)

Esquema provisional; corrígelo contra el texto.

### I. La economía generacional: fundamentos y aplicaciones (≈8) · 22 min — cap. 1
1. **Portada.**
2. **Consumimos toda la vida y producimos solo una parte.** Perfiles estilizados de
   consumo e ingreso laboral por edad; déficit en la infancia y la vejez, superávit en la
   edad de trabajar. Gráfica propia.
3. **Qué es la economía generacional.** Producción, consumo, reparto y ahorro vistos por
   edad; por qué las cuentas nacionales tradicionales no lo muestran.
4. **Tres formas de cubrir el déficit.** Transferencias públicas, transferencias privadas
   (familia) y activos (ahorro, crédito, propiedad). Diagrama.
5. **Instituciones distintas, mezclas distintas.** Cómo varía entre países el peso de la
   familia, el Estado y los activos para sostener a niños y personas mayores, según el
   capítulo.
6. **La razón de sostén.** Productores efectivos entre consumidores efectivos, ponderados
   con los perfiles por edad; definición formal.
7. **Los dos dividendos.** El primero como la tasa de crecimiento de la razón de sostén; el
   segundo, por la acumulación de activos para la vejez. Conecta con la Parte 1.
8. **Para qué sirve: aplicaciones.** Sostenibilidad fiscal, equidad entre generaciones,
   pensiones y salud, inversión en capital humano: las que el capítulo destaque. Pregunta
   (último overlay).

### II. El panorama de las cuentas (≈10) · 33 min — cap. 2
9. **Qué miden las NTA.** Flujos económicos por edad, consistentes con el Sistema de
   Cuentas Nacionales; diferencias con el SCN que el capítulo señale.
10. **La identidad de flujos.** Consumo − ingreso laboral = transferencias netas +
    reasignaciones basadas en activos, en la notación del Manual. Derivación corta con
    overlays.
11. **El ciclo de vida económico.** Consumo público y privado (educación, salud, resto) e
    ingreso laboral (asalariados y autoempleo).
12. **El déficit del ciclo de vida.** Edades de cruce; cómo se agrega por población.
13. **Reasignaciones públicas.** Impuestos y beneficios por edad: quién paga y quién
    recibe. Destaca que, en la vejez, las pensiones y la salud son el grueso de lo que
    recibe cada persona: es la base del bloque central de la Parte 3.
14. **Reasignaciones privadas.** Transferencias dentro y entre hogares.
15. **Reasignaciones basadas en activos.** Ingreso de activos menos ahorro.
16. **Población × perfiles = agregados.** Cómo la estructura por edad convierte perfiles
    en presiones agregadas.
17. **Comparaciones entre países.** Perfiles normalizados de algunos países, si el
    capítulo los trae; si no, usa datos de ntaccounts.org y cítalos.
18. *(opcional)* **Qué datos se necesitan.** Encuestas de ingreso y gasto, cuentas
    nacionales y registros administrativos; para México, ENIGH, el SCN del INEGI y la
    Cuenta Pública (verifica los nombres).

### III. Cierre (2) · 5 min
19. **Lo que cambia para las finanzas públicas.** El presupuesto como un sistema de
    reasignaciones por edad; enlace con Kaplow (un modelo estático) y con la sesión macro
    del 10 de noviembre.
20. **Pregunta para la Parte 3.** «¿Qué le pasa a ese sistema cuando la población
    envejece rápido?»

---

## Parte 3: América Latina envejece — CEPAL (2025) (≈20 diapositivas · 60 min)

El esquema sale del informe. Estructura sugerida; ajústala a los capítulos del documento.
**Pensiones, financiamiento de la salud y cuidados son el centro de esta parte**: tienen
bloque propio, con la lente de las NTA (Parte 2) y la mirada de México.
1. **Portada.**
2. **El mensaje del informe en una diapositiva.**
3–4. **La dinámica demográfica de la región**, breve porque ya se vio en la Parte 1: ritmo
   de envejecimiento, diferencias entre países y fin del bono demográfico, con datos del
   informe.
5–6. **Impactos económicos:** crecimiento, mercado laboral, ahorro y consumo; lo que el
   informe estime con NTA, si lo hace (enlace con la Parte 2).

### Bloque central: pensiones, salud y cuidados (≈8 diapositivas · 25 min)
7. **Tres presiones que crecen al mismo tiempo.** Gasto por edad en pensiones, salud y
   cuidados: el perfil de reasignaciones públicas de la Parte 2 multiplicado por una
   población que envejece. Gráfica con datos del informe o de NTA.
8. **Pensiones: cobertura y suficiencia.** Brecha de cobertura por la informalidad;
   suficiencia de los beneficios; peso de las pensiones no contributivas. Lo que diga el
   informe para la región.
9. **Pensiones en México.** Reforma de 2020 (la cuota patronal de la sesión del 26 de
   septiembre), pensión no contributiva para personas adultas mayores y Fondo de Pensiones
   para el Bienestar: verifica diseño y fechas en fuentes oficiales. Enlace con la trampa
   de formalización de la Parte 1.
10. **Salud: el gasto sube con la edad.** Perfil del gasto en salud por edad; enfermedades
    crónicas; gasto de bolsillo y protección financiera. Lo que diga el informe.
11. **Financiamiento de la salud.** Fragmentación entre esquemas contributivos y no
    contributivos; fuentes de financiamiento; enlace con el eje de salud de la presentación
    para la CEPAL de la Parte 1. México: verifica cifras de gasto público y de bolsillo.
12. **Cuidados: la demanda que nadie presupuesta.** Dependencia y cuidados de largo plazo;
    trabajo de cuidado no remunerado, sobre todo de mujeres; menos cuidadoras potenciales
    por familia cuando cae la fecundidad.
13. **El tiempo también se transfiere.** Las cuentas nacionales de transferencias de tiempo
    (NTTA) miden el cuidado no remunerado por edad y sexo; verifica la referencia del
    manual de la ONU antes de citarlo. Si el informe trae cifras, úsalas.
14. **Cómo se paga todo junto.** Presión fiscal combinada de pensiones, salud y cuidados
    bajo los escenarios del informe; enlace con la arquitectura de seguridad social de la
    Parte 1 (dos ejes de reforma) y con la sesión de deuda del 10 de noviembre. Pregunta
    (último overlay): «Si solo pudieran reformar uno de los tres, ¿cuál y por qué?»

### Recomendaciones, México y cierre
15–16. **Oportunidades y recomendaciones del informe**, presentadas como del informe.
17. **México en el informe:** cifras y posición relativa, solo lo que el informe traiga.
18. *(opcional)* **Economía plateada:** oportunidades del envejecimiento que el informe
    destaque (consumo, empleo en cuidados, trabajo de personas mayores).
19. **Lectura crítica.** Qué deja abierto el informe; conexión con la agenda de la Parte 1
    (escenarios de fecundidad, el laboratorio DFD, la nueva arquitectura de seguridad
    social). Pregunta (último overlay) para discutir.
20. **Cierre de la sesión.** Ideas centrales de las tres partes y puente al 10 de
    noviembre: deuda, sostenibilidad y la tasa de interés frente al crecimiento cuando la
    población envejece.

---

## Construcción
- LaTeX Beamer 16:9 con el preámbulo de la plantilla.
- Gráficas en TikZ/pgfplots con el estilo común: transición demográfica, pirámides,
  perfiles por edad, razón de sostén. Nada extraído de los PDF; si una gráfica necesita
  datos, usa los de la fuente y cítalos al pie.
- Derivaciones paso a paso con overlays, una por diapositiva, máximo 4–5 líneas. Nada por
  debajo de `\small`.
- Preguntas a la clase como último overlay, nunca como diapositiva aparte. Al menos dos por
  presentación.
- **Notas del curso:** en la versión para repartir, cada diapositiva debe entenderse sin
  exposición. Si hace falta contexto, ponlo en una línea al pie, no en un párrafo.
- **Cifras:** verifica cada cifra contra su fuente (CELADE, ONU, CONAPO, INEGI, el Manual,
  el informe). Lo que no logres verificar, **quítalo de la diapositiva** y anótalo en el
  reporte. No debe quedar ningún [VERIFICAR] en pantalla.
- Entregables sin errores ni cajas desbordadas. Revisión visual: convierte las páginas a
  imágenes y corrige texto que se salga, elementos encimados o etiquetas ilegibles.

## Idioma: que suene a persona, no a máquina (importa tanto como el contenido)
El texto debe sonar como lo diría un profesor mexicano de economía frente a su grupo.
Escribe directamente en español; no traduzcas el Manual frase por frase.
- Frases cortas, con sujeto y verbo; títulos que dicen el resultado («La mortalidad cae
  primero»; «Consumimos toda la vida y producimos solo una parte»).
- Ejemplos cotidianos antes que abstracciones: la colegiatura, la consulta médica, la
  pensión del abuelo, el dinero que mandan los hijos.
- Voz activa: «los hijos sostienen a los padres», no «se observa un flujo de recursos».
- Sin muletillas: «es importante destacar», «cabe señalar», «en este sentido», «en el marco
  de», «clave», «crucial», «fundamental», «robusto», «integral», «abordar», «explorar»,
  «profundizar», «potenciar», «desafíos y oportunidades» como muletilla, «en resumen» al
  abrir una diapositiva.
- Sin series de tres adjetivos por costumbre, sin viñetas idénticas en forma y sin
  transiciones vacías («Veamos ahora…»).
- Sin calcos: «suponer», no «asumir»; «papel», no «rol»; «afectar», no «impactar»; «a la
  larga», no «eventualmente».
- Trato de «ustedes». En la Parte 1, cuando se hable de la investigación propia, primera
  persona del plural («hemos encontrado», «nuestra pregunta»).

Al terminar cada presentación, relee todo de corrido **solo** para revisar el idioma. En
cada diapositiva, pregúntate si así lo diría el profesor en voz alta; si no, reescríbela.

## Reporte final
Por cada parte: lista de diapositivas con su fuente, diapositivas opcionales y sus minutos,
cifras verificadas con su fuente, lo que quitaste por no poder verificarlo, archivos de
Dalila usados (y si estaban respaldados con `endorsed_by`) y cualquier desviación del
esquema aprobado.
