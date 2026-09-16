#!/usr/bin/env bash
# Compila en Dalila, no en Overleaf. Dos pasadas de pdflatex; sin shell-escape.
set -u
export PATH="$HOME/.TinyTeX/bin/x86_64-linux:$PATH"
cd "$(dirname "$0")"
mkdir -p _entrega _build
echo "== comprobación estática =="
"${PYTHON:-python3}" validar_latex.py || { echo "ABORTA: la comprobación estática falló"; exit 1; }
echo; echo "== pdflatex, pasada 1 =="
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=_build main.tex >/dev/null 2>&1
r1=$?
echo "== pdflatex, pasada 2 =="
pdflatex -interaction=nonstopmode -output-directory=_build main.tex >/dev/null 2>&1
if [ -f _build/main.pdf ]; then
  cp _build/main.pdf _entrega/documento_2027.pdf
  echo "PDF: $(du -h _entrega/documento_2027.pdf | cut -f1), $(pdfinfo _entrega/documento_2027.pdf | awk '/^Pages/{print $2}') páginas"
else
  echo "NO SE PRODUJO PDF (pasada 1 salió con $r1)"
fi
echo; echo "== warnings =="
grep -E "^(LaTeX|Package|Class) (Warning|Error)|Overfull|Underfull" _build/main.log 2>/dev/null \
  | sed 's/^/  /' | sort | uniq -c | sort -rn | head -20
echo "  (total de líneas de warning: $(grep -cE "Warning|Overfull|Underfull" _build/main.log 2>/dev/null))"
