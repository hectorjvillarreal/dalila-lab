# NUMBERS — Experimento 2

Registro de cifras del experimento 2 del anexo del Núcleo 13 (cuota del Infonavit a un nuevo seguro solidario de salud y cuidados en la vejez).
Regla 3.7: ninguna cifra aparece en el borrador del anexo si no está en este registro. Ejercicio de análisis de ITED; no es una proyección ni una propuesta del IMSS o del Gobierno.
Montos en millones de pesos de 2026 (mdp) salvo indicación. «Puntos del salario» = % de la masa salarial con tope de 25 UMA y 337 días.

## Experimento 2 — 1. Cifras semilla (instrucción, sección 6)

| Clave | Valor | Fuente | Estado |
|---|---|---|---|
| Infonavit_tasa | 5 % del SBC, tope 25 UMA | Ley del Infonavit, art. 29; Informe, nota 176 | 5 % confirmado en la nota 176; el tope se toma de la instrucción (la Ley no se consultó en esta corrida) |
| NS_tasa | 2 % del SBC, tope 25 UMA | Supuesto del experimento | — |
| GMP_V24_base | Ingresos 89,499 / 104,369 / 119,537 / 142,886 / 169,522 / 197,734 / 217,061; saldo −68,398 / −97,760 / −134,117 / −138,282 / −157,934 / −180,930 / −203,895 (2026, 2031, …, 2051 y año final); VP 2,750,260 y −2,631,460 | Informe, Cuadro V.24 (base) | confirmada celda por celda contra el PDF (verificación 3.2) |
| GMP_V19 | Saldo −97,653 (2031) y −135,137 (2036) frente a −97,760 y −134,117 del V.24; VP gasto 5,388,234, ingresos 2,750,887, saldo −2,637,347 | Informe, Cuadro V.19 | nueva; los dos cuadros del escenario base no coinciden exactamente |
| GMP_V20 | Aportaciones futuras 2,647,226 (1.50 % del VPSF); otros ingresos 103,662; reserva 46,532; prima de equilibrio 3.05 % | Informe, Cuadro V.20 | nueva |
| GMP_prima_fin / eq | 1.5 % / 3.1 % | Informe, Cuadro II.16 | confirmada (3.05 % en el Cuadro V.20) |
| Vol_salarios_VP_SEM | 176,481,700 mdp de 2026 | Informe, Cuadro V.15 (base) | confirmada |
| SEM_ingresos_V13 | 562,126 / 642,375 / 740,391 / 859,501 / 995,073 / 1,131,634 / 1,215,833 (2026, 2031, …, 2051 y año final); VP 16,456,453 | Informe, Cuadro V.13 | nueva; denominador de «% de los ingresos del SEM» (decisión de Héctor, 18-10) |
| Tasa_descuento | 3 % real | Informe, Cuadro II.16, nota 1 | confirmada |
| DH_65mas_2025 | 16.6 % de la población adscrita a médico familiar | Informe, Gráfica I.31 | confirmada |
| DH_total | 79,178,109 | Informe, Cuadro I.4 | confirmada |
| PAMF_2025 | 63,598,543 adscripciones a médico familiar (60,266,622 personas por CURP) | Informe, texto del Cuadro I.4 y Gráfica I.23 | nueva; base propia de la proporción de la Gráfica I.31 |
| Vivienda_al_pensionarse | 71.45 % (base) / 57.45 % (riesgo); 83 % en 2026-2035, baja a 50 % al final del horizonte (base) | Informe, Cuadro II.18 y nota 3 | confirmada |
| CyV_patronal_2025_2026_2030 | Tabla de la sección 1.5 de la instrucción | DOF 16-12-2020, Segundo Transitorio (tabla en imagen, leída) y art. 168 fr. II a) (texto); Informe, Cuadro A.3 nota 6 (2025) | verificada en el DOF: coincide en todas las celdas |
| Cuota_social_dic2025 | 1 SM 12.18; 1.01 SM-1.50 UMA 11.33; 1.51-2 10.48; 2.01-2.5 9.63; 2.51-3 8.78; 3.01-3.5 7.93; 3.51-4 7.08 pesos por día | Informe, Cuadro A.3, nota 8 | nueva; se mantiene constante en UMA reales (se indexa al INPC) |
| c_D2 | 3.467 % (0.0346703) | Corrida v1.2 | confirmada |
| SBC_prom_dic2025 | 5.55 veces la UMA (627.87 pesos/día) | Informe, sección I.1.3 | confirmada en la v1.2; nivel «promedio» de la tabla de cuña |
| Patronales SEM, SIV, SGPS, Retiro | Cuota fija 20.40 % UMA; excedente 1.10 %; prestaciones en dinero 0.70 %; GMP 1.05 %; IV 1.75 %; GPS 1.00 %; Retiro 2.00 % | Informe, Cuadro A.3; libro, hoja `Tasas de Contribución` | confirmada |
| RT_prima_promedio | 1.80 % | Libro, hoja `Tasas de Contribución`, nota 2 (promedio 2023-2025) | confirmada; el Informe, Cuadro A.3, reporta 1.9078 % (mar. 2025-feb. 2026). Se usa 1.80 como en la instrucción |
| Obreras y federales | Obrera: excedente 0.40, PD 0.25, GMP 0.375, IV 0.625, CyV 1.125; federal: cuota fija 14.83 % UMA, PD 0.05, GMP 0.075, IV 0.125 | Informe, Cuadro A.3 | nueva |
| Art_36_LSS | Con salario mínimo, el patrón cubre íntegramente la cuota de la persona trabajadora | Ley del Seguro Social, art. 36 | nueva; texto citado de fuentes secundarias (IMCP), no del DOF |
| Infonavit_recaudacion_efectiva | No obtenida | Estados financieros del Infonavit 2024-2025 | omitida, como manda la instrucción |

## Experimento 2 — 2. Cifras calculadas (generadas por `src/`, archivo `data/derived/numbers_computed.json`)

| Clave | Valor | Fuente / cálculo |
|---|---|---|
| CONAPO_65mas_2025 | 11,698,499 | CONAPO 2023, población de 65 años o más, 2025 |
| DH65_2025 | 13,143,566 | 0.166 × 79,178,109 |
| DH65_2027 | 14,295,992 | 0.166 × 79,178,109 × (CONAPO 65+ t / CONAPO 65+ 2025) |
| DH65_2030 | 16,182,171 | 0.166 × 79,178,109 × (CONAPO 65+ t / CONAPO 65+ 2025) |
| DH65_2040 | 23,340,899 | 0.166 × 79,178,109 × (CONAPO 65+ t / CONAPO 65+ 2025) |
| DH65_2054 | 33,012,741 | 0.166 × 79,178,109 × (CONAPO 65+ t / CONAPO 65+ 2025) |
| DH65_PAMF_2025 | 10,557,358 | 0.166 × 63,598,543 (adscripciones a médico familiar) |
| DH65_PAMF_2027 | 11,483,026 | 0.166 × 63,598,543 × crecimiento CONAPO 65+ |
| DH65_PAMF_2030 | 12,998,069 | 0.166 × 63,598,543 × crecimiento CONAPO 65+ |
| DH65_PAMF_2040 | 18,748,202 | 0.166 × 63,598,543 × crecimiento CONAPO 65+ |
| DH65_PAMF_2054 | 26,516,953 | 0.166 × 63,598,543 × crecimiento CONAPO 65+ |
| DH65_PAMF_entre_CONAPO65_2025 | 90.2 | DH65 con base PAMF / población nacional de 65+ (%) |
| DH65_entre_CONAPO65_2025 | 112.4 | DH65 (instrucción) / población nacional de 65+ (%) |
| DH80_2027 | 3,084,411 | DH65 × (CONAPO 80+ / CONAPO 65+) |
| DH80_2030 | 3,486,854 | DH65 × (CONAPO 80+ / CONAPO 65+) |
| DH80_2040 | 5,553,803 | DH65 × (CONAPO 80+ / CONAPO 65+) |
| DH80_2054 | 10,286,912 | DH65 × (CONAPO 80+ / CONAPO 65+) |
| DH80_PAMF_2027 | 2,477,504 | DH65_PAMF × CONAPO 80+/65+ |
| DH80_PAMF_2030 | 2,800,759 | DH65_PAMF × CONAPO 80+/65+ |
| DH80_PAMF_2040 | 4,461,003 | DH65_PAMF × CONAPO 80+/65+ |
| DH80_PAMF_2054 | 8,262,796 | DH65_PAMF × CONAPO 80+/65+ |
| GMP_deficit_2027 | 74,270 | Informe, Cuadro V.24 (base), interpolación lineal |
| GMP_deficit_2030 | 91,888 | Informe, Cuadro V.24 (base), interpolación lineal |
| GMP_deficit_2040 | 137,449 | Informe, Cuadro V.24 (base), interpolación lineal |
| GMP_deficit_2054 | 198,154 | Informe, Cuadro V.24 (base), interpolación lineal |
| GMP_prima_eq_exacta | 3.053 | 5,388,234 / 176,481,700 (Cuadros V.19 y V.15) |
| GMP_prima_fin_exacta | 1.5 | 2,647,226 / 176,481,700 (Cuadros V.20 y V.15) |
| M2_DH_total_k1_pesos_por_dh65_2027 | 2,340 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_DH_total_k1_pesos_por_dh65_2030 | 1,471 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_DH_total_k1_pesos_por_dh65_2040 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_DH_total_k1_pesos_por_dh65_2054 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_DH_total_k1_pesos_por_dh80_2027 | 10,847 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_DH_total_k1_pesos_por_dh80_2030 | 6,825 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_DH_total_k1_pesos_por_dh80_2040 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_DH_total_k1_pesos_por_dh80_2054 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_DH_total_k2_pesos_por_dh65_2027 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_DH_total_k2_pesos_por_dh65_2030 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_DH_total_k2_pesos_por_dh65_2040 | 391 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_DH_total_k2_pesos_por_dh65_2054 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_DH_total_k2_pesos_por_dh80_2027 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_DH_total_k2_pesos_por_dh80_2030 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_DH_total_k2_pesos_por_dh80_2040 | 1,644 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_DH_total_k2_pesos_por_dh80_2054 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_PAMF_k1_pesos_por_dh65_2027 | 2,914 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_PAMF_k1_pesos_por_dh65_2030 | 1,831 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_PAMF_k1_pesos_por_dh65_2040 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_PAMF_k1_pesos_por_dh65_2054 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_PAMF_k1_pesos_por_dh80_2027 | 13,504 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_PAMF_k1_pesos_por_dh80_2030 | 8,497 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_PAMF_k1_pesos_por_dh80_2040 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_PAMF_k1_pesos_por_dh80_2054 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_PAMF_k2_pesos_por_dh65_2027 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_PAMF_k2_pesos_por_dh65_2030 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_PAMF_k2_pesos_por_dh65_2040 | 487 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_PAMF_k2_pesos_por_dh65_2054 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_PAMF_k2_pesos_por_dh80_2027 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_PAMF_k2_pesos_por_dh80_2030 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_PAMF_k2_pesos_por_dh80_2040 | 2,047 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_PAMF_k2_pesos_por_dh80_2054 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_cubre_desde | 2,027 | Primer año con I ≥ D |
| M2_deficit_GMP_pts_2027 | 1.379 | Puntos del salario (masa con tope, 337 días) |
| M2_deficit_GMP_pts_2030 | 1.589 | Puntos del salario (masa con tope, 337 días) |
| M2_deficit_GMP_pts_2040 | 2.089 | Puntos del salario (masa con tope, 337 días) |
| M2_deficit_GMP_pts_2054 | 2.678 | Puntos del salario (masa con tope, 337 días) |
| M2_deficit_GMP_sem_2027 | 12.85 | % de los ingresos del SEM (Cuadro V.13) |
| M2_deficit_GMP_sem_2030 | 14.67 | % de los ingresos del SEM (Cuadro V.13) |
| M2_deficit_GMP_sem_2040 | 16.45 | % de los ingresos del SEM (Cuadro V.13) |
| M2_deficit_GMP_sem_2054 | 16.58 | % de los ingresos del SEM (Cuadro V.13) |
| M2_deja_de_cubrir | 2,035 | Primer año posterior a 2027 con I < D |
| M2_factor_2027 | 0.9849 | Formalidad implícita 2025 / formalidad implícita t (prueba C de la v1.2) |
| M2_factor_2030 | 0.9321 | Formalidad implícita 2025 / formalidad implícita t (prueba C de la v1.2) |
| M2_factor_2040 | 0.7384 | Formalidad implícita 2025 / formalidad implícita t (prueba C de la v1.2) |
| M2_factor_2054 | 0.5385 | Formalidad implícita 2025 / formalidad implícita t (prueba C de la v1.2) |
| M2_holgura_min | -50,155 | Mínimo de ingreso − déficit de GMP, 2027-2054 (mdp de 2026) |
| M2_holgura_min_anio | 2,054 | Año de la holgura mínima |
| M2_holgura_min_pts | -0.678 | Holgura mínima en puntos del salario |
| M2_infonavit_5pct_teorico_2027 | 269,317 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_infonavit_5pct_teorico_2030 | 289,215 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_infonavit_5pct_teorico_2040 | 328,927 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_infonavit_5pct_teorico_2054 | 369,998 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_ingreso_NS_2027 | 107,727 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_ingreso_NS_2030 | 115,686 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_ingreso_NS_2040 | 131,571 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_ingreso_NS_2054 | 147,999 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_ingreso_NS_pts_2027 | 2 | Puntos del salario (masa con tope, 337 días) |
| M2_ingreso_NS_pts_2030 | 2 | Puntos del salario (masa con tope, 337 días) |
| M2_ingreso_NS_pts_2040 | 2 | Puntos del salario (masa con tope, 337 días) |
| M2_ingreso_NS_pts_2054 | 2 | Puntos del salario (masa con tope, 337 días) |
| M2_ingreso_NS_sem_2027 | 18.63 | % de los ingresos del SEM (Cuadro V.13) |
| M2_ingreso_NS_sem_2030 | 18.47 | % de los ingresos del SEM (Cuadro V.13) |
| M2_ingreso_NS_sem_2040 | 15.74 | % de los ingresos del SEM (Cuadro V.13) |
| M2_ingreso_NS_sem_2054 | 12.39 | % de los ingresos del SEM (Cuadro V.13) |
| M2_k1_anios_no_cubre | 20 | Años 2027-2054 con I < D |
| M2_k1_deficit_no_cubierto_2027 | 0 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k1_deficit_no_cubierto_2030 | 0 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k1_deficit_no_cubierto_2040 | 5,878 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k1_deficit_no_cubierto_2054 | 50,155 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k1_primer_anio_no_cubre | 2,035 | Primer año en que I < D (K1) |
| M2_k1_remanente_cuidados_2027 | 33,456 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k1_remanente_cuidados_2030 | 23,798 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k1_remanente_cuidados_2040 | 0 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k1_remanente_cuidados_2054 | 0 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k1_remanente_cuidados_pts_2027 | 0.621 | Puntos del salario (masa con tope, 337 días) |
| M2_k1_remanente_cuidados_pts_2030 | 0.411 | Puntos del salario (masa con tope, 337 días) |
| M2_k1_remanente_cuidados_pts_2040 | 0 | Puntos del salario (masa con tope, 337 días) |
| M2_k1_remanente_cuidados_pts_2054 | 0 | Puntos del salario (masa con tope, 337 días) |
| M2_k1_remanente_cuidados_sem_2027 | 5.79 | % de los ingresos del SEM (Cuadro V.13) |
| M2_k1_remanente_cuidados_sem_2030 | 3.8 | % de los ingresos del SEM (Cuadro V.13) |
| M2_k1_remanente_cuidados_sem_2040 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| M2_k1_remanente_cuidados_sem_2054 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| M2_k2_cuidados_2027 | 0 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k2_cuidados_2030 | 0 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k2_cuidados_2040 | 9,131 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k2_cuidados_2054 | 0 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k2_cuidados_pts_2027 | 0 | Puntos del salario (masa con tope, 337 días) |
| M2_k2_cuidados_pts_2030 | 0 | Puntos del salario (masa con tope, 337 días) |
| M2_k2_cuidados_pts_2040 | 0.139 | Puntos del salario (masa con tope, 337 días) |
| M2_k2_cuidados_pts_2054 | 0 | Puntos del salario (masa con tope, 337 días) |
| M2_k2_cuidados_sem_2027 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| M2_k2_cuidados_sem_2030 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| M2_k2_cuidados_sem_2040 | 1.09 | % de los ingresos del SEM (Cuadro V.13) |
| M2_k2_cuidados_sem_2054 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| M2_k2_primer_anio_no_cubre | 2,047 | Primer año con déficit no cubierto tras usar la reserva (K2) |
| M2_k2_reserva_fin_2027 | 33,456 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k2_reserva_fin_2030 | 119,838 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k2_reserva_fin_2040 | 117,101 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k2_reserva_fin_2054 | 0 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k2_reserva_inicio_2035 | 182,617 | Reserva K2 al inicio de 2035 |
| M2_k2_reserva_max | 182,617 | Reserva máxima K2 (mdp de 2026) |
| M2_k2_reserva_max_anio | 2,034 | Año de la reserva máxima K2 |
| M2_k2_retiro_anual | 9,131 | 1/20 de la reserva al inicio de 2035 (mdp de 2026) |
| M2_reduccion_cuna_legal_2027 | 161,590 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_reduccion_cuna_legal_2030 | 173,529 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_reduccion_cuna_legal_2040 | 197,356 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_reduccion_cuna_legal_2054 | 221,999 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_reduccion_cuna_legal_pts_2027 | 3 | Puntos del salario (masa con tope, 337 días) |
| M2_reduccion_cuna_legal_pts_2030 | 3 | Puntos del salario (masa con tope, 337 días) |
| M2_reduccion_cuna_legal_pts_2040 | 3 | Puntos del salario (masa con tope, 337 días) |
| M2_reduccion_cuna_legal_pts_2054 | 3 | Puntos del salario (masa con tope, 337 días) |
| M2_reduccion_cuna_legal_sem_2027 | 27.95 | % de los ingresos del SEM (Cuadro V.13) |
| M2_reduccion_cuna_legal_sem_2030 | 27.71 | % de los ingresos del SEM (Cuadro V.13) |
| M2_reduccion_cuna_legal_sem_2040 | 23.62 | % de los ingresos del SEM (Cuadro V.13) |
| M2_reduccion_cuna_legal_sem_2054 | 18.58 | % de los ingresos del SEM (Cuadro V.13) |
| SEM_ingresos_2027 | 578,176 | Informe, Cuadro V.13, interpolación lineal |
| SEM_ingresos_2030 | 626,325 | Informe, Cuadro V.13, interpolación lineal |
| SEM_ingresos_2040 | 835,679 | Informe, Cuadro V.13, interpolación lineal |
| SEM_ingresos_2054 | 1,194,783 | Informe, Cuadro V.13, interpolación lineal |
| VP_M2_deficit | 2,463,416 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M2_ingreso | 2,404,562 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M2_k1_no_cubierto | 203,014 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M2_k1_remanente | 144,160 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M2_k2_cuidados | 71,748 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M2_k2_no_cubierto | 130,603 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M2_k2_reserva_final | 0 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M2_masa | 120,228,094 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M2_reduccion | 3,606,843 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_base_deficit | 2,463,416 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_base_ingreso | 3,265,351 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_base_k1_no_cubierto | 0 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_base_k1_remanente | 801,935 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_base_k2_cuidados | 747,074 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_base_k2_no_cubierto | 0 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_base_k2_reserva_final | 54,861 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_base_masa | 163,267,574 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_base_reduccion | 4,898,027 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| base_DH_total_k1_pesos_por_dh65_2027 | 2,456 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_DH_total_k1_pesos_por_dh65_2030 | 1,991 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_DH_total_k1_pesos_por_dh65_2040 | 1,746 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_DH_total_k1_pesos_por_dh65_2054 | 2,322 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_DH_total_k1_pesos_por_dh80_2027 | 11,382 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_DH_total_k1_pesos_por_dh80_2030 | 9,241 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_DH_total_k1_pesos_por_dh80_2040 | 7,336 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_DH_total_k1_pesos_por_dh80_2054 | 7,453 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_DH_total_k2_pesos_por_dh65_2027 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_DH_total_k2_pesos_por_dh65_2030 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_DH_total_k2_pesos_por_dh65_2040 | 2,327 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_DH_total_k2_pesos_por_dh65_2054 | 2,733 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_DH_total_k2_pesos_por_dh80_2027 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_DH_total_k2_pesos_por_dh80_2030 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_DH_total_k2_pesos_por_dh80_2040 | 9,779 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_DH_total_k2_pesos_por_dh80_2054 | 8,772 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_PAMF_k1_pesos_por_dh65_2027 | 3,057 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_PAMF_k1_pesos_por_dh65_2030 | 2,479 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_PAMF_k1_pesos_por_dh65_2040 | 2,173 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_PAMF_k1_pesos_por_dh65_2054 | 2,891 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_PAMF_k1_pesos_por_dh80_2027 | 14,170 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_PAMF_k1_pesos_por_dh80_2030 | 11,505 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_PAMF_k1_pesos_por_dh80_2040 | 9,134 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_PAMF_k1_pesos_por_dh80_2054 | 9,279 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_PAMF_k2_pesos_por_dh65_2027 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_PAMF_k2_pesos_por_dh65_2030 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_PAMF_k2_pesos_por_dh65_2040 | 2,897 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_PAMF_k2_pesos_por_dh65_2054 | 3,403 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_PAMF_k2_pesos_por_dh80_2027 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_PAMF_k2_pesos_por_dh80_2030 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_PAMF_k2_pesos_por_dh80_2040 | 12,175 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_PAMF_k2_pesos_por_dh80_2054 | 10,921 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_cubre_desde | 2,027 | Primer año con I ≥ D |
| base_deficit_GMP_pts_2027 | 1.358 | Puntos del salario (masa con tope, 337 días) |
| base_deficit_GMP_pts_2030 | 1.481 | Puntos del salario (masa con tope, 337 días) |
| base_deficit_GMP_pts_2040 | 1.543 | Puntos del salario (masa con tope, 337 días) |
| base_deficit_GMP_pts_2054 | 1.442 | Puntos del salario (masa con tope, 337 días) |
| base_deficit_GMP_sem_2027 | 12.85 | % de los ingresos del SEM (Cuadro V.13) |
| base_deficit_GMP_sem_2030 | 14.67 | % de los ingresos del SEM (Cuadro V.13) |
| base_deficit_GMP_sem_2040 | 16.45 | % de los ingresos del SEM (Cuadro V.13) |
| base_deficit_GMP_sem_2054 | 16.58 | % de los ingresos del SEM (Cuadro V.13) |
| base_deja_de_cubrir | no deja de cubrir | Primer año posterior a 2027 con I < D |
| base_holgura_min | 19,991 | Mínimo de ingreso − déficit de GMP, 2027-2054 (mdp de 2026) |
| base_holgura_min_anio | 2,036 | Año de la holgura mínima |
| base_holgura_min_pts | 0.259 | Holgura mínima en puntos del salario |
| base_infonavit_5pct_teorico_2027 | 273,444 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_infonavit_5pct_teorico_2030 | 310,273 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_infonavit_5pct_teorico_2040 | 445,485 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_infonavit_5pct_teorico_2054 | 687,059 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_ingreso_NS_2027 | 109,378 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_ingreso_NS_2030 | 124,109 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_ingreso_NS_2040 | 178,194 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_ingreso_NS_2054 | 274,824 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_ingreso_NS_pts_2027 | 2 | Puntos del salario (masa con tope, 337 días) |
| base_ingreso_NS_pts_2030 | 2 | Puntos del salario (masa con tope, 337 días) |
| base_ingreso_NS_pts_2040 | 2 | Puntos del salario (masa con tope, 337 días) |
| base_ingreso_NS_pts_2054 | 2 | Puntos del salario (masa con tope, 337 días) |
| base_ingreso_NS_sem_2027 | 18.92 | % de los ingresos del SEM (Cuadro V.13) |
| base_ingreso_NS_sem_2030 | 19.82 | % de los ingresos del SEM (Cuadro V.13) |
| base_ingreso_NS_sem_2040 | 21.32 | % de los ingresos del SEM (Cuadro V.13) |
| base_ingreso_NS_sem_2054 | 23 | % de los ingresos del SEM (Cuadro V.13) |
| base_k1_anios_no_cubre | 0 | Años 2027-2054 con I < D |
| base_k1_deficit_no_cubierto_2027 | 0 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k1_deficit_no_cubierto_2030 | 0 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k1_deficit_no_cubierto_2040 | 0 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k1_deficit_no_cubierto_2054 | 0 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k1_primer_anio_no_cubre | ninguno | Primer año en que I < D (K1) |
| base_k1_remanente_cuidados_2027 | 35,107 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k1_remanente_cuidados_2030 | 32,222 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k1_remanente_cuidados_2040 | 40,745 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k1_remanente_cuidados_2054 | 76,670 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k1_remanente_cuidados_pts_2027 | 0.642 | Puntos del salario (masa con tope, 337 días) |
| base_k1_remanente_cuidados_pts_2030 | 0.519 | Puntos del salario (masa con tope, 337 días) |
| base_k1_remanente_cuidados_pts_2040 | 0.457 | Puntos del salario (masa con tope, 337 días) |
| base_k1_remanente_cuidados_pts_2054 | 0.558 | Puntos del salario (masa con tope, 337 días) |
| base_k1_remanente_cuidados_sem_2027 | 6.07 | % de los ingresos del SEM (Cuadro V.13) |
| base_k1_remanente_cuidados_sem_2030 | 5.14 | % de los ingresos del SEM (Cuadro V.13) |
| base_k1_remanente_cuidados_sem_2040 | 4.88 | % de los ingresos del SEM (Cuadro V.13) |
| base_k1_remanente_cuidados_sem_2054 | 6.42 | % de los ingresos del SEM (Cuadro V.13) |
| base_k2_cuidados_2027 | 0 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k2_cuidados_2030 | 0 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k2_cuidados_2040 | 54,312 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k2_cuidados_2054 | 90,237 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k2_cuidados_pts_2027 | 0 | Puntos del salario (masa con tope, 337 días) |
| base_k2_cuidados_pts_2030 | 0 | Puntos del salario (masa con tope, 337 días) |
| base_k2_cuidados_pts_2040 | 0.61 | Puntos del salario (masa con tope, 337 días) |
| base_k2_cuidados_pts_2054 | 0.657 | Puntos del salario (masa con tope, 337 días) |
| base_k2_cuidados_sem_2027 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| base_k2_cuidados_sem_2030 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| base_k2_cuidados_sem_2040 | 6.5 | % de los ingresos del SEM (Cuadro V.13) |
| base_k2_cuidados_sem_2054 | 7.55 | % de los ingresos del SEM (Cuadro V.13) |
| base_k2_primer_anio_no_cubre | ninguno | Primer año con déficit no cubierto tras usar la reserva (K2) |
| base_k2_reserva_fin_2027 | 35,107 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k2_reserva_fin_2030 | 139,975 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k2_reserva_fin_2040 | 236,235 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k2_reserva_fin_2054 | 125,518 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k2_reserva_inicio_2035 | 271,337 | Reserva K2 al inicio de 2035 |
| base_k2_reserva_max | 271,337 | Reserva máxima K2 (mdp de 2026) |
| base_k2_reserva_max_anio | 2,034 | Año de la reserva máxima K2 |
| base_k2_retiro_anual | 13,567 | 1/20 de la reserva al inicio de 2035 (mdp de 2026) |
| base_reduccion_cuna_legal_2027 | 164,066 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_reduccion_cuna_legal_2030 | 186,164 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_reduccion_cuna_legal_2040 | 267,291 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_reduccion_cuna_legal_2054 | 412,235 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_reduccion_cuna_legal_pts_2027 | 3 | Puntos del salario (masa con tope, 337 días) |
| base_reduccion_cuna_legal_pts_2030 | 3 | Puntos del salario (masa con tope, 337 días) |
| base_reduccion_cuna_legal_pts_2040 | 3 | Puntos del salario (masa con tope, 337 días) |
| base_reduccion_cuna_legal_pts_2054 | 3 | Puntos del salario (masa con tope, 337 días) |
| base_reduccion_cuna_legal_sem_2027 | 28.38 | % de los ingresos del SEM (Cuadro V.13) |
| base_reduccion_cuna_legal_sem_2030 | 29.72 | % de los ingresos del SEM (Cuadro V.13) |
| base_reduccion_cuna_legal_sem_2040 | 31.98 | % de los ingresos del SEM (Cuadro V.13) |
| base_reduccion_cuna_legal_sem_2054 | 34.5 | % de los ingresos del SEM (Cuadro V.13) |
| chk_00_3.1 | 0 | 3.1 masa con tope = base de la tasa D2 de la v1.2 (máx. desviación relativa) |
| chk_01_3.1 | 1.02267 | 3.1 masa con tope / denominador en puntos de la v1.2, 2027 (razón) |
| chk_02_3.1 | 1.01399 | 3.1 masa con tope / denominador en puntos de la v1.2, 2054 (razón) |
| chk_03_3.1 | 1.736048 | 3.1 proporción de la masa por encima del tope, 2027 (%) |
| chk_04_3.1 | 2.7145 | 3.1 proporción de la masa por encima del tope, 2054 (%) |
| chk_05_3.2 | 0 | 3.2 Cuadro V.24 transcrito = PDF (celdas distintas) |
| chk_06_3.2 | 0 | 3.2 interpolación preserva los años ancla (máx. desviación, mdp) |
| chk_07_3.2 | -0.498724 | 3.2 VP del déficit interpolado frente al Cuadro V.24 (%) |
| chk_08_3.3 | -1.178311 | 3.3 VP 2 % × masa propia frente a 2 % × volumen del Informe, mismo horizonte (%) |
| chk_09_3.4 | 0 | 3.4 identidad de la reserva (máx. desviación, mdp) |
| chk_3.6 | 0 | 3.6 apariciones de 2055 en las tablas |
| chk_cuna_0 | 0 | 3.5 (b) = (a) − 3 puntos en todo nivel hasta 25 UMA (máx. desviación, puntos) |
| chk_cuna_1 | 0 | 3.5 tasas de cesantía y vejez fuera de la tabla de 1.5 (casos) |
| chk_cuna_2 | 0 | 3.5 tabla 2030 = art. 168 fr. II a) del DOF 16-12-2020 (celdas distintas) |
| contraste_brecha | 2,823,707 | valor_presente.csv, horizonte del Informe (30 años desde 2026) |
| contraste_def_vp | 2,618,336 | valor_presente.csv, horizonte del Informe (30 años desde 2026) |
| contraste_def_vp_mid | 2,579,923 | valor_presente.csv, horizonte del Informe (30 años desde 2026) |
| contraste_ing_vp | 2,751,304 | valor_presente.csv, horizonte del Informe (30 años desde 2026) |
| contraste_masa_vp | 174,402,197 | valor_presente.csv, horizonte del Informe (30 años desde 2026) |
| contraste_masa_vp_sin | 178,288,615 | valor_presente.csv, horizonte del Informe (30 años desde 2026) |
| contraste_ns_informe | 3,529,634 | 0.02 × 176,481,700 |
| contraste_ns_propio | 3,488,044 | 0.02 × masa propia, mismo horizonte |
| contraste_redondeo | 82,699 | valor_presente.csv, horizonte del Informe (30 años desde 2026) |
| contraste_resto | -1 | valor_presente.csv, horizonte del Informe (30 años desde 2026) |
| contraste_v19_v24 | 5,887 | valor_presente.csv, horizonte del Informe (30 años desde 2026) |
| cotizantes_2027 | 23,213,820 | Libro de Finanzas, `Pob Emp & Nuevos` (modelo de cohortes de la v1.2) |
| cotizantes_2030 | 25,233,767 | Libro de Finanzas, `Pob Emp & Nuevos` (modelo de cohortes de la v1.2) |
| cotizantes_2040 | 33,884,896 | Libro de Finanzas, `Pob Emp & Nuevos` (modelo de cohortes de la v1.2) |
| cotizantes_2054 | 46,801,970 | Libro de Finanzas, `Pob Emp & Nuevos` (modelo de cohortes de la v1.2) |
| cuna_2026_1.01 SM, lectura por UMA_cyv_a | 6.026 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, lectura por UMA_cyv_b | 6.026 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, lectura por UMA_cyv_c | 6.026 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, lectura por UMA_federal_a | 8.58 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, lectura por UMA_federal_b | 8.58 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, lectura por UMA_federal_c | 8.58 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, lectura por UMA_obrera_a | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, lectura por UMA_obrera_b | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, lectura por UMA_obrera_c | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, lectura por UMA_patron_a | 26.848 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, lectura por UMA_patron_b | 23.848 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, lectura por UMA_patron_c | 19.793 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, lectura por UMA_total_a | 37.803 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, lectura por UMA_total_b | 34.803 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, lectura por UMA_total_c | 30.748 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_cyv_a | 3.676 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_cyv_b | 3.676 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_cyv_c | 3.676 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_federal_a | 9.411 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_federal_b | 9.411 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_federal_c | 9.411 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_obrera_a | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_obrera_b | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_obrera_c | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_patron_a | 24.498 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_patron_b | 21.498 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_patron_c | 17.443 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_total_a | 36.284 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_total_b | 33.284 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_total_c | 29.229 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_cyv_a | 7.513 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_cyv_b | 7.513 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_cyv_c | 7.513 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_federal_a | 1.733 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_federal_b | 1.733 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_federal_c | 1.733 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_obrera_a | 2.655 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_obrera_b | 2.655 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_obrera_c | 2.655 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_patron_a | 23.623 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_patron_b | 20.623 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_patron_c | 22.05 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_total_a | 28.011 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_total_b | 25.011 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_total_c | 26.438 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_cyv_a | 4.851 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_cyv_b | 4.851 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_cyv_c | 4.851 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_federal_a | 12.296 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_federal_b | 12.296 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_federal_c | 12.296 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_obrera_a | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_obrera_b | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_obrera_c | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_patron_a | 28.351 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_patron_b | 25.351 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_patron_c | 18.618 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_total_a | 43.022 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_total_b | 40.022 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_total_c | 33.289 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_cyv_a | 7.513 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_cyv_b | 7.513 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_cyv_c | 7.513 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_federal_a | 0.843 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_federal_b | 0.843 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_federal_c | 0.843 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_obrera_a | 2.727 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_obrera_b | 2.727 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_obrera_c | 2.727 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_patron_a | 22.597 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_patron_b | 19.597 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_patron_c | 22.248 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_total_a | 26.167 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_total_b | 23.167 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_total_c | 25.818 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_cyv_a | 6.026 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_cyv_b | 6.026 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_cyv_c | 6.026 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_federal_a | 7.78 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_federal_b | 7.78 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_federal_c | 7.78 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_obrera_a | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_obrera_b | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_obrera_c | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_patron_a | 26.126 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_patron_b | 23.126 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_patron_c | 19.793 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_total_a | 36.281 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_total_b | 33.281 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_total_c | 29.948 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_cyv_a | 6.613 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_cyv_b | 6.613 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_cyv_c | 6.613 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_federal_a | 5.522 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_federal_b | 5.522 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_federal_c | 5.522 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_obrera_a | 2.475 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_obrera_b | 2.475 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_obrera_c | 2.475 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_patron_a | 25.288 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_patron_b | 22.288 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_patron_c | 20.655 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_total_a | 33.285 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_total_b | 30.285 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_total_c | 28.652 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_cyv_a | 7.513 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_cyv_b | 7.513 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_cyv_c | 7.513 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_federal_a | 2.922 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_federal_b | 2.922 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_federal_c | 2.922 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_obrera_a | 2.559 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_obrera_b | 2.559 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_obrera_c | 2.559 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_patron_a | 24.994 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_patron_b | 21.994 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_patron_c | 21.785 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_total_a | 30.475 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_total_b | 27.475 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_total_c | 27.266 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_cyv_a | 3.15 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_cyv_b | 3.15 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_cyv_c | 3.15 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_federal_a | 9.782 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_federal_b | 9.782 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_federal_c | 9.782 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_obrera_a | 0 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_obrera_b | 0 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_obrera_c | 0 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_patron_a | 26.422 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_patron_b | 23.422 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_patron_c | 19.292 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_total_a | 36.204 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_total_b | 33.204 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_total_c | 29.074 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_cyv_a | 10.077 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_cyv_b | 10.077 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_cyv_c | 10.077 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_federal_a | 5.976 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_federal_b | 5.976 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_federal_c | 5.976 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_obrera_a | 2.449 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_obrera_b | 2.449 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_obrera_c | 2.449 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_patron_a | 29.12 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_patron_b | 26.12 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_patron_c | 24.048 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_total_a | 37.545 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_total_b | 34.545 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_total_c | 32.473 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_cyv_a | 4.202 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_cyv_b | 4.202 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_cyv_c | 4.202 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_federal_a | 6.996 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_federal_b | 6.996 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_federal_c | 6.996 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_obrera_a | 2.449 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_obrera_b | 2.449 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_obrera_c | 2.449 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_patron_a | 23.245 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_patron_b | 20.245 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_patron_c | 18.173 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_total_a | 32.69 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_total_b | 29.69 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_total_c | 27.618 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_cyv_a | 11.875 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_cyv_b | 11.875 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_cyv_c | 11.875 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_federal_a | 1.733 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_federal_b | 1.733 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_federal_c | 1.733 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_obrera_a | 2.655 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_obrera_b | 2.655 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_obrera_c | 2.655 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_patron_a | 27.985 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_patron_b | 24.985 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_patron_c | 26.412 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_total_a | 32.373 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_total_b | 29.373 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_total_c | 30.8 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_cyv_a | 6.552 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_cyv_b | 6.552 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_cyv_c | 6.552 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_federal_a | 12.296 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_federal_b | 12.296 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_federal_c | 12.296 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_obrera_a | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_obrera_b | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_obrera_c | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_patron_a | 30.052 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_patron_b | 27.052 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_patron_c | 20.319 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_total_a | 44.723 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_total_b | 41.723 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_total_c | 34.99 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_cyv_a | 11.875 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_cyv_b | 11.875 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_cyv_c | 11.875 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_federal_a | 0.843 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_federal_b | 0.843 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_federal_c | 0.843 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_obrera_a | 2.727 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_obrera_b | 2.727 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_obrera_c | 2.727 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_patron_a | 26.959 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_patron_b | 23.959 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_patron_c | 26.61 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_total_a | 30.529 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_total_b | 27.529 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_total_c | 30.18 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_cyv_a | 8.902 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_cyv_b | 8.902 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_cyv_c | 8.902 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_federal_a | 7.78 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_federal_b | 7.78 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_federal_c | 7.78 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_obrera_a | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_obrera_b | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_obrera_c | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_patron_a | 29.002 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_patron_b | 26.002 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_patron_c | 22.669 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_total_a | 39.157 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_total_b | 36.157 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_total_c | 32.824 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_cyv_a | 10.077 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_cyv_b | 10.077 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_cyv_c | 10.077 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_federal_a | 5.522 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_federal_b | 5.522 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_federal_c | 5.522 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_obrera_a | 2.475 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_obrera_b | 2.475 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_obrera_c | 2.475 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_patron_a | 28.752 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_patron_b | 25.752 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_patron_c | 24.119 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_total_a | 36.749 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_total_b | 33.749 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_total_c | 32.116 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_cyv_a | 11.875 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_cyv_b | 11.875 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_cyv_c | 11.875 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_federal_a | 2.922 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_federal_b | 2.922 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_federal_c | 2.922 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_obrera_a | 2.559 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_obrera_b | 2.559 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_obrera_c | 2.559 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_patron_a | 29.356 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_patron_b | 26.356 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_patron_c | 26.147 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_total_a | 34.837 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_total_b | 31.837 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_total_c | 31.628 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_cyv_a | 3.15 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_cyv_b | 3.15 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_cyv_c | 3.15 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_federal_a | 7.269 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_federal_b | 7.269 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_federal_c | 7.269 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_obrera_a | 0 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_obrera_b | 0 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_obrera_c | 0 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_patron_a | 24.685 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_patron_b | 21.685 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_patron_c | 19.558 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_total_a | 31.955 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_total_b | 28.955 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_total_c | 26.827 | cuna_legal_por_salario.csv, % del SBC |
| cuna_sm_uma_2026 | 2.685 | SM en veces la UMA (Sup_Fin) |
| cuna_sm_uma_2030 | 3.646 | SM en veces la UMA (Sup_Fin) |
| escalon_2026_primer_cyv | 3.676 | Tasa patronal de cesantía y vejez a 1.01 SM, 1.01 SM, primer tramo tras el mínimo |
| escalon_2026_primer_cyv_salto | 0.526 | Salto frente a 3.150 % del salario mínimo (puntos) |
| escalon_2026_primer_patron_salto | -1.924 | Salto del total a cargo del patrón entre SM y 1.01 SM, ley vigente (puntos; neto del fin del art. 36) |
| escalon_2026_uma_cyv | 6.026 | Tasa patronal de cesantía y vejez a 1.01 SM, 1.01 SM, lectura por UMA |
| escalon_2026_uma_cyv_salto | 2.876 | Salto frente a 3.150 % del salario mínimo (puntos) |
| escalon_2026_uma_patron_salto | 0.426 | Salto del total a cargo del patrón entre SM y 1.01 SM, ley vigente (puntos; neto del fin del art. 36) |
| escalon_2030_primer_cyv | 4.202 | Tasa patronal de cesantía y vejez a 1.01 SM, 1.01 SM, primer tramo tras el mínimo |
| escalon_2030_primer_cyv_salto | 1.052 | Salto frente a 3.150 % del salario mínimo (puntos) |
| escalon_2030_primer_patron_salto | -1.44 | Salto del total a cargo del patrón entre SM y 1.01 SM, ley vigente (puntos; neto del fin del art. 36) |
| escalon_2030_uma_cyv | 10.077 | Tasa patronal de cesantía y vejez a 1.01 SM, 1.01 SM, lectura por UMA |
| escalon_2030_uma_cyv_salto | 6.927 | Salto frente a 3.150 % del salario mínimo (puntos) |
| escalon_2030_uma_patron_salto | 4.435 | Salto del total a cargo del patrón entre SM y 1.01 SM, ley vigente (puntos; neto del fin del art. 36) |
| formalidad_implicita_2027 | 0.3452 | Cotizantes / ocupados (prueba C de la v1.2) |
| formalidad_implicita_2030 | 0.3647 | Cotizantes / ocupados (prueba C de la v1.2) |
| formalidad_implicita_2040 | 0.4604 | Cotizantes / ocupados (prueba C de la v1.2) |
| formalidad_implicita_2054 | 0.6313 | Cotizantes / ocupados (prueba C de la v1.2) |
| masa25_2027 | 5,468,877 | Σ cotizantes × SBC (R1, tope 25 UMA, piso SM) × UMA × 337, mdp de 2026 |
| masa25_2030 | 6,205,467 | Σ cotizantes × SBC (R1, tope 25 UMA, piso SM) × UMA × 337, mdp de 2026 |
| masa25_2040 | 8,909,700 | Σ cotizantes × SBC (R1, tope 25 UMA, piso SM) × UMA × 337, mdp de 2026 |
| masa25_2054 | 13,741,181 | Σ cotizantes × SBC (R1, tope 25 UMA, piso SM) × UMA × 337, mdp de 2026 |
| prop_sobre_tope_2027 | 1.74 | % de la masa sin tope que rebasa 25 UMA (forma R1 sin tope) |
| prop_sobre_tope_2030 | 1.81 | % de la masa sin tope que rebasa 25 UMA (forma R1 sin tope) |
| prop_sobre_tope_2040 | 2.12 | % de la masa sin tope que rebasa 25 UMA (forma R1 sin tope) |
| prop_sobre_tope_2054 | 2.71 | % de la masa sin tope que rebasa 25 UMA (forma R1 sin tope) |
| sm_uma_2027 | 2.899 | SM en veces la UMA (Sup_Fin; v1.2) |
| sm_uma_2030 | 3.646 | SM en veces la UMA (Sup_Fin; v1.2) |
| sm_uma_2040 | 3.833 | SM en veces la UMA (Sup_Fin; v1.2) |
| sm_uma_2054 | 4.11 | SM en veces la UMA (Sup_Fin; v1.2) |
