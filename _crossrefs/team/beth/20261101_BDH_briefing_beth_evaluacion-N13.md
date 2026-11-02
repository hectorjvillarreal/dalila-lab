---
type: briefing
to: Beth
from: Claude (for Héctor)
date: 2026-11-01
subject: "Evaluación ejecutada: Informe de Resultados e Informe de Recomendaciones del Núcleo 13, nivel 2 los dos"
evaluation: Missions/Funded/IMSS_Surgical/evaluacion_informes_N13/EVALUACION_N13.md
doc: https://claude.ai/artifact/GhP24wLk8SNFrbSMqKUpkJ
related: _crossrefs/_build_instructions/20261101_BDH_N13_evaluacion-informes_build_v1.0.md
commit_at_send: 192f37d
---

# Beth — tu instrucción de evaluación del N13 está ejecutada

**Qué pasó.** Héctor pidió ejecutar tu instrucción `20261101_BDH_N13_evaluacion-informes_build_v1.0` sobre la carpeta `entrega_finales_versiones/` (Resultados `Oct2026_LIMPIO`, Recomendaciones `-4`; sin cambios controlados ni comentarios de Word). Todo está en `evaluacion_informes_N13/` (192f37d, pushed en `p4-revision-final`); el resumen para el equipo es el doc de arriba. Los originales no se tocaron (hash igual antes y después).

**Qué se te pide.** Tres cosas:

1. Confirmar o corregir las decisiones marcadas **[REVISAR]** en `REPORT.md` §6: ningún hallazgo como «bloqueante»; D5 = 1 en los dos documentos; D1 = 3 en Resultados pese a las Figuras 5 y 10; y haber registrado como hallazgo nuevo (N-R20) que 6a/6b no coinciden con los anexos de ITED.
2. Decidir si N-C10 (la única cita de Recomendaciones, Reddy 2015, no existe) pasa a bloqueante para la Recomendación 1.
3. La instrucción quedó archivada con `status: executed` y `endorsed_by: []`; Cath tiene su propia briefing para la revisión de cifras.

## Resultado

| | Resultados | Recomendaciones |
|---|---|---|
| Nivel global | **2** | **2** (al borde del 1 en D2 y D5) |
| D1 · D2 · D3 · D4 | 3 · — · 2 · 3 | 3 · 2 · — · 2 |
| D5 · D6 · D7 · D8 · D9 | 1 · 2 · 3 · — · 3 | 1 · 2 · 3 · 2 · 2 |
| Conocidos (sección 3 de tu instrucción) | 5 resueltos · 7 parciales · 4 pendientes | 0 · 3 · 14 |
| Nuevos | 23 (4 mayores) | 10 (2 mayores) |

## Lo que más pesa

1. **Cuatro referencias no existen**: Arredondo & Aviles 2020, Castañeda-Orjuela & Arbelaez 2021, Lavín & Sosa 2019 y el capítulo de Reddy 2015 en DCP3 (única cita de Recomendaciones). Rechel es 2013; CONAPO es 2023 / 2020-2070; el «15 % de adultos mayores» no está en Rechel ni en OCDE. CIEP 2025 (Méndez Méndez) y el Cuadro A.4 sí respaldan lo citado.
2. **6a/6b no coinciden con los anexos de ITED**: saldo 288 vs 81 mil millones; seguro solidario 2037/2033 vs 2054/2037. Tres decisiones de método abiertas: gasto base (545,271 atribuido al SEM vs 494,275 del V.13), conteo (54.7 vs 79.2 M) y déficit de GMP (aproximación 60+ vs Cuadro V.24). El Informe del IMSS da un déficit de GMP **menor** que la aproximación (≈74 vs 89 en 2027), así que R5 va al revés, confirmado.
3. **Δ(t) 2030-2040 negativa es artefacto** (R3): advertido en 5.6, pero Tabla 5 y Figura 9 solo muestran esa trayectoria; el cuaderno entregado corrió solo `METODO_GASTO_BALANCE = "pct"`.
4. **Recomendaciones 2.2-2.3 describen el modelo anterior** (C1-C5 intactos); Rec. 4 añade «o permanecerán en Infonavit», no simulado; Rec. 5 sigue con «3.467 % con base en la ENIGH».
5. **Restos de edición**: Figuras 5 y 10 con leyendas E0-E6 de otra versión; «[año]»; nota de edición en la Figura 3; cinco notas rojas en la sección 4 de Recomendaciones; sin sección 1 ni paginación; listas de autores distintas.

## Qué hay en el expediente

- `EVALUACION_N13.md` (veredicto, calificaciones con evidencia, estado de los 33, nuevos, evaluación por sección, coherencia entre documentos, ruta de 11 acciones con quién decide).
- `tablas/hallazgos.csv` (66 filas), `referencias.csv` (26, con URL de verificación), `figuras_tablas.csv` (61), `cifras.csv` (2,533 automáticas) + `cifras_clave.csv` (20 magnitudes), `comentarios.csv` (vacío).
- Dos `.docx` `_evaluacion_comentado` con un comentario de Word por hallazgo mayor (9 + 12).
- `respaldo/`: reportes de los tres subagentes (visual, contraste IMSS/ITED, referencias) y los scripts.

## Lo que no se pudo verificar

Plantilla de la Comisión (no está en la carpeta); el comentario de Mónica Montano (sin comentarios en el archivo); las cifras internas del IMSS de 2.1 y 3.1; INEGI «+5 % anual»; el cuaderno de ingresos (no está en la entrega). El signo menos como cuadro vacío es del render de LibreOffice, no comprobado en Word.
