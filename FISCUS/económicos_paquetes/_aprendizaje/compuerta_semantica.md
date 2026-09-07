# Compuerta semántica

**Artefacto de método · FISCUS · creado 2026-09-07 · precarga §1.3 de
`INSTRUCCIONES_preparacion_2027.md`**

---

## La regla

> **El perímetro de la frase debe coincidir con el perímetro del cálculo.**

Un agregado calculado sobre una clasificación, una función o dos capítulos del
objeto del gasto **no puede nombrarse con la palabra general que designa al
conjunto mayor.** Si el cálculo es de «pensiones y jubilaciones de la
clasificación económica», la frase no dice «pensiones». Si es de los capítulos
6000 y 7000, la frase no dice «gasto de capital».

## Por qué existe

Es la lección de la comparación anónima de 2026. **Treinta y tres identidades
contables cerraron al peso y aun así tres afirmaciones excedieron su perímetro.**
Las identidades validan aritmética; **no validan semántica.** Un documento puede
cerrar perfectamente y contener un titular demasiado ancho, porque el error no
está en el número sino en el sujeto de la oración que lo lleva.

Los tres casos de 2026 son la misma falla, y ninguno era un error de cálculo:

| lo que decía | de dónde salía la cifra | por qué excedía |
|---|---|---|
| «Pensiones caen 0,7 %» | agregado de pensiones y jubilaciones de la clasificación económica | el bloque no contributivo, que está dentro de «pensiones» en el uso común, **crece** 12,1 % |
| «casi la mitad de todo el gasto de capital» son instrumentos financieros | capítulos 6000 y 7000 del objeto del gasto | «gasto de capital» nombra un conjunto mayor que esos dos capítulos |
| «menos recursos condicionados» | tasas reales de los Ramos 28 y 33 | las aportaciones **aumentan** 1,5 % real; lo que es menor es la tasa, no el monto |

**Ninguna prueba automática las habría detectado.** Es una revisión editorial y
se corre como paso obligatorio al cierre de cada capítulo, **antes de compilar.**

## El procedimiento

Se aplica a **cada titular, cada frase del resumen ejecutivo y cada pie de
figura o de cuadro.** No al cuerpo entero: el cuerpo declara su perímetro en su
propia sección y ahí el contexto lo sostiene. La compuerta protege las frases
que viajan solas.

1. **Toma la frase.** Titular, línea del resumen, pie de cuadro o de figura.
2. **Localiza el renglón de la ficha metodológica del que sale su cifra.** Si no
   se puede localizar, la frase no tiene respaldo y se borra o se calcula.
3. **Compara el sujeto de la frase con el perímetro de la ficha.** Si el sujeto
   es más amplio que el perímetro, **reescribe la frase, no la ficha.** La
   tentación inversa —ensanchar el perímetro para que la frase quede— es la
   falla que este proyecto le señala al género desde 2020.
4. **Marca cada afirmación causal** y pregúntale las cuatro del reporte:
   - ¿está documentada por la fuente, o la está infiriendo el redactor?
   - ¿puede ser una **reclasificación**?
   - ¿puede ser un efecto de **composición**?
   - ¿puede ser un efecto **contable** —cambio de añada, de base, de perímetro—?
5. **Registra en la bitácora cuántas frases se reescribieron**, por capítulo. El
   conteo es material de rúbrica: un capítulo con muchas reescrituras señala un
   perímetro mal declarado, no un redactor descuidado.

## Las reescrituras admisibles

Hay cuatro maneras de cerrar la brecha y sólo la última es mala:

- **Nombrar el objeto entero.** «El agregado de pensiones y jubilaciones de la
  clasificación económica cae 0,7 % real.» Larga, y correcta.
- **Añadir la excepción que el sujeto ancho ocultaba.** «…mientras las pensiones
  no contributivas crecen.»
- **Bajar el sujeto al perímetro real.** «Dentro de los capítulos 6000 y 7000…»
  en vez de «del gasto de capital».
- **Ensanchar el cálculo hasta el sujeto.** Legítimo sólo si el cálculo ancho se
  hace de verdad, con su identidad y su renglón de ficha. **No vale declararlo.**

## Lo que la compuerta no es

- **No es una prueba automática.** Ninguna identidad contable la sustituye, y
  ningún guion la corre. Si algún día se automatiza una parte, será la de
  localizar el renglón de ficha, nunca la de juzgar el sujeto.
- **No es un filtro de estilo.** No busca frases largas ni voz pasiva; busca
  sujetos más anchos que su cálculo.
- **No es censura del hallazgo.** Las tres frases de 2026 decían algo verdadero e
  importante. La compuerta no las quita: las hace decir exactamente lo que se
  midió.

## Prueba de la compuerta sobre un capítulo de 2026

Se corrió sobre `documento_2026/capitulos/07_pensiones.tex`, más el resumen
ejecutivo y los otros dos capítulos señalados por la comparación. **Resultado:
diez frases reescritas** —tres en el resumen ejecutivo, dos en Pensiones, tres en
Inversión y dos en Gasto federalizado— y **ninguna cifra modificada**. Ése es el
punto: la compuerta no corrige aritmética, y si alguna vez cambia un número es
señal de que el problema era otro. El documento vuelve a compilar en 66 páginas.

Hallazgo del paso 2 sobre el mismo capítulo, que no es de perímetro sino de
denominador: «la pensión media real baja» sale de un agregado dividido entre la
población de 65 años y más, que **incluye a quien no recibe pensión**. Es una
razón de presión demográfica, no una prestación media, y la frase quedó como
«el gasto pensionario medio por persona de 65 años y más». La advertencia ya
estaba en la capa demográfica; **la compuerta es lo que la hace llegar al
titular**.

**Hallazgo lateral de la primera corrida:** una de las frases marcadas no excedía
su perímetro sino que era ambigua en la magnitud comparada —«crece más del doble
que lo etiquetado», donde lo que es más del doble es la **tasa** y no el monto—.
La compuerta la atrapó porque el paso 3 obliga a leer el sujeto contra la ficha.
**Se incorpora al procedimiento: cuando la frase compara dos crecimientos, dice
si compara tasas o niveles.**
