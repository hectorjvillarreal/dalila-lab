# Reporte final — Jacobs, «Digitalization and Taxation»

26 de octubre de 2026 · Esquema aprobado: `esquema_jacobs.md` (20 diapositivas; dos canales; transferencias focalizadas e IVA a plataformas reemplazados)

## Entregables

Los tres compilan con `latexmk -pdf`, sin errores y sin cajas desbordadas:

- `jacobs_digitalizacion.tex`: fuente única.
- `jacobs_digitalizacion.pdf`: 21 diapositivas, 58 páginas con overlays.
- `jacobs_digitalizacion_handout.pdf`: 21 páginas. Se genera desde `jacobs_digitalizacion_handout.tex`, que pasa la opción `handout` y carga la misma fuente.

Revisión visual: convertí todas las páginas a imágenes y corregí etiquetas encimadas (diaps. 4 y 14), texto partido en cajas (8), un diagrama demasiado ancho (9) y una derivación demasiado ancha (12). No queda ningún [VERIFICAR] en pantalla.

Fuente bibliográfica, verificada en el PDF: Jacobs, B. (2017), «Digitalization and Taxation», cap. 2 en S. Gupta, M. Keen, A. Shah y G. Verdier (eds.), *Digital Revolutions in Public Finance*, Washington, D. C., FMI, pp. 25–55.

## Diapositivas y su respaldo en Jacobs

| # | Título | Respaldo |
|---|---|---|
| 1 | Portada | — |
| 2 | De Kaplow a Jacobs: el problema es de información | introducción, pp. 25–26 |
| 3 | Con información perfecta, no habría disyuntiva | p. 25 (primer teorema: repaso del curso) |
| 4 | Dos cosas que el gobierno no ve | pp. 25–28, 32–33; gráfica propia |
| 5 | En el modelo de Mirrlees, la digitalización no sirve de nada | pp. 33–34 (nota 9), 36–37 |
| 6 | Dos canales: fiscalizar mejor y diseñar mejor | pp. 26–27, 50–51 |
| 7 | La evasión cae cuando alguien más informa | pp. 28, 31–32; nota 3 |
| 8 | México: cada factura pasa por el SAT | otra fuente (CFF); respaldo conceptual p. 32 |
| 9 | Brasil: el impuesto se cobra al momento de pagar | otra fuente (Barreix; LC 214/2025); respaldo conceptual p. 32 |
| 10 | El presupuesto de cada persona delata lo que no declara | pp. 28–30 + LISR art. 91 |
| 11 | El capital ya no se esconde tan fácil en el extranjero | pp. 31–32, 39–43 + OCDE (2024) |
| 12 | Un IVA progresivo sin impuesto al ingreso (derivación) | pp. 34–35, notas 10–11 |
| 13 | El IVA personalizado: devolver solo a quien lo necesita | otra fuente (FMI, Barreix); respaldo pp. 34, 51 |
| 14 | Donde no hay reventa, el precio puede depender de cuánto se consume | pp. 37–38, nota 15 + SHCP |
| 15 | Etiquetado | pp. 49–52 |
| 16 | Mirar la historia, el patrimonio y la pareja | pp. 43–49, nota 24 |
| 17 | Los riesgos | pp. 27, 50, 51–52 + CFF art. 69-B |
| 18 | Lo que la digitalización no resuelve | pp. 26, 33–34; nota 7 |
| 19 | Kaplow y Jacobs: la misma teoría, otro énfasis (agregada después de aprobar) | Jacobs, pp. 27, 34–38, 51–52; Kaplow, caps. 1–2, notas 2 y 24, sec. 6.C |
| 20 | Tres ideas para llevarse | conclusión, pp. 50–52 |
| 21 | Puente: el 3 de noviembre | pp. 45–46, 49–50; amarre propio |

## Cifras y hechos verificados

| Dato en pantalla | Diap. | Fuente consultada |
|---|---|---|
| CFDI como único comprobante desde el 1 de enero de 2014 | 8 | Decreto de reformas al CFF, DOF 9-12-2013, art. 29 y transitorio primero (sin excepción para el art. 29); texto en diputados.gob.mx |
| El CFDI se manda al SAT o a un proveedor autorizado, que lo valida y le asigna folio; el comprador debe pedirlo | 8 | CFF, art. 29, primer párrafo y fr. IV (texto vigente, última reforma DOF 9-04-2026) |
| Pago fraccionado (26.5 como tasa estimada; consulta de créditos) | 9 | Barreix, Rocha y Tostes Neto (2025), nota larga, gráfico 3; LC 214/2025, arts. 31–35 (verificado en la sesión del IVA) |
| Pix y factura electrónica en Brasil | 9 | Nota larga de Barreix et al. (2025) |
| Discrepancia fiscal: gastos, compras y depósitos mayores a lo declarado se presumen ingreso; aplica a no inscritos | 10 | LISR, art. 91 (texto vigente, última reforma DOF 1-04-2024) |
| México se comprometió a intercambiar desde 2017; en 2024 mandó datos a 79 jurisdicciones | 11 | OCDE (2024), *Peer Review of the AEOI 2024 Update*, cuadro 1.1 |
| Cashback brasileño (hasta medio salario mínimo per cápita); Devolve ICMS desde 2021, más de 600 mil familias | 13 | Nota larga de Barreix et al. (2025); LC 214/2025, arts. 113 y 118 (verificado en la sesión del IVA) |
| Recuadro 1 y nota 28 del FMI | 13 | de Mooij, Hebous y Keen (2025), IMF WP/25/165, leído en el PDF |
| Tarifa 1: tres bloques; enero de 2021: 0.855, 1.034 y 3.026 pesos por kWh (el excedente, 3.5 veces el básico) | 14 | SHCP, oficio 349-B-1-I-244 (15-12-2020), anexo (copia en fiscalia.com) |
| Presunción de operaciones inexistentes y listas en el DOF y en la página del SAT | 17 | CFF, art. 69-B (texto vigente) |

## Lo que quité por no poder verificarlo

- **Declaración anual prellenada:** solo encontré fuentes secundarias de años anteriores. No sale en la diap. 8.
- **Umbrales de la tarifa 1 en kWh** (75 kWh de básico y 65 de intermedio, según la prensa): no los encontré en una fuente oficial, porque la página de la CFE no abrió por un problema de certificado. La gráfica de la diap. 14 muestra los bloques sin umbrales y con los precios de enero de 2021 del oficio de la SHCP. No usé precios de 2026, porque dos notas de prensa dan cifras distintas.
- **Comunicado del SAT de octubre de 2017** (38 jurisdicciones recibidas): solo lo cita prensa especializada. Usé el dato de la OCDE.
- **«La mitad trabaja en la informalidad»** en la pregunta de la diap. 13: la cambié por «buena parte de los hogares», para no poner en pantalla una cifra sin su fuente.

## Temas del esquema provisional que el capítulo no trata

- **Primer teorema del bienestar:** Jacobs solo usa el segundo. Queda en una línea de repaso (diap. 3).
- **CFDI, pago fraccionado, IVA personalizado y cashback, IVA progresivo de de la Feria y Swistak, empresas fantasma:** vienen de otras fuentes; Jacobs los respalda solo en lo conceptual.
- **Transferencias focalizadas con identidad digital** (Kanbur, cap. 9) e **IVA a plataformas** (Aslam y Shah, cap. 3): reemplazados, como se aprobó, por las diaps. 11 y 16.

## Desviaciones del esquema aprobado

1. Diap. 8: sin declaración prellenada (no verificada).
2. Diap. 14: la gráfica muestra precios de enero de 2021, no los vigentes, y no lleva umbrales en kWh.
3. Diap. 11: el impuesto único al capital y el ISR corporativo como retención se quedaron en la misma diapositiva, como en el esquema; el límite de los beneficiarios finales va en un bloque.
4. Diap. 10: agregué una línea de notación, porque Jacobs usa $g$ para los regalos en la p. 28 y para una transferencia en la nota 10.
5. Diap. 19 (nueva, pedida después de la entrega): contrasta a Kaplow y Jacobs en una tabla de cinco renglones, con una pregunta como último overlay. Las diapositivas de cierre pasan a ser la 20 y la 21; ninguna referencia interna cambia. Queda fuera el contraste sobre el impuesto al capital, porque no leí completo el cap. 9 de Kaplow.
