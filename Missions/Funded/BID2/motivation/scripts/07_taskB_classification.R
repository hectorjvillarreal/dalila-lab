# 07_taskB_classification.R — curative / preventive / ambiguous classification
# of ENIGH health claves (both coding schemes), written as an auditable CSV,
# plus composition by income decile computed TWICE (ambiguous -> curative and
# ambiguous -> preventive).
# Classification judgments (stated, not neutral):
#  - curative: responds to a realized health event — illness consultations,
#    hospitalization, surgery, prescribed/therapeutic medicines, rehab devices,
#    nursing/long-term care, ambulance, delivery (parto).
#  - preventive: anticipatory/scheduled — prenatal control, vaccination,
#    contraception, smoking cessation, screening/prevention products.
#  - ambiguous (own category, never forced): OTC medicines, optical, dental,
#    chronic-disease maintenance, diagnostics without stated motive
#    (screening vs workup), alternative medicine, first-aid supplies,
#    insurance premiums / prepayment quotas (financing, not care),
#    weight control.
# 2024 caveat: COICOP medicine rubros carry no prescription status, so
# therapeutic-class medicines are classed curative there while the J-scheme
# splits recetados (curative) / sin receta (ambiguous) — a scheme
# discontinuity reported with the results, bracketed by the two-way runs.

source("scripts/00_common.R")

cls <- function(claves, class, rationale)
  data.table(clave = claves, class = class, rationale = rationale)

map_j <- rbindlist(list(
  cls(sprintf("J%03d", 1:6),  "curative",  "delivery (parto): realized-event hospital/professional services"),
  cls(c("J007", "J010", "J011", "J013"), "preventive", "prenatal control: scheduled monitoring during pregnancy"),
  cls("J008", "ambiguous", "dental during pregnancy"),
  cls("J009", "ambiguous", "prescribed medicines in pregnancy: treatment vs supplementation not observable"),
  cls("J012", "curative",  "hospitalization during pregnancy (non-delivery): complication response"),
  cls("J014", "ambiguous", "herbal/home remedies in pregnancy"),
  cls("J015", "ambiguous", "mixed rubro: ambulance + injections + vaccines"),
  cls(c("J016", "J017"), "curative", "medical consultations: motive unobservable, predominantly illness-driven (stated judgment)"),
  cls("J018", "ambiguous", "dental"),
  cls("J019", "ambiguous", "diagnostics: screening vs illness workup not observable (2022 wording includes 'tamiz')"),
  cls(sprintf("J%03d", c(20:30, 35)), "curative", "prescribed medicines for acute conditions"),
  cls(c("J031", "J032"), "ambiguous", "chronic-disease maintenance medication (hypertension, diabetes)"),
  cls("J033", "ambiguous", "prescribed vitamins: supplementation"),
  cls("J034", "preventive", "contraception"),
  cls(sprintf("J%03d", 36:38), "ambiguous", "weight control: lifestyle vs treatment"),
  cls(sprintf("J%03d", 39:43), "curative", "hospitalization / surgery block"),
  cls(sprintf("J%03d", c(44:54, 59)), "ambiguous", "over-the-counter medicines (instruction-listed ambiguous)"),
  cls(c("J055", "J056", "J057"), "ambiguous", "OTC vitamins / chronic maintenance"),
  cls("J058", "preventive", "contraception (OTC)"),
  cls(c("J060", "J061"), "ambiguous", "first-aid supplies"),
  cls(c("J062", "J063", "J064"), "ambiguous", "alternative medicine"),
  cls(c("J065", "J066"), "ambiguous", "optical / hearing aids"),
  cls(c("J067", "J068"), "curative", "orthopedic/rehab devices for realized conditions"),
  cls("J069", "ambiguous", "mixed rubro: nursing care + chronic monitoring devices"),
  cls(c("J070", "J071", "J072"), "ambiguous", "insurance premiums / prepayment quotas: financing, not care")))

map_c <- rbindlist(list(
  cls(c("061111", "061112", "061114", "061115", "061116", "061118", "061119",
        "06111A", "06111C", "06111D", "06111E", "06111G", "06111H"),
      "curative", "therapeutic-class medicines (no prescription status in COICOP)"),
  cls("061113", "preventive", "hormonal contraception"),
  cls("06111B", "ambiguous", "gyneco-obstetric medicines: treatment vs pregnancy supplementation"),
  cls("06111F", "ambiguous", "weight control"),
  cls("06111I", "ambiguous", "chronic maintenance: blood pressure / cardiovascular"),
  cls("061117", "ambiguous", "chronic maintenance: insulin / diabetes control"),
  cls("06111J", "ambiguous", "antiseptics / first-aid supplies"),
  cls("06111K", "ambiguous", "mixed rubro: other medicines incl. vaccines, sera, oxygen"),
  cls("06111L", "ambiguous", "vitamins and minerals"),
  cls("061120", "ambiguous", "homeopathic / naturist products"),
  cls("061211", "preventive", "pregnancy tests: screening"),
  cls("061212", "ambiguous", "diagnostic products: monitoring devices"),
  cls(c("061221", "061222", "061223"), "preventive", "prevention products: condoms, nicotine replacement, protection"),
  cls("061230", "ambiguous", "personal treatment devices incl. first-aid kits"),
  cls(c("061311", "061312", "061320"), "ambiguous", "optical / hearing aids"),
  cls(c("061331", "061332", "061333", "061334", "061335", "061336", "061337",
        "061338", "061401", "061402"),
      "curative", "orthopedic/assistive/rehab devices for realized conditions"),
  cls("062110", "preventive", "immunization and vaccination services"),
  cls(c("062191", "062193"), "curative", "medical consultations: motive unobservable, predominantly illness-driven (stated judgment)"),
  cls(c("062192", "062194"), "preventive", "prenatal consultations: scheduled monitoring"),
  cls(c("062195", "062196", "062197"), "ambiguous", "alternative / other practitioners"),
  cls("062198", "ambiguous", "midwife services: delivery vs prenatal not distinguished"),
  cls(c("062210", "062291", "062292"), "ambiguous", "dental"),
  cls(c("062311", "062312", "062321", "062322", "062323"), "curative",
      "curative / rehabilitation / nursing / assistance services"),
  cls("062313", "ambiguous", "thermal baths / corrective gymnastics"),
  cls(c("063101", "063102", "063103", "063104", "063105", "063106", "063200"),
      "curative", "hospitalization / surgery (incl. pregnancy and delivery inpatient)"),
  cls(c("064101", "064102"), "ambiguous", "laboratory / imaging: screening vs workup not observable"),
  cls("064103", "preventive", "prenatal laboratory / ultrasound: scheduled monitoring"),
  cls(c("064201", "064202"), "curative", "paramedic / ambulance services"),
  cls(c("121201", "121202"), "ambiguous", "medical insurance premiums: financing, not care")))

map_j[, scheme := "J_2018_2022"]
map_c[, scheme := "COICOP_2024"]
map_all <- rbind(map_j, map_c)

# attach official descriptors and verify complete coverage
claves <- fread(file.path(OUTTAB, "enigh_health_claves_all.csv"),
                colClasses = list(character = "clave"))
claves[, scheme := fifelse(year <= 2022, "J_2018_2022", "COICOP_2024")]
# one row per code: keep the 2018 descriptor for the J scheme (it carries the
# parto/embarazo block context that later waves drop)
setorder(claves, scheme, clave, year)
cover <- merge(claves[, .(descripcion = first(descripcion)), by = .(scheme, clave)],
               map_all, by = c("scheme", "clave"), all.x = TRUE)
stopifnot(!anyNA(cover$class))
fwrite(cover[order(scheme, clave)],
       file.path(OUTTAB, "curative_preventive_classification.csv"))
message("classification written: ", nrow(cover), " codes (",
        cover[class == "ambiguous", .N], " ambiguous)")

# ---- composition by income decile, both ambiguous assignments ------------
res <- list()
for (y in ENIGH_YEARS) {
  gh <- readRDS(file.path(DERIV, sprintf("enigh_health_long_%d.rds", y)))
  con <- readRDS(file.path(DERIV, sprintf("enigh_hh_%d.rds", y)))
  gh <- merge(gh, con[, .(hh_id, decile, factor)], by = "hh_id")
  gh <- merge(gh, map_all[, .(clave, class)], by = "clave", all.x = TRUE)
  stopifnot(!anyNA(gh$class))
  agg <- gh[, .(w = sum(gasto_tri_r * factor)), by = .(decile, class)]
  agg[, share := w / sum(w), by = decile]
  agg[, year := y]
  res[[as.character(y)]] <- agg
}
comp <- rbindlist(res)
fwrite(comp, file.path(OUTTAB, "fig7_composition_by_decile.csv"))

# sensitivity: reassign ambiguous both ways, national aggregate shares
sens <- comp[, .(w = sum(w)), by = .(year, class)]
sens <- dcast(sens, year ~ class, value.var = "w")
sens[, `:=`(tot = curative + preventive + ambiguous)]
sens[, `:=`(prev_share_base      = preventive / tot,
            prev_share_amb_to_prev = (preventive + ambiguous) / tot,
            prev_share_amb_to_cur  = preventive / tot,
            cur_share_amb_to_cur   = (curative + ambiguous) / tot,
            amb_share = ambiguous / tot)]
print(sens[, .(year, amb_share, prev_share_amb_to_cur, prev_share_amb_to_prev)])
fwrite(sens, file.path(OUTTAB, "fig7_ambiguous_sensitivity.csv"))
message("07_taskB_classification done")
