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

## Adenda 2026-09-05 (corrida de evaluación CIEP 2021)

Durante la evaluación del documento CIEP 2021 (`_evaluacion/2021/`) se descargaron en fase 1, por mandato de su instrucción (§2), ocho analíticos presupuestarios xlsx: los cuatro del PPEF 2021 (`2021/2021_ppef_analitico-*.xlsx`, ruta `ppef.hacienda.gob.mx/work/models/PPEF2021/analiticosPresupuestarios/Proyecto/`) y los cuatro del PEF 2020 aprobado (`2020/2020_pef_analitico-*.xlsx`, ruta `pef.hacienda.gob.mx/work/models/PEF/Analiticos_Historico/2020/Autorizado/`). Verificados (`PK`), sha256 en `_manifiesto.csv`, tier `oficial_primaria`. Los siete PDF de CIEP 2020–2026 quedaron registrados con tier `derivada_ciep` (provisional; la columna por sección sigue pendiente). Manifiesto: 50 filas.

Rutas 2022–2026 (solo HEAD, nada descargado): las páginas de analíticos responden y listan archivos, pero todos los xlsx devuelven 404, igual que los tomos. Queda por probar la ruta del aprobado (`Analiticos_Historico/{t}/Autorizado/`). Detalle en `_aprendizaje/mapa_fuentes.md`.

## Adenda 2026-09-05 (corrida de evaluación CIEP 2022)

Sin descargas. Verificaciones por HEAD (una petición cada 2 s): exposición de motivos del PPEF 2022 (`/work/models/PPEF2022/docs/exposicion/EM_Documento_Completo.pdf`, `EM_Capitulo_1.pdf`) 404; miscelánea fiscal, iniciativa de LFD y LIF en `/work/models/PPEF2022/paquete/ingresos/` 404. Ruta del **PEF aprobado** (`pef.hacienda.gob.mx/work/models/PEF/Analiticos_Historico/{t}/Autorizado/ac01_ra_pp_ur_og.xlsx`): 200 con content-type xlsx para 2022–2026, sin descargar (tarea lateral 11.1 de la instrucción 2022). Detalle en `_aprendizaje/mapa_fuentes.md` y en `_evaluacion/2022/_bitacora_evaluacion.md`. Manifiesto sin cambios (50 filas).

## Adenda 2026-09-06 (corrida de evaluación CIEP 2023)

Descargas (todas registradas en `_manifiesto.csv`, ahora 55 líneas): (1) nota metodológica **SHCP, Balance Fiscal en México, abril 2023**, obtenida de la Gaceta Parlamentaria (`gaceta.diputados.gob.mx/PDF/65/2023/may/Shcp_balanceF-20230509.pdf`; la ruta canónica `secciones.hacienda.gob.mx/…/1bfm.pdf` sirve la edición vigente 2026 y Wayback no tiene 2023), escaneo sin texto, en `_metodologia/`, `oficial_primaria`; (2) **Cantú, Ramones y Villarreal (2016)** desde Wayback (la ruta de la UNAM devuelve 404 desde 2026), en `_metodologia/`, con el tier nuevo **`autoral_ited`** (el vocabulario pasa de dos a tres valores; decisión de tier por sección pendiente); (3) analíticos del **PEF aprobado** de entidades 2022 y 2023 (`pef.hacienda.gob.mx/…/Analiticos_Historico/{t}/Autorizado/ac01_ra_pp_ur_og_efe.xlsx`, con el bundle de certificados), en `2022/` y `2023/`, `oficial_primaria`, para la serie pensiones IMSS / cuotas IMSS (1.55 en 2022, 1.59 en 2023). Sonda a Transparencia Presupuestaria: cáscara JS sin enlaces, rutas adivinadas 404, nada descargado. DOF consultado en HTML para la trayectoria del DUC (65/58/54/40). Detalle en `_evaluacion/2023/_bitacora_evaluacion.md` y `_aprendizaje/mapa_fuentes.md`.

## Adenda 2026-09-06 (corrida de evaluación CIEP 2024, educación)

**Descargas (10 filas nuevas en `_manifiesto.csv`, ahora 64):** analíticos del **PEF aprobado** de Gobierno Federal y de entidades para 2023 y 2024, en sus cuatro cortes (`ac01_ra_pp_ur_og`, `ac01_ra_f_ur_og` y sus versiones `_efe`), ruta `pef.hacienda.gob.mx/work/models/PEF/Analiticos_Historico/{t}/Autorizado/`; y las **LIF aprobadas 2022, 2023 y 2024**, ruta `finanzaspublicas.hacienda.gob.mx/work/models/Finanzas_Publicas/docs/paquete_economico/lif/lif_{t}.pdf`. Los diez archivos se habían bajado en la fase 1 sin registrarse; las URL se reconstruyeron y **se verificaron una por una contra `Content-Length` del servidor: los diez coinciden al byte**. Todos `oficial_primaria`, con sha256.

**Trampa de lectura de los analíticos, para no volver a tropezar:** los datos están en la hoja **`Hoja1`**, no en la primera hoja, que es un resumen de 45 filas por ramo y hace creer que el archivo está vacío. Columnas F / FN / SF = finalidad / función / subfunción; el código de programa se arma como `MOD[0] + PP[:3]` porque la modalidad va en columna aparte.

**Resonda del árbol PPEF: no volvió, pero el diagnóstico cambia.** Las subpáginas `/es/PPEF2024/exposicion_de_motivos` y `/es/PPEF2024/analiticos_presupuestarios` responden **200 y enumeran los archivos**; los siete archivos que listan (Carta, `EM_Documento_Completo.pdf`, `EM_Capitulo_{1..4}.pdf`, `EM_Anexo.pdf`) dan **404**. Control 2021: el mismo `EM_Documento_Completo.pdf` responde **200 application/pdf**. Es **almacén de archivos roto o reubicado para 2022–2026, no retirada de documentos**. Wayback no tiene la exposición de motivos del PPEF 2024. Hallazgo lateral: las páginas índice listan los analíticos **sin** el segmento `/Proyecto/` y esa ruta da 404 incluso para 2021; la que sirve lo lleva. No tomar los href del portal como ruta canónica.

**Transparencia Presupuestaria comparte la cadena TLS mal encadenada de la SHCP** y el mismo bundle (YR1 + `root-yr-by-x1` por `--cacert`) la arregla; sin él falla con «unable to get local issuer certificate». `/es/PTP/Datos_Abiertos` devuelve 1,919 bytes de cáscara JS, sin un solo enlace a archivo y sin la cadena «PPEF», lo que corrobora lo que CIEP denuncia en su presentación de 2024.

**Faltante del proyecto: baja de catorce piezas a cinco.** Se resolvió tras cinco corridas el pendiente de la exposición de motivos de la ILIF: **no existe como documento separado porque el PDF de la ILIF la contiene**. Verificado en los nueve ejercicios 2018–2026 (oficio de remisión, exposición de motivos, articulado; encabezado literal en 2020–2026, sin encabezado en 2018–2019; en 2024 ocupa las páginas 1–65 y el articulado empieza en la 66). **Las nueve piezas «ILIF exposición de motivos» dejan de contarse como faltantes.** El faltante real es **la exposición de motivos del PPEF 2022–2026, cinco documentos**, y están caídos en el servidor, no ausentes del portal.

**Series.** La de pensiones IMSS / cuotas IMSS se rehízo con las LIF aprobadas y **el híbrido desaparece**: las LIF 2022–2024 coinciden con sus ILIF en las cuotas, así que los valores marcados como híbridos eran ya aprobado contra aprobado. Serie aprobada: **1.545 (2022), 1.594 (2023), 1.627 (2024)**. Serie ex ante: 1.31 (2020), 1.46 (2021), **detenida** porque la exposición de motivos del PPEF no existe para 2022–2026. El pasivo pensionario se rehízo con tres campos por observación y **la sospecha se confirma: la caída de 8.5 puntos es una comparación entre añadas y la comete la fuente oficial**, que en el CGPE 2023 pone 43.6 % (saldo 2021, pesos 2021, PIB 2021) contra 52.1 % (saldo 2020, pesos 2020, PIB 2020) como si fuera un cambio anual. Sigue congelada para calibración. Detalle en `_evaluacion/2024/_bitacora_evaluacion.md` §7.

**Remarcado retroactivo de 2023, ejecutado *ex post* el 2026-09-06:** veinte filas `aprox` pasan a `tipo_error = deflactor` (§2.10 de la instrucción v3). Todo conteo de `tipo_error` de 2023 anterior a esta fecha las excluye.

**Resultado de la evaluación.** 115 filas; 84 verificables; **87 % de coincidencia sobre verificable**, el punto más alto de la serie 2020–2024, pero **el salto de 65 % a 87 % es de las fuentes disponibles y no del evaluado**: por primera vez la corrida tuvo los analíticos completos de los dos años y pudo reconstruir los agregados de CIEP al mdp. Once errores, de los cuales **ocho son contradicciones internas del documento**. Con eso se cierra la serie de patrones: ingresos falla por base, gasto federal por perímetro, deuda por nombre, **gasto federalizado por consistencia interna**. Los tres hallazgos principales: la matrícula implícita de la Figura 8.2 **sube** 0.41 % mientras el texto atribuye el alza del gasto por alumno a «1.8 millones de NNA menos»; la nota al pie 11 presenta una cifra deflactada (22,297) como el monto que la Cámara aprobó en 2023 (21,275.7 corrientes); y el «mínimo histórico en puntos del PIB» solo se sostiene mezclando el PIB base 2013 con el base 2018, que es el cambio de vintage que el propio capítulo de deuda del documento sí corrige.

## Adenda 2026-09-06 (corrida de producción: documento propio ITED sobre el Paquete Económico 2025)

**Cambio de producto.** Las cinco corridas anteriores evaluaron; ésta produce. El entregable es un documento completo del género, de autoría ITED, en Markdown y LaTeX compilable, con la comparación contra CIEP al final y solo al final. Vive en `documento_2025/`.

**Control del ejercicio.** Pacto de estructura sellado a las **21:36:40**, escrito sin red y sin abrir ninguna pieza del paquete 2025 ni el documento de CIEP. Los trece capítulos se redactaron y comprometieron antes de las **23:08:39**, hora de la primera apertura de CIEP. Las marcas están en el historial de git.

**Hallazgo que condicionó la corrida: el CGPE 2025 se publicó sin capa de texto.** Noventa de sus noventa y una páginas son imagen; la única con texto trae las fórmulas del PIB potencial. El portal no sirve otra edición. Las cifras se leyeron de páginas renderizadas a 150 dpi y **se validaron por identidad contable y no por relectura**: cincuenta pruebas de cierre y de coherencia entre anexos, todas pasan. Los cuatro anexos que resuelven el documento son II.5, II.6, III.1 y III.2, páginas 81, 82, 84 y 85.

**Descargas (verificadas al byte):** Ley de Ingresos aprobada 2025 y los cuatro analíticos del PEF aprobado 2025.

**Perímetro de pensiones, adjudicado y no elegido.** El Anexo 3 del decreto publica los gastos obligatorios con y sin pensiones; su diferencia reproduce al mdp, en 2024 y 2025, la construcción desde los analíticos (tipo de gasto 4 de entidades más tipo de gasto 4 del GF sin la partida 45203). Es la técnica que la rúbrica adopta: **buscar la fuente independiente que adjudique el perímetro en vez de argumentarlo.**

**El documento.** Trece capítulos, 7,722 palabras de prosa, 513 afirmaciones cuantitativas, 21 cuadros generados desde datos registrados, y ningún capítulo por debajo del umbral. Cuatro huecos declarados en el cuerpo y no solo en bitácora. **La compilación queda abierta:** esta máquina no tiene LaTeX y la preferencia es no instalarlo, así que hay 96 comprobaciones estáticas que pasan y el criterio de aceptación 1.3 hay que cerrarlo en Overleaf.

**Errores propios, registrados porque son material de rúbrica.** Agrupar el gasto por nombre de ramo partió el Ramo 38, que cambió de nombre, e inventó una variación de 100 %: es el error de perímetro que este proyecto le señala al género desde 2020, cometido por nuestra herramienta. Seleccionar programas por nombre no encuentra «Personas **Adultas** Mayores». Y la única cifra que se tecleó de memoria estaba mal.

**Comparación contra CIEP 2025.** Coinciden las tres cifras de cabecera, incluidos los 13.4 pesos de cada 100 de financiamiento y las pensiones no contributivas con una diferencia de 1.1 mdp sobre 527 mil millones. **Hallazgo que solo se puede hacer un año después:** la Cámara aumentó el gasto educativo en 18,674.8 mdp entre el proyecto y el aprobado, lo suficiente para cambiar el signo del capítulo, de una caída real de 1.2 % a un aumento de 0.4 %. **Deflactor de CIEP recuperado: 1.04252**, que no es el del PIB sino el de la fórmula del límite de gasto corriente estructural; sus columnas rotuladas «PEF 2024» están en pesos de 2025, como en 2024.

**Contaminación:** ninguna en cifras, verificable por el orden de sellado. Dos en forma, y la más ilustrativa es que los dos documentos abren con la misma frase, «X pesos de cada 100 provendrán de financiamiento», escrita de forma independiente.

**Artefacto nuevo:** `_aprendizaje/protocolo_lectura_en_vivo.md`, con el orden de descarga, el orden de verificación, qué se puede afirmar a las dos horas, qué exige veinticuatro, y qué no se afirma nunca sin fuente en mano.

## Adenda 2026-09-07 (corrida de precarga para 2027)

**Qué es esta corrida.** No evalúa ni produce documento: **mueve trabajo fuera del
reloj.** La ejecuta `INSTRUCCIONES_preparacion_2027.md`, cuyo criterio de terminación son
diez puntos. **Los diez quedan cumplidos**, tres de ellos con un faltante declarado que se
nombra abajo.

### Parte A — las correcciones que pidió la comparación 2026

**La compuerta semántica, artefacto nuevo** (`_aprendizaje/compuerta_semantica.md`). Es la
primera entrada de la rúbrica que **ninguna identidad contable puede verificar**: en 2026
las treinta y tres pruebas cerraron al peso y aun así tres afirmaciones excedieron su
perímetro. La regla: *el perímetro de la frase debe coincidir con el perímetro del
cálculo.* Se corrió sobre el documento 2026 y **se reescribieron diez frases ---tres del
resumen ejecutivo, dos de Pensiones, tres de Inversión y dos de Gasto federalizado--- sin
tocar una sola cifra.** El documento recompila en 66 páginas.

Hallazgo del procedimiento, incorporado al paso 3: **cuando una frase compara dos
crecimientos, tiene que decir si compara tasas o niveles.** «Crece más del doble que lo
etiquetado» era ambiguo; lo que es más del doble es la tasa.

**El recuadro del deflactor** (§2 de la instrucción) va en la nota de método, con entorno
`recuadro` nuevo en el preámbulo. Dice tres cosas: deflactor del PIB para todo agregado
fiscal y toda razón a PIB; índice al consumidor sólo para el poder de compra de una
prestación individual, y **en ningún cuadro presupuestal**; y la sensibilidad con
inflación promedio **en una sola línea y sólo ahí**.

**La inconsistencia de la nota de método, corregida y rastreada.** El ejemplo de las dos
líneas de comparación ---+0,81 / +0,70 / −0,47 en educación--- **es del ejercicio 2025 y
la nota lo atribuía a 2026**, donde el capítulo correspondiente publica +3,4 %. El error
se había propagado a `rubrica.md` y a `especificacion_genero.md`; los tres quedan
corregidos con la nota de la corrección a la vista. Las cifras verdaderas de 2026 son
**+3,4 % en la línea P y +2,2 % en la línea G**, y el punto y dos décimas de diferencia
son los **12 641,1 mdp** que la Cámara añadió a la función educativa en diciembre de 2024.
**Ninguna comprobación estática lo veía: las dos cifras son correctas en su lugar y sólo
el vecindario las contradice.** De ahí la entrada 9 de la rúbrica.

**Defecto propio encontrado de paso:** el conversor a Markdown (`a_markdown.py`) borraba
los comentarios de LaTeX con `%.*` **sin excluir el `\%` escapado**, y con él se comía el
resto del renglón. **218 renglones del entregable en Markdown de 2026 terminaban en una
diagonal suelta y sin su signo de porcentaje.** Corregido con un lookbehind; el archivo
recuperó 8 KB de texto.

### Parte B — la precarga

**Capa demográfica, ocho series** (`datos_demograficos/`, tier `externa_demografica`):
CONAPO nacional y por entidad, matrícula de la SEP, derechohabientes del ISSSTE, registro
de IMSS-Bienestar, padrón único de Bienestar, contraste con Banco Mundial, y
**asegurados del IMSS**, que era *la* carencia de 2026.

**Cómo se resolvió el IMSS, que la corrida 2026 dio por perdido.** Tres cosas: el host
**va por HTTP** ---`https://` devuelve 503---; el portal es **Drupal y no CKAN**, así que
`package_search` devuelve HTML y por eso la sonda anterior lo declaró muerto; y el
**catálogo nacional no tiene la serie**. La ruta es directa al archivo mensual,
`datos.imss.gob.mx/sites/default/files/asg-AAAA-MM-DD.csv`, estable desde 1997. Pesa 400
MB, viene separado por barra vertical y en latin-1: **se agrega y se borra.** Julio de
2025: 30 642 265 asegurados; julio de 2026: 31 071 555. **ASEGURADOS NO ES
DERECHOHABIENTES** y la advertencia va en `_fuentes.csv` y tiene que llegar al cuadro.

**Serie del perímetro de la regla fiscal, 2018–2026** (§3.2, prioritaria): hecha, y
**corrige un dato de la propia instrucción** ---la LIF 2023 aprobada no devolvió el tope
de 3,1 %: quedó sin tope, como la iniciativa---. Documenta que el tope de 2026 iguala el
déficit con 1,8 mdp de diferencia, que la cláusula desapareció en 2024–2025 y volvió
abarcando **capital humano**, y que el renglón «balance sin inversión» **dejó de
publicarse** en el CGPE 2026. La conexión con Pemex se sostiene y está acotada: la ley
crea la posibilidad de excluir 0,68 % del PIB y el CGPE retira la evidencia; **no se
afirma que se haya aplicado.**

**Diff, identidades y rutas.** El diff corre contra 2025→2026 y resuelve los dos casos
obligatorios: IMSS-Bienestar a través de tres ramos (−0,59 % real, no extinción) y la
Guardia Nacional (−33,68 % real a través del cambio de ramo). Las **treinta y tres
identidades** quedan parametrizadas por ejercicio ---las pruebas son permanentes, las
cifras viven en `restituciones/{año}.json`--- y **cierran las treinta y tres contra
2026**. Las rutas de descarga: veinticinco renglones probados.

**Esqueleto de LaTeX** (`documento_2027/`): dieciséis capítulos ---uno nuevo, la regla
fiscal---, plantillas, `bibliografia.bib`, `LEEME.md` y `PLANTILLAS.md`. **Comprobación
estática 0 errores, dos pasadas de pdflatex, PDF de 41 páginas**, y el ZIP abierto en un
directorio limpio recompila idéntico. El cuadro de relleno se incluye por la ruta desde el
maestro en los dieciséis capítulos, para que el camino que se rompió veintiuna veces en
2025 y otras veintiuna en 2026 esté probado antes de la corrida. *Desviación declarada:
la carpeta se llama `documento_2027/` y no `_documento_2027/`, para no romper la serie
`documento_2025`, `documento_2026`.*

**Series históricas, y lo que se descongeló.** La serie ex ante de pensiones IMSS / cuotas
estaba detenida desde 2021 «porque la exposición de motivos del PPEF no existe desde
2022». **No hacía falta:** el numerador sale del analítico del **proyecto**, y esos
analíticos existen para 2020–2026. Faltaban los de 2022 y 2023; se descargaron ---más los
aprobados de 2021 y 2022 que faltaban--- y quedaron en el manifiesto, que pasa de 85 a 100
archivos registrados. **La serie pasa de dos puntos a siete**, y los dos viejos se reprodujeron al
milésimo (1,31 y 1,46 contra 1,306 y 1,463 calculados de cero). **Todos los puntos ya
registrados se reprodujeron menos uno**, que difiere en dos milésimas por el perímetro de
las pensiones no contributivas y **se deja a la vista en vez de ajustarlo para que
cuadre.**

**Regla nueva que sale de aquí:** el CGPE se publica **una sola vez, con el paquete**, de
modo que **no existe un CGPE aprobado** y toda razón que lo use es ex ante por
construcción. En la serie aprobada esas cuatro filas van vacías a propósito. La versión
anterior de estas series las mezclaba.

**Hallazgo lateral, verificado en los siete ejercicios:** al comparar proyecto contra
aprobado, **el total de las entidades de control directo cambió una sola vez en siete
años** (2024, −25 442,9 mdp) y el del Gobierno Federal dos (2020 y 2024). En cinco de
siete la Cámara **no movió un peso de ningún total: reasignó dentro.** En 2023, con el
total del Gobierno Federal idéntico al peso, se movieron diez ramos con suma neta cero
---Bienestar −6 342,1; INE +4 475,5; Poder Judicial +2 425,1---. **Un documento que
compare totales concluirá que la Cámara no hizo nada. Hizo, y el diff es lo que lo
muestra.** Y explica por qué las cinco razones que viven en entidades dan idéntico ex ante
y aprobado.

**Checklist de omisiones** (`_aprendizaje/checklist_omisiones.md`), que **sustituye al
comparador**: veintidós renglones en tres bloques ---los que la precarga desbloqueó, las
omisiones propias con fuente pública disponible, y los que dependen de una fuente que no
estará en vivo---, cada uno con su fuente y su columna de disponibilidad. El renglón que
más pesa: **la vara externa de suficiencia en salud se quedó fuera dos años seguidos** y
es una línea de texto y un cociente.

### Los tres faltantes, declarados

1. **Las cuatro razones que necesitan CGPE o Anexo 3 sólo llegan a 2024** hacia atrás: los
   escalares de años anteriores no están en forma legible por máquina y **el CGPE 2025 es
   un escaneo sin capa de texto**.
2. **2018 y 2019 quedan fuera de las series**: no hay analíticos en carpeta y el artículo
   1o. de 2018 no se extrae con el patrón que sirve de 2019 en adelante.
3. **La columna `no_trabajadores` del cubo del IMSS no se separó**: el denominador de
   asegurados incluye a quien no tiene empleo asociado. Para separarla hay que volver a
   bajar 400 MB.

