# Correcciones al PDF — Clase 3: Incidencia y distorsiones

Aplica estos cambios a `clase03_incidencia.tex`, recompila las dos versiones (con overlays
y `handout`) y, al terminar, reporta punto por punto qué cambiaste. Los números de
diapositiva son los del PDF actual (39 en el cuerpo).

La matemática y las gráficas ya se revisaron y están bien; estos son ajustes puntuales.

---

## 1. Urgente: diapositiva 35 (se ve en pantalla)

La cuota de 2025 ya está verificada: **$1.6451 por litro**, según el Acuerdo de
actualización anual de las cuotas del IEPS para 2025 (DOF, 27-12-2024).

- En la tabla, cambia «≈$1.65 ∗» por «$1.6451».
- Elimina las dos marcas [VERIFICAR]: la de la tabla y la del pie de la diapositiva.
- En el pie, agrega la fuente: «Cuota de 2025: Acuerdo de actualización de cuotas del IEPS
  (DOF, 27-12-2024)».

## 2. Global: «máx» no lleva acento

`babel` en español acentúa los operadores (se ve «máx» en la diapositiva 15). Quita el
acento en todo el documento:

- Opción preferida: `\usepackage[spanish,es-nodecimaldot,es-noaccentedoperators]{babel}`.
- Si esa opción no funciona con tu versión de `babel`, usa `\operatorname{max}` en lugar
  de `\max`.
- Revisa que tampoco queden acentuados `\min`, `\lim` ni otros operadores en el
  documento, incluido el apéndice. Verifica los decimales: deben seguir saliendo con punto.

## 3. Diapositiva 12: gráficas del mercado de trabajo

- **Panel izquierdo.** La oferta de trabajo $L^s$ no es lo bastante inelástica: como está
  dibujada, el trabajador carga cerca de 60 % de la cuota, pero el texto dice «casi toda».
  Haz $L^s$ casi vertical, de modo que el salario neto $w$ absorba la mayor parte de la
  cuña y el costo laboral $W$ apenas suba.
- **Panel derecho.** La llave de «desempleo» va de $E'$ a $F$ e incluye el desempleo que
  ya causaba el salario mínimo antes de la cuota. Cambia la llave para que vaya de $E'$ a
  $E$ con la etiqueta «desempleo adicional».
- Ajusta el pie: «Derecha: el neto no puede bajar y la cuota agrega desempleo.»

## 4. Diapositiva 31: lema de Shephard

Cambia «El último paso usa el lema de Shephard» por «La integral usa el lema de
Shephard». El lema entra en la segunda línea, no en la de la carga excesiva.

## 5. Diapositiva 26: etiqueta encimada

La línea de demanda $D$ atraviesa la etiqueta «carga excesiva». Mueve la etiqueta (y su
línea guía) a una zona libre, por ejemplo debajo de la oferta, a la derecha de $x_0$.

## 6. Diapositiva 9: falta $p_0$

En los dos paneles, agrega la etiqueta $p_0$ en el eje vertical, a la altura de la
frontera entre el área de consumidores y la de productores. Sin ella no se ve que los
consumidores cargan $q - p_0$ y los productores $p_0 - p$.

## 7. Diapositiva 18: definir $R$

$R$ aparece en las demandas sin definirse. Agrega «$R$: ingreso» en la línea de
notación del inicio.

---

## Opcional (decide Héctor)

**Diapositiva 37.** Una línea que une la regla del cuadrado con el caso real: «La cuota de
2026 es 1.87 veces la de 2025; con la regla de la diapositiva 28, la carga excesiva
crecería unas 3.5 veces, antes del argumento correctivo.»

---

## Al terminar

1. Recompila `clase03_incidencia.pdf` y `clase03_incidencia_handout.pdf`.
2. Convierte a imagen las diapositivas 9, 12, 15, 26, 31 y 35 y revísalas visualmente.
3. Confirma que no quede ninguna marca [VERIFICAR] en ninguno de los dos PDF.
4. Reporta la lista de cambios aplicados.
