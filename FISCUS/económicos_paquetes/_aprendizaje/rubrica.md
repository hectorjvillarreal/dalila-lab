# Rúbrica — seis criterios y lo que la corrida 2020 enseñó sobre cómo aplicarlos

## 1. Cobertura
**Cómo aplicarlo.** Construir primero el inventario oficial (fase 1) con una lista cerrada de "cifras que un lector del paquete esperaría ver": marco macro, metas, 12 indicadores, cláusulas de excepción, gastos fiscales, techo de deuda, metas de EPE, mediano plazo, riesgos, pasivo pensionario, anexos transversales. Después marcar presencia/ausencia en el documento evaluado.
**Casos límite.** Un tema puede estar "cubierto" en un cuadro sin que el texto lo use (cuadro 11.1 de CIEP contiene el balance pero el texto no explica su cambio). Contar como cobertura parcial y decirlo.
**Lo que no funcionó.** El criterio no distingue omisiones por decisión editorial (SAR, sistema financiero) de omisiones por descuido (anexo pobreza). Registrar ambas, no atribuir motivo.

## 2. Contrafactual declarado
**Cómo aplicarlo.** Clasificar cada comparación en cuatro ejes: nominal/real; aprobado/estimado de cierre; año previo/PIB; y unidad del año base (pesos de t). Marcar "explícito" solo si los cuatro se deducen del texto o del cuadro. Reportar tasa y lista.
**Casos límite.** Los cuadros de CIEP declaran bien la base; el texto que los comenta a veces cambia de base sin avisar ("vs cierre 2019" en ingresos). Evaluar texto y cuadro por separado.
**Distinción que hubo que precisar.** "2019" puede ser: LIF/PEF aprobado, estimado de cierre en CGPE, PEF original o PEF resectorizado (Gobernación/SSPC, PGR/FGR). Las dos últimas producen −90 % vs −21 % en el mismo ramo.

## 3. Cierre contable
**Cómo aplicarlo.** Rehacer: ingresos + deuda = gasto; primario = balance + costo financiero; RFSP = balance + fuera de presupuesto; totales de cada cuadro contra sus filas; residuos ("Otros"). Verificar que los porcentajes del PIB del documento usen el mismo PIB.
**Casos límite.** Un cierre puede ser exacto y estar mal etiquetado (cuadro 3.5: "cuotas al ISSSTE" 120,020 = aportaciones ISSSTE + apoyos a EPE). Reportar como "reproducible, etiqueta incorrecta".
**Lo que no funcionó.** No hay forma de cerrar sumas cuyo perímetro no está declarado (16.7 = 4.9 + 10.3 + 1.5). Marcar como no reproducible en lugar de intentar adivinar el perímetro.

## 4. Trato de los supuestos macro
**Cómo aplicarlo.** Listar los supuestos del CGPE (PIB, precio y plataforma, tipo de cambio, tasas, inflación) y buscar para cada uno: cita, comparación con expectativas privadas, sensibilidad, consecuencia si falla.
**Casos límite.** Una frase genérica de riesgo (p. V de CIEP) cuenta como interrogación cualitativa; no cuenta como sensibilidad.
**Distinción que hubo que precisar.** "Adoptar el supuesto" y "contradecirlo sin decirlo" (IVA cae "aun con crecimiento de 2 %" cuando la cifra oficial contra cierre sube 3.6 % real) son cosas distintas; la segunda pertenece también al criterio 2.

## 5. Separación descriptivo–normativo
**Cómo aplicarlo.** Recorrer solo las secciones descriptivas (POLÍTICA, EVOLUCIÓN, PROGRAMAS, cuadros, encabezados laterales) y anotar cada frase con verbo de valor o atribución causal no sustentada. Citar textual.
**Casos límite.** Los encabezados laterales en versalitas son parte del texto descriptivo y a veces cargan el juicio ("RECORTES…", "MÁS SUBSIDIOS"). La sección "Implicaciones" del frente (pp. II–V) es normativa por diseño; no penalizar.
**Lo que no funcionó.** El criterio no dice qué hacer con hipótesis explicativas prudentes ("esto puede tener implicaciones…"). Se registraron como juicio; se podría abrir una subcategoría "hipótesis" en 2021.

## 6. Horizonte
**Cómo aplicarlo.** Para pensiones, salud y deuda: ¿hay una cifra posterior al año del paquete? ¿Se declara el supuesto demográfico y de crecimiento? ¿Se usa lo que el CGPE ya proyecta (2021–2025, pasivo, sensibilidades)?
**Casos límite.** "Una generación más", "generaciones futuras" son horizonte sin cifra: registrar como presente-sin-cuantificar.
**Lo que enseñó 2020.** El paquete oficial tiene más horizonte que el documento evaluado (7 % real anual; 3.8 → 4.5 % del PIB; 43.2 % de pasivo; 9.8 → 19.5 millones). El criterio debe medir también si el evaluado aprovecha ese material, no solo si lo genera.

## Reglas transversales que salieron de la corrida
- Clasificar (a)/(b)/(c) por afirmación, no por párrafo; muchos párrafos mezclan.
- Umbral de "aprox": diferencias ≤ 0.2 pp o ≤ 0.5 % atribuibles a deflactor o redondeo. Todo lo demás es "no".
- Nunca aproximar una base t−1 que no esté en carpeta: se marca `no_verificable` y se anota qué archivo haría falta (PEF t−1 analítico, Cuenta Pública).
- Los analíticos del PPEF resuelven casi todo el año t; no resuelven nada de t−1.

## Adenda 2021

**Reorden (instrucción 2021 §7):** 1 contrafactual, 2 perímetro, 3 cobertura, 4 cierre contable, 5 descriptivo–normativo, 6 horizonte. El criterio "trato de los supuestos macro" de 2020 se absorbe en 1 y 6.

**Convenciones fijadas (§1 de la instrucción 2021), ahora reglas de la rúbrica:** deflactor del PIB (INPC solo para prestaciones individuales, marcado en el lugar; nunca ambos en un cuadro); las cuatro declaraciones del contrafactual; ex ante contra ex ante; perímetro declarado antes del primer cuadro y constante; umbral 0.5 % niveles / 0.1 pp tasas y razones; lo atribuible a deflactor se reporta como categoría propia; prohibición de yuxtaposición sin mecanismo; balances nombrados (público, sin inversión, RFSP).

**Tipología `tipo_error` (nueva columna del CSV):** transcripcion, contrafactual, perimetro, omision, deflactor. Solo cuando `coincide = no`.

**Criterio 2, perímetro — casos límite de 2021:** (a) un perímetro declarado en nota al pie que cambia entre cuadros del mismo capítulo (Pemex por actividad institucional en el cuadro 7 y por programa en el cuadro 8 de CIEP) se registra como `perimetro` aunque cada cuadro sea internamente correcto; (b) incluir una transferencia a estados (FASSA) como "programa del instituto" (INSABI) es error de perímetro, no de aritmética; (c) las reclasificaciones oficiales entre subfunciones (Seguro Popular en "protección social en salud" → INSABI en "servicios a la persona") crean caídas contables que no son presupuestales; el evaluador debe anticiparlas antes de comparar por subfunción.

**Criterio 1, contrafactual — lo que 2021 enseñó:** cuando el evaluado aplica un deflactor ligeramente distinto (bases 2020 0.02–0.03 % por encima de 1.034), la diferencia es `deflactor`, no `aprox`, y no cuenta como error de base. La EM misma compara a veces contra proyecto anterior ("+27.7 % respecto al PPEF 2020", p. 61): el contrafactual mal declarado también ocurre en la fuente oficial y debe señalarse igual.

**Pendiente 9.2 (resuelto hasta donde la carpeta permite):** el programa Pensión para el Bienestar de las Personas Adultas Mayores vale 126,650.3 mdp en el PPEF 2020 (AN, PP 176; EM 126.7) y 129,350.3 en el PEF 2020 aprobado. El Anexo 14 del DEC 2020 atribuye 120,017.9: no coincide con ninguna partición por partida ni por tipo de gasto (el programa es 43101 subsidios 126,549.3 + honorarios 101.1; TG 1 124,370.9 + TG 7 gastos indirectos 2,279.5). Es una atribución transversal parcial; el monto del programa es el analítico. Costo por beneficiario (126,650.3 / 6,849,252 = 18,491 pesos) contra apoyo nominal 15,300: +20.9 %; descontando gastos indirectos TG 7 (2,279.5 mdp): 18,158 pesos, **+18.7 % sin explicar**. Pago de marcha, altas durante el ejercicio y dispersión no se pueden separar con la carpeta (harían falta reglas de operación y Cuenta Pública). La cifra queda congelada.

**Lo que no funcionó en 2021:** el conteo de "afirmaciones comparativas con contrafactual explícito" sigue siendo manual y sensible a cómo se agrupan las filas del CSV; conviene una columna booleana `contrafactual_explicito` en 2022.

## Adenda 2022

**Reorden para un capítulo de ingresos (instrucción 2022 §9):** 1 contrafactual, 2 perímetro, 3 supuestos macro, 4 cobertura, 5 cierre contable, 6 descriptivo–normativo y horizonte. Perímetro y contrafactual quedan al mismo rango.

**Columnas nuevas del CSV:** `tier_seccion` (restitucion / juicio / mixta, según la subsección del género: "Evolución… a 2022" y aperturas → restitución; "Implicaciones" → juicio; "Incidencia" → mixta) y `contrafactual_explicito` (si / no / na). El conteo del criterio 1 sale del CSV por primera vez.

**Criterio 1, contrafactual — lo que ingresos enseñó:** (a) en ingresos la trampa de base no es aprobado vs cierre sino **el denominador del % del PIB**: el CGPE presenta el aprobado 2021 con el PIB de aprobación (22.2 %) y con el PIB revisado (21.3 %), y la comparación con 2022 cambia de signo (−0.3 vs +0.6 pp) según cuál se use; una afirmación en % del PIB necesita una quinta declaración, *con qué PIB para cada año*, cuando el año base tiene PIB revisado. (b) Una elasticidad derivada de dos cifras en % del PIB del mismo año (aprobado vs estimado) no es una elasticidad: mide la revisión del PIB, no la respuesta de la recaudación. Se registra como `contrafactual` aunque cada cifra sea correcta.

**Criterio 2, perímetro — casos de ingresos:** (a) "ingresos totales" del art. 1o. incluye deuda; toda razón sobre "ingresos" declara si es presupuestarios o totales (en 2022 CIEP lo declaró; su cuadro 2.1 usa presupuestarios como denominador bajo un rótulo que dice "ILIF"); (b) "petroleros" tiene dos definiciones oficiales que difieren en 56.9 mdp (ILIF: Pemex + FMP; CGPE: + ISR de contratistas y asignatarios), indistinguibles al décimo pero distintas de nombre; (c) "no tributarios no petroleros" de CIEP excluye CFE y el CGPE la incluye en "organismos y empresas": perímetro propio declarado, no error; (d) los aprovechamientos son dos objetos (con nombre y "Otros") y solo el segundo es material.

**Criterio 3, supuestos macro (nuevo rango):** el CGPE 2022 sí trae sensibilidades (p. 58) de choques individuales; la evaluación pide tres cosas: si el evaluado las cita, si computa elasticidades implícitas contra la base correcta (cierre), y si señala que la meta descansa en "eficiencia" no cuantificada. En 2022 la elasticidad implícita es 1.56 contra cierre (1.15 sin IEPS de gasolinas) y el paquete no separa actividad, eficiencia y miscelánea.

**Criterio 4, cobertura — lista mínima para ingresos:** memoria de cálculo (método), renuncias recaudatorias (cinco cifras), art. 16 estímulos, art. 21 retención, art. 22 DUC, transitorios con ingresos, RFP, precio máximo de referencia (art. 31 LFPRH), sensibilidades, proyección 2023–2027 por rubro, reclasificación ILIF–CGPE, dos presentaciones del aprobado t−1, "Otros aprovechamientos" y su obligación de reporte.

**Criterio 5, cierre contable — identidades de ingresos:** total art. 1o. = gasto neto (DEC art. 2); presupuestarios + financiamientos = total; gasto pagado − presupuestarios = déficit; financiamientos − déficit = diferimiento de pagos; suma de numerales = total; bloques ILIF = bloques CGPE salvo la reclasificación declarada.

**Fuentes ex post (decisión §1.2):** se admiten solo para verificar; en 2022 no se descargaron y las filas que las requerían quedaron `no_verificable` con "fuente ex post" en la nota.

**Lo que no funcionó en 2022:** el 40 % de las filas de ingresos tiene `contrafactual_explicito = na` porque son niveles o participaciones; la columna sirve, pero el criterio 1 en ingresos se juega en pocas filas y hay que leerlas una por una. Y la ausencia de la EM y de la miscelánea dejó al capítulo propio sin dos de sus fuentes naturales: la rúbrica debe prever un "nivel de carpeta" declarado al inicio (qué piezas del paquete faltan) porque condiciona qué criterios pueden aplicarse.

## Adenda 2023

**Reorden para un capítulo de deuda (instrucción 2023 §8):** 1 **identidad de objeto** (nuevo, primer criterio del rubro), 2 contrafactual declarado con la quinta declaración y la distinción ex ante / ex post, 3 cierre contable y consistencia flujo–acervo, 4 trato de los supuestos macro (las cuatro variables), 5 cobertura, 6 descriptivo–normativo y horizonte.

**Criterio 1, identidad de objeto — cómo aplicarlo.** Antes de verificar una cifra, nombrar qué es: cuál de los tres flujos (presupuestario / público o económico / RFSPF), cuál de los tres acervos (SHRFSPF / deuda neta del sector público federal / deuda bruta del sector público no financiero), si es techo (autorización de endeudamiento neto), endeudamiento (partida informativa del art. 1o.) o déficit (DEC art. 2), qué perímetro institucional (Gobierno Federal ⊂ presupuestario ⊂ no financiero ⊂ federal; nunca entidades federativas), y en qué unidad (pesos corrientes vs de t; % del PIB de qué añada). Cada confusión se adjudica contra la nota metodológica de la SHCP (edición del año del paquete; p. 3, 12–13, 16, 25–26, 40), no contra criterio propio. **Sexto valor de `tipo_error`: `objeto`**, cuando la cifra es correcta y el nombre no. Casos de 2023: financiamientos (1,176,173.8) llamados déficit presupuestario (V058); participaciones del costo financiero llamadas composición de la deuda (V041); % del PPEF llamados % del PIB (V037); serie nominal rotulada "MXN 2023" (V052); "equilibrio presupuestario" por déficit constante de 2.2 % (V032). **También le ocurre a la fuente oficial:** "deuda externa neta" (CGPE 2022) vs "bruta" (CGPE 2023) con las mismas cifras; "déficit público" (CGPE 2023 Anexo I) vs "déficit presupuestario" (CGPE 2024) para la misma línea; tres nombres (público, económico, déficit público) para un flujo dentro del CGPE 2023. La nota metodológica lo autoriza (p. 3) y por eso la equivalencia hay que declararla una vez, no corregirla.

**Nomenclatura de la casa:** RFSPF = RFSP; SHRFSPF = SHRFSP. Un objeto, dos grafías; ambas se buscan al extraer.

**Criterio 2, contrafactual — la quinta declaración en deuda.** Con qué PIB y de qué añada, para cada año. En 2023 el CGPE trae dos SHRFSPF para 2020 (51.6 en p. 120; 52.4 en p. 122), el costo financiero aprobado 2022 vale 2.8 % con el PIB de aprobación y 2.7 con el revisado, y el CGPE 2024 reexpresa toda la serie con base 2018 (49.9 → 49.2 para 2021; 48.9e → 47.7 para 2022). Regla: una añada para toda la comparación, declarada al inicio; ex ante contra ex ante; la ex post solo para validar el marco, y con su propia añada declarada. Cuando la revisión cambia el signo, se presentan las dos.

**Criterio 3, cierre contable y flujo–acervo — identidades de deuda:** ingresos totales = gasto neto (DEC art. 2); presupuestarios + financiamientos = total; financiamientos − déficit = diferimiento = Adefas; balance público = presupuestario + no presupuestario; RFSPF = público + fuera del presupuesto (suma de componentes con dos decimales, p. 66–67); costo financiero = Ramo 24 + Ramo 34 + Anexo 1.E; balance por entidad suma al presupuestario; ΔSHRFSPF ≈ RFSPF − d·n/(1+n) + tipo de cambio + activos (cierra a 0.1 pp ex ante en 2023); en pesos, Δ(d × PIB nominal) ≈ RFSPF en pesos (12 mmp de residuo en 2023).

**Criterio 4, supuestos macro — el marco de cuatro variables con el caso 2022 como criterio de aceptación.** d_t = d_{t−1}/(1+n) + rfsp + fx + otros, n = (1+γ)(1+π) − 1. Crecimiento: −d·γ/(1+n). Inflación: denominador −d·π(1+γ)/(1+n) **más** compensación pagada ≈ +d·π/(1+n), que viaja en el costo financiero y en las adecuaciones; neto ≈ 0 cuando la tasa nominal sigue a la inflación. Tasa real: intereses nominales − compensación. Tipo de cambio: ≈ 0.7 pp del PIB por peso (deuda externa del sector público 220 mmd; 29.6 % del SHRFSPF, no 19.2 % que es la del GF). **Aceptación:** reproducir 2022 con la añada del CGPE 2024 (49.2 → 47.7, RFSPF 4.3, γ 3.9, π 6.7, fx −0.9, activos −0.3): resultado −1.7 contra −1.5 observado; las otras añadas dan −1.4 y −1.3. Pasa. Aplicado a 2023: tasa real +1.4 domina; inflación neta −0.1. La pregunta de harness (§6.4): con rf fijo en % del PIB, menos inflación = menos compensación pagada por el mismo rf = tasa real más alta = más deuda; 49.1 con rf 5 y γ 3 en veinte años: 62.75 (π 5) vs 75.45 (π 3). La versión de manual (primario + r − g) va aparte y con el par SHRFSPF–RFSPF; el paquete no publica un primario de RFSPF y el del balance económico sesga al optimismo por una o dos décimas.

**Criterio 5, cobertura — lista mínima para deuda:** seis agregados con cifra y % PIB; balance por entidad; fuera del presupuesto por componente; tres acervos con interno/externo; SHRFSPF 2024–2028 y RFSPF "inercial"; techos por entidad, cláusula de intercambio y CDMX; endeudamiento informativo; costo financiero por ramo/entidad y su regla del 25 %; sensibilidades; portafolio; amortizaciones (tres objetos: bonos GF, GF total, sector público); marco macro de tasas con senda; pasivo pensionario y supuesto de pensiones; Pidiregas/APP; IPAB; amortiguadores; descomposición oficial ex post (ILIF del año siguiente); PFN; LMGCE. Agotar rutas antes de declarar ausencias (nota metodológica en la Gaceta; artículo autoral en Wayback).

**Sección cero obligatoria** (00, 03, 04): piezas presentes y ausentes con ruta; criterios condicionados; proporción esperada de `no_verificable` por carpeta vs por documento; asimetría de objeto cuando solo hay aprobado.

**Verificación del frente como objeto propio:** en 2023 el frente aportó 4 de los 14 `no` de la sesión principal (6.3 billones; −11.5 nominal; equilibrio por déficit; y el 2.7 del costo financiero aparece primero en el cap. 11). Filas propias siempre.

**Tier:** vocabulario de tres valores (`oficial_primaria`, `derivada_ciep`, `autoral_ited`); `tier_seccion` sigue poblándose (restitucion / juicio / mixta), decisión formal pendiente (Héctor con Clavellina). `fuente_oficial` registra el emisor (SHCP, Ejecutivo/DEC, Congreso/LFPRH, DOF, Gaceta).

**Lo que no funcionó en 2023:** (a) el documento CIEP 2023 imprime 37 páginas como imagen: la extracción de texto no basta y la lectura de imagen es lenta y aproximada para las figuras (los `no` que descansan en cifras leídas de figuras, V042, quedan marcados como cotejo interno); (b) la nota metodológica 2023 también es imagen: se usa la edición 2022 con texto como auxiliar y se verifica página por página; (c) el marco de cuatro variables reparte inflación y crecimiento por una convención (−d·γ/(1+n) y −d·π(1+γ)/(1+n)) que otra convención cambiaría en décimas; se declara; (d) la cota de indexación (cuánto de las adecuaciones es inflación pagada) no es identificable con el paquete y deja el interés real de 2022 en un rango de un punto.

## Historial
- 2026-09-05 · ejercicio 2020 · creado.
- 2026-09-05 · ejercicio 2021 · adenda (reorden, convenciones §1, tipo_error, casos límite de perímetro, pendiente 9.2).
- 2026-09-05 · ejercicio 2022 · adenda (reorden para ingresos, columnas nuevas, casos de contrafactual y perímetro en ingresos, criterio de supuestos macro, lista mínima de cobertura, identidades, fuentes ex post, lo que no funcionó).
- 2026-09-06 · ejercicio 2023 · adenda (identidad de objeto como primer criterio, `objeto`, nomenclatura RFSPF/SHRFSPF, quinta declaración en deuda, identidades, marco de cuatro variables con el caso 2022, cobertura de deuda, sección cero, frente, tier, lo que no funcionó).
