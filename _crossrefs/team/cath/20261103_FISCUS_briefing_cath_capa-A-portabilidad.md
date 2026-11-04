---
type: briefing
to: Cath
from: Claude (for Héctor)
date: 2026-11-03
subject: "Tu instrucción de portabilidad de la capa A (Simulador Fiscal CIEP, Stata → Python): veredicto, hallazgos de fondo y seis rulings"
report: FISCUS/capa_A_evaluacion/report/LAYER_A_PORTABILITY_ASSESSMENT.md
instruction: FISCUS/RC_simulador/20261103_FISCUS_buildinstr_layerA-python-portability_v1.md
related: [FISCUS/capa_A_evaluacion/report/parameter_surface.csv, FISCUS/capa_A_evaluacion/report/call_graph.md, FISCUS/capa_A_evaluacion/report/hazard_counts.csv, Missions/Funded/NTA_Inequality/paper_final.tex, "Missions/Funded/BID2/GE-now with Gender/ge_model_gender.jl"]
commit_at_send: 7635b33
confidentiality: estricta (regla FISCUS); la fuente del CIEP no está en el repo y el repo es público — no empujar esta rama sin decidirlo
---

# Cath — la capa A, evaluada

**Qué pasó.** Ejecuté tu instrucción completa sobre el zip `SimuladorCIEP-master.zip` (v8.15.3, CHANGELOG del 2026-11-03, baseline v8.15.0): manifiesto con SHA-256 de 2 542 archivos, inventario, grafo de llamadas, superficie de parámetros, respuestas Q1–Q6, mapa de riesgos con conteos, auditoría de literales, verificación y opinión. Héctor pidió después cuatro extensiones que no estaban en tu encargo: integración con el NTA propio (§10.6), con el OLG de BID2 (§10.7), la demografía desde el motor de DFD (§10.8) y la pregunta «¿modelos completos o simplificados?» (§11). Todo está en el informe (1 198 líneas) y commiteado localmente; nada salió de la máquina.

**Veredicto en una línea.** Moderado-a-difícil; no recomendable como transliteración del repositorio; recomendable como híbrido en dos fases, empezando por la cola de escenario que corre la web (unas 5 000 líneas) como `run(parámetros)` sobre artefactos congelados del CIEP: 7–12 semanas-persona. El pipeline micro (10 000 líneas) solo se reimplementa desde especificación y, visto tu NTA, como extensión de la base propia: 14–24 semanas-persona.

## Tres hallazgos que cambian la lectura de la capa A

1. **No hay cierre intertemporal.** El valor presente y las cuentas generacionales se retiraron el 2026-09-12 (`FiscalGap.ado:412-416, 1101-1125`); `CuentasGeneracionales.ado` está comentado (`SIM.do:524`) y lee rutas obsoletas. El motor proyecta ingresos y gastos año por año hasta anioPE+5 = 2032 y la deuda absorbe la brecha (`FiscalGap.ado:864-893`). La tasa de descuento (8) solo sobrevive en una población en valor presente para despliegue.
2. **La proyección de ingresos no depende del crecimiento del PIB.** Tras el ancla de 2027 cada rubro crece con su tendencia histórica per cápita (acotada a ±5 %) por el crecimiento de su base demográfica (`FiscalGap.ado:154-198`). `CRECPIB` mueve el denominador y el valor en pesos del ancla, nada más. Macro exógeno sin retroalimentación alguna.
3. **La aritmética de deuda es nominal con un factor de revaluación histórico.** Costo = tasa efectiva (media de cinco años, o `DEUDA0` del usuario) × saldo previo; deuda interna y externa × (1+g_act) + efecto cambiario + RFSP por participación, donde `actualizacion_geo` es el residuo geométrico que cierra la historia 2009→último (`FiscalGap.ado:840-892`). Ni (r−g) de libro ni descomposición de cuatro variables en la proyección; esa descomposición existe solo para la historia (`SHRFSP.ado:690-719`).

## Lo que vale del CIEP para FISCUS, y lo que no

Vale: los perfiles por edad simple y sexo de cada impuesto y transferencia anclados a LIF/PEF/SCN (`Simulador.ado`, archivos `*PERF`), las tasas efectivas macro/macro (`TasasEfectivas.ado`), el reparto de educación por matrícula y de salud por afiliación (`GastoPC.ado`), el PEF programa por programa y la superficie web de 142 parámetros. No vale conservar: su proyección anual, su bloque macro y su CONAPO.

Incidencia (Q4): estatutaria sin comportamiento. ISR de asalariados al trabajador con gross-up por la tarifa; cuotas patronales y federales dentro del ingreso bruto laboral; IVA/IEPS/ISAN al consumidor en proporción al gasto con haircut uniforme de informalidad; ISR de morales a hogares con negocio, que el propio autor marca como error pendiente para la 8.16; FMP y empresas públicas per cápita y fuera del neto. Cero elasticidades.

## Seis rulings que te toca dar

1. **Cierre FISCUS.** La capa A no lo tiene. ¿Qué regla añadimos en la fase 1 (impuesto, gasto, meta de deuda) y con qué horizonte, dado que el OLG de BID2 solo da estados estacionarios? Propongo la aritmética del CIEP a 2032 como puente y los estados estacionarios como anclas, etiquetados.
2. **Elasticidad ingreso–PIB.** ¿Dejamos la proyección del CIEP tal cual (tendencia per cápita, sin PIB) como referencia, o imponemos una elasticidad a PIB en nuestra versión? Decide antes de que se escriba el módulo.
3. **Tasas efectivas al OLG.** `τc`, `τw`, `τk` del OLG son 0.16, 0.20, 0.20 estatutarias/introducidas. Las efectivas del CIEP son otras y `τw` exige partir las cuotas IMSS entre su componente de pensión (5.15 + 1.12 + 1.49 % del SBC más cuota social) y el resto, porque el OLG tiene `τ^p` aparte (§10.7). ¿Efectivas o estatutarias, y quién firma la partición?
4. **Copias contradictorias del CIEP.** `CSS_ISSSTE` en `SIM.do:251-260` difiere de `Households.do:1583-1592`; `IEPST` tiene tres copias (17, 17 y 10 filas); la informalidad IVA es 23.1 en `SIM.do:288` y 7.77 en `Expenditure.do:1176`; `smdf` mezcla UMA y salario mínimo según el año. Qué copia es canónica se le pregunta a Ricardo, pero conviene que tú digas cuál es defendible antes.
5. **ISR de personas morales.** El CIEP lo asigna a hogares con negocio propio y lo corregirá en la 8.16 (∝ `d4_relativo`). Tu NTA lo pone al 30 % sobre el ingreso de capital observado. ¿Cuál convención adopta FISCUS mientras tanto?
6. **Dos NTA y dos perfiles de gasto de bolsillo.** Tu paper y el motor del CIEP son casi gemelos en método (ENIGH, cierre por λ, 2/3–1/3, punto fijo intrahogar, gross-up) y difieren en consumo público (plano vs matrícula/afiliación), transferencias (ancla agregada vs PEF por programa), activos y ahorro, y cierre de la identidad (brecha reportada vs forzada a 1e-9). Propuse quién es dueño de qué por dimensión (§10.6, tabla). ¿Lo firmas o lo cambias?

## Preguntas bloqueantes para Ricardo (§9), por si las llevas tú

Artefactos congelados de una versión (`perfiles2027.dta`, `master/2024/*`, los 41 `*RECprom`, `cache/`); régimen de precisión del VPS (`set type double`, procesadores, versión exacta de Stata: 17 vs 19.5 ya difieren en ~52 de ~5 000 valores, `runbook:529`); copia canónica de las tablas duplicadas; procedencia de los factores de calibración de `ISR_Mod.do` (184, 193, 208, 213) y de las anclas Pemex/ISSFAM en `GastoPC.ado`.

## Nota sobre el método

Todo lo del informe está etiquetado [observed] con archivo:línea o [inferred] con el razonamiento; «no determinable desde la fuente» donde aplica. No se ejecutó código del zip, no hubo red. El zip no trae ningún `.dta`, log ni Excel: verificar cualquier port exige una corrida de Stata con licencia al menos una vez, o que el CIEP entregue los artefactos.
