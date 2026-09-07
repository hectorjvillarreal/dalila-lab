# Protocolo de lectura en vivo de un paquete económico

Derivado de la corrida de producción del documento propio ITED sobre el Paquete Económico 2025 (2026-09-06). Responde a una pregunta operativa: **qué se descarga primero, en qué orden se verifica, qué se puede afirmar a las dos horas y qué exige veinticuatro, y qué no se afirma nunca sin fuente en mano.**

Está escrito para usarse con el paquete recién entregado y sin tiempo. No sustituye a la instrucción de la corrida; la precede.

---

## 0. Antes de que llegue el paquete

Tres cosas que se preparan con antelación y sin las cuales la primera hora se pierde.

1. **El bundle de certificados TLS.** El portal de la Secretaría presenta una hoja firmada por el intermedio YR1 y envía R10 en el handshake. Se descarga YR1 de su URL de AIA y la raíz cruzada, se concatenan con el almacén del sistema y se pasan con `--cacert`. **Nunca se desactiva la verificación.** Transparencia Presupuestaria comparte la misma cadena rota y el mismo bundle la arregla.
2. **El pacto de estructura**, sellado con hora. Después de varias corridas leyendo al evaluado, «parecido a lo de siempre» es una invitación a reproducirlo de memoria.
3. **Los analíticos del año anterior**, ya descargados y cacheados. Son la mitad de toda comparación y no cambian.

---

## 1. Orden de descarga, por rendimiento decreciente

| # | pieza | por qué en ese lugar |
|---|---|---|
| 1 | **Analíticos del PEF aprobado, cuatro cortes, del año t y del t−1** | Resuelven el 60 % de las filas de gasto. Sin ellos casi todo queda `no_verificable` |
| 2 | **Ley de Ingresos aprobada de los dos años** | Dos peticiones; resuelve el capítulo de ingresos entero y los denominadores de tres razones estructurales |
| 3 | **CGPE** | Marco macro, los tres flujos, los tres acervos y el mediano plazo |
| 4 | **Decreto de Presupuesto de Egresos** | El Anexo 1 da el neteo y el Anexo 3 los gastos obligatorios, que adjudican el perímetro de pensiones |
| 5 | **Iniciativa de Ley de Ingresos** | Solo para medir lo que cambió la Cámara. Contiene su propia exposición de motivos |

**No se busca la exposición de motivos del proyecto de presupuesto como pieza separada.** Para 2022–2026 está caída en el servidor: las subpáginas responden 200 y la enumeran, y los archivos devuelven 404. Se resonda una vez, con el control de 2021, y se sigue.

**Trampa de rutas:** las páginas índice del portal listan los analíticos sin el segmento `/Proyecto/` y esa ruta falla incluso para los años que sí sirven. No tomar sus enlaces como ruta canónica.

**Trampa de hoja:** los analíticos traen los datos en la hoja `Hoja1`. La primera hoja es una carátula de 45 filas por ramo y hace creer que el archivo está vacío.

---

## 2. Orden de verificación

Se verifica **antes** de leer nada del evaluado y antes de escribir una línea.

1. **Las identidades del propio paquete.** Ingresos totales igual a gasto neto total; balance presupuestario igual a ingresos menos gasto neto pagado; no programable igual a costo financiero más participaciones más adeudos; primario igual a balance más costo financiero; gasto neto total menos diferimiento igual a gasto neto pagado.
2. **Las razones a PIB**, con el PIB nominal declarado, contra las publicadas.
3. **La coherencia entre anexos.** Todo concepto que aparezca en dos cuadros del mismo documento debe coincidir en los dos.
4. **El puente entre analíticos y decreto.** Gobierno Federal bruto más entidades menos neteo igual a gasto neto total. Si cierra, los analíticos son los del año correcto y el neteo es el del Anexo 1.
5. **El perímetro de pensiones contra el Anexo 3.** La diferencia entre gastos obligatorios con y sin pensiones es el agregado de la clasificación económica. Si tu construcción no lo reproduce, tu construcción está mal.

**En la corrida 2025 fueron cincuenta pruebas y las cincuenta cerraron.** Ese conjunto es lo que permitió trabajar con un CGPE sin capa de texto: las cifras se leyeron de imágenes y se validaron por identidad, no por relectura.

---

## 3. Qué se puede afirmar a las dos horas

Con los analíticos cargados y las identidades cerradas, **y nada más**:

- El gasto neto total, el programable y el no programable, con su variación real y su porcentaje del PIB.
- El gasto por ramo, con las dos diferencias, nominal y real.
- Los tres flujos y los tres acervos con su nombre correcto.
- Los ingresos por renglón del artículo 1o. y el financiamiento por cada 100 pesos.
- El agregado de cualquier función o subfunción y su variación real.
- Los techos de endeudamiento y su distinción del déficit.

**Lo que NO se afirma a las dos horas, aunque el dato ya esté en pantalla:**

- **Que un ramo se recortó.** Hasta que el diff de códigos diga si cambió de nombre, si un programa se mudó o si una unidad responsable se renumeró. En 2025, Defensa parecía perder 112 mil millones y lo que perdía era obra ferroviaria que pasó a la administración civil; el Ramo 38 parecía desaparecer y solo había cambiado de nombre.
- **Cualquier cifra per cápita.** El denominador se declara o la cifra no se publica.
- **Que una serie toca un mínimo o un máximo histórico.** Exige recalcular los dos últimos puntos con la misma añada de PIB.

---

## 4. Qué exige veinticuatro horas

- **El diff de códigos completo**: ramos, programas y unidades responsables que aparecen, desaparecen o se renumeran, con su monto. Es lo que separa una caída contable de un recorte.
- **La descomposición del acervo en cuatro variables**, con su prueba de aceptación sobre un año pasado antes de aplicarla al año nuevo.
- **Los perímetros que hay que adjudicar**, como pensiones, que exigen contrastar la construcción propia contra una fuente independiente.
- **Las series estructurales**, que exigen la Ley de Ingresos aprobada de varios años para no mezclar bases.
- **La lectura como imagen de las páginas sin capa de texto**, si las hay.

---

## 5. Lo que no se afirma nunca sin fuente en mano

1. **Una variación en millones de pesos sin decir si es nominal o real.** Es el error más común del género y el más fácil de evitar.
2. **Un agregado cuyo perímetro no se pueda enumerar.** Si no puedes listar qué sumaste, no lo publiques.
3. **Una cifra per cápita sin denominador declarado y con fuente.**
4. **Un mínimo o máximo de serie sin añada homogénea.**
5. **Un recorte que el diff no haya explicado.**
6. **Una serie que mezcle proyecto con aprobado**, o exposición de motivos con ley aprobada, en la misma línea.
7. **Un deflactor derivado de agregados publicados redondeados.** Se usa el que declara el CGPE, y si el documento evaluado usa otro, se recupera de sus propios cuadros y se dice cuál es.

---

## 6. La lista de omisiones, para la corrida siguiente

Se llena con la sección «lo que el otro tiene y nosotros no» de la comparación. De la corrida 2025 salieron seis, y las seis son la checklist de 2026:

1. Series desde 2013, que exigen Cuentas Públicas.
2. Un capítulo de economía de los cuidados, cuyo material está en los anexos transversales del decreto y no se explotó.
3. Un capítulo de medio ambiente, cuyo perímetro es una función del analítico que ya se tiene.
4. La comparación contra los Pre-Criterios de abril, documento que no estaba en carpeta.
5. Una vara externa de suficiencia por sector.
6. El contraste del gasto corriente estructural observado contra su límite máximo, cuya fórmula ya se extrajo y no se aplicó.

**Cuatro de las seis no son carencias de fuente sino omisiones propias.** Ésa es la razón de existir de esta sección.
