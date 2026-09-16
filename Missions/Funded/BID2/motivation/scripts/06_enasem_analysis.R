# 06_enasem_analysis.R — ENASEM analyses.
# (1) Reproduction check of Judy's frailty-mortality probit (Model B:
#     frailty 2018 -> death 2018-21; published pseudo-R2 0.142 full, 0.159
#     women) — the reconstructed index is PROVISIONAL pending her confirmation.
# (2) Observed 50+ OOP profile by age-sex (fig 2 validation data).
# (3) Spending response to frailty decline by wealth tercile + subsequent
#     health/survival (fig 10) — DESCRIPTIVE conditional patterns, not causal.
# (4) Attrition 2018->2021/2024 vs baseline frailty and wealth.

source("scripts/00_common.R")

p18 <- readRDS(file.path(DERIV, "enasem_person_2018.rds"))
p21 <- readRDS(file.path(DERIV, "enasem_person_2021.rds"))
p24 <- readRDS(file.path(DERIV, "enasem_person_2024.rds"))
sp  <- readRDS(file.path(DERIV, "enasem_spine.rds"))

defl <- inpc_deflators(c(2018, 2021, 2024))

# ---------- (1) mortality probit reproduction check -----------------------
d <- merge(p18, sp[, .(cunicah, np, fallecido_21, fallecido_24)],
           by = c("cunicah", "np"), all.x = TRUE)
d[, died_1821 := fallecido_21 %in% c(1, 2)]
d[, male := genero == 1]
d[, upper_sec := !is.na(educacion) & educacion >= 10]
d[, edad2 := edad^2]
d[, frailty2 := frailty^2]

mb <- d[!is.na(frailty) & !is.na(edad) & !is.na(factori) & factori > 0]
des <- svydesign(ids = ~upm_dis, strata = ~est_dis, weights = ~factori,
                 data = mb, nest = TRUE)
pseudo_r2 <- function(fit) 1 - fit$deviance / fit$null.deviance

fit_all <- svyglm(died_1821 ~ frailty + frailty2 + edad + edad2 + upper_sec + male,
                  des, family = quasibinomial(link = "probit"))
fit_m <- svyglm(died_1821 ~ frailty + frailty2 + edad + edad2 + upper_sec,
                subset(des, male), family = quasibinomial(link = "probit"))
fit_f <- svyglm(died_1821 ~ frailty + frailty2 + edad + edad2 + upper_sec,
                subset(des, !male), family = quasibinomial(link = "probit"))

chk <- data.table(
  sample = c("full", "men", "women"),
  n = c(nrow(mb), mb[male == TRUE, .N], mb[male == FALSE, .N]),
  deaths = c(mb[died_1821 == TRUE, .N], mb[male == TRUE & died_1821 == TRUE, .N],
             mb[male == FALSE & died_1821 == TRUE, .N]),
  pseudo_r2 = c(pseudo_r2(fit_all), pseudo_r2(fit_m), pseudo_r2(fit_f)),
  published = c(0.142, 0.118, 0.159),
  coef_frailty = c(coef(fit_all)["frailty"], coef(fit_m)["frailty"], coef(fit_f)["frailty"]),
  coef_frailty2 = c(coef(fit_all)["frailty2"], coef(fit_m)["frailty2"], coef(fit_f)["frailty2"]))
print(chk)

# sensitivity variants on the sample definition (published n = 14,867 / 1,229
# deaths suggests a restriction we cannot see from the .tex alone)
mb50 <- mb[edad >= 50]
des50 <- svydesign(ids = ~upm_dis, strata = ~est_dis, weights = ~factori,
                   data = mb50, nest = TRUE)
fit_50 <- svyglm(died_1821 ~ frailty + frailty2 + edad + edad2 + upper_sec + male,
                 des50, family = quasibinomial(link = "probit"))
mbE <- copy(mb)[, died_1821 := fallecido_21 == 2]     # ENASEM-fieldwork deaths only
desE <- svydesign(ids = ~upm_dis, strata = ~est_dis, weights = ~factori,
                  data = mbE, nest = TRUE)
fit_E <- svyglm(died_1821 ~ frailty + frailty2 + edad + edad2 + upper_sec + male,
                desE, family = quasibinomial(link = "probit"))
var_chk <- data.table(
  variant = c("age>=50", "deaths=ENASEM fieldwork only"),
  n = c(nrow(mb50), nrow(mbE)),
  deaths = c(mb50[died_1821 == TRUE, .N], mbE[died_1821 == TRUE, .N]),
  pseudo_r2 = c(pseudo_r2(fit_50), pseudo_r2(fit_E)))
print(var_chk)
fwrite(var_chk, file.path(OUTTAB, "enasem_probit_check_variants.csv"))
fwrite(chk, file.path(OUTTAB, "enasem_probit_reproduction_check.csv"))

# ---------- (2) observed OOP profile, 50+ (fig 2) -------------------------
brk50 <- c(50, 55, 60, 65, 70, 75, 80, 85, Inf)
lab50 <- c("50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80-84", "85+")
prof <- list()
for (yy in c(2018, 2021, 2024)) {
  pp <- get(paste0("p", substr(yy, 3, 4)))
  dfl <- defl[yr == yy, deflator]
  pp[, edad := suppressWarnings(as.numeric(edad))]
  pp[edad %in% c(888, 999), edad := NA]
  pp <- pp[!is.na(edad) & edad >= 50 & !is.na(factori) & factori > 0]
  pp[, age_grp := cut(edad, brk50, right = FALSE, labels = lab50)]
  pp[, sex := fifelse(genero == 1, "male", "female")]
  # quarterly, constant Aug-Nov 2024 pesos, to align with ENIGH quarterly units
  pp[, oop_q24 := oop_annual * dfl / 4]
  dd <- svydesign(ids = ~upm_dis, strata = ~est_dis, weights = ~factori,
                  data = pp, nest = TRUE)
  pr <- data.table(svyby(~oop_q24, ~sex + age_grp, dd, svymean, na.rm = TRUE))
  pr[, wave := yy]
  prof[[as.character(yy)]] <- pr
}
fwrite(rbindlist(prof), file.path(OUTTAB, "fig2_enasem_observed_profile.csv"))

# ---------- (3) dynamics: spending response to frailty decline (fig 10) ---
pan <- merge(
  p18[, .(cunicah, np, frailty18 = frailty, oop18 = oop_annual, wealth18 = wealth,
          edad18 = edad, genero, factori18 = factori, est_dis, upm_dis)],
  p21[, .(cunicah, np, frailty21 = frailty, oop21 = oop_annual)],
  by = c("cunicah", "np"))
pan <- merge(pan, sp[, .(cunicah, np, fallecido_24)], by = c("cunicah", "np"),
             all.x = TRUE)
pan <- merge(pan, p24[, .(cunicah, np, frailty24 = frailty)],
             by = c("cunicah", "np"), all.x = TRUE)

pan <- pan[!is.na(frailty18) & !is.na(frailty21) & !is.na(factori18) & factori18 > 0]
# wealth terciles (weighted, among panel members with wealth observed)
pw <- pan[!is.na(wealth18)]
setorder(pw, wealth18)
cw <- cumsum(pw$factori18) / sum(pw$factori18)
pw[, wtercile := pmin(3L, findInterval(cw, c(1/3, 2/3)) + 1L)]
pan <- merge(pan, pw[, .(cunicah, np, wtercile)], by = c("cunicah", "np"), all.x = TRUE)

pan[, dfrail := frailty21 - frailty18]
pan[, decline := dfrail >= 0.10]                       # ~1 decile of the index range
pan[, doop := (oop21 * defl[yr == 2021, deflator]) - (oop18 * defl[yr == 2018, deflator])]
pan[, oop21_r := oop21 * defl[yr == 2021, deflator]]
pan[, died_2124 := fallecido_24 == 1]

dpan <- svydesign(ids = ~upm_dis, strata = ~est_dis, weights = ~factori18,
                  data = pan[!is.na(wtercile)], nest = TRUE)

r1 <- data.table(svyby(~oop21_r + doop, ~decline + wtercile, dpan, svymean, na.rm = TRUE))
# separate calls: a joint formula would casewise-delete the deceased, whose
# frailty24 is necessarily missing
r2a <- data.table(svyby(~died_2124, ~decline + wtercile,
                        subset(dpan, !is.na(died_2124)), svymean, na.rm = TRUE))
r2b <- data.table(svyby(~frailty24, ~decline + wtercile,
                        subset(dpan, !is.na(frailty24)), svymean, na.rm = TRUE))
r2 <- merge(r2a, r2b, by = c("decline", "wtercile"))
fwrite(r1, file.path(OUTTAB, "fig10_spending_response_by_wealth.csv"))
fwrite(r2, file.path(OUTTAB, "fig10_subsequent_outcomes_by_wealth.csv"))
print(r1); print(r2)

# ---------- (4) attrition -------------------------------------------------
att <- merge(p18[, .(cunicah, np, frailty18 = frailty, wealth18 = wealth,
                     factori18 = factori, est_dis, upm_dis)],
             sp[, .(cunicah, np, fallecido_21, tipne_21)],
             by = c("cunicah", "np"), all.x = TRUE)
att[, in21 := paste(cunicah, np) %in% p21[, paste(cunicah, np)]]
att[, died21 := fallecido_21 %in% c(1, 2)]
att[, attrited := !in21 & !died21]
pw2 <- att[!is.na(wealth18)]
setorder(pw2, wealth18)
cw2 <- cumsum(pw2$factori18) / sum(pw2$factori18)
pw2[, wtercile := pmin(3L, findInterval(cw2, c(1/3, 2/3)) + 1L)]
att <- merge(att, pw2[, .(cunicah, np, wtercile)], by = c("cunicah", "np"), all.x = TRUE)
att[, frail_terc := cut(frailty18, quantile(frailty18, c(0, 1/3, 2/3, 1), na.rm = TRUE),
                        include.lowest = TRUE, labels = c("low", "mid", "high"))]
datt <- svydesign(ids = ~upm_dis, strata = ~est_dis, weights = ~factori18,
                  data = att[!is.na(factori18) & factori18 > 0], nest = TRUE)
a1 <- data.table(svyby(~attrited + died21, ~frail_terc, subset(datt, !is.na(frail_terc)),
                       svymean, na.rm = TRUE))
a2 <- data.table(svyby(~attrited + died21, ~wtercile, subset(datt, !is.na(wtercile)),
                       svymean, na.rm = TRUE))
fwrite(a1, file.path(OUTTAB, "enasem_attrition_by_frailty.csv"))
fwrite(a2, file.path(OUTTAB, "enasem_attrition_by_wealth.csv"))
print(a1); print(a2)
message("06_enasem_analysis done")
