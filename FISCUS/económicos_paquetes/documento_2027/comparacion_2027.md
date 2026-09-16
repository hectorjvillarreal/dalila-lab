# Comparación contra *Implicaciones del Paquete Económico 2027* (CIEP)

**Objeto comparado:** el documento propio del ITED (`documento_2027/`, cuerpo del 8 de septiembre
de 2026 más las notas de actualización del 9 y el 10) contra *Implicaciones del Paquete Económico
2027*, CIEP, 125 páginas, fechado el 11 de septiembre de 2026 (`2027/PE2027-v1.pdf`).
**Hecha:** 2026-09-12. Cifras de CIEP citadas como las publica; cifras propias, con la
puntuación del documento.

## Control del ejercicio

| Hito | Fecha y hora |
|---|---|
| Cuerpo del documento propio redactado | 8 sep., 18:45–21:00 |
| Última compilación del PDF propio (con la segunda nota) | 10 sep., 22:11 CST |
| Creación del PDF de CIEP (metadatos) | 11 sep., 02:18 CST |
| PDF de CIEP en la carpeta `2027/` | 12 sep., 22:49 |

**Ninguna cifra ni frase del documento propio pudo venir del de CIEP**: el nuestro se cerró antes
de que el suyo existiera. La comparación es, por primera vez, *ex post* de verdad: la corrida en
vivo no tuvo comparador, y éste es el que habría tenido.

**Nota de calendario.** CIEP publicó a los tres días de la entrega (en 2026 fueron nueve).

---

## 1. Coincidencias por caminos independientes

| | ITED | CIEP |
|---|---|---|
| Ingresos presupuestarios | 9.156.528,9 mdp · 23,2 % PIB | 9 billones 156 mil 529 · 23.2 % |
| Tributarios | 6.263.886,8 · 15,9 % | 6 billones 263 mil 886.8 · 15.9 % |
| Petroleros, % PIB | 3,1 → 2,5 | 3.1 → 2.5 |
| Transferencias del FMP, real | −12,9 % | −12.9 % |
| IEPS combustibles | 538.549,2 | 538 mil 549.2 |
| Recaudación federal participable | 5.722.752 | 5 billones 722 mil 752 |
| RFSP · SHRFSP | 3,9 % · 55,0 % | 3.9 % · 55.0 % |
| **Pensiones contributivas** | **1.840.746,1** (Anexo 3, por diferencia) | **1,840,746** |
| Programa «Articulación de la Política de Hidrocarburos» | 81.100,0 (prosa del CGPE) | 81 mil 103 (por programa) |
| Inversión total · física · financiera | 1.133,6 · 1.026,5 · 92,3 mmp | 1,133,613.2 · 1,026,474.4 · 92,271.8 mdp |
| Contratos LFIIEDB: terceros · diferidos | 188,9 · 273,5 mmp | 188.9 · 273.5 |
| Anexo 13 · Anexo 31 · Anexo 33 | 636.133,1 · 475.959,7 · 43.369,4 | idénticos |
| Anexo 16 · Anexo 15, real | −27,6 % · +9,2 % | −27.6 % · +9.2 % |
| Programas E089/U013/U014 del Anexo 34 | 64.010,9 + 15.673,7 + 12.033,0 | mismos tres renglones |
| Pérdidas fiscales, plazo | **veinte** años (adjudicado contra la iniciativa de ISR) | de 10 a **20** años |

**La validación cruzada real son dos.** Las pensiones contributivas: CIEP publica exactamente el
perímetro que nosotros adjudicamos con el Anexo 3, y su columna 2026 (1,758,692 «mdp de 2027») es
nuestro 1.704.159,2 multiplicado por 1,0320 al peso. Y la explicación de la caída del Ramo 18: los
dos documentos la atribuyen al mismo programa. Nosotros llegamos por la prosa del CGPE comprobada
contra el Anexo 1; ellos, por el analítico, al millón.

**Coincidencias cualitativas:** los anexos transversales no son recursos adicionales (los dos lo
dicen de los nuevos); la caída de la inversión es financiera y no física; el marco
macroeconómico se revisó a la baja respecto de los Pre-Criterios.

---

## 2. Lo que CIEP tiene y nosotros no

### 2.1 Todo el nivel de programa, y dónde estaba · **el hallazgo mayor**

CIEP publica gasto en salud por subsistema y por programa (Cuadro 11), pensiones por institución
(IMSS, ISSSTE, CFE, Pemex, Gobierno Federal), educación por subfunción y por programa, la
composición programa por programa de los anexos 13, 31, 32 y 33, y aportaciones del Ramo 33 por
entidad y por habitante. **Todo eso es lo que nuestro documento declaró imposible en «Ruta B»**.

**Dónde estaba.** CIEP cita un árbol que nuestro mapa de fuentes no conoce:
`www.ppef.hacienda.gob.mx/work/models/PP3F2709/PPEF2027/yik327fP/`. Verificado hoy, 12 de
septiembre, con el bundle TLS de `_herramientas/_certs/bundle.pem`:

| Ruta bajo el árbol nuevo | Respuesta | Last-Modified del servidor |
|---|---|---|
| `docs/carta/Carta.pdf` | 200 PDF, 368.530 B | **8 sep. 08:58 GMT** |
| `docs/exposicion/EM_Documento_Completo.pdf`, `EM_Capitulo_1.pdf` | 206 PDF | — |
| `analiticosPresupuestarios/ac01_ra_pp_ur_og.xlsx` | 206 xlsx | — |
| `analiticosPresupuestarios/ac01_ra_f_ur_og.xlsx` | 200 xlsx, 5,6 MB | **11 sep. 20:55 GMT** |
| `analiticosPresupuestarios/ac01_ra_{pp,f}_ur_og_efe.xlsx` | 200 xlsx, 2,8 y 2,5 MB | 11 sep. 20:55 GMT |
| `analiticosPresupuestarios/Proyecto/…` (con el segmento) | **404** | — |

**Lo que esto corrige, con precisión:**

- **La exposición de motivos no «da 404 por sexto ejercicio».** La Carta existe desde la mañana del
  día de la entrega bajo el prefijo nuevo. Nuestros once 404 eran de la ruta vieja. El renglón del
  registro que lo atribuye al servidor es falso para 2027.
- **Los analíticos: el diagnóstico «el árbol no existe» fue de ruta, no de fuente.** El árbol vive
  con otro prefijo y sin `/Proyecto/`. Según la fecha que declara el servidor, los xlsx son del 11
  de septiembre por la tarde, **después** de nuestra tercera sonda (10 sep., 21:52) y también
  **después** de la creación del PDF de CIEP. Así que, o CIEP tuvo el analítico por otra vía, o el
  servidor volvió a subir los archivos y el Last-Modified no es la fecha de primera publicación.
  **No se adjudica.** Lo seguro es que el 12 de septiembre la Ruta A está abierta.
- Nada se descargó. Las sondas pidieron un byte o sólo encabezados.

### 2.2 El Anexo 32, «Acciones para la Movilidad y Seguridad Vial» · omisión propia, con causa de procedimiento

CIEP lo destaca desde la presentación: 175 mil 045.5 mdp, 82.1 % en Infraestructura, 66.8 % en un
solo programa ferroviario. **Nuestro documento no lo menciona**, y su capítulo de anexos dice
«aparece un anexo nuevo, el 33».

**El anexo está en nuestra copia del decreto**: páginas 242–244 del PDF, entre el 31 y el 33, y el
artículo 3 lo nombra. Pero la página 242 **empieza a media tabla**, con un subtotal de ramo
(13.819.913 pesos), sin el encabezado «ANEXO 32», sin el renglón «Total general» y sin la primera
línea de objetivo. La paginación impresa corre sin salto de la 241 a la 242. Nuestra extracción
reconocía cada anexo por su encabezado y su «Total general», y éste no tiene ninguno de los dos.

**No verificado:** si el encabezado falta en el decreto de la Secretaría o sólo en nuestra copia,
que pasó por PDF24 (anomalía de procedencia ya registrada). La comparación de sha256 contra el
portal sigue pendiente. **Tampoco se verificó el total de 175.045,5 mdp.**

**Falla de compuerta, además:** «aparece *un* anexo nuevo» es un sujeto más estrecho que la fuente,
y el artículo 3 del mismo decreto nombra los dos.

### 2.3 La inversión por proyecto · omisión propia, estaba en el CGPE

CIEP publica Pemex 255,529.2, Nuevos Trenes 150,875.6 (con nueve tramos), CFE 60,991.6 y
un total de 560,172.6 mdp. **Es la tabla «Prioridades de inversión» de la página 32 del CGPE 2027**,
en carpeta desde el día 8. Nuestro capítulo de inversión escribió que esa composición «exige el
analítico del proyecto y la cartera de inversión, ninguno de los dos disponible». **Falso: estaba
en el documento que citamos en ese mismo capítulo.**

### 2.4 Las pensiones no contributivas por programa · omisión propia, en la misma página

La tabla gemela de la página 32, «Programas sociales prioritarios», publica: Pensión Adultos
Mayores 543.498,4; Mujeres Bienestar 59.356,3; Personas con Discapacidad 37.436,3. Nuestro
capítulo de pensiones dijo que la parte no contributiva «se puede acotar con el Ramo 20, pero no
separar». **Con esa tabla, el perímetro de CIEP se reproduce al décimo:**

$$1.840.746,1 + (543.498,4 + 59.356,3 + 37.436,3) = 2.481.037,1 = 6,29\ \%\ \text{del PIB}$$

CIEP publica 2,481,037 y 6.3 %. Es la misma construcción que adjudicamos en 2026, y este año la
podíamos hacer nosotros.

### 2.5 La meta fiscal de los Pre-Criterios · omisión propia

CIEP: los Pre-Criterios de abril fijaban **RFSP de 3,5 % para 2027**, y el CGPE los deja en 3,9;
«hace un año se estimaba [bajar de 3 %] en 2028 y, hace dos, en 2027». Nuestro cuadro C1.2 comparó
abril contra septiembre **sólo en variables macro**. La tabla fiscal de los Pre-Criterios estaba en
carpeta: RFSP −3,5 % del PIB y SHRFSP de 21.848.685,1 mdp (55,0 %).

### 2.6 Varas externas, otra vez

- **Salud: el 6 % del PIB de la OPS/OMS** contra 2.9 %. Es el renglón B1 de la checklist. Nuestro
  documento dice que queda fuera «por tercer ejercicio consecutivo»; con 2025 es el cuarto.
- **Inversión: 4–6 % del PIB** (CEPAL, FMI, BID, Banco Mundial) contra 2.9 %.
- **Recaudación: OCDE 18.3 % contra 34.1 %**; América Latina 17.7 contra 21.3.
- **Crecimiento: FMI 1.9, Banco Mundial 1.7, encuesta de Banxico 1.8.** Nosotros lo declaramos
  fuera «por decisión de alcance». Es la misma omisión que la comparación de 2026 señaló en §2.4.

### 2.7 El espacio fiscal, cuantificado

1.6 % del PIB (1.7 en 2026). Segundo año que lo publican y que no lo computamos. Tampoco publican
cómo lo construyen.

### 2.8 Detalle que nuestro perímetro dejó fuera

- **La estimación de la Miscelánea:** rango de la SHCP de 130–140 mil mdp (0.33–0.36 % del PIB),
  una estimación propia de 135,344 y el costo de las renuncias recaudatorias (0.12 % del PIB).
  Nosotros escribimos que el rendimiento por medida no se publica. **No verificado:** la cifra de
  la SHCP no apareció en la búsqueda de texto del anexo E ni del CGPE.
- **El balance de Pemex y CFE, con y sin apoyos:** 14 y −65 mmdp sin apoyos. Nosotros lo dejamos
  fuera por decisión.
- **La inflación específica de salud:** el crecimiento real pasa de 11.7 a 9.7 %. **La pensión
  promedio por institución:** CFE es 60 veces la Pensión Mujeres Bienestar.
- **La Carta:** 124 mil 788.6 mdp para medicamentos. La Carta existía; véase §2.1.
- **Política nacional de mares y costas:** de 42,854 a 128,901 mdp, casi todo reetiquetado de
  educación media superior.
- **La explicación de la caída del Anexo 16:** «casi por completo por el cierre de la inversión
  del Tren Maya». Responde nuestra pregunta abierta, pero **no se verificó**: la caída del Tren
  Maya en su Cuadro 13 (−13,8 mmp) no alcanza a explicar los −52,4 mmp del anexo sin la lista por
  programa.

---

## 3. Lo que nosotros tenemos y CIEP no

### 3.1 La regla fiscal y su perímetro · cero tratamiento en CIEP

CIEP no menciona la desaparición de la cláusula de exclusión del artículo 1o. Tampoco la reforma
de abril a la LFPRH (sólo la cita en sus referencias), la ruptura de serie del gasto corriente
estructural (−51,3 % nominal, límite de 10,9 a 5,2 % del PIB) ni que el balance sin inversión no
se publica. Verificado por búsqueda: «sin inversión», 0; «estructural», 2, las dos en otro sentido.
Menciona la LFIIEDB sólo como cuadro de contratos. **Es el capítulo nuevo de 2027 y la aportación
más distinta del documento propio.**

### 3.2 El deflactor de la fuente oficial

Nosotros documentamos que el CGPE declara un deflactor del PIB de 4,04 % y calcula sus cuadros con
1,0325. **CIEP no lo menciona («deflact», una sola aparición, en salud) y usa en casi todo el
documento el mismo 1,032 del CGPE**. Véase §4.1.

### 3.3 Las dos líneas de comparación, y el caso que las justifica

CIEP rotula «PEF 2026» y mezcla bases: aprobado en el Cuadro 7, proyecto ×1,032 en pensiones. El
caso más elocuente es el **Poder Judicial**. CIEP publica **0.0 % real** (70,005.6 → 72,264.7);
nosotros, **−19,2 % en la línea P** (85.960,2 → 72.264,7). La diferencia, **15.954,6 mdp**, es lo
que la Cámara recortó en diciembre de 2025. Con su única columna, el lector no puede verlo.

| Ramo 11 · Poder Judicial · Ramo 16 | P / 1,040 | P / 1,032 | G / 1,040 | G / 1,032 |
|---|---|---|---|---|
| Ramo 11 | **+8,1** (ITED) | +8,9 | +5,8 | **+6,7** (CIEP) |
| Poder Judicial | **−19,2** (ITED) | −18,5 | −0,7 | **0,0** (CIEP) |
| Ramo 16 | **+8,0** (ITED) | +8,9 | **+4,5** (CIEP, cap. 8) | **+5,3** (CIEP, Cuadro 7) |

### 3.4 El resto

- **El CGPE en dos ediciones** y la contradicción del balance primario (0,5 frente a 0,6); la
  reescritura del índice de la Gaceta. CIEP: «Gaceta», 0.
- **La vara del artículo 61 de la Ley de Vivienda** (226.133,3 mdp contra un Ramo 15 de 37.873,6)
  y la **declaratoria ZAP** recalculada contra las 43.636 AGEB. CIEP: «ZAP», 0.
- **La identidad flujo–acervo**, cerrada a 0,006 puntos del PIB, y la negativa declarada a
  publicar una descomposición sin prueba de aceptación.
- **La comprobación aritmética del Ramo 18** contra el Anexo 1 (+571,1 mdp de resto del ramo).
- **La capa demográfica.** Véase §4.5: este año tiene una debilidad.
- **El registro de lo no verificable**, con sus fallas y sus correcciones fechadas.

---

## 4. Diferencias de método, sin declarar ganador

### 4.1 El deflactor · **dos deflactores en un documento, ninguno declarado**

Recuperado de sus propias cifras:

| Renglón de CIEP | Deflactor implícito |
|---|---|
| Gasto neto total (+1.1) | 1,0321 |
| Ramo 11 (+6.7) · IMSS (+9.9) · INE (+87.6) | 1,0316 · 1,0316 · 1,0319 |
| Participaciones (+3.0) · Salud (+4.8) · Poder Judicial (0.0) | 1,0319 · 1,0324 · 1,0323 |
| Base 2026 de pensiones contributivas · Anexo 17 | **1,0320 · 1,0320** (al peso) |
| **Ramo 16 en el capítulo 8 (+4.5)** · Anexo 16 (−27.6) · Anexo 15 (+9.2) | **1,0398 · 1,0404 · 1,0398** |
| **FMP en el capítulo 2 (−12.9)** | **1,040** (con 1,032 daría −12,2) |

**Casi todo el documento usa ≈1,032**, que es la inflación promedio del INPC y el mismo índice con
que el CGPE calcula sus cuadros. **Los capítulos de medio ambiente y del FMP usan 1,040**, el
deflactor del PIB. El Ramo 16 sale **+5.3 en el Cuadro 7 y +4.5 en el capítulo 8**, la misma cifra
con dos deflactores.

**La serie del deflactor de CIEP:** 1,0480 (2024), 1,04252 (2025), 1,0365 (2026), ≈1,032 (2027).
Cuatro años sin declararlo, y en 2027 además sin uniformidad. La brecha con nuestras variaciones
es de ~0,8 puntos donde usan 1,032 y nula donde usan 1,040. Por eso coincidimos al decimal en el
FMP y en los anexos 15 y 16.

### 4.2 La columna del año anterior, deflactada y rotulada como 2026 · quinto año

- El Cuadro 9 de anexos rotula «PEF 2026 (mdp)»: 618,378 = 599.145,4 × 1,0321.
- En inversión, «1 billón 292 mil 836.8 mdp en 2026» es 1.252.748,8 nominales × 1,032.
- Los Cuadros 10, 12 y 16 sí lo rotulan («mdp de 2027»). La convención es defendible; que no sea
  uniforme, no.

### 4.3 El Ramo 19 · **signo opuesto, las dos cifras correctas**

- **Nosotros:** «el Ramo 19 sube 119.489,2 mdp (+3,6 % real)», segundo del cuadro C4.1.
- **CIEP:** «se reduce el presupuesto para… las Aportaciones a Seguridad Social», 139,565.9 →
  134,893.2, −6.3 %.
- **Adjudicado:** CIEP neta las transferencias a IMSS e ISSSTE. Su cifra es el Ramo 19 bruto menos
  (neteo − cuotas), y se reproduce al décimo en los dos años: 1.541.518,7 − (1.553.113,1 −
  151.160,3) = 139.565,9, y 1.661.007,9 − (1.680.127,3 − 154.012,7) = 134.893,3.
- **Consecuencia para el nuestro:** las transferencias crecen **124.161,9 mdp, más que todo el
  aumento bruto del ramo**. Esos pesos vuelven a aparecer en el presupuesto del IMSS. El cuadro C4.1
  ordena un renglón bruto sin advertir el doble conteo, que sí advertimos en salud (C5.1). El
  titular «Ramo 19, +3,6 %» es correcto sobre su perímetro y engañoso como lectura de política.

### 4.4 Los perímetros

- **Pensiones:** 2.481.037,1 = Anexo 3 + tres programas del CGPE p. 32 (§2.4). Mismo patrón que
  2026.
- **Salud:** 1,148,530.6, función salud del IMSS y del ISSSTE más SSa, IMSS-Bienestar, FASSA,
  Sedena, Semar, Pemex, Ramo 19 sin pensiones y Salud Casa por Casa. Nosotros, cinco vehículos no
  sumados. Su IMSS-Bienestar (193,580.0) es 407,2 menos que nuestro Ramo 56.
- **Federalizado:** 3,048,223.2, con convenios, salud y subsidios. Nosotros, ramos 28 y 33 por
  separado.
- **Inversión: este año el mismo objeto** (clasificación económica del CGPE); en 2026 diferíamos.
  Queda la línea: −12,9 (P) contra −12.3 (G).
- **Medio ambiente: este año el mismo objeto**, el Ramo 16 (49,508). Quedan la línea y el
  deflactor.
- **Educación:** función «educación, ciencia y cultura», 1,387,788.4, +7.2 %, +93,714.5 mdp. **No
  se reconcilia con su propio Cuadro 8**: sus cinco subfunciones suman 1.147.347,1 → 1.163.691,6
  (+1,4 %). Probablemente falta una subfunción, «otros servicios educativos», pero no se adjudica.

### 4.5 La lectura demográfica · **el signo de nuestro titular depende del deflactor**

- **Nosotros:** «por persona de 65 años y más, el gasto pensionario cae 0,4 % real». Está en el
  resumen y en la implicación 4.
- **CIEP:** «el envejecimiento de la población presiona el gasto en pensiones».
- **Con el deflactor de CIEP, el mismo cociente sube +0,4 %.** El resultado está a cuatro décimas de
  cero y **cambia de signo con la convención de deflactación**. La compuerta semántica debió pedir
  la línea de sensibilidad que la nota de método promete («sensibilidad: una sola línea, aquí»), y
  no la hay para este titular.
- **Lo que sí se sostiene:** el perímetro pensionario crece prácticamente al ritmo de la población
  de 65 y más, no más rápido. La afirmación firme es «no crece por persona», no «cae».

### 4.6 La deuda: una inferencia que nosotros no hacemos

CIEP: el costo financiero (4.0 %) supera a los RFSP (3.9 %), luego «se requeriría destinar recursos
fiscales adicionales para cumplir con las obligaciones de deuda previamente contraídas, desplazando
gasto». Nuestro capítulo excluye esa lectura por fungibilidad. Hay además una aritmética: **que el
costo supere a los RFSP equivale a un superávit primario ampliado**, y el propio CGPE lo proyecta
(0,6 % del PIB). Es la definición de un ajuste, no la evidencia de un desplazamiento.

### 4.7 La arquitectura

CIEP pone la deuda primero, en cuatro partes y diez capítulos, con series 2018/2020–2027 y varas
externas. Nosotros seguimos la identidad presupuestal, en dieciséis capítulos con dos años, un
registro y dos notas fechadas. **Este año la diferencia de alcance no es sólo de estilo: ellos
tuvieron el nivel de programa y nosotros no** (§2.1).

---

## 5. Verificación de las cifras de CIEP 2027

Secundaria. **Coinciden** con la fuente todas las de la tabla de §1, más el gasto neto total, los
ramos del Cuadro 7 en niveles, el Anexo 3 y la LFIIEDB.

**Inconsistencias internas o errores de su documento:**

1. **Ingresos, portada del capítulo 3: «22.3 % PIB»**; el texto dice 23.2, y 9.156.528,9 /
   39.419.400 = 23,23 %. La misma portada dice «8.90 billones = 21.7 % del PIB»; da 22,6 %.
2. **«Ingresos presupuestarios estancados en 22.8 % del PIB»** (resumen, capítulo 1,
   implicaciones), contra el 23.2 del capítulo 3. No se declara a qué año o promedio corresponde.
3. **Portada del capítulo 1: «DEUDA CGPE 2026 $21,680,678.4 MDP».** El rótulo de año está mal, y la
   cifra no está en ninguna de las dos ediciones del CGPE 2027 (21.665.995,8) ni en los Pre-Criterios
   (21.848.685,1). La diferencia contra el CGPE es de +14.682,6 mdp.
4. **Presentación: el SHRFSP queda «0.7 pp por encima del aprobado para 2026».** Su capítulo 1 da
   un aprobado de 52.3 (2.7 pp) y el cierre estimado es 54.0 (1.0 pp).
5. **Cuadro 1 contra texto:** tasa de interés 6.1 contra 6.0; tipo de cambio 17.9 contra 18.0.
6. **«Por cada peso de Semarnat, 24 pesos en Pemex y CFE»,** atado en implicaciones a los 171.5 mmdp
   de apoyos. 171,5 / 49,5 = 3,5. El 24 se aproxima al gasto *total* de las dos empresas (25,3) o al
   programable (21,2), no a los apoyos. Es un sujeto distinto de su cálculo.
7. **«La transferencia a Pemex bajaría 69.2 %»** es variación **nominal** (81.103 / 263.476), en un
   documento donde las demás son reales. Con su deflactor sería −70,2 %.
8. **Secretaría de las Mujeres: «0.3 % del Anexo 13».** 2.269,4 / 636.133,1 = 0,357 %, que redondea
   a 0,4. Nosotros publicamos 0,36.
9. **Aportaciones: +5.9 % en el capítulo 9 contra +5.7 % del Ramo 33 en el Cuadro 7.** No se
   reconcilia sin su perímetro.
10. **Educación:** texto contra Cuadro 8 (§4.4).

**Requieren advertencia de deflactor:** todas sus variaciones reales, con la de §4.1 de que el
deflactor no es uniforme. **Requieren advertencia de columna:** las de §4.2.

**No verificables con esta carpeta:** el espacio fiscal de 1.6 %, su estimación de la Miscelánea
(supone deducciones del 90 % de los ingresos), el gasto per cápita por subsistema (padrones), el
Anexo 32 (§2.2) y la atribución de la caída del Anexo 16 al Tren Maya.

---

## 6. Contaminación

**En cifras y en frases, imposible por construcción** (§ Control).

**Una convergencia que no es contaminación:** los dos resúmenes abren con «13.9 de cada 100 pesos
provendrán de financiamiento». Es la misma aritmética (1.479.959,2 / 10.636.488,1 = 13,91 %) y el
mismo gesto del género, que esta casa aprendió leyendo a CIEP seis ejercicios. **La pregunta es
heredada; el número es de la fuente.**

**La advertencia de fondo, que es nueva.** En 2026 la contaminación a vigilar era qué preguntas
heredamos. **En 2027 la lección es la inversa: nuestro régimen de lectura en vivo convirtió una
falla de ruta en una falla de fuente**, y la escribió así en el resumen, en el registro y en dos
notas («no es una limitación de método ni de tiempo: es una fuente que el servidor no entregó»). El
comparador que no tuvimos lo habría detectado el día 11. **El control que falta no es de
contaminación: es de diagnóstico.** Un 404 sobre una ruta conocida no prueba que el recurso no
exista. Hay que buscar la ruta desplazada en lo publicado —la Carta, las referencias de terceros—
antes de declarar Ruta B.

---

## 7. Qué cambia para el proyecto

Las acciones van en orden de importancia; ninguna está ejecutada.

1. **`mapa_fuentes.md`:** registrar el árbol `ppef.hacienda.gob.mx/work/models/PP3F2709/PPEF{t}/<hash>/`,
   con analíticos **sin** `/Proyecto/` y exposición de motivos servida. Corregir la regla «404 =
   árbol no creado».
2. **Ruta A para 2027 abierta:** descargar los cuatro analíticos (≈16 MB) y decidir si hay tercera
   nota de actualización. Con ellos: diff institucional, auditoría de etiquetado, IMSS
   salud/pensiones, Anexo 32 por programa y el monto excluible de la regla fiscal.
3. **Extracción de anexos:** contrastar la lista de anexos que nombra el artículo 3 del decreto
   contra los extraídos. No depender de «ANEXO NN.» ni de «Total general». Comparar sha256 del
   decreto contra el portal (pendiente desde el día 8).
4. **Correcciones al documento propio que esta comparación hace exigibles:**
   - el Anexo 32;
   - la inversión por proyecto y la pensión no contributiva (CGPE p. 32);
   - la advertencia de doble conteo del Ramo 19 en C4.1;
   - la sensibilidad del titular de pensiones por persona («no crece», no «cae»);
   - la meta de RFSP de los Pre-Criterios;
   - el renglón de la exposición de motivos «404 por sexto ejercicio».

   **No se hace sin decisión de Héctor.** El cuerpo tiene la regla de no reescribirse.
5. **Checklist de omisiones:** B1 (vara de salud) pasa a cuarto ejercicio. Añadir «pronóstico
   externo de crecimiento», «tablas de la p. 32 del CGPE», «tabla fiscal de Pre-Criterios» y
   «anexos del artículo 3 contra extraídos».
