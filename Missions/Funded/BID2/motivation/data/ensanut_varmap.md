# ENSANUT variable map — BID2 health-expenditure motivation

**Waves**: ENSANUT 2018-19 (`data/ensanut/ensanut2018/`) and ENSANUT Continua 2024 (`data/ensanut/ensanutcontinua2024/`).
**Method**: all variable names, labels (verbatim Spanish) and value codes below were read from the shipped `Catálogo .xlsx` codebooks, CSV headers, and (for `adultos_ensanut2024_w.dta`) the Stata variable/value labels via pandas. Nothing is from memory. Cross-checks (row counts, merge keys) run on the actual microdata 2026-08-08.

---

## File inventory and row counts

| Wave | File | Rows (data) | Unit | Linking key |
|---|---|---|---|---|
| 2018 | CS_VIVIENDAS.csv | 44,069 | dwelling | UPM + VIV_SEL |
| 2018 | CS_HOGARES.csv | 44,612 | household | UPM + VIV_SEL + HOGAR |
| 2018 | CS_RESIDENTES.csv | 158,044 | person (roster) | UPM + VIV_SEL + HOGAR + NUMREN |
| 2018 | CS_ADULTOS.csv | 43,070 | selected adult 20+ | UPM + VIV_SEL + HOGAR + NUMREN |
| 2018 | CS_SERV_SALUD.csv | 8,757 | selected utilizador | UPM + VIV_SEL + HOGAR + NUMREN |
| 2024 | hogar_ensanut2024_w_ICB.csv | 10,975 | household | FOLIO_I |
| 2024 | integrantes_ensanut2024_w_ICB.csv | 36,021 | person (roster) | FOLIO_I + FOLIO_INT (also id_int) |
| 2024 | adultos_ensanut2024_w.dta | 12,924 | selected adult | FOLIO_I + FOLIO_INT |
| 2024 | utilizadores_ensanut2024_w.csv | 3,223 | selected utilizador | FOLIO_I + FOLIO_INT |
| 2024 | NSE_Hogar_ENSANUT_2024.csv | 10,975 | household | FOLIO_I |
| 2024 | NSE_Integrantes_ENSANUT_2024.csv | 36,021 | person | FOLIO_I + FOLIO_INT + id_int |

**Merge verification (all 100% matched, zero duplicates on keys):**
- 2018: CS_SERV_SALUD → CS_HOGARES on (UPM, VIV_SEL, HOGAR): 8,757/8,757. CS_SERV_SALUD → CS_RESIDENTES on (UPM, VIV_SEL, HOGAR, NUMREN): 8,757/8,757.
- 2024: integrantes → hogar on FOLIO_I: 36,021/36,021. utilizadores → integrantes on (FOLIO_I, FOLIO_INT): 3,223/3,223. NSE_Hogar → hogar on FOLIO_I: 10,975/10,975.
- CSV format note: **all CSVs are semicolon-delimited** with a UTF-8 BOM on the first column name. In the 2024 NSE files `indice1` uses **comma as decimal separator** (e.g. `,641003645224495`) — parse with `decimal=","`.

---

# ENSANUT 2018-19

## 1. Survey design

| Variable | File(s) | Label (verbatim) |
|---|---|---|
| `FACTOR` | CS_RESIDENTES | "Factor de residentes" — person-level weight for the roster |
| `FAC_HOGAR` | CS_HOGARES | "Factor del Hogar" |
| `FAC_VIV` | CS_VIVIENDAS | "Factor de la Vivienda" |
| `F_20MAS` | CS_ADULTOS | "Factor de Adultos" — weight for the adults-20+ module |
| `F_SERSA` | CS_SERV_SALUD | labeled "Factor de la Vivienda" in the catalog (sic), but it is the weight of the utilizadores (health-services) module |
| `EST_DIS` | all files | "Estrato de diseño" (design stratum) |
| `UPM_DIS` | all files | "UPM de diseño" (design PSU) |
| `UPM` | all files | "Unidad Primaria de Muestreo" (sampling frame PSU id; part of the merge key) |
| `ESTRATO` | all files | "Estrato sociodemográfico" — values 1–4 in data (no value labels in catalog; INEGI convention: 1 bajo … 4 alto) |
| `DOMINIO` | all files | 1 Urbano / 2 Rural |
| `REGION` | all files | 1 Norte / 2 Centro / 3 Ciudad de México / 4 Sur |
| `ENT` | all files | "Clave de Entidad Federativa" |

**Which weight for what**: use `FACTOR` for roster-level estimates (forgone care in CS_RESIDENTES), `F_SERSA` for the utilizadores module, `F_20MAS` for chronic-disease/adult outcomes, `FAC_HOGAR` for household expenditure. Design: `EST_DIS` (strata) + `UPM_DIS` (PSU).

## 2. Roster / demographics / insurance (CS_RESIDENTES)

| Variable | Label (verbatim) | Codes |
|---|---|---|
| `SEXO` | "es hombre/es mujer" | 1 Hombre, 2 Mujer |
| `EDAD` | "Edad" | years |
| `NUMREN` | "Número de Renglón" | person line number |
| `HOGAR` | "Número de Hogar" | |
| `P3_5` | "¿Qué es (NOMBRE) de la (del) jefa(e)?" | 01 Jefa(e) … 09 Sin parentesco |

**Insurance affiliation — P3_10 block**: "3.10 ¿(NOMBRE) tiene derecho o acceso a servicios médicos…" Dummies (0 = "No se declaró como opción afirmativa", 1 = Sí):
`P3_10_01` IMSS · `P3_10_02` ISSSTE · `P3_10_03` ISSSTE Estatal · `P3_10_04` Pemex · `P3_10_05` Defensa · `P3_10_06` Marina · `P3_10_07` **"del Seguro Popular o Seguro Médico Siglo XXI?"** · `P3_10_08` IMSS PROSPERA · `P3_10_09` "de un seguro privado de gastos médicos?" · `P3_10_10` otra institución · `P3_10_11` **"¿No está afiliado o inscrito a servicios médicos?"** (uninsured) · `P3_10_99` No sabe. `P3_10_OPC1`/`P3_10_OPC2` give first/second declared option as a single coded variable.

**Usual source of care — P3_9 block** ("Cuando (NOMBRE) tiene problemas de salud, ¿en dónde se atiende usualmente?"): dummies `P3_9_01`–`P3_9_12` incl. `P3_9_09` "Consultorios dependientes de farmacias", `P3_9_10` "Consultorio, clínica u hospital privado", `P3_9_11` "Se automedica", `P3_9_12` "No se atiende".

Also: employment benefits `P3_24_01` "¿(NOMBRE) recibe o puede recibir por su trabajo…Servicio médico (IMSS,ISSSTE u otro)?" (1 Sí/2 No/3 No sabe), `P3_24_10` "seguro privado para gastos médicos?".

## 3. FORGONE / DELAYED CARE (critical block)

### 3a. Roster screening, CS_RESIDENTES (all persons; weight `FACTOR`)

| Variable | Label (verbatim) | Codes |
|---|---|---|
| `P4_3` | "En el último mes ¿(NOMBRE), ha tenido algún problema de salud, por enfermedad, lesiones físicas, accidentes o Agresiones?" | 1 Sí, 2 No, 9 No sabe |
| `P4_4` | "¿Esto ocurrió en las últimas dos semanas?" | 1/2/9 |
| `P4_5` | "¿Está (NOMBRE) recibiendo o recibió atención por este padecimiento?" | 1 Sí, 2 No, 9 No sabe |
| `P4_8_01`–`P4_8_99` | "¿Quién atendió a (NOMBRE)?" dummies | 01 Familiar, 03 Dependiente de la farmacia, 11 Médico general, 12 Médico especialista, … 20 **Nadie** |

**Reasons for not getting professional care — P4_9 dummy block** ("¿Por qué no se atendió (NOMBRE) con un médico, enfermera o algún otro personal de salud?", each 0/1):

| Var | Reason (verbatim) |
|---|---|
| `P4_9_01` | No fue necesario |
| `P4_9_02` | Falta de confianza |
| `P4_9_03` | Decidió no atenderse |
| `P4_9_04` | Tratan mal |
| `P4_9_05` | No lo atendieron |
| `P4_9_06` | Le dijeron que su problema no era urgente |
| `P4_9_07` | No tuvo tiempo |
| `P4_9_08` | No había servicio en el horario en el que lo necesitaba |
| `P4_9_09` | La unidad médica estaba cerrada |
| `P4_9_10` | No tuvo quién lo llevara o acompañara |
| `P4_9_11` | Está muy lejos |
| **`P4_9_12`** | **Es caro** ← COST |
| **`P4_9_13`** | **No tenía dinero** ← COST |
| **`P4_9_14`** | **Le dijeron que tenía que pagar por la atención y los medicamentos** ← COST |
| `P4_9_15` | Le dijeron que el seguro no cubría la enfermedad que tiene |
| `P4_9_16` | En el lugar donde lo enviaron no atendían a las personas del Seguro Popular |
| `P4_9_17` | Le solicitaron un pase de referencia y no lo pudo conseguir |
| `P4_9_18` | No hay dónde atenderse |
| `P4_9_19` | No tenían el equipo necesario para atender su padecimiento |
| `P4_9_20` | Los trámites eran muy tardados |
| `P4_9_21` | No alcanzó ficha/había mucha gente |
| `P4_9_22` | El tiempo para pasar a consulta era muy largo |
| `P4_9_23` | El tiempo para ser hospitalizado era muy largo |
| `P4_9_77` / `P4_9_99` | Otro / No sabe |

### 3b. Utilizadores module, CS_SERV_SALUD (weight `F_SERSA`)

| Variable | Label (verbatim) | Codes (cost codes bold) |
|---|---|---|
| `P1_1` | "En las últimas dos semanas, ¿usted solicitó ser atendido(a) por algún profesional de salud o centro sanitario debido a un problema de salud, enfermedad, control de la misma, lesión o accidente?" | 1 Sí, 2 No |
| `P2_1` | "¿Por qué no buscó atención?" (single code) | 01 No hay dónde atenderse, **02 Es caro**, **03 No tenía dinero**, 04 Está muy lejos, 05 Falta de confianza, 06 Tratan mal, 07 No tuvo tiempo, 08 Decidió no atenderse, 09 No tuvo quien lo(la) llevara o acompañara, 10 No había servicio en el horario en que lo necesitaba, 11 Los trámites eran muy tardados, 12 El tiempo para pasar a consulta era muy largo, 13 No tuvo problemas de salud en las últimas dos semanas, 14 Otro, 99 No sabe |
| `P3_1` | "¿Le atendieron?" | 1 Sí, 2 No |
| `P3_2` | "¿Por qué motivo no le atendieron?" (sought but denied) | 01 El prestador pensó que no era necesario, **02 Es caro**, 03 Lo rechazaron por no ser derechohabiente, 04 seguro no cubría la enfermedad, 05 pase de referencia no conseguido, 06 no atendían a personas con Seguro Popular, 07 unidad cerrada, 08 No alcanzó ficha/había mucha gente, 09 problema no era urgente, **10 Le dijeron que tenía que pagar por la atención y los medicamentos**, 11 no tenían el equipo, 12 horario, 13 trámites tardados, 14 tiempo de espera largo, 15 Otro, 99 NS |

**Cost-barrier battery (12-month recall, Commonwealth-Fund style) — P8_1 block** ("Durante los últimos 12 meses, ¿hubo alguna vez en que usted…"), each coded 1 Sí, 2 No, 3 No aplica, 8 No responde, 9 No está seguro(a):

| Var | Item (verbatim) |
|---|---|
| **`P8_1_1`** | "tuvo un problema médico, pero no pudo "consultar" a un médico **debido al costo**?" |
| **`P8_1_2`** | "no se hizo un examen, un tratamiento o seguimiento médico recomendado por un médico **debido al costo**?" |
| **`P8_1_3`** | "no "compró" un medicamento de venta con receta, o no tomó todas las dosis **debido al costo**?" |
| `P8_1_4` | "no visitó a un médico debido a que tuvo dificultades para viajar?" |
| `P8_1_5` | "tuvo un problema médico que le preocupaba y tardó mucho tiempo en recibir un diagnóstico?" |

Delay-adjacent: `P8_2` "La última vez que estuvo enfermo(a)… ¿con qué rapidez pudo hacer una cita…?" (1 El mismo día … 7 Nunca pudo programar una cita).

**Medicines not obtained** — `P5_3` "¿Consiguió todos los medicamentos?" (1 Sí / 2 Sí, solo algunos / 3 No); `P5_5` "¿Por qué no lo(s) consiguió?": 01 No había el medicamento en la institución, … **06 Le parecieron caros**, **07 No tenía dinero**, 10 La atención no incluye los medicamentos, …

## 4. Utilization, service type, motive

**CS_RESIDENTES:** `P4_11` "En las últimas dos semanas, ¿(NOMBRE) solicitó consulta que no haya requerido hospitalización…?" (1/2/9); `P4_10` "¿En qué institución de salud se atendió (NOMBRE)?" 01 IMSS, 02 ISSSTE, 03 ISSSTE Estatal, 04 Pemex, 05 Defensa, 06 Marina, 07 Centro de Salud u Hospital de la SSA, 08 IMSS PROSPERA, **09 Consultorios dependientes de farmacias**, **10 Consultorio, clínica u hospital privado**, 11 Ninguna, 77 Otro, 99 NS. Hospitalization: `P4_12` (12-month), `P4_13` motive (01 Cirugía, 02 Enfermedad, 03/04 Lesiones, 05 Parto, 06 Cesárea, 07 Embarazo/puerperio, **08 Examen/chequeo**, 09 Caídas), `P4_14` institution (same list as P4_10).

**CS_SERV_SALUD:**
- `P1_2` "¿cuál fue el principal problema o motivo por el que tuvo necesidad de solicitar atención?" — 45-category condition list (01 Infecciones respiratorias … 12 Diabetes, 13 Hipertensión arterial, … 42 Susto/empacho/mal de ojo, **43 Embarazo**, 44 Cáncer o tumores, 45 Otro, 99 NS). Note: the 2018 module screens on illness/accident/control ("problema de salud, enfermedad, control de la misma, lesión o accidente"), so it is essentially **curative/condition-driven**; pure preventive check-ups are not a listed motive (embarazo=43 is the closest preventive-type code).
- `P3_3` "¿A qué tipo de centro o unidad médica fue a buscar atención?": 1 Hospital, 2 Consultorio o centro de salud, **3 Consultorios dependientes de farmacias**, **4 Consultorio, clínica u hospital privado**, 6 Otro, 9 NS.
- `P3_4` "¿Qué persona lo(a) atendió?": 01 Dependiente de la farmacia … 05 Médico general, 06 Médico especialista, 07 Dentista, 08 Enfermera, 09 Nutriólogo.
- `P3_7` "¿A qué institución pertenece la persona que le atendió?": same 01–10 institution list (09 = consultorios de farmacia, 10 = privado).
- `P3_6_1`–`P3_6_8` reasons for choosing the place (dummy; `P3_6_3` "Es barato/no cuesta").

**Preventive care (2018)** lives in CS_ADULTOS block P10: `P10_1_1`–`P10_1_11` "Durante los últimos 12 meses, ¿acudió al módulo de medicina preventiva para que le realizaran…" (papanicolaou, …, `P10_1_10` antígeno prostático, `P10_1_11` tacto rectal), each row with companion vars `P10_2_x`–`P10_7_x`.

## 5. Health status and chronic conditions (CS_ADULTOS; weight `F_20MAS`)

| Variable | Label (verbatim) | Codes |
|---|---|---|
| `P3_1` | "¿Algún médico le ha dicho que tiene diabetes (o alta el azúcar en la sangre)?" | 1 Sí, 2 Sí durante el embarazo (gestacional), 3 No |
| `P3_2` | age at diabetes diagnosis | 99 NS |
| `P4_1` | "¿Algún médico le ha dicho que tiene la presión alta?" | 1 Sí, 2 No |
| `P4_4` | "¿Actualmente toma alguna medicina (pastillas) para controlar su presión alta?" | |
| `P5_2_1` | "¿Le ha dicho el médico que usted tiene (o tuvo) ... un infarto o ataque al corazón?" | |
| `P6_4` | "¿Algún médico le ha dicho que tiene el colesterol alto?" | |
| `P1_1` | "¿Alguna vez le ha dicho un médico/dietista/nutriólogo que tiene o tuvo obesidad?" | |
| `P2_1_1`–`P2_1_7` | CESD-7 depression screen ("Durante la última semana…") | |

**No general self-rated health item** ("¿cómo diría que es su salud?") exists in CS_ADULTOS 2018 — see Gaps. Post-care perceived change only: CS_SERV_SALUD `P7_1` "Después de la última atención… ¿considera que su estado de salud…" (1 mejoró mucho … 5 empeoró mucho).

## 6. Socioeconomic position (2018)

- **Income (individual, roster)**: CS_RESIDENTES `P3_26_1` "¿Cada cuándo obtiene (NOMBRE) sus ingresos o le pagan?" (1 mes/2 quincena/3 semana/5 diario/6 no recibe/9 NS) + `P3_26_2` "¿Cuánto ganó o en cuánto calcula sus ingresos?" (999999 NS).
- **Assets**: CS_HOGARES `P6_1_1`–`P6_1_15` "¿Usted o algún integrante de su hogar tiene ... a) televisión? … o) horno de microondas?"; CS_VIVIENDAS `P1_24_1`–`P1_24_5` (calentador, tinaco, cisterna, medidor de luz, aire acondicionado) and `P1_25_1`–`P1_25_5` (otra propiedad, automóvil, camioneta, moto, otro vehículo); dwelling materials `P1_1`–`P1_3`, services `P1_11`–`P1_19`.
- **Stratum proxy**: `ESTRATO` "Estrato sociodemográfico" (1–4) in every file.
- **Household health spending (3-month recall)**: CS_HOGARES `P7_2_1`–`P7_2_9` "En los últimos 3 meses, ¿cuánto gastaron los integrantes del hogar en..." (hospitalización, consultas ambulatorias, curanderos, dentista, **`P7_2_5` medicamentos**, lentes/aparatos, laboratorio, otros, **`P7_2_9` primas de seguros voluntarios**). Distress financing: `P7_3_1`–`P7_3_6M` (ahorros, venta de propiedades, empeño, préstamos, crédito bancario, otro + montos). Hospital nights: `P7_4`, `P7_5`.

## 7. Out-of-pocket per-event amounts (2018)

| Variable | File | Label (verbatim) | Special codes |
|---|---|---|---|
| `P4_7` | CS_RESIDENTES | "¿Cuánto pago por los medicamentos que utilizo?" | 000000 No pagó, 999999 NS |
| `P4_2` | CS_SERV_SALUD | "En total, ¿cuánto pagó para llegar hasta el sitio en que lo(a) atendieron?" (transport) | 7777 No pagó, 9999 NS |
| `P4_8` / `P4_9` | CS_SERV_SALUD | "¿Le cobraron por la atención que recibió?" / "¿Cuánto le cobraron?" (consultation fee) | 9999 NS |
| `P5_6` | CS_SERV_SALUD | "¿Cuánto pagó por los medicamentos que consiguió?" | 0000 No pagó, 9999 NS |
| `P6_4` | CS_SERV_SALUD | "¿Cuánto pagó por los exámenes de laboratorio o gabinete que se realizó?" | 0000 No pagó, 9999 NS |
| `P6_6_1`–`P6_6_3` | CS_SERV_SALUD | "¿En qué y cuánto gastó?" Otros gastos médicos / Comida-hospedaje / Otros gastos | 9999 NS |

---

# ENSANUT Continua 2024

## 1. Survey design

| Variable | File(s) | Label (verbatim) |
|---|---|---|
| `ponde_f` | hogar | "ponderador de hogar" |
| `ponde_f` | integrantes | "ponderador de integrantes de hogar" |
| `ponde_f` | adultos (.dta) | "Ponderador" (adult-module weight) |
| `ponde_f` | utilizadores | "Ponderador" (utilizadores-module weight) |
| `estrato` | all | "Estrato urbanidad/ruralidad": 1 "Rural ( <2500 Hab )", 2 "Urbano ( 2500-99,999 Hab)", 3 "Metropolitano (100mil y + Hab)" |
| `est_sel` | all | "Estrato de seleccion" |
| `upm` | all | "Unidad primaria de muestreo" |
| `entidad` / `desc_ent` / `municipio` | all | state/municipality |
| `x_region` | hogar, integrantes | "Entidad" (region grouping, sic label) |

Same variable name `ponde_f` in every file but a **different weight in each** — use the weight shipped in the file whose unit of analysis you estimate. Design: `est_sel` (selection stratum) + `upm`; `estrato` is the urbanicity classifier.

## 2. Roster / demographics / insurance (integrantes_ensanut2024_w_ICB)

| Variable | Label (verbatim) | Codes |
|---|---|---|
| `h0302` | "Sexo" | 1 Hombre, 2 Mujer |
| `h0303` | "Edad" | years (`meses` for infants) |
| `FOLIO_I` / `FOLIO_INT` / `id_int` | Folio / Folio integrante / Int_hogar | keys |
| `h0305` | "¿Que es (NOMBRE) de la (del) jefe(a)?" | relationship |
| `intsel` | "Integrante Seleccionado Módulo Salud" | selection flag |

**Insurance — H0310A/B/C** (up to 3 mentions): "H0310 ¿(USTED/NOMBRE) tiene derecho o acceso a servicios médicos..." — 1 "del Seguro Social (IMSS)?", 2 "del ISSSTE/ ISSSTE Estatal?", 4 PEMEX, 5 Defensa, 6 Marina, 8 "de un seguro privado de gastos médicos?", 9 otra institución, **10 Ninguno** (uninsured), **11 IMSS-BIENESTAR (que eran antes centros de salud de la Secretaría de Salud)**, 99 NS/NR. Note: **no Seguro Popular/INSABI code — the public-uninsured scheme is code 11 IMSS-BIENESTAR**; code 3 and 7 are unused in the catalog.

**Usual source of care — `h0309`**: "Cuando tiene una necesidad de salud, ¿en dónde se atiende usualmente?..." 26-category provider list: 1 IMSS, 2 ISSSTE, 3 PEMEX, 4 Defensa, 5 Marina, 6 Centros de Salud u Hospital de la SSA, 8 DIF, 9 Cruz Roja/Verde, 10 Instituto Nacional de Salud, 11 ONG/dispensario, **12 Consultorios pertenecientes a farmacias/Farmacias con consultorio médico**, 13–18 private modalities (13 consultorio en hospital privado, 14 urgencias/hospitalización privada, 15 torre de consultorios/clínica sin camas, 16 consultorio en domicilio del médico, 17 atención privada a domicilio, 18 telemedicina privada), 19 médico laboral, 20–21 traditional/homeopath, 24 consultorio psicológico, 25 CESAME, **26 IMSS-BIENESTAR**.

## 3. FORGONE / DELAYED CARE (integrantes; weight `ponde_f` of integrantes)

Screening chain (verified distributions in data):

| Variable | Label (verbatim) | Codes / n |
|---|---|---|
| `h0401` | "H0401 En los últimos 3 meses ¿(USTED/NOMBRE) ha tenido alguna necesidad de salud?" | 1 Sí (n=8,805), 2 No (27,216) |
| `h0402` | "H0402 ¿Podría decirme cuál fue la última necesidad de salud que tuvo (USTED/NOMBRE) en los últimos 3 meses?" | see §4 |
| `h0403` | "H0403 ¿Esto ocurrió en las últimas dos semanas?" | 1/2 |
| `h0404` | "H0404 ¿(USTED/NOMBRE) buscó atención por esa necesidad de salud?" | 1 Sí (7,735), 2 No (1,070) |
| `h0406` | "H0406 ¿(USTED/NOMBRE) fue atendido por esa necesidad de salud en alguna institución de salud (pública o privada) o con algún practicante tradicional?" | 1 Sí (7,645), 2 No (90) |

**Reasons did not SEEK care — `H0405A`/`H0405B`/`H0405C`** (up to 3 mentions), "H0405 ¿Por qué motivo (USTED/NOMBRE) no buscó atención?":

| Code | Reason (verbatim) |
|---|---|
| 1 | Decidió que no era necesario buscar atención porque no era tan grave |
| 2 | No hay dónde atenderse |
| 3 | Está muy lejos el lugar más cercano donde se brinda atención |
| **4** | **Es caro / No tenía dinero** ← COST (single merged code in 2024) |
| 5 | No había servicio en el horario en que lo necesitaba |
| 6 | No tuvo tiempo |
| 7 | No tuvo quién lo(a) llevara o acompañara |
| 8 | Quien brinda la atención no me inspira confianza / no es amable |
| 9 | Los trámites son muy tardados |
| 10 | El tiempo de espera para pasar a consulta, por lo común, es muy largo |
| 11 | Miedo a contraer COVID-19/miedo a salir de casa |
| 12 | Me programaron la cita |
| 13 / 99 | Otro / No sabe |

**Reasons sought but NOT attended — `H0407A`/`H0407B`/`H0407C`**, "H0407 ¿Por qué motivo (USTED/NOMBRE) no fue atendido(a)?": 1 unidad cerrada, 2 seguro no cubría, 3 horario, 4 sin equipo, 5 rechazado por no ser derechohabiente, 6 pase de referencia, 7 no alcanzó ficha/mucha gente, **8 "No sabía que tenía que pagar por la atención y/o los medicamentos"**, **9 "No podía cubrir el costo total de la atención"** ← COST, 10 trámites, 11 espera larga, 12 prestador pensó que no era necesario, 13 no urgente, 14 solo COVID, 15 reprogramación de cita, 16 Otro, 99 NS.

Bypass-of-entitlement diagnostics (utilizadores file): `u0202ca/cb/cc` "¿Por qué motivos no se atendió en el lugar que le correspondía ir por su derechohabiencia?" — code **7 "Me hacen pagar consultas, medicamentos, laboratorios, otros"**; parallel `u0202c1a-c` for SSA facilities, and `u0202da-dc` / `u0202d1a-c` "¿Qué tendría que cumplirse para que acudiera…?" (code 7 = "Si no tuviera que pagar consultas, medicamentos, laboratorios u otros").

## 4. Utilization, service type, motive

**Motive / need — `h0402`** (integrantes; copied into utilizadores as `enf_hog`). Labeled codes in catalog (all codes appearing in data are labeled; the fine 01–51 questionnaire list was partly recoded to 52–59 buckets):

| Code | Label (verbatim) |
|---|---|
| 1 | 01 Infecciones respiratorias (gripe, catarro, dolor de garganta, sinusitis, amigdalitis) |
| 2 | 02 Diarrea o empacho (infección estomacal o intestinal por alguna bacteria o virus) |
| 15 | 15 COVID-19 (coronavirus) |
| 16 | 16 Control, seguimiento o diagnóstico de diabetes (azúcar alta) |
| 17 | 17 Control, seguimiento o diagnóstico de hipertensión arterial (presión alta) |
| 20 | 20 Gastritis, úlcera gástrica o duodenitis (reflujo) |
| 27 | 27 Cáncer o tumores |
| **28** | **28 Vacunación** ← preventive |
| **30** | **30 Chequeo o consulta médica** ← preventive check-up |
| **32** | **32 Control prenatal (embarazo)** ← preventive |
| 38 | 38 Lesión física por accidente, vehícular (fracturas, golpes, etc.) |
| 40 / 41 | 40 Dolor de cabeza / 41 Fiebre |
| 44 | 44 Dolor de músculos, huesos y/o articulaciones |
| 45 | 45 Dolor de nervios (hernia lumbar, ciática, …, herpes zóster, etc.) |
| 46 | 46 cirugía u operación de cualquier órgano o parte del cuerpo |
| 47 / 48 / 50 | 47 Depresión / 48 Ansiedad / 50 Estrés |
| 52 | 52 Otra causa no enlistada en las anteriores (especifica) |
| 53–59 | Otro-especifica buckets: 53 INFECCIONES AGUDAS, 54 ENFERMEDADES CRÓNICAS, **55 PREVENCIÓN**, 56 EVENTOS AGUDOS NO INFECCIOSOS, 57 DOLOR CRÓNICO O AGUDO, 58 CIRUGÍAS, 59 SALUD MENTAL |
| 99 | 99 No sabe |

Preventive classification 2024: codes **28, 30, 32, 55** (vs curative rest). The 2024 need concept is explicitly broader than 2018: h0309 instructs "Considere como necesidad de salud, además de enfermedades y lesiones, el malestar psicológico, consultas programadas, servicios de medicina preventiva."

**Provider / institution**: `h0408` (integrantes) "¿En qué institución de salud (USTED/NOMBRE) se atendió/solicitó ser atendido(a)?" and `u0201` (utilizadores) "¿En qué institución de salud (USTED/NOMBRE) se atendió/recibió atención?" — same 26-code list as `h0309` (12 = pharmacy-adjacent consultorio; 13–18 private; 26 IMSS-BIENESTAR). Utilizadores also carries `instut` (institution reported in the household interview) and `uh0310_m` (insurance from household interview).

**Level of care**: `H0409A`–`H0409D` "H0409 ¿La atención que buscó (USTED/NOMBRE) requirió..." — 1 "ir a consulta externa?", 2 "hospitalización (internamiento)?", 3 "ir a consulta de urgencias?", 4 "Otros (vía remota, domicilio, etc.)".

**Choice of place**: `U0202UA/UB/UC` "¿Por qué motivos se atendió en este lugar?" — 1 Tiene afiliación, 2 Está cerca, **3 Es barato/No cuesta**, 4 horario amplio, 5 sin cita, 6 cita rápida, 7 ofrece el servicio, 8 fácil agendar, 9 No tuve otra opción, 10 atienden rápido, 11 le gusta la atención, 12 ya tenía cita, 13 conoce al prestador, 14 publicidad, 15 recomendación, 16 Otro, 17 NS/NR.

## 5. Health status and chronic conditions (adultos_ensanut2024_w.dta; verified against .dta labels)

| Variable | Label (verbatim, from .dta) | Codes (from .dta value labels) |
|---|---|---|
| `a0301` | "¿Algún médico le ha dicho que tiene diabetes (o alta el azúcar en la sangre)?" | 1 "SÍ." (n=1,613), 2 "Sí, durante el embarazo (solo mujeres, diabetes gestacional)." (20), 3 "NO." (11,291) |
| `a0301a` | "3.A ¿Algún médico le ha dicho que tiene/tuvo prediabetes?" | 1 Sí, 2 No, 9 NS/NR |
| `a0302` | age at diabetes diagnosis | |
| `a0401` | "¿Algún médico le ha dicho que tiene la presión alta?" | 1 "SÍ." (2,513), **2 "SÍ, durante el embarazo."** (57), 3 "NO." (10,354) — note 3-code scheme, unlike 2018 |
| `a0404` | "¿Actualmente toma alguna medicina (pastillas) para controlar su presión alta?" | |
| `a0211`–`a0217` | CESD-7 depression items ("Durante la última semana...") | |
| `a0205` | "2.5 ¿Le hicieron un diagnóstico de depresión mediante valoración clínica…?" | |

Chronic-condition OOP inside adultos 2024 (bonus): `a0310a` "Normalmente, ¿cuánto paga por sus pastillas y/o tratamiento de insulina para controlar su diabetes en un mes?", `a03061c` "¿Cuánto pagó la última vez que estuvo hospitalizado(a) debido a su diabetes?", `a0404a` "¿Cuánto gasta usualmente por sus pastillas para controlar su presión alta un mes?", `a0406b` "¿Cuánto pagó la última vez que acudió al médico para controlar su hipertensión?".

**No general self-rated health item found in adultos 2024 either** (searched "su salud", "excelente", "estado de salud"; only memory-comparison `A1502` and accident/violence items exist). See Gaps.

## 6. Socioeconomic position (2024)

**NSE files** (one row per household / per person, 100% linkable on FOLIO_I / FOLIO_INT):

| Variable | Label (verbatim) | Codes |
|---|---|---|
| `indice1` | "Índice de bienestar (1er CP)" | continuous first-principal-component score (**comma decimal in CSV**) |
| `nseF` | "Condición de bienestar (terciles)" | 1 T1, 2 T2, 3 T3 |
| `nse5F` | "Condición de bienestar (quintiles)" | 1 Q1 … 5 Q5 |

Also in hogar_ensanut2024_w_ICB: `h0327` "H0327 Aproximadamente, ¿Cuánto dinero ganan regularmente todos los miembros del hogar al mes?" — 1 "1- 5,999 pesos", 2 "6,000-9,999", 3 "10,000-13,999", 4 "14,000-21,999", 5 "22,000 o más pesos", 6 No percibieron ingresos, 8 No quiso responder, 9 No sabe. Assets `h0501a`–`h0501y` ("¿Usted o algún integrante de su hogar tiene televisión?" etc.), dwelling materials/services `h0101`–`h0125`, food insecurity (ELCSA) `h0701`–`h0716`, water insecurity (ICB block) `h0801`–`h08b05`. Opinion of public system: `h308a` "el Sistema de Salud Público atiende las necesidades de salud de todos los mexicanos… de manera efectiva" (1 Muy de acuerdo … 5 Muy en desacuerdo).

## 7. Out-of-pocket per-event amounts (utilizadores_ensanut2024_w)

| Variable | Label (verbatim) | Notes |
|---|---|---|
| `u0203` | "U0203 En total, ¿cuánto gastó en transporte para llegar al sitio en que le atendieron?" | |
| `u0207` / `u0208` | "U0207 ¿Le cobraron por la atención que recibió?" (1 Si, 2 No, 9 NS/NR) / "U0208 ¿Cuánto le cobraron?" | consultation fee |
| `u0301` / `u0303` | medicines prescribed / "U0303 ¿Consiguió todos los medicamentos?" (1 Sí todos, 2 No ninguno, 3 Sólo algunos, 9 NS/NR) | |
| `u0306` | "U0306 ¿Cuánto pagó por los medicamentos que consiguió?" | |
| `u0401` / `u0402` / `u0405` | labs/imaging requested / done / "U0405 ¿Cuánto pagó por los exámenes de laboratorio o gabinete que se realizó?" | |
| `u0406` / `u0407a`–`u0407c` | other expenses yes/no / "¿En qué y cuánto gastó?" A. Otros gastos médicos, B. Comida/hospedaje, C. Otros gastos | |

`U0304A`–`U0304E1` where medicines were obtained (1 mismo lugar de la consulta, 2 otra unidad misma institución, **3 farmacia particular**, 4 otra institución, 5 otro).

---

# Comparability notes 2018 → 2024

1. **Recall windows differ**: 2018 roster forgone-care block = problem in last month / last two weeks; 2018 utilizadores = care sought in last two weeks (plus 12-month P8_1 cost battery). 2024 = health *need* in last 3 months (h0401), with h0403 flagging the 2-week subset.
2. **Need concept differs**: 2018 conditions on illness/injury/control; 2024 explicitly includes preventive and scheduled care ("consultas programadas, servicios de medicina preventiva") and lists Vacunación/Chequeo/Control prenatal as motives. Preventive share is only measurable cleanly in 2024 (or via the separate 2018 adultos P10 preventive-module block).
3. **Cost-reason coding**: 2018 separates "Es caro" from "No tenía dinero" (P4_9_12 vs P4_9_13; P2_1 codes 02 vs 03); 2024 merges them into a single code 4 "Es caro / No tenía dinero" (H0405). For denial-of-care, 2018 P3_2 codes 02/10 map to 2024 H0407 codes 9/8.
4. **Insurance categories**: Seguro Popular (2018 P3_10_07) has no 2024 counterpart; 2024 adds IMSS-BIENESTAR (code 11) and drops ISSSTE-Estatal as a separate code (merged into 2). "None" is P3_10_11 (dummy) in 2018 vs code 10 in H0310A in 2024.
5. **Reasons format**: 2018 roster reasons are 0/1 dummies (multi-response); 2024 are up-to-3 coded mentions (H0405A/B/C etc.). 2018 utilizadores P2_1 is single-response.
6. **Hypertension item**: 2024 `a0401` adds code 2 "SÍ, durante el embarazo." — 2018 `P4_1` was binary. Diabetes item has the gestational code in both waves.

# Gaps / not found

- **Self-rated general health (excellent–poor)**: not found in either wave's shipped files (2018 CS_ADULTOS and 2024 adultos .dta were both searched; only post-visit change `P7_1` (2018 utilizadores) and memory comparison `A1502` (2024) exist). If SRH is needed, it must come from another module not shipped here.
- **2018 `ESTRATO` value labels**: catalog gives no labels; data contain 1–4 (INEGI's sociodemographic stratum low→high, by convention — unverified in the shipped codebooks).
- **2024 `F_SERSA`-style module-weight documentation**: the catalogs label each file's `ponde_f` only tersely; no note on calibration population. Same for 2018 `F_SERSA` whose catalog label reads "Factor de la Vivienda" (almost certainly a mislabel; treat it as the utilizadores weight).
- **2024 h0402 fine condition list**: questionnaire codes 3–14, 18–19, 21–26, 29, 31, 33–37, 39, 42–43, 49, 51 do not occur in the data or catalog — they were recoded into buckets 52–59. The full original wording is in `5 VFINAL Cuestionario utilizadores ENSANUT 2024_ETIQUETAS.Cuestionarios.pdf` (not machine-parsed here).
- **2024 household health-expenditure block**: the 2018 CS_HOGARES P7_2 (3-month household health spending) has no counterpart in hogar_ensanut2024_w_ICB (its extra blocks are food security, water insecurity, willingness-to-pay for water). Per-event OOP in 2024 comes only from the utilizadores file and the chronic-disease items in adultos.
- **2024 12-month cost-barrier battery**: the 2018 P8_1_1–P8_1_5 (Commonwealth-style "debido al costo") battery does not appear in the 2024 utilizadores catalog.
- **Weights for NSE files**: NSE files carry no weight; merge them onto hogar/integrantes and use those files' `ponde_f`.
