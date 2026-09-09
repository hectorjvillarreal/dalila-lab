# FISCUS — Corrida en vivo, Paquete Económico 2027

**Documento 2 de 2.** **Condición de activación: CGPE, ILIF y PPEF 2027
publicados.** No ejecutes antes.

**Proyecto:** FISCUS · **Ubicación:** `FISCUS/económicos_paquetes/` · **Máquina:** Dalila
**Tipo:** instrucción de trabajo (no es build instruction registrada)
**Producto:** documento completo del género, de autoría ITED, sobre el Paquete
Económico 2027, en PDF, LaTeX y Markdown.
**Requisito previo:** `INSTRUCCIONES_preparacion_2027.md` ejecutado. Si algo de su
§3 no quedó precargado, se paga con reloj: anótalo y sigue.

---

## 0. Qué distingue esta corrida

Es la primera **sin documento de CIEP para comparar** y la primera con **reloj
real**. Las dos anteriores tenían comparador y tiempo; esta no tiene ninguno de
los dos.

De ahí tres cambios:

- **La checklist de omisiones sustituye al comparador.** No habrá quien detecte
  lo que se nos pase, así que la detección tiene que ser propia y sistemática.
- **La compuerta semántica es obligatoria antes de compilar.** Sin comparador
  externo, un titular que excede su perímetro no lo corrige nadie.
- **El alcance está decidido de antemano** (§7 del documento 1). No se
  reabre con el reloj corriendo.

---

## 1. Bandas de reloj

Arranca el cronómetro al iniciar y registra la hora en que cada hallazgo queda
disponible.

| Banda | Qué debe estar hecho |
|---|---|
| **0–2 h** | Descarga completa. Marco macro. Agregados de ingreso, gasto, balance y deuda. Pruebas de identidad corridas. Primer diff institucional. |
| **2–8 h** | Diff resuelto y reclasificaciones documentadas. Capítulos de ingresos, gasto agregado, energía, deuda y **regla fiscal**. Comparaciones estructurales extendidas. |
| **8–24 h** | Capítulos sectoriales: salud, educación, pensiones, inversión, seguridad, gasto federalizado, medio ambiente y agua, anexos transversales. Capa demográfica aplicada. |
| **24 h+** | Compuerta semántica. Fichas. Láminas. LaTeX, compilación y entrega. |

**No aceleres a costa de verificar.** Si una banda no se alcanza, se declara y se
sigue; el documento sale con los capítulos que estén y con las declaraciones de
los que no.

---

## 2. Fuentes y descarga

Corre el guion de rutas probadas (§3.8 del documento 1). Regla de no bloqueo:
**dos intentos por pieza; si falla, se registra ruta y respuesta, y la corrida
continúa.** Entrega degradada antes que no entrega.

Piezas: CGPE, ILIF —el PDF contiene su exposición de motivos—, PPEF con proyecto
de decreto y anexos; **analíticos del proyecto** (portal de la Secretaría, portal
de datos abiertos, Transparencia Presupuestaria, en ese orden); iniciativa de
miscelánea en la Gaceta Parlamentaria; y todo el histórico hasta 2026 inclusive,
aprobados incluidos.

Bundle TLS preparado, sin desactivar verificación. Los analíticos traen los datos
en la hoja **`Hoja1`**.

### 2.1 Las dos rutas

Resuelve en la primera banda y **declara cuál se adoptó**:

- **Ruta A, hay analíticos del proyecto:** el documento trabaja a nivel de
  programa presupuestario y unidad responsable.
- **Ruta B, no los hay:** el documento trabaja a nivel de ramo y función, y
  **declara en el texto qué no puede decir**: composición por programa,
  reasignaciones entre unidades, distribución territorial, y separación entre
  caída de ramo y caída de función donde la fuente no la permita.

Bajo la Ruta B varios capítulos pueden no alcanzar el presupuesto de
afirmaciones. **Eso es un resultado, no un fracaso:** se declaran no redactables
y se sigue.

---

## 3. Base de comparación — dos líneas, nunca mezcladas

| Línea | Comparación |
|---|---|
| **Primaria (de la casa)** | Proyecto 2027 contra proyecto 2026 — ex ante contra ex ante |
| **Segunda (del género)** | Proyecto 2027 contra aprobado 2026 — la que usa la discusión pública |

Ambas declaradas, ambas donde la cifra importe, **nunca en el mismo cuadro sin
etiqueta**. Donde difieran de forma material, la diferencia mide lo que la Cámara
cambió el ejercicio previo y es un hallazgo.

---

## 4. Antes de calcular una sola variación

**Corre el diff institucional** (§3.3 del documento 1): ramos, claves de
programa, unidades responsables, funciones y subfunciones. Por clave, no por
nombre, con emparejamiento por número de programa más contexto de ramo.

En 2026 hubo 271 claves nuevas y 358 desaparecidas, cinco ramos extintos y tres
nuevos. Sin diff previo, cualquier comparación produce recortes y aumentos
falsos.

**Regla que se conserva:** ramo y función son objetos distintos. Una caída de
ramo no es una caída de la función que su nombre sugiere. La Guardia Nacional en
2026 es el caso didáctico: cambio de ramo y reducción propia ocurriendo a la vez.

Corre después las **pruebas de identidad** parametrizadas. Un dígito mal rompe
una suma; no dependas de releer el mismo PDF.

---

## 5. Estructura del documento

Tres partes: **(+) Ingresos**, **(−) Gasto**, **(=) Balance y Deuda**. Plantilla
por capítulo: **POLÍTICA / EVOLUCIÓN / PROGRAMAS SELECCIONADOS / IMPLICACIONES**.
El juicio va en IMPLICACIONES.

Capítulos: resumen; marco macroeconómico; ingresos; ingresos energéticos y
empresas públicas; gasto total; **regla fiscal y perímetro de exclusión**; salud;
educación; pensiones; inversión; seguridad; gasto federalizado; medio ambiente y
agua; anexos transversales; balance y deuda; horizonte demográfico.

Cada capítulo: **lámina de apertura** (titular cuantitativo con signo y base
declarada, figura principal, párrafo de "qué cambió", párrafo de "por qué
importa"), cuerpo, **sección "qué no sabemos"**, y **ficha metodológica de
cierre**.

**Presupuesto de afirmaciones:** al menos doce verificables por capítulo, seis de
ellas restitución de fuente oficial, y no más de 30 % no verificables. Si no
llega, se escribe la declaración de capítulo no redactable en el registro del
documento.

### 5.1 Capítulo de la regla fiscal · NUEVO Y PRIORITARIO

Es el hallazgo que los dos documentos de 2026 perdieron y el de mayor valor.

Lee el artículo de la ILIF 2027 que fija, para efectos del equilibrio
presupuestario, el perímetro de gasto **no contabilizable** y su tope en
porcentaje del PIB. En 2026 fue 3.6 % e incluía inversión física, inversión
financiera y desarrollo de capital humano —educación, salud preventiva, formación
y certificación de competencias—, excluyendo pensiones, transferencias no
condicionadas, subsidios generalizados y gasto administrativo.

El capítulo debe traer:

1. El artículo y su texto, con la cifra del tope.
2. **La serie 2018–2027** del perímetro de exclusión (precargada, §3.2 del
   documento 1), con el diff respecto al ejercicio previo: qué conceptos entran,
   cuáles salen, cómo se mueve el tope.
3. El **monto potencialmente excluible** bajo el paquete, y su composición.
4. **La conexión con inversión financiera:** si hay aportación de capital a
   empresas públicas clasificada en el capítulo 7000 como adquisición de títulos
   y valores, es inversión financiera y por tanto candidata a quedar fuera del
   cómputo. Verifícalo y dilo con la cifra.
5. Consecuencias para la lectura del balance y para la comparabilidad temporal.

**No conviertas esto en un juicio sobre disciplina fiscal.** Es una descripción de
perímetro con su serie. El lector saca la conclusión.

### 5.2 Capítulo de deuda

Descomposición del cambio de la razón SHRFSPF/PIB en crecimiento, tasa real,
inflación y tipo de cambio, **con la exigencia de que los componentes sumen el
cambio observado**. Criterio de aceptación: reproducir la caída de 2022 —RFSPF de
4.5 % del PIB con el acervo bajando de 50.7 a 49.4 %— antes de aplicarla a 2027.

Reporta la sensibilidad al tipo de cambio: la trayectoria puede mejorar por
valuación sin mejora fiscal. En la inflación, no supongas el signo: parte del
pasivo está indexado, y cuando el índice exacto no se identifique, **presenta el
rango**. No presentes el marco de manual en el documento.

Declara siempre cuál de los tres flujos y cuál de los tres acervos se usa, y
distingue **techo de endeudamiento** de **déficit**.

### 5.3 Capa demográfica

Aplica la capa precargada. Cuadros presupuestales y per cápita **separados**;
cada cifra per cápita declara su denominador, año y cobertura; en educación se
distinguen población total, población en edad escolar y matrícula.

**La advertencia se conserva íntegra:** una razón de gasto pensionario sobre
población de 65 años y más es un indicador de presión demográfica, **no una
pensión media**, porque el denominador incluye a quien no recibe y el numerador
puede incluir pensiones de menores de esa edad.

Verifica el hallazgo transversal: si el paquete trae horizonte demográfico donde
la transición presiona al alza y lo omite donde puede liberar espacio fiscal.

### 5.4 Anexos transversales

Auditoría de etiquetado, que es donde nuestro método aporta: cuánto del gasto
programable aparece etiquetado, qué programas están en más de un anexo, qué
proporción del etiquetado para igualdad son programas de pensión. **Los anexos no
se suman**, y el tamaño de un anexo no mide el gasto marginal causado por la
prioridad que le da nombre.

Género y cuidados se tratan **solo así**. Lo que quede fuera se declara.

---

## 6. Convenciones — sin excepción

Nomenclatura **RFSPF/SHRFSPF** con equivalencia declarada una vez. Deflactor del
PIB con la excepción de prestaciones individuales, explicada en el recuadro
metodológico; nunca derivado de agregados redondeados. Las **cinco
declaraciones** del contrafactual: nominal o real; contra aprobado o contra
cierre; contra año previo o contra PIB; en pesos de qué año; con qué PIB y de qué
añada. Perímetro declarado antes del primer cuadro y constante. **Toda diferencia
en millones de pesos declara si es nominal o real.** Prohibición de yuxtaponer
magnitudes sin mecanismo declarado. Definiciones adjudicadas contra *Balance
Fiscal en México* (SHCP, abril 2023), nunca por criterio propio. Gasto pagado,
devengado y neto se distinguen.

Nunca cites tasas de acierto entre ejercicios sin decir qué había en carpeta.

**Nada de referencias temporales relativas.** Fecha o ejercicio.

---

## 7. Compuerta semántica — obligatoria antes de compilar

Aplica `_aprendizaje/compuerta_semantica.md` a cada titular, cada frase del
resumen y cada pie de figura:

1. Localiza el renglón de la ficha del que sale la cifra.
2. Compara el sujeto de la frase con el perímetro de la ficha. **Si el sujeto es
   más amplio, reescribe la frase, no la ficha.**
3. Marca cada afirmación causal y responde: ¿está documentada por la fuente?
   ¿puede ser reclasificación? ¿puede ser composición? ¿puede ser un efecto
   contable?

Casos que ya nos ocurrieron y no deben repetirse: nombrar "pensiones" un agregado
que es "pensiones y jubilaciones de la clasificación económica"; extrapolar a
"todo el gasto de capital" una proporción calculada sobre los capítulos 6000 y
7000; decir "menos recursos condicionados" cuando las aportaciones crecen, solo
que menos.

Y dos inferencias que no se hacen: la igualdad numérica entre endeudamiento y
costo financiero **no identifica** el destino marginal del financiamiento, porque
los recursos son fungibles; un subsidio tarifario **no demuestra** por sí solo
ineficiencia de la empresa.

Registra en la bitácora cuántas frases se reescribieron.

---

## 8. Checklist de omisiones — sustituye al comparador

Antes de cerrar, recorre `_aprendizaje/checklist_omisiones.md` renglón por
renglón y marca: **cubierto**, **parcial**, o **fuera de alcance con su razón**.

Lo que quede fuera de alcance **se declara en el documento**, no se omite en
silencio. Un capítulo que dice con precisión qué no aborda es mejor que uno que
finge cobertura.

---

## 9. Entrega

En `_documento_2027/entrega/`:

1. **`documento_2027.pdf`** — compilado en Dalila. **Un PDF que no exista no
   cuenta como entrega.**
2. **`documento_2027.zip`** — proyecto LaTeX portátil, con `LEEME.md` que indique
   versión de TeX Live y comando de compilación.
3. **`documento_2027.md`**.
4. **`datos/`** con `_fuentes.csv`.

Restricciones de portabilidad, ya establecidas: **sin `siunitx`**, números
formateados al generar los cuadros; `pgfplots` con `compat=1.16`; solo los
paquetes de la lista; nada con `shell-escape`.

Si un capítulo rompe la compilación: **aíslalo, compila el resto, entrega el PDF
parcial y reporta cuál falló y por qué.** Nunca un proyecto sin PDF.

---

## 10. Bitácora

Hora de inicio y **el reloj de cada hallazgo**. Piezas que no llegaron, con
respuesta del servidor, primero de todo. **Ruta adoptada (A o B), con hora.**
Resultado de las pruebas de identidad y del diff, con el conteo de claves nuevas
y desaparecidas. Presupuesto de afirmaciones por capítulo y capítulos no
redactables. **Frases reescritas por la compuerta semántica.** Estado de la
checklist de omisiones. Verificaciones imposibles en vivo. Compilación y
warnings. Las series de seguimiento, incluida la del perímetro de la regla
fiscal. El pasivo pensionario y el supuesto de crecimiento de pensiones **siguen
congelados para calibración**.

Y al final: **qué se pagó con reloj por no haber quedado precargado.** Eso es lo
que mejora la preparación del ejercicio siguiente.

---

## 11. Límites

- No uses nada aprobado del ejercicio 2027: no existe.
- No calcules una variación antes de correr el diff.
- No mezcles las dos líneas de comparación en un cuadro sin etiqueta.
- No mezcles cifras del paquete con denominadores externos en la misma línea.
- **No compiles sin pasar la compuerta semántica.**
- No rellenes: un capítulo sin datos se declara, no se escribe.
- No conviertas el capítulo de la regla fiscal en un juicio sobre disciplina
  fiscal: describe el perímetro y su serie.
- No uses el pasivo pensionario ni el supuesto de pensiones en calibración.
- No entregues proyecto sin PDF.
- El documento es de ITED, con portada y autoría propias, y no puede confundirse
  con el de ninguna otra casa.
- Donde no puedas verificar, dilo en el documento, no solo en la bitácora.
