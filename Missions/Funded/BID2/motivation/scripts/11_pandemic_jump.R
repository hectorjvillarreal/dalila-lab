# 11_pandemic_jump.R — decile split of the 2018->2020 real OOP surge.
# Who financed the pandemic jump in out-of-pocket health spending?
# All values constant Aug-Nov 2024 pesos (general INPC), design-based.
# Placebo: food spending (alimentos), a category with no comparable
# pandemic-provision shock, to separate behavior from instrument change.
# Outputs: output/tables/pandemic_jump_by_decile.csv, fig12 png/pdf.

source("scripts/00_common.R")
suppressPackageStartupMessages(library(ggplot2))

res <- list()
for (y in c(2018, 2020)) {
  con <- readRDS(file.path(DERIV, sprintf("enigh_hh_%d.rds", y)))
  con[, pos := salud > 0]
  des <- enigh_design(con)
  m <- data.table(svyby(~salud + alimentos + gasto_mon, ~decile, des, svymean))
  z <- data.table(svyby(~I(!pos), ~decile, des, svymean))
  cp <- data.table(svyby(~salud, ~decile, subset(des, pos), svymean))
  tot <- con[, .(salud_total = sum(salud * factor)), by = decile]
  out <- Reduce(function(a, b) merge(a, b, by = "decile"), list(
    m[, .(decile, salud, salud_se = se.salud, alimentos, gasto_mon)],
    z[, .(decile, p_zero = `I(!pos)TRUE`, p_zero_se = `se.I(!pos)TRUE`)],
    cp[, .(decile, salud_condpos = salud, salud_condpos_se = se)],
    tot))
  out[, year := y]
  res[[as.character(y)]] <- out
}
w <- merge(res[["2018"]], res[["2020"]], by = "decile", suffixes = c("_18", "_20"))

w[, `:=`(
  d_salud_pct     = salud_20 / salud_18 - 1,
  d_alim_pct      = alimentos_20 / alimentos_18 - 1,
  d_gasto_pct     = gasto_mon_20 / gasto_mon_18 - 1,
  d_condpos_pct   = salud_condpos_20 / salud_condpos_18 - 1,
  d_pzero_pp      = p_zero_20 - p_zero_18,
  jump_contrib    = (salud_total_20 - salud_total_18) /
                    (sum(salud_total_20) - sum(salud_total_18)))]

print(w[, .(decile,
            salud_18 = round(salud_18), salud_20 = round(salud_20),
            d_salud = round(d_salud_pct, 3), d_alim = round(d_alim_pct, 3),
            d_condpos = round(d_condpos_pct, 3),
            d_pzero_pp = round(d_pzero_pp, 3),
            contrib = round(jump_contrib, 3))])
fwrite(w, file.path(OUTTAB, "pandemic_jump_by_decile.csv"))

# figure: % change in mean household spending by decile, health vs food placebo
fl <- melt(w[, .(decile, Health = d_salud_pct, `Food (placebo)` = d_alim_pct)],
           id.vars = "decile")
p <- ggplot(fl, aes(factor(decile), value, fill = variable)) +
  geom_col(position = position_dodge(width = 0.7), width = 0.62) +
  geom_hline(yintercept = 0, color = "grey40", linewidth = 0.3) +
  scale_y_continuous(labels = scales::percent) +
  scale_fill_manual(values = c(Health = "#2a78d6", `Food (placebo)` = "#9a9992")) +
  labs(title = "The 2020 OOP health surge, by income decile",
       subtitle = "Change in mean real household spending, ENIGH 2018 to 2020, health vs food placebo",
       x = "Household income decile (1 = poorest)",
       y = "Change 2018-2020 (constant Aug-Nov 2024 pesos)",
       caption = paste("Source: ENIGH 2018, 2020 (INEGI), Tier 1 household level, design-based means by decile of quarterly current income.",
                       "Food = 'alimentos' concentrado aggregate, a category without a comparable pandemic provision shock.",
                       "Constant Aug-Nov 2024 pesos (general INPC). 2020 fieldwork Aug-Nov 2020.", sep = "\n")) +
  theme_minimal(base_size = 11) +
  theme(panel.grid.minor = element_blank(),
        panel.grid.major = element_line(color = "grey88", linewidth = 0.3),
        plot.caption = element_text(size = 7.5, color = "grey35", hjust = 0),
        plot.title = element_text(face = "bold", size = 12),
        plot.subtitle = element_text(size = 9.5, color = "grey25"),
        legend.position = "top", legend.title = element_blank())
ggsave(file.path(OUTFIG, "fig12_pandemic_jump.png"), p, width = 8, height = 5,
       dpi = 300, bg = "white")
ggsave(file.path(OUTFIG, "fig12_pandemic_jump.pdf"), p, width = 8, height = 5,
       bg = "white")
message("11_pandemic_jump done")
