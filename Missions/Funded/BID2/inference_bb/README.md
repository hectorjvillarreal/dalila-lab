# BID2 inference: Bayesian bootstrap of the calibration targets

Started 2026-11-08 from the assessment of Andrews, Moon and Shapiro (2026), "In Praise of the
Bayesian Bootstrap", *JEP* 40(4), 137–158 (`Research/andrews-et-al-2026-in-praise-of-the-bayesian-bootstrap.pdf`).
Target: the inference gap in `draft_november/Draft-November.tex`, Appendix "Estimation", which
reports no standard errors on the nine estimated parameters and mixes cluster-robust, delta-method
and clustered-bootstrap standard errors across the ten targets. Intended for the journal version,
not the IDB working-paper edition.

What this folder does: recompute the nine survey targets on Dalila from the public microdata, with
one procedure for all of them (Exp(1) weight per primary sampling unit, multiplied into the
expansion factor), and deliver (i) the joint posterior sample of the targets, (ii) a credible
check of the model moments against it, (iii) the comparison with the normal approximation the
draft's standard errors imply. What it does not do: re-estimate the nine parameters. That requires
the estimation code, which lives with Diego; `REPORT_20261108.md` gives the specification for that step.

## Run

```bash
cd ~/Dalila/Missions/Funded/BID2/inference_bb
PY=~/miniforge3/envs/dalila/bin/python
$PY -I src/enigh_moments_bb.py        # ~10 min; outputs/enigh_moments_bb.{json,draws.csv}
$PY -I src/enasem_survival_bb.py      # seconds; outputs/enasem_survival_bb.{json,draws.csv}
$PY -I src/make_figure.py             # figures/bb_targets.{png,pdf}
```

Data: `../motivation/data/enigh/{2016,2018}/` (2016 downloaded 2026-11-08 from the INEGI direct
pattern `contenidos/programas/enigh/nc/2016/microdatos/enigh2016_ns_<table>_csv.zip`, tables
concentradohogar, poblacion, ingresos, hogares; zip signatures verified) and
`../motivation/data/enasem/{2018,2021}/` (already on disk since 2026-08-08). Raw data are untracked.

## Layout

| Path | Contents |
|---|---|
| `src/bb.py` | Shared helpers: cluster weights, summary with split-half check, p-p distance to the normal, two-sided tail probability, joint Mahalanobis check |
| `src/enigh_moments_bb.py` | Seven ENIGH targets, pooled 2016+2018, PSU = wave × upm. Definitions in its `DEFINITIONS` dict; draft values in `DRAFT` |
| `src/enasem_survival_bb.py` | Two survival targets on the 2018→2021 wave pair (the draft uses 2012–2021 harmonized waves); a width demonstration, not a reproduction |
| `src/make_figure.py` | Nine-panel figure |
| `outputs/` | JSON summaries, replicate draws (CSV), run log |
| `figures/` | `bb_targets.png/.pdf` |
| `REPORT_20261108.md` | Results, reading, proposal for the appendix, specification for the parameter step |
| `appendix_inference_proposal.tex` | Drop-in text for Appendix "Estimation" (not spliced into the draft) |

## Reproduction of the draft's point targets

Where the draft's Measurement paragraph is silent, the definition was chosen to reproduce its point
target and is recorded in `DEFINITIONS`. The three spending shares reproduce exactly; the pooled
elasticity, within-age elasticity and log-slope reproduce to the second decimal; the skill premium
does not (0.69 vs 0.66 under "upper secondary or more"; 0.80 under "university or more"), so its
education split and earnings definition remain to be confirmed with Diego. See the report.
