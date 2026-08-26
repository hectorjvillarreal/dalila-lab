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
