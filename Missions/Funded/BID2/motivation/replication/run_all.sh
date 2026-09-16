#!/usr/bin/env bash
# run_all.sh — regenerates fig07_composition.pdf/.png from data/ into output/.
# Works from any working directory; requires only R (>= 4.4) with data.table
# and ggplot2 on the PATH as `Rscript`. Makes no network calls.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Fixed locale so decimal formatting cannot vary with the host machine.
export LC_ALL=C.UTF-8

command -v Rscript >/dev/null 2>&1 || {
  echo "ERROR: Rscript not found on PATH. See environment/environment.yml." >&2
  exit 1
}

Rscript "$HERE/code/make_fig07_composition.R"

for f in fig07_composition.pdf fig07_composition.png; do
  [ -s "$HERE/output/$f" ] || { echo "ERROR: $f was not produced." >&2; exit 1; }
done
echo "OK: output/fig07_composition.pdf and .png regenerated."
