# src/ — Sección 10 del Núcleo 13

Scripts de la sección 10 («Esquemas de financiamiento alternativos»). Leen los experimentos 1 y 2 sin modificarlos; las
cifras nuevas de la v1.1 las calcula `e_1…/src/seccion10_v11.py` dentro del experimento 1. Se corren con el entorno
`dalila` desde esta carpeta, en este orden (la versión, `v1` o `v1.1`, va como argumento; por omisión, `v1.1`):

| Script | Qué hace | Lee | Escribe |
|---|---|---|---|
| `figuras.py` | Las 8 figuras (F10a_1 a F10b_4) a 5.4 in de ancho, 9 pt; colores y marcadores fijos por escenario | `e_1…/outputs/tables/` (incluida `seccion10_v11_cuota_fija_patronal.csv`), `e_2…/tablas/` | `figuras/*.png` (300 ppp), `*.svg`, `*.csv` |
| `cifras_mapa.py` | Mapa explícito de cada cifra del texto a su clave en `NUMBERS.md`, a una semilla o a `config.yaml` | — | — (lo importa `verificar.py`) |
| `verificar.py [versión]` | Verificaciones 8.1 a 8.9 de la v1.0 y 5.3, 5.6, 5.7 y 5.8 de la v1.1 | el .md de la versión, registros `numbers_computed.json`, `config.yaml`, anexo v4 del experimento 2 | `tablas/seccion10_cifras[_v1.1].csv`, `data/verificaciones_<versión>.json` |
| `conciliacion.py` | Cifras compartidas con el documento de JP; marca diferencias mayores a 1 % | registros de los dos experimentos | `tablas/conciliacion_seccion10.csv` |
| `docx_seccion10.py [versión]` | Los dos .docx con el formato de JP (ver su docstring): notas al pie, tablas que no se parten, figuras al 85 %; verifica el hash del original y que la copia conserve comentarios y cambios con control | el .md, `figuras/*.png`, el .docx de JP | `N13_seccion10_…_<versión>.docx`, `…_con_seccion10_<versión>.docx`, `data/hash_original_despues.txt` |

Para revisar las páginas: convertir con `soffice --headless --convert-to pdf`, renderizar con `pdftoppm` y medir la franja
blanca más alta de cada página.
