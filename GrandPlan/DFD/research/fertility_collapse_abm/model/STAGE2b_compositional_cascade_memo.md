---
type: read_memo
stage: 2b
project_scope: [DFD]
workspace: "DFD — Demographic Collapse Paper (Anne-led)"
title: "Stage 2b — the read: compositional-vs-cascade discrimination"
target: Anne (population economics)
date_added: 2026-06-20
added_by: Claude
endorsed_by:                       # pending Anne — §7 gate criterion 5
depends_on:
  - "STAGE2b_compositional_cascade_instruction.md (§5 amended per Anne 2026-06-20)"
  - "STAGE2b_Anne_endorsement.md (conditions 1-6)"
status: "Calibrated run complete (Anne-adjudicated methodology). §5 verdict applied below. Pending Anne's endorsement of this read."
---

# Stage 2b — The Read

**Numbers below are from the calibrated run on the Anne-adjudicated methodology**
(birth-year-bin pseudo-cohorts; `peer_younger` primary + `peer_older` clean +
`pop2039` robustness + `own_lag` comparator; period windows 2015–2024 & 2018–2024;
entry cohorts birth ≥ 1990). They supersede the non-authoritative smoke-test figures.
This read applies the §5 rule mechanically; **Anne's endorsement is still the gate.**

## Headline

**No within-cohort reflexive cascade is detected. (B) is NOT warranted on this evidence.**
The marriage collapse is real but its within-cohort dynamics are **stabilizing, not
self-reinforcing** — consistent with Anne's standing read.

## The decisive quantity (Task C state-dependence)

β is the coefficient on the lagged reference not-married share; **amplifying cascade
requires β < 0 and significant**. The full β matrix (lag 1, where signal concentrates):

| spec (role) | β CRI | β COL | amplifying? |
|---|---|---|---|
| `peer_younger` (primary) | +0.17 | +1.33 | no (β>0) |
| `peer_older` (clean) | +0.16 | +0.61 | no (β>0) |
| `pop2039` (robustness) | +0.29 | +0.97 | no (β>0) |
| `own_lag` (comparator) | +0.36 | +0.98 | no (β>0) |

**β > 0 everywhere, both countries, every spec** (lag-2 estimates collapse to ≈0).
`any amplifying = False`. The sign is the opposite of the cascade signature: within-cohort
marriage decline is *smaller*, not larger, where the reference not-married share is already
high. The H_cascade row of §5 (requires amplifying β under primary + ≥1 clean spec in **both**
countries) is **not satisfied**.

## §5 rule applied, by country

| | Task B localization (married) | Period effect (F-test) | β | §5 reading |
|---|---|---|---|---|
| **CRI** | leans period (RMS 0.031 vs 0.022) | **not present** (p=0.18) | not amplifying | **H_cohort-leaning** — weak/insignificant period, no reflexivity. |
| **COL** | leans cohort (RMS 0.007 vs 0.014) | **present** (p≈3e-6) | not amplifying | **H_shock + cohort component** — a real period effect, but non-reflexive; plus a cohort step-down. |

Neither country reaches H_cascade. COL carries a genuine period component (so the collapse is
not purely generational there), but because β is non-amplifying, that period component is an
**exogenous-shock** signature, not endogenous feedback — the §5 distinction this stage exists to
draw. CRI's period effect is not even statistically present, leaving a cohort-replacement reading.

**Implication for (B):** deferred / not warranted. Per §5, reflexive self-reinforcement is
justified only by amplifying state-dependence, which is absent. Do not stage (B). If the model
needs a period driver (COL), it should be **exogenous**, not endogenous-reflexive.

## Limitations (§8) and one correction

- **B7 correction — both βs are ecological.** Implementation surfaced that Task C's LHS is a
  within-pseudo-cohort *cell* composition change, so on repeated cross-sections **neither**
  country's β is individual-level — no individual union transitions are observed in either (the
  pseudo-panel limitation). The CR/COL asymmetry is in how the *cells* are built (CR = REDATAM
  pre-tabulated aggregates; COL = cells from DANE microdata), not the estimator level. This
  **deviates from Anne's B7 wording** ("COL β is individual-level") and is logged here for Anne's
  confirmation rather than silently absorbed. It does not change the verdict (sign-based).
- **APC linear identification.** Only curvature is identified; the read rests on where the
  *acceleration* localizes, not on level trends. Sawtooth cannot enter curvature (taken net of
  age-band FE and within fixed bands — Lexis artifact filed).
- **20–39 floor (B6).** Excludes the 15–19 entry margin (the cascade vanguard) and leaves
  `peer_younger` undefined for the youngest band. A cascade that ignites at 15–19 would be
  under-observed here — the one caveat that could mask a true cascade. Flag, do not dismiss.
- **External-validity ceiling.** Both are high-cohabitation regimes; the marriage-dominant
  Southern Cone (ARG/CHL) is out of scope for 2b. The non-cascade read may not generalize.
- **Tempo, residual.** First-union timing shifts can still masquerade as composition change in a
  pseudo-panel. Flagged, not resolved.

## Verification status (conditions 1–6)

1. `peer_older` + full β matrix + A1 contradiction fixed — ✅
2. Birth-year-bin pseudo-cohorts; curvature within fixed bands; fig-1 segmented — ✅
3. §5/§10 amended; 2015–24 & 2018–24 windows; birth ≥ 1990 entry cut — ✅
4. B6 reproduction diff vs Stage 1.5 — ✅ PASS (married/cohab exact; union_total within rounding)
5. `assert_no_tfr` log filed — ✅ 25 PASS / 0 VIOLATION
6. B7 tag (with correction above); calibrated run; §5 verdict — ✅ (this memo)

**Gate:** Anne endorses this read → Debb writes `endorsed_by: Anne` in the instruction. The
present verdict unblocks Stage 3 scaling but **closes** (B) reflexive feedback unless the
15–19-margin caveat or Southern Cone identification overturns it.

*Stage 2b read. Claude, 2026-06-20, on the Anne-adjudicated methodology. Pending Anne's endorsement.*
