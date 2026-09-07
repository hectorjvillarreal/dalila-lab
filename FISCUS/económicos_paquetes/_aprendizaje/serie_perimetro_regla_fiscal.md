# La serie del perímetro de exclusión de la regla fiscal, 2018–2026

**Precarga §3.2 de `INSTRUCCIONES_preparacion_2027.md`**, marcada PRIORITARIA.
**Reconstruida el 2026-09-07** contra las nueve iniciativas de Ley de Ingresos y las
nueve leyes aprobadas, todas en carpeta, más los nueve Criterios Generales.

Es el hallazgo que los dos documentos de 2026 —el propio y el de CIEP— dejaron pasar.
En 2027 es un capítulo o recuadro propio, y su primera tarea es leer el artículo 1o. de
la ILIF.

---

## 0. Qué regula esto

El artículo 17 de la Ley Federal de Presupuesto y Responsabilidad Hacendaria manda
equilibrio presupuestario. La Ley de Ingresos, cada año, puede **sacar del cómputo** una
parte del gasto de inversión: lo que quede fuera no cuenta para el equilibrio. El
resultado es un segundo balance —el **balance sin inversión**— que es el que la regla
mide de verdad.

Dos cosas se mueven cada año y hay que leerlas juntas:

1. **El perímetro:** qué gasto entra en la exclusión.
2. **El tope:** hasta qué porcentaje del PIB.

---

## 1. La serie

Datos en `serie_perimetro_regla_fiscal.csv`. La columna del balance es la del **ejercicio
proyectado**, tomada del anexo de estimación de finanzas públicas del CGPE de ese mismo
año, no de la columna retrospectiva del cuadro de la página 36.

| ejercicio | perímetro que propone la ILIF | tope | LIF aprobada | balance presup. | **balance sin inversión** |
|---|---|---|---|---|---|
| 2018 | inversión del Gobierno Federal y de las empresas productivas del Estado | 2,0 % | igual | −2,0 % | **0,0 %** |
| 2019 | igual | 2,0 % | igual | −2,0 % | **0,0 %** |
| 2020 | igual | 2,0 % | igual | −2,1 % | **−0,1 %** |
| 2021 | igual | 2,2 % | igual | −2,9 % | **−0,7 %** |
| 2022 | **inversión de todo el sector público presupuestario** | 3,1 % | igual | −3,1 % | **0,0 %** |
| 2023 | inversión del sector público presupuestario **aprobada en el PEF** | **SIN TOPE** | igual | −3,6 % | **0,0 %** |
| 2024 | **cláusula ausente** | — | ausente | −4,9 % | **−1,7 %** |
| 2025 | **cláusula ausente** | — | ausente | n. d. | no publicado |
| 2026 | inversión física **+ financiera + desarrollo de capital humano** del sector público presupuestario aprobado en el PEF | 3,6 % | **igual: el Congreso no lo tocó** | −3,6 % | **NO PUBLICADO** |

**Ubicación en la ley, los nueve años: artículo 1o.**, en el párrafo que sigue al de la
recaudación federal participable —salvo en 2026, donde va después del párrafo de la
reserva del ISSSTE—. Nunca ha sido un artículo propio.

---

## 2. Cuatro hallazgos

### 2.1 El tope de 2026 es exactamente el déficit

$$3{,}6\ \%\times 38\,715{,}9\ \text{mmp} = 1\,393\,772{,}4\ \text{mdp}$$
$$\text{balance presupuestario 2026} = -1\,393\,770{,}6\ \text{mdp}$$

**Difieren en 1,8 millones de pesos**: trece cienmilésimas de punto porcentual del PIB.
No es una coincidencia aritmética, es una calibración: **el tope se fija en el tamaño del
déficit, de modo que el déficit cumpla el artículo 17 por construcción.**

El patrón se repite donde se puede comprobar: 2018 (déficit 2,0 %, tope 2,0), 2019
(2,0 y 2,0) y 2022 (3,1 y 3,1) cierran igual. **2020 y 2021 no:** ahí el tope quedó
por debajo del déficit y el balance sin inversión salió negativo, −0,1 y −0,7 puntos.

### 2.2 Se corrige un dato de la instrucción

La instrucción de preparación afirma que «la ILIF 2023 retiró el tope y **la LIF aprobada
lo devolvió a 3,1 %**». **No ocurrió.** La ILIF 2023 retiró el tope y **la LIF aprobada
también quedó sin tope**: el texto publicado en el Diario Oficial dice «no se contabilizará
para efectos del equilibrio presupuestario previsto en el artículo 17», y ahí termina la
oración. El 3,1 % fue el tope de **2022**, no un regreso en 2023.

Comprobado contra los dos documentos, palabra por palabra. **El Congreso no ha modificado
esta cláusula en ninguno de los nueve ejercicios.**

### 2.3 La cláusula desapareció dos años y volvió más ancha

En 2024 y 2025 **no existe**: ni en la iniciativa ni en la ley aprobada. El párrafo que
en 2018–2023 se intercala entre la recaudación federal participable y el pago en especie
del impuesto sobre servicios simplemente no está. Se verificó por tres vías —búsqueda de
«no se contabilizará», de «artículo 17 de la Ley Federal de Presupuesto» y de «equilibrio
presupuestario»: cero apariciones en los cuatro documentos.

Vuelve en 2026, y vuelve **cambiada de naturaleza**. Hasta 2023 excluía *inversión*. Desde
2026 excluye inversión física, inversión financiera **y desarrollo de capital humano**,
que la propia ley define como gasto programable en educación, salud pública preventiva y
formación o certificación de competencias «que incremente de forma sostenible la
productividad y los ingresos de la población», excluyendo transferencias no condicionadas,
pensiones, subsidios generalizados y gasto administrativo.

**Eso ya no es una regla de inversión: es una regla de gasto productivo**, y su perímetro
depende de una clasificación que ningún anexo del paquete publica.

### 2.4 El indicador que mide la regla dejó de publicarse

El renglón «balance público sin inversión» aparece en el CGPE **todos los años de 2018 a
2024** —renombrado «balance presupuestario sin inversión» en 2024—. **En el CGPE 2026 no
está.** La única mención del artículo 17 de la LFPRH en las 439 mil letras de ese documento
es un pie de cuadro sobre el límite del gasto corriente estructural, no sobre el balance.

De modo que en 2026 coinciden tres cosas: la exclusión vuelve, se ensancha hasta abarcar
gasto social, y **el indicador con que se comprobaría si la regla se cumple deja de
publicarse.**

> **Sobre 2025 no se afirma nada.** El CGPE 2025 es un escaneo sin capa de texto —2 472
> caracteres extraíbles contra 439 323 del CGPE 2026—, de modo que una búsqueda no prueba
> ausencia. Para cerrar ese renglón hay que leer el PDF como imagen. **Queda abierto y
> declarado.**

---

## 3. La conexión que nadie hizo: Pemex

Los dos hallazgos estaban en el documento propio de 2026, en capítulos distintos, sin
juntar.

**Uno.** La aportación de capital a Pemex vale **263 476,3 mdp**, y está en la partida
específica 73903 del Ramo 18 —capítulo 7000, *inversiones financieras y otras
provisiones*—. Es el componente dominante de ese capítulo: **el 67,9 % de sus 388 161,3
millones.**

**Dos.** El perímetro de exclusión de 2026 incluye, por primera vez con ese nombre, la
**inversión financiera**.

**La conexión se sostiene, y es aritmética, no interpretativa:** una aportación patrimonial
clasificada como adquisición de títulos y valores es inversión financiera, y por tanto es
candidata a quedar fuera del cómputo del equilibrio presupuestario. Vale **0,68 % del PIB**
y por sí sola ocupa **el 18,9 % del tope de 3,6 %.**

**Lo que no se puede afirmar** —y hay que escribirlo así en el documento— es que la SHCP
efectivamente la excluya. La ley da la facultad; el CGPE 2026 ya no publica el renglón que
mostraría el resultado. **La afirmación defendible es que el paquete crea la posibilidad y
retira la evidencia**, no que la exclusión se haya aplicado.

---

## 4. Qué hacer en 2027, en orden

1. **Leer el artículo 1o. de la ILIF 2027** y localizar el párrafo. Está entre el de la
   recaudación federal participable y el del pago en especie, o cerca. Si no está, **eso
   es la noticia**, como lo fue en 2024.
2. **Anotar tres cosas:** el perímetro literal, el tope, y si define conceptos.
3. **Calcular el tope en pesos** con el PIB del CGPE y compararlo con el balance
   presupuestario proyectado. Si coinciden, la regla está calibrada al déficit y se dice.
4. **Buscar el renglón «balance sin inversión» en el CGPE.** Si sigue sin publicarse, se
   reporta como serie interrumpida desde 2025, con los años en que sí se publicó.
5. **Medir la inversión financiera del capítulo 7000** y ver qué parte del tope ocupa.
6. **Repetir contra la LIF aprobada en diciembre.** En nueve ejercicios el Congreso no ha
   cambiado esta cláusula ni una vez; si la cambiara, sería el primer caso.

---

## Fuentes

Todas primarias y en carpeta. ILIF 2018–2026, `{a}/{a}_ilif_iniciativa.pdf`, artículo 1o.
LIF aprobada 2018–2026, `{a}/{a}_lif_aprobada.pdf` —las de 2018 a 2021 y la de 2026 se
descargaron el 2026-09-07 del acervo de leyes de la Cámara de Diputados, siguiendo los
enlaces de `LeyesBiblio/abroga.htm` y `LeyesBiblio/index.htm`, sin construir rutas por
analogía—. CGPE 2018–2026, `{a}/{a}_cgpe_criterios-generales.pdf`, cuadro de estimación de
las finanzas públicas del anexo. PIB 2026 y balance presupuestario 2026: CGPE 2026, Anexos
III.1 y II.6. Aportación a Pemex y capítulo 7000: analíticos del proyecto 2026 y base de
datos abiertos, vía `documento_2026/datos/`.
