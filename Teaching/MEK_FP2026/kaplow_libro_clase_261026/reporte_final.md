# Reporte final — Kaplow, capítulos 1 a 3

26 de octubre de 2026 · Esquema aprobado: `esquema_kaplow.md` (27 diapositivas)

## Entregables

Los tres compilan con `latexmk -pdf`, sin errores y sin cajas desbordadas:

- `kaplow_marco_unitario.tex`: fuente única.
- `kaplow_marco_unitario.pdf`: 27 diapositivas, 83 páginas con overlays.
- `kaplow_marco_unitario_handout.pdf`: 27 páginas. Se genera desde `kaplow_marco_unitario_handout.tex`, que pasa la opción `handout` y carga la misma fuente, igual que en la sesión del IVA.

Revisión visual: convertí todas las páginas del handout a imágenes y corregí las cajas con texto partido (diaps. 2, 3 y 12), las etiquetas encimadas (diaps. 4 y 9), la tabla desalineada (16) y el exceso de altura (17 y 20).

Las notas del presentador están en `\note{}` y no salen en los PDF. Para verlas: `\setbeameroption{show notes}`.

## Diapositivas y su respaldo en Kaplow

| # | Título | Respaldo |
|---|---|---|
| 1 | Portada | — |
| 2 | Una disciplina hecha pedazos | cap. 1, pp. 1–3 |
| 3 | Lo que ya vimos, con otra luz | propia |
| 4 | Ninguna política está completa sin su financiamiento | sec. 2.A, pp. 15–17 |
| 5 | Un impuesto plano puede redistribuir todo o nada | sec. 2.A, pp. 17–19 |
| 6 | La distorsión que importa es la del trabajo | cap. 1, p. 2; nota 12, p. 21 · ejemplo: sec. 6, p. 123 |
| 7 | Para redistribuir: impuesto al ingreso y transferencias | sec. 2.B, pp. 14, 19–21; notas 2 y 16 |
| 8 | Comparar manzanas con manzanas | sec. 2.C.1, pp. 22–25 |
| 9 | La reforma distributivamente neutral: la idea | sec. 2.C.2, pp. 25–27 |
| 10 | El modelo | **secs. 4.A y 6.A–6.B** (fuera) |
| 11 | La reforma neutral: el resultado | **secs. 6.B.1–6.B.2** (fuera); enunciado en cap. 1, p. 2 |
| 12 | Separar no es ignorar la distribución | sec. 2.C.3, pp. 29–31 y 34 |
| 13 | Primera consecuencia: impuestos a bienes | cap. 1, pp. 2, 5; sec. 2.C.2, pp. 28–29 |
| 14 | Segunda consecuencia: bienes públicos | cap. 1, pp. 3, 6; sec. 2.C.1, p. 25 · prueba: secs. 8.A–8.C |
| 15 | Tercera consecuencia: regulación y externalidades | cap. 1, p. 3; secs. 2.B, 2.C.2, 3.A.2 · gasolina y doble dividendo: sec. 8.G |
| 16 | Los supuestos que sostienen el marco | cap. 1, pp. 2, 4; secs. 2.B, 2.C.2, 2.C.3 |
| 17 | ¿Y en México? | nota 24, p. 31; nota 2, p. 15 |
| 18 | Las listas de criterios no deciden nada | sec. 3.A, pp. 36–39 |
| 19 | Bienestarismo | sec. 3.B.1, pp. 41–42 |
| 20 | Dos razones distintas para redistribuir | sec. 3.B.1, pp. 42–44 |
| 21 | De Rawls al utilitarismo, y el principio de Pareto | sec. 3.B.2, p. 45; cap. 1, p. 9 · prueba: sec. 13.A.2 |
| 22 | El utilitarismo tolera mucha pérdida al redistribuir | sec. 3.B.2, pp. 46–48 |
| 23 | ¿Importa qué función se elija? | sec. 3.B.3, pp. 48–50 |
| 24 | Lo que cambia en la práctica | secs. 2.A, 2.C.1, 3.A.2 · ponderadores: cap. 8, p. 180 |
| 25 | Tres ideas para llevarse | caps. 1–3 |
| 26 | Las críticas, en su versión más fuerte | sec. 2.C.3, pp. 31–33; nota 24 |
| 27 | Puente | propia; nota 2, p. 15 |

## Referencias externas verificadas

Comparé volumen y páginas con la bibliografía del libro (pp. 417–454). Los artículos no están en la carpeta, así que no verifiqué los números de fascículo y no los puse.

- Kaplow (1996), *National Tax Journal* 49: 513–533. Al pie de la diap. 14.
- Kaplow y Shavell (2001), *Journal of Political Economy* 109: 281–286. Al pie de la diap. 21.
- Kaplow y Shavell (1994), *Journal of Legal Studies* 23: 667–681. En las notas de la diap. 15, no al pie.
- Feldstein y Feenberg (1996), diap. 22: se presenta como «citados por Kaplow» (nota 15); no lo verifiqué en el original.

## Ideas que no están en los capítulos 1 a 3

- El modelo y la derivación (diaps. 10–11): cap. 6, aprobados con su marca al pie.
- El ejemplo del 2 % de poder de compra (diap. 6): cap. 6, p. 123.
- La gasolina como impuesto pigouviano y el doble dividendo (diap. 15): sec. 8.G.
- «Distorsiona dos veces» (Kaplow y Shavell, 1994): sec. 8.G, nota 41; está en las notas de la diap. 15.
- La prueba de que todo criterio que no es de bienestar viola Pareto (diap. 21): sec. 13.A.2; el bosquejo está en las notas.
- La respuesta de Kaplow a Sen y Rawls (diap. 26): sec. 13.B.4.
- Las pruebas del caso de bienes públicos (diap. 14): secs. 8.A–8.C.
- Los ponderadores distributivos en costo-beneficio (diap. 24): cap. 8, p. 180.
- Amarres propios: diaps. 3, 17 (FMI y Barreix, tomados de la sesión del IVA) y 27 (digitalización, cuentas nacionales de transferencia, Shafik).

## Desviaciones del esquema aprobado

1. Diap. 15: «distorsiona dos veces» pasó a las notas del presentador (me dejaste la decisión).
2. Diap. 20: la observación de que la curvatura de la utilidad le resta peso a $e$ (nota 10) y la fórmula con $\gamma$ pasaron a las notas, para no pasar de seis líneas.
3. Diap. 16: la tabla se muestra completa, sin overlays por renglón; con overlays las filas se desalineaban.
4. Diap. 26: agregué una pregunta como último overlay: «¿Cuál de estas críticas pesa más en México?».
5. Diap. 3: la pregunta guía va como último overlay: «¿A cada peso de gasto público hay que cargarle el costo de los fondos?». Se contesta en la diap. 14.
6. Diap. 4: los números son los de Kaplow, en dólares; el texto habla de «beneficio igual en dinero».
