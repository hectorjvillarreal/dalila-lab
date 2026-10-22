---
id: BUILD-20261022-SOBREMEXICO-BEAMER
title: "Build instruction — Beamer, Mesa de discusión 1, Congreso SobreMéxico 2026 (22-oct-2026) — v2, correcciones de revisión"
type: build_instruction
track: seminario / discusión pública (NO es producto RF)
version: v2
amends: BUILD-20261022-SOBREMEXICO-BEAMER v1 (2026-10-21)
derives_from: BUILD-20261013-FORO-HACENDARIO-BEAMER
added_by: Cath
endorsed_by:
date: 2026-10-21
target: Claude Code (Dalila)
deadline: PDF final hoy, 21-oct, antes de las 22:00; mesa el 22-oct a las 11:15
status: draft v2
---

# Instrucción de construcción v2: correcciones a la presentación de SobreMéxico

## 0. Contexto

La v1 de esta instrucción amplió la presentación del 13 de octubre a 9 láminas. Claude Code construyó el PDF (`GrandPlan/RF/foros_talleres/SobreMexico_2026-10-22/`, commit b4f473d) y publicó una página de revisión. Esta v2 registra las dos rondas de revisión posteriores y ordena aplicarlas.

Todo lo demás de la v1 sigue vigente: límites de vocabulario, cifras verificadas, metadatos, verificación y retención.

## 1. Bitácora de revisión

**Ronda 1 (Cath, sobre la página de revisión de Claude Code):**

| Lámina | Hallazgo | Corrección |
|---|---|---|
| 2 | La etiqueta de la segunda barra, "Gasto neto total (ingresos LIF con financiamiento)", es confusa. | Cambiar a "Gasto neto total, PPEF 2027". El total del PEF iguala por identidad al de la LIF. |
| 8 | La línea "Gasto en pensiones 2027: 6.3 % del PIB" repite el 6.3 de pensiones de la cascada (lámina 3, cierre 2026). En la lámina que dice que la Bolsa se encoge, la única cifra sugiere que las pensiones no crecen. | Sustituir por la compresión ya observada: "Ya ocurre: la inversión pública pasó de 3.9 % (2025) a 2.9 % del PIB (2027)." Ajustar la fuente del pie. |
| 9 | "…y pasivos contingentes fuera del presupuesto corriente" se lee como propuesta de mantenerlos fuera. | "Pemex y CFE: reglas claras para los apoyos fiscales y registro transparente de los pasivos contingentes que hoy quedan fuera del presupuesto." |

Puntos que Claude Code dejó para visto bueno, resueltos:

- **Brecha de ≈ 1.5 billones (lámina 2): aprobada.** Es el cierre devengado, 10.64 − 9.16 = 1.48; incluye 0.12 de Adefas y neta el superávit de organismos y empresas. En caja serían unos 1.36.
- **"Impuesto mínimo de alrededor de 1 %" (lámina 6): aprobado.** El tope de 96.67 % deja una base de 3.33 % de los ingresos; a 30 % da 1 %.
- **Diagrama en la lámina 8: aprobado,** con la corrección anterior.
- **Costo financiero de 3.8 (lámina 3, 2026) frente a 4.0 (lámina 5, 2027): se mantiene.** El aumento refuerza el argumento y la nueva lámina 5 lo hace explícito.

Estado: las correcciones de las láminas 8 y 9 ya están en el `.tex` que Héctor tiene; la de la lámina 2 está en la gráfica `fig/l2_ingresos_gasto_lif2027.pdf` y debe verificarse.

**Ronda 2 (Héctor):** la lámina 5 "está muy rara". Tres barras de conceptos y años distintos en una sola gráfica no se leen bien. Se rehace como igualdad tipográfica (sección 2).

## 2. Lámina 5 nueva

- Título: *La deuda ya cuesta tanto como el margen de decisión.*
- Dos cajas, mismo estilo que la lámina 4, unidas por un signo de igual:
  - Izquierda: Bolsa, margen de decisión, 4.0 % del PIB, actualización 2026.
  - Derecha: intereses de la deuda, 4.0 % del PIB, PPEF 2027, con "(3.8 en 2026)".
- Mensaje: *Por cada peso que queda para decidir, otro peso se va en intereses.*
- Se elimina la barra de inversión pública, que ya está en las láminas 4 y 8.
- `fig/l5_deuda_bolsa_2027.pdf` deja de usarse. No la borres; queda como provenance.

El preámbulo requiere añadir `calc`: `\usetikzlibrary{positioning,arrows.meta,calc}`.

Código del frame, ya compilado y verificado por Cath:

```latex
% ---------- 5. La deuda ya cuesta tanto como la Bolsa ----------
\begin{frame}{La deuda ya cuesta tanto como el margen de decisión}
  \centering
  \vspace{0.2em}
  \begin{tikzpicture}
    \node[draw=petroleo, line width=1.5pt, fill=fondo, rounded corners=4pt,
          minimum width=5.6cm, minimum height=3.4cm, align=center, text=gris] (b) {
      {\small Bolsa: margen de decisión}\\[0.3em]
      {\color{petroleo}\bfseries\fontsize{30}{34}\selectfont 4.0\,\%}\\[0.2em]
      {\small del PIB}\\[0.5em]
      {\footnotesize\color{grisclaro} Actualización 2026}};
    \node[draw=gris, line width=1.5pt, fill=white, rounded corners=4pt,
          minimum width=5.6cm, minimum height=3.4cm, align=center, text=gris,
          right=1.6cm of b] (d) {
      {\small Intereses de la deuda}\\[0.3em]
      {\color{gris}\bfseries\fontsize{30}{34}\selectfont 4.0\,\%}\\[0.2em]
      {\small del PIB}\\[0.5em]
      {\footnotesize\color{grisclaro} PPEF 2027 \;(3.8 en 2026)}};
    \node[font=\bfseries\fontsize{30}{34}\selectfont, text=petroleo] at ($(b.east)!0.5!(d.west)$) {=};
  \end{tikzpicture}\par
  \vspace{0.7em}
  {\large Por cada peso que queda para decidir, otro peso se va en intereses.\par}
  \fuente{\raggedright Bolsa y costo financiero 2026: actualización 2026, elaboración propia con datos de SHCP. Costo financiero 2027: PPEF 2027; fuente: CIEP con datos de SHCP. Razones con el PIB de SHCP; con un PIB más conservador serían algo mayores.\par}
\end{frame}
```

Nota de denominador (para Héctor, no para la lámina): el 4.0 de la Bolsa usa el PIB conservador de 2026 (36,500 mmdp) y el 4.0 de los intereses usa el PIB de SHCP para 2027. Con el mismo denominador conservador, los intereses de 2027 serían algo más de 4. La igualdad es generosa con la deuda, no con el argumento.

## 3. Qué hacer

1. Sustituir el `.tex` del repositorio por la versión de Héctor (`Villarreal_SobreMexico_2026-10-22.tex`, que ya incluye las rondas 1 y 2, salvo la lámina 2). Si no la tienes, aplica tú las correcciones de la sección 1 y el frame de la sección 2.
2. Lámina 2: verificar que la etiqueta de la segunda barra diga "Gasto neto total, PPEF 2027"; si no, regenerar `fig/l2_ingresos_gasto_lif2027.pdf`.
3. Recompilar dos veces sin errores. Confirmar 9 páginas.
4. Metadatos con `pikepdf` como en la v1.
5. Revisión visual con `pdftoppm -r 150` de las láminas 2, 5, 8 y 9; nada desbordado.
6. `pdftotext` y búsqueda de vocabulario interno, "Naranja", "Pensando en México", "13 de octubre" y "Villareal": todo vacío.
7. Commit con mensaje que cite esta instrucción (`BUILD-20261022-SOBREMEXICO-BEAMER v2`).
8. Republicar la página de revisión con las láminas nuevas y sin la sección de puntos pendientes.

## 4. Retención

Archivar esta v2 en `_crossrefs/_build_instructions/` junto a la v1 y a la instrucción del 13 de octubre, conforme a PROTO-RAG-001. No sobrescribir la v1: la cadena 13-oct → v1 → v2 es la provenance completa. `endorsed_by` queda vacío hasta revisión.
