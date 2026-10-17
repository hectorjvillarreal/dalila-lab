# F0 — Inventario de insumos

Anexo preliminar del Núcleo 13 (afiliación subsidiada al SEM). Instrucción: `20261017_BDH_N13_anexo-afiliacion-subsidiada_build_v1.1`.
Rutas relativas a la raíz de Dalila. sha256 truncado a 16 caracteres.

| # | Insumo | Ruta | Versión / sha256 | Estado | Decisión |
|---|---|---|---|---|---|
| I1 | Informe IMSS 2025-2026 | `Missions/Funded/IMSS_Surgical/e_1_imss_subsidiado/_informe-situacion-financiera_imss.pdf` | 338 páginas; sha256 `fe5caabf72f5b6a1` | Presente; validado con `pdfinfo` (338 pp.; título 2025-2026) | Copia local; no se descargó del Senado |
| I2 | Libro de Finanzas 07/09/2026 | `Missions/Funded/IMSS_Surgical/e_1_imss_subsidiado/Req inf fin_Modelo de demanda quirúrgica_070926.xlsx` | sha256 `1bd87ceea394273b` | Presente; versión 07/09 | Se usa solo esta versión |
| I3 | CONAPO, población a mitad de año | `GrandPlan/DFD/outputs/briefs/2026-09_EIC2025_nota/data/raw/CONAPO_2023_ConDem50a19_ProyPob20a70.zip` | Conciliación 1950-2019 y proyecciones 2020-2070 (publicación 2023); sha256 `ddcf182a05888672` | Presente | Misma base que el Núcleo 13: 2025 = 133,367,428 (el Núcleo 13 reporta 133.37 M y la llama «CONAPO 2022-2070») |
| I4 | ENIGH 2024 (nueva serie) | `Missions/Funded/BID2/motivation/data/enigh/2024/bundle` | Tablas población, trabajos, ingresos, noagro, agro, concentradohogar | Presente | Se usa el factor de expansión; no se reportan errores estándar |
| I5 | Perfil NTA de consumo público de salud | — | — | **No existe en Dalila** (`Missions/Funded/NTA_Inequality` no contiene perfiles por edad) | Respaldo R3: perfil plano (cota inferior) y estilizado 65+/20-64 = 2, 3 y 4 |
| I6 | Cuadernos del Núcleo 13 | — | — | **No están en Dalila** | Coherencia verificada contra el informe del Núcleo 13 (`~/Downloads/Nucleo13_Informe_Resultados_Oct2026 atendido JP.docx`): CONAPO 2025, Anexo H (cohortes), Anexo I, Anexo M |

## Sumas de control del libro de Finanzas (7.1)

| Verificación | Esperado | Obtenido | ¿Pasa? |
|---|---|---|---|
| Asegurados dic. 2025 | 21,800,692.00 | 21,800,692.00 | sí |
|   hombres | 13,102,667.00 | 13,102,667.00 | sí |
|   mujeres | 8,698,025.00 | 8,698,025.00 | sí |
| TIMSS dic. 2025 | 551,894.00 | 551,894.00 | sí |
| Total = stock 2025 de Pob Emp & Nuevos | 22,352,586.00 | 22,352,586.00 | sí |
| SBC promedio ponderado (pesos/día) | 627.21 | 627.21 | sí |
| Aportación federal SEM-A 2025 reconstruida (mdp de 2026) | 146,457.00 | 144,610.25 | sí |

La aportación federal SEM-A observada en 2025 es 146,457 mdp de 2026 (hoja `Ingresos IMSS`).

## Diferencias con el Informe, ingresos 2025 (7.2)

| Concepto | Libro de Finanzas | Cuadro II.14 (pág. PDF 67) | Diferencia |
|---|---|---|---|
| Cuotas obrero-patronales | 634,265 | 625,443 | +8,822 |
| Aportaciones del Gobierno Federal | 157,892 | 158,947 | -1,055 |
| Otros ingresos | 59,154 | 46,643 | +12,511 |
| Total sin pensiones en curso de pago | 851,311 | 831,033 | +20,278 |

**Fuente que se usa:** el libro de Finanzas, por coherencia con el Núcleo 13 (Anexo M del Núcleo 13 usa el mismo total, 851.3 mil millones).

## Respaldos activados

- **R1** (distribución del SBC), **R2** (beneficiarios por titular), **R3** (perfil de costo: sin NTA, estilizado) y **R4** (antigüedad) se activan; ver `REPORT.md`.
- No se detuvo la construcción: no falta ningún insumo crítico (C).
