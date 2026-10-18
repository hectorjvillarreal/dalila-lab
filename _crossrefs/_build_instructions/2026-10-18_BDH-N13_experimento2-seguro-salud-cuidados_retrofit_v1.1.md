---
id: 20261018_BDH_N13_experimento2-seguro-salud-cuidados_build_v1.1
title: "Instrucciones de construcción — Experimento 2 (v1.1): M2 completo, base ENIGH de personas mayores y denominador común"
type: build_instruction
build_type: retrofit
project: BDH
mission: IMSS — Núcleo 13 (Sostenibilidad financiera de la atención quirúrgica)
version: v1.1
supersedes: 20261018_BDH_N13_experimento2-seguro-salud-cuidados_build_v1.0   # parcialmente: ver la sección 0
date: 2026-10-18
language: es
corpus_affected:
  - Missions/Funded/IMSS_Surgical/e_2_imss_nuevoseguro/
  - Missions/Funded/IMSS_Surgical/e_1_imss_subsidiado/anexo_afiliacion_subsidiada/   # solo denominador y fuente de ingresos del SEM (sección 4)
triggered_by:
  - "Revisión de Beth y Cath del documento 'N13 · Experimento 2 … para Cath' (18-10-2026): respuestas a los ocho puntos [REVISAR]"
  - "Decisión de Héctor, 18-10-2026: hacer una nueva versión"
  - "Decisiones de Héctor, 18-10-2026, al ejecutar: el borrador v2 del experimento 1 queda intacto (solo tablas de cambios hasta que Beth decida); la limitación 'sin precedente histórico' se redacta sin esa afirmación si no se encuentra una serie primaria (no se encontró)"
agents_involved: [Beth, Cath, Claude Code]
added_by: Beth
endorsed_by: []          # Cath condiciona su aval a las secciones 1 y 4
protocol: PROTO-RAG-001
status: executed
executed: 2026-10-18   # Claude Code; e_2_imss_nuevoseguro/ (REPORT.md sección 'Experimento 2, v1.1', ANEXO_experimento2_borrador_v2.md) y denominador común en el experimento 1. Verificaciones 7.1-7.6 cumplidas; criterio del SUA no encontrado (pendiente con el IMSS)
executor: Claude Code (Dalila)
---

# Experimento 2, v1.2 de la corrida — cambios

## 0. Alcance

**Esta instrucción modifica la v1.0.** Todo lo que no se cambia aquí sigue vigente, incluidos:

- la regla de lenguaje sobre incidencia legal;
- las afirmaciones prohibidas;
- las limitaciones;
- la regla K2: se mantiene el retiro fijo en términos reales de 1/20 de la reserva de inicio de 2035.

**Prueba de regresión.** Con la configuración de la v1.0 deben reproducirse exactamente las cifras de esa corrida (por ejemplo, el remanente K1 de 2027 = 35,107 mdp). La configuración v1.0 se conserva en `config.yaml`.

**Lo que condiciona el aval de Cath:** las secciones 1 (M2 completo) y 4 (denominador común).

---

## 1. M2 completo y con el mismo peso que la base (condición de Cath)

### 1.1 Corrección

En la v1.0, M2 recortó el ingreso del nuevo seguro pero dejó el déficit de GMP en su valor institucional. Con menos cotizantes, también baja lo que recauda GMP con su prima de 1.5 % del salario.

Ajustar así:

```
razon_M(t)    = Masa_M(t) / Masa_base(t)
Ingreso_GMP_M = Ingreso_GMP_base(t) × razon_M(t)
Deficit_GMP_M = Deficit_GMP_base(t) + Ingreso_GMP_base(t) × (1 − razon_M(t))
```

- **Ingresos de GMP:** fila "Ingresos, escenario base" del Cuadro V.24 (2026: 89,499; 2031: 104,369; 2036: 119,537; 2041: 142,886; 2046: 169,522; 2051: 197,734; 2055: 217,061 mdp de 2026), interpolada como el déficit.
- **Gasto de GMP:** no se ajusta. Los pensionados del horizonte ya están determinados en gran medida por la historia contributiva. Declararlo como supuesto **[REVISAR]**.

### 1.2 Nuevo escenario intermedio M3

Formalización igual a la mitad de la ganancia institucional: la formalidad implícita sube de 34.5 % a 48.8 % en 2054, en lugar de 63.1 %. Mismo método que M2.

### 1.3 Reporte

Base, M3 y M2 van **lado a lado** en el cuadro principal y en la figura. Para cada uno reportar:

- el primer año sin cobertura de GMP, con K1 y con K2;
- el déficit no cubierto en 2054;
- el déficit no cubierto en valor presente;
- el remanente en valor presente.

**Frase obligatoria de apertura de resultados en el anexo** (rellenar con las cifras):

> "Con la formalización que supone la proyección institucional, el 2 % cubre el déficit de GMP en todo el horizonte. Con formalidad constante, lo cubre hasta [año]; con la mitad de esa formalización, hasta [año]."

---

## 2. Personas mayores: base ENIGH

1. **Base nueva.** Tasa de afiliación al IMSS (`inst_1`) por edad simple (o quinquenal si la muestra es chica) y sexo, para 65 años o más, en la ENIGH 2024, multiplicada por CONAPO por año. Es el mismo método del experimento 1.
2. Reportar el remanente por persona de 65+ y de 80+ con esta base.
3. **Conteo máximo.** La base del Informe (16.6 % × 79,178,109) se reporta como conteo máximo y se anota que equivale a 112.4 % de la población nacional de 65+. La base de adscripciones se elimina.
4. Registrar en `NUMBERS.md`:
   - la tasa ENIGH de 65+ y de 80+;
   - el conteo resultante para 2027, 2030, 2040 y 2054;
   - la razón contra la población nacional.

---

## 3. Cuña legal y escalón

### 3.1 Riesgos de Trabajo

En el Cuadro X-2.2 usar la prima promedio vigente del Informe: **1.9078 %** (Cuadro A.3, vigencia de marzo de 2025 a febrero de 2026). Nota al pie: las proyecciones de masa e ingreso usan 1.80 % (libro de Finanzas, promedio 2023-2025).

### 3.2 Artículo 36 de la LSS

Citar del texto vigente de la ley ("corresponde al patrón pagar íntegramente la cuota señalada para los trabajadores, en los casos en que éstos perciban como cuota diaria el salario mínimo"). Verificar la redacción contra el texto publicado por la Cámara de Diputados y registrar la fuente. Si la redacción difiere, usar la oficial.

### 3.3 Escalón de cesantía y vejez

El tramo "1.01 SM a 1.50 UMA" está vacío **desde 2023**, porque el salario mínimo ya rebasaba 1.5 UMA ese año. Verificarlo con el salario mínimo y la UMA de 2023 y registrar ambos. Esto significa que el IMSS ya aplica un criterio operativo.

1. Buscar en documentación pública del IMSS (SUA, guías de cálculo de cuotas, preguntas frecuentes del IDSE o del SUA, criterios normativos) qué tasa aplica a un salario de 1.01 SM cuando rebasa 1.50 UMA.
2. **Solo fuentes del IMSS o del DOF.** Si no se encuentra, mantener las dos lecturas y marcar el punto como **pendiente de confirmación con el IMSS**; Juan Pablo lo preguntará en la visita.
3. Reportar el escalón también para **2026**: +0.43 puntos con la lectura por UMA, frente a +4.435 en 2030.

### 3.4 Lectura agregada del Cuadro X-2.2 (para el borrador)

Agregar un párrafo con este contenido. Es una afirmación de incidencia legal, sin atribuir beneficiarios:

- La cuña legal a cargo del patrón hoy es mayor en el salario mínimo que en el salario promedio y que en 25 UMA. Cifras de la columna (a) de 2026.
- Con los dos experimentos, columna (c), la cuña legal baja 7.1 puntos en el salario mínimo, 3.2 en el promedio y 0.35 en 25 UMA, y se vuelve aproximadamente plana o creciente con el salario.

Confirmar las cifras con la tabla recalculada (cambia con 3.1).

---

## 4. Denominador y fuente de ingresos comunes a los dos experimentos (condición de Cath)

1. **Un solo denominador** para los puntos del salario en todo el anexo: masa con tope de 25 UMA, 337 días y distribución R1 con piso en el salario mínimo (la de la tasa D2).
2. **Recalcular los puntos del salario del experimento 1 (v1.2)** con ese denominador. Reportar la tabla de cambios: cifras viejas, cifras nuevas y diferencia. Los montos en mdp no cambian.
3. **Una sola fuente de ingresos del SEM** para los porcentajes del ingreso del SEM: **Cuadro V.13 del Informe**, por decisión de Héctor.
   - Migrar el experimento 1 a esa fuente.
   - Reportar la tabla de cambios.
   - Los años fuera del Cuadro V.13 se interpolan como el déficit de GMP.
   - Documentar en `NUMBERS.md` que el libro de Finanzas se sigue usando para cotizantes, salarios y supuestos, no para el denominador de ingresos del SEM.
4. **Contraste.** Reportar en `REPORT.md` la diferencia entre los ingresos del SEM del Cuadro V.13 y los del libro para 2026, 2030, 2040 y 2054.

---

## 5. Margen de 2036 sin provisiones

Reportar el margen anual de la base:

- **con provisiones:** como hoy;
- **sin provisiones:** restando del déficit de GMP las provisiones del Cuadro V.19 asignables a GMP en los años ancla, con el mismo método de interpolación.

Una línea en el anexo: el margen mínimo de 2036 refleja en parte cómo se concentran las provisiones.

---

## 6. Borrador del anexo: `ANEXO_experimento2_borrador_v2.md`

1. **X-2.3 Resultados** abre con la frase obligatoria de 1.3.
2. **Cuadro X-2.1** con columnas base, M3 y M2 para 2027, 2030, 2040 y 2054, en mdp y en puntos del salario con el denominador común. Una métrica por celda.
3. **Remanente por persona mayor** con la base ENIGH; el conteo máximo del Informe en nota.
4. **Cuadro X-2.2** recalculado con la prima de Riesgos de Trabajo de 1.9078 %, con el párrafo de 3.4 y el escalón (2026 y 2030; criterio del IMSS si se encontró).
5. **Limitaciones, agregar:**
   - M2 y M3 ajustan el ingreso de GMP pero no su gasto;
   - la formalización institucional (de 34.5 % a 63.1 %) no tiene precedente histórico en México.

   La segunda va como contexto, no como juicio.
6. Pie sin rutas de Dalila.

---

## 7. Verificaciones adicionales

| # | Verificación |
|---|---|
| 7.1 | Prueba de regresión con la configuración v1.0: desviación 0. |
| 7.2 | En la base, razon_M = 1 implica que el déficit de GMP ajustado es igual al del Cuadro V.24. Monotonicidad: déficit M2 > déficit M3 > déficit base en todos los años con ganancia de formalización. |
| 7.3 | La población de 65+ con IMSS según la base ENIGH es ≤ 100 % de la población nacional de 65+ en todos los años. |
| 7.4 | En los puntos del salario del experimento 1 recalculados, los montos en mdp no cambian (desviación 0); solo cambian los puntos. |
| 7.5 | En el Cuadro X-2.2, columna (b) = columna (a) − 3 con la nueva prima de Riesgos de Trabajo. |
| 7.6 | Ninguna salida contiene 2055; todas las cifras nuevas están en `NUMBERS.md`. |

---

## 8. Reporte

Agregar a `REPORT.md` una sección "Experimento 2, v1.1" con:

1. Resultados de base, M3 y M2 (sección 1.3).
2. Remanente por persona mayor con la base ENIGH.
3. Resultado de la búsqueda del criterio del SUA.
4. Tablas de cambios del experimento 1 (puntos del salario y % de los ingresos del SEM).
5. Verificaciones de la sección 7.
6. Decisiones propias marcadas como **[REVISAR]**.

Actualizar el documento para Cath solo si Héctor lo indica. Hacer commit y archivar esta instrucción en `_crossrefs/_build_instructions/`.
