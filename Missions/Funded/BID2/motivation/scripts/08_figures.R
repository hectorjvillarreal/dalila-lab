# 08_figures.R — all motivation figures, 300 dpi .png + .pdf, English labels.
# Palette validated colorblind-safe (dataviz six-checks validator, light mode):
#   blue #2a78d6 · orange #eb6834 · aqua #1baf7a · yellow #eda100; neutral gray
#   #9a9992 for "ambiguous". Sequential tercile ramp: one blue hue, light->dark.
# Every figure carries a note (source, wave, deflator, tier/allocation caveat)
# and has a machine-readable table in output/tables (written by scripts 02-07).

source("scripts/00_common.R")
suppressPackageStartupMessages(library(ggplot2))

C_BLUE <- "#2a78d6"; C_ORANGE <- "#eb6834"; C_AQUA <- "#1baf7a"
C_YELLOW <- "#eda100"; C_GRAY <- "#9a9992"
SEXCOL <- c(female = C_ORANGE, male = C_BLUE)
TERCOL <- c(`1` = "#a8c9ee", `2` = "#5f9cdf", `3` = "#2a78d6")
WAVECOL <- c(`2018` = C_BLUE, `2020` = C_ORANGE, `2022` = C_AQUA, `2024` = C_YELLOW)
AGE_LAB <- c("0-4", "5-14", "15-29", "30-44", "45-59", "60-64", "65-74", "75-84", "85+")

th <- theme_minimal(base_size = 11) +
  theme(panel.grid.minor = element_blank(),
        panel.grid.major = element_line(color = "grey88", linewidth = 0.3),
        plot.caption = element_text(size = 7.5, color = "grey35", hjust = 0),
        plot.title = element_text(face = "bold", size = 12),
        plot.subtitle = element_text(size = 9.5, color = "grey25"),
        legend.position = "top", legend.title = element_blank(),
        strip.text = element_text(face = "bold"))

save_fig <- function(p, name, w = 8, h = 5) {
  ggsave(file.path(OUTFIG, paste0(name, ".png")), p, width = w, height = h,
         dpi = 300, bg = "white")
  ggsave(file.path(OUTFIG, paste0(name, ".pdf")), p, width = w, height = h,
         bg = "white")
  message("saved ", name)
}

NOTE_OOP <- "Out-of-pocket spending only; public in-kind provision (IMSS/ISSSTE/SSA services) is not included. Constant Aug-Nov 2024 pesos (general INPC)."

# ---- Figure 1: age-sex profile, both allocation methods (ENIGH 2024) ------
f1 <- fread(file.path(OUTTAB, "fig1_age_sex_profile_2024.csv"))
f1[, age_grp := factor(age_grp, AGE_LAB)]
f1[, method := fifelse(method == "regression", "Household regression",
                       "NTA-style (ENSANUT utilization weights)")]
p1 <- ggplot(f1, aes(age_grp, value, color = sex, linetype = method,
                     group = interaction(sex, method))) +
  geom_hline(yintercept = 0, color = "grey70", linewidth = 0.3) +
  geom_ribbon(aes(ymin = value - 1.96 * se, ymax = value + 1.96 * se,
                  fill = sex, group = interaction(sex, method)),
              alpha = 0.12, color = NA) +
  geom_line(linewidth = 0.8) + geom_point(size = 2) +
  scale_color_manual(values = SEXCOL) + scale_fill_manual(values = SEXCOL, guide = "none") +
  labs(title = "Out-of-pocket health spending rises steeply with age",
       subtitle = "Estimated individual quarterly OOP health spending by age and sex, Mexico 2024 (two independent allocation methods)",
       x = "Age group", y = "Pesos per quarter (Aug-Nov 2024 prices)",
       caption = paste("Source: ENIGH 2024 (INEGI); utilization weights from ENSANUT Continua 2024 (INSP). Tier 3: individual profiles are ESTIMATES",
                       "conditional on an allocation rule, not observed data; household regression coefficients can be negative (ages 5-14).",
                       "Shaded band: 95% CI, design-based (strata x PSU x weights).", NOTE_OOP, sep = "\n")) + th
save_fig(p1, "fig01_age_sex_profile")

# ---- Figure 2: ENIGH Tier 3 vs ENASEM observed, ages 50+ ------------------
pa <- readRDS(file.path(DERIV, "enigh_person_alloc_2024.rds"))
brk50 <- c(50, 55, 60, 65, 70, 75, 80, 85, Inf)
lab50 <- c("50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80-84", "85+")
pa <- pa[edad >= 50]
pa[, age50 := cut(edad, brk50, right = FALSE, labels = lab50)]
pdes <- svydesign(ids = ~upm, strata = ~est_dis, weights = ~factor, data = pa,
                  nest = TRUE)
e50 <- data.table(svyby(~alloc, ~sex + age50, pdes, svymean))
e50[, src := "ENIGH 2024, Tier 3 estimate (NTA allocation)"]
setnames(e50, c("alloc", "se"), c("value", "se_v"))
en <- fread(file.path(OUTTAB, "fig2_enasem_observed_profile.csv"))
en <- en[wave == 2024, .(sex, age50 = age_grp, value = oop_q24, se_v = se,
                         src = "ENASEM 2024, observed individual OOP")]
f2 <- rbind(e50[, .(sex, age50, value, se_v, src)], en)
f2[, age50 := factor(age50, lab50)]
p2 <- ggplot(f2, aes(age50, value, color = src, group = src)) +
  geom_ribbon(aes(ymin = value - 1.96 * se_v, ymax = value + 1.96 * se_v,
                  fill = src), alpha = 0.12, color = NA) +
  geom_line(linewidth = 0.8) + geom_point(size = 2) +
  facet_wrap(~sex) +
  scale_color_manual(values = c(C_BLUE, C_ORANGE)) +
  scale_fill_manual(values = c(C_BLUE, C_ORANGE), guide = "none") +
  labs(title = "Validation: the ENIGH-estimated profile against ENASEM's observed profile",
       subtitle = "Quarterly OOP health spending, ages 50+, by sex, 2024",
       x = "Age group", y = "Pesos per quarter (Aug-Nov 2024 prices)",
       caption = paste("Sources: ENIGH 2024 Tier 3 (NTA-style allocation, ENSANUT utilization weights) vs ENASEM 2024 observed individual",
                       "spending (annual amounts / 4). ENASEM asks hospitalization, visits, procedures and a normal-month medication amount x 12;",
                       "ENIGH records all household health rubros. Recall design and item coverage differ; levels are not expected to coincide exactly.",
                       NOTE_OOP, sep = "\n")) + th
save_fig(p2, "fig02_validation_enigh_vs_enasem", w = 9)

# ---- Figure 3: profile by income tercile (ENIGH 2024, NTA) ----------------
f3 <- fread(file.path(OUTTAB, "fig3_profile_by_income_tercile.csv"))
f3 <- f3[year == 2024]
f3[, age_grp := factor(age_grp, AGE_LAB)]
p3 <- ggplot(f3, aes(age_grp, alloc, color = factor(inc_tercile),
                     group = inc_tercile)) +
  geom_ribbon(aes(ymin = alloc - 1.96 * se, ymax = alloc + 1.96 * se,
                  fill = factor(inc_tercile)), alpha = 0.12, color = NA) +
  geom_line(linewidth = 0.8) + geom_point(size = 2) + facet_wrap(~sex) +
  scale_color_manual(values = TERCOL, labels = paste("Income tercile", 1:3)) +
  scale_fill_manual(values = TERCOL, guide = "none") +
  labs(title = "The age gradient of health spending is far steeper for richer households",
       subtitle = "Estimated individual quarterly OOP health spending by age, sex and household income tercile, 2024",
       x = "Age group", y = "Pesos per quarter (Aug-Nov 2024 prices)",
       caption = paste("Source: ENIGH 2024, Tier 3 NTA-style allocation (ENSANUT 2024 utilization weights); income terciles of quarterly household",
                       "current income (weighted households). Tier 3 values are estimates conditional on the allocation rule.", NOTE_OOP, sep = "\n")) + th
save_fig(p3, "fig03_profile_by_income", w = 9)

# ---- Figure 4: budget share by decile -------------------------------------
f4 <- fread(file.path(OUTTAB, "fig4_budget_share_by_decile.csv"))
f4 <- melt(f4[year == 2024], id.vars = "decile",
           measure.vars = c("share_uncond", "share_condpos"))
f4[, variable := fifelse(variable == "share_uncond", "All households",
                         "Households with positive health spending")]
p4 <- ggplot(f4, aes(factor(decile), value, color = variable, group = variable)) +
  geom_line(linewidth = 0.8) + geom_point(size = 2.2) +
  scale_y_continuous(labels = scales::percent_format(accuracy = 0.1)) +
  scale_color_manual(values = c(C_BLUE, C_ORANGE)) +
  labs(title = "Health takes a similar budget share across the income distribution -\nbecause poor households often spend nothing",
       subtitle = "Mean health share of monetary spending by income decile, 2024",
       x = "Household income decile (1 = poorest)", y = "Health share of monetary expenditure",
       caption = paste("Source: ENIGH 2024 (INEGI), household level (Tier 1, no allocation assumption). Deciles of quarterly household current",
                       "income, weighted. Design-based estimates.", NOTE_OOP, sep = "\n")) + th
save_fig(p4, "fig04_budget_share_by_decile")

# ---- Figure 5: zero health spending by decile x 65+ -----------------------
f5 <- fread(file.path(OUTTAB, "fig5_zero_spending_by_decile_65plus.csv"))
f5 <- f5[year == 2024]
f5[, grp := fifelse(has65, "Household has a member 65+", "No member 65+")]
p5 <- ggplot(f5, aes(factor(decile), p_zero, color = grp, group = grp)) +
  geom_ribbon(aes(ymin = p_zero - 1.96 * p_zero_se, ymax = p_zero + 1.96 * p_zero_se,
                  fill = grp), alpha = 0.12, color = NA) +
  geom_line(linewidth = 0.8) + geom_point(size = 2.2) +
  scale_y_continuous(labels = scales::percent) +
  scale_color_manual(values = c(C_ORANGE, C_BLUE)) +
  scale_fill_manual(values = c(C_ORANGE, C_BLUE), guide = "none") +
  labs(title = "Zero health spending is most common in poor households -\neven those with older members",
       subtitle = "Share of households reporting zero OOP health spending in the quarter, by income decile, 2024",
       x = "Household income decile (1 = poorest)", y = "Share with zero health spending",
       caption = paste("Source: ENIGH 2024 (INEGI), Tier 1. Zero OOP spending among households containing a member aged 65+ is consistent with",
                       "unmet need rather than good health (see the ENSANUT forgone-care evidence, Fig. 6).", NOTE_OOP, sep = "\n")) + th
save_fig(p5, "fig05_zero_spending")

# ---- Figure 6: forgone care and cost-forgone care (ENSANUT) ---------------
f6 <- fread(file.path(OUTTAB, "fig6_forgone_care.csv"))
ses <- f6[grepl("^estrato|^nse_tercile", grp)]
ses[, xlab := fcase(grp == "estrato1", "Stratum 1\n(lowest)", grp == "estrato2", "Stratum 2",
                    grp == "estrato3", "Stratum 3", grp == "estrato4", "Stratum 4\n(highest)",
                    grp == "nse_tercile1", "Tercile 1\n(lowest)", grp == "nse_tercile2", "Tercile 2",
                    grp == "nse_tercile3", "Tercile 3\n(highest)")]
ses_l <- melt(ses, id.vars = c("xlab", "wave"),
              measure.vars = c("forgoneTRUE", "cost_forgoneTRUE"))
ses_l[, variable := fifelse(variable == "forgoneTRUE",
                            "Forgone care (any reason)", "Forgone care citing cost")]
p6 <- ggplot(ses_l, aes(xlab, value, fill = variable)) +
  geom_col(position = position_dodge(width = 0.7), width = 0.62) +
  facet_wrap(~wave, scales = "free_x",
             labeller = as_labeller(c(`2018` = "ENSANUT 2018-19 (socioeconomic stratum)",
                                      `2024` = "ENSANUT 2024 (wellbeing tercile)"))) +
  scale_y_continuous(labels = scales::percent) +
  scale_fill_manual(values = c(C_BLUE, C_ORANGE)) +
  labs(title = "Unmet need is concentrated at the bottom of the distribution",
       subtitle = "Among people with a health need: share who did not receive care, and share citing cost, by SES",
       x = NULL, y = "Share of those with a health need",
       caption = paste("Source: ENSANUT 2018-19 (need in last month, roster) and ENSANUT Continua 2024 (need in last 3 months); INSP. Design-based",
                       "estimates with module weights. Cost = 'es caro' / 'no tenia dinero' / told to pay (2018 codes P4_9_12-14; 2024 codes H0405A-C=4,",
                       "H0407A-C=8,9). Recall windows and need concepts differ across waves; levels are not directly comparable.", sep = "\n")) + th
save_fig(p6, "fig06_forgone_care", w = 9)

# insurance panel
ins <- f6[!grepl("^estrato|^nse_tercile|male$|^female", grp)]
ins_l <- melt(ins, id.vars = c("grp", "wave"),
              measure.vars = c("forgoneTRUE", "cost_forgoneTRUE"))
ins_l[, variable := fifelse(variable == "forgoneTRUE",
                            "Forgone care (any reason)", "Forgone care citing cost")]
p6b <- ggplot(ins_l, aes(reorder(grp, value), value, fill = variable)) +
  geom_col(position = position_dodge(width = 0.7), width = 0.62) +
  coord_flip() + facet_wrap(~wave) +
  scale_y_continuous(labels = scales::percent) +
  scale_fill_manual(values = c(C_BLUE, C_ORANGE)) +
  labs(title = "The uninsured forgo care most - and cite cost most",
       subtitle = "Among people with a health need, by insurance affiliation",
       x = NULL, y = "Share of those with a health need",
       caption = "Source: ENSANUT 2018-19 and Continua 2024 (INSP), design-based. Seguro Popular ended 2019; IMSS-Bienestar is the 2024 successor scheme.") + th
save_fig(p6b, "fig06b_forgone_by_insurance", w = 9)

# ---- Figure 7: curative / preventive / ambiguous composition --------------
f7 <- fread(file.path(OUTTAB, "fig7_composition_by_decile.csv"))
f7[, class := factor(class, c("preventive", "ambiguous", "curative"))]
p7 <- ggplot(f7[year %in% c(2018, 2024)],
             aes(factor(decile), share, fill = class)) +
  geom_col(width = 0.8, color = "white", linewidth = 0.4) +
  facet_wrap(~year) +
  scale_y_continuous(labels = scales::percent) +
  scale_fill_manual(values = c(preventive = C_AQUA, ambiguous = C_GRAY,
                               curative = C_BLUE),
                    labels = c("Preventive", "Ambiguous", "Curative")) +
  labs(title = "Observed OOP health spending is dominated by curative items in every decile",
       subtitle = "Composition of household OOP health spending by income decile (auditable rubro classification)",
       x = "Household income decile (1 = poorest)", y = "Share of health spending",
       caption = paste("Source: ENIGH 2018 (J-rubros) and 2024 (COICOP rubros), classification in output/tables/curative_preventive_classification.csv.",
                       "Ambiguous (OTC medicines, dental, optical, chronic maintenance, diagnostics, insurance premiums) is kept as its own category;",
                       "assigning it wholly to curative or wholly to preventive brackets the preventive share between ~2% and ~46% (see sensitivity table).",
                       "2024 rubros do not record prescription status, which shifts items from ambiguous to curative relative to 2018.", sep = "\n")) + th
save_fig(p7, "fig07_composition", w = 9)

# ---- Figure 8: catastrophic incidence by decile ---------------------------
f8 <- fread(file.path(OUTTAB, "fig8_catastrophic_by_decile.csv"))
f8l <- melt(f8[year == 2024], id.vars = "decile",
            measure.vars = c("cat40ctp", "cat25tot"))
f8l[, variable := fifelse(variable == "cat40ctp",
                          "OOP > 40% of capacity to pay (WHO)",
                          "OOP > 25% of total expenditure")]
p8 <- ggplot(f8l, aes(factor(decile), value, color = variable, group = variable)) +
  geom_line(linewidth = 0.8) + geom_point(size = 2.2) +
  scale_y_continuous(labels = scales::percent_format(accuracy = 0.5)) +
  scale_color_manual(values = c(C_ORANGE, C_BLUE)) +
  labs(title = "Catastrophic health spending falls hardest on poor households",
       subtitle = "Incidence of catastrophic OOP health spending by income decile, 2024",
       x = "Household income decile (1 = poorest)", y = "Share of households",
       caption = paste("Source: ENIGH 2024, Tier 1. WHO capacity to pay approximated as monetary expenditure minus food expenditure.",
                       "Sensitivity threshold: 25% of total monetary expenditure.", NOTE_OOP, sep = "\n")) + th
save_fig(p8, "fig08_catastrophic")

# ---- Figure 9: distribution of positive spending by decile ----------------
f9 <- fread(file.path(OUTTAB, "fig9_positive_spending_distribution.csv"))
f9 <- f9[year == 2024]
p9 <- ggplot(f9, aes(factor(decile))) +
  geom_ribbon(aes(ymin = p10, ymax = p90, group = 1), fill = C_BLUE, alpha = 0.15) +
  geom_ribbon(aes(ymin = p25, ymax = p75, group = 1), fill = C_BLUE, alpha = 0.30) +
  geom_line(aes(y = p50, group = 1), color = C_BLUE, linewidth = 1) +
  geom_line(aes(y = p95, group = 1), color = C_ORANGE, linewidth = 0.7,
            linetype = "dashed") +
  annotate("text", x = 9.6, y = f9[decile == 10, p95] * 1.1, label = "p95",
           color = C_ORANGE, size = 3.2) +
  annotate("text", x = 9.6, y = f9[decile == 10, p50] * 1.15, label = "median",
           color = C_BLUE, size = 3.2) +
  scale_y_log10(labels = scales::comma) +
  labs(title = "The right tail of health spending is an order of magnitude above the median",
       subtitle = "Distribution of positive quarterly OOP health spending within each income decile, 2024 (log scale)",
       x = "Household income decile (1 = poorest)", y = "Pesos per quarter (log scale)",
       caption = paste("Source: ENIGH 2024, Tier 1, households with positive health spending. Bands: p10-p90 (light), p25-p75 (dark), median line,",
                       "p95 dashed. The heavy right tail is the shock-response object the model formalizes.", NOTE_OOP, sep = "\n")) + th
save_fig(p9, "fig09_spending_distribution")

# ---- Figure 10: ENASEM dynamics -------------------------------------------
r1 <- fread(file.path(OUTTAB, "fig10_spending_response_by_wealth.csv"))
r2 <- fread(file.path(OUTTAB, "fig10_subsequent_outcomes_by_wealth.csv"))
r1[, panel := "Annual OOP spending in 2021 (pesos)"]
r1[, `:=`(value = oop21_r, se_v = se.oop21_r)]
r2[, panel := "Died between 2021 and 2024 (share)"]
r2[, `:=`(value = died_2124TRUE, se_v = se.died_2124TRUE)]
f10 <- rbind(r1[, .(decline, wtercile, panel, value, se_v)],
             r2[, .(decline, wtercile, panel, value, se_v)])
f10[, grp := fifelse(decline, "Frailty worsened 2018-21 (>= 0.10)", "No comparable decline")]
p10 <- ggplot(f10, aes(factor(wtercile), value, fill = grp)) +
  geom_col(position = position_dodge(width = 0.7), width = 0.62) +
  geom_errorbar(aes(ymin = value - 1.96 * se_v, ymax = value + 1.96 * se_v),
                position = position_dodge(width = 0.7), width = 0.18,
                color = "grey30", linewidth = 0.4) +
  facet_wrap(~panel, scales = "free_y") +
  scale_fill_manual(values = c(C_ORANGE, C_BLUE)) +
  scale_x_discrete(labels = paste("Wealth tercile", 1:3)) +
  labs(title = "After a health decline, richer households spend more - and die less",
       subtitle = "ENASEM panel 2018-2021-2024, ages 50+: spending response to a frailty increase, and subsequent mortality, by baseline wealth",
       x = NULL, y = NULL,
       caption = paste("Source: ENASEM 2018/2021/2024 (INEGI open data). DESCRIPTIVE conditional patterns, not causal estimates: wealth correlates with",
                       "insurance, education, prior health and access, none of which are controlled by a panel difference. Frailty: reconstructed 21-item",
                       "deficit-accumulation index (Searle convention) - PROVISIONAL pending confirmation by the coauthor whose index it reconstructs.",
                       "Spending in Aug-Nov 2024 pesos (general INPC). Wealth: household assets net of debts, 2018.", sep = "\n")) + th
save_fig(p10, "fig10_enasem_dynamics", w = 10)

# ---- Figure 11: stability across ENIGH waves ------------------------------
f11 <- fread(file.path(OUTTAB, "fig11_profile_stability.csv"))
f11[, age_grp := factor(age_grp, AGE_LAB)]
p11 <- ggplot(f11, aes(age_grp, alloc, color = factor(year), group = year)) +
  geom_line(linewidth = 0.8) + geom_point(size = 1.8) + facet_wrap(~sex) +
  scale_color_manual(values = WAVECOL) +
  labs(title = "The age profile of OOP health spending is stable across survey waves",
       subtitle = "Estimated individual quarterly OOP health spending (NTA-style allocation), constant Aug-Nov 2024 pesos",
       x = "Age group", y = "Pesos per quarter (Aug-Nov 2024 prices)",
       caption = paste("Source: ENIGH 2018-2024, Tier 3 NTA-style allocation (ENSANUT 2018 utilization weights for ENIGH 2018/2020; ENSANUT 2024",
                       "weights for 2022/2024). 2020 is pandemic-affected: fieldwork Aug-Nov 2020, with suppressed utilization and elevated",
                       "COVID-related spending; treat its level with caution.", NOTE_OOP, sep = "\n")) + th
save_fig(p11, "fig11_wave_stability", w = 9)

message("08_figures done")
