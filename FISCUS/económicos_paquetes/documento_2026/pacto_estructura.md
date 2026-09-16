# Pacto de estructura — documento propio ITED, Paquete Económico 2026

**Proyecto:** FISCUS · **Máquina:** Dalila · **Instrucción:** `INSTRUCCIONES_documento_propio_2026_v2.md`
**Producto:** documento completo del género, autoría ITED, en Markdown, LaTeX y PDF compilado en Dalila.
**Naturaleza de la corrida:** ensayo general del protocolo de lectura en vivo para 2027.

> ## SELLADO
>
> **Hora de sellado: 2026-09-07, 09:10:27 CST.**
> **Arranque del reloj (§5 de la instrucción): 2026-09-07, 09:03:57 CST.** T+0 es esa hora.
>
> Escrito en fase 0, **sin red**, **sin abrir ninguna pieza del paquete 2026** y con el
> documento del género sobre 2026 **en cuarentena física** desde las 09:05 CST
> (`_cuarentena_2026/`, ver §9).
>
> Fuentes usadas para escribirlo: `_aprendizaje/` completo —especificación del género
> con sus seis adendas, rúbrica con sus seis adendas, mapa de fuentes con sus cinco
> adendas, protocolo de lectura en vivo— y el listado de archivos de las carpetas
> `2018/` a `2026/`, leído sin abrir ningún documento.
>
> El detalle de granularidad queda pendiente de la fase 1 (§3 de la instrucción) y se
> resuelve en §6 de este pacto, que ya trae las dos rutas escritas.
>
> Todo cambio posterior se registra en §10 con su motivo y su hora.

---

## 1. Qué documento es este y qué no es

Es un documento del género *Implicaciones del Paquete Económico*, escrito por ITED sobre
el Paquete Económico 2026, **bajo régimen de simulación en vivo**: se escribe como si
solo existiera lo que se publicó el día de la entrega del paquete.

**No es una evaluación de CIEP.** Su documento sobre 2026 está en cuarentena hasta la
fase 7. Ninguna cifra suya entra al documento; si en la fase 7 resultara que alguna
afirmación propia se sostiene solo porque ellos la dijeron antes, eso se reporta como
contaminación, no se corrige en silencio.

**No es anónimo.** Portada, autoría, fecha y filiación ITED.

**No es la corrida de 2025 con otro año.** Tres diferencias deliberadas, y las tres son
lo que se está ensayando:

1. **Régimen restringido.** 2025 usó LIF aprobada, PEF aprobado y analíticos aprobados.
   Aquí no se usa nada aprobado del ejercicio 2026. El criterio es binario.
2. **Capa demográfica declarada.** 2025 se negó a calcular per cápita porque los
   denominadores no estaban en el paquete. Fue error de archivo, no disciplina. Aquí hay
   segunda capa con `tier = externa_demografica`.
3. **Capa de presentación.** Lámina de apertura y ficha metodológica por capítulo. En
   2025 el criterio de reconocimiento de género se cumplió a medias y fue ahí donde el
   documento perdió.

**Dónde se aparta del género, deliberadamente.** Se conservan las cuatro de 2025 —nota de
método al frente, descomposición de cuatro variables en deuda, capítulo de horizonte
demográfico, y declaración de nominal o real en toda diferencia en mdp— y se añaden dos:

5. **Dos líneas de comparación etiquetadas** (§3). El género usa solo la del género.
6. **Registro de lo no verificable en vivo**, escrito en el documento y no solo en la
   bitácora. Es el producto que sobrevive a la corrida.

---

## 2. Inventario de carpeta al sellar, y lo que ya se sabe que falta

Leído del sistema de archivos, sin abrir ningún documento.

**Permitido y presente para el ejercicio 2026** (`2026/`, tres piezas):
`2026_cgpe_criterios-generales.pdf` (3.9 MB), `2026_ilif_iniciativa.pdf` (1.3 MB, contiene
su propia exposición de motivos), `2026_ppef_proyecto-decreto.pdf` (6.9 MB).

**Prohibido y correctamente ausente:** LIF aprobada 2026, PEF aprobado 2026 y sus
analíticos, Cuenta Pública 2025, informes trimestrales posteriores a la entrega.

**Prohibido, presente y puesto en cuarentena:** `ciep_implicaciones2026.pdf`, movido a
`_cuarentena_2026/` a las 09:05 CST.

**Base de comparación disponible:**

| pieza | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|
| CGPE | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| ILIF | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| PPEF decreto | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| PPEF exposición de motivos | ✓ | ✓ | ✓ | ✓ | — | — | — | — |
| **PPEF analíticos (proyecto)** | — | — | ✓ | ✓ | **—** | **—** | **—** | **—** |
| LIF aprobada | — | — | — | — | ✓ | ✓ | ✓ | ✓ |
| PEF analíticos (aprobado) | — | — | ✓ | — | parcial | ✓ | ✓ | ✓ |

### 2.1 El hallazgo estructural de la fase 0, sellado — **REFUTADO POR LA FASE 1**

> **2026-09-07, 10:00 CST.** Lo que sigue se escribió a las 09:10 y **es falso**. La fase 1
> encontró los analíticos del **proyecto** para 2021–2026 en `pef.hacienda.gob.mx`, bajo
> `Analiticos_Historico/{t}/Proyecto/`, una ruta que este proyecto nunca había sondeado
> porque siempre buscó el proyecto en `ppef.hacienda.gob.mx`. **No hay techo de granularidad
> en la línea primaria.** Ver §6.5 y `_aprendizaje/mapa_fuentes.md`, adenda 2026-09-07.
>
> **El texto original se conserva porque una predicción sellada solo sirve si se puede
> comparar con lo que pasó, y porque el error importa: durante cuatro ejercicios este
> proyecto dio por ausente un archivo que estaba publicado.**


**La línea primaria de comparación —proyecto 2026 contra proyecto 2025— tiene un techo de
granularidad que ninguna ruta de la fase 1 puede levantar.**

Los analíticos del **proyecto** no existen en carpeta para 2022–2025 y llevan 404 en el
servidor desde 2022 (verificado el 2026-09-05 y el 2026-09-06; `mapa_fuentes.md`). Por
tanto, aunque la fase 1 consiga los analíticos del proyecto 2026 (Ruta A), **no habrá
contraparte de proyecto para 2025.** La línea primaria queda acotada, de forma permanente,
a lo que publica el proyecto de decreto: ramo (Anexo 1), gastos obligatorios (Anexo 3),
anexos transversales (Anexos 10–19), gasto corriente estructural (Anexo 2), y lo que el
CGPE y la ILIF traigan por agregado.

Consecuencia que hay que decir ahora y no descubrir en la fase 3: **la comparación por
programa y por unidad responsable solo es posible contra el aprobado 2025, es decir, en la
línea segunda, y por tanto mezcla ex ante con ex post de la Cámara.** Donde se use, se
etiqueta como tal y se recuerda que parte de la diferencia es lo que la Cámara cambió.

**Regla de operación que esta corrida entrega al protocolo 2027, descubierta antes de
descargar nada:** *los analíticos del proyecto se descargan y se archivan el día de la
entrega, todos los años, se vayan a usar o no.* El almacén del portal los retira. Un
archivo que no se guardó ese día no se recupera después, y su ausencia no se paga ese año
sino al año siguiente, cuando se convierte en la base de comparación que falta.

---

## 3. Las dos líneas de comparación

Se declaran las dos, aparecen las dos donde la cifra importa, y **nunca conviven en un
cuadro sin etiqueta**.

| línea | contenido | fuentes | granularidad máxima |
|---|---|---|---|
| **P — primaria, de la casa** | proyecto 2026 contra proyecto 2025 | ILIF 2026/2025; PPEF decreto 2026/2025; CGPE 2026/2025; **analíticos del proyecto 2026 y 2025** | **programa, unidad responsable, partida específica y entidad federativa** |
| **G — segunda, del género** | proyecto 2026 contra aprobado 2025 | mismas para 2026; LIF 2025 aprobada y analíticos del PEF 2025 para la base | programa y unidad responsable |

**Actualizado el 2026-09-07 a las 10:00 CST tras la fase 1.** Las dos líneas quedan a la
misma granularidad y la primaria deja de estar en desventaja. Sigue siendo obligatorio
etiquetarlas: la fase 0.5 mostró que la misma función educativa da **+0.81 % en la línea P,
+0.70 % aprobado contra aprobado y −0.47 % en la línea G**, y ninguna de las tres es falsa.

**Etiqueta obligatoria.** Toda columna de comparación lleva `P` o `G` en el encabezado del
cuadro y la letra se repite en el texto que la cita. Un cuadro sin etiqueta es un error de
la misma familia que un perímetro sin declarar.

**Donde P y G difieran de forma material, la diferencia es un hallazgo**, no un problema:
mide lo que la Cámara cambió en diciembre de 2024. Se reporta en el capítulo donde ocurre,
con su magnitud y su signo, y se recoge en el capítulo 4.

**Precedente que obliga a esperar diferencias grandes:** en el ejercicio 2025 la Cámara
aumentó el gasto educativo en 18,674.8 mdp entre proyecto y aprobado, lo bastante para
cambiar el signo del capítulo, de −1.2 % real a +0.4 %. La línea G de educación en este
documento arrastra ese movimiento por construcción.

---

## 4. Índice de capítulos

Catorce capítulos más frente y cierre, en el orden que fija la instrucción §4.1.

| # | capítulo | parte | nuevo en 2026 |
|---|---|---|---|
| — | Portada, autoría y **nota de método** | frente | — |
| — | Resumen ejecutivo | frente | — |
| 1 | Marco macroeconómico | frente | — |
| 2 | Ingresos presupuestarios | **(+) Ingresos** | — |
| 3 | Ingresos energéticos y empresas públicas | (+) Ingresos | ampliado |
| 4 | Gasto público: los agregados | **(−) Gasto** | — |
| 5 | Salud | (−) Gasto | — |
| 6 | Educación | (−) Gasto | — |
| 7 | Pensiones | (−) Gasto | — |
| 8 | Inversión | (−) Gasto | — |
| 9 | Seguridad | (−) Gasto | — |
| 10 | Gasto federalizado | (−) Gasto | — |
| 11 | **Medio ambiente y agua** | (−) Gasto | **sí** |
| 12 | **Anexos transversales** | (−) Gasto | **sí** |
| 13 | Balance, deuda y sostenibilidad | **(=) Balance y deuda** | — |
| 14 | Horizonte demográfico | cierre | metodológico |
| — | Implicaciones de política pública | cierre | — |
| — | Registro del documento: lo no verificable en vivo | cierre | **sí** |
| — | Anexo metodológico, acrónimos, bibliografía | cierre | — |

**Extensión objetivo:** 75 a 95 páginas. Capítulos de rubro de 4 a 7 páginas; el 4 y el 13,
de 8 a 10; el 11 y el 12, de 3 a 5 en su primera edición.

**Orden de partes:** (+), (−), (=), como en 2020, 2022, 2024 y 2025. No el de 2021.

### 4.1 Dos decisiones de colocación, tomadas ahora

**El capítulo 3 es un capítulo de ingresos, no de gasto.** «Empresas públicas» entra por su
relación fiscal con el Estado —derecho por la utilidad compartida, Fondo Mexicano del
Petróleo, aportación patrimonial, dividendo, meta de balance— que es un objeto de la Parte
I. El **gasto** de Pemex y CFE vive en el capítulo 4 (agregados, clasificación económica) y
en el 8 (inversión). Se declara en la apertura del capítulo 3 para que el lector no busque
ahí el presupuesto de las empresas.

**El capítulo 12 trata los anexos transversales como objeto presupuestal, no como ensayo de
política social.** Cuatro preguntas y solo cuatro: qué anexos existen, cuánto concentran,
qué proporción del etiquetado para igualdad es en realidad pensiones, y qué programas se
repiten entre anexos. Incidencia social sin fuente: no.

### 4.2 Los dos capítulos nuevos y por qué están

Cierran el hueco que abrió la comparación anónima de 2025: medio ambiente y agua obtuvo
4.5 y género y cuidados 4.0. Para un lector habitual del género, su ausencia no se lee como
decisión de alcance sino como fallo de reconocimiento. Cuatro de las seis omisiones de esa
comparación no eran carencias de fuente sino capítulos que no se escribieron.

---

## 5. Qué pregunta responde cada capítulo

Cada capítulo responde estas preguntas y solo estas. Si una no se puede responder con
fuente **bajo el régimen en vivo**, se dice en el capítulo y se anota en el registro.

**1. Marco macroeconómico.** ¿Qué supone la SHCP para 2026 en crecimiento, inflación, tasa,
tipo de cambio y petróleo? ¿Cómo se compara con el potencial declarado? ¿Qué sensibilidades
publica el paquete y a qué son sensibles las cifras del resto del documento? ¿Cuál es el
PIB nominal, de qué año base, y qué se reexpresó respecto del CGPE 2025?

**2. Ingresos presupuestarios.** ¿Cuánto se propone recaudar, por renglón del artículo 1o.?
¿Contra qué base cambia y en cuánto real, en la línea P y en la G? ¿Hubo miscelánea fiscal
y qué cifra tiene? ¿Qué elasticidad implícita hay entre el crecimiento supuesto y la
recaudación proyectada? ¿Cuántos pesos de cada cien se financian con deuda?

**3. Ingresos energéticos y empresas públicas.** ¿Cuánto aporta el sector energético y por
qué vía? ¿Qué suponen precio, plataforma y tipo de cambio? ¿Cuál es la tasa del derecho por
la utilidad compartida y cómo llegó ahí? ¿Cuánto transfiere el Fondo Mexicano del Petróleo
y cuánto es ingreso propio? ¿Qué metas de balance fija el decreto a Pemex y CFE?

**4. Gasto público: los agregados.** ¿Cuánto se propone gastar, por las clasificaciones que
el proyecto permita? ¿Qué ramos ganan y pierden en términos reales, en P y en G? ¿Qué parte
está comprometida, bajo qué definición y contra qué anexo? ¿Qué reclasificaciones hay entre
2025 y 2026 y qué caídas contables producen que no son presupuestales? ¿Dónde difieren P y
G de forma material y qué mide esa diferencia?

**5. Salud.** ¿Cuánto se destina, por subsistema, separando contributivo de no contributivo?
¿Qué pasó con IMSS-Bienestar? ¿Cuánto por afiliado en cada subsistema, con qué denominador
y de qué fuente? ¿Las cuotas cubren la salud del IMSS?

**6. Educación.** ¿Cuánto, por función y por ramo, separando federal de federalizado? ¿Cómo
se distribuye el FONE por entidad y cambió la fórmula? ¿Qué hacen las becas y dónde viven?
¿Declara el paquete un supuesto de matrícula? ¿Cuánto por alumno, y bajo cuál de los tres
denominadores?

**7. Pensiones.** ¿Cuánto cuestan y por institución? ¿Qué parte es contributiva y qué parte
no? ¿Cuánto aporta el Gobierno Federal al régimen en curso de pago? ¿Cuál es la relación
entre pensiones y cuotas del IMSS? ¿Qué horizonte declara el paquete? ¿Cuánto por persona
de 65 años y más?

**8. Inversión.** ¿Cuánta inversión física y cuánto gasto de inversión, que son cosas
distintas? ¿Qué proporción es obra pública directa y qué proporción es transferencia? ¿Qué
proyectos concentran el gasto? ¿Sigue habiendo obra civil ejecutada por las fuerzas armadas
y en qué dirección se mueve?

**9. Seguridad.** ¿Cuánto se destina al perímetro de quince subfunciones? ¿Cómo se reparte
entre civil y militar? ¿Qué obra pública no militar ejecutan las fuerzas armadas?

**10. Gasto federalizado.** ¿Cuánto se transfiere y por qué vía: participaciones,
aportaciones, convenios? ¿Cómo queda por entidad y por habitante? ¿Qué pasa con el fondo de
estabilización de los ingresos de las entidades federativas?

**11. Medio ambiente y agua.** ¿Cuánto se destina a la función de protección ambiental y
cómo se reparte entre sus subfunciones? ¿Cuánto va a agua potable, alcantarillado y
saneamiento, y en qué ramo vive? ¿Qué relación hay entre lo etiquetado en el anexo
transversal de cambio climático y lo que la clasificación funcional registra? ¿Cuánto por
habitante, y con qué denominador?

**12. Anexos transversales.** ¿Qué anexos existen en el proyecto de decreto y cuánto suma
cada uno? ¿Cuánto concentran en conjunto y qué fracción del gasto programable representan?
¿Qué proporción del anexo de igualdad entre mujeres y hombres es en realidad gasto
pensionario? ¿Qué programas se repiten entre anexos y cuánto vale el doble conteo?

**13. Balance, deuda y sostenibilidad.** ¿Cuáles son los tres flujos y los tres acervos, con
nombre correcto? ¿Qué techos autoriza la iniciativa de ingresos y en qué se distinguen del
déficit? ¿Cierra la identidad flujo–acervo? ¿Qué explica el cambio de la razón SHRFSPF/PIB,
repartido en cuatro variables? ¿Qué regla de excepción se invocó? ¿Cuánta deuda por
habitante?

**14. Horizonte demográfico.** ¿Dónde declara el paquete un supuesto demográfico y dónde no?
¿Cómo se ven los tres vértices de la tríada de NTA juntos? ¿Se repite el hallazgo
transversal —horizonte donde la demografía presiona al alza, ninguno donde presiona a la
baja— y qué habría significado tenerlo?

---

## 6. Granularidad: las dos rutas, escritas antes de saber cuál toca

> ## RUTA ADOPTADA: **A**
>
> **Resuelto el 2026-09-07 a las 09:47 CST (T+00:43).** Los analíticos del proyecto 2026
> existen, en los cuatro cortes, y también los de 2021 a 2025. Descargados 2024, 2025 y 2026.
> Además hay un CSV del proyecto en el repositorio de datos abiertos de la Secretaría, más
> rico que los xlsx. Detalle en §6.5 y en la bitácora §4.
>
> **Nada de §6.2 y §6.3 se ejecuta.** Se conservan escritos porque la predicción sellada es
> el instrumento con el que se mide qué habría costado la Ruta B, y porque la corrida 2027
> puede caer en ella.

La fase 1 resuelve si existen los analíticos del **proyecto** 2026. Las dos respuestas están
preparadas. **La ruta adoptada se anota en §10 con hora, y es un producto de la corrida por
sí misma:** dice si la corrida 2027 tendrá desagregación por programa desde el primer día.

### 6.1 Ruta A — hay analíticos del proyecto 2026

El documento trabaja a nivel de **programa presupuestario y unidad responsable**: perímetros
reproducibles por enumeración de claves, cuadro de UR por capítulo, distribución territorial
donde el fondo la tenga, y diff de claves **por clave, no por nombre**.

Límite que se mantiene aun bajo Ruta A: la comparación por programa y UR es contra el
**aprobado 2025** (línea G), porque no hay proyecto 2025 a ese nivel (§2.1).

### 6.2 Ruta B — no hay analíticos del proyecto 2026

El documento trabaja a nivel de **ramo y función**, con lo que traigan el proyecto de
decreto y sus anexos, y **declara en el propio texto qué no puede decir**: composición por
programa, reasignaciones entre unidades responsables, distribución territorial de fondos, y
separación entre caída de ramo y caída de función donde la fuente no la permita.

### 6.3 Qué se cae exactamente bajo Ruta B — predicción sellada

Se escribe ahora para que la caída no se lea después como conveniencia.

**Capítulos que sobreviven completos:** 1 macro, 2 ingresos, 3 energéticos, 4 agregados (a
nivel ramo y anexo), 12 anexos transversales, 13 deuda, 14 horizonte.

**Capítulos en riesgo de declararse no redactables:** 5 salud, 6 educación, 7 pensiones,
8 inversión, 9 seguridad, 10 federalizado, 11 medio ambiente y agua. Los siete dependen de
un corte por función, por programa o por unidad responsable que el proyecto de decreto no
publica.

**Rescate parcial previsto para tres de ellos, sin analíticos:**
- **7 Pensiones** — el agregado de la clasificación económica se obtiene del **Anexo 3 del
  decreto**, por diferencia entre gastos obligatorios con y sin pensiones. Eso da el nivel
  y su variación real en la línea P, y las pensiones no contributivas por programa siguen
  perdidas. Un capítulo corto pero redactable.
- **11 Medio ambiente y agua** — recuperable solo por su **anexo transversal de cambio
  climático**, que sí está en el decreto. Se declara que el anexo no es la función y que la
  cifra que se publica es la del anexo.
- **12 Anexos transversales** — no depende de analíticos en absoluto. Sobrevive intacto y
  pasa a ser el capítulo más fuerte de la Parte II. Ese es el motivo real por el que valía
  la pena añadirlo este año.

**Presupuesto de afirmaciones bajo Ruta B:** puede no alcanzarse en varios capítulos. Es un
resultado, no un fracaso. Se declara el capítulo no redactable y se sigue.

### 6.4 Qué se cae de las comparaciones estructurales bajo Ruta B

De las siete razones de §7, **cuatro sobreviven y tres se congelan en 2025**:

| razón | Ruta A | Ruta B | por qué |
|---|---|---|---|
| Tributarios / gastos obligatorios | ✓ | **✓** | ILIF art. 1o. + DEC Anexo 3 |
| Pensiones + costo financiero / tributarios | ✓ | **✓** | Anexo 3 + Anexo 1 (ramos 24/34) + ILIF |
| Costo financiero / tributarios | ✓ | **✓** | CGPE + DEC Anexo 8 + ILIF |
| SHRFSPF / tributarios, en años | ✓ | **✓** | CGPE + ILIF |
| Pensiones IMSS / cuotas IMSS | ✓ | **✗** | numerador exige analítico de entidades, TG 4 |
| Cuotas / gasto en salud del IMSS | ✓ | **✗** | numerador exige analítico de entidades por función |
| Educación / pensiones y jubilaciones | ✓ | **✗** | numerador exige analítico por función; el denominador sí está en el Anexo 3 |

Las tres que caen son exactamente las de la tríada de NTA. **Bajo Ruta B, el capítulo 14 se
escribe con las series detenidas en 2025 y con el hueco declarado**, que es en sí mismo el
hallazgo: sin analíticos del proyecto, la lectura en vivo no puede decir nada nuevo sobre
las tres transferencias de ciclo de vida.

---

### 6.5 Lo que la fase 1 encontró, y lo que hay que cambiar del pacto por eso

**Tres rutas nuevas, ninguna en el mapa de fuentes hasta hoy.**

1. **Analíticos del proyecto, 2021–2026, cuatro cortes:**
   `pef.hacienda.gob.mx/work/models/PEF/Analiticos_Historico/{t}/**Proyecto**/`. Veinticuatro
   peticiones, veinticuatro 200. Prueba de aceptación: el perímetro educativo de CIEP 2025
   reconstruido sobre el proyecto da **1,142,490.5** contra los **1,142,490.0** publicados.
2. **Repositorio de datos abiertos de la Secretaría (ATDT):** el proyecto completo en un CSV
   de 129,908 filas con **partida específica, clave de cartera y entidad federativa**, más
   un CSV de **anexos transversales desglosados por programa** (124 MB) y otro de plazas.
   **Ranura única sobrescrita:** los años anteriores devuelven 503.
3. **Gaceta Parlamentaria del día de la entrega** (8 de septiembre de 2025, número 6871):
   el paquete íntegro en anexos A a L, con URLs estables, incluida la miscelánea.

**Cambios al alcance que esto habilita, y que se adoptan:**

- **La línea P sube a programa y unidad responsable** (§3). El diff `C4.7` se hace por clave
  entre proyecto 2025 y proyecto 2026, que es la comparación limpia, y la versión contra el
  aprobado 2025 pasa a ser el cuadro secundario que mide a la Cámara.
- **Se descongela la serie ex ante de pensiones IMSS / cuotas IMSS** (§7), congelada desde
  2022 por falta de la exposición de motivos: se reconstruye del analítico de entidades del
  proyecto, tipo de gasto 4, para 2021–2026. Queda sujeta a que cierre contra el Anexo 3.
- **El capítulo 12 gana su fuente propia**: el CSV de anexos transversales trae el desglose
  por programa, que es lo que las preguntas de doble conteo y de composición del anexo de
  igualdad necesitan. Deja de depender de leer anexos del decreto en PDF.
- **El capítulo 11 recupera la función de protección ambiental** (finalidad 2, función 1) y
  el agua por programa. Sale de la lista de capítulos en riesgo.
- **Cuadro nuevo, `C8.3`: cartera de inversión por clave.** El CSV trae `id_clave_cartera`,
  que permite nombrar los proyectos que concentran la inversión sin recurrir al Tomo VIII.
- **Cuadro nuevo, `C2.6`: la miscelánea 2026 pieza por pieza.** Son tres leyes —Derechos,
  IEPS y Código Fiscal— y **no hay iniciativa de reforma al ISR ni al IVA**. Eso es una
  afirmación del capítulo de ingresos que sale del índice de la Gaceta.

**Reclasificación que hay que anticipar, detectada al abrir el CSV** (§11.3): **IMSS-Bienestar
es el Ramo 56 en 2026**, después de haber sido el 47 en 2025 y el 19 en 2024. Tercer cambio de
ubicación en tres ejercicios. Ninguna caída del Ramo 47 se escribe como recorte.

**Total bruto del proyecto 2026: 11,746,796.8 mdp** (Gobierno Federal más entidades, antes
del neteo). Queda por cerrar contra el Anexo 1 del decreto en la fase 2.

**Lo que la fase 1 NO consiguió**, y va al registro: matrícula por nivel educativo,
afiliación a IMSS e ISSSTE, y padrón de programas pensionarios. Sin ellos, `C5.2`, `C6.5` y
parte de `C14.3` no se publican. Se reintenta en la fase 2.

## 7. Comparaciones estructurales: cuál va en qué capítulo

Todas con perímetro declarado, base consistente y línea etiquetada. **Nunca una línea
híbrida:** ex ante con ex ante, aprobado con aprobado.

| cap. | comparación | serie conocida | estado |
|---|---|---|---|
| 2 | Tributarios / gastos obligatorios (con y sin cuotas IMSS) | 0.671 (2021), 0.674 (2022); con cuotas 0.743, 0.745 | extender 2023–2026 |
| 4 | Pensiones + costo financiero / tributarios | 0.60 (2023) **no reproducible** | **reconstruir antes de usar** |
| 7 | Pensiones IMSS / cuotas IMSS, serie aprobada | 1.545 (2022), 1.594 (2023), 1.627 (2024) | extender a 2025; 2026 solo bajo Ruta A |
| 7 | Pensiones IMSS / cuotas IMSS, serie ex ante | 1.31 (2020), 1.46 (2021) | **congelada** desde 2022 |
| 5 | Cuotas obrero-patronales / gasto en salud del IMSS | 0.85 (2021) | extender; 2026 solo bajo Ruta A |
| 5 | Pensiones IMSS+ISSSTE / salud IMSS+ISSSTE | 2.11 (2021) | extender; 2026 solo bajo Ruta A |
| 6 | Educación / pensiones y jubilaciones, clasif. económica | 0.709 (2023), 0.689 (2024) | extender; 2026 solo bajo Ruta A |
| 6 | segunda línea: educación / pensiones totales | 0.558 (2023), 0.518 (2024) | extender |
| 13 | Costo financiero / tributarios | 0.20 (2022), 0.23 (2023), 0.256 (2024) | extender 2025–2026 |
| 13 | SHRFSPF / tributarios, en años de ingreso | 3.6 (2022), 3.4 (2023), 3.40 (2024) | extender 2025–2026 |

**Advertencia sellada sobre la razón del capítulo 4, heredada de 2025 y todavía viva.** El
punto de 0.60 para 2023 no se reproduce con ninguna de las dos definiciones de pensiones:
con el perímetro amplio da 0.583 y con la clasificación económica 0.522. **Antes de extender
esa serie hay que reconstruir de dónde salió el 0.60.** Si no se reconstruye, la serie
arranca en 2024 con su definición declarada y el punto de 2023 se retira con nota. No se
publica una serie cuya base no cierra.

**Congeladas para calibración y no citables como trayectoria:** el pasivo pensionario y el
supuesto oficial de crecimiento real de pensiones. Se pueden mencionar con sus tres campos;
no se pueden encadenar.

---

## 8. Cuadros y figuras previstos, con el dato que cada uno necesita

Nomenclatura: `C` cuadro, `F` figura, `L` lámina de apertura de capítulo. Cada uno se genera
desde un `.csv` de `datos/` con su fila en `datos/_fuentes.csv`. **Ninguna cifra se teclea en
el cuerpo del texto; ninguna figura es una imagen pegada** salvo por la excepción de
robustez de §11.4.

Columna **ruta**: `AB` funciona con o sin analíticos del proyecto; `A` exige Ruta A; `B*`
tiene versión degradada bajo Ruta B, descrita en la celda. Columna **línea**: P, G o ambas.

### 8.0 La lámina y la ficha, que son estructura y no adorno

**Toda lámina `L{n}` tiene exactamente cuatro elementos**, y ninguno puede traer una cifra
que no tenga renglón en la ficha del mismo capítulo:

1. **Titular cuantitativo** con su signo, su magnitud, su base y su línea (P o G).
2. **Figura principal**, generada desde datos versionados.
3. **Párrafo «qué cambió»** — descriptivo, sin juicio.
4. **Párrafo «por qué importa»** — el juicio, señalado como tal.

**Toda ficha metodológica de cierre `M{n}` tiene ocho renglones:** perímetro (enumerable);
línea de comparación; deflactor y su fuente; año de los pesos; PIB y su añada; denominador
demográfico si el capítulo trae per cápita; fuentes con documento y página; y **qué no puede
afirmarse con ellas**. Catorce láminas y catorce fichas, una por capítulo.

### 8.1 Frente y capítulo 1

| id | contenido | dato que necesita | archivo | ruta | línea |
|---|---|---|---|---|---|
| C1.1 | Marco macro: 2025 aprobado, 2025 estimado, 2026, con las cinco variables | CGPE 2026, marco macro y finanzas públicas | `macro_marco.csv` | AB | P+G |
| C1.2 | Mediano plazo 2027–2031 | CGPE 2026, cuadros de proyección | `macro_medianoplazo.csv` | AB | — |
| C1.3 | Sensibilidades: 0.5 pp PIB, 1 dpb, 20 centavos, 50 mbd, 100 pb | CGPE 2026, cuadro de sensibilidades | `macro_sensibilidades.csv` | AB | — |
| C1.4 | **Reexpresión:** qué cambió en la serie entre CGPE 2025 y CGPE 2026, y con qué añada | CGPE 2026 y CGPE 2025 | `macro_reexpresion.csv` | AB | P |
| F1.1 | Crecimiento supuesto contra potencial declarado, 2019–2026 | C1.1 más los CGPE 2019–2025 en carpeta | `macro_crecimiento.csv` | AB | — |

### 8.2 Parte I — capítulos 2 y 3

| id | contenido | dato que necesita | archivo | ruta | línea |
|---|---|---|---|---|---|
| C2.1 | Ingresos por renglón del art. 1o.: **ILIF 2025, LIF 2025 aprobada, ILIF 2026**, % PIB, variación real nominal y real | ILIF 2026; ILIF 2025; LIF 2025; PIB de C1.1 | `ingresos_art1o.csv` | AB | **P y G en columnas separadas** |
| C2.2 | Reconciliación ILIF ↔ CGPE por renglón, con el residuo nombrado | ILIF 2026 art. 1o.; CGPE 2026 | `ingresos_reconciliacion.csv` | AB | — |
| C2.3 | Medidas de ingreso con cifra, y lista de las que no la tienen | ILIF 2026 exposición; miscelánea si la hay | `ingresos_medidas.csv` | AB | — |
| C2.4 | Elasticidad implícita: crecimiento supuesto contra variación real de tributarios, contra las dos bases | C1.1 y C2.1 | derivado de los anteriores | AB | P+G |
| F2.1 | Ingresos presupuestarios en % del PIB, serie | CGPE 2026, anexo de series | `ingresos_serie.csv` | AB | — |
| F2.2 | Composición: tributarios, petroleros, no tributarios, organismos | C2.1 | reusa `ingresos_art1o.csv` | AB | — |
| C2.5 | **Diferencia P − G por renglón** de ingresos: qué movió la Cámara en diciembre de 2024 | ILIF 2025 contra LIF 2025 | `ingresos_camara.csv` | AB | — |
| C3.1 | Ingresos energéticos por vía: FMP, ingreso propio de Pemex, de CFE, ISR de contratistas | ILIF 2026 art. 1o.; CGPE 2026 | `energia_ingresos.csv` | AB | P+G |
| C3.2 | Precio, plataforma y tipo de cambio supuestos, contra 2025 | C1.1 | reusa `macro_marco.csv` | AB | P |
| C3.3 | Metas de balance y aportación patrimonial de Pemex y CFE | DEC 2026 artículos de metas; DEC 2025 | `epe_metas.csv` | AB | P |
| — | Trayectoria del derecho por la utilidad compartida | CGPE 2026; ILIF art. 22; DOF para las reformas | `derecho_utilidad.csv` | AB | — |

### 8.3 Parte II — capítulo 4 y rubros

| id | contenido | dato que necesita | archivo | ruta | línea |
|---|---|---|---|---|---|
| C4.1 | Gasto neto, programable, no programable, costo financiero, participaciones | CGPE 2026; DEC 2026 art. 2 | `gasto_agregados.csv` | AB | P+G |
| C4.2 | **Por ramo:** PPEF 2025, PEF 2025 aprobado, PPEF 2026, diferencias nominal y real | DEC 2026 Anexo 1; DEC 2025 Anexo 1; PEF 2025 Anexo 1 | `gasto_ramos.csv` | AB | **P y G** |
| C4.3 | Clasificación económica: corriente, pensiones, inversión, capítulos de gasto | analíticos 2026 y contraparte | `gasto_economica.csv` | **A** · B*: solo el desglose que traiga el decreto | G |
| C4.4 | Clasificación funcional por finalidad y función | analíticos por función | `gasto_funcional.csv` | **A** · B*: se declara ausente | G |
| C4.5 | Gastos obligatorios con y sin pensiones | DEC 2026 Anexo 3; DEC 2025 Anexo 3 | `gasto_obligatorios.csv` | AB | **P** |
| C4.6 | Gasto corriente estructural contra su límite máximo | DEC Anexo 2; fórmula del CGPE (ya extraída en 2025) | `gce_limite.csv` | AB | P |
| C4.7 | **Diffs 2025 → 2026 por clave:** ramos, programas, UR y subfunciones que aparecen, desaparecen o se renumeran | analíticos de los dos años | `diffs_2025_2026.csv` | **A** · B*: solo ramos, desde el Anexo 1 | G (A) / P (B*) |
| C4.8 | **Dónde difieren P y G de forma material**, por ramo, con signo y magnitud | C4.2 | derivado | AB | — |
| F4.1 | Gasto neto y programable en % del PIB, serie | CGPE 2026 anexo de series | `gasto_serie.csv` | AB | — |
| C5.1 | Salud por subsistema, dos bloques etiquetados | analíticos por función Salud, GF y entidades | `salud_subsistema.csv` | **A** · B*: capítulo no redactable | G |
| C5.2 | **Gasto por afiliado** por subsistema, con denominador declarado | C5.1 + afiliación IMSS, ISSSTE y población sin seguridad social | `salud_percapita.csv` | **A** | G |
| F5.1 | Cuotas obrero-patronales contra gasto en salud del IMSS, serie | LIF/ILIF y analíticos de entidades | `ratio_cuotas_salud.csv` | **A** hasta 2026; serie hasta 2025 en AB | G |
| C6.1 | Función Educación por ramo, federal contra federalizado | analítico por función | `educacion_ramo.csv` | **A** · B*: no redactable | G |
| C6.2 | Por subfunción, los seis niveles | mismo analítico | `educacion_subfuncion.csv` | **A** | G |
| C6.3 | FONE por entidad, participación y variación real | analítico GF columna EF; DEC Anexo del FONE | `fone_entidad.csv` | **A** · B*: solo el anexo del decreto, sin cruce | G / P |
| C6.4 | Becas por programa y por ramo | analítico por programa | `becas.csv` | **A** | G |
| C6.5 | **Gasto por alumno bajo los tres denominadores:** población total, población en edad escolar, matrícula | C6.1 + estadística educativa oficial + CONAPO | `educacion_percapita.csv` | **A** | G |
| C7.1 | Pensiones por institución y por tipo de gasto 4 | analíticos GF y entidades | `pensiones_institucion.csv` | **A** | G |
| C7.2 | **Agregado de pensiones por diferencia del Anexo 3**, con su variación real | DEC 2026 y 2025 Anexo 3 | `pensiones_anexo3.csv` | **AB** | **P** |
| C7.3 | Contributivas contra no contributivas, con los programas nombrados por clave | analíticos por programa; DEC anexo de programas | `pensiones_contrib.csv` | **A** | G |
| C7.4 | Aportación del GF al régimen en curso de pago, serie desde 2020 | DEC artículo correspondiente, 2020–2026 | `pensiones_aportacion.csv` | AB | P |
| C7.5 | **Pensión por persona de 65 años y más** | C7.2 + CONAPO 65+ | `pensiones_percapita.csv` | AB | P |
| F7.1 | Pensiones IMSS / cuotas IMSS, serie aprobada | `pensiones_institucion.csv` y LIF | `ratio_pensiones_cuotas.csv` | **A** hasta 2026 | G |
| C8.1 | Inversión física contra gasto de inversión, con la diferencia explicada | CGPE 2026; analíticos capítulos 6000 y 7000 | `inversion_agregados.csv` | **A** · B*: solo el agregado del CGPE | G / P |
| C8.2 | Obra pública directa por ramo | analíticos, capítulo 6000 | `inversion_ramo.csv` | **A** | G |
| C9.1 | Perímetro de seguridad: quince subfunciones de cinco funciones | analítico por función | `seguridad_subfuncion.csv` | **A** · B*: no redactable | G |
| C9.2 | Civil contra militar, y obra pública no militar de las fuerzas armadas | analíticos por ramo, UR y capítulo 6000 | `seguridad_civil_militar.csv` | **A** | G |
| C10.1 | Gasto federalizado por vía: participaciones, aportaciones, convenios | CGPE 2026; DEC Anexos 1 y del ramo 33 | `federalizado_via.csv` | AB | P+G |
| C10.2 | **Por entidad y por habitante**, con población declarada | analíticos columna EF; CONAPO por entidad | `federalizado_entidad.csv` | **A** · B*: solo lo que el decreto reparta | G / P |
| C11.1 | Función de protección ambiental por subfunción | analítico por función | `ambiente_subfuncion.csv` | **A** · B*: se declara ausente | G |
| C11.2 | Agua potable, alcantarillado y saneamiento: ramo, programa y monto | analítico por programa; DEC Anexo 1 | `agua.csv` | **A** · B*: solo lo del decreto | G / P |
| C11.3 | **Anexo transversal de cambio climático contra la función**, y por qué no coinciden | DEC 2026 anexo; C11.1 | `ambiente_anexo_vs_funcion.csv` | **A** · B*: solo el anexo, declarando que no es la función | P |
| C11.4 | Gasto ambiental por habitante | C11.1 o C11.3 + CONAPO | `ambiente_percapita.csv` | AB | P |
| C12.1 | **Todos los anexos transversales del decreto: nombre, monto, % del programable**, 2025 y 2026 | DEC 2026 y 2025, Anexos 10–19 | `transversales.csv` | **AB** | **P** |
| C12.2 | **Qué fracción del anexo de igualdad es gasto pensionario** | C12.1 + el desglose del propio anexo | `transversal_igualdad.csv` | AB | P |
| C12.3 | **Programas que se repiten entre anexos, y el doble conteo que producen** | desglose por programa de cada anexo del decreto | `transversales_traslape.csv` | AB | P |
| F12.1 | Concentración: los anexos ordenados por monto, con su acumulado | C12.1 | reusa `transversales.csv` | AB | — |

### 8.4 Parte III — capítulo 13

| id | contenido | dato que necesita | archivo | ruta | línea |
|---|---|---|---|---|---|
| C13.1 | Los tres flujos, en mdp y % PIB | CGPE 2026 | `flujos.csv` | AB | P+G |
| C13.2 | Los tres acervos | CGPE 2026 | `acervos.csv` | AB | — |
| C13.3 | Techos de endeudamiento, y su distinción del déficit y del endeudamiento informativo | ILIF 2026 arts. 1o. a 3o. | `techos.csv` | AB | — |
| C13.4 | **Descomposición de cuatro variables** del cambio de SHRFSPF/PIB | C13.1, C13.2 y C1.1 | `descomposicion.csv` | AB | — |
| C13.5 | **Prueba de aceptación:** reproducir la caída de 2022 (RFSPF 4.5 % con el acervo de 50.7 a 49.4) **antes** de aplicar el marco a 2026 | CGPE 2024 con su añada; descomposición oficial de la ILIF 2024 | `descomposicion_2022.csv` | AB | — |
| C13.6 | **Sensibilidad al tipo de cambio de cierre**, que en 2025 resultó material | C13.4 + CGPE sensibilidades | `descomposicion_fx.csv` | AB | — |
| C13.7 | Costo financiero por ramo y entidad | DEC Anexo 1 ramos 24 y 34; Anexo 8 | `costo_financiero.csv` | AB | P+G |
| C13.8 | **Deuda por habitante** | C13.2 + CONAPO población total | `deuda_percapita.csv` | AB | P |
| F13.1 | SHRFSPF en % del PIB, serie y horizonte | CGPE 2026 | `deuda_serie.csv` | AB | — |

**El capítulo 13 no presenta el marco de manual** (primario más r menos g). Retirado por
sesgo sistemático; el diagnóstico vive en la bitácora y nunca en el documento.

### 8.5 Capítulo 14 y cierre

| id | contenido | dato que necesita | archivo | ruta | línea |
|---|---|---|---|---|---|
| C14.1 | La tríada de NTA: perfil de edad, dirección demográfica, dónde vive el gasto, denominador | C5.1, C6.1, C7.1 o sus sustitutos | `triada_nta.csv` | AB | — |
| C14.2 | **Dónde declara el paquete un supuesto demográfico y dónde no**, pieza por pieza | CGPE, ILIF y DEC 2026, búsqueda exhaustiva | `supuestos_demograficos.csv` | AB | — |
| C14.3 | **Qué habría significado tener el horizonte que falta:** los tres rubros por su denominador natural, proyectados con la demografía declarada | C5.2, C6.5, C7.5 + CONAPO/CELADE | `triada_percapita.csv` | **A** para dos de tres; pensiones en AB | — |
| F14.1 | Los tres rubros por su denominador natural, serie | C14.3 | reusa `triada_percapita.csv` | A | — |
| — | **Registro del documento** — verificaciones imposibles en vivo, capítulos no redactables, y qué no puede afirmarse | se llena en las fases 2 y 3 | `registro.csv` | AB | — |

**Total previsto: 47 cuadros y 8 figuras bajo Ruta A**; bajo Ruta B, 26 cuadros y 5 figuras,
más las declaraciones de capítulo no redactable. Las dos cifras se anotan ahora para poder
comparar contra lo que se entregue.

---

## 9. Capa demográfica declarada

Segunda capa, con `tier = externa_demografica`, **valor nuevo del vocabulario de tier**
(los tres anteriores son `oficial_primaria`, `derivada_ciep`, `autoral_ited`). Se anota en
la bitácora al adoptarlo.

| denominador | fuente prevista | usa |
|---|---|---|
| Población total y por edad, proyecciones | CONAPO; CELADE como control | C11.4, C13.8, C14.3 |
| Población de 65 años y más | CONAPO | C7.5 |
| Matrícula por nivel educativo | estadística educativa oficial | C6.5 |
| Población en edad escolar | CONAPO | C6.5 |
| Afiliación IMSS, ISSSTE, y población sin seguridad social | IMSS, ISSSTE, fuente de cobertura | C5.2 |
| Población por entidad federativa | CONAPO | C10.2 |
| Padrón de programas pensionarios | donde exista | C7.3 |

**Reglas, sin excepción:**

1. Cada denominador con **fuente, año de referencia y liga** en `datos/_fuentes.csv`.
2. **Cuadros presupuestales y cuadros per cápita van separados.** Nunca una cifra del
   paquete y un denominador externo en la misma línea sin marca.
3. Toda cifra per cápita declara su denominador. **En educación, los tres denominadores se
   presentan juntos y se leen distinto**: población total, población en edad escolar y
   matrícula.
4. Si un denominador no se consigue, **se declara y no se calcula**. La regla vieja —no
   publicar per cápita sin denominador— sigue vigente como último recurso; deja de ser el
   primero.

---

## 10. Presupuesto de afirmaciones

**Umbral por capítulo:** al menos **12 afirmaciones cuantitativas verificables**, de las
cuales al menos **6 de restitución de fuente oficial primaria**, y no más del **30 %** del
total del capítulo en `no_verificable`.

Se declara **antes** de redactar cada capítulo, en `documento_2026/presupuesto_afirmaciones.md`,
con una fila por capítulo: contadas, restituciones, derivaciones, juicios, no verificables,
y veredicto redactable o no redactable.

**Si un capítulo no llega, se escribe su declaración de no redactable** y esa declaración se
compila **como página del documento**, en el registro y no como nota técnica: qué se quiso
decir, qué fuente exacta haría falta, por qué no está bajo régimen en vivo, y qué
respondería si estuviera.

**La fluidez de la prosa no es evidencia de verificación.** El presupuesto se cuenta sobre
el borrador terminado, no sobre la intención.

**Nota específica de esta corrida:** bajo Ruta B se espera que varios capítulos no lleguen
(§6.3). Un capítulo que dice con precisión qué no puede afirmar es mejor que uno que lo
afirma sin fuente.

---

## 11. Convenciones que rigen todo el documento

Se declaran en la nota de método del frente y se cumplen en todos los capítulos.

1. **Nomenclatura.** RFSPF y SHRFSPF, con la equivalencia RFSP y SHRFSP declarada una vez.
2. **Deflactor.** El del PIB que declara el CGPE 2026. **Nunca derivado de agregados
   publicados redondeados.** Excepción marcada para prestaciones individuales, que usan el
   índice de precios al consumidor, señalada en el lugar y nunca los dos en un mismo cuadro.
3. **Las cinco declaraciones del contrafactual** en toda comparación: nominal o real; contra
   aprobado o contra cierre; contra año previo o contra PIB; en pesos de qué año; y con qué
   PIB de qué añada.
4. **Ex ante contra ex ante; aprobado contra aprobado.** Nunca una serie con bases mezcladas.
   La línea P es ex ante contra ex ante; la línea G declara su asimetría cada vez.
5. **Perímetro declarado antes del primer cuadro de cada capítulo y constante dentro del
   capítulo.** Si cambia entre cuadros, es error, aunque cada cuadro sea correcto.
6. **Umbrales.** 0.5 % en niveles, 0.1 pp en tasas y razones.
7. **Prohibición de yuxtaponer magnitudes sin mecanismo declarado.**
8. **Definiciones adjudicadas contra *Balance Fiscal en México*** (SHCP, abril 2023), en
   `_metodologia/`. Nunca por criterio propio.
9. **Toda diferencia expresada en millones de pesos declara si es nominal o real.** Los
   cuadros llevan las dos columnas.
10. **Ramo y función son objetos distintos.** Una caída de ramo no es una caída de la función
    que su nombre sugiere.
11. **Agrupación por clave, nunca por nombre**, en ramo, programa y unidad responsable.
12. **Tier en toda cifra:** `oficial_primaria`, `derivada_ciep`, `autoral_ited`,
    `externa_demografica`. Registrado en `_fuentes.csv`, no en el cuerpo del texto.
13. **No se presenta el marco de manual** de sostenibilidad.
14. **Donde no se pueda verificar, se dice en el documento**, no solo en la bitácora.
15. **Nada de referencias temporales relativas.** Fecha o ejercicio.
16. **Nunca se cita una tasa de acierto entre ejercicios sin decir qué había en carpeta.**
17. **La compensación por inflación del capítulo de deuda se presenta como rango con su cota
    declarada, nunca como punto.** La fase 0.5 mostró que el «−0.05» de 2025 sale de usar el
    deflactor del PIB en los dos lados de la identidad; con el INPC que el propio CGPE usa
    para su tasa real da −0.29, y con lo único identificable en el paquete —la línea de
    adecuaciones a registros presupuestarios— da hasta −1.72. Se nombra esa línea como la
    cota que el paquete ofrece y no se cierra el rango.

### 11.1 Validación por identidad, no por relectura

Las cifras que provengan de páginas sin capa de texto se leen renderizando la página y se
validan con un conjunto de identidades contables y de coherencia entre anexos. **En 2025
fueron cincuenta pruebas y hay que correrlas después de cada cambio en los datos.** El
conjunto mínimo, de la fase 2:

- Ingresos totales = gasto neto total (DEC art. 2).
- Presupuestarios + financiamientos = total del art. 1o.
- Gasto neto total − diferimiento = gasto neto pagado.
- No programable = costo financiero + participaciones + adeudos.
- Primario = balance + costo financiero.
- Balance público = presupuestario + no presupuestario; RFSPF = público + fuera de presupuesto.
- **Anexo 3: gastos obligatorios con pensiones − sin pensiones = pensiones y jubilaciones de
  la clasificación económica.** Es la fuente que adjudica el perímetro.
- Bajo Ruta A: Gobierno Federal bruto + entidades − neteo del Anexo 1 = gasto neto total.
- Razones a PIB con el PIB nominal declarado, contra las publicadas.
- Todo concepto que aparezca en dos cuadros del mismo documento coincide en los dos.

### 11.2 Consistencia interna antes que verificación externa

Orden fijado desde 2024: **verificar cada lámina contra su cuadro y contra el texto ANTES de
verificar el texto contra la fuente.** Las cuatro pruebas baratas —texto contra lámina, texto
contra su nota al pie, capítulo sectorial contra capítulo de implicaciones, y convención
aplicada en un capítulo y no en otro— se corren sobre el borrador propio. En 2023 fueron 24
de 39 discrepancias del evaluado; en 2024, ocho de once. No hay razón para suponer que un
documento propio escrito por capítulos es inmune.

### 11.3 Reclasificaciones: se anticipan, no se descubren

**Ningún ramo, función o programa se escribe como recorte hasta que el diff lo explique.**
Precedentes que se buscan explícitamente en 2026: cambios de ejecutor de obra (Defensa →
Infraestructura → Marina en 2025), cambios de ramo de un organismo (IMSS-Bienestar del 12 al
47 en 2024, del 19 al 47 en 2025), cambios de nombre de ramo sin cambio de contenido
(Ramo 38 en 2025), adeudos liquidados que no son servicio (R023 del Ramo 19 en 2025), y
programas cuyo nombre cambia de género gramatical.

### 11.4 Restricciones de compilación, que también rigen el diseño de los cuadros

Se declaran aquí porque condicionan cómo se generan los datos, no solo cómo se compila.

- **`siunitx` está prohibido.** **Los números se formatean al generar los cuadros**, en el
  paso de datos, con separador de miles y decimal en español, aplicados de forma uniforme.
- `pgfplots` con **`\pgfplotsset{compat=1.16}`**. Nada introducido después.
- Paquetes admitidos: `babel` (spanish), `geometry`, `fancyhdr`, `booktabs`, `graphicx`,
  `hyperref`, `caption`, `longtable`, `array`, `pgfplots`, y `lmodern` **siempre**, porque
  sin él T1 con Computer Modern genera fuentes bitmap y agota el tiempo de compilación.
- **Prohibidos:** `siunitx`, `minted`, cualquier cosa que exija `shell-escape`, fuentes no
  estándar, y cualquier paquete que haya que instalar.
- **Si una figura resulta frágil en `pgfplots`, se genera su PDF por separado y se incluye
  con `\includegraphics`**, conservando el script y los datos que la producen. Robustez
  antes que elegancia.
- La comprobación estática (`validar_latex.py`) corre antes de cada compilación y cubre:
  llaves y entornos balanceados, que todo `\input` **se resuelva desde el directorio del
  archivo maestro**, que todo `\ref` tenga su `\label`, que los paquetes estén en la lista, y
  que las columnas que pide una gráfica existan en el `.csv` que lee. **Y debe imprimir qué
  no comprueba.**

---

## 12. El reloj

**T+0 = 2026-09-07, 09:03:57 CST.** Cada hallazgo se registra en la bitácora de la corrida
con el momento en que quedó disponible, medido desde T+0. Al terminar, cada hallazgo se
clasifica en tres bandas: **dos horas**, **ocho horas**, **veinticuatro o más**.

Hipótesis de partida, del protocolo de 2025, que esta corrida pone a prueba **bajo régimen
restringido y por tanto puede refutar**:

- **A las dos horas** deberían estar: gasto neto, programable y no programable con su
  variación real y su % del PIB; el gasto por ramo con las dos diferencias; los tres flujos
  y los tres acervos con su nombre correcto; los ingresos por renglón del art. 1o. y el
  financiamiento por cada cien pesos; los techos de endeudamiento y su distinción del
  déficit.
- **Lo que no se afirma a las dos horas aunque el dato esté en pantalla:** que un ramo se
  recortó; cualquier cifra per cápita; que una serie toca un mínimo o un máximo histórico.
- **A las veinticuatro:** el diff de códigos completo, la descomposición del acervo con su
  prueba de aceptación, los perímetros que hay que adjudicar, las series estructurales, y la
  lectura como imagen de las páginas sin capa de texto.

**La banda de dos horas del protocolo de 2025 supone analíticos cargados.** Si la fase 1
resuelve Ruta B, esa banda se encoge y decirlo con precisión es el resultado principal de
esta corrida.

**No se acelera a costa de verificar.** El punto no es ser rápido: es saber qué se puede
decir a cada hora.

---

## 13. Riesgos declarados de antemano

1. **Ruta B.** Probabilidad alta: los analíticos del proyecto llevan 404 desde 2022 en las
   tres rutas conocidas. El plan B está escrito (§6.2, §6.3) y no se improvisa.
2. **CGPE 2026 sin capa de texto.** El de 2025 tenía 90 de 91 páginas como imagen. Si 2026
   repite, se renderiza a 150 dpi y se valida por identidad (§11.1). No es un imprevisto.
3. **Capítulos 11 y 12 son primera edición.** No hay perímetro heredado para medio ambiente
   y agua. Se construye y se declara; si no se puede enumerar, no se publica.
4. **Fase 0.5 puede invalidar cifras de 2025.** Si nuestras cifras de salud, educación,
   Defensa, tasa real del costo financiero o niveles del acervo no resisten, el resto de la
   corrida hereda el problema. Por eso va antes que la adquisición.
5. **Contaminación de forma, no de cifra.** En 2025 los dos documentos abrieron con la misma
   frase, escrita de forma independiente. El molde viaja aunque el dato no. Se busca
   explícitamente en la fase 7.

---

## 14. Cambios al pacto

Cada cambio lleva hora, qué cambia y por qué. Esta lista es un resultado del ejercicio.

**2026-09-07, 09:05 CST · Cuarentena física, antes de sellar.** La instrucción §2 afirma que
`2026/` «ya contiene solo piezas de proyecto: CGPE, ILIF y PPEF». No era cierto: la carpeta
contenía también `ciep_implicaciones2026.pdf`. Se movió a `_cuarentena_2026/` con `git mv` y
un `LEEME.md` que fija la condición de levantamiento. Motivo: el criterio de aceptación 1.4
es binario y no admite depender de la disciplina de no abrir un archivo que está a la vista.
Vuelve a `2026/` cuando la fase 7 levante la cuarentena, con la hora registrada.

**2026-09-07, 09:06 CST · Ruta de la carpeta de trabajo.** La instrucción §7.1 escribe
`_documento_2026/entrega/`. Se adopta `documento_2026/_entrega/`, que invierte el guion bajo,
por consistencia con `documento_2025/_entrega/` y con los scripts que ya lo suponen. Es una
desviación de forma, no de contenido, y se declara para que no se lea como descuido.

**2026-09-07, 09:38 CST · Convención nueva tras la fase 0.5.** Se añade la regla 17 de §11
(compensación por inflación como rango, no como punto) y se anota que las tres verificaciones
que la fase 0.5 pudo hacer —separar objeto de perímetro, medir lo que movió la Cámara, y
adjudicar un titular de proyecto contra el presupuesto ejercido— **son imposibles en vivo** y
entran en el registro del documento. Motivo: son el resultado de la fase 0.5, y el pacto tiene
que reflejarlo antes de la fase 1. Ver `fase05_adjudicacion.md`.

**2026-09-07, 10:05 CST · Ruta A adoptada y §2.1 refutado.** La fase 1 encontró los
analíticos del proyecto 2021–2026 en una ruta nunca sondeada, un repositorio de datos
abiertos con el proyecto completo a nivel de partida específica, y la Gaceta Parlamentaria
del día de la entrega con el paquete íntegro. Se marca §2.1 como refutado sin borrarlo, se
sube la línea P a programa y unidad responsable en §3, se descongela una serie en §7, y se
añaden `C2.6` (miscelánea) y `C8.3` (cartera de inversión) en §8. Motivo y detalle en §6.5 y
en `_aprendizaje/mapa_fuentes.md`, adenda 2026-09-07.
