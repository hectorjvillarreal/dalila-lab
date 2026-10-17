---
doc_id: 20261017_BDH_N13_BRIEF_consultas-anexo-afiliacion-subsidiada_v1.0
title: "Consultas previas a la ejecución: anexo de afiliación subsidiada al SEM (Núcleo 13)"
project: BDH
mission: IMSS — Núcleo 13 (Sostenibilidad financiera de la atención quirúrgica)
type: session_brief
version: 1.0
date: 2026-10-17
language: es
prepared_by: Claude Code (lectura de 20261017_BDH_N13_anexo-afiliacion-subsidiada_build_v1)
for: Beth
cc: Cath, Héctor
status: resolved   # fallos en 20261017_BDH_N13_anexo-afiliacion-subsidiada_build_v1.1, sección 11
refers_to:
  - 20261017_BDH_N13_anexo-afiliacion-subsidiada_build_v1
---

# Consultas antes de ejecutar el anexo de afiliación subsidiada

**No se ha ejecutado nada.** No hay carpeta `anexo_afiliacion_subsidiada/` ni `config.yaml`, y no se ha hecho ningún commit. Héctor pidió resolver estos puntos antes de la fase F0.

Las cifras semilla que se pueden comprobar con aritmética cuadran:

- La cuota fija equivale a 14.30 % del salario mínimo de 2025 y a 9.66 % en 2030.
- La aportación federal es de 16.78 pesos al día.
- Asegurados más trabajadores del IMSS: 22,352,586.
- Seguro de Salud para la Familia: −17,950 mdp, es decir, cubre 17 % de su gasto.
- La reconstrucción de la aportación federal al SEM-A da unos 144.6 mil millones contra 146,457 mdp: diferencia de 1.3 %.

Los problemas que siguen son de **diseño**, no de datos.

Constantes usadas abajo: UMA = 113.14; UMA·365 = 41,296 pesos; P* = 0.3523·UMA·365 = 14,549 pesos al año.

---

## 1. El Bloque B subsidia a formales de ingreso alto (bloqueante)

**El problema.** El pago del par formal π_F(m) incluye el excedente de 1.5 % sobre (m − 3) UMA, así que crece sin límite con *m*. El pago del informal π(m) tiene tope en κ·P*. La sección 4.3 dice: *"Donde π_F(m) > π(m), la cuota patronal fija se reduce para que el par formal pague π(m). El Gobierno Federal compensa la diferencia."* Con eso, todo formal cuyo π_F supere el tope recibe un subsidio federal.

**En G2** (κ = 20.40/35.23), el tope es 0.2040·UMA·365 = 8,424 pesos. Cualquier m > 3 produce una "violación":

| m (UMA) | π_F(m) | π(m) con s = 0 | Costo_B por formal al año |
|---|---|---|---|
| 3.0 | 8,424 | 8,424 | 0 |
| 5.54 (SBC promedio, 627 pesos/día) | 9,998 | 8,424 | 1,574 |
| 10 | 12,760 | 8,424 | 4,336 |
| 25 (tope del SBC) | 22,052 | 8,424 | 13,628 |

El costo por formal es 619.4·(m − 3) pesos al año. Lo recibiría la mayoría de los cotizantes, porque el SBC promedio está en 5.5 UMA.

**En G1** también ocurre. Si se iguala π_F(m) = P*, el umbral sale en m = 3 + (0.3523 − 0.2040)/0.015 ≈ **12.9 UMA**. Todo formal entre 12.9 y 25 UMA recibiría subsidio. La variante con la cuota de gastos médicos para pensionados (+0.01425·m·UMA·365) baja el umbral todavía más.

En la lectura inicial reporté esto solo para G2; también afecta a G1.

**Opciones:**

- **(a) Recomendada.** Que el Bloque B corrija solo en la dirección de bajo salario: aplicarlo solo donde s(m) > 0, o solo donde m ≤ m1. Por arriba de m1 no habría ajuste. Esto requiere aceptar que, arriba de m1, el par formal paga más que el informal. Entonces la regla de no arbitraje (3.1) tendría que reformularse de forma que esa diferencia en contra de los formales de ingreso alto no cuente como subsidio a la informalidad.
- **(b)** Corregir del lado del informal: sumar a π(m) el mismo excedente 0.015·max(0, m − 3)·UMA·365. Así la "tabla única" de 3.2 se cumple de verdad y el Bloque B solo opera en el tramo subsidiado. El costo es que el informal de ingreso alto paga más que P* y G2 cambia de sentido.
- **(c)** Mantener el texto literal y reportar el Costo_B completo. No lo recomiendo: el monto lo dominaría un subsidio a salarios altos que nadie propuso.

**Pregunta:** ¿(a), (b) u otra? Con (a) o (c) hay que reescribir la regla 3.1; con (b), la regla 3.2. Pide además la verificación 7.6: cero violaciones en todos los escenarios S y G.

---

## 2. U2: el precio por persona debe dividirse entre (1 + h)

La sección 4.2 define el precio individual como P*/h, con *h* = "derechohabientes por titular". El respaldo R2 calcula *h* como "personas con IMSS como beneficiarias por un familiar, entre titulares". Ese conteo **excluye al titular**.

Si P* cubre a la familia completa, el precio por persona es P*/(1 + h). Con unos 3 derechohabientes por cotizante (sección 3.6), h ≈ 2:

| Fórmula | Precio por persona |
|---|---|
| P*/h | 7,274 pesos |
| P*/(1 + h) | 4,850 pesos |

Con la fórmula actual, el precio queda **50 % arriba**.

**Pregunta:** ¿P*/(1 + h) con *h* = beneficiarios? ¿O redefinir *h* como derechohabientes totales por titular, titular incluido, y conservar P*/h?

---

## 3. Tabla única (3.2) frente a desigualdad (3.1)

- La sección 3.2 dice que formales e informales enfrentan **la misma** función π(m).
- La sección 3.1 solo exige que el informal pague **al menos** lo que paga el formal.

En G1 con s = 0, el informal paga 14,549 pesos y el formal de m ≤ 3 paga 8,424. Eso cumple 3.1 y viola 3.2. Este punto se resuelve junto con el 1: la opción (b) cumple 3.2 y la opción (a) cumple solo 3.1.

**Pregunta:** ¿3.2 se aplica a todo el rango de *m* o solo al tramo subsidiado (m < m1)?

---

## 4. Frontmatter de la instrucción frente a PROTO-RAG-001

El esquema `build_instruction` del protocolo (sección "Build instruction frontmatter") pide `build_type`, `corpus_affected`, `triggered_by` y `agents_involved`, y `status` debe tomar uno de estos valores: `pending_execution | executed | superseded`.

La instrucción v1 trae `status: ready_for_execution`, que no está en esa lista. Tampoco trae `build_type`, `corpus_affected` ni `triggered_by`. Además, `endorsed_by` está vacío: faltan Cath y Héctor.

**Propuesta:** que la v1.1 venga conforme al protocolo (`status: pending_execution`, `build_type: initial_scaffold`) y con los avales registrados antes de ejecutarla.

---

## 5. Ubicación (sección 6.1)

Los insumos I1 (Informe) e I2 (libro de Finanzas 07/09) ya están en `Missions/Funded/IMSS_Surgical/e_1_imss_subsidiado/`.

**Propuesta:** crear `anexo_afiliacion_subsidiada/` dentro de esa carpeta y no crear `Missions/IMSS_N13/`. ¿De acuerdo?

---

## Qué se necesita para arrancar

Una v1.1 de la instrucción, o una nota de fallo, que resuelva:

1. La regla del Bloque B y la redacción de 3.1 y 3.2 (puntos 1 y 3).
2. La fórmula de U2 (punto 2).
3. El frontmatter y los avales (punto 4).
4. La ubicación (punto 5).

La fase F0 (inventario y sumas de control de la sección 7.1) no depende de estos fallos. Puede correr en cuanto Héctor lo indique.
