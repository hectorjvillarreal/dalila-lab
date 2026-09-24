#!/usr/bin/env bash
# Rebuild the nota from committed inputs: scenarios -> fiscal -> figures -> numbers -> PDF.
# Step 0 (00_prepare_inputs.py) needs data/raw/ and is run only when inputs change.
set -euo pipefail
cd "$(dirname "$0")"
source ~/miniforge3/etc/profile.d/conda.sh && conda activate dalila
python scripts/01_scenarios.py > build/01_scenarios.log
python scripts/03_fiscal.py > build/03_fiscal.log
python scripts/02_figures.py
python scripts/04_numbers.py
export PATH="$HOME/.TinyTeX/bin/x86_64-linux:$PATH"
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build nota_EIC2025_v0.2.tex > build/latex.log 2>&1 || { tail -40 build/latex.log; exit 1; }
cp build/nota_EIC2025_v0.2.pdf nota_EIC2025_v0.2.pdf
echo "pages: $(pdfinfo nota_EIC2025_v0.2.pdf 2>/dev/null | awk '/^Pages/{print $2}')"
