# Instrucciones para Claude Code — NTA Paper: revisión de conclusiones (v2)
**Archivo objetivo:** `paper_final.tex`
**Contexto:** el abstract y las conclusiones ya fueron insertados en la ronda anterior. Un revisor externo pidió tres ajustes sustantivos y tres de edición sobre las conclusiones. El abstract NO se modifica.
**Alcance:** una sola operación de reemplazo. No tocar ninguna otra sección.

---

## Qué se está corrigiendo y por qué

Comentarios del revisor incorporados en esta versión:

1. **Reencuadre del hallazgo principal.** El mensaje no es que México tenga un déficit del ciclo de vida elevado, sino que su *composición* cambia con el envejecimiento y que los mecanismos de financiamiento difieren entre niñez y vejez.
2. **Cautela sobre el resultado por sexo.** El déficit femenino debe leerse dentro del marco monetario de las NTA. Esta versión no incorpora trabajo no remunerado, de modo que el resultado no es una medida integral de contribución económica.
3. **Disciplina sobre inferencias fiscales dinámicas.** El documento no modela respuestas de comportamiento ni cambios de política. Toda proyección implícita se condiciona con "bajo la estructura actual de transferencias" o "manteniendo constantes los perfiles observados".
4. **Edición:** no repetir cifras ya desarrolladas en la sección de resultados; presentar una sola contribución central; cerrar señalando que las simulaciones son una segunda etapa analítica.

Resultado: seis párrafos pasan a cinco, sin cifras repetidas del cuerpo.

---

## PASO ÚNICO — Reemplazar el bloque completo de conclusiones

Localizar la sección:

```bash
grep -n "\\\\section{Conclusiones}" paper_final.tex
grep -n "^\\\\appendix" paper_final.tex
```

El bloque a reemplazar va desde `\section{Conclusiones}` hasta la línea inmediatamente anterior a `% ---` que precede a `\appendix`.

### Texto a ELIMINAR

Todo el contenido actual entre `\section{Conclusiones}` y el separador previo a `\appendix`. Comienza con:

```
Este documento construyó una base de Cuentas Nacionales de Transferencia para México
con tres propiedades que la distinguen de ejercicios previos: cierre verificable contra
```

y termina con:

```
de capital pero no compromete las relativas a la incidencia fiscal por edad y sexo.
```

### Texto a INSERTAR

```latex
\section{Conclusiones}
\label{sec:conclusiones}
% ---------------------------------------------------------------------------

La contribución central de este documento es metodológica: una base de Cuentas
Nacionales de Transferencia para México construida con cierre verificable contra el
Sistema de Cuentas Nacionales, documentación explícita de cada imputación y sus
supuestos, y reporte de la brecha entre los dos métodos de cálculo del déficit del
ciclo de vida en lugar de un cierre forzado. Esa transparencia es lo que hace
comparables los resultados con otros países y reproducible el ejercicio ante cambios
en los datos o en las decisiones metodológicas.

Sobre esa base emergen tres hallazgos sustantivos. El primero es que el déficit
agregado del ciclo de vida en México no crece, pero su composición cambia: bajo la
estructura actual de transferencias y perfiles por edad, el déficit se desplaza hacia
la vejez al mismo ritmo en que envejece la población. Esto importa fiscalmente porque
los dos extremos del ciclo se financian por vías opuestas: la niñez carga el costo
sobre el circuito privado --- activos y transferencias entre hogares ---, mientras la
vejez depende en más de la mitad de transferencias públicas netas. Manteniendo
constantes los perfiles observados, cada punto porcentual que gane el grupo de mayores
en la distribución poblacional se traduce en presión presupuestaria directa; un cambio
equivalente en el peso de la niñez se absorbe dentro de los hogares.

El segundo hallazgo es que el promedio nacional oculta dos ciclos de vida
estructuralmente distintos por sexo. En el marco monetario de las NTA, el perfil
masculino alcanza superávit en un tramo amplio de la edad activa; el femenino no lo
alcanza en ninguna edad de ninguno de los cinco levantamientos. Esta asimetría debe
leerse dentro de los límites del instrumento: las NTA monetarias no incorporan el
trabajo no remunerado, de modo que el déficit femenino observado no es una medida
integral de la contribución económica de las mujeres, sino de su posición dentro del
ciclo de vida monetario tal como lo registran la encuesta y las cuentas nacionales.
Con esa cautela explícita, el resultado es informativo: el sistema público no compensa
la brecha de financiamiento por sexo en la vejez, y las transferencias privadas entre
hogares --- el único canal que favorece a las mujeres mayores frente a los hombres ---
resultan insuficientes para cerrarla.

El tercer hallazgo concierne a la dinámica interna del sistema público entre 2016 y
2024. La carga por aportante en edad activa creció de forma sustantiva, no por un
aumento proporcional de su contribución bruta, sino porque su participación en las
transferencias públicas recibidas cayó a la mitad. El sistema desplazó recursos hacia
las edades mayores sin ampliar la base que los financia, mientras la prestación real
por beneficiario mayor apenas varió. Esta configuración es descriptiva de la estructura
observada, no una proyección: cuánto persiste bajo distintos escenarios de política,
formalización o comportamiento laboral es una pregunta que requiere un modelo de
segunda etapa.

La base construida aquí es ese punto de partida. Los perfiles por edad, sexo y posición
en la distribución del ingreso que produce están listos para alimentar simulaciones
demográficas y fiscales que distingan los efectos de composición poblacional de los
efectos de política, y para extenderse hacia las Cuentas Nacionales de Inclusión
mediante la desagregación socioeconómica. Esas extensiones constituyen la segunda
etapa analítica.
```

---

## Verificación

```bash
# El bloque debe tener cinco párrafos
awk '/\\section{Conclusiones}/,/^\\appendix/' paper_final.tex | grep -c "^$"

# No deben quedar cifras específicas repetidas del cuerpo en conclusiones
awk '/\\section{Conclusiones}/,/^\\appendix/' paper_final.tex | grep -o "[0-9]\+\.[0-9]\+\\\\,\\\\%"
# Debe devolver vacío: las conclusiones no citan porcentajes puntuales

# Compilar
pdflatex paper_final && bibtex paper_final && pdflatex paper_final && pdflatex paper_final

# Verificar que no haya referencias rotas
grep -n "??" paper_final.log
```

---

## Lo que NO se toca

- **El abstract.** Queda tal como está. Contiene las cifras específicas por diseño: es el único lugar donde la repetición numérica es apropiada.
- **La sección 6.6 (Implicaciones).** Mantiene el desarrollo con cifras; las conclusiones ahora sintetizan sin repetir.
- **Cualquier otra sección del documento.**

---

## Nota sobre consistencia entre documentos

Si el resumen ejecutivo (`resumen_ejecutivo.tex`) o la presentación (`presentacion.tex`) van a circular junto con el paper, verificar que la cautela sobre trabajo no remunerado aparezca también en el resumen ejecutivo, que es el documento con mayor probabilidad de citarse fuera de contexto. Sugerencia de inserción en el resumen, tras la afirmación sobre el 76.3 % del déficit agregado:

> Esta cifra corresponde al marco monetario de las NTA, que no incorpora el trabajo no remunerado; mide la posición de las mujeres en el ciclo de vida monetario, no su contribución económica integral.

Decisión de Héctor si se incorpora.
