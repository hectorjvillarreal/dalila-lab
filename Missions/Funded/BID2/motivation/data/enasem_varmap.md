# ENASEM 2018 / 2021 / 2024 — Variable map for the BID2 panel (health, OOP spending, wealth, mortality, 50+)

**Prepared:** 2026-08-08. Every variable below was verified against the shipped
`diccionario_de_datos` CSVs and `catalogos` under
`~/Dalila/Missions/Funded/BID2/motivation/data/enasem/{2018,2021,2024}/`.
Nothing is quoted from memory of MHAS documentation.

## 0. File layout (verified row/column counts)

Each table folder contains `conjunto_de_datos/` (data csv), `catalogos/` (one code-list csv
per categorical variable, named `<var>.csv`), `diccionario_de_datos/`, `metadatos/`.

| Wave | Table (folder under wave dir) | Content | Rows | Cols |
|---|---|---|---|---|
| 2018 | `conjunto_de_datos_sect_a_c_d_f_e_pc_h_i_enasem_2018` | Individual sections A,C,D,F,E,PC,H,I | 17,114 | 960 |
| 2018 | `conjunto_de_datos_sect_g_j_k_sa_enasem_2018` | Household sections G,J,K,(SA widowhood) | 11,401 | 545 |
| 2018 | `conjunto_de_datos_MHAS_ENASEM_2018_variables_creadas_enasem_2018` | Constructed (MHAS-style) | 17,114 | 144 |
| 2018 | `conjunto_de_datos_archivo_maestro_seguimiento_enasem_2018` | Master follow-up 2001–2018 | 28,303 | 105 |
| 2018 | `conjunto_de_datos_sect_sa_sb_sc_sd_se_sh_si_enasem_2018` (+ `sect_sg_sj`) | Next-of-kin deceased interview | — | 226 (+40) |
| 2021 | `conjunto_de_datos_sect_a_c_d_e_pc_f_h_i_2021_enasem_2021` | Individual sections | 15,739* | 986 |
| 2021 | `conjunto_de_datos_sect_g_j_k_sa_2021_enasem_2021` | Household sections | — | 524 |
| 2021 | `conjunto_de_datos_mhas_enasem_2021_constructed_variables_creadas_enasem_2021` | Constructed | 15,739 | 121 |
| 2021 | `conjunto_de_datos_master_follow_up_file_2021_enasem_2021` | Master follow-up 2001–2021 | 28,483 | 127 |
| 2021 | `conjunto_de_datos_sect_sa_sb_sc_sd_se_sh_si_2021_enasem_2021` (+ `sect_sg_sj_2021`) | Deceased interview | — | 224 (+39) |
| 2024 | `conjunto_de_datos_tr_enasem24_sect_a_c_d_e_pc_f_h_i_enasem_2024` | Individual sections | 21,090 | 1,038 |
| 2024 | `conjunto_de_datos_tr_enasem24_sect_g_j_k_enasem_2024` | Household sections | 14,076 | 507 |
| 2024 | `conjunto_de_datos_mhas_enasem_2024_constructed_variables_creadas_enasem_2024` | Constructed | 21,090 | 132 |
| 2024 | `conjunto_de_datos_tr_enasem24_master_follow_up_file_enasem_2024` | Master follow-up 2001–2024 | 37,560 | 176 |
| 2024 | `conjunto_de_datos_tr_enasem24_sect_sa_sb_sc_sd_se_sh_si_enasem_2024` | Deceased interview (incl. SG/SJ) | — | 225 |

\* constructed-file row count; individual-section file has the same respondents.

Naming convention: raw questionnaire variables carry a wave suffix (`c4_18`, `c4_21`, `c4_24`);
**stems are identical across the three waves** for every variable checked (sections C, D, H, J, K).
2021 had **no refresher sample** (only follow-up tables exist); 2024 added a new sample
(`new_sample` tables, cunicah up to 26219).

## 1. IDs, linking, vital status

### Linking scheme
- **Household id:** `cunicah` (= `unhhid`), 5-digit, **constant across all waves since 2001**.
- **Person number:** `np` (3-digit; 010/020 = selected person and spouse; up to 044/060/064).
- **Person key = `cunicah` + `np`** (also shipped pre-concatenated as string `unhhidnp` in the
  master files and the 2018/2024 deceased files). This pair identifies the same person in every
  table of every wave. `subhog_01…subhog_24` handle household splits (subhousehold codes);
  keep them when a household splits between waves.
- The one-row-per-person spine is the **2024 master follow-up file**
  (`.../2024/conjunto_de_datos_tr_enasem24_master_follow_up_file_enasem_2024/conjunto_de_datos/…csv`,
  37,560 rows, one row per person ever sampled 2001–2024) — it contains, per wave `ww` ∈
  {01,03,12,15,18,21,24}: `elegible_ww`, `new_sample_ww`, `tipent_ww`, `tipne_ww`,
  `reason_proxy_ww`, `int_date_ww`, `fallecido_ww`, `age_ww`, `sex_ww`, `factori_ww`,
  `factorh_ww`, `tam_loc_ww`, plus `est_dis_21/24`, `upm_dis_21/24`, and `yrschool`.

### Vital status (verified catalog codes)
| Variable | File | Codes |
|---|---|---|
| `fallecido_18` | master 2018/2021/2024 | 0/1 = "Murió entre 2015 y 2018" |
| `fallecido_21` | master 2021 and 2024 | 0 = Vivo en 2021; 1 = Fallecido(a) en Mex-Cog 2021 (Jul–Ago); 2 = Fallecido(a) en ENASEM 2021 (Nov 21–Ene 22) |
| `fallecido_24` | master 2024 | 0 = Vivo(a) en 2024; 1 = Fallecido(a) en MHAS 2024 |
| `tipent_ww` | master + section files | 1 dir. seguimiento / 2 dir. nueva muestra / 3 sust. seguimiento / 4 sust. nueva muestra / **5 = Fallecido (entrevista sustituto)** |

### Date/cause of death (next-of-kin deceased interview, sect `sa_sb_sc_sd_se_sh_si`)
Identical stems in all three waves (`_18`/`_21`/`_24`):
| Variable | Label | Codes/range |
|---|---|---|
| `sa8_1_ww` / `sa8_2_ww` | Month / year of death | 01–12; year 2012–2018 (w18), 2015–2022 (w21), 2015–2024 (w24); 2088/2099 = NR/NS |
| `sa2_ww` | Age at death | ~038–115, 888, 999 |
| `sa4_ww`, `sa5_ww` | Died at home/hospital; locality | 1–3 / 1–5 |
| `sa6_ww`, `sa7_ww` | Cause type (illness/accident/…); main illness | 1–3; 1–6 (2018) → 01–09 (2021/24) |
| `sd5/sd8/sd10a/sd11a/sd12a/sd13a_ww` | End-of-life medical spending (see §6) | pesos + brackets |
The deceased file links by `cunicah`+`np` and carries its own `factori_ww`/`factorh_ww`.
2021/24 add `sa19a/sa20a/sa23a` (COVID-19 cause flags).

## 2. Survey design

| Concept | 2018 | 2021 | 2024 | File |
|---|---|---|---|---|
| Individual weight | `factori_18` (0–98,699) | `factori_21` (0–116,633) | `factori_24` (0–118,874) | constructed, master, and section files |
| Household weight | `factorh_18` (0–90,984) | `factorh_21` (0–98,872) | `factorh_24` (0–115,613) | idem |
| Stratum | `est_dis` (11–324) | `est_dis_21` (1–4) | `est_dis_24` (1–4) | constructed + master(21/24) + section files |
| PSU | `upm_dis` (17001–32208832) | `upm_dis_21` (1–12,514) | `upm_dis_24` (1–16,146) | idem |
| Urban/rural | `urbano_18` / `tam_loc_18` | `urbano_21` / `tam_loc_21` | `urbano_24` / `tam_loc_24` | constructed / master |

**Caution (verified ranges):** the 2018 design variables are named without suffix
(`est_dis`, `upm_dis`) and are on a **different coding scheme** than the 2021/2024
`est_dis_ww` (1–4) / `upm_dis_ww`. For a 2018-baseline panel, take the design pair from the
2018 constructed file; do not mix with the 21/24-suffixed pair without checking the survey
design notes. Deceased-interview files carry their own weights (`factori_18` in the 2018
deceased file ranges 26–26,017, i.e., a separate weight series).

## 3. Demographics (constructed file — preferred)

| Concept | 2018 | 2021 | 2024 | Codes |
|---|---|---|---|---|
| Sex | `genero` | `genero` | `genero` | 1 Hombre, 2 Mujer (catalog verified) |
| Age (years) | `edad_18` (16–107) | `edad_21` (23–106,888,999) | `edad_24` (18–107) | continuous; `edad_gru_ww` grouped |
| Education (years) | `educacion` (00–22) | `educacion` | `educacion` | `edu_gru` grouped 0–4; master 2024 also has `yrschool` |
| Marital status | `est_conyugal_18` | `est_conyugal_21` | `est_conyugal_24` | 1–4 |
| Locality size | `urbano_18` | `urbano_21` | `urbano_24` | 0/1 |
Master files add `age_ww`, `sex_ww` (1 = male) per wave, and birth month/year (`mes_03`, `a_o_03`).

## 4. Health deficits for the 21-item Searle-convention frailty index

**All five categories are covered by pre-constructed 0/1 deficits in the `variables_creadas`
files, with identical stems in the three waves** (suffix `_18`/`_21`/`_24`). Raw source items
(individual-sections file) are listed for auditing; raw stems are also identical across waves.

### (a) ADLs — constructed `abvd_*` (0/1 difficulty)
| Constructed | Label | Raw difficulty item | Raw "someone helps" item |
|---|---|---|---|
| `abvd_caminar_ww` | Difficulty walking across a room | `h15a_ww` | `h15d_ww` |
| `abvd_banar_ww` | Difficulty bathing (tub/shower) | `h16a_ww` | `h16d_ww` |
| `abvd_comer_ww` | Difficulty eating (e.g., cutting food) | `h17a_ww` | `h17d_ww` |
| `abvd_cama_ww` | Difficulty getting in/out of bed | `h18a_ww` | `h18d_ww` |
| `abvd_bano_ww` | Difficulty using the toilet | `h19a_ww` | `h19d_ww` |
| `abvd_vestirse_ww` | Difficulty dressing (6th ADL, available if wanted) | `h13_ww` | `h14_ww` |
| `n_abvd_ww` | ADL count 0–5 | | |
Raw H codes: 1 Sí, 2 No, 6 NO PUEDE, 7 NO LO HACE, 8 NR, 9 NS (catalog `h1_18` verified).
Constructed items are already 0/1. Note the coauthor's "walking" item maps to
*walking across a room* (`h15a`); broader mobility (several blocks) is `h1_ww`, one block `h3_ww`.

### (b) IADLs — constructed `aivd_*` (0/1)
| Constructed | Label | Raw difficulty | Raw help |
|---|---|---|---|
| `aivd_comidas_ww` | Preparing a hot meal | `h26a_ww` | `h26c_ww` |
| `aivd_comprar_ww` | Shopping for groceries | `h27a_ww` | `h27c_ww` |
| `aivd_medicina_ww` | Taking medications | `h28a_ww` | `h28c_ww` |
| `aivd_dinero_ww` | Managing money | `h29a_ww` | `h29c_ww` |
| `n_aivd_ww` | IADL count 0–4 | | |

### (c) Mental / cognitive
| Constructed | Label | Raw |
|---|---|---|
| `deprimido_ww`, `esfuerzo_ww`, `intranquilo_ww`, `feliz_ww`, `solo_ww`, `disf_vida_ww`, `triste_ww`, `cansado_ww`, `energia_ww` | 9 CES-D items, past week, 0/1 (positive items already handled in the score) | `c49_1_ww` … `c49_9_ww` (1 Sí / 2 No / 8 / 9) |
| `n_sint_depr_ww` | CES-D symptom count 0–9 | |
| `cesd_deprimido_ww` | 0/1: 5+ symptoms | |
| `memoria_ww` | Self-reported memory, 1–5 | `e1a_ww` (excellent…poor); `e1b_ww` vs 2 yrs ago |

### (d) Diagnosed conditions — constructed 0/1 ("ever told by a doctor")
| Constructed | Condition | Raw item |
|---|---|---|
| `hipertension_ww` | Hypertension | `c4_ww` |
| `diabetes_ww` | Diabetes | `c6_ww` |
| `cancer_ww` | Cancer | `c12_ww` |
| `enf_pulm_ww` | Respiratory disease (asthma/emphysema) | `c19_ww` |
| `infarto_ww` | Heart attack | `c22a_ww` |
| `prob_card_ww` | Heart problem (failure/arrhythmia/angina) | `c25b_ww` (and `c23` meds) |
| `embolia_ww` | Stroke (embolia/derrame/TIA) | `c26_ww` |
| `artritis_ww` | Arthritis/rheumatism | `c32_ww` |
| `n_enf_ww` | Disease count 0–6 (labelled "0–7") | |
Raw C codes: 1 Sí, 2 No, 8 NR, 9 NS. Diagnosis years available (`c18_1/2`, `c22b1/2`, `c30_1/2`).

### (e) Behaviors / anthropometrics
| Constructed | Label | Raw |
|---|---|---|
| `imc_cat_ww` | BMI in 5 categories (1–5; category 5 = highest) — obesity flag derivable | self-reported weight `c66_ww` (kilos 030–175) and height `c67_1_ww`/`c67_2_ww` |
| `tabaco_ww` | Currently smokes, 0/1 | `c51_ww` ever smoked; `c54_ww` smokes now; intensity `c55`–`c57` |
| `alcohol_ww`, `ejer_3_por_sem_ww` | extra behaviors if needed | `c50b_ww` exercise |

**Verdict:** all 21 items (5 ADL + 4 IADL + 2 mental [CES-D battery + memory] + 7–8 conditions +
obesity + current smoking) are constructible **in all three waves from the constructed files
alone**, with identical stems — only the wave suffix changes. The BMI category boundaries for
"obese" (`imc_cat_ww` = which category) should be confirmed once against MHAS constructed-file
documentation before publication (the shipped dictionary gives only "5 categorías").

## 5. Self-reported global health

| Wave | Constructed | Raw | Codes (catalog verified) |
|---|---|---|---|
| all | `salud_glob_ww` (1–5) | `c1_ww` | 1 excelente, 2 muy buena, 3 buena, 4 regular, 5 mala; 8 NR, 9 NS |
Also `c2a_ww` (vs two years ago), `c3a_ww` (vs peers).

## 6. Out-of-pocket health spending — Section D, individual-sections file

Location: `sect_a_c_d_f_e_pc_h_i` (2018) / `sect_a_c_d_e_pc_f_h_i` (2021, 2024), same stems.

| Variable | Content | Range/codes |
|---|---|---|
| `d4_ww` | Hospital nights, last year (count) | 000–200, 888, 999 |
| `d6_ww` | **Amount paid for hospitalizations, last year (pesos)** | 0–350,000/800,000/700,000; 888888 NR; 999999 NS |
| `d7a/b/c_ww` | Unfolding brackets if d6 missing (> $7,500 / $4,000 / $30,000) | 1,2,9 |
| `d8_1_ww` | Dentist visits, last year (count) | |
| `d8_2_ww` | Outpatient surgical procedures, last year (count) | |
| `d8_3_ww` | Doctor/medical-personnel visits, last year (count) | 000–365 |
| `d9_1/2/3_ww` | **Amount paid (cash or in kind) for dentist / outpatient procedures / doctor visits** | 0–600,000; **777777 = paid in kind**; 888888; 999999 |
| `d10a/b/c{1,2,3}_ww` | Brackets for each (> $2,000 / $400 / $15,000) | 1,2,9 |
| `d12a_ww` | **Monthly medication spending, normal month, last year (pesos)** | 0–100,000/350,000; 777777; 888888; 999999 |
| `d12b_a/b/c_ww` | Medication brackets (> $400 / $200 / $2,000) | 1,2,9 |
| `d12c_ww` | Skipped a needed medicine due to cost | 1,2,8,9 |
| `d13_ww` | **Who mainly paid the medical expenses** | 01 hijo(a), 02 yerno/nuera, 03 nieto(a), 04 padre/madre, 05 otro pariente, 06 otra persona, **07 entrevistado y/o cónyuge**, **08 no tuvo gastos**, 88, 99 (catalog verified) |
| `d15_ww`, `d16a-e(+f-h in 21/24)_ww` | Forwent care for a serious problem; reasons | |
| `d5_01…d5_99_ww`, `d10d*_ww`, `d17/d18_*` | Provider type used / would use (IMSS, ISSSTE, SSA, Pemex-Def-Mar, private, pharmacy…) | 0/1 dummies |
Constructed 0/1 utilization: `hospitalizacion_ww`, `visita_medica_ww`, `ciru_ambu_ww`, `visita_dental_ww`.

**Insurance-paid distinction:** there is **no per-service "insurance paid X" variable** in
section D. The amounts in d6/d9/d12a are what was paid by the respondent/household ("¿cuánto
pagó…?"), with `d13` identifying the payer person (no insurer category). An explicit
"covered by insurance" question exists only for funeral costs (`k113_ww`, spouse's death;
`sj8_ww`, deceased interview). End-of-life medical OOP for decedents: `sd5` (hospitalizations),
`sd8` (other services), `sd10a` (monthly meds), `sd11a` (who paid), `sd12a-c` / `sd13a-c`
(total medical / non-medical brackets, > $6,000 / $3,000 / $24,000) in the deceased file.

## 7. Insurance coverage

Preferred: constructed 0/1 dummies (all waves):

| 2018 | 2021 | 2024 |
|---|---|---|
| `imss_18` | `imss_21` | `imss_24` |
| `issste_18` | `issste_21` | `issste_24` |
| `seg_pop_18` (Seguro Popular) | **`insabi_21`** | **`imss_bienestar_24`** |
| `pem_def_mar_18` | `pem_def_mar_21` | `pem_def_mar_24` |
| `seguro_privado_18` | `seguro_privado_21` | `seguro_privado_24` |
| `otro_seguro_18` | `otro_seguro_21` | `otro_seguro_24` |
| `seguro_medico_18` (any) | `seguro_medico_21` | `seguro_medico_24` (+ `seguro_int_pub_24`) |

**Rename to note:** the public-insurance third pillar changes name with the policy regime:
Seguro Popular (2018) → INSABI (2021) → IMSS-Bienestar (2024). Treat as one "public
non-contributory" category for the panel.

Raw: battery `d1_1_ww` … `d1_6_ww` (+ `d1_7_24` in 2024) "¿Tiene derecho a servicio médico
en…?" (1 Sí/2 No/8/9) with `d1d_x` (since when) and `d2_x` (entitlement reason). The shipped
dictionaries do **not** spell out which institution each position x refers to (catalogs are
generic Sí/No) — use the constructed dummies, which encode the mapping.

## 8. Wealth and income — sections J & K (household file `sect_g_j_k[_sa]`)

One record per household (link to persons via `cunicah` [+ `subhog_ww`]). Amounts in pesos;
888888…/999999… = NR/NS; most amounts have unfolding brackets nearby. **No constructed
net-worth aggregate is shipped in `variables_creadas`** — assemble from components
(same stems in all waves, suffix `_18`/`_21`/`_24`):

| Component | Value | Debt/other | Income flow |
|---|---|---|---|
| Main residence | `j31_ww` current value if sold | `j26_ww` monthly payment; `j28_ww` amount still owed; `j22_ww` deed holder | — |
| Second home | `j34_ww` net value if sold (`j33_ww` owns) | | |
| Business/farm (up to 2) | `k8_1_ww`, `k8_2_ww` sale value (`k1` owns; `k3` debts) | | `k11_x` monthly income, `k13_x` expenses, `k15_x` profit |
| Other real estate | `k24_1_ww` sale value (`k17` owns; `k19` debts) | | `k27_1`, `k29_1` |
| Financial assets | `k33_1_ww` checking/savings/fixed-term; `k33_2_ww` loans made to third parties; `k33_3_ww` stocks/bonds (`k31a` owns) | | `k35_1` generated income |
| Vehicles | `k42_ww` sale value (`k39` debts) | | |
| Other debts | — | `k85_ww` has debts; `k86_ww` total amount; `k87a/b/c` brackets (> $25k/$12k/$90k) | |
| Household spending | — | — | `k88_ww` total monthly household spending (+ `k89a/b/c` brackets, 2018) |

Income (section K, same file): pensions — respondent `k58a–d_ww` (retirement, widowhood,
disability, other) with source `k59_*`, start year `k60_*`, amount brackets `k68*`;
spouse `k64c–f_ww`/`k65_*`/`k66_*`/`k68*`; expected pensions `k70–k77`; bonus income
`k48/k51/k54/k57`; asset sales/inheritance `k79c`, `k82e`. Widowhood-shock module:
`k100–k104` (pension change at spouse's death), `k111–k114` (funeral costs, insurance
coverage `k113`, distress financing `k114_1–5`). Individual labor income is in section I
(individual file; benefits incl. private medical insurance `i12_6_ww`, `i25a6_ww`).
Deceased's estate: `sj2/sj3_24` (home ownership at death, what happened to it), `sj6/sj8`
(funeral expenses, insurance).

## 9. Constructed-variables inventory (`variables_creadas`)

144 vars (2018) / 121 (2021) / 132 (2024); identical stems except wave-specific additions.
Groups (all with `_ww` suffix unless noted):

- **IDs/design:** `cunicah`, `np`, `subhog_*`, `tipent`, `new_sample`, `factori`, `factorh`, `est_dis(_ww)`, `upm_dis(_ww)`
- **Demographics:** `genero`, `edad`, `edad_gru`, `urbano`, `educacion`, `edu_gru`, `est_conyugal`, `n_uniones`, `n_hijos_vivos`, `migracion`, `ocupacion` (employment status 1–4)
- **Health:** `salud_glob`; ADLs `abvd_*` + `n_abvd`; IADLs `aivd_*` + `n_aivd`; CES-D 9 items + `n_sint_depr` + `cesd_deprimido`; 8 disease dummies + `n_enf`/`enf_cat`; `imc_cat`; `memoria`; `dormido` (sleep)
- **Behaviors/prevention:** `tabaco`, `alcohol`, `ejer_3_por_sem`, screening/vaccination dummies (`prueba_*`, `vacu_*`, `papanic`, `mamografia`, `exam_prostata`; `vacu_covid` in 21/24)
- **Utilization:** `hospitalizacion`, `visita_medica`, `ciru_ambu`, `visita_dental`
- **Insurance:** see §7
- **Psychosocial:** life-satisfaction (`vida_ideal`…`no_cambio`), loneliness (`falta_compa`, `ignorado`, `aislado`), decision-making (`peso_decis_*`), time-use dummies
- **Housing/durables (2018 only):** wall/roof/floor materials, services, 8 durable-goods dummies, `n_dura_hog`, tenure — a 2018-only asset-index option; **not repeated in 2021/2024 constructed files**
- **Family/help:** `arreglos_res_18`, `contacto_con_hijos_18`, `ayuda_a_hijos_18`, `ayuda_de_hijos_18` (2018 only)
- **Wave-specific:** 2021 COVID block (`covid_21`, `covid_hosp_21`, `covid_cons_21`, `covid_estres_21`, `fall_hijos_21`, `perdida_fin_21`); 2024 early-life (`fam_econ_24`, `fam_alcohol_24`), language, discrimination block, `fall_hijos_24`, `perdida_fin_24`
- **NOT included:** any wealth/net-worth or income aggregate, and no OOP-spending aggregate (see §6, §8)

## 10. Gaps and cautions

1. **No constructed net worth / income / OOP totals** anywhere in the shipped packages —
   must be built from J/K and D raw items (unfolding brackets → interval imputation needed
   for the many NR/NS amounts).
2. **Insurance-paid split for medical OOP does not exist** at service level; only `d13`
   (payer person, no insurer code) and funeral-cost insurance (`k113`, `sj8`).
3. **d1_x institution mapping** is positional and not documented in the shipped dictionaries;
   use constructed insurance dummies.
4. **2018 vs 2021/2024 design variables differ** (`est_dis` 11–324 & fine `upm_dis` vs
   `est_dis_21/24` 1–4); confirm which design the pooled panel should use before variance
   estimation.
5. **`fallecido_21` conflates two 2021 fieldworks** (Mex-Cog Jul–Aug vs ENASEM Nov–Jan);
   codes 1 and 2 both mean died 2018–2021, but reference dates differ; 2021 interview dates
   run 10/01/2021–04/02/2022 (`int_date_21`), 2024: 06/10/2024–30/01/2025.
6. **Weight/height are self-reported** (`c66`, `c67_*`); `imc_cat_ww` category
   bounds (which category = obese) not documented in the shipped dictionary — verify against
   MHAS constructed-file codebook.
7. **2021 has no refresher sample** and no "fallecidos nueva muestra" table; attrition
   2018→2021 also includes non-death non-response (`tipne_21`, codes 01–14).
8. **Household-level wealth (g_j_k) has no `np`** — merge to individuals on `cunicah`
   (+ subhousehold); the household informant is the selected respondent or spouse.
9. Spouse death year from the widowhood module (`sa18b`, `k111` block) and child deaths
   (`fall_hijos_21/24`) are available for shock analyses.
10. 2024 master adds GWAS/biomarker result fields (`res_gwas_*`, `res_apoe`, `res_ancestry`)
    and Mex-Cog 2021 fields — a person-level research-history spine beyond the survey core.
