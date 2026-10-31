# MX-SSRD pilot, Phase 0

Reproduces the two-stage extraction of IMF WP/26/236 on Mexican primary legal texts with a local Qwen model, and scores it against a reference set coded separately. The task is defined in `20261031_RF_BUILD_mx-ssrd-pilot_v1.md`; the result is `eval/report_20261031.md`.

## Rerun

```bash
cd ~/Dalila/GrandPlan/RF/narrative/mx_ssrd_pilot
PY=~/miniforge3/envs/dalila/bin/python
$PY -I src/extract.py --all          # Stage 1 and Stage 2, reuses finished steps; --force redoes them
$PY -I src/flatten.py                # out/records.csv
$PY -I src/evaluate.py               # eval/metrics.json, needs eval/episode_match.csv
```

The full run takes about an hour: run it inside Zellij. `extract.py` calls only `localhost:11434` and stops if the model is not fully on the GPU.

Rebuilding from the raw files: `src/to_text.py`, `src/chunk.py`, `src/make_schema.py`, `src/silver_expand.py`, `src/make_stage2.py`, in that order. See `src/README.md`.

## Layout

| Path | Contents |
|---|---|
| `manifest.yaml` | Corpus list with hashes, URLs and dates |
| `corpus/raw/` | Original files, read-only, untrusted |
| `corpus/text/`, `corpus/chunks/` | UTF-8 text and chunks |
| `schema/`, `prompts/` | JSON Schema and prompts; `stage2.txt` is generated from its template |
| `out/` | Stage 1 summaries, Stage 2 records, `records.csv` |
| `silver/` | Reference coding, never fed to Qwen except the anchor |
| `eval/` | Match table, metrics, report; `prompt_v1/` keeps the first aborted run |
| `logs/` | Model digest, parameters, prompt hashes, timings |
