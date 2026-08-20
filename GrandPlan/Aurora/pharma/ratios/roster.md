# roster.md — pharma ratio panel

**Owner:** Héctor. Human-owned, tool-read-only.
**Drafted by:** Nina, 2026-08-16. Draft for correction.
**Read by:** `20260816_AURORA_BUILD_pharma-ratio-panel_v1.0`.

Twenty firms. Chosen for **structural coverage**, not size — several large firms are
absent and several mid-caps are present. This is a back-office roster, not a board.
Nothing here classifies anything.

`loe_major` dates marked `?` are my approximations and are **unverified**. They must
be corrected against company disclosure before the column carries any weight. The
tool may not estimate them; blank is better than wrong.

---

## Roster

| # | Ticker | Firm | loe_major | Why on the roster |
|---|---|---|---|---|
| 1 | `LLY` | Eli Lilly | 2036 | Frontier rent at maximum; metabolic franchise concentration |
| 2 | `JNJ` | Johnson & Johnson | 2029 | Diversified across pharma and devices — tests whether diversification is a position or an accident |
| 3 | `AMGN` | Amgen | 2028 | Biologics incumbent whose own products are the biosimilar target |
| 4 | `PFE` | Pfizer | 2028 | Rent collapse followed by acquisition-led replacement — the cleanest replacement case |
| 5 | `MRK` | Merck & Co | 2028 | Single-asset concentration; the largest scheduled extinction in the industry |
| 6 | `VRTX` | Vertex | 2037 | Pure frontier, single disease area, no diffusion exposure at all |
| 7 | `NVO` | Novo Nordisk | 2032 | Frontier peer to LLY under a different ownership structure (foundation control) |
| 8 | `AZN` | AstraZeneca | 2032 | Deepest China exposure among Western majors — the walls case |
| 9 | `NVS` | Novartis | 2029 | Deliberately exited diffusion by spinning out Sandoz — a firm that chose a pole |
| 10 | `RO.SW` | Roche | 2029 | Pharma plus diagnostics; long biosimilar erosion history |
| 11 | `SNY` | Sanofi | 2031 | Vaccines plus branded; different rent structure from the small-molecule majors |
| 12 | `4502.T` | Takeda | 2032 | Debt-financed acquisition of frontier rent — leverage as strategy |
| 13 | `4568.T` | Daiichi Sankyo | 2033 | Owns a platform it licenses to a larger firm — stack rentability seen from the owner's side |
| 14 | `SUNPHARMA.NS` | Sun Pharmaceutical | n/a | India's largest; generics base attempting branded entry |
| 15 | `DRREDDY.NS` | Dr. Reddy's | n/a | Generics and biosimilars, heavy regulated-market exposure |
| 16 | `2359.HK` | WuXi AppTec | n/a | The service layer, and the named target of Western supply-security instruments |
| 17 | `600276.SS` | Jiangsu Hengrui | n/a | Chinese domestic frontier attempt with Western out-licensing |
| 18 | `TEVA` | Teva | n/a | Diffusion player that attempted the frontier and carried the debt for it |
| 19 | `SDZ.SW` | Sandoz | n/a | Pure-play biosimilar and generic — diffusion logic with nothing else attached |
| 20 | `LONN.SW` | Lonza | n/a | Manufacturing capacity as the product; the rentable frontier layer in pure form |

`n/a` in `loe_major` marks firms whose economics are not organised around a single
scheduled expiry. That is itself a structural fact and should not be read as missing
data.

## LOE verification (2026-08-18, by CC at Héctor's instruction)

All 13 dates verified against company disclosure or settlement reporting; `?` marks
removed. Anchor product, governing instrument, and source per firm:

| Ticker | Anchor product | Governs | Source |
|---|---|---|---|
| `LLY` | tirzepatide (Mounjaro/Zepbound) | US compound patent 2036 | Lilly 10-K FY2025 patent table |
| `JNJ` | Darzalex (daratumumab) | US patents incl. PTE 2029 | Genmab 20-F; JNJ 10-K |
| `AMGN` | 2028–29 cluster: Otezla (Feb 2028), Repatha (Aug 2028), Enbrel (Nov 2028/Apr 2029) | US patents per 10-K | Amgen 10-K patent table |
| `PFE` | Eliquis (apixaban, BMS alliance) | settlement entry no earlier than 2028-04-01 | BMS–Pfizer alliance statement; BMS 10-K |
| `MRK` | Keytruda (pembrolizumab) | US compound patent Dec 2028 | Merck 10-K FY2025 |
| `VRTX` | Trikafta | US basic product patent 2037 | Vertex 10-K FY2025 |
| `NVO` | semaglutide (Ozempic/Rybelsus/Wegovy) | US compound patent + ped. excl., company states 2032 | Novo 20-F FY2025 |
| `AZN` | Tagrisso (osimertinib) | US substance patents incl. PTE Jul–Aug 2032 | AZ patent-expiry schedule (Feb 2026) |
| `NVS` | Cosentyx (secukinumab) | US composition patents + PTE 2029 | Novartis 20-F |
| `RO.SW` | Ocrevus (ocrelizumab) | 12-yr BLA exclusivity floor Mar 2029; entry could slip to 2030 | FDA BLA date; trade reporting |
| `SNY` | Dupixent (dupilumab) | US composition patent Mar 2031 (company base case) | Sanofi investor disclosure via Fierce |
| `4502.T` | Entyvio (vedolizumab) | US patents ~May 2032 per 20-F; pre-2032 at-risk entry possible | Takeda 20-F FY2025 risk factors |
| `4568.T` | Enhertu (T-DXd) | US NME patent incl. PTE 2033 | AZ patent-expiry schedule (partner disclosure) |

Caveats that survive verification: `AMGN` has no single dominant product — 2028 is a
cluster, not one expiry. `RO.SW` 2029 is the regulatory exclusivity floor, not a
company-stated date (medium confidence). `PFE` and `4502.T` dates are
settlement/litigation-shaped. `LLY` and `SNY` hold formulation patents that could
extend effective protection well past the anchor year; the anchor is the compound
date. `VRTX` is migrating patients to Alyftrek (US 2039), so effective franchise LOE
may exceed 2037.

---

## Known weaknesses

**Mixed accounting regimes.** US GAAP, IFRS, Ind AS, and PRC GAAP are represented.
Ratios built from margins, book value, and R&D treatment are **not cleanly
comparable across this roster**. Currency cancels within most ratios; accounting
policy does not. Treat cross-sectional deviation on P/B, ROIC, and margins as
unreliable across regime boundaries, and lean on the own-history comparison for
firms 14–20.

**Deliberate absences.** Bristol Myers Squibb, AbbVie, GSK, Gilead, Regeneron,
Bayer, Viatris, Cipla, Samsung Biologics. Each is defensible; none adds structural
coverage the twenty above do not already provide. Samsung Biologics is the one I
would add first if the roster grows, since Korea as a biosimilar-and-CDMO base is
currently unrepresented.

**Selection is mine, not the board's.** These twenty encode a guess about which
structural positions exist in this industry. The board has not been built and may
disagree. When it does, the roster changes and the panel's history carries a break
— note the break rather than backfilling.
