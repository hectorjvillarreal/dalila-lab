# Automotive instance — findings

*Human-owned. Verbatim from the source board's scaffold section and board-level notes;
abstract, portable forms of the marked findings live in `scaffold/discipline.md` under
the anchors cross-referenced below. This file is instance-specific by design.*

## Provenance header (verbatim from the board)

> *Aurora · Auto apparatus, Layer 2 (player board) · Lead: Elle · Geopolitical watch items: Gina*
> *Looser than Dalila — no corpus frontmatter. Status notes are date-stamped; the field moves fast.*
> *Six entries loaded 2026-06-21; entry 007 (first mixture) added 2026-07-14. Figures are 2025 actuals or as dated.*

("Auto apparatus" is the board's original self-designation, retained verbatim; the
project vocabulary is now "automotive" — see README.)

## Entry template and slots (verbatim; generalized form in `scaffold/`)

**Entry template:** Player · Archetype · Span/position · Distinctive asset · The bet (falsifiable) · Watch items · Data slots · Status (dated).

**Data slots — how data fits later.** Each entry carries a fixed, consistently-formatted block of named fields. Two rules keep it clean: (1) slots are *derived from the bet* — each falsifiable claim names the variables that confirm or kill it; (2) the block is *model-agnostic* — a flat key→value set, not a model schema. The verify-at-load pass seeded `volume` and a few others; the feed maintains them. Slot blocks are parse-clean for a later Claude Code lift into YAML/JSON.

Provisional slot set (extensible): `volume` · `segment_span` · `vertical_integration` · `margin` · `cost_position` · `geographic_reach` · `legitimacy_assets` · `backing`.
The board has since surfaced **three slot families**: *challenger* (cost/integration), *incumbent* (china_dependence / restructuring_latency / transition_pace_exposure), *frontier* (compute_autonomy_moat / non_auto_optionality). Entries flag custom slots where the standard set doesn't reach.

## Integration ⊥ legitimacy — for Chinese capital only
*(cf. `scaffold/discipline.md#legislated-constraints`)*

**Constraint discovered (2026-07-14), re-specified same day — integration ⊥ legitimacy, *for Chinese capital only*.** First reading: architectural/software integration and Western-market legitimacy are negatively coupled — the US Connected Vehicle Rule adjudicates on governance, software sourcing and data infrastructure, so the integration that delivers cost advantage is the same property that disqualifies. Volvo (disentangled) authorized; Polestar (inside SEA, Geely servers) denied — same parent. **Correction (entry 007): Hyundai holds full architectural integration *and* unimpeded Western access simultaneously, sitting in the region Polestar was expelled from. The difference is a Korean passport.** So the forbidden region is not a structural law of the space — it is a **policy instrument, nationality-gated, discretionary and revocable**. Constraints in this space can be *legislated into existence*, which is a foresight object in its own right.

## The synthetic chokepoint
*(cf. `scaffold/discipline.md#synthetic-chokepoint`)*

**Instance note — the synthetic chokepoint.** Diffusion industries have no natural chokepoint to sanction (no lithography machine to deny). The Connected Vehicle Rule is the answer: where no chokepoint exists, *manufacture one* — data security as pretext, software authorization as gate. Frontier/chokepoint logic imported into a diffusion industry by regulatory construction. It works: it removed a player from the largest premium market. Corollary: walls don't stop the walled-out player, they **channel** it (Polestar → Europe, SE Asia, Eastern Europe, Latin America, Canada). *Portable to pharma: ask what the synthetic chokepoint is there.*

## The poles are unbundling
*(cf. `scaffold/discipline.md#poles-unbundle`)*

**Architecture finding (2026-07-16) — the poles are unbundling.** Two of six corners have now cracked under contact with data: 004 (Toyota) bundles *hedge* with *skepticism*; 001 (Geely) bundles *segment span* with *legitimacy assets*. The poles chosen intuitively were composites mistaken for extremes; data is separating them. This is the archetypal-analysis purity problem arriving empirically — and it **settles the quantification question**: loadings cannot be computed on a basis whose elements keep splitting. The qualitative discipline is not a compromise pending better method; it is the only representation that survives contact. *Poles unbundling is the instrument refining, not failing.*

## Slot corrections

**Slot correction (entry 007):** `china_dependence` and **`tariff_exposure`** are separate — the board had them fused. VW carries both maxed; Hyundai carries only the second. The difference between "flat with a profit hit" and "worst result since dieselgate" in the same year, same tariff regime, same EV softness, is approximately the diffusion exposure.

**Slot correction (2026-07-16):** `transition_pace_exposure` is **regionally conditional**, not a scalar. Great Wall (NEV ~30% of domestic sales vs industry >63%) was eliminated from China's top-ten retail running the skeptic archetype in a fast-transition market; Toyota runs the same archetype in slow-transition markets and prints profit. The archetype is neither right nor wrong — it is region-indexed.

## Shakeouts have institutional forms
*(cf. `scaffold/discipline.md#shakeout-institutional-forms`)*

**Generalization (2026-07-20) — shakeouts have institutional forms.** Same underlying pressure, three mechanisms: **China → elimination** (price war; Great Wall out of the top-ten); **Japan → negotiated consolidation** (JAMA standardisation; Nissan–Honda cooperation reportedly close; Nissan ~27% of Mitsubishi; Toyota stakes in Subaru/Mazda/Suzuki); **Germany → blocked restructuring** (VW, July 9). China's commonality *emerged* endogenously from a tournament; Japan's must be *negotiated* through an association — and negotiation is slow by construction, because consent is its price. "Institutions constrain strategy shape" (VW, 2026-07-14) is now a cross-national regularity, not a single-firm observation. **Portable to pharma directly.**
**Sharpening (added 2026-07-24, from the same source): Japan's consolidation is *nationalizing*.** Domestic ties tighten (Nissan–Honda, Nissan~27% Mitsubishi, Toyota's Subaru/Mazda/Suzuki stakes, a common JAMA supplier standard) while the one *cross-border* alliance loosens — Renault has ceded day-to-day control of Nissan, the partnership now case-by-case model sharing (Micra/R5, Duster/Tekton) rather than central management. Consolidation is not merely negotiated; it is negotiated **along national lines**. *Gina: alliance geometry re-forming around the nation-state as the competitive unit — consistent with the level limitation below.*

## The level limitation
*(cf. `scaffold/discipline.md#level-limitation`)*

**⚠ Level limitation (2026-07-20) — the board is firm-level; the contest may not be.** The diffusion advantage was never BYD-the-firm: it is supplier density, ecosystem depth, commonality produced by a domestic tournament. Japan's response is at the *system* level because that is where the competition sits. **A firm-level board may mis-locate the contest.** Not fixed by adding a player — "national coordination" is a *level*, not an archetype, and must not be entered as a pole (cf. the rejected "export-channel pole"). Possible future object: a **coalition register** alongside the player board. Not now.

## Wall gradient
*(cf. `scaffold/discipline.md#wall-gradient`)*

**Wall gradient (2026-07-20) — walls slow, they do not stop.** Three-point natural experiment on wall height: **US** (tariffs + synthetic chokepoint) → Chinese marques excluded · **Europe** (tariffed) → Chinese marques *collectively outsold Japanese marques for the first time*, May 2026 · **Australia** (unwalled) → China the leading source of new cars YTD-May (144,425 vs Japan 117,332). **Unwalled developed markets flip.** *Direct read for Latin America: Australia is the preview for any market without a wall.*

## Regulation reshapes the tournament from both ends
*(cf. `scaffold/discipline.md#regulation-both-ends`)*

**Instance note — regulation reshapes the tournament from both ends.** The US builds a synthetic chokepoint (Connected Vehicle Rule) to exclude China's *strong* players; China raises a mandatory NEV safety standard (July 2026: crash + battery thermal, "thermal runaway without fire") plus 2027 hybrid tax-exemption shifts that squeeze its *weak* ones. Both favour the big and integrated. Consolidation by regulation, symmetric.

## Regime change (board-level status, 2026-07-16)

**Regime change logged (2026-07-16, CPCA/CAAM H1-2026).** China domestic passenger retail **8.701M, −20.2%**; CAAM total domestic 9.921M, −21.1%. Exports **5.096M, +65.3%** — the primary driver of overall sales. *The diffusion model's engine room — brutal domestic scale and competition — is contracting by a fifth, and growth has relocated wholesale to exports.* Industry framing: an **"elimination cycle"** in a saturated market, survival decided by technology depth, export channels, and manufacturing adaptability rather than domestic scale. **This reframes the board's founding question: "who becomes the Chinese top player" is no longer answered at home.**

**Export standings H1-2026:** Chery **931,600 (+70.9%, 21.9%)** · BYD 769,300 (+73.6%, 18.1%) — *duopoly ≈40% of exports* · Geely 472,500 (+158.3%) · SAIC PV 404,200 (+66.6%) · GWM 256,000 (+52.8%) · Leapmotor 96,300 (+372.6%).

## Board at seven — live contrasts (verbatim closing note)

*Board at seven — a spanning archetype set plus its first mixture, never a size ranking. Live contrasts: diffusion vs frontier (BYD ↔ Tesla) · span conglomerate riser vs faller (Geely ↔ VW) · the incumbent's responses (Toyota hedge ↔ VW adapt ↔ Hyundai diversify) · the AI layer (Huawei-Xiaomi ↔ Tesla ↔ Hyundai) · corners vs the un-cornered middle (007) · **archetype vs instantiation (Leapmotor ↔ BYD)**.*

## Open repairs and next entry (human backlog — not tool work)

**Open repairs:** split the Toyota pole **three ways** (hedge ≠ tempo-skepticism ≠ system coordination) · split the Geely pole (segment span ≠ legitimacy assets) · back-fill `tariff_exposure` for 004/005/006 · region-index `transition_pace_exposure` · decide whether a **coalition register** is needed alongside the firm-level board.
**Thresholds added:** JAMA harness specs agreed by end-2027? (bears on 004) — booked as TH-003 in `thresholds.yaml`.

**Entry 008 — now clearly indicated: Chery.** The board has **no export-channel pole**, and export channel is the variable that now decides the tournament. Chery leads it (931,600, ahead of BYD) and the board doesn't have it. It is also a HIMA partner (Luxeed) — so it enters as a *mixture*, testing the loadings discipline a second time — and it is the export champion into the global South including **Latin America**, which is where this instance touches the DFD/LatAm thread directly. *Runner-up candidate: Leapmotor (the diffusion archetype's better instance; possible Stellantis channel inversion).*

## Custom slot definitions (instance registry)

Per `scaffold/slot-registry.yaml` custom-slot policy, the automotive instance uses:

- `china_dependence` — share of volume/profit dependent on the China market (incumbent family).
- `restructuring_latency` — institutional speed limit on restructuring (incumbent family).
- `transition_pace_exposure` — share of profit pool dependent on the transition staying slow; **regionally conditional, not scalar** (incumbent family).
- `tariff_exposure` — exposure to tariff walls, distinct from `china_dependence` (correction, entry 007).
- `compute_autonomy_moat` — depth of the compute/software/autonomy stack moat (frontier family).
- `non_auto_optionality` — value options outside the vehicle business (frontier family).
