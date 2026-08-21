# Instrucciones para Claude Code — NTA Paper: edición final
**Archivo objetivo:** `paper_final.tex`  
**Fecha de entrega:** 21 de agosto de 2026  
**Ejecutar en orden. No saltarse pasos.**

---

## PASO 1 — Eliminar todos los marcadores `\revisar{}`

El documento define `\revisar{}` como macro de color rojo para notas internas. Ninguna debe aparecer en la versión final.

Localiza todas las ocurrencias:
```bash
grep -n "\\\\revisar{" paper_final.tex
```

Hay al menos seis instancias. Para cada una, toma una de estas dos acciones según el caso:

**A) Si el punto ya está resuelto en el cuerpo del texto:** elimina el `\revisar{}` completo sin reemplazarlo.

**B) Si el punto describe una limitación real que debe quedar documentada:** mueve el contenido al Anexo E (tab_limitaciones), añadiéndolo como fila adicional de la tabla si no está ya ahí. Luego elimina el `\revisar{}` del cuerpo.

Casos específicos:
- `\revisar{}` sobre el trimestre de referencia y estacionalidad → ya está resuelto en el cuerpo (sección 3.3, último párrafo). Eliminar.
- `\revisar{}` sobre la división 2/3–1/3 del ingreso mixto → mencionar en el cuerpo como supuesto E1 (ya está en tab_supuestos). Eliminar el marcador.
- `\revisar{}` sobre el ajuste de remesas → ya está tratado en sección 6.5. Eliminar.
- `\revisar{}` sobre consumo de gobierno plano → ya está en el cuerpo (sección 4.2) y en limitaciones (L7). Eliminar.
- `\revisar{}` sobre alquiler imputado → ya resuelto en sección 4.6. Eliminar.
- `\revisar{}` sobre subcaptación diferencial por edad → ya está en sección 5 y Anexo E. Eliminar.

Verificación final:
```bash
grep -c "\\\\revisar{" paper_final.tex
# Debe devolver 0
```

---

## PASO 2 — Verificar y corregir la sección 2.3

La sección `\subsection{Aplicaciones y usos de NTA en América Latina}` tiene contenido completo en el `.tex` (tres párrafos con citas a Rosero-Bixby, Mason, Rosero 2024, Olivera 2023, Mejía-Guevara y Rivero 2024). Verificar que compile correctamente y que todas las claves de cita existan en `referencias.bib`:

```bash
grep -o "\\\\citet{[^}]*}\|\\\\citep{[^}]*}" paper_final.tex | sort -u
```

Comparar contra las entradas de `referencias.bib`. Si alguna clave falta, agregarla al `.bib` con los datos completos de la referencia.

---

## PASO 3 — Verificar numeración del Anexo C y consistencia de apéndices

El texto referencia los apéndices como:
- `\ref{anexo:series}` → Anexo A
- `\ref{anexo:mapeo}` → Anexo B  
- `\ref{anexo:supuestos}` → Anexo C (Registro de supuestos)
- `\ref{anexo:lambda}` → Anexo D (Factores de reescalamiento)
- `\ref{anexo:limitaciones}` → Anexo E (Limitaciones)

Verificar que LaTeX asigne las letras correctas al compilar. Si hay desfase (el Cuadro de supuestos aparece en D en lugar de C), revisar el orden de los `\section{}` dentro de `\appendix`.

---

## PASO 4 — Verificar que no exista L3 faltante en tab_limitaciones.tex

Abrir `tables/tab_limitaciones.tex` y verificar la secuencia de etiquetas. Si la numeración salta de L2 a L4, hay dos opciones:

**A)** Si L3 fue eliminada deliberadamente: renumerar L4–L9 como L3–L8 para que la secuencia sea continua.

**B)** Si L3 existe pero fue omitida por error: reincorporarla.

La secuencia final debe ser continua sin saltos.

---

## PASO 5 — Escribir el abstract

Insertar inmediatamente después de `\maketitle` y antes de `\section{Objetivo}`:

```latex
\begin{abstract}
Este documento construye una base persona-año de Cuentas Nacionales de Transferencia
para México a partir de cinco levantamientos bienales de la Encuesta Nacional de
Ingresos y Gastos de los Hogares (ENIGH) 2016--2024, con 1.46 millones de registros,
conciliada con el Sistema de Cuentas Nacionales mediante un único factor de
reescalamiento por variable y año. El procedimiento toma de la encuesta la forma del
perfil por edad y de las cuentas nacionales el nivel, garantiza el cierre contra siete
agregados de control y reporta la brecha entre los dos métodos independientes de cálculo
del déficit del ciclo de vida en lugar de forzarla a cero.

Los resultados documentan tres asimetrías estructurales. Primera: el déficit del ciclo
de vida en México es un resultado de composición por sexo. El perfil masculino alcanza
superávit entre los 33 y los 62 años en 2024; el femenino no lo alcanza en ninguna edad
de ninguno de los cinco levantamientos. Las mujeres concentran el 76.3\,\% del déficit
agregado. Segunda: el déficit no crece en términos agregados --- bajó de 47.4\,\% a
42.2\,\% del consumo entre 2016 y 2024 ---, pero se desplaza hacia la vejez: el déficit
per cápita de los mayores de 60 años subió 71.7\,\% en términos reales mientras su peso
poblacional pasó de 11.3\,\% a 15.1\,\%. Tercera: los dos extremos del ciclo se
financian por vías opuestas. La niñez cubre su déficit en 88.6\,\% con recursos privados;
la vejez lo cubre en 54.5\,\% con transferencias públicas netas. Un envejecimiento
demográfico que aumente el peso de la vejez se traduce de forma directa en presión
presupuestaria, mientras un cambio en el peso de la niñez se absorbe dentro de los
hogares. El sistema público no compensa la brecha de financiamiento por sexo en la vejez:
las mujeres mayores de 60 años reciben 24.0\,\% menos en transferencias públicas netas
que los hombres, pese a que su déficit duplica al de ellos.
\end{abstract}
```

---

## PASO 6 — Escribir las conclusiones

Insertar una nueva sección antes de `\appendix`:

```latex
% ---------------------------------------------------------------------------
\section{Conclusiones}
\label{sec:conclusiones}
% ---------------------------------------------------------------------------

Este documento construyó una base de Cuentas Nacionales de Transferencia para México
con tres propiedades que la distinguen de ejercicios previos: cierre verificable contra
siete agregados de control del Sistema de Cuentas Nacionales, documentación explícita de
cada imputación con su supuesto y su impacto, y reporte de la brecha entre los dos
métodos de cálculo del déficit del ciclo de vida en lugar de un cierre forzado. La
brecha en 2024 equivale a 0.001\,\% del déficit total, lo que valida la consistencia
interna del procedimiento sin requerir ningún supuesto adicional sobre el bloque privado.

El resultado empírico central es que el ciclo de vida económico en México no es
deficitario en todas las edades: es deficitario en el agregado porque agrega dos ciclos
de vida estructuralmente distintos. El perfil masculino alcanza superávit en treinta
edades consecutivas alrededor de los 47 años; el femenino no cruza el eje en ninguna
edad de ningún levantamiento. Esta asimetría no se corrigió entre 2016 y 2024: la razón
del ingreso laboral femenino al masculino subió de 41.6\,\% a 47.9\,\%, pero el déficit
de las mujeres en edad activa continuó más que duplicando al del grupo completo. Financiar
el ciclo de vida en México es, en su mayor parte, financiar el déficit femenino.

El análisis de financiamiento añade una dimensión fiscal. La niñez y la vejez se
financian por mecanismos opuestos: la primera recurre principalmente a la reasignación de
activos del hogar y a las transferencias privadas entre hogares; la segunda depende en
más de la mitad de las transferencias públicas netas. Esta asimetría implica que el
envejecimiento demográfico no es un shock simétrico sobre el presupuesto: cada punto
porcentual que gana el grupo de 60 años o más en la distribución de la población se
traduce directamente en presión sobre el gasto público, mientras que un cambio equivalente
en el peso de la niñez se absorbe sobre todo dentro de los hogares. México ya recorrió
ese camino: el grupo de mayores pasó de 11.3\,\% a 15.1\,\% de la población entre 2016
y 2024.

La dinámica interna del sistema público durante ese periodo muestra una tensión creciente.
El pago neto de transferencias públicas por persona en edad activa subió 39.1\,\% en
términos reales, pero no porque la carga tributaria individual haya aumentado en esa
proporción --- el pago bruto per cápita subió 15\,\% --- sino porque la participación del
grupo en las transferencias públicas recibidas cayó a la mitad. El sistema desplazó
recursos hacia las edades mayores sin ampliar la base que los financia. La transferencia
pública neta por adulto mayor, en cambio, subió apenas 3.8\,\% real en el mismo periodo,
de modo que la carga por aportante creció sin que la prestación por beneficiario
avanzara proporcionalmente. El resto del déficit de la vejez se trasladó a la
reasignación por activos y a los hogares.

La desigualdad por sexo en la vejez opera en el mismo sentido que la brecha laboral: las
mujeres mayores de 60 años enfrentan un déficit 2.2 veces el de los hombres de ese grupo,
y reciben 24.0\,\% menos en transferencias públicas netas. El sistema público no
compensa la diferencia de origen; se suma a ella. El único canal que favorece a las
mujeres mayores frente a los hombres es el de las transferencias privadas entre hogares,
insuficiente para cerrar la brecha de los otros dos canales.

El procedimiento construido habilita extensiones directas. Los perfiles por edad, sexo y
posición en la distribución del ingreso son el insumo para proyectar el déficit del ciclo
de vida bajo distintos escenarios de envejecimiento, formalización y reforma de la
política social, y para evaluar el efecto de cambios paramétricos sobre cada grupo. Esa
proyección requiere, adicionalmente, un modelo de comportamiento que permita distinguir
los efectos de composición demográfica de los efectos de política. Las Cuentas Nacionales
de Transferencia construidas aquí son el punto de partida contable, no el modelo de
comportamiento; la distinción es pertinente porque el reescalamiento proporcional
preserva la forma por edad de la encuesta y no corrige subcaptación diferencial por
posición en la distribución, lo que acota las inferencias sobre desigualdad del ingreso
de capital pero no compromete las relativas a la incidencia fiscal por edad y sexo.
```

---

## PASO 7 — Compilación y verificación final

```bash
# Compilar
pdflatex paper_final
bibtex paper_final
pdflatex paper_final
pdflatex paper_final

# Verificar que no quedan marcadores internos
grep -n "REVISAR\|revisar\|TODO\|PENDIENTE\|verificar" paper_final.tex

# Verificar referencias cruzadas no resueltas
grep -n "??" paper_final.log

# Contar palabras del abstract (debe estar entre 200 y 250)
# Contar palabras de las conclusiones (debe estar entre 500 y 650)
```

Si hay advertencias de referencias no resueltas (`??`), localizarlas y corregir las etiquetas `\label` / `\ref` correspondientes.

---

## Notas de consistencia de cifras

Las cifras del paper_final.tex son la versión canónica. El resumen ejecutivo y la presentación deben coincidir con ellas. Las cifras clave a verificar en todos los documentos:

| Concepto | Cifra canónica (paper_final.tex) |
|---|---|
| Vejez financiada por transferencias públicas netas | 54.5 % |
| Niñez financiada por recursos privados | 88.6 % |
| Déficit agregado como % del consumo, 2016 | 47.4 % |
| Déficit agregado como % del consumo, 2024 | 42.2 % |
| Déficit per cápita vejez, cambio real 2016–2024 | +71.7 % |
| Peso poblacional 60+, 2016 | 11.3 % |
| Peso poblacional 60+, 2024 | 15.1 % |
| Pago neto edad activa, cambio real 2016–2024 | +39.1 % |
| Transferencia pública neta adulto mayor, cambio real | +3.8 % |
| Mujeres concentran del déficit agregado 2024 | 76.3 % |
| Brecha transferencias públicas mujeres/hombres 60+ | −24.0 % |
| Brecha M1–M2 como % del déficit total | 0.001 % |
