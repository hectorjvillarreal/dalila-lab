# Helper scripts — Layer A portability assessment

All scripts are read-only on `source/` and take the source root as an argument. Run them
with `python3 -I` from `capa_A_evaluacion/` (never from inside `source/`).

| Script | Produces | Notes |
|---|---|---|
| `manifest.py <root> <manifest.csv> <inventory.csv>` | `report/manifest.csv` (relpath, size, SHA-256, ext for all 2,542 files) and `report/inventory.csv` (counts and bytes by extension) | Fixes the exact version assessed. |
| `loc.py <root> <loc.csv>` | `report/loc.csv` (total / non-blank / code lines per `.do`/`.ado`) | Code lines exclude `*`, `//` and `/* */` comments. |
| `callgraph.py <root> <edges.csv>` | `report/callgraph_edges.csv` (caller, line, kind, target) | Kinds: `do`/`run`/`include` and `cmd` (call to a program defined in a shipped `.ado` or `program define`). |
| `grep_io.sh <root>` | `report/io_grep.txt` | `version` statements, inputs (`use`, `import`, `merge using`, …), outputs (`save`, `export`, `file write`, …), paths, shell/python/mata escapes, `net install`. |
| `hazards.py <root> <hazard_counts.csv>` | `report/hazard_counts.csv` (construct, occurrences, files, examples) | Regex counts over code lines; see the hazard map in the report for interpretation. Counts are approximate (regex), examples give exact lines. |

Reproduce everything:

```bash
cd FISCUS/capa_A_evaluacion
python3 -I scripts/manifest.py source/SimuladorCIEP-master report/manifest.csv report/inventory.csv
python3 -I scripts/loc.py      source/SimuladorCIEP-master report/loc.csv
python3 -I scripts/callgraph.py source/SimuladorCIEP-master report/callgraph_edges.csv
bash scripts/grep_io.sh source/SimuladorCIEP-master > report/io_grep.txt
python3 -I scripts/hazards.py  source/SimuladorCIEP-master report/hazard_counts.csv
```
