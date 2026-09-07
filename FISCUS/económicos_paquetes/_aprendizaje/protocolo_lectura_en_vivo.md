# Protocolo de lectura en vivo de un paquete económico

**Versión 2**, reescrita el 2026-09-07 tras la corrida de simulación en vivo sobre el Paquete
Económico 2026. La versión 1 se derivó de la corrida de producción de 2025, que trabajó con
piezas aprobadas; ésta se derivó de una corrida que se prohibió usarlas.

Responde una pregunta operativa: **qué se descarga primero, en qué orden se verifica, qué se
puede afirmar a las dos horas y qué exige veinticuatro, y qué no se afirma nunca sin fuente
en mano.**

Está escrito para usarse con el paquete recién entregado y sin tiempo. No sustituye a la
instrucción de la corrida; la precede.

---

## 0. Antes de que llegue el paquete

Cuatro cosas. Sin ellas se pierde la primera hora.

1. **El bundle de certificados TLS.** El portal de la Secretaría presenta una hoja firmada por
   el intermedio YR1 y envía R10 en el handshake. Se descarga YR1 de su URL de AIA
   (`http://yr1.i.lencr.org/`) y la raíz cruzada
   (`https://letsencrypt.org/certs/gen-y/root-yr-by-x1.pem`), se concatenan con el almacén del
   sistema y se pasan con `--cacert`. **Nunca se desactiva la verificación.**
   **YR1 llega en DER: hay que convertirlo con `openssl x509 -inform DER -outform PEM`.** Un
   `cat` del DER produce un bundle que curl acepta sin protestar y que no arregla nada; el
   síntoma es idéntico al de no tener bundle.
2. **El pacto de estructura**, sellado con hora, escrito sin abrir el paquete.
3. **Los analíticos del año anterior, del PROYECTO y del APROBADO**, ya descargados. Son la
   mitad de toda comparación y no cambian.
4. **La carpeta histórica al día**, con las tres piezas de cada ejercicio.

---

## 1. Orden de descarga, por rendimiento decreciente

**La primera parada es la Gaceta Parlamentaria, no el portal de la Secretaría.** Es el
cambio mayor de esta versión.

| # | pieza | dónde | por qué en ese lugar |
|---|---|---|---|
| 1 | **El paquete completo** | `gaceta.diputados.gob.mx/Gaceta/{leg}/{año}/sep/{aaaammdd}.html` y sus anexos `…/PDF/{leg}/{año}/sep/{aaaammdd}-{A..L}.pdf` | Publica ILIF, PPEF, CGPE **y la miscelánea** el mismo día de la entrega, con URLs estables y archivo histórico. El portal de la Secretaría es lento y su almacén se rompe |
| 2 | **Analíticos del PROYECTO, cuatro cortes, año t y t−1** | `pef.hacienda.gob.mx/work/models/PEF/Analiticos_Historico/{t}/**Proyecto**/{ac01_ra_pp_ur_og, ac01_ra_f_ur_og, +_efe}.xlsx` | Resuelven el 60 % de las filas de gasto y **hacen posible el diff en la banda de dos horas** |
| 3 | **La base del proyecto en datos abiertos** | vía `datos.gob.mx/api/3/action/package_search?q=PPEF` → `repodatos.atdt.gob.mx/api_update/secretaria_hacienda/…` | Trae **partida específica, clave de cartera y entidad federativa**, que los xlsx no traen, y los **anexos transversales desglosados por programa** |
| 4 | **Analíticos del APROBADO del año anterior** | mismo árbol, carpeta `Autorizado/` | Para la línea del género |
| 5 | **Denominadores demográficos** | CONAPO por la misma API de datos abiertos | Sin ellos no hay capa per cápita |

### Las tres trampas de ruta, verificadas el 2026-09-07

**Primera: el host.** Los analíticos del proyecto **no** están en `ppef.hacienda.gob.mx`
desde 2021. Ese árbol lleva cuatro ejercicios devolviendo 404 para todo, con las páginas
índice enumerando los archivos. **Están en `pef.hacienda.gob.mx`, bajo `Proyecto/`.** Este
proyecto tardó cuatro corridas en encontrarlo porque nunca sondeó la carpeta hermana de la
que ya usaba.

**Segunda: las páginas índice mienten.** Listan los analíticos sin el segmento de etapa, y esa
ruta falla incluso para los años que sí sirven. **No tomar sus `href` como ruta canónica.**

**Tercera: la ranura única.** El repositorio de datos abiertos guarda **un solo archivo de
proyecto y lo sobrescribe** cuando llega el paquete siguiente. Los años anteriores devuelven
503. **Lo que no se descargue el día de la entrega desaparece.**

### Trampa de hoja y de columna

Los analíticos traen los datos en la hoja **`Hoja1`**; la primera es una carátula de 45 filas
por ramo y hace creer que el archivo está vacío. En los cortes por función, `F` y `FN` vienen
**como texto con nombre** («2 Desarrollo Social»); en los cortes por programa, como número.

---

## 2. Orden de verificación

Se verifica **antes** de leer nada del evaluado y antes de escribir una línea. En la corrida
2026 fueron treinta y tres pruebas y las treinta y tres cerraron.

1. **El Anexo 1 del decreto consigo mismo.** Ramos autónomos, administrativos, generales,
   entidades y empresas, **más los ramos que se imprimen fuera del subtotal**, menos el
   neteo, igual al gasto neto total. *En 2026 los ramos 40 y 32 van fuera del subtotal de
   autónomos: sin sumarlos el anexo falla por 15 mil millones.*
2. **Los analíticos contra el Anexo 1.** Gobierno Federal más entidades igual al bruto.
3. **La base de datos abiertos contra los analíticos.** Dos hosts, dos formatos, el mismo
   número. Es la validación cruzada más barata que existe.
4. **El corte por función contra el corte por programa**, en los dos ámbitos.
5. **El total del artículo 1o.\ igual al gasto neto total del decreto.**
6. **Las identidades internas del CGPE:** balance, RFSP, no programable, devengado contra
   pagado, composición de ingresos.
7. **Las razones a PIB** con el PIB nominal declarado, contra las publicadas.
8. **El Anexo 3:** obligatorios con pensiones menos sin pensiones igual al agregado de
   pensiones de la clasificación económica.
9. **Flujo contra acervo:** el cambio del saldo igual al requerimiento más el efecto de tipo
   de cambio.

**Cuando una identidad no cierra, la primera hipótesis es de OBJETO, no de aritmética.** En
2026 la única que falló fue el balance primario, por 500 millones: el CGPE lo rotula
«económico» donde el año anterior lo rotulaba «presupuestario», y la diferencia es el balance
no presupuestario. Con el objeto bien nombrado, cierra al décimo.

---

## 3. Qué se puede afirmar a las dos horas

**Esta banda se ensanchó respecto de la versión 1**, y por una sola razón: con los analíticos
de los dos años en disco, **el diff de claves cabe en la banda de dos horas**.

Con los archivos cargados y las identidades cerradas:

- El gasto neto total, el programable y el no programable, con su variación real y su
  porcentaje del PIB, **en las dos líneas de comparación**.
- El gasto por ramo, con las dos diferencias, nominal y real.
- **El diff de claves completo:** qué ramos, programas y unidades responsables aparecen,
  desaparecen o se renumeran, con su monto. **Y por tanto, qué caída es real y cuál es
  contable.**
- Los tres flujos y los tres acervos con su nombre correcto.
- Los ingresos por renglón del artículo 1o.\ y el financiamiento por cada cien pesos.
- El agregado de cualquier función o subfunción y su variación real.
- Los techos de endeudamiento y su distinción del déficit.
- **El etiquetado transversal y su traslape**, si la base por programa está disponible.
- **El contenido de la miscelánea**, del índice de la Gaceta.

**Lo que NO se afirma a las dos horas, aunque el dato esté en pantalla:**

- **Cualquier cifra per cápita**, hasta que el denominador esté descargado y declarado.
- **Que una serie toca un mínimo o un máximo histórico.** Exige recalcular los dos últimos
  puntos con la misma añada.
- **Que una cifra propia difiere de la de otro documento por método.** Puede ser por objeto, y
  bajo régimen en vivo no se distingue.

---

## 4. Qué exige veinticuatro horas

- **Las series largas**, que exigen Cuentas Públicas.
- **El reparto de los fondos federalizados por entidad**, que vive en anexos del decreto en
  PDF.
- **Los denominadores que no estén en el catálogo nacional de datos abiertos.**
- **La adjudicación del perímetro de otro documento**, que exige reconstruirlo línea por
  línea.
- **La lectura como imagen de las páginas sin capa de texto**, si las hay. *En 2026 el CGPE sí
  trajo capa de texto: seis páginas de noventa y tres sin ella, contra noventa de noventa y
  una en 2025. No dar por hecho ninguno de los dos casos.*

---

## 5. Lo que no se afirma nunca sin fuente en mano

1. **Una variación en millones de pesos sin decir si es nominal o real.**
2. **Un agregado cuyo perímetro no se pueda enumerar.**
3. **Una cifra per cápita sin denominador declarado y con fuente.**
4. **Un mínimo o máximo de serie sin añada homogénea.**
5. **Un recorte que el diff no haya explicado.**
6. **Una serie que mezcle proyecto con aprobado en la misma línea.**
7. **Un deflactor derivado de agregados publicados redondeados.**
8. **Una cifra tecleada de memoria.** *En la corrida 2026 se tecleó dos veces y las dos veces
   la cifra era falsa. Toda cifra entra al archivo de datos desde su fuente o no entra.*

---

## 6. Las tres verificaciones imposibles en vivo

Se descubrieron en la corrida 2026 y son de la misma familia: **todas exigen el presupuesto
aprobado del mismo ejercicio, que el día de la entrega no existe.**

1. **Separar objeto de perímetro** en una discrepancia contra otro documento.
2. **Medir lo que movió la Cámara** entre el proyecto y el aprobado.
3. **Adjudicar un titular del proyecto** contra el presupuesto que se ejerce.

**No son carencias de una corrida: son la definición del régimen.** Todo documento publicado a
las setenta y dos horas las tiene, las declare o no. Este protocolo obliga a declararlas.

---

## 7. La checklist de omisiones propias

De la corrida 2025 salieron seis. **La corrida 2026 cerró cuatro:**

| omisión de 2025 | estado tras 2026 |
|---|---|
| 1. Series desde 2013 | **abierta.** Exige Cuentas Públicas |
| 2. Capítulo de cuidados | **cerrada.** El anexo transversal de cuidados da la fuente |
| 3. Capítulo de medio ambiente | **cerrada.** Perímetro enumerable: función 2.1 más subfunción 2.2.3 |
| 4. Comparación con los Pre-Criterios | **abierta.** Ese documento sigue sin estar en carpeta |
| 5. Vara externa de suficiencia | **abierta.** El documento sigue sin ninguna |
| 6. Gasto corriente estructural contra su límite | **cerrada.** Se aplicó: 356 980,1 millones de holgura |

Y **la capa demográfica**, que no estaba en la lista y era el hueco mayor: cerrada.

**Las tres que quedan abiertas son las tres que exigen documentos fuera del paquete.** Es una
distinción útil: las omisiones propias se cierran en una corrida; las de carpeta exigen una
decisión de alcance.

---

## 8. Las trampas de clave, actualizadas

La regla era «por clave, nunca por nombre». **No basta.**

1. **Los nombres cambian.** «Pemex Consolidado» pasó a «Petróleos Mexicanos» y «CFE
   Consolidado» a «Comisión Federal de Electricidad» entre 2025 y 2026. Un filtro por nombre
   devuelve cero.
2. **La clave misma cambia de prefijo.** La Pensión Mujeres Bienestar es **U316** en 2025 y
   **S316** en 2026: cambió la modalidad, no el número. **Se selecciona por el número de
   programa dentro del ramo, y se verifica la modalidad contra el diff.**
3. **Los programas se renumeran conservando el objeto.** El programa mayor de salud del IMSS
   pasó de 011 «Atención a la Salud» a 031 «Servicios de atención a la salud»: ni la clave ni
   el nombre lo encuentran.
4. **Los ramos enteros cambian de unidad responsable.** Todo el Ramo 33 pasó de la UR 420 a la
   411 en 2026.
5. **Los organismos cambian de ramo, a veces todos los años.** IMSS-Bienestar: Ramo 19 en
   2024, 47 en 2025, **56 en 2026**.

**Corolario:** la única agregación estable es por **función y subfunción**, que son un catálogo
nacional y no cambian con la estructura administrativa. Todo perímetro de rubro se define ahí
primero y se desagrega por ramo después.

---

## 9. La comprobación estática de LaTeX

**Se corre siempre, antes de compilar**, y cubre: llaves y entornos balanceados; que todo
`\input` **se resuelva desde el directorio del archivo maestro**; que todo `\ref` tenga su
`\label`; que los paquetes estén en la lista permitida; que nada exija `shell-escape`. **Y
debe imprimir qué no comprueba.**

**En 2025 encontró veintiuna inclusiones mal resueltas. En 2026 encontró veintiuna, otra
vez.** Las dos veces habrían roto la compilación entera y ninguna lectura del texto las habría
revelado. Es el control que más veces ha pagado su costo.

---

## Historial
- 2026-09-06 · versión 1 · derivada de la corrida de producción del documento propio 2025.
- 2026-09-07 · **versión 2** · derivada de la corrida de simulación en vivo sobre el Paquete
  Económico 2026. Cambios mayores: la Gaceta Parlamentaria como primera parada; la ruta real
  de los analíticos del proyecto; la ranura única del repositorio de datos abiertos; el diff
  de claves movido a la banda de dos horas; las tres verificaciones imposibles en vivo; las
  trampas de clave ampliadas de una a cinco; y la checklist de omisiones con cuatro de seis
  cerradas.
