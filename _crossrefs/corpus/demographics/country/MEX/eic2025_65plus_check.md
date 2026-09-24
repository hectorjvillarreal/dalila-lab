---
type: working_note
title: "65+ gate check — CPV 2020 aged forward to 15 Oct 2025 against EIC 2025"
date: 2026-09-23
added_by: Claude Code
endorsed_by:
projects: [DFD, BDH]
indicators: [population, mortality, migration]
geography: [MEX]
workflow_status: pending-anne — reading NOT chosen (ambiguous; stopped for Anne per instruction)
companion_of: eic2025_65plus_check.py
build_instruction: _crossrefs/_build_instructions/2026-09-23_demographics_commit-endorsements_nota-v0.2.md (Step 4)
governing_record: _crossrefs/corpus/demographics/_pending/2026-09-23_nota-EIC2025-v0.1_Anne-Cath-review.md §2
---

## What was done

The CPV 2020 population by single year of age and sex was taken at 15 Mar 2020 (INEGI, Censo de Población y
Vivienda 2020, cuestionario básico tabulado 01-03, `cpv2020_b_eum_01_poblacion.xlsx`, accessed
2026-09-23, sha256 `387965e0…9d`). Age "no especificado" (273,386) was prorated by sex; an unprorated variant is
also reported. Each cohort was **survived to 15 Oct 2025** (5.58 years, monthly steps) with CONAPO
2023 conciliación death rates, m = deaths / mid-year population by single age, sex and calendar year,
2020–2025. Those rates include the 2020–21 excess mortality. EIC-measured emigration at the same ages was then subtracted.
The emigration comes from RR 37/26 Gráfica 9 (emigrants Oct 2020–Oct 2025 by 5-year age and sex, as % of 1.3 M),
transcribed to `GrandPlan/DFD/outputs/briefs/2026-09_EIC2025_nota/data/eic2025_emigrants_age_sex_grafica9.csv`.
The result was compared with EIC 2025 on the same date: private dwellings plus the 517,925 complementary population at
CPV 2020 non-household age-sex shares.

Script: `eic2025_65plus_check.py`. Output: `eic2025_65plus_check.csv`, `eic2025_65plus_check_context.csv`.

## Results (prorated variant; the unprorated variant differs by < 0.3 pp)

| Group | Sex | CPV 2020 aged, net of emigration | EIC 2025 | EIC − aged | % |
|---|---|---|---|---|---|
| 65–69 | M | 2,050,943 | 2,220,836 | +169,894 | +8.3 |
| 70–74 | M | 1,502,584 | 1,567,788 | +65,204 | +4.3 |
| 75+ | M | 2,137,851 | 2,185,652 | +47,801 | +2.2 |
| **65+** | **M** | **5,691,378** | **5,974,276** | **+282,899** | **+5.0** |
| 65–69 | F | 2,411,756 | 2,610,305 | +198,550 | +8.2 |
| 70–74 | F | 1,785,440 | 1,841,599 | +56,160 | +3.1 |
| 75+ | F | 2,619,238 | 2,807,687 | +188,448 | +7.2 |
| **65+** | **F** | **6,816,434** | **7,259,591** | **+443,157** | **+6.5** |
| **65+** | **Total** | **12,507,811** | **13,233,867** | **+726,056** | **+5.8** |

Emigration subtracted at 65+: 15,600 (6,500 M, 9,100 F). This is negligible, as the record expected.

**Context: where CONAPO sits.**

| | 65+ |
|---|---|
| CPV 2020, 15 Mar 2020 (prorated) | 10,344,330 |
| CONAPO conciliación, mid-2020 | 9,860,625 (**−0.48 M vs the census**) |
| CPV 2020 aged to 15 Oct 2025 | 12,507,811 |
| CONAPO, 15 Oct 2025 (linear between mid-2025 11,698,499 and mid-2026 12,201,321) | ≈ 11,842,000 (**−0.67 M vs aged CPV**) |
| EIC 2025, 15 Oct 2025 | 13,233,867 (**+0.73 M vs aged CPV**) |

## Reading — ambiguous; not chosen

The EIC-vs-CONAPO gap on the EIC date is about +1.39 M. The check splits it roughly in half:

1. **About 0.67 M is CONAPO's.** CONAPO's conciliación was already 0.48 M below the census 65+ in 2020, and
   that difference carries forward. On this part the record's first reading holds: CONAPO understates
   the elderly relative to the census.
2. **About 0.73 M (+5.8 %) is EIC above the aged census.** This is not "aged-CPV ≈ EIC". It is also not
   cleanly the second reading (EIC age overstatement), for two reasons:
   - The excess is concentrated at **65–69 (+8.3 % both sexes)**, the cohort aged 59–64 in the census. That is
     the pattern age heaping or age drift across 60/65 would produce, in either instrument, and it favours the
     overstatement reading.
   - The aging uses CONAPO's own death rates. The cohorts reaching 65+ lose **3.25 M** to CONAPO mortality over
     2020–25, so a 10 % overstatement of that mortality would move the aged figure by ~0.32 M, about 45 % of the
     residual. CONAPO's deaths are a modelled series, not INEGI registrations, and this check cannot rule that out.
     Women's 75+ (+7.2 %) is where mortality error would concentrate, and it is elevated too.

   Two other contributions are small but point the same way: undercount of the elderly in CPV 2020 itself, and
   return migration of older migrants (EIC returns 150.8 k, age not published).

Per the instruction ("do not choose between the readings if the difference is ambiguous; report it and stop for
Anne"), **no reading is adopted and the base 65+ is not replaced**. The nota v0.2 is built on the EIC base, as
the instruction provides when this step does not conclude "EIC > aged-CPV". It carries the CONAPO-65+
sensitivity row the record asks for.

**Suggested discriminating checks (for Anne; not run):**
- (a) Rerun the aging with INEGI *registered* deaths 2020–2024 by age and sex in place of CONAPO rates. This
  bounds the mortality lever.
- (b) Compare single-year ages 58–68 in CPV 2020 and EIC 2025 for heaping at 60 and 65 (Whipple/Myers). EIC
  single-year ages are in the microdata due Nov 2026.

## Provenance of the CONAPO data (record §5 gate)

- **Copy used:** Internet Archive capture of the official zip,
  `https://web.archive.org/web/20241110075122id_/https://conapo.segob.gob.mx/work/models/CONAPO/pry23/DB/ConDem50a19_ProyPob20a70.zip`,
  sha256 `ddcf182a05888672806f43113cf9405f17ef4cb410e8f5e4017067d160b1c19b`, 80,454,093 bytes (internal
  file dates 2023-07-21 / 2023-08-01).
- **Retry of official endpoints, 2026-09-23 23:51 UTC:**
  - `https://conapo.segob.gob.mx/…/ConDem50a19_ProyPob20a70.zip` → redirect to gob.mx, **404**.
  - `http://conapo.segob.gob.mx/…` → **no response** (000).
  - `https://www.gob.mx/conapo/documentos/bases-de-datos-…-2020-a-2070` → **200**, but it serves a bot "Challenge
    Validation" page, not the page itself.
  - `https://datos.gob.mx/api/3/action/package_search?q=conapo proyecciones` → **200** (it returned 403 earlier
    the same day). It lists dataset `proyecciones-de-poblacion` (modified 2025-10-27), whose resources point to
    `repodatos.atdt.gob.mx/CONAPO/proyecciones/*.csv`. Those return **403 (Akamai "Access Denied")** to scripted
    requests.
  - The indicators file hosted on datos.gob.mx itself downloaded: `05_indicadores_demograficos_proyecciones.csv`,
    **200**, sha256 `e0407d1640f38232023cf97656a0cb7be46049b1cb2344198c7e4aaec7cae6cd`.
- **Verification against the official file (2020–2050, national):** mid-year population, deaths, births and net
  international migration are **identical**. The single-age population and death sums reproduce the official
  totals and 65+ **exactly**. TGF and e0 differ only in the third decimal (rounding in the official CSV). The
  Wayback copy is therefore the official CONAPO 2023 release. Replace the file with a direct official download
  when `repodatos` admits scripted access.
