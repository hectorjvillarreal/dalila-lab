# Bitácora de la corrida en vivo — Paquete Económico 2027

Ejecuta `INSTRUCCIONES_corrida_en_vivo_2027.md`. Máquina: Dalila.

**Arranque del cronómetro: 2026-09-08T18:45:07-06:00.**
Entrega del paquete: martes 8 de septiembre de 2026, Gaceta Parlamentaria número
**7121**, legislatura LXVI, doce anexos.

---

## Banda 0–2 h

### 1. Piezas que no llegaron, primero de todo

Regla de no bloqueo aplicada: dos intentos, se registra ruta y respuesta, la corrida
sigue.

| pieza | ruta | respuesta | intentos |
|---|---|---|---|
| analítico proyecto GF ramo-programa | `pef.hacienda.gob.mx/…/Analiticos_Historico/2027/Proyecto/ac01_ra_pp_ur_og.xlsx` | **404** `text/html` | 1 |
| analítico proyecto GF ramo-función | `…/2027/Proyecto/ac01_ra_f_ur_og.xlsx` | **404** | 1 |
| analítico proyecto entidades ramo-programa | `…/2027/Proyecto/ac01_ra_pp_ur_og_efe.xlsx` | **404** | 1 |
| analítico proyecto entidades ramo-función | `…/2027/Proyecto/ac01_ra_f_ur_og_efe.xlsx` | **404** | 1 |
| PPEF por clave (ATDT) | `repodatos.atdt.gob.mx/…/PPEF_2027.csv` | **503** | 1 |
| anexos transversales (ATDT) | `…/anexos_transversales_ppef2027.csv` | **503** | 1 |
| miscelánea, Código Fiscal | Gaceta anexo **F** | **404** `text/html`, 1 007 B | **2** |
| informe arancelario art. 131 | Gaceta anexo **G** | **404**, 1 007 B | **2** |

F y G **están enlazados en el índice de la Gaceta** y aun así no se sirven: es el mismo
patrón de almacén roto que el proyecto documentó para la exposición de motivos del PPEF
2022–2026. Reintentar en la banda siguiente.

**El analítico de plazas (ATDT) responde 200, pero es el archivo de 2026.**
`content-length` 11 663 197 y `last-modified` 2026-06-03: idéntico byte a byte al que ya
está en `2026/`. La ranura única **todavía no se ha sobrescrito con 2027**. Vigilarla: el
día que cambie, lo que hoy responde desaparece.

### 2. Ruta adoptada: **B**, con hora

**2026-09-08T18:48 — Ruta B.** Los cuatro analíticos del proyecto dan 404 el día de la
entrega. El documento trabaja **a nivel de ramo y función** con lo que publica el decreto,
y **declara en el texto lo que no puede decir**: composición por programa presupuestario,
reasignaciones entre unidades responsables, distribución territorial y separación entre
caída de ramo y caída de función.

**La ruta se revisa, no se cierra.** En 2026 los analíticos del proyecto sí existieron;
nada indica retirada, sólo que no están el mismo día. Si aparecen dentro de la corrida, se
pasa a Ruta A y se declara la hora del cambio.

**Consecuencia inmediata: el diff institucional no se puede correr.** Necesita claves de
programa y unidad responsable del proyecto 2027. Queda pendiente de la Ruta A. Mientras
tanto **ninguna variación por programa se calcula**, conforme al límite 2 de la
instrucción.

### 3. Lo que sí llegó

De la Gaceta del día de la entrega (`gaceta.diputados.gob.mx/PDF/66/2026/sep/`):
anexo **A** ILIF, **B** proyecto de decreto, **C** CGPE, **D** Ley Federal de Derechos,
**E** Ley del Impuesto sobre la Renta. Del portal de la Secretaría: CGPE e ILIF.

**Las letras cambiaron y la advertencia de la precarga sirvió.** En 2026 fueron
D = Derechos, E = IEPS, F = Código Fiscal, G = arancelario. En 2027 la **E es ISR** y
**no hay anexo de IEPS**: la miscelánea 2027 toca Derechos, ISR y Código Fiscal. Suponer
las letras habría archivado el ISR como si fuera IEPS.

Manifiesto: de 103 a 107 archivos registrados.

### 4. El sha256 de las tres piezas que ya estaban en carpeta

Tarea heredada del ordenamiento del 2026-09-08: las piezas descargadas a mano traían
`Producer: pypdf` y `Creator: PDF24`, y había que comprobar si el contenido era el del
servidor.

- **ILIF: resuelto y sin anomalía.** El archivo que sirve el portal de la Secretaría es
  **byte a byte idéntico** (sha256 `8048a912…`). El `pypdf` es de la propia Secretaría.
  `url_origen` corregida en el manifiesto.
- **PPEF, proyecto de decreto: contenido idéntico** al anexo B de la Gaceta, página por
  página, con desfase de una hoja por la portada de la Gaceta. Las 252 páginas coinciden
  en texto normalizado. El `PDF24` no alteró nada.
- **CGPE: no idéntico, y el hallazgo es de fondo.** Ver §5.

### 5. HALLAZGO — el CGPE 2027 circula en dos ediciones que no dicen lo mismo

| | edición **SHCP** | edición **Gaceta** |
|---|---|---|
| dónde | `finanzaspublicas…/cgpe/cgpe_2027.pdf` | anexo C de la Gaceta 7121 |
| productor | Word 2016 | Acrobat Distiller (PScript5) |
| páginas | 75 | 78 (una es portada de la Gaceta) |
| archivo | `2027_cgpe_criterios-generales.pdf` | `2027_cgpe_criterios-generales_gaceta.pdf` |

Las dos están fechadas el 8 de septiembre de 2026 y **difieren en 64 bloques de texto**,
de los cuales una docena son cifras. Lo comprobado:

- **Balance primario 2027: 0.5 % del PIB (SHCP) contra 0.6 % (Gaceta).** Es un renglón del
  cuadro resumen de la página 6, el que abre el documento.
- **La base de 2026 del IEPS de gasolinas cambia** —473.3 / 288.2 contra 488.6 / 297.5 en
  la LIF, y 449.0 / 277.3 contra 463.5 / 286.2 en el estimado— y con ella **todo lo
  derivado**: la variación de ese renglón pasa de **+1.5 % a −7.8 %**, es decir **cambia de
  signo**.
- **El crecimiento real de la recaudación tributaria excluyendo el IEPS de combustibles:
  2.6 % (Gaceta) contra 3.4 % (SHCP)**, sobre el mismo nivel de 5 725.3 mmp. La diferencia
  está en la base, no en la meta.
- **El plazo para amortizar pérdidas fiscales: de 10 a 15 años (Gaceta) contra de 10 a 20
  años (SHCP).**

**Adjudicación, con fuente independiente y no por criterio propio.** *Ampliada en la banda
2–8 h; la versión de las 18:56 daba por ganadora a la edición SHCP en bloque y **eso era
prematuro**. Adjudicado punto por punto:*

1. **Pérdidas fiscales — gana la SHCP.** Lo resuelve el **anexo E, la iniciativa de reforma
   al ISR**, que viaja en la misma Gaceta: dice **veinte** de forma consistente, en la
   exposición de motivos, en el transitorio de las pérdidas generadas hasta 2026 y en el
   articulado («podrán disminuirse en los veinte ejercicios siguientes»). La edición de la
   Gaceta contradice a la iniciativa que resume.
2. **Cuadros de ingresos — gana la SHCP, y el mecanismo queda identificado.** Los dos
   cuadros de la página 27 se titulan «**Miles de millones de pesos de 2027**». La columna
   de 2026 de la edición **Gaceta está en pesos nominales de 2026**: su IEPS de gasolinas
   dice **473.3**, que es exactamente el **473,279.1 mdp de la LIF 2026 aprobada**, sin
   convertir. La edición SHCP publica **488.6**, que es esa misma cifra multiplicada por
   **1.0323** —la inflación promedio de 2027, 3.2 %—. El factor reproduce las cuatro parejas
   comprobadas (473.3→488.6, 288.2→297.5, 449.0→463.5, 277.3→286.2 y el total
   5,365.3→5,538.4). **La edición de la Gaceta queda internamente incoherente**: su renglón
   informativo pone una diferencia absoluta de 360.0 mmp junto a una relativa de 3.4 %,
   cuando 360.0 sobre su propia base son 6.7 %. En la edición SHCP el mismo renglón dice
   186.9 y 3.4 %, y **cierra**. Es, literalmente, el error que este proyecto le señala al
   género desde 2020: **nominal comparado con real bajo un encabezado de pesos constantes.**
3. **Balance primario — gana la GACETA, y aquí la SHCP se contradice a sí misma.** El
   **Anexo II.6 es idéntico en las dos ediciones**: superávit económico primario 2027 =
   **216,891.3 mdp**, columna de % del PIB **0.6**. Sobre el PIB de 39,419.4 mmp son
   0.550 %, que redondea a 0.6. El cuadro resumen de la página 6 de la **edición Gaceta dice
   0.6** y concuerda con su anexo; el de la **edición SHCP dice 0.5** y **contradice al
   Anexo II.6 de su propio documento**.

**Lectura de conjunto.** La edición de la SHCP es la **corregida**: arregla la deflactación
de los cuadros de ingresos y el plazo de las pérdidas fiscales. Pero al reeditar **rompió
una celda** del cuadro resumen. Ninguna de las dos domina.

**Regla de trabajo, revisada:** se adopta la **edición SHCP como base de trabajo** —es la
que publica la Secretaría y la que gana dos de los tres puntos arbitrables—, **con el
balance primario tomado del Anexo II.6 (0.6 % del PIB), no de su página 6**. Toda cifra
tomada del CGPE declara su edición. Las dos se conservan: la discrepancia es material del
documento, no ruido a limpiar.

*Advertencia sobre las marcas de tiempo:* el PDF de la Gaceta se generó a las 17:19 y el
de la SHCP a las 13:40, pero eso fecha el armado del PDF por la Cámara, no la añada del
contenido. **La antigüedad no adjudica; el anexo E sí.**

### 6. Marco macroeconómico (edición SHCP, anexos II.5 p. 66 y III.1 p. 68)

| | 2026 aprobado | 2026 estimado | **2027** |
|---|---|---|---|
| PIB nominal (mmp) | 38 715.9 | 37 160.7 | **39 419.4** |
| Crecimiento real (rango) | [1.8, 2.8] | [1.0, 2.0] | **[1.5, 2.5]** |
| Deflactor del PIB | 4.8 | 3.8 | **4.0** |
| Inflación dic./dic. | 3.0 | 3.5 | **3.0** |
| Tipo de cambio promedio | 19.3 | 17.6 | **17.9** |
| Cetes 28 días, promedio | 6.6 | 6.5 | **6.1** |
| Petróleo (dpb) | 54.9 | 78.4 | **61.8** |
| Plataforma producción (mbd) | 1 794.0 | 1 800.0 | **1 800.1** |
| Plataforma exportación (mbd) | 521.0 | 522.4 | **426.6** |
| Cuenta corriente (% PIB) | −0.6 | −0.5 | **−0.6** |

**El PIB de 2026 se revisó a la baja en 1 555.2 mmp** entre el aprobado y el estimado, un
4.0 %. Toda razón a PIB de 2026 depende de cuál añada se use, y la instrucción obliga a
declararlo.

### 7. Agregados de ingreso, gasto, balance y deuda

**Resumen de finanzas públicas, % del PIB** (CGPE edición SHCP, p. 6):

| | 2026 aprob. | 2026 estim. | **2027** |
|---|---|---|---|
| Ingresos presupuestarios | 22.5 | 23.0 | **23.2** |
| — petroleros | 3.1 | 3.0 | **2.5** |
| — no petroleros | 19.4 | 20.0 | **20.7** |
| Gasto neto pagado | 26.1 | 26.6 | **26.7** |
| — programable pagado | 18.1 | 18.9 | **18.5** |
| — no programable | 8.0 | 7.7 | **8.1** |
| Balance presupuestario | −3.6 | −3.6 | **−3.4** |
| Balance primario | 0.5 | 0.1 | **0.5** *(0.6 en la edición Gaceta)* |
| RFSP | −4.1 | −4.1 | **−3.9** |
| SHRFSP | 52.3 | 54.0 | **55.0** |

**De la ILIF (artículo 1o.):** ingreso total **10 636 488.1 mdp**; recaudación federal
participable proyectada **5 722 752 mdp**; pago en especie 527 mdp.
**Artículo 2o.:** endeudamiento neto interno hasta **1 700 000 mdp**; externo hasta
**13 500 mdd**. *Techo de endeudamiento, no déficit: la distinción se conserva.*

**Del decreto:** Anexo 2, **gasto corriente estructural 1 884 958 240 686 pesos**;
Anexo 3, **previsiones para gastos obligatorios 6 693 540.5 mdp** y **con pensiones y
jubilaciones 8 534 286.6 mdp**.

**El perímetro de pensiones queda adjudicado por diferencia: 1 840 746.1 mdp**, que es la
técnica que la rúbrica adopta desde 2025 —buscar la fuente que adjudique en vez de
argumentar el perímetro—.

### 8. HALLAZGO — la cláusula de exclusión no desapareció: se mudó de ley

La verificación previa a la corrida ya había establecido que **el artículo 1o. de la ILIF
2027 no trae cláusula de exclusión ni tope en porcentaje del PIB**, y que las cadenas
«contabiliz\*» y «equilibrio presupuestario» no aparecen ni en las 308 páginas de la ILIF
ni en las 252 del decreto. Eso ponía a 2027 como «cláusula ausente», igual que 2024 y 2025.

**La lectura del decreto lo corrige.** El **Anexo 2** del proyecto de decreto declara que
el gasto corriente estructural está «estimado con la **nueva metodología**, derivada de la
publicación el **9 de abril de 2026** del Decreto por el que se expide la **Ley para el
Fomento de la Inversión en Infraestructura Estratégica para el Desarrollo con Bienestar**,
y se **reforman y adicionan diversas disposiciones de la LFPRH**».

Las otras dos apariciones sostienen la pista:

1. La **ILIF (p. 205)** exceptúa de la concentración en la Tesorería «los ingresos
   federales que generen los proyectos para el desarrollo con bienestar previstos» en esa
   ley.
2. El **CGPE trae un cuadro nuevo** (p. 75) de contratos LFIIEDB, con **inversión de
   terceros 188.9 mmp y pagos diferidos 273.5 mmp**, y una nota que remite a los artículos
   82 y 116 de la ley.

**Lo que esto cambia para el capítulo de la regla fiscal.** Deja de ser «la cláusula volvió
en 2026 y se fue en 2027». La hipótesis de trabajo es **migración**: el perímetro sale de
la Ley de Ingresos —que se renegocia cada año y el Congreso puede tocar— y pasa a una
**ley permanente que además reforma la LFPRH**, con un vehículo de contratos de terceros y
pagos diferidos. **Sigue siendo descripción de perímetro con su serie, no juicio sobre
disciplina fiscal**, conforme al límite 7 de la instrucción.

**Pendiente y no afirmado:** no se ha leído la LFIIEDB. Hasta leerla no se afirma qué
excluye, ni cuánto, ni si sustituye funcionalmente al tope de 3.6 % de 2026. Tampoco se ha
verificado si el CGPE 2027 publica el renglón «balance sin inversión», que el CGPE 2026
dejó de publicar.

### 9. Pruebas de identidad

**No corridas todavía.** Las treinta y tres están parametrizadas por ejercicio y necesitan
`_herramientas/restituciones/2027.json`, que se arma con los agregados de esta banda.
Es la primera tarea de la banda 2–8 h.

### 10. Estado al cierre de la banda

Cronómetro: **18:45 → 19:05, veinte minutos.** La banda 0–2 h queda cumplida en descarga,
marco macro y agregados; **incumplida en diff institucional y pruebas de identidad**, el
primero por falta de fuente (Ruta B) y las segundas por orden de trabajo.

**Lo que se paga con reloj por no haber quedado precargado:** nada todavía. Las rutas
probadas, el bundle de certificados y la advertencia sobre las letras de los anexos
funcionaron los tres a la primera.

---

## Banda 2–8 h

Arranca **19:05**.

### 11. Reintentos: nada se recuperó, y el diagnóstico se amplía

Segundo y tercer intento sobre todo lo que faltaba: **los cuatro analíticos del proyecto
siguen en 404**, las dos ranuras del ATDT **siguen en 503**, y los anexos **F y G de la
Gaceta siguen en 404**.

**Hallazgo de la resonda: el almacén de `PPEF2027` está caído entero.** El sitio
`ppef.hacienda.gob.mx/es/PPEF2027` responde **200** y su portada enlaza siete piezas
—CGPE, LIF, LFD, Informe de Aranceles, LISR, Proyecto de Decreto—; la subpágina
`/es/PPEF2027/exposicion_de_motivos` responde **200** y enlaza la Carta de la Presidenta,
los cuatro capítulos de la exposición de motivos, el Anexo y el **Documento Completo**.
**Los once archivos dan 404.** La subpágina de analíticos ni siquiera existe: 404.

Es el **sexto ejercicio consecutivo** con el mismo patrón —2022, 2023, 2024, 2025, 2026 y
ahora 2027—: **las páginas índice enumeran archivos que el almacén no sirve.** Lo que en
2024 se diagnosticó como «almacén roto o reubicado, no retirada de documentos» se
confirma como **estado permanente del sitio PPEF**, no como incidencia.

Consecuencia práctica: **la exposición de motivos del PPEF 2027 aparece enlistada y no se
puede bajar.** El faltante estructural del proyecto pasa de cinco documentos (2022–2026) a
**seis**.

*Nota de red, para la corrida siguiente:* el **DOF exige el host sin `www`**. El
certificado de `www.dof.gob.mx` tiene un solo SAN, `dof.gob.mx`, y curl falla con «no
alternative certificate subject name matches». Se resolvió cambiando el host, **sin
desactivar la verificación**. Va al registro de rutas junto a la cadena mal encadenada de
la SHCP.

### 12. Pruebas de identidad: **29 cierran, 0 fallan**

*Sustituye a la §9, que las declaraba no corridas.* Se escribió
`_herramientas/restituciones/2027.json` con las cifras copiadas de su documento —Anexos 1,
2 y 3 del decreto; artículo 1o. de la ILIF; Anexos II.5, II.6, III.1 y III.2 del CGPE— y
se añadió el renglón 2027 a `parametros_ejercicio.csv`.

**Cierran las veintinueve que se pueden correr.** Las mayores no dejan residuo:

- Anexo 1: ramos + los dos que van fuera del subtotal − neteo = **10,636,488.1 mdp**,
  al peso. *Los ramos 40 (INEGI) y 32 (TFJA) vuelven a imprimirse fuera del subtotal de
  autónomos, como en 2026; sin sumarlos el anexo falla por quince mil millones.*
- Artículo 1o. de la ILIF = gasto neto total del decreto, **al peso**.
- Gasto neto total − financiamientos = ingresos presupuestarios del CGPE, **al peso**.
- Las siete razones a PIB publicadas se reproducen dentro de 0.05 pp.
- La identidad flujo-acervo cierra en **0.006 pp del PIB**.

**Cuatro pruebas no corren y no cuentan como aprobadas:** las del bloque 2, que cotejan el
decreto contra los analíticos. Es la Ruta B. Se modificó `identidades.py` para que la
ausencia de analíticos **declare y siga** en vez de abortar la corrida; antes reventaba con
`FileNotFoundError` y se llevaba por delante las veinticinco pruebas siguientes.

**Cambio contra 2026 que vale la pena nombrar:** la reconciliación entre los tributarios
del CGPE y los impuestos de la ILIF da **0.0 mdp**. En 2026 había un residuo de 29.9 mdp
que hubo que nombrar en el capítulo de ingresos. Este año los dos documentos publican
6,263,886.8 y no hay nada que reconciliar.

### 13. HALLAZGO PRINCIPAL — la regla fiscal se mudó de ley, y el agregado que la mide se
partió a la mitad por redefinición

La banda anterior dejó la hipótesis de migración con una pista: el Anexo 2 del decreto y su
«nueva metodología». **Leída la ley, la hipótesis se sostiene y se puede acotar.**

**La fuente.** DOF del 9 de abril de 2026, edición vespertina, código 5784517: *Decreto por
el que se expide la Ley para el Fomento de la Inversión en Infraestructura Estratégica para
el Desarrollo con Bienestar, y se reforman y adicionan diversas disposiciones de la LFPRH*.
Archivada en `_metodologia/` y registrada en el manifiesto.

**Qué hace con la regla, en tres piezas:**

1. **Saca a las empresas públicas del cómputo.** La reforma a la LFPRH dice que «**el gasto
   de las empresas públicas del Estado no se contabilizará** dentro del gasto corriente
   estructural que se utilice como base para el cálculo de dicho límite máximo, aquél que se
   incluya en el proyecto de Presupuesto de Egresos, así como el que apruebe la Cámara de
   Diputados y el que se ejerza». **Reaparece el verbo «no se contabilizará», que había
   desaparecido de la Ley de Ingresos**: no se fue del marco fiscal, se fue de la ley anual.
2. **Crea el vehículo.** El **contrato de inversión estratégica** (artículo 116) instrumenta
   proyectos de infraestructura de largo plazo con **Vehículos de Propósito Específico**
   —personas morales o fideicomisos, con auditor externo propio (artículo 17 de la nueva
   ley)—, que pueden además operar por concesión, asignación o permiso. Y fija el criterio
   contable: «**el registro contable y presupuestal de los Proyectos para el desarrollo con
   bienestar deberá realizarse conforme a los pagos asociados a los mismos**».
3. **Autoriza el diferimiento.** El **artículo 82** permite pactar **pagos por
   diferimiento** —el pago va después de la entrega—, topados a la tasa de recargos de la
   LIF, con obligación de provisionarlos en el anteproyecto del año que corresponda.

**Lo que se ve en las cifras del paquete, y es lo que hace comparable la serie:**

| | 2026 | 2027 |
|---|---|---|
| Gasto corriente estructural (Anexo 2 del decreto) | 3,868,319.9 mdp | **1,884,958.2 mdp** |
| Límite máximo (LMGCE) | 10.9 % del PIB | **5.2 % del PIB** (2,058.5 mmp) |

**El agregado cae 51 % y el límite cae a menos de la mitad. Ninguna de las dos caídas es de
gasto: son de definición.** El propio CGPE lo deja a la vista en su cuadro de mediano plazo,
donde el renglón del LMGCE pasa de 10.9 en la columna de 2026 aprobado a **5.2 ya en la
columna de 2026 estimado**: el mismo ejercicio, restatado. **La serie del LMGCE se rompe en
2027 y no se puede encadenar con la anterior.** Queda anotado en `restituciones/2027.json`.

**Y el vehículo ya tiene cifra.** El CGPE 2027 trae un cuadro nuevo (p. 75) de contratos
LFIIEDB: **inversión de terceros 188.9 mmp y pagos diferidos 273.5 mmp**, repartidos de 2027
a 2032 y con una columna «anterior a 2027».

**Lo que NO se afirma.** No se afirma que esto sea elusión de la regla, ni que el gasto
excluido sea equivalente al que amparaba el tope de 3.6 % de 2026, ni que los pagos
diferidos sean deuda. La instrucción es explícita —límite 7— y el hallazgo se sostiene sin
necesidad de adjetivos: **describir el perímetro, publicar la serie, dejar la ruptura a la
vista.** Lo que el capítulo debe añadir todavía es el monto potencialmente excluible bajo el
paquete y su composición, que exige el desglose por empresa pública, y **eso está bloqueado
por la Ruta B.**

### 14. Estado al cierre de la banda

- **Diff institucional: sigue sin correr.** No es orden de trabajo, es falta de fuente.
- **Reclasificaciones: no documentadas**, por lo mismo.
- **Capítulos de ingresos, gasto agregado, energía, deuda y regla fiscal: no redactados.**
  Los insumos de ingresos, deuda y regla fiscal están completos y verificados; los de gasto
  agregado y energía llegan a ramo y función y no más.
- **Comparaciones estructurales extendidas: no corridas.**

**Lo que se paga con reloj por no haber quedado precargado: nada todavía.** Lo que se paga
es por fuentes que el servidor no entrega, que es distinto y no se arregla preparando mejor.

### 15. Capítulos redactados con lo que hay

Cierre de la banda a las **19:21**. Se redactaron **seis de los dieciséis capítulos**: los
cinco que la instrucción asigna a esta banda ---ingresos, ingresos energéticos, gasto total,
balance y deuda, y regla fiscal--- **más el marco macroeconómico**, que la banda anterior
había dejado con los insumos verificados y sin escribir.

**4.908 palabras de prosa y 426 cifras cuantitativas en el cuerpo**, sin contar las de los
cuadros. Ningún capítulo por debajo del presupuesto de doce afirmaciones verificables.

| capítulo | palabras | cifras |
|---|---|---|
| 01 Marco macroeconómico | 602 | 71 |
| 02 Ingresos | 766 | 76 |
| 03 Ingresos energéticos y empresas públicas | 691 | 66 |
| 04 Gasto total | 752 | 66 |
| 13 Balance y deuda | 907 | 62 |
| 14 Regla fiscal y perímetro de exclusión | 1.190 | 85 |

**Nueve cuadros generados desde datos registrados, ninguno tecleado.**
`generar_cuadros.py` los produce a partir de `datos/_fuentes.csv` ---una fila por cifra, con
su documento y su ubicación--- y de `datos/ramos.csv`, que se extrae del Anexo 1 de los dos
decretos **por clave de ramo**. Los números se formatean en el generador porque el pacto
prohíbe `siunitx`.

**Compila en Dalila:** comprobación estática **0 errores, 0 avisos**; dos pasadas de
pdflatex; **PDF de 47 páginas**; **cero cajas desbordadas**. El PDF vive en
`_entrega/documento_2027.pdf`. La ruta de los cuadros desde el maestro ---la trampa que
rompió veintiuna inclusiones en 2025 y otras veintiuna en 2026--- aguantó.

**Defecto propio, encontrado y corregido en el acto.** El extractor de nombres de ramo
juntaba palabras: la regla que arreglaba «Legislativ o» también producía «Aportacionesa
Seguridad Social» y «Agriculturay Desarrollo Rural». La causa es que `pdftotext` parte la
palabra **después de v o de x** en esta tipografía, y la regla estaba escrita sobre el
espacio en general. Corregida con esa condición, respeta los espacios reales.

**Dos decisiones de contención, ambas declaradas en el propio documento y no sólo aquí:**

1. **La descomposición del cambio del SHRFSP no se publica.** Su criterio de aceptación es
   reproducir la caída de 2022 antes de aplicarla a 2027, y la serie histórica no está en
   forma legible por máquina. Publicar cuatro componentes que suman el total por
   construcción, sin haber pasado la prueba, sería peor que no publicarlos. **La identidad
   flujo-acervo que sí se corrió está en el capítulo: cierra en 0,006 pp del PIB.**
2. **La caída del Ramo 18 Energía ---181.804,9 mdp, 69,2 % real--- se reporta como magnitud
   sin explicación.** Es el movimiento más grande del Anexo 1 y separar reducción de
   reclasificación exige el analítico ausente. El CGPE ofrece una pista propia ---menor
   línea para amortizaciones de deuda de Pemex en inversión financiera--- que **se cita como
   explicación de la fuente y no como verificación nuestra.**

**Un error propio de redacción, cazado antes de compilar.** El capítulo de la regla fiscal
decía «durante nueve ejercicios la exclusión vivió en el mismo lugar». Son **siete**: 2018 a
2023 y 2026. Los ejercicios 2024 y 2025 no tuvieron cláusula, cosa que la serie del propio
capítulo publica dos párrafos antes. **Ninguna comprobación estática lo veía**, igual que la
inconsistencia de la nota de método que se corrigió en la precarga: la cifra era correcta en
la tabla y falsa en la frase.

**Lo que sigue sin poder redactarse:** los ocho capítulos sectoriales de la banda 8--24 h
dependen del corte por función y del analítico por programa. Bajo Ruta B, salud, educación,
pensiones, inversión, seguridad, gasto federalizado, medio ambiente y anexos transversales
**sólo alcanzan el nivel de ramo**, y el capítulo de anexos transversales **no es redactable
en absoluto**: su única fuente es el CSV de anexos transversales del ATDT, que responde 503.

### 16. Resonda de los analíticos, 19:22–19:26

Nada se recuperó. Pero la resonda **separa dos fallas que hasta ahora se contaban juntas**,
y la distinción cambia el pronóstico.

**Falla A — no publicado todavía (`pef.hacienda.gob.mx`).** Los cuatro analíticos del
proyecto siguen en 404, y también el directorio que los contendría: `/Analiticos_Historico/2027/`
responde **404**, igual que `/es/PEF2027`. **Control corrido en la misma pasada:** el mismo
archivo del ejercicio 2026 ---`/2027/` sustituido por `/2026/`--- responde **200** con
`content-type` de xlsx. **La ruta es correcta y el árbol del ejercicio 2027 no existe
aún.** Se probaron además cuatro variantes ---`/Autorizado/`, sin segmento de etapa,
`/PPEF/`, y la extensión en mayúsculas---: las cuatro, 404.

**Falla B — publicado y no servido (`ppef.hacienda.gob.mx`).** Distinta cosa: ahí las
páginas índice **sí existen y sí enumeran los archivos**, y los archivos dan 404. Va por el
sexto año.

**Por qué importa la distinción.** La falla B lleva seis ejercicios sin resolverse y no hay
razón para esperar que se resuelva. **La falla A es un árbol que todavía no se crea**, y en
2026 ese mismo árbol acabó existiendo: es razonable esperar que aparezca en horas o días.
**La Ruta B es, por tanto, provisional por motivo distinto en cada caso**: la exposición de
motivos del PPEF probablemente no llegue nunca; los analíticos, probablemente sí.

**Las otras dos paradas del orden que fija la instrucción, agotadas:**

- **Portal de datos abiertos.** `package_search` devuelve los dos paquetes esperados, y sus
  recursos **siguen apuntando a 2026**: `PPEF_2026.csv` (metadato del 24 de febrero de 2026)
  y `anexos_transversales_ppef2026.csv`. **El 503 de las ranuras de 2027 no es una caída
  temporal: es la respuesta a una ranura que no existe.** La ranura de 2026 sigue viva
  (200), de modo que todavía no ha sido sobrescrita.
- **Transparencia Presupuestaria.** `/es/PTP/Datos_Abiertos` responde 200 con **1.923 bytes
  de cáscara JS, cero enlaces a archivo, sin la cadena «PPEF» ni «2027»**. Es el mismo
  hallazgo de la corrida 2024, que midió 1.919 bytes. Dos años después, idéntico.

**Recomendación operativa para lo que sigue:** vigilar `/Analiticos_Historico/2027/Proyecto/`
y las dos ranuras del ATDT. En cuanto respondan, se pasa a Ruta A, se declara la hora del
cambio, se corre el diff institucional y se desbloquean los ocho capítulos sectoriales y el
monto excluible del capítulo de la regla fiscal. **Hasta entonces el documento no cambia de
altitud.**

---

## Banda 8–24 h (adelantada)

Arranca **19:26**, al cerrar el sondeo. Cierre de esta sección: **19:58**.

### 17. Los ocho capítulos sectoriales, redactados en Ruta B

**Catorce de los dieciséis capítulos quedan escritos**: los seis de la banda anterior más
salud, educación, pensiones, inversión, seguridad, gasto federalizado, medio ambiente y
**anexos transversales**. Faltan el resumen ejecutivo, el horizonte demográfico y las
implicaciones finales.

**10.011 palabras de prosa y 881 cifras cuantitativas** en el cuerpo, sin contar cuadros.
**Dieciocho cuadros**, todos generados desde datos registrados. Compilación: **0 errores
estáticos, 53 páginas, cero cajas desbordadas.**

**Corrección de la §15.** Esa sección declaró el capítulo de anexos transversales «no
redactable en absoluto». **Era falso y la falla era nuestra**: se supuso que su única fuente
era el CSV del ATDT. **Los anexos transversales están impresos en el propio decreto**, con su
renglón «Total general», y se leyeron los diecisiete que existen en los dos ejercicios. Lo
que el 503 sí impide es la **auditoría de etiquetado** ---qué programas están en más de un
anexo--- y así queda declarado dentro del capítulo.

### 18. HALLAZGO — el CGPE deflacta con el índice al consumidor, no con el deflactor del PIB que declara

El CGPE 2027 escribe su deflactor con tres decimales en la fórmula del LMGCE (p. 25):
**π₂₇ = 4,04 %**, y lo publica redondeado a 4,0 en el Anexo III.1.

**Sus cuadros presupuestales no están calculados con él.** Despejando el deflactor implícito
de los nueve renglones de la clasificación económica del gasto ---donde publica nivel 2026,
nivel 2027 y variación real--- se obtiene 1,0318 · 1,0322 · 1,0326 · 1,0328 · 1,0326 ·
1,0325 · 1,0320 · 1,0339 · 1,0321. **Mediana 1,0325**, que es la **inflación promedio del
INPC proyectada para 2027, 3,2 %**, publicada en su propio Anexo II.5.

**La diferencia es sistemática y vale unos 0,8 puntos porcentuales.** Donde el CGPE imprime
+3,6 % real de inversión física, este documento imprime +2,8 %.

Es exactamente lo que el recuadro del deflactor de este proyecto prohíbe: **índice al
consumidor en un cuadro presupuestal.** Lo comete la fuente oficial, en el documento que
declara el deflactor correcto tres páginas antes. Va al recuadro de la nota de método, que
crece con una subsección propia, **y no se corrige ninguna cifra del CGPE**: se citan como
las publica y se advierte qué convención usa cada una.

### 19. La caída del Ramo 18 dejó de estar sin explicar

La §15 registró como decisión de contención que los 181.804,9 mdp del Ramo 18 se reportaban
«como magnitud sin explicación». **Al leer la clasificación económica apareció la respuesta,
publicada por la fuente**: la contracción es del programa **«Articulación de la Política de
Hidrocarburos»**, que pasa de **263.476,0 a 81.100,0 mdp** «como resultado de la
reformulación de la estrategia de rescate financiero de Pemex».

**La aritmética cierra contra el decreto y eso es lo que aporta el documento:** la caída del
programa es de 182.376,0 mdp y la del ramo completo de 181.804,9; **la diferencia, +571,1
mdp, es lo que el resto del ramo gana**. Un solo programa explica el movimiento más grande
del presupuesto de 2027. Los capítulos 3, 4 y 8 quedaron actualizados.

### 20. Dos comprobaciones nuevas que cierran al peso

- **Los ocho fondos del Ramo 33 suman su total** en los dos ejercicios: 1.041.892,8 contra
  1.041.892,9 en 2026 y 1.136.351,5 contra 1.136.351,6 en 2027. Valida la lectura del
  Anexo 22 contra el Anexo 1.
- **El perímetro pensionario coincide por dos caminos independientes**: la diferencia de los
  dos renglones del Anexo 3 del decreto (1.840.746,1 mdp) y la línea «Pensiones y
  jubilaciones» de la clasificación económica del CGPE (1.840,7 mmp), en 2027 y en 2026.

### 21. Hallazgos menores del ejercicio

- **Anexo 33, «Diversidad sexual y de género», es nuevo**: 43.369,4 mdp, no existía en 2026.
- **Los anexos transversales cambiaron de forma**: en 2027 traen columnas de objetivo, ramo,
  programa presupuestario y acción transversal. El de igualdad **pasa de cuatro a diecisiete
  páginas**. Es más información publicada, aunque esta corrida no haya podido explotarla.
- **Cuatro fondos del Ramo 33 crecen exactamente 3,0 % real** ---FAIS, FORTAMUN, FAM y
  FAFEF---: están atados por fórmula a la recaudación federal participable. **El FONE, que no
  lo está, explica el 64 % del aumento del ramo.**
- **Casi nueve de cada diez pesos que gana el FONE son servicios personales**: 54.536,5 de
  60.481,4 mdp.
- **No se publica ninguna cifra de la Guardia Nacional.** Sin diff no se puede separar cambio
  de ramo de reducción propia, que es justamente el caso didáctico de 2026.

### 22. Error propio corregido antes de compilar

En el capítulo de gasto federalizado, la suma de los cuatro fondos indexados decía
**27.989,1 mdp** y son **27.989,5**. Se recalculó desde el CSV en vez de rehacer la cuenta a
mano.

### 23. Lo que falta

**Capítulos:** resumen ejecutivo, horizonte demográfico e implicaciones finales.
**Bandas:** la compuerta semántica sobre todos los titulares, las fichas ya escritas, la
checklist de omisiones y el empaquetado. **Y todo lo que dependa de la Ruta A**, que el
sondeo automático vigila cada media hora.

### 24. Los tres capítulos que faltaban, 19:58–20:10

**Los dieciséis capítulos quedan escritos. Ninguno se declaró no redactable.** Se cerraron el
resumen ejecutivo, el horizonte demográfico y las implicaciones.

**13.136 palabras y 1.057 cifras** en el cuerpo de los veinte archivos de capítulo,
**diecinueve cuadros** generados desde datos registrados, **57 páginas**. Comprobación
estática **0 errores y 0 avisos**; **cero cajas desbordadas** tras cuatro reescrituras de
fichas donde una ruta larga en tipo de máquina no cabía en la caja. Queda un solo aviso de
caja **subllena**, dentro del recuadro de un titular, que es cosmético e inevitable en texto
enmarcado.

**Capa demográfica aplicada, con la regla de separación intacta.** El cuadro de indicadores
no trae un solo peso y el de razones por persona no trae un solo agregado presupuestal, como
manda la nota de método.

**Hallazgo del capítulo demográfico, y es el que da vuelta al documento:**

| | monto | población | por persona |
|---|---|---|---|
| Perímetro pensionario | **+3,9 % real** | 65 y más: **+4,29 %** | **−0,4 % real** |
| FONE | **+6,8 % real** | edad escolar básica: **−0,95 %** | **+7,8 % real** |

**El mismo paquete que aumenta las pensiones en pesos las reduce por cabeza, y el que
aumenta menos la educación la aumenta más por persona.** Las dos lecturas son correctas y dan
signos opuestos; sólo se ven al dividir. **Un documento que se quede en los montos concluirá
que el paquete favorece a las pensiones sobre la educación; por persona ocurre lo
contrario.**

**Tres denominadores que se buscaron y NO se usaron, cada uno con su razón escrita en el
capítulo:** el registro de IMSS-Bienestar, porque es padrón de registro de cobertura parcial
y no medición de quién carece de afiliación; los asegurados del IMSS, porque **asegurados no
es derechohabientes** y el cociente daría una cifra varias veces mayor que la verdadera; y
CELADE, que no se pudo obtener y cuyo sustituto declarado es el contraste con el Banco
Mundial ---una diferencia sistemática de entre 1,05 y 1,16 % que **movería todas las razones
por persona alrededor de un punto**---.

**La demostración del denominador, publicada a propósito:** el mismo FONE de 2027 da
**24.102 pesos** por persona en edad escolar básica y **26.564** por alumno inscrito. Los dos
denominadores difieren **10,2 %**. Va en el cuadro, en dos renglones consecutivos, para que se
vea.

**Sobre el paquete y la demografía:** el CGPE proyecta finanzas públicas a 2032 y **no publica
proyección demográfica propia ni asocia sus supuestos de gasto a la población**. La población
en edad escolar básica lleva años cayendo y el documento no lo menciona al justificar el gasto
educativo. **No se afirma que la omisión sea deliberada**; se afirma que el vínculo no está
publicado.

**Limpieza:** se borró `C0_1.tex`, el cuadro de relleno del esqueleto, que quedó huérfano al
sustituirse los dieciséis capítulos. La comprobación estática lo detectó como «generado y no
incluido».

**Lo que sigue abierto:** `99_registro.tex` conserva su estructura de esqueleto y hay que
llenarlo con los denominadores que no se obtuvieron y los renglones fuera de alcance. Faltan
además la compuerta semántica sobre los dieciséis titulares, la checklist de omisiones
renglón por renglón, y el empaquetado de la entrega.

### 25. Compuerta semántica y registro, 20:20–20:35

**Compuerta semántica: trece frases reescritas, ninguna cifra modificada.** Se aplicó a los
dieciséis titulares, a las frases del resumen ejecutivo y a los pies de los diecinueve
cuadros, conforme a `_aprendizaje/compuerta_semantica.md`. En 2026 fueron diez frases; este
año trece.

| capítulo | qué decía y por qué excedía |
|---|---|
| Ingresos | Afirmaba que el total no se mueve **porque dos renglones se cancelan**. No se cancelan: los impuestos ganan 425.345,7 mdp y las ventas pierden 173.433,7. La razón real es que el crecimiento nominal, 4,3 %, apenas supera al deflactor de 4,0 %. **Era una causa inventada, no un perímetro ancho.** |
| Energéticos | Atribuía la caída de ingresos petroleros a **la plataforma de exportación**, que la fuente no nombra como causa, y **omitía el tipo de cambio**, que sí nombra. Se reescribe con la atribución de la fuente. |
| Gasto total | «El de 2026 **con la inflación encima**». La actualización es por el deflactor del PIB, y en este documento esa distinción es el hallazgo §18. |
| Salud | Llamaba «vehículos presupuestales **de salud**» a cinco agregados de los que dos ---IMSS e ISSSTE--- pagan pensiones con la misma bolsa. |
| Educación | «El mayor aumento de los ramos administrativos **grandes**» no era verificable: Marina crece 18,5 % y Agricultura 13,5 %. Se sustituye por **el mayor aumento en pesos**, que sí lo es. |
| Federalizado | «Una proporción mayor de **lo que transfiere**» abarcaba convenios, Ramo 23 y Ramo 25, que el propio capítulo declara fuera de perímetro. Se acota a los dos ramos y se publica la proporción: **41,7 a 42,3 %**. |
| Deuda | El balance se comparaba contra el aprobado y el acervo contra el estimado, **sin decirlo**. El titular viaja solo y ahora declara su base. |
| Regla fiscal | «La exclusión **cambió de ley**», como hecho establecido. Son **dos cómputos distintos** ---equilibrio presupuestario contra límite de gasto corriente estructural--- y la migración es la hipótesis de trabajo del cuerpo, no un hecho verificado. |
| Horizonte (×2) | «Las pensiones… **por cabeza**» excedía el perímetro del Anexo 3 e invitaba a leer una prestación media. Y decía que los montos «favorecen a las pensiones sobre la educación» cuando **en tasa el FONE crece más** (6,8 % contra 3,9 %): comparaba niveles y tasas sin decir cuál. |
| Implicaciones | Misma corrección que el capítulo de la regla fiscal. |
| Resumen (×2) | «El movimiento más grande **del presupuesto**» no es verificable sin el analítico por programa; lo verificable es que es el mayor **entre ramos**. Y la misma equivalencia no establecida de los dos cómputos. |

**Dos observaciones de rúbrica.** La primera: **cuatro de las trece no eran perímetros
anchos sino causas o comparaciones mal planteadas** ---una causa inventada, una atribución
que contradice a la fuente, un superlativo no verificable y una comparación de tasas
presentada como de niveles---. La compuerta las atrapó igual, porque el paso 3 obliga a leer
el sujeto contra la ficha. **La regla incorporada en la precarga ---«cuando la frase compara
dos crecimientos, dice si compara tasas o niveles»--- se ganó su lugar: cazó el caso de
Horizonte.**

La segunda: **los dos capítulos con más reescrituras son Horizonte y el par regla
fiscal--implicaciones**, y en los dos el problema era el mismo: un hallazgo fuerte empuja al
titular a decir más de lo que el cálculo sostiene. **Es señal de perímetro mal declarado, no
de redacción descuidada**, y así lo dice el propio artefacto.

**Registro (`99_registro.tex`) lleno**, con sus cinco secciones: lo imposible bajo lectura
en vivo; **cinco denominadores que se buscaron y no se usaron**, cada uno con su razón; lo
declarado fuera de alcance, separado en **lo que el servidor no entregó** y **lo que se
decidió por método**; las **tres discrepancias de la fuente que este documento no resuelve**;
y la **declaración de capítulos no redactables: ninguno**.

**Compilación:** comprobación estática 0 errores y 0 avisos; **60 páginas**. Queda **una caja
desbordada de 1,5 puntos** ---medio milímetro, invisible en página--- en un párrafo del
registro que resistió tres reescrituras, y una caja subllena dentro del recuadro de un
titular. **Se declaran en vez de afirmar cero.**

### 26. Checklist de omisiones, renglón por renglón, 20:50–21:00

Veintitrés renglones ---los veintidós de la lista más el que la lista aprendió a incluir
sola---. **Ninguno queda PENDIENTE**, que es la única condición que el artefacto impone al
compilar.

**Resultado: 4 hechos · 6 parciales · 12 fuera de alcance · 1 no adoptado.**

| # | renglón | estado |
|---|---|---|
| A1 | Gasto en salud por persona afiliada, por subsistema | **PARCIAL** — las fuentes están precargadas, pero ninguna sirve como denominador comparable: IMSS da asegurados, ISSSTE da derechohabientes y IMSS-Bienestar es padrón parcial. **Se declara el porqué en el registro y no se publica el cociente.** |
| A2 | Gasto por alumno, por nivel educativo | **PARCIAL** — hecho para básica, con los dos denominadores en renglones contiguos (24.102 contra 26.564 pesos). **Por nivel exige el analítico.** |
| A3 | Padrones de programas pensionarios no contributivos | **FUERA DE ALCANCE** — precargado, pero cruzarlo con el perímetro del Anexo 3 exige el analítico |
| A4 | Perímetro de exclusión de la regla fiscal | **HECHO** — capítulo propio, y con el hallazgo de la migración a la LFIIEDB |
| B1 | Vara externa de suficiencia en salud (6 % del PIB) | **FUERA DE ALCANCE** — tercer año, **pero por razón distinta**: el numerador exige la clasificación funcional a nivel de función y el CGPE la publica sólo por grupo |
| B2 | Contraste del marco macro con pronósticos externos | **FUERA DE ALCANCE por decisión, no por fuente.** Las dos fuentes estaban disponibles |
| B3 | Comparación contra los Pre-Criterios | **HECHO EN ESTA PASADA** |
| B4 | LMGCE contra el observado | **HECHO** — holgura de 173.541,8 mdp, y es identidad en el guion |
| B5 | Ramo 54 como proporción del anexo de igualdad | **HECHO EN ESTA PASADA** — 0,36 % |
| B6 | Convenios de reasignación | **FUERA DE ALCANCE** — analítico |
| B7 | Federalismo más allá de los Ramos 28 y 33 | **FUERA DE ALCANCE** — analítico |
| B8 | Balances de las empresas públicas con y sin apoyos | **FUERA DE ALCANCE por decisión** |
| B9 | Cuidados: qué parte del anexo es preexistente | **PARCIAL** — el total y su variación (−1,9 % real); el desglose por programa, no |
| B10 | Género: concentración y qué proporción son pensiones | **FUERA DE ALCANCE** — el 503 del CSV de anexos |
| B11 | Medio ambiente y agua como política | **PARCIAL y limitado, como la propia lista anticipó**: la exposición de motivos del PPEF no se publica, sexto año |
| C1 | Series largas desde 2013 | **FUERA DE ALCANCE.** La mitigación barata que la lista proponía ---los analíticos del proyecto desde 2021--- **tampoco sirve este año**, porque los de 2027 son justamente los que faltan |
| C2 | Desigualdad pensionaria | **FUERA DE ALCANCE** — fuente no disponible en vivo |
| C3 | Gasto de bolsillo en salud | **FUERA DE ALCANCE** — fuente no disponible en vivo |
| C4 | Política tributaria en detalle | **PARCIAL** — cambios de tasa y base de los anexos D y E; **el anexo F, Código Fiscal, dio 404** |
| C5 | Inversión por sector con nombre de proyecto | **FUERA DE ALCANCE** — sin analítico no hay ni claves |
| C6 | Incidencia distributiva completa | **FUERA DE ALCANCE por decisión de la instrucción** |
| C7 | El espacio fiscal como cifra única | **NO SE ADOPTA**, y la diferencia de enfoque se declara |
| — | Fondos y programas nuevos que no detectamos | **PARCIAL** — sin diff no hay altas de programa. Sí se comprobó que **las cuarenta claves de ramo no cambiaron** y que los ocho fondos del Ramo 33 son los mismos, y **se detectó el Anexo 33 nuevo** |

**Dos renglones se cerraron en esta pasada porque correr la lista los encontró
alcanzables.** No estaban en el plan de la banda:

1. **B3, los Pre-Criterios.** `precgpe_2027.pdf` responde 200 en el portal de la Secretaría.
   Se descargó, se registró (manifiesto: 110 archivos) y se comparó. **Es lo que el mismo
   Ejecutivo proyectaba el 6 de abril contra lo que entregó el 8 de septiembre**, y las dos
   revisiones grandes van en sentidos contrarios: el **precio del petróleo sube de 54,7 a
   61,8 dólares por barril**, un supuesto 13 % más alto, mientras el **crecimiento se revisa
   a la baja cuatro décimas en los dos extremos del rango** y el **tipo de cambio se aprecia
   sesenta centavos**. Hallazgo lateral que cierra un cabo suelto del capítulo macro: los
   Pre-Criterios explican la brecha entre el PIB aprobado y el estimado de 2026 ---**la
   revisión del INEGI a la serie histórica de 2023 y 2024**---.
2. **B5, el Ramo 54.** La dependencia que lleva el nombre de la política tiene **2.269,4
   mdp: el 0,36 % del anexo de igualdad**, que vale 636.133,1. Es la cifra pequeña y elocuente
   que la lista pedía desde 2026.

**El renglón que más pesa sigue abierto, y hay que decirlo sin adornos.** **B1, la vara de
suficiencia en salud, queda fuera por tercer ejercicio consecutivo.** Este año la razón es
de fuente y no de olvido ---el CGPE publica la clasificación funcional sólo por grupo, y el
desglose por función vive en el analítico que dio 404---, pero **el resultado para el lector
es el mismo tres años seguidos**. Va al registro con esa redacción.

**Error propio de esta pasada, corregido antes de compilar:** el capítulo macro decía que el
tipo de cambio «se aprecia seis centavos» cuando 18,5 a 17,9 son **sesenta**.

### 27. Entrega empaquetada, 21:00

En `documento_2027/_entrega/`:

| pieza | tamaño |
|---|---|
| `documento_2027.pdf` | 557 KB, **61 páginas** |
| `documento_2027.zip` | 104 KB, proyecto LaTeX portátil |
| `documento_2027.md` | 128 KB, 2.155 renglones |
| `datos/` | `_fuentes.csv` (136 filas) más `ramos.csv`, `ramo33.csv`, `anexos.csv` |

**El ZIP se probó en un directorio limpio y pasó las dos pruebas**: `generar_cuadros.py`
regenera los diecinueve cuadros y `pdflatex` produce **61 páginas cuyo texto extraído tiene
el mismo sha256** que el PDF de la entrega. Idéntico, no equivalente.

**Defecto de portabilidad encontrado en esa prueba y corregido.** La primera versión del ZIP
compilaba pero **no regeneraba**: `generar_cuadros.py` leía dos CSV de fuera del documento
---la serie del perímetro y la población de CONAPO--- que no viajaban en el paquete. Se
copiaron a `datos/` y la función de rutas ahora **prefiere el original del árbol del proyecto
y cae en la copia local cuando no está**. Un ZIP «portátil» que sólo compila con los cuadros
ya cocinados no es portátil.

**El conversor a Markdown es nuevo** (`a_markdown.py`), porque el de 2026 leía los cuadros de
CSV y aquí ya son `.tex` generados. **No repite el defecto de 2026**: la limpieza de
comentarios usa el lookbehind, y la comprobación de salida cuenta **cero renglones terminados
en diagonal suelta** contra los 218 de aquel entregable.

**LEEME.md de la entrega**: comando de compilación, versión exacta del motor ---TeX Live
2026, TinyTeX, `tlmgr` 79639, pdfTeX 1.40.29---, las restricciones de portabilidad que el
proyecto respeta, qué hay en cada carpeta, y la advertencia del deflactor, que es lo primero
que necesita quien compare nuestras cifras con las del CGPE.

---

## Cierre de la sesión, 2026-09-08T21:47

**Cronómetro: 18:45 → 21:47, tres horas y dos minutos.** El sondeo automático queda
**detenido** por instrucción de Héctor; corrió cada media hora desde las 19:26 y en sus
ocho pasadas los seis recursos siguieron caídos.

**Estado al cierre.**

- **La corrida cumple el criterio de entrega**: PDF de 61 páginas, ZIP portátil probado en
  directorio limpio, Markdown y datos, todo en `documento_2027/_entrega/`.
- **La Ruta B sigue vigente.** Último sondeo a las 21:45: los cuatro analíticos en 404 y las
  dos ranuras del ATDT en 503.
- **Todo commiteado** en la rama `p3-correcciones-tex`: `87932b6` la adquisición, `1eded47`
  el documento.

**Lo primero que hay que hacer al retomar**, en este orden:

1. **Sondear los seis recursos.** Si el árbol `Analiticos_Historico/2027/Proyecto/` existe,
   se pasa a **Ruta A**, se declara la hora, y se desbloquean de golpe: el diff
   institucional, la auditoría de etiquetado de los anexos transversales, el monto
   potencialmente excluible del capítulo de la regla fiscal, la separación entre atención
   médica y pensiones en el IMSS y el ISSSTE, el destino de los 571,1 mdp restantes del
   Ramo 18, y siete renglones de la checklist que hoy están fuera de alcance.
2. **Vigilar la ranura de plazas del ATDT**, que hoy respondía 200 sirviendo todavía el
   archivo de 2026. **El día que se sobrescriba, lo de 2026 desaparece**; ya está en
   carpeta, pero la de 2027 hay que tomarla el mismo día.
3. **Reintentar los anexos F y G de la Gaceta** y la exposición de motivos del PPEF, sin
   esperar nada: son las fallas que llevan seis años.

**Lo que NO hay que rehacer.** Las identidades, la compuerta semántica y la checklist ya
corrieron sobre el documento tal como está. Si llega la Ruta A y se reescriben capítulos,
**las tres se vuelven a correr**, porque validan el texto que hay, no el que hubo.

---

## Retoma, 2026-09-09T07:33-06:00

Se ejecuta el orden anotado al cierre. Los dos primeros renglones no mueven nada; el
tercero, que se anotó «sin esperar nada», resultó ser el que cambia el documento.

### 28. Sondeo de los seis recursos: sin cambio, la Ruta B sigue vigente

| recurso | respuesta 09-08 21:45 | respuesta 09-09 07:33 |
|---|---|---|
| `…/Analiticos_Historico/2027/Proyecto/ac01_ra_pp_ur_og.xlsx` | 404 | **404** |
| `…/2027/Proyecto/ac01_ra_f_ur_og.xlsx` | 404 | **404** |
| `…/2027/Proyecto/ac01_ra_pp_ur_og_efe.xlsx` | 404 | **404** |
| `…/2027/Proyecto/ac01_ra_f_ur_og_efe.xlsx` | 404 | **404** |
| `…/PPEF_2027.csv` (ATDT) | 503 | **503** |
| `…/anexos_transversales_ppef2027.csv` (ATDT) | 503 | **503** |

**No hay Ruta A.** El diff institucional, la auditoría de etiquetado y los otros cinco
renglones bloqueados siguen bloqueados. Nada de lo que el documento declara como fuera
de alcance cambia de estado.

**La ranura de plazas del ATDT tampoco se ha sobrescrito.** `last-modified`
2026-06-03T19:03:11 y `content-length` 11 663 197: el mismo archivo de 2026 que ya está
en carpeta. Sigue en vigilancia.

### 29. Los anexos de la Gaceta: las letras se movieron después de la entrega

Se reintentaron F y G. Responden **200**, pero **no traen lo que el índice del día de la
entrega decía que traían**. El índice se volvió a bajar y se comparó con el que se guardó
a las 18:51 del 8 de septiembre. Diferencia, textual:

```
 Anexo F
-Que reforma, adiciona y deroga diversas disposiciones del Código Fiscal de la Federación
+Que reforma y adiciona diversas disposiciones de la Ley Aduanera
 Anexo G
+Que expide la Ley de Economía Digital para Pagos Digitales y Electrónicos
+Anexo H
+Que expide la Ley General para el Fortalecimiento y Armonización Catastral y Registral
+Anexo J
 Informe sobre el uso de la facultad conferida al Ejecutivo Federal en materia arancelaria…
```

**Tres cosas pasaron a la vez, y ninguna es la que se supuso el día de la entrega.**

1. **La iniciativa de Código Fiscal desapareció del índice.** No se sirvió nunca —404 en
   tres intentos el día 8— y el 9 su renglón ya no existe. Lo que ocupa la letra F es una
   reforma a la **Ley Aduanera**.
2. **Se insertaron dos iniciativas que no estaban**: la **Ley de Economía Digital para
   Pagos Digitales y Electrónicos** (G) y la **Ley General para el Fortalecimiento y
   Armonización Catastral y Registral** (H).
3. **El informe arancelario del artículo 131 se recorrió de G a J.** No cambió de
   contenido: cambió de letra porque le metieron dos anexos delante.

**Y hay cuatro anexos más que el índice todavía no lista.** K, L, M y N se sirven y el
índice vivo no los menciona; sólo aparecen en un bloque **comentado en el HTML**, con
letras viejas (H, J, K, L) y fechados **2026**. Los PDF dicen **2027**. El índice va
atrás del almacén en un sentido y adelante en el otro.

**Mapa real de letras al 2026-09-09T07:40**, leído de los PDF servidos, no del índice:

| letra | contenido | pp | creado (metadato del PDF) |
|---|---|---|---|
| A | ILIF 2027 | — | 09-08 |
| B | PPEF, proyecto de decreto | — | 09-08 |
| C | CGPE 2027 | — | 09-08 |
| D | Ley Federal de Derechos | — | 09-08 |
| E | Ley del Impuesto sobre la Renta | — | 09-08 |
| **F** | **Ley Aduanera** | 28 | 09-08 19:18 |
| **G** | **Ley de Economía Digital** | 22 | 09-08 19:06 |
| **H** | **Ley Catastral y Registral** | 28 | 09-08 19:08 |
| **J** | Informe arancelario, art. 131 | 12 | 09-08 19:54 |
| **K** | Nota metodológica y declaratoria **ZAP 2027** | 18 | **09-09 05:29** |
| **L** | Listado **ZAP rurales 2027** | 244 | **09-09 05:38** |
| **M** | Listado **ZAP urbanas 2027** | 224 | **09-09 05:41** |
| **N** | Estimación de subsidios de **vivienda y suelo 2027** | 6 | **09-09 05:46** |

**A, C, D y E se volvieron a bajar y son idénticos byte a byte** a los que están en
carpeta (sha256 sin cambio). Lo que se movió es la cola del paquete, no la cabeza.

**El 404 de la Gaceta es intermitente, no definitivo.** El anexo L respondió **404 a las
07:34 y 206 a las 07:38**, misma URL, cuatro minutos de diferencia. Eso corrige la lectura
del día 8: el «almacén roto» de la Gaceta **no retira archivos, los sirve tarde y de forma
inestable**. La regla de dos intentos alcanza para no bloquear la corrida, pero **no
alcanza para dar por inexistente un anexo**.

**Lección para la precarga 2028, que es más dura que la de 2027.** El aviso vigente decía
«las letras no son fijas: léelas del índice». **No basta.** El índice se reescribe después
de la entrega y las letras se reasignan. La regla nueva: **la letra no identifica nada;
identifica el PDF, por su primera página**, y el índice se guarda con marca de tiempo cada
vez que se consulta, porque es un documento que cambia.

### 30. Lo que llegó, y qué de eso es utilizable

Ocho anexos nuevos y una segunda copia del índice en `2027/`, registradas en el manifiesto, que pasa de 109 a 118 registros, 18 de ellos del ejercicio 2027:

**Las tres iniciativas de ley y el informe arancelario vienen escaneados.** F, G, H y J
tienen capa de texto **sólo en la portada y el colofón** —2 de 28, 2 de 22, 2 de 28 y 2 de
12 páginas—. El cuerpo es imagen. Sin OCR no son legibles por máquina, y el OCR de un
texto legal no se usa para citar cifras sin cotejo a mano. **Se archivan; no se explotan en
esta pasada.**

**Los cuatro anexos de Bienestar sí traen texto completo** (K 17/18, L 243/244, M 224/224,
N 6/6). Dos hallazgos con cifra:

1. **La vara de suficiencia en vivienda, que el documento no tenía.** El anexo N es la
   estimación que ordena el artículo 61 de la Ley de Vivienda: **226 133,3 mdp** es el
   monto que la Secretaría de Bienestar declara necesario para cumplimentar la política de
   subsidios de vivienda y suelo en 2027. Se compone de 849 226 hogares que requieren
   mejora, 771 091 ampliación y 36 246 vivienda nueva, costeados a 25, 50 y 100 UMA. El
   **Ramo 15 completo** del PPEF 2027 son **37 873,6 mdp**: el **16,7 %** de esa cifra, y
   el ramo es mucho más que subsidios de vivienda. *Advertencia obligatoria al usarla:*
   los costos unitarios salen de las Reglas de Operación **de 2026** y de la **UMA de
   2026**, de modo que el requerimiento está en pesos de 2026 y el presupuesto en pesos de
   2027; y CONAVI es un descentralizado, así que la comparación es de orden de magnitud a
   nivel de ramo, no un cierre contable.
2. **La declaratoria ZAP 2027.** 1 575 municipios rurales prioritarios en las 32
   entidades, y 43 636 AGEB urbanas en 4 531 localidades de 2 423 municipios. La
   construcción es acumulativa y está documentada criterio por criterio (790 por
   marginación → 796 con rezago social → 953 con municipios indígenas → 959 con
   afromexicanos → 1 383 con incidencia delictiva → 1 621 con pobreza extrema → 1 638 con
   grado de accesibilidad → 1 645 con municipios de creación reciente → 1 575 al pasar 70
   urbanos a la lista urbana).

**Ruta nueva que aparece en la nota metodológica y que la precarga no tenía:**
`sisge.bienestar.gob.mx/dae/zap2027/zap_urbanas_2027_43636_variables_descarga.zip`, las
43 636 AGEB con sus variables. Va al registro de rutas.

### 31. La adenda: decisión, y qué se volvió a correr

**Decisión de Héctor: adenda fechada.** El cuerpo de los dieciséis capítulos **no se
reescribe**: es el artefacto de la corrida del 8 de septiembre y se conserva como tal. Lo
que llegó después entra en un capítulo nuevo, `99b_actualizacion.tex`, fechado el 9, que
declara en su primer párrafo qué es y qué no es.

**Lo que la adenda contiene.** El sondeo sin cambio y la vigencia de la Ruta B; la
reasignación de letras con el cuadro C99.1, que es el mapa real leído de los PDF; la vara de
vivienda con el cuadro C99.2 y sus tres advertencias; y la declaratoria ZAP 2027, registrada
como denominador disponible pero **no cruzada con el gasto**, porque cruzarla exige la
distribución territorial y ésa sigue enganchada a la Ruta A.

**Corrección en el sitio, dentro del §99.** El renglón que decía que los anexos F y G eran
el Código Fiscal y el informe arancelario se reescribe: el 404 era cierto, la descripción no.
Remite a la adenda.

**Las tres verificaciones se volvieron a correr.**

- **Identidades: de 29 a 41 pruebas, 0 fallan.** Las doce nuevas son de la cola del paquete:
  los tres montos de vivienda contra hogares por costo unitario, los tres desgloses
  urbano-rural del Cuadro 1 contra los hogares del Cuadro 3, la UMA implícita en los tres
  costos ---3.566,22 en los tres, que es la UMA mensual de 2026---, las dos sumas del total
  (226.133.296.956 pesos y 63.409.800 UMA) y la aritmética de los municipios de la ZAP
  (1.645 − 70 = 1.575). Las cifras viven en el bloque `gaceta_cola` de
  `restituciones/2027.json`; el guion no las lleva dentro, conforme a la separación del
  archivo.
- **Compuerta semántica: tres frases reescritas, ninguna cifra modificada.** Todas por
  sujeto más ancho que su cálculo: (1) el titular decía «el Ramo 15 completo son 37.873,6
  mdp: el 16,7 % de esa cifra» sin advertir que el ramo es mucho más que subsidios de
  vivienda; (2) «el vehículo presupuestal completo que podría pagarla» nombra un conjunto
  mayor que el Ramo 15, porque CONAVI es descentralizado y hay gasto en vivienda fuera del
  ramo ---se bajó a «el ramo entero que la aloja»---; (3) «el perímetro territorial de la
  política social» nombra más de lo que la ZAP es, y se bajó a «el perímetro territorial que
  se declara cada año junto con el presupuesto».
- **Checklist de omisiones: dos renglones nuevos y una corrección.** **B12**, vara externa de
  suficiencia en vivienda, nace y se marca **resuelta en 2027**: es el equivalente de B1 en
  salud y llegó antes que B1, que sigue fuera por tercer ejercicio. **B13**, la ZAP como
  denominador territorial, queda registrada y enganchada a la Ruta A. Y **C4** se corrige:
  el detalle tributario no queda fuera sólo por alcance, sino **también por fuente**, porque
  las iniciativas fiscales de la cola llegan escaneadas.

**Un error de conteo del cuerpo, encontrado al recontar y corregido.** El §99 decía que la
compuerta se aplicó a los pies de «los diecinueve cuadros». Eran **veinte** el día 8. Con los
dos de la adenda, veintidós. Se corrigió el número en el §99 y en el LEEME de la entrega; no
cambia ninguna cifra.

### 32. Entrega reempaquetada

| pieza | antes (8 sep.) | ahora (9 sep.) |
|---|---|---|
| `documento_2027.pdf` | 557 KB, 61 páginas | **563 KB, 66 páginas** |
| `documento_2027.zip` | 104 KB | **111 KB** |
| `documento_2027.md` | 128 KB, 2.155 renglones | **138 KB, 2.352 renglones** |
| `datos/` | 6 CSV | **8 CSV**, con `gaceta_anexos_2027.csv` y `vivienda_art61.csv` |

**El ZIP volvió a pasar la prueba del directorio limpio, y esta vez la prueba fue más dura:
se borraron los veintidós cuadros antes de regenerarlos.** `generar_cuadros.py` los reconstruye
desde `datos/`, `pdflatex` produce 66 páginas y **el texto extraído tiene el mismo sha256**
que el PDF de la entrega, `088dd50e…`. El Markdown regenerado desde el ZIP es idéntico al de
la entrega, y sigue en **cero renglones terminados en diagonal suelta**.

Composición: los dos avisos que quedan ---un `Underfull` en el capítulo 12 y un `Overfull` de
1,46 pt en el §99--- **son los mismos del día 8**. El cuadro C99.1 desbordaba 214,7 pt en su
primera versión y se corrigió con columnas `p{}` antes de cerrar.

**Lo que sigue abierto, sin cambios respecto del cierre de ayer:** los cuatro analíticos del
proyecto, las dos ranuras del ATDT, la ranura de plazas por vigilar, y la exposición de
motivos del PPEF, que va por su sexto ejercicio. **Y una tarea nueva:** el ZIP de las 43.636
AGEB de la ZAP urbana, que la nota metodológica publica y que este proyecto todavía no ha
descargado.

---

## Retoma, 2026-09-10T21:52-06:00

Se ejecuta otra vez el orden del cierre. Los dos primeros renglones vuelven a no mover nada;
el tercero vuelve a ser el que mueve, y aparece un cuarto que no estaba en la lista: la tarea
nueva que dejó la adenda de ayer.

### 33. Sondeo de los seis recursos: segundo día sin cambio

| recurso | 09-08 21:45 | 09-09 07:33 | 09-10 21:52 |
|---|---|---|---|
| `…/Analiticos_Historico/2027/Proyecto/ac01_ra_pp_ur_og.xlsx` | 404 | 404 | **404** |
| `…/2027/Proyecto/ac01_ra_f_ur_og.xlsx` | 404 | 404 | **404** |
| `…/2027/Proyecto/ac01_ra_pp_ur_og_efe.xlsx` | 404 | 404 | **404** |
| `…/2027/Proyecto/ac01_ra_f_ur_og_efe.xlsx` | 404 | 404 | **404** |
| `…/PPEF_2027.csv` (ATDT) | 503 | 503 | **503** |
| `…/anexos_transversales_ppef2027.csv` (ATDT) | 503 | 503 | **503** |

**Sigue sin haber Ruta A**, al tercer día. Los cuatro analíticos devuelven el mismo 404 de
2 978 bytes de HTML y las dos ranuras del ATDT el mismo 503 de 592 bytes: no es que el árbol
esté vacío, es que no existe, y no es que el recurso falte, es que el servicio está caído.
La distinción importa y se sostiene: **falla «árbol no creado», no falla «almacén roto»**.

**La ranura de plazas tampoco se ha sobrescrito.** `last-modified` 2026-06-03T19:03:11 y
`content-length` 11 663 197, byte por byte el archivo de 2026 que ya está en carpeta. Tercer
día en vigilancia.

### 34. El índice de la Gaceta se reescribió por tercera vez, y esta vez se corrigió

Se bajó la tercera copia (`2027_gaceta_indice-entrega_20260910.html`, 86 039 bytes) y se
comparó con la del 9. **El bloque que el día 9 estaba comentado ---con las letras y el año del
ejercicio anterior--- se descomentó, se le corrigieron las letras y se le corrigió el año.**
Lo que ahora publica el índice es esto:

| letra | el índice del 8 | el índice del 9 | el índice del 10 |
|---|---|---|---|
| K | no listada | comentada, como «H … ZAP 2026» | **nota metodológica y declaratoria ZAP** |
| L | no listada | comentada, como «J … rurales 2026» | **listado ZAP rurales 2027** |
| M | no listada | comentada, como «K … urbanas 2026» | **listado ZAP urbanas 2027** |
| N | no listada | comentada, como «L … vivienda 2026» | **estimación de subsidios de vivienda 2027** |

**El índice quedó idéntico al cuadro C99.1 de la adenda**, que se construyó leyendo la primera
página de cada PDF porque el índice no servía. No cambia una sola cifra del documento: lo que
cambia es el estatus del cuadro, que pasa de reconstrucción propia a **reconstrucción propia
confirmada por la fuente dos días después**. La regla que sale de aquí, y que ya está escrita
en el registro de rutas: **el índice converge, pero tarda dos días; el día de la corrida la
única fuente fiable es el PDF.**

Dos detalles menores. El índice del 10 estrena un **Anexo O** (orden del día de la sesión) y un
**Anexo V** (comunicación de la Mesa Directiva con los turnos), más una sección de
Prevenciones: **nada de eso es paquete económico** y no toca el perímetro. Y el renglón K
conserva un error de la fuente: titula «zonas de atención prioritaria 2026» en su primera
cláusula y «2027» en la segunda, cuando el PDF es de 2027 en las dos.

### 35. La tarea nueva, cumplida: las 43 636 AGEB de la ZAP urbana

La adenda de ayer cerró con una tarea que no estaba en ninguna lista previa: **el ZIP de AGEB
con variables que la propia nota metodológica publica y que este proyecto no había bajado.**
Se bajó.

`2027/2027_zap-urbanas-agebs_variables.zip`, 2 163 470 bytes, sha256 `3e1a6ed3…`, un solo
`.xlsx` dentro, **encabezado en el renglón 5**, doce columnas, 43 636 renglones de datos.
Manifiesto: **de 119 a 121 archivos**, con el índice del día 10.

**Hallazgo de procedencia, y es el que más pesa para el año que viene:** el `last-modified`
del servidor es **2026-07-15**, es decir **dos meses antes de la entrega del paquete**. Este
archivo *no es pieza de cola*. Lo que llega con el paquete no es el archivo: es **el nombre
del archivo**, porque el conteo de AGEB va dentro del nombre y sólo la nota metodológica lo
dice. La ruta estaba servida desde julio y nadie podía adivinarla.

**Las cinco cuentas de la declaratoria cierran contra el archivo** ---identidades 42 a 47, y el
tablero pasa de 41 a **47 pruebas, 0 fallan**---:

| cuenta | declarado en el anexo K | en el archivo |
|---|---|---|
| AGEB urbanas | 43 636 | **43 636**, y sin una sola repetida |
| entidades | 32 | **32** |
| municipios | 2 423 | **2 423**, sobre la clave actual |
| localidades | 4 531 | **4 531**, sobre la clave actual |

**«Sobre la clave actual» no es un detalle de redacción.** El archivo trae sus propias columnas
de clave de municipio y de localidad, y con ésas los conteos **no cierran**: dan **2 416
municipios y 4 540 localidades**. Lo que la declaratoria cuenta es la última columna, *clave de
localidad actual a junio de 2026*. **120 AGEB están reasignadas**, 105 de ellas cambian de
municipio, y aparecen **siete municipios que la clave vieja no tiene**: 02007 (San Felipe, Baja
California), 04013 (Dzitbalché, Campeche), 12082 y 12085 (Guerrero), 24059 (San Luis Potosí),
25019 y 25020 (Sinaloa). Son **los municipios de creación reciente**, que es justamente uno de
los criterios de la cadena acumulativa de la nota metodológica. La diferencia 2 423 − 2 416 = 7
es esa lista. Quien cuente sobre las columnas del archivo publicará una cifra que no coincide
con la declaratoria y no sabrá por qué.

**Un dato que la nota no publica y el archivo sí:** **25 836 de las 43 636 AGEB urbanas, el
59,2 %, caen dentro de los 1 575 municipios ZAP rurales.** Las dos listas **no son disjuntas**:
se traslapan en seis de cada diez AGEB urbanas. Cualquier suma de «municipios ZAP» que junte
las dos declaratorias cuenta doble.

B13 pasa de «registrada, no cruzada» a **«denominador en mano, cruce pendiente»**. El cruce con
el gasto sigue exigiendo la distribución territorial, que sale de los analíticos: **enganchado
a la Ruta A**, como todo lo demás.

### 36. Estado al cierre del 10 de septiembre

- **La entrega no se tocó.** El PDF de 66 páginas, el ZIP y el Markdown siguen siendo los del
  9 de septiembre; ninguna cifra del documento cambió hoy.
- **Lo de hoy es adquisición, verificación y registro**: dos archivos nuevos en `2027/`, dos
  renglones nuevos en el manifiesto, seis identidades nuevas, dos notas de ruta corregidas y
  B13 avanzado.
- **Queda para Héctor una sola decisión**: si la confirmación del mapa de anexos por el propio
  índice y las seis cuentas de la ZAP entran al documento como **segunda adenda fechada el
  10**, o se quedan en bitácora hasta que llegue la Ruta A y se reabra el cuerpo. **No hay
  urgencia:** nada de lo de hoy contradice una línea de lo entregado; lo confirma.
- **Sigue abierto, sin cambios:** los cuatro analíticos del proyecto, las dos ranuras del ATDT,
  la ranura de plazas por vigilar, la exposición de motivos del PPEF en su sexto ejercicio, y
  B1, la vara de suficiencia en salud, que sigue siendo una línea de texto y un cociente.
