# Aurora — Nina Monetary Theory Foundation
## The Duffie-Reis Framework: Fed Balance Sheet, Reserve Demand, and Elastic Supply

*Document type: Knowledge File · Aurora Project*
*Session date: April 2026*
*Authors: Nina (primary), Debb (editorial)*
*Status: Active — foundational module*

---

## 1. Context and Purpose

This document records the foundational monetary theory session for Nina's Aurora integration. The session was anchored in the Duffie-Reis exchange at the Brookings Papers on Economic Activity (BPEA), Spring 2026 conference, supplemented by Warsh (2025), Bailey (2024), and Schnabel (2025). It establishes Nina's core monetary framework for Aurora scenario analysis, the ABM research agenda, and the cross-project connection to DFD's fiscal sustainability work.

The session was organized around a thread by Ricardo Reis (LSE) on X, summarizing the Brookings discussion in eight points for a broader economics audience, paired with his written BPEA discussion comment and the Duffie (2026) paper itself.

---

## 2. Why Monetary Theory Belongs in Aurora

Although monetary policy lies outside the four TD drivers (AI, quantum computing, energy, life sciences), it belongs in Aurora for three reasons:

**Capital structure for TD transitions.** Energy transitions and AI diffusion at TD scale require decades of patient capital. The monetary regime — real rates, fiscal dominance, sovereign spreads — determines whether that capital is available and at what cost.

**Financial amplification of TD diffusion.** AI adoption propagates through financial conditions and firm balance sheets. Brunnermeier-Reis amplification mechanisms apply: productivity surges concentrated in a few sectors can generate asset price dynamics, currency mismatches, and confidence spirals in emerging markets.

**ABM as Aurora's scenario engine.** The regime transitions Aurora tracks — technological disruption, geopolitical realignment, demographic inflection — generate nonlinear macro-financial dynamics. Nina's ABM layer is the computational tool for producing those transition scenarios endogenously.

---

## 3. The ABCD Framework: Why Reserve Demand Has Grown

*Primary source: Reis (2026 BPEA); Duffie (2026 BPEA)*

Banks hold **reserve balances** at the Federal Reserve to make payments to each other. Before 2008, total US reserve balances were approximately $10 billion. By end-2025 they stood at approximately $3 trillion — roughly 300 times larger. Reis organizes the reasons for this structural shift into four factors:

**A — Regulatory minimums.**
Post-GFC liquidity regulations (Reg YY, RLAP, CLAR) require large banks to demonstrate self-sufficient liquidity. Supervisors have interpreted these rules as requiring large reserve cushions. Pre-crisis, the ten largest banks averaged $120 billion per day in daylight overdrafts from the Fed. By 2025, system-wide daylight overdrafts average under $5 billion. The effective regulatory floor on reserve holdings has increased by hundreds of billions of dollars.

**B — Surplus bank lending incentives.**
Pre-GFC, the Fed paid no interest on reserves, so banks with surplus reserves lent them immediately. Post-GFC, the Fed remunerates reserves at approximately market rates (IORB). Surplus banks now have weak incentives to lend excess reserves into the interbank market. The redistributive function of the federal funds market has largely collapsed.

**C — Interbank friction costs.**
FDIC insurance fees (up to 42 basis points on total liabilities for the largest banks) and higher leverage capital requirements have made interbank reserve borrowing substantially more expensive. The market that should clear reserve imbalances efficiently is now too costly to do so smoothly.

**D — Discount window / SRF stigma and penalty.**
Banks that run short of reserves can borrow from Fed facilities (discount window, Standing Repo Facility). In practice, supervisors treat facility usage as a potential stress signal — even for routine liquidity management. Banks rationally avoid these facilities even when borrowing would be profitable, leaving money on the table to preserve supervisory standing.

**All four factors shifted right after 2008.** Combined, they have produced a permanently higher and more volatile demand curve for reserves. Each factor has a different policy owner and a different reform timeline — making coordinated demand reduction institutionally complex.

---

## 4. The Policy Problem: Inelastic Supply Meets Volatile Demand

The Fed has historically supplied reserves **inelastically** — choosing a fixed quantity through open market operations and holding it. When demand fluctuates around that fixed supply, money market rates become volatile.

The canonical failure event is **September 17, 2019**:
- Reserve balances had declined to $1.4 trillion during quantitative tightening
- SOFR jumped 315 basis points above IORB in a single day
- Interdealer repo rates spiked approximately 1,000 basis points above IORB
- Mechanism: self-fulfilling coordination failure — banks expecting payment delays throttled outgoing payments, causing the delays they feared
- This is a **Brunnermeier-Reis run mechanism** applied to the payment system rather than a bank's funding structure

More recent stress events: October 31, 2025 (SOFR 32bps above IORB) and December 31, 2025 prompted the Fed to halt quantitative tightening and begin reserve management purchases of $40 billion per month.

---

## 5. The Political Economy: Warsh and the Balance Sheet Reduction Goal

*Primary source: Warsh (2025), "Commanding Heights: Central Banks at a Crossroads," G30/IMF lecture*

Kevin Warsh, incoming Fed chair, has argued that the large balance sheet is not a neutral monetary instrument. His case has two tracks:

**The fiscal track.** QE has subsidized government borrowing costs, making fiscal expansion easier and blurring the line between monetary and fiscal policy. Warsh introduces the concept of **economic imprinting**: each Fed intervention expands its footprint, enabling more fiscal expansion, which requires a larger subsequent intervention. Path dependency may be driving policy toward structural instability.

**The institutional track.** Fed expansion into climate policy, inclusive employment definitions, and other areas beyond core mandate has weakened the credibility needed to perform core functions. A smaller balance sheet is part of a strategic reset toward a narrower, more credible institution.

Warsh's disposition creates a direct tension with the Duffie-Reis analysis: political pressure to shrink the balance sheet is accelerating while the structural reforms needed to do so safely are multi-year undertakings.

---

## 6. The Logan-Schulhofer-Wohl Insight: Supply and Demand Are the Same Lever

*Primary source: Logan and Schulhofer-Wohl (2018, 2025); Reis (2026)*

The most important conceptual clarification in the thread: **balance sheet reduction and reserve demand reduction are not two separate policy levers — they are the same lever.**

The Fed can reduce its asset portfolio through QT, but if structural reserve demand has not also fallen, the system will hit the payment-system floor before reaching any politically meaningful balance sheet target. The September 2019 dynamics will replay.

This means balance sheet strategy and banking regulation are **institutionally inseparable** — but they sit in different parts of the Fed's governance structure and involve different external stakeholders whose cooperation is not guaranteed.

---

## 7. The Solution Architecture: Elastic Supply

*Primary source: Reis (2026 BPEA); Bailey (2024 Goodhart Lecture); Schnabel (2025 ECB)*

Reis argues the Fed must transition from inelastic to **elastic supply**. The architecture has two components:

**Standing stock V\*.** A baseline quantity of reserves supplied through normal open market operations. This can be smaller than today's $3 trillion once demand reforms (ABCD) take effect.

**Full-allotment standing repo facility at fixed rate i\*.** Any eligible bank can exchange Treasury bills for reserves in any quantity at any time at a pre-announced rate set just above IORB — small enough that the two rates are operationally interchangeable as "the policy rate."

The facility makes the supply curve **horizontal above V\***. When demand spikes — TGA fluctuation, quarter-end window dressing, geopolitical shock — banks access the facility rather than bidding up money market rates. Rate volatility is eliminated by design.

**Key property:** an elastic supply produces the **smallest possible average balance sheet** consistent with the Friedman rule target. An inelastic supply targeting the same average systematically overshoots because it cannot respond to downside demand shocks.

**Existence proofs:**
- Bank of England Short Term Repo (STR): full allotment at Bank Rate, one-week tenor. Banks borrowed a record £100.9 billion in January 2026. Sterling reserve balances declined overall.
- ECB: Schnabel (2025) articulates the demand-driven framework as central bank operations being part of day-to-day bank liquidity management, not a backstop.

---

## 8. The Obstacle: Stigma as Supervisory Failure

*Primary source: Reis (2026 BPEA), point 8 of thread*

The Fed created Standing Repo Operations in December 2025 — a version of the elastic supply facility. Banks have largely not used it, even when borrowing reserves from other banks at rates well above the SRF rate.

Reis's diagnosis is explicit: **stigma is doublespeak for supervisory failure.**

Two specific failures:

**Supervisory misclassification.** US supervisors treat SRF usage as analogous to discount window borrowing — a potential stress signal. But the discount window is emergency access at a penalty rate; the SRF is routine liquidity management at the policy rate. Treating them identically is a supervisory error with no prudential justification.

**Absent central clearing.** The Fed does not centrally clear its repo operations. When a bank uses the SRF, the transaction consumes a small amount of capital — which would not occur if centrally cleared. There is no justification for this design flaw.

**Cross-country evidence is decisive.** Banks in the eurozone and UK face equally stringent regulation and use standing repo facilities routinely without stigma. The difference is not the rules — it is how US supervisors implement the rules. This is correctable without legislation, without interagency coordination, and without a multi-year infrastructure project. It requires a change in supervisory culture and CLAR implementation within the Fed's own governance.

---

## 9. Aurora Risk Scenario

The scenario Aurora tracks at the intersection of this framework with fiscal and geopolitical dynamics:

Political pressure to shrink the balance sheet (Warsh) accelerates faster than demand-side (ABCD) and supervisory reforms. The system encounters a TGA shock or quarter-end window dressing event while reserves are near the payment-system floor. The SRF remains stigmatized and underused. The September 2019 coordination failure replays — but in a fiscal environment with larger deficits, higher debt levels, and less QE capacity to resolve the episode, and in a geopolitical environment that amplifies dollar funding stress.

**Transmission to emerging markets.** A US payment system coordination failure under these conditions does not stay contained. The amplification channels are:
- Cross-currency basis spikes as dollar funding stress propagates
- Sudden stops in capital flows to emerging markets
- Reserve drawdowns by central banks defending exchange rate pegs
- Sovereign spread widening where fiscal dominance is already present

Latin America is most exposed: dollar-denominated liabilities, thin reserve buffers, fiscal dominance pressures, and deep exposure to US money market conditions. This connects Nina's monetary framework directly to Cath's OLG fiscal sustainability work and Gina's geopolitical layer.

---

## 10. Nina's ABM Research Agenda

The ABCD framework maps directly to an agent-based model design:

**Micro layer.** Heterogeneous banks with individual ABCD parameters, supervisory risk perceptions, and beliefs about counterparty behavior. The stigma coordination failure — no bank uses the SRF even when profitable because no bank expects others to — is the target emergent phenomenon.

**Macro layer.** Aggregation of individual decisions into system-wide reserve balances, money market rates, and payment timing distributions. September 2019 is the calibration target: reproduce a sudden rate spike from a coordination failure without an exogenous shock.

**External stress layer.** Fiscal shocks (TGA volatility, sovereign spread widening) and geopolitical shocks (dollar funding stress, sudden stops) as perturbations. This is where Gina's scenario inputs enter the model.

**Implementation:** Agents.jl in Julia, consistent with the existing Dalila/DFD stack.

**First deliverable:** A design note specifying agent types, behavioral rules, parameter space, and calibration targets — before any code is written. This provides Cath with the OLG-ABM interface specification simultaneously.

---

## 11. Key References

| Reference | Role in Framework |
|---|---|
| Duffie, D. (2026). "The Payment System Puts a Floor on the Fed's Balance Sheet." BPEA Spring 2026. | Primary empirical and institutional analysis. Payment system mechanics, ABCD demand drivers, September 2019 evidence, policy toolkit. |
| Reis, R. (2026). "Payment Needs and the Size of the Federal Reserve's Balance Sheet." BPEA Spring 2026. | Analytical framework. ABCD taxonomy, elastic supply architecture, stigma as supervisory failure. |
| Warsh, K. (2025). "Commanding Heights: Central Banks at a Crossroads." G30/IMF Lecture, April 2025. | Political economy context. Balance sheet reduction rationale, institutional critique, economic imprinting concept. |
| Bailey, A. (2024). "The Importance of Central Bank Reserves." Goodhart Lecture, LSE. | BOE elastic supply existence proof. STR design and supervisory normalization. |
| Schnabel, I. (2025). "Towards a New Eurosystem Balance Sheet." ECB Conference on Money Markets. | ECB demand-driven framework. Elastic supply in the eurozone context. |
| Logan, L. and Schulhofer-Wohl, S. (2025). "Options for Modernizing the FOMC's Operating Target Interest Rate." Dallas Fed. | Supply-demand identity insight. Balance sheet reduction requires demand reduction. |
| Brunnermeier, M. and Reis, R. (2023). *A Crash Course on Crises.* Princeton University Press. | Nina's foundational crisis framework. Run mechanisms, amplification taxonomy applied to payment system coordination failures. |

---

## 12. Agent Interfaces

| Agent | Connection to this framework |
|---|---|
| **Cath** | OLG fiscal sustainability work connects to monetary-fiscal interaction under fiscal dominance. OLG-ABM interface specification needed when ABM design note is produced. |
| **Gina** | Geopolitical shock layer: dollar funding stress, sudden stops, and reserve drawdowns as external stress inputs to the ABM scenario engine. |
| **Elle** | Strategic architecture: this framework feeds Aurora's structural scenario design and the TD drivers' capital structure analysis. |
| **Debb** | Corpus documentation: this file is the primary Knowledge File for Nina's monetary theory module. |

---

*Last updated: April 2026 · Nina & Debb · Aurora Project · GrandPlan*
