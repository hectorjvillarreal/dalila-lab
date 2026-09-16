# Fase 2 — inventario, diffs y datos

**Corrida:** FISCUS · Dalila · fase 2 de `INSTRUCCIONES_documento_propio_2026_v2.md`
**Ejecutada:** 2026-09-07, de 10:01 a 10:16 CST · **T+00:57 a T+01:12**
**Reproducible con:** `verificar.py` (identidades), `construir_diffs.py`, `construir_datos.py`

---

## 1. Inventario oficial, con documento y ubicación

Todo del **proyecto**. Ninguna pieza aprobada del ejercicio 2026.

| pieza | páginas | capa de texto | lo que resuelve |
|---|---|---|---|
| CGPE 2026 | 93 | **sí**, 6 páginas sin ella | marco macro (II.5 p. 83), finanzas públicas (II.6 p. 84), mediano plazo (III.1 p. 86, III.2 p. 87), amortizaciones (III.3 p. 91) |
| ILIF 2026 | 238 | sí | ingresos por renglón del art. 1o. (PDF pp. 105 ss.), techos, exposición de motivos propia |
| Proyecto de decreto de PEF 2026 | 171 | sí | Anexo 1 gasto neto por ramo (pp. 65-67), Anexo 2 gasto corriente estructural, Anexo 3 gastos obligatorios, Anexos 10-19 transversales, Anexo 22 Ramo 33 |
| Analíticos del proyecto 2026 | 4 archivos | — | ramo × programa × UR × objeto y ramo × función × UR × objeto, GF y entidades |
| CSV del proyecto 2026 | 129,908 filas | — | lo anterior más partida específica, clave de cartera y entidad federativa |
| CSV de anexos transversales | 102,829 filas | — | cada anexo transversal desglosado por programa |
| Miscelánea (Gaceta, anexos D, E, F) | 346 | sí | Ley Federal de Derechos, IEPS, Código Fiscal |

**El CGPE 2026 sí trae capa de texto**, contra 90 de 91 páginas como imagen en 2025. La
técnica de renderizar y leer como imagen no hizo falta este año. **Se conserva la validación
por identidad de todas formas**: es una técnica general, no un parche.

---

## 2. Reconciliaciones · **33 pruebas, 33 cierran**

`verificar.py`. Se corren antes de escribir y después de cada cambio en los datos.

### 2.1 Las que cierran exactamente, al peso

- **Anexo 1: A+B+C+D+E más los ramos 40 y 32, menos el neteo, igual al gasto neto total.**
  11,746,796.8 − 1,553,113.1 = **10,193,683.7**. Cero de diferencia.
  *Trampa del cuadro: los ramos 40 y 32 se imprimen fuera del subtotal de ramos autónomos.
  Sin sumarlos, el Anexo 1 falla por 15,207.5 mdp.*
- **Los analíticos del proyecto reproducen el bruto del Anexo 1** al peso: 8,306,699.0 de
  Gobierno Federal más 3,440,097.8 de entidades.
- **El CSV de datos abiertos reproduce los analíticos xlsx** al peso. Dos rutas
  independientes, dos hosts distintos, el mismo número.
- **El corte por función reproduce el corte por programa**, en los dos ámbitos.
- **El total del artículo 1o. de la ILIF es el gasto neto total del decreto**: 10,193,683.7.
- Las nueve identidades internas del CGPE: balance, RFSP, no programable, devengado contra
  pagado, composición de ingresos.
- Los puentes: participaciones del CGPE contra Ramo 28; Adefas contra Ramo 30; gasto neto
  menos financiamientos igual a ingresos presupuestarios.
- **Proyecto 2025 menos su neteo igual a su gasto neto total**: 9,302,015.8. La línea
  primaria queda validada en los dos extremos.

### 2.2 Las razones a PIB, todas dentro de una décima

RFSP, balance, ingresos, tributarios, gasto neto, costo financiero, SHRFSP y las pensiones
del Anexo 3. La peor difiere 0.039 pp.

### 2.3 Flujo contra acervo

| | mdp |
|---|---|
| Δ SHRFSP (2026 menos 2025 estimado) | 1,355,995.8 |
| RFSP 2026 | 1,587,349.9 |
| efecto del tipo de cambio (−0.613 pp sobre 12.2 pp de deuda externa) | −237,353.8 |
| **residuo** | **+5,999.7** = **+0.015 % del PIB** |

---

## 3. **Un hallazgo de objeto en la fuente oficial**

La única identidad que no cerró al primer intento fue el balance primario, por **499.9 mdp**.

El CGPE 2026 rotula ese renglón **«Superávit ECONÓMICO primario»**. El CGPE 2025 rotulaba el
mismo renglón **«Superávit primario PRESUPUESTARIO»**, y para el mismo año —2025 aprobado—
publicaba **217,807.2**, mientras el CGPE 2026 publica **218,307.2**.

**Mismo año, dos rótulos, 500.0 mdp de diferencia, en las dos columnas del cuadro.** Esos
500.0 mdp son el balance no presupuestario. Con el objeto bien nombrado, la identidad cierra
al décimo en los dos años.

Es el error característico de la Parte III que la rúbrica fija desde 2023 —la cifra correcta
con el nombre equivocado— **cometido por la fuente oficial**, y la nota metodológica de la
SHCP lo autoriza (p. 3). **La equivalencia se declara una vez en la nota de método y no se
corrige.** Va al capítulo 13.

---

## 4. Diffs por clave · `datos/diffs_2025_2026.csv`, 2,397 filas

**Proyecto 2025 contra proyecto 2026**, la línea primaria, posible por primera vez a este
nivel. Detalle explicado en `diffs_explicados.md`.

| nivel | claves | aparecen | desaparecen |
|---|---|---|---|
| ramo | 51 | 3 (178,486.1 mdp) | 5 (3,735.0 mdp) |
| programa | 874 | **271 (5,330,813.3 mdp)** | **358 (3,154,347.5 mdp)** |
| unidad responsable | 1,384 | 124 (1,390,999.0 mdp) | 172 (1,515,686.6 mdp) |
| subfunción | 88 | — | — |

**2026 es un año de reclasificación excepcional.** Casi la mitad del gasto programable pasa
por una clave que cambió. Los ocho movimientos que hay que anticipar antes de redactar:

1. **Cinco ramos se extinguen** (IFT, INAI, COFECE, CRE, CNH) y tres nacen (54 Mujeres,
   55 ATDT, 56 IMSS-Bienestar).
2. **IMSS-Bienestar cambia de ramo por tercer año:** 19 → 47 → **56**. El Ramo 47 cae
   −95.4 % real sin una sola decisión de gasto detrás.
3. **La Guardia Nacional SÍ se mudó a Defensa**, al revés que en 2025, cuando se comprobó
   expresamente que no. Del Ramo 36 UR H00 al Ramo 07 UR 148, y con ella la función 1.7
   entra al ramo militar.
4. **Defensa sube 12.3 % nominal y, sin la Guardia Nacional, caería 3.1 %.**
5. **El ferroviario se muda por tercer año**, ahora a la UR D00.
6. **Pensiones: toda la nomenclatura cambia de clave.** Y los 795,824 del Ramo 19 y los
   795,824 del IMSS son el mismo dinero visto dos veces.
7. **El programa mayor de salud del IMSS se renumera** (011 → 031) y también cambia de
   nombre: no lo encuentra ni una búsqueda por clave ni una por nombre.
8. **Las dos empresas cambian de nombre**: «Pemex Consolidado» → «Petróleos Mexicanos»,
   «CFE Consolidado» → «Comisión Federal de Electricidad`. Un filtro por nombre da cero.

**El punto 8 nos volvió a pasar.** El primer intento de calcular el gasto de Pemex y CFE
devolvió 0.0 para las dos empresas, con un filtro por nombre. Es la misma trampa que partió
el Ramo 38 en la corrida 2025. **La regla existía y se incumplió otra vez**; queda anotada
como reincidencia, no como novedad.

---

## 5. `datos/` construido · 36 archivos, `_fuentes.csv` con 30 filas

Toda cifra del documento sale de aquí. Ninguna se teclea en el cuerpo del texto.

**Lo que ya se puede decir, con la fuente cerrada:**

| | proyecto 2025 | proyecto 2026 | real |
|---|---|---|---|
| Gasto bruto (GF + entidades) | 10,795,085.1 | 11,746,796.8 | **+3.83 %** |
| Gasto neto total | 9,302,015.8 | 10,193,683.7 | +4.57 % |
| **Pensiones y jubilaciones (Anexo 3)** | 1,637,665.1 | 1,704,159.2 | **−0.71 %** |
| Función Salud (bruta) | 888,527.1 | 974,302.2 | **+4.63 %** |
| Función Educación (bruta) | 1,071,949.8 | 1,161,862.4 | +3.42 % |
| Función Combustibles y Energía | 1,373,266.1 | 1,614,806.4 | **+12.20 %** |
| Costo financiero | 1,388,373.6 | 1,572,073.3 | +8.09 % |
| **Financiamiento por cada 100 pesos de ingreso** | **13.40** | **14.45** | — |

**Dos titulares que el dato ya sostiene y que hay que verificar antes de escribir:** las
pensiones caen en términos reales por primera vez en la serie, y la salud sube 4.6 % real
después de caer 12.2 % el año anterior. **Las dos exigen el diff antes que la prosa.**

**El gasto corriente estructural cumple su límite:** 3,868,319.9 contra un máximo de
4,220,033.1 mdp, con 351,713.2 de holgura. Es la comprobación que la corrida 2025 omitió y
que CIEP sí hizo.

### 5.1 Anexos transversales — el capítulo 12 tiene material propio

Doce anexos, **5,215,304.6 mdp: el 74.3 % del gasto programable.**

- **El anexo de igualdad entre mujeres y hombres vale 599,145.4 mdp y el 48.1 % son
  programas de pensión.** Su renglón mayor, con 261,776.1 mdp, es la Pensión para el
  Bienestar de las Personas Adultas Mayores: **el 43.7 % de todo el anexo, en un solo
  programa que no es de igualdad de género sino de vejez.**
- **Existe un anexo de «Consolidación de una Sociedad de Cuidados», 466,674.9 mdp.** Es el
  capítulo de economía de los cuidados que la comparación de 2025 nos señaló como omisión, y
  ahora tiene fuente propia.
- **170 de los 288 programas etiquetados aparecen en más de un anexo**, y suman 4,995,476.4
  mdp: **el 95.8 % del etiquetado transversal está en programas que se cuentan más de una
  vez.** El total de 5,215,304.6 no es dinero adicional; es una suma de etiquetas.

---

## 6. Una cifra tecleada de memoria, otra vez

Al construir `ingresos_art1o.csv` se escribieron de memoria los renglones de la ILIF 2025.
**Cuatro de las primeras seis estaban mal**, y por márgenes grandes: los impuestos, 4,929,412.4
contra los 5,297,812.9 reales; el ISR, 2,591,780.0 contra 2,859,575.1.

Se detectaron al cotejar contra el PDF **antes** de escribir una sola línea del documento, y
se corrigieron. **La corrida 2025 registró exactamente este incidente en su bitácora** —una
cifra tecleada de memoria, en el único lugar donde se tecleó— y volvió a ocurrir.

**Regla, reforzada: toda cifra entra a `datos/` desde su fuente o no entra.** La comodidad de
teclear un número que uno "recuerda" es el modo de falla más persistente de este proyecto.

---

## 7. Lo que falta para la fase 3

- **Matrícula por nivel educativo, afiliación a IMSS e ISSSTE, padrón de programas
  pensionarios.** Sin ellos, `C5.2`, `C6.5` y parte de `C14.3` no se publican.
- **El salto del Ramo 18 Energía** (+84.5 %) y su relación con el gasto de Pemex: hay que
  establecer qué es apoyo fiscal y qué es doble conteo **antes** de escribir el capítulo 3.
- **Los techos de endeudamiento** del artículo 2o. de la ILIF, aún sin extraer.
- **El reparto del Ramo 33 por entidad** (Anexo 22 del decreto) para el capítulo 10.
