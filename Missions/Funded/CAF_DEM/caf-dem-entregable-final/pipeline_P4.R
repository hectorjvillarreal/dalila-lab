# pipeline_P4.R — Bloque B del P4 (CAF_DEM). Reproduce la etapa de proyección del
# pipeline P3 (FISCAL_DEMO_v4) a partir de base_analisis_P3.csv y aplica:
#   B.1  re-estimación de las series de gasto funcional con (1) ventana de validación
#        anterior a 2020 y (2) sólo especificaciones amortiguadas; se elige la opción
#        con diagnósticos más limpios (control de rango + Ljung-Box).
#   B.2  poda de paneles con MASE > 2 (se retiran de la figura, se conservan en tabla).
#   B.3  regeneración sincronizada: figuras, tab_modelos, tab_frecuencia, base P4.
suppressPackageStartupMessages({library(tidyverse); library(forecast); library(knitr)})
set.seed(1)
base <- read_csv("base_analisis_P3.csv", show_col_types = FALSE)
niveles_ind <- c("Ingresos del gobierno general", "Balance primario",
                 "Deuda neta del gobierno general",
                 "Gasto público en salud", "Gasto público en pensiones")
funcionales <- c("Gasto público en salud", "Gasto público en pensiones")
obs <- base %>% filter(indicador %in% niveles_ind, tipo != "Proyección propia") %>%
  mutate(indicador = factor(indicador, levels = niveles_ind)) %>% arrange(indicador, pais, anio)
claves <- obs %>% distinct(indicador, pais) %>% arrange(indicador, pais)
series_list <- map(seq_len(nrow(claves)), function(i) {
  d <- obs %>% filter(indicador == claves$indicador[i], pais == claves$pais[i]) %>% arrange(anio)
  stopifnot(all(diff(d$anio) == 1)); ts(d$valor, start = min(d$anio), frequency = 1)})
names(series_list) <- paste(claves$indicador, claves$pais, sep = " — ")
cat("Series:", length(series_list), "\n")

h_eval <- 4; h_final <- 10; n_min <- 14
lambda_seguro <- function(y) if (min(y) > 0) BoxCox.lambda(y) else NULL
ajustar <- function(y, modelo, h, lambda) switch(modelo,
  "ARIMA" = forecast(auto.arima(y, lambda = lambda, stepwise = FALSE, approximation = FALSE), h = h),
  "ETS"   = forecast(ets(y, lambda = lambda), h = h),
  "ETS amortiguado" = forecast(ets(y, lambda = lambda, damped = TRUE), h = h),
  "Holt amortiguado" = holt(y, damped = TRUE, h = h, lambda = lambda))
metricas_oos <- function(real, pred, train) { e <- real - pred
  tibble(MAE = mean(abs(e)), RMSE = sqrt(mean(e^2)), MASE = mean(abs(e)) / mean(abs(diff(as.numeric(train))))) }
finito <- function(f) !is.null(f) && all(is.finite(f$mean)) && all(is.finite(f$lower)) && all(is.finite(f$upper))

# ventana: "P3" = últimos 4 años; "pre2020" = 4 años anteriores a 2020 (test 2016-2019)
correr <- function(i, ventana = "P3", cands_set = c("ARIMA","ETS","Holt amortiguado")) {
  y <- series_list[[i]]; nom <- names(series_list)[i]; n <- length(y); fin <- tsp(y)[2]
  if (n < n_min) return(NULL)
  if (ventana == "pre2020" && fin >= 2020) { fin_val <- 2019 } else { fin_val <- fin }
  train <- window(y, end = fin_val - h_eval)
  test  <- as.numeric(window(y, start = fin_val - h_eval + 1, end = fin_val))
  lam_t <- lambda_seguro(train)
  cands <- map(set_names(cands_set), ~ tryCatch(ajustar(train, .x, h_eval, lam_t), error = function(e) NULL))
  cands <- cands[!map_lgl(cands, is.null)]; if (!length(cands)) return(NULL)
  met <- imap_dfr(cands, ~ metricas_oos(test, as.numeric(.x$mean), train) %>% mutate(Modelo = .y))
  ganador <- met$Modelo[which.min(met$RMSE)]
  lam_f <- lambda_seguro(y); boxcox_retirado <- FALSE
  fc <- tryCatch(ajustar(y, ganador, h_final, lam_f), error = function(e) NULL)
  if (!finito(fc) && !is.null(lam_f)) { fc <- tryCatch(ajustar(y, ganador, h_final, NULL), error = function(e) NULL); boxcox_retirado <- TRUE }
  if (!finito(fc)) return(NULL)
  lb <- tryCatch(Box.test(na.omit(residuals(fc)), lag = min(8, floor(n / 3)), type = "Ljung-Box")$p.value, error = function(e) NA_real_)
  hist_min <- min(y); hist_max <- max(y); rango <- hist_max - hist_min; fin_proy <- as.numeric(tail(fc$mean, 1))
  list(res = tibble(Indicador = as.character(claves$indicador[i]), pais = claves$pais[i], n = n, Modelo = ganador,
         RMSE = round(met$RMSE[met$Modelo == ganador], 3), MASE = round(met$MASE[met$Modelo == ganador], 2),
         LjungBox = round(lb, 3), ventana = ventana, test_ini = fin_val - h_eval + 1, test_fin = fin_val,
         hist_min = hist_min, hist_max = hist_max, ultimo = as.numeric(tail(y, 1)), fin_proy = fin_proy,
         excede = fin_proy > hist_max + 0.5 * rango | fin_proy < hist_min - 0.5 * rango, boxcox_retirado = boxcox_retirado),
       fc = tibble(indicador = as.character(claves$indicador[i]), pais = claves$pais[i], modelo = ganador,
                   anio = seq(fin + 1, by = 1, length.out = h_final), media = as.numeric(fc$mean)))
}
idx_fun <- which(claves$indicador %in% funcionales); idx_agg <- setdiff(seq_len(nrow(claves)), idx_fun)
cat("\n== Agregados WEO: procedimiento P3 sin cambio ==\n")
r_agg <- map(idx_agg, correr)
cat("== Funcionales: réplica P3 (control) ==\n");      r_f0 <- map(idx_fun, correr, ventana = "P3")
cat("== Funcionales: Opción 1 (ventana pre-2020) ==\n"); r_f1 <- map(idx_fun, correr, ventana = "pre2020")
cat("== Funcionales: Opción 2 (sólo amortiguadas) ==\n"); r_f2 <- map(idx_fun, correr, ventana = "P3", cands_set = c("ETS amortiguado","Holt amortiguado"))
cat("== Diagnóstico adicional: Opción 1+2 (ventana pre-2020 y sólo amortiguadas) ==\n"); r_f12 <- map(idx_fun, correr, ventana = "pre2020", cands_set = c("ETS amortiguado","Holt amortiguado"))
tab <- function(r) map_dfr(r, "res"); fcs <- function(r) map_dfr(r, "fc")
resumen <- bind_rows(tab(r_f0) %>% mutate(opcion = "P3"), tab(r_f1) %>% mutate(opcion = "Opción 1"), tab(r_f2) %>% mutate(opcion = "Opción 2"), tab(r_f12) %>% mutate(opcion = "Opción 1+2 (diagnóstico)")) %>%
  select(opcion, Indicador, pais, Modelo, RMSE, MASE, LjungBox, ultimo, fin_proy, excede)
print(kable(resumen, digits = 2)); write_csv(resumen, "tablas/B1_comparacion_opciones.csv")
alert_p3 <- resumen %>% filter(opcion == "P3", excede) %>% transmute(Indicador, pais, en_p3 = TRUE)
diag <- resumen %>% left_join(alert_p3, by = c("Indicador","pais")) %>% group_by(opcion) %>%
  summarise(alertas = sum(excede), alertas_nuevas = sum(excede & is.na(en_p3)), lb_fallo = sum(LjungBox < 0.05, na.rm = TRUE), mase_gt2 = sum(MASE > 2), .groups = "drop")
print(diag); write_csv(diag, "tablas/B1_diagnostico_opciones.csv")
# Elección entre las dos opciones previstas en las instrucciones: menos alertas; empate -> menos alertas
# nuevas (series que no disparaban en P3); empate -> menos fallos Ljung-Box; empate -> menos MASE>2
eleg <- diag %>% filter(opcion %in% c("Opción 1","Opción 2")) %>% arrange(alertas, alertas_nuevas, lb_fallo, mase_gt2) %>% slice(1) %>% pull(opcion)
cat("\n>>> Opción elegida:", eleg, "\n")
r_fun <- if (eleg == "Opción 1") r_f1 else r_f2
resultados <- bind_rows(tab(r_agg), tab(r_fun)) %>% mutate(Indicador = factor(Indicador, levels = niveles_ind)) %>% arrange(Indicador, pais)
fc_tidy <- bind_rows(fcs(r_agg), fcs(r_fun)) %>% mutate(indicador = factor(indicador, levels = niveles_ind))
alertas <- resultados %>% filter(excede); cat("\nAlertas de rango tras la corrección:", nrow(alertas), "\n"); if (nrow(alertas)) print(alertas)
# --- B.2 poda -----------------------------------------------------------------
resultados <- resultados %>% mutate(informativa = MASE <= 2)
podadas <- resultados %>% filter(!informativa); cat("\nSeries no informativas (MASE > 2):\n"); print(select(podadas, Indicador, pais, MASE))
# --- Tablas LaTeX -----------------------------------------------------------------
exportar_tex <- function(df, archivo, alinear = NULL) { if (is.null(alinear)) alinear <- c("l", rep("r", ncol(df) - 1))
  cat(kable(df, format = "latex", booktabs = TRUE, linesep = "", align = alinear, escape = TRUE), file = file.path("tablas", archivo)); invisible(df) }
tab_modelos <- resultados %>% transmute(Indicador = as.character(Indicador), País = pais, n, Modelo, RMSE, MASE,
  `Ljung-Box (p)` = LjungBox, Ventana = paste0(test_ini, "-", test_fin), Figura = if_else(informativa, "sí", "no (n.i.)"))
exportar_tex(tab_modelos, "tab_modelos.tex")
frecuencia_modelos <- count(resultados, Modelo, sort = TRUE) %>% rename(`Series ganadas` = n); exportar_tex(frecuencia_modelos, "tab_frecuencia_modelos.tex")
write_csv(resultados, "tablas/B_resultados_completos.csv")
# --- Figuras --------------------------------------------------------------------------
color_hist <- "#1B3A5C"; color_fc <- "#8C1D40"
theme_caf <- function(base_size = 11) theme_minimal(base_size = base_size) + theme(
  plot.title = element_text(face = "bold", size = rel(1.02), color = "#1B3A5C"), plot.subtitle = element_text(size = rel(0.82), color = "grey35"),
  plot.caption = element_text(size = rel(0.68), color = "grey45", hjust = 0), strip.background = element_rect(fill = "#1B3A5C", color = NA),
  strip.text = element_text(color = "white", face = "bold", size = rel(0.78)), panel.grid.minor = element_blank(),
  panel.grid.major = element_line(color = "grey88", linewidth = 0.3), panel.background = element_rect(fill = "white", color = NA),
  plot.background = element_rect(fill = "white", color = NA), legend.position = "bottom", axis.title = element_text(size = rel(0.82), color = "grey20"), axis.text = element_text(color = "grey30"))
archivos_proj <- c("Ingresos del gobierno general" = "fig_proj_ingresos", "Deuda neta del gobierno general" = "fig_proj_deuda",
                   "Gasto público en salud" = "fig_proj_salud", "Gasto público en pensiones" = "fig_proj_pensiones")
for (ind in names(archivos_proj)) {
  keep <- resultados %>% filter(Indicador == ind, informativa) %>% pull(pais)
  fc_i <- fc_tidy %>% filter(indicador == ind, pais %in% keep); if (!nrow(fc_i)) next
  panel_lab <- fc_i %>% distinct(pais, modelo) %>% mutate(panel = paste0(pais, " · ", modelo))
  fc_i <- left_join(fc_i, panel_lab, by = c("pais", "modelo"))
  hist_i <- obs %>% filter(indicador == ind, pais %in% keep) %>% inner_join(panel_lab, by = "pais")
  ncol_p <- if (length(keep) <= 3) length(keep) else 3
  g <- ggplot() + geom_line(data = hist_i, aes(anio, valor), color = color_hist, linewidth = 0.7) +
    geom_line(data = fc_i, aes(anio, media), color = color_fc, linetype = "22", linewidth = 0.8) +
    facet_wrap(~ panel, scales = "free_y", ncol = ncol_p) +
    labs(title = paste0(ind, ": trayectoria observada y proyección a ", h_final, " años"),
         subtitle = paste0("Azul marino: observado · granate punteado: proyección. Se omiten los paneles con MASE > 2 (", 
                           paste(setdiff(unique(claves$pais), keep), collapse = ", "), ")."),
         x = NULL, y = "% del PIB", caption = "Fuentes: FMI-WEO (abril 2025) y CEPAL/FMI-GFS. Proyección: elaboración propia.") + theme_caf()
  ggsave(paste0("graficas/", archivos_proj[[ind]], ".png"), g, width = 10, height = if (length(keep) <= 3) 3.6 else 6, dpi = 300)
}
# --- Base P4 --------------------------------------------------------------------------------------
meta <- base %>% filter(indicador %in% niveles_ind) %>% distinct(indicador, codigo_indicador, unidad, cobertura_institucional, fuente)
notas <- base %>% filter(indicador %in% niveles_ind, tipo == "Proyección propia") %>% distinct(pais, indicador, nota)
base_fc <- fc_tidy %>% transmute(pais, anio, indicador = as.character(indicador), tipo = "Proyección propia", modelo, valor = round(media, 4)) %>%
  left_join(meta, by = "indicador") %>% left_join(notas, by = c("pais", "indicador")) %>%
  left_join(resultados %>% transmute(indicador = as.character(Indicador), pais, informativa), by = c("pais","indicador")) %>%
  mutate(iso3 = c(Brasil="BRA", Chile="CHL", Colombia="COL", `Costa Rica`="CRI", `México`="MEX", `Panamá`="PAN")[pais],
         nota = if_else(informativa, nota, if_else(is.na(nota), "Serie no informativa (MASE > 2): no citar como estimación puntual", paste(nota, "No informativa (MASE > 2): no citar como estimación puntual", sep = ". ")))) %>%
  select(pais, iso3, anio, indicador, codigo_indicador, tipo, modelo, valor, unidad, cobertura_institucional, fuente, nota)
nuevas <- read_csv("weo/series_nuevas_P4.csv", show_col_types = FALSE) %>% mutate(modelo = as.character(modelo))
base_p4 <- bind_rows(base %>% filter(tipo != "Proyección propia"), base_fc, nuevas) %>% arrange(indicador, pais, anio)
stopifnot(!any(duplicated(base_p4[, c("pais","anio","indicador")])))
write_excel_csv(base_p4, "base_analisis_P4.csv"); cat("base_analisis_P4.csv:", nrow(base_p4), "filas\n")
dic <- read_csv("base_analisis_P3_diccionario.csv", show_col_types = FALSE) %>% filter(Campo != "ADVERTENCIA DE USO")
adv <- paste0("Las proyecciones de gasto en salud y pensiones (tipo = 'Proyección propia') se re-estimaron en el Producto 4 (", eleg, ": ",
  if (eleg == "Opción 1") "ventana de validación 2016-2019, anterior al choque de 2020" else "conjunto de especificaciones restringido a modelos amortiguados",
  "). Tras la corrección ", if (nrow(alertas) == 0) "ninguna proyección excede el rango histórico observado según el control automático del pipeline." else paste0(nrow(alertas), " serie(s) siguen excediendo el rango histórico y conservan advertencia textual."),
  " Las series con MASE > 2 respecto del método ingenuo (", paste(paste(podadas$pais, tolower(podadas$Indicador), sep = ": "), collapse = "; "),
  ") se conservan en la base marcadas como no informativas y no deben citarse como estimación puntual. El balance primario no se grafica: es estacionario y su extrapolación univariada no aporta información más allá de su media. ",
  "Las series 'Crecimiento nominal del PIB' y 'Balance fiscal global' se incorporaron del WEO abril 2025 para el cálculo del diferencial (r - g) de la Sección 6.")
dic <- bind_rows(dic, tibble(Campo = "ADVERTENCIA DE USO", Descripción = adv)); write_excel_csv(dic, "base_analisis_P4_diccionario.csv")
exportar_tex(dic, "anexo_diccionario_base.tex", alinear = c("l","l"))
cat("\nLISTO. Opción:", eleg, "| alertas:", nrow(alertas), "| podadas:", nrow(podadas), "\n")
