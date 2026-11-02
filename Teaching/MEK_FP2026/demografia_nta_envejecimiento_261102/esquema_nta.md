# Esquema — «Cuentas Nacionales de Transferencia y envejecimiento»

Fase 1 · 1 de noviembre de 2026 · **para aprobación** · sesión del 2 y 3 de noviembre

Fuentes leídas completas:
- **Manual:** Naciones Unidas (2013), *National Transfer Accounts Manual*, cap. 1 (pp. 1–23) y cap. 2 (pp. 25–54), más p. 56 del cap. 3. Títulos y páginas confirmados en el PDF. Cotejé términos en la edición en español (Naciones Unidas, 2022).
- **Informe:** Cecchini, Comelatto, Holz, Kang y Paes (2025), *Impactos económicos del envejecimiento en América Latina y el Caribe: desafíos y oportunidades*, Serie Población y Desarrollo 140 (LC/TS.2025/50), CEPAL, 76 pp. Es un documento de serie firmado por sus autores, no un informe institucional: se cita así.
- **Dalila:** los archivos que se indican en cada diapositiva.

Los tres PDF quedaron en `fuentes/` (no estaban en Dalila). CEPAL bloquea la descarga directa; los dos documentos de CEPAL vienen de copias del Internet Archive.

Marcas:
- **[opcional · N min]**: lleva el distintivo gris en la esquina.
- **[NUEVA]**: no estaba en el esquema provisional; la pide la fuente.
- **[FUERA]**: el dato no está en la fuente principal de esa parte; se dice de dónde sale.
- **[PROPIA]**: amarre o gráfica nuestra.
- **✓**: cifra ya verificada contra la fuente en esta fase. Las demás se verifican en la fase 2; la que no se pueda verificar se quita de la diapositiva y va al reporte.

---

## Cinco decisiones que necesito de ti

Cada una trae mi recomendación. Si apruebas sin comentarios, aplico la recomendación.

### 1. El informe de CEPAL no sostiene el bloque central de la Parte 3

Le pediste al bloque de pensiones, salud y cuidados que fuera el centro, con CEPAL como fuente única. El informe no trae casi nada de eso:

| Lo que pide el esquema provisional | Lo que trae el informe |
|---|---|
| Gasto por edad en pensiones, salud y cuidados | Nada. Sus perfiles son consumo, ingreso laboral y déficit, sin desglose por función |
| Cobertura y suficiencia de pensiones | Sí: pp. 17–19 |
| Peso de las pensiones no contributivas | Nada |
| Perfil de gasto en salud, gasto de bolsillo, protección financiera | Nada. Solo salud en el gasto de los hogares (pp. 26–27) y un párrafo sectorial (p. 49) |
| Fragmentación del financiamiento de la salud | Nada |
| Cuidados | Tres párrafos (pp. 10, 49 y 68) y la ley coreana (pp. 54–55) |
| Cuentas de transferencias de tiempo (NTTA) | Nada |
| «Presión fiscal combinada bajo los escenarios del informe» | **El informe no tiene escenarios fiscales.** Su único ejercicio es el PIB per cápita (pp. 46–47) |

**Recomendación:** conservar el bloque, porque es lo que quieres enseñar, y romper la regla de fuente única solo ahí. Cada diapositiva dice en pantalla qué viene del informe y qué no. Las diapositivas 11, 13, 15 y 16 de la Parte 3 quedan como [FUERA] con fuente propia. La 16 se reescribe sin escenarios: el informe no los tiene y no los voy a inventar.

### 2. No encuentro la presentación para la CISS

Busqué en Dalila, Descargas y Documentos. No existe ningún archivo con «CISS» salvo una coincidencia en un PDF ajeno, y la frase «el cero se habla con el uno, el dos con el tres» no aparece en ningún lado. Sí encontré:
- la trampa de la formalización y el efecto escalón, en la presentación para la CEPAL (láminas 3–4) y en el deck de Boston (`boston_20260828_v2.tex`, láminas 13–14, con la fuente Fietz et al., 2025);
- la lectura por pilares, en `Missions/Funded/CAF_DEM/caf-dem-entregable-final/main.tex` (cinco bloques, con el Pilar 1-B).

**Recomendación:** pásame el PDF esta noche si lo tienes. Si no, la diapositiva 16 de la Parte 1 se arma con lo anterior y la frase queda como tuya, sin atribuirla a la CISS.

### 3. Fecundidad de México: 1.89 o 1.23

El encargo pide tomar las cifras observadas de CELADE u ONU. Para México eso da un número que nuestra propia investigación rechaza:

| TGF 2024 | CELADE/ONU (revisión 2024) ✓ | Fuente nacional |
|---|---|---|
| México | 1.89 | **1.23**: INEGI, Encuesta Intercensal 2025 (`releases/2026-09-22_inegi-eic2025_tgf-trigger-fired.md`, `endorsed_by: Anne`) |
| Chile | 1.14 | 1.03, provisional: INE Chile |
| Costa Rica | 1.32 | 1.12: INEC |
| Colombia | 1.63 | 1.1, preliminar: DANE |

Las tres últimas están fijadas en `scenario_anchors.md` (`endorsed_by: Anne`). `_baseline.md` no existe en el árbol, así que no hay nada que usar por error. El valor de 1.55 de `seminario-cepal-2026.md` no se usa.

**Recomendación:** la diapositiva 11 de la Parte 1 muestra esta tabla completa. Justo ahí está el argumento: la brecha entre lo que proyecta CELADE/ONU y lo que miden los países. En el resto de las diapositivas regionales uso CELADE/ONU con año y fuente, y México siempre lleva las dos cifras.

### 4. La pirámide de 2050: ONU, CONAPO o nuestra proyección

El encargo dice «ONU o CONAPO». El 24 de octubre me dijiste que WPP no sirve como insumo y que CONAPO no se usa para México.

**Recomendación:** 1970 con WPP 2024, porque no hay otra serie digital en Dalila; 2020 con el Censo (`inegi_cpv2020_single_age_prorated.csv`); 2050 con nuestro motor nacional (`projection_national.py`, TGF 1.23, 129.4 M y 22.6 % de 65+ ✓), rotulada «escenario», y el total de WPP (148.9 M ✓) como referencia en gris al pie. Salvedad: ese motor es un producto de comunicación, sin `endorsed_by`, y hay que volver a correrlo para sacar la distribución por edad.

Para la diapositiva 11 hay otra cifra de 2050, la de la Nota EIC 2025 v1.0 (Anne y Cath; pendiente de tu firma): Optimista 144.2, Central 135.5, INEGI directo 128.7, Estrés 121.2 M (corregido en la fase 2 contra el PDF v1.0). Uso esas cuatro como abanico de escenarios y aviso en la nota del presentador que la Nota sigue sin firma.

### 5. Cuánto mostrar de la Misión NTA

`Missions/Funded/NTA_Inequality/` tiene resultados reales, no agenda, y es lo más valioso de la sesión: México no está entre los seis países de CEPAL. Pero el documento es un borrador de agosto y en la carpeta no están los datos ni las figuras (`paper.ipynb` no está), así que puedo citar cifras pero no dibujar los perfiles.

**Recomendación:** usar las cifras del resumen como trabajo en curso, rotuladas así. Si quieres los perfiles de México dibujados, dime dónde está la base. Si no aparece, la diapositiva de comparaciones de la Parte 2 usa los perfiles de ntaccounts.org.

---

## Decisiones que ya tomé

- **Términos.** El encargo pide usar el español de CEPAL cuando exista, y ahí choca con dos términos propios. Uso **bono demográfico** (primer y segundo bono), como el informe; el Manual en español dice «dividendo». Uso **razón de sostenimiento**, como el informe (el Manual en español dice «razón de sustento económico»; tu encargo, «razón de sostén económico»). *Support ratio* en inglés una sola vez. Nota al pie en la primera aparición.
- **Plantilla.** `kaplow_marco_unitario.tex`. La opción `es-noaccentedoperators` no existe en esta versión de babel; se queda `\unaccentedoperators`, como en Kaplow.
- **Tiempo.** Las tres partes suman 180 minutos, con 10 opcionales cada una. Quedan 22 diapositivas en las Partes 2 y 3, no 20, porque el Manual y el informe piden material que no estaba. Las adicionales son opcionales o breves.

## Correcciones al esquema provisional

**Parte 1**
1. **El motor son cuatro módulos más una capa, y no son los que dice el encargo.** La fuente lista: demográfico, financiamiento de la salud, seguridad social y pensiones, y núcleo OLG/DSGE. La capa de agentes es aparte y complementa al núcleo. Salud y seguridad social son dos módulos, no uno.
2. **«Horizonte de 100 años» es incorrecto.** Los hogares entran a los 20 años y pueden vivir hasta los 100. El periodo dura cinco años.
3. **«Historia contributiva» no la pude confirmar** en `DFD_rag.md` ni en la revisión. El estado del trabajador es $s^w=(a,m,f,\eta,q)$, sin definir ahí. Lo reviso en `Integrated_6.tex` en la fase 2; si no aparece, se quita.
4. **No existe un documento con «las preguntas de ITED» fiscales.** `Tec_Seis_Preguntas_Demografía.docx` trata de la demanda universitaria. La diapositiva 10 es redacción mía a partir de la agenda DFD: revísala con cuidado.
5. **América Latina no es la región más rápida.** Pasa de 10 % a 20 % de 65+ en 28 años, contra 55 de Europa. Pero Japón lo hizo en 21 y Corea en 17. La frase es «más rápido que Europa», no «más rápido que nadie».

**Parte 2**
6. **El segundo bono tiene dos canales en el Manual:** capital humano (p. 12) y ahorro y capital (pp. 13–15). El provisional solo daba el segundo.
7. **Las aplicaciones fiscales merecen más que una viñeta.** Son la parte del cap. 1 más útil para este curso: flechas de Lee (pp. 17–18) y razón de sostenimiento fiscal (pp. 18–19).
8. **Las NTA no explican: contabilizan.** El Manual insiste en que no hay causalidad y en que los perfiles son de corte transversal (pp. 6 y 34). Va en pantalla.
9. **Los capítulos 1 y 2 no traen tablas por país con perfiles normalizados.** Solo Estados Unidos 2003 (tablas) y Filipinas (gráficas). Las tablas de Estados Unidos dan las cifras exactas de la mitad de la parte.

**Parte 3**
10. Ver la decisión 1. Además, el informe trae un capítulo entero sobre Corea que el provisional no veía; va como opcional.
11. **México casi no está en el informe y no está en los seis países con NTA.** La diapositiva 19 lo dice de frente.

## Erratas en las fuentes (no las repito en pantalla)

| Fuente | Dice | Debe decir o cómo lo trato |
|---|---|---|
| Manual, p. 11 | El retiro tardío «reduce» la razón de sostenimiento | La aumenta: más trabajadores por consumidor. Lo explico sin citar la frase |
| Informe, p. 33 | Mínimo de 29 años de bono en Martinica | Su gráfico 18 da Guadalupe 29 y Martinica 33. No lo uso |
| Informe, p. 40 | Chile: diferencia de 15 puntos entre etapas 1 y 3 | Su cuadro 1 da 31 − 14 = 17. Uso el cuadro |
| Informe, p. 36, n. 6 | Perú aparece en los dos grupos | Probable confusión con Paraguay. No lo uso |
| Informe, p. 48 | «6 países» | Lista siete. No lo uso |
| Nota de prensa de CEPAL | 68 M y 10.2 % de 65+ en 2024 | El informe dice 65 M y 9.9 % (pp. 9–10). Uso el informe |

---

# Parte 1 · La transición demográfica y nuestra investigación

60 min · 20 diapositivas · opcionales: 6, 13 y 18 (10 min) · preguntas a la clase: 5 y 11

## I. El modelo de transición demográfica · 25 min

1. **Portada.** «Parte 1: la transición demográfica». Noviembre de 2026.
2. **Las finanzas públicas cobran a unas edades y gastan en otras.** Cuando cambia la estructura por edad, cambia todo el presupuesto. Enlace con Kaplow, un modelo sin edad. — Fuente: Manual, pp. 1–2; [PROPIA].
3. **Cuatro fases, dos curvas.** Gráfica esquemática sin datos: natalidad, mortalidad y crecimiento natural como área. Mención de la segunda transición y de la fecundidad bajo el reemplazo. — Fuente: Lee (2003), *JEP* 17(4); Lesthaeghe y van de Kaa para la segunda transición; verificar ambas referencias.
4. **La mortalidad cae primero.** Salud pública y nutrición; se ensancha la base. Gráfica real de México: tasas brutas 1950–2023. — Fuente: WPP 2024, `WPP2024_Demographic_Indicators_Medium.csv.gz`.
5. **La fecundidad cae después, y aquí cayó de golpe.** Urbanización, educación de las mujeres, costo de los hijos (cantidad y calidad, Becker). México: 6.53 hijos en 1970, 2.71 en 2000 ✓. Pregunta (último overlay): ¿qué cambió en la casa de sus abuelas? — Fuente: Manual, p. 8; WPP 2024.
6. **[opcional · 3 min] Debajo del reemplazo.** Qué viene después de la cuarta fase. América Latina: 1.80 en 2024 ✓. — Fuente: WPP 2024; Manual, p. 1.
7. **Tres pirámides de México.** 1970, 2020 y 2050 (escenario). — Fuente: decisión 4.
8. **Envejecemos más rápido que Europa.** Años para pasar de 10 % a 20 % de 65+ ✓: Corea 17, Japón 21, Costa Rica 21, Brasil y Colombia 24, Chile 26, América Latina y México 28, España 49, Europa 55, Francia y Suecia más de 68 (ya tenían 10 % en 1950). «Envejecer antes de enriquecerse». Lo posterior a 2024 es escenario. — Fuente: cálculo propio con WPP 2024, `WPP2024_PopulationByAge5GroupSex_Medium.csv.gz`; Manual, p. 1.
9. **El bono demográfico y su fin.** Primer bono: más gente en edad de trabajar. Segundo bono: activos para la vejez. Para la región termina en 2028 ✓. Puente a la Parte 2. — Fuente: Informe, pp. 32–33 y 44; Mason y Lee (2006).

## II. Lo que hemos investigado · 30 min

10. **Nuestra pregunta.** Cómo reordena la transición las finanzas públicas en una economía de ingreso medio con mucha informalidad. — Fuente: `GrandPlan/DFD/DFD_rag.md` §2; `CLAUDE.md` raíz §5; ver corrección 4.
11. **Lo que proyectan y lo que medimos.** Tabla de TGF y abanico de escenarios a 2050, rotulados. Línea sobre el modelo de agentes: sin reflexividad reproduce el colapso de Costa Rica y Colombia; es reemplazo de cohortes, sin cascada. Pregunta: si el censo y la proyección no coinciden, ¿a cuál le creen? — Fuente: decisiones 3 y 4; `scenario_anchors.md`; `releases/2026-09-22_…`; `nota_EIC2025_v1.0.pdf`; `GrandPlan/DFD/research/fertility_collapse_abm/STAGE3a_Nina_signoff.md` (`endorsed_by: Nina`).
12. **El laboratorio DFD.** Diagrama propio: cuatro módulos, capa de agentes y LLM local como interfaz. Rótulo: «en construcción». — Fuente: `_ops/20260407_CROSS_CF_cross-tar-001-prep_v1.md` (preparatorio, sin `endorsed_by`).
13. **[opcional · 4 min] El núcleo: generaciones traslapadas.** Entrada a los 20, retiro exógeno, hasta los 100 años, periodos de cinco, dos tipos de habilidad, mercados incompletos. Sin álgebra. — Fuente: misma de la 12; `DFD_rag.md` §«Model class»; corrección 3.
14. **Automatización: ¿el rescate también aplica aquí?** Acemoglu et al. encuentran que menos nacimientos van con más crecimiento por trabajador, por tecnología que ahorra trabajo. Nuestra pregunta: ¿existe un umbral de ingreso e innovación debajo del cual eso no ocurre? Cautelas: no tiene resultados fiscales y su ventana es casi toda de bono. — Fuente: `_crossrefs/corpus/demographics/2026-07-11_baby-busts-growth-booms.md` (**`endorsed_by` vacío**: pendiente de Cath y Elle; va al reporte). La fecha de emisión está en disputa en la propia nota (24 de junio o 6 de julio); se cita solo el año.
15. **Una seguridad social para una población que envejece.** Dos ejes: instrumentos nuevos para financiar salud; transferencias consolidadas en un impuesto negativo. Y una condición: sin contener pensiones no hay espacio para salud. — Fuente: `CEPAL_NuevaSegSocial_Villarreal_Héctor-2.pdf`, láminas 5–9 (copia en `Comunidad_conocimiento_financiamientosalud_LATAM/Roche/boston_20260828/inputs/`).
16. **Pensiones: la trampa de la formalización.** Costo cierto de cotizar, beneficios inciertos y escalón. La arquitectura multipilar. — Fuente: decisión 2.
17. **Las cuentas de México.** Qué medimos y qué hallamos: las mujeres concentran 76.3 % del déficit; la niñez se financia en 88.6 % con recursos privados y la vejez en 54.5 % con transferencias públicas ✓. Puente a la Parte 2. — Fuente: `Missions/Funded/NTA_Inequality/paper_final.tex`, `resumen_ejecutivo.tex`; `NTA_paper.pdf` en Descargas; decisión 5. Nota: la misión no está en `Missions/_index.md`.
18. **[opcional · 3 min] Cómo trabajamos.** Corpus con procedencia citada y equipo de agentes; enlace con la persona de investigación de los alumnos. — Fuente: `_crossrefs/protocols/PROTO-RAG-001.md`; `_crossrefs/corpus/demographics/README.md`.

## III. Cierre · 5 min

19. **Tres ideas para llevarse.**
20. **Pregunta para la Parte 2.** «Si cada edad consume distinto de lo que produce, ¿quién paga la diferencia?»

---

# Parte 2 · La economía generacional — Manual NTA, caps. 1 y 2

60 min · 22 diapositivas · opcionales: 8, 18 y 20 (10 min) · preguntas a la clase: 5, 9 y 14

## I. La economía generacional · 22 min — cap. 1

1. **Portada.** «Parte 2: la economía generacional».
2. **Consumimos toda la vida y producimos solo una parte.** Perfiles estilizados, gráfica propia. Filipinas 1999 y Alemania 2003: déficit hasta los 27; desde los 60 y los 58 ✓. — Fuente: Manual, pp. 1 y 3–4, fig. 1.1.
3. **Qué es la economía generacional.** Producir, consumir, compartir y ahorrar por edad. Las cuentas nacionales no ven la edad. Cinco razones para medirla. — Fuente: Manual, pp. 1–3.
4. **Tres formas de cubrir el déficit.** Transferencias públicas, transferencias privadas y activos. Cuadro de sector por mecanismo: la colegiatura, la pensión del abuelo, la casa propia, la deuda pública. — Fuente: Manual, pp. 3–5, cuadro 1.1.
5. **Cada país paga distinto.** Filipinas casi solo activos; Japón, Costa Rica, Alemania y Chile, dos tercios públicos; Austria, Hungría y Suecia, casi solo públicos ✓. En México, con datos viejos, dos tercios o más vienen de activos y los mayores dan más a la familia de lo que reciben ✓. Contraste [PROPIA]: nuestra cuenta 2016–2024 da 54.5 % público para 60+. Pregunta: ¿qué creen que cambió, México o la medición? — Fuente: Manual, pp. 15–16, fig. 1.6; decisión 5.
6. **La razón de sostenimiento.** $L/N$: productores efectivos entre consumidores efectivos, ponderados con perfiles. Por qué es mejor que contar personas de 15 a 64. — Fuente: Manual, pp. 10–11, ec. 1.1.
7. **Los dos bonos.** $gr[C/N]=gr[(1-s)Y/L]+gr[L/N]$, con overlays. Primero: crece $L/N$; China sumó 0.7 % al año entre 1972 y 2014 ✓. Segundo: capital humano o capital. Conecta con la Parte 1. — Fuente: Manual, pp. 10–14, ecs. 1.1–1.2.
8. **[opcional · 4 min] [NUEVA] Las flechas de Lee.** Brasil 2002, redibujada con datos: educación baja de 37.6 a 16.0 años; pensiones sube de 38.0 a 62.5 ✓. El área es riqueza de transferencias y alguien futuro la paga. — Fuente: Manual, pp. 17–18, fig. 1.8.
9. **[NUEVA] La razón de sostenimiento fiscal.** Contribuyentes efectivos entre beneficiarios efectivos. Brasil 2010–2050: bajar beneficios 30 % o subir impuestos otro tanto ✓. La deuda no resuelve: solo agrega intereses. Pregunta: ¿qué haría el Congreso? — Fuente: Manual, pp. 18–19, fig. 1.9.

## II. El panorama de las cuentas · 33 min — cap. 2

10. **Qué miden las NTA, y qué no.** Flujos por edad vistos desde la persona; empresas y gobierno son intermediarios. Cuatro diferencias con el SCN: quién es la unidad, ingreso mixto repartido entre trabajo y capital, precios antes de impuestos a los productos, flujos dentro del hogar. Es contabilidad de corte transversal: no da causas. — Fuente: Manual, pp. 6, 25–29 y 34.
11. **La identidad de flujos.** De la ec. 2.1 a $C(x)-Y^l(x)=[\tau^+(x)-\tau^-(x)]+[Y^A(x)-S(x)]$. Derivación corta con overlays. — Fuente: Manual, p. 29, ecs. 2.1–2.2.
12. **El ciclo de vida económico.** Consumo público y privado (educación, salud, resto); ingreso laboral (salarios y autoempleo, dos tercios del ingreso mixto). Estados Unidos 2003 por tres grupos de edad ✓. — Fuente: Manual, pp. 35 y 39, cuadro 2.4.
13. **El déficit del ciclo de vida.** Por persona: +20,526; −9,164; +38,045 dólares ✓. Agregado: la población cambia el orden de magnitud. La suma no da cero: el ingreso laboral no alcanza. — Fuente: Manual, pp. 33 y 38, cuadros 2.2–2.3.
14. **Reasignaciones públicas.** Quién paga y quién recibe. En 65+ entran 25,273 dólares por persona: salud y pensiones son 80 % ✓. Los mayores también pagan: 9,830 ✓. Base del bloque central de la Parte 3. Pregunta: ¿quién paga el IVA de la medicina del abuelo? — Fuente: Manual, pp. 16–17 y 40, cuadro 2.6, fig. 1.7.
15. **Reasignaciones privadas.** Dentro del hogar y entre hogares. Los padres sostienen a los hijos: +11,088 netos dentro del hogar para 0–24 ✓. Lo que supone el Manual: reglas de reparto y jefe del hogar. — Fuente: Manual, pp. 27–28 y 41, cuadro 2.8.
16. **Reasignaciones basadas en activos.** Ingreso de activos menos ahorro. En 65+: 23,749 de ingreso y −1,396 de ahorro dan 25,146 ✓. Los intereses de la deuda pública son transferencia que pagan los contribuyentes. — Fuente: Manual, pp. 5, 31 y 41, cuadros 2.6 y 2.8.
17. **Población × perfiles = agregados.** La restricción: las transferencias deben cuadrar, y si cambia la estructura por edad, los perfiles se ajustan. — Fuente: Manual, pp. 3, 30 y 50–51.
18. **[opcional · 3 min] Comparaciones entre países.** Perfiles normalizados por el ingreso laboral de 30–49 años. El cap. 2 no los trae. — Fuente: [FUERA] ntaccounts.org, o la base de la Misión NTA según la decisión 5.
19. **[NUEVA] Lo que las NTA no ven.** No separan por sexo, no miden el trabajo del hogar ni el tiempo, y dan promedios por edad. Enlace con el hallazgo de México y con las NTTA. — Fuente: Manual, pp. 52–53.
20. **[opcional · 3 min] Qué datos se necesitan.** Población, cuentas nacionales y flujos por edad. Controles macro: si la encuesta da 100 y el SCN 110, multiplicas por 1.1 ✓. En México la encuesta capta entre 10 % y 53 % del agregado ✓. — Fuente: Manual, pp. 28 y 56; `paper_final.tex`. Nombres de ENIGH, SCN y Cuenta Pública por verificar.

## III. Cierre · 5 min

21. **El presupuesto es un sistema de reasignaciones por edad.** Enlace con Kaplow y con la sesión del 10 de noviembre.
22. **Pregunta para la Parte 3.** «¿Qué le pasa a ese sistema cuando la población envejece rápido?»

---

# Parte 3 · América Latina envejece — Cecchini et al. (CEPAL, 2025)

60 min · 22 diapositivas · opcionales: 10, 18 y 20 (10 min) · preguntas a la clase: 16 y 21

## I. Lo que dice el informe · 18 min

1. **Portada.** «Parte 3: América Latina envejece».
2. **El informe en una diapositiva.** La región no aprovechó el primer bono; se acaba con menos margen fiscal; hay retos y hay mercados nuevos. — Fuente: Informe, pp. 7 y 67.
3. **El ritmo.** 65+: 9.9 % en 2024, 18.9 % en 2050 ✓. Se duplica en 28 años. Los de 80+ pasan de 1.9 % a 5.1 % ✓. Cuatro desventajas frente a Europa. — Fuente: Informe, pp. 9–11, gráficos 1–2.
4. **El bono se acaba en 2028.** Duración por país; México 59 años ✓. Asia oriental creció 6.1 % al año y América Latina 0.9 % ✓. — Fuente: Informe, pp. 32–34, gráficos 17–18.
5. **La razón de sostenimiento ya llegó a su máximo.** Chile 2023, Brasil 2025, Costa Rica 2026, Perú 2036, Argentina 2038, Paraguay 2055 ✓. — Fuente: Informe, pp. 35–36, gráfico 19.
6. **El déficit se muda a la vejez.** Cuadro 1 de seis países y gráfica propia de edades medias: en 2014 los recursos fluyen hacia los jóvenes; en 2100, en cinco de seis, hacia los mayores ✓. — Fuente: Informe, pp. 39–45, cuadro 1, gráfico 25.
7. **Crecimiento: pierden los que van adelante.** Efecto anual sobre el PIB per cápita 2025–2050: Brasil −0.24, Chile −0.11, México +0.24, Guatemala +0.73 ✓. Es un ejercicio mecánico, con productividad constante. — Fuente: Informe, pp. 46–47, gráfico 26 (redibujado con sus etiquetas).

## II. Bloque central: pensiones, salud y cuidados · 25 min

8. **Tres presiones que crecen al mismo tiempo.** El perfil público de la Parte 2 por una población que envejece. Gráfica con el perfil de la Parte 2. — Fuente: Informe, pp. 10 y 67; [FUERA] Manual, cuadro 2.6 y fig. 1.7.
9. **Pensiones: muchos cobran, pocos alcanzan.** Cobertura 75.5 % en 2022, pero 43 % no recibe pensión o recibe menos que una línea de pobreza; más de 83 % en el quintil más bajo ✓. A pensión más insuficiente, más mayores trabajando. — Fuente: Informe, pp. 17–19, gráficos 4 y 6. Las no contributivas: [FUERA], fuente por definir.
10. **[opcional · 3 min] [NUEVA] Los niños son más pobres que los abuelos.** Pobreza: 41.4 % de 0–14 años, 14.7 % de 65+ ✓. Por qué, y qué le dice eso al presupuesto. — Fuente: Informe, p. 16, gráfico 3.
11. **Pensiones en México.** [FUERA] Reforma de 2020: cuota patronal escalonada 2023–2030 ✓ (sesión del 26 de septiembre). Pensión para adultos mayores y Fondo de Pensiones para el Bienestar: verificar en DOF. Enlace con la trampa de la formalización. — Fuente: Ley del Seguro Social, art. 168 (DOF 16-12-2020); `clase03_incidencia.tex`; `FISCUS/económicos_paquetes/documento_2027/capitulos/07_pensiones.tex`; DOF.
12. **Salud: el gasto sube con la edad.** Crónicas y demanda especializada. Hogares de solo mayores: salud 8.9 % del gasto, su tercer rubro ✓. Perfil de gasto y gasto de bolsillo: [FUERA]. — Fuente: Informe, pp. 27 y 49; Manual, cuadro 2.6.
13. **Financiamiento de la salud.** [FUERA] Fragmentación y nómina. Enlace con el eje de salud de la Parte 1. México: 2.6 % del PIB de gasto público, por verificar. — Fuente: `CEPAL_NuevaSegSocial`, láminas 2 y 5–6; `boston_20260828_v2.tex`; GHED/OMS.
14. **Cuidados: la demanda que nadie presupuesta.** «Envejecimiento del envejecimiento»: de 12 a 37 millones de personas de 80+ ✓. El cuidado recae en mujeres. — Fuente: Informe, pp. 10, 49 y 68.
15. **El tiempo también se transfiere.** [FUERA] Las NTTA miden el cuidado no remunerado por edad y sexo. Manual confirmado: UN DESA (2024), *National Time Transfer Accounts Manual* ✓. Para México, posible cifra de la Cuenta Satélite del Trabajo No Remunerado de INEGI, por verificar. — Fuente: Manual NTA, pp. 52–53; UN DESA (2024).
16. **Cómo se paga todo junto.** [FUERA] Sin escenarios del informe. Tres piezas: el déficit se muda a la vejez (diapositiva 6), Brasil −30 % (Parte 2) y la doble prueba: sostenibilidad e incentivos a formalizarse. Enlace con el 10 de noviembre. Pregunta (último overlay): «Si solo pudieran reformar uno de los tres, ¿cuál y por qué?» — Fuente: Informe, pp. 42–45; Manual, pp. 18–19; `CEPAL_NuevaSegSocial`, láminas 9–10.

## III. Recomendaciones, México y cierre · 17 min

17. **Lo que recomienda el informe.** Empleo digno para personas mayores, protección social, salud preventiva, envejecimiento saludable, inversión en todo el ciclo de vida. Presentado como del informe. — Fuente: Informe, pp. 67–68.
18. **[opcional · 4 min] [NUEVA] Corea: leyes, seguro y un tropiezo.** Seguro de cuidados de largo plazo (2007), ley de industrias (2006). Pero en 2024 se recortó por completo el presupuesto de promoción y quedaba una sola persona a cargo ✓. — Fuente: Informe, pp. 54–58, cuadro 3.
19. **México en el informe.** Lo que trae: 59 años de bono, +0.24, su punto en el gráfico 6. Lo que no: no está entre los seis países con NTA. Nuestra Misión NTA cubre ese hueco. — Fuente: Informe, pp. 19, 34, 37 y 47; decisión 5.
20. **[opcional · 3 min] Economía plateada.** Salud, cuidados, finanzas, farmacéutica, turismo, vivienda. La región debe dimensionarlo aparte por informalidad y baja cobertura. — Fuente: Informe, pp. 11–13 y 49–51.
21. **Lectura crítica.** Qué deja abierto: sin escenarios fiscales, sin México en las NTA, usa la revisión 2024 de CELADE/ONU (TGF de 1.89 para México), y sus oportunidades dependen de capacidad de gasto. Conexión con la Parte 1. Pregunta (último overlay) para discutir. — Fuente: Informe; Parte 1.
22. **Cierre de la sesión.** Ideas de las tres partes y puente al 10 de noviembre: deuda, sostenibilidad y tasa de interés frente a crecimiento. — Fuente: [PROPIA].

---

## Referencias que se verifican en la fase 2

- Lee (2003), *JEP* 17(4), y Lesthaeghe y van de Kaa, sobre transición y segunda transición.
- Mason y Lee (2006), como la cita el informe.
- Observatorio Demográfico 2025: el valor por país. WPP 2024 es la misma revisión, pero falta cotejar el documento.
- Presidencia y DOF: Pensión para el Bienestar de las Personas Adultas Mayores (art. 4.º constitucional) y Fondo de Pensiones para el Bienestar.
- Gasto público y de bolsillo en salud de México (GHED/OMS).

</content>
