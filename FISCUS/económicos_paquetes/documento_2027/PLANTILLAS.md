# Plantillas del documento

**Precarga §3.6.** Cuatro plantillas obligatorias. No son sugerencias de estilo: son la
forma en que este proyecto impide que una frase exceda su cálculo. Las tres primeras están
ya escritas como macros en `main.tex` y como relleno en cada capítulo del esqueleto.

---

## 1. Lámina de capítulo

Cuatro piezas, **en este orden**, antes de cualquier sección:

| pieza | macro | qué lleva |
|---|---|---|
| **Titular** | `\titular{}` | Una cifra con **signo y base declarada**: variación real, línea de comparación (P o G), y el objeto nombrado con la anchura exacta del cálculo. |
| **Figura o cuadro principal** | `\input{capitulos/cuadros/CN_N}` | El cuadro que sostiene el titular. Ruta desde el maestro. |
| **Qué cambió** | `\quecambio{}` | Dos o tres movimientos con su clave. Hechos, no interpretación. |
| **Por qué importa** | `\porqueimporta{}` | Una consecuencia. No un adjetivo, no una recomendación de política. |

**El titular pasa por la compuerta semántica antes de compilar.** El sujeto de la frase no
puede ser más ancho que el perímetro de la ficha. Véase
`_aprendizaje/compuerta_semantica.md`.

---

## 2. Ficha metodológica de cierre

`\begin{ficha}{nombre corto}` … `\end{ficha}`, **ocho renglones, siempre los mismos, ninguno
en blanco**:

1. **Perímetro** — enumerable por clave, función o capítulo del objeto del gasto.
2. **Línea de comparación** — P o G, y cuál se usó en cada columna.
3. **Deflactor** — cuál y de dónde sale.
4. **Año de los pesos.**
5. **PIB y añada** — qué PIB y de qué CGPE, porque la añada cambia la razón.
6. **Denominadores** — ninguno, o el que se usó con fuente, año de referencia y cobertura.
7. **Fuentes** — los renglones del archivo de datos que sostienen las cifras.
8. **Qué no puede afirmarse con ellas** — la frase explícita. **Este renglón nunca se deja
   vacío**; si cuesta escribirlo, el perímetro está mal declarado.

---

## 3. Sección «Qué no sabemos», por capítulo

Una sección corta, antes de la ficha. Dos familias:

- **Lo que la fuente no permite afirmar**, con el nombre de la fuente que haría falta y por
  qué no se tiene.
- **Lo que exigiría el presupuesto aprobado del mismo ejercicio**, que bajo régimen de
  lectura en vivo no existe.

No es una disculpa: es la parte del capítulo que un lector usa para saber hasta dónde
apoyarse en él.

---

## 4. Declaración de capítulo no redactable

Va en `99_registro.tex`, sección cuatro, y **sólo si ocurre**. Cuatro renglones:

- **Qué capítulo.**
- **Qué fuente faltó**, con nombre y ruta probada.
- **Qué se intentó**, con las rutas alternativas y sus códigos de respuesta.
- **Qué habría afirmado** el capítulo si la fuente hubiera llegado.

> **Un capítulo declarado no redactable es un resultado. Uno redactado sin fuente es un
> error.** La regla existe porque el reloj empuja a rellenar, y rellenar con una inferencia
> bien argumentada sobre una fuente que no se tiene es exactamente lo que este proyecto le
> señala al género desde 2020.

---

## 5. Recuadro metodológico

`\begin{recuadro}{título}` … `\end{recuadro}`. Para convenciones que valen para **todo** el
documento y **no se repiten por capítulo**. Hoy hay uno obligatorio: el del deflactor, en la
nota de método. La sensibilidad con inflación promedio vive ahí y **en ningún cuadro**, para
que nadie mezcle dos convenciones en una misma columna.
