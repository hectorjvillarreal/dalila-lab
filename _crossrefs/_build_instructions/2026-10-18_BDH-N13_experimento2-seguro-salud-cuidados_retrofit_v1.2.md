---
id: 20261018_BDH_N13_experimento2-seguro-salud-cuidados_build_v1.2
title: "Instrucciones de construcción — Experimento 2 (v1.2): sensibilidad a provisiones y a la masa, orden de usos en K2 y contexto de formalización"
type: build_instruction
build_type: retrofit
project: BDH
mission: IMSS — Núcleo 13 (Sostenibilidad financiera de la atención quirúrgica)
version: v1.2
supersedes: 20261018_BDH_N13_experimento2-seguro-salud-cuidados_build_v1.1   # parcialmente: ver la sección 0
date: 2026-10-18
language: es
corpus_affected:
  - Missions/Funded/IMSS_Surgical/e_2_imss_nuevoseguro/
triggered_by:
  - "Revisión de Beth y Cath del documento 'N13 · Experimento 2 … (v1.1)' (18-10-2026)"
  - "Decisión de Héctor, 18-10-2026: adelante con la v1.2"
agents_involved: [Beth, Cath, Claude Code]
added_by: Beth
endorsed_by: [Cath]      # aval de Cath a las secciones 1 y 4 de la v1.1; la v1.2 no lo condiciona
protocol: PROTO-RAG-001
status: superseded   # por 20261018_BDH_N13_experimento2-seguro-salud-cuidados_build_v1.3 (18-10-2026)
executed: 2026-10-18   # Claude Code; e_2_imss_nuevoseguro/ (REPORT.md sección 'Experimento 2, v1.2', ANEXO_experimento2_borrador_v3.md). Verificaciones 8.1-8.7 cumplidas; K2 cambia en M3 y M2; la fecha de M3 depende de las provisiones; serie de formalización con fuentes primarias (IMSS, ENOE); variante opcional de personas mayores no construida (sin proyección de pensionados en el Informe)
executor: Claude Code (Dalila)
---

# Experimento 2, v1.2 — cambios

## 0. Alcance

**Esta instrucción modifica la v1.1.** Todo lo que no se cambia aquí sigue vigente: diseño, escenarios base/M3/M2, regla de lenguaje sobre incidencia legal, afirmaciones prohibidas, denominador común y fuente de ingresos del SEM (Cuadro V.13).

**Decisiones de la ejecución v1.1 que quedan aceptadas** (registrarlas en `NUMBERS.md` como decisiones aprobadas):

- M3 se mide desde 2025 (34.0 % → 48.56 % en 2054), con la misma referencia que M2.
- Los puntos del salario de cada escenario usan la masa de ese escenario (misma definición, valores propios).
- ENIGH por grupos quinquenales.
- La limitación sobre la formalización no usa "sin precedente histórico" (se sustituye por datos; sección 4).

**Prueba de regresión.** Con la configuración v1.1 deben reproducirse exactamente sus cifras, por ejemplo: primer año sin cobertura K1 = 2035 (M3) y 2033 (M2); margen de la base en 2036 = 19,991 mdp; remanente K1 base 2027 = 35,107 mdp. Conservar la configuración v1.1 en `config.yaml`.

**Lo que es titular y lo que es sensibilidad.** El resultado principal sigue siendo el de la v1.1 (déficit institucional del Cuadro V.24, con provisiones; masa del libro). Las secciones 1 y 2 son sensibilidades que van en el anexo, pero no reemplazan el cuadro principal.

---

## 1. M3 y M2 sin provisiones

En la v1.1, el primer año sin cobertura de M3 (2035) coincide con el pico de provisiones de 2036, que la interpolación reparte entre 2032 y 2040. En 2040 lo no cubierto en M3 es de solo 648 mdp. Hay que saber si la fecha la marcan las provisiones.

1. Aplicar a M3 y M2 el mismo método del margen de 2036 sin provisiones de la v1.1: restar del déficit de GMP las provisiones del Cuadro V.19 asignables a GMP en los años ancla e interpolar igual. El ajuste de ingreso de GMP por `razon_M` no cambia.
2. Reportar, para base, M3 y M2, con y sin provisiones:
   - primer año sin cobertura (K1 y K2);
   - déficit no cubierto en valor presente (K1 y K2);
   - margen mínimo del horizonte y su año.
3. **Frase de apertura.** Si el primer año sin cobertura de M3 o M2 cambia sin provisiones, la frase de la v1.1 se mantiene y se agrega, en la misma oración o en la siguiente, el rango: "… hasta 2034 (hasta [año] sin las provisiones de GMP)". Si no cambia, la frase queda igual y se anota en `REPORT.md` que la fecha no depende de las provisiones.

---

## 2. Consistencia de masa entre el libro y el Informe

El ingreso de GMP del Cuadro V.24 equivale a 1.69 % de la masa propia en 2027, 1.63 % en 2030 y 1.55 % en 2040 y 2054 (cálculo de Cath con las cifras de la v1.1). Si las dos fuentes supusieran el mismo crecimiento de la masa, la razón sería casi constante. La holgura de la base puede venir en parte de combinar la masa del libro con el déficit del Informe.

1. **Diagnóstico.** Calcular `r(t) = Ingreso_GMP_V24(t) / Masa_propia_base(t)` para todos los años 2027-2054 y guardarlo en `tablas/razon_ingresoGMP_masa.csv`. Reportar el valor en 2027, 2030, 2036, 2040 y 2054 y la caída porcentual 2027-2054.
2. **Sensibilidad S-masa.** El ingreso del nuevo seguro crece al ritmo del ingreso de GMP del Informe:
   ```
   Ingreso_nuevo_S(t) = Ingreso_nuevo_base(2027) × Ingreso_GMP_V24(t) / Ingreso_GMP_V24(2027)
   ```
   - En M3 y M2, multiplicar además por `razon_M(t)`, como en la v1.1.
   - El déficit de GMP es el mismo de la v1.1 en cada escenario.
   - Correr con y sin provisiones.
3. Reportar para S-masa lo mismo que en 1.2. Referencia de Cath (aproximada, para verificar): en la base, el margen de 2036 baja de 19,991 a unos 7,300 mdp y el de 2040 de 40,745 a unos 26,000; la base sigue cubriendo todo el horizonte.
4. **En el anexo:** un párrafo corto en X-2.3, después del cuadro resumen, con el resultado de S-masa para los tres escenarios. Sin juicio sobre cuál proyección es mejor. Explicar en una oración que el libro y el Informe suponen trayectorias de masa distintas.

---

## 3. Orden de usos en K2

El principio del diseño es que el nuevo seguro cubre primero GMP. En M3, K2 cubre hasta 2050, así que la reserva ya paga GMP. Falta confirmar qué pasa con el retiro fijo para cuidados en esos años.

1. **Documentar** en `REPORT.md` lo que hace el código v1.1, año por año, en los años con faltante de GMP.
2. **Regla K2 (precisión, decisión de Beth).** Desde 2035, cada año:
   1. El ingreso del año cubre GMP.
   2. Si no alcanza, la diferencia sale de la reserva.
   3. Los cuidados reciben el remanente del año (si lo hay) más el retiro fijo de 1/20 de la reserva de inicio de 2035, **solo en los años sin faltante de GMP** y solo si la reserva alcanza. En los años con faltante, el retiro fijo se suspende y la reserva se usa solo para GMP.
   4. Si la reserva se agota, el faltante restante es déficit no cubierto.
3. Si el código v1.1 ya hacía esto, la v1.2 no cambia cifras de K2; anotarlo. Si no, recalcular K2 en los tres escenarios y reportar la tabla de cambios (antes, después, diferencia).
4. **Trayectoria de la reserva.** Nueva tabla `tablas/reserva_K2.csv` y cuadro breve en el anexo: saldo al inicio de 2035, 2040, 2045, 2050 y 2054; retiros para GMP y para cuidados acumulados 2035-2054; año de agotamiento, si existe. Para base, M3 y M2, con provisiones.

---

## 4. Contexto de la formalización: serie histórica

La base supone que la razón cotizantes/ocupados sube de 34.0 % en 2025 a 63.13 % en 2054, unos 29 puntos en 29 años. La limitación debe dar el contexto con datos, no con un juicio.

1. **Construir la serie 2005-2025** con fuentes primarias:
   - Numerador: trabajadores asegurados en el IMSS (datos abiertos del IMSS o Memoria Estadística), con la definición más cercana a la de "cotizantes" del libro de Finanzas.
   - Denominador: población ocupada de la ENOE (INEGI); para años previos a 2005, no usar la ENE.
   - Promedio anual, o cuarto trimestre si el promedio no está disponible; documentar la elección.
2. **Empalme con el libro.** Comparar el valor de 2025 de la serie con el 34.0 % del libro y reportar la diferencia. Si difieren por definición, reportar ambas sin ajustar.
3. **En la limitación**, una oración con el dato: "Entre 2005 y 2025, la razón pasó de X % a Y % (Z puntos en 20 años); la proyección supone 29 puntos en 29 años." Sin calificativos.
4. Si una fuente no se puede descargar, no sustituirla con cifras de memoria ni con fuentes secundarias: dejar la oración pendiente y reportarlo.

---

## 5. Personas mayores: consistencia por cohorte

La tasa ENIGH de afiliación de 65+ (46.6 %) se mantiene constante por edad y sexo, mientras la base supone que la formalidad sube a 63 %. Las cohortes que llegan a 65+ hacia 2040-2054 tendrían más afiliación.

1. **Obligatorio:** nota bajo el cuadro de remanente por persona: en la base, las cifras de 2040 y 2054 son una cota superior, porque la afiliación de 65+ se mantiene en su nivel de 2024.
2. **Opcional, solo si existe la fuente:** si el Informe trae una proyección de pensionados del IMSS por año, agregar una variante que escale la afiliación de 65+ con el crecimiento de esa proyección, con tope de 100 % por celda. Reportarla en nota. Si no existe, no construir la variante y anotarlo.

---

## 6. Cuña legal: lectura de 2026 y 2030

1. **Fechar el párrafo de lectura.** La lectura actual vale para 2026 y así debe decirlo.
2. **Agregar 2030:**
   - Con la ley vigente, la cuña a cargo del patrón ya es menor en el salario mínimo (24.793 %) que en el promedio (29.464 %), por el calendario de cesantía y vejez.
   - Con la columna (c) baja 5.127 puntos en el mínimo, 3.209 en el promedio y 0.349 en 25 UMA. Confirmar con la tabla.
3. **Escalón.** Una oración: ninguno de los dos experimentos modifica el escalón arriba del salario mínimo; con la lectura por UMA, en 2030 es de +4.435 puntos con la ley vigente y de [cifra] con la columna (c). Calcular la cifra (c) con la tabla.
4. **D2 en salarios altos.** Una oración: en la columna (c), la cuña sube 2.651 puntos en 25 UMA frente a (b), porque D2 sustituye la cuota fija por una tasa proporcional. Confirmar con la tabla.
5. **Aportación federal fuera de la cuña.** La cuña legal total suma solo contribuciones a cargo del patrón y del trabajador. La aportación federal se reporta aparte, en la misma nota, como transferencia del Gobierno Federal. Recalcular la cifra de 34.945 % → 31.945 % en 2030 con esa definición y reportar ambas.

---

## 7. Ajustes de texto en el borrador

Solo estos; la redacción general sigue pendiente.

1. "Recaudación teórica actual de 5 % para el Infonavit … en 2027" → "recaudación teórica de 5 % para el Infonavit en 2027".
2. En Limitaciones, sustituir "en el largo plazo, buena parte de las contribuciones a cargo del patrón suele trasladarse al salario" por: "quién soporta la cuña depende de las elasticidades de oferta y demanda de trabajo; el ejercicio no lo estima". Sin cita.
3. Agregar al final de X-2.3 una oración descriptiva: "Fuera del escenario base, el nuevo seguro financia sobre todo el déficit de GMP; el remanente para cuidados depende de la formalización." Sin juicio adicional.
4. Pie sin rutas de Dalila (se mantiene).

Guardar como `ANEXO_experimento2_borrador_v3.md`. La v2 se conserva.

---

## 8. Verificaciones

| # | Verificación |
|---|---|
| 8.1 | Regresión con la configuración v1.1: desviación 0 en las tablas de la v1.1. |
| 8.2 | Sin provisiones, el déficit de GMP es menor o igual al de con provisiones en todos los años y escenarios; con provisiones, coincide con la v1.1. |
| 8.3 | En S-masa, `Ingreso_nuevo_S(2027) = Ingreso_nuevo_base(2027)` y la razón `Ingreso_nuevo_S(t) / Ingreso_GMP_V24(t)` es constante en la base. |
| 8.4 | En K2, ningún año con faltante de GMP tiene retiro fijo para cuidados; la identidad de la reserva se cumple exactamente (saldo inicial + depósitos + intereses − retiros = saldo final). |
| 8.5 | La serie de formalización usa solo fuentes primarias; cada valor tiene fuente y fecha de descarga en `NUMBERS.md`. |
| 8.6 | En el Cuadro X-2.3, (b) = (a) − 3 se mantiene; la cuña sin aportación federal es menor que la cuña con ella en todos los niveles. |
| 8.7 | Ninguna salida contiene 2055; todas las cifras nuevas están en `NUMBERS.md`. |

---

## 9. Reporte

Agregar a `REPORT.md` una sección "Experimento 2, v1.2" con:

1. Base, M3 y M2 con y sin provisiones (sección 1) y la frase de apertura resultante.
2. Diagnóstico `r(t)` y resultados de S-masa (sección 2).
3. Qué hacía el código en K2, si cambió y la trayectoria de la reserva (sección 3).
4. Serie de formalización 2005-2025 y empalme con el libro (sección 4).
5. Nota o variante de personas mayores (sección 5).
6. Cifras nuevas del Cuadro X-2.3 (sección 6).
7. Verificaciones de la sección 8.
8. Decisiones propias marcadas como **[REVISAR]**.

Actualizar el documento para Beth y Cath con una sección "v1.2" al inicio (qué cambió, en cinco líneas como máximo) y el borrador v3. Hacer commit y archivar esta instrucción en `_crossrefs/_build_instructions/`.
