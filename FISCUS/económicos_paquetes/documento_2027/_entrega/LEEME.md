# Implicaciones del Paquete Económico 2027 — proyecto LaTeX portátil

**Autoría ITED.** Documento sobre el proyecto de Paquete Económico 2027, escrito el día de
su entrega al Congreso, el 8 de septiembre de 2026.

**Lleva tres notas de actualización fechadas**, al final del documento, y el cuerpo no se
reescribió en ninguna de las tres. La del **9 de septiembre** registra los anexos que la
Gaceta no sirvió hasta el día siguiente, corrige un renglón del registro y publica dos
hallazgos que el paquete completo permite. La del **10 de septiembre** deja constancia de
que el índice de la Gaceta se corrigió solo y confirmó el mapa de anexos que el documento
había reconstruido de los PDF, y verifica las cuentas de la declaratoria urbana contra el
archivo de las 43.636 AGEB. **Ninguna cifra del cuerpo cambió en ninguna de las dos.**

La del **12 de septiembre** es distinta: **corrige afirmaciones del cuerpo**. Los analíticos
del proyecto sí estaban publicados, bajo un prefijo de dirección que el documento no sondeó;
con ellos reparte el perímetro pensionario por institución, separa la salud del IMSS de sus
pensiones y hace la auditoría de etiquetado de los anexos transversales, incluido el Anexo
32, que el cuerpo no leyó. Corrige además la causa de la caída del gasto corriente
estructural, que el CGPE explica en su p. 24, y el signo del titular de pensiones por
persona, que depende del deflactor. **Ninguna cifra del cuerpo estaba mal calculada; lo que
cambia es lo que el cuerpo dijo que no se podía saber y dos lecturas que excedían su
cálculo.**

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
| `capitulos/` | los veintitrés archivos de capítulo, incluidas las tres notas de actualización |
| `capitulos/cuadros/` | los treinta cuadros, **generados, no escritos a mano** |
| `datos/_fuentes.csv` | una fila por cifra, con documento y ubicación |
| `datos/ramos.csv` | Anexo 1 de los decretos 2026 y 2027, por clave de ramo |
| `datos/ramo33.csv` | los ocho fondos del Ramo 33, del Anexo 22 |
| `datos/anexos.csv` | totales de los anexos transversales de los dos ejercicios |
| `datos/gaceta_anexos_2027.csv` | los trece anexos del paquete que sirve la Gaceta, con la letra que el índice les daba el día de la entrega |
| `datos/vivienda_art61.csv` | la estimación del artículo 61 de la Ley de Vivienda, del anexo N |
| `datos/gaceta_indice_convergencia.csv` | lo que el índice de la Gaceta dijo de cada anexo en sus tres versiones |
| `datos/zap_urbanas_conteos.csv` | las cuentas de la declaratoria urbana, declaradas y recalculadas |
| `datos/zap_municipios_nuevos.csv` | los siete municipios que sólo existen bajo la clave actualizada |
| `datos/gce_limite_2027.csv` | el cuadro del gasto corriente estructural de la p. 24 del CGPE |
| `datos/cgpe_p32_2027.csv` | programas sociales e inversión prioritarios, p. 32 del CGPE |
| `datos/ruta_a/` | los CSV de la tercera nota, producidos desde los analíticos del proyecto (el guion que los genera exige los analíticos y no viaja aquí) |
| `generar_cuadros.py` | produce los cuadros desde los CSV de `datos/` |
| `a_markdown.py` | produce la versión en Markdown desde el mismo LaTeX |
| `validar_latex.py` | comprobación estática previa a compilar |

## Advertencia sobre las cifras

**Las variaciones reales de este documento usan el deflactor del PIB (1,040) y no coinciden
con las que imprime el CGPE 2027**, que están calculadas con aproximadamente 1,0325. La
diferencia es sistemática y vale unos 0,8 puntos porcentuales. Está explicada en la nota de
método del propio documento.
