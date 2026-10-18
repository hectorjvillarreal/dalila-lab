---
id: 20261018_BDH_N13_experimento2-seguro-salud-cuidados_build_v1.3
title: "Instrucciones de construcción — Experimento 2 (v1.3): K2 como regla base, escenario de ritmo histórico y limpieza antes de redacción"
type: build_instruction
build_type: retrofit
project: BDH
mission: IMSS — Núcleo 13 (Sostenibilidad financiera de la atención quirúrgica)
version: v1.3
supersedes: 20261018_BDH_N13_experimento2-seguro-salud-cuidados_build_v1.2   # parcialmente: ver la sección 0
date: 2026-10-18
language: es
corpus_affected:
  - Missions/Funded/IMSS_Surgical/e_2_imss_nuevoseguro/
triggered_by:
  - "Revisión de Beth y Cath del documento 'N13 · Experimento 2 … (v1.2)' (18-10-2026); aval preliminar de Cath a la v1.2"
  - "Decisión de Héctor, 18-10-2026: K2 como regla base y escenario de ritmo histórico, antes de pasar a redacción"
  - "Decisiones de Héctor, 18-10-2026, al ejecutar: MH con tope en la formalidad de la base (6.3 se aplica desde 2035); reserva final = saldo de cierre de 2054"
agents_involved: [Beth, Cath, Claude Code]
added_by: Beth
endorsed_by: [Cath]      # aval de Cath a la v1.2 como resultado preliminar; K2 como base es propuesta suya
protocol: PROTO-RAG-001
status: executed
executed: 2026-10-18   # Claude Code; e_2_imss_nuevoseguro/ (REPORT.md sección 'Experimento 2, v1.3', ANEXO_experimento2_borrador_v4.md) y documento para Beth y Cath (v1.3). Verificaciones 6.1-6.7 cumplidas; decisiones de Héctor: MH con tope en la base y reserva final = saldo de cierre de 2054
executor: Claude Code (Dalila)
---

# Experimento 2, v1.3 — cambios

## 0. Alcance

**Esta instrucción modifica la v1.2.** Todo lo que no se cambia aquí sigue vigente: diseño, escenarios base/M3/M2, sensibilidades sin provisiones y S-masa, regla K2 precisada en la v1.2, denominador común, Cuadro V.13, regla de lenguaje sobre incidencia legal y afirmaciones prohibidas.

**Es la última versión de modelo antes de redacción.** Después de esta corrida solo se cambia el texto.

**Prueba de regresión.** Con la configuración v1.2 deben reproducirse exactamente sus cifras, por ejemplo:

- K2, base: reserva de inicio de 2035 = 271,337 mdp; reserva de inicio de 2054 = 135,034 mdp.
- K2, M2: agotamiento en 2038.
- K1, M3: primer año sin cobertura 2035 con provisiones y 2042 sin ellas.

Conservar la configuración v1.2 en `config.yaml`.

---

## 1. K2 como regla base

**Decisión de Héctor, a propuesta de Cath.** En la base, K2 da cerca del mismo valor presente que K1: 747,074 mdp para cuidados más la reserva de 2054 (135,034 mdp, unos 59,000 en valor presente), frente a 801,935 de K1. En M3 y M2, K2 reduce mucho el déficit no cubierto.

1. **K2 pasa a ser la regla base** en el cuadro principal, en la figura y en la frase de apertura. K1 se reporta como variante "sin reserva" en un cuadro aparte.
2. **Cuadro X-2.1 (principal)**, para base, M3 y M2 en 2027, 2030, 2040 y 2054, en mdp y en puntos del salario:
   - ingreso del nuevo seguro;
   - déficit de GMP;
   - depósito a la reserva (antes de 2035) o retiro de la reserva para GMP (desde 2035);
   - gasto en cuidados;
   - déficit no cubierto.

   Una métrica por fila.
3. **Cuadro resumen (K2 y K1 lado a lado)**, para base, M3 y M2:
   - último año con cobertura completa de GMP;
   - déficit no cubierto en 2054 y en valor presente;
   - cuidados en valor presente;
   - **reserva al final del horizonte en valor presente** (fila nueva; en K1 es 0);
   - cuidados más reserva final, en valor presente.

   Declarar en una nota el año al que se descuenta y usar el mismo en todos los valores presentes del anexo. Si hasta ahora no se ha usado el mismo año, reportarlo.
4. **Remanente por persona mayor** con K2, en la base: 2040 y 2054, para 65+ y 80+. En 2027 y 2030 es 0, porque no hay gasto en cuidados antes de 2035; decirlo en una oración. Las cifras de K1 van en nota, como referencia.
5. **Frase obligatoria de apertura de X-2.3** (rellenar con las cifras; ajustar si alguna celda no corresponde):

> "Con una reserva que se acumula hasta 2034, el 2 % cubre el déficit de GMP en todo el horizonte con la formalización que supone la proyección institucional y también con la mitad de esa formalización; con formalidad constante, lo cubre hasta [año]. Sin reserva, la cobertura con la mitad de la formalización llega hasta [año] ([año] sin las provisiones de GMP), y con formalidad constante hasta [año] ([año])."

---

## 2. Escenario de ritmo histórico (MH)

La formalización 2005-2025 avanzó 6.6 puntos en 20 años; la proyección supone 29.1 puntos en 29 años.

1. **Definición.** Formalidad 2025 = 34.0 % (libro). Desde ahí sube cada año al ritmo histórico: (37.7 − 31.1) / 20 puntos por año, con los extremos exactos de la serie de la v1.2, no con una regresión. Valor de referencia para verificar: unos 43.6 % en 2054. Mismo método de masa y de ajuste del ingreso de GMP que M2 y M3.
2. **Ubicación.** **Solo** en el cuadro de sensibilidades (X-2.3) y en una oración del texto. No va en el cuadro principal ni en la figura. Base, M3 y M2 siguen siendo los escenarios con el mismo peso.
3. **Cuadro X-2.3 ampliado.** Último año con cobertura completa de GMP para base, M3, MH y M2, con K2 y con K1. Columnas: con y sin provisiones, por masa del libro y por S-masa (8 columnas, o dos paneles: K2 y K1).
4. **Oración en el texto** (descriptiva, sin juicio): "Si la formalización avanzara al ritmo de 2005-2025, la formalidad llegaría a [x] % en 2054, entre M2 y M3; con reserva, el 2 % cubriría el déficit de GMP hasta [año]."

---

## 3. Una sola convención para las fechas

En todo el anexo y en el documento usar **"último año con cobertura completa"** ("lo cubre hasta [año]"), no "primer año sin cobertura". Renombrar las filas de los cuadros y convertir las cifras. Verificar que la frase de apertura y los cuadros coincidan.

---

## 4. Ajustes menores

1. S-masa se rotula como **"cota inferior del ingreso"**, no como "la variante más conservadora". Una oración explica por qué: combina el nivel propio de 2027 con el crecimiento del Informe.
2. El párrafo de K2 en Diseño se mantiene (ya incluye la regla precisada) y agrega que la reserva que queda en 2054 se reporta en valor presente.
3. La limitación de Cuidados agrega: con K2, el retiro fijo de 1/20 no agota la reserva en 20 años; la reserva final es un recurso disponible, no un gasto.

Guardar como `ANEXO_experimento2_borrador_v4.md`. La v3 se conserva.

---

## 5. Limpieza del documento para Beth y Cath

Actualizar el documento en Claude Docs. El título termina en "(v1.3)". El contenido queda así, en este orden:

1. **Versiones.** Un historial breve, de seis líneas como máximo, de v1.0 a v1.3: qué cambió en cada una.
2. **Borrador v4** completo.
3. **Verificaciones** de la v1.3 (sección 6) y, en una tabla aparte, las de la v1.2 (8.1-8.7) y las del borrador v3 del experimento 1 (3.1-3.5), con su resultado.
4. **Pendientes:** criterio del SUA (Juan Pablo), recaudación efectiva del Infonavit, discrepancia de derechohabientes del N13 (Juan Pablo).

**Se eliminan:**

- la nota de la v1.1;
- la tabla "Los ocho puntos";
- la lista "Decisiones de la ejecución que conviene revisar" (ya aceptadas en la v1.2);
- la frase de que no se encontró una serie primaria de formalización;
- las tablas de cambios del experimento 1 de la v1.1, que se sustituyen por una línea: el borrador v3 del experimento 1 cambió 112 cifras, y el detalle está en `tablas/exp1_borrador_v2_a_v3.csv`.

El pie no lleva rutas de Dalila.

---

## 6. Verificaciones

| # | Verificación |
|---|---|
| 6.1 | Regresión con la configuración v1.2: desviación 0. |
| 6.2 | Las cifras de K2 y K1 del cuadro resumen coinciden con las de la v1.2 (solo cambia el orden, la convención de fechas y las filas nuevas). |
| 6.3 | MH: formalidad entre M2 y M3 en todos los años 2026-2054; la masa y el déficit ajustado de MH quedan entre los de M2 y M3 en todos los años; último año con cobertura de MH entre el de M2 y el de M3 en cada columna. |
| 6.4 | Reserva final en valor presente: igual a la reserva de inicio de 2054 más el movimiento de 2054, descontada al año declarado; en K1 es 0. |
| 6.5 | Ninguna fecha del anexo usa "primer año sin cobertura"; la frase de apertura coincide con los cuadros. |
| 6.6 | El documento no contiene las secciones eliminadas en la sección 5. |
| 6.7 | Ninguna salida contiene 2055; todas las cifras nuevas están en `NUMBERS.md`. |

---

## 7. Reporte

Agregar a `REPORT.md` una sección "Experimento 2, v1.3" con:

1. El cuadro resumen K2 y K1.
2. MH y el Cuadro X-2.3 ampliado.
3. La frase de apertura resultante.
4. El año de descuento de los valores presentes y, si se unificó, qué cifras cambiaron.
5. Las verificaciones de la sección 6.
6. Las decisiones propias marcadas como **[REVISAR]**.

Hacer commit y archivar esta instrucción en `_crossrefs/_build_instructions/`. Cambiar `status` de la v1.2 a `superseded` en el archivo y de esta a `executed` al terminar.
