Scripts used for `2026-11-09_fiscal_policy_corpus_initial.md` (run with the `dalila` conda env Python, `-I`):

1. `clean_pages.py <photos_dir> <out_dir>` — EXIF transpose, rotate, Otsu paper mask, gutter split, shading flatten, paper mask → one PNG per book page. Env: `GUTTER_WIN` (half-width of the gutter search window, default 0.15; 0.06 was needed for photos 64594–64595), `ONLY_PAGES=192,194` to redo specific spreads.
2. `qwen_page.py <page.png>` — one page through `qwen3.5:9b` on ollama (`/api/generate`, temperature 0, think off, 1600 px max side). Prompt inside.
3. `run_all.py <pages_dir> <out_dir>` — all pages, one `.md` each, resumable, `_progress.md` log.
4. `merge.py` — merges `_transcription_pages/p*.md` into one body: heading normalisation, box titles as `####`, page markers, cross-page paragraph joins.
