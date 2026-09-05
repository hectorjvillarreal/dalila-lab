# Instrucción de adquisición — Paquetes Económicos federales 2018–2026

**Proyecto:** FISCUS
**Ubicación de trabajo:** `FISCUS/económicos_paquetes/`
**Máquina:** Dalila
**Tipo:** instrucción de trabajo (no es build instruction registrada)
**Alcance:** adquisición únicamente. No hay interpretación en esta corrida.

---

## 1. Contexto

Construir el archivo local de los paquetes económicos federales de México,
ejercicios fiscales 2018 a 2026, desde la fuente oficial de la Secretaría de
Hacienda y Crédito Público.

Todo lo que se descargue en esta corrida es **tier 1: fuente primaria oficial
(SHCP)**. No se mezcla con material derivado.

---

## 2. Fuente

Punto de entrada:

```
https://www.finanzaspublicas.hacienda.gob.mx/es/Finanzas_Publicas/Paquete_Economico_y_Presupuesto
```

Desde ahí, cada ejercicio fiscal tiene su propia página. Los CGPE y la ILIF son
alcanzables en pocos pasos. El PPEF requiere entrar a su sección propia dentro
del ejercicio; los PDFs están ahí, un nivel más adentro.

**Regla dura:** navega hasta encontrar los documentos. **No construyas URLs por
analogía ni por patrón.** Si un documento no aparece donde esperabas, regístralo
en la bitácora como faltante en vez de adivinar la ruta. Un faltante reportado es
recuperable; un archivo mal asignado no se detecta después.

---

## 3. Qué descargar, por ejercicio fiscal

1. **Criterios Generales de Política Económica (CGPE)** — documento completo.

2. **Iniciativa de Ley de Ingresos de la Federación (ILIF)** — iniciativa y
   exposición de motivos.

3. **Proyecto de Presupuesto de Egresos de la Federación (PPEF)** — en la sección
   del PPEF hay dos tipos de material:

   - **(a) exposición de motivos y proyecto de decreto — ESTO SÍ**
   - **(b) tomos, anexos, analíticos, archivos por ramo — ESTO NO**

   Descarga solo (a). Si la distinción no es obvia en algún ejercicio, descarga lo
   que claramente sea (a) y anota en la bitácora lo que no supiste clasificar.
   No descargues por si acaso.

### Ejercicios

2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026. Nueve en total.

**El año de la carpeta es el ejercicio fiscal, no el año de entrega.** El paquete
del ejercicio 2018 se entregó en septiembre de 2017.

**No descargues el paquete 2027.** Se entrega el 8 de septiembre de 2026 y tiene
su propia corrida.

---

## 4. Estructura de carpetas

Una carpeta por ejercicio. Los PDFs van sueltos dentro de la carpeta del año, sin
subcarpetas por pieza.

```
FISCUS/económicos_paquetes/
  2018/
    2018_cgpe_criterios-generales.pdf
    2018_ilif_iniciativa.pdf
    2018_ilif_exposicion-motivos.pdf
    2018_ppef_exposicion-motivos.pdf
    2018_ppef_proyecto-decreto.pdf
  2019/
  2020/
  2021/
  2022/
  2023/
  2024/
  2025/
  2026/
  _manifiesto.csv
  _bitacora.md
```

Nomenclatura de archivo: `{ejercicio}_{pieza}_{slug}.pdf`

`pieza` es uno de: `cgpe`, `ilif`, `ppef`.

---

## 5. Manifiesto

`_manifiesto.csv`, una fila por archivo descargado:

```
ejercicio, pieza, nombre_archivo, url_origen, fecha_acceso_iso, bytes, sha256, tier
```

`tier` es siempre `oficial_primaria` en esta corrida.

El manifiesto es para procesarlo, no para leerlo. La bitácora es para leerla.

---

## 6. Verificación

Después de cada descarga, comprueba que el archivo empieza con `%PDF`.

Los portales de gobierno devuelven páginas de error HTML con código 200 y
extensión `.pdf`. Si el archivo no es un PDF válido: bórralo, reinténtalo una vez,
y si vuelve a fallar regístralo en la bitácora con la URL y lo que devolvió el
servidor.

---

## 7. Conducta de red

- Máximo una petición cada 2 segundos.
- Descargas secuenciales, no paralelas.
- Si la corrida se interrumpe, al reanudar salta los archivos que ya estén en el
  manifiesto con sha256 válido.

---

## 8. Bitácora

Escribe `_bitacora.md` con esta estructura:

```markdown
# Bitácora de adquisición — paquetes económicos 2018–2026

## Corrida
Fecha y hora de inicio y fin (ISO).
Fuente: URL del punto de entrada.
Tier: oficial_primaria (SHCP).
Alcance solicitado: CGPE, ILIF, PPEF (exposición de motivos y proyecto de
decreto). Tomos y anexos excluidos por instrucción.

## Resultado por ejercicio
Tabla: ejercicio | CGPE | ILIF | PPEF | archivos | MB
Marca cada pieza como completa, parcial o ausente.

## Faltantes
Por cada documento no obtenido: ejercicio, pieza, qué se intentó, qué respondió
el servidor.

## Anomalías
Todo lo que no encaje: PDFs sospechosamente pequeños, documentos cuya
denominación no corresponde a la esperada para el ejercicio, material que no
supiste clasificar entre (a) y (b) del PPEF, redirecciones raras.
Descríbelo, no lo resuelvas.

## Notas de estructura del portal
Dónde estaba cada pieza y cuántos pasos de navegación hicieron falta, por
ejercicio. Esto sirve para la corrida del 2027.
```

Un hueco documentado vale. Un hueco tapado con un archivo equivocado no.

---

## 9. Al terminar

Escribe la bitácora e imprime en pantalla un resumen de tres líneas: total de
archivos, total de MB, número de faltantes.

**No interpretes el contenido de los documentos. No clasifiques, no resumas, no
extraigas nada.** Esta corrida es solo adquisición.
