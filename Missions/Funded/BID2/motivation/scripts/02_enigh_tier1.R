# 02_enigh_tier1.R — Tier 1 (household-level, no allocation assumption).
# Produces the plotted-value tables for: budget share by decile (fig 4),
# zero health spending by decile x presence of 65+ (fig 5), catastrophic
# incidence by decile (fig 8), distribution of positive spending (fig 9).
# All estimates design-based: est_dis strata, upm PSUs, factor weights.

source("scripts/00_common.R")

res_share <- list(); res_zero <- list(); res_cat <- list(); res_dist <- list()

for (y in ENIGH_YEARS) {
  message("== Tier 1, ", y)
  con <- readRDS(file.path(DERIV, sprintf("enigh_hh_%d.rds", y)))

  con[, share_gasto := fifelse(gasto_mon > 0, salud / gasto_mon, NA_real_)]
  con[, pos := salud > 0]
  con[, has65 := p65mas > 0]
  # WHO capacity to pay ~ non-subsistence spending: gasto_mon - alimentos
  con[, ctp := pmax(gasto_mon - alimentos, 0)]
  con[, cat40ctp := pos & ctp > 0 & salud > 0.40 * ctp]
  con[, cat25tot := pos & gasto_mon > 0 & salud > 0.25 * gasto_mon]

  des <- enigh_design(con)

  s1 <- svyby(~share_gasto, ~decile, des, svymean, na.rm = TRUE)
  s2 <- svyby(~share_gasto, ~decile, subset(des, pos), svymean, na.rm = TRUE)
  s3 <- svyby(~salud, ~decile, des, svymean)
  sh <- data.table(decile = s1$decile,
                   share_uncond = s1$share_gasto, share_uncond_se = s1$se,
                   share_condpos = s2$share_gasto, share_condpos_se = s2$se,
                   mean_salud = s3$salud, mean_salud_se = s3$se, year = y)
  res_share[[as.character(y)]] <- sh

  z <- svyby(~I(!pos), ~decile + has65, des, svymean)
  zd <- data.table(z)[, .(decile, has65, p_zero = `I(!pos)TRUE`,
                          p_zero_se = `se.I(!pos)TRUE`, year = y)]
  res_zero[[as.character(y)]] <- zd

  cc <- svyby(~cat40ctp + cat25tot, ~decile, des, svymean)
  cd <- data.table(cc)[, .(decile, cat40ctp = cat40ctpTRUE, cat40ctp_se = se.cat40ctpTRUE,
                           cat25tot = cat25totTRUE, cat25tot_se = se.cat25totTRUE, year = y)]
  res_cat[[as.character(y)]] <- cd

  qs <- c(.10, .25, .50, .75, .90, .95, .99)
  qb <- svyby(~salud, ~decile, subset(des, pos), svyquantile,
              quantiles = qs, ci = FALSE, keep.var = FALSE)
  qd <- data.table(qb)
  setnames(qd, c("decile", paste0("p", qs * 100)))
  qd[, year := y]
  res_dist[[as.character(y)]] <- qd
}

fwrite(rbindlist(res_share), file.path(OUTTAB, "fig4_budget_share_by_decile.csv"))
fwrite(rbindlist(res_zero),  file.path(OUTTAB, "fig5_zero_spending_by_decile_65plus.csv"))
fwrite(rbindlist(res_cat),   file.path(OUTTAB, "fig8_catastrophic_by_decile.csv"))
fwrite(rbindlist(res_dist),  file.path(OUTTAB, "fig9_positive_spending_distribution.csv"))
message("02_enigh_tier1 done")
