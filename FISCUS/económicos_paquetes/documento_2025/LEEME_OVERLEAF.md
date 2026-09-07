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

## Qué revisar en la primera compilación

Esta máquina no tiene toolchain de LaTeX, así que **el documento no se ha
compilado**. Pasó 96 comprobaciones estáticas (llaves y entornos balanceados, todo
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
