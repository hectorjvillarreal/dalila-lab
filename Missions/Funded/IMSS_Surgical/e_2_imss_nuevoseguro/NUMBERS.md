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
| PAMF_2025 | 63,598,543 adscripciones a médico familiar (60,266,622 personas por CURP) | Informe, texto del Cuadro I.4 y Gráfica I.23 | solo para la regresión v1.0; la v1.1 elimina esta base |
| ENIGH_IMSS_65mas | Tasa de afiliación al IMSS (poblacion.inst_1 = 1) por grupo quinquenal (65-69 … 85+) y sexo, ponderada con factor | ENIGH 2024 (INEGI), tabla poblacion | nueva (v1.1); base de personas mayores, × CONAPO por año; mismo método del experimento 1 |
| GMP_V19_provisiones | 123 / 9,971 / 19,577 / 541 / 540 / 542 / 545 mdp de 2026 (2026, 2031, …, 2051 y año final) | Informe, Cuadro V.19, fila Provisiones | nueva (v1.1); margen sin provisiones |
| SM_2023 / UMA_2023 | 207.44 pesos/día (resto del país) / 103.74 pesos/día (vigente desde el 1-02-2023): el SM equivale a 2.00 UMA | DOF 07-12-2022, Resolución del Consejo de Representantes de la CONASAMI; DOF 10-01-2023, INEGI, valor de la UMA | nueva (v1.1); el tramo «1.01 SM a 1.50 UMA» ya estaba vacío en 2023 |
| Vivienda_al_pensionarse | 71.45 % (base) / 57.45 % (riesgo); 83 % en 2026-2035, baja a 50 % al final del horizonte (base) | Informe, Cuadro II.18 y nota 3 | confirmada |
| CyV_patronal_2025_2026_2030 | Tabla de la sección 1.5 de la instrucción | DOF 16-12-2020, Segundo Transitorio (tabla en imagen, leída) y art. 168 fr. II a) (texto); Informe, Cuadro A.3 nota 6 (2025) | verificada en el DOF: coincide en todas las celdas |
| Cuota_social_dic2025 | 1 SM 12.18; 1.01 SM-1.50 UMA 11.33; 1.51-2 10.48; 2.01-2.5 9.63; 2.51-3 8.78; 3.01-3.5 7.93; 3.51-4 7.08 pesos por día | Informe, Cuadro A.3, nota 8 | nueva; se mantiene constante en UMA reales (se indexa al INPC) |
| c_D2 | 3.467 % (0.0346703) | Corrida v1.2 | confirmada |
| SBC_prom_dic2025 | 5.55 veces la UMA (627.87 pesos/día) | Informe, sección I.1.3 | confirmada en la v1.2; nivel «promedio» de la tabla de cuña |
| Patronales SEM, SIV, SGPS, Retiro | Cuota fija 20.40 % UMA; excedente 1.10 %; prestaciones en dinero 0.70 %; GMP 1.05 %; IV 1.75 %; GPS 1.00 %; Retiro 2.00 % | Informe, Cuadro A.3; libro, hoja `Tasas de Contribución` | confirmada |
| RT_prima_promedio | 1.9078 % en el Cuadro X-2.2; 1.80 % en las proyecciones de masa e ingreso | Informe, Cuadro A.3, nota 1 (vigencia mar. 2025-feb. 2026); libro, hoja `Tasas de Contribución`, nota 2 (promedio 2023-2025) | v1.1: el cuadro de cuña usa 1.9078 %; la regresión v1.0 usa 1.80 % |
| Obreras y federales | Obrera: excedente 0.40, PD 0.25, GMP 0.375, IV 0.625, CyV 1.125; federal: cuota fija 14.83 % UMA, PD 0.05, GMP 0.075, IV 0.125 | Informe, Cuadro A.3 | nueva |
| Art_36_LSS | «Corresponde al patrón pagar íntegramente la cuota señalada para los trabajadores, en los casos en que éstos perciban como cuota diaria el salario mínimo.» | Ley del Seguro Social, art. 36, texto vigente publicado por la Cámara de Diputados (última reforma DOF 15-01-2026) | verificada (v1.1); coincide con la redacción citada |
| Criterio_SUA_1.01SM | No encontrado | Búsqueda en documentación pública del IMSS y del DOF (18-10-2026); la página del SUA requiere sesión | pendiente de confirmación con el IMSS (visita de Juan Pablo) |
| Decision_aprobada_M3 | M3 se mide desde 2025 (34.0 % → 48.56 % en 2054), con la misma referencia que M2 | Instrucción v1.2, sección 0 (Beth y Cath) | decisión aprobada |
| Decision_aprobada_puntos | Los puntos del salario de cada escenario usan la masa de ese escenario (misma definición, valores propios) | Instrucción v1.2, sección 0 | decisión aprobada |
| Decision_aprobada_ENIGH | Tasa de afiliación de 65+ de la ENIGH por grupos quinquenales (85 y más) y sexo | Instrucción v1.2, sección 0 | decisión aprobada |
| Decision_aprobada_formalizacion | La limitación sobre la formalización no usa «sin precedente histórico»; se sustituye por la serie 2005-2025 | Instrucción v1.2, secciones 0 y 4 | decisión aprobada |
| Regla_K2_v12 | Desde 2035: el ingreso cubre GMP; el faltante sale de la reserva; el retiro fijo de 1/20 de la reserva de inicio de 2035 va a cuidados solo en años sin faltante y hasta donde alcance la reserva; agotada la reserva, el faltante es déficit no cubierto | Instrucción v1.2, sección 3.2 (decisión de Beth) | aplicada en la v1.2 |
| IMSS_puestos_Memoria | Puestos de trabajo afiliados al IMSS al 31 de diciembre, 1997-2025, fila Nacional (modalidades 10, 13, 14, 17, 30, 34, 35, 36, 38, 42, 43 y 44) | IMSS, Memoria Estadística 2025, capítulo I, Cuadro I.2 (imss.gob.mx/sites/all/statics/pdf/estadisticas/memoria/2025/01-Asegurados.xlsx), descargado el 18-10-2026 | nueva (v1.2); numerador de la serie de formalización |
| ENOE_ocupados_T4 | Población ocupada de 15 años o más, cuarto trimestre de 2005 a 2025: tabla SDEMT, r_def = 0, c_res ∈ {1, 3}, clase2 = 1, 15 ≤ eda ≤ 97, factor fac (2005-2019) o fac_tri (2020-2025) | INEGI, ENOE, microdatos (inegi.org.mx/contenidos/programas/enoe/15ymas/microdatos/), descargados el 18-10-2026 | nueva (v1.2); denominador de la serie de formalización; cuarto trimestre para empatar con el corte de diciembre del IMSS |
| Proyeccion_pensionados_IMSS | No existe en el Informe una proyección anual de pensionados del IMSS (solo la del RJP, grupo cerrado, Gráfica VIII.1) | Informe 2025-2026, revisión de los capítulos II, V y VIII | la variante opcional de personas mayores (v1.2, 5.2) no se construye |
| Infonavit_recaudacion_efectiva | No obtenida | Estados financieros del Infonavit 2024-2025 | omitida, como manda la instrucción |

## Experimento 2 — 2. Cifras calculadas (generadas por `src/`, archivo `data/derived/numbers_computed.json`)

| Clave | Valor | Fuente / cálculo |
|---|---|---|
| CONAPO_65mas_2025 | 11,698,499 | CONAPO 2023, población de 65 años o más, 2025 |
| DH65_2025 | 13,143,566 | Conteo máximo: 0.166 × 79,178,109 |
| DH65_2027 | 14,295,992 | Conteo máximo: 0.166 × 79,178,109 × (CONAPO 65+ t / CONAPO 65+ 2025) |
| DH65_2030 | 16,182,171 | Conteo máximo: 0.166 × 79,178,109 × (CONAPO 65+ t / CONAPO 65+ 2025) |
| DH65_2040 | 23,340,899 | Conteo máximo: 0.166 × 79,178,109 × (CONAPO 65+ t / CONAPO 65+ 2025) |
| DH65_2054 | 33,012,741 | Conteo máximo: 0.166 × 79,178,109 × (CONAPO 65+ t / CONAPO 65+ 2025) |
| DH65_entre_CONAPO65_2025 | 112.4 | Conteo máximo / población nacional de 65+ (%) |
| DH65_entre_CONAPO65_2027 | 112.4 | Conteo máximo 65+ / población nacional de 65+ (%) |
| DH65_entre_CONAPO65_2030 | 112.4 | Conteo máximo 65+ / población nacional de 65+ (%) |
| DH65_entre_CONAPO65_2040 | 112.4 | Conteo máximo 65+ / población nacional de 65+ (%) |
| DH65_entre_CONAPO65_2054 | 112.4 | Conteo máximo 65+ / población nacional de 65+ (%) |
| DH80_2027 | 3,084,411 | Conteo máximo: DH65 × (CONAPO 80+ / CONAPO 65+) |
| DH80_2030 | 3,486,854 | Conteo máximo: DH65 × (CONAPO 80+ / CONAPO 65+) |
| DH80_2040 | 5,553,803 | Conteo máximo: DH65 × (CONAPO 80+ / CONAPO 65+) |
| DH80_2054 | 10,286,912 | Conteo máximo: DH65 × (CONAPO 80+ / CONAPO 65+) |
| ENIGH65_2025 | 5,445,347 | Base ENIGH, 65+, 2025 |
| ENIGH65_2027 | 5,923,223 | Tasa IMSS (inst_1) de la ENIGH 2024 por grupo quinquenal y sexo × CONAPO, 65+ |
| ENIGH65_2030 | 6,704,827 | Tasa IMSS (inst_1) de la ENIGH 2024 por grupo quinquenal y sexo × CONAPO, 65+ |
| ENIGH65_2040 | 9,645,418 | Tasa IMSS (inst_1) de la ENIGH 2024 por grupo quinquenal y sexo × CONAPO, 65+ |
| ENIGH65_2054 | 13,476,177 | Tasa IMSS (inst_1) de la ENIGH 2024 por grupo quinquenal y sexo × CONAPO, 65+ |
| ENIGH65_entre_CONAPO65_2027 | 46.6 | Base ENIGH 65+ / población nacional de 65+ (%) |
| ENIGH65_entre_CONAPO65_2030 | 46.6 | Base ENIGH 65+ / población nacional de 65+ (%) |
| ENIGH65_entre_CONAPO65_2040 | 46.4 | Base ENIGH 65+ / población nacional de 65+ (%) |
| ENIGH65_entre_CONAPO65_2054 | 45.9 | Base ENIGH 65+ / población nacional de 65+ (%) |
| ENIGH80_2027 | 1,147,234 | Idem, 80+ |
| ENIGH80_2030 | 1,295,372 | Idem, 80+ |
| ENIGH80_2040 | 2,063,704 | Idem, 80+ |
| ENIGH80_2054 | 3,796,023 | Idem, 80+ |
| ENIGH_n_min_celda | 1,329 | Observaciones mínimas por celda grupo × sexo (65+) |
| ENIGH_tasa_65_H | 46.77 | Tasa IMSS por grupo quinquenal (85 = 85 y más) y sexo, ENIGH 2024 (%) |
| ENIGH_tasa_65_M | 47 | Tasa IMSS por grupo quinquenal (85 = 85 y más) y sexo, ENIGH 2024 (%) |
| ENIGH_tasa_70_H | 50.42 | Tasa IMSS por grupo quinquenal (85 = 85 y más) y sexo, ENIGH 2024 (%) |
| ENIGH_tasa_70_M | 49.3 | Tasa IMSS por grupo quinquenal (85 = 85 y más) y sexo, ENIGH 2024 (%) |
| ENIGH_tasa_75_H | 47.7 | Tasa IMSS por grupo quinquenal (85 = 85 y más) y sexo, ENIGH 2024 (%) |
| ENIGH_tasa_75_M | 46.33 | Tasa IMSS por grupo quinquenal (85 = 85 y más) y sexo, ENIGH 2024 (%) |
| ENIGH_tasa_80_H | 43.35 | Tasa IMSS por grupo quinquenal (85 = 85 y más) y sexo, ENIGH 2024 (%) |
| ENIGH_tasa_80_M | 45.48 | Tasa IMSS por grupo quinquenal (85 = 85 y más) y sexo, ENIGH 2024 (%) |
| ENIGH_tasa_85_H | 40.53 | Tasa IMSS por grupo quinquenal (85 = 85 y más) y sexo, ENIGH 2024 (%) |
| ENIGH_tasa_85_M | 37.28 | Tasa IMSS por grupo quinquenal (85 = 85 y más) y sexo, ENIGH 2024 (%) |
| ENIGH_tasa_IMSS_65mas | 46.62 | ENIGH 2024, % de 65+ con inst_1 = 1 (ponderado) |
| ENIGH_tasa_IMSS_80mas | 41.84 | ENIGH 2024, % de 80+ con inst_1 = 1 (ponderado) |
| ENOE_ocupados_T4_2005 | 41,949,328 | ENOE T4, ocupados de 15+ (INEGI, microdatos) |
| ENOE_ocupados_T4_2010 | 45,147,139 | ENOE T4, ocupados de 15+ (INEGI, microdatos) |
| ENOE_ocupados_T4_2015 | 50,768,849 | ENOE T4, ocupados de 15+ (INEGI, microdatos) |
| ENOE_ocupados_T4_2020 | 53,084,911 | ENOE T4, ocupados de 15+ (INEGI, microdatos) |
| ENOE_ocupados_T4_2025 | 59,751,051 | ENOE T4, ocupados de 15+ (INEGI, microdatos) |
| GMP_deficit_2027 | 74,270 | Informe, Cuadro V.24 (base), interpolación lineal |
| GMP_deficit_2030 | 91,888 | Informe, Cuadro V.24 (base), interpolación lineal |
| GMP_deficit_2040 | 137,449 | Informe, Cuadro V.24 (base), interpolación lineal |
| GMP_deficit_2054 | 198,154 | Informe, Cuadro V.24 (base), interpolación lineal |
| GMP_ingresos_2027 | 92,473 | Informe, Cuadro V.24 (base), ingresos, interpolación lineal |
| GMP_ingresos_2030 | 101,395 | Informe, Cuadro V.24 (base), ingresos, interpolación lineal |
| GMP_ingresos_2040 | 138,216 | Informe, Cuadro V.24 (base), ingresos, interpolación lineal |
| GMP_ingresos_2054 | 212,229 | Informe, Cuadro V.24 (base), ingresos, interpolación lineal |
| GMP_prima_eq_exacta | 3.053 | 5,388,234 / 176,481,700 (Cuadros V.19 y V.15) |
| GMP_prima_fin_exacta | 1.5 | 2,647,226 / 176,481,700 (Cuadros V.20 y V.15) |
| GMP_provisiones_2027 | 2,093 | Informe, Cuadro V.19, provisiones, interpolación lineal |
| GMP_provisiones_2030 | 8,001 | Informe, Cuadro V.19, provisiones, interpolación lineal |
| GMP_provisiones_2040 | 4,348 | Informe, Cuadro V.19, provisiones, interpolación lineal |
| GMP_provisiones_2054 | 544 | Informe, Cuadro V.19, provisiones, interpolación lineal |
| IMSS_puestos_dic_2005 | 13,061,565 | IMSS, Memoria Estadística 2025, Cuadro I.2, Nacional |
| IMSS_puestos_dic_2010 | 14,738,783 | IMSS, Memoria Estadística 2025, Cuadro I.2, Nacional |
| IMSS_puestos_dic_2015 | 17,884,033 | IMSS, Memoria Estadística 2025, Cuadro I.2, Nacional |
| IMSS_puestos_dic_2020 | 19,773,732 | IMSS, Memoria Estadística 2025, Cuadro I.2, Nacional |
| IMSS_puestos_dic_2025 | 22,517,076 | IMSS, Memoria Estadística 2025, Cuadro I.2, Nacional |
| M2_ENIGH_k1_pesos_por_dh65_2027 | 5,413 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_ENIGH_k1_pesos_por_dh65_2030 | 2,523 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_ENIGH_k1_pesos_por_dh65_2040 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_ENIGH_k1_pesos_por_dh65_2054 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_ENIGH_k1_pesos_por_dh80_2027 | 27,946 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_ENIGH_k1_pesos_por_dh80_2030 | 13,059 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_ENIGH_k1_pesos_por_dh80_2040 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_ENIGH_k1_pesos_por_dh80_2054 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_ENIGH_k2_pesos_por_dh65_2027 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_ENIGH_k2_pesos_por_dh65_2030 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_ENIGH_k2_pesos_por_dh65_2040 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_ENIGH_k2_pesos_por_dh65_2054 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_ENIGH_k2_pesos_por_dh80_2027 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_ENIGH_k2_pesos_por_dh80_2030 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_ENIGH_k2_pesos_por_dh80_2040 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_ENIGH_k2_pesos_por_dh80_2054 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_Informe_max_k1_pesos_por_dh65_2027 | 2,243 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_Informe_max_k1_pesos_por_dh65_2030 | 1,045 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_Informe_max_k1_pesos_por_dh65_2040 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_Informe_max_k1_pesos_por_dh65_2054 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_Informe_max_k1_pesos_por_dh80_2027 | 10,394 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_Informe_max_k1_pesos_por_dh80_2030 | 4,852 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_Informe_max_k1_pesos_por_dh80_2040 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_Informe_max_k1_pesos_por_dh80_2054 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_Informe_max_k2_pesos_por_dh65_2027 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_Informe_max_k2_pesos_por_dh65_2030 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_Informe_max_k2_pesos_por_dh65_2040 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_Informe_max_k2_pesos_por_dh65_2054 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_Informe_max_k2_pesos_por_dh80_2027 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_Informe_max_k2_pesos_por_dh80_2030 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_Informe_max_k2_pesos_por_dh80_2040 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_Informe_max_k2_pesos_por_dh80_2054 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M2_conprov_libro_k1_primer_anio_sin_cobertura | 2,033 | sensibilidad_provisiones_masa.csv |
| M2_conprov_libro_k2_primer_anio_sin_cobertura | 2,038 | sensibilidad_provisiones_masa.csv |
| M2_conprov_libro_margen_2036 | -30,787 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M2_conprov_libro_margen_2040 | -42,042 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M2_conprov_libro_margen_min | -148,093 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M2_conprov_libro_margen_min_anio | 2,054 | sensibilidad_provisiones_masa.csv |
| M2_conprov_libro_vp_k1_deficit_no_cubierto | 831,627 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M2_conprov_libro_vp_k2_deficit_no_cubierto | 728,630 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M2_conprov_smasa_k1_primer_anio_sin_cobertura | 2,032 | sensibilidad_provisiones_masa.csv |
| M2_conprov_smasa_k2_primer_anio_sin_cobertura | 2,037 | sensibilidad_provisiones_masa.csv |
| M2_conprov_smasa_margen_2036 | -41,145 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M2_conprov_smasa_margen_2040 | -52,904 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M2_conprov_smasa_margen_min | -160,909 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M2_conprov_smasa_margen_min_anio | 2,054 | sensibilidad_provisiones_masa.csv |
| M2_conprov_smasa_vp_k1_deficit_no_cubierto | 976,427 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M2_conprov_smasa_vp_k2_deficit_no_cubierto | 885,956 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M2_deficit_GMP_2027 | 75,666 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_deficit_GMP_2030 | 98,769 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_deficit_GMP_2040 | 173,612 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_deficit_GMP_2054 | 296,092 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_deficit_GMP_pts_2027 | 1.405 | Puntos del salario (masa del escenario con tope, 337 días) |
| M2_deficit_GMP_pts_2030 | 1.708 | Puntos del salario (masa del escenario con tope, 337 días) |
| M2_deficit_GMP_pts_2040 | 2.639 | Puntos del salario (masa del escenario con tope, 337 días) |
| M2_deficit_GMP_pts_2054 | 4.001 | Puntos del salario (masa del escenario con tope, 337 días) |
| M2_deficit_GMP_sem_2027 | 13.09 | % de los ingresos del SEM (Cuadro V.13) |
| M2_deficit_GMP_sem_2030 | 15.77 | % de los ingresos del SEM (Cuadro V.13) |
| M2_deficit_GMP_sem_2040 | 20.78 | % de los ingresos del SEM (Cuadro V.13) |
| M2_deficit_GMP_sem_2054 | 24.78 | % de los ingresos del SEM (Cuadro V.13) |
| M2_factor_masa_2027 | 0.9849 | Masa M2 / masa base |
| M2_factor_masa_2030 | 0.9321 | Masa M2 / masa base |
| M2_factor_masa_2040 | 0.7384 | Masa M2 / masa base |
| M2_factor_masa_2054 | 0.5385 | Masa M2 / masa base |
| M2_formalidad_2027 | 34 | Formalidad implícita del escenario M2 (%) |
| M2_formalidad_2030 | 34 | Formalidad implícita del escenario M2 (%) |
| M2_formalidad_2040 | 34 | Formalidad implícita del escenario M2 (%) |
| M2_formalidad_2054 | 34 | Formalidad implícita del escenario M2 (%) |
| M2_holgura_min | -148,093 | Mínimo de ingreso − déficit de GMP, 2027-2054 (mdp de 2026) |
| M2_holgura_min_anio | 2,054 | Año de la holgura mínima |
| M2_holgura_min_pts | -2.001 | Holgura mínima en puntos del salario |
| M2_infonavit_5pct_teorico_2027 | 269,317 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_infonavit_5pct_teorico_2030 | 289,215 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_infonavit_5pct_teorico_2040 | 328,927 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_infonavit_5pct_teorico_2054 | 369,998 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_ingreso_NS_2027 | 107,727 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_ingreso_NS_2030 | 115,686 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_ingreso_NS_2040 | 131,571 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_ingreso_NS_2054 | 147,999 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_ingreso_NS_pts_2027 | 2 | Puntos del salario (masa del escenario con tope, 337 días) |
| M2_ingreso_NS_pts_2030 | 2 | Puntos del salario (masa del escenario con tope, 337 días) |
| M2_ingreso_NS_pts_2040 | 2 | Puntos del salario (masa del escenario con tope, 337 días) |
| M2_ingreso_NS_pts_2054 | 2 | Puntos del salario (masa del escenario con tope, 337 días) |
| M2_ingreso_NS_sem_2027 | 18.63 | % de los ingresos del SEM (Cuadro V.13) |
| M2_ingreso_NS_sem_2030 | 18.47 | % de los ingresos del SEM (Cuadro V.13) |
| M2_ingreso_NS_sem_2040 | 15.74 | % de los ingresos del SEM (Cuadro V.13) |
| M2_ingreso_NS_sem_2054 | 12.39 | % de los ingresos del SEM (Cuadro V.13) |
| M2_k1_anios_no_cubre | 22 | Años 2027-2054 con I < D |
| M2_k1_cubre_hasta | 2,032 | Último año cubierto antes del primero sin cobertura (K1) |
| M2_k1_deficit_no_cubierto_2027 | 0 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k1_deficit_no_cubierto_2030 | 0 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k1_deficit_no_cubierto_2040 | 42,042 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k1_deficit_no_cubierto_2054 | 148,093 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k1_deficit_no_cubierto_pts_2027 | 0 | Puntos del salario (masa del escenario con tope, 337 días) |
| M2_k1_deficit_no_cubierto_pts_2030 | 0 | Puntos del salario (masa del escenario con tope, 337 días) |
| M2_k1_deficit_no_cubierto_pts_2040 | 0.639 | Puntos del salario (masa del escenario con tope, 337 días) |
| M2_k1_deficit_no_cubierto_pts_2054 | 2.001 | Puntos del salario (masa del escenario con tope, 337 días) |
| M2_k1_deficit_no_cubierto_sem_2027 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| M2_k1_deficit_no_cubierto_sem_2030 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| M2_k1_deficit_no_cubierto_sem_2040 | 5.03 | % de los ingresos del SEM (Cuadro V.13) |
| M2_k1_deficit_no_cubierto_sem_2054 | 12.39 | % de los ingresos del SEM (Cuadro V.13) |
| M2_k1_primer_anio_no_cubre | 2,033 | Primer año en que I < D (K1) |
| M2_k1_remanente_cuidados_2027 | 32,061 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k1_remanente_cuidados_2030 | 16,917 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k1_remanente_cuidados_2040 | 0 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k1_remanente_cuidados_2054 | 0 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k1_remanente_cuidados_pts_2027 | 0.595 | Puntos del salario (masa del escenario con tope, 337 días) |
| M2_k1_remanente_cuidados_pts_2030 | 0.292 | Puntos del salario (masa del escenario con tope, 337 días) |
| M2_k1_remanente_cuidados_pts_2040 | 0 | Puntos del salario (masa del escenario con tope, 337 días) |
| M2_k1_remanente_cuidados_pts_2054 | 0 | Puntos del salario (masa del escenario con tope, 337 días) |
| M2_k1_remanente_cuidados_sem_2027 | 5.55 | % de los ingresos del SEM (Cuadro V.13) |
| M2_k1_remanente_cuidados_sem_2030 | 2.7 | % de los ingresos del SEM (Cuadro V.13) |
| M2_k1_remanente_cuidados_sem_2040 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| M2_k1_remanente_cuidados_sem_2054 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| M2_k2_cuidados_2027 | 0 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k2_cuidados_2030 | 0 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k2_cuidados_2040 | 0 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k2_cuidados_2054 | 0 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k2_cuidados_pts_2027 | 0 | Puntos del salario (masa del escenario con tope, 337 días) |
| M2_k2_cuidados_pts_2030 | 0 | Puntos del salario (masa del escenario con tope, 337 días) |
| M2_k2_cuidados_pts_2040 | 0 | Puntos del salario (masa del escenario con tope, 337 días) |
| M2_k2_cuidados_pts_2054 | 0 | Puntos del salario (masa del escenario con tope, 337 días) |
| M2_k2_cuidados_sem_2027 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| M2_k2_cuidados_sem_2030 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| M2_k2_cuidados_sem_2040 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| M2_k2_cuidados_sem_2054 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| M2_k2_primer_anio_no_cubre | 2,038 | Primer año con déficit no cubierto tras usar la reserva (K2) |
| M2_k2_reserva_fin_2027 | 32,061 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k2_reserva_fin_2030 | 103,179 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k2_reserva_fin_2040 | 0 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k2_reserva_fin_2054 | 0 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_k2_reserva_inicio_2035 | 110,952 | Reserva K2 al inicio de 2035 |
| M2_k2_reserva_max | 122,984 | Reserva máxima K2 (mdp de 2026) |
| M2_k2_reserva_max_anio | 2,032 | Año de la reserva máxima K2 |
| M2_k2_retiro_anual | 5,548 | 1/20 de la reserva al inicio de 2035 (mdp de 2026) |
| M2_k2cambio_cuidados_2040_antes_v11 | 0 | k2_cambios_v11_v12.csv |
| M2_k2cambio_cuidados_2040_despues_v12 | 0 | k2_cambios_v11_v12.csv |
| M2_k2cambio_cuidados_2054_antes_v11 | 0 | k2_cambios_v11_v12.csv |
| M2_k2cambio_cuidados_2054_despues_v12 | 0 | k2_cambios_v11_v12.csv |
| M2_k2cambio_primer_antes_v11 | 2,038 | k2_cambios_v11_v12.csv |
| M2_k2cambio_primer_despues_v12 | 2,038 | k2_cambios_v11_v12.csv |
| M2_k2cambio_reserva_2054_antes_v11 | 0 | k2_cambios_v11_v12.csv |
| M2_k2cambio_reserva_2054_despues_v12 | 0 | k2_cambios_v11_v12.csv |
| M2_k2cambio_vp_cuidados_antes_v11 | 12,387 | k2_cambios_v11_v12.csv |
| M2_k2cambio_vp_cuidados_despues_v12 | 0 | k2_cambios_v11_v12.csv |
| M2_k2cambio_vp_no_cubierto_antes_v11 | 741,017 | k2_cambios_v11_v12.csv |
| M2_k2cambio_vp_no_cubierto_despues_v12 | 728,630 | k2_cambios_v11_v12.csv |
| M2_k2v11_anios_faltante_con_pago | 3 | k2_v11_anios_con_faltante.csv |
| M2_k2v11_pago_cuidados_con_faltante | 16,643 | Σ pagos a cuidados de la v1.1 en años con faltante |
| M2_k2v12_agotamiento | 2,038 | reserva_K2.csv |
| M2_k2v12_retiros_GMP | 119,940 | reserva_K2.csv, Σ 2035-2054 |
| M2_k2v12_retiros_cuidados | 0 | reserva_K2.csv, Σ 2035-2054 |
| M2_k2v12_saldo_cierre_2054 | 0 | reserva_K2.csv |
| M2_k2v12_saldo_inicio_2035 | 110,952 | reserva_K2.csv, mdp de 2026 |
| M2_k2v12_saldo_inicio_2040 | 0 | reserva_K2.csv, mdp de 2026 |
| M2_k2v12_saldo_inicio_2045 | 0 | reserva_K2.csv, mdp de 2026 |
| M2_k2v12_saldo_inicio_2050 | 0 | reserva_K2.csv, mdp de 2026 |
| M2_k2v12_saldo_inicio_2054 | 0 | reserva_K2.csv, mdp de 2026 |
| M2_margen_sin_prov_2036 | -11,210 | Margen sin provisiones en 2036 |
| M2_margen_sin_prov_min | -147,549 | Mínimo de ingreso − (déficit − provisiones de GMP), 2027-2054 |
| M2_margen_sin_prov_min_anio | 2,054 | Año del margen mínimo sin provisiones |
| M2_masa_tope25_2027 | 5,386,337 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_masa_tope25_2030 | 5,784,296 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_masa_tope25_2040 | 6,578,532 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_masa_tope25_2054 | 7,399,962 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_reduccion_cuna_legal_2027 | 161,590 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_reduccion_cuna_legal_2030 | 173,529 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_reduccion_cuna_legal_2040 | 197,356 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_reduccion_cuna_legal_2054 | 221,999 | ingreso_vs_GMP.csv, M2, mdp de 2026 |
| M2_reduccion_cuna_legal_pts_2027 | 3 | Puntos del salario (masa del escenario con tope, 337 días) |
| M2_reduccion_cuna_legal_pts_2030 | 3 | Puntos del salario (masa del escenario con tope, 337 días) |
| M2_reduccion_cuna_legal_pts_2040 | 3 | Puntos del salario (masa del escenario con tope, 337 días) |
| M2_reduccion_cuna_legal_pts_2054 | 3 | Puntos del salario (masa del escenario con tope, 337 días) |
| M2_reduccion_cuna_legal_sem_2027 | 27.95 | % de los ingresos del SEM (Cuadro V.13) |
| M2_reduccion_cuna_legal_sem_2030 | 27.71 | % de los ingresos del SEM (Cuadro V.13) |
| M2_reduccion_cuna_legal_sem_2040 | 23.62 | % de los ingresos del SEM (Cuadro V.13) |
| M2_reduccion_cuna_legal_sem_2054 | 18.58 | % de los ingresos del SEM (Cuadro V.13) |
| M2_sinprov_libro_k1_primer_anio_sin_cobertura | 2,035 | sensibilidad_provisiones_masa.csv |
| M2_sinprov_libro_k2_primer_anio_sin_cobertura | 2,043 | sensibilidad_provisiones_masa.csv |
| M2_sinprov_libro_margen_2036 | -11,210 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M2_sinprov_libro_margen_2040 | -37,694 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M2_sinprov_libro_margen_min | -147,549 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M2_sinprov_libro_margen_min_anio | 2,054 | sensibilidad_provisiones_masa.csv |
| M2_sinprov_libro_vp_k1_deficit_no_cubierto | 755,864 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M2_sinprov_libro_vp_k2_deficit_no_cubierto | 607,575 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M2_sinprov_smasa_k1_primer_anio_sin_cobertura | 2,034 | sensibilidad_provisiones_masa.csv |
| M2_sinprov_smasa_k2_primer_anio_sin_cobertura | 2,040 | sensibilidad_provisiones_masa.csv |
| M2_sinprov_smasa_margen_2036 | -21,568 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M2_sinprov_smasa_margen_2040 | -48,556 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M2_sinprov_smasa_margen_min | -160,365 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M2_sinprov_smasa_margen_min_anio | 2,054 | sensibilidad_provisiones_masa.csv |
| M2_sinprov_smasa_vp_k1_deficit_no_cubierto | 891,400 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M2_sinprov_smasa_vp_k2_deficit_no_cubierto | 764,901 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M3_ENIGH_k1_pesos_por_dh65_2027 | 5,670 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_ENIGH_k1_pesos_por_dh65_2030 | 3,664 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_ENIGH_k1_pesos_por_dh65_2040 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_ENIGH_k1_pesos_por_dh65_2054 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_ENIGH_k1_pesos_por_dh80_2027 | 29,274 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_ENIGH_k1_pesos_por_dh80_2030 | 18,967 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_ENIGH_k1_pesos_por_dh80_2040 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_ENIGH_k1_pesos_por_dh80_2054 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_ENIGH_k2_pesos_por_dh65_2027 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_ENIGH_k2_pesos_por_dh65_2030 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_ENIGH_k2_pesos_por_dh65_2040 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_ENIGH_k2_pesos_por_dh65_2054 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_ENIGH_k2_pesos_por_dh80_2027 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_ENIGH_k2_pesos_por_dh80_2030 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_ENIGH_k2_pesos_por_dh80_2040 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_ENIGH_k2_pesos_por_dh80_2054 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_Informe_max_k1_pesos_por_dh65_2027 | 2,349 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_Informe_max_k1_pesos_por_dh65_2030 | 1,518 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_Informe_max_k1_pesos_por_dh65_2040 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_Informe_max_k1_pesos_por_dh65_2054 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_Informe_max_k1_pesos_por_dh80_2027 | 10,888 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_Informe_max_k1_pesos_por_dh80_2030 | 7,046 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_Informe_max_k1_pesos_por_dh80_2040 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_Informe_max_k1_pesos_por_dh80_2054 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_Informe_max_k2_pesos_por_dh65_2027 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_Informe_max_k2_pesos_por_dh65_2030 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_Informe_max_k2_pesos_por_dh65_2040 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_Informe_max_k2_pesos_por_dh65_2054 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_Informe_max_k2_pesos_por_dh80_2027 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_Informe_max_k2_pesos_por_dh80_2030 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_Informe_max_k2_pesos_por_dh80_2040 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_Informe_max_k2_pesos_por_dh80_2054 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| M3_conprov_libro_k1_primer_anio_sin_cobertura | 2,035 | sensibilidad_provisiones_masa.csv |
| M3_conprov_libro_k2_primer_anio_sin_cobertura | ninguno | sensibilidad_provisiones_masa.csv |
| M3_conprov_libro_margen_2036 | -5,398 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M3_conprov_libro_margen_2040 | -648 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M3_conprov_libro_margen_min | -35,712 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M3_conprov_libro_margen_min_anio | 2,054 | sensibilidad_provisiones_masa.csv |
| M3_conprov_libro_vp_k1_deficit_no_cubierto | 114,602 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M3_conprov_libro_vp_k2_deficit_no_cubierto | 0 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M3_conprov_smasa_k1_primer_anio_sin_cobertura | 2,034 | sensibilidad_provisiones_masa.csv |
| M3_conprov_smasa_k2_primer_anio_sin_cobertura | 2,046 | sensibilidad_provisiones_masa.csv |
| M3_conprov_smasa_margen_2036 | -16,937 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M3_conprov_smasa_margen_2040 | -13,435 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M3_conprov_smasa_margen_min | -54,018 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M3_conprov_smasa_margen_min_anio | 2,054 | sensibilidad_provisiones_masa.csv |
| M3_conprov_smasa_vp_k1_deficit_no_cubierto | 280,658 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M3_conprov_smasa_vp_k2_deficit_no_cubierto | 154,961 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M3_deficit_GMP_2027 | 74,968 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_deficit_GMP_2030 | 95,328 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_deficit_GMP_2040 | 155,531 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_deficit_GMP_2054 | 247,123 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_deficit_GMP_pts_2027 | 1.381 | Puntos del salario (masa del escenario con tope, 337 días) |
| M3_deficit_GMP_pts_2030 | 1.59 | Puntos del salario (masa del escenario con tope, 337 días) |
| M3_deficit_GMP_pts_2040 | 2.008 | Puntos del salario (masa del escenario con tope, 337 días) |
| M3_deficit_GMP_pts_2054 | 2.338 | Puntos del salario (masa del escenario con tope, 337 días) |
| M3_deficit_GMP_sem_2027 | 12.97 | % de los ingresos del SEM (Cuadro V.13) |
| M3_deficit_GMP_sem_2030 | 15.22 | % de los ingresos del SEM (Cuadro V.13) |
| M3_deficit_GMP_sem_2040 | 18.61 | % de los ingresos del SEM (Cuadro V.13) |
| M3_deficit_GMP_sem_2054 | 20.68 | % de los ingresos del SEM (Cuadro V.13) |
| M3_factor_masa_2027 | 0.9925 | Masa M3 / masa base |
| M3_factor_masa_2030 | 0.9661 | Masa M3 / masa base |
| M3_factor_masa_2040 | 0.8692 | Masa M3 / masa base |
| M3_factor_masa_2054 | 0.7693 | Masa M3 / masa base |
| M3_formalidad_2027 | 34.26 | Formalidad implícita del escenario M3 (%) |
| M3_formalidad_2030 | 35.23 | Formalidad M3 2030 (%) |
| M3_formalidad_2035 | 37.38 | Formalidad M3 2035 (%) |
| M3_formalidad_2040 | 40.02 | Formalidad implícita del escenario M3 (%) |
| M3_formalidad_2054 | 48.56 | Formalidad implícita del escenario M3 (%) |
| M3_holgura_min | -35,712 | Mínimo de ingreso − déficit de GMP, 2027-2054 (mdp de 2026) |
| M3_holgura_min_anio | 2,054 | Año de la holgura mínima |
| M3_holgura_min_pts | -0.338 | Holgura mínima en puntos del salario |
| M3_infonavit_5pct_teorico_2027 | 271,380 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_infonavit_5pct_teorico_2030 | 299,744 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_infonavit_5pct_teorico_2040 | 387,206 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_infonavit_5pct_teorico_2054 | 528,529 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_ingreso_NS_2027 | 108,552 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_ingreso_NS_2030 | 119,898 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_ingreso_NS_2040 | 154,882 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_ingreso_NS_2054 | 211,411 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_ingreso_NS_pts_2027 | 2 | Puntos del salario (masa del escenario con tope, 337 días) |
| M3_ingreso_NS_pts_2030 | 2 | Puntos del salario (masa del escenario con tope, 337 días) |
| M3_ingreso_NS_pts_2040 | 2 | Puntos del salario (masa del escenario con tope, 337 días) |
| M3_ingreso_NS_pts_2054 | 2 | Puntos del salario (masa del escenario con tope, 337 días) |
| M3_ingreso_NS_sem_2027 | 18.77 | % de los ingresos del SEM (Cuadro V.13) |
| M3_ingreso_NS_sem_2030 | 19.14 | % de los ingresos del SEM (Cuadro V.13) |
| M3_ingreso_NS_sem_2040 | 18.53 | % de los ingresos del SEM (Cuadro V.13) |
| M3_ingreso_NS_sem_2054 | 17.69 | % de los ingresos del SEM (Cuadro V.13) |
| M3_k1_anios_no_cubre | 19 | Años 2027-2054 con I < D |
| M3_k1_cubre_hasta | 2,034 | Último año cubierto antes del primero sin cobertura (K1) |
| M3_k1_deficit_no_cubierto_2027 | 0 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_k1_deficit_no_cubierto_2030 | 0 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_k1_deficit_no_cubierto_2040 | 648 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_k1_deficit_no_cubierto_2054 | 35,712 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_k1_deficit_no_cubierto_pts_2027 | 0 | Puntos del salario (masa del escenario con tope, 337 días) |
| M3_k1_deficit_no_cubierto_pts_2030 | 0 | Puntos del salario (masa del escenario con tope, 337 días) |
| M3_k1_deficit_no_cubierto_pts_2040 | 0.008 | Puntos del salario (masa del escenario con tope, 337 días) |
| M3_k1_deficit_no_cubierto_pts_2054 | 0.338 | Puntos del salario (masa del escenario con tope, 337 días) |
| M3_k1_deficit_no_cubierto_sem_2027 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| M3_k1_deficit_no_cubierto_sem_2030 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| M3_k1_deficit_no_cubierto_sem_2040 | 0.08 | % de los ingresos del SEM (Cuadro V.13) |
| M3_k1_deficit_no_cubierto_sem_2054 | 2.99 | % de los ingresos del SEM (Cuadro V.13) |
| M3_k1_primer_anio_no_cubre | 2,035 | Primer año en que I < D (K1) |
| M3_k1_remanente_cuidados_2027 | 33,584 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_k1_remanente_cuidados_2030 | 24,569 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_k1_remanente_cuidados_2040 | 0 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_k1_remanente_cuidados_2054 | 0 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_k1_remanente_cuidados_pts_2027 | 0.619 | Puntos del salario (masa del escenario con tope, 337 días) |
| M3_k1_remanente_cuidados_pts_2030 | 0.41 | Puntos del salario (masa del escenario con tope, 337 días) |
| M3_k1_remanente_cuidados_pts_2040 | 0 | Puntos del salario (masa del escenario con tope, 337 días) |
| M3_k1_remanente_cuidados_pts_2054 | 0 | Puntos del salario (masa del escenario con tope, 337 días) |
| M3_k1_remanente_cuidados_sem_2027 | 5.81 | % de los ingresos del SEM (Cuadro V.13) |
| M3_k1_remanente_cuidados_sem_2030 | 3.92 | % de los ingresos del SEM (Cuadro V.13) |
| M3_k1_remanente_cuidados_sem_2040 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| M3_k1_remanente_cuidados_sem_2054 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| M3_k2_cuidados_2027 | 0 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_k2_cuidados_2030 | 0 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_k2_cuidados_2040 | 0 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_k2_cuidados_2054 | 0 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_k2_cuidados_pts_2027 | 0 | Puntos del salario (masa del escenario con tope, 337 días) |
| M3_k2_cuidados_pts_2030 | 0 | Puntos del salario (masa del escenario con tope, 337 días) |
| M3_k2_cuidados_pts_2040 | 0 | Puntos del salario (masa del escenario con tope, 337 días) |
| M3_k2_cuidados_pts_2054 | 0 | Puntos del salario (masa del escenario con tope, 337 días) |
| M3_k2_cuidados_sem_2027 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| M3_k2_cuidados_sem_2030 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| M3_k2_cuidados_sem_2040 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| M3_k2_cuidados_sem_2054 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| M3_k2_primer_anio_no_cubre | ninguno | Primer año con déficit no cubierto tras usar la reserva (K2) |
| M3_k2_reserva_fin_2027 | 33,584 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_k2_reserva_fin_2030 | 121,577 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_k2_reserva_fin_2040 | 211,449 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_k2_reserva_fin_2054 | 68,993 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_k2_reserva_inicio_2035 | 191,144 | Reserva K2 al inicio de 2035 |
| M3_k2_reserva_max | 217,030 | Reserva máxima K2 (mdp de 2026) |
| M3_k2_reserva_max_anio | 2,044 | Año de la reserva máxima K2 |
| M3_k2_retiro_anual | 9,557 | 1/20 de la reserva al inicio de 2035 (mdp de 2026) |
| M3_k2cambio_cuidados_2040_antes_v11 | 9,557 | k2_cambios_v11_v12.csv |
| M3_k2cambio_cuidados_2040_despues_v12 | 0 | k2_cambios_v11_v12.csv |
| M3_k2cambio_cuidados_2054_antes_v11 | 0 | k2_cambios_v11_v12.csv |
| M3_k2cambio_cuidados_2054_despues_v12 | 0 | k2_cambios_v11_v12.csv |
| M3_k2cambio_primer_antes_v11 | 2,051 | k2_cambios_v11_v12.csv |
| M3_k2cambio_primer_despues_v12 | ninguno | k2_cambios_v11_v12.csv |
| M3_k2cambio_reserva_2054_antes_v11 | 0 | k2_cambios_v11_v12.csv |
| M3_k2cambio_reserva_2054_despues_v12 | 68,993 | k2_cambios_v11_v12.csv |
| M3_k2cambio_vp_cuidados_antes_v11 | 90,603 | k2_cambios_v11_v12.csv |
| M3_k2cambio_vp_cuidados_despues_v12 | 6,498 | k2_cambios_v11_v12.csv |
| M3_k2cambio_vp_no_cubierto_antes_v11 | 53,950 | k2_cambios_v11_v12.csv |
| M3_k2cambio_vp_no_cubierto_despues_v12 | 0 | k2_cambios_v11_v12.csv |
| M3_k2v11_anios_faltante_con_pago | 15 | k2_v11_anios_con_faltante.csv |
| M3_k2v11_pago_cuidados_con_faltante | 134,154 | Σ pagos a cuidados de la v1.1 en años con faltante |
| M3_k2v12_agotamiento | no se agota | reserva_K2.csv |
| M3_k2v12_retiros_GMP | 227,552 | reserva_K2.csv, Σ 2035-2054 |
| M3_k2v12_retiros_cuidados | 9,557 | reserva_K2.csv, Σ 2035-2054 |
| M3_k2v12_saldo_cierre_2054 | 68,993 | reserva_K2.csv |
| M3_k2v12_saldo_inicio_2035 | 191,144 | reserva_K2.csv, mdp de 2026 |
| M3_k2v12_saldo_inicio_2040 | 205,920 | reserva_K2.csv, mdp de 2026 |
| M3_k2v12_saldo_inicio_2045 | 217,030 | reserva_K2.csv, mdp de 2026 |
| M3_k2v12_saldo_inicio_2050 | 186,168 | reserva_K2.csv, mdp de 2026 |
| M3_k2v12_saldo_inicio_2054 | 101,655 | reserva_K2.csv, mdp de 2026 |
| M3_margen_sin_prov_2036 | 14,179 | Margen sin provisiones en 2036 |
| M3_margen_sin_prov_min | -35,167 | Mínimo de ingreso − (déficit − provisiones de GMP), 2027-2054 |
| M3_margen_sin_prov_min_anio | 2,054 | Año del margen mínimo sin provisiones |
| M3_masa_tope25_2027 | 5,427,607 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_masa_tope25_2030 | 5,994,882 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_masa_tope25_2040 | 7,744,116 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_masa_tope25_2054 | 10,570,571 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_reduccion_cuna_legal_2027 | 162,828 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_reduccion_cuna_legal_2030 | 179,846 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_reduccion_cuna_legal_2040 | 232,323 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_reduccion_cuna_legal_2054 | 317,117 | ingreso_vs_GMP.csv, M3, mdp de 2026 |
| M3_reduccion_cuna_legal_pts_2027 | 3 | Puntos del salario (masa del escenario con tope, 337 días) |
| M3_reduccion_cuna_legal_pts_2030 | 3 | Puntos del salario (masa del escenario con tope, 337 días) |
| M3_reduccion_cuna_legal_pts_2040 | 3 | Puntos del salario (masa del escenario con tope, 337 días) |
| M3_reduccion_cuna_legal_pts_2054 | 3 | Puntos del salario (masa del escenario con tope, 337 días) |
| M3_reduccion_cuna_legal_sem_2027 | 28.16 | % de los ingresos del SEM (Cuadro V.13) |
| M3_reduccion_cuna_legal_sem_2030 | 28.71 | % de los ingresos del SEM (Cuadro V.13) |
| M3_reduccion_cuna_legal_sem_2040 | 27.8 | % de los ingresos del SEM (Cuadro V.13) |
| M3_reduccion_cuna_legal_sem_2054 | 26.54 | % de los ingresos del SEM (Cuadro V.13) |
| M3_sinprov_libro_k1_primer_anio_sin_cobertura | 2,042 | sensibilidad_provisiones_masa.csv |
| M3_sinprov_libro_k2_primer_anio_sin_cobertura | ninguno | sensibilidad_provisiones_masa.csv |
| M3_sinprov_libro_margen_2036 | 14,179 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M3_sinprov_libro_margen_2040 | 3,700 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M3_sinprov_libro_margen_min | -35,167 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M3_sinprov_libro_margen_min_anio | 2,054 | sensibilidad_provisiones_masa.csv |
| M3_sinprov_libro_vp_k1_deficit_no_cubierto | 99,808 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M3_sinprov_libro_vp_k2_deficit_no_cubierto | 0 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M3_sinprov_smasa_k1_primer_anio_sin_cobertura | 2,037 | sensibilidad_provisiones_masa.csv |
| M3_sinprov_smasa_k2_primer_anio_sin_cobertura | 2,052 | sensibilidad_provisiones_masa.csv |
| M3_sinprov_smasa_margen_2036 | 2,640 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M3_sinprov_smasa_margen_2040 | -9,087 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M3_sinprov_smasa_margen_min | -53,474 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M3_sinprov_smasa_margen_min_anio | 2,054 | sensibilidad_provisiones_masa.csv |
| M3_sinprov_smasa_vp_k1_deficit_no_cubierto | 225,331 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| M3_sinprov_smasa_vp_k2_deficit_no_cubierto | 59,216 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| MH_anios_con_tope | 2 | Años en que el tope en la base es activo |
| MH_formalidad_2030 | 35.63 | Formalidad MH 2030 (%) |
| MH_formalidad_2035 | 37.27 | Formalidad MH 2035 (%) |
| MH_formalidad_2054 | 43.49 | Formalidad de MH en 2054 (%) |
| MH_paso_pts_anio | 0.3274 | (razón 2025 − razón 2005) / 20, serie histórica de la v1.2 |
| MH_sin_tope_2026 | 34.32 | MH sin tope, 2026 (%) |
| RT_prima_cuna | 1.9078 | Prima de RT en el Cuadro X-2.2 (Informe, Cuadro A.3) |
| SEM_V13_menos_libro_2026 | 9,232 | Ingresos del SEM: Cuadro V.13 − libro (SEM-A + SEM-GMP), mdp |
| SEM_V13_menos_libro_2030 | 15,148 | Ingresos del SEM: Cuadro V.13 − libro (SEM-A + SEM-GMP), mdp |
| SEM_V13_menos_libro_2040 | 2,620 | Ingresos del SEM: Cuadro V.13 − libro (SEM-A + SEM-GMP), mdp |
| SEM_V13_menos_libro_2054 | -11,640 | Ingresos del SEM: Cuadro V.13 − libro (SEM-A + SEM-GMP), mdp |
| SEM_V13_menos_libro_pct_2026 | 1.67 | Idem, % del libro |
| SEM_V13_menos_libro_pct_2030 | 2.48 | Idem, % del libro |
| SEM_V13_menos_libro_pct_2040 | 0.31 | Idem, % del libro |
| SEM_V13_menos_libro_pct_2054 | -0.96 | Idem, % del libro |
| SEM_ingresos_2027 | 578,176 | Informe, Cuadro V.13, interpolación lineal |
| SEM_ingresos_2030 | 626,325 | Informe, Cuadro V.13, interpolación lineal |
| SEM_ingresos_2040 | 835,679 | Informe, Cuadro V.13, interpolación lineal |
| SEM_ingresos_2054 | 1,194,783 | Informe, Cuadro V.13, interpolación lineal |
| SEM_ingresos_libro_2027 | 561,611 | Libro de Finanzas, SEM-A + SEM-GMP |
| SEM_ingresos_libro_2030 | 611,178 | Libro de Finanzas, SEM-A + SEM-GMP |
| SEM_ingresos_libro_2040 | 833,059 | Libro de Finanzas, SEM-A + SEM-GMP |
| SEM_ingresos_libro_2054 | 1,206,423 | Libro de Finanzas, SEM-A + SEM-GMP |
| VP_M2_deficit | 3,133,192 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M2_ingreso | 2,404,562 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M2_k1_no_cubierto | 831,627 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M2_k1_remanente | 102,997 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M2_k2_cuidados | 0 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M2_k2_no_cubierto | 728,630 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M2_k2_reserva_final | 0 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M2_masa | 120,228,094 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M2_reduccion | 3,606,843 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M3_deficit | 2,798,304 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M3_ingreso | 2,834,957 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M3_k1_no_cubierto | 114,602 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M3_k1_remanente | 151,254 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M3_k2_cuidados | 6,498 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M3_k2_no_cubierto | 0 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M3_k2_reserva_final | 30,155 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M3_masa | 141,747,834 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_M3_reduccion | 4,252,435 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_base_deficit | 2,463,416 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_base_ingreso | 3,265,351 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_base_k1_no_cubierto | 0 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_base_k1_remanente | 801,935 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_base_k2_cuidados | 747,074 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_base_k2_no_cubierto | 0 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_base_k2_reserva_final | 54,861 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_base_masa | 163,267,574 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| VP_base_reduccion | 4,898,027 | valor_presente.csv, 2027-2054, 3 % real, mdp de 2026 |
| base_ENIGH_k1_pesos_por_dh65_2027 | 5,927 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_ENIGH_k1_pesos_por_dh65_2030 | 4,806 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_ENIGH_k1_pesos_por_dh65_2040 | 4,224 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_ENIGH_k1_pesos_por_dh65_2054 | 5,689 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_ENIGH_k1_pesos_por_dh80_2027 | 30,602 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_ENIGH_k1_pesos_por_dh80_2030 | 24,875 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_ENIGH_k1_pesos_por_dh80_2040 | 19,744 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_ENIGH_k1_pesos_por_dh80_2054 | 20,197 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_ENIGH_k2_pesos_por_dh65_2027 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_ENIGH_k2_pesos_por_dh65_2030 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_ENIGH_k2_pesos_por_dh65_2040 | 5,631 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_ENIGH_k2_pesos_por_dh65_2054 | 6,696 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_ENIGH_k2_pesos_por_dh80_2027 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_ENIGH_k2_pesos_por_dh80_2030 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_ENIGH_k2_pesos_por_dh80_2040 | 26,318 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_ENIGH_k2_pesos_por_dh80_2054 | 23,771 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_Informe_max_k1_pesos_por_dh65_2027 | 2,456 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_Informe_max_k1_pesos_por_dh65_2030 | 1,991 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_Informe_max_k1_pesos_por_dh65_2040 | 1,746 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_Informe_max_k1_pesos_por_dh65_2054 | 2,322 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_Informe_max_k1_pesos_por_dh80_2027 | 11,382 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_Informe_max_k1_pesos_por_dh80_2030 | 9,241 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_Informe_max_k1_pesos_por_dh80_2040 | 7,336 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_Informe_max_k1_pesos_por_dh80_2054 | 7,453 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_Informe_max_k2_pesos_por_dh65_2027 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_Informe_max_k2_pesos_por_dh65_2030 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_Informe_max_k2_pesos_por_dh65_2040 | 2,327 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_Informe_max_k2_pesos_por_dh65_2054 | 2,733 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_Informe_max_k2_pesos_por_dh80_2027 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_Informe_max_k2_pesos_por_dh80_2030 | 0 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_Informe_max_k2_pesos_por_dh80_2040 | 9,779 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_Informe_max_k2_pesos_por_dh80_2054 | 8,772 | remanente_por_mayor.csv, pesos de 2026 por persona al año |
| base_conprov_libro_k1_primer_anio_sin_cobertura | ninguno | sensibilidad_provisiones_masa.csv |
| base_conprov_libro_k2_primer_anio_sin_cobertura | ninguno | sensibilidad_provisiones_masa.csv |
| base_conprov_libro_margen_2036 | 19,991 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| base_conprov_libro_margen_2040 | 40,745 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| base_conprov_libro_margen_min | 19,991 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| base_conprov_libro_margen_min_anio | 2,036 | sensibilidad_provisiones_masa.csv |
| base_conprov_libro_vp_k1_deficit_no_cubierto | 0 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| base_conprov_libro_vp_k2_deficit_no_cubierto | 0 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| base_conprov_smasa_k1_primer_anio_sin_cobertura | ninguno | sensibilidad_provisiones_masa.csv |
| base_conprov_smasa_k2_primer_anio_sin_cobertura | ninguno | sensibilidad_provisiones_masa.csv |
| base_conprov_smasa_margen_2036 | 7,272 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| base_conprov_smasa_margen_2040 | 26,034 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| base_conprov_smasa_margen_min | 7,272 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| base_conprov_smasa_margen_min_anio | 2,036 | sensibilidad_provisiones_masa.csv |
| base_conprov_smasa_vp_k1_deficit_no_cubierto | 0 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| base_conprov_smasa_vp_k2_deficit_no_cubierto | 0 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| base_deficit_GMP_2027 | 74,270 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_deficit_GMP_2030 | 91,888 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_deficit_GMP_2040 | 137,449 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_deficit_GMP_2054 | 198,154 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_deficit_GMP_pts_2027 | 1.358 | Puntos del salario (masa del escenario con tope, 337 días) |
| base_deficit_GMP_pts_2030 | 1.481 | Puntos del salario (masa del escenario con tope, 337 días) |
| base_deficit_GMP_pts_2040 | 1.543 | Puntos del salario (masa del escenario con tope, 337 días) |
| base_deficit_GMP_pts_2054 | 1.442 | Puntos del salario (masa del escenario con tope, 337 días) |
| base_deficit_GMP_sem_2027 | 12.85 | % de los ingresos del SEM (Cuadro V.13) |
| base_deficit_GMP_sem_2030 | 14.67 | % de los ingresos del SEM (Cuadro V.13) |
| base_deficit_GMP_sem_2040 | 16.45 | % de los ingresos del SEM (Cuadro V.13) |
| base_deficit_GMP_sem_2054 | 16.58 | % de los ingresos del SEM (Cuadro V.13) |
| base_factor_masa_2027 | 1 | Masa base / masa base |
| base_factor_masa_2030 | 1 | Masa base / masa base |
| base_factor_masa_2040 | 1 | Masa base / masa base |
| base_factor_masa_2054 | 1 | Masa base / masa base |
| base_formalidad_2026 | 34.08 | Formalidad base, 2026 (%) |
| base_formalidad_2027 | 34.52 | Formalidad implícita del escenario base (%) |
| base_formalidad_2030 | 36.47 | Formalidad implícita del escenario base (%) |
| base_formalidad_2040 | 46.04 | Formalidad implícita del escenario base (%) |
| base_formalidad_2054 | 63.13 | Formalidad implícita del escenario base (%) |
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
| base_ingreso_NS_pts_2027 | 2 | Puntos del salario (masa del escenario con tope, 337 días) |
| base_ingreso_NS_pts_2030 | 2 | Puntos del salario (masa del escenario con tope, 337 días) |
| base_ingreso_NS_pts_2040 | 2 | Puntos del salario (masa del escenario con tope, 337 días) |
| base_ingreso_NS_pts_2054 | 2 | Puntos del salario (masa del escenario con tope, 337 días) |
| base_ingreso_NS_sem_2027 | 18.92 | % de los ingresos del SEM (Cuadro V.13) |
| base_ingreso_NS_sem_2030 | 19.82 | % de los ingresos del SEM (Cuadro V.13) |
| base_ingreso_NS_sem_2040 | 21.32 | % de los ingresos del SEM (Cuadro V.13) |
| base_ingreso_NS_sem_2054 | 23 | % de los ingresos del SEM (Cuadro V.13) |
| base_k1_anios_no_cubre | 0 | Años 2027-2054 con I < D |
| base_k1_cubre_hasta | 2,054 | Último año cubierto antes del primero sin cobertura (K1) |
| base_k1_deficit_no_cubierto_2027 | 0 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k1_deficit_no_cubierto_2030 | 0 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k1_deficit_no_cubierto_2040 | 0 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k1_deficit_no_cubierto_2054 | 0 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k1_deficit_no_cubierto_pts_2027 | 0 | Puntos del salario (masa del escenario con tope, 337 días) |
| base_k1_deficit_no_cubierto_pts_2030 | 0 | Puntos del salario (masa del escenario con tope, 337 días) |
| base_k1_deficit_no_cubierto_pts_2040 | 0 | Puntos del salario (masa del escenario con tope, 337 días) |
| base_k1_deficit_no_cubierto_pts_2054 | 0 | Puntos del salario (masa del escenario con tope, 337 días) |
| base_k1_deficit_no_cubierto_sem_2027 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| base_k1_deficit_no_cubierto_sem_2030 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| base_k1_deficit_no_cubierto_sem_2040 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| base_k1_deficit_no_cubierto_sem_2054 | 0 | % de los ingresos del SEM (Cuadro V.13) |
| base_k1_primer_anio_no_cubre | ninguno | Primer año en que I < D (K1) |
| base_k1_remanente_cuidados_2027 | 35,107 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k1_remanente_cuidados_2030 | 32,222 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k1_remanente_cuidados_2040 | 40,745 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k1_remanente_cuidados_2054 | 76,670 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k1_remanente_cuidados_pts_2027 | 0.642 | Puntos del salario (masa del escenario con tope, 337 días) |
| base_k1_remanente_cuidados_pts_2030 | 0.519 | Puntos del salario (masa del escenario con tope, 337 días) |
| base_k1_remanente_cuidados_pts_2040 | 0.457 | Puntos del salario (masa del escenario con tope, 337 días) |
| base_k1_remanente_cuidados_pts_2054 | 0.558 | Puntos del salario (masa del escenario con tope, 337 días) |
| base_k1_remanente_cuidados_sem_2027 | 6.07 | % de los ingresos del SEM (Cuadro V.13) |
| base_k1_remanente_cuidados_sem_2030 | 5.14 | % de los ingresos del SEM (Cuadro V.13) |
| base_k1_remanente_cuidados_sem_2040 | 4.88 | % de los ingresos del SEM (Cuadro V.13) |
| base_k1_remanente_cuidados_sem_2054 | 6.42 | % de los ingresos del SEM (Cuadro V.13) |
| base_k2_cuidados_2027 | 0 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k2_cuidados_2030 | 0 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k2_cuidados_2040 | 54,312 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k2_cuidados_2054 | 90,237 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_k2_cuidados_pts_2027 | 0 | Puntos del salario (masa del escenario con tope, 337 días) |
| base_k2_cuidados_pts_2030 | 0 | Puntos del salario (masa del escenario con tope, 337 días) |
| base_k2_cuidados_pts_2040 | 0.61 | Puntos del salario (masa del escenario con tope, 337 días) |
| base_k2_cuidados_pts_2054 | 0.657 | Puntos del salario (masa del escenario con tope, 337 días) |
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
| base_k2cambio_cuidados_2040_antes_v11 | 54,312 | k2_cambios_v11_v12.csv |
| base_k2cambio_cuidados_2040_despues_v12 | 54,312 | k2_cambios_v11_v12.csv |
| base_k2cambio_cuidados_2054_antes_v11 | 90,237 | k2_cambios_v11_v12.csv |
| base_k2cambio_cuidados_2054_despues_v12 | 90,237 | k2_cambios_v11_v12.csv |
| base_k2cambio_primer_antes_v11 | ninguno | k2_cambios_v11_v12.csv |
| base_k2cambio_primer_despues_v12 | ninguno | k2_cambios_v11_v12.csv |
| base_k2cambio_reserva_2054_antes_v11 | 125,518 | k2_cambios_v11_v12.csv |
| base_k2cambio_reserva_2054_despues_v12 | 125,518 | k2_cambios_v11_v12.csv |
| base_k2cambio_vp_cuidados_antes_v11 | 747,074 | k2_cambios_v11_v12.csv |
| base_k2cambio_vp_cuidados_despues_v12 | 747,074 | k2_cambios_v11_v12.csv |
| base_k2cambio_vp_no_cubierto_antes_v11 | 0 | k2_cambios_v11_v12.csv |
| base_k2cambio_vp_no_cubierto_despues_v12 | 0 | k2_cambios_v11_v12.csv |
| base_k2v11_anios_faltante_con_pago | 0 | k2_v11_anios_con_faltante.csv |
| base_k2v11_pago_cuidados_con_faltante | 0 | Σ pagos a cuidados de la v1.1 en años con faltante |
| base_k2v12_agotamiento | no se agota | reserva_K2.csv |
| base_k2v12_retiros_GMP | 0 | reserva_K2.csv, Σ 2035-2054 |
| base_k2v12_retiros_cuidados | 271,337 | reserva_K2.csv, Σ 2035-2054 |
| base_k2v12_saldo_cierre_2054 | 125,518 | reserva_K2.csv |
| base_k2v12_saldo_inicio_2035 | 271,337 | reserva_K2.csv, mdp de 2026 |
| base_k2v12_saldo_inicio_2040 | 242,526 | reserva_K2.csv, mdp de 2026 |
| base_k2v12_saldo_inicio_2045 | 209,125 | reserva_K2.csv, mdp de 2026 |
| base_k2v12_saldo_inicio_2050 | 170,405 | reserva_K2.csv, mdp de 2026 |
| base_k2v12_saldo_inicio_2054 | 135,034 | reserva_K2.csv, mdp de 2026 |
| base_margen_sin_prov_2036 | 39,568 | Margen sin provisiones en 2036 |
| base_margen_sin_prov_min | 37,200 | Mínimo de ingreso − (déficit − provisiones de GMP), 2027-2054 |
| base_margen_sin_prov_min_anio | 2,027 | Año del margen mínimo sin provisiones |
| base_masa_tope25_2027 | 5,468,877 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_masa_tope25_2030 | 6,205,467 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_masa_tope25_2040 | 8,909,700 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_masa_tope25_2054 | 13,741,181 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_reduccion_cuna_legal_2027 | 164,066 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_reduccion_cuna_legal_2030 | 186,164 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_reduccion_cuna_legal_2040 | 267,291 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_reduccion_cuna_legal_2054 | 412,235 | ingreso_vs_GMP.csv, base, mdp de 2026 |
| base_reduccion_cuna_legal_pts_2027 | 3 | Puntos del salario (masa del escenario con tope, 337 días) |
| base_reduccion_cuna_legal_pts_2030 | 3 | Puntos del salario (masa del escenario con tope, 337 días) |
| base_reduccion_cuna_legal_pts_2040 | 3 | Puntos del salario (masa del escenario con tope, 337 días) |
| base_reduccion_cuna_legal_pts_2054 | 3 | Puntos del salario (masa del escenario con tope, 337 días) |
| base_reduccion_cuna_legal_sem_2027 | 28.38 | % de los ingresos del SEM (Cuadro V.13) |
| base_reduccion_cuna_legal_sem_2030 | 29.72 | % de los ingresos del SEM (Cuadro V.13) |
| base_reduccion_cuna_legal_sem_2040 | 31.98 | % de los ingresos del SEM (Cuadro V.13) |
| base_reduccion_cuna_legal_sem_2054 | 34.5 | % de los ingresos del SEM (Cuadro V.13) |
| base_sinprov_libro_k1_primer_anio_sin_cobertura | ninguno | sensibilidad_provisiones_masa.csv |
| base_sinprov_libro_k2_primer_anio_sin_cobertura | ninguno | sensibilidad_provisiones_masa.csv |
| base_sinprov_libro_margen_2036 | 39,568 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| base_sinprov_libro_margen_2040 | 45,093 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| base_sinprov_libro_margen_min | 37,200 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| base_sinprov_libro_margen_min_anio | 2,027 | sensibilidad_provisiones_masa.csv |
| base_sinprov_libro_vp_k1_deficit_no_cubierto | 0 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| base_sinprov_libro_vp_k2_deficit_no_cubierto | 0 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| base_sinprov_smasa_k1_primer_anio_sin_cobertura | ninguno | sensibilidad_provisiones_masa.csv |
| base_sinprov_smasa_k2_primer_anio_sin_cobertura | ninguno | sensibilidad_provisiones_masa.csv |
| base_sinprov_smasa_margen_2036 | 26,849 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| base_sinprov_smasa_margen_2040 | 30,382 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| base_sinprov_smasa_margen_min | 26,849 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| base_sinprov_smasa_margen_min_anio | 2,036 | sensibilidad_provisiones_masa.csv |
| base_sinprov_smasa_vp_k1_deficit_no_cubierto | 0 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| base_sinprov_smasa_vp_k2_deficit_no_cubierto | 0 | sensibilidad_provisiones_masa.csv, mdp de 2026 |
| chk12_00 | 0 | 8.1 regresión v1.1: ingreso_vs_GMP (máx. desviación) |
| chk12_01 | 0 | 8.1 regresión v1.1: valor_presente (máx. desviación) |
| chk12_02 | 0 | 8.1 regresión v1.1: remanente_por_mayor (máx. desviación) |
| chk12_03 | 0 | 8.1 regresión v1.1: resumen_escenarios (máx. desviación) |
| chk12_04 | 0 | 8.2 años con déficit sin provisiones > con provisiones |
| chk12_05 | 0 | 8.2 déficit con provisiones frente a la v1.1 (máx. desviación, mdp) |
| chk12_06 | 0 | 8.3 S-masa: ingreso 2027 = ingreso base 2027 (desviación, mdp) |
| chk12_07 | 0 | 8.3 S-masa: razón ingreso nuevo / ingreso GMP constante en la base (rango) |
| chk12_08 | 0 | 8.4 K2: años con faltante de GMP y retiro para cuidados |
| chk12_09 | 0 | 8.4 K2: identidad de la reserva (máx. desviación, mdp) |
| chk13_00 | 0 | 6.1 regresión v1.2: ingreso_vs_GMP (máx. desviación) |
| chk13_01 | 0 | 6.1 regresión v1.2: valor_presente (máx. desviación) |
| chk13_02 | 0 | 6.1 regresión v1.2: remanente_por_mayor (máx. desviación) |
| chk13_03 | 0 | 6.1 regresión v1.2: resumen_escenarios (máx. desviación) |
| chk13_04 | 0 | 6.1 regresión v1.2: sensibilidad_provisiones_masa (máx. desviación) |
| chk13_05 | 0 | 6.1 regresión v1.2: reserva_K2 (máx. desviación) |
| chk13_06 | 0 | 6.2 resumen K2/K1 frente a la v1.2 (máx. desviación, mdp) |
| chk13_07 | 0 | 6.2 fechas que no corresponden a la v1.2 (primer año sin cobertura − 1) |
| chk13_08 | 0 | 6.3 MH ≤ base en todos los años (años que fallan) |
| chk13_09 | 0 | 6.3 MH entre M2 y M3, 2035-2054: formalidad (años que fallan) |
| chk13_10 | 9 | 6.3 MH por encima de M3, 2026-2034 (años; informativo) |
| chk13_11 | 0 | 6.3 MH entre M2 y M3, 2035-2054: masa y déficit ajustado (años que fallan) |
| chk13_12 | 0 | 6.3 último año con cobertura de MH entre M2 y M3 (columnas que fallan) |
| chk13_13 | 0 | 6.4 reserva final en VP = (inicio 2054 + movimiento 2054) descontada a 2026 (máx. desviación) |
| chk13_14 | 0 | 6.4 reserva final en K1 (máximo) |
| chk_00_3.1 | 0 | 3.1 masa con tope = base de la tasa D2 de la v1.2 (máx. desviación relativa) |
| chk_01_3.1 | 1.02267 | 3.1 masa con tope / denominador anterior de la v1.2, 2027 (razón) |
| chk_02_3.1 | 1.01399 | 3.1 masa con tope / denominador anterior de la v1.2, 2054 (razón) |
| chk_03_3.1 | 1.736048 | 3.1 proporción de la masa por encima del tope, 2027 (%) |
| chk_04_3.1 | 2.7145 | 3.1 proporción de la masa por encima del tope, 2054 (%) |
| chk_05_3.2 | 0 | 3.2 Cuadro V.24 transcrito = PDF (celdas distintas) |
| chk_06_3.2 | 0 | 3.2 interpolación preserva los años ancla (máx. desviación, mdp) |
| chk_07_3.2 | -0.498724 | 3.2 VP del déficit interpolado frente al Cuadro V.24 (%) |
| chk_08_3.3 | -1.178311 | 3.3 VP 2 % × masa propia frente a 2 % × volumen del Informe, mismo horizonte (%) |
| chk_09_3.4 | 0 | 3.4 identidad de la reserva (máx. desviación, mdp) |
| chk_10_7.2 | 0 | 7.2 base: déficit ajustado = Cuadro V.24 (máx. desviación, mdp) |
| chk_11_7.2 | 0 | 7.2 déficit M2 > M3 > base en años con ganancia de formalización (años que fallan) |
| chk_12_7.3 | 46.552264 | 7.3 base ENIGH de 65+ / población nacional de 65+, máximo 2027-2054 (%) |
| chk_13_7.1 | 0 | 7.1 regresión v1.0: ingreso_vs_GMP (máx. desviación) |
| chk_14_7.1 | 0 | 7.1 regresión v1.0: valor_presente (máx. desviación) |
| chk_15_7.1 | 0 | 7.1 regresión v1.0: remanente_por_mayor (máx. desviación) |
| chk_3.6 | 0 | 3.6/6.7 apariciones de 2055 en las tablas |
| chk_cuna_0 | 0 | 3.5/7.5 (b) = (a) − 3 puntos en todo nivel hasta 25 UMA (máx. desviación, puntos) |
| chk_cuna_1 | 0 | 3.5 tasas de cesantía y vejez fuera de la tabla de 1.5 (casos) |
| chk_cuna_2 | 0 | 3.5 tabla 2030 = art. 168 fr. II a) del DOF 16-12-2020 (celdas distintas) |
| chk_cuna_3 | 0 | 7.1 regresión v1.0: cuna_legal_por_salario (máx. desviación) |
| chk_cuna_4 | 0 | 8.1 regresión v1.1: cuna_legal_por_salario (máx. desviación) |
| chk_cuna_5 | 0 | 8.6 cuña sin aportación federal ≥ cuña con ella (niveles que fallan) |
| chk_exp1_0 | 0 | 7.4 experimento 1: montos en mdp de resultados_v12 sin cambio (máx. desviación) |
| chk_exp1_1 | 0 | 8.1 regresión v1.1: exp1_cambios_denominador (máx. desviación) |
| chk_exp1_2 | 0 | 7.4 experimento 1: cifras cambiadas que no son puntos ni % del SEM |
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
| cuna_2026_1.01 SM, lectura por UMA_patron_a | 26.956 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, lectura por UMA_patron_b | 23.956 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, lectura por UMA_patron_c | 19.901 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, lectura por UMA_sinfed_a | 29.331 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_1.01 SM, lectura por UMA_sinfed_b | 26.331 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_1.01 SM, lectura por UMA_sinfed_c | 22.276 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_1.01 SM, lectura por UMA_total_a | 37.911 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, lectura por UMA_total_b | 34.911 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, lectura por UMA_total_c | 30.856 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_cyv_a | 3.676 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_cyv_b | 3.676 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_cyv_c | 3.676 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_federal_a | 9.411 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_federal_b | 9.411 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_federal_c | 9.411 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_obrera_a | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_obrera_b | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_obrera_c | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_patron_a | 24.606 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_patron_b | 21.606 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_patron_c | 17.551 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_sinfed_a | 26.981 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_sinfed_b | 23.981 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_sinfed_c | 19.926 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_total_a | 36.392 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_total_b | 33.392 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_1.01 SM, primer tramo tras el mínimo_total_c | 29.337 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_cyv_a | 7.513 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_cyv_b | 7.513 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_cyv_c | 7.513 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_federal_a | 1.733 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_federal_b | 1.733 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_federal_c | 1.733 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_obrera_a | 2.655 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_obrera_b | 2.655 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_obrera_c | 2.655 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_patron_a | 23.731 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_patron_b | 20.731 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_patron_c | 22.158 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_sinfed_a | 26.386 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_10 UMA_sinfed_b | 23.386 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_10 UMA_sinfed_c | 24.813 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_10 UMA_total_a | 28.119 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_total_b | 25.119 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_10 UMA_total_c | 26.546 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_cyv_a | 4.851 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_cyv_b | 4.851 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_cyv_c | 4.851 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_federal_a | 12.296 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_federal_b | 12.296 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_federal_c | 12.296 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_obrera_a | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_obrera_b | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_obrera_c | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_patron_a | 28.459 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_patron_b | 25.459 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_patron_c | 18.726 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_sinfed_a | 30.834 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_2 UMA_sinfed_b | 27.834 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_2 UMA_sinfed_c | 21.101 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_2 UMA_total_a | 43.13 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_total_b | 40.13 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_2 UMA_total_c | 33.397 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_cyv_a | 7.513 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_cyv_b | 7.513 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_cyv_c | 7.513 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_federal_a | 0.843 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_federal_b | 0.843 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_federal_c | 0.843 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_obrera_a | 2.727 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_obrera_b | 2.727 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_obrera_c | 2.727 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_patron_a | 22.705 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_patron_b | 19.705 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_patron_c | 22.356 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_sinfed_a | 25.432 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_25 UMA_sinfed_b | 22.432 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_25 UMA_sinfed_c | 25.083 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_25 UMA_total_a | 26.275 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_total_b | 23.275 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25 UMA_total_c | 25.926 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_25uma_c_menos_a | -0.349 | Cambio de la cuña legal a cargo del patrón, (c) − (a), puntos del SBC |
| cuna_2026_25uma_c_menos_b | 2.651 | (c) − (b) en 25 UMA: efecto de D2 en salarios altos |
| cuna_2026_3 UMA_cyv_a | 6.026 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_cyv_b | 6.026 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_cyv_c | 6.026 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_federal_a | 7.78 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_federal_b | 7.78 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_federal_c | 7.78 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_obrera_a | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_obrera_b | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_obrera_c | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_patron_a | 26.234 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_patron_b | 23.234 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_patron_c | 19.901 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_sinfed_a | 28.609 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_3 UMA_sinfed_b | 25.609 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_3 UMA_sinfed_c | 22.276 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_3 UMA_total_a | 36.389 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_total_b | 33.389 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_3 UMA_total_c | 30.056 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_cyv_a | 6.613 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_cyv_b | 6.613 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_cyv_c | 6.613 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_federal_a | 5.522 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_federal_b | 5.522 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_federal_c | 5.522 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_obrera_a | 2.475 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_obrera_b | 2.475 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_obrera_c | 2.475 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_patron_a | 25.396 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_patron_b | 22.396 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_patron_c | 20.763 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_sinfed_a | 27.871 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_4 UMA_sinfed_b | 24.871 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_4 UMA_sinfed_c | 23.238 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_4 UMA_total_a | 33.393 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_total_b | 30.393 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_4 UMA_total_c | 28.76 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_cyv_a | 7.513 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_cyv_b | 7.513 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_cyv_c | 7.513 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_federal_a | 2.922 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_federal_b | 2.922 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_federal_c | 2.922 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_obrera_a | 2.559 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_obrera_b | 2.559 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_obrera_c | 2.559 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_patron_a | 25.102 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_patron_b | 22.102 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_patron_c | 21.893 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_sinfed_a | 27.661 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_5.55 UMA_sinfed_b | 24.661 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_5.55 UMA_sinfed_c | 24.452 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_5.55 UMA_total_a | 30.583 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_total_b | 27.583 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_5.55 UMA_total_c | 27.374 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_cyv_a | 3.15 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_cyv_b | 3.15 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_cyv_c | 3.15 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_federal_a | 9.782 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_federal_b | 9.782 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_federal_c | 9.782 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_obrera_a | 0 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_obrera_b | 0 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_obrera_c | 0 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_patron_a | 26.53 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_patron_b | 23.53 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_patron_c | 19.4 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_sinfed_a | 26.53 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_Salario mínimo_sinfed_b | 23.53 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_Salario mínimo_sinfed_c | 19.4 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2026_Salario mínimo_total_a | 36.312 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_total_b | 33.312 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_Salario mínimo_total_c | 29.182 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2026_prom_c_menos_a | -3.209 | Cambio de la cuña legal a cargo del patrón, (c) − (a), puntos del SBC |
| cuna_2026_sm_c_menos_a | -7.13 | Cambio de la cuña legal a cargo del patrón, (c) − (a), puntos del SBC |
| cuna_2030_1.01 SM, lectura por UMA_cyv_a | 10.077 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_cyv_b | 10.077 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_cyv_c | 10.077 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_federal_a | 5.976 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_federal_b | 5.976 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_federal_c | 5.976 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_obrera_a | 2.449 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_obrera_b | 2.449 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_obrera_c | 2.449 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_patron_a | 29.228 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_patron_b | 26.228 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_patron_c | 24.156 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_sinfed_a | 31.677 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_sinfed_b | 28.677 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_sinfed_c | 26.605 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_total_a | 37.653 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_total_b | 34.653 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, lectura por UMA_total_c | 32.581 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_cyv_a | 4.202 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_cyv_b | 4.202 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_cyv_c | 4.202 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_federal_a | 6.996 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_federal_b | 6.996 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_federal_c | 6.996 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_obrera_a | 2.449 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_obrera_b | 2.449 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_obrera_c | 2.449 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_patron_a | 23.353 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_patron_b | 20.353 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_patron_c | 18.281 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_sinfed_a | 25.802 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_sinfed_b | 22.802 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_sinfed_c | 20.73 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_total_a | 32.798 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_total_b | 29.798 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_1.01 SM, primer tramo tras el mínimo_total_c | 27.726 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_cyv_a | 11.875 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_cyv_b | 11.875 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_cyv_c | 11.875 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_federal_a | 1.733 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_federal_b | 1.733 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_federal_c | 1.733 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_obrera_a | 2.655 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_obrera_b | 2.655 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_obrera_c | 2.655 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_patron_a | 28.093 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_patron_b | 25.093 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_patron_c | 26.52 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_sinfed_a | 30.748 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_10 UMA_sinfed_b | 27.748 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_10 UMA_sinfed_c | 29.175 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_10 UMA_total_a | 32.481 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_total_b | 29.481 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_10 UMA_total_c | 30.908 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_cyv_a | 6.552 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_cyv_b | 6.552 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_cyv_c | 6.552 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_federal_a | 12.296 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_federal_b | 12.296 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_federal_c | 12.296 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_obrera_a | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_obrera_b | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_obrera_c | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_patron_a | 30.16 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_patron_b | 27.16 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_patron_c | 20.427 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_sinfed_a | 32.535 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_2 UMA_sinfed_b | 29.535 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_2 UMA_sinfed_c | 22.802 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_2 UMA_total_a | 44.831 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_total_b | 41.831 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_2 UMA_total_c | 35.098 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_cyv_a | 11.875 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_cyv_b | 11.875 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_cyv_c | 11.875 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_federal_a | 0.843 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_federal_b | 0.843 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_federal_c | 0.843 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_obrera_a | 2.727 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_obrera_b | 2.727 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_obrera_c | 2.727 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_patron_a | 27.067 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_patron_b | 24.067 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_patron_c | 26.718 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_sinfed_a | 29.794 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_25 UMA_sinfed_b | 26.794 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_25 UMA_sinfed_c | 29.445 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_25 UMA_total_a | 30.637 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_total_b | 27.637 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25 UMA_total_c | 30.288 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_25uma_c_menos_a | -0.349 | Cambio de la cuña legal a cargo del patrón, (c) − (a), puntos del SBC |
| cuna_2030_25uma_c_menos_b | 2.651 | (c) − (b) en 25 UMA: efecto de D2 en salarios altos |
| cuna_2030_3 UMA_cyv_a | 8.902 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_cyv_b | 8.902 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_cyv_c | 8.902 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_federal_a | 7.78 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_federal_b | 7.78 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_federal_c | 7.78 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_obrera_a | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_obrera_b | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_obrera_c | 2.375 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_patron_a | 29.11 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_patron_b | 26.11 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_patron_c | 22.777 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_sinfed_a | 31.485 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_3 UMA_sinfed_b | 28.485 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_3 UMA_sinfed_c | 25.152 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_3 UMA_total_a | 39.265 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_total_b | 36.265 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_3 UMA_total_c | 32.932 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_cyv_a | 10.077 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_cyv_b | 10.077 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_cyv_c | 10.077 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_federal_a | 5.522 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_federal_b | 5.522 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_federal_c | 5.522 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_obrera_a | 2.475 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_obrera_b | 2.475 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_obrera_c | 2.475 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_patron_a | 28.86 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_patron_b | 25.86 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_patron_c | 24.227 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_sinfed_a | 31.335 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_4 UMA_sinfed_b | 28.335 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_4 UMA_sinfed_c | 26.702 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_4 UMA_total_a | 36.857 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_total_b | 33.857 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_4 UMA_total_c | 32.224 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_cyv_a | 11.875 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_cyv_b | 11.875 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_cyv_c | 11.875 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_federal_a | 2.922 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_federal_b | 2.922 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_federal_c | 2.922 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_obrera_a | 2.559 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_obrera_b | 2.559 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_obrera_c | 2.559 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_patron_a | 29.464 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_patron_b | 26.464 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_patron_c | 26.255 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_sinfed_a | 32.023 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_5.55 UMA_sinfed_b | 29.023 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_5.55 UMA_sinfed_c | 28.814 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_5.55 UMA_total_a | 34.945 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_total_b | 31.945 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_5.55 UMA_total_c | 31.736 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_cyv_a | 3.15 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_cyv_b | 3.15 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_cyv_c | 3.15 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_federal_a | 7.269 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_federal_b | 7.269 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_federal_c | 7.269 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_obrera_a | 0 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_obrera_b | 0 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_obrera_c | 0 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_patron_a | 24.793 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_patron_b | 21.793 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_patron_c | 19.666 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_sinfed_a | 24.793 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_Salario mínimo_sinfed_b | 21.793 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_Salario mínimo_sinfed_c | 19.666 | Cuña legal total sin la aportación federal (patrón + trabajador), % del SBC |
| cuna_2030_Salario mínimo_total_a | 32.063 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_total_b | 29.063 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_Salario mínimo_total_c | 26.935 | cuna_legal_por_salario.csv, % del SBC |
| cuna_2030_prom_c_menos_a | -3.209 | Cambio de la cuña legal a cargo del patrón, (c) − (a), puntos del SBC |
| cuna_2030_sm_c_menos_a | -5.128 | Cambio de la cuña legal a cargo del patrón, (c) − (a), puntos del SBC |
| cuna_sm_uma_2026 | 2.685 | SM en veces la UMA (Sup_Fin) |
| cuna_sm_uma_2030 | 3.646 | SM en veces la UMA (Sup_Fin) |
| escalon_2026_primer_cyv | 3.676 | Tasa patronal de cesantía y vejez a 1.01 SM, 1.01 SM, primer tramo tras el mínimo |
| escalon_2026_primer_cyv_salto | 0.526 | Salto frente a 3.150 % del salario mínimo (puntos) |
| escalon_2026_primer_patron_salto | -1.924 | Salto del total a cargo del patrón entre SM y 1.01 SM, ley vigente (puntos; neto del fin del art. 36) |
| escalon_2026_uma_cyv | 6.026 | Tasa patronal de cesantía y vejez a 1.01 SM, 1.01 SM, lectura por UMA |
| escalon_2026_uma_cyv_salto | 2.876 | Salto frente a 3.150 % del salario mínimo (puntos) |
| escalon_2026_uma_patron_salto | 0.426 | Salto del total a cargo del patrón entre SM y 1.01 SM, ley vigente (puntos; neto del fin del art. 36) |
| escalon_2026_uma_patron_salto_a | 0.426 | Salto del total a cargo del patrón entre SM y 1.01 SM, lectura por UMA, columna (a) |
| escalon_2026_uma_patron_salto_b | 0.426 | Salto del total a cargo del patrón entre SM y 1.01 SM, lectura por UMA, columna (b) |
| escalon_2026_uma_patron_salto_c | 0.501 | Salto del total a cargo del patrón entre SM y 1.01 SM, lectura por UMA, columna (c) |
| escalon_2030_primer_cyv | 4.202 | Tasa patronal de cesantía y vejez a 1.01 SM, 1.01 SM, primer tramo tras el mínimo |
| escalon_2030_primer_cyv_salto | 1.052 | Salto frente a 3.150 % del salario mínimo (puntos) |
| escalon_2030_primer_patron_salto | -1.44 | Salto del total a cargo del patrón entre SM y 1.01 SM, ley vigente (puntos; neto del fin del art. 36) |
| escalon_2030_uma_cyv | 10.077 | Tasa patronal de cesantía y vejez a 1.01 SM, 1.01 SM, lectura por UMA |
| escalon_2030_uma_cyv_salto | 6.927 | Salto frente a 3.150 % del salario mínimo (puntos) |
| escalon_2030_uma_patron_salto | 4.435 | Salto del total a cargo del patrón entre SM y 1.01 SM, ley vigente (puntos; neto del fin del art. 36) |
| escalon_2030_uma_patron_salto_a | 4.435 | Salto del total a cargo del patrón entre SM y 1.01 SM, lectura por UMA, columna (a) |
| escalon_2030_uma_patron_salto_b | 4.435 | Salto del total a cargo del patrón entre SM y 1.01 SM, lectura por UMA, columna (b) |
| escalon_2030_uma_patron_salto_c | 4.49 | Salto del total a cargo del patrón entre SM y 1.01 SM, lectura por UMA, columna (c) |
| exp1_cifras_cambiadas | 186 | Cifras del registro del experimento 1 que cambian por el denominador común |
| exp1_cifras_cambiadas_pts | 123 | Idem, puntos del salario |
| exp1_cifras_cambiadas_sem | 63 | Idem, % de los ingresos del SEM |
| form_hist_2005 | 31.1 | Puestos de trabajo IMSS (31-dic) / ocupados ENOE T4, 15+ (%) |
| form_hist_2025 | 37.7 | Idem, 2025 |
| form_hist_anios_faltantes | 0 | Años 2005-2025 sin dato de la ENOE |
| form_hist_cambio_pts | 6.5 | Cambio 2005-2025, puntos porcentuales |
| form_hist_max | 37.7 | Máximo de la serie 2005-2025 (%) |
| form_hist_max_anio | 2,025 | Año del máximo |
| form_hist_menos_libro_2025 | 3.7 | Serie histórica 2025 − formalidad implícita del libro (puntos) |
| form_libro_2025 | 34 | Formalidad implícita del libro: cotizantes / ocupados (CONAPO × ENIGH), 2025 (%) |
| form_proy_cambio_pts | 29.1 | Cambio 2025-2054 en la proyección base (puntos) |
| formalidad_implicita_2027 | 0.3452 | Cotizantes / ocupados (prueba C de la v1.2) |
| formalidad_implicita_2030 | 0.3647 | Cotizantes / ocupados (prueba C de la v1.2) |
| formalidad_implicita_2040 | 0.4604 | Cotizantes / ocupados (prueba C de la v1.2) |
| formalidad_implicita_2054 | 0.6313 | Cotizantes / ocupados (prueba C de la v1.2) |
| fuente_enoe_descarga | 2026-10-18 12:55-13:01 CST (inegi.org.mx, microdatos ENOE T4 2005-2025; ver data/raw/enoe/descargas.log) | Microdatos ENOE T4 2005-2025, inegi.org.mx/contenidos/programas/enoe/15ymas/microdatos/ |
| fuente_memoria_sha256 | 12e667d918383b3c | 01-Asegurados.xlsx, descargado 2026-10-18 (imss.gob.mx, Memoria Estadística 2025, 01-Asegurados.xlsx) |
| k2_pesos_por_dh65_2040 | 5,631 | Base, K2, base ENIGH, pesos de 2026 por persona al año |
| k2_pesos_por_dh65_2054 | 6,696 | Base, K2, base ENIGH, pesos de 2026 por persona al año |
| k2_pesos_por_dh80_2040 | 26,318 | Base, K2, base ENIGH, pesos de 2026 por persona al año |
| k2_pesos_por_dh80_2054 | 23,771 | Base, K2, base ENIGH, pesos de 2026 por persona al año |
| k2p_M2_cuidados_2027 | 0 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M2_cuidados_2030 | 0 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M2_cuidados_2040 | 0 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M2_cuidados_2054 | 0 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M2_cuidados_pts_2027 | 0 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M2_cuidados_pts_2030 | 0 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M2_cuidados_pts_2040 | 0 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M2_cuidados_pts_2054 | 0 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M2_deficit_2027 | 75,666 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M2_deficit_2030 | 98,769 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M2_deficit_2040 | 173,612 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M2_deficit_2054 | 296,092 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M2_deficit_pts_2027 | 1.405 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M2_deficit_pts_2030 | 1.708 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M2_deficit_pts_2040 | 2.639 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M2_deficit_pts_2054 | 4.001 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M2_ingreso_2027 | 107,727 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M2_ingreso_2030 | 115,686 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M2_ingreso_2040 | 131,571 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M2_ingreso_2054 | 147,999 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M2_ingreso_pts_2027 | 2 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M2_ingreso_pts_2030 | 2 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M2_ingreso_pts_2040 | 2 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M2_ingreso_pts_2054 | 2 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M2_mov_reserva_2027 | 32,061 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M2_mov_reserva_2030 | 16,917 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M2_mov_reserva_2040 | 0 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M2_mov_reserva_2054 | 0 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M2_mov_reserva_pts_2027 | 0.595 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M2_mov_reserva_pts_2030 | 0.292 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M2_mov_reserva_pts_2040 | 0 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M2_mov_reserva_pts_2054 | 0 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M2_no_cubierto_2027 | 0 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M2_no_cubierto_2030 | 0 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M2_no_cubierto_2040 | 42,042 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M2_no_cubierto_2054 | 148,093 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M2_no_cubierto_pts_2027 | 0 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M2_no_cubierto_pts_2030 | 0 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M2_no_cubierto_pts_2040 | 0.639 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M2_no_cubierto_pts_2054 | 2.001 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M3_cuidados_2027 | 0 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M3_cuidados_2030 | 0 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M3_cuidados_2040 | 0 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M3_cuidados_2054 | 0 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M3_cuidados_pts_2027 | 0 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M3_cuidados_pts_2030 | 0 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M3_cuidados_pts_2040 | 0 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M3_cuidados_pts_2054 | 0 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M3_deficit_2027 | 74,968 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M3_deficit_2030 | 95,328 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M3_deficit_2040 | 155,531 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M3_deficit_2054 | 247,123 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M3_deficit_pts_2027 | 1.381 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M3_deficit_pts_2030 | 1.59 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M3_deficit_pts_2040 | 2.008 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M3_deficit_pts_2054 | 2.338 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M3_ingreso_2027 | 108,552 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M3_ingreso_2030 | 119,898 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M3_ingreso_2040 | 154,882 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M3_ingreso_2054 | 211,411 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M3_ingreso_pts_2027 | 2 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M3_ingreso_pts_2030 | 2 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M3_ingreso_pts_2040 | 2 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M3_ingreso_pts_2054 | 2 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M3_mov_reserva_2027 | 33,584 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M3_mov_reserva_2030 | 24,569 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M3_mov_reserva_2040 | -648 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M3_mov_reserva_2054 | -35,712 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M3_mov_reserva_pts_2027 | 0.619 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M3_mov_reserva_pts_2030 | 0.41 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M3_mov_reserva_pts_2040 | -0.008 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M3_mov_reserva_pts_2054 | -0.338 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M3_no_cubierto_2027 | 0 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M3_no_cubierto_2030 | 0 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M3_no_cubierto_2040 | 0 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M3_no_cubierto_2054 | 0 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_M3_no_cubierto_pts_2027 | 0 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M3_no_cubierto_pts_2030 | 0 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M3_no_cubierto_pts_2040 | 0 | cuadro_principal_K2.csv, puntos del salario |
| k2p_M3_no_cubierto_pts_2054 | 0 | cuadro_principal_K2.csv, puntos del salario |
| k2p_base_cuidados_2027 | 0 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_base_cuidados_2030 | 0 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_base_cuidados_2040 | 54,312 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_base_cuidados_2054 | 90,237 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_base_cuidados_pts_2027 | 0 | cuadro_principal_K2.csv, puntos del salario |
| k2p_base_cuidados_pts_2030 | 0 | cuadro_principal_K2.csv, puntos del salario |
| k2p_base_cuidados_pts_2040 | 0.61 | cuadro_principal_K2.csv, puntos del salario |
| k2p_base_cuidados_pts_2054 | 0.657 | cuadro_principal_K2.csv, puntos del salario |
| k2p_base_deficit_2027 | 74,270 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_base_deficit_2030 | 91,888 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_base_deficit_2040 | 137,449 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_base_deficit_2054 | 198,154 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_base_deficit_pts_2027 | 1.358 | cuadro_principal_K2.csv, puntos del salario |
| k2p_base_deficit_pts_2030 | 1.481 | cuadro_principal_K2.csv, puntos del salario |
| k2p_base_deficit_pts_2040 | 1.543 | cuadro_principal_K2.csv, puntos del salario |
| k2p_base_deficit_pts_2054 | 1.442 | cuadro_principal_K2.csv, puntos del salario |
| k2p_base_ingreso_2027 | 109,378 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_base_ingreso_2030 | 124,109 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_base_ingreso_2040 | 178,194 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_base_ingreso_2054 | 274,824 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_base_ingreso_pts_2027 | 2 | cuadro_principal_K2.csv, puntos del salario |
| k2p_base_ingreso_pts_2030 | 2 | cuadro_principal_K2.csv, puntos del salario |
| k2p_base_ingreso_pts_2040 | 2 | cuadro_principal_K2.csv, puntos del salario |
| k2p_base_ingreso_pts_2054 | 2 | cuadro_principal_K2.csv, puntos del salario |
| k2p_base_mov_reserva_2027 | 35,107 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_base_mov_reserva_2030 | 32,222 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_base_mov_reserva_2040 | 0 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_base_mov_reserva_2054 | 0 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_base_mov_reserva_pts_2027 | 0.642 | cuadro_principal_K2.csv, puntos del salario |
| k2p_base_mov_reserva_pts_2030 | 0.519 | cuadro_principal_K2.csv, puntos del salario |
| k2p_base_mov_reserva_pts_2040 | 0 | cuadro_principal_K2.csv, puntos del salario |
| k2p_base_mov_reserva_pts_2054 | 0 | cuadro_principal_K2.csv, puntos del salario |
| k2p_base_no_cubierto_2027 | 0 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_base_no_cubierto_2030 | 0 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_base_no_cubierto_2040 | 0 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_base_no_cubierto_2054 | 0 | cuadro_principal_K2.csv, mdp de 2026 |
| k2p_base_no_cubierto_pts_2027 | 0 | cuadro_principal_K2.csv, puntos del salario |
| k2p_base_no_cubierto_pts_2030 | 0 | cuadro_principal_K2.csv, puntos del salario |
| k2p_base_no_cubierto_pts_2040 | 0 | cuadro_principal_K2.csv, puntos del salario |
| k2p_base_no_cubierto_pts_2054 | 0 | cuadro_principal_K2.csv, puntos del salario |
| masa25_2027 | 5,468,877 | Σ cotizantes × SBC (R1, tope 25 UMA, piso SM) × UMA × 337, mdp de 2026 |
| masa25_2030 | 6,205,467 | Σ cotizantes × SBC (R1, tope 25 UMA, piso SM) × UMA × 337, mdp de 2026 |
| masa25_2040 | 8,909,700 | Σ cotizantes × SBC (R1, tope 25 UMA, piso SM) × UMA × 337, mdp de 2026 |
| masa25_2054 | 13,741,181 | Σ cotizantes × SBC (R1, tope 25 UMA, piso SM) × UMA × 337, mdp de 2026 |
| prop_sobre_tope_2027 | 1.74 | % de la masa sin tope que rebasa 25 UMA (forma R1 sin tope) |
| prop_sobre_tope_2030 | 1.81 | % de la masa sin tope que rebasa 25 UMA (forma R1 sin tope) |
| prop_sobre_tope_2040 | 2.12 | % de la masa sin tope que rebasa 25 UMA (forma R1 sin tope) |
| prop_sobre_tope_2054 | 2.71 | % de la masa sin tope que rebasa 25 UMA (forma R1 sin tope) |
| r_ingresoGMP_masa_2027 | 1.691 | Ingreso de GMP (Cuadro V.24) / masa propia base (%) |
| r_ingresoGMP_masa_2030 | 1.634 | Ingreso de GMP (Cuadro V.24) / masa propia base (%) |
| r_ingresoGMP_masa_2036 | 1.551 | Ingreso de GMP (Cuadro V.24) / masa propia base (%) |
| r_ingresoGMP_masa_2040 | 1.551 | Ingreso de GMP (Cuadro V.24) / masa propia base (%) |
| r_ingresoGMP_masa_2054 | 1.544 | Ingreso de GMP (Cuadro V.24) / masa propia base (%) |
| r_ingresoGMP_masa_caida_pct | -8.66 | Caída porcentual de r(t), 2027-2054 |
| res_M2_K1_deficit_no_cubierto_2054 | 148,093 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_M2_K1_ultimo | 2,032 | resumen_K2_K1.csv: último año con cobertura completa de GMP |
| res_M2_K1_vp_cuidados | 102,997 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_M2_K1_vp_cuidados_mas_reserva | 102,997 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_M2_K1_vp_deficit_no_cubierto | 831,627 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_M2_K1_vp_reserva_final | 0 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_M2_K2_deficit_no_cubierto_2054 | 148,093 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_M2_K2_ultimo | 2,037 | resumen_K2_K1.csv: último año con cobertura completa de GMP |
| res_M2_K2_vp_cuidados | 0 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_M2_K2_vp_cuidados_mas_reserva | 0 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_M2_K2_vp_deficit_no_cubierto | 728,630 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_M2_K2_vp_reserva_final | 0 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_M3_K1_deficit_no_cubierto_2054 | 35,712 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_M3_K1_ultimo | 2,034 | resumen_K2_K1.csv: último año con cobertura completa de GMP |
| res_M3_K1_vp_cuidados | 151,254 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_M3_K1_vp_cuidados_mas_reserva | 151,254 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_M3_K1_vp_deficit_no_cubierto | 114,602 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_M3_K1_vp_reserva_final | 0 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_M3_K2_deficit_no_cubierto_2054 | 0 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_M3_K2_ultimo | 2,054 | resumen_K2_K1.csv: último año con cobertura completa de GMP |
| res_M3_K2_vp_cuidados | 6,498 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_M3_K2_vp_cuidados_mas_reserva | 36,653 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_M3_K2_vp_deficit_no_cubierto | 0 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_M3_K2_vp_reserva_final | 30,155 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_base_K1_deficit_no_cubierto_2054 | 0 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_base_K1_ultimo | 2,054 | resumen_K2_K1.csv: último año con cobertura completa de GMP |
| res_base_K1_vp_cuidados | 801,935 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_base_K1_vp_cuidados_mas_reserva | 801,935 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_base_K1_vp_deficit_no_cubierto | 0 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_base_K1_vp_reserva_final | 0 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_base_K2_deficit_no_cubierto_2054 | 0 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_base_K2_ultimo | 2,054 | resumen_K2_K1.csv: último año con cobertura completa de GMP |
| res_base_K2_vp_cuidados | 747,074 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_base_K2_vp_cuidados_mas_reserva | 801,935 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_base_K2_vp_deficit_no_cubierto | 0 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| res_base_K2_vp_reserva_final | 54,861 | resumen_K2_K1.csv, mdp de 2026; VP descontado al 3 % real a 2026 |
| sens13_K1_M2_0 | 2,032 | sensibilidad_v13.csv, último año con cobertura completa, con provisiones, masa del libro |
| sens13_K1_M2_1 | 2,034 | sensibilidad_v13.csv, último año con cobertura completa, sin provisiones, masa del libro |
| sens13_K1_M2_2 | 2,031 | sensibilidad_v13.csv, último año con cobertura completa, con provisiones, S-masa |
| sens13_K1_M2_3 | 2,033 | sensibilidad_v13.csv, último año con cobertura completa, sin provisiones, S-masa |
| sens13_K1_M3_0 | 2,034 | sensibilidad_v13.csv, último año con cobertura completa, con provisiones, masa del libro |
| sens13_K1_M3_1 | 2,041 | sensibilidad_v13.csv, último año con cobertura completa, sin provisiones, masa del libro |
| sens13_K1_M3_2 | 2,033 | sensibilidad_v13.csv, último año con cobertura completa, con provisiones, S-masa |
| sens13_K1_M3_3 | 2,036 | sensibilidad_v13.csv, último año con cobertura completa, sin provisiones, S-masa |
| sens13_K1_MH_0 | 2,034 | sensibilidad_v13.csv, último año con cobertura completa, con provisiones, masa del libro |
| sens13_K1_MH_1 | 2,039 | sensibilidad_v13.csv, último año con cobertura completa, sin provisiones, masa del libro |
| sens13_K1_MH_2 | 2,033 | sensibilidad_v13.csv, último año con cobertura completa, con provisiones, S-masa |
| sens13_K1_MH_3 | 2,036 | sensibilidad_v13.csv, último año con cobertura completa, sin provisiones, S-masa |
| sens13_K1_base_0 | 2,054 | sensibilidad_v13.csv, último año con cobertura completa, con provisiones, masa del libro |
| sens13_K1_base_1 | 2,054 | sensibilidad_v13.csv, último año con cobertura completa, sin provisiones, masa del libro |
| sens13_K1_base_2 | 2,054 | sensibilidad_v13.csv, último año con cobertura completa, con provisiones, S-masa |
| sens13_K1_base_3 | 2,054 | sensibilidad_v13.csv, último año con cobertura completa, sin provisiones, S-masa |
| sens13_K2_M2_0 | 2,037 | sensibilidad_v13.csv, último año con cobertura completa, con provisiones, masa del libro |
| sens13_K2_M2_1 | 2,042 | sensibilidad_v13.csv, último año con cobertura completa, sin provisiones, masa del libro |
| sens13_K2_M2_2 | 2,036 | sensibilidad_v13.csv, último año con cobertura completa, con provisiones, S-masa |
| sens13_K2_M2_3 | 2,039 | sensibilidad_v13.csv, último año con cobertura completa, sin provisiones, S-masa |
| sens13_K2_M3_0 | 2,054 | sensibilidad_v13.csv, último año con cobertura completa, con provisiones, masa del libro |
| sens13_K2_M3_1 | 2,054 | sensibilidad_v13.csv, último año con cobertura completa, sin provisiones, masa del libro |
| sens13_K2_M3_2 | 2,045 | sensibilidad_v13.csv, último año con cobertura completa, con provisiones, S-masa |
| sens13_K2_M3_3 | 2,051 | sensibilidad_v13.csv, último año con cobertura completa, sin provisiones, S-masa |
| sens13_K2_MH_0 | 2,049 | sensibilidad_v13.csv, último año con cobertura completa, con provisiones, masa del libro |
| sens13_K2_MH_1 | 2,050 | sensibilidad_v13.csv, último año con cobertura completa, sin provisiones, masa del libro |
| sens13_K2_MH_2 | 2,043 | sensibilidad_v13.csv, último año con cobertura completa, con provisiones, S-masa |
| sens13_K2_MH_3 | 2,047 | sensibilidad_v13.csv, último año con cobertura completa, sin provisiones, S-masa |
| sens13_K2_base_0 | 2,054 | sensibilidad_v13.csv, último año con cobertura completa, con provisiones, masa del libro |
| sens13_K2_base_1 | 2,054 | sensibilidad_v13.csv, último año con cobertura completa, sin provisiones, masa del libro |
| sens13_K2_base_2 | 2,054 | sensibilidad_v13.csv, último año con cobertura completa, con provisiones, S-masa |
| sens13_K2_base_3 | 2,054 | sensibilidad_v13.csv, último año con cobertura completa, sin provisiones, S-masa |
| sm_uma_2027 | 2.899 | SM en veces la UMA (Sup_Fin; v1.2) |
| sm_uma_2030 | 3.646 | SM en veces la UMA (Sup_Fin; v1.2) |
| sm_uma_2040 | 3.833 | SM en veces la UMA (Sup_Fin; v1.2) |
| sm_uma_2054 | 4.11 | SM en veces la UMA (Sup_Fin; v1.2) |
