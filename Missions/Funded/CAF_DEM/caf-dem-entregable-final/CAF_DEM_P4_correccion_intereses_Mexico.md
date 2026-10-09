---
mission: CAF_DEM
producto: P4
tipo: instrucciones-claude-code
alcance: corrección de intereses de México + cuatro frases del árbitro
autor: Beth y Cath — BDH Core Team
revisor: Juan Pablo López Reynosa
fecha: 2026-10-09
entrega: sábado 10 de octubre de 2026
---

# CAF_DEM · P4 — Corrección de intereses de México

> **Registro.** En la revisión del 8 de octubre (Bloque 1.1) se sustituyó la serie de intereses de México derivada del WEO por intereses de la SHCP con **perímetro RFSP** (5,2 % del PIB en 2024). Esa elección venía de nuestras instrucciones, que afirmaban sin verificarlo que la deuda neta de la base coincidía con el SHRFSP. Héctor la corrigió el 9 de octubre: no hay razón para usar RFSP. La serie correcta es el **costo financiero del sector público presupuestario**. Para 2024 es del orden de 3,4 % del PIB (Gobierno Federal, Pemex y CFE pagaron 1,15 billones de pesos por intereses, comisiones y gastos de la deuda, según IMCO con datos de la SHCP). Esa cifra es aproximada y la oficial se toma de la fuente.

## 0. Reglas

1. **Ningún número inventado.** Si la serie no se puede obtener de la fuente oficial, detenerse y reportar. **No volver al perímetro RFSP ni a la diferencia de balances del WEO.**
2. No cambiar el método de cálculo de la tasa implícita, del diferencial (r−g) ni de pb\*. Sólo cambia la serie de intereses de México.
3. Lo que cambie en una tabla cambia en el texto, y al revés.
4. **Perímetro de la deuda.** La deuda neta de México en la base (51,4 % del PIB en 2024) es el SHRFSP, es decir, perímetro RFSP. Si el numerador pasa al sector público presupuestario y el denominador sigue en SHRFSP, la tasa implícita mezcla perímetros. Con los valores actuales, r caería de 9,3 % a cerca de 6,5 %, igual al crecimiento nominal de la base (6,5 %), y la brecha desaparecería por construcción. **Héctor decide antes de ejecutar** (ver «Decisión previa»).

Todo se ejecuta desde la carpeta del entregable, en una rama creada desde `p4-revision-final` (último commit del documento: f9d65c3, 8 de octubre):

```bash
cd ~/Dalila/Missions/Funded/CAF_DEM/caf-dem-entregable-final/
git checkout p4-revision-final
git checkout -b p4-intereses-mexico
```

## ⏸ DECISIÓN PREVIA — perímetro del denominador

Antes del Paso 1, Héctor elige:

- **(a)** Usar también como denominador la deuda neta del **sector público presupuestario** (SHCP), para que intereses y deuda tengan el mismo perímetro. Implica cambiar la serie de deuda neta de México en la tabla de espacio fiscal, en la ficha y en el Tipo A/B/C, y declararlo en la nota (a).
- **(b)** Mantener el SHRFSP como denominador y declarar en la nota (a) que intereses y deuda tienen perímetros distintos, y en qué sentido sesga la tasa implícita (hacia abajo).

Si la serie de deuda neta presupuestaria no se puede obtener de la fuente oficial, detenerse y reportar (regla 1).

---

## PASO 1 — Serie y recálculo

1. **Fuente:** SHCP, Estadísticas Oportunas de Finanzas Públicas. Serie anual del **costo financiero del sector público presupuestario**, 2015–2024, en millones de pesos corrientes.
2. **Reportar qué incluye la serie descargada**: si es sólo "intereses, comisiones y gastos de la deuda" o si incluye también el Ramo 34 (programas de apoyo a ahorradores y deudores de la banca). No decidir; reportarlo.
3. Expresar en % del PIB con el **mismo PIB nominal que usa la base** (WEO), para no mezclar denominadores. Reportar al lado el porcentaje que publica la SHCP, como contraste.
4. **Dónde entra al cálculo:** `calc_seccion6.py`, l. 16–22 (hoy lee `weo/shcp_rfsp_intereses_mex.csv`) y l. 58–65 (fila de la base: `codigo_indicador = 'SHCP_RF213000SPFC'`, `cobertura_institucional`, `fuente` y `nota` con perímetro RFSP). Guardar la serie nueva en `weo/` con un nombre propio, actualizar el comentario de l. 16–19 y ejecutar de nuevo el script para regenerar `seccion6_espacio_fiscal.csv`, `seccion6_presion_demografica.csv` y la base.
5. Incorporar la serie a `base_analisis_P4.csv` con `fuente`, `tipo = "Observado"` y `cobertura_institucional = "Sector público presupuestario"`. Eliminar la serie RFSP de la base. Si el registro de su uso debe conservarse, que quede en el diccionario. Actualizar también las menciones RFSP en `base_analisis_P4_diccionario.csv`, `tablas/anexo_diccionario_base.tex` y `pipeline_P4.R`. Si `pipeline_P4.R` sólo documenta la versión anterior, reportarlo sin cambiar su lógica.
6. Recalcular para México, **sólo con la ventana histórica** 2015–2024: tasa implícita, (r−g), pb\* y brecha. La ventana proyectada sigue como n.c.
7. Recalcular el total de México en la Tabla de presión (brecha + incremento en pensiones + incremento en salud) y el **ordenamiento de los seis países en espacio fiscal** de la Tabla de síntesis.

## ⏸ PUNTO DE CONTROL — reportar a Héctor antes de seguir

Entregar en un mensaje corto:

- Opción elegida en la decisión previa (a/b) y perímetro final del numerador y del denominador.
- Serie 2015–2024 (pesos y % del PIB) y qué incluye.
- Valores anteriores y nuevos de México: intereses 2024, tasa implícita, (r−g), pb\*, brecha, total de la Tabla de presión.
- Nuevo ordenamiento de espacio fiscal de los seis países (anterior y nuevo).

**Esperar su indicación sobre la clasificación A/B/C de México** antes del Paso 2. Hoy México está en el Tipo B ("riesgo demográfico sobre fragilidad fiscal previa") con dos argumentos: una brecha de 1,2 puntos y un aumento de 4,7 puntos en la deuda neta en 2024. Si la brecha desaparece, queda sólo el segundo, y el riesgo que describe la ficha es de arquitectura (sustitución contributivo→no contributivo). La decisión es de Héctor.

---

## PASO 2 — Actualizar el documento

Ubicaciones conocidas (líneas aproximadas de la versión del 9 de octubre). **Además, buscar por patrón** (desde `caf-dem-entregable-final/`): `grep -n "1,2 puntos\|5,2\\\\,\\\\%\|RFSP\|diferencial" main.tex tablas/*.tex`, y revisar cada mención de posiciones ordinales en espacio fiscal ("quinta", "sexto o cuarto", "segunda brecha", etc.), porque el ordenamiento puede cambiar para otros países.

| Lugar | Qué cambia |
|---|---|
| `calc_seccion6.py`, base y diccionarios | Ver Paso 1, puntos 4 y 5 |
| `tablas/anexo_diccionario_base.tex` | Menciones de RFSP o de la clave `RF213000SPFC` |
| `tablas/tab_espacio_fiscal.tex` | Fila de México (intereses, r, r−g, pb\*, brecha), incluida la sensibilidad con deuda bruta |
| Nota (a) de la Tabla de espacio fiscal (~l. 2000) | Sustituir la explicación RFSP por: *En México, la diferencia entre balance primario y balance global del WEO no mide intereses; se usa el costo financiero del sector público presupuestario de la SHCP, 2015–2024. No existe serie comparable para 2025–2030, por lo que la ventana proyectada no se calcula (n.c.).* Añadir media línea que señale que el perímetro de esa serie es el del sector público presupuestario. |
| §6.2, párrafo "Chile y México ocupan una posición intermedia…" (~l. 2026) | Reescribir la parte de México con la nueva brecha. Si deja de ser intermedia, reubicar a México en el párrafo que corresponda. |
| `tablas/tab_presion_demografica.tex` y su texto en §6.3 | Total de México |
| Ficha de México, bloque *Espacio fiscal* (~l. 2490) | Intereses, fuente y brecha. Quitar "perímetro RFSP". |
| Tabla de síntesis y §6.6 "Dónde coinciden / Dónde divergen" | Posición de México y de cualquier país cuyo lugar cambie |
| §6.6 Tipos de exposición (~l. 2623) | Según la decisión de Héctor en el punto de control |
| Principales hallazgos (~l. 266–283) | Posiciones ordinales en espacio fiscal ("Costa Rica… quinta en espacio fiscal") si cambian |
| Conclusiones (~l. 2830–2840) | "Chile y México en posición intermedia" y "en Brasil, Chile y México el incremento mecánico del gasto a 2050 es entre tres y siete veces el ajuste que la posición de 2024 ya requiere". Si la brecha de México se acerca a cero, ese cociente pierde sentido para México: sacarlo de la frase y recalcular el rango para Brasil y Chile. Comprobar que el rango nuevo coincide con los cocientes de la Tabla de presión. |

---

## PASO 3 — Cuatro frases del árbitro (segunda evaluación)

Independientes del Paso 1. Texto de reemplazo aprobado:

**3.1 Salud frente a pensiones** (§4.3, primera hipótesis de la enumeración, ~l. 1293). Sustituir el enunciado en negrita por:
> La presión demográfica sobre la salud puede ser tan importante como la pensionaria, e incluso superarla donde la exposición pública previsional es limitada o el gasto sanitario de partida es elevado.

Conservar la explicación que sigue.

**3.2 Las tres limitaciones** (última oración de las Conclusiones, ~l. 2858). Sustituir "Las tres limitaciones apuntan en la misma dirección: las magnitudes de este documento son conservadoras" por:
> Dos de estas limitaciones, la cobertura incompleta y probablemente el insumo demográfico, sugieren que las magnitudes son conservadoras; la metodológica añade incertidumbre sin una dirección definida.

(En el texto, la metodológica es la *segunda* limitación y el insumo demográfico la *tercera*; por eso no se usa un ordinal.)

**3.3 "La demografía es casi todo el problema"**
- Principales hallazgos (~l. 280–282): la oración siguiente ya dice "su presión fiscal mecánica a 2050 es casi enteramente demográfica", así que reemplazar el bloque completo para no repetir. Sustituir "En otros la demografía es casi todo el problema: Costa Rica y Colombia tienen brechas de 0,2 y 0,0 puntos, y su presión fiscal mecánica a 2050 es casi enteramente demográfica (4,3 a 4,7 y 6,3 a 8,2 puntos)" por "En otros, con la ventana histórica, la presión adicional es casi enteramente demográfica: Costa Rica y Colombia tienen brechas de 0,2 y 0,0 puntos, frente a una presión fiscal mecánica a 2050 de 4,3 a 4,7 y 6,3 a 8,2 puntos". Si el Paso 1 cambia la posición de México, revisar que el bloque siga siendo correcto.
- Conclusiones (~l. 2839): "en Colombia y Costa Rica la demografía es todo el problema" → "en Colombia y Costa Rica, con la ventana histórica, la presión adicional es predominantemente demográfica, aunque en Colombia la brecha sube a 1,4 puntos con la proyección del FMI".

**3.4 "El ajuste está hecho" (Costa Rica)**
- §6.2 (~l. 2038): "su ajuste fiscal posterior a la regla fiscal de 2018 está hecho, y la sensibilidad con la proyección del FMI, con la que la brecha es negativa ($-0{,}7$), lo confirma" → "su posición primaria es compatible con la estabilización de la deuda con ambas ventanas; con la proyección del FMI la brecha es negativa ($-0{,}7$)".
- Ficha de Costa Rica (~l. 2448): "El ajuste fiscal está hecho y la integración…" → "La posición primaria es compatible con estabilizar la deuda y la integración…".
- Conclusiones (~l. 2835): "Costa Rica con el ajuste hecho" → "Costa Rica con una posición primaria compatible con estabilizar la deuda".

Si el Paso 2 cambia alguna de estas frases (por ejemplo, la de Conclusiones que menciona a México), aplicar ambas correcciones de forma coherente.

---

## PASO 4 — Verificación y entrega

Todos los comandos, desde `caf-dem-entregable-final/`.

- [ ] Compilar tres veces: cero errores, referencias y citas indefinidas
- [ ] `grep -n "RFSP" main.tex tablas/*.tex`: ninguna mención como fuente de intereses de México (puede quedar como concepto de déficit si aparece en otro contexto)
- [ ] `grep -n "5,2" main.tex tablas/*.tex`: revisado en contexto (Panamá tiene una brecha de 5,2 que **no** cambia)
- [ ] `grep -n "está hecho\|ajuste hecho\|casi todo el problema\|todo el problema\|misma dirección: las magnitudes\|proporcionalmente mayor" main.tex`: cero
- [ ] `grep -n "9,3\|2,8" main.tex tablas/*.tex`: revisar en contexto cualquier mención de la tasa implícita (9,3 %) o del (r−g) (2,8) anteriores de México
- [ ] `grep -n "RFSP\|RF213000" calc_seccion6.py base_analisis_P4_diccionario.csv tablas/anexo_diccionario_base.tex`: sólo las menciones que la opción elegida justifique
- [ ] Cifras y ordenamientos de México idénticos en tabla de espacio fiscal, Tabla de presión, Tabla de síntesis, §6.2, §6.6, ficha, Principales hallazgos y Conclusiones

```bash
git add .   # sólo caf-dem-entregable-final/; el repositorio tiene cambios ajenos (BID2, DFD) que NO deben entrar
git status --short .   # revisar antes del commit
git commit -m "P4: intereses de México con costo financiero presupuestario SHCP; cuatro precisiones del árbitro"
git push -u origin p4-intereses-mexico
```

## Reporte final

1. Serie usada, qué incluye y cifra 2024.
2. Valores anteriores y nuevos de México, y ordenamiento anterior y nuevo.
3. Lista de cada línea modificada por el Paso 2.
4. Confirmación del Paso 3.
5. PDF compilado y `git diff f9d65c3 -- main.tex tablas/ calc_seccion6.py`.
