# src/ — Sección 10 del Núcleo 13

Scripts de la sección 10 («Esquemas de financiamiento alternativos»). Leen los experimentos 1 y 2 sin modificarlos.
Se corren con el entorno `dalila` desde esta carpeta, en este orden:

| Script | Qué hace | Lee | Escribe |
|---|---|---|---|
| `figuras.py` | Las 8 figuras (F10a_1 a F10b_4); colores y trazos fijos por escenario; 6 in de ancho, 9 pt | `e_1…/outputs/tables/`, `e_2…/tablas/` | `figuras/*.png` (300 ppp), `*.svg`, `*.csv` |
| `cifras_mapa.py` | Mapa explícito de cada cifra del texto a su clave en `NUMBERS.md`, a una semilla o a `config.yaml` | — | — (lo importa `verificar.py`) |
| `verificar.py` | Verificaciones 8.1 a 8.9: extensión, cifras, expresiones prohibidas, años, legibilidad (Fernández Huerta), apartados, frases obligatorias, términos | el .md, registros `numbers_computed.json`, `config.yaml` | `tablas/seccion10_cifras.csv`, `data/verificaciones.json` |
| `conciliacion.py` | Cifras compartidas con el documento de JP; marca diferencias mayores a 1 % | registros de los dos experimentos | `tablas/conciliacion_seccion10.csv` |
| `docx_seccion10.py` | Los dos .docx con el formato de JP (ver su docstring); verifica el hash del original y que la copia conserve comentarios y cambios con control | el .md, `figuras/*.png`, el .docx de JP | `N13_seccion10_…_v1.docx`, `…_con_seccion10_v1.docx`, `data/hash_original_despues.txt` |

Para revisar las páginas: convertir la copia con `soffice --headless --convert-to pdf` y renderizar con `pdftoppm`.
