# Implicaciones del Paquete Económico 2027 — proyecto LaTeX portátil

**Autoría ITED.** Documento sobre el proyecto de Paquete Económico 2027, escrito el día de
su entrega al Congreso, el 8 de septiembre de 2026.

**Lleva una nota de actualización fechada el 9 de septiembre**, al final del documento. El
cuerpo no se reescribió: la nota registra los anexos que la Gaceta no sirvió hasta el día
siguiente, corrige un renglón del registro y publica dos hallazgos que el paquete completo
permite. Ninguna cifra del cuerpo cambió.

## Cómo compilar

```
python3 generar_cuadros.py     # regenera capitulos/cuadros/*.tex desde datos/
python3 validar_latex.py       # comprobación estática: inclusiones, llaves, paquetes
pdflatex -interaction=nonstopmode -output-directory=_build main.tex
pdflatex -interaction=nonstopmode -output-directory=_build main.tex
```

O, en una sola pasada, `./compilar.sh`, que hace las cuatro cosas y copia el PDF a
`_entrega/`.

**Dos pasadas de `pdflatex` son necesarias** para el índice y las referencias cruzadas.

## Con qué se compiló

- **TeX Live 2026**, distribución TinyTeX (`tlmgr` revisión 79639, 2026-07-10).
- **pdfTeX 3.141592653-2.6-1.40.29**, kpathsea 6.4.2.
- Ubuntu 24.04 LTS.
- Python 3.12 para los guiones de datos. Sólo biblioteca estándar: **no requiere pandas ni
  ningún paquete externo.**

## Restricciones de portabilidad que este proyecto respeta

- **Sin `siunitx`.** Los números se formatean al generar los cuadros, en
  `generar_cuadros.py`: punto de millares y coma decimal, convención española.
- **`pgfplots` con `compat=1.16`**, declarado en el preámbulo.
- **Nada que exija `shell-escape`.**
- Sólo los paquetes de la lista permitida: `fontenc`, `inputenc`, `lmodern`, `babel`,
  `geometry`, `fancyhdr`, `booktabs`, `graphicx`, `caption`, `longtable`, `array`,
  `pgfplots` e `hyperref`. **`lmodern` es obligatorio**: sin él, T1 más Computer Modern
  genera fuentes de mapa de bits y la compilación se alarga hasta agotar el tiempo en
  servicios en línea.

## Qué hay en cada carpeta

| ruta | qué contiene |
|---|---|
| `main.tex` | maestro: preámbulo, macros de lámina y ficha, orden de capítulos |
| `capitulos/` | los veintiún archivos de capítulo, incluida la nota de actualización |
| `capitulos/cuadros/` | los veintidós cuadros, **generados, no escritos a mano** |
| `datos/_fuentes.csv` | una fila por cifra, con documento y ubicación |
| `datos/ramos.csv` | Anexo 1 de los decretos 2026 y 2027, por clave de ramo |
| `datos/ramo33.csv` | los ocho fondos del Ramo 33, del Anexo 22 |
| `datos/anexos.csv` | totales de los anexos transversales de los dos ejercicios |
| `datos/gaceta_anexos_2027.csv` | los trece anexos del paquete que sirve la Gaceta, con la letra que el índice les daba el día de la entrega |
| `datos/vivienda_art61.csv` | la estimación del artículo 61 de la Ley de Vivienda, del anexo N |
| `generar_cuadros.py` | produce los cuadros desde los CSV de `datos/` |
| `a_markdown.py` | produce la versión en Markdown desde el mismo LaTeX |
| `validar_latex.py` | comprobación estática previa a compilar |

## Advertencia sobre las cifras

**Las variaciones reales de este documento usan el deflactor del PIB (1,040) y no coinciden
con las que imprime el CGPE 2027**, que están calculadas con aproximadamente 1,0325. La
diferencia es sistemática y vale unos 0,8 puntos porcentuales. Está explicada en la nota de
método del propio documento.
