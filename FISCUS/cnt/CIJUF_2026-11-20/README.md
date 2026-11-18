# CIJUF, sesión interna del 20 de noviembre de 2026: Cuentas Nacionales de Transferencia

Beamer de 20 láminas para unos 30 minutos. Se construyó el 18 de noviembre de 2026 por encargo de Héctor, con la estructura que él propuso: importancia, CNT (la ecuación y su conexión con las cuentas nacionales), contribución, resultados y líneas futuras. Por decisión suya, los resultados se presentan como preliminares y se anuncia la revisión.

- `Villarreal_CIJUF_2026-11-20.tex`: archivo único. Compila con `pdflatex` en dos pasadas y usa el estilo de los decks de CEESP y RIUSS. Las gráficas son pgfplots nativas.
- `datos/prep_cijuf.py`: genera `datos/coordenadas.txt`, que contiene las coordenadas pegadas en el `.tex`, y `datos/verificaciones.txt`.

## Fuentes

| Qué | De dónde |
|---|---|
| Cifras del texto (láminas 7, 9, 11–16) | Versión de agosto de 2026 de NTA_ITED (`nta_ited/paper/paper.tex` y presentación del 20 de agosto, `../NTA_PPT.pdf`) |
| Perfiles de las gráficas (láminas 3, 11, 12, 14, 15) | Corrida local de NTA_ITED `badcf23` (`../nta_dem/profiles_2024_age_sex.csv`), que reproduce el documento con diferencias de alrededor de 1.5 %; promedio móvil de tres edades solo para mostrar |
| Demografía (lámina 4) | Motor demográfico nacional DFD, solo con datos del INEGI, escenario central (`../nta_dem/population_mex.csv`) |
| Proyección (lámina 18) | `../nta_dem/projection_aggregates.csv`: perfiles de 2024 fijos multiplicados por la población proyectada |
| Puntos de la revisión (lámina 17) | `../20261117_revision_metodologia_nta_ited_v1.md`, puntos 1–4 de la sección A |

Las gráficas no llevan etiquetas numéricas cuando la cifra local difiere de la del documento (por ejemplo, 57.7 contra 57.4 %). La única excepción es la lámina 13, que usa directamente las cifras del documento.

## Hallazgo nuevo de esta construcción

Por grupo de edad, la suma de los componentes del financiamiento no reproduce el déficit. En la niñez cubre 0.48 del déficit y en la vejez 2.18. La razón es que el ahorro no se asigna por edad (punto 2 del memo). Esto se menciona en la lámina 17.

## Decisiones de Héctor (18 de noviembre)

1. El orden de autores es correcto, con Juan Pablo primero.
2. La frase «Estudio realizado con el apoyo de la CIJUF» queda como está.
3. Héctor habla con Juan Pablo sobre la revisión antes del viernes.
4. Subir al repo: se sube esta carpeta, en conocimiento de que dalila-lab es público. El resto de `FISCUS/cnt/` sigue sin seguimiento.

Sigue abierto: la lámina 4 afirma que la vejez depende del presupuesto público mucho más que la niñez. La dirección es la estándar en NTA, pero la magnitud de esta serie es preliminar.

## Ajuste del 18 de noviembre: sexo y género

Se aplicó `../nota_sexo_genero_NTA_NTTA.md`. La medición se presenta «por sexo» y la interpretación de mecanismos habla de «género».

- Lámina 10: nota al pie con el texto sugerido por la nota.
- Lámina 12: la diferencia «responde, al menos en parte, a desigualdades de género».
- Lámina 15: las pensiones contributivas «trasladan a la vejez trayectorias laborales desiguales por género».
- Lámina 19: «distribución del trabajo no remunerado por sexo» y «brechas de género en los cuidados».
- Se quitaron los adjetivos «femenino» y «masculino» (láminas 11, 12, 19 y 20) y se cambiaron por «de las mujeres» y «de los hombres».
