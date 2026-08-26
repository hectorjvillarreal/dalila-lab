---
doc_id: 20260826_COMUNIDAD_PANEL_ocho_paises_v1
project: COMUNIDAD
doctype: PANEL
slug: panel_ocho_paises
version: 1
date: 2026-08-26
added_by: Claude Code
endorsed_by:
build_instruction: 20260826_COMUNIDAD_BUILDINST_boston_deck_v1
status: archivo aparte (§4.7); no es lámina
---

# Panel comparativo — los ocho países en la sala

Argentina, Colombia, Costa Rica, Ecuador, México, Paraguay, República Dominicana, Uruguay. Entregable opcional 4 de la instrucción de construcción (§4.7): archivo de apoyo para el expositor, no lámina. Todas las cifras verificadas el 26 de agosto de 2026; método y fuentes al pie de cada bloque.

## Cuadro síntesis

| País | % 65+ 2024 | % 65+ 2050 | Cierre del bono demográfico | Gasto salud gobierno general % PIB (2023) | Gasto de bolsillo % gasto corriente (2023) | Informalidad (OIT, 1S 2025) | Ocupados que cotizan / afiliados a pensiones |
|---|---|---|---|---|---|---|---|
| Argentina | 12.4 | 19.9 | 2034 | 6.18 | 24.5 | 42.6 | s/d |
| Colombia | 9.8 | 20.6 | 2022 (ya terminó) | 5.74 | 14.6 | 54.5 | 42.9 (2024) |
| Costa Rica | 12.2 | 25.3 | 2024 (terminando) | 4.61 | 24.1 | 34.7 | 72.8 (2023) |
| Ecuador | 8.3 | 17.2 | hacia 2034 | 4.68 | 30.9 | 70.0 | 35.3 afiliado (2024) |
| México | 8.2 | 17.0 | hacia 2030 | 2.68 | 41.2 | 51.1 | 34.1 (2024) |
| Paraguay | 6.5 | 12.4 | hacia 2043 | 4.63 | 36.3 | 67.2 | 24.7 (2024) |
| República Dominicana | 7.9 | 15.0 | hacia 2037 | 2.95 | 25.1 | 53.1 | 43.1 afiliado (2024) |
| Uruguay | 16.0 | 23.5 | 2032 | 6.53 | 17.1 | 22.3 | 77.3 (2024) |
| **América Latina y el Caribe** | 9.9 | 18.9 | 2028 (CEPAL) / 2029 (WPP, meseta 2026–2031) | 4.05 | 29.7 | 46.7 | sin agregado |

Lecturas para el expositor: (1) Costa Rica y Colombia ya cerraron el bono y Costa Rica será el país más envejecido de los ocho en 2050; (2) México tiene el gasto público en salud más bajo y el gasto de bolsillo más alto de la mesa; (3) Uruguay y Costa Rica son las excepciones a "menos de la mitad cotiza": no generalizar en su presencia; (4) Ecuador y Paraguay superan dos tercios de informalidad.

---

## Panel demográfico — ocho países + ALC (WPP 2024, variante media)

| País | % 65+ 2024 | % 65+ 2050 | Año cierre del bono (mín. razón de dependencia, WPP 2024) | Año cierre según CEPAL (lectura del gráfico III.2, CEPAL 2026) | Duración del bono, años (CEPAL, Serie 140, gráfico 18) | TGF 2024 | % 80+ 2050 |
|---|---|---|---|---|---|---|---|
| Argentina | 12,4 | 19,9 | 2034 | ≈2034 | 47 | 1,50 | 5,3 |
| Colombia | 9,8 | 20,6 | 2022 | ≈2022 (ya terminó) | 59 | 1,63 | 5,8 |
| Costa Rica | 12,2 | 25,3 | 2024 | ≈2024 (terminando) | 62 | 1,32 | 8,4 |
| Ecuador | 8,3 | 17,2 | 2034 | ≈2034 | 71 | 1,81 | 4,3 |
| México | 8,2 | 17,0 | 2030 | ≈2030 | 59 | 1,89 | 4,4 |
| Paraguay | 6,5 | 12,4 | 2043 | ≈2043 (después de 2040) | 88 | 2,42 | 2,7 |
| República Dominicana | 7,9 | 15,0 | 2037 | ≈2037 | 72 | 2,22 | 3,8 |
| Uruguay | 16,0 | 23,5 | 2032 | ≈2032 | 53 | 1,40 | 7,7 |
| **América Latina y el Caribe** | 9,9 | 18,9 | 2029 (meseta 2026–2031) | **2028** (cifra textual) | 64 | 1,80 | 5,1 |

Fuentes:
- Naciones Unidas, DESA, División de Población, *World Population Prospects 2024*, variante media: `WPP2024_PopulationByAge5GroupSex_Medium.csv.gz` y `WPP2024_Demographic_Indicators_Medium.csv.gz` (https://population.un.org/wpp/ → Download). LocID: ARG 32, COL 170, CRI 188, ECU 218, MEX 484, PRY 600, DOM 214, URY 858, ALC 1830. Cálculo propio: cierre del bono = año de mínimo de la razón de dependencia total [(0–14 + 65+)/(15–64)]; coincide en todos los casos con el año de máximo de la participación 15–64. Script: scratchpad `wpp/compute.py`.
- CEPAL (2026), *Impactos del cambio demográfico en América Latina y el Caribe: retos y opciones para la política pública*, LC/CRPD.6/3, cap. III.A, p. 74 ("para el promedio de América Latina y el Caribe, el bono demográfico terminará en 2028 … En 5 países de América Latina y en 13 países y territorios del Caribe, se estima que el bono ya ha terminado") y gráfico III.2 (barras sin etiqueta numérica; años por país leídos de las coordenadas vectoriales del PDF, ±0,3 años). https://repositorio.cepal.org/handle/11362/90225
- CEPAL (2025), Serie Población y Desarrollo 140, LC/TS.2025/50, p. 33 y gráfico 18 (p. 34): duraciones por país. https://repositorio.cepal.org/handle/11362/82262
- CEPAL (2022), *Observatorio Demográfico 2022*, LC/PUB.2022/13-P, pp. 15–17: con WPP 2022 el cierre regional se proyectaba en 2029; Colombia y Costa Rica "ya han terminado, o están terminando"; Paraguay "después de 2040".

Caveats: en WPP 2024 los años 2024–2025 son ya proyección; poblaciones a 1 de julio; mínimos planos (±1–2 años) en México 2029–2032, Ecuador 2032–2035, Paraguay 2042–2045, R. Dominicana 2036–2039, ALC 2026–2031 — conviene "hacia 2030", etc. No existe tabla publicada por CEPAL con año de cierre por país; la única cifra textual es el 2028 regional. *Panorama Social 2024* no menciona el bono demográfico. Si el deck usa 2025 como base: % 65+ ARG 12,6 · COL 10,2 · CRI 12,8 · ECU 8,6 · MEX 8,5 · PRY 6,7 · DOM 8,2 · URY 16,3 · ALC 10,2.

---

## Panel — columnas de gasto en salud e informalidad (ocho países)

| País | Gasto salud gobierno general % PIB (2023) | Gasto corriente en salud % PIB (2023) | Gasto de bolsillo % gasto corriente (2023) | Informalidad OIT-PL 1S 2025 (%) | Informalidad ILOSTAT ODS 8.3.1, 2024 (%) | Ocupados que cotizan / afiliados a pensiones (% ocupados, CEPALSTAT) |
|---|---|---|---|---|---|---|
| Argentina | 6.18 | 10.27 | 24.5 | 42.6 | 51.6 (EPH, urbano) | s/d nacional |
| Colombia | 5.74 | 8.16 | 14.6 | 54.5 | 56.1 | 42.9 cotiza (2024) |
| Costa Rica | 4.61 | 6.87 | 24.1 | 34.7 | 37.4 | 72.8 cotiza (2023) |
| Ecuador | 4.68 | 7.56 | 30.9 | 70.0 | 68.6 | 35.3 afiliado (2024) |
| México | 2.68 | 5.50 | 41.2 | 51.1 | 56.4 | 34.1 cotiza (2024) |
| Paraguay | 4.63 | 8.36 | 36.3 | 67.2 | 65.4 | 24.7 cotiza (2024) |
| República Dominicana | 2.95 | 4.60 | 25.1 | 53.1 | 54.7 | 43.1 afiliado (2024) |
| Uruguay | 6.53 | 9.02 | 17.1 | 22.3 | 28.5 | 77.3 cotiza (2024) |
| **ALC** | **4.05** (BM, ZJ) | **7.94** | **29.7** | **46.7** (prom. 12 países) | **51.4** (X26, modelada) | sin agregado |

Fuentes: columnas 2–4, Banco Mundial API (`SH.XPD.GHED.GD.ZS`, `SH.XPD.CHEX.GD.ZS`, `SH.XPD.OOPC.CH.ZS`; valores idénticos a OMS GHED), https://api.worldbank.org/v2/country/MEX;ARG;COL;CRI;ECU;PRY;DOM;URY;ZJ/indicator/SH.XPD.GHED.GD.ZS?format=json&date=2015:2024&per_page=500 . Columna 5: OIT, *Panorama Laboral 2025*, gráfico 3.4 (orden verificado: Uruguay 22.3, Chile 24.9, Costa Rica 34.7, Brasil 35.8, Argentina 42.6, promedio 46.7, México 51.1, R. Dominicana 53.1, Colombia 54.5, Paraguay 67.2, Ecuador 70.0, Perú 70.8, Bolivia 82.3). Columna 6: ILOSTAT SDMX `DF_SDG_0831_SEX_ECO_RT` (ENOE, GEIH, ECE, ENEMDU, EPHC, ENCFT, ECH, EPH-urbana). Columna 7: CEPALSTAT 3136 ("aporta") y 3138 ("afiliada"), nacional, ambos sexos.
