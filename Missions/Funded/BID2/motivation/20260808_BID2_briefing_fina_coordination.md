# Briefing for Fina — coordination view of the motivation build and the three coauthor briefings

**From:** Héctor (analysis run on Dalila, 2026-08-08)
**Mission:** BID2 · health-refocused paper, motivation section
**Purpose:** the build is done and three coauthor briefings went out the same
day. This note is the coherence layer: who holds which open loop, what blocks
what, where the cross-project hooks are, and the consistency rules the draft
must not violate.

---

## State of play in one paragraph

The motivation section's empirical base exists, runs end to end
(`motivation/scripts/00–11`, R 4.4.3 in conda env `renv`), and is committed on
`p3-correcciones-tex`: 12 figures, per-figure value tables, `NUMBERS.md`,
`VERIFICATION.md`, `provenance.md`, `READTHIS.md`. All three motivating facts
are supported with stated qualifications; unmet need is established on four
independent evidence lines (three planned, plus the 2020 pandemic surge found
along the way, fig 12). Nothing blocks drafting the section now — every
unresolved item is fenced with an explicit flag in the outputs rather than
sitting as silent risk.

## Who holds what — the three briefings and their open loops

| Briefing | Holder | Open loop | What resolution triggers |
|---|---|---|---|
| `20260808_BID2_briefing_judy_frailty.md` | **Judy** | Confirm the 21-item reconstruction (5 numbered questions), or send her construction script | Provisional flags come off fig 10, READTHIS, provenance; if her code differs, `scripts/05` is a one-file swap and 06/figures rerun in minutes. **Cheapest unlock in the whole system — one email.** |
| `20260808_BID2_briefing_beth_motivation.md` | **Beth** | (a) Ratify or override the curative/preventive judgment calls (each code has a rationale in the classification CSV); (b) decide the 2020 natural experiment's place in the draft (footnote vs subsection) | (a) Reclassification = one-line edits in `scripts/07`, fig 7 + sensitivity regenerate; (b) if promoted, the stated next step is differencing against an external utilization series — small, but it is new scope and should be a conscious add. |
| `20260808_BID2_briefing_anne_age_profiles.md` | **Anne** | None urgent — the composition experiment (×1.47 per-adult OOP) uses her primitives verbatim and reproduces her 0.744 anchor at 0.747 | Her already-scheduled September WPP single-age swap automatically converts my stationary **upper bound** into the transitional 2050 number: `scripts/10` becomes load-real-pyramid. No new ask; just link the two deliverables when September planning happens. |

Sequencing recommendation: **Judy first** (one email, removes the only
"provisional" flag in the deliverable), Beth's classification pass second
(changes a headline figure), Anne rides the existing September cadence.

## Dependency and consistency map

- **Nothing gates the draft.** All flags are self-contained; the section can
  be written today quoting `NUMBERS.md`.
- **Three rules the draft must not violate**, wherever the text is written:
  1. ENIGH gives **shapes and gradients, never levels** (22–34% of GHED OOP;
     ~3–4× below ENASEM observed). Any peso level quoted as a total is wrong.
  2. The preventive share is a **bracket (2%–46%)**, not a number; the
     licensed phrase is "majority curative."
  3. The **ages 5–14 Tier-3 cell is embargoed** (method-fragile), and Tier-3
     profiles are always "estimated," never "observed."
- **Fig 10 carries Judy's provisional flag** until she confirms; if the draft
  goes out before that, the flag goes with it (it is already in the figure
  note, so default behavior is safe).
- **Internal consistency check that should stay true after any rerun:** the
  composition experiment's implied 65+/(20–64) = 0.747 must keep matching
  Anne's stationary dependency anchor (0.744). If a rerun breaks this, the
  demographic inputs have diverged — stop and reconcile.

## Cross-project hooks (things that outlive BID2)

- **ENSANUT age-sex utilization schedule**
  (`output/tables/ensanut_util_weights_2024.csv`): a design-based NTA-style
  health-utilization profile — relevant to DFD's NTA methodology line and a
  candidate for the demographics corpus if Anne endorses it as a reusable
  input rather than a BID2-local artifact.
- **INEGI/ENSANUT acquisition mechanics** (soft-404s, JSON-LD `contentUrl`,
  ENSANUT base64-`ArchId` POST, GHED/World Bank APIs) are in team memory —
  directly reusable for RF corpus downloads and any future INEGI pull.
- **m_j is now empirical.** The estimated age-sex profile is the measured
  counterpart of the health block in `ge_model_gender.jl`; when the model's
  m_j is next calibrated, it should cite these profiles (shapes) rather than
  stylized values — that closes a loop between the motivation section and
  the quantitative model that reviewers will check.
- **The 2020 surge** may interest DFD beyond BID2: a provision shock that
  moved OOP participation economy-wide is a fiscal-demographic event in RF's
  narrative window (2000–2025) and could be worth a fiscal-events entry there.

## Cadence flags

- The three coauthor briefings went out dated the same day; replies will
  arrive on different clocks. The only time-sensitive one is Judy's (it holds
  a flag in a deliverable figure); a nudge is warranted if nothing arrives
  within two weeks.
- September deliverable planning should explicitly list the `scripts/10`
  rerun under Anne's WPP swap, or it will be forgotten — it is two lines in
  a plan now versus an inconsistency discovered in a draft later.
- If Beth promotes the 2020 finding, scope it deliberately (external
  utilization series check) rather than letting it grow inside the
  motivation section.

## Pointers

Base: `~/Dalila/Missions/Funded/BID2/motivation/` (branch `p3-correcciones-tex`).
Read order for anyone new: `output/READTHIS.md` → the relevant coauthor
briefing → `provenance.md` for any specific decision. Every number the draft
cites comes from `output/NUMBERS.md`, never from a figure.
