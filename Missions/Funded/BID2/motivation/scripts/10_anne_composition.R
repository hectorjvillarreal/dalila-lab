# 10_anne_composition.R — demographic composition experiment for Anne's
# briefing: hold the 2024 estimated age-sex OOP profile (Tier 3, NTA
# allocation) fixed and reweight from the observed ENIGH 2024 adult age
# structure to the 2050 stationary structure implied by Anne's primitives
# (demographics_2050.jl: psi_male/female Brass-logit 2050, n_p_2050).
# Pure composition effect — no behavior, no prices, no income growth.
# Output: output/tables/anne_composition_2050.csv

source("scripts/00_common.R")

# Anne's 2050 primitives (transcribed from demographics_2050.jl, J=17 bands
# 20-24 ... 100+; verified against the file on 2026-08-08)
psi_m <- c(1, 1, 1, 1, 1, 1, 0.9925, 0.9867, 0.9783, 0.9665, 0.9499, 0.9239,
           0.8678, 0.7521, 0.5652, 0.3303, 0.1535)
psi_f <- c(1, 1, 1, 1, 1, 1, 0.9974, 0.9954, 0.9924, 0.9880, 0.9814, 0.9704,
           0.9440, 0.8775, 0.7245, 0.4377, 0.1776)
n5 <- (1 - 0.004)^5 - 1

BANDS <- c(paste(seq(20, 95, 5), seq(24, 99, 5), sep = "-"), "100+")

# stationary band populations: N_1 = 1 at age 20; N_{j+1} = N_j * psi_j / (1+n5)
stationary <- function(psi) {
  N <- numeric(17); N[1] <- 1
  for (j in 2:17) N[j] <- N[j - 1] * psi[j - 1] / (1 + n5)
  N
}
s2050 <- data.table(band = rep(BANDS, 2),
                    sex = rep(c("male", "female"), each = 17),
                    pop = c(stationary(psi_m), stationary(psi_f)))  # 50/50 entry
s2050[, share := pop / sum(pop)]

# observed 2024 adult structure and profile (person-level Tier 3 allocation)
pa <- readRDS(file.path(DERIV, "enigh_person_alloc_2024.rds"))
pa <- pa[edad >= 20]
pa[, band := BANDS[pmin(17L, (edad - 20L) %/% 5L + 1L)]]
obs <- pa[, .(pop = sum(factor), m = weighted.mean(alloc, factor)),
          by = .(band, sex)]
obs[, share := pop / sum(pop)]

cmp <- merge(obs[, .(band, sex, m, share_2024 = share)],
             s2050[, .(band, sex, share_2050 = share)], by = c("band", "sex"))
agg24 <- cmp[, sum(m * share_2024)]
agg50 <- cmp[, sum(m * share_2050)]
old24 <- cmp[band %in% BANDS[10:17], sum(m * share_2024)] / agg24
old50 <- cmp[band %in% BANDS[10:17], sum(m * share_2050)] / agg50
sh65_24 <- cmp[band %in% BANDS[10:17], sum(share_2024)]
sh65_50 <- cmp[band %in% BANDS[10:17], sum(share_2050)]

out <- data.table(
  quantity = c("aggregate OOP per adult (quarterly, Aug-Nov 2024 pesos)",
               "share of adults 65+", "share of OOP spent by 65+"),
  structure_2024 = round(c(agg24, sh65_24, old24), 4),
  structure_2050 = round(c(agg50, sh65_50, old50), 4))
out[, lift := round(structure_2050 / structure_2024, 3)]
print(out)
fwrite(out, file.path(OUTTAB, "anne_composition_2050.csv"))
fwrite(cmp[order(sex, band)], file.path(OUTTAB, "anne_composition_detail.csv"))
message("10_anne_composition done")
