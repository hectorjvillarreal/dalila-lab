# Instrucción de trabajo — Documento propio, ejercicio 2026

**Versión 2.** Cambios respecto a la v1: cuarentena simplificada (§2); dos rutas
declaradas según disponibilidad de los analíticos del proyecto (§3); entrega de
PDF compilado en Dalila y ZIP portátil, con `siunitx` eliminado (§7).

**Proyecto:** FISCUS · **Ubicación:** `FISCUS/económicos_paquetes/` · **Máquina:** Dalila
**Tipo:** instrucción de trabajo (no es build instruction registrada)
**Producto:** documento completo del género, de autoría ITED, sobre el Paquete
Económico 2026, en Markdown, LaTeX y PDF.
**Antecedente:** documento propio 2025 y su comparación anónima contra el del género.

---

## 0. Qué es esta corrida

Es un **ensayo general**. El documento de 2026 es el entregable, pero el objetivo
real es producir y validar el **protocolo de lectura en vivo** para la corrida del
Paquete Económico 2027, donde **no existirá documento de CIEP para comparar** y
donde solo estará disponible lo que se publique el día de la entrega.

De ahí las diferencias con la corrida de 2025:

- **Régimen restringido.** La corrida de 2025 usó Ley de Ingresos aprobada, PEF
  aprobado y analíticos aprobados. Era legítimo bajo su instrucción, pero produce
  un ejercicio irrepetible en vivo. Aquí no se usa nada aprobado del ejercicio.
- **Se cierran los dos huecos que señaló la comparación anónima:** la capa
  demográfica —negarse a calcular per cápita fue error de archivo, no disciplina—
  y la capa de presentación, que es donde el documento perdía frente al género.

---

## 1. Criterios de aceptación

Cuatro. Ninguno compensa a otro.

**1.1 Reconocimiento de género.** Un lector habitual de las *Implicaciones* debe
reconocerlo como documento de ese género: arquitectura en tres partes, plantilla
de capítulo, registro, densidad de cuadros y figuras, **y presentación**: lámina
de apertura por capítulo, titular cuantitativo, figura principal. En 2025 este
criterio se cumplió a medias.

**1.2 Autoría ITED, visible e inconfundible.** Portada, autoría, fecha y
filiación propias. No puede confundirse con un documento de CIEP. Toda cifra con
tier declarado; lo de CIEP se cita como `derivada_ciep` con página.

**1.3 Entregables completos y compilados** (§7). Un PDF que no exista no cuenta.

**1.4 Régimen en vivo respetado** (§2). Binario: si se usó una pieza aprobada del
ejercicio 2026, la corrida no sirve como ensayo aunque el documento sea bueno.

---

## 2. Régimen de simulación en vivo

La carpeta `2026/` **ya contiene solo piezas de proyecto**: CGPE, ILIF y PPEF. No
hace falta construir una carpeta paralela. La regla se reduce a una prohibición
de descarga.

### 2.1 Prohibido para el ejercicio 2026

- **Ley de Ingresos aprobada 2026.**
- **PEF aprobado 2026 y sus analíticos.**
- Cuenta Pública 2025 e informes trimestrales posteriores a la entrega del
  paquete.
- **El documento de CIEP sobre el Paquete 2026**, hasta la fase 8.

### 2.2 Permitido

- CGPE, ILIF y PPEF 2026 (el PDF de la ILIF contiene su exposición de motivos;
  verificado 2018–2026).
- **Analíticos del proyecto 2026**, si se consiguen (§3).
- Iniciativa de miscelánea vía Gaceta Parlamentaria, si la hay.
- **Todo el histórico hasta 2025 inclusive, aprobados incluidos.** Eso sí existe
  en el momento de una entrega y es la base de comparación legítima.
- Las dos piezas de `_metodologia/` y la capa demográfica de §6.

### 2.3 Verificación imposible en vivo

Si una verificación exige una pieza prohibida, la respuesta correcta es
**declararla no verificable en vivo** y anotarla. Ese registro es uno de los
productos más valiosos: dice qué no se podrá afirmar en la corrida 2027.

### 2.4 Base de comparación — dos líneas, nunca mezcladas

| Línea | Comparación | Por qué |
|---|---|---|
| **Primaria (de la casa)** | **Proyecto 2026 contra proyecto 2025** | Ex ante contra ex ante, disponible en vivo, y nadie más la construye. Tenemos los PPEF de 2018 a 2026. |
| **Segunda (del género)** | Proyecto 2026 contra aprobado 2025 | Es la que usa la discusión pública y la que hará el documento del género. |

Ambas se declaran; ambas aparecen donde la cifra importa; **nunca conviven en un
cuadro sin etiqueta**. Donde difieran de forma material, la diferencia es un
hallazgo: mide lo que la Cámara cambió el año previo.

---

## 3. Analíticos del proyecto — dos rutas, ambas preparadas

Es la incógnita que decide el alcance del documento, y hay que estar listos para
las dos respuestas. **Resuélvelo en la fase 1, antes de sellar el detalle del
pacto.**

### 3.1 Búsqueda

Busca los analíticos presupuestarios del **proyecto** 2026, en este orden:

1. `ppef.hacienda.gob.mx`, sección de analíticos presupuestarios del ejercicio.
2. **Portal de datos abiertos de la Secretaría de Hacienda**, que es donde suelen
   publicarse el día de la entrega.
3. Transparencia Presupuestaria.

Registra ruta, respuesta y hora en la bitácora. **Este resultado es un producto
de la corrida por sí mismo:** dice si la corrida 2027 tendrá desagregación por
programa desde el primer día.

Nota de operación: los analíticos traen los datos en la hoja `Hoja1`, no en la
primera, que es un resumen por ramo y hace creer que el archivo está vacío.

### 3.2 Ruta A — hay analíticos del proyecto

El documento trabaja a nivel de **programa presupuestario y unidad responsable**:
perímetros reproducibles por enumeración de claves, cuadro de UR por capítulo,
distribución territorial donde el fondo la tenga, y diff de claves 2025 → 2026
**por clave, no por nombre**.

### 3.3 Ruta B — no hay analíticos del proyecto

El documento trabaja a nivel de **ramo y función**, con lo que trae el proyecto
de decreto y sus anexos, y **declara en el propio texto qué no puede decir**:
composición por programa, reasignaciones entre unidades responsables,
distribución territorial de fondos, y separación entre caída de ramo y caída de
función cuando la fuente no la permita.

Esa declaración va en el documento, no solo en la bitácora, y se escribe en el
registro del documento. **Un capítulo que dice con precisión qué no puede afirmar
es mejor que uno que lo afirma sin fuente.**

Bajo la Ruta B, el presupuesto de afirmaciones de §7 puede no alcanzarse en
varios capítulos. Eso es un resultado, no un fracaso: declara los capítulos no
redactables y sigue.

---

## 4. Arquitectura del documento

Tres partes: **(+) Ingresos**, **(−) Gasto**, **(=) Balance y Deuda**. Plantilla
por capítulo: **POLÍTICA / EVOLUCIÓN / PROGRAMAS SELECCIONADOS / IMPLICACIONES**.
El juicio va en IMPLICACIONES.

### 4.1 Capítulos

Resumen; marco macroeconómico; ingresos; ingresos energéticos y empresas
públicas; gasto total; salud; educación; pensiones; inversión; seguridad; gasto
federalizado; **medio ambiente y agua**; **anexos transversales**; balance y
deuda; y un capítulo metodológico de horizonte demográfico.

Los dos capítulos nuevos cierran el hueco de la comparación anónima: medio
ambiente y agua obtuvo 4.5, género y cuidados 4.0. Para un lector habitual, su
ausencia es fallo de reconocimiento, no decisión de alcance.

**Anexos transversales se trata como objeto presupuestal, no como ensayo de
política social:** qué anexos existen, cuánto concentran, qué proporción del
etiquetado para igualdad es en realidad pensiones, qué programas se repiten entre
anexos. Eso es análisis fiscal y está dentro del mandato. Lo que no se hace es
incidencia social sin fuente.

### 4.2 Capa de presentación

Cada capítulo abre con una **lámina**: titular cuantitativo con su signo y su
base declarada; figura principal generada desde datos versionados; un párrafo de
**"qué cambió"**; un párrafo de **"por qué importa"**.

Y cierra con una **ficha metodológica**: perímetro, base de comparación,
deflactor, año de los pesos, PIB y añada, fuentes, y qué no puede afirmarse con
ellas.

Ninguna cifra de la lámina puede carecer de su renglón en la ficha.
**Presentación no es laxitud: es la misma cifra, mejor colocada.**

### 4.3 Comparaciones estructurales de la casa

Perímetro declarado, dos líneas donde aplique, nunca híbridas.

| Capítulo | Comparación |
|---|---|
| Ingresos | Tributarios / gastos obligatorios (con y sin cuotas IMSS) |
| Gasto total | Pensiones + costo financiero / tributarios |
| Pensiones | Pensiones IMSS / cuotas IMSS |
| Salud | Cuotas obrero-patronales / gasto en salud IMSS |
| Educación | Educación / pensiones y jubilaciones; segunda línea contra pensiones totales |
| Deuda | Costo financiero / tributarios; SHRFSPF / tributarios en años |

### 4.4 Capítulo de deuda

Descomposición del cambio de la razón SHRFSPF/PIB en cuatro variables:
crecimiento, tasa real, inflación y tipo de cambio. **Criterio de aceptación:**
reproducir la caída de 2022 —RFSPF de 4.5 % del PIB con el acervo bajando de 50.7
a 49.4 %— antes de aplicarse a 2026. Reporta la sensibilidad al tipo de cambio de
cierre, que en 2025 resultó material. No presentes el marco de manual: retirado
por sesgo sistemático, diagnóstico interno en bitácora.

---

## 5. El reloj

Registra en la bitácora **el momento en que cada hallazgo quedó disponible**,
medido desde el inicio. Al terminar, clasifica cada hallazgo en tres bandas: lo
afirmable en las primeras **dos horas**, en **ocho**, y lo que exige
**veinticuatro o más**. Es el insumo directo del protocolo de la fase 7.

No aceleres a costa de verificar. El punto no es ser rápido: es saber qué se
puede decir a cada hora.

---

## 6. Capa demográfica declarada

La corrida de 2025 se negó a calcular por alumno, por afiliado y por habitante
porque los denominadores no estaban en el paquete. Correcto para auditar,
equivocado para un documento: los denominadores existen y están dentro del
alcance de ITED.

Segunda capa, declarada, con `tier = externa_demografica` (valor nuevo; anótalo
en la bitácora):

- Población por edad y proyecciones: CONAPO, CELADE.
- Matrícula por nivel educativo: estadística educativa oficial.
- Afiliación a sistemas de salud: IMSS, ISSSTE, población sin seguridad social.
- Población por entidad federativa, para gasto federalizado.
- Padrón de programas pensionarios donde exista.

**Reglas, sin excepción:**
- Cada denominador con fuente, año de referencia y liga en `datos/_fuentes.csv`.
- **Cuadros presupuestales y cuadros per cápita van separados.** Nunca una cifra
  del paquete y un denominador externo en la misma línea sin marca.
- Toda cifra per cápita declara su denominador. En educación distinguir
  **población total, población en edad escolar y matrícula**: tres denominadores,
  tres lecturas.
- Si un denominador no se consigue, se declara y no se calcula. La regla vieja
  sigue vigente como último recurso; deja de ser el primero.

Verifica si se repite el hallazgo transversal: el paquete trae horizonte
demográfico donde la transición presiona al alza (pensiones) y no lo trae donde
presiona a la baja (educación). Con la capa externa ya podemos decir qué habría
significado.

---

## 7. Entregables y compilación · REESCRITO

### 7.1 Qué se entrega

En `_documento_2026/entrega/`, los cuatro:

1. **`documento_2026.pdf`** — compilado **en Dalila**, no en Overleaf.
2. **`documento_2026.zip`** — proyecto LaTeX completo y portátil: `main.tex`,
   `capitulos/`, `datos/`, `figuras/`, `bibliografia.bib`, y un `LEEME.md` con
   la versión de TeX Live usada y el comando de compilación.
3. **`documento_2026.md`** — misma sustancia, generada del mismo contenido.
4. **`datos/`** con `_fuentes.csv`.

**Un PDF que no exista no cuenta como entrega.** Si algún capítulo rompe la
compilación, aíslalo, compila el resto, entrega el PDF parcial y reporta cuál
falló y por qué. Nunca entregues un proyecto que no compila sin el PDF.

### 7.2 Compilación local

`latexmk -pdf` o dos pasadas de `pdflatex`, en Dalila. Reporta warnings.

### 7.3 Portabilidad — restricciones duras

La versión de Overleaf en uso ha dado problemas de compilación. Reduce la
superficie de dependencias:

- **No uses `siunitx`.** Es la fuente más probable del problema: su sintaxis
  cambió entre versiones mayores y rompe en instalaciones anteriores. **Los
  números se formatean al generar los cuadros**, en el paso de datos, no en
  LaTeX. Separador de miles y decimal en español, aplicados de forma uniforme.
- `pgfplots` con **`\pgfplotsset{compat=1.16}`**, no con la versión más reciente.
  Evita funciones introducidas después.
- Paquetes admitidos: `babel` (spanish), `geometry`, `fancyhdr`, `booktabs`,
  `graphicx`, `hyperref`, `caption`, `longtable`, `array`, `pgfplots`.
- **Prohibidos:** `siunitx`, `minted` y cualquier cosa que requiera
  `shell-escape`, fuentes no estándar, y cualquier paquete que haya que instalar.
- Si una figura resulta frágil en `pgfplots`, **genera el PDF de la figura por
  separado y súbelo con `\includegraphics`**, conservando el script y los datos
  que la producen. Robustez antes que elegancia.

---

## 8. Secuencia

**Fase 0 — Lectura local y pacto.** Lee `_aprendizaje/` completo. Escribe y
**sella** `pacto_estructura.md`: índice, preguntas por capítulo, comparaciones
estructurales, cuadros y figuras previstos con el dato que cada uno necesita.
Registra la hora y arranca el reloj (§5). El detalle de granularidad queda
pendiente de la fase 1.

**Fase 0.5 — Adjudicación pendiente de 2025.** Acotada a cinco puntos, contra
fuentes, a mano: la caída de salud (−12.2 y −7.2 nuestros contra −11 del género),
la de educación (+0.7 contra −1.2), la de Defensa (ramo contra función), la tasa
real del costo financiero, y los niveles nominales del acervo. Resuelve quién
tenía razón y por qué. **Si nuestras cifras no resisten, el resto de la corrida
hereda el problema**, así que va antes.

**Fase 1 — Analíticos y adquisición** (§3). Resuelve la ruta, cierra el pacto con
la granularidad que corresponda, y baja lo permitido. Regla de no bloqueo: dos
intentos, se registra, se sigue.

**Fase 2 — Inventario, diffs y datos.** Inventario con documento, cuadro y
página. Diffs **por clave, no por nombre**, de programa, unidad responsable y
subfunción 2025 → 2026, y del Anexo 3. Reconciliaciones: ILIF ↔ CGPE; ramos ↔
función; flujo contra acervo. Construye `datos/` completo con `_fuentes.csv`,
incluida la capa demográfica, **antes** de redactar.

**Fase 3 — Redacción.** Por capítulo: declarar el presupuesto de afirmaciones —al
menos doce verificables, seis de restitución oficial, no más de 30 % no
verificables—; si no llega, escribir la declaración de capítulo no redactable en
el registro del documento; si llega, redactar contra el pacto, con lámina y
ficha.

**Fase 4 — LaTeX, compilación y entrega** (§7).

**Fase 5 — Bandas de reloj** (§5).

**Fase 6 — Protocolo de lectura en vivo.**
`_aprendizaje/protocolo_lectura_en_vivo.md`: qué se descarga primero y en qué
orden; qué se verifica en cada banda; qué es seguro afirmar a las dos horas;
**qué no se puede afirmar sin piezas que no existen en vivo**; y la checklist de
omisiones recurrentes propias, derivada de las corridas anteriores. Este archivo
es el producto que sobrevive.

**Fase 7 — Comparación contra el documento del género.** Se levanta la
cuarentena; registra la hora. Cinco apartados: coincidencias; **lo que ellos
tienen y nosotros no**, con dónde estaba el dato y por qué no llegamos —esa lista
es el comparador que la corrida 2027 no tendrá—; lo que nosotros tenemos y ellos
no; diferencias de método sin declarar ganador; y **contaminación**: qué
afirmaciones propias se sostienen solo porque ellos las dijeron antes.

**Fase 8 — Aprendizaje.** Actualiza los tres artefactos. En la especificación del
género, qué cambió al escribir bajo restricción de vivo.

---

## 9. Convenciones vigentes

Nomenclatura **RFSPF/SHRFSPF** con equivalencia declarada una vez. Deflactor del
PIB, nunca derivado de agregados redondeados. Las **cinco declaraciones** del
contrafactual. Perímetro declarado antes del primer cuadro y constante. Toda
diferencia en millones de pesos declara si es nominal o real. Prohibición de
yuxtaponer magnitudes sin mecanismo. Definiciones adjudicadas contra *Balance
Fiscal en México* (SHCP, abril 2023), nunca por criterio propio. **Ramo y función
son objetos distintos:** una caída de ramo no es una caída de la función que su
nombre sugiere. Códigos por clave, no por nombre.

Nunca cites tasas de acierto entre ejercicios sin decir qué había en carpeta.

Notas de operación: bundle TLS antes de descargar, sin desactivar verificación;
las figuras sin capa de texto se leen renderizando la página, como paso
explícito.

**Nada de referencias temporales relativas.** Fecha o ejercicio.

---

## 10. Bitácora

Piezas que no llegaron, con respuesta del servidor, primero de todo. **Resultado
de la búsqueda de analíticos del proyecto y ruta adoptada (A o B), con hora.**
Hora de sellado del pacto, hora de levantamiento de la cuarentena, y el reloj de
cada hallazgo. Resultado de la fase 0.5. Presupuesto de afirmaciones por capítulo
y capítulos no redactables. **Lista de verificaciones imposibles en vivo.**
Resultado de la compilación y warnings, y si hubo capítulos aislados. Cambios al
pacto con motivo. Las series de seguimiento; el pasivo pensionario y el supuesto
de crecimiento de pensiones **siguen congelados para calibración**. Qué cambiar
para la corrida 2027.

---

## 11. Límites

- **No uses nada aprobado del ejercicio 2026** (§2.1). Criterio binario.
- No mezcles las dos líneas de comparación en un cuadro sin etiqueta.
- No rellenes: un capítulo sin datos se declara, no se escribe.
- No mezcles cifras del paquete con denominadores externos en la misma línea.
- No uses `siunitx` ni ningún paquete fuera de la lista de §7.3.
- No entregues proyecto sin PDF.
- No uses el pasivo pensionario ni el supuesto de pensiones en calibración.
- No presentes el marco de manual en el documento.
- El documento es de ITED, con portada y autoría propias.
- Donde no puedas verificar, dilo en el documento, no solo en la bitácora.
