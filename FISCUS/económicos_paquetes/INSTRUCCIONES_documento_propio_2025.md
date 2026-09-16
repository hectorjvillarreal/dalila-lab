# Instrucción de trabajo — Documento propio, ejercicio 2025

**Proyecto:** FISCUS
**Ubicación:** `FISCUS/económicos_paquetes/`
**Máquina:** Dalila
**Tipo:** instrucción de trabajo (no es build instruction registrada)
**Ejercicio:** 2025 · **Producto:** documento completo del género, de autoría ITED
**Antecedentes:** cinco corridas de evaluación (2020 pensiones, 2021 salud,
2022 ingresos, 2023 deuda, 2024 educación).

---

## 0. Esto es un cambio de producto

Las cinco corridas anteriores **evaluaron**. Esta **produce**.

El entregable es un documento completo sobre el Paquete Económico 2025, del mismo
género que las *Implicaciones* del CIEP, escrito por ITED, en dos formatos:
Markdown y LaTeX compilable. Al final —y solo al final— se compara contra el
documento del CIEP.

El criterio de éxito ya no es la tasa de aciertos. Es si el objeto resiste ser
leído por alguien de fuera.

**Nota de calendario, importante.** El Paquete Económico 2025 se entregó el
**15 de noviembre de 2024**, no el 8 de septiembre, por cambio de administración.
Es el único de la serie con esa fecha. Es el primer paquete del gobierno
entrante. Eso afecta la cronología, el fechado del documento de CIEP y cualquier
comparación de plazos: verifícalo, no lo asumas.

---

## 1. Criterios de aceptación

Tres. Los tres deben cumplirse; ninguno compensa a otro.

**1.1 Reconocimiento de género.** Un lector habitual de las *Implicaciones* —no
alguien de CIEP, un lector— debe reconocerlo como un documento de ese género:
misma arquitectura en tres partes, misma plantilla de capítulo, mismo registro,
densidad comparable de cuadros y figuras. Un lector así no juzga por la
tipografía; juzga porque el capítulo de pensiones responde las preguntas que
espera, en el orden que espera, con el tipo de cuadro que espera. **Es contenido,
no diseño.**

**1.2 Autoría ITED, visible e inconfundible.** Original quiere decir **de ITED**,
no anónimo. Portada, autoría, fecha y filiación propias. **El documento nunca
puede pasar por uno de CIEP**, ni por descuido de un lector distraído. CIEP e
ITED son aliadas y precisamente por eso la procedencia debe ser inequívoca: si el
objeto sale bien y luego circula suelto, la confusión sería un problema real para
las dos casas.

Corolario de corpus: toda cifra lleva su tier declarado. Donde se cite a CIEP
—que se puede— se cita como `derivada_ciep`, con documento y página. Lo que
perderíamos si no, es la distinción que llevamos cinco corridas construyendo.

**1.3 Compila en Overleaf sin intervención.** Desde cero, sin ajustes manuales,
sin `shell-escape`, con lo que Overleaf trae de fábrica. **Si no compila, no está
terminado**, por bueno que sea el contenido.

---

## 2. Los cinco mecanismos

Estos son los que hacen que el ejercicio funcione. No son recomendaciones.

### 2.1 Pacto de estructura, sellado antes de abrir nada

**Antes** de mirar el paquete 2025 y muy especialmente antes de abrir el
documento de CIEP 2025, escribe y **cierra** `pacto_estructura.md`:

- Índice de capítulos, con su parte del documento.
- Las preguntas que cada capítulo responde.
- Las comparaciones estructurales que aparecerán y en qué capítulo.
- Los cuadros y figuras previstos, con el dato que cada uno necesita.

**Sellado significa sellado.** Registra la hora. Si después hay que cambiarlo, el
cambio se registra con su motivo en `pacto_estructura.md`, y esa lista de cambios
es información sobre el ejercicio, no un trámite.

Razón: después de cinco corridas leyendo a CIEP, "parecido a CIEP" es una
invitación a reproducirlo de memoria. El pacto es lo que impide que el documento
se convierta en el de CIEP con enmiendas.

### 2.2 Presupuesto de afirmaciones, por capítulo

Antes de redactar cada capítulo, declara cuántas afirmaciones verificables
sostiene con la carpeta disponible.

**Umbral:** un capítulo necesita al menos **doce afirmaciones cuantitativas
verificables**, de las cuales al menos **seis sean restitución de fuente oficial
primaria**, y no más del **30 %** de sus afirmaciones pueden quedar
`no_verificable`.

Si no llega al umbral, **el capítulo se declara no redactable y esa declaración
se publica en su lugar**, compilada como una página del documento, escrita en el
registro del documento y no como nota técnica: qué se quiso decir, qué fuente
haría falta, por qué no está.

Nueve capítulos y tres declaraciones de imposibilidad es un resultado honesto.
Doce capítulos de los que cuatro son relleno elegante es un fracaso disfrazado
que además pasa desapercibido. **La fluidez de la prosa no es evidencia de
verificación.**

### 2.3 Datos separados de prosa

Ninguna cifra se teclea en el cuerpo del texto y ninguna figura es una imagen
pegada.

```
documento_2025/
  datos/
    _fuentes.csv          # registro: archivo, documento, cuadro, página, tier
    ingresos_art1o.csv
    gasto_funcion.csv
    ...
```

Cada archivo de datos tiene su fila en `_fuentes.csv` con documento, cuadro,
página y tier. Las figuras se generan con `pgfplots` leyendo esos `.csv`. Los
cuadros se generan desde los mismos archivos.

Efecto buscado: **la gráfica se vuelve verificable como una cifra**, y el
documento se puede reejecutar en 2026 y 2027 cambiando los datos y no el texto.

### 2.4 LaTeX que compile de verdad

```
documento_2025/
  main.tex
  capitulos/00_resumen.tex, 01_....tex, ...
  datos/
  figuras/            # solo si algo no puede hacerse con pgfplots
  bibliografia.bib
```

- `pdflatex`, sin `shell-escape`.
- Paquetes admitidos: `babel` (spanish), `geometry`, `fancyhdr`, `booktabs`,
  `siunitx`, `pgfplots` (con `\pgfplotsset{compat=1.18}`), `graphicx`,
  `hyperref`, `caption`, `longtable`.
- **Prohibidos:** `minted` y cualquier cosa que requiera `shell-escape`; fuentes
  no incluidas en Overleaf; paquetes que haya que instalar.
- Números en español: separador de miles y decimal configurados una vez en
  `siunitx`, aplicados en todo el documento.

**Prueba de aceptación:** compila desde cero, dos pasadas, sin errores. Reporta
warnings. Si no compila, el capítulo que rompe se aísla y se reporta; no se
entrega un proyecto roto.

### 2.5 La pregunta incómoda, al final

En la comparación contra CIEP, además de los cuatro apartados de siempre, uno
nuevo: **qué afirmaciones propias se sostienen solo porque CIEP las dijo antes.**

Se busca explícitamente, no se confía en que no ocurrió. Después de cinco
corridas leyendo ese documento, la contaminación es el riesgo real.

---

## 3. Arquitectura del documento

Tres partes, como el género: **(+) Ingresos**, **(−) Gasto**, **(=) Balance y
Deuda**. La restricción presupuestal del gobierno usada como índice.

Plantilla por capítulo de rubro: **POLÍTICA / EVOLUCIÓN / PROGRAMAS
SELECCIONADOS / IMPLICACIONES.** El juicio va en IMPLICACIONES; las secciones
descriptivas describen.

**La Parte III va.** Un lector del género nota de inmediato si falta, y es donde
el documento se distingue: la descomposición de cuatro variables sobre la razón
SHRFSPF/PIB no existe en el género.

Índice sugerido, a fijar en el pacto: resumen; marco macroeconómico; ingresos;
gasto total; salud; educación; pensiones; inversión; energía; seguridad; gasto
federalizado; balance y deuda.

### 3.1 Las comparaciones estructurales de la casa

Son lo que hace que el documento sea de ITED y no una imitación. Todas con
perímetro declarado y las dos líneas donde aplique:

| Capítulo | Comparación | Serie conocida |
|---|---|---|
| Ingresos | Tributarios / gastos obligatorios (con y sin cuotas IMSS) | 0.671 (2021), 0.674 (2022) |
| Gasto total | Pensiones + costo financiero / tributarios | 0.60 (2023) |
| Pensiones | Pensiones IMSS / cuotas IMSS (serie aprobada) | 1.545, 1.594, 1.627 |
| Salud | Cuotas obrero-patronales / gasto en salud IMSS | 0.85 (2021) |
| Educación | Educación / pensiones y jubilaciones (clas. económica) | 0.709 → 0.689 |
| | segunda línea: / pensiones totales | 0.558 → 0.518 |
| Deuda | Costo financiero / tributarios; SHRFSPF / tributarios en años | 0.20→0.23; 3.6→3.4 |

Extiéndelas a 2025 con base consistente. **Nunca una línea híbrida:** ex ante con
ex ante, aprobado con aprobado.

### 3.2 El capítulo de deuda

Descomposición del cambio de la razón SHRFSPF/PIB en las cuatro variables:
crecimiento, tasa de interés real, inflación y tipo de cambio. **Con el criterio
de aceptación de 2023:** debe reproducir la caída de 2022 (RFSPF de 4.5 % del PIB
con el acervo bajando de 50.7 a 49.4 %) antes de aplicarse a 2025.

No presentes el marco de manual (primario más r−g). Retirado por sesgo
sistemático; diagnóstico interno en bitácora, nunca en el documento.

### 3.3 El horizonte demográfico

Es lo nuestro y es donde el documento aporta algo que el género no trae.

La tríada de NTA está completa y su hallazgo transversal es una asimetría: **el
paquete tiene horizonte demográfico donde la demografía presiona al alza
—pensiones, 65+ de 8.2 % en 2023 a 17.0 % en 2050— y no lo tiene donde presiona a
la baja**, que es educación. Si en 2025 se repite, dilo con la fuente. Si cambió,
es noticia.

---

## 4. Convenciones vigentes

Todas las de las cinco corridas, sin excepción.

Nomenclatura **RFSPF/SHRFSPF** con equivalencia declarada una vez. Deflactor del
PIB, con excepción marcada para prestaciones individuales, **nunca derivado de
agregados redondeados**. Las **cinco declaraciones** del contrafactual: nominal o
real, contra aprobado o contra cierre, contra año previo o contra PIB, en pesos
de qué año, y con qué PIB de qué añada. Ex ante contra ex ante. Perímetro
declarado antes del primer cuadro y constante dentro del capítulo. Prohibición de
yuxtaponer magnitudes sin mecanismo declarado. Definiciones adjudicadas contra
*Balance Fiscal en México* (SHCP, abril 2023), nunca por criterio propio.

**Y una regla propia que este documento estrena:** toda diferencia expresada en
millones de pesos **declara si es nominal o real**. El género no lo hace —en
2024, ocho de ocho renglones verificados eran reales sin decirlo, y eso produjo
una afirmación falsa sobre una cifra aprobada por la Cámara—. Nosotros lo
declaramos siempre.

---

## 5. Secuencia

### Fase 0 — Lectura local y pacto. Sin red, sin CIEP.

Lee `_aprendizaje/` completo y los artefactos de las cinco corridas. Escribe y
**sella** `pacto_estructura.md` (§2.1). Registra la hora.

**No abras el documento de CIEP 2025 hasta la fase 5.** Registra también la hora
de esa primera apertura. Si el orden se rompió, el ejercicio pierde su control y
hay que decirlo.

### Fase 1 — Adquisición, no bloqueante

**Regla de no bloqueo:** dos intentos por pieza; si falla, se registra la ruta y
la respuesta del servidor, y **la corrida continúa**. Entrega degradada antes que
no entrega.

Piezas: CGPE, ILIF y decreto 2025; LIF aprobada 2025; analíticos del PEF aprobado
2024 y 2025 (Gobierno Federal y entidades, los cuatro cortes de cada año).

Notas de operación ganadas en corridas previas:
- Prepara el bundle de certificados TLS antes de descargar (hoja firmada por el
  intermedio YR1; el servidor envía R10). **No desactives la verificación.**
- **Los analíticos traen los datos en la hoja `Hoja1`,** no en la primera hoja,
  que es un resumen de 45 filas por ramo y hace creer que el archivo está vacío.
- La exposición de motivos del PPEF 2022–2026 **está caída en el servidor, no
  ausente del portal**: las subpáginas responden 200 y la enumeran, los archivos
  dan 404, Wayback no la tiene. Resonda una vez y sigue.
- El PDF de la ILIF **contiene su exposición de motivos** (verificado 2018–2026).
  No la busques como pieza separada.

### Fase 2 — Inventario y construcción de datos

Inventario del paquete 2025 con documento, cuadro y página. Diffs de códigos de
programa, unidad responsable y subfunción 2024 → 2025, y del Anexo 3 del decreto.
Reconciliaciones: ILIF ↔ CGPE en ingresos; suma por ramos ↔ suma por función;
flujo contra acervo.

**Construye `datos/` completo antes de redactar**, con su `_fuentes.csv`. Un
capítulo no se empieza sin sus datos: es lo que hace exigible el presupuesto de
afirmaciones.

**Lee las figuras del paquete como imágenes cuando no tengan capa de texto.**
Renderizar la página y leer los rótulos es un paso explícito, no un recurso de
emergencia: en 2024 de ahí salió el hallazgo principal.

### Fase 3 — Redacción

Capítulo por capítulo. Para cada uno, en este orden: declarar el presupuesto de
afirmaciones; si no llega al umbral, escribir la declaración de no redactable y
pasar al siguiente; si llega, redactar contra el pacto.

Cada afirmación con fuente. Cada comparación con las cinco declaraciones. Cada
diferencia en mdp declarando si es nominal o real.

### Fase 4 — LaTeX y compilación

Construye el proyecto, compila, corrige hasta que pase la prueba de §2.4.
Entrega también la versión Markdown, generada del mismo contenido.

### Fase 5 — Comparación contra CIEP 2025

**Ahora sí** abre el documento de CIEP. Registra la hora.

`comparacion_2025.md`, cinco apartados:

1. **Coincidencias.**
2. **Lo que CIEP tiene y nosotros no.** Por cada cosa: dónde estaba el dato y por
   qué no llegamos a él. Esto es lo que sustituye al comparador que **no
   tendremos el martes**: la lista de omisiones recurrentes se vuelve la
   checklist de 2027. Regístralas con detalle, no solo cuéntalas.
3. **Lo que nosotros tenemos y CIEP no.**
4. **Diferencias de método.** Sin declarar ganador.
5. **Contaminación (§2.5).** Qué afirmaciones propias se sostienen solo porque
   CIEP las dijo antes.

Verifica también las cifras de CIEP 2025 contra las fuentes, con el CSV de
siempre, pero **esto es secundario en esta corrida**. El producto es el documento.

### Fase 6 — Aprendizaje

`especificacion_genero.md` — qué se aprendió al **escribir** el género y no solo
al leerlo. Qué resultó más difícil de imitar. Qué convenciones del género
resultaron indefendibles al intentar aplicarlas.

`mapa_fuentes.md`, `rubrica.md` — como siempre. Y un archivo nuevo:
**`protocolo_lectura_en_vivo.md`**, derivado de esta corrida: qué se descarga
primero, en qué orden se verifica, qué se puede afirmar a las dos horas y qué
exige veinticuatro, y qué no se afirma nunca sin fuente en mano. Ese archivo es
lo que se usa el martes.

---

## 6. Bitácora

- Piezas que no llegaron, con respuesta del servidor, primero de todo.
- **Hora de sellado del pacto y hora de primera apertura de CIEP 2025.**
- Presupuesto de afirmaciones declarado y cumplido, por capítulo. Capítulos
  declarados no redactables y por qué.
- Resultado de la compilación y warnings.
- Cambios al pacto, con motivo.
- Las series de seguimiento. **El pasivo pensionario y el supuesto de crecimiento
  de pensiones siguen congelados para calibración:** el CGPE 2023 compara entre
  añadas explícitamente, el PIB implícito de 2022 no coincide con ninguna base, y
  el componente del ISSSTE cambia de método en el CGPE 2024.
- Qué cambiar para la segunda prueba (2026).

---

## 7. Límites

- **Ninguna descarga bloquea la corrida.**
- **No abras CIEP 2025 antes de la fase 5.**
- **No rellenes.** Un capítulo sin datos se declara, no se escribe.
- El documento es de ITED, con portada y autoría propias, y no puede confundirse
  con uno de CIEP.
- Toda cifra con tier declarado; lo de CIEP se cita como `derivada_ciep` con
  página.
- No mezcles bases en una serie.
- No uses el pasivo pensionario ni el supuesto de pensiones en calibración.
- No presentes el marco de manual en el documento.
- No cites tasas de acierto entre ejercicios sin decir qué había en carpeta: el
  salto de 65 % a 87 % entre 2023 y 2024 lo explican los analíticos, no el
  documento evaluado.
- Donde no puedas verificar, dilo, y dilo en el documento, no solo en la
  bitácora.
