# src: MX-SSRD Phase 0 code

All Python runs with `-I`. That flag drops the script directory from `sys.path`, so scripts that import a sibling add it back explicitly. No code lives in `corpus/`.

| Module | Does | Reads | Writes |
|---|---|---|---|
| `to_text.py` | PDF or HTML to UTF-8. HTML keeps only `DivDetalleNota`, marks image tables, cuts the DOF disclaimer. PDF uses reading order for two-column pages, not `-layout`, which interleaves columns. Prepends the DOF date line. | `corpus/raw/`, `manifest.yaml` | `corpus/text/`, hashes in `manifest.yaml` |
| `chunk.py` | Splits on articles with one article of overlap; transitorios apart. Tokens estimated as chars / 3.5, ceiling 80 % of `num_ctx`. | `corpus/text/`, `prompts/stage1.txt` | `corpus/chunks/` |
| `make_schema.py` | Generates the JSON Schema: 31 GPRD names verbatim, Mexican extensions, enums. Multi-value GPRD fields are arrays here; `flatten.py` restores the `;` format. | | `schema/` |
| `silver_expand.py` | Expands hand-coded sparse records, checks schema and verbatim quotes, lists unquoted filled fields as inferred. | `silver/_sparse/` | `silver/NN.json` |
| `make_stage2.py` | Inserts the anchor into the Stage 2 template. | `silver/04.json` | `prompts/stage2.txt` |
| `extract.py` | Stage 1, batched merge, Stage 2 with `format` and up to two retries. Refuses to run if the model is not fully on the GPU. | `prompts/`, `corpus/` | `out/`, `logs/` |
| `validate.py` | Schema check, quote check, evidence coverage. Library and script. | | |
| `flatten.py` | JSON to CSV. | `out/stage2/` | `out/records.csv` |
| `evaluate.py` | Metrics against silver, excluding document 04. `--suggest` drafts the match table. | `out/`, `silver/`, `eval/episode_match.csv` | `eval/metrics.json` |
| `bootstrap_eval.py` | Bayesian bootstrap (Rubin 1981; Andrews, Moon and Shapiro 2026) of the same metrics with the document as the cluster: 95 % credible intervals, p-p distance to the naive normal, split-half check, Phase 1 sizing. Imports `evaluate.py`. | same as `evaluate.py` | `eval/intervals.json`, `eval/intervals_<date>.md`, `eval/figures/bb_metrics.png` |

## Decisions that differ from the build instruction

- `num_ctx` 16384 instead of 65536: Héctor's ruling after the fit test (`presence_penalty` 0 is added; see `extract.py`).
- Stage 1 without reasoning mode: at this context, reasoning spent 6,000 tokens on a three-page document without answering.
- Chunk summaries merge in batches, because they do not fit in one merge call at this context.
- The transitorios of document 04 split on their ordinals, because they exceed one chunk.
- Stage 2 runs once per episode, not once per document, so that a record fits in the output budget.
