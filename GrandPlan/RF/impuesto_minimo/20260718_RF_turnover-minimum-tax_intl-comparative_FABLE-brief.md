---
title: "International comparative — turnover-based corporate minimum taxes"
task_type: research_brief / build_instruction
project: RF (Reforma Fiscal) — 2027 economic-package adjustment track
added_by: Cath
endorsed_by:            # pending Héctor
prepared_for: Claude Code (Fable 5), web-research enabled
date: 2026-07-18
status: draft for execution
provenance: Frames the instrument discussed in the RF thread — a creditable corporate
  minimum tax on gross sales, max(2% turnover, corporate income tax). Retain under
  _crossrefs/_build_instructions/ per build-instruction convention.
---

# Research task: how other countries do a turnover-based corporate minimum tax

## 1. Purpose

We are evaluating a **corporate minimum tax computed on gross sales (turnover)** as a
candidate instrument for Mexico's 2027 economic package. The motivation is anti-avoidance:
firms that report perpetual fiscal losses through inflated/abusive deductions while being
economically profitable. The idea is to put a floor under corporate income tax (ISR) that
these firms cannot erode by manipulating the profit base, because turnover is highly
observable (in Mexico, via near-real-time CFDI electronic invoicing).

Your job is **not** to design the Mexican instrument. It is to find out **who else has built
something similar, what they call it, and how well it has worked** — so we do not reinvent the
wheel and can learn from real outcomes, including failures.

## 2. The exact instrument we care about (read carefully)

- **Base:** gross sales / turnover / gross revenue. *Not* profit, *not* assets, *not*
  value-added.
- **Mechanics:** liability = **max( rate × turnover , regular corporate income tax )** — the
  "pay the greater of the two" structure.
- **Creditability:** fully creditable / recoverable — turnover-based tax paid in a bad year can
  be credited against income tax in later years. (This is the feature that separates a firm
  having one bad year from a chronic loss-reporter.)
- **Illustrative parameter:** 2% of turnover, against a 30% corporate income tax rate.

**Analytical equivalence to carry through the whole task.** A rate `t` on turnover under a
"greater of" rule with corporate income tax rate `τ` is algebraically a **minimum presumptive
profit-margin floor** of `t / τ`. Our 2%/30% ≈ **6.67% margin floor**: the instrument taxes any
firm as if it earned at least 6.67% of sales as profit. **Compute this implied margin floor for
every foreign instrument you find** (their `t` ÷ their headline corporate rate) so all cases are
comparable on one metric. This is the single most decision-relevant number for us, because it
tells us which genuinely low-margin sectors each design punishes.

## 3. Classification discipline — do this FIRST for every hit

Many instruments are called "minimum tax" but sit on completely different bases. Before
recording anything, tag each finding into exactly one of these four buckets:

| Bucket | Base | Mexican analog | Is it our analog? |
|---|---|---|---|
| **A. Turnover / gross-revenue** | gross sales | (none current) | **YES — primary target** |
| **B. Assets / net worth** | balance-sheet stock | IMPAC (1989–2007) | Cousin — note but don't confuse |
| **C. Value-added / cash-flow** | receipts − purchases − investment | IETU (2008–2013) | Cousin — relevant contrast |
| **D. Profit / book-income** | accounting or taxable profit | — | **NO** — e.g. OECD Pillar Two 15%, US CAMT, most "MAT" |

**Do not return the OECD Pillar Two global minimum tax (15% on profit) as if it were
analogous.** It is bucket D. Mention it only to draw the contrast. Same for India's MAT and the
US CAMT — book-profit minimums, bucket D.

Our target is **bucket A**. Buckets B and C are useful because Mexico already tried them
(IMPAC, IETU) and we know how they ended; flag any foreign B/C case that is unusually
instructive, but keep the search centered on A.

## 4. Seed leads (starting points — verify the canonical name yourself)

These are places where a bucket-A or near-A instrument is likely to exist. Treat as leads, not
answers; the deliverable must include the **exact statutory name in the local language plus an
English gloss** for each real instrument.

- **Latin America (richest terrain):** Panama (alternative calculation on gross income),
  Guatemala, Nicaragua (definitive minimum payment on gross income), Honduras, Dominican
  Republic, Peru (a 1990s turnover-based minimum income tax was struck down — find out on what
  doctrine; note ITAN is bucket B), Argentina (presumed minimum profit — bucket B, repealed),
  Colombia, Costa Rica, Ecuador, Bolivia.
- **Europe:** France (a historical annual minimum keyed to turnover brackets — was it phased
  out, and why?), Italy (the "non-operating / shell company" presumptive regime).
- **United States (sub-national gross-receipts taxes):** Ohio, Washington State, Texas, Nevada,
  Oregon. These are gross-receipts taxes, not always structured as "greater of income tax," but
  the economics literature on them (cascading, margin distortion, pyramiding) is directly
  relevant.
- **Asia / Africa:** Pakistan (a turnover-based minimum tax that is well studied empirically —
  prioritize this), francophone Africa (a common minimum-tax-on-turnover archetype across
  several countries).

If you find bucket-A instruments **not** on this list, include them — the list is not
exhaustive.

## 5. What to extract per country (structured schema)

For each real instrument, produce a record with these fields. Mark any field you cannot verify
as `unknown` rather than guessing.

1. **Country / jurisdiction.**
2. **Statutory name** (local language) + **English gloss**.
3. **Bucket** (A/B/C/D) and one-line justification.
4. **Base definition** — precisely what counts as turnover/gross income; major exclusions or
   carve-outs.
5. **Rate(s)** — headline rate; any sectoral differentiation.
6. **Corporate income tax rate** in that country + **implied margin floor** (`rate ÷ CIT rate`,
   per §2).
7. **Interaction rule** — is it "greater of," an add-on, an advance payment? Creditable?
   Recoverable forward? For how many years?
8. **Escape / relief mechanism for genuinely low-margin firms** — e.g. a petition to opt out on
   proof of low real margin, sectoral exemptions, start-up grace periods. *(This is the fix to
   the margin-heterogeneity problem; flag it prominently wherever it exists.)*
9. **Performance evidence** — revenue yield (% of GDP or % of CIT), base-broadening (firms
   pulled into the tax net), documented distortions, sectoral incidence, pass-through to prices
   where studied.
10. **Legal challenges** — constitutional litigation and outcomes, especially on
    **confiscation / non-confiscatory / proportionality** grounds (a turnover minimum can
    exceed a low-margin firm's entire real profit — courts have reacted to exactly this).
11. **Trajectory & verdict** — in force / reformed / repealed; if repealed, the stated and the
    real (political-economy) reasons; year.
12. **Sources** — primary where possible (tax code, finance ministry, OECD/IMF/IDB/ECLAC/CIAT,
    peer-reviewed). Note conflicts between sources; state your confidence.

## 6. Analytical lens to apply (this is where the value is)

For each case and in the synthesis, keep four questions in front:

- **Margin heterogeneity.** Given the implied margin floor, which sectors does this design catch
  correctly (abusers whose real margin is well above the floor) vs. punish wrongly (thin-margin,
  high-volume honest firms — fuel retail, wholesale, distribution, supermarkets)? How did that
  country handle it?
- **Creditability vs. definitive.** Is the instrument a timing device (creditable/recoverable,
  low efficiency cost on genuinely profitable firms) or a definitive add-on tax on turnover
  (cascading properties, à la a turnover tax)? Which produced better outcomes?
- **Erosion resistance.** Mexico's IMPAC and IETU were both eroded by rate cuts, special
  regimes, and litigation until the control function collapsed. Which foreign designs resisted
  erosion, and how (broad base, uniform rate, constitutional anchoring)?
- **Constitutionality.** On what doctrine have turnover minimums survived or fallen? (Peru's
  strike-down and Mexico's SCJN upholding of a gross-income base are two poles worth mapping.)

## 7. Deliverable

A single markdown file:

- **Comparative table** — one row per instrument, columns from the §5 schema (at minimum:
  country, name, bucket, rate, implied margin floor, creditable?, escape valve?, status,
  one-line verdict).
- **Per-country notes** — the full §5 record for each bucket-A case and any especially
  instructive B/C case; keep bucket-D mentions to a short "not analogous, here's why" list.
- **Synthesis for the RF instrument** — 1–2 pages max, organized around the four questions in
  §6, ending with: which foreign design(s) are the closest working model for a Mexican
  turnover-based minimum, and which design features consistently correlate with success vs.
  failure/repeal.

Suggested landing path once reviewed: `~/Dalila/GrandPlan/RF/_crossrefs/calibration/` (or a new
`_comparative/` subfolder if Héctor prefers). Do not create a PROTO-RAG-001 corpus ficha unless
Héctor asks — this is a research note, not a formal corpus entry.

## 8. Boundaries

- **Scope is the standalone 2027-package instrument.** Do not analyze it as part of any larger
  structural reform; treat it as an autonomous, cyclical measure.
- **Stay in bucket A.** Do not drift into a Pillar Two / global-minimum-tax survey; one
  contrast paragraph is enough.
- **Do not design the Mexican parameters** (rate, carve-outs, sectoral schedule). That is a
  downstream decision. Your output is evidence, not a proposal.
- **Formal/informal margin and OLG calibration implications:** flag them in one line if a source
  raises them, but do not develop them — that is Cath's downstream work, out of scope here.
- **Sourcing hygiene:** paraphrase; cite primary and multilateral sources; never invent a name,
  rate, or attribution. If an instrument's name or status cannot be verified, say so explicitly.

---

*Prepared by Cath for the RF thread. Reference points already in hand on the Mexican side:
IMPAC (assets minimum, 1989–2007, eroded by rate cuts + special regimes + amparos) and IETU
(value-added/cash-flow minimum, 2008–2013, upheld by the SCJN on a gross-income base yet
repealed in 2014). SHCP's 2011 IETU diagnostic (UPI) is the domestic anchor document.*
