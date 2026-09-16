#!/usr/bin/env python3
"""Comprobación estática del proyecto LaTeX, antes de compilar.

Cubre: llaves y entornos balanceados; que todo \input apunte a un archivo existente
RESUELTO DESDE EL DIRECTORIO DEL ARCHIVO MAESTRO; que todo \ref tenga su \label; que los
paquetes estén en la lista permitida; que nada exija shell-escape.

Y DEBE IMPRIMIR QUÉ NO COMPRUEBA.
"""
import re, sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
MAESTRO = RAIZ / "main.tex"
PERMITIDOS = {"fontenc","inputenc","lmodern","babel","geometry","fancyhdr","booktabs",
              "graphicx","caption","longtable","array","pgfplots","hyperref"}
PROHIBIDOS = {"siunitx","minted","fontspec","unicode-math","tikz-external"}

errores, avisos = [], []

def archivos():
    vistos, cola = [], [MAESTRO]
    while cola:
        f = cola.pop(0)
        if f in vistos or not f.exists():
            continue
        vistos.append(f)
        for m in re.finditer(r"\\input\{([^}]+)\}", f.read_text(encoding="utf-8")):
            ruta = m.group(1)
            cand = RAIZ / (ruta if ruta.endswith(".tex") else ruta + ".tex")
            cola.append(cand)
    return vistos

# 1. inputs resueltos desde el maestro
todos = set()
for f in archivos():
    txt = f.read_text(encoding="utf-8")
    for m in re.finditer(r"\\input\{([^}]+)\}", txt):
        ruta = m.group(1)
        cand = RAIZ / (ruta if ruta.endswith(".tex") else ruta + ".tex")
        todos.add(str(cand))
        if not cand.exists():
            errores.append(f"\\input no resuelve desde el maestro: {ruta}  (en {f.name})")

leidos = archivos()
print(f"[1] Inclusiones: {len(todos)} \\input, {len(leidos)} archivos alcanzados desde main.tex")

# 2. balanceo
for f in leidos:
    txt = f.read_text(encoding="utf-8")
    sin = re.sub(r"(?<!\\)%.*", "", txt)
    ab = len(re.findall(r"(?<!\\)\{", sin)); ce = len(re.findall(r"(?<!\\)\}", sin))
    if ab != ce:
        errores.append(f"llaves desbalanceadas en {f.name}: {ab} abren, {ce} cierran")
    for ent in set(re.findall(r"\\begin\{([a-zA-Z*]+)\}", sin)):
        b = len(re.findall(r"\\begin\{" + re.escape(ent) + r"\}", sin))
        e = len(re.findall(r"\\end\{" + re.escape(ent) + r"\}", sin))
        if b != e:
            errores.append(f"entorno «{ent}» desbalanceado en {f.name}: {b} begin, {e} end")
print(f"[2] Balanceo de llaves y entornos: {len(leidos)} archivos revisados")

# 3. ref/label
labels, refs = set(), []
for f in leidos:
    txt = f.read_text(encoding="utf-8")
    labels |= set(re.findall(r"\\label\{([^}]+)\}", txt))
    refs += [(r, f.name) for r in re.findall(r"\\(?:ref|autoref|pageref)\{([^}]+)\}", txt)]
for r, fn in refs:
    if r not in labels:
        errores.append(f"\\ref sin \\label: {r} (en {fn})")
print(f"[3] Referencias cruzadas: {len(refs)} \\ref contra {len(labels)} \\label")

# 4. paquetes
usados = set()
for m in re.finditer(r"\\usepackage(?:\[[^\]]*\])?\{([^}]+)\}", MAESTRO.read_text(encoding="utf-8")):
    usados |= {p.strip() for p in m.group(1).split(",")}
for p in usados - PERMITIDOS:
    errores.append(f"paquete fuera de la lista permitida: {p}")
for p in usados & PROHIBIDOS:
    errores.append(f"PAQUETE PROHIBIDO por el pacto §11.4: {p}")
print(f"[4] Paquetes: {len(usados)} declarados, todos en la lista permitida"
      if not (usados - PERMITIDOS) else f"[4] Paquetes: {sorted(usados)}")

# 5. shell-escape
for f in leidos:
    if re.search(r"\\write18|shellesc|--shell-escape", f.read_text(encoding="utf-8")):
        errores.append(f"exige shell-escape: {f.name}")
print("[5] shell-escape: no se encontró ninguna construcción que lo exija"
      if not any("shell" in e for e in errores) else "[5] shell-escape: PROBLEMA")

# 6. cuadros generados contra cuadros incluidos
incl = {Path(p).stem for p in todos if "/cuadros/" in p}
gen = {p.stem for p in (RAIZ / "capitulos" / "cuadros").glob("*.tex")}
if incl - gen:
    errores.append(f"cuadros incluidos y no generados: {sorted(incl - gen)}")
if gen - incl:
    avisos.append(f"cuadros generados y no incluidos: {sorted(gen - incl)}")
print(f"[6] Cuadros: {len(incl)} incluidos, {len(gen)} generados")

print("\nLO QUE ESTA COMPROBACIÓN NO REVISA:")
for x in ("que las columnas que pide una gráfica existan en su archivo de datos "
          "(este documento no usa pgfplots con archivos externos)",
          "que las cifras del texto coincidan con las de los cuadros: eso es "
          "consistencia interna y se verifica a mano",
          "desbordes de caja, viudas y huérfanas, ni ningún problema de composición",
          "que los caracteres acentuados estén bien codificados en el PDF final",
          "errores de LaTeX que solo aparecen al compilar"):
    print(f"  - {x}")

print()
for a in avisos:
    print(f"AVISO:  {a}")
for e in errores:
    print(f"ERROR:  {e}")
print(f"\nRESULTADO: {len(errores)} errores, {len(avisos)} avisos")
sys.exit(1 if errores else 0)
