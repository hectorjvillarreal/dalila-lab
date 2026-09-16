# Series históricas de la casa, 2020–2026

**Precarga §3.7 de `INSTRUCCIONES_preparacion_2027.md`.** Construidas el 2026-09-07.
Guion: `_herramientas/series_historicas.py`. Datos:
`series_historicas_ex_ante.csv`, `series_historicas_aprobado.csv`, y los insumos
renglón por renglón en `series_insumos_*.csv`.

**En 2027 sólo se agrega un punto.** El guion es paramétrico: no se toca para correr
otro año.

---

## 0. La regla que manda: ninguna línea híbrida

**Ex ante con ex ante, aprobado con aprobado, en archivos distintos.** La versión
anterior de estas series ---`documento_2025/datos/razones_estructurales.csv`--- las
tenía en una sola tabla, y en algunas filas mezclaba analíticos aprobados con cifras
del CGPE. **El CGPE se publica una sola vez, con el paquete: no existe un CGPE
aprobado.** De modo que toda razón que use el CGPE es ex ante por construcción, y en la
serie aprobada esas filas van **vacías a propósito**, no por falta de dato.

Son cuatro filas en esa condición: las dos de gastos obligatorios (denominador del
Anexo 3 del decreto), la de pensiones más costo financiero, y las dos de deuda.

---

## 1. Lo que esta corrida descongeló

**La serie ex ante de pensiones IMSS / cuotas estaba detenida desde 2021.** La bitácora
del 2026-09-06 la declaró interrumpida «porque la exposición de motivos del PPEF no
existe para 2022–2026».

**No hacía falta esa exposición de motivos.** El numerador es el tipo de gasto 4 del
IMSS y sale del **analítico del proyecto**, que existe para los siete ejercicios en
`Analiticos_Historico/{t}/Proyecto/`. Faltaban en carpeta los de 2022 y 2023; se
descargaron y quedaron en el manifiesto.

**La serie pasa de dos puntos a siete**, y los dos que ya existían se reprodujeron al
milésimo: 1,31 en 2020 y 1,46 en 2021, contra 1,306 y 1,463 calculados de cero. **Es la
prueba de que la reconstrucción mide el mismo objeto.**

---

## 2. Las series

### Ex ante (línea P) — proyecto contra proyecto

| razón | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|
| Impuestos / gastos obligatorios con pensiones | | | | | 0,674 | 0,689 | **0,695** |
| Impuestos + cuotas / gastos obligatorios con pensiones | | | | | 0,747 | 0,768 | **0,771** |
| Pensiones y jubilaciones + costo financiero / impuestos | | | | | 0,559 | 0,571 | **0,561** |
| Pensiones IMSS / cuotas de seguridad social | 1,306 | 1,463 | 1,545 | 1,593 | 1,627 | 1,603 | **1,575** |
| Gasto en salud del IMSS / cuotas | 0,854 | 0,852 | 0,866 | 0,841 | 0,851 | 0,798 | **0,867** |
| Pensiones IMSS+ISSSTE / salud IMSS+ISSSTE | 1,920 | 2,109 | 2,148 | 2,227 | 2,282 | 2,412 | **2,204** |
| Función Educación / pensiones y jubilaciones | 0,813 | 0,764 | 0,733 | 0,709 | 0,680 | 0,655 | **0,682** |
| Función Educación / pensiones totales | 0,719 | 0,669 | 0,602 | 0,558 | 0,512 | 0,495 | **0,500** |
| Costo financiero / impuestos | | | | | 0,256 | 0,262 | **0,269** |
| SHRFSP / impuestos, en años de recaudación | | | | | 3,40 | 3,51 | **3,47** |

### Aprobado — aprobado contra aprobado

Idéntica en las cinco filas que salen sólo de analíticos y ley de ingresos, salvo en las
dos de educación. Las cuatro filas que necesitan CGPE o Anexo 3 quedan vacías por la
razón de §0.

| razón | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|
| Función Educación / pensiones y jubilaciones | 0,815 | 0,764 | 0,733 | 0,709 | 0,689 | 0,662 | **0,688** |
| Función Educación / pensiones totales | 0,718 | 0,669 | 0,601 | 0,556 | 0,518 | 0,501 | **0,505** |

---

## 3. Verificación: todo punto ya registrado se reprodujo

Ningún valor se copió de una corrida anterior. Se recalcularon todos y **se cotejaron
contra los que ya estaban registrados**:

| punto registrado | dónde estaba | recalculado | ¿cierra? |
|---|---|---|---|
| Pensiones IMSS / cuotas, ex ante 2020 y 2021: 1,31 y 1,46 | bitácora 2024 | 1,306 y 1,463 | **sí** |
| Pensiones IMSS / cuotas, aprobado 2022–2025: 1,545 · 1,593 · 1,627 · 1,603 | `razones_estructurales.csv` | idénticos | **sí** |
| Salud IMSS / cuotas, aprobado 2021 · 2024 · 2025: 0,85 · 0,851 · 0,798 | íd. | 0,852 · 0,851 · 0,798 | **sí** |
| Pensiones IMSS+ISSSTE / salud, 2021 · 2024 · 2025: 2,11 · 2,282 · 2,412 | íd. | 2,109 · 2,282 · 2,412 | **sí** |
| Educación / pensiones, aprobado 2023 · 2024 · 2025: 0,709 · 0,689 · 0,662 | íd. | idénticos | **sí** |
| Educación / pensiones totales, aprobado 2024 · 2025: 0,518 · 0,501 | íd. | idénticos | **sí** |
| Educación / pensiones totales, aprobado 2023: 0,558 | íd. | 0,556 | **no, por 0,002** |

**La única discrepancia** es el punto de 2023 de la segunda fila de educación, y la
causa es el perímetro de las pensiones no contributivas: este guion las toma por
**número de programa** ---176, 286 y 316 del Ramo 20--- y la corrida de 2023 usó la lista
de programas vigente entonces. Dos milésimas. **Se deja la discrepancia a la vista en vez
de ajustar el perímetro para que cuadre.**

---

## 4. Hallazgo lateral, verificado y reusable

Al comparar proyecto contra aprobado en los siete ejercicios apareció un patrón que
importa para la línea G:

| ejercicio | Δ total entidades | Δ total Gobierno Federal |
|---|---|---|
| 2020 | 0,0 | **+11 396,6** |
| 2021 | 0,0 | 0,0 |
| 2022 | 0,0 | 0,0 |
| 2023 | 0,0 | 0,0 |
| 2024 | **−25 442,9** | **+25 442,9** |
| 2025 | 0,0 | 0,0 |
| 2026 | 0,0 | 0,0 |

**En cinco de los siete ejercicios la Cámara no movió un peso del total de ninguno de
los dos bloques: reasignó dentro.** El total de las entidades de control directo
---IMSS, ISSSTE, Pemex, CFE--- **cambió una sola vez en siete años.**

De ahí que las cinco razones que viven en entidades den exactamente lo mismo ex ante y
aprobado. **Y de ahí la advertencia práctica: la diferencia entre la línea P y la línea
G no está en los totales, está adentro.** En 2023, por ejemplo, el total del Gobierno
Federal no cambió y aun así diez ramos se movieron ---Bienestar −6 342,1; el Instituto
Nacional Electoral +4 475,5; el Poder Judicial +2 425,1---, con suma neta cero. Un
documento que compare totales concluirá que la Cámara no hizo nada. **Hizo, y el diff de
claves es lo que lo muestra.**

---

## 5. Lo que falta, declarado

- **2018 y 2019** no tienen analíticos en carpeta y su artículo 1o. no se extrae con el
  mismo patrón que 2019–2026 (el de 2018 tiene otra maquetación). Las series arrancan en
  2020.
- **Las cuatro razones con CGPE o Anexo 3** sólo tienen 2024–2026, porque los escalares
  de años anteriores no están en forma legible por máquina. Para extenderlas hay que leer
  el CGPE de cada año; **el CGPE 2025 es un escaneo sin capa de texto** y exige lectura de
  imagen.
- **`no_trabajadores` del cubo del IMSS** no se separó: el gasto por asegurado de esta
  corrida usa el total de asegurados, que incluye a los que no tienen empleo asociado.
