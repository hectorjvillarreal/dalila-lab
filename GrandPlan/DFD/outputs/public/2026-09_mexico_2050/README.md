# México en 2050: no serán 149 millones — gráfica pública

> **English header.** Public communication chart (Sept 2026): Mexico's total population 2025–2050
> from the INEGI EIC 2025 count under three fertility levels (1.5, 1.23, falling to 0.9), against
> UN WPP 2024 medium. **Not a forecast, not a DFD scenario, not IM-6** — it does not use the v1.6
> scenario table or the EIC-rebased skeleton. Its standing rests on reproducibility only.
> Build instruction: `_crossrefs/_build_instructions/2026-09-23_DFD_public-chart_mex2050_commit-and-verify.md`.
> Publication of the PNG is Héctor's decision; do not copy it outside this folder.

## Qué muestra y qué no es

La gráfica `figures/mexico_2050_fecundidad_realista.png` proyecta la población total de México de
2025 a 2050 partiendo del conteo de la Encuesta Intercensal 2025 del INEGI, con tres niveles de
fecundidad (sube a 1.5; se queda en 1.23; baja a 1.0 en 2030 y 0.9 después), frente a la variante
media de la ONU (WPP 2024).

**No es** un pronóstico, **no es** un escenario de DFD y **no es** IM-6. No usa la tabla de escenarios
v1.6 ni el esqueleto rebasado a la EIC. Estas cifras no alimentan el corpus, la tabla de
escenarios, la nota EIC 2025 ni IM-6.

## Método (cinco líneas)

1. Proyección por componentes: grupos quinquenales de edad × pasos de cinco años, 2025–2050.
2. Base 2025 = total EIC 2025 (130,911,314), con la estructura edad-sexo de la ONU 2025 reescalada dentro de tres grupos amplios para igualar las proporciones EIC (0–14 = 21.6 %, 65+ = 10.1 %).
3. Mortalidad (tablas de vida abreviadas, punto medio del paso), migración neta (totales anuales de la variante media, perfil edad-sexo fijo) y patrón de fecundidad por edad: ONU WPP 2024 media. Razón de sexos al nacer 1.05.
4. Sólo cambia el **nivel** de la fecundidad entre escenarios.
5. Validación: con base y TGF de la ONU, el método debe reproducir la cifra ONU 2050 con error < 0.5 M; el script termina con error si no.

## Reproducción

```
cd GrandPlan/DFD/outputs/public/2026-09_mexico_2050
~/miniforge3/envs/dalila/bin/python mex2050_projection.py   # Python ≥ 3.10 + matplotlib
```

La primera corrida descarga cinco archivos de la ONU (~290 MB) a `data/` (ignorado por git).

**Script:** `mex2050_projection.py`, SHA-256
`12d1d03139d0243055e8bedefd7f81b1b0e2511601d1f3e643be6c0745d3db24` (2026-09-23, after edit 4).
The original was `8e3d947b9b3c1047ead6c6f6309726fa6c5c97bce9ec968bda9e72e3eaead1f9`, a byte-for-byte copy of the
instruction's appendix. **Edit 4** of the Anne/Cath review of the nota v0.2
(`_crossrefs/corpus/demographics/_pending/2026-09-23_nota-EIC2025-v0.2_Anne-Cath-review.md` §4–§5) is the one
permitted edit beyond `EIC_SHARES`: one sentence appended to the method note (`src`) after "…148.9 millones)."
The added sentence is «Si además se usa la emigración que midió el INEGI, las cifras de 2050 bajan cerca de 1.5 millones
(ver la nota ITED de septiembre de 2026).» After the rerun, exit was 0 and `results/scenarios.csv`
(`7e521a13…26f6`), `results/validation.txt` (`dade4cf0…a2d0`) and `results/inputs_sha256.txt` were
**unchanged**; only the text moved. For the record, the nota v1.0 gap at equal fertility is 1.4 M
(136.9 vs 135.5 M; 130.1 vs 128.7 M). "Cerca de 1.5" is the reviewers' wording and was kept verbatim.

**Insumos ONU** (descargados 2026-09-23 de
`https://population.un.org/wpp/assets/Excel%20Files/1_Indicator%20(Standard)/CSV_FILES/`; idénticos
a los de la corrida en el chat):

```
a04d7d1486a5eb2832cc812d599448f0a71e8ac9e1e7e6fa4066673d6a2487cd  WPP2024_PopulationByAge5GroupSex_Medium.csv.gz
c0d3b5b7e992902df3be1980cfa86c440c1cd673ecec9d4826142a03aece04ec  WPP2024_Fertility_by_Age5.csv.gz
286ac36bb1415e2e1ade03acfef0a29f0e4c087e2f78e38c48f50c5df89082bc  WPP2024_Demographic_Indicators_Medium.csv.gz
3aa9b324ba654ae61e292889be0677d30d97061a30c2c05a0ecc86cc2c5c8159  WPP2024_Life_Table_Abridged_Medium_2024-2100.csv.gz
66b84489fd7875b62de9b40d960b803b8c8439367c98deab89c2f770970925b9  WPP2024_TotalPopulationBySex.csv.gz
```

**Validación** (`results/validation.txt`):
`Validation: UN base + UN medium TFR -> 2050 = 148.71 M; UN published 148.95 M; 0-14 in 2050 = 26.14 M`

## Resultados de la re-ejecución en Dalila (2026-09-23)

| Escenario | 2025 | 2035 | 2050 | 0–14 en 2050 |
|---|---|---|---|---|
| `sube_1.5` | 130.9 | 135.7 | 136.9 | 20.7 |
| `observada_1.23` | 130.9 | 132.9 | 130.1 | 16.7 |
| `baja_0.9` | 130.9 | 131.5 | 124.2 | 12.1 |

`results/scenarios.csv` SHA-256 `7e521a134f8ede0add7c27816a4d7181c10b9656e16f1b25b67b5ee0608626f6`
(coincide con la corrida del chat). Salida 0. Todas las condiciones de aceptación se cumplen.
El PNG se revisó visualmente (matplotlib 3.10.9, DejaVu Sans); su hash no es criterio de
aceptación.

## Insumos EIC 2025 — verificación (paso 3 de la instrucción)

- **Total 130,911,314**: INEGI, EIC 2025, Resultados de la Encuesta (RR 37/26, 2026-09-22),
  `_crossrefs/corpus/demographics/sources/INEGI_2026-09-22_EIC2025_RR-37-26.pdf`. Equivale a
  130,393,389 en viviendas particulares + 517,925 de población complementaria.
- **Proporciones 0–14 y 65+**: recalculadas del tabulado de datos abiertos *INEGI, Encuesta
  Intercensal 2025, «Principales resultados por localidad de 50 000 y más habitantes»*
  (identificador `NTMPPIEG_INEGI_UES-EIC-2025`, conjunto `conjunto_datos_eic2025_105.csv`, fila
  nacional `CVEGEO = 000000000`, `ESTIMADOR = Valor`; modificado 2026-09-22; acceso 2026-09-23),
  archivado en `_crossrefs/corpus/demographics/sources/INEGI_2026-09-22_EIC2025_datos-abiertos_105_localidad50k.zip`
  (SHA-256 `e6ad7e8f8661f414face015e50e8d95652ab07442e912c76191eefd77defa182`).

| | Conteo | Proporción (÷ POBTOT 130,393,389) | Suma de `PCN_P_*` quinquenales | En el script |
|---|---|---|---|---|
| 0–14 (`POB0_14`) | 28,124,921 | 21.57 % | 5.81 + 7.42 + 8.35 = 21.58 % | 21.6 % |
| 65+ (`POB65_MAS`) | 13,194,535 | 10.12 % | 3.70 + 2.61 + 3.81 = 10.12 % | 10.1 % |

**Resultado: verificado.** Ambas coinciden a un decimal; `EIC_SHARES` y la nota de método no se
modificaron. Observación: las proporciones del tabulado son sobre la población en viviendas
particulares; el script las aplica al total que incluye la población complementaria (sin
desglose por edad en el tabulado). Con la población complementaria repartida según la estructura
no-hogar del CPV 2020, 65+ = 13,233,867 / 130,911,314 = 10.11 % (`eic2025_65plus_check.md`); no
cambia el redondeo.

## Limitaciones conocidas (verbatim de la instrucción)

1. The EIC 65+ share exceeds CONAPO's conciliación by ~1.2 M at mid-2025; this is unresolved
   (Q4 gate). It barely moves total population to 2050 but would matter for any dependency
   chart built on this base.
2. Net migration is the UN medium's, not the EIC-observed −230 k/yr; using the EIC flow would
   lower every line.
3. The EIC 2025 reference date (15 Oct) is treated as the 2025 start without a time shift.
4. The UN line starts ~1 M above INEGI's count; the gap in 2050 is fertility *and* base.

## Autoría

Anne (método), Claude (código), septiembre 2026. Re-ejecución y verificación: Claude Code
(Dalila), 2026-09-23. Revisión independiente opcional (Cath o sesión nueva, sin leer el script)
pendiente de decisión de Héctor.
