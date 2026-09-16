# Inventario del paquete económico 2024, apartado de educación y diffs 2023 → 2024

**Corrida:** evaluación CIEP 2024 · FISCUS · Dalila · 2026-09-06 (instrucción v3)
**Fase:** 2. Construido antes de leer el documento CIEP más allá de su índice (PDF 3–5, leído 16:06:08; solo líneas de encabezado con puntos de guía; ver bitácora).
**Capítulo propio:** educación (instrucción v3 §1). Cierra la tríada NTA: pensiones (2020), salud (2021), educación (2024).
**Convenciones (instrucción §3):** deflactor del CGPE 2024 **1.0479** (4.8 %, p. 118 y 121; verificado: gasto neto aprobado 2023 8,257,614.7 → 8,653.2 mmp de 2024 = 1.04791); comparación ex ante contra ex ante (PPEF/ILIF 2024 vs PEF/LIF 2023 aprobados); donde se usa el PEF aprobado 2024 en lugar del proyecto se marca **"PEF aprobado, no proyecto"**; añada de PIB declarada en §9.

mmp = miles de millones de pesos; mdp = millones de pesos; "a" = aprobado 2023; "est." = cierre estimado 2023 (CGPE 2024); "p" = proyecto 2024; "A" = aprobado 2024 (PEF, Cámara); pp = puntos porcentuales del PIB.

---

## Sección cero — estado de la carpeta

**Regla de no bloqueo (§0) aplicada:** ninguna descarga condicionó el arranque. Fase 0 (lectura local) 16:00–16:06; sondas HEAD 16:07; descargas 16:08–16:09 (10 archivos, 43 MB, dos intentos máximo, ninguno falló); fase 2 con todo en carpeta.

**Piezas oficiales del paquete 2024 presentes** (`_manifiesto.csv`, `oficial_primaria`):

| clave | archivo | páginas | paginación |
|---|---|---|---|
| CGPE | `2024/2024_cgpe_criterios-generales.pdf` | 128 | impresa = PDF |
| ILIF | `2024/2024_ilif_iniciativa.pdf` | 123 | exposición en romanos I–LXV (= PDF 1–65); **art. 1o. impreso 1 = PDF 66**; art. 2o. PDF 76; art. 3o. PDF 79; art. 16 PDF 96; art. 22 PDF 108 |
| DEC | `2024/2024_ppef_proyecto-decreto.pdf` | 174 | impresa = PDF; art. 2 p. 2; Anexo 1 p. 62–64; Anexos 2–5 p. 64; Anexo 8 p. 68; Anexo 12 p. 75–78; Anexo 18 p. 90–92; Anexos 20–22 p. 95–96; Anexo 24 p. 165; Anexo 29 p. 170–171 |
| CIEP | `2024/ciep_implicaciones2024.pdf` (`derivada_ciep`) | 96 PDF | **27 de 96 páginas son imagen sin capa de texto** (PDF 1, 13, 18–19, 23–24, 31–32, 36–37, 42–43, 48–49, 53–54, 59–60, 66–67, 72–73, 80–81, 85, 96); rendidas a PNG en fase 1 (`scratchpad/png24/`). Índice: 13 capítulos; Parte I deuda (1–2), Parte II gasto (3–10; **educación = cap. 8, impresas 44–47**), Parte III ingresos (11–12), cap. 13 implicaciones |

**Piezas adquiridas en esta corrida (fase 1, §5; todas `oficial_primaria`; sha256 en `_manifiesto.csv`):**

| pieza | ruta | archivo | tamaño |
|---|---|---|---|
| Analítico PEF **aprobado** 2024, GF ramo × programa × UR × objeto | `pef.hacienda.gob.mx/work/models/PEF/Analiticos_Historico/2024/Autorizado/ac01_ra_pp_ur_og.xlsx` | `2024/2024_pef_analitico-gf-ramo-programa-ur-objeto.xlsx` | 9.5 MB |
| Analítico PEF aprobado 2024, GF ramo × función × UR × objeto | `…/2024/Autorizado/ac01_ra_f_ur_og.xlsx` | `2024/2024_pef_analitico-gf-ramo-funcion-ur-objeto.xlsx` | 6.7 MB |
| Analíticos PEF aprobado 2024, entidades (programa y función) | `…/2024/Autorizado/ac01_ra_pp_ur_og_efe.xlsx`, `ac01_ra_f_ur_og_efe.xlsx` | `2024/2024_pef_analitico-entidades-ramo-{programa,funcion}-ur-objeto.xlsx` | 2.8 + 2.6 MB |
| Analíticos PEF aprobado 2023, GF (programa y función) y entidades función | `…/2023/Autorizado/…` | `2023/2023_pef_analitico-gf-ramo-{programa,funcion}-ur-objeto.xlsx`, `2023/2023_pef_analitico-entidades-ramo-funcion-ur-objeto.xlsx` | 9.2 + 6.6 + 2.7 MB |
| **LIF aprobada** 2022, 2023, 2024 (decreto publicado en el DOF, 12-nov-2021, 14-nov-2022, 13-nov-2023) | `finanzaspublicas.hacienda.gob.mx/work/models/Finanzas_Publicas/docs/paquete_economico/lif/lif_{t}.pdf` (columna LIF del punto de entrada; minúsculas; `LIF_{t}.pdf` da 404) | `{t}/{t}_lif_aprobada.pdf` | 0.3–0.7 MB |

Nota de infraestructura: bundle de certificados de la bitácora general (`scratchpad/certs/bundle.pem`, hoja firmada por YR1) con `--cacert`; verificación TLS activa. Una primera ronda de sondas falló por un error propio de la variable del bundle (no del servidor); no cuenta como intento.

**Piezas ausentes y ruta probada:**

| pieza | ruta / estado | consecuencia para educación |
|---|---|---|
| Exposición de motivos del PPEF 2024 (Tomo I) | `ppef.hacienda.gob.mx/work/models/PPEF2024/docs/exposicion/EM_Documento_Completo.pdf` 404 el 2026-09-05 (bitácora general); **resonda en fase 7** | sin cuadro oficial "gasto en educación" consolidado neto por nivel, sin metas físicas (matrícula, planteles), sin texto de política educativa más allá del CGPE p. 61–62 |
| Analíticos del **proyecto** PPEF 2024 | mismo árbol, 404 | CIEP evalúa el proyecto; aquí se verifica contra el **aprobado**. La asimetría es material en 2024 (ver §5.6): la Cámara añadió 13,262.4 mdp al Ramo 11 |
| Cuentas Públicas 2016–2022 | no se descargan (decisión §5.5) | las series 2016–2022 de CIEP quedan `no_verificable`; el empalme ejercido/proyecto se reporta como hallazgo de criterio 2 |
| Proyecciones de población CONAPO; matrícula SEP (Formato 911 / Principales Cifras) | no en carpeta; no se buscaron (fuera de perímetro de la carpeta) | **ninguna cifra per cápita ni por alumno es computable desde la carpeta**; se declara en el capítulo |
| Miscelánea fiscal 2024 | no aplica: la ILIF 2024 no propone cambios a leyes impositivas (sin miscelánea); no se buscó | — |
| Nota metodológica SHCP y Cantú et al. (2016) | en carpeta desde 2023 (`_metodologia/`) | se usan para los flujos y acervos de §4 |

**Criterios condicionados por la carpeta:** perímetro (criterio 1) no condicionado: función vs ramo, federal vs federalizado y becas se resuelven con los analíticos aprobados y el decreto. Contrafactual (2) no condicionado. Consistencia interna (3) no condicionada. Cobertura (4) condicionada en metas físicas y en la EM. Supuestos macro y de matrícula (5): el paquete no declara supuesto de matrícula en ninguna pieza en carpeta (CGPE, ILIF, DEC); si tampoco está en la EM, es hallazgo de horizonte. Series 2016–2022 (criterio 6): condicionadas por Cuentas Públicas.

**Asimetría de objeto (instrucción §2.2), cuantificada:** el PEF aprobado 2024 difiere del proyecto en 11 ramos (§5.6). En educación: Ramo 11 +13,262.4 mdp (todo en el PP S072 Becas de Educación Básica: 36,607.4 → 49,869.8), Ramo 33 −1,492.4 (FAM asistencia social −76.5, FAM infraestructura educativa −89.8, FAIS −516.7, FORTAMUN −523.5, FAFEF −286.0), Ramo 25 sin cambio. En 2023 los ramos 11, 25 y 33 no cambiaron en la Cámara (analítico aprobado 2023 = DEC 2023 en los tres). **Toda fila resuelta con el aprobado 2024 lleva la marca; toda discrepancia de CIEP en becas o ramo 33 se contrasta primero contra el proyecto reconstruido (aprobado menos la reasignación) antes de atribuirse.**

**Proporción esperada de `no_verificable` atribuible a la carpeta:** baja para montos 2024 de programas, UR, fondos y subfunciones (los analíticos aprobados los cubren); alta para series 2016–2022, per cápita, por alumno y metas físicas.

**Nivel de carpeta comparado con 2023:** mejor. En 2023 faltaban los analíticos del GF y el capítulo 7 de CIEP quedó con 23 de 32 filas sin verificar; en 2024 los analíticos aprobados del GF (2023 y 2024) están en carpeta y la LIF aprobada de tres ejercicios también.

---

## 1. Marco macroeconómico (CGPE 2024 p. 118, 121; base 2018)

| variable | 2023 aprobado (CGPE 2023) | 2023 estimado | 2024 |
|---|---|---|---|
| PIB real, % (puntual para finanzas públicas) | 3.0 | 3.0 ([2.5, 3.5]) | **2.6** (p. 46; rango [2.5, 3.5]) |
| PIB nominal, mmp | 31,402 (base 2013) | **31,963.0** | **34,374.5** |
| Deflactor del PIB | 5.0 | 5.0 | **4.8** |
| Inflación dic/dic; promedio | 3.2; 4.7 | 4.5; 5.7 | 3.8; 4.5 |
| Cetes 28 fin; promedio | 8.5; 8.9 | 11.3; 11.2 | 9.5; 10.3 (real promedio 5.5) |
| Tipo de cambio fin; promedio | 20.6; 20.6 | 17.3; 17.5 | 17.6; 17.1 |
| Petróleo, dpb; plataforma, mbd | 68.7; 1,872 | 67.0; 1,955 | 56.7; 1,983 |
| Cuenta corriente, % PIB | −1.2 | −0.8 | −0.7 |

Mediano plazo (p. 80, 121): PIB [2.0, 3.0] 2025–2029; inflación 3.0; Cetes 5.5 desde 2026; petróleo 53.2 → 44.3 dpb; PIB nominal 2029 46,185.5 mmp. **Cambio de año base del PIB (2013 → 2018):** todas las razones a PIB de 2023 aprobado se reexpresan (ingresos 22.7 → 22.3; gasto neto 26.3 → 25.8; SHRFSP 49.4 → 48.5; RFSP 4.1 → 4.0), con nota */ en cada cuadro.

**Deflactor implícito del documento evaluado:** se calculará desde los cuadros de CIEP en fase 4 antes de contrastar variaciones (instrucción §2.8); el oficial es 1.0479.

## 2. Ingresos (CGPE 2024 p. 53–54, 119; ILIF art. 1o. PDF 66–75; LIF aprobada 2024 DOF 13-nov-2023)

| mmp de 2024 | LIF 2023 | estimado 2023 | ILIF 2024 | var. real vs LIF | vs est. |
|---|---|---|---|---|---|
| Ingresos presupuestarios | 7,464.7 | 7,270.7 | **7,329.0** | −1.8 | +0.8 |
| Petroleros | 1,380.8 | 1,181.3 | 1,048.1 | −24.1 | −11.3 |
| Tributarios | 4,841.5 | 4,657.3 | 4,941.5 | +2.1 | +6.1 |
| IEPS gasolinas | 291.8 | 295.5 | 456.4 | +56.4 | +54.5 |
| Tributarios sin IEPS gasolinas | 4,549.7 | 4,361.9 | 4,485.2 | −1.4 | +2.8 |
| No tributarios | 248.7 | 342.3 | 261.6 | +5.2 | −23.6 |
| Organismos y empresas | 993.8 | 1,089.8 | 1,077.7 | +8.5 | −1.1 |

En corrientes (p. 119): presupuestarios 7,328,995.2 (21.3 % del PIB); tributarios 4,941,540.8 (14.4 %); sistema renta 2,709.2 mmp; IVA 1,330.4. ILIF art. 1o.: total 9,066,045.8; impuestos 4,942,030.3; ISR 2,709,899.5; IVA 1,330,421.0; IEPS 688,083.6 (combustibles 456,389.4); cuotas IMSS 535,254.7; derechos 59,091.4; productos 8,641.6; aprovechamientos 193,877.0; IMSS 42,286.1; ISSSTE 53,246.4; Pemex 744,362.7; CFE 446,951.3; FMP 303,217.2; financiamientos 1,737,050.6 (endeudamiento interno GF 1,906,069.4; diferimiento 44,050.6; superávit de organismos −68,069.3).

**LIF aprobada 2024 (DOF 13-nov-2023) vs ILIF:** 181 renglones idénticos salvo dos: Pemex 744,362.7 → **769,805.6** (+25,442.9) y transferencias del FMP 303,217.2 → **277,774.3** (−25,442.9). Total, presupuestarios, tributarios, cuotas y financiamientos sin cambio. El mismo monto sale del Ramo 18 en el PEF aprobado (§5.6): la Cámara sustituyó aportación patrimonial por renta petrolera retenida (menor DUC). **LIF 2023 y LIF 2022 aprobadas = ILIF en todos los renglones consultados** (totales, impuestos, ISR, IVA, cuotas, Pemex, CFE, financiamientos), lo que resuelve el híbrido de la serie de §8: en 2022–2024 el denominador ILIF es igual al aprobado.

Renuncias recaudatorias: la ILIF remite al documento DRR 2024 (p. XIV), no en carpeta. Sin miscelánea fiscal.

## 3. Gasto (CGPE 2024 p. 57–66, 117, 119; DEC 2024 art. 2 y Anexo 1)

| mmp de 2024 | PEF 2023 a | PPEF 2024 p | var. real |
|---|---|---|---|
| Gasto neto total (pagado) | 8,653.2 | **9,022.0** | +4.3 |
| Programable devengado | 6,243.7 | 6,490.4 | +4.0 |
| No programable | 2,453.6 | 2,575.6 | +5.0 |
| Costo financiero | 1,130.8 | 1,264.0 | +11.8 |
| Participaciones | 1,278.7 | 1,267.6 | −0.9 |
| Gasto de inversión / inversión física | 1,246.8 / 1,153.5 | 1,108.4 / 888.8 | −11.1 / **−23.0** |
| Pensiones (clasificación económica) | 1,397.2 | **1,499.0** | +7.3 |
| Desarrollo social (funcional) | 4,094.2 | 4,384.6 | +7.1 |
| Gasto federalizado | 2,550.4 | 2,563.3 | +0.5 |

DEC art. 2: gasto neto total **9,066,045,800,000** = ingresos LIF; déficit presupuestario 1,693,000.0. Neteo (Anexo 1): 1,340,643.2 mdp; suma A–E = 10,406,689.0. Gasto neto pagado 9,021,995.2 = 9,066,045.8 − diferimiento 44,050.6 ✓.

**Por ramo (CGPE p. 117, mdp de 2024, columna PEF 2023 → PPEF 2024, var. real):** Educación Pública 421,548.2 → 425,755.5 (**+1.0 %**); Ramo 25 (dentro de generales); Bienestar 434,367.8 → 543,933.0 (+25.2); Defensa → 259,433.8 (incorpora Tren Maya S.A. y el grupo aeroportuario Olmeca-Maya-Mexica); Salud 219,658.3 → 96,990.0 (**−55.8**, IMSS-Bienestar pasa a Entidades no Sectorizadas 137,996.6, +1,380.6 %); Energía 51,768.6 → 193,179.1 (+273.2, aportación a Pemex/CFE); Turismo 2,611.1 → 1,973.7; Conahcyt 33,171.6 → 33,170.7 (0.0); Cultura 16,688.0 → 16,754.9; ramos generales 2,509,589.5 → 2,668,064.2 (+6.3); IMSS 1,221,542.7 → 1,345,950.7 (+10.2); ISSSTE 460,077.2 → 475,829.0 (+3.4); Pemex 710,906.5 → 456,021.4 (−35.9); CFE 460,840.2 → 493,380.7 (+7.1). Programas prioritarios (p. 58): PAM 465,048.7; **Programas de Becas 87,675.0**; LEEN 28,358.3; PPD 27,860.4; Universidades para el Bienestar 1,562.6. Proyectos: Tren Maya 120,000.0; Istmo 21,059.3; Toluca 4,000.0.

**12 acciones / clasificación económica (p. 60):** corriente 59.8 % del programable, pensiones 23.1 %, inversión 17.1 %; servicios personales 45.1 % del corriente; subsidios 25.8 %.

## 4. Los tres flujos y los tres acervos (CGPE 2024 p. 9, 46–49, 81, 119, 122)

| flujo, mdp / % PIB | 2023 aprobado (PIB base 2018) | 2023 estimado | 2024 proyecto |
|---|---|---|---|
| Balance presupuestario | −1,134,140.7 / −3.5 | −1,048,102.5 / −3.3 | **−1,693,000.0 / −4.9** |
| Balance presupuestario sin inversión | +55,652.9 / 0.2 | +47,693.4 / 0.1 | −584,588.1 / −1.7 |
| Balance primario | −55,053.7 / −0.2 | +25,635.4 / 0.1 | **−429,005.9 / −1.2** |
| Fuera del presupuesto | −157,008.4 / −0.5 | −193,500.0 / −0.6 | −171,872.3 / −0.5 |
| RFSP | −1,291,149.1 / −4.0 | −1,241,602.5 / −3.9 | **−1,864,872.3 / −5.4** |
| SHRFSP, mdp / % PIB | 15,500,270.6 / 48.5 | 14,857,772.7 / 46.5 | **16,787,906.1 / 48.8** |
| Deuda neta del sector público federal, % PIB | 48.3 | 46.3 | 48.7 (ILIF p. XXXV: externa 11.5, interna 37.1; EPE y banca 7.8) |
| Deuda bruta del sector público no financiero, % PIB | 53.9 | 50.9 | 52.9 |

Balance por entidad (p. 49): Gobierno Federal −1,906.1 mmp (−5.5 % del PIB); Pemex +145,000 (0.4) compensado por la aportación del GF en el programable "con efecto neutral"; CFE 0. **Regla invocada (p. 46):** art. 11 del RLFPRH, caída del precio del petróleo mayor a 10 % respecto a la LIF anterior (−17.5 %); en 2023 la regla invocada fue la del costo financiero (>25 %). Composición fuera del presupuesto (p. 46–47): IPAB 0.11, deudores 0.01, adecuaciones 0.18, Pidiregas 0.14, banca −0.01. Balance sin inversión: la ILIF 2024 art. 1o. excluye "la inversión presupuestaria" (perímetro total, como la ILIF 2023). DUC: **35 %** (CGPE p. 48; 40 % en 2023).

**Techos (ILIF arts. 2o.–3o.):** interno neto GF **1,990,000 mdp** (2023: 1,170,000; +70.1 % nominal); externo neto sector público **18,000 mdd** (5,500; +227 %); Pemex 138,119.1 mdp / 3,726.5 mdd (27,068.4 / 142.2); CFE 600 mdp / 1,188 mdd (12,750 / 397); CDMX 2,500 mdp (3,000); banca de desarrollo déficit por intermediación 0; IPAB canje y refinanciamiento; cláusula de intercambio recíproca. Endeudamiento neto informativo del GF (art. 1o.): 1,906,069.4 = déficit del GF 1,906.1 mmp ✓; techo 1,990,000 > endeudamiento 1,906,069.4 > déficit presupuestario 1,693,000.0: los tres objetos separados, como en 2023.

**Flujo–acervo ex ante 2024:** ΔSHRFSP = 48.8 − 46.5 = **+2.3 pp**; RFSP 5.4; efecto del PIB nominal (+7.54 %): −46.5 × 0.0754/1.0754 = **−3.26**; suma 2.14; residuo +0.16 (tipo de cambio 17.3 → 17.6, +1.7 % sobre 11.8 pp externos ≈ +0.2). Cierra al décimo, como en 2023.

**Mediano plazo (p. 81, 122):** RFSP 2.6 en 2025 y 2.7 en 2026–2029; balance −2.1/−2.2; primario +0.9 (2025) → +0.3; SHRFSP 48.8 constante; costo financiero 3.7 → 2.5 % del PIB; **pensiones y jubilaciones 4.4 (2024) → 4.7 % del PIB (2029)**; inversión física 2.6 → 2.4; programable pagado 18.8 → 16.4 en 2025 (**−2.4 pp en un año**: el ajuste de 2025 recae en el programable).

**Sensibilidades 2024 (p. 82, mmp):** 0.5 pp de PIB = 24.4; 1 dpb = 13.4; 20 centavos de apreciación = −7.5 neto (petroleros −10.3, costo financiero +2.8, misma contradicción de signo en la nota que en 2023); 50 mbd = 17.9; 100 pb = 30.5 (incluye IPAB).

**Contingencias (p. 83–87):** pasivo pensionario ver §8; PAM 465,048.7 = 1.4 % del PIB con 6,000 pesos bimestrales (+25 %) para "más de 11 millones"; AFORE 5,551 mmp = 19 % del PIB (jun-2023); seguro catastrófico 5 mmp vigente al 5-jul-2024 (esta vez sí vigente); bono catastrófico 485 mdd a marzo 2024; FCL 47 mmd; reservas 204 mmd; Pidiregas exposición 118,282 mdp; depósitos 7.04 bn (22.3 % del PIB), ICAP 19.49 %.

---

## 5. Apartado de educación: dónde vive cada peso (analíticos del PEF aprobado 2023 y 2024; DEC 2023 y 2024)

Todas las cifras de esta sección en **mdp corrientes del PEF aprobado** salvo indicación; variación real con 1.0479. **Marca: PEF aprobado, no proyecto.** Donde el aprobado 2024 difiere del proyecto se da también el proyecto reconstruido.

### 5.1 Función Educación (finalidad 2 Desarrollo Social, función 5), Gobierno Federal bruto

| ramo | 2023 | 2024 | var. real | 2024, % de la función |
|---|---|---|---|---|
| 33 Aportaciones federales (FONE, FAETA, FAM IE) | 484,899.5 | **526,250.1** | +3.6 | 51.0 |
| 11 Educación Pública (parte educativa) | 376,296.6 | **411,848.3** | +4.4 | 39.9 |
| 25 Previsiones y aportaciones (CDMX, previsiones FONE/FAETA) | 72,743.8 | 82,460.5 | +8.2 | 8.0 |
| 08 Agricultura (Antonio Narro, Chapingo) | 5,048.6 | 5,346.7 | +1.1 | 0.5 |
| 07 Defensa (sistema educativo militar) | 3,520.8 | 3,854.1 | +4.5 | 0.4 |
| 13 Marina | 1,904.2 | 2,230.0 | +11.8 | 0.2 |
| 47 Entidades no sectorizadas | 597.6 | 631.7 | +0.9 | 0.1 |
| **Función Educación, GF bruto** | **945,011.1** | **1,032,621.4** | **+4.3** | 100 |

Entidades de control directo (IMSS, ISSSTE, Pemex, CFE): función Educación = **0** en ambos años (el EBDI del ISSSTE, 3,013.0 mdp en 2024, está en función Protección Social). No hay "función educación" fuera del Gobierno Federal.

**Por subfunción (GF bruto):**

| subfunción | 2023 | 2024 | var. real | 2024 ramo 11 / 33 / 25 / otros |
|---|---|---|---|---|
| 1 Educación básica | 589,264.0 | **650,707.5** | +5.4 | 90,955.3 / 509,634.7 / 49,935.3 / 182.1 |
| 2 Educación media superior | 140,856.0 | 145,417.1 | −1.5 | 135,714.4 / 6,745.1 / 0 / 2,957.6 |
| 3 Educación superior | 153,078.8 | 165,466.5 | +3.2 | 154,210.1 / 6,276.5 / 1,378.4 / 3,601.5 |
| 4 Posgrado | 9,665.2 | 10,322.0 | +1.9 | 7,862.3 / 0 / 0 / 2,459.7 |
| 5 Educación para adultos | 5,073.1 | 5,452.1 | +2.6 | 1,858.3 / 3,593.8 / 0 / 0 |
| 6 Otros servicios educativos y actividades inherentes | 47,074.0 | 55,256.3 | **+12.0** | 21,247.8 / 0 / 31,146.9 / 2,861.7 |

Las seis subfunciones de 2023 coinciden exactamente con las que CIEP 2023 publicó en su lámina (589,264; 140,856; 153,079; 9,665; 5,073; 47,074): el aprobado 2023 no cambió respecto al proyecto en esta función. La subfunción 6 crece 12 % real porque el Ramo 25 lleva ahí las **previsiones salariales** del FONE y FAETA (25,645.5 → 31,146.9) y el Ramo 11 el gasto administrativo central (PPs M001, P001, O001, E068, U080).

**Por tipo de gasto y capítulo (GF, 2024):** corriente (TG 1) 1,006,868.8 (97.5 %); pensiones (TG 2) 20,966.2; inversión física (TG 3) **1,048.4** (2023: 155.4); TG 7 3,738.0. Capítulos: 1000 servicios personales 181,310.8 (17.6 %); 4000 transferencias y subsidios 265,479.0 (25.7 %); **8000 participaciones y aportaciones 552,199.0 (53.5 %)**; 6000 obra pública 1,048.4 (0.1 %). Más de la mitad de la función es transferencia etiquetada a estados; la inversión física directa es 0.1 %.

### 5.2 Ramo 11 (SEP) por función

| | 2023 | 2024 A | 2024 p (reconstruido) |
|---|---|---|---|
| Ramo 11 total | 402,276.7 | **439,017.9** | 425,755.5 (DEC Anexo 1; CGPE p. 61, "425.8 mil millones, 19.3 % de los ramos administrativos") |
| … función Educación | 376,296.6 | 411,848.3 | 398,585.9 |
| … función CTI (investigación, Cinvestav) | 18,256.6 | 19,064.4 | 19,064.4 |
| … función Cultura y deporte | 7,489.4 | 7,855.9 | 7,855.9 |
| … coordinación (O001) | 234.1 | 249.4 | 249.4 |

**Cámara 2024:** +13,262.4 mdp íntegramente en S072 Becas de Educación Básica para el Bienestar Benito Juárez (36,607.4 en el proyecto, que es la cifra del Anexo 18 del decreto y cierra con "Programas de Becas 87,675.0" del CGPE = 36,607.4 + 39,366.6 + 11,701.1; **49,869.8 aprobados**). Con el aprobado el Ramo 11 crece **+4.1 % real**; con el proyecto **+1.0 %** (CGPE p. 117). La diferencia entre el proyecto y el aprobado (13.3 mmp) es tres veces mayor que el crecimiento real del proyecto (4.2 mmp).

**Ramo 11 por programa (2023 → 2024 A, mdp; var. real):** U006 Subsidios para organismos descentralizados estatales 105,468.8 → 110,558.4 (0.0); E010 Servicios de educación superior y posgrado 62,120.4 → 66,430.7 (+2.1); E007 Servicios de EMS 53,551.6 → 56,579.1 (+0.8); S072 Becas EB 34,922.1 → 49,869.8 (+36.3; proyecto 36,607.4, 0.0); S311 Beca Universal EMS 37,554.3 → 39,366.6 (0.0); U282 La Escuela es Nuestra 27,052.9 → 28,358.3 (0.0); E021 Investigación científica 17,992.7 → 18,944.2 (+0.5); S283 Jóvenes Escribiendo el Futuro 11,162.4 → 11,701.1 (0.0); U080 Apoyos a centros y organizaciones 9,725.7 → 10,195.0 (0.0); E066 Educación inicial y básica comunitaria 5,562.4 → 5,836.6 (0.0); S243 Becas Elisa Acuña 1,927.6 → 2,020.6 (0.0); E064 INEA 1,642.6 → 1,727.5 (+0.4); U083 Universidades para el Bienestar 1,476.4 → 1,547.6 (0.0; CGPE 1,562.6 incluye la UR MEY completa); K009 Proyectos de infraestructura social 145.0 → 1,170.0 (+670 %); S312 Expansión de la educación inicial 826.6 → 866.5 (0.0). **Patrón:** 14 de los 20 programas mayores del Ramo 11 crecen exactamente 4.8 % nominal, que es el deflactor del PIB 2024: variación real 0.0 %. Es una actualización mecánica por inflación, no una asignación; los únicos programas con crecimiento real son E010 (+2.1), E007 (+0.8), K009 (+670 %, sobre 145 mdp) y, por la Cámara, S072.

**Ramo 11 por unidad responsable (top, 2024 A):** O00 Coordinación Nacional de Becas 101,324.2 (23.1 % del ramo; 84,002.2 en 2023, +15.1 % real con la reasignación; proyecto ≈ 88,061.8, 0.0 %); 511 DGESUI (subsidios a universidades estatales) 75,635.2 (+0.1); A3Q **UNAM 50,418.4** (+1.0); 180 DG La Escuela es Nuestra 28,358.3; 600 Subsecretaría de EMS 27,398.5; 611 DGETI 26,329.4; M00 **TecNM 21,715.2** (+1.9); B00 **IPN 21,361.5** (+0.5); 610 DGETA 13,219.8; 700 Unidad de Administración y Finanzas 9,909.1; A2M **UAM 9,465.5** (+4.4); L6W CONAFE 6,015.7; 514 DG Universidades Tecnológicas y Politécnicas 5,575.3; L6J CONALITEG 3,686.0; L4J Cinvestav 2,908.0; MDA INEA 1,869.3; MEY Universidades para el Bienestar 1,562.6; A00 UPN 1,077.1.

### 5.3 Ramo 33: FONE, FAETA, FAM

| fondo (PP) | 2023 | 2024 p (DEC Anexo 22) | 2024 A | var. real A |
|---|---|---|---|---|
| I013 FONE servicios personales | 416,012.8 | 454,187.0 | 454,187.0 | +4.2 |
| I014 FONE otros de gasto corriente | 11,283.4 | 11,823.4 | 11,823.4 | 0.0 |
| I015 FONE gasto de operación | 17,084.2 | 17,901.9 | 17,901.9 | 0.0 |
| I016 FONE fondo de compensación | 12,292.2 | 12,880.5 | 12,880.5 | 0.0 |
| **FONE total** | **456,672.7** | **496,792.7** | 496,792.7 | **+3.8** |
| I009 FAETA educación tecnológica | 5,388.7 | 5,798.0 | 5,798.0 | +2.7 |
| I010 FAETA educación de adultos | 3,307.3 | 3,593.8 | 3,593.8 | +3.7 |
| I007 FAM infraestructura educativa básica | 12,499.7 | —* | 12,842.0 | −2.0 |
| I008 FAM infraestructura educativa MS y S | 7,031.1 | —* | 7,223.6 | −2.0 |
| FAM infraestructura educativa, total | 19,530.8 | 20,155.4 | 20,065.6 | −2.0 |
| Ramo 33, función Educación | 484,899.5 | — | 526,250.1 | +3.6 |
| Ramo 33 total | 924,331.7 | 985,976.9 | 984,484.5 | +1.6 |

\* El decreto da FAM infraestructura educativa como una línea (20,155.4); el reparto básica / MS-S es del analítico aprobado (20,065.6, tras −89.8 de la Cámara). **El FONE es la partida dominante del gasto educativo: 496.8 mmp = 48.1 % de la función Educación del GF y 1.13 × el Ramo 11 completo.**

**FONE por entidad federativa (I013–I016, 2024 A, mdp; participación; var. real):** Estado de México 49,009.1 (9.9 %; +2.3); Veracruz 36,335.3 (7.3; +3.6); Oaxaca 31,126.2 (6.3; +5.7); Jalisco 24,740.3 (5.0; +4.2); Chiapas 24,657.5 (5.0; +2.7); Guerrero 24,412.3 (4.9; +5.9); Michoacán 23,857.4 (4.8; +3.1); Puebla 22,799.5 (4.6; +3.3); Guanajuato 20,543.9 (4.1; +3.2); Hidalgo 18,941.7 (3.8; +5.8); Nuevo León 18,703.0 (3.8; +3.7); Tamaulipas 16,634.5 (3.3; +3.8); Chihuahua 16,202.3 (3.3; +4.3); San Luis Potosí 15,114.5 (3.0; +5.1); Baja California 14,267.3 (2.9; +1.8); Sinaloa 13,856.9 (2.8; +3.3); Coahuila 13,603.9 (2.7; +3.4); Sonora 11,304.9 (2.3; +3.4); Durango 10,142.5 (2.0; +5.1); Tabasco 9,670.4 (1.9; +2.8); Morelos 9,535.4 (1.9; +4.4); Zacatecas 9,187.4 (1.8; +4.1); Querétaro 8,814.3 (1.8; +3.9); Yucatán 8,202.8 (1.7; +3.9); Aguascalientes 7,798.6 (1.6; +3.8); Quintana Roo 7,362.5 (1.5; +3.3); Tlaxcala 7,133.5 (1.4; +3.9); Nayarit 6,835.0 (1.4; +4.6); Baja California Sur 5,930.7 (1.2; +2.4); Campeche 5,613.6 (1.1; +4.0); Colima 4,413.2 (0.9; +4.5); no distribuible 42.6. **La Ciudad de México no está en el FONE:** sus servicios de educación básica y normal van por el Ramo 25 (51,864.2 en 2024; 47,388.2 en 2023; +4.4 % real). Sin CONAPO no se computa FONE por habitante ni por alumno; la fórmula de distribución (LCF art. 27) no está en las piezas en carpeta y no se puede decir si cambió.

### 5.4 Ramo 25

| | 2023 | 2024 | var. real |
|---|---|---|---|
| Aportaciones para educación básica y normal en la CDMX | 47,388.2 | 51,864.2 | +4.4 |
| Previsiones salariales y económicas (CDMX, FONE, FAETA) | 25,394.5 | 30,654.3 | +15.2 |
| **Ramo 25 total** | 72,782.7 | **82,518.5** | **+8.2** |

Las previsiones (30.7 mmp) se registran en subfunción 6 y se distribuyen durante el año al FONE (Anexo 24: FONE 25,637.0; FAETA 311.9). Es gasto educativo que **no aparece en el FONE del decreto** al momento de aprobar.

### 5.5 Educación superior, becas, CTI, cultura

- **Subsidios a universidades públicas estatales (U006, UR 511):** 110,558.4 en 2024 (0.0 % real); por entidad en DEC Anexo 29: 74,688.8 (2023: 71,250.5; +0.0 % real) —la diferencia con el PP (35.9 mmp) es la parte del U006 fuera del Anexo 29 (UR 514, 515 y otras)—; Jalisco 7,321.6, Nuevo León 6,636.2, Sinaloa 5,541.3, Puebla 5,257.0.
- **Universidades federales (UR en Ramo 11):** UNAM 50,418.4 (+1.0 % real), IPN 21,361.5 (+0.5), TecNM 21,715.2 (+1.9), UAM 9,465.5 (+4.4), Cinvestav 2,908.0, UPN 1,077.1, Antonio Narro (Ramo 08) 1,260.5. **Todas en el Ramo 11 (salvo Narro); ninguna en función CTI salvo E021.**
- **Becas, por ramo (2024 A):** Ramo 11: S072 EB 49,869.8 (proyecto 36,607.4), S311 EMS 39,366.6, S283 JEF 11,701.1, S243 Elisa Acuña 2,020.6 → **102,958.1** (proyecto 89,695.7); Ramo 38: S190 Becas de posgrado y apoyos a la calidad (Conahcyt); Ramo 48: Becas artísticas; Ramos 07 y 13: becas para hijos del personal militar; Ramo 25: becas para población atendida por el sector educativo (199.0). **Las tres becas Benito Juárez viven en el Ramo 11 (UR O00), no en Bienestar.** El CGPE agrupa las tres como "Programas de Becas 87,675.0" (proyecto).
- **CTI:** Ramo 38 33,170.7 (0.0 % real; renombrado Humanidades, Ciencias, Tecnologías e Innovación; UR 90X = Conahcyt 25,722.4); función CTI del GF incluye además E021 del Ramo 11 (18,944.2). Anexo 12 (programa transversal de CTI) 148,154.2 (2023: 128,746.3; +9.8 % real).
- **Cultura y deporte:** Ramo 48 16,754.9 (+0.4 % real); función 4 del Ramo 11 7,855.9 (Conade 2,636.2).

### 5.6 Suma por ramos ↔ suma por función (la reconciliación obligatoria)

| perímetro, 2024 A | mdp | % PIB (34,374.5) |
|---|---|---|
| Ramo 11 completo | 439,017.9 | 1.28 |
| Ramo 11 + Ramo 25 | 521,536.4 | 1.52 |
| Ramo 11 + 25 + FONE + FAETA + FAM IE (ramos "educativos") | 1,047,724.5 | 3.05 |
| **Función Educación, GF bruto** | **1,032,621.4** | **3.00** |
| Función Educación neta (CGPE p. 66: 22.4 % × 4,384.6) | 982,190 | 2.86 |
| Función Educación + CTI GF (33,085.1 + 18,944.2 + E021…) + cultura/deporte del Ramo 11 | ≈ 1,090,000 | 3.2 |

La diferencia entre "ramos educativos" (1,047.7) y la función (1,032.6) son 15.1 mmp: las funciones CTI y Cultura del Ramo 11 (26.9) menos la educación que vive fuera de esos ramos (Defensa, Marina, Agricultura, ENS: 12.1). **La diferencia entre la función bruta (1,032.6) y la neta del CGPE (982.2) son ≈ 50 mmp de operaciones compensadas (aportaciones ISSSTE y transferencias a entidades) que el CGPE netea y los analíticos no.** Con 2023: función bruta 945.0 (3.01 % del PIB de 31,401.7; 2.96 % con el PIB revisado 31,963.0), neta 908.9 (23.3 % × 3,900.7). En 2024 la función bruta crece **+4.3 % real** y el Ramo 11 aprobado **+4.1 %** (proyecto +1.0 %).

**Serie oficial de la función Educación, % del PIB (CGPE 2024 p. 104, neta, base 2018):** 2017 3.1; 2018 3.0; 2019 2.9; 2020 3.2; 2021 3.0; 2022 2.9; 2023 aprobado 2.8; 2023 estimado **2.7**; diferencia 2023–2017 −0.3 pp (−6.1 % real). 2024 proyecto: 2.86 (cálculo propio con p. 66). La función pierde 0.4 pp del PIB entre 2017 y 2023 estimado y recupera 0.1–0.2 en 2024.

**Cámara 2024, todos los ramos (aprobado − proyecto, mdp):** Ramo 11 +13,262.4; Ramo 09 SICT +7,189.1; Ramo 18 Energía **−25,442.9** (compensado en la LIF con +25,442.9 de ingresos propios de Pemex y −25,442.9 del FMP); Ramo 03 Poder Judicial −6,465.1; Ramo 22 INE −5,003.2; Ramo 28 participaciones −4,807.4; Ramo 01 Legislativo −1,636.8; Ramo 33 −1,492.4; Ramo 23 −889.3; Ramo 41 Cofece −86.2; Ramo 44 INAI −71.0. Suma −25,442.8 = el traslado de la aportación a Pemex. Gasto neto total sin cambio (9,066,045.8). Entidades: Pemex aprobado 624,805.6 (bruto) vs proyecto 599,362.6 (+25,443.0); IMSS, ISSSTE y CFE sin cambio.

### 5.7 Lo que el paquete dice de educación en texto (CGPE p. 57, 61–62, 66)

"Fortalecimiento del sector educativo en las vertientes de apoyo a los estudiantes, mediante los programas de becas, y el apoyo a la infraestructura con La Escuela es Nuestra" (p. 57). Ramo 11: 425.8 mmp, 19.3 % de los ramos administrativos; seis programas nombrados sin cifra (becas EB, beca EMS, JEF, LEEN, Universidades para el Bienestar, libros de texto) (p. 61–62). Función educación 22.4 % del desarrollo social (p. 66). **No hay en el CGPE, la ILIF ni el DEC ninguna cifra de matrícula, cobertura, planteles ni docentes, ni supuesto demográfico para educación**; el único horizonte demográfico del paquete es el de pensiones (p. 83–84: 65+ de 8.2 % en 2023 a 17.0 % en 2050). El horizonte de mediano plazo (p. 122) no desagrega funciones.

---

## 6. Diffs previos (instrucción fase 2)

**6.1 Códigos de programa y UR, 2023 → 2024 (analíticos aprobados):**
- Ramo 11: desaparece K027 Mantenimiento de infraestructura (275.6 en 2023); la UR N00 Coordinación General @prende.mx pasa a **418 Dirección General @prende.mx** (cambio de código, mismo nombre). Ningún PP nuevo.
- Ramo 33 y Ramo 19: la UR de gestión cambia de 416 DGPyP "A" a 420 DGPyP "C" (reasignación administrativa en SHCP, sin efecto en montos).
- Ramo 38: Conacyt → Consejo Nacional de Humanidades, Ciencias y Tecnologías (UR 90X, mismo código; el ramo se renombra en el Anexo 1).
- Ramo 48: K009 Proyectos de infraestructura social del sector cultura → R001 Provisiones para el desarrollo de infraestructura cultural; desaparece la UR 330 DG de Publicaciones.
- Ramo 20: desaparece el PP 016 Articulación de políticas integrales de juventud y la UR VUY Instituto Mexicano de la Juventud (IMJUVE sale de Bienestar).
- Ramo 25: sin cambios. Subfunciones de educación: mismas seis en ambos años.

**6.2 Anexo 3 del decreto (gastos obligatorios):** 2023: 5,355,844.5 / con pensiones 6,689,188.3; 2024: **5,828,550.2 / 7,327,588.8** (+8.8 % / +9.5 % nominal; +3.9 % / +4.5 % real). Pensiones implícitas en el Anexo: 1,333.3 → **1,499.0 mmp** (= la línea de pensiones de la clasificación económica, p. 60). El decreto sigue sin definir la composición.

**6.3 Anexos transversales con educación (DEC 2023 → 2024, proyecto):**

| anexo | 2023 | 2024 | var. real | renglones educativos 2024 |
|---|---|---|---|---|
| 18 Niñas, niños y adolescentes | 899,447.2 | **966,107.8** | +2.5 | Ramo 11 213,090.1 (2023: 205,347.5); Ramo 33 556,689.3 (2023: 510,734.3; FONE completo); Ramo 25 49,935.3; becas EB 36,607.4 (= proyecto completo); LEEN 28,358.3; U006 33,712.4 |
| 17 Jóvenes | 515,946.4 | 570,856.9 | +5.6 | Ramo 11 315,695.5 (2023: 298,283.2); Ramo 33 132,683.0; U006 110,335.1 (tres renglones); Ramo 25 17,119.4 |
| 12 Ciencia, tecnología e innovación | 128,746.3 | 148,154.2 | +9.8 | Ramo 38 38,178.4; Ramo 11 52,858.7 |
| 10 Pueblos indígenas | 141,353.9 | 149,691.9 | +1.1 | Ramo 11 17,878.6; becas EB 10,250.1 |
| 13 Igualdad | 346,077.0 | 409,107.9 | +12.8 | Ramo 11 92,596.9; becas EB 28,293.6 |
| 14 Grupos vulnerables | 484,340.4 | 622,335.6 | +22.6 | Ramo 11 47,143.0; LEEN 26,940.4 |

El Anexo 18 lleva el FONE completo (556.7 mmp) como gasto en niñez: 57.6 % del anexo es nómina educativa federalizada.

**6.4 Definiciones del CGPE, 2023 → 2024:** año base del PIB 2013 → 2018 en toda la serie; "déficit público" (2023) sigue como "déficit presupuestario" (p. 99, cuadro I.1) y "déficit público de 4.9 %" en texto (p. 46) para el mismo objeto; cuadros con dos columnas 2023 (aprobado sobre PIB revisado, estimado); "Cifras excluyendo/incluyendo ROBM" en las figuras de p. 47–48 (novedad: el remanente de Banxico como partida informativa); DUC 40 → 35 %; regla de déficit: costo financiero (2023) → precio del petróleo (2024).

## 7. Reconciliaciones obligatorias

1. **ILIF ↔ CGPE en ingresos:** presupuestarios 9,066,045.8 − 1,737,050.6 = **7,328,995.2** = CGPE p. 119 ✓. Tributarios ILIF numeral 1 = 4,942,030.3; CGPE = 4,941,540.8; diferencia **489.5 mdp** (2023: 3,417.8; 2022: 56.9; 2021: 57.0); petroleros ILIF (Pemex 744,362.7 + FMP 303,217.2 = 1,047,579.9) vs CGPE 1,048,069.4: **+489.5** ✓ la misma partida, reclasificada de impuestos a petroleros del GF (ISR de contratistas y asignatarios). Reaparece, con un orden de magnitud distinto cada año y sin nota.
2. **Suma por ramos ↔ suma por función en educación:** ver §5.6. Ramos educativos 1,047.7 vs función bruta 1,032.6 vs función neta 982.2 (2024); la diferencia es el hallazgo (26.9 de CTI y cultura dentro del Ramo 11; 12.1 de educación fuera de los ramos educativos; ≈50 de neteo).
3. **Flujo contra acervo:** ver §4; cierra a 0.2 pp.
4. **Gasto neto total:** DEC art. 2 9,066,045.8 = LIF total ✓; Anexo 1 suma A–E 10,406,689.0 − neteo 1,340,643.2 = 9,066,045.8 ✓; analítico GF aprobado 7,431,571.1 + entidades 2,975,117.9 − neteo = 9,066,045.8 ✓ (10,406,689.0).

## 8. Series de seguimiento permanente (instrucción §4; sin interpretación)

| serie | 2020 | 2021 | 2022 | 2023 | **2024** | fuentes 2024 |
|---|---|---|---|---|---|---|
| Pensiones IMSS / cuotas IMSS, **serie aprobada** (PEF TG 4 / LIF art. 1o.) | — | — | 1.545 (636,461.8 / 411,852.5) | 1.593 (750,252.1 / 470,845.4) | **1.627** (870,981.7 / 535,254.7) | analítico entidades 2024 (GYR, TG 4); LIF aprobada 2024 |
| … serie ex ante (EM / ILIF) | 1.31 | 1.46 | — (EM ausente) | — | — | EM ausente desde 2022; ILIF cuotas = LIF cuotas en 2022–2024, de modo que los valores "híbridos" de 2023 son la serie aprobada |
| Pasivo pensionario, % del PIB | 43.2 (CGPE 2020; pesos 2018; saldo 2018) | 47.7 (CGPE 2021; pesos 2019; saldo 2019) | 52.1 (CGPE 2022; pesos 2020; saldo 2020) | 43.6 (CGPE 2023; pesos 2021; saldo 2021; ISSSTE saldo 2020) | **38.1** (CGPE 2024 p. 85; pesos de 2022; saldo 2022; ISSSTE saldo 2021 "actualizado por inflación"; PIB base 2018) | IMSS-RJP 3,094.6 (10.9); ISSSTE 5,571.2 (19.6); CFE 601.6 (2.1); Pemex 1,306.9 (4.6); otros 274.6 (1.0); total 10,848.8 |
| Supuesto oficial de crecimiento real de pensiones | — | 7.0 % | 4.2 % | 4.2 % | (trayectoria p. 122: 4.4 → 4.7 % del PIB 2024–2029; supuesto explícito no localizado en fase 2) | CGPE p. 122 |
| Tributarios / gastos obligatorios con pensiones | — | 0.671 | 0.674 | 0.691 | **0.674** (4,942,030.3 / 7,327,588.8); con cuotas IMSS 0.747 | ILIF art. 1o.; DEC Anexo 3 |
| Costo financiero / tributarios | — | 0.205 | 0.201 | 0.234 | **0.256** (1,263,994.1 / 4,941,540.8) | CGPE p. 119; DEC Anexo 8 |
| SHRFSP / tributarios, años | — | — | 3.6 | 3.4 | **3.40** (16,787,906.1 / 4,941,540.8) | CGPE p. 119 |
| Pensiones + costo financiero / tributarios | — | — | — | 0.60 (con pensiones totales 1,692.9) / 0.52 (contributivas 1,333.3) | **0.66** con totales (1,499.0 + 465.0 + 27.9 + 1,264.0) / 4,941.5; **0.56** con contributivas (1,499.0 + 1,264.0) | CGPE p. 58, 60, 119 |

Notas: (i) el pasivo pensionario ahora tiene los tres campos (documento, fecha del saldo, pesos de qué año) en toda la serie: el 43.6 → 38.1 vuelve a caer 5.5 pp; con IMSS-RJP en pesos 3,348.6 (2021) → 3,094.6 (2022) y ISSSTE 5,869.7 → 5,571.2, la caída es de nuevo real en pesos y no solo de denominador; sigue congelada. (ii) La ficha de 2023 fijó 0.60 con pensiones **totales**; se reporta con las dos definiciones para que Cath elija; la instrucción §2.9 no lo precisa.

## 9. Añada de PIB (quinta declaración) adoptada

- **Ex ante 2024:** CGPE 2024, PIB base 2018, nominal 2023e **31,963.0** y 2024 **34,374.5** mmp. Toda razón a PIB de 2024 usa 34,374.5. Toda razón a PIB del aprobado 2023 usa **31,963.0** cuando se compara con 2024 (es lo que hace el CGPE 2024 en p. 113, 117, 119 con la nota */), y **31,401.7** (base 2013) solo cuando se restituye una cifra del CGPE 2023. Se declara en cada cuadro.
- Deflactor 1.0479. Cuando dos añadas cambien el signo de una lectura se presentan ambas.

## 10. Lo que 2024 tiene de particular (verificado contra el texto)

- Último paquete de la administración; déficit presupuestario 4.9 % del PIB (el mayor de la serie 2017–2024), justificado con la regla petrolera del art. 11 RLFPRH; ajuste programado para 2025: programable pagado 18.8 → 16.4 % del PIB.
- Cambio de año base del PIB; "excluyendo/incluyendo ROBM".
- Reubicaciones institucionales que mueven el gasto entre ramos sin mover la función: IMSS-Bienestar de Ramo 12 a Ramo 47 (Salud −55.8 %); Tren Maya S.A. y el grupo aeroportuario a Defensa (Turismo −24.4 %; Defensa 259.4 mmp); aportación a Pemex/CFE en Ramo 18 (+273 %), que la Cámara sacó en parte.
- PAM a 6,000 pesos bimestrales (+25 %), 465.0 mmp = 1.4 % del PIB; pensiones de la clasificación económica +7.3 % real.
- Educación: función +4.3 % real (aprobado); Ramo 11 proyecto +1.0 %; **la Cámara añadió 13.3 mmp a becas de educación básica** (S072 +36.3 % real); FAM infraestructura educativa −2.0 % real; inversión física en la función 0.1 %.

## 11. Lista cerrada de cifras que un lector del paquete esperaría en un capítulo de educación (criterio de cobertura)

Ramo 11 total y variación (proyecto y aprobado); función Educación total (bruta o neta, declarada) y por subfunción; FONE total, por componente y por entidad; FAETA; FAM infraestructura educativa; Ramo 25 (CDMX y previsiones); las tres becas Benito Juárez con su ramo; LEEN; U006 y Anexo 29 por entidad; UNAM/IPN/UAM/TecNM; Conahcyt y función CTI; educación para adultos (INEA + FAETA adultos); educación inicial (E066, S312, nota 5/ del Anexo 1: 200 mdp); Anexo 18 (FONE dentro de NNA); función Educación en % del PIB, serie 2017–2023 (p. 104); educación dentro del desarrollo social (22.4 %); inversión física en educación (TG 3 = 1,048.4); tipo de gasto y capítulo; reasignaciones de la Cámara; supuesto de matrícula (ausente en el paquete); per cápita con denominador declarado (no computable desde la carpeta).
