---
id: 20261018_BDH_N13_anexo-afiliacion-subsidiada_build_v1.3
title: "Instrucciones de construcción — Anexo preliminar: afiliación subsidiada al SEM (v1.3: borrador con el denominador común)"
type: build_instruction
build_type: retrofit
project: BDH
mission: IMSS — Núcleo 13 (Sostenibilidad financiera de la atención quirúrgica)
version: v1.3
supersedes: 20261017_BDH_N13_anexo-afiliacion-subsidiada_build_v1.2   # solo el borrador; modelo y cifras en mdp sin cambio
date: 2026-10-18
language: es
corpus_affected:
  - Missions/Funded/IMSS_Surgical/e_1_imss_subsidiado/anexo_afiliacion_subsidiada/
triggered_by:
  - "Experimento 2 v1.1 (commit 7a3b4ce): migración del experimento 1 al denominador común y a los ingresos del SEM del Cuadro V.13; 186 cifras cambian (tablas/exp1_cambios_denominador.csv)"
  - "Decisión de Beth, 18-10-2026: actualizar ya el borrador del experimento 1, solo en cifras"
agents_involved: [Beth, Cath, Claude Code]
added_by: Beth
endorsed_by: []          # revisión pendiente: Cath (consistencia de cifras)
protocol: PROTO-RAG-001
status: executed
executed: 2026-10-18   # Claude Code; ANEXO_borrador_v3.md (112 cifras cambian de texto), trazabilidad outputs/tables/exp1_borrador_v2_a_v3.csv; verificaciones 3.1-3.5 cumplidas; ninguna oración [REVISAR]
executor: Claude Code (Dalila)
---

# v1.3 — Borrador del experimento 1 con el denominador común

## 0. Alcance

**Solo cambian cifras del borrador.** No cambian el modelo, la configuración base (D2 · G2 · S1 · U1 · τ=0.50 · ρ=0.75 · μ=1.10 · C1 · F0 · π_m=0 · perfil 3.0 · 337 días), los montos en mdp ni la redacción. La redacción general queda para una pasada posterior.

**Insumo:** `tablas/exp1_cambios_denominador.csv` generado por la corrida del experimento 2 v1.1 (commit 7a3b4ce, rama p4-revision-final). Si el experimento 1 vive en otra rama, traer solo ese archivo y las salidas recalculadas; no fusionar otros cambios.

---

## 1. Borrador v3

1. Partir de `ANEXO_borrador_v2.md` y guardar como `ANEXO_borrador_v3.md`. La v2 se conserva.
2. Sustituir cada cifra en puntos del salario y en % de los ingresos del SEM por su valor nuevo. Ejemplo: en 2030, «1.36 puntos del SBC y 13.2 % de los ingresos del SEM» pasa a los valores nuevos de la tabla (saldo total −1.305 puntos y −12.93 %, con el redondeo que use el borrador).
3. Mantener el redondeo y el formato de cada cifra en el borrador v2.
4. **Única oración nueva permitida**, en la sección de datos: los puntos del salario se miden sobre la masa con tope de 25 UMA, 337 días y distribución R1 con piso en el salario mínimo, y los porcentajes de los ingresos del SEM usan el Cuadro V.13 del Informe; el libro de Finanzas se usa para cotizantes, salarios y supuestos. Si ya existe una oración sobre el denominador, sustituirla.
5. Si alguna oración deja de ser cierta con las cifras nuevas (por ejemplo, un orden o una comparación), no reescribirla: marcarla **[REVISAR]** y listarla en el reporte.

---

## 2. Trazabilidad

1. `tablas/exp1_borrador_v2_a_v3.csv`: una fila por cifra sustituida, con identificador en `NUMBERS.md`, texto anterior, texto nuevo y sección del borrador.
2. Registrar en `NUMBERS.md` la fuente nueva de cada cifra (denominador común; Cuadro V.13) y la decisión de esta versión.

---

## 3. Verificaciones

| # | Verificación |
|---|---|
| 3.1 | Ningún monto en mdp del borrador cambia (desviación 0 contra v2). |
| 3.2 | Toda cifra en puntos o en % del SEM del borrador v3 está en `NUMBERS.md` con su valor nuevo; ninguna cifra vieja queda en el texto. |
| 3.3 | Las cifras sustituidas son un subconjunto de las 186 de `exp1_cambios_denominador.csv`; reportar cuántas de las 186 aparecen en el borrador. |
| 3.4 | Fuera de las cifras y de la oración de la sección 1.4, el diff entre v2 y v3 está vacío. |
| 3.5 | Ninguna salida contiene 2055. |

---

## 4. Reporte

Agregar a `REPORT.md` una sección "v1.3" con: número de cifras sustituidas, oraciones marcadas [REVISAR], resultado de las verificaciones y el diff resumido.

Actualizar el documento del experimento 1 en Claude Docs solo si Héctor lo indica. Hacer commit y archivar esta instrucción en `_crossrefs/_build_instructions/`.
