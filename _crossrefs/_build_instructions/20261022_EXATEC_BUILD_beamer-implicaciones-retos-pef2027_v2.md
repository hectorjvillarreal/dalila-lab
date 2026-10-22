---
id: BUILD-20261022-EXATEC-BEAMER
title: "Build instruction — Beamer, 3er Encuentro EXATEC (22-oct-2026) — v2, correcciones de revisión"
type: build_instruction
track: seminario / discusión pública (NO es producto RF)
version: v2
amends: BUILD-20261022-EXATEC-BEAMER v1 (2026-10-21)
derives_from: BUILD-20261022-SOBREMEXICO-BEAMER v2
added_by: Cath
endorsed_by:
date: 2026-10-21
target: Claude Code (Dalila)
deadline: 22-oct, antes de las 14:00; conferencia a las 18:40
status: draft v2
---

# Instrucción de construcción v2: correcciones a la presentación EXATEC

## 0. Contexto

La v1 produjo un PDF de 15 láminas (`GrandPlan/RF/foros_talleres/EXATEC_2026-10-22/`, commit 3d7ceb6) y una página de revisión. Esta v2 registra la revisión de Cath y ordena dos cambios. Todo lo demás de la v1 sigue vigente.

## 1. Bitácora de revisión

Decisiones de armado de Claude Code, resueltas:

| # | Decisión | Resolución |
|---|---|---|
| 1 | Lámina 10: "usa el crédito" en lugar de "recupera el crédito" | Aprobada: es fiel a la fuente. |
| 2 | Lámina 14: cuatro cajas, con la deuda de CFE separada | Aprobada, con cambio de título (sección 2). |
| 3 | Lámina 13: cuerpo un punto más chico | Aprobada. |
| 4 | Lámina 15: tres barras con perímetros distintos | Se rehace (sección 2). El riesgo es el mismo que llevó a rehacer la lámina 5 de SobreMéxico. |

Cifras opcionales: se aprueban el uso del 1.3 % de Pakistán (Best et al., 2015) y del 0.7 % de apoyos a Pemex, así como la omisión de gastos fiscales y predial. No se usa el 1.7 % del PIB de las exenciones de IVA: es solo una parte y se leería como el total.

Láminas 1–13 sin cambios.

## 2. Cambios

**Lámina 14**

- Título: *Empresas del Estado: un costo repartido y fuera de la vista.* El título actual dice "Pemex", pero la lámina también incluye a CFE.
- Caja "Apoyos del presupuesto": "Apoyos a Pemex: 0.7 % del PIB, lo mismo que entra por transferencias del FMP: la renta petrolera regresa a Pemex (actualización 2026)."
  Motivo: la nota de la lámina 3 dice que ambos montos se compensan. Sin esta aclaración alguien puede ver una contradicción; con ella, la compensación se vuelve el argumento.
- Caja "Pasivos contingentes": "No aparecen en el presupuesto ni en los techos de deuda."

**Lámina 15**

- Título: *El techo de deuda no ancla: la LIF autoriza casi un punto más de lo programado.*
- Gráfica de **dos** barras horizontales, mismo perímetro (Gobierno Federal) y misma fuente (LIF 2027), en % del PIB:
  1. Techo autorizado (LIF 2027, art. 2o): 4.9
  2. Endeudamiento programado (LIF 2027, art. 1o): 4.0
- Bajo la gráfica, en texto normal: "Meta de RFSP del sector público: 3.9 % del PIB (CGPE 2027)."
- Pie: "Fuente: LIF 2027, arts. 1o y 2o, dictamen de la Cámara de Diputados; SHCP, CGPE 2027. % del PIB con el PIB de SHCP." Se elimina la advertencia de perímetros, que ya no hace falta.
- Banda de cierre sin cambios.

Motivo del cambio de título: lo que la lámina demuestra es la holgura del techo de endeudamiento, no el funcionamiento de toda la regla fiscal (que se fija en la meta de balance). Decir "la regla fiscal no ancla" es más de lo que la gráfica sostiene.

## 3. Qué hacer

1. Aplicar los cambios de la sección 2.
2. Recompilar dos veces; confirmar 15 páginas; metadatos con `pikepdf`.
3. Revisión visual de las láminas 14 y 15. Repetir la búsqueda de términos de la v1 (sección 5.3).
4. Commit citando `BUILD-20261022-EXATEC-BEAMER v2`.
5. Republicar la página de revisión, sin las secciones de decisiones pendientes.

## 4. Retención

Archivar junto a la v1 en `_crossrefs/_build_instructions/`, sin sobrescribirla. `endorsed_by` queda vacío hasta revisión.
