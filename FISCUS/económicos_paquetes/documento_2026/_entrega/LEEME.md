# Documento propio ITED — Paquete Económico 2026

Proyecto LaTeX completo y portátil. **Compilado en Dalila**, no en Overleaf.

## Cómo compilar

```
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

Dos pasadas. No hace falta bibtex ni latexmk. **No usar `--shell-escape`**: nada lo exige.

El guion `compilar.sh` corre la comprobación estática, las dos pasadas y el reporte de
warnings, y copia el PDF a `_entrega/`.

## Versión de TeX usada

TinyTeX sobre TeX Live, en `~/.TinyTeX/bin/x86_64-linux`. Distribución mínima: si falta un
paquete, `tlmgr install <paquete>`.

## Restricciones duras de este proyecto

- **`siunitx` está prohibido.** Su sintaxis cambió entre versiones mayores y rompe en
  instalaciones anteriores. **Los números se formatean al generar los cuadros**, en
  `tablas.py`, con separador de miles y decimal en español aplicados de forma uniforme.
- **`lmodern` siempre.** Sin él, T1 con Computer Modern genera fuentes bitmap y agota el
  tiempo de compilación.
- `pgfplots` con `\pgfplotsset{compat=1.16}`. Este documento no lo usa para figuras externas.
- **Paquetes admitidos:** `fontenc`, `inputenc`, `lmodern`, `babel`, `geometry`, `fancyhdr`,
  `booktabs`, `graphicx`, `caption`, `longtable`, `array`, `pgfplots`, `hyperref`.
- **Prohibidos:** `siunitx`, `minted`, `fontspec`, `unicode-math`, cualquier cosa que exija
  `shell-escape`, fuentes no estándar y cualquier paquete que haya que instalar.

## Trampa que este proyecto ya pisó dos veces

**LaTeX resuelve `\input` desde el directorio del archivo maestro, no desde el del capítulo
que lo incluye.** Un cuadro incluido desde `capitulos/05_salud.tex` se escribe
`\input{capitulos/cuadros/C5_1}`, no `\input{cuadros/C5_1}`.

En la corrida de 2025 hubo veintiuna inclusiones mal resueltas. **En la de 2026 hubo
veintiuna, otra vez**, y las dos veces las encontró la comprobación estática antes de
compilar. Ninguna lectura del texto las habría revelado: rompen la compilación entera.

## Estructura

```
main.tex                     maestro
capitulos/*.tex              19 archivos: frente, catorce capítulos, cierre y registro
capitulos/cuadros/*.tex      21 cuadros, GENERADOS — no editar a mano
datos/*.csv                  todos los datos, con _fuentes.csv
datos/_externas/             denominadores demográficos
```

## Cómo se regenera todo

```
python construir_diffs.py     # diffs por clave, proyecto 2025 -> proyecto 2026
python construir_datos.py     # datos/ completo y _fuentes.csv
python verificar.py           # 33 identidades contables; DEBE dar 0 fallas
python generar_cuadros.py     # capitulos/cuadros/*.tex desde datos/
python validar_latex.py       # comprobación estática; DEBE dar 0 errores
./compilar.sh                 # las dos pasadas y el PDF
python a_markdown.py          # la versión Markdown, del mismo contenido
```

**`verificar.py` se corre después de cada cambio en los datos**, no solo al principio.

## Regla que gobierna los datos

**Ninguna cifra se teclea en el cuerpo del texto.** Toda cifra sale de un `.csv` de `datos/`
que tiene su fila en `datos/_fuentes.csv` con documento, ubicación y tier. En esta corrida se
tecleó de memoria dos veces y las dos veces la cifra era falsa; se detectó al cotejar contra
la fuente. La regla no es una formalidad.
