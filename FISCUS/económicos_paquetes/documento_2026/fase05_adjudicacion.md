# Fase 0.5 — adjudicación pendiente del ejercicio 2025

**Corrida:** FISCUS · Dalila · fase 0.5 de `INSTRUCCIONES_documento_propio_2026_v2.md`
**Ejecutada:** 2026-09-07, de 09:12 a 09:36 CST · **T+00:08 a T+00:32**
**Reproducible con:** `documento_2026/fase05_adjudicacion.py` → `fase05_salida.txt`

Cinco puntos, contra fuentes. Todo se recomputó **desde cero**, sin reusar los
`construir_*.py` de `documento_2025/`: las únicas entradas son los analíticos del PEF
aprobado 2024 y 2025 y las páginas del CGPE 2025 leídas como imagen a 150 dpi.

**Por qué va antes de la adquisición:** si nuestras cifras de 2025 no resisten, el resto de
la corrida hereda el problema.

---

## Veredicto en una línea

**Las cinco cifras resisten. Ninguna hay que retirar.** Cuatro de los cinco puntos se
cierran con la fuente en la mano y con las discrepancias contra el género explicadas por
completo. El quinto —la compensación por inflación del capítulo de deuda— **es correcto en
su aritmética y está publicado con más precisión de la que la fuente admite**, y ahí hay una
corrección que hacer en la convención, no en el número.

| # | punto | veredicto |
|---|---|---|
| 1 | Salud, −12.2 y −7.2 contra −11.0 | **resiste.** La brecha se descompone: 0.97 pp de objeto, 0.21 pp de perímetro |
| 2 | Educación, +0.7 contra −1.2 | **resiste.** 1.52 pp de objeto, 0.38 pp de perímetro |
| 3 | Defensa, ramo contra función | **resiste.** 97 % de la caída es transporte, no gasto militar. Una imprecisión menor que corregir |
| 4 | Tasa real del costo financiero | **la descomposición resiste; el «−0.05» no está identificado.** Rango real: −0.05 a −1.72 |
| 5 | Niveles nominales del acervo | **resiste.** Restitución de fuente, no derivación del porcentaje |

---

## Punto 1 — la caída de salud

**Nuestras cifras, recomputadas desde los analíticos:** la función Salud (finalidad 2,
función 3) del Gobierno Federal más las entidades de control directo, en bruto, pasa de
**970,522.5 a 888,903.7 mdp**, es decir **−12.19 % real** con el deflactor del CGPE (1.043)
y −12.15 % con el implícito de CIEP (1.04252). Descontando el programa R023 del Ramo 19
—los adeudos con el IMSS y el ISSSTE, 52,324.5 en 2024 y 339.8 en 2025— la caída pasa a
**−7.22 %**. Las dos cifras publicadas, 12.2 y 7.2, se reproducen al decimal.

### El perímetro de CIEP, reconstruido y adjudicado

Su nota al pie 6 y el pie de su cuadro 4.1 enumeran el perímetro. Reconstruido sobre el
**PEF aprobado 2024**, línea por línea:

| línea | CIEP 2024 (mdp 2025) | su base nominal implícita | nuestra reconstrucción | dif |
|---|---|---|---|---|
| IMSS | 475,517.3 | 456,120.8 | 456,122.5 | +1.7 |
| ISSSTE | 79,608.5 | 76,361.5 | 76,361.5 | 0.0 |
| Pemex (AI 231) | 20,091.1 | 19,271.9 | 19,271.6 | −0.3 |
| IMSS-Bienestar | 134,145.2 | 128,673.0 | 128,623.9 | −49.1 |
| FASSA | 141,354.8 | 135,589.5 | 135,589.4 | −0.1 |
| SSa (Ramo 12 total) | 101,114.1 | 96,989.7 | 96,990.0 | +0.3 |
| Aportaciones SS (UR 420) | 68,034.3 | 65,259.3 | 65,259.4 | +0.1 |
| Sedena | 8,349.9 | 8,009.3 | 8,009.4 | +0.1 |
| Semar | 3,814.5 | 3,659.0 | 3,659.0 | 0.0 |
| **TOTAL** | **1,032,029.7** | **989,937.6** | **989,886.8** | **−50.8** |

**Cincuenta millones de pesos de diferencia sobre novecientos noventa mil millones**
(0.005 %). Su perímetro queda adjudicado: es enumerable y reproducible.

**Las dos diferencias de perímetro que lo separan del nuestro**, ahora nombradas y no
supuestas:

1. **Excluyen al ISSFAM.** Su línea «Aportaciones a la seguridad social» es únicamente la
   UR 420 del Ramo 19. La función Salud del Ramo 19 incluye además la UR HXA, Instituto de
   Seguridad Social para las Fuerzas Armadas Mexicanas: **8,967.0 mdp en 2024 y 9,135.9 en
   2025**. Nosotros la incluimos porque tomamos la función completa.
2. **Añaden la actividad institucional 231 de Pemex**, «Personal activo y jubilado saludable
   y con calidad de vida»: 19,271.6 (2024) y 18,442.6 (2025). Vive en la función 3.3
   Combustibles y Energía, **fuera** de la función Salud, y nosotros no la traemos.

### La descomposición de la brecha

| paso | variación real | efecto |
|---|---|---|
| CIEP, su perímetro, **proyecto** (publicado) | **−11.01 %** | — |
| CIEP, su perímetro, **aprobado** | −11.98 % | **objeto: −0.97 pp** |
| Nuestro perímetro (función Salud estricta), aprobado | **−12.19 %** | **perímetro: −0.21 pp** |

**Las dos cifras son correctas de objetos distintos y la brecha está explicada por
completo.** Nueve de las diez líneas de su cuadro reconstruyen al decimal sobre el
aprobado; solo dos se mueven entre proyecto y aprobado:

- **IMSS: −10,021.1 mdp.** Su cifra de proyecto es 491,976.4; el aprobado da 481,955.3 con
  la misma receta que reproduce 2024 al 1.7. Es un movimiento entre proyecto y aprobado.
- **Sedena: +376.5 mdp**, en sentido contrario.

**Consecuencia para la corrida 2026:** en vivo no se puede hacer esta adjudicación, porque
exige el aprobado del mismo ejercicio. Va a la lista de verificaciones imposibles en vivo.

---

## Punto 2 — la caída de educación

**Nuestra cifra:** función Educación (finalidad 2, función 5) del Gobierno Federal, bruta,
**1,032,621.4 → 1,084,590.9 mdp**, **+0.70 % real**. Se reproduce al decimal.

**El perímetro de CIEP** —ramos 11, 38 y 48 completos más el resto de la función Educación—
reconstruido sobre el aprobado da **1,109,716.7 → 1,161,164.8**, es decir **+0.32 % real**.
Su base de 2024, deducida de su propia columna deflactada, es 1,109,203.1 nominales contra
nuestros 1,109,716.7: **513.6 mdp de diferencia sobre 1.11 billones (0.05 %)**. Su perímetro
también queda adjudicado.

### La descomposición de la brecha

| paso | variación real | efecto |
|---|---|---|
| CIEP, su perímetro, **proyecto** (publicado) | **−1.2 %** | — |
| CIEP, su perímetro, **aprobado** | +0.32 % | **objeto: +1.52 pp** |
| Nuestro perímetro (función Educación estricta), aprobado | **+0.70 %** | **perímetro: +0.38 pp** |

**La Cámara movió +18,674.8 mdp nominales dentro de su perímetro** entre el proyecto y el
aprobado. Es la cifra que ya estaba en la comparación de 2025 y aquí se confirma por una vía
independiente.

**El efecto de objeto es cinco veces mayor que el de perímetro, y cambia el signo.** Ése es
el punto: su titular —«el gasto educativo cae 1.2 % real»— es correcto del proyecto y dejó
de serlo en diciembre de 2024.

---

## Punto 3 — Defensa, ramo contra función

**El Ramo 07 pasa de 259,433.8 a 158,287.8 mdp**: −101,146.0 nominales, **−41.5 % real**.
Los dos cortes, por programa y por función, dan el mismo total en los dos años.

**Por función, dentro del Ramo 07:**

| función | 2024 | 2025 | diferencia nominal |
|---|---|---|---|
| 3.5 Transporte | 127,556.9 | 41,772.1 | **−85,784.8** |
| 3.1 Asuntos económicos y comerciales | 15,172.8 | 2,255.8 | **−12,917.0** |
| 1.6 Seguridad Nacional | 103,530.1 | 101,948.0 | −1,582.1 |
| 2.3 Salud | 8,009.4 | 7,053.5 | −955.9 |
| 2.5 Educación | 3,854.1 | 3,992.7 | +138.6 |
| 1.2 Justicia | 1,310.5 | 1,265.7 | −44.8 |

**Las dos funciones no militares explican 98,701.8 de los 101,146.0, el 97.6 %.** Por unidad
responsable, las dos que caen son H0M Tren Maya (125,937.3 → 40,827.8) y H0C Grupo
Aeroportuario, Ferroviario y de Servicios Auxiliares (15,172.8 → 2,275.5): juntas
−98,006.8, el 96.9 %.

**Veredicto: la afirmación resiste.** La caída del ramo es obra de transporte que baja de
escala, no gasto militar que se recorta.

**Una imprecisión que sí hay que corregir.** `diffs_explicados.md` §3 dice que la función
1.6 Seguridad Nacional queda «prácticamente plana». **Es cierto en nominal (−1.5 %) y falso
en real: cae 5.6 %.** Es exactamente la regla de la casa —toda diferencia declara si es
nominal o real— incumplida en un archivo interno propio. Se corrige en `diffs_explicados.md`
y se anota como precedente: la regla hay que aplicarla también fuera del documento
compilado.

---

## Punto 4 — la tasa real del costo financiero

Es el único punto donde hay una corrección de fondo, y no es un error de aritmética.

**Lo que resiste.** La descomposición de cuatro variables reproduce sus términos al
milésimo: crecimiento −1.063 (publicamos −1.06), inflación por el denominador −2.119
(−2.12), tipo de cambio −0.786 (−0.79), RFSPF +3.949 (+3.9). La suma da −0.018 puntos contra
un cambio observado de 0.0. **El marco cierra mejor de lo que publicamos**, porque
publicamos el RFSPF redondeado a 3.9.

**Lo que no resiste es el «−0.05».** El capítulo 12 afirma que «el efecto neto de la
inflación es de −0.05 puntos, es decir prácticamente cero». Ese número sale de usar **el
mismo índice de precios en los dos lados**: el deflactor del PIB, 4.3 %, tanto para diluir
el denominador como para valuar la compensación que el sector público paga. Con eso, la
cancelación es casi una identidad y no un hallazgo.

**El propio CGPE usa otro índice para el mismo objeto.** Su renglón «Tasa de interés,
real promedio» de 4.9 % para 2025 sale de la nominal de 8.9 deflactada por el **INPC
promedio de 3.8**, no por el deflactor del PIB. Si la compensación se valúa con el índice
que el paquete usa para hablar de tasas reales, el resultado cambia:

| índice usado para la compensación | compensación | efecto neto de la inflación |
|---|---|---|
| deflactor del PIB, 4.3 % (**el que publicamos**) | +2.073 pp | **−0.046 pp** |
| INPC promedio, 3.8 % (el del propio CGPE) | +1.832 pp | −0.287 pp |
| INPC dic/dic, 3.5 % | +1.688 pp | −0.431 pp |
| solo lo **identificable** en el paquete (ver abajo) | ≤ +0.400 pp | ≥ −1.719 pp |

**Y el paquete acota lo identificable.** La nota 1 del Anexo III.2 del CGPE 2025 (p. 85)
declara que la línea «Adecuaciones a registros presupuestarios» —**0.4 % del PIB en 2025**—
incluye «el componente inflacionario de la deuda indexada a la inflación», junto con la
ganancia por colocación sobre par, los ingresos por recompra y un ajuste por venta de
activos. Es decir: **la única compensación que el paquete nombra vale a lo sumo cuatro
décimas, y viene mezclada con otras tres cosas.** El resto de la compensación viaja dentro
del costo financiero y no es separable.

**Comprobación de orden de magnitud.** La tasa nominal efectiva sobre el acervo —costo
financiero 2025 entre SHRFSP 2024 estimado— es **7.96 %**: 3.66 % real con el deflactor del
PIB y 4.16 % con el INPC, contra el 4.9 % que el CGPE publica para Cetes 28. Los tres son
del mismo orden y ninguno adjudica entre las convenciones.

**Veredicto.** La descomposición no cambia: la compensación es una lectura del RFSPF, no un
término aditivo del marco, y el resultado de que el acervo se mantiene plano se sostiene
íntegro. **Lo que hay que retirar es la precisión del −0.05 y la frase «prácticamente
cero».** El efecto neto de la inflación está en un rango de −0.05 a −1.7 puntos del PIB
según qué índice se atribuya al pago, y **el paquete no permite cerrarlo**. Esto ya estaba
declarado: la rúbrica lo registró en 2023 como «la cota de indexación no es identificable
con el paquete y deja el interés real de 2022 en un rango de un punto». **Se declaró la
limitación y después se publicó una cifra que la ignora.**

**Consecuencia para 2026.** El capítulo 13 presenta la descomposición con la compensación
**como rango declarado, no como punto**, y nombra la línea de adecuaciones como la única
cota que el paquete ofrece. Va a las convenciones del pacto.

---

## Punto 5 — los niveles nominales del acervo

**Fuente: CGPE 2025, Anexo II.6, página 82**, leída como imagen a 150 dpi porque el
documento no tiene capa de texto. Los tres niveles son restitución directa del cuadro
«Estimación de las finanzas públicas, 2024-2025», renglón SHRFSP.

**Prueba de que el nivel se leyó y no se derivó del porcentaje.** Si los niveles se hubieran
inferido de las razones publicadas, la recalculada coincidiría por construcción y no
probaría nada. Lo que se hace es al revés: se toma el nivel leído, se divide entre el PIB
nominal de su propia añada y se compara con el porcentaje publicado.

| concepto | nivel leído (mdp) | PIB de su añada (mmp) | % recalculado | % publicado | dif |
|---|---|---|---|---|---|
| SHRFSP 2024 aprobado | 16,787,906.1 | 34,374.0 (CGPE 2024) | 48.839 | 48.8 | +0.039 |
| SHRFSP 2024 estimado | 17,440,245.8 | 33,927.7 | 51.404 | 51.4 | +0.004 |
| SHRFSP 2025 | 18,591,005.5 | 36,166.4 | 51.404 | 51.4 | +0.004 |

Las tres caen dentro del umbral de 0.1 pp. **El caso de 2024 aprobado es el que vale**,
porque exige el PIB de otra añada —el estimado en el CGPE 2024, como el propio cuadro
advierte en su nota— y aun así cierra a cuatro centésimas.

**Prueba independiente: la identidad flujo–acervo, en pesos.**

| | mdp |
|---|---|
| Δ acervo observado (2025 menos 2024 estimado) | 1,150,759.7 |
| RFSPF 2025 | 1,428,348.1 |
| efecto del tipo de cambio (−0.786 pp sobre 12.9 pp de deuda externa) | −284,190.8 |
| RFSPF más tipo de cambio | 1,144,157.3 |
| **residuo** | **+6,602.4** |

**Seis mil seiscientos millones de pesos de residuo, dos centésimas de punto del PIB.** La
identidad cierra. Un dígito mal leído en cualquiera de los tres niveles la rompería.

**Veredicto: los niveles resisten.** Y el método resiste con ellos: es la validación por
identidad contable, no por relectura, aplicada al caso en que la fuente no tiene capa de
texto.

---

## Lo que esta fase deja para el resto de la corrida

1. **Ninguna cifra de 2025 se retira.** La corrida 2026 no hereda un problema de datos.
2. **Una corrección de convención, no de número:** la compensación por inflación se
   presenta como rango con su cota declarada, nunca como punto. Entra en el pacto §11.
3. **Una corrección de texto en un artefacto interno:** `diffs_explicados.md` §3 llama
   «prácticamente plana» a una función que cae 5.6 % real. La regla de nominal-o-real rige
   también fuera del documento compilado.
4. **Dos perímetros ajenos quedan adjudicados y enumerables** —el de salud y el de
   educación del género— con su receta exacta. Eso permite, en la fase 7, comparar contra
   el documento de 2026 sin volver a reconstruirlos.
5. **Tres verificaciones que esta fase pudo hacer y la corrida en vivo no podrá**, porque
   exigen el aprobado del mismo ejercicio: separar objeto de perímetro en cualquier
   discrepancia, medir lo que movió la Cámara, y adjudicar un titular de proyecto contra el
   presupuesto que se ejerce. Van a la lista de imposibles en vivo.

---

# Revisión, 2026-09-07 · 10:00 CST · **la fase 1 refuta parte del punto 1**

La fase 0.5 se hizo bajo una premisa que la fase 1 derribó una hora después: que los
analíticos del **proyecto** no existían para 2022–2025. Existen (`mapa_fuentes.md`, adenda
2026-09-07). Con el archivo del proyecto 2025 en la mano, dos cosas cambian.

**Esta sección no reescribe lo anterior. Lo corrige con fecha, que es la única forma
honesta de corregir un documento que ya afirmó algo.**

## Punto 1 — el veredicto cambia

La fase 0.5 atribuyó a **objeto** los 10,021.1 mdp de diferencia en la línea IMSS del cuadro
de salud de CIEP, razonando que su cifra era del proyecto y la nuestra del aprobado. **Era
una inferencia, no una medición, y es falsa.**

Reconstruido el perímetro de CIEP sobre el **proyecto** 2025, nueve de sus diez líneas
coinciden al decimal —incluidas Pemex, FASSA, SSa, ISSSTE, IMSS-Bienestar, Bienestar,
Aportaciones SS y Semar— y **la línea del IMSS sigue difiriendo en los mismos 10,021.1 mdp**.
Su IMSS es 491,976.4; el proyecto da 481,955.3 y el aprobado da 481,955.3 **también**. La
Cámara no tocó la función Salud del IMSS.

**Qué es entonces esa diferencia.** No se reconstruye. Se buscó en el IMSS un componente de
10,021.1 fuera de la función Salud y no existe: los candidatos por magnitud —«Prevención y
control de enfermedades» 10,155.9 y «Programas de adquisiciones» 10,138.9— fallan por 135 y
118 mdp. **La fila correcta es `no_verificable`, no `no`**, por la regla que la propia
rúbrica fijó en 2024: un agregado de partes nombradas pero no listadas es irrecuperable.

**La única diferencia real de objeto en su cuadro de salud son 376.5 mdp en Sedena**
(proyecto 6,677.0, aprobado 7,053.5), es decir cuatro centésimas de punto porcentual.

### La descomposición corregida

| paso | variación real | efecto |
|---|---|---|
| CIEP publica (su perímetro, proyecto contra aprobado 2024) | **−11.01 %** | — |
| lo mismo, **reconstruido por nosotros** | −12.03 % | **su línea de IMSS no reconstruible: 1.02 pp** |
| nuestro perímetro (función Salud estricta), misma base | −12.22 % | **perímetro: 0.19 pp** |
| lo que publicamos (aprobado contra aprobado) | **−12.19 %** | **objeto: 0.03 pp** |

**El objeto no explica casi nada de la brecha de salud**, al revés de lo que dijo la fase
0.5. La función Salud es prácticamente idéntica en el proyecto y en el aprobado los dos
años: 970,522.5 contra 970,522.5 en 2024, y 888,527.1 contra 888,903.7 en 2025. Nuestra
cifra da −12.22 % proyecto contra proyecto y −12.19 % aprobado contra aprobado.

**Lo que sí queda establecido, y es más incómodo para el género que lo que decía la fase
0.5:** de la brecha de 1.18 puntos entre su titular y el nuestro, **1.02 puntos son una
línea de su propio cuadro que no se reconstruye desde ninguna fuente del paquete.**

## Punto 2 — el veredicto se confirma, por una vía mejor

La fase 0.5 dedujo el efecto de objeto en educación comparando su perímetro sobre el
aprobado contra su cifra publicada. Ahora se mide directamente: **su perímetro reconstruido
sobre el proyecto 2025 da 1,142,490.5 mdp contra los 1,142,490.0 que publican.** Medio
millón de pesos sobre 1.14 billones. La cifra de CIEP queda reconstruida, no inferida.

Con las cuatro celdas disponibles, el cuadro completo de la función Educación del Gobierno
Federal, bruta:

| | 2024 | 2025 | variación real |
|---|---|---|---|
| proyecto contra proyecto (**línea P**) | 1,019,448.8 | 1,071,949.8 | **+0.81 %** |
| aprobado contra aprobado (**lo que publicamos**) | 1,032,621.4 | 1,084,590.9 | **+0.70 %** |
| aprobado 2024 contra proyecto 2025 (**línea G**) | 1,032,621.4 | 1,071,949.8 | **−0.47 %** |

Y el perímetro de CIEP:

| | 2024 | 2025 | variación real |
|---|---|---|---|
| proyecto contra proyecto | 1,096,544.1 | 1,142,490.5 | −0.11 % |
| aprobado contra aprobado | 1,109,716.7 | 1,161,164.8 | +0.32 % |
| **línea G, que es la suya** | 1,109,716.7 | 1,142,490.5 | **−1.29 %** (publican −1.2) |

**Su −1.2 queda reconstruido a nueve centésimas**, atribuibles al deflactor. Y el cuadro
muestra por qué el signo del capítulo es tan frágil: **la misma función educativa da +0.81,
+0.70 o −0.47 según qué dos objetos se comparen.** Ninguna de las tres es falsa. Es el mejor
argumento posible a favor de la regla de etiquetar la línea en cada columna.

## Lo que esta revisión enseña sobre el método

**Una inferencia bien argumentada sobre una fuente que no se tiene es una hipótesis, y hay
que rotularla como tal.** La fase 0.5 escribió «es un movimiento entre proyecto y aprobado»
donde debió escribir «es compatible con un movimiento entre proyecto y aprobado, y no puedo
distinguirlo de un detalle de perímetro sin el archivo del proyecto». La diferencia entre
las dos frases es exactamente lo que este proyecto le viene señalando al género desde 2020.

Se corrige, se fecha, y se deja escrito. **Los puntos 3, 4 y 5 no cambian**: ninguno
dependía del archivo del proyecto.
