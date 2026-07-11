---
type: working_note
tier: consult_request
project_scope: [DFD]
authors: [Claude Code (Stage 1.5 execution)]
addressed_to: Anne (population economics, DFD Core Team)
year: 2026
title: "Stage 1.5 — open questions for Anne: the map-side result, the marriage margin, and the Argentina/Chile call"
venue: "DFD parallel research, internal — fertility-collapse ABM"
date_added: 2026-06-18
added_by: ClaudeCode
endorsed_by:
build_instruction: "STAGE1_5_addendumA_colombia_geih.md"
---

# Stage 1.5 — Open questions for Anne

**From:** Claude Code (Stage 1.5 execution)
**To:** Anne (population economics)
**Date:** 2026-06-18
**Re:** what the Colombia coupling extraction settled, and the four places where the
next move is *your* call, not mine.

---

## Why this note

The Colombia GEIH coupling series is built (2007–2024, observed against DANE EEVV TFR),
and with it the Stage 1.5 gate is now **decidable**. Mechanically the result is clean.
But "decidable" is not the same as "interpreted," and several of the choices that flow
from it are demographic judgments I should not make alone. This note states the result
plainly, then asks you four specific questions. **I have deliberately not pre-decided
them** — where I lean a particular way I say so and say why, but each needs your read,
including the freedom to tell me the framing is wrong.

Artifacts to look at first: `COL_coupling_vs_tfr.png` (the one-glance version),
`COL_coupling_annual.csv` (+ sidecar `.md`), `COL_identification.csv`, and the updated
`STAGE1_5_identification_memo.md` §"Colombia".

---

## What the data say (neutral statement)

- **Total co-residential union (women 20–39)** sits on a flat plateau of **~59–60% for
  twelve years (2008–2020)**, then drifts down to **54.0% by 2024** — a ~6 pt, ~11% fall
  concentrated in 2021–2024.
- **Marriage** falls the *entire time*: **20.7% (2008) → 11.9% (2024)**, roughly halved,
  with **cohabitation rising underneath** so the total barely moves until 2021.
- **Observed TFR** is flat at **1.7 (2015–2018)**, then collapses to **1.1 (2024)**, −35%.
- **Check A is clean:** the union variable (P6070) is coded identically across the 2021–22
  "Marco 2018" redesign, so none of this is a recode artifact.

So a *small, smooth* change in total coupling sits against a *large* fertility collapse.
Mechanically that reads as **map-side** nonlinearity (the action is in the coupling→fertility
map, not in partnership formation) and **no coupling→TFR lead** (if anything coupling lags).
Colombia agrees with Costa Rica; Mexico — the slow-decline comparator — is the lone
coupling-side case.

---

## Question 1 — Is "map-side" the right *demographic* reading, or an aggregate artifact?

The mechanical verdict is map-side. But "the coupling→fertility map became more negative"
is a black box until you say what is inside it. Plausible contents, all demographic:
- within-union **postponement** (tempo) — couples form but defer births;
- **parity-specific** collapse (first births delayed, higher parities forgone);
- a **contraceptive / intention** shift independent of union status;
- or total union is simply the **wrong aggregate** and the real coupling signal is hiding
  in the marriage margin (see Q2).

**What I need from you:** does map-side survive contact with what you know about Colombian
fertility 2015–2024? Is there a parity or ASFR-shape fact that tells us *which* of the above
the "map" actually is? If you think the map-side read is an artifact of using total union,
say so — that redirects the whole Stage 2 spec.

## Question 2 — The marriage margin: is marriage-weighted union the state variable?

This was *your* original caution — that modern LAC cohabitation may be an increasingly low-
or deferred-fertility state — and Colombia is the sharp test of it: total union is stable
while marriage halves. If marriage and cohabitation differ enough in fertility intensity,
the behaviorally-relevant coupling variable is **marriage-weighted**, not total union, and
the "map-side / no-lead" verdict on *total* union might flip on the *marriage* series.

**What I need from you:**
1. Should Stage 2's primary coupling state variable be marriage-weighted union (or a
   fertility-intensity-weighted blend), and if a blend, how would you set the weights?
2. Can you pin an LAC (ideally Colombian) **marriage-vs-cohabitation fertility-intensity
   differential** — even a rough ASFR or parity ratio with a source? That number is what
   turns "marriage-weighted" from a hand-wave into a calibrated quantity. (This likely
   belongs in the demographics corpus as a scenario anchor.)
3. I can re-run the full Q1–Q4 identification on the *marriage* series in an afternoon if
   you want to see whether a lead reappears there. Worth doing?

## Question 3 — Is the "no lead / coupling lags" finding robust, or a dating artifact?

The lead test is the mechanism's core causal claim, and Colombia is the only place we can
run it against an *observed* TFR. The differenced correlation's best alignment is a **lag**
(coupling follows TFR). But I distrust the precise lag: the TFR is a chart-label rounded to
1 decimal over only 9 difference-points, and the result hinges on whether Colombia's fertility
turn is dated to the *gradual* 2019–2020 slide (1.7→1.5) or the *steep* 2021–2022 break.

**What I need from you:** as the demographer, **how do you date the Colombian fertility turn?**
If the real turn is 2021–22 (steep part), total coupling's 2021 break is roughly contemporaneous,
not lagging, and the verdict softens. Would you trust a parity- or ASFR-based alignment over the
period-TFR one? Is the "no clean lead" conclusion safe to put in front of a referee, or do we
hedge it harder?

## Question 4 — Argentina and Chile: motivation only, or worth the acquisition cost?

The paper motivates with four collapse countries (CRI, COL, ARG, CHL); we identify on two
(CRI, COL), both of which are **high-cohabitation regimes**. ARG and CHL have no accessible
annual coupling microdata (ARG's public EPH stops 2014 and is urban-only; CHL's CASEN is
periodic to 2011), so they are currently out of the identification panel.

My instinct — but this is squarely your domain — is that **Argentina is more than enrichment**:
the Southern Cone is a *different nuptiality regime*, so ARG would test whether the map-side /
marriage-margin story generalizes beyond high-cohabitation settings, and it already has a
reconstructed annual TFR, so even a couple of coupling endpoints could make it a third
lead-test case. Chile (periodic CASEN) is probably endpoints-only regardless.

**What I need from you:**
1. Is the CRI+COL high-cohabitation commonality a **real external-validity threat**, or are
   these regimes representative enough of the LAC collapse that two cases suffice?
2. Is Argentina worth a Stage 2 acquisition push (and do you know an annual or near-annual
   ARG nuptiality source I'm missing — census 2010/2022, EPH microdata, a vital-stats union
   field)?
3. How should ARG/CHL be **framed in the paper** — purely in the motivating stylized fact,
   or held open as a stated panel limitation with an enrichment plan?

---

## What happens with your answers

- Q1–Q2 set the **Stage 2 state variable** (total vs marriage-weighted) and the substantive
  content of the "map" — i.e., what the ABM's fertility-response function actually represents.
- Q3 sets **how hard we hedge the lead claim** in the writeup.
- Q4 sets **scope** (two-country mechanism vs broader panel) — a call you, Héctor, and Fina
  share, but it starts from your demographic read.

No Stage 2 specification work has begun; this is still the gate. Nina's nesting-model spec is
ready to freeze the moment Q1–Q2 are settled.

*Stage 1.5 of 4. Consult request, 2026-06-18. Companion to STAGE1_5_identification_memo.md
(v2.0) and STAGE1_5_addendumA_colombia_geih.md.*
