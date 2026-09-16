#!/bin/sh
# Compila el documento. Tres pasadas: índice, referencias cruzadas y longtables.
#
# Requiere una instalación de TeX. En Dalila se usa TinyTeX, instalada en
# ~/.TinyTeX, que es de usuario y no toca el sistema:
#   curl -sL https://yihui.org/tinytex/install-bin-unix.sh | sh
#   tlmgr install booktabs geometry fancyhdr caption pgfplots siunitx \
#                 hyperref babel-spanish xcolor etoolbox pgf array lmodern
#
# Uso:  sh compilar.sh   (desde documento_2025/)
set -e
AQUI=$(cd "$(dirname "$0")" && pwd)
export PATH="$HOME/.TinyTeX/bin/x86_64-linux:$PATH"
command -v pdflatex >/dev/null || { echo "no hay pdflatex en el PATH"; exit 1; }

echo "1. regenerando datos y cuadros desde los .csv"
python "$AQUI/generar_cuadros.py" >/dev/null
echo "2. comprobaciones estáticas"
python "$AQUI/validar_latex.py" | head -2
echo "3. cierre contable de los datos"
python "$AQUI/verificar.py" | tail -1

B=$(mktemp -d)
cp -r "$AQUI/main.tex" "$AQUI/capitulos" "$AQUI/datos" "$B/"
cd "$B"
echo "4. compilando, tres pasadas"
for i in 1 2 3; do pdflatex -interaction=nonstopmode main.tex > "pase$i.log" 2>&1; done

echo
grep -c "^!" pase3.log > /dev/null 2>&1 && true
python - <<'PY'
import re
t = open("pase3.log", encoding="utf-8", errors="replace").read()
o = [float(x) for x in re.findall(r"Overfull .hbox \(([0-9.]+)pt too wide\)", t)]
print("   errores:", len(re.findall(r"(?m)^!", t)))
print("   overfull:", len(o), "| mayor:", round(max(o), 1) if o else 0, "pt")
m = re.search(r"Output written on main.pdf \([^)]*\)", t)
print("  ", m.group(0) if m else "SIN PDF")
PY
mkdir -p "$AQUI/_entrega"
cp main.pdf "$AQUI/_entrega/Implicaciones_PE2025_ITED.pdf"
echo "   pdf en _entrega/Implicaciones_PE2025_ITED.pdf"
