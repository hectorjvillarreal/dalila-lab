"""Genera cuadros LaTeX desde los CSV de datos/. Los números se formatean AQUÍ,
en español, porque siunitx está prohibido (pacto §11.4)."""
from pathlib import Path
import pandas as pd

DATOS = Path(__file__).resolve().parent / "datos"
SALIDA = Path(__file__).resolve().parent / "capitulos" / "cuadros"
SALIDA.mkdir(parents=True, exist_ok=True)


def num(v, dec=1):
    if v is None or (isinstance(v, float) and pd.isna(v)) or v == "":
        return "---"
    if isinstance(v, str):
        return v.replace("_", "\\_").replace("%", "\\%").replace("&", "\\&")
    s = f"{v:,.{dec}f}"
    return s.replace(",", " ").replace(".", ",")


def esc(t):
    return (str(t).replace("\\", "").replace("&", "\\&").replace("%", "\\%")
            .replace("_", "\\_").replace("#", "\\#").replace("$", "\\$"))


def cuadro(idc, titulo, df, cols, encabezados, decs=None, nota="", align=None, ancho=None):
    """df: DataFrame; cols: columnas a imprimir; decs: decimales por columna."""
    decs = decs or [1] * len(cols)
    align = align or ("l" + "r" * (len(cols) - 1))
    lineas = [f"% cuadro {idc}", "\\begin{table}[htbp]", "\\centering",
              "\\scriptsize",
              f"\\caption{{{esc(titulo)}}}", f"\\label{{cua:{idc}}}",
              f"\\begin{{tabular}}{{{align}}}", "\\toprule",
              " & ".join(f"\\textbf{{{esc(h)}}}" for h in encabezados) + " \\\\", "\\midrule"]
    for _, r in df.iterrows():
        celdas = []
        for c, d in zip(cols, decs):
            v = r[c] if c in r else ""
            celdas.append(num(v, d) if not isinstance(v, str) else esc(v))
        fila = " & ".join(celdas)
        if str(r[cols[0]]).strip().upper().startswith(("TOTAL", "PERIMETRO", "PERÍMETRO")):
            lineas.append("\\midrule")
            fila = " & ".join(f"\\textbf{{{c}}}" for c in celdas)
        lineas.append(fila + " \\\\")
    lineas += ["\\bottomrule", "\\end{tabular}"]
    if nota:
        lineas.append(f"\\\\[2pt]\\begin{{minipage}}{{0.92\\textwidth}}\\scriptsize {esc(nota)}"
                      "\\end{minipage}")
    lineas += ["\\end{table}", ""]
    (SALIDA / f"{idc}.tex").write_text("\n".join(lineas), encoding="utf-8")
    return idc


def leer(n):
    return pd.read_csv(DATOS / n)
