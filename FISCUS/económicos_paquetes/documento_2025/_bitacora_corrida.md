# Bitácora — producción del documento propio ITED, Paquete Económico 2025

**Corrida:** FISCUS · Dalila · 2026-09-06 · `INSTRUCCIONES_documento_propio_2025.md`
**Producto:** documento completo del género, autoría ITED, en Markdown y LaTeX.

---

## 1. Qué no llegó y con qué respuesta del servidor

Primero de todo. **Ninguna ausencia bloqueó la corrida.**

| pieza | ruta | respuesta |
|---|---|---|
| Exposición de motivos del PPEF 2025 | `ppef.hacienda.gob.mx/work/models/PPEF2025/docs/exposicion/…` | **404**, con la subpágina respondiendo 200 y enumerándola. Control 2021: 200 `application/pdf` |
| CGPE 2025 con capa de texto | ruta canónica del portal | **200, pero es el mismo archivo de 22,852,266 bytes**, sin texto. No hay otra edición |
| Pre-Criterios Generales 2025 | no se intentó | fuera del alcance declarado. Aparece en la lista de omisiones |
| Cuentas Públicas 2013–2024 | no se intentó | decisión de alcance. Es la ausencia más costosa |
| CONAPO, población por entidad y por edad | no está en carpeta | hueco declarado en el cuerpo del documento |
| Padrón de derechohabientes IMSS/ISSSTE | no está en carpeta | hueco declarado en el cuerpo |
| Trayectoria de la tasa del derecho por la utilidad compartida | no se buscó en el DOF | hueco declarado en el cuerpo, capítulo 3 |

**Descargas logradas y verificadas al byte:** Ley de Ingresos aprobada 2025 y los cuatro analíticos del PEF aprobado 2025.

## 2. Horas, que son el control del ejercicio

| hito | hora (2026-09-06, CST) |
|---|---|
| **Sellado del pacto de estructura**, sin red y sin abrir nada del paquete | **21:36:40** |
| Descarga de las piezas faltantes | 21:39–21:42 |
| Primera lectura del CGPE 2025 (índice) | 21:44 |
| **Primera apertura del documento de CIEP 2025** | **23:08:39** |

Los trece capítulos se redactaron y comprometieron a git antes de las 23:08. El orden no se rompió.

## 3. El hallazgo que condicionó toda la corrida

**El CGPE 2025 se publicó sin capa de texto.** 90 de 91 páginas son imagen. Se comprobó que el portal no sirve otra edición.

Procedimiento adoptado: leer el índice, renderizar los cuatro anexos que resuelven el documento (II.5, II.6, III.1 y III.2, páginas 81, 82, 84 y 85) y leerlos como imagen. **Validación por identidad contable y no por relectura:** 50 pruebas de cierre y de coherencia entre anexos, todas pasan.

Queda declarado en `datos/_fuentes.csv`, en la nota de método del documento y en su anexo metodológico. **No equivale a una restitución de texto y el lector debe saberlo.**

## 4. Cambios al pacto

Tres, todos registrados en `pacto_estructura.md` §8 con su hora y motivo: la precisión de que el objeto primario es el aprobado contra el aprobado; la proveniencia de las cifras del CGPE; y la advertencia anticipada sobre las reclasificaciones de salud y seguridad, escrita **antes** de redactar esos capítulos.

## 5. Presupuesto de afirmaciones

**Trece capítulos, trece redactables, ninguna declaración de no redactable.** 7,722 palabras de prosa y 513 afirmaciones cuantitativas, todos los capítulos por encima del umbral de doce.

Conviene la honestidad sobre el resultado: **dos de los tres capítulos que el pacto puso en riesgo se rescataron construyendo datos que no existían al sellarlo**. El tercero, ingresos energéticos, llega a dieciséis cifras y publica su ausencia en el cuerpo.

Cuatro huecos quedan declarados **en el documento y no solo aquí**: población por afiliación, población por entidad, matrícula, y la trayectoria del derecho petrolero.

## 6. Compilación

**No se compiló.** Esta máquina no tiene toolchain de LaTeX y la preferencia del proyecto es no instalarlo. **El criterio de aceptación 1.3 de la instrucción queda abierto y hay que cerrarlo en Overleaf.**

Lo que sí se hizo: `validar_latex.py`, 96 comprobaciones estáticas, todas pasan. Llaves y entornos balanceados; todo `\input` apunta a un archivo existente; todo `\ref` tiene su `\label`; solo paquetes de la lista permitida; nada exige `shell-escape`; las columnas que pide pgfplots existen en su archivo de datos.

**La comprobación encontró un error que habría roto la compilación entera:** LaTeX resuelve los `\input` desde el directorio del archivo maestro, no desde el del capítulo, y las veintiuna inclusiones de cuadro estaban mal.

**Lo que la comprobación estática no cubre y hay que ver en Overleaf:** que compile en dos pasadas sin errores, desbordes de caja en los cuadros anchos (C1\_2, C12\_2, C12\_4), que siunitx acepte todas las celdas de las columnas tipo S, y la colocación de flotantes.

## 6.bis Entrega para Overleaf

`_entrega/Implicaciones_PE2025_ITED.zip`, 98 KB, 74 archivos, con **main.tex en la raíz del zip y no dentro de una carpeta**: Overleaf compila desde la raíz del proyecto y una carpeta envolvente rompería las 42 inclusiones. Se probó extrayendo el zip en limpio y comprobando que las 42 resuelven.

Cuatro correcciones de maquetación que se hicieron al preparar la entrega, todas por riesgo real de que la compilación falle o se desborde:

1. **Celdas vacías en columnas `S` de siunitx.** Salían como `---` sin llaves, que es un error de compilación. Ahora salen como `{---}`. Afectaba a ocho cuadros.
2. **Marginalia sin ancho de margen.** El género usa notas al margen y el preámbulo tenía márgenes simétricos de 2.6 cm, con lo que cada `\marginpar` se habría salido de la página. Margen derecho a 4.8 cm y `marginparwidth` de 3.3 cm.
3. **`es-tabla` en babel** rotulaba las leyendas como «Tabla»; el género rotula «Cuadro». Retirado.
4. **Cuadros que no caben.** Se añadió ajuste automático: `longtable` para los de más de 26 filas (C7\_3, C10\_1, C11\_1, C12\_2) y `\resizebox` para los de más de 7 columnas (C1\_2, C2\_1, C12\_4).

**Y se cerró un hueco del pacto:** prometía ocho figuras y el borrador no tenía ninguna. Se generaron cuatro (F2\_1, F12\_1, F12\_2, F13\_1) **con las coordenadas en línea**, no leyendo el `.csv` en tiempo de compilación. La proveniencia es la misma, porque el generador lee el `.csv`; lo que se evita es la parte más frágil de un proyecto LaTeX que no se puede probar aquí. Siguen faltando cuatro de las ocho previstas.

## 7. Errores propios que la corrida cometió y corrigió

Se registran porque son el material de la rúbrica.

1. **Agrupar el gasto por nombre de ramo y no por clave.** El Ramo 38 cambió de nombre entre 2024 y 2025 y la herramienta produjo un ramo que desaparecía con 33,170.7 y otro que aparecía con 33,295.9: una variación de 100 % inexistente. **Es el error de perímetro que este proyecto le señala al género desde 2020.**
2. **Seleccionar programas por nombre.** El patrón «Adultos Mayores» no encuentra «Personas Adultas Mayores». La razón educación sobre pensiones totales salió mal hasta que la selección pasó a hacerse por clave.
3. **Coercionar a número una columna que traía nombre.** En los cortes por función, `F` y `FN` vienen como texto; con pandas 3 el dtype es `str` y no `object`, de modo que la comprobación habitual falla en silencio.
4. **Una cifra tecleada de memoria.** El impuesto a la exploración de 2024 se escribió como 8,459.0 cuando la ley dice 7,811.0. Se detectó al contrastar contra el PDF. **Es exactamente lo que la regla de no teclear cifras existe para evitar, y ocurrió en el único lugar donde se tecleó.**
5. **Rutas `\input` mal resueltas**, ver §6.
6. **Etiquetas de eje y encabezados con doble escape.** El generador escapaba texto que ya traía `\%`, produciendo `\textbackslash\{\}\%`. Ocurrió dos veces, en los encabezados de cuadro y en las etiquetas de eje de las figuras, y las dos se detectaron mirando el `.tex` generado, no el texto.

## 8. Series de seguimiento

| serie | 2024 | 2025 |
|---|---|---|
| Impuestos / gastos obligatorios con pensiones | 0.674 | **0.690** |
| … con cuotas del IMSS en el numerador | 0.747 | **0.768** |
| Pensiones + costo financiero / impuestos | 0.559 | **0.571** |
| Pensiones IMSS / cuotas IMSS, serie aprobada | 1.627 | **1.603** |
| Salud del IMSS / cuotas IMSS | 0.851 | **0.798** |
| Pensiones / salud en IMSS+ISSSTE | 2.282 | **2.412** |
| Educación / pensiones y jubilaciones | 0.689 | **0.662** |
| … / pensiones totales | 0.518 | **0.501** |
| Costo financiero / impuestos | 0.256 | **0.262** |
| SHRFSPF / impuestos, en años | 3.40 | **3.51** |

**Dos notas.** La razón pensiones sobre cuotas del IMSS **baja por primera vez** en la serie. Y el punto de 0.60 de 2023 de la razón del capítulo 4 **se retira**: no se reproduce con ninguna de las dos definiciones de pensiones, que dan 0.583 y 0.522.

**Congeladas:** el pasivo pensionario y el supuesto oficial de crecimiento de pensiones, por las razones de la corrida 2024. La serie *ex ante* de pensiones sobre cuotas sigue detenida en 2021 porque la exposición de motivos del PPEF no existe desde 2022.

## 9. Qué cambiar para la segunda prueba

1. **Descargar Cuentas Públicas.** Es la ausencia que más pesa y la única que impide escribir en el registro del género. Sin serie de doce años el documento se lee como otra cosa.
2. **Escribir los capítulos de cuidados y de medio ambiente.** El material está en los anexos transversales del decreto y en una función del analítico, los dos ya en carpeta. **Fueron omisiones nuestras, no carencias de fuente.**
3. **Descargar los Pre-Criterios de abril**, para poder contrastar lo prometido con lo entregado.
4. **Aplicar el límite máximo de gasto corriente estructural** contra el gasto observado. La fórmula ya se extrajo y no se usó.
5. **Cerrar la compilación en Overleaf** antes de dar por terminado nada.
6. **Buscar la trayectoria del derecho por la utilidad compartida en el DOF** en fase 1, no al final.
7. Mantener el orden de sellado y de apertura. Funcionó, y es lo único que permite afirmar que no hubo contaminación de cifras.
