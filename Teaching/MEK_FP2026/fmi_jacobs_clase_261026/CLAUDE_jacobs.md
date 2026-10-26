# Encargo: presentación Beamer — Jacobs, «Digitalization and Taxation»

## Contexto
Curso de Finanzas Públicas, Maestría en Economía Aplicada, Escuela de Gobierno y
Transformación Pública, Tec de Monterrey. Profesor: Héctor Juan Villarreal.
Sesión «Buscando un marco unitario para el sistema fiscal / Digitalización de las finanzas
públicas». **Segunda sección de la clase de hoy: 60 minutos, sin descanso.** Llega justo
después de 90 minutos sobre Kaplow, capítulos 1 a 3 (marco integrado, reforma
distributivamente neutral, objetivo social). Un solo PDF debe servir en presencial y en
línea.

**El capítulo es muy técnico. La presentación pone el énfasis en las aplicaciones.** La
teoría (teoremas del bienestar y el problema de información) da el hilo, en pocas
diapositivas y con intuición; el peso está en qué cambia, en la práctica, cuando el
gobierno sabe más. Proporción orientativa: 40 % teoría y 60 % aplicaciones.

Lo que los alumnos ya vieron y aquí se retoma:
- Kaplow (la primera sección de hoy): en Mirrlees la restricción es de información; el
  impuesto al ingreso como instrumento redistributivo; la diapositiva «¿Y en México?»
  sobre un instrumento redistributivo débil.
- IVA (12–13 de octubre): cobro fraccionado y huella documental, pago fraccionado en
  Brasil, IVA personalizado y cashback de Barreix, la nota 28 del FMI y su recuadro 1
  sobre impuestos individuales al consumo, Atkinson-Stiglitz.
- Incidencia (26 de septiembre): informalidad y traslado.

## Entregables obligatorios
**El producto es el PDF compilado, no solo el .tex.** Al terminar deben existir, compilados
con `latexmk -pdf`:
- `jacobs_digitalizacion.pdf` y `jacobs_digitalizacion_handout.pdf`
  (`\documentclass[handout]{beamer}`).
- `jacobs_digitalizacion.tex`, por si hay que corregir.

Si la compilación falla, corrige y vuelve a compilar; no entregues un .tex sin su PDF.

## Fases y tiempos
**Fase 1 (meta: 13:00) — esquema, y detente.** Lee el capítulo completo y escribe
`esquema_jacobs.md`: lista numerada de diapositivas con título, una línea de contenido y
**la sección y página del capítulo que la respalda**. Parte del esquema provisional de
abajo, pero corrígelo contra el texto: se armó sin el capítulo a la mano. Reemplaza los
temas que el capítulo no trate por los que sí trata, y señala lo que venga de otra fuente.
Espera aprobación.

**Fase 2 (meta: 16:30) — construcción**, solo después de aprobar el esquema.

## Fuentes (en esta carpeta)
- **Jacobs, B. (2017), «Digitalization and Taxation», cap. 2 en S. Gupta, M. Keen, A. Shah
  y G. Verdier (eds.), *Digital Revolutions in Public Finance*, Fondo Monetario
  Internacional.** Fuente principal: conceptos, argumentos y notación salen de aquí.
  Verifica en el PDF los datos bibliográficos exactos.
- **Barreix, Rocha y Tostes Neto (2025)**, CIATBlog, y la nota larga en .docx: pago
  fraccionado, cashback, factura electrónica, Devolve ICMS.
- **de Mooij, Hebous y Keen (2025)**, IMF WP/25/165: recuadro 1 (impuestos individuales al
  consumo) y nota 28 (IVA personalizado de Barreix et al. e IVA progresivo de de la Feria y
  Swistak).
- **`kaplow_marco_unitario.tex`** (si ya existe) o **`consumo_iva.tex`**: plantilla.
  Hereda el preámbulo (incluido
  `\usepackage[spanish,es-nodecimaldot,es-noaccentedoperators]{babel}`), el tema, los
  colores, el estilo de las gráficas, los bloques y el formato de las preguntas a la clase.

Las fuentes son de consulta: no copies párrafos ni figuras. Las gráficas se redibujan.

## Decisiones acordadas
- Pie de página: «Digitalización · Jacobs (2017)». Portada: «Digitalización e impuestos:
  ¿qué cambia cuando el gobierno sabe más?», con la fecha «Octubre de 2026».
- Notación: la de Jacobs, empatada en una línea con la de Kaplow de la primera sección.
- Términos: «primer y segundo teoremas del bienestar», «impuestos de suma fija
  individualizados», «primer mejor» y «segundo mejor», «etiquetado» (*tagging*, en inglés
  solo la primera vez), «reporte de terceros», «factura electrónica», «pago fraccionado»,
  «IVA personalizado».
- Remite a la primera sección así: «Kaplow, diap. N». A sesiones anteriores: «sesión del
  IVA, diap. N».

---

## Esquema provisional (17 diapositivas · 60 min)

### I. El problema de fondo es de información (5) · 20 min
1. **Portada.**
2. **De Kaplow a Jacobs.** Kaplow dejó una idea: en Mirrlees, la restricción es de
   información. El gobierno no ve la capacidad, solo el ingreso. Pregunta de hoy: ¿qué pasa
   cuando la digitalización le deja ver más?
3. **Los teoremas del bienestar, en una diapositiva.** Primero: el equilibrio competitivo es
   eficiente. Segundo: cualquier asignación eficiente se alcanza con transferencias de suma
   fija y mercados. Si existieran, eficiencia y equidad no chocarían.
4. **Por qué no hay suma fija individualizada.** Gravar la capacidad requiere observarla; el
   gobierno grava lo que ve (ingreso, consumo) y eso distorsiona. De ahí sale la disyuntiva
   entre equidad y eficiencia: es un problema de información, no de preferencias. Gráfica
   propia: frontera de primer mejor y de segundo mejor.
5. **Qué puede cambiar la digitalización.** Tres canales, según los organice el capítulo:
   (i) observar más características (etiquetado), (ii) medir mejor las bases existentes
   (reporte de terceros, menos evasión), (iii) hacer viables instrumentos nuevos
   (impuestos personalizados al consumo, transferencias focalizadas). Mapa del resto de la
   presentación.

### II. Aplicaciones (10) · 35 min
6. **Etiquetado: gravar lo que se ve y se correlaciona con la capacidad.** Akerlof (1978) en
   una línea; ejemplos (edad, discapacidad, ubicación). Límites: equidad horizontal (enlace
   con Kaplow, diap. 19), manipulación de la señal y privacidad. Pregunta (último overlay):
   «¿Qué etiqueta les parecería legítima y cuál no?»
7. **Reporte de terceros: la evasión cae cuando alguien más informa.** La factura
   electrónica como reporte de terceros masivo. Evidencia que cite el capítulo; si citas
   otra, verifícala.
8. **México: la factura electrónica (CFDI).** Obligatoria y generalizada; el SAT cruza
   emisor y receptor; declaraciones prellenadas. Verifica fechas y alcance en fuentes
   oficiales (SAT, CFF). Lectura con el cobro fraccionado de la sesión del IVA (diap. 5).
9. **Brasil: el pago fraccionado, de la factura al pago.** Retoma la sesión del IVA
   (diap. 20): el fisco cobra en el momento de la liquidación, con consulta previa de
   créditos; sistemas de pago como Pix. Del lado de la teoría: la digitalización acerca el
   cumplimiento a uno automático.
10. **Impuestos personalizados al consumo.** Con identidad digital y pago electrónico, el IVA
    puede depender de quién compra. Recuadro 1 del FMI; IVA progresivo de de la Feria y
    Swistak (2024). Contraste con Atkinson-Stiglitz: si el impuesto al ingreso funciona, la
    personalización del IVA sobra; si no funciona (informalidad), puede servir.
11. **El IVA personalizado de Barreix: la conexión directa.** Base amplia y tasa uniforme,
    con devolución a los hogares de menor ingreso, calibrada por la factura y los medios de
    pago electrónicos. Cashback en Brasil; Devolve ICMS en Rio Grande do Sul. Es el canal
    (iii) llevado a la práctica, y responde a la pregunta de la diapositiva «¿Y en
    México?» de Kaplow.
12. **Transferencias focalizadas con identidad digital.** Lo que el capítulo diga sobre
    transferencias y focalización; si no lo trata, una línea con un ejemplo verificado
    (por ejemplo, Aadhaar en India) y la fuente.
13. **Bases que se vuelven gravables.** Rentas del capital y riqueza con intercambio
    automático de información entre países, y la economía digital (plataformas). México:
    IVA a servicios digitales de plataformas extranjeras; verifica el año y el diseño en la
    LIVA. Ajusta según lo que trate el capítulo.
14. **Los riesgos.** Privacidad y confianza; nuevas formas de fraude (facturas falsas en
    México: las «empresas fantasma»; verifica con fuente oficial); capacidad institucional;
    exclusión de quien no tiene cuenta ni identidad digital. Pregunta (último overlay):
    «¿Qué información no le darían al SAT?»
15. **Lo que la digitalización no resuelve.** La capacidad sigue sin verse: el problema de
    Mirrlees se reduce, no desaparece. La conducta responde a lo que se grava. Según el
    capítulo, qué distorsiones quedan.

### III. Cierre (2) · 5 min
16. **Tres ideas para llevarse.** La disyuntiva entre equidad y eficiencia es, en el
    fondo, de información; la digitalización mueve la frontera de lo posible; los
    instrumentos nuevos (IVA personalizado, pago fraccionado) solo valen si hay capacidad y
    confianza.
17. **Puente.** Próxima sesión, 3 de noviembre: cuentas nacionales de transferencia y
    envejecimiento. La información por edad es otra dimensión que el sistema fiscal empieza
    a ver.

Ritmo: cada idea teórica en una diapositiva, con intuición y a lo sumo una ecuación; cada
aplicación con un caso concreto (México primero, luego Brasil o la región).

---

## Construcción
- LaTeX Beamer 16:9 con el preámbulo de la plantilla.
- Gráficas en TikZ/pgfplots con el estilo común. Diagramas de flujo para la factura
  electrónica y el pago fraccionado. Nada extraído de los PDF.
- Teoría: **a lo sumo una derivación** en toda la presentación, con overlays y en 4–5
  líneas. Lo demás, intuición y gráficas.
- Preguntas a la clase como último overlay, nunca como diapositiva aparte.
- Al pie de cada diapositiva, la sección del capítulo que la respalda (por ejemplo,
  «Jacobs, sec. 3»).
- **Cifras y hechos de México y de la región:** verifica en la web cada cifra, fecha y
  diseño. Lo que no logres verificar, **quítalo de la diapositiva** y anótalo en el
  reporte. No debe quedar ningún [VERIFICAR] en pantalla.
- Entregables sin errores ni cajas desbordadas. Revisión visual: convierte las páginas a
  imágenes y corrige texto que se salga, elementos encimados o etiquetas ilegibles.

## Idioma: que suene a persona, no a máquina (importa tanto como el contenido)
El texto debe sonar como lo diría un profesor mexicano de economía frente a su grupo.
Escribe directamente en español; no traduzcas a Jacobs frase por frase.
- Frases cortas, con sujeto y verbo; títulos que dicen el resultado («La evasión cae
  cuando alguien más informa»).
- Ejemplos cotidianos antes que abstracciones: la factura al pagar la comida, el pago con
  el celular, la devolución que llega a la cuenta.
- Voz activa: «el SAT cruza las facturas», no «se realiza el cruce de información».
- Sin muletillas: «es importante destacar», «cabe señalar», «en este sentido», «en el marco
  de», «clave», «crucial», «fundamental», «robusto», «integral», «abordar», «explorar»,
  «profundizar», «potenciar», «transformación digital» como muletilla, «en resumen» al
  abrir una diapositiva.
- Sin series de tres adjetivos por costumbre, sin viñetas idénticas en forma y sin
  transiciones vacías («Veamos ahora…»).
- Sin calcos: «suponer», no «asumir»; «papel», no «rol»; «afectar», no «impactar»;
  «digitalización», no «digitalizar» como sustantivo.
- Trato de «ustedes».

Al terminar, relee todo de corrido **solo** para revisar el idioma. En cada diapositiva,
pregúntate si así lo diría el profesor en voz alta; si no, reescríbela.

## Reporte final
Lista de diapositivas con su sección del capítulo, cifras y hechos verificados con su
fuente, lo que quitaste por no poder verificarlo, temas del esquema provisional que el
capítulo no trata y cualquier desviación del esquema aprobado.
