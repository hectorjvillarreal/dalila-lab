# Instrucción de trabajo — Evaluación del documento CIEP, ejercicio 2023

**Versión 2.** Sustituye a la v1. Cambios de fondo en §2.7 (nomenclatura),
§5 (piezas metodológicas), §6.2 (marco de descomposición) y §2.8 (tier autoral).

**Proyecto:** FISCUS
**Ubicación de trabajo:** `FISCUS/económicos_paquetes/`
**Máquina:** Dalila
**Tipo:** instrucción de trabajo (no es build instruction registrada)
**Ejercicio:** 2023 · **Capítulo propio:** DEUDA Y BALANCE
**Antecedentes:** 2020 (pensiones), 2021 (salud), 2022 (ingresos).

---

## 0. Qué cambia en esta corrida

Se cierra el recorrido por las tres partes del género: **(=) Balance y Deuda**.

Y cambia la naturaleza de la prueba. En 2022 el capítulo de deuda de CIEP
**cerró aritméticamente**: cuadro 13.1 correcto, identidades verificadas, techos
reproducidos. Sus tres fallas fueron de otro orden —llamar "déficit público
total" al RFSP, usar una cifra sin distinguir el techo de endeudamiento del
déficit del Gobierno Federal, y reconstruir el saldo 2020 con un PIB revisado
cuando el CGPE daba saldos observados—. Son **errores conceptuales, no de suma**.

Hasta ahora se probó si el sistema sabe verificar cifras. Esta corrida prueba si
sabe **distinguir objetos**. Un capítulo de deuda en el que todo suma y nada
significa lo que dice es el fallo característico de este rubro.

---

## 1. Sección cero obligatoria — estado de la carpeta

**Toda salida abre con un apartado `## Estado de la carpeta`.** No en la
bitácora: en el encabezado de `00`, `03` y `04`.

- Piezas oficiales presentes y ausentes, con la ruta probada para cada ausencia.
- Qué criterios de la rúbrica quedan **condicionados** por esas ausencias.
- Proporción esperada de `no_verificable` atribuible a la carpeta, distinguida de
  la atribuible al documento de CIEP.

En 2022 el 41 % de lo no verificable venía de la carpeta y no del documento. Eso
es información sobre nosotros, no sobre CIEP, y enterrada en la bitácora
terminará leyéndose al revés.

---

## 2. Decisiones fijadas

**2.1 Comparación estructural de ingresos: adoptada.** Tributarios sobre gastos
obligatorios incluidas pensiones (ILIF art. 1o. / DEC Anexo 3): 0.671 en 2021,
0.674 en 2022. **Dos líneas**, con y sin cuotas IMSS en el numerador (0.743 /
0.745), porque las cuotas están afectadas y los tributarios no.
**Condición:** diff del Anexo 3 entre ejercicios antes de extender la serie; su
composición puede cambiar por decreto.

**2.2 Analíticos: sonda acotada, decisión diferida a 2024.** El PEF aprobado
responde para 2022–2026; el proyecto no. Prueba **Transparencia Presupuestaria**
una vez, registra en `mapa_fuentes.md` y detente. Queda escrito: **si solo hay
aprobado, no evaluamos el mismo objeto que CIEP**, que evalúa el proyecto. Es
asimetría de objeto, no de etiqueta, y va en la sección cero.

**2.3 Miscelánea y decretos: admitidos.** Iniciativa de miscelánea vía Gaceta
Parlamentaria; decretos vía DOF. `tier = oficial_primaria`. El campo
`fuente_oficial` **registra el órgano emisor**: una iniciativa en la Gaceta, un
decreto en el DOF y una estimación de la SHCP son actos distintos con estatus
jurídico distinto. Y **prueba la ruta alternativa de cada pieza antes de
declararla ausente**, registrando el intento.

**2.4 Quinta declaración del contrafactual: fijada.** Con qué PIB, y de qué
añada, para cada año. Una sola añada para toda la comparación, declarada al
inicio; cuando la revisión del año base cambie el signo de la lectura, se
presentan las dos y se dice cuál se adopta.

**2.5 Tier por sección.** Se sigue poblando `tier_seccion`
(`restitucion` | `juicio` | `mixta`). Decisión formal de Héctor con Clavellina.

**2.6 Series de seguimiento permanente.** Todos los años, sea cual sea el
capítulo propio, en la bitácora, con sus dos fuentes y sin interpretación:

| Serie | Estado |
|---|---|
| Pensiones IMSS / cuotas IMSS | 1.31 (2020), 1.46 (2021), pendiente (2022) |
| Pasivo pensionario, % del PIB | 43.2 (CGPE 2020), 47.7 (2021), 52.1 (2022) |
| Supuesto oficial de crecimiento real de pensiones | 7.0 % (CGPE 2021), 4.2 % (CGPE 2022) |
| Tributarios / gastos obligatorios | 0.671 (2021), 0.674 (2022) |

El pendiente de 2022 se reintenta con el **PEF aprobado**. La tercera serie es la
más importante para DFD: el supuesto oficial cambió 2.8 puntos anuales entre
paquetes sin explicación. **Un supuesto que se mueve en silencio es un hallazgo.**

### 2.7 Nomenclatura de la casa — RFSPF y SHRFSPF · NUEVO

**Convención adoptada:** el flujo es **RFSPF**, requerimientos financieros del
sector público federal; el acervo es **SHRFSPF**, saldo histórico de los RFSPF.

Los documentos oficiales usan con frecuencia las formas cortas **RFSP** y
**SHRFSP**. **Son el mismo objeto.** Declara la equivalencia una vez en el
capítulo y trata ambas grafías como una sola entidad al extraer y al recuperar,
para que ninguna cita se pierda por la forma del acrónimo.

Cobertura: gobierno federal y entidades del sector público federal. **No incluye
deudas de entidades federativas ni municipios**, que son heterogéneas y requieren
análisis particular. Toda afirmación sobre "deuda pública" que no declare esta
frontera es incompleta.

### 2.8 Tier autoral · NUEVO

Se agrega el valor **`autoral_ited`** al vocabulario de tier, para material de
autoría propia que además fija convención interna y no es ni fuente oficial
primaria ni derivada de CIEP.

Esta corrida lo estrena con dos piezas (§5.2). Anota en la bitácora que el
vocabulario de tier pasó de dos valores a tres, porque esa ampliación y la
decisión pendiente de tier por sección deben resolverse juntas.

---

## 3. Convenciones vigentes

Sin cambio: deflactor del PIB con excepción marcada para prestaciones
individuales; las **cinco** declaraciones del contrafactual; ex ante contra
ex ante; perímetro declarado antes del primer cuadro y constante; umbrales de
0.5 % en niveles y 0.1 pp en tasas con lo atribuible a deflactor aparte;
prohibición de yuxtaponer magnitudes sin mecanismo declarado; fuentes ex post
solo para verificar, nunca como base propia; reparto con subagente con cotejo de
todas las `no`, muestra de las `si` **y muestra de las `no_verificable`**, contra
fuentes y no solo contra el texto.

**Lee `_aprendizaje/` completo antes de empezar.**

---

## 4. Orden de fases — obligatorio

El capítulo propio se redacta **antes** de leer el capítulo de deuda de CIEP.
Registra hora de cierre y hora de primera lectura. Si el orden se rompió, la
comparación no vale y hay que decirlo.

---

## 5. Fase 1 — Piezas, inventario y diffs

### 5.1 Piezas del paquete

CGPE 2023, ILIF 2023 (articulado íntegro con transitorios), PPEF 2023, e
*Implicaciones del Paquete Económico 2023* (CIEP).

### 5.2 Piezas metodológicas obligatorias · NUEVO

Dos documentos que no son del paquete pero sin los cuales este capítulo no se
puede hacer bien. Descárgalos y regístralos en el manifiesto.

1. **SHCP, *Balance Fiscal en México. Definición y Metodología*, abril de 2023.**
   `tier = oficial_primaria`, emisor SHCP. Es la fuente que la propia Secretaría
   reconoce para distinguir balance público, económico, presupuestario,
   financiero y RFSPF, y para la composición de los requerimientos. **Toda
   controversia de definición en esta corrida se resuelve contra este documento,
   no contra criterio propio.**

2. **Cantú, Ramones y Villarreal (2016), "Por un sistema fiscal sostenible y con
   objetivos", *Revista de Economía Mexicana*, Anuario UNAM 1, Jaime Ros (ed.).**
   `tier = autoral_ited`. Presentación técnica del marco de aritmética de deuda
   que esta corrida aplica. Ricardo Cantú es el arquitecto de Layer A: **el marco
   de la evaluación y el del simulador deben ser el mismo.**

Si alguna no es descargable, dilo en la sección cero y sigue; pero regístralo
como condicionante del criterio 1.

### 5.3 Inventario de deuda y balance

Con documento, cuadro y página:

**Los tres flujos:** balance público; balance público sin inversión de alto
impacto; **RFSPF**.

**Los tres acervos:** **SHRFSPF**; deuda neta del sector público federal; deuda
bruta del sector público no financiero. En 2022 fueron 51.0, 49.7 y 58.6 % del
PIB según el paquete. **Los tres, siempre.**

**Advertencia de añada:** las cifras del paquete son *ex ante*; las de informes
trimestrales y cierres son *ex post* y difieren. Para 2022, la serie observada da
SHRFSPF de 50.7 % al cierre de 2021 y 49.4 % al cierre de 2022, con RFSPF de
4.5 %. No mezcles las dos series en un mismo cuadro; declara cuál usas (§2.4 y
§1.2 de la instrucción 2022).

**Techos de endeudamiento** (ILIF, art. 2o. y siguientes): interno, externo,
Ciudad de México, y por entidad (Pemex, CFE, banca de desarrollo). **El techo es
una autorización de endeudamiento neto; el déficit es un flujo.** En 2022 ambos
daban 850 mil mdp por coincidencia, y esa coincidencia es la trampa.

**Costo financiero:** Ramo 24 desagregado, más el de entidades de control
directo.

**Perfil de amortizaciones** e **indicadores del portafolio**: plazo promedio,
duración, proporción a tasa fija, proporción en moneda extranjera. Esta última
importa de manera directa: alrededor de una cuarta parte de la deuda pública
mexicana está denominada en otras monedas, así que el tipo de cambio entra en la
aritmética (§6.2).

**Contingencias:** pasivo pensionario, Pidiregas, PPS, garantías.

### 5.4 Diffs previos a escribir

- **Anexo 3 del decreto** (gastos obligatorios), 2022 → 2023, por §2.1.
- **Artículos de endeudamiento de la ILIF**, 2022 → 2023.
- **Definiciones del CGPE**: cambios de nomenclatura o de agregado respecto al
  año previo, cotejados contra el documento metodológico de §5.2.1.

### 5.5 Reconciliaciones obligatorias

Ambas quedan escritas aunque cierren.

1. **ILIF ↔ CGPE en ingresos.** En 2022 quedaron 56.9 mdp sin explicar (57.0 en
   2021), presumiblemente ISR de contratistas y asignatarios que la ILIF clasifica
   en impuestos y el CGPE en petroleros. Verifica si reaparece en 2023.

2. **Flujo contra acervo.** El cambio del SHRFSPF **no es igual** a los RFSPF del
   periodo. Documenta la brecha y sus componentes. Si el paquete no permite
   cerrarla, dilo: eso mismo es hallazgo.

---

## 6. Fase 2 — Capítulo propio de DEUDA Y BALANCE, a ciegas

Plantilla: **POLÍTICA DE DEUDA 2023 / EVOLUCIÓN DEL BALANCE Y LA DEUDA /
INSTRUMENTOS Y TECHOS / IMPLICACIONES.**

### 6.1 Declaraciones de apertura

- **Cuál flujo** de los tres, en cada afirmación.
- **Cuál acervo** de los tres.
- **Qué añada de PIB** para cada año, y si la serie es ex ante o ex post.
- **Perímetro institucional:** Gobierno Federal, sector público presupuestario,
  sector público federal, sector público no financiero. No son intercambiables,
  y ninguno incluye entidades federativas y municipios.

### 6.2 Marco de descomposición — CORREGIDO respecto a la v1

**El marco canónico es el de cuatro variables sobre la razón SHRFSPF / PIB:**

1. **Crecimiento económico.** Agranda el denominador y baja la razón. Una
   economía que crece con vigor sostiene mayor endeudamiento sin deteriorar el
   cociente.
2. **Tasa de interés real.** Determina el servicio. Los intereses del periodo se
   pagan, así que no acumulan saldo directamente, pero presionan los RFSPF y por
   esa vía sí alimentan el acervo. El efecto es indirecto y hay que trazarlo
   como tal.
3. **Inflación.** Vía doble y de signo opuesto: si el PIB nominal crece y los
   pasivos no lo siguen, la razón baja; pero si la tasa nominal sigue a la
   inflación o la excede, la presión sobre los RFSPF aumenta el acervo. **No
   supongas el signo: calcúlalo.**
4. **Tipo de cambio.** Aproximadamente una cuarta parte de la deuda está en otras
   monedas, así que depreciación y apreciación mueven el SHRFSPF.

La versión de manual —balance primario más diferencial r − g más ajustes— se
mantiene **solo como verificación cruzada, etiquetada y en cuadro aparte**.
Razón: exige un primario congruente con el acervo amplio, que el paquete no
siempre publica limpio; y el marco de cuatro variables opera sobre magnitudes que
sí están publicadas. Si presentas la versión de manual, el par acervo–flujo debe
ser SHRFSPF–RFSPF con su propio primario. **Nunca un acervo amplio con un
primario presupuestario:** el balance estabilizador resultante queda sesgado, y
sesgado hacia el optimismo.

### 6.3 Validación obligatoria con el caso 2022 · NUEVO

Antes de aplicar la descomposición a 2023, **reprodúcela para 2022**, donde el
resultado se conoce: con RFSPF de 4.5 % del PIB, el SHRFSPF **bajó** de 50.7 a
49.4 %. La combinación fue crecimiento importante, inflación alta, pago de
intereses contenido y apreciación del peso.

Descompón esa caída de 1.3 puntos en las cuatro variables. **Si tu descomposición
no reproduce el signo y el orden de magnitud, no está funcionando y debes
reportarlo antes de aplicarla a 2023.** Ese es el criterio de aceptación.

### 6.4 Proyección ilustrativa

Con los supuestos de los CGPE, proyecta la trayectoria del SHRFSPF. Declara cada
supuesto y preséntalo como aritmética, no como pronóstico.

Ejecuta al menos **dos escenarios que difieran solo en inflación**, manteniendo
RFSPF y crecimiento constantes. El resultado no es intuitivo y por eso importa:
en el ejercicio de referencia, con RFSPF de 5 % del PIB y crecimiento de 3 %
durante veinte años desde 49.1 %, una inflación de 5 % lleva el acervo a 62.75 %
del PIB, y una de 3 % lo lleva a 75.45 %. **Menos inflación puede producir más
deuda como proporción del producto.** Verifica si tu marco lo reproduce.

### 6.5 Sensibilidad

Aplica las sensibilidades publicadas en los CGPE al servicio de deuda y al
acervo: qué implica un punto de tasa, un peso de tipo de cambio, un punto de
crecimiento. Si el paquete no publica la sensibilidad del costo financiero, dilo.

### 6.6 Lo que 2023 tiene de particular — verifícalo, no lo des por hecho

- **Ciclo de alzas de tasas** y su efecto sobre el costo financiero: cómo lo
  estima el paquete y contra qué trayectoria.
- **Apoyos a Pemex:** qué es aportación patrimonial, qué es reducción de carga
  fiscal, qué es endeudamiento de la empresa. Tres caminos, tres efectos
  distintos sobre flujo y sobre acervo.
- **Registro de proyectos de inversión:** presupuestario o no presupuestario.
- **Plan Anual de Financiamiento:** se publica en diciembre y **no forma parte
  del paquete**, igual que el Presupuesto de Gastos Fiscales. Si CIEP lo invoca,
  es fuente externa y así se marca.

### 6.7 Comparación estructural

Propón una canónica para deuda, con el estándar de las tres adoptadas: **habla de
estructura o financiamiento, no de magnitud, y se sostiene con la fuente en la
mano.** Candidata a evaluar, no a asumir: **costo financiero sobre ingresos
tributarios**. Justifica la elegida y descarta las demás por escrito.

### 6.8 Reglas de redacción

Cifra con fuente. Comparaciones con las cinco declaraciones. Ex ante contra
ex ante. Si un dato no es obtenible, dilo. El juicio va en IMPLICACIONES.

`_evaluacion/2023/01_capitulo_propio_deuda.md`. Ciérralo, anota la hora.

---

## 7. Fase 3 — Verificación de cifras

```
id, capitulo, seccion, afirmacion, tipo, tier_seccion, valor_ciep,
fuente_oficial, valor_oficial, coincide, discrepancia, tipo_error,
contrafactual_explicito, nota
```

**Sexto valor de `tipo_error`: `objeto`.** Aplica cuando la cifra es correcta
pero nombra la cosa equivocada: llamar déficit al RFSPF, deuda al SHRFSPF, techo
al déficit, sector público federal al no financiero, o incluir entidades
federativas en un agregado que no las cubre. Es el error característico del rubro
y en 2022 no tenía categoría.

`fuente_oficial` registra el órgano emisor además del documento (§2.3).

### 7.1 Verificación del frente del documento

Trata resumen ejecutivo e introducción de CIEP como objeto propio, con sus filas
en el CSV. En 2022 el frente contradijo a los capítulos en cuatro cifras, y es lo
que la mayoría de los lectores lee.

---

## 8. Fase 4 — Evaluación de calidad

1. **Identidad de objeto.** ¿Cada agregado nombrado con precisión? ¿Se distinguen
   los tres flujos, los tres acervos, el techo del déficit, los perímetros
   institucionales, la frontera federal? Cada confusión, con cita y nombre
   correcto, **adjudicada contra el documento metodológico de §5.2.1**.
   Primer criterio en este rubro.
2. **Contrafactual declarado**, incluida la quinta declaración y la distinción
   ex ante / ex post.
3. **Cierre contable y consistencia flujo–acervo.**
4. **Trato de los supuestos macro.** Tasas, crecimiento, inflación, tipo de
   cambio: las cuatro variables del marco. ¿CIEP las interroga o las adopta?
   ¿Hace sensibilidad del costo financiero?
5. **Cobertura**, incluidos techos por entidad, contingencias y perfil de
   amortizaciones. Agota rutas antes de declarar ausencias.
6. **Separación descriptivo–normativo** y **horizonte.** En deuda el horizonte se
   juega en si el documento razona sobre sostenibilidad con la aritmética
   completa o se detiene en el nivel del año.

`_evaluacion/2023/03_evaluacion_calidad.md`, con sección cero.

---

## 9. Fase 5 — Comparación

`_evaluacion/2023/04_comparacion_deuda.md`, con sección cero. Coincidencias; lo
que CIEP tiene y tú no; lo que tú tienes y CIEP no; diferencias de método.

Atención particular a las diferencias de método: dos lecturas de la deuda pueden
diferir enteramente por elección de agregado sin que ninguna cifra esté mal.
Describe la diferencia y qué implica cada elección, sin declarar ganador.

---

## 10. Tareas laterales acotadas

**10.1** Sonda a Transparencia Presupuestaria por el proyecto. Ruta y resultado
en `mapa_fuentes.md`. No descargues.

**10.2** Las cuatro series de seguimiento (§2.6), con fuentes. Reintenta la de
pensiones IMSS / cuotas IMSS para 2022 con el PEF aprobado.

**10.3** Trayectoria del DUC (65 → 58 → 54 → 40) reconstruida con los decretos
del DOF. Pendiente de 2022. Serie y decretos, sin interpretación.

**10.4 · NUEVO — candidata para el harness.** Registra en la bitácora, con su
respuesta y su derivación, el ejercicio de §6.4: por qué una inflación menor
puede elevar la razón deuda/PIB manteniendo RFSPF y crecimiento constantes. No es
contestable de memoria, se resuelve por completo con el marco, y por eso es
buena pregunta de evaluación. Sin desarrollarla más: solo dejarla registrada.

**Ninguna otra.** Las tesis del IVA (2020) y de la elasticidad (2022) quedan
fuera: su adjudicación es manual y corresponde a la autoridad definicional.

---

## 11. Fase 6 — Artefactos de aprendizaje

Agrega, no sobrescribas. Entrada fechada en `## Historial`.

**`especificacion_genero.md`** — con esta corrida quedan cubiertas las tres
partes. Escribe una **caracterización comparada**: qué distingue estructuralmente
un capítulo de ingresos, uno de gasto y uno de deuda; qué error es característico
de cada uno; qué verificación es barata y cuál cara en cada parte. Ese apartado
es el que se usa cuando toque leer un paquete en vivo.

**`mapa_fuentes.md`** — dónde vive cada flujo, cada acervo, cada techo, el perfil
de amortizaciones y los indicadores del portafolio. Las dos piezas metodológicas
de §5.2. Rutas de Gaceta Parlamentaria y DOF. Resultado de las sondas.

**`rubrica.md`** — identidad de objeto como primer criterio del rubro; el valor
`objeto`; la quinta declaración; la sección cero; la verificación del frente;
la nomenclatura RFSPF/SHRFSPF con su equivalencia; el valor `autoral_ited`;
y el marco de cuatro variables con el caso 2022 como criterio de aceptación.

---

## 12. Bitácora

`_evaluacion/2023/_bitacora_evaluacion.md`:

- Inicio y fin (ISO).
- **Hora de cierre del capítulo propio y hora de primera lectura del capítulo de
  deuda de CIEP.**
- Piezas descargadas, rutas alternativas probadas, qué motivó cada descarga.
- **Resultado de la validación 2022 (§6.3).** Si no reprodujo la caída de 1.3
  puntos, dilo primero y antes que nada.
- Conteos por tipo (a/b/c), por `tipo_error` —incluido `objeto`—, por
  `tier_seccion` y por `contrafactual_explicito`. Compara con la serie: 2020,
  38 % coincidencia exacta y 22 % discrepancia; 2021, 54 % y 18 %, perímetro
  dominante; 2022, 65 % de acierto sobre lo verificable en ambos lados, con
  perímetro dominante en gasto y transcripción/base en ingresos. Di si deuda se
  parece a alguno o es un cuarto patrón.
- Las cuatro series de seguimiento y la candidata de harness.
- Anomalías: lo que no cierra y no supiste explicar. Descríbelas, no las
  resuelvas.
- Qué debería cambiar para 2024, cuando se vuelve a gasto con educación y se
  decide el asunto de los analíticos.

---

## 13. Límites

- No califiques globalmente el documento de CIEP ni su solvencia analítica.
- No presentes coincidencias de magnitud como si fueran relaciones.
- No uses fuente ex post como base de comparación del capítulo propio.
- No uses el pasivo pensionario ni el supuesto de crecimiento de pensiones en
  ninguna calibración: congelados hasta que se descompongan.
- No resuelvas controversias de definición por criterio propio: se adjudican
  contra el documento metodológico de la SHCP (§5.2.1).
- No modifiques nada dentro de `2023/` salvo agregar archivos oficiales y su fila
  de manifiesto.
- Donde no puedas verificar, dilo, y dilo en la sección cero.
