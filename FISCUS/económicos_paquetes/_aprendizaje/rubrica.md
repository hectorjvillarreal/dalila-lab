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

## Historial
- 2026-09-05 · ejercicio 2020 · creado.
- 2026-09-05 · ejercicio 2021 · adenda (reorden, convenciones §1, tipo_error, casos límite de perímetro, pendiente 9.2).
