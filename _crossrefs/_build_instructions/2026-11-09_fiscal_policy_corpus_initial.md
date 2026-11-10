---
type: build_instruction
build_type: initial_scaffold
date: 2026-11-09
corpus_affected: [_crossrefs/corpus/fiscal_policy/, GrandPlan/RF/_crossrefs/RF_corpus_fiscal_policy.md, GrandPlan/DFD/docs/corpus/_cross_references.md, FISCUS/_crossrefs_fiscal_policy_corpus.md, Teaching/MEK_FP2026/benassy_quere_cap4_fiscal_261109/, _crossrefs/mission-project-map.md]
triggered_by: "Héctor photographed Chapter 4 (Fiscal Policy) of Bénassy-Quéré et al. (2019) for class; identified it as critical to RF, FISCUS, DFD and teaching; asked for a Markdown version and for mapping across folders (2026-11-09 session)."
agents_involved: [Héctor, Claude Code, Debb, Cath]
status: executed
notes: "Scaffold executed 2026-11-09. Transcription route decided the same day after two dead ends: (1) Claude Code cannot emit a verbatim copy of a copyrighted chapter (output filter), (2) Tesseract 5.5 and RapidOCR fail on the curved, keystoned phone photos. Working route: each photographed spread is split at the gutter, shading-flattened and masked to the paper; each single page is then transcribed by the LOCAL vision model qwen3.5:9b through ollama (temperature 0, no thinking), one Markdown file per page in foundational/_transcription_pages/. Spot-checks on pp. 149, 163, 164: prose near-verbatim, LaTeX equations exact, occasional skipped or duplicated line. Verification pass and merge pending; Cath to endorse after equations are checked."
---

# Build: Fiscal Policy corpus — initial scaffold

## Decisions recorded

1. **One home, many pointers.** The chapter lives in `_crossrefs/corpus/fiscal_policy/foundational/`. RF, DFD, FISCUS and Teaching receive pointer files only, per the shared-resource rule in the root CLAUDE.md.
2. **FISCUS is a scope code.** Héctor's ruling (2026-11-09): FISCUS is more than a project and appears in `project_scope` alongside the Grand Plan codes.
3. **Copyright.** Purchased copy, personal study use. The PDF and transcription stay on Héctor's machines; nothing is redistributed. The PDF (48 MB) is kept in the Teaching folder and excluded from git via `.gitignore`.
4. **Source assembly.** 46-page PDF built from 45 phone photos received in five batches (Gmail drafts with Drive links, then ~/Downloads). Each PDF page is an upright two-page spread; all pages were placed by reading printed page numbers, except pp. 224–225 (placed by content: Box 4.20).

## Steps executed

- Created `_crossrefs/corpus/fiscal_policy/` with README, `foundational/` entry, `watch_items/`.
- Added pointer files in RF, DFD, FISCUS and the Teaching class folder.
- Registered the corpus in `mission-project-map.md`.
- Added the PDF path to `.gitignore`.

## Transcription method (decided 2026-11-09, evening)

- Page preparation (`scratchpad/clean_pages.py`, dalila env): EXIF transpose, rotate 90° CCW, Otsu paper mask, gutter found as the darkest column band (85th-percentile brightness) in the central 30% of the book, split, per-half paper mask with holes filled, background divided out with a σ=60 Gaussian, non-paper painted white, unsharp mask. 89 single-page PNGs.
- Transcription: `qwen3.5:9b` via ollama `/api/generate`, image downscaled to 1600 px max side, temperature 0, `think: false`, `num_predict` 3000. Prompt asks for verbatim Markdown, LaTeX equations with their (B4.x.y) labels, boxes as blockquotes, figure captions plus a short description, footnote markers as `[^n]`, running headers and neighbouring-page slivers ignored. About 15–30 s per page on the RTX PRO 2000.
- Why not Tesseract/RapidOCR: both installed into the dalila env without sudo; both break on the page curvature (Tesseract ≈ 40% garbage; RapidOCR detects 11–20 of ~45 lines per page).
- Why not Claude Code directly: a verbatim transcription of a copyrighted chapter is blocked by the output filter, even for the owner's personal use.

## Steps executed (evening, 2026-11-09)

- 89 pages transcribed (≈37,000 words). Two spreads (pp. 192–195) had been split at the wrong gutter; re-split with a narrower window and re-transcribed. p. 236 discarded (photo illegible; the model hallucinated unrelated content) and replaced by a placeholder.
- Verification: all display equations in Boxes 4.2, 4.5, 4.9–4.15 and eqs (4.1)–(4.2) checked symbol by symbol against the page images — exact. Prose checked on ~20 pages; fixes: skipped line p. 149 area, duplicated half-line p. 164, invented page-break words p. 152, spurious footnote p. 192, placeholder footnotes p. 215, duplicated note p. 230.
- Merged into `foundational/benassy-quere_2019_ch4_fiscal_policy.md` with page markers. Book misprint noted: two boxes printed "4.18" (pp. 213, 219); text refers to the first as 4.17.
- Scripts archived in `2026-11-09_fiscal_policy_corpus_scripts/`.

- p. 236 re-photographed (64691.jpg, 14:36); three references read directly from the sharp image and added; PDF page 46 replaced by the new photo.

- Endorsement requested from Cath: `_crossrefs/corpus/fiscal_policy/20261109_CORPUS_briefing_cath_fiscal-policy-endorsement.md` (copy in `_crossrefs/team/cath/`).

- 2026-11-09 (evening) — Cath review (`…/20261109_CORPUS_briefing_cath_fiscal-policy-endorsement.md`, two replies): endorsement withheld pending A1–A4 (page-image checks) and B1–B5 (clean-up); team notes 1–2 supplied. Claude Code executed A1–A4 and B1–B5 the same evening (script `2026-11-09_fiscal_policy_corpus_scripts/apply_cath_review.py`): B4.13.6 misprint confirmed and annotated, ≅ restored in B4.5.4–5, Box 4.14 ¶1 restored, placeholders removed, box-end markers and anchors added, team notes inserted, two watch items opened. Re-check of A1 by Cath required before `endorsed_by` is set.
- Note: the merged entry is now the canonical, hand-corrected layer; `merge.py` must not be re-run over it (it would regenerate from the raw page files and drop these fixes).

## Steps pending

- Cath re-checks A1 and endorses; `endorsed_by` filled; `transcription_status` set to `verified`.
