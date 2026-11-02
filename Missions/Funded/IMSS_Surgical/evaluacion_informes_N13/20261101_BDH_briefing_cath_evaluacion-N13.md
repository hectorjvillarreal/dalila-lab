---
type: briefing
to: Cath
from: Claude (for Héctor)
date: 2026-11-01
subject: "Revisión de cifras y lectura fiscal: evaluación de los informes del Núcleo 13"
evaluation: Missions/Funded/IMSS_Surgical/evaluacion_informes_N13/EVALUACION_N13.md
doc: https://claude.ai/artifact/GhP24wLk8SNFrbSMqKUpkJ
related: _crossrefs/_build_instructions/20261101_BDH_N13_evaluacion-informes_build_v1.0.md
commit_at_send: 192f37d
---

# Cath — cifras y lectura fiscal de la evaluación del N13

**Qué pasó.** Ejecuté la instrucción de Beth sobre la última versión de los dos informes del Núcleo 13. Los dos quedan en nivel 2 (cambios mayores). La instrucción te tenía como revisora pendiente de «cifras y lectura fiscal»; esta es la parte que te toca. Expediente en `evaluacion_informes_N13/` (192f37d, pushed); resumen en el doc de arriba.

**Qué se te pide.** Cinco rulings, en orden de peso:

1. **Base de la sección 6.** El informe usa como costo por persona 545,271 millones de «gasto corriente en salud» 2025 atribuidos completos al SEM, entre 54.7 M de derechohabientes (9,977 pesos). Los anexos de ITED usan 494,275 (prestaciones en especie, Cuadro V.13, 2026) entre 79.2 M (6,243 pesos). Con eso, el saldo de la afiliación subsidiada es 288 vs 81 mil millones y el seguro solidario cubre hasta 2037/2033 vs 2054/2037. ¿Cuál es la base defendible ante el IMSS, y qué incluye el agregado de 545,271 (administración, RJP, Riesgos de Trabajo)? (R6, N-R20.)
2. **Déficit de GMP.** El informe lo aproxima como costo de todos los derechohabientes de 60+ menos ingresos de GMP: 89 mil millones en 2027, 272 en 2054. El Cuadro V.19/V.24 del Informe 2025-2026 da 68.4 (2026), 97.8 (2031), 203.9 (2055), con administración y provisiones incluidas; interpolado, ≈74 en 2027 y ≈198 en 2054. La aproximación sobrestima, de modo que 6b.5 («el déficit sería mayor y el seguro alcanzaría por menos tiempo») va en la dirección contraria. ¿Confirmas la lectura y el uso de V.24 como referencia? (R4, R5.)
3. **Δ(t).** Desde 2028 el gasto se proyecta como 63.55 % de los ingresos totales del IMSS; eso produce una brecha negativa 2030-2040 que 5.6 llama artefacto, pero Tabla 5 y Figura 9 solo muestran esa trayectoria. El cuaderno tiene la variante «demanda» como interruptor y se corrió solo con «pct». ¿Dos columnas en la Tabla 5 o advertencia en el resumen? (R3.)
4. **Lenguaje de incidencia en Recomendaciones.** 3.4: «sin que los patrones paguen más: con esta opción, lo que pagan sobre la nómina baja 3 puntos o permanece constante»; 3.5: «una cuota que no cueste proporcionalmente más a quien gana menos»; 5.5: «quienes ganan menos pagarían menos». Resultados sí habla de tasas legales. Además, 3.5 dice que el 3.467 % se calculó «con base en la ENIGH»; según N.2 se calibró con los ingresos de GMP de la proyección institucional y en 2026 ya deja 8 mil millones de diferencia. (C12, C13, N-C4.)
5. **Recomendación 4.** Añade «los otros 3 puntos se dejarían de cobrar o permanecerán en Infonavit», que 6b no simula (6b baja la tasa legal 3 puntos). ¿Se quita o se simula?

## Cifras que sí cuadran

Tablas 1-6, K.2, J.2 y E.1 suman; 89 %/11 %, 2.5 %/2.7 %, −4.0/+5.9 %, 47.2 %, 10.9 %, 29 % se recalculan; la Tabla 5 coincide al peso con la celda 16.6 del cuaderno. Contra el Informe del IMSS: Cuadro A.4 (9.60 = 5.97 + 0.82 + 2.81) exacto; primas 12.94 % vs 8.9 % (horizonte 2026-2055); 337 días; 3 % real; 22,352,586 cotizantes SEM. Los 46.8 M de 2054 vienen del libro de Finanzas (el Informe no publica 2054; Gráfica C.1: 47.15 M). Los 79.2 M son población «potencial» (15.6 M de familiares no adscritos estimados); adscritos: 63.6 M, conteo que la Tabla I.3 no incluye.

## Cifras que no cuadran

| Dónde | Problema | ID |
|---|---|---|
| Nota de 6a / Anexo I | 54.6 vs 53.63 M con IMSS en la ENIGH | N-R5 |
| 5.5 / Anexo M | «se cruzan alrededor de 2038, antes el gasto crece más rápido» vs «crece más lento a partir de 2028» | N-R4 |
| 6a.2 / 6a.4 | Cuota fija 8,735 (365 días) vs 8,065 (337 días) | N-R8 |
| 2.1 | «discrepancia de 49.5 %» con 10,536 / 21,259 (da 49.6 o 50.4) | N-R11 |
| 6a-6c | Horizontes 2054 (6a, 6b) y 2055 (6c), con la caída de nuevos cotizantes de 2055 en el denominador | N-R7, R13 |
| Figuras 5 y 10 | Leyendas E0-E6 «Expansión» de otra versión; Tablas 3 y 6 tienen E0-E9 | N-R17 |
| 7.1 | «gasto crece más que el PIB cuando los adultos mayores superan 15 %»: no está en Rechel 2013 ni en OCDE 2019 | N-R21 |

## Referencias

Cuatro entradas no existen (Arredondo & Aviles 2020; Castañeda-Orjuela & Arbelaez 2021; Lavín & Sosa 2019; capítulo de Reddy 2015 en DCP3, única cita de Recomendaciones). Detalle con URL en `tablas/referencias.csv`.
