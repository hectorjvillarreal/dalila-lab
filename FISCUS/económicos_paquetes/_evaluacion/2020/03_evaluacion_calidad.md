# Evaluación de calidad — Implicaciones del Paquete Económico 2020 (CIEP)

**Corrida:** evaluación CIEP 2020 · FISCUS · Dalila · 2026-09-05
**Regla:** hallazgos con cita; sin calificación global. Referencias a CIEP por página impresa (romanos para el frente; arábigos para capítulos). Referencias oficiales como en `00_inventario_paquete.md`. Ids `Vnnn` remiten a `02_verificacion_cifras.csv`.

## 1. Cobertura

**Lo que CIEP trata del inventario oficial.** Ingresos totales y por concepto (cap. 1), ingresos del sector energético (cap. 2), gasto neto y sus tres clasificaciones (cap. 3), siete rubros de gasto (caps. 4–10), RFSP y SHRFSP (cap. 11). Los agregados de gasto de la EM se reproducen con exactitud (V093–V099).

**Omisiones materiales, con la cifra omitida y su fuente:**

- **Marco macroeconómico como objeto de análisis.** CGPE p. 69: PIB 2.0 % puntual (rango 1.5–2.5), 49 dpb, 1,951 mbd, Cetes 7.4 %, tipo de cambio 19.9. CIEP usa 2.0 % (p. 4, 11) y 49 dpb (p. 15) como datos, no como supuestos evaluables. No hay ninguna mención al comparativo de expectativas del CGPE p. 66 (mediana Banxico 1.4 %).
- **Cláusula de excepción de la LFPRH.** CGPE p. 70: meta de RFSP de 2.3 % + 0.3 % del PIB (78.8 mmp) de déficit adicional por el menor precio del petróleo. El cap. 11 atribuye el aumento de RFSP a FONADIN (p. 77) y a menores ingresos (p. 78); la explicación oficial no aparece (V179).
- **Pasivo pensionario.** CGPE cuadro p. 130: 10,153.6 mmp de 2018 = 43.2 % del PIB (IMSS-RJP 11.4; ISSSTE 23.7; CFE 2.1; Pemex 4.6). El cap. 7 no lo cita. Es la única cifra de largo plazo del paquete en la materia.
- **Trayectoria oficial 2021–2025 de pensiones.** CGPE p. 122/124 y EM p. 141: 3.8 → 4.5 % del PIB con +7.0 % real anual. CIEP la alude ("perspectivas de crecimiento constante hasta 2025", p. 54) sin reproducir ni una cifra.
- **Sensibilidades y amortiguadores.** CGPE p. 127–128: +1 dólar/barril = +13,775.8 mdp; +100 pb = +19,477.9 mdp de costo financiero; FEIP 296.3 mmp; coberturas al 100 %. Ausentes, pese a que p. V afirma que "los equilibrios de largo plazo dependan de… la expansión de la producción petrolera o la reducción de tasas".
- **Gastos fiscales.** ILIF p. XII: tasa cero de IVA 305,392 mdp (1.17 % del PIB); exentos ISR salarios 156,966; estímulos 130,584. CIEP p. 5 y 11 hablan de "patrones de consumo… tasa cero" y de "evaluar el efecto redistributivo de los estímulos" sin la cifra.
- **Techo de endeudamiento.** ILIF art. 2o.: 532 mil mdp interno y 5,300 mdd externo; CFE 9,835 mdp y 508 mdd. No aparece en el cap. 11.
- **Meta de balance de Pemex y su ajuste.** DEC art. 5: −62,623.5 mdp; ILIF p. XXXIII: 30,771.5 mdp del déficit se atribuyen a la caída de 55 a 49 dpb. Ausente en caps. 2 y 8.
- **Anexo transversal "Programas para superar la pobreza".** EM p. 215: 470,626 mdp. CIEP cuadro 3.2 lo declara sin información y "se asume que desapareció", lo que produce un total de anexos −13.6 % en lugar de +4.2 % (V102).
- **Ramo 19 por programa.** Analítico: pensiones en curso IMSS 344,161.7; déficit de nómina ISSSTE 244,211.1; LFC 22,130.5; civiles y militares 27,244.3. CIEP neta el ramo a 137,614 (V105) sin desglosar lo que resta.
- **Límite de gasto corriente estructural.** CGPE p. 74: 2,405.7 mmp propuesto vs límite 2,633.6. Ausente.

**Cobertura sin contraparte oficial en la carpeta (aporte de CIEP):** costeo de atención universal en salud (cuadros 4.4–4.5), cobertura de la pensión no contributiva vs CONAPO (7.3), distribución per cápita del gasto federalizado (10.2), series desde Cuenta Pública 2013–2018.

## 2. Contrafactual declarado

Conteo manual sobre las 187 filas del CSV: 104 afirmaciones son comparativas (variación, diferencia o tendencia). En 86 el contrafactual está explícito y es consistente ("respecto al PEF 2019", "pesos de 2020", "estimado de cierre 2019"). En 18 falta o está mal declarado (17 %):

| id | afirmación | problema |
|---|---|---|
| V004 | pensiones contributivas "aprox. 7 %" | sin base; la oficial es 6.2 % vs aprobado |
| V010 | participaciones caen "por primera vez en la última década" | serie no mostrada; cierto vs aprobado, plano vs estimado |
| V015, V048, V056 | "disminución del IVA respecto a 2019" | el texto dice cierre 2019 (p. 4, 11) pero los números solo cierran contra aprobado |
| V050 | Pemex "+0.1 pp vs cierre 2019" | oficial +0.3 |
| V051 | FMP "−0.2 pp vs lo esperado en 2018" | año equivocado; la cifra corresponde a 2019 estimado |
| V059–V063 | cuadro 2.1 "variación real respecto a 2019* (estimado de cierre)" | ninguna de las cuatro tasas coincide con CGPE p. 86 contra estimado ni contra LIF |
| V075 | "2016 26.7 %" | serie oficial 26.6 |
| V085 | participaciones y aportaciones "por primera vez desde 2013" | serie no en carpeta ni en el documento |
| V150 | pensiones "+35.5 % desde 2014" | no dice si aprobado o ejercido ni año base en pesos |
| V155 | "a partir de 2017… +211 %, +30 %, +17 %" | base 2017 sin declarar (aprobado/ejercido) |
| V178 | cuadro 11.1 columna "PEF 2019" | mezcla aprobado y estimado (FONADIN, banca de desarrollo) |
| V182 | costo de la deuda "de 3.1 % a 2.9 %" | ninguna pareja oficial |
| V184 | deuda per cápita "+3 % vs 2018" | base y deflactor sin declarar |

Práctica que sí es consistente: todas las tablas de gasto (cuadros 3.1–3.5, 4.1–4.2, 10.1) declaran "PEF 2019 / PPEF 2020, millones de pesos de 2020".

## 3. Cierre contable

- **Identidad ingreso = gasto.** Cuadro 1.1: total 6,096,335.8 = DEC art. 2 ✓. Ingresos 21.0 + deuda 2.2 = 23.2 = gasto 23.2 % del PIB (p. 3, p. 19) ✓.
- **Balance primario.** Figura 11.1: 21.0 − 20.3 = 0.7 ✓ (CGPE p. 185). Pero el texto de 11.2 usa costo de la deuda 2.9 %: 0.7 − 2.9 = −2.2, no el −2.1 que reporta (V181). Con el 2.8 oficial cierra.
- **RFSP.** Cuadro 11.1: −2.1 −0.1 −0.1 −0.1 +0.0 +0.1 −0.3 = −2.6 ✓ para 2020. La columna 2019 (−2.0 −0.1 −0.1 +0.0 +0.0 +0.0 −0.3 = −2.5) cierra solo porque dos filas están tomadas del estimado (V178).
- **Cuadro 1.1.** El residuo "Otros" 335,499.6 se obtiene con el ISR erróneo (1,846,445.7); con el oficial es 335,485.6 (V041–V043).
- **Programable 16.7 = 4.9 + 10.3 + 1.5.** Cierra por construcción: 1.5 es bruto (396.3 mmp), 10.3 no es reproducible y 4.9 es residuo (V079).
- **Cuadro 3.2.** Total 2020 2,276,681 omite 470,626 del anexo pobreza; el −13.6 % es artefacto (V102).
- **Cuadro 3.5.** Bruto 6,216,356 − 120,020 = 6,096,336 ✓; el "120,020" es aportaciones ISSSTE 50,019.9 + apoyos a EPE 70,000 (V108), no "cuotas al ISSSTE".
- **Pensiones.** 965,202 + 138,556 = 1,103,758 ✓; 4.2 % ✓; IVA 3.8 % ✓ (V035).
- **Salud, inversión, seguridad, educación.** Los perímetros suman exactamente lo que los analíticos dan (V019, V028, V036, V022).

## 4. Trato de los supuestos macro

- **Adopción sin comentario:** PIB 2.0 % (p. 4, 11), 49 dpb (p. 15), 1,951 mbd implícito ("producción petrolera sustancialmente mayor", p. II), Henry Hub 2.4 (p. 16), tasas ("reducción de tasas de interés internas", p. V). No se cita el rango 1.5–2.5 ni el comparativo de expectativas (CGPE p. 66).
- **Interrogación cualitativa:** p. V: "el que los equilibrios de largo plazo dependan de variables como la expansión de la producción petrolera o la reducción de tasas de interés internas, le transmiten riesgos al sistema". Es la única frase que cuestiona un supuesto.
- **Sensibilidad:** ninguna. El CGPE la ofrece (p. 127) y no se usa.
- **Un caso de contradicción del supuesto sin decirlo:** p. 4 y 11 sostienen que el IVA cae aun con crecimiento de 2 %; la cifra oficial contra cierre 2019 es +3.6 % real (V048). La crítica al supuesto de recaudación descansa en un contrafactual equivocado.

## 5. Separación descriptivo–normativo

Casos en que el juicio aparece en secciones descriptivas (POLÍTICA, EVOLUCIÓN, PROGRAMAS, cuadros):

| sección | cita | por qué es juicio |
|---|---|---|
| 1.2.1 (p. 4) | "Esto puede tener implicaciones en temas de administración fiscal o en patrones de consumo" | hipótesis explicativa dentro de la evolución de ingresos |
| p. II (Ingresos) | "una debilidad no explicada en la recaudación por IVA… La baja presión fiscal es una debilidad estructural" | valoración en el resumen descriptivo de ingresos |
| 2.1 (p. 14) | "sin estar necesariamente etiquetados a gasto de capital redituable en el largo plazo" | juicio sobre el destino del FMP en sección de renta petrolera |
| 2.1 (p. 15) | "la medida compromete la recaudación… así como el fortalecimiento de la reserva" | valoración en sección descriptiva |
| 4.3 (p. 33) | "aún no existe un plan de acción aprobado que considere variables de epidemiología y demografía… ni enfoque de sostenibilidad fiscal" | juicio en PROGRAMAS SELECCIONADOS |
| 7.2 (p. 55) | "presionando así las finanzas del IMSS y del gobierno federal" | consecuencia valorativa en EVOLUCIÓN |
| 8.2.2 (p. 60) | "dicha medida no es consistente con el presupuesto destinado" | juicio en sección descriptiva de CFE |
| 3.2.4 (p. 23) | encabezado lateral "RECORTES EN LOS RAMOS ADMINISTRATIVOS" con "como resultado del ajuste al programa Jóvenes Construyendo el Futuro" | atribución causal en clasificación administrativa |
| p. III–IV | "la estructura programática siguió una lógica esencialmente política"; "No necesariamente las cancelaciones o recortes tienen como sustento evaluaciones formales" | juicios en la sección de espacio fiscal, que precede a IMPLICACIONES |

Capítulos donde la separación se respeta: 5 (inversión), 9 (seguridad), 10 (federalizado): el juicio está confinado a "IMPLICACIONES".

## 6. Horizonte

**Lo que el paquete ofrece.** Proyección 2021–2025 (CGPE p. 112, 122, 124; EM p. 140–143): pensiones 3.8 → 4.5 % del PIB a 7.0 % real anual; costo financiero 2.6 %; inversión física 3.0 %; SHRFSP 44.7 % en 2025. Demografía: 9.8 → 19.5 millones en edad de pensionarse 2020–2040 (CGPE p. 128, Conapo). Pasivo pensionario 43.2 % del PIB (p. 130). Afirmación oficial de que las presiones "disminuyan gradualmente hasta desaparecer" en la próxima década (p. 129).

**Lo que CIEP hace con ello.**
- Pensiones (7.2, p. 54): cita "perspectivas de crecimiento constante hasta 2025 SHCP (2019)"; no reproduce la cifra 4.5 %, ni el supuesto de 7 %, ni la contradicción con p. 129 del CGPE. 7.4 concluye "una tendencia creciente por, al menos, una generación más" sin supuesto demográfico ni de crecimiento declarado; la única cifra demográfica es CONAPO 7.1 millones de 68+ para 2020 (p. 55).
- Salud (4.5, p. 36): "costos de salud que representa la transición epidemiológica" sin horizonte ni cifra; los escenarios de 4.5.1 son estáticos (2020).
- Deuda (11.4, p. 79–80): "mayores recursos en el futuro"; "transferencia de deuda pública a las generaciones futuras"; no usa la trayectoria 2021–2025 del SHRFSP (CGPE p. 120) ni el perfil de amortizaciones (ILIF p. XXIX: 756.8 mmp en 2020).
- Inversión (5.2): serie hacia atrás 2015–2020; nada hacia adelante (CGPE p. 124: 3.0 % del PIB promedio 2021–2025).
- Ingresos (1.2): serie 2013–2020; nada de la proyección 2021–2025 de la ILIF (p. IX: 21.3 → 21.7 % del PIB).

**Resultado.** El análisis se detiene en 2020 en todos los capítulos. Donde extiende el horizonte lo hace con lenguaje ("generación", "futuro") sin cifra ni supuesto. Para un trabajo cuyo eje son pensiones y salud, la ausencia del cuadro p. 122 y del pasivo p. 130 es la omisión de mayor peso de todo el documento.
