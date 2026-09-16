# MANIFEST — fig07 composition replication package

Packaged 2026-08-30 from the BID2 motivation build repository at commit
`cd8ed6c6e6aa9f77ff84cb65d90622b532dd4d99`, branch `p3-correcciones-tex`. All
three data files were unmodified in the working tree at packaging time and were
copied byte-for-byte (SHA-256 verified against the originals).

This manifest covers the package only. It does not cover `output/`, which is
produced by `run_all.sh` and not shipped by hand, nor this manifest itself.
**The raw survey microdata (ENIGH, ENSANUT, ENASEM) is not included** in any
form; only derived aggregates are distributed.

| path | SHA-256 | bytes | what it is | origin (script → repository path) |
|---|---|---|---|---|
| `README.md` | `d1af50d375f38245f2aacf7b12afd44393df73cb4fb4167793ec5e9219ff90cb` | 6877 | package documentation | written for this package |
| `run_all.sh` | `099c1faed9c3ff2415614ba86c4355f6efd5c5f5a69c245637225286ccdbe47e` | 795 | one-command entry point | written for this package |
| `code/make_fig07_composition.R` | `1b1b023552a8f42c65105e94e24b7f88911b150f29af42eff4581a02d7a70688` | 3062 | figure generator | figure-7 block of `scripts/08_figures.R`, verbatim, paths made package-relative |
| `data/fig7_composition_by_decile.csv` | `f1fe183ac6f2be36833e78e04400be8b6cbe92d7ee3f046a1c4de827ce27645b` | 6178 | decile × class × wave composition aggregate | `scripts/07_taskB_classification.R` → `output/tables/fig7_composition_by_decile.csv` |
| `data/curative_preventive_classification.csv` | `694cc5cfb75fd253aaf82ff3c2f167c9f346dae2d4dc90684b5fbceeaa42a2d0` | 19292 | item-level rubro classification | `scripts/07_taskB_classification.R` → `output/tables/curative_preventive_classification.csv` |
| `data/fig7_ambiguous_sensitivity.csv` | `6a8b64d59fefd7ad3e9aced09a8a6024e67a83a4b7a3d532c45ac4f8c5ea22bc` | 778 | national shares incl. two-way ambiguous reassignment; carries the 2.0 / 53.6 / 44.5 headline (2024 row) | `scripts/07_taskB_classification.R` → `output/tables/fig7_ambiguous_sensitivity.csv` |
| `environment/environment.yml` | `f311c6c6b0dd3719bc1dec90440fcdd18824db7d1889629ac9f148d5748af88b` | 5015 | pinned conda environment (R 4.4.3, conda-forge) | `conda env export -n renv` at packaging time |
| `environment/R_sessioninfo.txt` | `8b83293b6344bb305c57c8f1d325c23989359bcb37ae51d69e2b0a9cb24f4677` | 1288 | exact R session used for verification | `sessionInfo()` in the `renv` environment at packaging time |
