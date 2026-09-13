# Checklist de omisiones propias

**Artefacto de método · FISCUS · creado 2026-09-07 · precarga §3.9 de
`INSTRUCCIONES_preparacion_2027.md`**

---

## Por qué existe

En 2027 **no habrá documento del género con qué compararse**: la corrida es en vivo y el
ejemplar de CIEP sobre el mismo paquete no existirá cuando cerremos. Las secciones «lo que
el otro documento tiene y nosotros no» de las comparaciones 2025 y 2026 fueron el mecanismo
que detectaba nuestras omisiones. **Esta lista es su reemplazo, y hay que correrla a mano.**

El precedente que la justifica: la vara externa de suficiencia en salud ---el 6 % del PIB
que recomienda la Organización Mundial de la Salud--- **estaba en la checklist de la corrida
2025 y volvió a quedarse fuera en 2026**. Una lista que no se revisa capítulo por capítulo
no sirve de nada.

## Cómo se usa

Al cerrar cada capítulo, y otra vez antes de compilar. Tres respuestas posibles por renglón:

- **HECHO** — está en el documento, con el capítulo donde vive.
- **FUERA DE ALCANCE** — se declara en el registro del documento **con su razón**, no se
  omite en silencio.
- **PENDIENTE** — no se ha decidido. Ningún renglón puede quedar así al compilar.

La columna que hace utilizable la lista es **«¿está en vivo?»**: si la fuente no estará
disponible el día de la entrega, el renglón nace fuera de alcance y eso se sabe antes de
gastar reloj en buscarlo.

---

## La lista

### A. Renglones que la corrida 2026 ya puede resolver, porque la precarga los desbloqueó

| # | qué falta | fuente que lo resuelve | ¿está en vivo? | estado 2027 |
|---|---|---|---|---|
| A1 | **Gasto en salud por persona afiliada, por subsistema** | `datos_demograficos/`: asegurados del IMSS (cubo mensual del portal propio del Instituto), derechohabientes del ISSSTE (catálogo nacional), registro de IMSS-Bienestar | **Sí, precargado.** No depende del paquete | Era la carencia número uno de 2026. **Resuelta en la precarga.** Cuidado: asegurados del IMSS **no** es derechohabientes; la razón entre subsistemas cambia según cuál se use y hay que decir cuál |
| A2 | **Gasto por alumno, por nivel educativo** | `datos_demograficos/matricula_sep.csv`, Principales Cifras del Sistema Educativo Nacional | **Sí, precargado** | Resuelta. Los tres denominadores ---población total, población en edad escolar, matrícula--- van en cuadros separados |
| A3 | **Padrones de programas pensionarios no contributivos** | `datos_demograficos/padron_bienestar.csv` | **Sí, precargado** | Resuelta |
| A4 | **El perímetro de exclusión de la regla fiscal** | ILIF 2027, artículo del equilibrio presupuestario; serie 2018-2026 en `_aprendizaje/serie_perimetro_regla_fiscal.md` | **Sí**: la ILIF llega el día de la entrega y contiene su exposición de motivos | **Capítulo propio en 2027** (`14_regla_fiscal`). Lo perdieron los dos documentos de 2026 |

### B. Omisiones propias: la fuente existe y es pública, y no la usamos

| # | qué falta | fuente que lo resuelve | ¿está en vivo? | nota |
|---|---|---|---|---|
| B1 | **Vara externa de suficiencia en salud** (6 % del PIB, OMS) | Recomendación pública, no requiere descarga | **Sí, siempre** | **Se quedó fuera dos años seguidos.** Es una línea de texto y un cociente |
| B2 | **Contraste del marco macro con pronósticos externos** | Encuesta de expectativas del banco central (mensual); *World Economic Outlook* del FMI, edición de abril; organismos internacionales | **Sí** la encuesta y la edición de abril. **No** la edición de octubre del WEO, que sale después de la entrega: se usa la de abril y **se declara la añada** | El capítulo macro de 2026 discute el marco contra sí mismo y contra nadie más |
| B3 | **Comparación contra los Pre-Criterios** | Pre-Criterios del ejercicio, publicados en abril | **Sí** | Es el contraste entre lo prometido en abril y lo entregado en septiembre. El punto de entrada ya lista la fila 2027 con sus Pre-Criterios |
| B4 | **Límite de gasto corriente estructural contra el observado** | CGPE, partida informativa y su restitución en el texto | **Sí** | Hecho en 2026 y convertido en identidad; **se conserva en el guion de identidades** |
| B5 | **Presupuesto de la Secretaría de las Mujeres como proporción del anexo de igualdad** | Analíticos por ramo más el anexo transversal | **Sí** | Cifra pequeña y elocuente que no calculamos |
| B6 | **Convenios de reasignación** | Analíticos, concepto de gasto federalizado no comprendido en los Ramos 28 y 33 | **Sí** | Nuestro perímetro federalizado los excluyó por declaración; **la declaración se mantiene, pero el monto se reporta** |
| B7 | **Federalismo más allá de los Ramos 28 y 33**: convenios, subsidios, coordinación fiscal, distribución subnacional | Analíticos de entidades, anexos del decreto, Ley de Coordinación Fiscal | **Sí** | Es la ampliación natural del capítulo de gasto federalizado |
| B8 | **Balances de las empresas públicas con y sin apoyos** | CGPE, anexos de Pemex y CFE | **Sí** | El capítulo de energéticos de 2026 mira la renta y la aportación de capital, no el balance |
| B9 | **Economía de cuidados: qué parte del anexo es gasto preexistente** | Anexo transversal de cuidados, contra el mismo anexo del ejercicio anterior | **Sí**, con el diff de anexos ya construido | **Sólo como auditoría de etiquetado**, que es donde nuestro método aporta (§4 de la instrucción) |
| B10 | **Género: concentración del anexo y qué proporción son pensiones** | Anexo de igualdad entre mujeres y hombres, por programa | **Sí** | Hecho parcialmente en 2026 (48,1 % son programas de pensión). Se conserva y se amplía a la concentración |
| B12 | **Vara externa de suficiencia en vivienda** | Anexo de la Gaceta con la estimación que ordena el **artículo 61 de la Ley de Vivienda**: el monto de recursos federales requeridos para la política de subsidios de vivienda y suelo, elaborado por la Secretaría de Bienestar | **Sí**, pero **en la cola del paquete**: en 2027 no se sirvió hasta la mañana siguiente a la entrega, y el índice no lo listaba | **RESUELTA en 2027**, en la nota de actualización: 226.133,3 mdp de requerimiento contra 37.873,6 del Ramo 15 completo. Es el equivalente en vivienda de lo que B1 es en salud, y **llegó antes que B1**. Al usarla: años de pesos distintos (UMA y Reglas de Operación del ejercicio anterior) y el ramo no es el perímetro del gasto en subsidios |
| B13 | **Zonas de atención prioritaria como denominador territorial** | Nota metodológica y declaratoria ZAP del ejercicio, más los listados rural y urbano, en la cola del paquete; y el ZIP de AGEB con variables que la propia nota publica | **Sí**, con la misma advertencia de cola que B12 | **Denominador en mano, cruce pendiente, en 2027**: 1.575 municipios rurales y 43.636 AGEB urbanas. El ZIP de AGEB se descargó el 10 de septiembre y **las cinco cuentas de la declaratoria cierran contra él** ---con la advertencia de que municipios y localidades se cuentan sobre la clave actual a junio, no sobre las claves del propio archivo---. Lo que falta es cruzarlo con el gasto, que exige la distribución territorial; **eso sigue enganchado a la Ruta A** |
| B11 | **Medio ambiente y agua como política, no sólo como composición funcional** | CGPE y exposición de motivos del PPEF | **Parcial**: la exposición de motivos del PPEF **no se publica desde 2022** (servidor caído, no retirada). Si en 2027 sigue sin aparecer, el renglón nace limitado y se declara | El capítulo de 2026 es composición funcional |

### C. Renglones que dependen de una fuente que no estará en vivo

| # | qué falta | fuente que lo resolvería | ¿está en vivo? | decisión |
|---|---|---|---|---|
| C1 | **Series largas desde 2013** en las figuras sectoriales | Cuentas Públicas | **No**, y por decisión de alcance no se descargan | **Fuera de alcance, declarado.** Mitigación: los analíticos del **proyecto** están disponibles desde 2021 en `Analiticos_Historico/{t}/Proyecto/`, así que la línea P admite **seis puntos** sin tocar Cuenta Pública. Es la ampliación de serie más barata disponible |
| C2 | **Desigualdad pensionaria** | Distribución de montos por pensionado: memorias estadísticas institucionales y encuesta de ingresos y gastos | **No**: el paquete no la trae y las memorias no salen ese día | **Fuera de alcance**, con la razón escrita |
| C3 | **Gasto de bolsillo en salud** | Encuesta de ingresos y gastos de los hogares; cuentas en salud | **No** en la ventana; la encuesta es bienal y su vintage no coincide | Fuera de alcance, o **como referencia contextual fechada**, nunca como cifra del ejercicio |
| C4 | **Política tributaria en detalle**: Código Fiscal, facturación, RFC, aduanas, comercio electrónico, impuestos específicos | Iniciativa de miscelánea fiscal, en la Gaceta Parlamentaria el día de la entrega | **Sí, en vivo** ---la Gaceta publica el paquete completo el mismo día--- **pero es lectura jurídica de cientos de páginas** | **Decisión de alcance, no de fuente:** se hace la lectura de los cambios de tasa y base, y se declara que el detalle procedimental queda fuera . **Corrección de 2027, y es de fuente además de alcance:** las iniciativas fiscales de la cola llegan **escaneadas** ---capa de texto sólo en portada y colofón--- de modo que no son legibles por máquina y su lectura es manual o no es. Y la iniciativa que el índice anunciaba en la letra F, el Código Fiscal, **desapareció del índice sin haberse servido nunca**: lo que 2027 trajo fueron Derechos, ISR, Ley Aduanera, Ley de Economía Digital y Ley Catastral y Registral |
| C5 | **Inversión por sector con nombre de proyecto** | Cartera de inversión con denominación; los analíticos traen la clave sin nombre | **Parcial**: la clave sí, el nombre no | Se publican claves y montos, y **se declara que la denominación no está en la base** |
| C6 | **Incidencia distributiva completa** | Microdatos y modelo de incidencia | **No** | **Fuera de alcance por decisión de la instrucción** (§4) |
| C7 | **El espacio fiscal como cifra única** | Definición propia | n/a | **No se adopta.** Es un concepto que este proyecto no computa; lo que el género resume en una cifra, nuestro documento lo dice en tres capítulos. Se declara la diferencia de enfoque, no se copia la cifra |

### D. Estado al 12 de septiembre de 2026, tras la comparación con CIEP y la Ruta A

La comparación con CIEP (`documento_2027/comparacion_2027.md`) hizo el trabajo que esta
lista debía hacer en vivo, y **encontró omisiones que la lista no tenía como renglón**. Se
registran aquí; la tercera nota de actualización del documento las publica.

| # | renglón | estado |
|---|---|---|
| B1 | Vara externa de salud (6 % del PIB) | **Sigue fuera, cuarto ejercicio** contando 2025. CIEP la trae otra vez |
| B2 | Pronóstico externo del marco macro | **Sigue fuera.** CIEP cita FMI, Banco Mundial y la encuesta de Banxico |
| B3 | Pre-Criterios | **A medias en el cuerpo**: sólo macro. La meta fiscal de abril (RFSP 3,5 %) entra en la tercera nota |
| B5 | Mujeres como proporción del anexo de igualdad | **HECHO** (0,36 %, capítulo de anexos) |
| B10 | Pensiones en el anexo de igualdad | **HECHO** en la tercera nota: 57,2 % en 2027 contra 48,1 % en 2026 |
| C5 | Inversión por proyecto con nombre | **Tiene fuente**: la tabla «Prioridades de inversión» de la **p. 32 del CGPE** (total 560.172,6). El documento sólo cita el total |
| D1 | **Anexos que nombra el artículo 3 del decreto contra anexos extraídos** | **Nuevo.** El Anexo 32 no tiene encabezado ni total en el decreto y la extracción lo perdió |
| D2 | **Leer el CGPE completo antes de escribir «la fuente no lo publica»** | **Nuevo.** La p. 24 (metodología del gasto corriente estructural) y la p. 32 (inversión por proyecto, pensiones no contributivas) estaban en carpeta |
| D3 | **Antes de declarar Ruta B, buscar el prefijo vigente del árbol del PPEF en lo publicado** | **Nuevo.** Véase la adenda 2027 de `mapa_fuentes.md` |
| D4 | **Titulares cuyo signo depende del deflactor** | **Nuevo.** «Por persona de 65 y más, las pensiones caen 0,4 %» sube 0,3 % con 1,0325. Toda afirmación con variación real menor que la brecha entre deflactores (~0,8 pp) lleva línea de sensibilidad |
| D5 | **Ramos brutos que cuentan dos veces** | **Nuevo.** El Ramo 19 transfiere al IMSS y al ISSSTE; en un cuadro de ramos se advierte o se neta |

---

## Renglón que la lista aprendió a incluir sola

**Fondos y programas nuevos que no detectamos.** En 2026 se nos pasó el FAISPIAM ---fondo
nuevo de infraestructura social para pueblos indígenas y afromexicanos, presentado como
programa de Bienestar y no como aportación federal---. **No es un renglón temático: es una
salida del diff.** El diff de claves de `_herramientas/diff_claves.py` lista las altas; la
regla es **revisar la lista de altas completa antes de cerrar el capítulo de gasto**, y
nombrar en el documento toda alta que supere el umbral. Con eso este renglón deja de
depender de que alguien se acuerde.
