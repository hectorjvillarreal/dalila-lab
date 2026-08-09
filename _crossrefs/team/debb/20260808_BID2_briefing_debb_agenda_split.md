# Briefing for Debb — two tracks came out of the motivation build; keep them apart

**From:** Héctor (analysis run on Dalila, 2026-08-08)
**Mission:** BID2 · health-refocused paper
**The problem this note solves:** today's build produced what the paper needs —
and, along the way, a set of findings that amount to a research agenda in their
own right. Those are different objects with different clocks. Tomorrow the
team thinks about BID2 and the **September 2 objective**; nothing from the
second track should leak into that. But the second track must not evaporate
either. Architecting that separation — parked now, resurfaced at the right
time — is your domain, so this note hands it to you explicitly.

---

## Track 1 — the paper: what tomorrow is about

The motivation section's empirical base is **done and closed** for drafting
purposes: three facts established (age gradient, unequal capacity, curative
dominance), the unmet-need corollary on four independent evidence lines,
twelve figures with per-figure value tables, verification against GHED,
everything committed on `p3-correcciones-tex`. Entry point:
`Missions/Funded/BID2/motivation/output/READTHIS.md`; coordination view (open
loops, dependencies): Fina's briefing in `_crossrefs/team/fina/`.

What Track 1 needs between now and September 2 is **drafting and scope
discipline**, not more analysis:

- Write the motivation section quoting `output/NUMBERS.md`, under the three
  standing rules (ENIGH shapes-not-levels; preventive share as the 2%–46%
  bracket; ages 5–14 Tier-3 cell embargoed).
- Close the three open loops already assigned: Judy (frailty confirmation),
  Beth (classification ratification; placement of the 2020 finding as
  footnote vs subsection), Anne (September WPP swap → `scripts/10` rerun).
- The only analysis permitted on this track is what a coauthor's answer
  triggers (each is a scripted, minutes-scale rerun).

**The boundary rule I'm asking you to enforce editorially:** the motivation
section *uses* today's findings only as fenced in READTHIS. If a draft
paragraph starts arguing any Track 2 item on its merits, it has crossed the
line — cut it and point the text back to the fenced version.

## Track 2 — the research agenda that fell out of the build

Six findings, each larger than the paper needs. For each: what it is, why it
deserves its own life, and roughly what going deeper costs. None of them is
urgent; all of them are perishable if left unfiled.

1. **The 2020 provision-shock episode.** Real OOP rose in every decile
   (+76% poorest, +29% richest), food placebo flat, never reversed; the
   margin was participation — zeros fell 13–15 pp everywhere. A public
   in-kind system failed and conscripted poor households into out-of-pocket
   payment, observably, in a two-wave window. Deeper = event-study against an
   external utilization series (IMSS/SSA administrative), heterogeneity by
   insurance, welfare accounting. That is a standalone paper, plausibly the
   strongest of the six.
2. **Zeros as access-plus-unmet-need.** The 2020 collapse of the zeros
   validates a general measurement claim: household-survey zeros in health
   are not corner solutions, they are the public system plus rationing.
   Deeper = a measurement note with direct implications for catastrophic-
   spending and poverty-of-health-access metrics used by IDB/WHO.
3. **ENIGH captures 22–34% of GHED OOP.** Everyone "knows" surveys
   undercapture; a documented, wave-by-wave reconciliation for Mexico with
   the capture ratio jumping at 2020 does not exist in the literature we
   know of. Deeper = survey-vs-NHA reconciliation (item coverage, recall
   design, top-tail truncation), joint with the ENASEM 3–4× gap.
4. **The middle-tercile mortality anomaly.** Post-decline mortality is
   highest in wealth tercile 2 (20.1%), not tercile 1 — assets to spend
   down, no insurance depth? Wide CIs; could be noise. Deeper = only after
   Judy confirms the index; then a partial-protection hypothesis test. Park
   with an explicit dependency on her answer.
5. **Survey instruments encode the curative bias.** ENSANUT 2018 literally
   could not record a preventive motive; 2024 redefined "need" to include
   prevention. The measurement system's own evolution mirrors the paper's
   thesis. Deeper = a short methods/commentary piece; low cost, high charm;
   also a warning for anyone doing 2018→2024 utilization comparisons.
6. **The frailty reconstruction outperforms the published index**
   (pseudo-R² 0.167 vs 0.142) — backwards for a reconstruction, which makes
   sample definition (which deaths count, who is at risk) the substantive
   question. Deeper = a methodological note with Judy once her code surfaces;
   gated on the same answer as item 4.

Cross-cutting asset rather than finding: the **ENSANUT age-sex utilization
schedule** (`output/tables/ensanut_util_weights_2024.csv`) — a design-based,
NTA-style input relevant to DFD; candidate for the demographics corpus
pending Anne's endorsement.

## What I am asking you to do

1. **File Track 2 so it resurfaces, using existing artifact types** — this is
   your call, but my reading of the infrastructure: items 1–3 and 5 fit the
   watch-item convention (each with a one-line trigger for revisiting); items
   4 and 6 are dependency-gated (Judy's answer) and belong wherever you park
   things that wake on an event rather than a date; the utilization schedule
   goes through the demographics-corpus `_pending/` endorsement path to Anne.
   Per PROTO-RAG-001, conform to what exists — invent no new artifact type
   for this.
2. **Set the resurfacing clock.** Suggested: nothing before September 2;
   first review of the parked agenda in the week after, when the deliverable
   pressure is off — with items 4 and 6 waking early only if Judy replies.
3. **Hold the boundary in editorial passes** (the rule in Track 1 above).

The findings are good enough that the temptation tomorrow will be to think
about them instead of the paper. The point of this note is that we do not
have to choose — we have to sequence. Park them well, and in time we come
back and go deeper.

## Pointers

Canonical work: `Missions/Funded/BID2/motivation/` (branch
`p3-correcciones-tex`) — `output/READTHIS.md` first. Briefings:
`_crossrefs/team/{anne,beth,fina,judy}/`. Registered in
`_crossrefs/mission-project-map.md` (2026-08-08 entry). Numbers for anything
quoted here: `output/NUMBERS.md`, table sources in `output/tables/`.
