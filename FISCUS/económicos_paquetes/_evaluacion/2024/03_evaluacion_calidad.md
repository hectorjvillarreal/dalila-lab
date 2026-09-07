# Evaluación de calidad — capítulo de educación de CIEP, Paquete Económico 2024

**Corrida:** FISCUS · Dalila · 2026-09-06 · instrucción v3, fase 5
**Objeto evaluado:** *Implicaciones del Paquete Económico 2024* (CIEP, 14 de septiembre de 2023), capítulo 8 «Gasto en educación» (pp. 44–47), el frente del documento (presentación pp. v–vii y resumen ejecutivo pp. viii–x) y el apartado de educación del capítulo 13 (p. 76).
**Base de verificación:** `02_verificacion_cifras.csv`, 115 filas.

---

## Sección cero — qué condiciona esta evaluación

1. **Asimetría de objeto.** CIEP evalúa el **proyecto** (PPEF 2024). Esta corrida verifica contra el **PEF aprobado** de 2023 y 2024, porque los analíticos del proyecto no se obtuvieron: el árbol `ppef.hacienda.gob.mx/work/models/PPEF2024/` devolvía 404 en la resonda (fase 7). Donde el aprobado difiere del proyecto se reconstruyó el proyecto restando la reasignación de la Cámara, que en educación está identificada renglón por renglón: **+13,262.4 mdp al Ramo 11, íntegramente al programa S072 Becas de Educación Básica**, y **−89.8 mdp al FAM infraestructura educativa** (−57.9 básica, −3.9 media superior, −28.5 superior). Con esa corrección los agregados de CIEP reconstruyen al mdp, lo que valida el procedimiento.
2. **Series históricas ausentes.** Seis de las nueve columnas de las dos figuras del capítulo son ejercido 2016–2022, es decir Cuentas Públicas, que no están en carpeta y por decisión confirmada (§5.5 de la instrucción) **no se descargan**. Treinta y una filas del CSV quedan `no_verificable` por esta razón, casi todas comparaciones contra 2016, 2017 o 2018.
3. **Sin fuentes de matrícula.** No hay CONAPO ni estadística educativa de la SEP en la carpeta. Los denominadores de las tres series de gasto por estudiante se reconstruyen por división, no se verifican contra su fuente.
4. **El capítulo 8 no contiene ningún cuadro.** Dos figuras y cero tablas, contra el capítulo 9 (salud), que sí trae una. Las comprobaciones de lámina contra cuadro se convirtieron necesariamente en lámina contra texto.

---

## 1. Perímetro

**El perímetro está declarado y es recuperable, y esa es la mejor noticia del capítulo.** La nota al pie 10 dice qué se suma: Ramo 11 completo, más Ramo 38 (CONAHCYT), más Ramo 48 (Cultura), más el resto de la función Educación. Con esa receta el agregado se reconstruye al mdp:

| componente (proyecto 2024, mdp) | monto |
|---|---|
| Ramo 11 Educación Pública, total | 425,755.5 |
| Ramo 38 Humanidades, Ciencias, Tecnologías e Innovación | 33,170.7 |
| Ramo 48 Cultura | 16,754.9 |
| Función Educación fuera del Ramo 11 (ramos 33, 25, 08, 07, 13, 47) | 620,862.9 |
| **total reconstruido** | **1,096,543.8** |
| **cifra publicada por CIEP** | **1,096,544** |

Por la **prueba de divulgación** de §2.5 esto es `perimetro`, no `objeto`: los componentes están a la vista y el lector puede ver qué se sumó. Es la diferencia con el capítulo de deuda de 2023, donde la etiqueta sustituía a los componentes.

Dicho eso, el perímetro **no es el del gasto en educación**. Añade 52.2 mmp de ciencia y tecnología (Ramo 38 más la función CTI del Ramo 11) y 24.6 mmp de cultura y deporte (Ramo 48 más la función 4 del Ramo 11) que no son función Educación, y a cambio no omite nada de ella. La función Educación del Gobierno Federal, que es la única definición oficial que cruza ramos, vale **1,019,448.8 mdp en el proyecto** y 1,032,621.4 en el aprobado: **77.1 mmp menos que el agregado de CIEP, 0.22 puntos del PIB menos en la razón** (2.97 % contra 3.19 %). Las dos definiciones son legítimas; el problema es que la brecha de 0.81 pp contra la recomendación internacional (V030, V098) se calcula con la ancha. Con la función Educación estricta la brecha es de 1.03 pp, un cuarto mayor.

**Donde el perímetro sí falla es en los subagregados.** La nota 10 cubre el total y nada más:

- **Ciencia, tecnología e innovación, 52,150 mdp** (V092). Reconstruye exactamente como Ramo 38 + Ramo 11 en función CTI (33,085.1 + 19,064.4 = 52,149.5). La función completa del Gobierno Federal vale 60,385.7: quedan fuera los ramos 08, 12 y 23. El perímetro no se declara aquí.
- **«Continúan sin asignarse recursos a la innovación»** (V094). Cierto dentro de esos dos ramos. En el Gobierno Federal la subfunción Innovación tiene 1,805.5 mdp, todos en el Ramo 23. La frase es verdadera y su alcance no está dicho.
- **Pensiones, 21.9 % del gasto neto total** (V044). Solo se obtiene con el perímetro amplio (contributivas más pensión de adultos mayores más personas con discapacidad, 1,991.9 mmp). Por clasificación económica son 1,499.0 mmp, 16.5 %. El capítulo 8 usa el amplio sin decirlo; el capítulo 13 lo declara implícitamente al escribir 5.8 % del PIB (V110). Un perímetro, dos capítulos, ninguna declaración.
- **«Segundo programa más importante»** para la beca de media superior (V074). Cierto dentro de la subfunción de media superior; en el Ramo 11 es el quinto. El universo del ranking no se dice.
- **Cultura, deporte y recreación, 24,542 mdp** (V090) y su composición de 47.4 % (V091) reconstruyen al décimo con la función completa. Aquí el perímetro implícito sí es el oficial.

**Federal contra federalizado: ausente.** El capítulo trata 1.1 billones de pesos como un solo objeto sin decir nunca que **el 59 % de la función Educación se transfiere a las entidades** y que el capítulo 8000 (participaciones y aportaciones) es el 53.5 % de ella. El FONE aparece cuatro veces, siempre como un programa que sube, nunca como lo que es: 496.8 mmp, el 48 % del gasto educativo federal y 1.13 veces el Ramo 11 completo. Un lector del capítulo termina creyendo que el gasto educativo federal es la SEP.

**Veredicto de perímetro:** declarado y auditable en el agregado, indeclarado en cinco subagregados, y ciego a la distinción que decide el rubro.

---

## 2. Contrafactual declarado

**Las dos tasas de §2.1**, sobre las 68 filas donde la comparación aplica:

| medida | 2024 educación | 2023 deuda |
|---|---|---|
| Estricta, cinco declaraciones | **41 %** (28/68) | 17 % |
| Puente de cuatro declaraciones (sin el denominador poblacional) | **49 %** (33/68) | 68 % |

La estricta mejora 24 puntos; el puente cae 19. La razón de que las dos tasas casi coincidan en 2024 es que el capítulo de educación tiene pocas cifras per cápita, mientras que el de deuda estaba hecho de ellas.

**Pero el hallazgo de esta sección no es la tasa: es que el documento nunca declara su deflactor.** No hay una sola mención del factor de 1.0480 ni de la añada de pesos en las 96 páginas. Y sin embargo el capítulo entero está construido con él.

**El patrón dominante del capítulo 8 es que las variaciones en mdp son reales y se presentan como diferencias de nivel.** Verificado renglón por renglón:

| afirmación | variación real (2024 = CIEP) | variación nominal | fila |
|---|---|---|---|
| Presupuesto educativo total | +29,081 | +77,972 | V036 |
| FONE servicios personales | +18,206 | +38,174 | V060 |
| Previsiones salariales del FONE | +3,340 | +4,361 | V101 |
| Servicios de educación básica en la CDMX | +1,926 | +4,115 | V061 |
| Apoyo administrativo, Ramo 25 | +890 | +1,087 | V041 |
| Apoyo administrativo, Ramo 11 | +471 | +757 | V042 |
| U006 en media superior | −3,017 | −1,335 | V072 |
| U006 en superior | +3,044 | +6,359 | V081 |

Ocho de ocho. El texto dice «es 29 mil 81 mdp mayor al de 2023», «incrementaría en 18 mil 206 mdp», «presenta la mayor reducción con 3 mil 17 mdp menos». Ninguna dice «en términos reales». Un lector que sume las partidas del decreto no encontrará ninguno de estos números.

**El caso que convierte el hábito en error es la nota al pie 11** (V038). Dice: «En 2023, se aprobaron 22 mil 297 mdp para Previsiones salariales y económicas del FONE, pero no se han ejercido». Lo que la Cámara aprobó en 2023 fueron **21,275.7 mdp corrientes**. Los 22,297 son esa cifra multiplicada por 1.048. Es la deflactación aplicada a un hecho legal, donde no cabe: un decreto aprueba pesos corrientes de su año. Aquí el hábito deja de ser una omisión de etiqueta y produce una afirmación falsa sobre lo que dice el Presupuesto de Egresos.

**Lo que sí está bien.** Cuando CIEP compara en porcentajes, nombra su base y acierta: «1 % por arriba del PEF 2023» (V048), «3.2 % más que en el PEF 2023» (V058), «1.5 % menor al PEF 2023» (V070), «no presentan variación real» (V043, con el calificador correcto). Las cuatro cierran contra los analíticos. Y el tratamiento del **cambio de año base del PIB** en el resumen ejecutivo (V019) —«si se usara el mismo PIB en ambos años, el indicador pasaría de 48.5 % a 48.8 %»— es el mejor contrafactual del documento y el único que declara un cambio de vintage. Que exista prueba de que la casa sabe hacerlo agrava lo que sigue.

---

## 3. Consistencia interna del documento

Se sube de rango por la lección de 2023, y vuelve a ser la fuente principal de hallazgos: **de los once renglones marcados `no`, ocho son contradicciones del documento consigo mismo**, no discrepancias contra la fuente oficial.

**3.1 La lámina contra el texto: el gasto por alumno de educación básica.** El texto de 8.2 dice que el gasto por alumno de educación básica alcanza su máximo «pero el aumento es resultado de 1.8 millones de NNA menos en las escuelas», y 8.3 lo repite: «El gasto en EB si incrementa por mayores recursos para previsiones salariales y una menor matrícula» (V065, V103). La propia Figura 8.2 lo desmiente:

| | 2023 | 2024 | variación |
|---|---|---|---|
| Gasto de educación básica (pesos de 2024) | 617,548.7 | 637,503.0 | +3.23 % |
| Gasto por alumno (Figura 8.2) | 28,738 | 29,545 | +2.81 % |
| **Matrícula implícita** | **21.489 M** | **21.577 M** | **+0.41 %** |

El denominador **sube**. El gasto por alumno crece porque el presupuesto crece más rápido que la matrícula, no porque haya menos niños. Y hay más: los denominadores implícitos de los tres niveles crecen exactamente lo mismo —básica +0.413 %, media superior +0.412 %, superior +0.413 %—, lo que indica que la serie por estudiante se construyó con **un solo factor de crecimiento común**, no con matrícula por nivel. Es el hallazgo de horizonte del capítulo: la única cifra demográfica que el texto invoca (1.8 millones menos) es incompatible con la aritmética de su propia gráfica.

**3.2 El texto contra su nota al pie: apoyo administrativo.** El encabezado (p. 44) resalta «el aumento de 1 mil 385 mdp para Actividades de apoyo administrativo». La nota al pie 15 (p. 47) lo desglosa: «890 mdp en el Ramo 25 y 471 mdp en la SEP». Suman **1,361** (V040). Los dos sumandos son exactos contra los analíticos; el total no. Y en el Gobierno Federal completo ese programa **cae 164 mdp** en términos reales: el aumento solo existe si se miran los dos ramos educativos.

**3.3 Un capítulo contra otro: el gasto por estudiante contra 2016.** El capítulo 8 acota correctamente: los incrementos «no garantizan un gasto por estudiante mayor a los niveles de 2016 **en EMS y Educación Superior**» (V102). El capítulo 13 repite la frase **sin el calificador**: «no se garantiza un gasto por estudiante mayor a los niveles de 2016» (V107). Queda contradicha por la Figura 8.2, cuyo titular es que la educación básica alcanza su máximo de la serie. El calificador se pierde al pasar del capítulo sectorial a las implicaciones, que es donde más se cita.

**3.4 La presentación contra el capítulo 13: el espacio fiscal.** La presentación (p. v) dice que el espacio fiscal pasa de 2.0 % del PIB en 2023 a 0.9 % en 2024. El capítulo 13 (p. 75) dice que «cayó 60 %». De 2.0 a 0.9 la caída es de **55.0 %** (V108). Para que fuera 60 % haría falta 2.25 → 0.9 o 2.0 → 0.8.

**3.5 El año de la base del costo financiero.** El resumen ejecutivo dice que el costo financiero «es mayor en 11.8 % a lo aprobado para **2022**» (V021). La tasa es correcta contra el **PEF 2023**, que es además lo que comparan el capítulo 2 y el 13.

**3.6 El rango de crecimiento de 2023.** El cuadro macro de la presentación da «2.5 a 3.0» para el estimado de 2023 (V012). El CGPE 2024 da **[2.5, 3.5]** en los cinco cuadros donde aparece; [1.2, 3.0] es el rango de la aprobación de 2023, no del estimado.

**3.7 Mínimos en proporción del PIB.** El encabezado y el resumen ejecutivo afirman que el monto «como proporción del PIB y del gasto neto total alcanza mínimos» (V026, V097). Para el gasto neto es cierto y la Figura 8.1 lo rotula: 12.10 contra 12.27 en 2023. Para el PIB **no**: con el PIB rebasado a 2018, 2023 vale 3.187 % y 2024 vale 3.190 %. El mínimo solo aparece si el punto de 2023 se deja en el PIB base 2013 (3.24 %, que es exactamente lo que el propio CIEP publicó en 2023) y el de 2024 se calcula con la base nueva. **Es el mismo cambio de vintage que el capítulo de deuda sí corrige** (V019), aplicado en un capítulo y no en el otro.

**Discrepancias contra la fuente oficial, no internas:** tres. El rango de crecimiento de 2023 (V012, §3.6), la nota 11 de las previsiones del FONE (V038) y la nota 13 del programa de infraestructura educativa (V080), que declara 891 mdp y un aumento de 517 cuando el programa vale 1,170.0 y sube 1,018.0 reales sobre una base de 145.0. Esta última no reconstruye por ningún perímetro probado y la Cámara no lo tocó.

---

## 4. Cobertura

**Lo que el capítulo cubre y cubre bien.** Los tres niveles educativos con nivel, variación y gasto por estudiante; las cuatro becas con su suma y su peso en la SEP; posgrado, educación para adultos, cultura y CTI; el conteo de programas y unidades responsables con reducción en cada subfunción. Este último es notable: **4 de 18 en básica, 4 de 19 en media superior, 3 de 23 unidades responsables en superior, con los tres nombres correctos**, todos verificados exactamente contra los analíticos (V059, V071, V078). Es trabajo de detalle real sobre el analítico, hecho en 72 horas.

**Lo que falta, en orden de importancia.**

1. **El FONE como objeto.** 496.8 mmp, el 48 % del gasto educativo federal, aparece solo como dos incrementos de partida. No hay nivel, no hay peso relativo, no hay reparto por entidad. **El FONE se distribuye por fórmula (LCF art. 27) y el capítulo no dice cómo, ni si la fórmula cambió.** Sin corte territorial el capítulo no dice nada sobre incidencia, que es el título de su sección 8.2. El reparto está en el decreto (Anexo 22) y es reproducible: el Estado de México 49,009.1 (9.9 %), Veracruz 36,335.3, Oaxaca 31,126.2, y la Ciudad de México ausente porque su educación básica va por el Ramo 25.
2. **La separación federal / federalizado**, tratada en §1.
3. **El supuesto de matrícula.** El paquete no lo trae —ni el CGPE, ni la ILIF, ni el decreto declaran alumnos, cobertura, planteles ni docentes— y esa ausencia es un hallazgo que el capítulo no reporta. En su lugar construye tres series por estudiante con denominadores que nunca enuncia y que, según §3.1, no son matrícula.
4. **La reasignación de la Cámara.** CIEP evalúa el proyecto, lo cual es su encargo. Pero el documento se lee todo el año, y en el Ramo 11 la Cámara movió 13,262.4 mdp a un solo programa, tres veces el crecimiento real del proyecto entero. La afirmación «Becas Universales no presentan variación real» (V043) es cierta del proyecto y falsa del presupuesto vigente, donde el programa crece 36.3 % real. El documento no advierte que sus cifras caducan en noviembre.
5. **Los anexos transversales.** Ninguna mención al Anexo 12 (ciencia y tecnología, 148,154.2 mdp, +9.8 % real) ni al Anexo 29 (subsidios a universidades públicas estatales por entidad, 74,688.8 repartidos entre 31 estados). El segundo es el único corte territorial de educación superior que publica el paquete.
6. **La unidad responsable como instrumento.** El capítulo usa las UR para contar recortes en superior, y ahí se le escapa lo que las UR sirven para ver: de los tres «recortes» que nombra, el de la Dirección General de Programación y Presupuesto es una **renumeración administrativa** —la UR 416 desaparece con 6,109.2 mdp y la UR 420 aparece con 6,276.5— y el movimiento real conjunto es de −126.0, no de −6,402.5 (V078). El conteo es correcto; la lectura induce a error. La reasignación entre unidades responsables es el mecanismo habitual de cambiar política sin cambiar el agregado, y en 2024 hay una que sí importa y el capítulo no ve: la Coordinación Nacional de Becas pasa de 20.9 % a 23.1 % del Ramo 11, y es obra de la Cámara.
7. **Las tres partidas de infraestructura educativa** dispersas entre el FAM (20,065.6, −2.0 % real), La Escuela es Nuestra (28,358.3) y la obra pública directa (1,048.4). El capítulo menciona la segunda y una parte de la tercera; el FAM no aparece.

**Rutas agotadas antes de declarar ausencias:** se verificó que ninguna de las siete piezas anteriores esté en otra sección del documento ni en el capítulo 4 (gasto federalizado), que trata el FONE como parte del agregado transferido sin desglose educativo.

---

## 5. Trato de los supuestos macro y del supuesto de matrícula

**Los macro se tratan bien y por separado.** El cuadro de la presentación pone tres columnas —2023 aprobado, 2023 estimado, 2024— y las cinco variables cierran contra el CGPE salvo el rango de 2023 (V012). El documento no adopta el marco de la SHCP: lo contrasta con Banxico y el FMI y dice en qué dirección discrepa. Y usa el crecimiento potencial de 2.39 % para el argumento correcto (V009), aunque conviene registrar que la propia SHCP declara r = 2.38 % justamente por ser menor al potencial: hay dos tasas oficiales de crecimiento para 2024 en el mismo documento y CIEP toma la del marco macro, no la de la regla de deuda.

**El supuesto de matrícula no se trata: se sustituye.** El paquete no lo declara, el capítulo no reporta esa ausencia, y las tres series por estudiante se construyen con un denominador implícito que crece 0.41 % uniforme (§3.1). La única cifra de matrícula del capítulo —81,670 estudiantes más en superior desde 2019 (V083)— viene de fuente externa y **no se usa como denominador de ninguna razón**.

**La conexión demográfica está invertida.** Educación es el rubro donde la transición opera a la baja: la población en edad escolar se contrae mientras la de edad avanzada crece. El documento tiene el horizonte demográfico del lado de pensiones —el capítulo 13 insiste en «una población cada vez más envejecida»— y en el lado de educación lo invoca una sola vez, con el signo correcto pero con una cifra que su propia gráfica contradice. Un gasto educativo que crece 0.0 % real por programa **sube por alumno si la matrícula cae y baja si la matrícula sube**, y el capítulo no puede decir cuál porque no tiene matrícula.

---

## 6. Separación descriptivo–normativo y horizonte

**La separación es limpia y está señalizada tipográficamente.** Las secciones 1 y 2 de cada capítulo describen, la 3 concluye, y el capítulo 13 recoge lo normativo del documento entero. Las recomendaciones llevan fuente (BID 2022, Banco Mundial 2017, Naciones Unidas 2023). De las 115 filas solo 12 son `juicio` y ninguna se presenta como dato.

**Dos objeciones.** La primera: la brecha de 0.81 puntos del PIB (V030, V098) se enuncia como si «la recomendación internacional» fuera un umbral y es un rango de 4 a 6 %; la brecha contra el límite superior es de 2.81 pp, tres veces y media mayor. Elegir el extremo benigno de un rango y llamarlo «la recomendación» es una decisión normativa presentada como descriptiva, y es la cifra que el resumen ejecutivo repite. La segunda: el 80 % del gasto «ya comprometido» (V109) no se reconstruye con los tres conceptos que la frase nombra —pensiones, gasto federalizado y costo de la deuda suman 64.2 % con el perímetro amplio— y falta definición de «comprometido».

**El horizonte es de un año.** Las dos figuras van de 2016 a 2024 y ninguna proyecta. El capítulo 13 exige que las proyecciones de deuda incorporen el envejecimiento, y el capítulo 8 no proyecta nada. El paquete tampoco lo permite: el horizonte de mediano plazo del CGPE (p. 122) no desagrega funciones. Pero la asimetría es del documento: reclama horizonte para pensiones y no lo ofrece para educación, que es el rubro donde la demografía es favorable y donde por eso mismo la ausencia de matrícula duele más.

---

## Recuento

| | 2024 educación | 2023 deuda |
|---|---|---|
| Filas | 115 | 376 |
| Verificables | 84 (73 %) | — |
| Coinciden (`si` + `aprox`) | 73 de 84 (87 %) | 65 % |
| No coinciden | 11 | — |
| No verificables | 31 (27 %) | — |
| Contrafactual explícito, tasa estricta | 41 % | 17 % |

**`tipo_error`:** `transcripcion` 5, `objeto` 4, `perimetro` 1, `deflactor` 1.

**Ocho de los once errores son contradicciones internas.** La serie de patrones se cierra como anticipaba la instrucción: **ingresos falla por base, gasto por perímetro, deuda por nombre, y un rubro federalizado falla por consistencia interna.** No porque CIEP compare mal contra la fuente oficial —contra la fuente acierta 87 % de las veces y reconstruye el agregado al mdp— sino porque un rubro que vive en cuatro ramos, seis subfunciones y treinta y dos entidades obliga a mantener coherentes un texto, dos láminas, doce notas al pie y dos capítulos, y ahí es donde se rompe.
