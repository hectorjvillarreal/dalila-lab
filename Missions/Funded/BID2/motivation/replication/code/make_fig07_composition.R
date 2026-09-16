# make_fig07_composition.R — regenerates fig07_composition.pdf/.png from the
# shipped decile-level aggregate. Extracted verbatim from the build's
# scripts/08_figures.R (figure 7 block plus the palette, theme, and save
# helper it uses); no other figure code is included. Reads only ../data,
# writes only ../output, relative to this script's own location. No network.

suppressPackageStartupMessages({
  library(data.table)
  library(ggplot2)
})

a <- commandArgs(trailingOnly = FALSE)
here <- dirname(normalizePath(sub("^--file=", "", grep("^--file=", a, value = TRUE)[1])))
DATA <- file.path(here, "..", "data")
OUTFIG <- file.path(here, "..", "output")
dir.create(OUTFIG, showWarnings = FALSE, recursive = TRUE)

C_BLUE <- "#2a78d6"; C_AQUA <- "#1baf7a"; C_GRAY <- "#9a9992"

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

f7 <- fread(file.path(DATA, "fig7_composition_by_decile.csv"))
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
