# ¿Y si en América Latina cada mujer tuviera un solo hijo? — gráfica pública

> **English header.** Public communication chart (Sept 2026): total population of Latin America and the
> Caribbean (49 UN WPP countries and territories), 2025–2100, if every country's TFR moves from its latest
> observed level to 1.0 in 2030 and stays there, against UN WPP 2024 medium. **Theoretical scenario, not
> a forecast, not a DFD scenario, not IM-6.** It does not use the v1.6 scenario table. Its standing rests on
> reproducibility only. Built on Héctor's request in a Claude Code session (2026-09-24); no build
> instruction was filed. Publication of the PNG is Héctor's decision.

## Qué muestra

`figures/latam_un_hijo_regional.png`: población total de la región bajo el escenario (roja) frente a la
variante media de la ONU (gris), más un recuadro sobre menores de 15 y mayores de 65.

| | 2025 | 2030 | 2050 | 2075 | 2100 |
|---|---|---|---|---|---|
| ONU, variante media (publicada) | 667.9 | 687.7 | 730.1 | 698.8 | 613.4 |
| Escenario: 1 hijo por mujer desde 2030 | 666.9 | 673.1 | 642.3 | 510.5 | 329.3 |
| Menores de 15 (escenario) | 144.3 | 125.2 | 68.7 | 35.7 | 19.8 |
| 65 y más (escenario) | 69.9 | 83.1 | 137.8 | 192.1 | 163.6 |

Millones. Los mayores de 65 superan a los menores de 15 desde 2040.

## Método

1. Proyección por componentes, grupos quinquenales de edad × pasos de cinco años, 2025–2100, país por
   país (49 países y territorios con `ParentID` ∈ {915, 916, 931} en WPP 2024), sumando al final.
   Mismo método que `../2026-09_mexico_2050/mex2050_projection.py`.
2. Base 2025: ONU WPP 2024, **salvo México = INEGI EIC 2025** (130,911,314; proporciones 0–14 = 21.6 %,
   65+ = 10.1 %, reescalando la estructura ONU dentro de tres grupos amplios, igual que la gráfica de México).
3. TGF: pasa linealmente dentro del paso 2025–2030 del nivel actual a 1.0 en 2030 y se queda en 1.0.
   Nivel actual = último dato de registro civil donde existe (ver abajo); ONU 2025 en los demás.
4. Mortalidad (tablas abreviadas, punto medio del paso), migración neta (totales anuales ONU media, perfil
   edad-sexo fijo), patrón de fecundidad por edad: ONU WPP 2024 media. Razón de sexos al nacer 1.05.
5. Validación: con base y TGF de la ONU, el método reproduce los totales ONU publicados con error máximo
   de **0.40 M por país-año** hasta 2100 (columnas `un_method` vs `un_published` en `results/`).

### TGF inicial observada (18 países)

Fuente: tabla de registros civiles de Fernández-Villaverde (15 sep 2026, lámina 8), en el corpus como
`_crossrefs/corpus/demographics/observations/2026-09-15_fernandez-villaverde-slides-latam.md` (endorsed,
Anne). México reemplaza el 1.51 extrapolado de esa tabla por el 1.23 de INEGI EIC 2025.

| PRI | CHL | COL | CRI | BHS | URY | JAM | ARG | CUB | MEX | BRA | DOM | BLZ | PER | PAN | NIC | GTM | BOL |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.87 | 0.99 | 1.01 | 1.12 | 1.15 | 1.19 | 1.22 | 1.23 | 1.30 | 1.23 | 1.52 | 1.61 | 1.63 | 1.67 | 1.79 | 1.80 | 1.91 | 2.06 |

TGF regional ponderada por población resultante: 1.49 (ONU 2025: 1.77), coherente con el «≈ 1.50» de la
misma tabla.

## Reproducción

```
cd GrandPlan/DFD/outputs/public/2026-09_latam_un_hijo
# requiere los CSV ONU en ../2026-09_mexico_2050/data/ (git-ignored; los baja mex2050_projection.py)
~/miniforge3/envs/dalila/bin/python lac_tfr1_projection.py   # pandas; ~1–2 min
~/miniforge3/envs/dalila/bin/python draw_regional_es.py      # matplotlib
```

Insumos: los mismos cinco archivos ONU de la gráfica de México (SHA-256 en
`../2026-09_mexico_2050/README.md`). Salidas verificadas el 2026-09-24:

```
e875f0031eb697636a23e5da5a37f4f1364c283e8104a21442a7d7731d5d3811  lac_tfr1_projection.py
067bbf2fa2436d3b1240508e50f73c3e135cf7aecfbe38c58850026f3bb25c2e  draw_regional_es.py
2636f439493d4418fc30b8cf132b656f5b37c91af084243e015b784123680cff  results/lac_tfr1_aggregate.csv
2697ac18696549cd3a868b8191c0ebd5b7fd349c2158ddd79d1dbf5e0f997085  results/lac_tfr1_results.csv
```

## Limitaciones conocidas

1. Vintages mezclados: las TGF observadas son de 2022 a 2025 y se tratan como el nivel de 2025.
2. Puerto Rico (0.87) está bajo 1.0: en el escenario su fecundidad *sube* a 1.0.
3. Argentina usa 1.23 (DEIS); RENAPER muestra 1.05 para 2024, leído en el corpus como registro
   incompleto (`observations/2026-09-23_argentina-renaper-tfr_source-discrepancy.md`).
4. Migración neta ONU media, no observada; para México, la emigración EIC bajaría la línea (ver nota EIC 2025).
5. La proporción 65+ de la EIC excede a CONAPO en ~1.2 M (compuerta Q4 sin resolver); casi no mueve el total.
6. Las cifras no alimentan el corpus, la tabla de escenarios v1.6 ni IM-6.

## Autoría

Claude Code (Dalila), 2026-09-24, a petición de Héctor. Método heredado de Anne (gráfica México 2050).
Revisión independiente pendiente de decisión de Héctor.
