# 00_common.R — shared paths, deflators, and helpers
# BID2 motivation: Mexican health expenditure by sex, income, and age
# Run everything from the motivation/ folder: Rscript scripts/01_...R

suppressPackageStartupMessages({
  library(data.table)
  library(survey)
})

ROOT   <- normalizePath(".")
DATA   <- file.path(ROOT, "data")
DERIV  <- file.path(DATA, "derived")
OUTFIG <- file.path(ROOT, "output", "figures")
OUTTAB <- file.path(ROOT, "output", "tables")
dir.create(DERIV, showWarnings = FALSE, recursive = TRUE)

ENIGH_YEARS <- c(2018, 2020, 2022, 2024)

# Lonely-PSU handling: certainty-adjust rather than fail (standard for these designs)
options(survey.lonely.psu = "adjust")

# ---- INPC deflator -------------------------------------------------------
# General INPC (base 2a quincena julio 2018), INEGI open data, monthly.
# The open-data indicator file carries the general index and core subindices
# only — no health subindex — so the GENERAL index is used (stated in notes).
# ENIGH money variables are quarterly amounts referenced to Aug–Nov of the
# survey year; each wave is deflated by the ratio of the Aug–Nov 2024 mean
# index to the wave's own Aug–Nov mean. Base: Aug–Nov 2024 pesos.
inpc_deflators <- function(years = ENIGH_YEARS) {
  f <- file.path(DATA, "inpc", "2018a", "conjunto_de_datos",
                 "conjunto_de_datos_inpc_mensual.csv")
  inpc <- fread(f, encoding = "UTF-8")
  inpc <- inpc[grepl("Precios al Consumidor (INPC)", CONCEPTO, fixed = TRUE) &
               COBERTURA == "Nacional"]
  inpc[, fecha := as.IDate(FECHA, format = "%d/%m/%Y")]
  inpc[, `:=`(yr = year(fecha), mo = month(fecha))]
  ref <- inpc[mo %in% 8:11, .(idx = mean(VALOR)), by = yr]
  base <- ref[yr == 2024, idx]
  defl <- ref[yr %in% years, .(yr, deflator = base / idx)]
  stopifnot(nrow(defl) == length(years))
  defl
}

# ---- ENIGH design --------------------------------------------------------
enigh_design <- function(dt) {
  svydesign(ids = ~upm, strata = ~est_dis, weights = ~factor,
            data = dt, nest = TRUE)
}

# Weighted decile of households by quarterly current income (ing_cor),
# INEGI tabulados convention: deciles hold equal weighted household counts.
add_income_decile <- function(dt) {
  setorder(dt, ing_cor)
  cw <- cumsum(dt$factor) / sum(dt$factor)
  dt[, decile := pmin(10L, findInterval(cw, seq(0.1, 0.9, 0.1)) + 1L)]
  dt
}
