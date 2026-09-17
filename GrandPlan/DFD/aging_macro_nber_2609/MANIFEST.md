---
name: MANIFEST-2026-09-17-demographics-nber-batch
description: Source manifest — maps each monitoring note in this batch to its source PDF and bibliographic record
date: 2026-09-17
added_by: Debb
endorsed_by:
protocol: PROTO-RAG-001
type: manifest
retention: permanent
---

# Manifest — Demographics Batch, 2026-09-17

## Purpose

The source filenames in `sources/` are opaque acquisition artifacts and carry no bibliographic
information. This manifest is the mapping that makes them legible, and it is the object worth
retaining under corpus-as-intellectual-provenance. **Do not rename the PDFs.** The names carry
the acquisition trace; legibility lives here.

The PDFs are third-party working papers held as local reference copies for research. They are
**sources, not corpus objects**: no PROTO-RAG-001 entry frontmatter, no promotion status, no
endorsement, not for redistribution.

## Mapping

| # | Note (`notes/`) | Source (`sources/`) | Paper | Dated | pp |
|---|---|---|---|---|---|
| 1 | `2026-09-17_costs-of-building-walls.md` | `f249677.pdf` | Bernardino, Franco & Teles Morais — *The Costs of Building Walls: Immigration and the Fiscal Burden of Aging in Europe* | May 2026 | 75 |
| 2 | `2026-09-17_demographic-cliff-higher-education.md` | `f249853.pdf` | Krueger, Ludwig & Popova — *The Demographic Cliff and the Market for Higher Education: Implications for Public Finance* | 9 Sep 2026 | 100 |
| 3 | `2026-09-17_baby-busts-growth-booms.md` | `f249089.pdf` | Acemoglu, Autor, Beirne & Scott — *Baby Busts and Growth Booms: Demographic Change and the Macroeconomy* | 24 Jun 2026 | 72 |
| 4 | `2026-09-17_endogenous-technical-change-demographic-transition.md` | `f249391.pdf` | Pettersson — *Endogenous Technological Change Along the Demographic Transition* | 27 May 2026 | 56 |
| 5 | `2026-09-17_aging-realignment-world-trade.md` | `f249850.pdf` | Kopecky — *Population Aging and the Realignment of World Trade* | 10 Sep 2026 | 40 |
| 6 | `2026-09-17_global-transition-demographics-ai.md` | `f249854.pdf` | Benzell, Kotlikoff & Ye — *The Global Transition: The Impact of Demographics and AI on Economic Power* | 13 Aug 2026 | 56 |
| 7 | `2026-09-17_dividend-to-drag-kotschy-bloom.md` | `kb2026wp.pdf` | Kotschy & Bloom — *Population Dynamics and Economic Growth: From Demographic Dividend to Demographic Drag?* | 31 Mar 2026 | 66 |
| 8 | `2026-09-17_spatial-consequences-depopulation.md` | `Depopulation.pdf` | de Silva & Paron — *Making Room on an Empty Planet: The Spatial Consequences of Depopulation* | 21 Aug 2026 | 126 |
| 9 | `2026-09-17_ghost-town-geography-depopulation-aging.md` | `TheGeographyofAgingandDepopulation_latest.pdf` | Giannone, Miyauchi, Paixão, Pang & Suzuki — *Living in a Ghost Town: The Geography of Depopulation and Aging* | Sep 2026 | 71 |

## Verification required

**Rows 4 and 5 carry no page count because those two sources were never opened from disk during
the drafting session — they were delivered in context, so their file-level metadata is
unverified.**

Claude Code: run `pdfinfo` across all nine, complete rows 4 and 5, and confirm the seven verified
page counts against the file. Report any mismatch rather than correcting it — a mismatch means
the file in `sources/` is not the file the note was drafted from, which is a provenance failure,
not a typo.

## Acquisition context

Items 1–6 were obtained in connection with the NBER virtual conference on the macroeconomic
effects of population aging (Auclert et al.), September 2026.

Items 7–9 are related material of different provenance: Kotschy & Bloom predates the conference
and supersedes an earlier working paper; de Silva & Paron and Giannone et al. are spatial-economics
papers acquired alongside. Their conference status is **not established** and should not be
asserted in any citation drawn from this batch.

## Not in this manifest

`synthesis/2026-09-17_nber-aging-conference-synthesis.md` is a briefing note, not a monitoring
note, and has no single source. It is held pending briefing-note schema resolution in the
Architecture workspace and is deliberately kept outside `notes/` so that a directory glob cannot
sweep it into the monitoring batch.
