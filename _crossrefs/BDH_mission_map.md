# BDH Mission Map
## Cross-Mission Architecture and Analytical Connections

**Location:** `Dalila/_crossrefs/BDH_mission_map.md`  
**Maintained by:** Debb (documentation), supervised with Beth, Cath, Anne  
**Last updated:** 2026-05-10  
**Version:** 0.2

---

## 1. Purpose of This File

This document describes the analytical architecture connecting BDH's four active funded missions. It is designed to be read by Claude Code when retrieving context across missions, and by Debb when reviewing autonomous updates to Dalila files.

It is a **pointer document, not a content document.** It links; it does not duplicate. Each mission's content lives in its own README and dedicated files. This map describes the connections between them.

---

## 2. The Four Missions

| ID | Mission | Level | Primary output |
|---|---|---|---|
| M1 | BID 2 — Spending Smarter | Regional (MEX, CRI, PAN) | Academic paper + simulations |
| M2 | CAF Jalisco | Subnational (Jalisco, MX) | Policy report + diagnostic |
| M3 | IMSS Surgical | National institution (IMSS) | Research report + financing strategies |
| M4 | Community — Health Financing LATAM | Regional (Latin America) | Knowledge community + publications |

---

## 3. The Unifying Logic

These four missions form a coherent research program, not a set of parallel projects. The connecting thread is a single analytical question asked at four different scales:

> **How can health systems in Latin America remain fiscally sustainable and institutionally credible through demographic and epidemiological transition — without undermining the contributory architecture that sustains social security?**

The **formalization incentive constraint** is the analytical spine:
- M1 theorizes and quantifies it within an OLG framework
- M3 operationalizes it within IMSS, a Bismarckian contributory institution
- M2 tests it in a hybrid subnational context (Jalisco's Seguro Popular revival)
- M4 propagates the lesson and builds regional analytical capacity

---

## 4. Layered Architecture

```
Regional framework (M1, M4)
        │
        ├── National institutional case (M3 — IMSS)
        │
        └── Subnational case (M2 — Jalisco)
```

M1 provides the **methodological backbone**: OLG model, fiscal gap framework, formalization tax rate (FTR), demographic projections.

M3 and M2 are **calibration cases**: real institutional settings where the concepts are operationalized with administrative data.

M4 is the **synthesis and dissemination layer**: regional knowledge community, comparative analysis, journal outputs.

---

## 5. Shared Concepts and Components

The following concepts appear across multiple missions. When Claude Code retrieves context, these are the bridging terms.

| Concept | M1 | M2 | M3 | M4 |
|---|---|---|---|---|
| Fiscal gap | ✓ core | ✓ subnational | ✓ institutional | ✓ regional |
| Formalization tax rate (FTR) | ✓ core | ✓ applied | ✓ applied | ✓ disseminated |
| Contributory architecture | ✓ modeled | ✓ tested | ✓ institutional | ✓ comparative |
| OLG simulation framework | ✓ core | — | — | — |
| Demographic projection | ✓ regional | ✓ subnational | ✓ national | ✓ regional |
| Fiscal sustainability test | ✓ core | ✓ applied | ✓ applied | ✓ disseminated |
| Health expenditure profiles | ✓ modeled | ✓ empirical | ✓ empirical | ✓ comparative |
| Informality constraint | ✓ modeled | ✓ contextual | ✓ structural | ✓ regional |
| Epidemiological transition | ✓ calibrated | ✓ local | ✓ IMSS data | ✓ regional |

---

## 6. Shared Data Sources

| Source | Used by |
|---|---|
| CONAPO / CELADE demographic projections | M1, M2, M3, M4 |
| GBD 2021 (DALYs, YLDs, HALE) | M1, M3 |
| OECD health expenditure data | M1, M4 |
| IMSS administrative records (2018–2024) | M3 |
| Jalisco state health accounts | M2 |
| National health accounts (SINAIS) | M2, M3 |
| World Bank — Formalizing Jobs LAC (2025) | M1, M4 |

---

## 7. Methodological Flow

M1 generates outputs that can inform M2, M3, and M4:

- The **fiscal gap methodology** (Appendix A of BID 2) is directly applicable to Jalisco (M2) and IMSS (M3) with subnational/institutional calibration
- The **OLG model** provides the theoretical grounding for financing scenario evaluation in M3
- The **FTR framework** is the evaluative lens for any reform proposal in M2 and M3
- M4 synthesizes findings from M1, M2, and M3 for regional comparative analysis

---

## 8. Bounding Principles for Claude Code

Claude Code must respect three constraints when updating any BDH file autonomously:

**Principle 1 — Scope ceiling.**
Each mission file describes its own mission. Cross-mission content is not added to individual README files. Connections live here, in this map, not in mission files.

**Principle 2 — Pointers, not content.**
This map links to missions; it does not reproduce their content. An entry in the shared concepts table is a pointer. The concept's full treatment lives in the mission file or paper where it originates.

**Principle 3 — Output-triggered growth.**
A new entry — concept, data source, connection — is added only when a mission produces a concrete output that warrants it. Speculative or anticipated connections are not registered until they are real.

---

## 9. Update Log

Claude Code appends a brief entry here after every autonomous update to any BDH Dalila file. Debb reviews this log at the opening of each BDH HQ session.

| Date | File updated | Nature of change | Triggered by |
|---|---|---|---|
| 2026-04-06 | This file | Initial draft | Beth/Debb — BDH HQ session |
| 2026-05-10 | This file | §10 path fixes: capitalize `Funded/`; resolve M4 to actual folder `KC_FHSLatam/README.md` (file renamed from `read.md`) | Héctor — folder/path audit |

---

## 10. File Locations

| Mission | Dalila path |
|---|---|
| M1 — BID 2 | `Missions/Funded/BID2/README.md` |
| M2 — CAF Jalisco | `Missions/Funded/CAF_Jalisco/README.md` |
| M3 — IMSS Surgical | `Missions/Funded/IMSS_Surgical/README.md` |
| M4 — Community LATAM (KC_FHSLatam) | `Missions/Funded/KC_FHSLatam/README.md` |
| This file | `_crossrefs/BDH_mission_map.md` |
| Mission registry | `Missions/_index.md` |
