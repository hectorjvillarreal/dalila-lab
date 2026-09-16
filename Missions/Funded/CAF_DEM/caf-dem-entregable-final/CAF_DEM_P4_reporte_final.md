---
mission: CAF_DEM
producto: P4
tipo: reporte-final-claude-code
responde_a: CAF_DEM_P4_instrucciones.md (Beth y Cath, 2026-09-16)
rama: p4-version-final
fecha: 2026-09-16
para: Héctor Juan Villarreal Páez · Juan Pablo López Reynosa
---

# CAF_DEM · Producto 4 — Reporte final de ejecución

**R sí se pudo ejecutar.** Se instaló en el entorno conda `dalila` (r-base 4.x con `readxl`, `tidyverse`, `forecast`, `tseries`, `strucchange`, `knitr`) y el Bloque B corrió completo.

Resultado global: `main.tex` compila sin errores, sin referencias ni citas indefinidas, 102 páginas, ocho secciones y dos apéndices. El PDF está en `main.pdf`.

---

## 1. Bloques completados y bloques con incidencia

| Bloque | Estado | Incidencia |
|---|---|---|
| A — Revisión general | Completo | Ninguna. A.4 se escribió (Lei Complementar 200/2023, *Regime Fiscal Sustentável*); ver §5 de este reporte. |
| B — Corrección de proyecciones | Completo con incidencia | El control de rango **no dejó de disparar del todo**: 2 alertas persisten tras ambas opciones. Ver §3. |
| C — Sección 6 | Completo | §6.2 por Ruta A. Brasil sin cifra primaria de registro vital (pendiente declarado). |
| D — Sección 7 | Completo (4 pp.) | La cifra «una cuarta parte del tiempo que tuvo Europa» se dejó **cualitativa**: no hay fuente citable en el corpus del documento. Ver §5. |
| E — Sección 8 | Completo (2 pp.) | Ninguna. |
| F — Apéndice A | Completo (5 pp.) | El PDF del BID no trae portada, título ni autores; ver §5. |
| G — Apéndice B | Completo (6 pp.) | Ninguna. Quiebres recuperados del HTML tejido sin recomputar (las series observadas no cambiaron). |
| H — Bibliografía, compilación, verificación | Completo | Lista de verificación H.3 cumplida íntegra (detalle en §6). |

## 2. Las tres ⚠ DESVIACIÓN

| Desviación | Estado |
|---|---|
| **1** — Eliminar *Apéndice B: Fichas-país* (P1) | **Aplicada.** Confirmada por Héctor el 2026-09-16. Las fichas de riesgo viven en §6.5. |
| **2** — Discusión del sesgo del WPP en §6.4 sin revertir la decisión de §5.1 | **Aplicada.** Se cita la presentación de Fernández-Villaverde (Héctor autorizó citar material no publicado) y cada cifra se ancla en el registro vital nacional. |
| **3** — Apéndice B pasa a ser el anexo técnico | **Aplicada.** Quiebres estructurales (tabla + 5 figuras) y diccionario de la base P4. |

## 3. Resultado del Bloque B

**Series re-estimadas:** las doce series de gasto funcional (salud y pensiones × 6 países). Los agregados del WEO no se tocaron.

**Opción elegida: Opción 1** (ventana de validación 2016–2019, anterior al choque). Regla de elección, escrita en `pipeline_P4.R`: menos alertas de rango; empate → menos alertas *nuevas* (series que no disparaban en P3); empate → menos fallos Ljung-Box; empate → menos MASE > 2.

| Variante | Alertas de rango | Alertas nuevas | Ljung-Box < 0.05 | MASE > 2 (funcionales) |
|---|---|---|---|---|
| P3 (réplica de control) | 3 | 0 | 0 | 2 |
| **Opción 1** (ventana pre-2020) | **2** | **0** | 0 | 3 |
| Opción 2 (sólo amortiguadas) | 2 | 1 (Colombia pensiones, a la baja) | 0 | 3 |
| Diagnóstico 1+2 (no previsto en instrucciones; sólo informativo) | 2 | 1 | 0 | 5 |

**Las tres series objetivo:**

| Serie | P3 (2030) | Opción 1 (2030) | ¿Alerta? |
|---|---|---|---|
| Pensiones México | 3.01 → **5.30** | 3.01 → **2.99** (Holt amortiguado) | **Corregida** |
| Salud Chile | 6.03 → 12.38 | 6.03 → 12.53 (ARIMA) | Persiste |
| Salud México | 1.24 → 1.65 | 1.24 → 1.65 (ETS) | Persiste |

Conforme a la instrucción («si sigue disparando después de ambas opciones, no forzar»), Chile salud y México salud conservan su proyección y la advertencia textual (caption de la figura, §5.3.3 y ADVERTENCIA DE USO del diccionario). Se reporta aquí y en el texto.

**Poda (B.2), con MASE > 2 tras la re-estimación (10 series):** ingresos Chile (2.24) y Costa Rica (2.89); balance primario Brasil (4.23), Chile (2.37), Costa Rica (5.59), Panamá (3.26); deuda neta Costa Rica (7.38); salud Colombia (2.28) y México (2.09); pensiones Brasil (2.60, nueva bajo Opción 1). Se retiran de las figuras y se conservan en la Tabla de modelos con la marca «no (n.i.)» y en la base con nota. **La Figura del balance primario se eliminó por completo** y se sustituyó por el párrafo explicativo en §5.3.2.

**Sincronía (B.3):** regenerados en el mismo pase `graficas/fig_proj_{ingresos,deuda,salud,pensiones}.png`, `tablas/tab_modelos.tex` (ahora con columnas *Ventana* y *Figura*), `tablas/tab_frecuencia_modelos.tex` (ETS 15 · Holt 10 · ARIMA 5), `base_analisis_P4.csv` (2 038 filas) y `base_analisis_P4_diccionario.csv` con ADVERTENCIA DE USO reescrita. `base_analisis_P3.csv` y su diccionario quedan intactos como *provenance*. `fig_proj_balance.png` fue borrada.

## 4. Ruta usada para (r − g) en §6.2

**Ruta A.** El WEO abril 2025 completo se descargó de `imf.org/-/media/Files/Publications/WEO/WEO-Database/2025/april/WEOApr2025all.xls` (es un TSV UTF-16, no un Excel; la URL `.ashx` que sugiere el sitio devuelve *BlobNotFound*). Se incorporaron a la base P4 dos series con su `tipo`, `fuente` y `cobertura`: *Crecimiento nominal del PIB* (código `NGDP`, variación del PIB corriente en moneda nacional) y *Balance fiscal global* (`GGXCNL_NGDP`). El pago neto de intereses es balance primario − balance global; la tasa implícita es intereses del año / deuda neta del año anterior.

Decisiones de cálculo, todas escritas en la nota de la Tabla 15:
- $(r-g)$ sobre 2015–2024 como **razón de sumas** para $r$ (suma de intereses / suma de deuda neta inicial) y media geométrica para $g$. La razón de sumas se adoptó porque la tasa implícita sobre deuda *neta* es inestable cuando ésta es pequeña (Chile 2015–2017 daba −5 %, −9 % y +41 %).
- Columna de sensibilidad con las proyecciones del propio WEO 2025–2030.

Ordenamiento resultante (brecha, ventana histórica): Panamá 5.2 · Brasil 3.1 · México 1.5 · Chile 1.4 · Costa Rica 0.2 · Colombia 0.0. Con la ventana proyectada Colombia pasa a 1.4 y Costa Rica a −0.7; el texto explica el porqué.

Los cálculos están en `calc_seccion6.py`; salidas en `seccion6_espacio_fiscal.csv` y `seccion6_presion_demografica.csv`.

## 5. Datos que una instrucción pedía y no estaban disponibles (reportados, no completados)

1. **Gasto en pensiones y salud de 2024** (§6.3 pide `gasto_2024`). La base termina en 2020/2019/2017. Se usó el último observado y se declara en la ecuación y en la tabla (año entre paréntesis).
2. **TFR de registro vital para Brasil.** No hay publicación primaria del IBGE en el corpus; la celda dice *Pendiente* y la cifra de la presentación (1.52/2025) se reporta sólo como corroboración en nota.
3. **Nacimientos 2024 observados vs WPP para Costa Rica y México.** No figuran en la comparación de 37 países de la fuente; celdas «n.d.».
4. **Título, autores y número de serie del paper del BID.** El PDF empieza en el abstract; sólo trae la nota de copyright (reproducida textualmente en la bibliografía). Se citó como *Banco Interamericano de Desarrollo (2026), Spending Smarter*, siguiendo la instrucción H.1. **Hay que confirmar autores y serie contra la portada oficial antes de entregar.**
5. **«Aproximadamente una cuarta parte del tiempo que tuvo Europa»** (Bloque D). No hay fuente en el `.tex`, en la base ni en los insumos. Se escribió «una fracción del que tuvieron las economías europeas». Si se quiere la cifra, hace falta una cita (p. ej. la comparación clásica Francia 115 años vs. Brasil/Colombia ~20 para pasar de 7 % a 14 % de 65+), que no verifiqué en esta sesión.
6. **Cobertura contributiva de la PEA, diferencial de ingreso a PPA, magnitud de la *saúde suplementar* (ANS), perfiles NTA de gasto por edad.** Promesas heredadas del P3 al P4; ninguna está en las bases. Las cuatro frases se reescribieron como pendientes declarados (§2.4, §3.3.2, §4.1, nota de §4.3.1).
7. **Cobertura 65+ de Chile** sigue *Pend.* en la Tabla 8 (SEDLAC no incluye a Chile).
8. **Cifra de TFR de México 2025 (1.51).** La propia fuente advierte que es extrapolación (~72 % de registro en el año); se incluye con esa nota y se ancla en ENADID 2023 (1.60), que es encuesta, no registro. Se dice en la tabla.

## 6. Cadenas no localizadas, referencias rotas y comentarios eliminados

- **Cadenas no localizadas:** ninguna de fondo. Una edición del §1.4 falló al primer intento porque el texto real terminaba en «agregados fiscales relevantes» y no en «agregados fiscales»; se reintentó con el texto exacto. El HTML se llama `FISCAL_DEMO_v4(1).html`, no `FISCAL_DEMO_v4_1_.html` como decía la instrucción.
- **Referencias cruzadas rotas encontradas:** ninguna indefinida. Se resolvieron vía `\ref` las 14 referencias escritas a mano («Sección 3.1.6», «3.3.1», «3.2», «4.2.1», «2.4», «3.1.1» ×2, «3.1.5», «5.3.1», «Secciones 3.1 y 3.2» ×2, y «Tabla~1» ×1). Para ello se añadieron 16 `\label` a secciones que no lo tenían. La Tabla de integración (`tab_integracion.tex`) existía en `tablas/` pero no estaba en el documento; se incorporó en §5.3.1 porque §5.3.2 la necesita.
- **Comentarios de deliberación eliminados:** el `.tex` de P3 no contenía comentarios de deliberación (sólo separadores estructurales). Se eliminó la **«Nota de cierre»** de P3 (`\subsection*` no numerada al final de §5), cuyo contenido era: (i) que los resultados de quiebres estructurales «están disponibles» y su exclusión del cuerpo fue decisión de diseño → ahora es el Apéndice B; (ii) la asimetría de cobertura temporal WEO 2024 vs GFS 2017–2020 → ya está en la tercera precisión de §5.3.3. Copia del texto eliminado en `/tmp/claude-1000/nota_cierre_eliminada.tex` (temporal de sesión).
- **Nota (a) huérfana (A.1):** corregida; empieza en «el RGPS es de afiliación obligatoria…».
- **Bloques huérfanos (A.2):** *Bases de datos* y *Fuentes normativas* son ahora `\section*` con entrada en el índice.
- **Citas (A.3):** 20 `\cite*` (había 1). Nuevas entradas: Aaron (1966), BID (2026), DANE (2025), Fernández-Villaverde (2026), INE Chile (2025), INEC Costa Rica (2025), INEC Panamá (2025), INEGI (2024), Krueger y Ludwig (2007).
- **Cosméticos (A.5):** Panel A y B de la Tabla 9 alineados a la derecha (todas las cifras tienen dos decimales, así que alinean por punto sin `siunitx`); `\allowbreak` en `SAR/AFORE/PENSIONISSSTE`. Un `\headheight` de 14 pt para silenciar el aviso de `fancyhdr`.
- **Problema de compilación resuelto:** babel-spanish falla con `\,\%` dentro de modo matemático («Incompatible glue units»); se movió el `\%` fuera de `$…$` en cuatro lugares.
- **TinyTeX:** hubo que instalar `microtype adjustbox collectbox setspace parskip tools xcolor titlesec xltabular ltablex multirow enumitem pdflscape hyphen-spanish`.

## 7. Conteo de páginas

| Parte | Páginas | Extensión |
|---|---|---|
| Documento completo | 1–102 | 102 pp. |
| §6 Análisis heurístico de riesgos | 67–82 | 16 pp. |
| §7 Consideraciones de política | 83–86 | 4 pp. (objetivo 3–5) |
| §8 Conclusiones | 87–88 | 2 pp. (objetivo 2–3) |
| **Apéndice A — Equilibrio general** | **89–93** | **5 pp. (límite 5–7: cumple)** |
| Apéndice B — Anexo técnico | 94–99 | 6 pp. (5 figuras + 2 tablas) |
| Referencias, bases, fuentes normativas | 100–102 | 3 pp. |

## 8. Lista de verificación H.3

- [x] Cero errores de compilación, cero referencias indefinidas, cero citas indefinidas (3 pasadas de `pdflatex`)
- [x] `grep "VERIFICAR"` → 0
- [x] `grep "^%"` → sólo separadores estructurales (cabecera, PORTADA, BIBLIOGRAFÍA)
- [x] Encabezado, portada, `pdftitle`, fecha (22 de octubre de 2026): todo dice P4
- [x] Índice: ocho secciones y dos apéndices (más Referencias, Bases de datos, Fuentes normativas)
- [x] Toda referencia «Sección X.Y» resuelta vía `\ref` (grep → 0)
- [x] Ningún número en §6 sin supuesto explícito en texto visible (ecuaciones 1–3 y notas de tablas 15–19)
- [x] Figuras, `tab_modelos.tex`, `tab_frecuencia_modelos.tex` y `base_analisis_P4.csv` regenerados en el mismo pase
- [x] Ninguna tabla del BID reproducida (sólo la identidad τᵖ = κ·Nᴿ/Nᵂ y resultados descritos en prosa)
- [x] Ninguna cita textual de Fietz et al. (tres paráfrasis con `\citep{wb2025}`)
- [x] Las tres ⚠ DESVIACIÓN señaladas (§2 de este reporte)

## 9. Git

Rama `p4-version-final`, creada desde `dfd-demographics-fv-cornerstone` (la rama de trabajo actual; `main` está desactualizada). **Se versionó únicamente `Missions/Funded/CAF_DEM/caf-dem-entregable-final/`**, no `git add -A` como decía H.4: el árbol de trabajo tenía cambios ajenos a esta misión (READMEs borrados en KC_FHSLatam y _crossrefs, y ~30 archivos sin rastrear de BID2, Aurora, RF) que no debían entrar en este commit. El WEO completo (20 MB) y los auxiliares de LaTeX están en `.gitignore`; se conserva el subconjunto de seis países.

**No fusionado a `main`.** Pendiente de revisión de Héctor y de Juan Pablo.

## 10. Archivos de la entrega

```
caf-dem-entregable-final/
├── main.tex · main.pdf                    documento P4 (102 pp.)
├── graficas/  (16 png)                    4 figuras de proyección regeneradas + 5 de quiebres
├── tablas/    (14 tex + 3 csv)            tab_modelos/tab_frecuencia regeneradas; 6 tablas nuevas; diagnósticos B
├── base_analisis_P4.csv (+diccionario)    base consolidada P4 (2 038 filas)
├── base_analisis_P3.csv (+diccionario)    intactas, provenance
├── pipeline_P4.R · pipeline_P4.log        Bloque B reproducible (lee base P3, escribe todo lo demás)
├── pipeline_P3_extraido.R                 código R extraído del HTML tejido
├── calc_seccion6.py · seccion6_*.csv      §6.2 y §6.3 reproducibles
├── weo/weo_apr2025_6paises_subset.tsv     insumo WEO (subconjunto); series_nuevas_P4.csv
├── CAF_DEM_P4_instrucciones.md            instrucciones (Beth y Cath)
└── CAF_DEM_P4_reporte_final.md            este reporte
```
