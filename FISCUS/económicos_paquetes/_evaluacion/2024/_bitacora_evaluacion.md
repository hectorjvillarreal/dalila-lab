# Bitácora — evaluación del documento CIEP, ejercicio 2024 (educación)

**Corrida:** FISCUS · Dalila · 2026-09-06 · instrucción `INSTRUCCIONES_evaluacion_CIEP_2024_v3.md`
**Capítulo propio:** EDUCACIÓN · **Documento evaluado:** *Implicaciones del Paquete Económico 2024* (CIEP, 14 de septiembre de 2023), 96 páginas
**Artefactos:** `00_inventario_paquete.md`, `01_capitulo_propio_educacion.md`, `02_verificacion_cifras.csv` (115 filas), `03_evaluacion_calidad.md`, `04_comparacion_educacion.md`

---

## 1. Qué no llegó y con qué respuesta del servidor

Primero de todo, como manda §6 de la instrucción. **Ninguna ausencia bloqueó la corrida** (regla §0).

| pieza | ruta probada | respuesta |
|---|---|---|
| Exposición de motivos del PPEF 2024, documento completo | `www.ppef.hacienda.gob.mx/work/models/PPEF2024/docs/exposicion/EM_Documento_Completo.pdf` | **404 text/html** |
| Exposición de motivos del PPEF 2024, capítulos 1–4 y anexo | `…/docs/exposicion/EM_Capitulo_{1,2,3,4}.pdf`, `EM_Anexo.pdf` | **404 text/html** (los cinco) |
| Carta del Presidente, PPEF 2024 | `…/docs/carta/Carta.pdf` | **404 text/html** |
| Analíticos del PPEF 2024 (proyecto) | `…/analiticosPresupuestarios/Proyecto/ac01_ra_pp_ur_og.xlsx` y `…/analiticosPresupuestarios/ac01_ra_pp_ur_og.xlsx` | **404** en las dos rutas |
| Exposición de motivos del PPEF 2024 en Wayback | `archive.org/wayback/available?url=…` con y sin `www` | `archived_snapshots: {}` |
| Base de datos del PPEF en Transparencia Presupuestaria | `/es/PTP/Datos_Abiertos` y ruta adivinada `…/PPEF_2024.zip` | 200 con **cáscara JS de 1,919 bytes sin enlaces**; 404 |
| Cuentas Públicas 2016–2022 | no se intentó | decisión confirmada §5.5: **no se descargan** |
| Matrícula y cobertura (SEP, CONAPO) | no está en carpeta | hueco declarado en el capítulo propio |

**Descargas logradas** (todas registradas en `_manifiesto.csv`): analíticos del PEF aprobado de Gobierno Federal 2023 y 2024 (ramo × programa × UR × objeto y ramo × función × UR × objeto), analíticos de entidades 2024, y **LIF aprobadas 2022, 2023 y 2024**.

## 2. Resonda del árbol PPEF · el árbol NO volvió

Se dice primero, como pide la instrucción: **el árbol sigue caído y el alcance de esta corrida y de las que faltan no cambia.**

Pero la resonda encontró más de lo que buscaba. **Las subpáginas responden 200 y enumeran los archivos; los archivos dan 404.** El control de 2021 sirve `EM_Documento_Completo.pdf` con 200 `application/pdf`. Es decir: **almacén de archivos roto o reubicado para 2022–2026, no retirada de documentos.** Las páginas índice se generan de una base que conserva las entradas.

Hallazgo lateral: **las páginas índice están desactualizadas respecto al almacén en todos los años.** Listan los analíticos como `analiticosPresupuestarios/ac01_*.xlsx`, ruta que da 404 incluso para 2021; la que funciona en 2021 lleva el segmento `/Proyecto/`. No tomar los href de las páginas como ruta canónica.

Hallazgo lateral 2: **Transparencia Presupuestaria comparte la cadena TLS mal encadenada de la SHCP** y el mismo bundle (hoja firmada por YR1, servidor que envía R10; se pasa YR1 + `root-yr-by-x1` con `--cacert`) la arregla. La verificación TLS no se desactivó en ninguna petición. Ritmo: una petición cada 2 segundos.

## 3. Contenido de la ILIF única · RESUELTO tras cinco corridas

**El portal no ofrece la exposición de motivos de la ILIF como pieza separada porque no existe: el PDF de la ILIF la contiene.** Verificado en los nueve ejercicios 2018–2026. En 2020–2026 lleva el encabezado literal «EXPOSICIÓN DE MOTIVOS»; en 2018 y 2019 el mismo texto va sin encabezado. En 2024 ocupa las páginas 1–65 del PDF y el articulado empieza en la 66.

**Consecuencia para el manifiesto: las nueve piezas «ILIF exposición de motivos» dejan de contarse como faltantes.** El faltante real del proyecto baja a **cinco documentos: la exposición de motivos del PPEF 2022–2026**, y esos están caídos en el servidor, no ausentes del portal.

## 4. Horas

| hito | hora (2026-09-06, CST) |
|---|---|
| Cierre del capítulo propio de educación, escrito a ciegas | **16:23** |
| Primera lectura del capítulo 8 y del frente de CIEP 2024 | **20:47** |
| Lectura de las figuras 8.1 y 8.2 como imagen | 20:57 |

Cuatro horas y veinticuatro minutos entre el cierre y la primera lectura. El capítulo propio no se modificó después de las 16:23; las tres correcciones que la lectura obligó están registradas en `04_comparacion_educacion.md` y no se aplicaron al capítulo.

## 5. Recuento de la verificación

**115 filas.** Por sección del documento: capítulo 8, 72; frente (presentación y resumen ejecutivo), 32; capítulo 13, 11.

| | 2024 educación | 2023 deuda |
|---|---|---|
| Filas | 115 | 376 |
| Verificables | 84 (73 %) | — |
| Coinciden (`si` + `aprox`) | 73 de 84 = **87 %** | 65 % |
| No coinciden | 11 | — |
| `no_verificable` | 31 (27 %) | — |

**`tier_seccion`:** `restitucion` 103, `juicio` 12, `mixta` 0. (En 2023: 250 / 45 / 81.) Un capítulo de rubro es casi todo restitución; la mixtura aparecía en deuda porque los agregados nombrados obligaban a juzgar la definición antes de restituir la cifra.

**`tipo_error`:** `transcripcion` 5, `objeto` 4, `perimetro` 1, `deflactor` 1. Total 11. (En 2023, antes del remarcado: `transcripcion` 29, `perimetro` 8, `objeto` 7, `contrafactual` 6, `omision` 3.)

**Las dos tasas del contrafactual (§2.1),** sobre las 68 filas donde la comparación aplica: **estricta 41 % (28/68); puente de cuatro declaraciones 49 % (33/68)**. Serie: 17 % / 68 % en deuda (2023). La estricta mejora 24 puntos y el puente cae 19; las dos casi coinciden en 2024 porque el capítulo de educación tiene pocas cifras per cápita, mientras que el de deuda estaba hecho de ellas. **Comparar el par, nunca una sola de las dos entre ejercicios.**

**Serie de la corrida, contra 2020–2023 (38/22, 54/18, 65 sobre verificable, 37/26/37 en deuda):** el punto de 2024 es **87 % sobre verificable**, el más alto de la serie. La lectura no es que CIEP haya mejorado veintidós puntos: es que **por primera vez la corrida tuvo los analíticos completos de los dos años y pudo reconstruir los agregados del evaluado al mdp** en vez de dejarlos en `no_verificable`. La comparabilidad del indicador entre ejercicios depende de qué había en carpeta, y eso hay que decirlo cada vez que se cite.

**Deflactor implícito del documento evaluado: 1.0480**, calculado desde sus propios cuadros antes de contrastar ninguna variación, como manda §2.8. Recuperado de cuatro renglones independientes que cierran al mdp: la variación de 0.02 % de S072, los 18,206 del FONE servicios personales, los 3,017 de U006 en media superior y los 22,297 de la nota al pie 11. El oficial del CGPE es 1.0479. La brecha es de un diezmilésimo y no explica ninguna fila.

**Los tres hallazgos que sostienen la evaluación:**
1. **La matrícula implícita sube, no baja.** El texto atribuye el máximo histórico de gasto por alumno de educación básica a «1.8 millones de NNA menos», y el denominador implícito de su propia Figura 8.2 crece 0.41 % (21.489 → 21.577 millones). Los tres niveles crecen exactamente 0.41 %, lo que indica un solo factor común y no matrícula por nivel.
2. **Una cifra deflactada presentada como monto aprobado.** La nota al pie 11 dice que en 2023 «se aprobaron 22 mil 297 mdp» para las previsiones del FONE; la Cámara aprobó **21,275.7 corrientes**, y 22,297 es esa cifra por 1.048.
3. **El mínimo en puntos del PIB depende de mezclar bases.** Con el PIB rebasado a 2018, 2023 vale 3.187 % y 2024 vale 3.190 %: 2024 no es mínimo. Solo lo es si el punto de 2023 se deja en base 2013. Es el mismo cambio de vintage que el capítulo de deuda del propio documento sí corrige.

**Ocho de los once errores son contradicciones internas** del documento, no discrepancias contra la fuente oficial. Es el cuarto patrón de la serie: ingresos falla por base, gasto federal por perímetro, deuda por nombre, **gasto federalizado por consistencia interna**.

## 6. Remarcado retroactivo de 2023 · ejecutado ex post

**Se deja constancia expresa de que las veinte filas de 2023 se remarcaron *ex post*, el 2026-09-06, durante la corrida de 2024, y no en su clasificación original.** Todo conteo de `tipo_error` de 2023 anterior a esta fecha excluye estas veinte.

Filas remarcadas con `tipo_error = deflactor`, todas `coincide = aprox` (§2.10): V036, V102, V107, V111, V112, V128, V132, V140, V203, V221, V256, V290, V291, V296, V299, V309, V312, V320, V369, V384. Cada nota lleva la marca del remarcado.

**V107 y V111** combinan deflactor con la reclasificación ILIF–CGPE de 3.4 mmp: el campo lleva la causa dominante (`deflactor`) y la nota registra las dos.

`tipo_error` de 2023 tras el remarcado: `transcripcion` 29, **`deflactor` 20**, `perimetro` 8, `objeto` 7, `contrafactual` 6, `omision` 3. El validador de §2.8 corre limpio: cero violaciones de esquema en los dos CSV.

## 7. Series de seguimiento

Sin interpretación, con fuentes.

### 7.1 Pensiones IMSS / cuotas IMSS · las dos series, separadas

**Serie aprobada** (numerador PEF aprobado, tipo de gasto 4, analítico de entidades; denominador **LIF aprobada**, art. 1o. numeral 2, renglón 01):

| ejercicio | pensiones IMSS (mdp) | cuotas IMSS (mdp) | razón |
|---|---|---|---|
| 2022 | 636,461.8 | 411,852.5 | **1.545** |
| 2023 | 750,252.1 | 470,845.4 | **1.594** |
| 2024 | 870,981.7 | 535,254.7 | **1.627** |

**Serie ex ante** (numerador exposición de motivos del PPEF; denominador ILIF): 2020 **1.31**, 2021 **1.46**. **Se detiene en 2021** porque la exposición de motivos del PPEF no existe para 2022–2026 (§1 y §2 de esta bitácora). No se prolonga con otra fuente.

**Los valores 1.55 y 1.59 se rehabilitan y dejan de estar marcados como híbridos.** La razón: se descargaron las LIF aprobadas y **coinciden con sus ILIF en las cuotas del IMSS en 2022, 2023 y 2024** (411,852.5 / 470,845.4 / 535,254.7 en ambas), de modo que el denominador que se había usado era ya el aprobado. Los valores precisos son 1.545 y 1.594. Corolario para la rúbrica: **antes de descartar puntos por híbridos, comprobar si las dos bases coinciden.**

Las dos series **no se unen en una línea**. La aprobada sube 8 centésimas en dos años; la ex ante tiene dos puntos y está congelada.

### 7.2 Pasivo pensionario · serie rehecha con tres campos

| documento de origen | fecha del saldo | pesos de | mmp | % del PIB de |
|---|---|---|---|---|
| CGPE 2022 | 2020 (ISSSTE: 2019) | 2020 | 12,021.2 | **52.1** (PIB 2020) |
| CGPE 2023, p. 104–105 | 2021 (ISSSTE: 2020) | 2021 | 11,457.9 | **43.6** (PIB 2021) |
| CGPE 2024, p. 84 | 2022 (ISSSTE: 2021 actualizado con inflación) | 2022 | 10,848.8 | **38.1** (PIB 2022) |

**La sospecha de la instrucción §4.2 queda confirmada y ampliada: la caída de 8.5 puntos es una comparación entre añadas, y la comete la fuente oficial.** El CGPE 2023 escribe literalmente que «la cifra observada fue menor en 8.5 pp del PIB respecto a lo registrado en 2020 (52.1 %)», poniendo lado a lado un saldo de 2021 en pesos de 2021 sobre PIB de 2021 contra uno de 2020 en pesos de 2020 sobre PIB de 2020. Nuestra serie heredó el error de la fuente.

Además: los PIB implícitos son 23,073 (2020), 26,280 (2021) y 28,475 (2022) mmp. El de 2022 no coincide ni con la añada base 2013 (28,129.3) ni con la revisada base 2018 (29,058.3): **es una tercera añada** que el documento no identifica. Y el componente del ISSSTE cambia de método en el CGPE 2024, donde ya no es una valuación actuarial del año sino una de 2021 «actualizada con inflación».

**La serie sigue congelada para calibración y ahora tiene sus tres campos.** No se cita como trayectoria. Lo único que se puede afirmar con los tres puntos es que en pesos de su propio año el pasivo baja (12,021.2 → 11,457.9 → 10,848.8), y ni siquiera eso es limpio porque cambian la fecha de referencia y el método de un componente.

### 7.3 Las demás

| serie | estado |
|---|---|
| Supuesto oficial de crecimiento real de pensiones | 7.0 (2021), 4.2 (2022), 4.2 (2023) — **congelada** |
| Tributarios / gastos obligatorios | 0.671 (2021), 0.674 (2022) |
| Costo financiero / tributarios | 0.20 (2022), 0.23 (2023), **0.256 (2024:** 1,264.0 / 4,941.5) |
| SHRFSPF / tributarios, en años | 3.6 (2022), 3.4 (2023), **3.40 (2024:** 16,787.9 / 4,941.5) |
| Pensiones + costo financiero / tributarios | 0.60 (2023, base por confirmar); **2024: 0.659 con pensiones perímetro amplio** (1,991.9 + 1,264.0) / 4,941.5 y **0.559 con pensiones por clasificación económica** (1,499.0 + 1,264.0) / 4,941.5. **Recalculada con las dos definiciones para 2023 da 0.583 y 0.522, ninguna igual al 0.60 registrado: hay que reconstruir de dónde salió ese punto antes de prolongar la serie.** |
| **Educación / pensiones y jubilaciones** (nueva, §2.9 análoga para gasto) | **0.709 (2023), 0.689 (2024)**; con pensiones totales 0.558 → 0.518 |

## 8. Cota de indexación (§8.3)

**No se cierra en esta corrida y no le corresponde.** Con el paquete no se identifica cuánto de las adecuaciones de registro es inflación pagada, y por eso el interés real de 2022 sigue en un rango de un punto.

**Qué serie haría falta, para que Layer A no vuelva a derivarlo:** el saldo y el pago de intereses de los **Udibonos** (donde la compensación por inflación viaja como revalorización del principal, no como interés) y de los **Bondes** (donde viaja en el cupón revisable), separados del resto del portafolio interno. La fuente es el Plan Anual de Financiamiento y los informes trimestrales de deuda de la SHCP, no el paquete. **Con eso, y no antes, la parte de las adecuaciones que es inflación pagada queda identificada y el rango de un punto se cierra.** Esta corrida se detiene aquí: cerrar el rango corresponde a Layer A.

## 9. Diagnóstico de manual (no se presenta)

Se conserva aquí y solo aquí, por §2.6. El contraste de manual del capítulo de deuda (primario + r − g) no se aplicó en esta corrida porque el rubro es de gasto y no de deuda. La razón del retiro sigue escrita en la rúbrica: el paquete no publica un primario del RFSPF y el del balance económico sesga al optimismo por una o dos décimas.

## 10. Qué cambiar para 2025

**Nota de calendario, primero:** el paquete 2025 se entregó el **15 de noviembre de 2024** por cambio de administración, no el 8 de septiembre. Es el único de la serie con esa fecha y hay que tenerlo presente al construir cualquier cronología, al fechar el documento de CIEP y al comparar plazos de elaboración (CIEP dice hacer su análisis en 72 horas; en 2025 esas 72 horas caen en noviembre).

1. **El rubro de 2025 debería ser salud**, para cerrar la tríada de NTA con un capítulo evaluado propio. La propuesta de comparación estructural para salud quedó abierta desde 2021 y sigue sin adoptarse. Alternativa: gasto federalizado como rubro, ahora que 2024 mostró que la distinción federal/federalizado decide la lectura.
2. **Descargar los analíticos aprobados de los dos años en fase 1, sin excepción.** Fue lo que subió la tasa de verificación de 65 % a 87 %. Y anotar en la instrucción la trampa de la hoja: **los datos están en `Hoja1`, no en la primera hoja**, que es un resumen de 45 filas y hace creer que el archivo está vacío.
3. **Renderizar como imagen todas las figuras del capítulo evaluado antes de escribir la verificación.** Los rótulos de las series de CIEP 2024 son legibles y de ahí salió el hallazgo principal. En 2023 se leyeron a ojo y con reservas; conviene hacerlo siempre y con `pdftoppm -r 160`.
4. **Aplicar las cuatro pruebas baratas de consistencia interna** (§9 de `especificacion_genero.md`) como paso explícito de la fase 4, antes de contrastar contra la fuente. Produjeron ocho de los once errores de 2024.
5. **Añadir a la fase 1 la descarga de la LIF aprobada del año y del anterior.** Costó dos peticiones y resolvió un pendiente de dos corridas.
6. **La resonda del árbol PPEF pasa a ser una sola petición de control**, no una batería: basta comprobar `PPEF{t}/docs/exposicion/EM_Documento_Completo.pdf` contra el control de 2021. Si el de 2021 deja de responder, el diagnóstico cambia de «almacén roto» a «retirada» y hay que archivar lo que quede.
7. **Decidir el `tier_seccion`.** Lleva cuatro corridas provisional. Es decisión de Héctor con Clavellina y ya hay **1,142 filas** clasificadas en los cinco ejercicios (187 + 206 + 258 + 376 + 115) con un vocabulario que nadie ha ratificado.
8. **No citar la tasa «sobre verificable» entre ejercicios sin decir qué había en carpeta.** El salto de 65 % a 87 % es de las fuentes disponibles, no del evaluado.
