# Ruta A del ejercicio 2027 — lo que dicen los analíticos del proyecto

**Corrida:** 2026-09-12, desde las 23:08 CST, en Dalila. **Guion:** `documento_2027/ruta_a.py`
(reproduce todo; 8 pruebas, 0 fallas). **Salidas:** `documento_2027/datos/ruta_a/*.csv` y
`_herramientas/_salidas/diffs_2026_2027.csv`.
**Convención:** línea P (proyecto 2027 contra proyecto 2026), deflactor del PIB 1,040, mdp.

**Qué es y qué no es.** Es el insumo de la **tercera nota de actualización** del documento
(`capitulos/99d_actualizacion.tex`, 12 de septiembre de 2026), que publica lo que aquí se
resume con cinco cuadros nuevos (C99.6 a C99.10). **No reescribe el documento**: el cuerpo de
los dieciséis capítulos sigue con su regla. Donde un resultado corrige una afirmación del
documento, se dice aquí con la cita.

## 0. Fuente y validación

**Cambio de ruta: 2026-09-12 23:08 — Ruta A.** Los cuatro analíticos del proyecto se localizaron
en `ppef.hacienda.gob.mx/work/models/PP3F2709/PPEF2027/yik327fP/analiticosPresupuestarios/`, **sin
`/Proyecto/`**, siguiendo las referencias del documento de CIEP (véase `comparacion_2027.md` §2.1).
Descargados con el bundle TLS y registrados en `_manifiesto.csv` con sha256:

| archivo | bytes |
|---|---|
| `2027_ppef_analitico-gf-ramo-programa-ur-objeto.xlsx` | 7.933.031 |
| `2027_ppef_analitico-gf-ramo-funcion-ur-objeto.xlsx` | 5.621.893 |
| `2027_ppef_analitico-entidades-ramo-programa-ur-objeto.xlsx` | 2.751.373 |
| `2027_ppef_analitico-entidades-ramo-funcion-ur-objeto.xlsx` | 2.531.275 |

**Pruebas de identidad, todas pasan:**

- Los 40 ramos del Anexo 1 del decreto se reproducen con el analítico del Gobierno Federal, en
  2026 y en 2027. La diferencia máxima es de 0,05 mdp, por redondeo.
- IMSS, ISSSTE, Pemex y CFE reproducen el Anexo 1 al décimo.
- La función salud de 2026 da **974.302,2**, la cifra del documento 2026.
- La partida 73903 de 2026 da **263.476,3**, la cifra del documento 2026.
- El Ramo 19 neto de transferencias reproduce el de CIEP en los dos años.
- El Anexo 32 extraído del decreto da **175.045,5**, la cifra de CIEP.

Las ranuras del ATDT (PPEF por clave y anexos transversales) responden **403** el 12 de
septiembre. La auditoría de etiquetado se hizo, por tanto, **leyendo las tablas de los anexos del
decreto** (§8).

---

## 1. Diff institucional 2026 → 2027

| nivel | claves | aparecen (mdp 2027) | desaparecen (mdp 2026) |
|---|---|---|---|
| ramo | 46 | **0** | **0** |
| programa (modalidad + número) | 564 | 48 (664.440,9) | 27 (566.912,1) |
| programa por número | 485 | 41 (647.728,2) | 23 (543.346,0) |
| unidad responsable dentro del ramo | 1.445 | 233 (160.182,7) | 158 (168.280,8) |
| unidad responsable entre ramos | 581 | 84 (128.359,9) | 50 (24.637,9) |
| subfunción | 87 | 0 | 0 |

**Ningún ramo nace ni se extingue** (en 2026 fueron cinco extintos y tres nuevos). **Casi todo lo
que «aparece» es recodificación**, y leerlo como gasto nuevo sería el error que el diff previene:

- **Ramo 28:** «C003 Otros conceptos participables e incentivos» (329.115,1) se abre en fondos con
  nombre propio. Los mayores son C012 Fondo ISR 128.147,5, C005 Fiscalización y Recaudación
  71.534,4, C014 Otros Incentivos 64.998,4, C011 Venta final de gasolina y diésel 36.185,4 y C008
  IEPS 20.583,5.
- **CFE:** 077, 078 y 079 («Servicios de operación y mantenimiento…») pasan a 015, 016 y 017
  («Funciones de operación y mantenimiento…»).
- **Ramo 56, IMSS-Bienestar:** U013 (80.768,4) se divide en **E089 64.010,9 + U013 15.673,7 + U014
  12.033,0**, más R038 Sistema Universal de Salud 2.500,0.
- **Hacienda y Seguridad:** E013 y E012 pasan a X004 y X003; E055 pasa a X009, con E088 y X011
  nuevos. **Nace una modalidad, «X» («Funciones de…»)**, que en 2026 no existía.
- **Cuatro cambios de modalidad conservando el número:** G003→X003 (CONSAR), A015→E015 y A016→E016
  (Defensa) y E019→K019 (aeropuertos).

**Unidades nuevas o extintas con monto:**

- Nace JZO **Agencia de Trenes y Transporte Público Integrado**, en el Ramo 09, con **108.767,7**.
- Desaparecen la 237 Dirección General de Eficiencia Hídrica en el Temporal (Ramo 08, 18.216,5) y la
  **145 Cuerpo de Policía Militar (Ramo 07, 19.978,4)**.

**Casos de prueba obligatorios:**

- **IMSS-Bienestar:** sigue en el Ramo 56, UR AYO, y crece +8,1 % real. Sin cambio de ramo.
- **Guardia Nacional:** sigue en el Ramo 07, UR 148, y pasa de 23.492,8 a **31.486,6, +28,9 % real**.
  Este año **no hay cambio de ramo**: la variación es presupuestal. Crece su programa E056 (16.934,2
  → 25.126,9).
- **Policía Militar:** su desaparición no se localiza en una sola UR. Las que más ganan en el Ramo
  07 son la Fuerza Aérea (+10.816,5), la DG de Administración (+9.364,9), la Guardia Nacional
  (+7.993,8) y la I Región Militar (+5.962,1). **No se atribuye** el traslado, porque el analítico no
  lo permite.

---

## 2. Pensiones por institución · el perímetro del Anexo 3, descompuesto

Tipo de gasto 4 (pensiones y jubilaciones) de los analíticos:

| institución | 2026 | 2027 | var. real |
|---|---|---|---|
| IMSS | 1.010.525,2 | **1.136.228,0** | **+8,1 %** |
| ISSSTE | 395.156,0 | 409.867,0 | −0,3 % |
| Pemex | 92.333,4 | 94.472,9 | −1,6 % |
| CFE | 67.841,7 | 66.154,8 | −6,2 % |
| Resto del Gobierno Federal (por diferencia) | 138.302,9 | 134.023,4 | −6,8 % |
| **Perímetro del Anexo 3** | **1.704.159,2** | **1.840.746,1** | **+3,9 %** |

**El perímetro que el documento adjudicó por diferencia del Anexo 3 se descompone ahora por
institución.** El IMSS aporta **125.702,8 de los 136.586,9 mdp** del aumento, el 92 %. Pemex, CFE y
el resto del Gobierno Federal caen en términos reales, en línea con el límite constitucional a las
pensiones públicas que cita CIEP. El «qué no sabemos» del capítulo de pensiones («cómo se reparte
el perímetro entre IMSS, ISSSTE, Pemex, CFE…») **queda respondido**. Las cifras de IMSS e ISSSTE
coinciden con las de CIEP al peso.

**El Ramo 19, adjudicado:** transfiere a IMSS e ISSSTE **1.401.952,8 → 1.526.114,6 (+124.161,8)**.
El Ramo 19 neto de esas transferencias es **139.565,9 → 134.893,2**, que es la cifra de CIEP. Del
aumento transferido, **94.205,5 mdp son del J003 «Pensiones y jubilaciones en curso de pago»** (el
IMSS, régimen de 1973) y 19.427,0 del J002 déficit de la nómina del ISSSTE.

---

## 3. IMSS e ISSSTE: salud y pensiones, separados

El capítulo de salud del documento declaró que no podía separarlos. Con el corte por función:

| entidad · función | 2026 | 2027 | var. real |
|---|---|---|---|
| IMSS · 2.3 Salud | 556.342,6 | **640.797,1** | **+10,8 %** |
| IMSS · 2.6 Protección social | 1.032.733,4 | 1.160.838,9 | +8,1 % |
| ISSSTE · 2.3 Salud | 81.525,8 | **99.963,9** | **+17,9 %** |
| ISSSTE · 2.6 Protección social | 457.005,5 | 471.135,6 | −0,9 % |

**Corrección de lectura al capítulo de salud.** El documento tituló que el IMSS crece 9,0 % y
advirtió que esa cifra mezcla salud y pensiones. **La salud del IMSS crece más que su agregado
(+10,8 %)**, y la del ISSSTE casi 18 %, mientras su protección social cae. La advertencia era
correcta; ahora tiene cifra.

## 4. Función salud por subfunción

GF más entidades: **974.302,2 → 1.114.506,5, +10,0 % real.** La mayor subfunción, 2.3.2
(prestación de servicios de salud a la persona), sube +13,8 %.

**Un falso recorte que el diff por subfunción desactiva:** la 2.3.4 cae **−74,3 %**. Casi toda la
caída es del **Ramo 33 (FASSA)**, que baja de 30.092,8 a 3.352,1 en esa subfunción mientras sube de
37.964,6 a 69.171,3 en la 2.3.2. **Es reclasificación del mismo fondo entre subfunciones**, no un
recorte a la rectoría del sistema.

## 5. Función educación por subfunción

**1.161.862,4 → 1.299.226,2, +7,5 % real.** Por subfunción:

| subfunción | var. real |
|---|---|
| 2.5.1 básica | +4,9 % |
| 2.5.2 media superior | +1,9 % |
| 2.5.3 superior | +5,5 % |
| 2.5.4 posgrado | +6,9 % |
| 2.5.5 adultos | +1,0 % |
| **2.5.6 otros servicios educativos** | **+66,1 % (55.872,5 → 96.507,1)** |

La 2.5.6 crece en el Ramo 11 (+33.204,5, con 18.746,7 en la DG de Recursos Humanos) y en el Ramo 25
(+7.339,8). **Es la subfunción que falta en el Cuadro 8 de CIEP** y explica que su texto (+7,2 %) no
cuadre con su cuadro (+1,4 %), como se sospechó en `comparacion_2027.md` §4.4.

---

## 6. Inversión y la regla fiscal

**Por capítulo del objeto del gasto (GF + entidades):**

| concepto | 2026 | 2027 | var. real |
|---|---|---|---|
| Capítulo 6000, inversión pública | 431.608,6 | 485.257,6 | **+8,1 %** |
| Capítulo 7000, inversiones financieras | 388.161,3 | 164.329,3 | **−59,3 %** |
| Ramo 18, partida **73903** (aportaciones de capital a Pemex) | 263.476,3 | **81.103,0** | −70,4 % |

- **Cierra el punto 4 del capítulo de la regla fiscal**, que el documento dejó «no se afirma ni se
  niega». **Sí hay aportación de capital a una empresa pública clasificada en el capítulo 7000**:
  81.103,0 mdp en la partida 73903 del Ramo 18. Bajo la cláusula de 2026 habría sido inversión
  financiera excluible; en 2027 no hay cláusula.
- **Con la partida exacta, la aritmética del Ramo 18 se afina.** La caída de la aportación es de
  182.373,3 y la del ramo, de 181.804,9. **El resto del ramo sube 568,4**, no los 571,1 que salían de
  las cifras redondeadas de la prosa del CGPE.
- **Capítulo 6000 por ejecutor:**
  - Ramo 09 Infraestructura: 62.566,0 → **115.265,8 (+77,1 %)**.
  - Defensa: 31.510,9 → 17.158,8 (−47,6 %, Tren Maya).
  - Pemex: 239.843,2 → 241.237,2 (−3,3 %).
  - CFE: 39.761,8 → 38.043,3 (−8,0 %).

**El gasto corriente estructural, con la fuente que el documento no leyó.** El CGPE 2027
(pp. 23–24) publica la nueva metodología completa. Sobre la Cuenta Pública 2025, además de excluir
a las empresas públicas, **resta cuatro rubros nuevos**:

| rubro excluido (CP 2025) | mdp |
|---|---|
| (7) programas sociales universales establecidos en la Constitución | 766.412,4 |
| (8) servicios personales de la función educación | 648.331,6 |
| (9) servicios personales de la función salud | 522.120,5 |
| (10) servicios personales de asuntos de orden público y seguridad interior | 27.635,3 |
| **Suma** | **1.964.499,8** |

- **Corrección al capítulo de la regla fiscal y a la implicación 2.** El documento atribuyó la caída
  del agregado (3.868.319,9 → 1.884.958,2, −51,3 %) a que «el gasto de las empresas públicas no se
  contabilizará». **Es incompleto.** Esos cuatro rubros suman del orden de la caída entera.
- **Las empresas públicas pesan menos de lo que el documento sugiere.** Su gasto corriente sin
  costo financiero, según los analíticos, es de **598.657,0 (2026) → 573.721,3 (2027)**. La frase
  debe decir que el nuevo cómputo **excluye empresas públicas, programas sociales constitucionales y
  la nómina de educación, salud y seguridad**.
- El CGPE estaba en carpeta desde el día 8. **No fue un límite de la Ruta B.**

---

## 7. Ramo 33 por entidad federativa

- **Todas las entidades crecen en términos reales** en el Ramo 33. El rango va de Michoacán (+1,2 %)
  a Aguascalientes (+7,5 %); la Ciudad de México sube +2,4 %.
- **El componente «no distribuible geográficamente» crece +12,9 %** (62.754,2 → 73.696,3), más que
  cualquier entidad. La distribución completa está en `ramo33_entidad_federativa.csv`.
- El documento no la publica (capítulo de gasto federalizado, «qué no sabemos»); ahora está en
  carpeta.

---

## 8. Anexos transversales · la auditoría de etiquetado

**Método.** Se leyeron las tablas de los anexos 13–19, 31, 32 y 33 del proyecto de decreto de 2026
y de 2027. Desde 2027 esas tablas traen objetivo, ramo, programa y acción, y **cada monto se valida
contra el «Total general» de su anexo**:

- 2026: cobertura del 100,00 % en los ocho anexos.
- 2027: 100,00 % en siete, 99,99 % en el 13 y 99,78 % en el 31 (1.067,7 mdp no localizados, que se
  declaran).
- El 32 no tiene total impreso. Su extracción da 175.045,5, la cifra de CIEP.

**Las tres preguntas que el documento dejó sin responder:**

| | 2026 | 2027 (mismos anexos) | 2027 (con 32 y 33) |
|---|---|---|---|
| programas etiquetados | 226 | 228 | 243 |
| en más de un anexo | 123 | 123 | 136 |
| **% del etiquetado que está en programas con más de una etiqueta** | **95,4 %** | **95,8 %** | **95,2 %** |
| suma aritmética de etiquetas (mdp) | 4.284.445,1 | 4.381.269,1 | 4.599.683,9 |
| **pensiones no contributivas en el Anexo 13 (S176, S286, S316)** | **48,1 %** | **57,2 %** | — |

- **El traslape no cambia:** 95 de cada 100 pesos etiquetados están en programas que llevan más de
  una etiqueta. (El documento 2026 publicó 95,8 % con el CSV del ATDT; el mismo cálculo sobre el
  decreto da 95,4 %.)
- **La igualdad se vuelve más pensión.** El 57,2 % del anexo de igualdad son tres pensiones no
  contributivas, nueve puntos más que en 2026. La Pensión Mujeres Bienestar pasa de 14.550,0 a
  **56.969,0** dentro del anexo.
- **Los anexos nuevos son reetiquetado.**
  - **Anexo 33:** 54 de sus 62 programas ya estaban etiquetados en otro anexo de 2027, con 43.322,2
    de sus 43.369,4 mdp: **el 99,9 %**. Responde el «qué no sabemos» del documento («si el Anexo 33
    es gasto nuevo o reetiquetado»).
  - **Anexo 32:** 16 de 23 programas y 130.912,2 de 175.045,5 mdp (74,8 %) ya estaban en otro
    anexo. El 66,8 % del anexo es un solo programa, K019, infraestructura ferroviaria.

**La caída del Anexo 16 (cambio climático), adjudicada.** De 212.569,7 a 160.120,9. **Tres
programas dejan de etiquetarse**:

| programa | etiqueta 2026 |
|---|---|
| 07-A001 Defensa de la Integridad, la Independencia y la Soberanía | 44.673,4 |
| 07-K003 Infraestructura en materia de seguridad nacional | 40.000,0 |
| 18-P038 Articulación de la política de hidrocarburos | 26.370,0 |
| **Suma** | **111.043,4** |

- **Es desetiquetado, no recorte.** El A001 sigue en el presupuesto de 2027, con 59.083,2.
- **La explicación de CIEP, «el cierre de la inversión del Tren Maya», no la sostiene la lista
  por programa.** El E015 del Tren Maya pierde 604,8 de etiqueta.
- **Anomalía de la fuente, registrada.** En 2026 el Anexo 16 etiquetó **40.000,0 mdp al K003, cuyo
  presupuesto en el analítico del proyecto era de 1.510,9**. Es el único caso de etiqueta mayor que
  el programa entre los 2026 del Anexo 16, y el programa ya no existe en 2027.

---

## 9. Qué del documento cambia con esto

**No se ha tocado el documento.** Estas son las afirmaciones que la Ruta A corrige o completa.
Quedan para decisión de Héctor sobre una tercera nota:

1. **Resumen, capítulos 4, 5, 6, 8, 9, 10, 12 y registro:** «no baja al programa presupuestario»,
   «el árbol no existe». La Ruta A existe desde el 11 de septiembre, por lo menos.
2. **Capítulo de la regla fiscal e implicación 2:** la causa de la caída del gasto corriente
   estructural (§6). **Es la corrección de mayor peso.**
3. **Capítulo de salud:** IMSS salud +10,8 % e ISSSTE salud +17,9 % (§3); la función salud,
   +10,0 %.
4. **Capítulo de pensiones:** el reparto del perímetro por institución (§2).
5. **Capítulo de anexos:** el Anexo 32, las tres preguntas de la auditoría, el Anexo 33 como
   reetiquetado, la caída del 16 (§8).
6. **Capítulo de seguridad:** la Guardia Nacional, +28,9 % real sin cambio de ramo; la Policía
   Militar desaparece como UR (§1).
7. **Capítulo de inversión y energía:** la partida 73903 y el resto del Ramo 18, +568,4 (§6).
8. **Gasto total (C4.1):** la advertencia del Ramo 19 bruto (§2).

**Lo que la Ruta A no hizo:**

- el agua (la Conagua dentro del Ramo 16);
- la exposición de motivos del PPEF, que existe y no se leyó;
- el cruce de la ZAP con el gasto (el analítico trae la entidad federativa, no el municipio);
- la línea G a nivel de programa (exige el analítico aprobado de 2026, que está en carpeta);
- actualizar `_herramientas/rutas.py` con el prefijo nuevo.
