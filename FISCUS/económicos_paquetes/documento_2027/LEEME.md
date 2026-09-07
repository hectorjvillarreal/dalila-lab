# Documento propio ITED — Paquete Económico 2027 · ESQUELETO

**Construido el 2026-09-07, un año antes de la entrega**, como precarga §3.5 de
`INSTRUCCIONES_preparacion_2027.md`. Todo el contenido es relleno: se sustituye
íntegro durante la corrida. **Ningún minuto del reloj de 2027 debe irse en depurar
compilación.**

## Estado verificado

| comprobación | resultado | fecha |
|---|---|---|
| comprobación estática (`validar_latex.py`) | 0 errores, 0 avisos | 2026-09-07 |
| dos pasadas de `pdflatex` | **PDF de 41 páginas, 344 KB** | 2026-09-07 |
| warnings de compilación | 3 líneas, ninguna de error | 2026-09-07 |
| ZIP abierto en directorio limpio y recompilado | ver `_entrega/` | 2026-09-07 |

## Cómo compilar

```
./compilar.sh
```

Corre la comprobación estática, dos pasadas de `pdflatex` sin `shell-escape`, y copia el
PDF a `_entrega/`. TinyTeX en `~/.TinyTeX/bin/x86_64-linux`. **Compilado en Dalila, no en
Overleaf.** Si falta un paquete: `tlmgr install <paquete>`.

## Restricciones duras

- **`siunitx` prohibido.** Su sintaxis cambió entre versiones mayores y rompe en
  instalaciones anteriores. **Los números se formatean al generar los cuadros.**
- **`lmodern` siempre.** Sin él, T1 con Computer Modern genera fuentes bitmap y agota el
  tiempo de compilación.
- `pgfplots` con `\pgfplotsset{compat=1.16}`.
- **Paquetes admitidos:** `fontenc`, `inputenc`, `lmodern`, `babel` (spanish), `geometry`,
  `fancyhdr`, `booktabs`, `graphicx`, `caption`, `longtable`, `array`, `pgfplots`,
  `hyperref`.
- **Prohibidos:** `siunitx`, `minted`, `fontspec`, `unicode-math`, cualquier cosa que exija
  `shell-escape`, fuentes no estándar y **cualquier paquete que haya que instalar**.

## La trampa que este proyecto pisó dos veces

**LaTeX resuelve `\input` desde el directorio del archivo maestro, no desde el del capítulo
que lo incluye.** Un cuadro incluido desde `capitulos/05_salud.tex` se escribe
`capitulos/cuadros/C5_1`, no `cuadros/C5_1`. Veintiuna inclusiones rotas en 2025 y
veintiuna en 2026. La comprobación estática las detecta; ninguna lectura del texto lo hace.
**El esqueleto ya trae un cuadro de relleno incluido por la ruta correcta en los dieciséis
capítulos, para que el camino esté probado antes de la corrida.**

## Estructura

```
main.tex                  maestro; preámbulo, capa de presentación y orden de capítulos
capitulos/*.tex           19 archivos: frente, dieciséis capítulos, cierre y registro
capitulos/cuadros/*.tex   cuadros GENERADOS — no editar a mano
datos/                    un CSV por cuadro, con _fuentes.csv
figuras/                  PDF de figuras, generados por guion
bibliografia.bib          referencias metodológicas; el documento no usa bibtex
PLANTILLAS.md             lámina, ficha, «qué no sabemos» y declaración de no redactable
compilar.sh               comprobación estática + dos pasadas + reporte
validar_latex.py          96 comprobaciones que no exigen compilar
```

## Índice de capítulos

Dieciséis capítulos, uno más que en 2026: **`14_regla_fiscal`**, que es el hallazgo que las
dos comparaciones perdieron y que la serie de `_aprendizaje/serie_perimetro_regla_fiscal.md`
deja precargado. Su primera tarea el día de la entrega es leer el artículo correspondiente
de la ILIF 2027.

## Lo que falta hacer con el reloj corriendo

Sustituir el relleno. Nada más. Los datos, la capa demográfica, el diff, las identidades y
las rutas de descarga están precargados fuera de `documento_2027/`, en `_herramientas/`,
`datos_demograficos/` y `_aprendizaje/`.
