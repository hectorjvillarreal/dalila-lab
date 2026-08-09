# 04_enigh_tier3.R — Tier 2 (per capita) and Tier 3 (estimated individual)
# age-sex profiles of household health spending, two independent methods:
#   (i)  survey-weighted regression of household health spending on counts of
#        members in each age-sex cell (no intercept; coefficient = implied
#        per-member spending), design-based CIs;
#   (ii) NTA-style allocation proportional to ENSANUT age-sex utilization
#        rates (derived in 03, never imported from published profiles);
#        ENSANUT 2018 rates weight ENIGH 2018/2020, ENSANUT 2024 rates weight
#        ENIGH 2022/2024.
# Tier 3 output is ALWAYS an estimate conditional on the allocation rule.
# Outputs: fig1 (age-sex profile, both methods), fig3 (by income tercile),
#          fig11 (stability across waves); all in output/tables.

source("scripts/00_common.R")

AGE_LAB <- c("0-4", "5-14", "15-29", "30-44", "45-59", "60-64", "65-74", "75-84", "85+")
cells <- as.vector(outer(c("male", "female"), AGE_LAB, paste, sep = "_"))

# 2018 file carries util2wTRUE (two-week window), 2024 util3mTRUE (three-month)
u18 <- fread(file.path(OUTTAB, "ensanut_util_weights_2018.csv"))
u24 <- fread(file.path(OUTTAB, "ensanut_util_weights_2024.csv"))
uw <- rbind(u18[, .(sex, age_grp, wave, u = util2wTRUE)],
            u24[, .(sex, age_grp, wave, u = util3mTRUE)])
util_wave <- function(y) if (y <= 2020) 2018 else 2024

reg_res <- list(); nta_res <- list(); nta_inc <- list()

for (y in ENIGH_YEARS) {
  message("== Tier 3, ", y)
  con <- readRDS(file.path(DERIV, sprintf("enigh_hh_%d.rds", y)))
  pob <- readRDS(file.path(DERIV, sprintf("enigh_pob_%d.rds", y)))

  # income terciles (weighted household counts, by ing_cor)
  setorder(con, ing_cor)
  cw <- cumsum(con$factor) / sum(con$factor)
  con[, inc_tercile := pmin(3L, findInterval(cw, c(1/3, 2/3)) + 1L)]

  # ---- method (i): regression on age-sex cell counts -------------------
  present <- cells[cells %in% names(con)]
  fml <- as.formula(paste("salud ~ 0 +",
                          paste0("`", present, "`", collapse = " + ")))
  des <- enigh_design(con)
  fit <- svyglm(fml, des)
  cf <- coef(fit); se <- sqrt(diag(vcov(fit)))
  rg <- data.table(cell = gsub("`", "", names(cf)), coef = cf, se = se, year = y,
                   method = "regression")
  rg[, c("sex", "age_grp") := tstrsplit(cell, "_", fixed = TRUE)]
  reg_res[[as.character(y)]] <- rg

  # ---- method (ii): NTA-style allocation by utilization weights --------
  u <- uw[wave == util_wave(y)]
  p <- merge(pob, con[, .(hh_id, salud, factor, upm, est_dis, tot_integ,
                          inc_tercile)], by = "hh_id")
  p[, sex := fifelse(sexo == 1, "male", "female")]
  p <- merge(p, u[, .(sex, age_grp, u)], by = c("sex", "age_grp"), all.x = TRUE)
  p[, usum := sum(u), by = hh_id]
  p[, alloc := fifelse(usum > 0, salud * u / usum, 0)]
  p[, alloc_pc := salud / tot_integ]   # Tier 2: equal split (per capita scale)

  pdes <- svydesign(ids = ~upm, strata = ~est_dis, weights = ~factor,
                    data = p, nest = TRUE)
  nt <- data.table(svyby(~alloc + alloc_pc, ~sex + age_grp, pdes, svymean,
                         na.rm = TRUE))
  nt[, `:=`(year = y, method = "nta_utilization")]
  nta_res[[as.character(y)]] <- nt

  ni <- data.table(svyby(~alloc, ~sex + age_grp + inc_tercile, pdes, svymean,
                         na.rm = TRUE))
  ni[, `:=`(year = y, method = "nta_utilization")]
  nta_inc[[as.character(y)]] <- ni

  # person-level allocation kept for regrouping into other age bins (fig 2)
  saveRDS(p[, .(hh_id, sexo, edad, sex, age_grp, factor, upm, est_dis,
                alloc, alloc_pc, inc_tercile)],
          file.path(DERIV, sprintf("enigh_person_alloc_%d.rds", y)))
}

reg_all <- rbindlist(reg_res)
nta_all <- rbindlist(nta_res)
fwrite(reg_all, file.path(OUTTAB, "tier3_regression_profiles.csv"))
fwrite(nta_all, file.path(OUTTAB, "tier3_nta_profiles.csv"))
fwrite(rbindlist(nta_inc), file.path(OUTTAB, "fig3_profile_by_income_tercile.csv"))

# fig 1 table: 2024, both methods side by side (quarterly pesos per person)
f1 <- rbind(
  reg_all[year == 2024, .(sex, age_grp, value = coef, se, method)],
  nta_all[year == 2024, .(sex, age_grp, value = alloc, se = se.alloc, method)])
fwrite(f1, file.path(OUTTAB, "fig1_age_sex_profile_2024.csv"))

# fig 11 table: NTA profiles across all four waves (constant 2024 pesos)
fwrite(nta_all[, .(year, sex, age_grp, alloc, se.alloc)],
       file.path(OUTTAB, "fig11_profile_stability.csv"))

# method agreement check (correlation and ratio by cell, 2024)
cmp <- merge(reg_all[year == 2024, .(sex, age_grp, reg = coef)],
             nta_all[year == 2024, .(sex, age_grp, nta = alloc)],
             by = c("sex", "age_grp"))
message(sprintf("2024 method correlation: %.3f", cmp[, cor(reg, nta)]))
print(cmp[order(sex, age_grp)])
fwrite(cmp, file.path(OUTTAB, "tier3_method_agreement_2024.csv"))
message("04_enigh_tier3 done")
