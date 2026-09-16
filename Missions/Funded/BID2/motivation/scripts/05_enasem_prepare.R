# 05_enasem_prepare.R — ENASEM 2018/2021/2024 panel construction.
# Builds per-wave person files with: 21-item Searle-convention frailty deficits
# (reconstruction of Judy's index — PROVISIONAL pending her confirmation),
# annual out-of-pocket health spending (section D), insurance, design vars;
# household net wealth (sections J/K); mortality spine from the 2024 master.
# Variable names from data/enasem_varmap.md (verified against dictionaries).
# 21 deficits = 5 ADL + 4 IADL + 2 mental (CES-D 5+ symptoms, poor memory)
#             + 8 diagnoses + obesity (BMI>=30 from self-reported c66/c67)
#             + current smoking.

source("scripts/00_common.R")

WAVES <- c("18", "21", "24")

find_csv <- function(year, pattern) {
  hits <- Sys.glob(file.path(DATA, "enasem", year,
                             paste0("*", pattern, "*"), "conjunto_de_datos", "*.csv"))
  stopifnot(length(hits) >= 1)
  hits[1]
}

clean_amt <- function(x, na_codes) {
  x <- as.numeric(x)
  fifelse(x %in% na_codes, NA_real_, x)
}
NA6 <- c(777777, 888888, 999999)  # in-kind / NR / NS for 6-digit amounts

for (ww in WAVES) {
  year <- paste0("20", ww)
  message("== ENASEM ", year)
  sfx <- function(stem) paste0(stem, "_", ww)

  # ---- constructed file: demographics, deficits, insurance ---------------
  cons <- fread(find_csv(year, "variables_creadas"), encoding = "UTF-8")
  setnames(cons, tolower(names(cons)))

  deficits <- c(paste0("abvd_", c("caminar", "banar", "comer", "cama", "bano")),
                paste0("aivd_", c("comidas", "comprar", "medicina", "dinero")),
                "hipertension", "diabetes", "cancer", "enf_pulm",
                "infarto", "prob_card", "embolia", "artritis", "tabaco")
  keep <- c("cunicah", "np", sfx("factori"), sfx("factorh"),
            "genero", "educacion", sfx("edad"), sfx("salud_glob"),
            sfx(deficits), sfx("cesd_deprimido"), sfx("memoria"),
            sfx("imc_cat"),
            sfx(c("hospitalizacion", "visita_medica", "ciru_ambu", "visita_dental")),
            sfx("seguro_medico"),
            if (ww == "18") c("est_dis", "upm_dis") else sfx(c("est_dis", "upm_dis")),
            if (ww == "18") "seg_pop_18",
            if (ww == "21") "insabi_21",
            if (ww == "24") "imss_bienestar_24",
            sfx(c("imss", "issste", "pem_def_mar", "seguro_privado")))
  keep <- intersect(keep, names(cons))
  p <- cons[, ..keep]
  # strip wave suffix for a harmonized panel layout
  setnames(p, keep, gsub(paste0("_", ww, "$"), "", keep))
  if (ww == "18") setnames(p, "seg_pop", "pub_noncontrib", skip_absent = TRUE)
  if (ww == "21") setnames(p, "insabi", "pub_noncontrib", skip_absent = TRUE)
  if (ww == "24") setnames(p, "imss_bienestar", "pub_noncontrib", skip_absent = TRUE)

  # mental deficits
  p[, def_depr := fifelse(cesd_deprimido %in% c(0, 1), as.numeric(cesd_deprimido), NA_real_)]
  p[, def_memoria := fcase(memoria %in% 4:5, 1, memoria %in% 1:3, 0, default = NA_real_)]

  # ---- individual sections: OOP spending + height/weight -----------------
  ind <- fread(find_csv(year, "sect_a_c_d"), encoding = "UTF-8",
               select = NULL)
  setnames(ind, tolower(names(ind)))
  dvars <- c("d6", "d9_1", "d9_2", "d9_3", "d12a", "d12c", "d13",
             "c66", "c67_1", "c67_2")
  sel <- c("cunicah", "np", sfx(dvars))
  sel <- intersect(sel, names(ind))
  ind <- ind[, ..sel]
  setnames(ind, sel, gsub(paste0("_", ww, "$"), "", sel))

  for (v in c("d6", "d9_1", "d9_2", "d9_3", "d12a"))
    if (v %in% names(ind)) ind[, (v) := clean_amt(get(v), NA6)]
  ind[, oop_annual := {
    comps <- cbind(d6, d9_1, d9_2, d9_3, 12 * d12a)
    allna <- rowSums(!is.na(comps)) == 0
    s <- rowSums(comps, na.rm = TRUE)
    fifelse(allna, NA_real_, s)
  }]
  # BMI from self-reported weight (kg) / height (m) — c67_1 metros, c67_2 cm
  ind[, c66 := clean_amt(c66, c(888, 999, 8888, 9999))]
  ind[, ht_m := suppressWarnings(as.numeric(c67_1) + as.numeric(c67_2) / 100)]
  ind[, ht_m := fifelse(ht_m > 1 & ht_m < 2.3, ht_m, NA_real_)]
  ind[, bmi := fifelse(!is.na(c66) & c66 >= 30 & c66 <= 175, c66, NA_real_) / ht_m^2]
  ind[, def_obese := fcase(bmi >= 30, 1, bmi < 30, 0, default = NA_real_)]

  p <- merge(p, ind, by = c("cunicah", "np"), all.x = TRUE)

  # ---- household wealth (sections J/K) -----------------------------------
  hh <- fread(find_csv(year, "sect_g_j_k"), encoding = "UTF-8")
  setnames(hh, tolower(names(hh)))
  wvars <- c("j31", "j34", "k8_1", "k8_2", "k24_1", "k33_1", "k33_2", "k33_3",
             "k42", "k86")
  wsel <- c("cunicah", sfx(wvars))
  wsel <- intersect(wsel, names(hh))
  hw <- hh[, ..wsel]
  setnames(hw, wsel, gsub(paste0("_", ww, "$"), "", wsel))
  NA8 <- c(88888888, 99999999, 8888888, 9999999, 888888, 999999)
  for (v in setdiff(names(hw), "cunicah")) hw[, (v) := clean_amt(get(v), NA8)]
  hw <- hw[, lapply(.SD, function(x) suppressWarnings(mean(x, na.rm = TRUE))),
           by = cunicah]  # one record per household id
  assets <- intersect(c("j31", "j34", "k8_1", "k8_2", "k24_1",
                        "k33_1", "k33_2", "k33_3", "k42"), names(hw))
  hw[, wealth := {
    a <- rowSums(as.matrix(.SD), na.rm = TRUE)
    allna <- rowSums(!is.na(as.matrix(.SD))) == 0
    fifelse(allna, NA_real_, a)
  }, .SDcols = assets]
  if ("k86" %in% names(hw)) hw[, wealth := wealth - fifelse(is.na(k86), 0, k86)]
  p <- merge(p, hw[, .(cunicah, wealth)], by = "cunicah", all.x = TRUE)

  # ---- frailty index (denominator = items observed; require >= 15/21) ----
  defcols <- c(paste0("abvd_", c("caminar", "banar", "comer", "cama", "bano")),
               paste0("aivd_", c("comidas", "comprar", "medicina", "dinero")),
               "hipertension", "diabetes", "cancer", "enf_pulm", "infarto",
               "prob_card", "embolia", "artritis", "tabaco",
               "def_depr", "def_memoria", "def_obese")
  defcols <- intersect(defcols, names(p))
  for (v in defcols) p[, (v) := fifelse(get(v) %in% c(0, 1), as.numeric(get(v)), NA_real_)]
  p[, n_def_obs := rowSums(!is.na(.SD)), .SDcols = defcols]
  p[, frailty := fifelse(n_def_obs >= 15,
                         rowSums(.SD, na.rm = TRUE) / n_def_obs, NA_real_),
    .SDcols = defcols]

  p[, wave := as.integer(year)]
  saveRDS(p, file.path(DERIV, sprintf("enasem_person_%s.rds", year)))
  message(sprintf("   %d persons | frailty obs: %d (median %.3f) | OOP obs: %d | wealth obs: %d",
                  nrow(p), p[!is.na(frailty), .N], p[, median(frailty, na.rm = TRUE)],
                  p[!is.na(oop_annual), .N], p[!is.na(wealth), .N]))
}

# ---- mortality / attrition spine from the 2024 master --------------------
mst <- fread(find_csv("2024", "master_follow_up"), encoding = "UTF-8")
setnames(mst, tolower(names(mst)))
msel <- intersect(c("cunicah", "np", "fallecido_18", "fallecido_21", "fallecido_24",
                    "tipent_18", "tipent_21", "tipent_24", "tipne_21", "tipne_24",
                    "age_18", "age_21", "age_24", "sex_18", "sex_21", "sex_24",
                    "factori_18", "factori_21", "factori_24", "yrschool"),
                  names(mst))
spine <- mst[, ..msel]
saveRDS(spine, file.path(DERIV, "enasem_spine.rds"))
message(sprintf("spine: %d persons | died 18-21: %d | died 21-24: %d",
                nrow(spine), spine[fallecido_21 %in% c(1, 2), .N],
                spine[fallecido_24 == 1, .N]))
message("05_enasem_prepare done")
