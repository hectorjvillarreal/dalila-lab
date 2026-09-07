"""validar_latex.py — comprobación estática del proyecto LaTeX.

NO SUSTITUYE A LA COMPILACIÓN, pero ya no es lo único que hay: desde el
2026-09-07 Dalila tiene TinyTeX en ~/.TinyTeX y `compilar.sh` hace la compilación
de verdad. Este script sigue siendo útil porque es instantáneo y porque atrapa
cosas que la compilación no señala como error, y se corre antes de compilar.

Comprueba: llaves balanceadas, entornos abiertos y cerrados, que todo \\input
apunte a un archivo que existe, que todo \\ref tenga su \\label, que los paquetes
usados estén en la lista permitida, que no haya comandos que exijan shell-escape,
y que las columnas que pgfplots pide existan en el .csv que lee.
"""
import os, re, sys, csv

AQUI = os.path.dirname(os.path.abspath(__file__))
CAPS = os.path.join(AQUI, "capitulos")
DATOS = os.path.join(AQUI, "datos")
MAIN = os.path.join(AQUI, "main.tex")

PERMITIDOS = {"inputenc", "fontenc", "babel", "geometry", "booktabs", "longtable", "array", "lmodern",
              "graphicx", "caption", "fancyhdr", "pgfplots", "siunitx", "hyperref"}
PROHIBIDOS = {"minted", "shellesc", "svg", "epstopdf"}

problemas, avisos, comprobaciones = [], [], 0


def archivos():
    yield MAIN
    for n in sorted(os.listdir(CAPS)):
        if n.endswith(".tex"):
            yield os.path.join(CAPS, n)
    sub = os.path.join(CAPS, "cuadros")
    for n in sorted(os.listdir(sub)):
        if n.endswith(".tex"):
            yield os.path.join(sub, n)


def sin_comentarios(t):
    return "\n".join(re.sub(r"(?<!\\)%.*$", "", l) for l in t.split("\n"))


# ------------------------------------------------------ llaves y entornos ---
for ruta in archivos():
    comprobaciones += 1
    t = sin_comentarios(open(ruta, encoding="utf-8").read())
    limpio = re.sub(r"\\[{}]", "", t)
    if limpio.count("{") != limpio.count("}"):
        problemas.append(f"llaves desbalanceadas en {os.path.relpath(ruta, AQUI)}: "
                         f"{limpio.count('{')} abren, {limpio.count('}')} cierran")
    pila = []
    for m in re.finditer(r"\\(begin|end)\{([a-zA-Z*]+)\}", t):
        if m.group(1) == "begin":
            pila.append(m.group(2))
        else:
            if not pila:
                problemas.append(f"\\end{{{m.group(2)}}} sin apertura en "
                                 f"{os.path.relpath(ruta, AQUI)}")
            elif pila[-1] != m.group(2):
                problemas.append(f"entorno mal anidado en {os.path.relpath(ruta, AQUI)}: "
                                 f"abre {pila[-1]}, cierra {m.group(2)}")
                pila.pop()
            else:
                pila.pop()
    if pila:
        problemas.append(f"entornos sin cerrar en {os.path.relpath(ruta, AQUI)}: {pila}")

# ------------------------------------------------------------------ input ---
texto_todo = "\n".join(sin_comentarios(open(r, encoding="utf-8").read()) for r in archivos())
for m in re.finditer(r"\\input\{([^}]+)\}", texto_todo):
    comprobaciones += 1
    destino = os.path.join(AQUI, m.group(1) + ".tex")
    if not os.path.exists(destino):
        problemas.append(f"\\input a un archivo que no existe: {m.group(1)}.tex")

# --------------------------------------------------------- label y ref ---
labels = set(re.findall(r"\\label\{([^}]+)\}", texto_todo))
for m in re.finditer(r"\\ref\{([^}]+)\}", texto_todo):
    comprobaciones += 1
    if m.group(1) not in labels:
        problemas.append(f"\\ref{{{m.group(1)}}} sin \\label correspondiente")

# ------------------------------------------------------------- paquetes ---
usados = set()
for m in re.finditer(r"\\usepackage(?:\[[^\]]*\])?\{([^}]+)\}", texto_todo):
    usados |= {p.strip() for p in m.group(1).split(",")}
comprobaciones += 1
fuera = usados - PERMITIDOS
if fuera:
    problemas.append(f"paquetes fuera de la lista permitida: {sorted(fuera)}")
mal = usados & PROHIBIDOS
if mal:
    problemas.append(f"paquetes prohibidos (exigen shell-escape o instalacion): {sorted(mal)}")

comprobaciones += 1
if re.search(r"\\write18|shell-?escape", texto_todo):
    problemas.append("el proyecto invoca shell-escape, que esta prohibido")

# --------------------------------------- columnas que pgfplots pide del csv ---
for m in re.finditer(r"table\s*\[([^\]]*)\]\s*\{([^}]+)\}", texto_todo):
    comprobaciones += 1
    opts, ruta_csv = m.group(1), m.group(2)
    base = os.path.basename(ruta_csv)
    p = os.path.join(DATOS, base)
    if not os.path.exists(p):
        problemas.append(f"pgfplots lee un csv que no existe: {base}")
        continue
    with open(p, encoding="utf-8") as f:
        cols = next(csv.reader(f))
    for c in re.findall(r"\b[xy]\s*=\s*([A-Za-z0-9_]+)", opts):
        if c not in cols:
            problemas.append(f"pgfplots pide la columna '{c}' que no esta en {base}")

# ---------------------------------------------------- capitulos del main ---
for m in re.finditer(r"\\input\{capitulos/([a-z0-9_]+)\}", sin_comentarios(open(MAIN, encoding="utf-8").read())):
    comprobaciones += 1
    if not os.path.exists(os.path.join(CAPS, m.group(1) + ".tex")):
        problemas.append(f"main.tex llama a un capitulo que no existe: {m.group(1)}")

# --------------------------------------------------------------- resumen ---
print(f"{comprobaciones} comprobaciones estáticas")
if problemas:
    print(f"\n{len(problemas)} PROBLEMAS:")
    for p_ in problemas:
        print("   " + p_)
else:
    print("Sin problemas estáticos.")
print("\nLO QUE ESTO NO COMPRUEBA: corre `sh compilar.sh`, que sí compila.")
print("   - desbordes de caja, que solo aparecen al componer")
print("   - la colocacion de flotantes y la paginacion")
print("   - si una figura quedo ilegible por escala, que ningun log reporta")
sys.exit(1 if problemas else 0)
