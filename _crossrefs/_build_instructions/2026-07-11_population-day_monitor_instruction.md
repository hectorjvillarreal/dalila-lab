---
type: skill_invocation
project_scope: [DFD, BDH, Aurora]
workspace: "demographics corpus (cross-project) — routed from the collapse-paper workspace"
title: "Population Day 2026 — demographics-monitor note on the UNFPA Demographic Futures Survey"
target: Claude Code (Dalila)
date_added: 2026-07-11
added_by: Debb
endorsed_by:                      # note is pending-anne on production
skill: dfd-demographics-monitor
status: "ACTIONABLE NOW. Live test of the skill's revision-vs-report discriminator."
---

# Population Day 2026 — Demographics-Monitor Note
# Target: Claude Code (Dalila) · Skill: dfd-demographics-monitor

## 0. What this is

World Population Day 2026. A UN demographic release landed today — run the demographics-monitor
skill and produce a monitoring note. This is the **live test** of the skill's discriminator that we
flagged: distinguish a full WPP revision (Revision Transition Protocol → re-baseline) from a
report/survey (normal monitoring note). Today is the second kind. Resolve it correctly.

## 1. The discriminator ruling (apply, do not re-derive)

**REPORT, not REVISION.** → Monitoring note, promotion **pending-anne**, routed to the shared
demographics corpus. **Do NOT** fire the Revision Transition Protocol. **Do NOT** re-baseline.
**Do NOT** touch OLG / IM-6 calibration. The current UN projection reference remains **WPP 2024**;
nothing today supersedes it. If the skill would have tried to re-baseline off a survey, that is the
bug — stop and flag it.

## 2. The source (verified 2026-07-11; cross-check on fetch)

- **UNFPA Demographic Futures Survey 2026**, report **"Lives, Choices and Futures: What young
  people want and what shapes their decisions about relationships and parenthood."**
- Scope: **108,000+ internet-connected young adults aged 18–39 across 73 countries**; partnership,
  reproductive, and life aspirations, plus the barriers and enablers shaping them.
- Published **7 July 2026**, ahead of World Population Day (11 July). Theme: "Realizing the hopes
  and aspirations of young people – today and for the future." Primary: unfpa.org.
- **Accuracy caveat — do NOT conflate with the 2025 report.** The widely-quoted "14-country survey,
  18% expect fewer/more children than they want; barriers cost / job insecurity / housing" figure is
  from the **2025** State of World Population report, NOT this one. This release is the 73-country
  Demographic Futures Survey. Cite the 2026 report's own figures on fetch; do not import 2025's.

## 3. Produce the note

Run `dfd-demographics-monitor`. Fetch the primary UNFPA source; extract the 2026 report's own
headline figures (survey scope, partnership/aspiration findings, barriers/enablers, any country
breakdowns). Output a PROTO-RAG-001 monitoring note to
`_crossrefs/corpus/demographics/_pending/`, `promotion_status: pending-anne`, `added_by: Claude`,
`endorsed_by:` blank.

## 4. DFD relevance flags (for the note's routing section)

- **Coupling / partnership aspirations = the collapse mechanism.** Unlike a TFR release, this survey
  is about *partnership formation and reproductive aspirations* — the extensive margin and union
  composition that 2b/2c and the SDT frame are built on. Genuine framing-layer relevance.
- **Framing-layer only — does NOT touch the collapse-paper verdict.** The 2b/2c econometrics are
  behind the identification wall; a UNFPA survey changes nothing there. Flag as framing input, not
  evidence bearing on the cascade/cohort verdict.
- **Adjudication for Anne (do not resolve in the note).** UNFPA frames the gap as *constraints on
  reproductive agency* (people cannot have the children they want); our SDT framing centers
  *value/behavior change* (channel-assisted compression). Complementary or competing is Anne's call
  — flag the tension, don't settle it.
- **Check for LAC country breakdowns.** If CR / COL / CHL / MEX partnership-aspiration data are in
  the survey, flag them as a candidate input to the coupling story (and note whether microdata are
  released) — pending-anne.

## 5. What NOT to do

- No re-baseline; no Revision Transition Protocol; no OLG/IM-6 calibration change.
- Do not import the 2025 14-country / 18% figure as if it were the 2026 release.
- Do not claim relevance to the collapse-paper verdict — framing layer only.

## 6. Deliverable + gate

Monitoring note filed to `_crossrefs/corpus/demographics/_pending/`, pending-anne. Anne promotes
(or not) and adjudicates the agency-vs-SDT framing tension. Log the build under PROTO-RAG-001;
cross-reference from the demographics corpus index.

*Debb, 2026-07-11. Live discriminator test — report, not revision. For Claude Code.*
