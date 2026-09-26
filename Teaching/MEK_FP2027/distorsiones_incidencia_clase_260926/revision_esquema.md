# Revisión del esquema — Clase 3: Incidencia, distorsiones y pérdida de bienestar

Aplica estos cambios a `esquema.md` antes de construir la presentación. Los números de
diapositiva se refieren al esquema original; al final, renumera.

Condiciones de la sesión: **150 minutos, en línea (virtual)**. La densidad matemática
debe funcionar en pantalla compartida.

---

## 1. Cambios de contenido

### 1.1 Bloque de mercado de trabajo (diapositivas 12–13): teoría frente a evidencia
El título actual de la diapositiva 12 afirma el resultado de libro como hecho, pero la
evidencia que cita en la misma diapositiva (Saez, Schoefer y Seim, 2019) encontró que el
salario neto no se movió. Esa tensión es lo más interesante de la sesión: conviene
mostrarla, no esconderla.

- **Diapositiva 12 (teoría).** Título: «La teoría: con oferta de trabajo inelástica, la
  cuota recae sobre el salario». Se conservan la gráfica de dos paneles y el caso del
  salario mínimo. La cita de Suecia pasa a la diapositiva siguiente.
- **Nueva diapositiva 13a (evidencia).** Título sugerido: «En la práctica, la carga no
  siempre llega al salario». Contenido:
  - Suecia (Saez, Schoefer y Seim, 2019): la rebaja de la cuota patronal a jóvenes no
    movió su salario neto y aumentó su empleo. Efecto papel matamoscas (flypaper).
  - Vínculo contribución-beneficio (Summers, 1989, *AER Papers and Proceedings* 79(2)):
    si el trabajador valora lo que compra la cuota, esa parte no es impuesto; la oferta
    se desplaza y el salario absorbe la cuota sin pérdida de empleo. Relevante para 2020:
    el aumento de la cuota de cesantía en edad avanzada y vejez va a cuentas individuales
    (AFORE).
  - Kumler, Verhoogen y Frías (2020) pasan aquí: la reforma de 1997 ligó la pensión al
    salario declarado y redujo la subdeclaración. Es evidencia de vínculo
    contribución-beneficio.
- **Diapositiva 13b (informalidad en México).** Se conserva el contenido de Ulyssea y de
  Bosch y Campos-Vázquez. Cierra respondiendo de forma explícita la pregunta de la
  diapositiva 2, en tres líneas: la teoría (salario), la evidencia (la carga se queda
  donde cae) y la informalidad (el ajuste se va al empleo formal), con el vínculo
  contribución-beneficio como variable que decide entre ellas.

### 1.2 Diapositiva 6: corregir la línea sobre Grecia
La redacción actual («los patrones compensaron a los trabajadores por la cuota patronal
adicional») sugiere lo contrario de lo que, según entendemos, encontraron Saez, Matsaganis
y Tsakloglou (2012): la cuota patronal no se trasladó al salario y la absorbieron las
empresas. **Verifica contra el resumen del artículo** y redacta en una línea, sin el verbo
«compensar».

### 1.3 Diapositiva 11: «media armónica»
$e_S e_D/(e_S+e_D)$ es **la mitad** de la media armónica. Corrige o elimina la etiqueta.

### 1.4 Diapositiva 20: condiciones del caso Cobb-Douglas
El resultado de Harberger de que el capital carga con todo el impuesto requiere que las
tres elasticidades sean unitarias: $\sigma_X = \sigma_Y = e_D = 1$. Escríbelo así;
«con Cobb-Douglas» a secas es ambiguo.

### 1.5 Diapositiva 38: la próxima sesión es el 6 de octubre
La siguiente sesión es el **taller del Simulador Fiscal del CIEP (6 de octubre)**; IVA e
impuestos verdes van el 13 de octubre. Título: «Próximas sesiones». Sugerencia: el taller
es buen lugar para correr con el simulador los números del IEPS de las diapositivas 34–36.
Confirma en el índice de Salanié el número de capítulo de la regla de Ramsey.

---

## 2. Densidad y formato para sesión virtual

### 2.1 Diapositivas sobrecargadas
- **Diapositiva 19.** En el cuerpo: planteamiento y resultado para $(\hat w - \hat r)$.
  El álgebra de sombreros completa pasa al apéndice (A2).
- **Diapositiva 30.** En el cuerpo: la medida con variación equivalente y la gráfica de
  demandas marshalliana y hicksiana. La comparación con variación compensada y con el
  excedente de Dupuit-Marshall pasa al apéndice (A1).
- **Diapositiva 33.** En el cuerpo: la derivación, la lectura con $\eta = 0.2$ y el caso
  $\eta \to 1$, más una línea de implicaciones (bases amplias, tasas estables). Las
  estimaciones de Browning (1976) y el rango de Salanié para modelos de EGC pasan a nota
  del presentador (`\note{}`).

### 2.2 Derivaciones en pantalla
- Cada derivación se revela paso a paso con overlays (`\pause` u `\onslide`), una
  línea a la vez. El resultado final va en un bloque destacado.
- Una derivación por diapositiva, como máximo.
- Tamaño mínimo: nada por debajo de `\small` en texto ni en etiquetas de gráficas.

### 2.3 Preguntas rápidas a la clase
Agrega una pregunta breve como **último overlay** de cuatro diapositivas existentes (no
como diapositivas nuevas), para romper el ritmo en línea:
- Diapositiva 9: «¿Quién carga con un impuesto a los cigarros? ¿Y a los boletos de avión
  de temporada baja?»
- Diapositiva 20: «Si $X$ usa mucho trabajo, ¿puede ganar el capital con el impuesto?»
- Diapositiva 28: «¿Qué bien preferirían gravar para minimizar la carga excesiva?»
- Diapositiva 35: «Si el precio subió más que el impuesto, ¿qué nos dice sobre la
  competencia en el mercado?»

### 2.4 Versión para repartir
Compila una segunda versión con `\documentclass[handout]{beamer}` (sin overlays) como
`clase03_incidencia_handout.pdf`, para compartir antes de la sesión.

### 2.5 Apéndice
Después de `\appendix`, con el paquete `appendixnumberbeamer` para que no altere la
numeración principal:
- A1. Variación compensada, variación equivalente y excedente de Dupuit-Marshall.
- A2. Álgebra de sombreros completa del modelo de Harberger.

---

## 3. Idioma
La redacción ya suena natural. Dos ajustes:
- Diapositiva 2: la primera vez, el nombre completo: «cesantía en edad avanzada y vejez».
- Diapositiva 2: la primera vez, «papel matamoscas (flypaper)», para que los alumnos
  encuentren la literatura.

---

## 4. Conteo y tiempos

Con la división de la diapositiva 13, el cuerpo queda en **39 diapositivas** más dos de
apéndice. Tiempos orientativos (incluye descanso):

| Bloque | Diapositivas (nueva numeración) | Minutos |
|---|---|---|
| I. Motivación | 1–3 | 10 |
| II. Equilibrio parcial | 4–15 | 45 |
| III. Equilibrio general | 16–22 | 25 |
| Descanso | — | 10 |
| IV. Distorsiones y carga excesiva | 23–34 | 45 |
| V. IEPS a bebidas azucaradas | 35–37 | 10 |
| VI. Cierre | 38–39 | 5 |
| **Total** | | **150** |

Marca el descanso con una diapositiva de transición mínima o con una nota del presentador
al final del bloque III; no cuenta dentro de las 39.
