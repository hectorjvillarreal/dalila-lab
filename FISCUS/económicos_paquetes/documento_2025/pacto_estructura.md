# Pacto de estructura — documento propio ITED, Paquete Económico 2025

**Proyecto:** FISCUS · **Máquina:** Dalila · **Instrucción:** `INSTRUCCIONES_documento_propio_2025.md`
**Producto:** documento completo del género, autoría ITED, en Markdown y LaTeX compilable.

> ## SELLADO
>
> **Hora de sellado: 2026-09-06, 21:36:40 CST.**
>
> Escrito en fase 0, **sin red**, **sin abrir ninguna pieza del paquete 2025** y **sin abrir el documento de CIEP 2025**, que ya está en `2025/ciep_implicaciones2025.pdf` y no se toca hasta la fase 5.
>
> Fuentes usadas para escribirlo: `_aprendizaje/` completo (especificación del género con sus cuatro adendas, rúbrica con sus cuatro adendas, mapa de fuentes) y los artefactos de las cinco corridas de evaluación 2020–2024.
>
> Todo cambio posterior se registra en §8 con su motivo y su hora. Esa lista es información sobre el ejercicio, no un trámite.

---

## 1. Qué documento es este y qué no es

Es un documento del género *Implicaciones del Paquete Económico*, escrito por ITED sobre el Paquete Económico 2025. Sigue la arquitectura en tres partes sobre la restricción presupuestal, la plantilla de capítulo por rubro, el registro y la densidad de aparato del género.

**No es una evaluación de CIEP.** No cita a CIEP salvo donde una cifra provenga de ahí, y en ese caso con tier `derivada_ciep`, documento y página.

**No es anónimo.** Portada, autoría y filiación ITED. La procedencia tiene que ser inequívoca para un lector distraído, no solo para uno atento.

**Dónde se aparta del género, deliberadamente.** Cuatro lugares, y los cuatro son la aportación propia:

1. **Nota de método al frente.** El género no la tiene. Declara perímetros, deflactor, las cinco declaraciones del contrafactual y el vocabulario de tier antes del primer capítulo.
2. **Capítulo de balance y deuda con descomposición de cuatro variables.** El género trata la deuda descriptivamente. La descomposición del cambio de la razón SHRFSPF/PIB en crecimiento, tasa real, inflación y tipo de cambio no existe en él.
3. **Capítulo de horizonte demográfico.** Cierra el documento con la tríada de NTA y su asimetría.
4. **Declaración de nominal o real en toda diferencia expresada en millones de pesos.** El género no lo hace y en 2024 eso produjo una afirmación falsa sobre una cifra aprobada por la Cámara.

---

## 2. Índice de capítulos

Trece capítulos más frente y cierre. La numeración de parte va en el título, como en el género.

| # | capítulo | parte |
|---|---|---|
| — | Portada, autoría y **nota de método** | frente |
| — | Resumen ejecutivo | frente |
| 1 | Marco macroeconómico | frente |
| 2 | Ingresos presupuestarios | **(+) Ingresos** |
| 3 | Ingresos energéticos | (+) Ingresos |
| 4 | Gasto público: los agregados | **(−) Gasto** |
| 5 | Pensiones | (−) Gasto |
| 6 | Salud | (−) Gasto |
| 7 | Educación | (−) Gasto |
| 8 | Inversión | (−) Gasto |
| 9 | Energía | (−) Gasto |
| 10 | Seguridad | (−) Gasto |
| 11 | Gasto federalizado | (−) Gasto |
| 12 | Balance, deuda y sostenibilidad | **(=) Balance y deuda** |
| 13 | Horizonte demográfico | cierre |
| — | Implicaciones de política pública | cierre |
| — | Anexo metodológico, acrónimos, bibliografía | cierre |

**Extensión objetivo:** 70 a 90 páginas. Capítulos de rubro de 4 a 7 páginas; el 4 y el 12, de 8 a 10.

**Orden de partes.** Se adopta el de 2020, 2022 y 2024 —(+), (−), (=)— y no el de 2021, que puso la deuda al frente. Razón: la identidad presupuestal se lee en ese orden y el capítulo 12 necesita los agregados del 2, el 3 y el 4 ya establecidos.

**Riesgo declarado de antemano.** Los capítulos con más probabilidad de no alcanzar el presupuesto de afirmaciones (§4) son, en este orden: **9 Energía**, **10 Seguridad** y **3 Ingresos energéticos**. Los tres dependen de piezas que en 2022–2026 no se han obtenido: las estrategias programáticas por ramo y la exposición de motivos del PPEF. Si alguno cae, se publica su declaración de no redactable. **Se dice ahora para que la caída no se lea después como una decisión de conveniencia.**

---

## 3. Qué pregunta responde cada capítulo

Cada capítulo responde estas preguntas y solo estas. Si una pregunta no se puede responder con fuente, se dice en el capítulo.

**1. Marco macroeconómico.** ¿Qué supone la SHCP para 2025 en crecimiento, inflación, tasa, tipo de cambio y petróleo? ¿Cómo se compara con el potencial declarado y con las expectativas privadas? ¿Qué sensibilidades publica el paquete y a qué son sensibles las cifras del resto del documento? ¿Cuál es el PIB nominal y de qué año base, y qué se reexpresó?

**2. Ingresos presupuestarios.** ¿Cuánto se propone recaudar, por renglón del artículo 1o.? ¿Contra qué base cambia y en cuánto, en términos reales? ¿Hubo miscelánea fiscal y qué cifra tiene? ¿Qué elasticidad implícita hay entre el crecimiento supuesto y la recaudación proyectada? ¿Qué parte del gasto se financia con deuda?

**3. Ingresos energéticos.** ¿Cuánto aporta el sector energético y por qué vía? ¿Qué suponen el precio, la plataforma y el tipo de cambio? ¿Cuál es la tasa del derecho por la utilidad compartida y cómo llegó ahí? ¿Cuánto transfiere el Fondo Mexicano del Petróleo y cuánto es ingreso propio de las empresas?

**4. Gasto público: los agregados.** ¿Cuánto se propone gastar, por las tres clasificaciones? ¿Qué ramos ganan y pierden en términos reales? ¿Qué parte del gasto está comprometida y bajo qué definición? ¿Qué reclasificaciones institucionales hay entre 2024 y 2025 y qué caídas contables producen que no son presupuestales?

**5. Pensiones.** ¿Cuánto cuestan y por institución? ¿Qué parte es contributiva y qué parte no? ¿Cuánto aporta el Gobierno Federal al régimen en curso de pago? ¿Cuál es la relación entre pensiones y cuotas del IMSS? ¿Qué horizonte declara el paquete?

**6. Salud.** ¿Cuánto se destina, por subsistema, separando contributivo de no contributivo? ¿Qué pasó con IMSS-Bienestar tras su reasignación de ramo? ¿Cuánto por afiliado en cada subsistema y con qué denominador? ¿Las cuotas cubren la salud del IMSS?

**7. Educación.** ¿Cuánto, por función y por ramo, separando federal de federalizado? ¿Cómo se distribuye el FONE por entidad y cambió la fórmula? ¿Qué hacen las becas y dónde viven? ¿Declara el paquete un supuesto de matrícula?

**8. Inversión.** ¿Cuánta inversión física y cuánto gasto de inversión, que son cosas distintas? ¿Qué proporción es obra pública directa y qué proporción es transferencia? ¿Qué proyectos concentran el gasto?

**9. Energía (gasto).** ¿Cuánto reciben Pemex y CFE y por qué vía: aportación patrimonial, subsidio o ingreso propio? ¿Cuánto es inversión y cuánto es servicio de deuda? ¿Cuánto cuesta el subsidio eléctrico?

**10. Seguridad.** ¿Cuánto se destina al perímetro de quince subfunciones? ¿Cómo se reparte entre civil y militar? ¿Qué obra pública no militar ejecutan las fuerzas armadas?

**11. Gasto federalizado.** ¿Cuánto se transfiere y por qué vía: participaciones, aportaciones, convenios? ¿Cómo queda por entidad y por habitante? ¿Qué pasa con el fondo de estabilización de los ingresos de las entidades federativas?

**12. Balance, deuda y sostenibilidad.** ¿Cuáles son los tres flujos y los tres acervos, con nombre correcto? ¿Qué techos autoriza la iniciativa de ingresos y en qué se distinguen del déficit? ¿Cierra la identidad flujo–acervo? ¿Qué explica el cambio de la razón SHRFSPF/PIB, repartido en cuatro variables? ¿Qué regla de excepción se invocó?

**13. Horizonte demográfico.** ¿Dónde declara el paquete un supuesto demográfico y dónde no? ¿Cómo se ven los tres vértices de la tríada de NTA juntos? ¿Qué le pasa a cada uno bajo la transición y qué de eso está en el paquete?

---

## 4. Presupuesto de afirmaciones

**Umbral por capítulo:** al menos **12 afirmaciones cuantitativas verificables**, de las cuales al menos **6 sean restitución de fuente oficial primaria**, y no más del **30 %** del total del capítulo en `no_verificable`.

Se declara **antes** de redactar cada capítulo, en `documento_2025/presupuesto_afirmaciones.md`, con una fila por capítulo: contadas, restituciones, derivaciones, juicios, no verificables, y veredicto redactable o no redactable.

**Si un capítulo no llega, se escribe su declaración de no redactable** y esa declaración se compila como una página del documento, en el registro del documento y no como nota técnica: qué se quiso decir, qué fuente exacta haría falta, por qué no está, y qué respondería si estuviera. Nueve capítulos y tres declaraciones es un resultado; doce capítulos con cuatro de relleno es un fracaso que además no se ve.

**La fluidez de la prosa no es evidencia de verificación.** El presupuesto se cuenta sobre el borrador terminado, no sobre la intención.

---

## 5. Comparaciones estructurales: cuál va en qué capítulo

Son lo que hace que el documento sea de ITED. Todas con perímetro declarado, base consistente y las dos líneas donde aplique. **Nunca una línea híbrida:** ex ante con ex ante, aprobado con aprobado.

| cap. | comparación | serie conocida | estado |
|---|---|---|---|
| 2 | Tributarios / gastos obligatorios (con y sin cuotas IMSS) | 0.671 (2021), 0.674 (2022); con cuotas 0.743, 0.745 | extender a 2023–2025 |
| 4 | Pensiones + costo financiero / tributarios | 0.60 (2023) **no reproducible** | **reconstruir antes de usar** |
| 5 | Pensiones IMSS / cuotas IMSS, serie aprobada | 1.545 (2022), 1.594 (2023), 1.627 (2024) | extender a 2025 |
| 5 | Pensiones IMSS / cuotas IMSS, serie ex ante | 1.31 (2020), 1.46 (2021) | **congelada**, la EM del PPEF no existe desde 2022 |
| 6 | Cuotas obrero-patronales / gasto en salud del IMSS | 0.85 (2021) | extender |
| 6 | Pensiones IMSS+ISSSTE / salud IMSS+ISSSTE | 2.11 (2021) | extender |
| 7 | Educación / pensiones y jubilaciones, clasificación económica | 0.709 (2023), 0.689 (2024) | extender |
| 7 | segunda línea: educación / pensiones totales | 0.558, 0.518 | extender |
| 12 | Costo financiero / tributarios | 0.20 (2022), 0.23 (2023), 0.256 (2024) | extender |
| 12 | SHRFSPF / tributarios, en años de ingreso | 3.6 (2022), 3.4 (2023), 3.40 (2024) | extender |

**Advertencia sellada sobre la razón del capítulo 4.** El punto de 0.60 para 2023 **no se reproduce con ninguna de las dos definiciones de pensiones**: con el perímetro amplio da 0.583 y con la clasificación económica 0.522. Se detectó en la corrida 2024 y está en su bitácora. **Antes de extender esa serie hay que reconstruir de dónde salió el 0.60.** Si no se reconstruye, la serie arranca en 2024 con su definición declarada y el punto de 2023 se retira con nota. No se publica una serie cuya base no cierra.

**Congeladas y no citables como trayectoria:** el pasivo pensionario y el supuesto oficial de crecimiento real de pensiones. Razones, ya establecidas: el CGPE 2023 compara explícitamente entre añadas, el PIB implícito de 2022 no coincide con ninguna base publicada, y el componente del ISSSTE cambia de método en el CGPE 2024. Se pueden mencionar con sus tres campos; no se pueden encadenar.

---

## 6. Cuadros y figuras previstos, con el dato que cada uno necesita

Nomenclatura: `C` cuadro, `F` figura. Cada uno se genera desde un `.csv` de `datos/` con su fila en `_fuentes.csv`. **Ninguna cifra se teclea en el cuerpo del texto; ninguna figura es una imagen pegada.** Las figuras se hacen con `pgfplots` leyendo el mismo `.csv` que alimenta el cuadro.

### Frente y capítulo 1

| id | contenido | dato que necesita | archivo |
|---|---|---|---|
| C1.1 | Marco macro: 2024 aprobado, 2024 estimado, 2025, con las cinco variables | CGPE 2025, cuadro de marco macro y de finanzas públicas | `macro_marco.csv` |
| C1.2 | Mediano plazo 2026–2030: PIB, RFSPF, balance, primario, costo financiero, programable | CGPE 2025, cuadros de proyección | `macro_medianoplazo.csv` |
| C1.3 | Sensibilidades: 0.5 pp de PIB, 1 dpb, 20 centavos de tipo de cambio, 50 mbd, 100 pb | CGPE 2025, cuadro de sensibilidades | `macro_sensibilidades.csv` |
| F1.1 | Crecimiento supuesto contra potencial declarado, 2019–2025 | C1.1 más los CGPE previos ya en carpeta | `macro_crecimiento.csv` |

### Parte I — capítulos 2 y 3

| id | contenido | dato que necesita | archivo |
|---|---|---|---|
| C2.1 | Ingresos por renglón del art. 1o.: LIF 2024, ILIF 2025, % PIB de cada año, variación real | ILIF 2025 art. 1o.; LIF 2024 aprobada; PIB de C1.1 | `ingresos_art1o.csv` |
| C2.2 | Reconciliación ILIF ↔ CGPE por renglón, con el residuo nombrado | ILIF 2025 art. 1o.; CGPE 2025 cuadro de ingresos | `ingresos_reconciliacion.csv` |
| C2.3 | Medidas de ingreso con cifra, y lista de las que no la tienen | ILIF 2025 exposición de motivos; miscelánea si existe | `ingresos_medidas.csv` |
| F2.1 | Serie de ingresos presupuestarios en % del PIB | CGPE 2025, anexo de series | `ingresos_serie.csv` |
| F2.2 | Composición: tributarios, petroleros, no tributarios, organismos | C2.1 | reusa `ingresos_art1o.csv` |
| C2.4 | Elasticidad implícita: crecimiento supuesto contra variación real de tributarios | C1.1 y C2.1 | derivado, sin archivo propio |
| C3.1 | Ingresos energéticos por vía: FMP, ingreso propio de Pemex, ingreso propio de CFE, ISR de contratistas | ILIF 2025 art. 1o.; CGPE 2025 | `energia_ingresos.csv` |
| C3.2 | Precio, plataforma y tipo de cambio supuestos, contra 2024 | C1.1 | reusa `macro_marco.csv` |
| — | Trayectoria del derecho por la utilidad compartida | CGPE 2025; DOF para las reformas | texto con fuente, `derecho_utilidad.csv` si hay serie |

### Parte II — capítulo 4 y rubros

| id | contenido | dato que necesita | archivo |
|---|---|---|---|
| C4.1 | Gasto neto, programable, no programable, costo financiero, participaciones: PEF 2024, PPEF 2025, variación real, % PIB | CGPE 2025 cuadro de gasto; DEC 2025 art. 2 | `gasto_agregados.csv` |
| C4.2 | Por ramo: PEF 2024, PPEF 2025, diferencia, variación real | DEC 2025 Anexo 1; DEC 2024 Anexo 1 | `gasto_ramos.csv` |
| C4.3 | Clasificación económica: corriente, pensiones, inversión, y capítulos de gasto | analíticos 2024 y 2025, columna TG y primer dígito de PE | `gasto_economica.csv` |
| C4.4 | Clasificación funcional por finalidad y función | analíticos por función, 2024 y 2025 | `gasto_funcional.csv` |
| C4.5 | Gastos obligatorios con y sin pensiones | DEC 2025 Anexo 3 | `gasto_obligatorios.csv` |
| F4.1 | Gasto neto y programable en % del PIB, serie | CGPE 2025 anexo de series | `gasto_serie.csv` |
| C4.6 | **Diffs 2024 → 2025:** ramos, programas, unidades responsables y subfunciones que aparecen, desaparecen o cambian de código | analíticos 2024 y 2025 | `diffs_2024_2025.csv` |
| C5.1 | Pensiones por institución y por tipo de gasto 4 | analíticos GF y entidades, TG 4 | `pensiones_institucion.csv` |
| C5.2 | Contributivas contra no contributivas, con los programas de pensión no contributiva nombrados | analíticos por programa; DEC Anexo de programas | `pensiones_contrib.csv` |
| C5.3 | Aportación del Gobierno Federal al régimen en curso de pago | DEC 2025, artículo correspondiente; serie desde 2020 | `pensiones_aportacion.csv` |
| F5.1 | Pensiones IMSS / cuotas IMSS, serie aprobada | `pensiones_institucion.csv` y LIF aprobada | `ratio_pensiones_cuotas.csv` |
| C6.1 | Salud por subsistema en dos bloques, contributivo y no contributivo | analíticos por función Salud, GF y entidades | `salud_subsistema.csv` |
| C6.2 | Gasto por afiliado por subsistema, **con el denominador declarado y su fuente** | C6.1 más población afiliada; si no hay fuente, se declara el hueco | `salud_percapita.csv` |
| F6.1 | Cuotas obrero-patronales contra gasto en salud del IMSS, serie | LIF y analíticos de entidades | `ratio_cuotas_salud.csv` |
| C7.1 | Función Educación por ramo, separando federal de federalizado | analítico por función, 2024 y 2025 | `educacion_ramo.csv` |
| C7.2 | Por subfunción, los seis niveles | mismo analítico | `educacion_subfuncion.csv` |
| C7.3 | FONE por entidad federativa, con participación y variación real | analítico GF, columna EF; DEC Anexo del FONE | `fone_entidad.csv` |
| C7.4 | Becas por programa y por ramo | analítico por programa | `becas.csv` |
| C8.1 | Inversión física contra gasto de inversión, con la diferencia explicada | CGPE 2025; analíticos capítulos 6000 y 7000 | `inversion_agregados.csv` |
| C8.2 | Obra pública directa por ramo | analíticos, capítulo 6000 | `inversion_ramo.csv` |
| C9.1 | Pemex y CFE: aportación patrimonial, ingreso propio, inversión, costo financiero | DEC Anexo 1 ramo 18; analíticos de entidades; ILIF art. 1o. | `energia_gasto.csv` |
| C9.2 | Subsidio eléctrico | DEC 2025; CGPE 2025 | `subsidio_electrico.csv` |
| C10.1 | Perímetro de seguridad: quince subfunciones de cinco funciones | analítico por función, 2024 y 2025 | `seguridad_subfuncion.csv` |
| C10.2 | Civil contra militar, y obra pública no militar ejecutada por las fuerzas armadas | analíticos por ramo, UR y capítulo 6000 | `seguridad_civil_militar.csv` |
| C11.1 | Gasto federalizado por vía: participaciones, aportaciones, convenios | CGPE 2025; DEC Anexos 1 y del ramo 33 | `federalizado_via.csv` |
| C11.2 | Por entidad federativa y por habitante, **con la población declarada y su fuente** | analíticos columna EF; CONAPO si se obtiene, si no se declara el hueco | `federalizado_entidad.csv` |

### Parte III — capítulo 12

| id | contenido | dato que necesita | archivo |
|---|---|---|---|
| C12.1 | Los tres flujos: balance presupuestario, balance público, RFSPF, en mdp y % PIB | CGPE 2025 | `flujos.csv` |
| C12.2 | Los tres acervos: SHRFSPF, deuda neta del sector público federal, deuda bruta del no financiero | CGPE 2025 | `acervos.csv` |
| C12.3 | Techos de endeudamiento por entidad, y su distinción del déficit y del endeudamiento informativo | ILIF 2025 arts. 1o. a 3o. | `techos.csv` |
| C12.4 | **Descomposición de cuatro variables** del cambio de SHRFSPF/PIB | C12.1, C12.2 y C1.1 | `descomposicion.csv` |
| C12.5 | Costo financiero por ramo y entidad | DEC Anexo 1 ramos 24 y 34; analíticos de entidades | `costo_financiero.csv` |
| F12.1 | SHRFSPF en % del PIB, serie y horizonte | CGPE 2025 | `deuda_serie.csv` |

### Capítulo 13

| id | contenido | dato que necesita | archivo |
|---|---|---|---|
| C13.1 | La tríada de NTA: pensiones, salud, educación con su perfil de edad, su dirección demográfica, dónde vive el gasto y qué denominador le corresponde | C5.1, C6.1, C7.1 | `triada_nta.csv` |
| C13.2 | Dónde declara el paquete un supuesto demográfico y dónde no, pieza por pieza | CGPE, ILIF y DEC 2025, búsqueda exhaustiva | `supuestos_demograficos.csv` |

**Total previsto: 38 cuadros y 8 figuras.** Densidad comparable a la del género, que trae entre 30 y 45 cuadros en 90 páginas.

---

## 7. Convenciones que rigen todo el documento

Se declaran en la nota de método del frente y se cumplen en todos los capítulos.

1. **Nomenclatura.** RFSPF y SHRFSPF, con la equivalencia RFSP y SHRFSP declarada una vez.
2. **Deflactor.** El del PIB que declara el CGPE 2025. **Nunca derivado de agregados publicados redondeados.** Excepción marcada para prestaciones individuales, que usan el índice de precios al consumidor, señalada en el lugar y nunca los dos en un mismo cuadro.
3. **Las cinco declaraciones del contrafactual**, en toda comparación: nominal o real; contra aprobado o contra cierre; contra año previo o contra PIB; en pesos de qué año; y con qué PIB de qué añada.
4. **Ex ante contra ex ante.** Aprobado contra aprobado. Nunca una serie con bases mezcladas.
5. **Perímetro declarado antes del primer cuadro de cada capítulo y constante dentro del capítulo.** Si cambia entre cuadros, es error, aunque cada cuadro sea internamente correcto.
6. **Umbrales.** 0.5 % en niveles, 0.1 pp en tasas y razones.
7. **Prohibición de yuxtaponer magnitudes sin mecanismo declarado.**
8. **Definiciones adjudicadas contra *Balance Fiscal en México* (SHCP, abril 2023)**, que está en `_metodologia/`. Nunca por criterio propio.
9. **Regla propia que este documento estrena: toda diferencia expresada en millones de pesos declara si es nominal o real.**
10. **Tier en toda cifra:** `oficial_primaria`, `derivada_ciep`, `autoral_ited`. Registrado en `_fuentes.csv`, no en el cuerpo del texto.
11. **No se presenta el marco de manual** de sostenibilidad, primario más r menos g. Retirado por sesgo sistemático; el diagnóstico va en bitácora, nunca en el documento.
12. **Donde no se pueda verificar, se dice en el documento**, no solo en la bitácora.

### Decisión de perímetro que hay que tomar ahora, no después

**El perímetro canónico de salud está definido sobre una fuente que no existe para 2025.** La convención fijada en 2022 lo ancla al cuadro «Gasto en salud: dependencias, entidades y ramos generales» de la exposición de motivos del PPEF, y esa exposición está caída en el servidor para 2022–2026.

**Decisión sellada:** el perímetro de salud se reconstruye desde los analíticos por función, respetando las siete líneas y los dos bloques etiquetados —contributivo con IMSS, ISSSTE, Sedena y Semar; no contributivo con el ramo 12 completo, IMSS-Bienestar y el fondo de aportaciones para los servicios de salud— con los servicios médicos de Pemex fuera, como partida informativa. **La sustitución de fuente se declara en el capítulo**, porque cambia el objeto: los analíticos son brutos y el cuadro de la exposición de motivos es neto.

**Advertencia adicional para el capítulo 6:** IMSS-Bienestar cambió de ramo en 2024, del 12 al 47. Si en 2025 vuelve a moverse, la caída o el salto del ramo 12 es contable y no presupuestal. Se anticipa, no se descubre.

---

## 8. Cambios al pacto

Cada cambio lleva hora, qué cambia y por qué. Esta lista es un resultado del ejercicio.

**2026-09-06, 21:50 · Precisión, no cambio de estructura.** El pacto declaró «aprobado contra aprobado» como convención (§7.4) pero no dijo cuál es el objeto primario del documento. Se fija: **las cifras de gasto son del PEF aprobado 2025 contra el PEF aprobado 2024**, y donde el CGPE o el decreto son la única fuente se usa el proyecto y se dice. Motivo: los analíticos del proyecto no existen para 2022–2026 y los del aprobado sí; CIEP escribe sobre el proyecto porque publica en 72 horas, nosotros escribimos un año después y no tenemos esa restricción. La asimetría se declara en la nota de método.

**2026-09-06, 21:44 · El CGPE 2025 no tiene capa de texto.** 90 de sus 91 páginas son imagen; la única con texto es la 34, y son las fórmulas del PIB potencial. Se comprobó que el portal no sirve otra edición: la ruta canónica devuelve el mismo archivo de 22,852,266 bytes. **Consecuencia de método:** todas las cifras del CGPE se leen de páginas renderizadas a 150 dpi, queda declarado en `_fuentes.csv` y en la nota de método, y se validan por identidad contable en vez de por relectura. Las 45 primeras pruebas cierran. No es un cambio de estructura pero sí de proveniencia, y por eso se registra.

**2026-09-06, 21:56 · Advertencia anticipada para los capítulos 6 y 10.** Los dos rubros traen reclasificaciones grandes entre 2024 y 2025 que producen caídas contables: en salud, el Ramo 19 pasa 64.3 mmp de la función Salud a Protección Social sin que el ramo pierda tamaño, y el FASSA cae 54.4 mmp nominales; en seguridad, el Ramo 36 cae 35.4 mmp nominales. **Ninguna de las dos se escribe como recorte hasta que el diff la explique.** Queda anotado antes de redactar, que es donde debe quedar.
