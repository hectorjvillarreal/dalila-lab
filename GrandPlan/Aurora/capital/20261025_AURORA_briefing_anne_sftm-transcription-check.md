---
type: briefing
to: Anne
from: Claude (for Héctor)
date: 2026-10-25
subject: "Transcription check: EIC 2025 figures in the SFTM México note (Elle's review, comment 3)"
note: GrandPlan/Aurora/capital/20261025_AURORA_SFTM-MEX-inference_v1.md
doc: https://claude.ai/artifact/XxVSKpppC35Z8N8A6sFkiU
source: GrandPlan/DFD/outputs/briefs/2026-09_EIC2025_nota/ (Nota EIC 2025 v1.0, endorsed by Anne and Cath, 23b74a0)
commit_at_send: 2694a21
---

# Anne — transcription check on the EIC 2025 figures

**Ask (Elle's review, comment 3).** Confirm that the EIC 2025 figures in the SFTM México note
transferred correctly from your endorsed Nota EIC 2025 v1.0. Elle frames it as "a transcription
check, not a doubt about content". It is provenance hygiene before any endorsement. Cath is
checking the fiscal figures in parallel.

**Where the figures sit.** In the note, the table in §3.4 "Demographic realism". The same figures
are repeated in the §1 synthesis ("15–64 falling from 2036") and in the BKY-seam paragraph added
after Elle's comment 2. In the doc, the table is in "Demographic realism (Anne)".

## Figures to check

| Figure in the note | Where it is in the Nota v1.0 PDF | Pre-check |
|---|---|---|
| TFR 1.23 (EIC 2025, for 2024) | Text, p. 1 ("de 1.23 en 2024"); also the release note `_crossrefs/corpus/demographics/releases/2026-09-22_inegi-eic2025_tgf-trigger-fired.md` | Found in the PDF |
| Total dependency ratio minimum 45.0 in 2030; within 1 point over 2027–2035 (Central) | Scenario table, Central row; text "menos de un punto de su mínimo entre 2027 y 2035" | Found in the PDF |
| 15–64 grows 0.37%/yr 2025–2035; first falls in 2036 in every scenario | Text: "crece 0.37 % anual entre 2025 y 2035 y empieza a caer en 2036 en los…" | Found in the PDF |
| 15–64 falls 0.48%/yr 2035–2050 (Central) | **Not in the PDF text.** Taken from `_assumptions.md` (the v0.2 working file, Step 3 block) | Please confirm, or tell us to drop it |
| Old-age ratio (65+/15–64) 14.6 in 2025 → 33.1 in 2050 (Central) | 33.1 is in the scenario table ("Razón de vejez"). **14.6 is not in the PDF text.** It comes from `_assumptions.md` ("OADR 2025 → 2050: 14.6 → 33.1") | Please confirm the 2025 value, and that it uses the same definition as the 2050 one |
| PAYG-equivalent contribution rate 11.6% → 26.2% of the wage bill (Central, 2025 → 2050) | Contribution table, Central row; text "pase de 11.6 % a 26.2 % (Central)" | Found in the PDF |

## Also check

1. **Framing of the TFR row.** The note's table is labelled "Central scenario", but its TFR row
   shows the observed EIC value, 1.23. In the Nota, Central *assumes* 1.50 and "INEGI directo"
   carries 1.23. Should the row be relabelled "observed (EIC 2025)" to avoid implying that
   Central runs at 1.23?
2. **BKY seam (comment 2, added today).** The note says BKY's 2097 adoption date rests on WPP 2024
   with México's TFR near 1.7 in 2050. That figure comes from the Debb source check in
   `GrandPlan/DFD/aging_macro_nber_2609/2026-09-17_global-transition-demographics-ai.md`: WPP 2024
   medium gives 1.701 at 2050. The paper's own Table 6 gives 1.67. Is "near 1.7" the right
   wording? Open question 8 (adoption date on current demographics) is routed to you and Nina.

**Reply.** Confirm or correct each row in your review record or as doc comments. Corrections go to
both the note (canonical) and the doc. After this check, your endorsement of §3.4 can be
recorded.
