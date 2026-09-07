# Diffs 2024 → 2025 explicados, antes de redactar

Se anticipan, no se descubren. Este archivo existe para que ninguna caída contable se escriba como recorte. Cada movimiento va con el programa o la unidad responsable que lo produce, y con el veredicto de si es presupuestal o contable.

Fuente en todos los casos: analíticos del PEF aprobado 2024 y 2025, cortes por programa y por función. Aprobado contra aprobado.

---

## 1. La función Salud cae 12.2 % real y la mayor parte no es un recorte

La función 2.3 Salud, Gobierno Federal más entidades, en bruto, pasa de **970,522.5 a 888,903.7 mdp**, una caída de 12.2 % real. Cuatro movimientos la explican y solo uno es una decisión de gasto sobre el servicio.

| movimiento | 2024 | 2025 | qué es |
|---|---|---|---|
| Ramo 19, R023 Adeudos con el IMSS e ISSSTE | 52,324.5 | 339.8 | **no se repite.** Fue una liquidación de adeudos en 2024. Su desaparición no reduce la atención médica de nadie |
| Ramo 19, S038 Programa IMSS-BIENESTAR | 21,623.7 | 0.0 | **se reubica.** El programa sale del Ramo 19 |
| Ramo 47, IMSS-Bienestar como organismo | 128,623.9 | 165,352.2 | **recibe.** Sube 36,728.3 nominales, que es donde aterriza parte de lo anterior |
| Ramo 33, FASSA (I002) | 135,589.4 | 81,220.5 | **cae de verdad**, 54,368.9 nominales, y es lo que hay que explicar |

**Conclusión para el capítulo 6.** De los 81.6 mmp nominales que pierde la función, **73.9 son la desaparición de un adeudo liquidado y la reubicación de un programa**. Lo que queda es la caída del fondo de aportaciones para los servicios de salud, y ésa sí es una decisión. **El titular "el gasto en salud cae 12 %" es cierto de la función y falso del servicio, y el capítulo tiene que decir las dos cosas.**

Advertencia adicional: el IMSS y el ISSSTE, que son quienes prestan la mayor parte del servicio, **suben** en la función Salud (481,083.0 y 81,687.2 contra 455,245.4 y 76,252.2).

---

## 2. Seguridad cae 17.6 % real, y aquí sí es presupuestal

El perímetro de quince subfunciones pasa de **387,626.5 a 333,091.1 mdp**. El movimiento está concentrado y no es una reclasificación.

| movimiento | 2024 | 2025 | qué es |
|---|---|---|---|
| Ramo 36, Guardia Nacional (UR H00) | 70,767.4 | 33,799.8 | **cae a menos de la mitad.** La unidad responsable sigue existiendo en el mismo ramo con el mismo nombre |
| Ramo 36, R001 Provisiones para infraestructura de seguridad | 23,272.7 | 10,208.9 | cae |
| Ramo 36, M001 Actividades de apoyo administrativo | 13,889.1 | 9,284.7 | cae |
| Función 1.6 Seguridad Nacional, todos los ramos | 150,602.8 | 139,011.9 | cae 7.7 % nominal |

**Se comprobó que la Guardia Nacional no se movió de ramo:** en 2025 sigue siendo la unidad responsable H00 del Ramo 36, y no aparece ninguna unidad con ese nombre en Defensa. La caída es de monto, no de ubicación.

---

## 3. Defensa pierde 101 mmp y no es un recorte a las fuerzas armadas

El Ramo 07 pasa de **259,433.8 a 158,287.8 mdp**. La explicación está entera en dos unidades responsables que no son militares:

| unidad responsable | 2024 | 2025 |
|---|---|---|
| H0M Tren Maya, S.A. de C.V. | 125,937.3 | 40,827.8 |
| H0C Grupo Aeroportuario, Ferroviario y de Servicios Auxiliares | 15,172.8 | 2,275.5 |

Por función, la caída vive en **3.5 Transporte** (127,556.9 → 41,772.1), no en 1.6 Seguridad Nacional (103,530.1 → 101,948.0, prácticamente plana).

**Conclusión para los capítulos 8 y 10.** Defensa cae porque los proyectos de transporte que ejecuta bajan de escala, no porque baje el gasto militar. **Cualquier lectura de "recorte a Defensa" que no separe las dos cosas está mal.** Y la contraparte: la obra pública de infraestructura de transporte ejecutada por las fuerzas armadas es una partida de inversión que el capítulo 8 tiene que nombrar.

---

## 4. Un programa nuevo de pensión no contributiva

**U316 Pensión Mujeres Bienestar, 15,000.0 mdp**, no existía en 2024. Se suma a las dos que ya estaban (S176 Adultas Mayores, 483,427.6; S286 Discapacidad, 28,961.4). También aparece **U317 Salud Casa por casa, 2,000.0**.

Efecto en las series: las pensiones no contributivas pasan de 492,909.0 a 527,389.1 mdp. **Si la serie de "pensiones totales" no incorpora el programa nuevo, la razón educación sobre pensiones sale mal.** Por eso la selección se hace por clave de programa y no por nombre.

Trampa de nomenclatura que costó una vuelta: el programa se llama «Personas **Adultas** Mayores», en femenino, y un patrón de búsqueda con «Adultos Mayores» no lo encuentra. Se seleccionan las claves S176, S286 y U316.

---

## 5. Lo que el diff de códigos arroja en bruto

`datos/diffs_2024_2025.csv` lista los ramos, programas presupuestarios y unidades responsables que aparecen o desaparecen entre los dos años, con su monto. Se consulta antes de escribir cualquier variación de programa: **un código que aparece o desaparece produce una variación contable que no es presupuestal**, y es el error de perímetro que la serie FISCUS le viene señalando al género desde 2020.
