---
mission: CAF_DEM
producto: P4
tipo: reporte-revision-final
instruccion: CAF_DEM_P4_revision_final.md
rama: p4-revision-final
fecha: 2026-10-08
---

# CAF_DEM · P4 — Reporte de la revisión final

Entregables en esta carpeta: `main.pdf` (compilado tres veces, sin errores ni
referencias o citas indefinidas), `CAF_DEM_P4_revision_final.diff` (diff contra la
versión del 8 de octubre, sin el PDF) y este reporte.

## 1. Bloque 1.1 — Intereses de México y Brasil

**México.** La serie derivada del WEO (balance primario − balance global) da
2,7–5,9 % del PIB en 2015–2024. Contra la SHCP (Estadísticas Oportunas, datos
abiertos), con el PIB nominal del WEO:

| % del PIB | 2015 | 2017 | 2019 | 2021 | 2023 | 2024 |
|---|---|---|---|---|---|---|
| WEO derivada | 2,69 | 3,58 | 4,40 | 4,33 | 5,80 | 5,92 |
| Costo financiero presupuestario (XAC21) | 2,12 | 2,37 | 2,65 | 2,57 | 3,28 | 3,39 |
| Intereses, perímetro RFSP (RF213000SPFC) | 2,82 | 3,76 | 3,92 | 3,97 | 4,71 | 5,17 |

- La diferencia con el costo financiero supera un punto en todos los años desde
  2017, así que se aplicó la sustitución.
- Dos precisiones sobre la instrucción:
  1. El 3,7 % de 2024 no se reproduce: el costo financiero pagado suma 1.150 mmdp,
     que es 3,4 % del PIB.
  2. El costo financiero presupuestario no tiene el perímetro del SHRFSP, que
     incluye IPAB, Pidiregas y otros conceptos.
- **Decisión de Héctor (opción a):** se usan los intereses del sector público
  federal en el perímetro RFSP, que es el de la deuda neta. Con el costo
  presupuestario, la brecha de México habría sido −0,3.
- **Resultado para México:**
  - r = 9,26; (r−g) = 2,8; pb\* = 1,4.
  - **La brecha pasa de 1,5 a 1,2 puntos.**
  - La ventana 2025–2030 queda como **n.c.**, porque no existe una serie SHCP
    equivalente a 2030 y reescalar la del WEO habría sido inventar el dato.
- **Orden de espacio fiscal:** Panamá 5,2 · Brasil 3,1 · **Chile 1,4 · México 1,2**
  · Costa Rica 0,2 · Colombia 0,0. México baja del 3.º al 4.º lugar.
- **Dónde se actualizó:**
  - Tabla de espacio fiscal, con nota (a).
  - §6.2: párrafo de datos y orden intermedio.
  - §6.3: México pasa de "dos y media y tres" a "tres y casi cuatro veces" la
    brecha.
  - Totales de México en la Tabla de presión: 5,3–5,9 → 4,9–5,6.
  - Tabla de síntesis: Chile 3, México 4.
  - Ficha de México y Conclusiones (Conclusiones: "entre tres y siete veces").
- **Consecuencia en §6.6:** Chile queda ahora en la mitad superior de las tres
  dimensiones, igual que Brasil. Se reescribió "Dónde coinciden" para decirlo y
  para aclarar que el tercer lugar chileno se debe al déficit primario de 2024,
  no a la deuda.
- **Base de datos:**
  - Serie SHCP en `weo/shcp_rfsp_intereses_mex.csv`; `calc_seccion6.py` la usa
    para México.
  - `base_analisis_P4.csv` gana 10 filas ("Pago de intereses del sector público",
    con fuente y tipo) y una nota específica en el balance global de México.
  - Diccionario, anexo del diccionario y `pipeline_P4.R` mencionan la sustitución.
  - No se reejecutaron las proyecciones del pipeline: sólo cambiaron filas de
    México.

**Brasil.** Contra los *juros nominais* del setor público consolidado del BCB (SGS
5760, que coincide con el 8,07 % que publica el BCB para 2024; la serie SGS 5727 es
el déficit nominal, no los intereses):

- La diferencia es menor a un punto en 2015–2022, −1,00 en 2023 y −1,78 en 2024.
- **Decisión de Héctor:** se mantiene el WEO, con una nota en la tabla que
  reporta la diferencia. Con la serie del BCB, la brecha subiría de 3,1 a 3,5 sin
  cambiar el orden.

## 2. Bloques completados y omitidos

Todos completados.

- **1.2 — Fecundidad de Chile.**
  - Diferencias con el WPP calculadas desde `tab_contraste_tfr.tex`: Colombia
    0,53–0,62; México 0,29–0,38; Panamá 0,31–0,32; Costa Rica 0,20; Chile
    0,11–0,15.
  - Corregidos §6.4, Conclusiones y ficha de Chile.
  - También se corrigió la frase de §6.4 que llamaba "menor" a la diferencia de
    Costa Rica, México y Panamá: las tres son mayores que la de Chile.
- **2 — Contradicciones internas.**
  - 2.1: MASE de México-salud = 2,09 (confirmado en `tab_modelos.tex` y en el
    pipeline). La serie también activa el control de rango, y así se dice.
    §5.3.1 y §5.3.3 son ahora consistentes. La Figura 11 ya era correcta.
  - 2.2: Costa Rica 0,2 / −0,7, en §6.2 y en su ficha.
  - 2.3, 2.4 y 2.5 aplicados.
- **3 — Autoría del Apéndice A.**
  - `ascarza2026` sustituye a `bid2026`, con la nota de copyright intacta.
  - Declaración de autoría al inicio del apéndice.
  - Corregidas las frases de validación circular, y "el ejercicio del BID" pasó
    a "el ejercicio del Apéndice A".
  - No queda ninguna mención a "BID" ni a la División Fiscal.
- **4 — Correcciones de la evaluación.**
  - 4.1: "presión fiscal mecánica a 2050", más la oración sobre la regla de
    estrés.
  - 4.2: "conservador" para el sesgo del WPP, más la precisión temporal (sin
    cuantificar).
  - 4.3: asteriscos en las Tablas 12 y 19.
  - 4.4: tipos A/B/C. Clasificación revisada tras el Bloque 1.1:
    - México sigue en el tipo B (brecha positiva de diferencial y deuda +4,7
      puntos en 2024).
    - Chile sigue en el tipo A, por deuda baja. Su brecha (1,4) es ahora mayor
      que la de México y se explica en la misma línea.
  - 4.5: "Principales hallazgos", escrito al final, con cifras tomadas del cuerpo.
- **5 — Sensibilidad con deuda bruta.** Hecha, porque el subconjunto del WEO ya
  traía `GGXWDG_NGDP`.
  - Brechas con deuda bruta: Panamá 5,4 · Brasil 4,3 · México 1,3 · Chile 1,0 ·
    Costa Rica 0,2 · Colombia −0,1.
  - Sólo se invierten México y Chile; una oración en §6.2 lo explica.
  - Para que la tabla quepa se acortaron los encabezados ("Histórica 2015--2024",
    "WEO 2025--2030").
- **6 — Redacción.**
  - Pasada completa sobre la Sección 6, la Sección 7, las Conclusiones y el
    Apéndice A: frases-anuncio, enfáticos, moldes "no es X, es Y", rayas (ninguna
    queda de la Sección 6 al Apéndice A) y meta-comentario.
  - Aforismos conservados: dos ("son lo que queda disponible si no ocurre" y
    "Cada margen revalúa un acervo…").
  - Sin negrita inicial en 63 párrafos de §3.1–3.3.
  - Matices de la evaluación aplicados en §3.1 (Pilar 1-B como categoría propia),
    §3.2, §6.1, §7.4, ficha de México, §4.1 (gasto de bolsillo), §4.3 (inflación
    tecnológica y Baumol) y §7.3 (definición de frontera).
  - §5.3.1: el control de rango se definió **desde el código** (`pipeline_P4.R`,
    línea 57). Alerta si el valor al final del horizonte supera el máximo
    histórico, o queda bajo el mínimo, en más de la mitad del rango histórico.
- **7 — Verificación y entrega.**
  - Checklist limpio.
  - "5,9" sobrevive sólo en la nota que explica la discrepancia de México y en el
    retorno de mercado del Apéndice A, que no tiene relación con ella.
  - Los "cota inferior" restantes son por cobertura, salvo dos de México:
    - §6.3: la serie de gasto termina en 2020, antes de la expansión del Pilar 0.
    - Ficha: canal de sustitución.
    
    Ninguno se refiere al sesgo del WPP, así que se dejaron. Se señalan para su
    revisión.

## 3. Datos no disponibles

- **Proyección 2025–2030 de intereses de México en perímetro RFSP:** no existe;
  la celda queda como n.c.
- **Costo financiero de 3,7 % para 2024 citado en la instrucción:** no se
  reproduce con los datos abiertos de la SHCP (3,4 %).

## 4. Páginas

102 antes, 105 después: hallazgos, taxonomía, notas y columnas de deuda bruta.
Persisten dos cajas sobrellenas de 2 pt en tablas de §3.1 que este pase no tocó.

## Pendiente

- Commits f9d65c3 y 2c9622e en `p4-revision-final`, publicados en origin el 2026-10-08.
- Revisión de Héctor y Juan Pablo.
