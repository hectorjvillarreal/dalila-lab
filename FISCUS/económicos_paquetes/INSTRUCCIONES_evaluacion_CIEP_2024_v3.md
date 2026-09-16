# Instrucción de trabajo — Evaluación del documento CIEP, ejercicio 2024

**Versión 3.** Sustituye a la v1 (no ejecutada) y recoge la auditoría del
subagente de 2023 (`20260906_FISCUS_ajustes_instruccion_2024_cath.md`).

**Cambios respecto a la v1:**
- Se aplican las cuatro correcciones del subagente (§2.8, §4 serie IMSS, §4
  pasivo pensionario, §0 filas de educación).
- Se resuelven las tres confirmaciones que pedía (§2.10, §4.1, §5.5).
- **Resecuenciación:** ninguna dependencia de red bloquea la corrida. La v1 puso
  tres candados de red antes de la primera línea de análisis y por eso no
  arrancó.

**Proyecto:** FISCUS · **Ejercicio:** 2024 · **Capítulo propio:** EDUCACIÓN
**Ubicación:** `FISCUS/económicos_paquetes/` · **Máquina:** Dalila
**Tipo:** instrucción de trabajo (no es build instruction registrada)

---

## 0. Regla de no bloqueo — rige sobre todo lo demás

**Ninguna descarga es precondición de nada.** Si una pieza no se obtiene tras dos
intentos: se registra en la sección cero con la ruta probada y la respuesta del
servidor, **y la corrida continúa** con lo que hay en carpeta.

El portal `ppef.hacienda.gob.mx` devolvía 404 para todo el rango 2022–2026 el
2026-09-05, y su certificado TLS está mal encadenado. Es un servidor que falla de
formas conocidas. La corrida tiene que entregar aunque siga caído.

**Entrega degradada antes que no entrega.** Un capítulo propio hecho con fuentes
incompletas y declaradas vale; una corrida que no arranca no vale nada.

---

## 1. Por qué educación

Cierra la **tríada de perfiles de edad de NTA**: pensiones (vejez), salud (todo
el ciclo), educación (juventud). Layer B es el sistema de NTA y estos tres son su
columna vertebral.

Es además el primer rubro **predominantemente federalizado**: el FONE vive en el
Ramo 33, no en el Ramo 11. La distinción federal / federalizado deja de ser nota
al margen y pasa a decidir el resultado.

**Qué faltó en 2023 y por qué:** de 32 filas de educación quedaron 23 sin
verificar por **tres** piezas ausentes —analíticos del Gobierno Federal,
exposición de motivos y PEF 2022 aprobado—, no solo por los analíticos. Y los
analíticos aprobados **no resuelven** el cuadro 7.3 de CIEP: seis de sus ocho
columnas son ejercido 2016–2021, es decir Cuentas Públicas, que no están en
carpeta. No esperes de los analíticos lo que no dan.

---

## 2. Decisiones

**2.1 Quinta declaración:** se reportan las dos tasas. La estricta (cinco
declaraciones) es la principal; la de cuatro se conserva como puente de serie.
En 2023 fueron 17 % y 68 %.

**2.2 Analíticos: aprobado contra aprobado, con etiqueta.** Analíticos del **PEF
aprobado** de Gobierno Federal 2023 y 2024 (≈10 MB cada uno); entidades si el
capítulo los requiere. Tres condiciones:
- Toda fila resuelta así lleva en `nota` la marca **"PEF aprobado, no proyecto"**.
- La asimetría de objeto va en la sección cero: **CIEP evalúa el proyecto;
  nosotros verificamos contra el aprobado.**
- **Antes de atribuir a CIEP una discrepancia, comprueba si la explica una
  reasignación de la Cámara.** En 2023 tres renglones del cuadro 8.3 diferían por
  eso, incluso en entidades.

**2.3 Analíticos de entidades:** admitidos como fuente de segundo nivel, misma
marca y misma reserva.

**2.4 Tier.** Tres valores (`oficial_primaria`, `derivada_ciep`, `autoral_ited`).
`tier_seccion` se sigue poblando y sigue provisional; decisión de Héctor con
Clavellina.

**2.5 `objeto` frente a `perimetro` — prueba de divulgación.** Si los componentes
del agregado están a la vista y el lector puede ver qué se sumó, es `perimetro`;
si la etiqueta sustituye a los componentes y afirma una identidad que no se
cumple, es `objeto`. Adefas dentro del "costo de la deuda" (V216) queda en
`perimetro`.

**2.6 Marco de manual: retirado de la presentación.** El paquete no publica un
primario del RFSPF y el del balance económico sesga al optimismo por una o dos
décimas. Un contraste sistemáticamente sesgado, colocado junto al bueno, termina
citándose. Se conserva **solo como diagnóstico en la bitácora**. La razón queda
escrita en la rúbrica para que no se reinvente.

**2.7 Harness:** adoptada con la formulación "requerimientos financieros fijos en
porcentaje del PIB **en términos nominales**". El mecanismo real es que fijar rf
nominal y bajar la inflación **sube la tasa real que paga el sector público**;
con la misma tasa real, la inflación no cambia nada. Se remite a Fina; esta
corrida no la desarrolla.

**2.8 Deflactor de referencia: el del CGPE** (1.0497 para 2023). Cuando una
diferencia se explique **por completo** por el deflactor implícito de CIEP
(1.0492), la fila va `aprox` con `tipo_error = deflactor`.

> **Excepción de esquema, obligatoria.** Desde 2021 el CSV solo llena
> `tipo_error` cuando `coincide = no`, y el validador de 2023 rechaza cualquier
> otra combinación. Esta decisión introduce **una única excepción**:
> `tipo_error = deflactor` es admisible con `coincide = aprox`. **Cualquier otro
> valor de `tipo_error` en una fila `aprox` es error de captura.** Ajusta el
> validador y deja la excepción escrita en la rúbrica, o la corrida tropieza con
> su propia regla.

Regla permanente: **nunca derives un deflactor de agregados publicados
redondeados.** Se usa el factor que el CGPE declara.

**2.9 Comparación estructural del gasto: pensiones + costo financiero sobre
tributarios** (0.60 en 2023). Va a la ficha. *Ineludibles / ingresos
presupuestarios* (0.91) solo como informativa etiquetada: los "ineludibles" son
construcción de CIEP sin definición oficial estable, y el denominador mete el
ingreso propio de las empresas productivas en el numerador de unas razones y su
gasto en el denominador de otras. La adoptada comparte denominador con la de
ingresos ya canónica.

**2.10 Remarcado retroactivo de 2023 · CONFIRMADO.** Se remarcan con
`tipo_error = deflactor` las veinte filas `aprox` del CSV de 2023 que citan el
deflactor en su nota (V036, V102, V107, V111, V112, V128, V132, V140, V203, V221,
V256, V290, V291, V296, V299, V309, V312, V320, V369, V384). Están identificadas
una por una y el costo es bajo; una serie que cambia de definición a la mitad
vale menos que el trabajo de rehacerla.

Dos condiciones:
- **La bitácora registra que 2023 se remarcó *ex post*,** para que el conteo no
  se lea como clasificación original.
- **V107 y V111** combinan deflactor con la reclasificación ILIF–CGPE de
  3.4 mmp: el campo lleva la **causa dominante** y la nota registra las dos.

---

## 3. Convenciones vigentes

Nomenclatura **RFSPF/SHRFSPF** con la equivalencia RFSP/SHRFSP declarada una vez;
deflactor del PIB con excepción marcada para prestaciones individuales; las cinco
declaraciones del contrafactual; ex ante contra ex ante; perímetro declarado
antes del primer cuadro y constante; umbrales de 0.5 % en niveles y 0.1 pp en
tasas; prohibición de yuxtaponer magnitudes sin mecanismo; fuentes ex post solo
para verificar; sección cero; verificación del frente del documento; adjudicación
de definiciones contra la nota metodológica de la SHCP; reparto con subagente con
cotejo de todas las `no`, muestra de las `si` y muestra de las `no_verificable`,
contra fuentes y no solo contra el texto.

`tipo_error`: `transcripcion`, `contrafactual`, `perimetro`, `omision`,
`deflactor`, `objeto`.

---

## 4. Series de seguimiento

En la bitácora, con fuentes y sin interpretación.

**4.1 Pensiones IMSS / cuotas IMSS — la serie se parte en dos · CORREGIDO**

Los valores 1.55 (2022) y 1.59 (2023) calculados en la corrida anterior **no se
adoptan como continuación**: mezclan numerador del PEF aprobado con denominador
de la ILIF, es decir aprobado contra proyecto. Y los dos puntos previos, 1.31 y
1.46, salieron de exposición de motivos e ILIF, o sea proyecto en ambos lados.
Cuatro puntos con tres bases distintas no son una serie. Peor: si la Cámara sube
el gasto pensionario, el cociente se infla por construcción.

**Construye dos series internamente consistentes, y nunca una línea híbrida:**

| Serie | Numerador | Denominador | Años |
|---|---|---|---|
| **Ex ante** | EM del PPEF | ILIF | donde ambas existan |
| **Aprobada** | PEF aprobado (TG 4) | **LIF aprobada** | donde ambas existan |

La **LIF aprobada** está en el portal, en la tabla del punto de entrada, columna
LIF. Descárgala para los años que hagan falta, bajo la regla de no bloqueo. Los
valores 1.55 y 1.59 se conservan **marcados como híbridos** y fuera de ambas
series, hasta que la LIF permita recalcularlos.

**4.2 Pasivo pensionario — la serie se rehace antes de citarse · CORREGIDO**

El 43.6 estaba mal atribuido: es **CGPE 2023, p. 104–105, saldo al cierre de
2021** (ISSSTE con dato de 2020), no CGPE 2024.

Eso obliga a algo más que corregir la fuente. Si 52.1 venía del CGPE 2022 en
pesos de 2020 y 43.6 del CGPE 2023 al cierre de 2021, **la caída de 8.5 puntos
puede ser un artefacto**: no sabemos si cambió el saldo, la fecha de referencia o
la añada de pesos. Es el error de objeto que perseguimos, cometido por nosotros
en nuestra propia serie.

**Rehaz la serie con tres campos por observación:** documento CGPE de origen,
**fecha del saldo**, y **pesos de qué año**. Hasta que esté así, no se cita ni se
usa. Sigue congelada para calibración.

**4.3 Las demás**

| Serie | Estado |
|---|---|
| Supuesto oficial de crecimiento real de pensiones | 7.0 % (2021), 4.2 % (2022), 4.2 % (2023) — **congelada** |
| Tributarios / gastos obligatorios | 0.671 (2021), 0.674 (2022) |
| Costo financiero / tributarios | 0.20 (2022), 0.23 (2023) |
| SHRFSPF / tributarios, en años | 3.6 (2022), 3.4 (2023) |
| Pensiones + costo financiero / tributarios | 0.60 (2023) |

---

## 5. Secuencia de la corrida

### Fase 0 — Lectura local. Sin red.

`_aprendizaje/` completo (especificación del género, mapa de fuentes, rúbrica),
los artefactos de `_evaluacion/2023/`, y el inventario de lo que hay en
`2024/`. Con esto ya se puede trabajar.

### Fase 1 — Adquisición acotada, no bloqueante

Bajo la regla de §0: dos intentos por pieza, registrar, continuar.

Prioridad, en orden:
1. Analíticos del **PEF aprobado** GF 2023 y 2024 (§2.2).
2. **LIF aprobada** de los años necesarios para §4.1.
3. Analíticos de entidades, si el capítulo los pide.

Prepara el bundle de certificados antes de descargar —hoja firmada por el
intermedio YR1, el servidor envía R10— como se hizo el 2026-09-05. **No
desactives la verificación TLS.**

Lo que no llegue va a la sección cero y la corrida sigue.

### Fase 2 — Inventario y diffs, con lo que haya

**Inventario estándar** (marco macro, ingresos, gasto por ramo, tres flujos, tres
acervos) más un **apartado de educación que declare dónde vive cada peso**:

- **Ramo 11 (SEP)** y sus programas.
- **Ramo 33: FONE** —la partida dominante— y **FAETA**; FAM en su componente de
  infraestructura educativa.
- **Ramo 25**, previsiones y aportaciones para educación básica, normal,
  tecnológica y de adultos.
- **Educación superior:** subsidios a universidades públicas estatales, UNAM,
  IPN, UAM y centros públicos de investigación, con su ramo de origen.
- **Becas** Benito Juárez en sus vertientes, con su ramo, que no es
  necesariamente el 11.
- **Por función:** función Educación en el analítico ramo × función, contra la
  suma por ramos. **No dan lo mismo, y la diferencia es el hallazgo.**

**Diffs previos a escribir:** códigos de programa presupuestario, unidad
responsable y subfunción 2023 → 2024; Anexo 3 del decreto; anexos transversales
de educación. Se anticipan, no se descubren.

**Reconciliaciones:** ILIF ↔ CGPE en ingresos (la partida de ≈57 mdp que no
reconcilia, presumiblemente ISR de contratistas y asignatarios: ¿reaparece?);
suma por ramos ↔ suma por función en educación; flujo contra acervo.

### Fase 3 — Capítulo propio de EDUCACIÓN, a ciegas

**Antes de leer el capítulo de educación de CIEP.** Registra hora de cierre y
hora de primera lectura.

Plantilla: **POLÍTICA EDUCATIVA 2024 / EVOLUCIÓN DEL GASTO EN EDUCACIÓN /
PROGRAMAS SELECCIONADOS / IMPLICACIONES.**

**Declaraciones de apertura:** perímetro (ramo o función; federal o federalizado;
nivel educativo; becas dentro o fuera), añada de PIB, ex ante o ex post,
deflactor y su fuente. Líneas por separado antes de cualquier suma etiquetada.

**Obligaciones específicas:**

*Cuadro de unidad responsable.* Pendiente desde 2021, cuando estaban las columnas
y no se usaron. En educación es donde más informa: la reasignación entre UR es el
mecanismo habitual de cambiar política sin cambiar el agregado.

*Distribución territorial del FONE.* Se distribuye por entidad con fórmula.
Preséntala, y si la fórmula cambió, dilo. Sin corte territorial el capítulo no
dice nada sobre incidencia.

*Población implícita.* Toda cifra per cápita declara su denominador. En 2023 los
capítulos 3 y 9 usaban 131.2 millones de forma consistente. Para educación
distingue **población total, población en edad escolar y matrícula**: tres
denominadores, tres lecturas.

*Conexión demográfica.* Educación es el rubro donde la transición opera a la
baja: la población en edad escolar se contrae mientras la de edad avanzada crece.
Si el paquete proyecta gasto educativo, verifica si declara el supuesto de
matrícula. **Si no lo declara, ese es el hallazgo de horizonte del capítulo.**

**Comparación estructural.** Propón la canónica de educación con el estándar de
las cuatro adoptadas. Candidata a evaluar, no a asumir: **gasto en educación
sobre pensiones contributivas**, que compara las dos transferencias públicas de
extremos opuestos del ciclo de vida con el mismo perímetro presupuestario.
Justifica la elegida y descarta las demás por escrito.

### Fase 4 — Verificación

CSV con la estructura de 2023, más la marca de fuente aprobada donde aplique y la
excepción de esquema de §2.8.

**Procedimiento, en este orden:**
1. Analíticos aprobados y decreto (Anexos 1, 8, 20–22): resuelven cerca del 60 %
   de las filas de gasto en una hora.
2. **Calcula el deflactor implícito del documento desde sus propios cuadros
   antes** de contrastar cualquier variación.
3. **Valida la base t−1 por identidad antes de declararla ausente.** En 2023 eso
   rescató doce filas.
4. **Verifica cada lámina contra su cuadro y contra el texto antes** de verificar
   el texto contra la fuente. En 2023, 24 de 39 discrepancias fueron
   contradicciones internas del documento.

Verificación del frente (resumen e introducción) como objeto propio, con filas
propias.

**5.5 Cuadro 7.3 y las Cuentas Públicas · CONFIRMADO.** **No se descargan.**

Pero el hueco no es solo hueco: un cuadro que coloca seis columnas de ejercido
junto a dos de proyecto **sin declarar el empalme** es un hallazgo de criterio 2,
y para verlo no hace falta bajar nada. Repórtalo como tal. El hueco de cifras se
declara en la sección cero como condicionante.

### Fase 5 — Evaluación de calidad

Orden para un rubro federalizado:

1. **Perímetro.** Ramo contra función, federal contra federalizado, becas dentro
   o fuera. Prueba de divulgación de §2.5 para separarlo de `objeto`.
2. **Contrafactual declarado**, con las dos tasas de §2.1.
3. **Consistencia interna del documento.** Lámina contra cuadro contra texto.
   Sube de rango: en 2023 fue la fuente principal de discrepancias.
4. **Cobertura.** Contra el inventario, incluidos FONE, FAETA, becas y
   transversales. Agota rutas antes de declarar ausencias.
5. **Trato de los supuestos macro** y del supuesto de matrícula.
6. **Separación descriptivo–normativo** y **horizonte.**

### Fase 6 — Comparación

`_evaluacion/2024/04_comparacion_educacion.md`, con sección cero. Cuatro
apartados de siempre. El de "lo que CIEP tiene y tú no" es el que mide si la
corrida sirvió.

### Fase 7 — Tareas de red, al final

Ninguna es precondición de nada. Si fallan, se registran y ya.

**7.1 Resonda del árbol PPEF** para 2024:
`/work/models/PPEF2024/docs/exposicion/EM_Documento_Completo.pdf`, la subpágina
`/es/PPEF2024/exposicion_de_motivos`, y `/es/PPEF2024/analiticos_presupuestarios`.
El 2026-09-05 todo el rango 2022–2026 devolvía 404 mientras 2021 respondía, lo
que sugiere caída o reubicación, no ausencia. **Si el árbol volvió, dilo primero
en la bitácora:** se recuperan cinco exposiciones de motivos y cambia el alcance
de esta corrida y de las que faltan. Si sigue caído, prueba Transparencia
Presupuestaria y registra en `mapa_fuentes.md`.

**7.2 Contenido de la ILIF única.** El portal no ofrece exposición de motivos de
la ILIF como pieza separada en ningún ejercicio. **Abre el PDF de la ILIF 2024 y
determina si la contiene.** Lleva cinco corridas sin resolverse. Registra en
`mapa_fuentes.md`.

### Fase 8 — Tareas de corpus y aprendizaje

**8.1** Remarcado retroactivo de las veinte filas de 2023 (§2.10), con la nota de
*ex post* en la bitácora.

**8.2** Las series de §4, con las dos series de IMSS separadas y el pasivo
pensionario rehecho con sus tres campos.

**8.3 Cota de indexación.** Registra cuánto de las adecuaciones de registro es
inflación pagada. Con el paquete no se identifica y el interés real de 2022 queda
en un rango de un punto. **Anota qué serie haría falta** (Udibonos y Bondes) y
detente: cerrar el rango corresponde a Layer A.

**8.4 Artefactos.**

`especificacion_genero.md` — completa la caracterización comparada con el cuarto
patrón de error. La serie va: ingresos falla por base, gasto por perímetro, deuda
por nombre. Di qué patrón muestra un rubro federalizado. Añade la **tríada de
NTA** como conjunto: qué comparten pensiones, salud y educación y en qué
difieren.

`mapa_fuentes.md` — dónde vive cada peso de educación, por ramo y por función;
rutas de analíticos aprobados y de la LIF aprobada; resultado de las sondas;
contenido de la ILIF única; el certificado TLS.

`rubrica.md` — ocho entradas: prueba de divulgación; dos tasas del criterio 2;
convención de deflactor con la prohibición de derivarlo de cifras redondeadas;
**la excepción de esquema de §2.8**; retiro del marco de manual con su razón;
consistencia interna como criterio de rango alto; marca de fuente aprobada; y la
regla de series internamente consistentes de §4.1.

---

## 6. Bitácora

Además de lo habitual: **qué piezas no llegaron y con qué respuesta del
servidor**, primero de todo; horas de cierre del capítulo propio y de primera
lectura de CIEP; resultado de la resonda; las series; conteos por `tipo_error`,
`tier_seccion` y las dos tasas de contrafactual, comparados con la serie
2020–2023 (38/22, 54/18, 65 sobre verificable, 37/26/37 en deuda); la nota de
remarcado ex post; la cota de indexación; y qué cambiar para 2025.

**Nota sobre 2025:** el paquete 2025 se entregó el **15 de noviembre de 2024**
por cambio de administración, no el 8 de septiembre. Es el único de la serie con
esa fecha; tenlo presente al construir cualquier cronología.

---

## 7. Límites

- **Ninguna descarga bloquea la corrida** (§0).
- No califiques globalmente el documento de CIEP ni su solvencia analítica.
- No atribuyas a CIEP una discrepancia que explique una reasignación de la
  Cámara.
- No presentes el marco de manual fuera de la bitácora.
- No mezcles bases en una serie: ex ante con ex ante, aprobado con aprobado.
- No uses el pasivo pensionario ni el supuesto de pensiones en calibración.
- No resuelvas definiciones por criterio propio: se adjudican contra la nota
  metodológica de la SHCP.
- No derives deflactores de agregados redondeados.
- Donde no puedas verificar, dilo, y dilo en la sección cero.
