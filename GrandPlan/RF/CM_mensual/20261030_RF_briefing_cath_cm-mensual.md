---
type: briefing
to: Cath
from: Claude (for Héctor)
date: 2026-10-30
subject: "CM actualizada a enero-septiembre 2026; monitor de la instrucción v2 borrado por Héctor"
note: GrandPlan/RF/CM_mensual/Contabilidad_Mortal_202609.docx
related: _crossrefs/_build_instructions/20261030_RF_BUILD_monitor-CM_v2.md
commit_at_send: 2975488
---

# Cath — CM de septiembre y cierre de la instrucción v2

**Qué pasó.** Héctor te pidió que yo actualizara la Contabilidad Mortal con el último informe de la SHCP. La instrucción v2 pedía otra cosa, un monitor mensual en `monitor_cm/`. Lo construí y lo corrí, y Héctor lo mandó borrar. Lo que queda es una tarjeta por informe en `GrandPlan/RF/CM_mensual/`, `Contabilidad_Mortal_AAAAMM.docx`. La de `202609` está en `p4-revision-final` (2975488).

**Qué se te pide.** Dos cosas:

1. Decide cómo queda la v2 en `_build_instructions/`. Sigue ahí como procedencia, sin commit y sin endoso. Ya no hace falta una v3 del monitor.
2. Si tienes la v1, déjala en el archivo. No aparece en el disco, y la v2 dice que la sustituye.

## Resultado

| % del PIB (36,500 mmdp) | Julio | Septiembre |
|---|---:|---:|
| Tributarios | 16.0 | 15.7 |
| No tributarios | 1.2 | 1.1 |
| Organismos y Empresas | 3.5 | 3.5 |
| Ingresos Disponibles | 20.7 | 20.3 |
| Gasto No Programable | 8.3 | 8.2 |
| Pensiones | 6.3 | 6.1 |
| Uso propio | 2.1 | 2.1 |
| **Bolsa** | **4.0** | **4.0** |

## Decisiones de Héctor (30-oct)

- El desglose de ingresos sale de CGPE 2027, Anexo II.6, no del reparto del §5b. Sus totales coinciden con el Estimado de la Tabla I.1.
- Adefas en 69.0 mmdp (CGPE), no en 0.3%.
- Costo financiero se mantiene en 3.8%, aunque el estimado oficial ya es 3.7% (1,364.5 mmdp) y el ritmo observado ≈3.6%.
- Pensiones por fórmula: (línea 6 − línea 5) − participaciones + PBAM (526.5, PEF 2026, S176).
- La Bolsa se imprime en 4.0%.

## Lo que debes saber antes de citar la cifra

- **El 4.0 no cierra a la vista.** El valor exacto es 3.95, y la resta impresa (20.3 − 8.2 − 6.1 − 2.1) da 3.9. Héctor pidió dejar 4.0.
- **La estabilidad viene del método.** Los ingresos netos de uso propio restan 0.38 pp. Adefas y pensiones suman 0.33 pp por las decisiones de arriba. Con los supuestos de julio la Bolsa sería 3.6%.
- **Pemex.** La tarjeta ahora dice 0.7% de FMP contra 0.5% de aportaciones y «se compensan en buena parte». El 0.5 es línea 7 − línea 6 de la Tabla I.1, con todo el sector público; el informe no rotula los apoyos a Pemex.
- **Materiales ya presentados.** Los decks de SobreMéxico y EXATEC usan la versión anterior, con tributarios 16.0, Adefas 0.3 y pensiones 6.3. La igualdad Bolsa 4.0 = intereses 4.0 sigue impresa igual, pero la Bolsa exacta es 3.95.

## Premisas de la v2 que ya no valen

- Estimado oficial de costo financiero: 3.7%, no 4.2%.
- PIB oficial 2026: 37,160.7 mmdp (CGPE 2027), no 37,324.8 de Pre-Criterios.
- El informe trimestral publica el SHRFSP en % del PIB, no el RFSP.
- Los datos abiertos iban a agosto el 30-oct; el archivo es `ingreso_gasto_finan.csv` y requiere el bundle TLS de las descargas SHCP.
