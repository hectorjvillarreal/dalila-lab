# Instrucción de trabajo — Evaluación del documento CIEP, ejercicio 2020

**Proyecto:** FISCUS
**Ubicación de trabajo:** `FISCUS/económicos_paquetes/`
**Máquina:** Dalila
**Tipo:** instrucción de trabajo (no es build instruction registrada)
**Ejercicio:** 2020 (primero de la serie; se repetirá para 2021–2026)

---

## 1. Qué es esta corrida

Evaluar el documento *Implicaciones del Paquete Económico 2020* del CIEP contra
las fuentes oficiales del mismo ejercicio, y en el proceso construir los
artefactos que permitan repetir el ejercicio en años siguientes y, eventualmente,
redactar un documento propio.

Hay dos productos. El reporte de 2020 es el visible. Los artefactos de
aprendizaje son el importante: son lo único que sobrevive a esta corrida.

### Fuentes

En `FISCUS/económicos_paquetes/2020/`:

- **Tier 1, oficial primaria (SHCP):** CGPE 2020, ILIF 2020, PPEF 2020
  (exposición de motivos y proyecto de decreto).
- **Tier 2, derivada (CIEP):** Implicaciones del Paquete Económico 2020.

El tier **no es propiedad del documento sino de la sección**. El documento de
CIEP contiene restitución fiel de cifras oficiales y también juicio propio. Esa
distinción es el eje de toda la corrida.

### Salidas

Nada se escribe dentro de `2020/`. El archivo oficial se mantiene limpio.

```
FISCUS/económicos_paquetes/
  _evaluacion/2020/
    00_inventario_paquete.md
    01_capitulo_propio_pensiones.md
    02_verificacion_cifras.csv
    03_evaluacion_calidad.md
    04_comparacion_pensiones.md
    _bitacora_evaluacion.md
  _aprendizaje/
    especificacion_genero.md
    mapa_fuentes.md
    rubrica.md
```

`_aprendizaje/` es acumulativo entre ejercicios: se crea en esta corrida y se
enriquece en las siguientes. Nunca se sobrescribe sin dejar constancia.

---

## 2. Orden de fases — es obligatorio

La fase 2 ocurre **antes** de leer el capítulo de pensiones del CIEP. No es una
sugerencia de estilo: si lees primero a CIEP, tu capítulo será una reconstrucción
del suyo y el diferencial que buscamos desaparece.

Registra en la bitácora la hora de cierre de la fase 2 y la hora de primera
lectura del capítulo 7 del documento CIEP. Si el orden no se respetó, la corrida
no sirve y hay que decirlo.

---

## 3. Fase 1 — Inventario del paquete oficial

Antes de mirar el documento de CIEP más allá de su índice, construye el
inventario de lo que el paquete oficial 2020 efectivamente contiene.

De los **CGPE 2020**: marco macroeconómico completo. Crecimiento del PIB, precio
y plataforma de la mezcla mexicana, tipo de cambio, inflación, tasas de interés,
y las metas de balance público, balance primario y RFSP.

De la **ILIF 2020**: ingresos presupuestarios totales y su desagregación
(tributarios por impuesto, petroleros, no tributarios, endeudamiento), techo de
endeudamiento, y las medidas de la miscelánea que modifican recaudación.

Del **PPEF 2020**: gasto neto total y su desagregación por ramo administrativo,
ramo general y entidad de control directo. Identifica los ramos y programas con
variación real significativa respecto al aprobado 2019.

Escribe `00_inventario_paquete.md`. Cada cifra con su fuente: documento, sección
o cuadro, y página. Este inventario es la base contra la que se mide la cobertura
de CIEP, así que tiene que estar completo antes de continuar.

---

## 4. Fase 2 — Capítulo propio de pensiones, a ciegas

**No abras todavía el capítulo 7 del documento de CIEP.** Puedes haber visto el
índice general; nada más.

Redacta un capítulo sobre gasto en pensiones en el paquete 2020 usando
exclusivamente fuentes oficiales. Sigue la plantilla del género:

- **POLÍTICA 2020** — qué propone el paquete en materia de pensiones.
- **EVOLUCIÓN DEL GASTO EN PENSIONES** — trayectoria y composición, contributivo
  y no contributivo, con la serie que las fuentes permitan reconstruir.
- **IMPLICACIONES** — tu lectura, claramente separada de lo descriptivo.

Reglas de redacción:

- Toda cifra lleva fuente: documento, cuadro, página.
- Todo comparativo declara su contrafactual: nominal o real, contra aprobado o
  contra cierre estimado, contra el año previo o contra el PIB. Sin excepción.
- Si necesitas un dato que no está en las fuentes de la carpeta, ve a la
  sección 7 de esta instrucción y consíguelo por la vía autorizada.
- Si un dato no es obtenible, dilo. No estimes para completar el relato.

Escribe `01_capitulo_propio_pensiones.md` y ciérralo. Anota la hora en la
bitácora. A partir de aquí ya puedes leer el documento de CIEP completo.

---

## 5. Fase 3 — Verificación de cifras

Recorre el documento de CIEP y extrae toda afirmación cuantitativa. Clasifica
cada una en uno de tres tipos:

- **(a) Restitución** — cifra tomada de un documento oficial. Verificable contra
  la fuente. Coincide o no coincide.
- **(b) Derivación** — cifra construida por CIEP a partir de cifras oficiales
  (cocientes, tasas reales, agregaciones, proyecciones). Reproducible: rehaz la
  operación y di si cierra.
- **(c) Juicio** — afirmación interpretativa. No verificable. Se registra y no
  se califica en esta fase.

Ejemplo de la distinción, del propio documento: que el gasto federal en pensiones
represente 4.2 % del PIB es tipo (a) o (b) según de dónde salga; que eso
"absorbe toda la recaudación del IVA y hay un faltante de 100 mil millones" es
tipo (b), y el cociente se puede rehacer; cualquier afirmación sobre si eso es
sostenible o deseable es tipo (c).

Escribe `02_verificacion_cifras.csv` con columnas:

```
id, capitulo, seccion, afirmacion, tipo, valor_ciep, fuente_oficial,
valor_oficial, coincide, discrepancia, nota
```

Para tipo (b), `nota` lleva la operación rehecha, paso a paso.
Para tipo (c), `coincide` va vacío y `nota` dice por qué no es verificable.

Si la verificación no es posible con las fuentes disponibles, `coincide` es
`no_verificable` y `nota` dice qué fuente haría falta. **No aproximes.** Un hueco
declarado vale; un hueco tapado con una cifra parecida contamina el corpus.

---

## 6. Fase 4 — Evaluación de calidad

Seis criterios. Ninguno admite respuesta sin evidencia citada: cada hallazgo
apunta a una sección concreta del documento de CIEP y, cuando corresponda, a una
fuente oficial. **No emitas calificaciones globales ni juicios sobre la solvencia
analítica de CIEP.** Registra hallazgos verificables y deja el juicio al lector.

**1. Cobertura.** Contra `00_inventario_paquete.md`: qué del paquete oficial
trata CIEP y qué omite. Una omisión material se reporta con la cifra omitida y
su fuente. No especules sobre el motivo.

**2. Contrafactual declarado.** Por cada afirmación comparativa de CIEP,
determina si el contrafactual está explícito (real o nominal, contra aprobado o
contra cierre, contra año previo o contra PIB). Reporta la tasa de afirmaciones
con contrafactual explícito y lista las que no lo tienen.

**3. Cierre contable.** El documento se organiza en (+) ingresos, (−) gasto,
(=) balance y deuda. Verifica que los agregados de cada parte sean consistentes
entre sí y con la restricción presupuestal. Reporta cualquier inconsistencia con
las cifras que no cierran.

**4. Trato de los supuestos macro.** Los CGPE traen crecimiento, precio y
plataforma de la mezcla, tipo de cambio, tasas. ¿CIEP los interroga, hace
sensibilidad, o los adopta sin comentario? Presencia o ausencia, con cita.

**5. Separación descriptivo–normativo.** Dada la plantilla POLÍTICA / EVOLUCIÓN /
IMPLICACIONES: ¿el juicio se queda en IMPLICACIONES o aparece en las secciones
descriptivas presentado como descripción? Cada caso, con cita textual y sección.

**6. Horizonte.** Pensiones y salud no son problemas de un ejercicio fiscal.
¿El análisis se detiene en 2020 o extiende la trayectoria? Donde la extiende,
¿declara el supuesto demográfico y de crecimiento? Este criterio es el más
importante para nuestro trabajo: repórtalo con detalle.

Escribe `03_evaluacion_calidad.md`, un apartado por criterio.

---

## 7. Fuentes adicionales, por demanda

Los tomos y anexos del PPEF 2020 no están en la carpeta. Si la verificación de un
capítulo de gasto los requiere, **estás autorizado a descargarlos, uno por uno y
solo lo necesario.**

- Punto de entrada:
  `https://www.finanzaspublicas.hacienda.gob.mx/es/Finanzas_Publicas/Paquete_Economico_y_Presupuesto`
- Navega hasta el archivo. No construyas URLs por analogía.
- Guárdalo en `2020/` con la nomenclatura existente:
  `2020_ppef_{slug}.pdf`
- Agrega su fila a `_manifiesto.csv` con `tier = oficial_primaria`, sha256 y
  fecha de acceso.
- Verifica cabecera `%PDF`.
- Una petición cada 2 segundos.
- Anota en la bitácora qué verificación motivó cada descarga.

Nada de descarga masiva. El archivo crece por necesidad demostrada.

---

## 8. Fase 5 — Comparación

Ahora sí, contrasta tu `01_capitulo_propio_pensiones.md` contra el capítulo 7 de
CIEP. Escribe `04_comparacion_pensiones.md` con cuatro apartados:

- **Coincidencias.** Qué cifras y lecturas comparten.
- **Lo que CIEP tiene y tú no.** Cifras que encontró y tú no; relaciones que
  construyó y tú no viste; fuentes que usó y no estaban en tu mapa. Por cada
  una: dónde estaba el dato y por qué no llegaste a él.
- **Lo que tú tienes y CIEP no.** Mismo tratamiento. Si es una omisión de CIEP,
  cruza con el criterio 1.
- **Diferencias de método.** Contrafactuales distintos, agregaciones distintas,
  horizontes distintos. Sin declarar ganador: describe la diferencia y qué
  implica cada elección.

Este apartado es el contenido pedagógico de la corrida. Sé específico y sé duro
contigo mismo: lo que no encontraste importa más que lo que sí.

---

## 9. Fase 6 — Artefactos de aprendizaje

Lo único que sobrevive a esta corrida. Escríbelos pensando en que quien los lea
el año próximo no tendrá memoria de esta sesión.

**`_aprendizaje/especificacion_genero.md`** — qué es un documento de
Implicaciones: arquitectura en tres partes, capítulos por rubro, plantilla
interna, extensión típica, qué va en cada subsección, qué tipo de afirmación
aparece dónde. Escrito como especificación reutilizable, no como descripción
del 2020.

**`_aprendizaje/mapa_fuentes.md`** — qué documento oficial y qué cuadro alimenta
cada sección del género. Por ejemplo: la sección de ingresos presupuestarios se
alimenta del cuadro X de la ILIF; el capítulo de pensiones requiere el ramo Y del
PPEF y el analítico Z. Incluye los tomos que hubo que descargar y para qué. Este
mapa es lo que hará la corrida de 2021 mucho más barata.

**`_aprendizaje/rubrica.md`** — los seis criterios, con lo que esta corrida haya
enseñado sobre cómo aplicarlos: casos límite, criterios que resultaron ambiguos,
distinciones que hubo que precisar. Si un criterio no funcionó, dilo.

Al final de cada archivo, una sección `## Historial` con la fecha y el ejercicio
que lo generó o modificó. En corridas futuras se agrega, no se sobrescribe.

---

## 10. Bitácora

`_evaluacion/2020/_bitacora_evaluacion.md`:

- Inicio y fin de la corrida (ISO).
- **Hora de cierre de la fase 2 y hora de primera lectura del capítulo 7 de
  CIEP.** Si el orden se rompió, dilo explícitamente.
- Documentos oficiales descargados por demanda, con la verificación que los
  motivó.
- Conteo de afirmaciones por tipo (a / b / c), y cuántas quedaron
  `no_verificable` y por qué.
- Anomalías: cifras que no cierran y no supiste explicar, secciones del documento
  CIEP cuya lectura te resultó ambigua, cuadros ilegibles. Descríbelas, no las
  resuelvas.
- Qué de esta corrida debería cambiar en la instrucción para 2021.

---

## 11. Límites

- No califiques globalmente el documento de CIEP ni su solvencia analítica. Esa
  lectura es humana. Tú entregas hallazgos con evidencia.
- No modifiques nada dentro de `2020/` salvo agregar PDFs oficiales descargados
  por demanda y su fila de manifiesto.
- Donde no puedas verificar, dilo. La utilidad de esta corrida depende
  enteramente de que los huecos estén declarados.
