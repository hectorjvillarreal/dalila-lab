# Review Memo: Fiscal Dominance and Asset Price Redistribution
# To: Héctor (author)
# From: Anne (DFD Core Team)
# Date: 2026-04-04 (updated)
# Re: Draft review — Economics Letters submission (post-revision)

---

## Overall Assessment

The paper is now in submittable form. All items flagged in the April 3 review have
been addressed. The distributional result is formally derived (Proposition 2), the
abstract matches the model's deliverables, the interest rate rule is motivated with
both theory and empirical episodes, and the literature positioning has been
strengthened with three well-chosen additions. The paper does one thing cleanly and
is correctly sized for Economics Letters.

---

## What Works

**The mechanism chain is clear.** Debt pressure → monetary accommodation → lower
discount rates → asset price inflation → concentrated capital gains. Each link is
stated, the algebra is straightforward, and Figure 1 illustrates the nonlinearity
usefully.

**The debt-threshold extension is worth keeping.** The `max(D_t - D̄, 0)` formulation
captures fiscal dominance as a regime rather than a continuous condition. This maps
naturally onto the empirical literature on debt limits and strengthens the paper's
connection to nonlinear fiscal reaction functions.

**Literature positioning is now strong.** The original three strands — fiscal
dominance, debt sustainability in low-rate environments, and discount-rate asset
pricing — are correctly identified. The additions of Greenwald, Leombroni, Lustig,
and Van Nieuwerburgh (2024), Eggertsson, Mehrotra, and Robbins (2019), and
OECD (2025) each serve a distinct purpose: empirical grounding of the asset-price
inequality channel, the demographic-secular stagnation link to r*, and institutional
documentation of the debt environment motivating fiscal dominance.

---

## Items Addressed Since April 3 Review

### 1. Proposition 2 — ✓ Added

The distributional result is now formally stated and proved. The wealth share
σ_t = W_t/(W_t + W̄) is shown to be increasing in D_t under fiscal dominance,
using equation (6) and Proposition 1. The proof is clean and the algebra is
minimal. This closes the gap between what the abstract promises and what the
model delivers.

### 2. Interest rate rule motivation — ✓ Added

Equation (3) now has a full paragraph of motivation at the point of introduction.
It invokes Bianchi-Melosi (2019) for theoretical foundations, cites the Bank of
Japan's yield curve control and the ECB's spread management as empirical episodes,
and connects the rule to the central bank's implicit constraint under debt
sustainability pressure. This is sufficient for Economics Letters referees.

### 3. Perpetuity pricing acknowledgment — ✓ Added

The Gordon growth alternative P = A/(r − g) is explicitly noted, with the
observation that it would not alter the directional result — only the magnitude
of ∂P/∂D — and that it connects naturally to the r − g framework of
Blanchard (2019).

### 4. Abstract precision — ✓ Revised

The abstract now reads "derives a formal condition under which fiscal dominance
generates redistribution toward asset-owning households through the asset price
channel, and show that the wealth share of asset holders is increasing in public
debt." This matches the model's deliverables exactly.

### 5. Figure 1 second panel — ✓ Added

Figure 1 now has two panels: (a) the asset price P(D) and (b) the marginal
effect ∂P/∂D. The convexity of the relationship is now visually apparent.
Parameter values appear in the caption.

### 6. Section 4 title — ✓ Revised

Now reads "Distributional Implications and Policy Interpretation."

### 7. Equation (6) — ✓ Now used in Proposition 2

W_t = λP_t is formally invoked in the proof of Proposition 2, resolving the
unfulfilled-expectations concern.

---

## New Additions (April 4 session)

### 8. Demographic paragraph in Discussion — Added

A paragraph connecting the strength of fiscal dominance (ϕ) to demographic
structure: aging economies face structurally higher ϕ through pension and health
expenditure pressures, while demographic shifts depress r* through saving behavior
changes. This is anchored to Eggertsson, Mehrotra, and Robbins (2019) and
flagged as particularly relevant for middle-income economies undergoing rapid
fertility decline. The paragraph does not expand the formal model — appropriate
for the Economics Letters constraint.

### 9. W̄ invariance acknowledgment — Added

A sentence noting that if public transfers to non-asset-holders are themselves
constrained by the same debt dynamics, the redistributive effect of Proposition 2
is amplified. This is stated as a simplification, not a limitation — it correctly
signals that the model provides a lower bound on the redistribution channel.

### 10. Greenwald et al. (2024) — Added

Cited in the introduction's third literature strand. Their empirical finding —
that declining interest rates generate capital gains on long-duration assets
increasing financial wealth inequality — operates through a closely related
channel. This strengthens the paper's claim to relevance and positions it
relative to the most important recent contribution on the topic.

### 11. OECD (2025) — Added

The OECD Global Debt Report's documentation of record sovereign issuance and
rising interest-payment-to-GDP ratios across member countries is cited as
institutional motivation for the fiscal dominance regime. This gives the paper
empirical grounding without requiring a calibration exercise.

### 12. Elsevier preprint footer — Removed

The `preprint` documentclass option was removed and the `pprintTitle` page style
overridden to suppress the Elsevier footer on the title page.

### 13. Duplicate "future work" — Fixed

The final two paragraphs of the Discussion previously both ended with "is left
for future work." These are now merged into a single closing sentence referencing
both the OLG framework and the micro data requirement.

---

## On the Calibration Question

Assessment unchanged from April 3. The decision to stay fully theoretical is
correct for this submission. The closing sentence in the Discussion now cleanly
delineates the empirical frontier.

If a referee pushes for empirical content, a proxy calibration using ENIGH
financial assets data combined with CNBV brokerage/investment fund data could
yield a defensible range of λ ≈ 0.10–0.15 for Mexico, presented as illustrative
sensitivity analysis rather than a point estimate. But this should not be in the
first submission.

---

## Connection to Paper 2 and DFD

The two-paper sequencing is now cleaner with the demographic paragraph in place:

- **Paper 1 (this draft):** Establishes the mechanism — fiscal dominance redistributes
  wealth through asset prices. Notes the demographic amplifier in the Discussion.
  Theoretical. Economics Letters.
- **Paper 2 (DFD extension):** Endogenizes ϕ through the demographic module, quantifies
  the mechanism in a calibrated OLG setting with NTA age profiles and cohort-level
  asset ownership. The Mexico baseline (June 2026 deliverable) provides the
  quantitative backbone. Empirical. Longer journal.

The demographic paragraph in Paper 1 plants the flag; the DFD simulation engine
delivers the quantification.

---

## Summary Checklist

| Item | Status |
|------|--------|
| Proposition 1 (debt → asset prices) | ✓ Complete |
| Proposition 2 (debt → wealth concentration) | ✓ Complete |
| Motivation for interest rate rule (eq. 3) | ✓ Complete |
| Acknowledgment of perpetuity pricing assumption | ✓ Complete |
| Abstract precision | ✓ Revised |
| Figure 1 second panel (∂P/∂D) | ✓ Added |
| Section 4 title | ✓ Revised |
| Equation (6) used in formal result | ✓ Complete |
| Demographic paragraph in Discussion | ✓ Added |
| W̄ invariance acknowledged | ✓ Added |
| Greenwald et al. (2024) cited | ✓ Added |
| OECD (2025) cited | ✓ Added |
| Eggertsson et al. (2019) cited | ✓ Added |
| Elsevier footer removed | ✓ Done |
| Duplicate "future work" fixed | ✓ Done |
| Calibration deferred to Paper 2 | ✓ Correct |

**Verdict: ready for submission.**

---

*Prepared by Anne · DFD Core Team · April 2026*
*Cross-reference: fiscalD_redistribution.pdf · Debt Ideas Discussion (Héctor–Anne–Cath)*
