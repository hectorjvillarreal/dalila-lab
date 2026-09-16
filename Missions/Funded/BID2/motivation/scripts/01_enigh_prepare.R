# 01_enigh_prepare.R — read ENIGH waves, select health claves from shipped
# catalogs, build household-level and person-count files for Tasks A, B, C.
# Outputs: data/derived/enigh_hh_<year>.rds, enigh_health_long_<year>.rds,
#          output/tables/enigh_health_claves_<year>.csv (audit list)
# Health claves are taken from each wave's shipped gastos.csv catalog — never
# from memory: 2018/2020/2022 use J-codes; 2024 uses COICOP 06-codes.

source("scripts/00_common.R")

read_enigh_csv <- function(path, select = NULL) {
  fread(path, select = select, colClasses = list(character = c("folioviv", "foliohog")),
        encoding = "UTF-8")
}

gastos_catalog <- function(year) {
  d <- Sys.glob(file.path(DATA, "enigh", year, "bundle", "*gastoshogar*",
                          "catalogos", "gastos.csv"))[1]
  raw <- readLines(d, warn = FALSE, encoding = "latin1")
  # 2018 ships latin1; 2020+ ship UTF-8(-BOM). Detect by validity.
  if (all(validUTF8(raw))) raw <- readLines(d, warn = FALSE, encoding = "UTF-8")
  cat_dt <- fread(text = raw)
  setnames(cat_dt, c("clave", "descripcion"))
  cat_dt
}

# 2024 note: COICOP moved health-insurance premiums out of division 06 into
# 1212xx (seguro de gastos médicos / seguro médico voluntario IMSS); the old
# J-set (2018-2022) includes premiums (J071, J072), and the 2024 concentrado
# 'salud' aggregate includes 1212xx (verified: 06+1212 reproduces it at 0.998,
# 06 alone only 0.892). Include 1212xx for cross-wave comparability.
health_claves <- function(year, cat_dt) {
  if (year <= 2022) cat_dt[grepl("^J[0-9]{3}$", clave)]
  else              cat_dt[grepl("^06|^1212", clave)]
}

defl <- inpc_deflators()

all_claves <- list()
for (y in ENIGH_YEARS) {
  message("== ENIGH ", y)
  dfl <- defl[yr == y, deflator]

  cat_dt <- gastos_catalog(y)
  hc <- health_claves(y, cat_dt)
  hc[, year := y]
  all_claves[[as.character(y)]] <- hc
  fwrite(hc, file.path(OUTTAB, sprintf("enigh_health_claves_%d.csv", y)))

  # -- household concentrado --
  con <- read_enigh_csv(file.path(DATA, "enigh", y, "concentradohogar.csv"),
    select = c("folioviv", "foliohog", "est_dis", "upm", "factor", "tot_integ",
               "hombres", "mujeres", "menores", "p12_64", "p65mas",
               "ing_cor", "gasto_mon", "alimentos", "salud"))
  con[, hh_id := paste0(folioviv, "_", foliohog)]
  con <- add_income_decile(con)

  # -- health expenditure detail (gastoshogar, health claves only) --
  gh <- read_enigh_csv(file.path(DATA, "enigh", y, "gastoshogar.csv"),
    select = c("folioviv", "foliohog", "clave", "tipo_gasto", "gasto_tri"))
  gh <- gh[clave %in% hc$clave]
  # G1 = monetary expenditure; keep monetary out-of-pocket only (exclude
  # in-kind imputations: autoconsumo, pago en especie, regalos = other Gs)
  gh <- gh[tipo_gasto == "G1"]
  gh[, gasto_tri := as.numeric(gasto_tri)]
  gh[, hh_id := paste0(folioviv, "_", foliohog)]

  hh_health <- gh[, .(salud_detalle_tri = sum(gasto_tri, na.rm = TRUE)), by = hh_id]
  con <- merge(con, hh_health, by = "hh_id", all.x = TRUE)
  con[is.na(salud_detalle_tri), salud_detalle_tri := 0]

  # -- deflate money to Aug–Nov 2024 pesos (general INPC) --
  for (v in c("ing_cor", "gasto_mon", "alimentos", "salud", "salud_detalle_tri"))
    con[, (v) := get(v) * dfl]
  gh[, gasto_tri_r := gasto_tri * dfl]

  # -- person counts by age-sex cell (poblacion) for Tier 3 allocation --
  pob <- read_enigh_csv(file.path(DATA, "enigh", y, "poblacion.csv"),
    select = c("folioviv", "foliohog", "numren", "sexo", "edad"))
  pob[, hh_id := paste0(folioviv, "_", foliohog)]
  brk <- c(0, 5, 15, 30, 45, 60, 65, 75, 85, Inf)
  lab <- c("0-4", "5-14", "15-29", "30-44", "45-59", "60-64", "65-74", "75-84", "85+")
  pob[, age_grp := cut(edad, brk, right = FALSE, labels = lab)]
  pob[, sex := fifelse(sexo == 1, "male", "female")]
  cnt <- dcast(pob, hh_id ~ sex + age_grp, fun.aggregate = length,
               value.var = "numren", sep = "_")
  con <- merge(con, cnt, by = "hh_id", all.x = TRUE)
  cellcols <- setdiff(names(cnt), "hh_id")
  con[, (cellcols) := lapply(.SD, function(x) fifelse(is.na(x), 0L, x)), .SDcols = cellcols]

  con[, year := y]
  gh[, year := y]
  saveRDS(con, file.path(DERIV, sprintf("enigh_hh_%d.rds", y)))
  saveRDS(gh,  file.path(DERIV, sprintf("enigh_health_long_%d.rds", y)))
  saveRDS(pob, file.path(DERIV, sprintf("enigh_pob_%d.rds", y)))
  message(sprintf("   hh: %d rows | health items: %d | persons: %d | deflator %.4f",
                  nrow(con), nrow(gh), nrow(pob), dfl))
}

claves_all <- rbindlist(all_claves)
fwrite(claves_all, file.path(OUTTAB, "enigh_health_claves_all.csv"))

# quick internal check: detail sum vs concentrado 'salud' aggregate
for (y in ENIGH_YEARS) {
  con <- readRDS(file.path(DERIV, sprintf("enigh_hh_%d.rds", y)))
  r <- con[, sum(salud_detalle_tri * factor) / sum(salud * factor)]
  message(sprintf("check %d: detail/concentrado salud ratio = %.3f", y, r))
}
message("01_enigh_prepare done")
