---
type: nota_tecnica
project_scope: [RF]
related_missions: [BID2]
title: "RF — El modelo OLG de BID2 y la propuesta de formalización subsidiada: estado al 7 de noviembre de 2026"
institution: "ITED — Iniciativa para la Transición Económica y Demográfica (Tecnológico de Monterrey)"
date_added: 2026-11-07
version: v1
status: notas de trabajo
added_by: Beth (con Cath)
endorsed_by:
confidencialidad: "Uso interno de ITED."
---

# RF — El modelo OLG de BID2 y la propuesta de formalización subsidiada

**Fecha:** 7 de noviembre de 2026
**Propósito:** dejar asentado qué puede aportar hoy el modelo de BID2 al cuadre de equilibrio general de la Reforma Fiscal, qué le falta para evaluar la propuesta de formalización subsidiada para los grupos de ingreso bajo y medio-bajo, y cómo se conecta con el trabajo previsto para enero de 2027. Esta nota no modifica el documento de trabajo de BID2.

---

## 1. Resumen

El modelo de BID2 ya hace bien la parte de cuadre: cierra la restricción presupuestal, deja que salarios y tasa de interés respondan, y reporta la incidencia por edad, sexo y educación. No puede evaluar la propuesta de formalización subsidiada, porque le faltan las dos piezas que la definen: **un margen formal/informal y un vínculo entre las contribuciones de cada persona y lo que recibe.** En el modelo todos los trabajadores son formales y la pensión es plana.

Por eso el trabajo de enero no es aplicar el modelo a RF, sino ampliarlo. Esa ampliación es también el candidato natural a un segundo artículo sobre el mismo modelo, y comparte cimientos con el trabajo de diciembre en FISCUS y en la versión de revista: transiciones y un cierre fiscal con la deuda fijada.

**Interpretación que conviene confirmar:** en esta nota, "cuadre" (adding up) significa comprobar que las piezas de la reforma sumen en equilibrio general: que el presupuesto cierre con una regla de financiamiento explícita, que los precios de los factores respondan y que los costos y beneficios de cada grupo sumen al agregado.

---

## 2. Lo que el modelo ya ofrece a RF

| Elemento | Para qué sirve en RF |
|---|---|
| Restricción presupuestal del gobierno con impuestos al consumo, al ingreso laboral, al ingreso de capital y al gasto médico | Base para cuadrar el financiamiento de un subsidio con ingresos generales |
| Identidad de reparto τp = κ · N^R/N^W con τp endógena | Muestra cómo cualquier cambio en la base de cotizantes repercute en la tasa de contribución |
| Precios de factores endógenos | Los efectos de la reforma sobre salarios y rendimientos, no solo los efectos directos |
| Cuatro tipos (sexo × educación) con perfiles medidos de productividad y supervivencia | Incidencia por grupo, que es donde se juega una propuesta focalizada |
| Bienestar en equivalente de consumo, al nacer y por edad | Comparación de ganadores y perdedores con una métrica común |
| Gasto médico de bolsillo como decisión del hogar | Punto de partida para la cobertura de salud, que es el beneficio que los trabajadores más valoran |

---

## 3. Lo que falta para evaluar la formalización subsidiada

Cada pieza responde a una parte de la propuesta o a una de las pruebas de BDH (incentivos a la formalización y sostenibilidad fiscal).

| Pieza faltante | Por qué la propuesta la necesita | Costo aproximado |
|---|---|---|
| **Margen formal/informal** por tipo y edad | Sin elección de formalidad no hay respuesta que evaluar | Alto: una decisión discreta adicional por periodo |
| **Vínculo individual entre contribuciones y beneficios** | Un subsidio a la cotización solo cambia la decisión si lo que se recibe depende de lo que se cotiza; con una pensión plana, el subsidio no tiene efecto sobre el incentivo | Alto: una variable de estado con la historia de cotización, o una aproximación por promedio de ingresos |
| **Cobertura de salud contributiva y no contributiva** (IMSS frente a IMSS-Bienestar) | La salud es el beneficio que más pesa en la decisión de formalizarse; la cobertura no contributiva reduce el valor relativo de cotizar | Medio: se comparte con la especificación 3 del bloque de salud en la versión de revista (provisión pública) |
| **Subsidio focalizado financiado con ingresos generales** | Es la propuesta misma | Bajo una vez que el cierre fiscal tenga la deuda fija y un impuesto que ajusta |
| **Tasa de dependencia por cotizantes**, no demográfica | Con informalidad, la presión sobre el sistema depende de cuántos cotizan, no de cuántos trabajan | Bajo una vez que exista el margen formal/informal |
| **Tasa de impuesto a la formalización (FTR) por tipo** | Medida de incentivos del marco de Fietz et al. (2025): cuña fiscal menos el valor que el trabajador asigna a los beneficios | Bajo: se calcula a partir del modelo ampliado |
| **Tratamiento fiscal del sector informal** | El sector informal paga IVA pero no cotiza; esto cambia el cuadre de cualquier subsidio | Bajo |

**Datos que harán falta:** ENOE para formalidad por edad, sexo y educación (Milo); ENIGH para ingresos y gasto por condición de formalidad; los registros de afiliación del IMSS como contraste.

---

## 4. Conexión con FISCUS y con la versión de revista

- **Diciembre de 2026 (FISCUS, Capa C, y fase 1 de la versión de revista):** cierre fiscal con deuda fija, corrección de la base del impuesto al capital, solucionador de transiciones y prototipo del nuevo bloque de salud. RF necesita las dos primeras antes de empezar.
- **Enero de 2027 (RF):** diseño e implementación del margen formal/informal. Corre en paralelo con la fase 2 de la versión de revista, que reestima el bloque de salud. Las dos tareas tocan el mismo código, por lo que conviene acordar desde ahora cómo se organizan las ramas.
- **Diseño modular:** si en diciembre el bloque de pensiones se reescribe de forma que el vínculo entre contribución y beneficio pueda añadirse como módulo, enero no empezará con una reconstrucción.
- **El artículo de BID2 no incluye la formalización.** La nota de estrategia para Diego la deja expresamente fuera y la propone como segundo artículo.

---

## 5. Plan propuesto para enero de 2027

1. **Especificación del margen** (primera semana): decisión discreta formal/informal por periodo; salario y productividad en cada sector; qué paga y qué recibe el trabajador en cada sector; cómo entra la cobertura de salud.
2. **Momentos de formalidad** (en paralelo): participación formal por edad, sexo y educación (ENOE); brecha salarial formal/informal; transiciones entre sectores si el panel lo permite.
3. **Prototipo en estado estacionario**, sin transiciones, para comprobar que el margen responde a los incentivos de forma razonable.
4. **El subsidio:** diseño focalizado en ingresos bajos y medio-bajos, financiado con el instrumento que ajusta en el cierre; cálculo del costo fiscal neto, de la FTR por tipo y de la incidencia.
5. **Prueba de sostenibilidad fiscal** con trayectorias, en cuanto el solucionador de transiciones esté disponible.

---

## 6. Reglas que aplican

- **Ninguna cifra del documento de trabajo de BID2 es una cifra de RF.** El modelo cambiará; cada versión requiere su propio registro de resultados.
- **Lenguaje de incidencia:** no escribir "costo para el patrón" ni "ahorro en costo laboral" para cambios en cuotas. Eso supone medir la incidencia económica. Describir tasas legales y la cuña contributiva legal.
- **Las dos pruebas de BDH no son negociables:** toda variante de la propuesta se evalúa por sus incentivos a la formalización y por su sostenibilidad fiscal.
- **Separación:** el artículo de BID2 no menciona RF ni FISCUS.

---

## 7. Decisiones pendientes

1. Confirmar la interpretación de "cuadre" de la sección 1 (Héctor).
2. Pensión ligada a la historia de cotización con variable de estado, o aproximación por promedio de ingresos (Héctor y Diego).
3. Si la cobertura de salud entra como estado exógeno por tipo o como elección ligada a la formalidad (Héctor).
4. Calendario de RF frente a la fase 2 de la versión de revista, que compiten por el tiempo de Diego en enero–marzo de 2027 (Héctor y Diego).
5. Relación con el artículo de CONOSAFI que acompaña la propuesta: qué resultados del modelo, si alguno, entran en él (Héctor).
