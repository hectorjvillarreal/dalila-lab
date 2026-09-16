# Replication package — Composition of out-of-pocket health spending (Figure 7)

This package regenerates, offline and from derived aggregates only, the figure
**"Observed OOP health spending is dominated by curative items in every decile"**
(`fig07_composition.pdf`) and the three headline shares the paper reports from
this analysis: **2.0 per cent** of observed out-of-pocket (OOP) health spending
unambiguously preventive, **53.6 per cent** unambiguously curative, and
**44.5 per cent** ambiguous (Mexico, ENIGH 2024).

No survey microdata is included or required. The package contains **derived,
aggregated data only** — decile-level composition shares, national aggregate
shares, and an item-level classification table. Nothing in it identifies a
household or an individual.

## What you need

- R ≥ 4.4 with the packages `data.table` and `ggplot2` (which pulls `scales`).
- The figure was produced with R 4.4.3, data.table 1.18.4, ggplot2 4.0.3,
  scales 1.4.0, installed from conda-forge. The full pinned environment is in
  `environment/environment.yml` (recreate with
  `conda env create -f environment/environment.yml`); the exact session is
  recorded in `environment/R_sessioninfo.txt`.
- No network connection. The scripts make no downloads and no API calls.

## How to run

```
./run_all.sh
```

One command, from any working directory. It reads only from `data/`, writes
`fig07_composition.pdf` and `fig07_composition.png` into `output/`, and exits
non-zero on any failure. A run takes about one second and under 200 MB of
memory. Verified result: the PNG is byte-identical to the published figure, and
the PDF differs from the published one only in its embedded creation/modification
timestamps (pixel-identical when rasterized at 150 dpi).

## Data files

All files are UTF-8 CSV with a header row, copied byte-for-byte from the build
output — no value in them was recomputed for this package.

### `data/fig7_composition_by_decile.csv` (120 rows)

The figure's input. One row per household income decile × spending class ×
ENIGH wave. The figure uses the 2018 and 2024 waves (60 cells).

| column | type | meaning |
|---|---|---|
| `decile` | integer 1–10 | household income decile, 1 = poorest |
| `class` | text | `preventive`, `ambiguous`, or `curative` |
| `w` | numeric | survey-weighted sum of household quarterly OOP health spending on rubros in this class, pesos, constant Aug–Nov 2024 prices (general INPC) |
| `share` | numeric | `w` divided by total weighted OOP health spending in the same decile and year |
| `year` | integer | ENIGH wave: 2018, 2020, 2022, or 2024 |

The smallest cell in the figure rests on 109 unweighted expenditure records
from 79 distinct households (decile 1, preventive, 2018); no cell poses a
disclosure risk.

### `data/curative_preventive_classification.csv` (145 rows)

The auditable item-level classification behind the split. One row per health
expenditure rubro code; no household-level content.

| column | type | meaning |
|---|---|---|
| `scheme` | text | `J_2018_2022` (ENIGH J-rubros, waves 2018–2022) or `COICOP_2024` |
| `clave` | text | official rubro code (keep as text: COICOP codes have leading zeros) |
| `descripcion` | text | official ENIGH descriptor (Spanish) |
| `class` | text | `preventive`, `ambiguous`, or `curative` |
| `rationale` | text | stated judgment behind the assignment |

Classification rule: *curative* items respond to a realized health event
(illness consultations, hospitalization, surgery, therapeutic medicines, rehab
devices, ambulance, delivery); *preventive* items are anticipatory or scheduled
(prenatal control, vaccination, contraception, screening products); everything
whose motive is not observable in the rubro — OTC medicines, dental, optical,
chronic-disease maintenance, diagnostics, insurance premiums — is kept as
*ambiguous*, its own category, never forced into either side.

### `data/fig7_ambiguous_sensitivity.csv` (4 rows)

National aggregate shares by wave, including the two-way reassignment of the
ambiguous block. The paper's headline numbers are the 2024 row:
`prev_share_base` = 0.0195 (≈ 2.0%), `amb_share` = 0.4449 (≈ 44.5%), and
curative = `curative`/`tot` = 0.5356 (≈ 53.6%).

| column | type | meaning |
|---|---|---|
| `year` | integer | ENIGH wave |
| `ambiguous`, `curative`, `preventive`, `tot` | numeric | national survey-weighted OOP pesos by class, and their total, constant Aug–Nov 2024 prices |
| `prev_share_base` | numeric | preventive / total (ambiguous kept as its own category) |
| `prev_share_amb_to_prev` | numeric | preventive share if the ambiguous block is assigned wholly to preventive |
| `prev_share_amb_to_cur` | numeric | preventive share if ambiguous is assigned wholly to curative (equals the base share by construction) |
| `cur_share_amb_to_cur` | numeric | curative share if ambiguous is assigned wholly to curative |
| `amb_share` | numeric | ambiguous / total |

## Source data and how to obtain it

The aggregates derive from the **ENIGH** household income and expenditure
survey (INEGI — Instituto Nacional de Estadística y Geografía, Mexico), waves
2018, 2020, 2022 and 2024, public-use microdata available from INEGI at
https://www.inegi.org.mx/programas/enigh/nc/ for each wave. Income deciles are
household-level, survey-weighted. Only derived aggregates are redistributed
here; the microdata itself is an INEGI product and must be obtained from INEGI
under its terms of use. (The wider study also uses ENSANUT (INSP) and ENASEM;
neither enters this figure.)

## Caveats — read before comparing across waves

- **The ambiguous block is reported, not allocated.** The 44.5 per cent that
  cannot be signed is shown as its own category. Assigning it wholly to
  preventive or wholly to curative brackets the preventive share between
  roughly 2 and 46 per cent (see the sensitivity table). Any statement about
  "the" preventive share must carry that bracket.
- **Composition is not comparable across waves.** The 2024 COICOP rubros do not
  record prescription status, so therapeutic-class medicines are classed
  curative in 2024, while the 2018–2022 J-scheme splits prescribed (curative)
  from non-prescribed (ambiguous). This scheme discontinuity mechanically
  shifts spending from ambiguous to curative in 2024 relative to 2018. Do not
  read the 2018→2024 change in the curative or ambiguous share as behavior.
- Spending is out-of-pocket only; public in-kind provision (IMSS/ISSSTE/SSA
  services) is not included.

## Provenance

Code and data were extracted at commit `cd8ed6c` (branch `p3-correcciones-tex`)
of the build repository; `MANIFEST.md` lists every file with its SHA-256 and
origin. The plotting code in `code/make_fig07_composition.R` is the figure-7
block of the build's `scripts/08_figures.R`, verbatim, with paths made relative
to this package.
