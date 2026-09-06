# Instrucción de trabajo — Evaluación del documento CIEP, ejercicio 2021

**Proyecto:** FISCUS
**Ubicación de trabajo:** `FISCUS/económicos_paquetes/`
**Máquina:** Dalila
**Tipo:** instrucción de trabajo (no es build instruction registrada)
**Ejercicio:** 2021 · **Capítulo propio:** SALUD
**Antecedente:** corrida 2020, commit `91685d0`. Las decisiones de esta
instrucción resuelven las preguntas abiertas en el memo de esa corrida.

---

## 0. Antes de nada: lee lo que ya aprendiste

Esta corrida **no empieza en blanco**. Lee primero, completos:

```
_aprendizaje/especificacion_genero.md
_aprendizaje/mapa_fuentes.md
_aprendizaje/rubrica.md
```

Estos archivos se **actualizan**, no se sobrescriben. Al final de la corrida se
les agrega lo aprendido en 2021, con entrada fechada en `## Historial`.

La corrida 2020 estableció un hallazgo que reordena la rúbrica: **el punto de
falla no es la aritmética, es la base de comparación.** De 187 afirmaciones
verificadas, 41 discreparon y casi ninguna por error de suma. Todas por cambio de
base sin declarar. El criterio 2 pasa a ser el primero de la rúbrica.

---

## 1. Convenciones fijadas — rigen toda la corrida

Estas ya no se discuten. Se aplican y se declaran.

### 1.1 Deflactor

**Deflactor del PIB** para todo agregado fiscal y toda razón a PIB. Se declara
una sola vez al inicio del capítulo propio, con su valor y su fuente en los CGPE.

Excepción única: cuando lo que se deflacta es el valor real de una prestación
individual (lo que recibe una persona), el índice de precios al consumidor es el
correcto, porque la pregunta es de bienestar y no de agregado fiscal. En ese
caso se marca **en el lugar**, no en una nota al pie.

**Nunca los dos índices en un mismo cuadro.**

Las discrepancias atribuibles a deflactor se reportan **como categoría propia**,
no se absorben en el umbral de tolerancia.

### 1.2 Contrafactual — las cuatro declaraciones

Toda afirmación comparativa, tuya o de CIEP, se evalúa contra cuatro
declaraciones. Si falta una, la afirmación está incompleta:

1. ¿nominal o real?
2. ¿contra aprobado o contra cierre estimado?
3. ¿contra el año previo o contra el PIB?
4. ¿en pesos de qué año?

### 1.3 Comparación ex ante contra ex ante

Se compara **PPEF 2021 contra PEF 2020 aprobado**. Proyecto contra proyecto,
aprobado contra aprobado. Comparar un proyecto contra un ejercido es el origen de
la mayoría de los problemas de contrafactual documentados en 2020, y tener ahora
más fuentes disponibles no es licencia para reproducirlo.

El cierre estimado se cita únicamente donde los CGPE lo dan, **etiquetado como
tal**, y nunca como base de una tasa de variación sin decirlo.

### 1.4 Perímetro

**Se declara antes del primer cuadro y no cambia dentro del capítulo.**

No se construyen cocientes que mezclen perímetros. En 2020 CIEP presentó
"programable 16.7 % = 4.9 + 10.3 + 1.5" combinando consolidado neto, bruto con
autónomos y un residuo: ninguna de las tres partes resultó verificable por
separado. No lo repitas.

Cuando un agregado sume componentes de naturaleza fiscal distinta, se presentan
**las líneas por separado y después la suma etiquetada**. Nunca un agregado
silencioso.

### 1.5 Umbral de tolerancia

- Niveles: **0.5 %**
- Tasas y razones a PIB: **0.1 pp**
- Lo atribuible a deflactor o redondeo se reporta aparte, con su categoría.

### 1.6 Prohibición de yuxtaposición

**No presentes dos cifras de magnitud parecida sugiriendo relación sin mecanismo
declarado y verificable.** Poner dos números en el mismo párrafo ya insinúa un
vínculo. Si hay una relación de restricción presupuestal, se muestra; si no la
puedes mostrar, las cifras van en secciones distintas o no van.

### 1.7 Balances

Cualquier afirmación sobre déficit, balance o deuda declara **cuál** de los tres
balances usa: balance público, balance sin inversión de alto impacto, o RFSP.
Los tres coexisten en el marco mexicano y deslizarse entre ellos produce
exactamente las inconsistencias detectadas en el capítulo de deuda de 2020.
El cuadro de RFSP de los CGPE es la fuente preferente.

---

## 2. Fuentes

En `FISCUS/económicos_paquetes/2021/`: CGPE 2021, ILIF 2021, PPEF 2021, e
*Implicaciones del Paquete Económico 2021* (CIEP).

**Descarga obligatoria en fase 1, antes de escribir una línea del capítulo
propio.** En 2020 estos archivos se bajaron hasta la fase 3 y la comparación lo
pagó:

- Los cuatro analíticos del **PPEF 2021**: ramo × programa y ramo × función, en
  sus versiones Gobierno Federal y entidades.
- Los mismos cuatro analíticos del **PEF 2020 aprobado**
  (`pef.hacienda.gob.mx`).

Reglas de descarga: navega, no construyas URLs por analogía; verifica cabecera;
una petición cada 2 segundos; registra cada archivo en `_manifiesto.csv` con
sha256, fecha de acceso y tier.

**Tier.** Se admite ahora `derivada_ciep` además de `oficial_primaria`. Registra
los PDF del CIEP que estén sin fila. Esto es **provisional**: ya establecimos que
el tier es propiedad de la sección y no del documento, y la columna a nivel de
sección sigue pendiente de decisión. Anótalo así en la bitácora.

---

## 3. Orden de fases — obligatorio

El capítulo propio de salud se redacta **antes** de leer el capítulo de salud de
CIEP. Registra en la bitácora la hora de cierre del capítulo propio y la hora de
primera lectura del capítulo de salud de CIEP. Si el orden se rompió, la
comparación no vale y hay que decirlo.

Puedes ver el índice general del documento CIEP; nada más de ese capítulo.

---

## 4. Fase 1 — Inventario del paquete oficial 2021

Como en 2020: CGPE (marco macro completo, metas de balance y RFSP), ILIF
(ingresos y su desagregación, techo de endeudamiento, medidas de miscelánea),
PPEF (gasto neto y desagregación por ramo, con variaciones reales significativas
contra PEF 2020 aprobado).

Añade en 2021 un apartado específico sobre **salud**, porque el ejercicio tiene
complicaciones que 2020 no tenía:

- Es el primer paquete formulado bajo la pandemia. Identifica qué es gasto
  extraordinario declarado y qué es tendencia, y si el paquete los distingue.
- El INSABI está en operación y la transición desde el Seguro Popular no está
  cerrada. Rastrea a dónde fueron los recursos y qué pasó con el FONSABI.
- La aportación al FASSA (Ramo 33) es gasto federalizado en salud y no está en
  el Ramo 12. Decide si entra al perímetro y decláralo.

Escribe `_evaluacion/2021/00_inventario_paquete.md`. Cada cifra con documento,
cuadro y página.

---

## 5. Fase 2 — Capítulo propio de SALUD, a ciegas

Plantilla del género: **POLÍTICA 2021 / EVOLUCIÓN DEL GASTO EN SALUD /
PROGRAMAS SELECCIONADOS / IMPLICACIONES.**

### 5.1 El perímetro es el problema central de este capítulo

Antes del primer cuadro, declara qué cuenta como gasto público en salud y qué no.
Las opciones no son equivalentes y la elección determina todo lo demás:

- **Por función** (función Salud en el analítico ramo × función) contra
  **por ramo** (Ramo 12 y afines). No dan lo mismo.
- **Contributivo** (IMSS, ISSSTE, servicios médicos de Pemex y fuerzas armadas)
  contra **no contributivo** (Ramo 12, INSABI, FASSA).
- Federal contra federalizado.
- Presupuestario contra gasto total en salud, que incluye gasto de bolsillo y
  privado y **no está en el paquete**. Si lo mencionas, di de dónde sale y que
  es otra fuente.

Presenta las líneas por separado y después la suma etiquetada. Nunca un agregado
silencioso: contributivo y no contributivo son objetos fiscales distintos, con
fuentes de financiamiento y determinantes de trayectoria distintos, y agregarlos
sin etiqueta borra precisamente lo que nos interesa medir.

### 5.2 Reglas de redacción

- Toda cifra con fuente: documento, cuadro, página.
- Toda comparación con las cuatro declaraciones de §1.2.
- Comparaciones ex ante contra ex ante (§1.3).
- Si un dato no es obtenible con las fuentes autorizadas, dilo. No estimes para
  completar el relato.
- El juicio va en IMPLICACIONES. Las secciones descriptivas describen.

Escribe `_evaluacion/2021/01_capitulo_propio_salud.md`, ciérralo, anota la hora.

---

## 6. Fase 3 — Verificación de cifras

Igual que en 2020: extrae toda afirmación cuantitativa de CIEP y clasifícala en
**(a) restitución**, **(b) derivación** reproducible paso a paso, o **(c) juicio**
no verificable.

`_evaluacion/2021/02_verificacion_cifras.csv`, con una columna nueva:

```
id, capitulo, seccion, afirmacion, tipo, valor_ciep, fuente_oficial,
valor_oficial, coincide, discrepancia, tipo_error, nota
```

`tipo_error` toma uno de cinco valores, y solo aplica cuando hay discrepancia:

- `transcripcion` — la cifra está mal copiada.
- `contrafactual` — la cifra es correcta contra otra base que la declarada.
- `perimetro` — la cifra mezcla o cambia perímetro.
- `omision` — falta un componente que la fuente sí trae.
- `deflactor` — la diferencia se explica por el índice usado.

Esta tipología salió sola en 2020 y ahora se registra desde el inicio para que
sea comparable entre ejercicios.

Cuando la verificación no sea posible, `coincide = no_verificable` y `nota` dice
qué fuente haría falta. **No aproximes.**

---

## 7. Fase 4 — Evaluación de calidad

Seis criterios, sin calificaciones globales, cada hallazgo con cita a sección de
CIEP y a fuente oficial. El orden cambia respecto a 2020: el contrafactual va
primero.

1. **Contrafactual declarado.** Por afirmación comparativa, cuáles de las cuatro
   declaraciones están explícitas. Reporta la tasa y lista las incompletas.
2. **Perímetro.** ¿Se declara? ¿Se mantiene dentro del capítulo? ¿Hay cocientes
   que mezclen perímetros? Cada caso con las cifras.
3. **Cobertura.** Contra el inventario: qué omite CIEP. Reporta la cifra omitida
   y su fuente. **Antes de declarar algo ausente, agota las rutas:** en 2020 CIEP
   dio por desaparecido un anexo transversal que sí estaba en la exposición de
   motivos, y de esa omisión derivó una tendencia inexistente.
4. **Cierre contable.** Que (+) ingresos, (−) gasto, (=) balance sean
   consistentes entre sí y con la restricción presupuestal. Aplica §1.7.
5. **Separación descriptivo–normativo.** ¿El juicio se queda en IMPLICACIONES o
   se filtra a las secciones descriptivas presentado como descripción?
6. **Horizonte.** ¿El análisis se detiene en 2021 o extiende la trayectoria?
   ¿Declara supuesto demográfico y de crecimiento? En 2020 el paquete oficial
   tenía más horizonte que el documento que lo evaluaba. Verifica si se repite.

`_evaluacion/2021/03_evaluacion_calidad.md`, un apartado por criterio.

---

## 8. Fase 5 — Comparación

`_evaluacion/2021/04_comparacion_salud.md`. Cuatro apartados: coincidencias; lo
que CIEP tiene y tú no; lo que tú tienes y CIEP no; diferencias de método.

Por cada cosa que CIEP encontró y tú no: dónde estaba el dato y por qué no
llegaste a él. Sé duro contigo mismo. Lo que no encontraste importa más que lo
que sí, y ahora ya no tienes la excusa de 2020 de haber bajado los analíticos
tarde.

---

## 9. Pendientes heredados de 2020

Dos tareas acotadas, verificables, que quedaron abiertas. **No abras ninguna
otra.**

**9.1 CGPE 2020, página 129.** Léela completa y en contexto. La corrida 2020
reportó como contradicción que esa página diga que las presiones pensionarias
disminuyen hasta desaparecer mientras la p. 122 las proyecta al alza hasta 2025.
La hipótesis a probar es que son **dos objetos distintos**: el costo de
transición del régimen 1973 sí se extingue conforme se agotan las cohortes,
mientras el gasto pensionario total sigue creciendo por demografía. Ambas cosas
pueden ser ciertas simultáneamente. Determina qué agregado nombra cada página y
reporta. **No uses la palabra contradicción salvo que la evidencia la sostenga**;
si la hipótesis se confirma, el caso pasa a la especificación del género como
ejemplo de por qué el perímetro debe declararse.

**9.2 Pensión no contributiva 2020: 126.7 contra 120.0.** El Anexo 14 del decreto
atribuye 120.0 mmp al programa; la cifra usada fue 126.7. Reconcilia primero esa
diferencia y reporta a qué corresponde. Con 120.0 el hueco contra el apoyo
nominal baja de 21 % a 14 %. Ese remanente **no se explica con una hipótesis
narrada**: descomponlo en componentes verificables (pago de marcha, altas durante
el ejercicio, gastos de operación y dispersión) o repórtalo sin explicar.
La cifra permanece **congelada para calibración** hasta que la descomposición
cierre.

**Lo que no debes tocar:** la tesis del IVA de 2020. Su verificación es manual y
corresponde a la autoridad definicional del corpus, no a esta corrida.

---

## 10. Fase 6 — Actualización de los artefactos de aprendizaje

Agrega, no sobrescribas. Entrada fechada en `## Historial` de cada archivo.

**`especificacion_genero.md`** — qué cambió del género entre 2020 y 2021, si es
que cambió. Incorpora como comparación canónica del capítulo de pensiones la
razón **pensiones IMSS sobre cuotas IMSS** (1.31× en 2020): habla de
financiamiento y no solo de magnitud, y muestra que el régimen 1973 dejó de
financiarse con contribuciones aunque la ley lo llame contributivo. Si en salud
encuentras una comparación estructural equivalente, propónla con el mismo
estándar: tiene que hablar de financiamiento y sostenerse con la fuente en la
mano.

**`mapa_fuentes.md`** — qué cuadro de qué documento alimenta cada sección. Añade
las rutas de los analíticos del PPEF t y del PEF t−1, que son ahora parte del
procedimiento estándar. Añade lo específico de salud: dónde vive cada perímetro.

**`rubrica.md`** — el reorden de criterios, las convenciones de §1, la tipología
de `tipo_error`, y lo que 2021 haya enseñado sobre casos límite. Si un criterio
no funcionó, dilo.

---

## 11. Tarea lateral — rutas de analíticos 2022–2026

Independiente de lo anterior, al final de la corrida: prueba la ruta de
analíticos para los ejercicios 2022 a 2026. En 2020 los tomos devolvían 404 pero
los analíticos no. Solo **comprueba disponibilidad y registra la ruta** en
`mapa_fuentes.md`. **No descargues nada** en esta corrida.

---

## 12. Bitácora

`_evaluacion/2021/_bitacora_evaluacion.md`:

- Inicio y fin (ISO).
- **Hora de cierre del capítulo propio y hora de primera lectura del capítulo de
  salud de CIEP.** Si el orden se rompió, dilo.
- Archivos descargados, con la verificación o fase que los motivó.
- Conteo de afirmaciones por tipo (a/b/c) y por `tipo_error`. Compáralo con 2020:
  187 afirmaciones, 41 discrepancias, 17 % no verificable.
- Resultado de los dos pendientes heredados.
- Anomalías: lo que no cierra y no supiste explicar. Descríbelas, no las
  resuelvas.
- Qué debería cambiar en la instrucción de 2022.

---

## 13. Límites

- No califiques globalmente el documento de CIEP ni su solvencia analítica.
  Entregas hallazgos con evidencia; la lectura es humana.
- No presentes coincidencias de magnitud como si fueran relaciones (§1.6).
- No modifiques nada dentro de `2021/` salvo agregar archivos oficiales y su
  fila de manifiesto.
- Donde no puedas verificar, dilo. La utilidad de la corrida depende enteramente
  de que los huecos estén declarados.
