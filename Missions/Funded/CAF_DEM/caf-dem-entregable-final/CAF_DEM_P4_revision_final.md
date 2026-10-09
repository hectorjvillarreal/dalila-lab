---
mission: CAF_DEM
producto: P4
tipo: instrucciones-claude-code
alcance: revisión final sobre main.tex entregado el 8 oct 2026
autor: Beth y Cath — BDH Core Team
revisor: Juan Pablo López Reynosa
fecha: 2026-10-08
entrega: sábado 10 de octubre de 2026
---

# CAF_DEM · P4 — Revisión final antes de entrega

> **Para Juan Pablo.** Esta es la última pasada antes de entregar. Viene de dos fuentes: una evaluación anónima del documento y nuestra propia revisión, que encontró errores que la evaluación no vio. Los bloques están en orden de prioridad. Si el tiempo no alcanza, se corta desde el final.

## 0. Reglas

1. **Ningún número inventado.** Si un dato no está en la base, en el `.tex` o en una fuente verificable, se reporta como pendiente. Esta regla anula cualquier otra.
2. **No tocar lo que no se pide.** Este pase corrige; no reescribe secciones completas ni reorganiza el documento.
3. Las tablas de la Sección 6 viven en `tablas/` (`tab_espacio_fiscal.tex`, `tab_presion_demografica.tex`, `tab_contraste_tfr.tex`, `tab_modelos.tex`). Si cambia un número en el texto, cambia en la tabla, y al revés.
4. Tiempo objetivo: terminar el viernes temprano para dejar el viernes a la revisión de Héctor y Juan Pablo.

```bash
cd ~/Dalila/Missions/Funded/CAF_DEM/
git checkout -b p4-revision-final
```

---

## BLOQUE 1 — Errores de cifra (obligatorio)

### 1.1 Intereses de México (el más importante)

**Problema.** La ficha de México y §6.2 reportan un pago neto de intereses de **5,9 % del PIB** en 2024. Hacienda reporta un costo financiero de **3,7 % del PIB** para 2024 (Pre-Criterios 2025 lo revisa a 3,6 %). El 5,9 coincide exactamente con los Requerimientos Financieros del Sector Público (RFSP) de 2024, que son una medida amplia de déficit, no de intereses. Hipótesis: al despejar intereses como *balance primario − balance global*, el balance global del WEO para México arrastra partidas del concepto RFSP que no son intereses.

**Consecuencia.** La tasa implícita de México está inflada, el diferencial (r−g) también, y la brecha de 1,5 puntos probablemente está sobreestimada.

**Qué hacer, en orden:**

1. Imprimir la serie derivada de intereses de México 2015–2024 (% del PIB) desde `base_analisis_P4.csv` y compararla con el costo financiero del sector público de la SHCP (Estadísticas Oportunas de Finanzas Públicas). La deuda neta de la base para México (51,4 % en 2024) coincide con el SHRFSP, así que el costo financiero de la SHCP corresponde al mismo perímetro.
2. **Si la diferencia supera 1 punto del PIB en cualquier año:** sustituir la serie de intereses de México por el costo financiero de la SHCP 2015–2024, anotarlo en la base con su `fuente` y `tipo`, recalcular r, (r−g), pb\* y la brecha con ambas ventanas, y actualizar `tab_espacio_fiscal.tex`, el texto de §6.2, la ficha de México, la Tabla de presión (columna de total), la Tabla de síntesis (si cambia el orden) y las Conclusiones.
3. **Hacer la misma comparación para Brasil** contra los *juros nominais do setor público consolidado* del Banco Central do Brasil. Si la diferencia es menor a 1 punto, dejar Brasil como está y decirlo en el reporte.
4. **Si no se puede acceder a la serie de la SHCP:** no publicar la brecha de México. Marcar la celda como "n.c." (no confiable) en la tabla, con nota explicando la discrepancia, y ajustar el texto de §6.2, la ficha y la síntesis para no usar el número. **No dejar el 1,5 en el documento si se sabe que está inflado.**

### 1.2 Fecundidad de Chile

§6.4 (párrafo "La magnitud para nuestra muestra") dice que en Colombia y Chile la diferencia con el WPP es "de orden, no de decimales: entre 0,5 y 0,6 hijos por mujer". Es cierto para Colombia (1,63 frente a 1,01–1,1). Para Chile no: 1,14 frente a 0,99–1,03 da entre **0,11 y 0,15**.

- Reescribir para que Colombia sea el caso de mayor discrepancia y Chile el de nivel más bajo, con su diferencia real.
- En las **Conclusiones**, la frase "los registros vitales nacionales de Colombia, Chile y Costa Rica muestran tasas globales de fecundidad entre 0,2 y 0,6 hijos por mujer inferiores" debe corregirse con las cifras de `tab_contraste_tfr.tex`. Calcular cada diferencia desde la tabla; no redondear para que quepa en una frase.
- Revisar la ficha de Chile ("la que más se ha alejado de la proyección") contra las mismas cifras: no es la que más se alejó, es la de nivel más bajo.

---

## BLOQUE 2 — Contradicciones internas (obligatorio)

### 2.1 México-salud: MASE mayor y menor que dos a la vez
§5.3.3 la incluye entre las series con MASE superior a dos (2,09), y la Figura 11 la omite por esa razón. El mismo párrafo la incluye después entre "las dos series de salud que, con MASE inferior a dos, siguen excediendo el rango histórico". Verificar el valor en `tab_modelos.tex` y dejar el texto consistente. Si el MASE es 2,09, quitar a México de la frase sobre el control de rango y ajustar §5.3.1 ("en las series de salud de Chile y de México la selección no cambia...") y la nota de la Figura 11.

### 2.2 Brecha de Costa Rica
La Tabla de síntesis le asigna 0,2 puntos, y los totales de la Tabla de presión cuadran sumando ese 0,2. Pero §6.2 dice que Costa Rica y Colombia "no presentan brecha" y la ficha dice "brecha nula o negativa". Tomar el valor de `tab_espacio_fiscal.tex` y escribir lo que dice: por ejemplo, "una brecha mínima (0,2 puntos) con la ventana histórica y negativa con la proyección del FMI".

### 2.3 La afirmación de los diez puntos de cotizantes (§7.3)
"Elevar la proporción de cotizantes en diez puntos haría más por la razón de dependencia del sistema que cualquier cambio de edad". Con cobertura cercana a 45 %, diez puntos más reducen la razón en torno a 18 %. El experimento del Apéndice A muestra que el retiro a 70 la reduce de 0,307 a 0,219, casi 29 %. La afirmación es falsa según el propio documento. Sustituir por una formulación sin comparación cuantitativa, por ejemplo: que en los países con informalidad superior a 55 % la ampliación de la base de cotizantes es el margen de mayor tamaño potencial y el que menos depende de un parámetro, porque depende de la credibilidad del contrato.

### 2.4 Afirmación no verificada sobre CONAPO (Apéndice A, última subsección)
Eliminar "que descansa en supuestos de fecundidad de la misma familia que los del WPP". Reformular el párrafo diciendo sólo que si la proyección demográfica subestima la razón de dependencia, la tasa de contribución de equilibrio es mayor que la reportada.

### 2.5 Menores
- Nota de **Alcance** en la portada: atribuye el marco institucional a "Secciones 2 a 4", pero la 2 es demografía. Corregir a "Secciones 3 y 4" y mencionar la demografía por separado.
- §1.3: "y aislar qué reglas amplifican o amortiguan" → "y comparar qué configuraciones institucionales tienden a amplificar o amortiguar".

---

## BLOQUE 3 — Autoría del modelo del Apéndice A (obligatorio)

El modelo que resume el Apéndice A es trabajo de los autores de esta nota con otros coautores.

### 3.1 Cita correcta
Sustituir la entrada `bid2026` por:

> Ascarza-Mendoza, D., Villarreal, H. J., Cortés, H. y Méndez, J. (2026). *Spending Smarter under Demographic Pressure: Fiscal Efficiency, Health, and Gender Dynamics in Latin America*. Documento financiado por la Red de Investigación de América Latina y el Caribe del Banco Interamericano de Desarrollo, agosto de 2026.

Conservar la nota de copyright del BID tal como está. Cambiar la clave a `ascarza2026` y actualizar todos los `\citep`/`\citet`. El financiamiento es de la Red de Investigación (confirmado por Héctor); no mencionar la División Fiscal en ninguna parte del documento.

### 3.2 Declaración visible
Al inicio de la primera subsección del Apéndice A, una oración sin rodeos:

> El modelo que aquí se resume fue desarrollado por los autores de esta nota junto con Diego Ascarza-Mendoza, Hermilo Cortés y Judith Méndez, en un trabajo financiado por la Red de Investigación de América Latina y el Caribe del Banco Interamericano de Desarrollo \citep{ascarza2026}.

Eliminar la descripción actual que lo presenta como un documento externo, en la medida en que la oración nueva la sustituya.

### 3.3 Frases que suenan a validación independiente
Con autoría compartida, estas frases leen como circulares. Ajustar:

- Apéndice A, menú de reforma: "La conclusión que el ejercicio extrae, y que esta nota adopta en la Sección 7" → "Esta conclusión organiza las consideraciones de la Sección 7".
- §6.3: "El supuesto está justificado teóricamente por la identidad de cierre... que se desarrolla en el Apéndice A" → aclarar que la identidad es notación estándar de cualquier sistema de reparto; el apéndice la presenta, no la demuestra.
- §7 (introducción y margen de la tasa de reemplazo): donde diga "el ejercicio del BID", decir "el ejercicio del Apéndice A".

---

## BLOQUE 4 — Correcciones de la evaluación (prioridad alta)

### 4.1 "Ajuste total requerido" → "presión fiscal mecánica a 2050"
El término sugiere precisión actuarial que el documento niega. Sustituir en: encabezado y nota de `tab_presion_demografica.tex`, título de la Tabla de presión, texto de §6.3, ficha de Brasil ("ajuste requerido a 2050"), §6.6 y Conclusiones. Añadir una oración en §6.3, después de la ecuación de pensiones: la elasticidad unitaria es una regla de estrés, apropiada para un reparto maduro con parámetros constantes y menos para sistemas mixtos o regímenes en extinción por cohorte, como reconocen las fichas de Chile y México.

### 4.2 "Cota inferior" por sesgo demográfico → "conservador"
**Distinguir dos usos.** "Cota inferior" por cobertura de gobierno central (Costa Rica, Panamá, México) es correcto y **se conserva**. "Cota inferior" o "piso" por el sesgo del WPP es demasiado fuerte y **se suaviza**. Ubicaciones a corregir: §6.4 párrafo 3 ("deben leerse como cota inferior del riesgo"), §6.6 párrafo final ("Cota inferior"; "ninguno de los seis está mejor de lo que la tabla indica"), Conclusiones ("todas son cota inferior"; "lo que aquí se ordena es un piso"), Apéndice A última subsección.

Formulación base: *la evidencia disponible sugiere que el escenario demográfico utilizado puede subestimar la velocidad del envejecimiento, por lo que las estimaciones de presión deben leerse como conservadoras.*

**Añadir en §6.4, párrafo 3, una precisión temporal** que hace el argumento más exacto:

> Antes de 2050, el sesgo de fecundidad sólo alcanza el denominador de la razón de dependencia: la población de 65 años y más en 2050 ya nació, y la sobreestimación de nacimientos se refleja en las cohortes que en 2050 estarán en las primeras edades activas. Su efecto sobre la razón de dependencia de 2050 es, por tanto, moderado; es después de 2050 cuando la diferencia se amplía. La migración, que la presentación no analiza, puede compensar parcialmente en los países que reciben población en edad de trabajar, como Colombia y Chile.

No cuantificar el efecto: no está calculado.

### 4.3 Marcas de cobertura visibles
En la Tabla 12 (participación en el gasto) y en la Tabla de síntesis, añadir un asterisco junto a Costa Rica, Panamá y México con la nota "cota inferior por cobertura de gobierno central". Sólo eso; no rediseñar tablas.

### 4.4 Taxonomía A/B/C en §6.6
Después del párrafo "Dónde divergen", un párrafo nuevo y breve:

- **Tipo A — riesgo demográfico sobre finanzas sólidas:** Chile, Costa Rica.
- **Tipo B — riesgo demográfico sobre fragilidad fiscal previa:** Brasil, Colombia, México.
- **Tipo C — fragilidad fiscal predominantemente no demográfica:** Panamá.

Una línea de justificación por país, tomada de las fichas. Para Costa Rica, mencionar la salvedad de la base recaudatoria estrecha. **Si el Bloque 1.1 cambia sustancialmente la brecha de México, verificar que la clasificación siga siendo coherente con su ficha y reportarlo.**

### 4.5 Principales hallazgos al final de la introducción
Nueva subsección `\subsection{Principales hallazgos}` después de §1.4, de media página como máximo, con cuatro o cinco puntos:

- La presión demográfica no ordena a los países igual que el espacio fiscal; los casos de divergencia son los más informativos.
- La arquitectura institucional decide por qué canal llega el riesgo: donde el componente no contributivo puede sustituir al contributivo, la presión se desplaza hacia las rentas generales por la vía de la base de cotización.
- En algunos países el problema inmediato es fiscal y no demográfico (Panamá); en otros la demografía es casi todo el problema (Costa Rica, Colombia).
- En equilibrio general, para México, el envejecimiento con política sin cambio redistribuye más de lo que empobrece, y las reformas difieren más en quién paga que en cuánto bienestar entregan.
- El insumo demográfico oficial probablemente subestima la velocidad del envejecimiento; las cifras deben leerse como conservadoras.

Cerrar con una oración organizadora escrita con palabras propias, en esta línea: el riesgo macrofiscal del envejecimiento no depende sólo de cuántos adultos mayores tendrá un país, sino de qué sistema promete pagarles, quién cotiza, qué parte se financia con rentas generales y cuánto espacio fiscal queda cuando la transición se acelera.

**Las cifras del resumen deben coincidir con el cuerpo después de los Bloques 1 y 2.** Escribir este bloque al final.

---

## BLOQUE 5 — Sensibilidad con deuda bruta (sólo si hay tiempo)

Si el WEO de abril 2025 con deuda bruta del gobierno general está disponible en el entorno o es de descarga directa: añadir a `tab_espacio_fiscal.tex` dos columnas, deuda bruta 2024 y brecha con deuda bruta, usando la misma tasa y crecimiento. Una oración en §6.2 sobre si el orden cambia. Si no está disponible en 30 minutos, omitir y reportarlo.

---

## BLOQUE 6 — Lenguaje: que se lea escrito por una persona

Héctor pidió explícitamente que el documento no parezca escrito por una IA. Este pase es de redacción, no de contenido.

**Reglas:**
- No cambiar ningún número, referencia cruzada, cita ni afirmación sustantiva.
- Prioridad: Principales hallazgos, Sección 6, Sección 7, Conclusiones, Apéndice A. Las Secciones 3 a 5 sólo para los puntos marcados abajo.
- Registro: español académico de un economista mexicano escribiendo para un banco de desarrollo. Frases directas, voz activa, longitud variada.

**Qué eliminar o reducir:**

1. **Frases-anuncio** que dicen que algo es importante en lugar de decirlo: "Conviene subrayar", "merece atención", "Es lo más importante de esta subsección", "La pregunta que da sentido a la sección", "Conviene cerrar con", "Tres lecturas se desprenden", "Tres cosas se siguen", "El punto que ninguna contabilidad produce". Ir directo a la afirmación.
2. **Expresiones enfáticas** que vienen de las instrucciones previas y no corresponden a una nota técnica: "la única opción honesta", "sin adornos", "no admite suavizarse", "con diferencia", "deliberadamente", "precisamente" (cuando no aporta), "nítido" (dejar una sola vez, en México).
3. **El molde "no es X, es Y"** y sus variantes ("no es un catálogo: determina...", "eso lo hace menos visible, no menor", "su problema es de 2024, no de 2050"). Dejar como máximo uno por sección; los demás reescribirlos como afirmación simple.
4. **Cierres aforísticos** al final de párrafo: "lo que aquí se ordena es un piso", "Cada margen revalúa un acervo que alguien ya tiene y no puede reconstruir", "son lo que queda disponible si no ocurre". Conservar uno o dos en todo el documento, no uno por párrafo.
5. **Incisos con raya (`---`)**: el documento los usa en exceso. Sustituir la mayoría por comas, paréntesis o una oración nueva. Conservar sólo donde el inciso es largo y la raya ayuda a leer.
6. **Enumeraciones en tríada forzada.** Si un párrafo enumera tres cosas porque tres suena bien, dejar las que realmente aportan.
7. **Negrita en la primera oración de cada párrafo** en las Secciones 3.1, 3.2 y 3.3. Quitar la negrita (conservar el texto). Es un patrón visible y en un documento de 60 páginas cansa. Mantener negrita sólo en definiciones y en los avisos de las notas de tabla.
8. **Meta-comentario sobre el propio documento**: "Esta subsección no revierte esa decisión", "Lo que sigue describe la estructura mínima, la identidad...", "Las seis fichas que siguen se construyen exclusivamente con...". Reducir a lo indispensable.

**Correcciones de matiz de la evaluación**, en el mismo pase:
- Relación Pilar 0–informalidad: usar "puede reducir", "tiende a erosionar", no relación determinista. Revisar §3.2, §6.1, §7.4 y la ficha de México ("la sustitución está operando" → "sería señal de que la sustitución está operando").
- §4.1: gasto de bolsillo elevado como indicador "más directo" de segmentación → uno de varios factores posibles (copagos, preferencia por proveedores privados, listas de espera, exclusiones).
- §4.3: "inflación tecnológica" → precisar que incluye precios médicos, expansión de la canasta y mayor intensidad de uso; y no presentar a Baumol como la explicación dominante del crecimiento del gasto.
- §3.1: una oración que diga que el Pilar 1-B es una categoría introducida en este documento para separar la asistencia general de las garantías específicas sobre el resultado de la capitalización.
- §7.3: definir "frontera" en la primera línea: la edad o regla que separa contribuyentes de beneficiarios.
- §5.3.1: una oración que defina el control de rango a partir del código del pipeline (qué umbral usa respecto del máximo histórico). **Tomar la definición del código, no inventarla.** Si no está en el código, reportarlo.

---

## BLOQUE 7 — Verificación y entrega

1. Compilar tres veces.
2. Lista:
   - [ ] Cero errores, referencias y citas indefinidas
   - [ ] `grep -n "5,9\|5.9" main.tex tablas/*.tex` revisado en contexto (México)
   - [ ] `grep -n "ajuste total requerido\|ajuste requerido" main.tex tablas/*.tex` → cero
   - [ ] `grep -n "cota inferior\|piso" main.tex` → cada caso restante es por cobertura, no por sesgo demográfico
   - [ ] `grep -n "bid2026\|aislar\|única opción honesta\|sin adornos\|no admite suavizarse" main.tex` → cero
   - [ ] Cifras del resumen de hallazgos idénticas a las del cuerpo
   - [ ] `grep -n "^%" main.tex` → sólo separadores estructurales
3. Entregar a Héctor: PDF compilado, `git diff` contra la versión del 8 de octubre, y un reporte breve.

```bash
git add -A
git commit -m "P4: revisión final — cifras México/Chile, contradicciones, autoría Ap. A, evaluación, redacción"
git push -u origin p4-revision-final
```

## Reporte final (breve)

1. Resultado del Bloque 1.1: qué mostró la comparación con la SHCP, si se recalculó o se marcó como no confiable, y cómo quedaron la brecha y el orden. Lo mismo para Brasil.
2. Bloques completados y omitidos.
3. Cualquier dato que una instrucción pedía y no estaba disponible.
4. Conteo de páginas antes y después.
