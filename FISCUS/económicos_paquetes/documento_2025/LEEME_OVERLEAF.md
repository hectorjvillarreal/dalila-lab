# Implicaciones del Paquete Económico 2025 — proyecto de Overleaf

Documento del ITED, proyecto FISCUS.

## Cómo compilar

1. En Overleaf, **Nuevo proyecto → Subir proyecto** y sube este zip.
2. El archivo principal es **`main.tex`** (Overleaf debería detectarlo solo; si no,
   *Menú → Main document → main.tex*).
3. Compilador: **pdfLaTeX**. **No** requiere `shell-escape`.
4. Compila **dos veces** para que cuadren el índice y las referencias cruzadas.

## Qué contiene

```
main.tex                     preámbulo, portada e índice
capitulos/                   los diecisiete archivos de capítulo
capitulos/cuadros/           los veintiún cuadros, GENERADOS, no escritos a mano
datos/                       los .csv de los que sale cada cuadro
datos/_fuentes.csv           registro de procedencia: documento, ubicación y tier
```

**Ninguna cifra está tecleada en el cuerpo del texto.** Cada cuadro se genera desde
un `.csv` de `datos/` y cada `.csv` tiene su fila en `datos/_fuentes.csv` con el
documento, la ubicación y el tier de donde viene. Si un dato cambia, se regenera el
cuadro y el texto no se toca.

Los guiones que generan los cuadros (`tablas.py`, `generar_cuadros.py` y los
`construir_*.py`) **no van en este zip** porque Overleaf no los necesita. Viven en
el repositorio, junto con `verificar.py`, que corre las cincuenta pruebas de cierre
contable, y `validar_latex.py`, que corre las comprobaciones estáticas.

## Paquetes

Solo los que Overleaf trae de fábrica: `inputenc`, `fontenc`, `babel` (spanish),
`geometry`, `booktabs`, `longtable`, `graphicx`, `caption`, `fancyhdr`, `pgfplots`,
`siunitx` e `hyperref`. Ninguna fuente externa, ningún paquete que haya que
instalar, nada que exija `shell-escape`.

## Estado: ya compila

**El documento se compiló** con pdfLaTeX, tres pasadas: **57 páginas, 0 errores, 0
referencias sin resolver, 4 desbordes de caja de menos de 8 pt** (líneas de prosa,
dentro de la tolerancia normal de un texto justificado). El PDF resultante viene
en la entrega.

Si la versión anterior no compiló en Overleaf gratuito, el sospechoso principal
era **la generación de fuentes de mapa de bits**: sin `lmodern`, la combinación de
`fontenc` T1 con Computer Modern obliga a `mktexpk` a generar fuentes al vuelo. En
esta máquina eso costaba 8.2 segundos por pasada; con `lmodern` baja a 3.1. En un
servidor compartido y con el límite de tiempo del plan gratuito, esa diferencia
decide. **`lmodern` ya está en el preámbulo.**

Además se corrigieron, en este orden de importancia:

1. **Once cuadros se salían de la caja**, hasta 363 pt, porque la primera columna
   no envolvía el texto. Ahora usa un tipo de columna `L{ancho}` que parte los
   nombres largos en varias líneas.
2. **Las etiquetas del eje de años salían como «2,025»**, porque `siunitx` y
   `pgfplots` comparten el separador de millares y un año no es una cantidad.
3. **Las tres curvas de una figura salían idénticas**: `\addplot[...]` sobrescribe
   la lista de estilos; con `\addplot+[...]` se respeta, y ahora se distinguen por
   trazo y por marca, que es lo que hace falta para leerlas en blanco y negro.
4. **Una figura mezclaba el acervo (51.4) con los flujos (de −3.9 a 0.6)** en el
   mismo eje, con lo que los flujos quedaban aplastados contra el cero.

## Qué revisar en la primera compilación

Ya compilado, quedan por mirar con ojo editorial. Pasó 104 comprobaciones estáticas (llaves y entornos balanceados, todo
`\input` apuntando a un archivo existente, todo `\ref` con su `\label`, paquetes
dentro de la lista permitida, columnas de `pgfplots` existentes en su `.csv`), pero
eso no es lo mismo que compilar. Conviene mirar:

- **Desbordes de caja** en los cuadros anchos. C1\_2, C2\_1 y C12\_4 van envueltos
  en `\resizebox`; C10\_1, C11\_1, C12\_2 y C7\_3 van como `longtable` porque no
  caben en una página.
- **La marginalia.** El margen derecho es de 4.8 cm con `marginparwidth` de 3.3 cm.
  Si alguna nota al margen queda larga, se acorta el texto del `\marginal`.
- **Las columnas tipo `S` de siunitx.** Las celdas vacías salen como `{---}`, que
  siunitx acepta. Si alguna celda no numérica se coló sin llaves, el error lo dirá
  con nombre de cuadro.
- **La colocación de flotantes**, que en un documento con veintiún cuadros siempre
  pide algún ajuste.

## Convenciones del documento

Están declaradas en la **Nota de método**, que va antes del primer capítulo:
aprobado contra aprobado, deflactor del PIB de 4.3 % declarado por el CGPE, las
cinco declaraciones del contrafactual, y la regla propia de que **toda diferencia
en millones de pesos dice si es nominal o real**.

Los números usan convención mexicana: millar con coma y decimal con punto,
configurado una sola vez en `siunitx`.
