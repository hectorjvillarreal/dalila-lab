# Bitácora de adquisición — paquetes económicos 2018–2026

## Corrida
- Inicio (navegación y mapeo del portal): 2026-09-05T11:26:00-06:00
- Inicio (descargas): 2026-09-05T11:30:46-06:00
- Fin: 2026-09-05T11:34:41-06:00
- Fuente: https://www.finanzaspublicas.hacienda.gob.mx/es/Finanzas_Publicas/Paquete_Economico_y_Presupuesto
- Tier: oficial_primaria (SHCP).
- Alcance solicitado: CGPE, ILIF, PPEF (exposición de motivos y proyecto de decreto). Tomos y anexos excluidos por instrucción.
- Máquina: Dalila. Cliente: curl 8.x vía script Python secuencial, 1 petición cada 2 s, sin paralelismo.
- Verificación: cabecera `%PDF` en cada archivo; sha256 en `_manifiesto.csv`.

## Resultado por ejercicio

| ejercicio | CGPE | ILIF | PPEF | archivos | MB |
|---|---|---|---|---|---|
| 2018 | completa | parcial (documento único; sin exposición de motivos separada) | completa | 4 | 9.4 |
| 2019 | completa | parcial (documento único; sin exposición de motivos separada) | completa | 4 | 12.0 |
| 2020 | completa | parcial (documento único; sin exposición de motivos separada) | completa | 4 | 10.6 |
| 2021 | completa | parcial (documento único; sin exposición de motivos separada) | completa | 4 | 17.8 |
| 2022 | completa | parcial (documento único; sin exposición de motivos separada) | parcial (proyecto de decreto, manual; exposición de motivos ausente) | 3 | 8.0 |
| 2023 | completa | parcial (documento único; sin exposición de motivos separada) | parcial (proyecto de decreto, manual; exposición de motivos ausente) | 3 | 9.6 |
| 2024 | completa | parcial (documento único; sin exposición de motivos separada) | parcial (proyecto de decreto, manual; exposición de motivos ausente) | 3 | 12.2 |
| 2025 | completa | parcial (documento único; sin exposición de motivos separada) | parcial (proyecto de decreto, manual; exposición de motivos ausente) | 3 | 28.6 |
| 2026 | completa | parcial (documento único; sin exposición de motivos separada) | parcial (proyecto de decreto, manual; exposición de motivos ausente) | 3 | 12.1 |

**Totales: 31 archivos, 120.4 MB, 5 faltantes** (exposición de motivos PPEF 2022–2026; los 5 proyectos de decreto se recuperaron manualmente, ver Adenda) (más 9 piezas «ILIF exposición de motivos» que el portal no ofrece como documento separado; ver Anomalías).

## Faltantes

Todos los faltantes corresponden a la sección PPEF de los ejercicios 2022 a 2026 en `www.ppef.hacienda.gob.mx`. Los enlaces existen en las páginas HTML del portal (misma forma exacta que los de 2018–2021, que sí descargaron), pero el servidor responde 404 para cualquier archivo bajo `/work/models/PPEF2022/` … `/work/models/PPEF2026/`. Sondeos de diagnóstico sobre otros enlaces de esas mismas páginas (EM_Capitulo_1.pdf de 2022, Carta.pdf de 2026, CGPE_2026.pdf del sitio PPEF) también devolvieron 404, mientras que Carta.pdf de 2021 respondió 206 `application/pdf`. Conclusión operativa: el árbol de documentos PPEF 2022–2026 del sitio ppef.hacienda.gob.mx está caído o reubicado en la fecha de la corrida. No se construyeron rutas alternativas por instrucción.

- **2022 / ppef / `2022_ppef_proyecto-decreto.pdf`** — URL tomada del enlace del portal PPEF2022 (página principal, sección Egresos): `https://www.ppef.hacienda.gob.mx/work/models/PPEF2022/paquete/egresos/Proyecto_Decreto.pdf`. Dos intentos (2 s de espera). Respuesta del servidor: HTTP 404, `text/html`, 2978 bytes, página de error genérica de Hacienda («No se encontró la página solicitada. Es posible que ya no exista en el sitio, haya cambiado de ubicación o no esté disponible temporalmente»). Archivo descartado.
- **2022 / ppef / `2022_ppef_exposicion-motivos.pdf`** — URL tomada del enlace del portal PPEF2022 (subpágina Exposición de Motivos, fila Documento Completo): `https://www.ppef.hacienda.gob.mx/work/models/PPEF2022/docs/exposicion/EM_Documento_Completo.pdf`. Dos intentos (2 s de espera). Respuesta del servidor: HTTP 404, `text/html`, 2978 bytes, página de error genérica de Hacienda («No se encontró la página solicitada. Es posible que ya no exista en el sitio, haya cambiado de ubicación o no esté disponible temporalmente»). Archivo descartado.
- **2023 / ppef / `2023_ppef_proyecto-decreto.pdf`** — URL tomada del enlace del portal PPEF2023 (página principal, sección Egresos): `https://www.ppef.hacienda.gob.mx/work/models/PPEF2023/paquete/egresos/Proyecto_Decreto.pdf`. Dos intentos (2 s de espera). Respuesta del servidor: HTTP 404, `text/html`, 2978 bytes, página de error genérica de Hacienda («No se encontró la página solicitada. Es posible que ya no exista en el sitio, haya cambiado de ubicación o no esté disponible temporalmente»). Archivo descartado.
- **2023 / ppef / `2023_ppef_exposicion-motivos.pdf`** — URL tomada del enlace del portal PPEF2023 (subpágina Exposición de Motivos, fila Documento Completo): `https://www.ppef.hacienda.gob.mx/work/models/PPEF2023/docs/exposicion/EM_Documento_Completo.pdf`. Dos intentos (2 s de espera). Respuesta del servidor: HTTP 404, `text/html`, 2978 bytes, página de error genérica de Hacienda («No se encontró la página solicitada. Es posible que ya no exista en el sitio, haya cambiado de ubicación o no esté disponible temporalmente»). Archivo descartado.
- **2024 / ppef / `2024_ppef_proyecto-decreto.pdf`** — URL tomada del enlace del portal PPEF2024 (página principal, sección Egresos): `https://www.ppef.hacienda.gob.mx/work/models/PPEF2024/paquete/egresos/Proyecto_Decreto.pdf`. Dos intentos (2 s de espera). Respuesta del servidor: HTTP 404, `text/html`, 2978 bytes, página de error genérica de Hacienda («No se encontró la página solicitada. Es posible que ya no exista en el sitio, haya cambiado de ubicación o no esté disponible temporalmente»). Archivo descartado.
- **2024 / ppef / `2024_ppef_exposicion-motivos.pdf`** — URL tomada del enlace del portal PPEF2024 (subpágina Exposición de Motivos, fila Documento Completo): `https://www.ppef.hacienda.gob.mx/work/models/PPEF2024/docs/exposicion/EM_Documento_Completo.pdf`. Dos intentos (2 s de espera). Respuesta del servidor: HTTP 404, `text/html`, 2978 bytes, página de error genérica de Hacienda («No se encontró la página solicitada. Es posible que ya no exista en el sitio, haya cambiado de ubicación o no esté disponible temporalmente»). Archivo descartado.
- **2025 / ppef / `2025_ppef_proyecto-decreto.pdf`** — URL tomada del enlace del portal PPEF2025 (página principal, sección Egresos): `https://www.ppef.hacienda.gob.mx/work/models/PPEF2025/paquete/egresos/Proyecto_Decreto.pdf`. Dos intentos (2 s de espera). Respuesta del servidor: HTTP 404, `text/html`, 2978 bytes, página de error genérica de Hacienda («No se encontró la página solicitada. Es posible que ya no exista en el sitio, haya cambiado de ubicación o no esté disponible temporalmente»). Archivo descartado.
- **2025 / ppef / `2025_ppef_exposicion-motivos.pdf`** — URL tomada del enlace del portal PPEF2025 (subpágina Exposición de Motivos, fila Documento Completo): `https://www.ppef.hacienda.gob.mx/work/models/PPEF2025/docs/exposicion/EM_Documento_Completo.pdf`. Dos intentos (2 s de espera). Respuesta del servidor: HTTP 404, `text/html`, 2978 bytes, página de error genérica de Hacienda («No se encontró la página solicitada. Es posible que ya no exista en el sitio, haya cambiado de ubicación o no esté disponible temporalmente»). Archivo descartado.
- **2026 / ppef / `2026_ppef_proyecto-decreto.pdf`** — URL tomada del enlace del portal PPEF2026 (página principal, sección Egresos): `https://www.ppef.hacienda.gob.mx/work/models/PPEF2026/paquete/egresos/Proyecto_Decreto.pdf`. Dos intentos (2 s de espera). Respuesta del servidor: HTTP 404, `text/html`, 2978 bytes, página de error genérica de Hacienda («No se encontró la página solicitada. Es posible que ya no exista en el sitio, haya cambiado de ubicación o no esté disponible temporalmente»). Archivo descartado.
- **2026 / ppef / `2026_ppef_exposicion-motivos.pdf`** — URL tomada del enlace del portal PPEF2026 (subpágina Exposición de Motivos, fila Documento Completo): `https://www.ppef.hacienda.gob.mx/work/models/PPEF2026/docs/exposicion/EM_Documento_Completo.pdf`. Dos intentos (2 s de espera). Respuesta del servidor: HTTP 404, `text/html`, 2978 bytes, página de error genérica de Hacienda («No se encontró la página solicitada. Es posible que ya no exista en el sitio, haya cambiado de ubicación o no esté disponible temporalmente»). Archivo descartado.

## Anomalías

- **ILIF: un solo documento por ejercicio.** Tanto la tabla del punto de entrada (`ilif_{año}.pdf`) como el sitio PPEF de cada ejercicio (`LIF_{año}.pdf`, sección Ingresos) ofrecen un único PDF etiquetado «Iniciativa de Ley de Ingresos de la Federación». No existe en el portal una pieza separada denominada «exposición de motivos» de la ILIF. Se descargó el documento único como `{año}_ilif_iniciativa.pdf`; el archivo `{año}_ilif_exposicion-motivos.pdf` previsto en la instrucción no se creó en ningún ejercicio. No se abrió el PDF para comprobar si contiene la exposición de motivos (fuera de alcance).
- **Certificado TLS del portal mal encadenado.** `www.finanzaspublicas.hacienda.gob.mx` y `www.ppef.hacienda.gob.mx` (mismo certificado, SAN compartido) presentan una hoja firmada por el intermedio Let's Encrypt **YR1**, pero envían en el handshake el intermedio **R10**. curl y Python en Ubuntu 24.04 fallan con «unable to get local issuer certificate». Se resolvió sin desactivar la verificación: se descargó YR1 desde la URL AIA del propio certificado (`http://yr1.i.lencr.org/`) y la raíz «ISRG Root YR» cross-firmada por ISRG Root X1 (`https://letsencrypt.org/certs/gen-y/root-yr-by-x1.pem`), y se pasó el bundle a curl con `--cacert`. La cadena verifica contra el almacén del sistema. Los navegadores no lo notan porque descargan el intermedio faltante por AIA automáticamente. Relevante para la corrida 2027.
- **Extensiones en mayúsculas.** `cgpe_2023.PDF` (punto de entrada) y varios `precgpe_*.PDF`. La subpágina de exposición de motivos de 2024 se enlaza como `/es/PPEF2024/Introduccion` (mayúscula), el resto en minúsculas.
- **Tamaños.** CGPE 2025: 22.9 MB, muy por encima del resto (2.4–3.9 MB, salvo 2021 con 8.8 MB). ILIF uniformes entre 1.0 y 1.3 MB. No se examinó el contenido.
- **Material no clasificado / no descargado (a propósito).** En la sección Exposición de Motivos del sitio PPEF hay además: «Carta del Presidente» (2026: «Carta de la Presidenta»), capítulos sueltos EM_Capitulo_1–4 y (desde 2020) EM_Anexo. Se tomó solo «Documento Completo». En la sección Ingresos del sitio PPEF hay iniciativas de reforma (LISR/LIVA/LIEPS/CFF, LFD, LISH, LFPRH, Informe de aranceles) que no forman parte de las tres piezas solicitadas. En la columna CGPE del punto de entrada, 2019–2023 muestran «Consultar» que abre un bloque con el CGPE más «Guía PIB potencial» y «Guía metas fiscales»; se tomó solo el CGPE.
- **Duplicidad de fuentes para CGPE e ILIF.** Cada pieza está disponible en dos hosts SHCP (finanzaspublicas y ppef). Se usó finanzaspublicas (punto de entrada, menos pasos); no se comparó sha256 entre hosts.

## Notas de estructura del portal

Punto de entrada: una tabla con una fila por ejercicio (2000–2027) y columnas: Pre-criterios (Art. 42 LFPRH) | CGPE | ILIF | PPEF | LIF | PEF | Plan Anual de Financiamiento. Los enlaces a PDF son relativos a `/work/models/Finanzas_Publicas/docs/paquete_economico/{cgpe,ilif,lif,paf,precgpe,pef}/`.

Por ejercicio (idéntico en 2018–2026):

| pieza | dónde | pasos desde el punto de entrada |
|---|---|---|
| CGPE | punto de entrada, columna CGPE, enlace «PDF» (2019–2023 dentro del bloque «Consultar») | 1 |
| ILIF | punto de entrada, columna ILIF, enlace «PDF» | 1 |
| PPEF proyecto de decreto | columna PPEF «Ver Sitio» → `www.ppef.hacienda.gob.mx/es/PPEF{año}` → sección Egresos → «Proyecto de Decreto…» | 2 |
| PPEF exposición de motivos | … → `/es/PPEF{año}/introduccion` («Carta del Presidente, Exposición de Motivos, Tomos y Anexos → Consultar») → menú lateral «Exposición de Motivos» → `/es/PPEF{año}/exposicion_de_motivos` → tabla «Documento Completo» | 4 |

El sitio PPEF de cada ejercicio reproduce además el CGPE y la ILIF (`/work/models/PPEF{año}/paquete/politica_hacendaria/CGPE_{año}.pdf`, `/work/models/PPEF{año}/paquete/ingresos/LIF_{año}.pdf`). Los tomos y anexos cuelgan de `/es/PPEF{año}/introduccion` y `/es/PPEF{año}/analiticos_presupuestarios`; no se tocaron.

Para la corrida 2027: (1) preparar el bundle de certificados antes de descargar; (2) comprobar primero si el árbol `/work/models/PPEF2027/` responde, porque en 2026-09-05 los de 2022–2026 no lo hacían; (3) el punto de entrada ya lista una fila 2027 con solo Pre-criterios.

## Adenda 2026-09-05 (misma fecha, tras la corrida)

Héctor descargó manualmente los proyectos de decreto PPEF 2022–2026 y los dejó en las carpetas de cada ejercicio como `PPEF_{año}.pdf`. Verificación hecha en Dalila:

- Los cinco archivos empiezan con `%PDF`, `pdfinfo` los abre sin error, no están cifrados, y la última página se extrae limpiamente.
- Identificación por primera página (sin leer el contenido más allá del encabezado): los cinco son «PROYECTO DE PRESUPUESTO DE EGRESOS DE LA FEDERACIÓN PARA EL EJERCICIO FISCAL {año}», Título Primero, Capítulo I, Artículo 1. Es decir, el **proyecto de decreto** (articulado). Ninguno contiene la cadena «exposición de motivos» y cada uno tiene una sección «Transitorios», como el decreto 2021.
- Páginas: 2022 151, 2023 168, 2024 174, 2025 183, 2026 171 (decreto 2021: 137; exposición de motivos 2021: 376).
- Metadatos: Word 2016; fechas de creación 2021-09-07, 2022-09-08, 2023-09-08, 2024-11-15, 2025-09-08. La de 2025 coincide con la entrega tardía del paquete 2025 por cambio de administración; no es anomalía.
- Renombrados a `{año}_ppef_proyecto-decreto.pdf` e incorporados a `_manifiesto.csv` con sha256. `url_origen` quedó como «descarga manual» porque no se registró la URL; conviene anotarla si se conoce.

Estado tras la adenda: **31 archivos, 120.4 MB**. Faltante real: **exposición de motivos PPEF 2022–2026 (5 documentos)**. Las 9 piezas «ILIF exposición de motivos» siguen sin existir como documento separado en el portal.

## Archivos descargados

| ejercicio | pieza | archivo | MB |
|---|---|---|---|
| 2018 | cgpe | `2018_cgpe_criterios-generales.pdf` | 2.8 |
| 2018 | ilif | `2018_ilif_iniciativa.pdf` | 1.1 |
| 2018 | ppef | `2018_ppef_exposicion-motivos.pdf` | 4.3 |
| 2018 | ppef | `2018_ppef_proyecto-decreto.pdf` | 1.2 |
| 2019 | cgpe | `2019_cgpe_criterios-generales.pdf` | 3.8 |
| 2019 | ilif | `2019_ilif_iniciativa.pdf` | 1.0 |
| 2019 | ppef | `2019_ppef_exposicion-motivos.pdf` | 5.8 |
| 2019 | ppef | `2019_ppef_proyecto-decreto.pdf` | 1.4 |
| 2020 | cgpe | `2020_cgpe_criterios-generales.pdf` | 3.6 |
| 2020 | ilif | `2020_ilif_iniciativa.pdf` | 1.1 |
| 2020 | ppef | `2020_ppef_exposicion-motivos.pdf` | 3.4 |
| 2020 | ppef | `2020_ppef_proyecto-decreto.pdf` | 2.5 |
| 2021 | cgpe | `2021_cgpe_criterios-generales.pdf` | 8.8 |
| 2021 | ilif | `2021_ilif_iniciativa.pdf` | 1.1 |
| 2021 | ppef | `2021_ppef_exposicion-motivos.pdf` | 5.6 |
| 2021 | ppef | `2021_ppef_proyecto-decreto.pdf` | 2.3 |
| 2022 | cgpe | `2022_cgpe_criterios-generales.pdf` | 2.4 |
| 2022 | ilif | `2022_ilif_iniciativa.pdf` | 1.1 |
| 2022 | ppef | `2022_ppef_proyecto-decreto.pdf` | 4.5 |
| 2023 | cgpe | `2023_cgpe_criterios-generales.pdf` | 3.9 |
| 2023 | ilif | `2023_ilif_iniciativa.pdf` | 1.0 |
| 2023 | ppef | `2023_ppef_proyecto-decreto.pdf` | 4.7 |
| 2024 | cgpe | `2024_cgpe_criterios-generales.pdf` | 3.7 |
| 2024 | ilif | `2024_ilif_iniciativa.pdf` | 1.1 |
| 2024 | ppef | `2024_ppef_proyecto-decreto.pdf` | 7.3 |
| 2025 | cgpe | `2025_cgpe_criterios-generales.pdf` | 22.9 |
| 2025 | ilif | `2025_ilif_iniciativa.pdf` | 1.2 |
| 2025 | ppef | `2025_ppef_proyecto-decreto.pdf` | 4.6 |
| 2026 | cgpe | `2026_cgpe_criterios-generales.pdf` | 3.9 |
| 2026 | ilif | `2026_ilif_iniciativa.pdf` | 1.3 |
| 2026 | ppef | `2026_ppef_proyecto-decreto.pdf` | 6.9 |

## Adenda 2026-09-05 (corrida de evaluación CIEP 2020)

Durante la evaluación del documento CIEP 2020 (`_evaluacion/2020/`) se descargaron por demanda, conforme a la sección 7 de su instrucción, cuatro analíticos presupuestarios del PPEF 2020 en formato xlsx (ramo×programa y ramo×función, versiones Gobierno Federal y entidades). Están en `2020/` con prefijo `2020_ppef_analitico-` y registrados en `_manifiesto.csv` (35 filas). Hallazgo de estructura del portal: aunque `/work/models/PPEF2020/docs/` y `/paquete/` devuelven 404, `/work/models/PPEF2020/analiticosPresupuestarios/Proyecto/` sí sirve archivos; conviene probar esa ruta para 2022–2026 antes de dar por perdidos los materiales PPEF.

Los siete PDF `ciep_implicaciones{año}.pdf` (2020–2026) que Héctor colocó en las carpetas de ejercicio son material derivado (tier 2, CIEP) y no están en el manifiesto, cuyo esquema solo prevé `oficial_primaria`. Solo el de 2020 fue verificado (`%PDF`, sha256 `327c7e28…`).
