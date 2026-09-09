# datos/

Un CSV por cuadro, **generado**, nunca escrito a mano. Cada uno lleva su renglón en
`_fuentes.csv` con documento, ubicación, tier y fecha de acceso.

**Regla que costó dos incidentes en 2025 y 2026:** toda cifra entra desde su fuente o no
entra. Ninguna se teclea de memoria, ni siquiera para una prueba.

`_externas/` guarda los denominadores demográficos copiados de `datos_demograficos/`, para
que el proyecto sea portátil. La copia declara de qué archivo salió.

**Añadidos el 2026-09-09, con la nota de actualización.** `gaceta_anexos_2027.csv` es el
mapa real de los trece anexos que sirve la Gaceta 7121, con la letra que el índice les daba
el día de la entrega: se llenó leyendo la primera página de cada PDF, no el índice, porque
las letras se reasignaron. `vivienda_art61.csv` es la estimación del artículo 61 de la Ley
de Vivienda, copiada del Cuadro 3 del anexo N; los desgloses urbano-rural del Cuadro 1 del
mismo anexo viven en `_herramientas/restituciones/2027.json`, donde el guion de identidades
los cruza contra los totales.
