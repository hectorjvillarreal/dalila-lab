# 03_ensanut_prepare.R — ENSANUT 2018-19 and Continua 2024.
# Builds: (a) forgone/cost-forgone care flags by SES and insurance (fig 6),
# (b) age-sex utilization rates = NTA-style allocation weights for ENIGH Tier 3,
# (c) preventive/curative motive split, 2024 (Task B ENSANUT side; the 2018
#     utilizadores module conditions on illness so it cannot yield a preventive
#     share — that asymmetry is itself reported).
# Variable names from data/ensanut_varmap.md, verified against shipped codebooks.
# All ENSANUT CSVs are semicolon-delimited with UTF-8 BOM.

source("scripts/00_common.R")

AGE_BRK <- c(0, 5, 15, 30, 45, 60, 65, 75, 85, Inf)
AGE_LAB <- c("0-4", "5-14", "15-29", "30-44", "45-59", "60-64", "65-74", "75-84", "85+")

read_semi <- function(path) {
  dt <- fread(path, sep = ";", encoding = "UTF-8")
  setnames(dt, toupper(names(dt)))
  dt
}

# ============================ 2018 =======================================
message("== ENSANUT 2018 roster")
res <- read_semi(file.path(DATA, "ensanut", "ensanut2018", "CS_RESIDENTES.csv"))

res[, sex := fifelse(SEXO == 1, "male", "female")]
res[, age_grp := cut(EDAD, AGE_BRK, right = FALSE, labels = AGE_LAB)]

# insurance (first affirmative in the P3_10 dummy block; uninsured = P3_10_11)
res[, insurance := fcase(
  P3_10_01 == 1, "IMSS",
  P3_10_02 == 1 | P3_10_03 == 1, "ISSSTE",
  P3_10_04 == 1 | P3_10_05 == 1 | P3_10_06 == 1, "Pemex/Armed",
  P3_10_07 == 1 | P3_10_08 == 1, "SeguroPopular/Prospera",
  P3_10_09 == 1, "Private",
  P3_10_11 == 1, "None",
  default = "Other/DK")]

# forgone care among those with a health problem in the last month
res[, need := P4_3 == 1]
res[, forgone := need & P4_5 == 2]
res[, cost_reason := (P4_9_12 == 1 | P4_9_13 == 1 | P4_9_14 == 1)]
res[, cost_forgone := forgone & cost_reason]
# two-week outpatient utilization (allocation weight numerator)
res[, util2w := !is.na(P4_11) & P4_11 == 1]

d18 <- svydesign(ids = ~UPM_DIS, strata = ~EST_DIS, weights = ~FACTOR,
                 data = res, nest = TRUE)

fg <- function(des, byf) {
  z <- svyby(~forgone + cost_forgone, byf, subset(des, need), svymean, na.rm = TRUE)
  data.table(z)
}
f6_18 <- rbindlist(list(
  fg(d18, ~ESTRATO)[, grp := paste0("estrato", ESTRATO)],
  fg(d18, ~insurance)[, grp := insurance],
  fg(d18, ~sex)[, grp := sex]), fill = TRUE)
f6_18[, `:=`(wave = 2018, base = "need last month, all ages",
             ESTRATO = NULL, insurance = NULL, sex = NULL)]

# 12-month Commonwealth-style cost battery (utilizadores module, F_SERSA)
ser <- read_semi(file.path(DATA, "ensanut", "ensanut2018", "CS_SERV_SALUD.csv"))
ser[, ESTRATO := ESTRATO]
dser <- svydesign(ids = ~UPM_DIS, strata = ~EST_DIS, weights = ~F_SERSA,
                  data = ser, nest = TRUE)
cb <- svyby(~I(P8_1_1 == 1) + I(P8_1_2 == 1) + I(P8_1_3 == 1), ~ESTRATO, dser,
            svymean, na.rm = TRUE)
fwrite(data.table(cb), file.path(OUTTAB, "fig6_cost_battery_2018.csv"))

# utilization by age-sex (allocation weights)
u18 <- data.table(svyby(~util2w, ~sex + age_grp, d18, svymean, na.rm = TRUE))
u18[, wave := 2018]
fwrite(u18, file.path(OUTTAB, "ensanut_util_weights_2018.csv"))

saveRDS(res[, .(FACTOR, EST_DIS, UPM_DIS, ESTRATO, sex, age_grp, EDAD, insurance,
                need, forgone, cost_forgone, util2w)],
        file.path(DERIV, "ensanut2018_roster.rds"))

# ============================ 2024 =======================================
message("== ENSANUT 2024 roster")
# the _ICB integrantes file already carries the NSE index columns (NSEF terciles,
# NSE5F quintiles), fully populated — no merge with the NSE file needed
itg <- read_semi(file.path(DATA, "ensanut", "ensanutcontinua2024",
                           "integrantes_ensanut2024_w_ICB.csv"))

itg[, sex := fifelse(H0302 == 1, "male", "female")]
itg[, age_grp := cut(H0303, AGE_BRK, right = FALSE, labels = AGE_LAB)]

itg[, insurance := fcase(
  H0310A == 1, "IMSS",
  H0310A == 2, "ISSSTE",
  H0310A %in% c(4, 5, 6), "Pemex/Armed",
  H0310A == 11, "IMSS-Bienestar",
  H0310A == 8, "Private",
  H0310A == 10, "None",
  default = "Other/DK")]

itg[, need := H0401 == 1]
itg[, not_sought := need & H0404 == 2]
itg[, not_attended := need & H0404 == 1 & H0406 == 2]
itg[, forgone := not_sought | not_attended]
itg[, cost_ns := not_sought &
      (H0405A %in% 4 | H0405B %in% 4 | H0405C %in% 4)]
itg[, cost_na := not_attended &
      (H0407A %in% c(8, 9) | H0407B %in% c(8, 9) | H0407C %in% c(8, 9))]
itg[, cost_forgone := cost_ns | cost_na]
itg[, util3m := need & H0406 == 1]

d24 <- svydesign(ids = ~UPM, strata = ~EST_SEL, weights = ~PONDE_F,
                 data = itg, nest = TRUE)

f6_24 <- rbindlist(list(
  data.table(svyby(~forgone + cost_forgone, ~NSEF, subset(d24, need & !is.na(NSEF)),
                   svymean, na.rm = TRUE))[, grp := paste0("nse_tercile", NSEF)],
  data.table(svyby(~forgone + cost_forgone, ~insurance, subset(d24, need),
                   svymean, na.rm = TRUE))[, grp := insurance],
  data.table(svyby(~forgone + cost_forgone, ~sex, subset(d24, need),
                   svymean, na.rm = TRUE))[, grp := sex]), fill = TRUE)
f6_24[, `:=`(wave = 2024, base = "need last 3 months, all ages",
             NSEF = NULL, insurance = NULL, sex = NULL)]

fwrite(rbindlist(list(f6_18, f6_24), fill = TRUE),
       file.path(OUTTAB, "fig6_forgone_care.csv"))

# utilization by age-sex (allocation weights; attended a need, 3-month window)
u24 <- data.table(svyby(~util3m, ~sex + age_grp, d24, svymean, na.rm = TRUE))
u24[, wave := 2024]
fwrite(u24, file.path(OUTTAB, "ensanut_util_weights_2024.csv"))

# preventive / curative / ambiguous split of last need (2024 only; h0402)
# preventive: 28 vacunación, 30 chequeo, 32 control prenatal, 55 otro-prevención
# ambiguous: 16/17 chronic control-seguimiento-diagnóstico, 52 otra causa, 99 NS
itg[, motive_class := fcase(
  H0402 %in% c(28, 30, 32, 55), "preventive",
  H0402 %in% c(16, 17, 52, 99), "ambiguous",
  !is.na(H0402) & need, "curative",
  default = NA_character_)]
mm <- data.table(svymean(~factor(motive_class),
                         subset(d24, need & !is.na(motive_class))))
pc <- data.table(svyby(~I(motive_class == "preventive") + I(motive_class == "ambiguous"),
                       ~NSEF, subset(d24, need & !is.na(motive_class) & !is.na(NSEF)),
                       svymean, na.rm = TRUE))
fwrite(pc, file.path(OUTTAB, "ensanut2024_preventive_share_by_nse.csv"))

saveRDS(itg[, .(FOLIO_I, FOLIO_INT, PONDE_F, EST_SEL, UPM, NSEF, NSE5F, sex,
                age_grp, H0303, insurance, need, forgone, cost_forgone,
                util3m, motive_class)],
        file.path(DERIV, "ensanut2024_roster.rds"))

message("03_ensanut_prepare done")
