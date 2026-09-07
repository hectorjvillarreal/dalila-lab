"""tablas.py — genera cuadros y figuras desde datos/*.csv, en LaTeX y en Markdown.

Regla del pacto §2.3: ninguna cifra se teclea en el cuerpo del texto y ninguna
figura es una imagen pegada. Este módulo es lo que hace exigible esa regla: los
capítulos hacen \\input de lo que sale de aquí, y si un dato cambia, el texto no
se toca.

Salida:
    latex/cuadro_XX.tex     tabular con booktabs y siunitx
    latex/figura_XX.tex     pgfplots leyendo el .csv
    markdown/cuadro_XX.md   el mismo cuadro en Markdown
"""
from __future__ import annotations
import csv, os, re

AQUI = os.path.dirname(os.path.abspath(__file__))
DATOS = os.path.join(AQUI, "datos")
TEX = os.path.join(AQUI, "capitulos", "cuadros")
MD = os.path.join(AQUI, "markdown", "cuadros")
for d in (TEX, MD):
    os.makedirs(d, exist_ok=True)


def _esc(s: str) -> str:
    """Escapa LaTeX. El acento va tal cual porque el documento usa inputenc utf8."""
    s = str(s)
    for a, b in [("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"), ("$", r"\$"),
                 ("#", r"\#"), ("_", r"\_"), ("{", r"\{"), ("}", r"\}"),
                 ("~", r"\textasciitilde{}"), ("^", r"\textasciicircum{}")]:
        s = s.replace(a, b)
    return s


def _num(v: str) -> bool:
    return bool(re.fullmatch(r"-?\d+(\.\d+)?", str(v).strip()))


def _fmt(v: str) -> str:
    """Numero -> \\num{} de siunitx, que aplica el formato espanol declarado una vez."""
    v = str(v).strip()
    if v in ("", "nan", "None"):
        return "---"
    return r"\num{" + v + "}" if _num(v) else _esc(v)


def leer(archivo: str, filtro=None, columnas=None, renombrar=None, limite=None):
    with open(os.path.join(DATOS, archivo), newline="", encoding="utf-8") as f:
        filas = list(csv.DictReader(f))
    if filtro:
        filas = [r for r in filas if filtro(r)]
    if limite:
        filas = filas[:limite]
    cols = columnas or list(filas[0].keys())
    enc = [(renombrar or {}).get(c, c) for c in cols]
    return enc, [[r.get(c, "") for c in cols] for r in filas]


def cuadro(ident: str, archivo: str, titulo: str, fuente: str, *,
           columnas=None, renombrar=None, filtro=None, limite=None,
           alineacion=None, nota: str = "") -> None:
    enc, filas = leer(archivo, filtro, columnas, renombrar, limite)
    ncol = len(enc)
    al = alineacion or ("l" + "S" * (ncol - 1))

    # ---- LaTeX
    out = [r"\begin{table}[htbp]", r"\centering",
           r"\caption{" + _esc(titulo) + "}", r"\label{tab:" + ident + "}",
           r"\small", r"\begin{tabular}{" + al + "}", r"\toprule"]
    # Los encabezados van CRUDOS: permiten $d_{t-1}$ y \%. Las celdas si se escapan.
    out.append(" & ".join("{" + str(e) + "}" for e in enc) + r" \\")
    out.append(r"\midrule")
    for fila in filas:
        # Una fila de subtitulo (primera celda con guiones) se pone en cursiva.
        if str(fila[0]).startswith("--") and not any(str(c).strip() for c in fila[1:]):
            out.append(r"\multicolumn{" + str(ncol) + r"}{l}{\itshape " +
                       _esc(str(fila[0]).strip("- ")) + r"} \\")
            continue
        out.append(" & ".join(_fmt(c) for c in fila) + r" \\")
    out += [r"\bottomrule", r"\end{tabular}"]
    pie = r"\par\vspace{2pt}\footnotesize Fuente: " + _esc(fuente) + "."
    if nota:
        pie += r" " + _esc(nota)
    out += [pie, r"\end{table}", ""]
    with open(os.path.join(TEX, f"{ident}.tex"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))

    # ---- Markdown
    limpio = [re.sub(r"\\\\[a-zA-Z]+|[$\\\\{}]", "", str(e)).strip() for e in enc]
    md = [f"**Cuadro {ident}. {titulo}**", "",
          "| " + " | ".join(limpio) + " |",
          "|" + "|".join("---" for _ in enc) + "|"]
    for fila in filas:
        if str(fila[0]).startswith("--") and not any(str(c).strip() for c in fila[1:]):
            md.append("| *" + str(fila[0]).strip("- ") + "* |" + " |" * (ncol - 1))
            continue
        md.append("| " + " | ".join("" if str(c).strip() in ("", "nan") else str(c)
                                    for c in fila) + " |")
    md += ["", f"Fuente: {fuente}." + (f" {nota}" if nota else ""), ""]
    with open(os.path.join(MD, f"{ident}.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md))


def figura(ident: str, archivo: str, titulo: str, fuente: str, *,
           x: str, series: list, xlabel: str = "", ylabel: str = "",
           tipo: str = "ybar", ancho: str = r"0.92\textwidth", nota: str = "") -> None:
    """pgfplots leyendo el .csv directamente. La grafica se vuelve verificable
    como una cifra: apunta al mismo archivo que el cuadro."""
    ruta = f"datos/{archivo}"  # relativa al directorio de compilacion, no al del capitulo
    out = [r"\begin{figure}[htbp]", r"\centering",
           r"\begin{tikzpicture}",
           r"\begin{axis}[",
           f"  width={ancho}, height=6.2cm,",
           f"  xlabel={{{_esc(xlabel)}}}, ylabel={{{_esc(ylabel)}}},",
           r"  legend style={font=\footnotesize, at={(0.5,-0.22)}, anchor=north, legend columns=-1},",
           r"  tick label style={font=\footnotesize},",
           r"  ymajorgrids=true, grid style={dashed, gray!30},",
           r"  enlarge x limits=0.08,"]
    if tipo == "ybar":
        out.append(r"  ybar, bar width=7pt,")
    out.append(r"]")
    for s in series:
        estilo = "" if tipo == "ybar" else "[mark=*, thick]"
        out.append(rf"\addplot{estilo} table [x={x}, y={s}, col sep=comma] {{{ruta}}};")
        out.append(r"\addlegendentry{" + _esc(s.replace("_", " ")) + "}")
    out += [r"\end{axis}", r"\end{tikzpicture}",
            r"\caption{" + _esc(titulo) + "}", r"\label{fig:" + ident + "}",
            r"\par\vspace{2pt}\footnotesize Fuente: " + _esc(fuente) + "." +
            (" " + _esc(nota) if nota else ""),
            r"\end{figure}", ""]
    with open(os.path.join(TEX, f"{ident}.tex"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    with open(os.path.join(MD, f"{ident}.md"), "w", encoding="utf-8") as f:
        f.write(f"**Figura {ident}. {titulo}**\n\n"
                f"*(serie generada desde `datos/{archivo}`; en la version LaTeX es una "
                f"grafica pgfplots que lee ese mismo archivo)*\n\nFuente: {fuente}.\n")
