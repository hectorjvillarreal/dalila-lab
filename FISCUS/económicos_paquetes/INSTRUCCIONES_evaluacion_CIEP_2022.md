# Instrucción de trabajo — Evaluación del documento CIEP, ejercicio 2022

**Proyecto:** FISCUS
**Ubicación de trabajo:** `FISCUS/económicos_paquetes/`
**Máquina:** Dalila
**Tipo:** instrucción de trabajo (no es build instruction registrada)
**Ejercicio:** 2022 · **Capítulo propio:** INGRESOS
**Antecedentes:** corridas 2020 (pensiones) y 2021 (salud). Las seis decisiones
abiertas en el memo de 2021 quedan resueltas en §1 y no se reabren.

---

## 0. Cambio de parte del documento

Las dos corridas anteriores evaluaron capítulos de la **Parte II (−) Gasto**.
Esta entra a la **Parte I (+) Ingresos**. Es deliberado.

Tres razones. El método ya se probó dos veces sobre el mismo tipo de objeto y un
tercer capítulo de gasto confirmaría lo que ya sabemos. El hallazgo más grave de
2020 —la tesis del IVA— vive del lado del ingreso y lo congelamos por no tener
método para adjudicarlo. Y el sistema se entrega a la SHCP, que es
técnicamente más fuerte precisamente en el lado del ingreso: llegar sabiendo
auditar solo gasto es llegar cojo.

Hay además una razón práctica que decide: **un capítulo de ingresos no depende de
los analíticos del PPEF.** Se verifica contra el artículo 1o de la ILIF, la
exposición de motivos de la iniciativa y el marco macro de los CGPE, todo en
PDF y todo ya en carpeta. Mientras se resuelve el 404 de los xlsx 2022–2026, la
serie avanza.

---

## 1. Decisiones fijadas tras la corrida 2021

**1.1 Perímetro canónico de salud** (para cuando vuelva a usarse): cuadro de la
EM p. 67–68, siete líneas, presentado en dos bloques etiquetados —contributivo y
no contributivo—, FASSA dentro del no contributivo, servicios médicos de Pemex
fuera como partida informativa. Va a `especificacion_genero.md`.

**1.2 Fuentes ex post: admitidas solo para verificar.** Informes trimestrales y
Cuenta Pública pueden usarse **únicamente** para verificar afirmaciones de CIEP
que comparen contra modificado o ejercido. **Nunca** como base de una comparación
del capítulo propio. La convención sigue siendo ex ante contra ex ante. Toda fila
del CSV que se apoye en fuente ex post lo marca en `nota`.

**1.3 Analíticos 2022–2026.** Prueba acotada, no proyecto: la ruta del **PEF
aprobado** y, si falla, **Transparencia Presupuestaria**. Solo comprobar
disponibilidad y registrar rutas. Si resultara que únicamente existe el aprobado,
aprobado contra aprobado es aceptable **con etiqueta explícita**, pero es
decisión para 2023, no para esta corrida.

**1.4 Comparación estructural de salud:** adoptada como canónica (cuotas
obrero-patronales / gasto en salud IMSS = 0.85; pensiones IMSS+ISSSTE = 2.11× su
salud). Y una obligación nueva: **la razón pensiones IMSS / cuotas IMSS se
calcula todos los años**, sea cual sea el capítulo propio. Pasó de 1.31 (2020) a
1.46 (2021); como serie vale más que como dato aislado. Va en la bitácora.

**1.5 Reparto con subagente:** aceptado como método estándar. Cotejo mínimo
obligatorio: **todas** las filas con `coincide = no`, más una muestra de las `si`,
**cotejadas contra las fuentes y no solo contra el texto de CIEP**.

**1.6 Tier por sección:** sigue pendiente de decisión de Héctor, con Clavellina
como autoridad definicional. Mientras tanto, **puebla desde ahora la columna
`tier_seccion`** con `restitucion` o `juicio` según la subsección del género
(POLÍTICA y EVOLUCIÓN → restitución; IMPLICACIONES → juicio; cualquier caso
ambiguo → `mixta`, y anótalo). Así, cuando se decida, no habrá que reprocesar
tres ejercicios.

---

## 2. Convenciones vigentes — no se discuten

Rigen las de la instrucción 2021, sin cambio: deflactor del PIB con excepción
marcada para prestaciones individuales (§1.1 de 2021); las cuatro declaraciones
del contrafactual —nominal o real, contra aprobado o contra cierre, contra año
previo o contra PIB, en pesos de qué año—; comparación ex ante contra ex ante;
perímetro declarado antes del primer cuadro y constante dentro del capítulo;
umbrales de 0.5 % en niveles y 0.1 pp en tasas con lo atribuible a deflactor
reportado aparte; prohibición de yuxtaponer magnitudes sin mecanismo declarado;
y declaración explícita de cuál de los tres balances se usa.

**Lee `_aprendizaje/` completo antes de empezar.** Los tres archivos se
actualizan, no se sobrescriben.

---

## 3. Lo que las dos corridas anteriores enseñaron y aquí se aplica

**El error se desplazó de contrafactual a perímetro.** En 2021, de 42 filas con
tipo de error, 16 fueron perímetro contra 13 de contrafactual. Los dos criterios
van ahora al mismo rango en la rúbrica.

**Los transitorios de la ILIF llevan información.** En 2021 la única cifra
oficial del FONSABI en todo el paquete estaba en un transitorio. Para un capítulo
de ingresos esto deja de ser una lección y pasa a ser el centro: los transitorios
y los artículos de estímulos son donde vive buena parte de la política de
ingresos.

**Las reclasificaciones fabrican tendencias.** El diff de códigos entre t−1 y t
se hace **antes** de escribir una línea, no se descubre a medio camino.

---

## 4. Fuentes y descarga

En `FISCUS/económicos_paquetes/2022/`: CGPE 2022, ILIF 2022, PPEF 2022, e
*Implicaciones del Paquete Económico 2022* (CIEP).

Verifica que la ILIF esté **completa**: iniciativa (articulado íntegro, incluidos
transitorios) y exposición de motivos. Si falta el articulado completo,
descárgalo antes de nada; sin él este capítulo no se puede hacer.

Descarga por demanda, con las reglas de siempre: navegar sin construir URLs,
verificar cabecera `%PDF`, una petición cada 2 segundos, fila en
`_manifiesto.csv` con sha256, fecha de acceso y tier (`oficial_primaria` o
`derivada_ciep`).

---

## 5. Orden de fases — obligatorio

El capítulo propio de ingresos se redacta **antes** de leer el capítulo de
ingresos de CIEP. Registra hora de cierre del capítulo propio y hora de primera
lectura del capítulo de CIEP. Si el orden se rompió, la comparación no vale y hay
que decirlo.

---

## 6. Fase 1 — Inventario y diff estructural

### 6.1 Inventario del paquete oficial 2022

Como siempre: marco macro completo de los CGPE, ingresos y su desagregación,
gasto neto por ramo, metas de balance y RFSP. Cada cifra con documento, cuadro y
página.

### 6.2 Diff estructural ILIF 2021 → ILIF 2022

**Antes de escribir una línea.** Compara la estructura del artículo 1o entre
ejercicios: rubros que cambian de numeración, de nombre, de nivel de agregación,
o que aparecen y desaparecen. Cualquier serie que crucemos entre años está rota
donde haya un cambio de estos, y es exactamente el error que en 2021 hizo caer la
subfunción 5 un 43.5 % sin que cayera un peso.

Igual para los artículos de estímulos y para los transitorios: qué se mantiene,
qué es nuevo, qué desapareció.

Resultado en `_evaluacion/2022/00_inventario_paquete.md`, con apartado propio de
diff.

### 6.3 Reconciliación obligatoria

El artículo 1o de la ILIF y el cuadro de ingresos presupuestarios de los CGPE
tienen que reconciliar. Si no reconcilian, esa diferencia es el primer hallazgo
del capítulo y hay que explicarla antes de seguir.

---

## 7. Fase 2 — Capítulo propio de INGRESOS, a ciegas

Plantilla del género: **POLÍTICA DE INGRESOS 2022 / EVOLUCIÓN DE LOS INGRESOS /
FUENTES SELECCIONADAS / IMPLICACIONES.**

### 7.1 El perímetro cambia de naturaleza

En gasto el problema era qué sumar. En ingresos la trampa es otra y hay que
declararla antes del primer cuadro:

- **El total del artículo 1o incluye ingresos por financiamiento**, es decir
  deuda. Cualquier razón construida sobre "ingresos totales" sin declarar si
  incluye endeudamiento está mal. Distingue siempre **ingresos presupuestarios**
  de **ingresos totales**.
- **Gobierno Federal contra organismos y empresas** (IMSS, ISSSTE, Pemex, CFE).
  El artículo 1o está estructurado así y agregarlos sin etiqueta borra de dónde
  viene el dinero.
- **Petroleros:** transferencias del Fondo Mexicano del Petróleo, y el reparto
  entre Gobierno Federal y Pemex. Declara qué concepto usas.
- **Tributarios brutos o netos** de devoluciones y compensaciones.
- **Participaciones:** la recaudación federal participable es bruta; lo que queda
  al Gobierno Federal después de participaciones es otro objeto. No los mezcles
  en un cociente.
- **Aprovechamientos:** separa lo recurrente de lo no recurrente
  (aprovechamientos por recuperación de fideicomisos, remanentes, activos
  financieros). Un año que cierra con no recurrentes altos no es comparable con
  uno que no los tiene, y presentarlos juntos fabrica una tendencia.

### 7.2 Los supuestos macro suben de rango

En un capítulo de gasto los supuestos macro de los CGPE son contexto. En uno de
ingresos son **el determinante directo**: crecimiento del PIB, inflación, tipo de
cambio, tasas, precio de la mezcla y plataforma de producción entran en la
estimación de cada renglón.

Tu capítulo debe declarar qué supuesto sostiene qué estimación, y decir si el
paquete presenta o no un análisis de sensibilidad. Si la meta de recaudación
descansa en supuestos de eficiencia recaudatoria en lugar de en cambios de tasa,
dilo con la cita: es una afirmación de política, no de aritmética.

### 7.3 Lo que 2022 tiene de particular — verifícalo, no lo des por hecho

Trátalo como expectativa a comprobar contra el texto, no como dato:

- El **Régimen Simplificado de Confianza** y su tratamiento en la miscelánea:
  ¿se le atribuye recaudación estimada, y con qué base?
- Efectos de base de la **reforma de subcontratación de 2021** sobre ISR de
  nómina y sobre cuotas de seguridad social.
- Si el paquete propone **tasas nuevas** o descansa en administración y
  eficiencia.
- **IEPS de combustibles** y el mecanismo de estímulo: cómo se estima cuando el
  estímulo puede anular la recaudación del renglón.
- **Gastos fiscales:** el Presupuesto de Gastos Fiscales es un documento
  distinto, publicado en junio, **fuera del paquete**. Si CIEP lo invoca, es
  fuente externa y así debe marcarse.

### 7.4 Comparación estructural

Propón una comparación estructural canónica para el capítulo de ingresos, con el
mismo estándar que las de pensiones y salud: **tiene que hablar de estructura o
de financiamiento, no solo de magnitud, y sostenerse con la fuente en la mano.**
Candidatas a evaluar, no a asumir: tributarios sobre gasto programable;
dependencia petrolera medida sin ingresos por financiamiento; tributarios sobre
gasto no programable. Justifica la que elijas y descarta las otras por escrito.

### 7.5 Reglas de redacción

Cifra con fuente (documento, cuadro, página). Comparaciones con las cuatro
declaraciones. Ex ante contra ex ante. Si un dato no es obtenible, dilo; no
estimes para completar el relato. El juicio va en IMPLICACIONES.

Escribe `_evaluacion/2022/01_capitulo_propio_ingresos.md`, ciérralo, anota la
hora.

---

## 8. Fase 3 — Verificación de cifras

Extrae toda afirmación cuantitativa de CIEP. Clasifica en **(a) restitución**,
**(b) derivación** reproducible paso a paso, **(c) juicio**.

`_evaluacion/2022/02_verificacion_cifras.csv`, con dos columnas nuevas respecto a
2021:

```
id, capitulo, seccion, afirmacion, tipo, tier_seccion, valor_ciep,
fuente_oficial, valor_oficial, coincide, discrepancia, tipo_error,
contrafactual_explicito, nota
```

- `tier_seccion`: `restitucion` | `juicio` | `mixta` (§1.6).
- `contrafactual_explicito`: `si` | `no` | `na`. En 2021 el conteo del criterio 1
  se hizo a mano; ahora sale del CSV.
- `tipo_error` conserva sus cinco valores: `transcripcion`, `contrafactual`,
  `perimetro`, `omision`, `deflactor`.

Cuando la verificación no sea posible: `coincide = no_verificable` y `nota` dice
qué fuente haría falta. Si se usó fuente ex post, márcalo (§1.2). **No aproximes.**

Aplica el cotejo mínimo de §1.5 a cualquier extracción delegada.

---

## 9. Fase 4 — Evaluación de calidad

Seis criterios, sin calificación global, cada hallazgo con cita a sección de CIEP
y a fuente oficial. Orden para un capítulo de ingresos:

1. **Contrafactual declarado.** Tasa y lista de incompletas, ahora desde la
   columna del CSV.
2. **Perímetro.** ¿Declarado? ¿Constante? ¿Hay cocientes que mezclen ingresos
   presupuestarios con totales, brutos con netos, o Gobierno Federal con
   organismos? Cada caso con cifras.
3. **Trato de los supuestos macro.** Sube al tercer lugar por lo dicho en §7.2.
   ¿CIEP interroga los supuestos, hace sensibilidad, o los adopta sin comentario?
   Si la meta de ingresos depende de eficiencia recaudatoria, ¿lo señala?
4. **Cobertura.** Contra el inventario: qué omite CIEP, con la cifra y su fuente.
   **Agota las rutas antes de declarar algo ausente**, incluidos transitorios y
   artículos de estímulos.
5. **Cierre contable.** Que (+) ingresos, (−) gasto, (=) balance sean
   consistentes, con el balance nombrado.
6. **Separación descriptivo–normativo** y **horizonte**, como en corridas
   previas. En ingresos, el horizonte se juega en si el documento distingue
   recaudación estructural de no recurrente.

`_evaluacion/2022/03_evaluacion_calidad.md`.

---

## 10. Fase 5 — Comparación

`_evaluacion/2022/04_comparacion_ingresos.md`. Cuatro apartados: coincidencias;
lo que CIEP tiene y tú no; lo que tú tienes y CIEP no; diferencias de método.

Por cada cosa que CIEP encontró y tú no: dónde estaba el dato y por qué no
llegaste a él. Ya no hay excusa de descarga tardía ni de columnas sin explotar.

---

## 11. Tareas laterales acotadas

**11.1 Rutas de analíticos 2022–2026.** Prueba la ruta del PEF aprobado y, si
falla, Transparencia Presupuestaria. Solo disponibilidad y ruta, registradas en
`mapa_fuentes.md`. **No descargues.**

**11.2 Serie pensiones IMSS / cuotas IMSS.** Calcúlala para 2022 con la ILIF y la
EM del PPEF, y añádela a la serie (1.31 en 2020, 1.46 en 2021). Solo la cifra con
sus dos fuentes; sin interpretación.

**Ninguna otra tarea lateral.** La tesis del IVA de 2020 sigue fuera del alcance
de estas corridas.

---

## 12. Fase 6 — Artefactos de aprendizaje

Agrega, no sobrescribas. Entrada fechada en `## Historial`.

**`especificacion_genero.md`** — incorpora el perímetro canónico de salud (§1.1),
la comparación estructural de salud adoptada (§1.4), y lo que 2022 enseñe sobre
la arquitectura del capítulo de ingresos: qué subsecciones tiene, qué tipo de
afirmación aparece en cada una, y en qué se distingue estructuralmente de un
capítulo de gasto.

**`mapa_fuentes.md`** — qué documento y qué cuadro alimenta cada sección del
capítulo de ingresos. Con detalle sobre dónde vive cada perímetro y en qué
artículo o transitorio de la ILIF está cada instrumento.

**`rubrica.md`** — el reorden de criterios para ingresos, las columnas nuevas del
CSV, y los casos límite que aparezcan. Si un criterio no funcionó en este tipo de
capítulo, dilo.

---

## 13. Bitácora

`_evaluacion/2022/_bitacora_evaluacion.md`:

- Inicio y fin (ISO).
- **Hora de cierre del capítulo propio y hora de primera lectura del capítulo de
  ingresos de CIEP.**
- Archivos descargados y qué los motivó.
- Conteos por tipo (a/b/c), por `tipo_error` y por `tier_seccion`. **Compáralos
  con la serie:** 2020, 187 afirmaciones, 38 % coincidencia exacta, 22 %
  discrepancia; 2021, 54 % y 18 %, con 16 perímetro / 13 contrafactual / 11
  transcripción. Si la distribución de ingresos se parece a la de gasto, tenemos
  un patrón del género; si no, tenemos dos géneros distintos y hay que decirlo.
- Resultado de las tareas laterales.
- Anomalías: lo que no cierra y no supiste explicar. Descríbelas, no las
  resuelvas.
- Qué debería cambiar para 2023 (deuda y balance).

---

## 14. Límites

- No califiques globalmente el documento de CIEP ni su solvencia analítica.
- No presentes coincidencias de magnitud como si fueran relaciones.
- No uses fuente ex post como base de comparación del capítulo propio.
- No modifiques nada dentro de `2022/` salvo agregar archivos oficiales y su fila
  de manifiesto.
- Donde no puedas verificar, dilo. Un hueco declarado es utilizable; uno tapado
  contamina todo lo que venga después.
