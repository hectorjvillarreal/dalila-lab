# Mission: BID 2 — Second IADB Paper

**Status:** Open — Active  
**Priority:** High  
**Last updated:** 2026-04-05

---

## Title

*Spending Smarter under Demographic Pressure: Fiscal Efficiency, Health, and Informality in Latin America*

## Team

Héctor J. Villarreal · Diego Ascarza-Mendoza · Hermilo Cortés · Judith Méndez  
Institution: ITED, Escuela de Gobierno y Transformación Pública, Tecnológico de Monterrey  
Commissioned by: Inter-American Development Bank (IADB), Fiscal Division

## Countries

México · Costa Rica · Panamá

---

## Position in BDH

BID 2 is the core modeling mission of BDH. It is the main quantitative contribution of the IADB project *Demographic Transition and Development in Latin America and the Caribbean*. It builds directly on the ITED/DFD modeling architecture.

---

## Core Research Question

How can Latin American governments spend smarter on health under demographic pressure while preserving fiscal sustainability and the contributory architecture of social security?

---

## Modeling Framework

Stochastic OLG model in stationary competitive equilibrium. Heterogeneous agents by skill (low/high), health status (good/poor), and formality status (formal/informal). PAYG pension system with eligibility tied to cumulative contribution record. Endogenous factor prices, incomplete asset markets, consumption floor guarantee.

---

## Empirical Components

- Fiscal-health mapping: health subsystems linked to government budgets and fiscal accounts
- Epidemiological calibration: GBD 2021 DALYs, YLDs, Healthy Life Expectancy
- Age-specific OOP expenditure profiles by skill and health status
- Formality transition matrices by skill type

---

## Current State of Outputs

| Component | Status |
|---|---|
| Abstract | Complete |
| Introduction | Complete |
| Demographic and Fiscal Context | Complete |
| Literature Review | Complete |
| Fiscal Gap Methodology (Appendix A) | Complete |
| Baseline Model document (Diego) | Complete — pending integration into Section 4 |
| Country Health System Profiles (Appendix B) | TODO |
| Calibration (Section 5) | Pending — Milo's Julia code |
| Results (Section 6) | Pending — simulations |
| Policy Implications (Section 7) | Pending |
| Conclusion (Section 8) | Pending |
| References | Pending |

---

## Timeline

| Period | Milestone |
|---|---|
| Nov–Dec 2025 | Project launch and data compilation |
| Jan–Mar 2026 | Fiscal-health mapping and preliminary findings |
| **Apr 2026** | **Epidemiological calibration and first draft — current** |
| May–Jun 2026 | Model integration and policy experiments |
| Jul–Aug 2026 | Sensitivity analysis and policy refinement |
| Sep 2026 | Final paper and replication materials |

Two IADB seminars scheduled: first on preliminary results and framework; second on model results and policy simulations.

---

## Immediate Priority

Credible first draft within approximately six weeks from March 2026. Key pending items: Section 4 integration from model document, Appendix B country profiles, calibration once Julia code is operational.

---

## Cross-references

- Grand Plan project: `GrandPlan/BDH/`
- Model document: Ascarza-Mendoza et al., March 2026 (separate file)
- Dalila compute: Julia (Milo), GPU-accelerated simulation
- Related mission chat: BDH HQ coordination
