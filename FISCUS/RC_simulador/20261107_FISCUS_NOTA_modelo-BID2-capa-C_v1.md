---
type: nota_tecnica
project_scope: [FISCUS]
related_missions: [BID2]
title: "FISCUS — Capa C: estado del modelo OLG de BID2 al 7 de noviembre de 2026"
institution: "ITED — Iniciativa para la Transición Económica y Demográfica (Tecnológico de Monterrey)"
date_added: 2026-11-07
version: v1
status: notas de trabajo
added_by: Beth (con Cath)
endorsed_by:
confidencialidad: "CONFIDENCIAL — uso interno de ITED. No circular sin autorización expresa de Héctor J. Villarreal Páez."
---

# FISCUS — Capa C: estado del modelo OLG de BID2

**Fecha:** 7 de noviembre de 2026
**Propósito:** dejar asentado qué es hoy el modelo que se convertirá en la Capa C, qué le falta para cumplir con los principios de diseño de FISCUS y qué conviene hacer en diciembre. Esta nota no modifica el documento de trabajo de BID2, que sigue su propio curso hacia la serie de documentos de trabajo del BID y, después, hacia una revista.

---

## 1. Resumen

El modelo de BID2 es un OLG estocástico de equilibrio general con capital de salud y supervivencia endógenos, cuatro tipos de hogar (dos niveles educativos por sexo) y un sistema de reparto cuya tasa de contribución se ajusta para equilibrarlo. Está calibrado y estimado en dos etapas con microdatos mexicanos. Funciona, resuelve y produce resultados coherentes, pero tiene cuatro limitaciones que lo hacen inadecuado como Capa C tal como está:

1. Solo compara estados estacionarios. La SHCP preguntará por trayectorias.
2. La deuda pública es el residuo del presupuesto y resulta entre 107 y 124 % del producto anual, contra cerca de 50 % observado. Esto contradice el principio de diseño 2 de FISCUS.
3. La demografía entra como una sola tasa de crecimiento poblacional, no como un escenario año por año de la Capa 0.
4. El bloque de salud, en su especificación actual, no mueve ningún resultado de política.

Las cuatro coinciden con lo que exige la versión de revista del artículo. Si el trabajo de diciembre sobre la Capa C se organiza alrededor de esas cuatro correcciones, la Capa C y el artículo avanzan juntos. Esta es la recomendación central de la nota.

---

## 2. Qué es el modelo hoy

### 2.1 Estructura

| Componente | Especificación actual |
|---|---|
| Hogares | Generaciones traslapadas en periodos de cinco años; cuatro tipos (sexo × educación); riesgo idiosincrático de productividad; preferencias GHH con amenidad de salud multiplicativa y valor de flujo de estar vivo |
| Salud | Stock continuo con depreciación por edad; gasto médico elegido **antes** del choque de salud (preventivo por construcción); choques que afectan el stock, no el presupuesto |
| Supervivencia | Calendarios base por sexo y educación (ENASEM), modulados por el stock de salud y acotados en uno |
| Producción | Cobb-Douglas; salarios y tasa de interés endógenos |
| Pensiones | Un solo pilar de reparto; beneficio plano indexado al ingreso laboral promedio por trabajador; la tasa de contribución cumple τp = κ · N^R/N^W |
| Gobierno | Impuestos al consumo, al ingreso laboral, al ingreso de capital y al gasto médico; la deuda cierra el presupuesto |
| Activos al morir | Se destruyen; no hay anualidades ni herencias |

### 2.2 Calibración

Dos etapas. Primera: demografía, tecnología, proceso de ingresos e instrumentos fiscales fijados con datos externos y microdatos (ENIGH 2016–2018 agrupada, ENASEM). Segunda: nueve parámetros estructurales estimados por distancia mínima con diez momentos, nueve de ellos de microdatos mexicanos. Dos parámetros quedan en sus cotas, uno se fija porque la función objetivo es plana en esa dirección y no hay errores estándar.

### 2.3 Resultados del documento de trabajo (solo como referencia)

Bajo la demografía de 2050 con ajuste de la tasa de contribución, esta pasa de 5.66 a 12.26 %, el salario sube 12.4 % y la tasa de interés baja de 8.58 a 6.82 % anual. El bienestar de los recién nacidos casi no cambia; las pérdidas se concentran en los residentes de mayor edad con activos. Reducir la tasa de reemplazo de 0.40 a 0.185 o elevar la edad de retiro a 70 mejora el bienestar de los recién nacidos (8.29 y 3.11 % respectivamente frente al ajuste de contribuciones), con incidencias opuestas por edad y tipo.

**Estas cifras pertenecen a la calibración actual. En cuanto el modelo cambie, ninguna puede presentarse como resultado de la Capa C.** La capa de lenguaje de FISCUS no debe tener acceso a ellas como si fueran salidas del laboratorio.

### 2.4 Código

El solucionador está en Julia. La fase 2 (salud continua con depreciación por edad) está aprobada; la fase 4 (elección de inversión en salud) implica una expansión de unas quince veces en la búsqueda de raíces. Con hilos de CPU se obtienen alrededor de 2.7 núcleos efectivos; la capacidad real de Dalila está en la GPU.

---

## 3. Qué le falta para ser la Capa C

Cada punto se contrasta con un principio o requisito de la descripción de FISCUS v0.

| Requisito de FISCUS | Estado del modelo | Qué se necesita |
|---|---|---|
| Respuestas sobre trayectorias ("qué ocurre con las pensiones si la fecundidad cae más rápido") | Solo estados estacionarios | Solucionador de transiciones con demografía año por año |
| Principio 2: la restricción presupuestal siempre cierra, con regla de financiamiento explícita | Cierra, pero con la deuda como residuo y en niveles irreales | Deuda fijada en su nivel observado y un instrumento que ajusta; la regla de financiamiento debe ser un parámetro del escenario |
| La demografía entra como parámetro desde la Capa 0 | Una tasa de crecimiento estacionaria | Interfaz que reciba fecundidad, mortalidad y, si aplica, migración por año desde la Capa 0 |
| Consistencia interna entre capas | Sin conexión con las capas A y B | Perfiles por edad del modelo contrastados con las NTA de la Capa B; salidas en unidades que la Capa A pueda leer |
| Procedencia trazable de cada corrida | Salidas en archivos, sin registro estandarizado | Registro por corrida: versión del código, parámetros, escenario, semilla, tiempo |
| Instituciones mexicanas | Un solo pilar de reparto plano | Como mínimo, la pensión universal no contributiva financiada con ingresos generales; idealmente, las cuentas individuales posteriores a 1997 |
| Respuesta del bloque de salud a la política | La salud está en su techo y no responde | Respecificación del gasto médico para incluir restauración después del choque, sujeta a lo que el hogar puede pagar |

Además hay una duda abierta que afecta directamente al cierre: **la base del impuesto al ingreso de capital.** Los hogares pagan el impuesto sobre todos sus activos (capital más deuda pública), pero la restricción del gobierno, como está escrita, lo recauda solo sobre el capital físico. Diego debe confirmar qué hace el código. Mientras no se resuelva, cualquier cifra de deuda del modelo es dudosa, y en FISCUS la deuda no es un detalle: es lo que la Capa A y la SHCP leerán.

---

## 4. Interfaz con las otras capas

**Lo que la Capa C recibe.**

- De la Capa 0: el escenario demográfico por año (fecundidad, mortalidad, composición educativa de las cohortes que entran).
- De la Capa A: los parámetros fiscales del escenario (tasas, reglas de beneficio, regla de cierre presupuestal).
- De la Capa B: los perfiles por edad de consumo e ingreso laboral de las NTA, para validar los perfiles que el modelo genera. Es una validación externa que el artículo no tiene y que la Capa C puede aportar.

**Lo que la Capa C entrega.** Trayectorias anuales o quinquenales de la tasa de contribución, salarios, tasa de interés, capital, producto, gasto en pensiones y en salud como porcentaje del PIB, deuda o el instrumento que ajusta, y bienestar por cohorte y tipo. La procedencia por capa se conserva en el registro interno de la corrida y no llega a la capa de lenguaje.

---

## 5. Un riesgo práctico: el tiempo de respuesta

Una transición completa con salud continua, cuatro tipos y riesgo de ingreso cuesta muchas veces lo que una solución estacionaria; en la máquina de la SHCP puede tardar horas. Una consulta en lenguaje natural que espera horas no es usable. Hay tres salidas, que no se excluyen entre sí:

1. **Biblioteca de corridas precalculadas** para los escenarios más probables, que la capa de lenguaje consulta.
2. **Estados estacionarios para preguntas rápidas** y transiciones como corridas diferidas, avisando al usuario.
3. **Un modelo reducido** calibrado sobre las corridas completas, para respuestas aproximadas inmediatas, siempre marcado como tal.

La decisión importa también para el hardware: la descripción de FISCUS ya señala que el cuello de botella de la máquina de ciclo es CPU y memoria. El costo por trayectoria que estime Diego es el dato que hace falta.

---

## 6. Plan para diciembre de 2026

Alineado con la fase 1 del plan de la versión de revista (nota a Diego del 7 de noviembre), para que el mismo trabajo sirva a ambos:

| Tarea | Responsable | Producto |
|---|---|---|
| Confirmar la base del impuesto al capital y corregir la ecuación que corresponda | Diego | Cierre fiscal coherente entre texto y código |
| Cierre con deuda fijada y un instrumento que ajusta (impuesto al consumo como base, impuesto laboral como prueba de robustez) | Diego | Baseline resuelto de nuevo |
| Solucionador de transiciones sobre el modelo actual, probado con la trayectoria de envejecimiento | Diego | Primera trayectoria y costo de cómputo medido |
| Prototipo del nuevo bloque de salud en equilibrio parcial | Diego | Respuesta a la compuerta G1 (fin de diciembre) |
| Interfaz de entrada de la Capa 0 (formato del escenario demográfico) | Héctor, Diego | Especificación escrita |
| Registro de corridas | Diego | Formato definido |

**Organización del código.** Una sola base con dos ramas: una de producción para la Capa C, documentada, validada y congelada en mayo de 2027 para la entrega de junio; y una de investigación para el artículo. Los cambios pasan de investigación a producción solo después de validarse, y cada versión queda registrada en Dalila.

---

## 7. Discrepancia que hay que resolver

La descripción del proyecto FISCUS v0 (31 de octubre de 2026) dice que la Capa C "documenta un resultado de no existencia de equilibrio bajo financiamiento exclusivo con deuda". Ese resultado se retiró del artículo de BID2 en agosto y no aparece en la versión actual. Hay dos opciones:

- Corregir la descripción de FISCUS y retirar la frase.
- Documentar el resultado de nuevo en los materiales de la Capa C, verificándolo con el modelo vigente.

La decisión es de Héctor. Mientras tanto, la descripción no debería circular con esa frase.

---

## 8. Separación y procedencia

- El artículo de BID2 no menciona FISCUS, la SHCP, OSF ni RF, y no los mencionará.
- El modelo se desarrolló dentro de un proyecto financiado por el BID y pasa a ser propiedad de ITED dentro de FISCUS. Conviene documentar esa procedencia ahora, como se hizo con el marco SS/PS/AS, antes de que alguien lo pregunte.
- Ninguna cifra del documento de trabajo debe entrar al corpus de FISCUS como salida del laboratorio.

---

## 9. Decisiones pendientes

1. Base del impuesto al capital (Diego).
2. Instrumento que ajusta el presupuesto en el cierre (Héctor y Diego).
3. Estrategia de tiempo de respuesta: biblioteca, estacionarios más diferidos, o modelo reducido (Héctor, con Elena Villalobos para la parte de arquitectura).
4. Qué hacer con la frase sobre el resultado de no existencia (Héctor).
5. Si la pensión universal no contributiva entra en la Capa C desde la versión de junio (Héctor y Diego).
