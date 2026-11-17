# Fina — Endorsement check of design note B0 v1.1

*Fina · Aurora · 2026-11-16 · Read only. I read the note (014e171 and 3edcb0d), the build instruction, the spec's §5.6 amendment and footer, line 6 of the README and my filed review. The figures were recomputed with a fresh script of my own, `fina_check/scripts/check3.py`, from Appendix A of v1.1.*
*Filed verbatim by Claude Code, 2026-11-16. The alternative 3σ-day values (post-ETF within-window 1.58 % BTC / 1.68 % ETH; pre-ETF excluding 2020-03-12 from the series 2.08 % / 1.79 %) were re-verified by Claude Code before filing. Fixes 1–8 are applied in design note v1.2.*

## Endorsement

**Endorse with minor fixes (listed below; no re-review needed).** All seven required changes and all five recommended changes are applied. One convention still needs a sentence, the 3σ-day share; the figures reproduce once it is stated.

## Per-item table

| Item | Result |
|---|---|
| Req. 1 (§1.1 columns, the regime reading, confounders) | Applied correctly. |
| Req. 2 (regime-shift test moved to B2, one factor at a time, targets s.d. and the 10 %-day share) | Applied correctly. The new rule that leverage changes are "taken from data" is an improvement. |
| Req. 3 (phase map and spec amendment) | Applied, with one problem. §3.4 and the §5.6 amendment line are good. But the spec's own status line (line 6) still says "Part B not started … Nina's review pending." |
| Req. 4 (§1.4) | Applied correctly. Causes are marked unsourced, the table is retitled, the missing rows and cells are filled, and 2022-11-09 is corrected to −14.3 %. |
| Req. 5 (bridge to the board) | Applied correctly. There is no drawdown leg, everything is in board-observable units, bands are ruled on observed data now, and the rule "no model number on the dashboard" is restored. |
| Req. 6 (build instruction and back-links) | Applied, with two small problems. All seven mandatory frontmatter fields are present (type, build_type, date, corpus_affected, triggered_by, agents_involved, status). Back-links are in the spec footer, README line 6 and the note header. The problems: the body is a retrospective record, not PROTO-RAG-001's eight-section format, which I accept for a record; and the data snapshot is still in the scratchpad. It is listed as an open item and is due in B1a. |
| Req. 7 (location, GPU check) | Applied correctly. `tests/gpu_check.jl` exists on main, so a branch cut from main carries it. |
| Rec. fivefold vs threefold; Brunnermeier-Pedersen "stand-in"; Monetary Foundation §10 caveat and Gina hook; Ester timing; §3.3 labels | All applied correctly. |
| §11 acceptance criteria | Carried accurately. Cath's additions are folded in: the φ=0 ablation, conservation, perp=spot, and the same optimiser for recovery. "Common random numbers" dropped out of criterion 7. |
| §12 cadence | Carried accurately. |
| Option C (branch plan) | Recorded consistently in note §8 and §10, the note header and the build instruction's notes. It does not say where build instruction 2_of_2 will be filed. |
| Filed review | Verbatim apart from the header line: my script path was dropped and a filing note was added. That is acceptable. |

## Number check

**These reproduce exactly**, to the printed precision, in all six §1.1 columns:
- s.d. (daily and annualised);
- skewness and excess kurtosis;
- Hill index;
- ACF of |r| at lag 1;
- the shares of days beyond 10 %, log and simple;
- worst days;
- correlation (0.84 / 0.83) and beta (1.07 / 1.18);
- the "7×" and "2×" ratios.

Every figure in the §1.4 episodes table also reproduces.

**The 3σ-day share reproduces only under a rule the note does not state.** The pre-ETF columns match my values (1.96 % BTC, 1.73 % ETH). The other four cells depend on two choices:

- **Post-ETF (1.92 % BTC, 1.73 % ETH).** These reproduce only if the 90-day trailing s.d. reaches back before 2024-01-11. Kept within the window, as Appendix A says returns are, they are 1.58 % and 1.68 %.
- **Pre-ETF without 2020-03-12 (1.90 % BTC, 1.67 % ETH).** These reproduce only if the crash day is dropped from the count but kept inside the trailing s.d. That is 33/1,734 and 29/1,734 days. If the day is dropped from the series, as for the other moments in that column, the values are 2.08 % and 1.79 %.

The conclusion that tail shape does not move survives under every variant, because the Hill index carries it. But "about 1.9 % throughout" holds only under the note's unstated rule.

## Minor fixes (exact wording)

1. **Appendix A, 3σ bullet.**
   - Replace: "3σ day: |r_t| > 3 × s.d.(r_{t−90..t−1});"
   - With: "3σ day: |r_t| > 3 × s.d.(r_{t−90..t−1}), where the trailing s.d. uses the full return history, including returns before the window opens. In the column that excludes 2020-03-12, that day is removed from the count but kept in the trailing s.d. With a within-window trailing s.d., post-ETF BTC is 1.58 % and ETH 1.68 %."
2. **§1.1 Reading.**
   - Replace: "the 3σ-day share is about 1.9 % throughout"
   - With: "the 3σ-day share is 1.9–2.0 % for BTC and about 1.7 % for ETH in both periods (convention in Appendix A)"
3. **§0.**
   - Replace: "Returns throughout are simple, measured from the prior close."
   - With: "Returns in examples, worst days and episodes are simple, measured from the prior close; moments use log returns (§1)."
4. **§1 intro.**
   - Replace: "reproduced independently by Fina (whose own run also gives the Hill indices)"
   - With: "reproduced independently by Fina (review and endorsement check, 2026-11-16)"
5. **Spec, line 6.**
   - Replace: "Part B not started — B0 design note waits for Héctor's go. Nina's review pending."
   - With: "Part B: design note B0 v1.1 filed 2026-11-16, D1–D6 ruled, reviewed by Cath and Fina; B1 waits for Héctor's go."
6. **Note header, §8 provenance line.** After "B1 gets build instruction 2_of_2", add: ", filed on main before the first commit on `aurora-crypto-abm`."
7. **§11, criterion 7.**
   - Replace: "A fixed seed gives bit-identical runs,"
   - With: "A fixed seed gives bit-identical runs, with common random numbers across draws,"
8. **After endorsement**, update three places:
   - the note's Status line and D6: "Endorsement of v1.1 by Cath and Fina is pending" becomes "Fina endorsed v1.1 with minor fixes, 2026-11-16". Record Cath's endorsement separately.
   - item 3 of §4 of the build instruction ("Design note v1.1: endorsement by Cath and Fina"), updated to match.

I made no edits and no price statements.
