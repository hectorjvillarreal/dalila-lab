# Presupuesto de afirmaciones, por capítulo

**Declarado antes de redactar**, como manda §2.2 de la instrucción. Se cierra contra el borrador terminado, no contra la intención.

**Umbral:** al menos **12 afirmaciones cuantitativas verificables** por capítulo, de las cuales al menos **6** sean restitución de fuente oficial primaria, y no más del **30 %** en `no_verificable`.

**Regla que gobierna esta hoja:** si un capítulo no llega, **se escribe su declaración de no redactable y se publica en su lugar**, compilada como una página del documento, en el registro del documento y no como nota técnica. Nueve capítulos y tres declaraciones es un resultado; trece capítulos con cuatro de relleno es un fracaso que además no se ve.

---

## Estado al 2026-09-06, con `datos/` completo

Se cuentan filas con al menos dos celdas numéricas en los archivos que alimentan cada capítulo, más los puntos de las razones estructurales de 2024 y 2025. La cuenta es del **material disponible**, no de las afirmaciones que el capítulo hará; esas se cuentan sobre el borrador.

| cap. | capítulo | archivos | filas con dato | razones | veredicto previo |
|---|---|---|---|---|---|
| 1 | Marco macroeconómico | 2 | 40 | — | redactable |
| 2 | Ingresos presupuestarios | 1 | 15 | 4 | redactable |
| 3 | Ingresos energéticos | 1 | 5 | — | **en riesgo** |
| 4 | Gasto: los agregados | 7 | 117 | 2 | redactable |
| 5 | Pensiones | 2 | 10 | 2 | límite, ver nota |
| 6 | Salud | 1 | 9 | 4 | límite, ver nota |
| 7 | Educación | 2 | 47 | 4 | redactable |
| 8 | Inversión | 1 | 16 | — | redactable |
| 9 | Energía | 2 | 18 | — | redactable |
| 10 | Seguridad | 1 | 54 | — | redactable |
| 11 | Gasto federalizado | 1 | 51 | — | redactable |
| 12 | Balance y deuda | 4 | 70 | 4 | redactable |
| 13 | Horizonte demográfico | 1 | 4 | — | **en riesgo** |

**Los dos capítulos en riesgo son dos de los tres que el pacto nombró de antemano** (§2 del pacto: 9 Energía, 10 Seguridad, 3 Ingresos energéticos). El 9 y el 10 se rescataron al construir `energia_empresas.csv` y al agotar el analítico por subfunción. El 3 sigue en riesgo. El 13 no estaba en la lista y aparece por una razón distinta: es un capítulo de síntesis y su material vive en los capítulos 5, 6 y 7, no en un archivo propio.

---

## Nota por capítulo, con lo que falta

**1. Marco macroeconómico. Redactable.** Cuarenta filas entre el marco 2024–2025 y el de mediano plazo 2023–2030, todas del CGPE. **Falta:** el cuadro de sensibilidades (CGPE §4.3, pp. 57–61), que está en páginas de imagen y hay que leer. Sin él el capítulo pierde una de sus cuatro preguntas. Se lee antes de redactar.

**2. Ingresos presupuestarios. Redactable.** Quince renglones del artículo 1o. con las dos bases aprobadas y la columna de lo que cambió la Cámara, más cuatro puntos de razón estructural. **Falta:** confirmar si hubo miscelánea fiscal en 2025 y, si la hubo, su impacto recaudatorio. Si no la hubo, es un hecho y se dice.

**3. Ingresos energéticos. En riesgo, y el pacto lo anticipó.** Cinco renglones propios: transferencias del Fondo Mexicano del Petróleo, ingreso propio de Pemex, ingreso propio de la CFE, e impuesto a la exploración y extracción. Llega a doce afirmaciones **solo si** se cuentan los supuestos de precio, plataforma y tipo de cambio del capítulo 1, que son del mismo objeto pero no del mismo cuadro. **Falta, y es lo que decide:** la trayectoria de la tasa del derecho por la utilidad compartida, que no está en el paquete y hay que buscar en el Diario Oficial. **Si no se obtiene, el capítulo se escribe con lo que hay y declara la ausencia en el cuerpo, o se declara no redactable.** La decisión se toma sobre el borrador, no antes.

**4. Gasto: los agregados. Redactable con holgura.** Ciento diecisiete filas entre siete archivos: los agregados del CGPE, los ramos, las entidades, las tres clasificaciones y los diffs de códigos. Es el capítulo mejor abastecido del documento.

**5. Pensiones. Límite en archivos, redactable en realidad.** Diez filas parecen pocas, pero cada una es un agregado de institución y el capítulo suma cuatro puntos de la serie aprobada de pensiones sobre cuotas, más el Anexo 3 del decreto como fuente independiente. Con eso pasa de doce. **Lo que lo sostiene no es el número de filas sino que el perímetro está adjudicado:** la diferencia entre gastos obligatorios con y sin pensiones del Anexo 3 reproduce nuestro consolidado al mdp en los dos años.

**6. Salud. Límite, y con un hueco que se declara en el cuerpo.** Nueve filas de subsistema más seis puntos de dos razones estructurales. **Falta y no se va a conseguir con la carpeta:** la población por afiliación, que es el denominador de la pregunta «cuánto por afiliado». **El capítulo declara el hueco en su texto, no solo en la bitácora.** Y arrastra un problema mayor: el desplome de 12.2 % real de la función Salud es en parte reclasificación y no se escribe como recorte hasta que el diff lo explique.

**7. Educación. Redactable con holgura.** Cuarenta y siete filas entre función, ramo, subfunción y el FONE por entidad, más cuatro puntos de la comparación adoptada.

**8. Inversión. Redactable.** Dieciséis filas entre los tres capítulos de objeto del gasto y la obra pública por ramo.

**9. Energía. Rescatado.** Estaba primero en la lista de riesgo del pacto. Dieciocho filas tras construir el detalle de Pemex y CFE por vía de entrada: aportación del Ramo 18, ingreso propio y deuda.

**10. Seguridad. Rescatado, con advertencia.** Cincuenta y cuatro filas del perímetro de quince subfunciones, por función y por ramo. **Advertencia:** la caída de 17.6 % real está dominada por el Ramo 36, que pierde 35.4 mmp nominales, y eso huele a reasignación institucional. **No se escribe como recorte hasta que el diff lo explique.**

**11. Gasto federalizado. Redactable.** Cincuenta y una filas entre vías, fondos del Ramo 33 y entidades federativas. **Falta:** la población por entidad, que es el denominador de «por habitante». Sin CONAPO en carpeta, el corte per cápita **no se publica**; se declara el hueco.

**12. Balance y deuda. Redactable, y es donde el documento se distingue.** Setenta filas entre los tres flujos, los tres acervos, los techos y la descomposición de cuatro variables. **La descomposición ya pasó su prueba de aceptación** en las dos añadas de 2022 que estaban en disputa, con residuos de 0.18 y 0.01 puntos, y aplicada a 2025 deja un residuo de 0.07.

**13. Horizonte demográfico. En riesgo por ser de síntesis.** Cuatro filas propias, que son los tres vértices de la tríada con sus perímetros. Llega al umbral contando la proyección de pensiones a 2030 del CGPE (siete puntos) y el rastreo de supuestos demográficos pieza por pieza, que **falta construir**. Si el rastreo no produce material, el capítulo se convierte en una sección del 12 y se dice por qué.

---

## Huecos que se declaran en el cuerpo del documento, no solo aquí

Son cuatro y ninguno se va a resolver con la carpeta. La regla del pacto es decirlo en el documento.

1. **Población por afiliación** para el gasto en salud por afiliado (cap. 6).
2. **Población por entidad federativa** para el gasto federalizado por habitante (cap. 11).
3. **Matrícula** para el gasto educativo por alumno (cap. 7). El paquete tampoco la declara, y esa ausencia es en sí un hallazgo del capítulo 13.
4. **Exposición de motivos del PPEF 2022–2026**, caída en el servidor. Afecta el perímetro canónico de salud, que se reconstruye desde los analíticos con la sustitución declarada.

---

## Cierre

Se rellena al terminar cada borrador, con la cuenta real de afirmaciones.

| cap. | afirmaciones | restituciones | derivaciones | juicios | no verificables | % NV | veredicto |
|---|---|---|---|---|---|---|---|
| | | | | | | | *(pendiente)* |
