library(readxl)
library(tidyverse)
library(forecast)
library(tseries)

# Ajustar a la carpeta con los archivos brutos:
#   WEO_Gobierno_balance.xlsx · IMF_Pensiones_salud.xlsx · demografia_LIMPIA.xlsx
# setwd("C:/ruta/a/tu/carpeta")

dir.create("graficas", showWarnings = FALSE)
dir.create("tablas",   showWarnings = FALSE)

# --- Codificación ---------------------------------------------------------
# Este archivo debe estar guardado en UTF-8. Si los acentos del propio código
# se ven mal en el editor, en RStudio: File > Reopen with Encoding > UTF-8
# (y luego File > Save with Encoding > UTF-8 para dejarlo fijo).
# Los .csv se exportan con readr::write_excel_csv, que escribe UTF-8 con BOM
# para que Excel en Windows los abra correctamente.
cat("Locale:", Sys.getlocale("LC_CTYPE"), "\n")

cat("Codificación nativa:", l10n_info()$codeset, "\n")

# Paleta institucional (sin colores pastel por defecto de ggplot2)
paleta_paises <- c(
  "Brasil"     = "#1B3A5C",  # azul marino
  "Chile"      = "#8C1D40",  # granate
  "Colombia"   = "#3E7C8C",  # azul petróleo
  "Costa Rica" = "#B08D57",  # bronce
  "México"     = "#4C6445",  # verde oscuro
  "Panamá"     = "#5C5C5C"   # gris carbón
)
color_hist <- "#1B3A5C"; color_fc <- "#8C1D40"

theme_caf <- function(base_size = 11) {
  theme_minimal(base_size = base_size) +
    theme(
      plot.title       = element_text(face = "bold", size = rel(1.02), color = "#1B3A5C"),
      plot.subtitle    = element_text(size = rel(0.82), color = "grey35"),
      plot.caption     = element_text(size = rel(0.68), color = "grey45", hjust = 0),
      strip.background = element_rect(fill = "#1B3A5C", color = NA),
      strip.text       = element_text(color = "white", face = "bold", size = rel(0.78)),
      panel.grid.minor = element_blank(),
      panel.grid.major = element_line(color = "grey88", linewidth = 0.3),
      panel.background = element_rect(fill = "white", color = NA),
      plot.background  = element_rect(fill = "white", color = NA),
      legend.position  = "bottom",
      legend.title     = element_text(face = "bold", size = rel(0.82)),
      legend.text      = element_text(size = rel(0.78)),
      axis.title       = element_text(size = rel(0.82), color = "grey20"),
      axis.text        = element_text(color = "grey30")
    )
}

# Exportador de tablas a LaTeX (booktabs, sin entorno table: se envuelve en el .tex)
exportar_tex <- function(df, archivo, alinear = NULL) {
  if (is.null(alinear)) alinear <- c("l", rep("r", ncol(df) - 1))
  cat(
    knitr::kable(df, format = "latex", booktabs = TRUE, linesep = "",
                 align = alinear, escape = TRUE),
    file = file.path("tablas", archivo)
  )
  invisible(df)
}

demog_tfr <- read_excel("limpio/demografia_LIMPIA.xlsx", sheet = "tfg")
demog_dep <- read_excel("limpio/demografia_LIMPIA.xlsx", sheet = "dependencia")
resumen_demog <- read_excel("limpio/demografia_LIMPIA.xlsx", sheet = "resumen_tab_demog")

anio_corte_demog <- 2023   # WPP: estimación hasta 2023; proyección mediana desde 2024

tfr <- demog_tfr %>%
  transmute(pais, anio = as.integer(anio),
            indicador = "Tasa global de fecundidad (hijos por mujer)",
            valor = as.numeric(valor))

dep_senil <- demog_dep %>%
  filter(indicador == "Razón de dependencia senil (65+/15-64)") %>%
  transmute(pais, anio = as.integer(anio),
            indicador = "Razón de dependencia senil (%)",
            valor = as.numeric(valor) * 100)

df_demog <- bind_rows(tfr, dep_senil) %>%
  mutate(
    indicador = factor(indicador, levels = c(
      "Tasa global de fecundidad (hijos por mujer)",
      "Razón de dependencia senil (%)")),
    periodo = if_else(anio <= anio_corte_demog, "Estimación", "Proyección (mediana)")
  )

g_demog <- ggplot(df_demog, aes(anio, valor, color = pais, linetype = periodo)) +
  geom_line(linewidth = 0.8) +
  geom_vline(xintercept = anio_corte_demog, linetype = "dotted", color = "grey50") +
  facet_wrap(~ indicador, scales = "free_y", nrow = 1) +
  scale_color_manual(values = paleta_paises) +
  scale_linetype_manual(values = c("Estimación" = "solid", "Proyección (mediana)" = "22")) +
  labs(x = NULL, y = NULL, color = "País", linetype = NULL,
       caption = "Fuente: UN World Population Prospects 2024, revisión mediana. Línea vertical: fin de la estimación (2023).") +
  theme_caf()
print(g_demog)

ggsave("graficas/fig_demografia.png", g_demog, width = 10, height = 5, dpi = 300)

tab_demog <- resumen_demog %>%
  transmute(
    País = pais,
    `TFR (2024)`        = round(TFR_2024, 2),
    `RD senil 2025 (\\%)` = round(RD_senil_2025 * 100, 1),
    `RD senil 2050 (\\%)` = round(RD_senil_2050 * 100, 1),
    `Factor 2025--2050`   = round(veces_duplica_RD, 2)
  ) %>%
  arrange(desc(`RD senil 2050 (\\%)`))

knitr::kable(tab_demog, caption = "Indicadores demográficos, seis países (UN WPP 2024)")

exportar_tex(tab_demog, "tab_demografia.tex")

weo_raw <- read_excel("WEO_Gobierno_balance.xlsx",
                      sheet = "WEO_Gobierno_balance", na = c("n/a", "--", ""))
imf_raw <- read_excel("IMF_Pensiones_salud.xlsx", sheet = "datos")

anios_weo <- as.character(2000:2024)

# --- WEO: ingresos, balance primario, deuda neta y gasto total ---
weo_long <- weo_raw %>%
  filter(!is.na(ISO)) %>%
  filter(`WEO Subject Code` %in% c("GGR_NGDP", "GGXONLB_NGDP",
                                   "GGXWDN_NGDP", "GGX_NGDP")) %>%
  select(ISO, code = `WEO Subject Code`, all_of(anios_weo)) %>%
  mutate(across(all_of(anios_weo), as.character)) %>%
  pivot_longer(all_of(anios_weo), names_to = "anio", values_to = "valor") %>%
  mutate(anio = as.integer(anio), valor = as.numeric(valor),
         pais = recode(ISO, BRA = "Brasil", CHL = "Chile", COL = "Colombia",
                       CRI = "Costa Rica", MEX = "México", PAN = "Panamá")) %>%
  filter(!is.na(valor))

weo <- weo_long %>%
  filter(code != "GGX_NGDP") %>%
  mutate(indicador = recode(code,
    GGR_NGDP     = "Ingresos del gobierno general",
    GGXONLB_NGDP = "Balance primario",
    GGXWDN_NGDP  = "Deuda neta del gobierno general")) %>%
  select(pais, anio, indicador, valor)

gasto_total <- weo_long %>%
  filter(code == "GGX_NGDP") %>%
  select(pais, anio, gasto_total = valor)

# --- Salud y pensiones (gobierno central) ---
imf <- imf_raw %>%
  select(pais = `País__ESTANDAR`, funcion = `Gasto público por función`,
         anio = `Años__ESTANDAR`, valor = value) %>%
  mutate(anio = as.integer(anio), valor = as.numeric(valor))

salud <- imf %>% filter(funcion == "Salud") %>%
  mutate(indicador = "Gasto público en salud") %>%
  select(pais, anio, indicador, valor)

imf_wide <- imf %>% filter(funcion != "Salud") %>%
  pivot_wider(names_from = funcion, values_from = valor) %>%
  rename(vejez = `Edad avanzada`, enfermedad = `Enfermedad e incapacidad`)

# Regla de agregación: se suma "Enfermedad e incapacidad" a "Edad avanzada"
# sólo si su cobertura alcanza el 70% de los años con dato de vejez; en caso
# contrario la serie es sólo vejez (cota inferior). Evita saltos de definición
# a mitad de muestra.
regla_pensiones <- imf_wide %>%
  group_by(pais) %>%
  summarise(n_vejez = sum(!is.na(vejez)), n_enf = sum(!is.na(enfermedad)),
            cobertura = round(n_enf / n_vejez, 2),
            incluye_enf = cobertura >= 0.7, .groups = "drop")

pensiones <- imf_wide %>%
  left_join(select(regla_pensiones, pais, incluye_enf), by = "pais") %>%
  mutate(valor = if_else(incluye_enf, vejez + enfermedad, vejez)) %>%
  filter(!is.na(valor)) %>%
  mutate(indicador = "Gasto público en pensiones") %>%
  select(pais, anio, indicador, valor)

niveles_ind <- c("Ingresos del gobierno general", "Balance primario",
                 "Deuda neta del gobierno general",
                 "Gasto público en salud", "Gasto público en pensiones")

df_fiscal <- bind_rows(weo, salud, pensiones) %>%
  mutate(indicador = factor(indicador, levels = niveles_ind)) %>%
  arrange(indicador, pais, anio)

# Conservar el tramo contiguo más reciente (requisito para declarar ts sin huecos)
tramo_contiguo <- function(d) {
  d <- arrange(d, anio)
  g <- cumsum(c(0, diff(d$anio) != 1))
  filter(mutate(d, g = g), g == max(g)) %>% select(-g)
}
df_fiscal <- df_fiscal %>% group_by(indicador, pais) %>%
  group_modify(~ tramo_contiguo(.x)) %>% ungroup()

knitr::kable(regla_pensiones,
             caption = "Regla de agregación de la serie de pensiones por país")

archivos_fig <- c(
  "Ingresos del gobierno general"     = "fig_ingresos",
  "Balance primario"                  = "fig_balance",
  "Deuda neta del gobierno general"   = "fig_deuda",
  "Gasto público en salud"            = "fig_salud",
  "Gasto público en pensiones"        = "fig_pensiones"
)

fuente_weo <- "Fuente: FMI, World Economic Outlook (abril 2025). Los valores de 2024 son estimación del FMI en Brasil, Costa Rica y Panamá."
fuente_gfs <- "Fuente: CEPAL/FMI-GFS, gasto público por función, cobertura de gobierno central."

for (ind in levels(df_fiscal$indicador)) {
  d <- filter(df_fiscal, indicador == ind)
  es_weo <- ind %in% c("Ingresos del gobierno general", "Balance primario",
                       "Deuda neta del gobierno general")

  g <- ggplot(d, aes(anio, valor, color = pais)) +
    geom_line(linewidth = 0.85) +
    scale_color_manual(values = paleta_paises) +
    labs(title = ind, x = NULL, y = "% del PIB", color = "País",
         caption = if (es_weo) fuente_weo else fuente_gfs) +
    theme_caf()

  # El balance primario cruza el cero: se marca la referencia
  if (ind == "Balance primario") {
    g <- g + geom_hline(yintercept = 0, linetype = "dashed",
                        color = "grey45", linewidth = 0.4)
  }

  print(g)
  ggsave(paste0("graficas/", archivos_fig[[ind]], ".png"), g,
         width = 9, height = 4.6, dpi = 300)
}

# Último dato y variación (diferencia en p.p.) por serie
tab_ultimo <- df_fiscal %>%
  group_by(indicador, pais) %>%
  arrange(anio) %>%
  slice_tail(n = 2) %>%
  summarise(anio_t = last(anio), valor_t = last(valor),
            valor_t1 = first(valor), .groups = "drop") %>%
  mutate(delta = valor_t - valor_t1)

# --- Tabla A: agregados WEO (los tres terminan en 2024) ---
tab_weo <- tab_ultimo %>%
  filter(indicador %in% c("Ingresos del gobierno general", "Balance primario",
                          "Deuda neta del gobierno general")) %>%
  mutate(ind_corto = recode(as.character(indicador),
    "Ingresos del gobierno general"   = "Ingresos",
    "Balance primario"                = "Balance",
    "Deuda neta del gobierno general" = "Deuda")) %>%
  select(pais, ind_corto, valor_t, delta) %>%
  pivot_wider(names_from = ind_corto, values_from = c(valor_t, delta)) %>%
  transmute(País = pais,
            Ingresos    = round(valor_t_Ingresos, 1),
            `$\\Delta$ Ing.`   = sprintf("%+.1f", delta_Ingresos),
            Balance     = round(valor_t_Balance, 1),
            `$\\Delta$ Bal.`   = sprintf("%+.1f", delta_Balance),
            Deuda       = round(valor_t_Deuda, 1),
            `$\\Delta$ Deuda`  = sprintf("%+.1f", delta_Deuda)) %>%
  arrange(País)

knitr::kable(tab_weo,
             caption = "Agregados fiscales en 2024 y variación respecto a 2023 (% del PIB; variación en p.p.)")

exportar_tex(tab_weo, "tab_ultimo_weo.tex")

# --- Tabla B: gasto funcional (año de corte distinto por país) ---
tab_gfs <- tab_ultimo %>%
  filter(indicador %in% c("Gasto público en salud", "Gasto público en pensiones")) %>%
  mutate(ind_corto = recode(as.character(indicador),
    "Gasto público en salud"     = "Salud",
    "Gasto público en pensiones" = "Pensiones")) %>%
  select(pais, ind_corto, anio_t, valor_t, delta) %>%
  pivot_wider(names_from = ind_corto, values_from = c(anio_t, valor_t, delta))

# Verificación: la columna "Año" asume que salud y pensiones terminan el mismo año
if (any(tab_gfs$anio_t_Salud != tab_gfs$anio_t_Pensiones)) {
  warning("Salud y pensiones tienen años de corte distintos en algún país: revisar tabla.")
}

tab_gfs <- tab_gfs %>%
  transmute(País = pais,
            Año = anio_t_Salud,
            Salud       = round(valor_t_Salud, 2),
            `$\\Delta$ Salud` = sprintf("%+.2f", delta_Salud),
            Pensiones   = round(valor_t_Pensiones, 2),
            `$\\Delta$ Pens.` = sprintf("%+.2f", delta_Pensiones)) %>%
  arrange(País)

knitr::kable(tab_gfs,
             caption = "Gasto en salud y pensiones: último año disponible y variación respecto al año previo")

exportar_tex(tab_gfs, "tab_ultimo_gfs.tex")

gasto_funcional <- bind_rows(salud, pensiones) %>%
  pivot_wider(names_from = indicador, values_from = valor) %>%
  rename(salud = `Gasto público en salud`,
         pensiones = `Gasto público en pensiones`) %>%
  filter(!is.na(salud), !is.na(pensiones)) %>%
  inner_join(gasto_total, by = c("pais", "anio")) %>%
  mutate(
    suma_funcional = salud + pensiones,
    part_salud     = 100 * salud     / gasto_total,
    part_pensiones = 100 * pensiones / gasto_total,
    part_total     = 100 * suma_funcional / gasto_total
  )

# Último año con dato simultáneo de las tres fuentes, por país
comp_ultimo <- gasto_funcional %>%
  group_by(pais) %>% slice_max(anio, n = 1, with_ties = FALSE) %>% ungroup()

tab_composicion <- comp_ultimo %>%
  transmute(País = pais, Año = anio,
            `Salud (\\% PIB)`      = round(salud, 1),
            `Pensiones (\\% PIB)`  = round(pensiones, 1),
            `Gasto total (\\% PIB)` = round(gasto_total, 1),
            `Salud (\\% del gasto)`     = round(part_salud, 1),
            `Pensiones (\\% del gasto)` = round(part_pensiones, 1),
            `Suma (\\% del gasto)`      = round(part_total, 1)) %>%
  arrange(desc(`Suma (\\% del gasto)`))

knitr::kable(tab_composicion,
             caption = "Peso de salud y pensiones en el gasto público total, último año con dato simultáneo")

exportar_tex(tab_composicion, "tab_composicion_gasto.tex")

d_comp <- comp_ultimo %>%
  select(pais, anio, Salud = part_salud, Pensiones = part_pensiones) %>%
  pivot_longer(c(Salud, Pensiones), names_to = "funcion", values_to = "participacion") %>%
  mutate(pais_lab = paste0(pais, "\n(", anio, ")"))

orden_pais <- comp_ultimo %>% arrange(desc(part_total)) %>%
  mutate(pais_lab = paste0(pais, "\n(", anio, ")")) %>% pull(pais_lab)
d_comp$pais_lab <- factor(d_comp$pais_lab, levels = orden_pais)

g_comp <- ggplot(d_comp, aes(pais_lab, participacion, fill = funcion)) +
  geom_col(width = 0.62) +
  scale_fill_manual(values = c("Salud" = "#3E7C8C", "Pensiones" = "#1B3A5C")) +
  labs(title = "Participación de salud y pensiones en el gasto público total",
       subtitle = "Último año con dato simultáneo de gasto funcional y gasto total; entre paréntesis, el año",
       x = NULL, y = "% del gasto público total", fill = NULL,
       caption = paste("Fuentes: CEPAL/FMI-GFS (gasto funcional, gobierno central) y FMI-WEO (gasto total, gobierno general).",
                       "\nLa diferencia de cobertura institucional implica que las participaciones son una cota inferior, especialmente donde la seguridad social opera fuera del gobierno central.")) +
  theme_caf()
print(g_comp)

ggsave("graficas/fig_composicion_gasto.png", g_comp, width = 9, height = 4.6, dpi = 300)

claves <- df_fiscal %>% distinct(indicador, pais) %>% arrange(indicador, pais)
series_list <- vector("list", nrow(claves))
names(series_list) <- paste(claves$indicador, claves$pais, sep = " — ")
for (i in seq_len(nrow(claves))) {
  d <- df_fiscal %>%
    filter(indicador == claves$indicador[i], pais == claves$pais[i]) %>% arrange(anio)
  series_list[[i]] <- ts(d$valor, start = min(d$anio), frequency = 1)
}
cat("Series construidas:", nrow(claves), "\n")

library(strucchange)

tab_integracion <- map_dfr(seq_len(nrow(claves)), function(i) {
  y <- series_list[[i]]
  tibble(
    Indicador = as.character(claves$indicador[i]),
    pais      = claves$pais[i],
    n         = length(y),
    ADF_p     = tryCatch(round(suppressWarnings(adf.test(y)$p.value), 3),  error = function(e) NA),
    KPSS_p    = tryCatch(round(suppressWarnings(kpss.test(y)$p.value), 3), error = function(e) NA),
    d         = tryCatch(ndiffs(y), error = function(e) NA_integer_)
  )
})

resumen_d <- tab_integracion %>%
  count(Indicador, d) %>%
  pivot_wider(names_from = d, values_from = n, values_fill = 0,
              names_prefix = "d = ")

knitr::kable(resumen_d,
             caption = "Orden de integración sugerido (ndiffs), número de países por indicador")

exportar_tex(resumen_d, "tab_integracion.tex")

knitr::kable(tab_integracion, caption = "Detalle por serie: pruebas de raíz unitaria y diferencias sugeridas")

h_eval  <- 4    # años reservados para validación
h_final <- 10   # horizonte de proyección
n_min   <- 14   # tamaño mínimo de serie

lambda_seguro <- function(y) if (min(y) > 0) BoxCox.lambda(y) else NULL

ajustar <- function(y, modelo, h, lambda) {
  switch(modelo,
    "ARIMA" = forecast(auto.arima(y, lambda = lambda, stepwise = FALSE,
                                  approximation = FALSE), h = h),
    "ETS"   = forecast(ets(y, lambda = lambda), h = h),
    "Holt amortiguado" = holt(y, damped = TRUE, h = h, lambda = lambda)
  )
}

metricas_oos <- function(real, pred, train) {
  e <- real - pred
  tibble(MAE  = mean(abs(e)),
         RMSE = sqrt(mean(e^2)),
         MASE = mean(abs(e)) / mean(abs(diff(as.numeric(train)))))
}

resultados <- tibble(); fc_tidy <- tibble(); bitacora <- tibble()

for (i in seq_len(nrow(claves))) {
  y <- series_list[[i]]; nom <- names(series_list)[i]; n <- length(y)
  if (n < n_min) next

  fin   <- tsp(y)[2]
  train <- window(y, end = fin - h_eval)
  test  <- as.numeric(window(y, start = fin - h_eval + 1))
  lam_t <- lambda_seguro(train)

  cands <- list(
    "ARIMA"            = tryCatch(ajustar(train, "ARIMA", h_eval, lam_t), error = function(e) NULL),
    "ETS"              = tryCatch(ajustar(train, "ETS",   h_eval, lam_t), error = function(e) NULL),
    "Holt amortiguado" = tryCatch(ajustar(train, "Holt amortiguado", h_eval, lam_t), error = function(e) NULL)
  )
  cands <- cands[!map_lgl(cands, is.null)]
  if (!length(cands)) next

  met <- imap_dfr(cands, ~ metricas_oos(test, as.numeric(.x$mean), train) %>%
                    mutate(Modelo = .y))
  ganador <- met$Modelo[which.min(met$RMSE)]

  # Reestimación sobre la muestra completa. Salvaguarda: si la retrotransformación
  # Box-Cox produce valores no finitos al horizonte largo, se reestima sin ella.
  lam_f  <- lambda_seguro(y)
  fc     <- tryCatch(ajustar(y, ganador, h_final, lam_f), error = function(e) NULL)
  finito <- function(f) !is.null(f) && all(is.finite(f$mean)) &&
                        all(is.finite(f$lower)) && all(is.finite(f$upper))
  if (!finito(fc) && !is.null(lam_f)) {
    fc <- tryCatch(ajustar(y, ganador, h_final, NULL), error = function(e) NULL)
    bitacora <- bind_rows(bitacora, tibble(serie = nom, lambda = round(lam_f, 4)))
  }
  if (!finito(fc)) next

  lb <- tryCatch(Box.test(na.omit(residuals(fc)), lag = min(8, floor(n / 3)),
                          type = "Ljung-Box")$p.value, error = function(e) NA_real_)

  resultados <- bind_rows(resultados, tibble(
    Indicador = as.character(claves$indicador[i]), pais = claves$pais[i],
    n = n, Modelo = ganador,
    RMSE = round(met$RMSE[met$Modelo == ganador], 3),
    MASE = round(met$MASE[met$Modelo == ganador], 2),
    LjungBox = round(lb, 3)))

  fc_tidy <- bind_rows(fc_tidy, tibble(
    indicador = as.character(claves$indicador[i]), pais = claves$pais[i],
    modelo = ganador, anio = seq(fin + 1, by = 1, length.out = h_final),
    media = as.numeric(fc$mean)))
}

fc_tidy <- fc_tidy %>% mutate(indicador = factor(indicador, levels = niveles_ind))

tab_modelos <- resultados %>%
  transmute(Indicador, País = pais, n, Modelo,
            RMSE, MASE, `Ljung-Box (p)` = LjungBox)

knitr::kable(tab_modelos,
             caption = "Modelo seleccionado por serie, desempeño fuera de muestra y diagnóstico de residuales")

exportar_tex(tab_modelos, "tab_modelos.tex")

frecuencia_modelos <- count(resultados, Modelo, sort = TRUE) %>%
  rename(`Series ganadas` = n)
knitr::kable(frecuencia_modelos, caption = "Frecuencia de selección por familia de modelo")

exportar_tex(frecuencia_modelos, "tab_frecuencia_modelos.tex")

if (nrow(bitacora)) {
  knitr::kable(bitacora, caption = "Series reestimadas sin transformación Box-Cox")
} else cat("Ninguna serie requirió reestimación sin Box-Cox.\n")

archivos_proj <- c(
  "Ingresos del gobierno general"   = "fig_proj_ingresos",
  "Balance primario"                = "fig_proj_balance",
  "Deuda neta del gobierno general" = "fig_proj_deuda",
  "Gasto público en salud"          = "fig_proj_salud",
  "Gasto público en pensiones"      = "fig_proj_pensiones"
)

for (ind in levels(df_fiscal$indicador)) {
  fc_i <- fc_tidy %>% filter(indicador == ind)
  if (!nrow(fc_i)) next

  panel_lab <- fc_i %>% distinct(pais, modelo) %>%
    mutate(panel = paste0(pais, " · ", modelo))

  fc_i   <- left_join(fc_i, panel_lab, by = c("pais", "modelo"))
  hist_i <- df_fiscal %>% filter(indicador == ind) %>%
    inner_join(panel_lab, by = "pais")

  g <- ggplot() +
    geom_line(data = hist_i, aes(anio, valor), color = color_hist, linewidth = 0.7) +
    geom_line(data = fc_i, aes(anio, media), color = color_fc,
              linetype = "22", linewidth = 0.8) +
    facet_wrap(~ panel, scales = "free_y", nrow = 2) +
    labs(title = paste0(ind, ": trayectoria observada y proyección a ", h_final, " años"),
         subtitle = "Azul marino: observado · granate punteado: proyección. El encabezado de cada panel indica el modelo seleccionado.",
         x = NULL, y = "% del PIB",
         caption = "Fuentes: FMI-WEO (abril 2025) y CEPAL/FMI-GFS. Proyección: elaboración propia.") +
    theme_caf()

  print(g)
  ggsave(paste0("graficas/", archivos_proj[[ind]], ".png"), g,
         width = 10, height = 6, dpi = 300)
}

# --- Códigos ISO3 ---
iso3_map <- c("Brasil" = "BRA", "Chile" = "CHL", "Colombia" = "COL",
              "Costa Rica" = "CRI", "México" = "MEX", "Panamá" = "PAN")

# --- Último año observado según el FMI (columna "Estimates Start After") ---
# A partir de ese año los valores del WEO son estimación, no dato observado.
estim_desde <- weo_raw %>%
  filter(!is.na(ISO)) %>%
  distinct(ISO, `Estimates Start After`) %>%
  transmute(pais = recode(ISO, BRA = "Brasil", CHL = "Chile", COL = "Colombia",
                          CRI = "Costa Rica", MEX = "México", PAN = "Panamá"),
            ultimo_observado = as.integer(`Estimates Start After`))

knitr::kable(estim_desde,
             caption = "Último año observado por país en el WEO; los posteriores son estimación del FMI")

# --- Metadatos por indicador ---
meta_ind <- tibble::tribble(
  ~indicador,                          ~codigo,        ~unidad,        ~cobertura,          ~fuente,
  "Ingresos del gobierno general",     "GGR_NGDP",     "% del PIB",    "Gobierno general",  "FMI, World Economic Outlook, abril 2025",
  "Balance primario",                  "GGXONLB_NGDP", "% del PIB",    "Gobierno general",  "FMI, World Economic Outlook, abril 2025",
  "Deuda neta del gobierno general",   "GGXWDN_NGDP",  "% del PIB",    "Gobierno general",  "FMI, World Economic Outlook, abril 2025",
  "Gasto público en salud",            "GFS_SALUD",    "% del PIB",    "Gobierno central",  "CEPAL/FMI-GFS, gasto público por función",
  "Gasto público en pensiones",        "GFS_PENSIONES","% del PIB",    "Gobierno central",  "CEPAL/FMI-GFS, gasto público por función"
)

# --- Nota de construcción de la serie de pensiones, por país ---
nota_pensiones <- regla_pensiones %>%
  transmute(pais,
            nota_pen = if_else(incluye_enf,
              "Suma de edad avanzada y enfermedad e incapacidad",
              "Sólo edad avanzada; cota inferior del gasto en pensiones"))

# --- Bloque 1: fiscal observado / estimado ---
base_fiscal_obs <- df_fiscal %>%
  left_join(estim_desde, by = "pais") %>%
  mutate(
    tipo = if_else(anio > ultimo_observado & indicador %in%
                     c("Ingresos del gobierno general", "Balance primario",
                       "Deuda neta del gobierno general"),
                   "Estimación de la fuente", "Observado"),
    modelo = NA_character_
  ) %>%
  select(pais, anio, indicador, tipo, modelo, valor)

# --- Bloque 2: fiscal proyectado (modelos propios) ---
base_fiscal_fc <- fc_tidy %>%
  transmute(pais, anio, indicador, tipo = "Proyección propia",
            modelo, valor = media)

# --- Bloque 3: demografía (UN WPP: estimación hasta 2023, proyección después) ---
base_demog <- df_demog %>%
  mutate(tipo = if_else(periodo == "Estimación", "Observado", "Proyección de la fuente"),
         modelo = NA_character_) %>%
  select(pais, anio, indicador, tipo, modelo, valor)

meta_demog <- tibble::tribble(
  ~indicador,                                    ~codigo,     ~unidad,            ~cobertura, ~fuente,
  "Tasa global de fecundidad (hijos por mujer)", "WPP_TFR",   "hijos por mujer",  "Nacional", "UN World Population Prospects 2024, revisión mediana",
  "Razón de dependencia senil (%)",              "WPP_RDSEN", "%",                "Nacional", "UN World Population Prospects 2024, revisión mediana"
)

# --- Consolidación ---
base_analisis <- bind_rows(base_fiscal_obs, base_fiscal_fc, base_demog) %>%
  mutate(indicador = as.character(indicador)) %>%
  left_join(bind_rows(meta_ind, meta_demog), by = "indicador") %>%
  left_join(nota_pensiones, by = "pais") %>%
  mutate(
    iso3 = unname(iso3_map[pais]),
    # Nota compuesta: regla de construcción (pensiones) y/o advertencia de
    # cobertura institucional (países con seguridad social fuera del gob. central)
    nota_cobertura = if_else(
      indicador %in% c("Gasto público en salud", "Gasto público en pensiones") &
        pais %in% c("Costa Rica", "Panamá", "México"),
      "Excluye seguridad social autónoma; subestima el gasto efectivo",
      NA_character_),
    nota_construccion = if_else(indicador == "Gasto público en pensiones",
                                nota_pen, NA_character_),
    nota = case_when(
      !is.na(nota_construccion) & !is.na(nota_cobertura) ~
        paste(nota_construccion, nota_cobertura, sep = ". "),
      !is.na(nota_construccion) ~ nota_construccion,
      !is.na(nota_cobertura)    ~ nota_cobertura,
      TRUE ~ NA_character_
    ),
    valor = round(valor, 4)
  ) %>%
  transmute(
    pais, iso3, anio,
    indicador, codigo_indicador = codigo,
    tipo, modelo,
    valor, unidad,
    cobertura_institucional = cobertura,
    fuente, nota
  ) %>%
  arrange(indicador, pais, anio)

# --- Validaciones ---
stopifnot(
  !any(is.na(base_analisis$valor)),
  !any(is.na(base_analisis$iso3)),
  !any(is.na(base_analisis$codigo_indicador)),
  !any(duplicated(base_analisis[, c("pais", "anio", "indicador")]))
)

# Se escribe con readr::write_excel_csv, que genera UTF-8 CON BOM.
# El BOM es lo que permite a Excel en Windows reconocer la codificación;
# write.csv(fileEncoding = "UTF-8") no lo incluye y produce mojibake
# ("MÃ©xico" en lugar de "México") al abrir el archivo desde Excel.
readr::write_excel_csv(base_analisis, "base_analisis_P3.csv")

cat("base_analisis_P3.csv —", nrow(base_analisis), "filas,",
    ncol(base_analisis), "columnas\n\n")

count(base_analisis, indicador, tipo) %>% knitr::kable(caption = "Composición de la base")

diccionario <- tibble::tribble(
  ~Campo,                     ~Descripción,
  "pais",                     "Nombre del país",
  "iso3",                     "Código ISO 3166-1 alfa-3",
  "anio",                     "Año de referencia",
  "indicador",                "Nombre del indicador",
  "codigo_indicador",         "Código de la serie en la fuente original",
  "tipo",                     "Observado | Estimación de la fuente | Proyección de la fuente | Proyección propia",
  "modelo",                   "Especificación empleada; vacío salvo en proyección propia",
  "valor",                    "Valor del indicador",
  "unidad",                   "Unidad de medida",
  "cobertura_institucional",  "Perímetro institucional del dato",
  "fuente",                   "Fuente primaria",
  "nota",                     "Advertencia de construcción o comparabilidad, cuando aplica"
)

# --- Advertencia de uso sobre las proyecciones de gasto funcional ---
nota_uso <- tibble::tribble(
  ~Campo, ~Descripción,
  "ADVERTENCIA DE USO",
  paste(
    "Las proyecciones de gasto en salud y pensiones (tipo = 'Proyección propia')",
    "parten de un último dato observado en 2020 en cuatro de los seis países, año",
    "afectado por el choque sanitario. Dado que la ventana de validación del modelo",
    "(últimos cuatro años) contiene dicho choque, la selección favorece",
    "especificaciones de tendencia no amortiguada que extrapolan el incremento de",
    "2020 como si fuera estructural. Esto es particularmente relevante en tres",
    "series: gasto en salud de Chile (6.03 en 2020 a 12.38 en 2030), gasto en",
    "pensiones de México (3.01 a 5.30) y gasto en salud de México (1.24 a 1.65),",
    "cuyas trayectorias exceden el rango histórico observado. Estas proyecciones",
    "deben interpretarse como cota superior de un escenario inercial, no como",
    "estimación central. Los agregados fiscales del WEO no presentan esta",
    "limitación por disponer de datos hasta 2024."
  )
)

diccionario <- bind_rows(diccionario, nota_uso)

knitr::kable(diccionario, caption = "Diccionario de variables")

exportar_tex(diccionario, "anexo_diccionario_base.tex", alinear = c("l", "l"))

readr::write_excel_csv(diccionario, "base_analisis_P3_diccionario.csv")

# Control automático: detecta proyecciones que exceden el rango histórico
# observado en más de medio rango. Reproduce la revisión que originó la
# advertencia de uso; si al reejecutar aparecen series nuevas, deben añadirse
# a esa nota o corregirse la especificación.
control_rango <- base_analisis %>%
  filter(tipo != "Proyección de la fuente") %>%
  group_by(indicador, pais) %>%
  summarise(
    hist_min  = min(valor[tipo != "Proyección propia"]),
    hist_max  = max(valor[tipo != "Proyección propia"]),
    ultimo    = valor[tipo != "Proyección propia"][which.max(anio[tipo != "Proyección propia"])],
    fin_proy  = if (any(tipo == "Proyección propia"))
                  valor[tipo == "Proyección propia"][which.max(anio[tipo == "Proyección propia"])]
                else NA_real_,
    modelo    = first(na.omit(modelo)),
    .groups = "drop"
  ) %>%
  filter(!is.na(fin_proy)) %>%
  mutate(
    rango  = hist_max - hist_min,
    excede = fin_proy > hist_max + 0.5 * rango | fin_proy < hist_min - 0.5 * rango
  )

alertas <- filter(control_rango, excede)

if (nrow(alertas)) {
  warning("Proyecciones fuera del rango histórico: ", nrow(alertas), " serie(s).")
  alertas %>%
    transmute(Indicador = indicador, País = pais, Modelo = modelo,
              `Hist. mín` = round(hist_min, 2), `Hist. máx` = round(hist_max, 2),
              `Último obs.` = round(ultimo, 2), `Fin proyección` = round(fin_proy, 2)) %>%
    knitr::kable(caption = "ALERTA: proyecciones que exceden el rango histórico observado")
} else {
  cat("Ninguna proyección excede el rango histórico observado.\n")
}

cat("Salidas generadas:\n",
    "  graficas/                     figuras del documento y del anexo\n",
    "  tablas/                       fragmentos LaTeX\n",
    "  base_analisis_P3.csv          base consolidada\n",
    "  base_analisis_P3_diccionario.csv  diccionario de variables\n")

grid_quiebres <- function(ind) {
  idx <- which(claves$indicador == ind)
  par(mfrow = c(2, 3), oma = c(0, 0, 2.3, 0), mar = c(3, 3, 2, 0.8),
      mgp = c(1.8, 0.6, 0), cex.axis = 0.75)
  for (i in idx) {
    y <- series_list[[i]]
    if (length(y) < 20) {
      plot.new(); title(main = paste0(claves$pais[i], " (n<20)"), cex.main = 0.9)
      next
    }
    fs <- tryCatch(Fstats(y ~ 1), error = function(e) NULL)
    if (is.null(fs)) { plot.new(); title(main = paste0(claves$pais[i], " (s/d)")); next }
    plot(fs, main = claves$pais[i], cex.main = 0.9, col = "#1B3A5C")
    bp <- tryCatch(breakpoints(y ~ 1), error = function(e) NULL)
    fechas <- if (!is.null(bp)) breakdates(bp) else NA
    if (!all(is.na(fechas))) abline(v = fechas, col = "#8C1D40", lty = 2, lwd = 1.3)
  }
  mtext(paste0("Prueba F de quiebre estructural — ", ind),
        outer = TRUE, cex = 1, font = 2, col = "#1B3A5C")
  par(mfrow = c(1, 1))
}

slug <- function(x) gsub("(^_|_$)", "", gsub("[^a-z0-9]+", "_",
       tolower(iconv(x, from = "", to = "ASCII//TRANSLIT"))))

for (ind in levels(df_fiscal$indicador)) {
  grid_quiebres(ind)
  png(paste0("graficas/anexo_quiebres_", slug(ind), ".png"),
      width = 8, height = 4.5, units = "in", res = 300)
  grid_quiebres(ind); dev.off()
}

tab_quiebres <- map_dfr(seq_len(nrow(claves)), function(i) {
  y <- series_list[[i]]
  base <- tibble(Indicador = as.character(claves$indicador[i]),
                 País = claves$pais[i], n = length(y))

  if (length(y) < 20) {
    return(mutate(base, `supF (p)` = NA_real_, Quiebres = "n < 20 (no evaluado)"))
  }

  fs <- tryCatch(Fstats(y ~ 1), error = function(e) NULL)
  p_f <- if (!is.null(fs)) tryCatch(sctest(fs)$p.value, error = function(e) NA_real_) else NA_real_
  bp  <- tryCatch(breakpoints(y ~ 1), error = function(e) NULL)
  fechas <- if (!is.null(bp)) breakdates(bp) else NA

  mutate(base,
         `supF (p)` = round(p_f, 3),
         Quiebres = if (all(is.na(fechas))) "Sin quiebres"
                    else paste(round(fechas, 0), collapse = ", "))
})

knitr::kable(tab_quiebres,
             caption = "Prueba supF de constancia de parámetros y fechas de quiebre (Bai-Perron, criterio BIC)")

exportar_tex(tab_quiebres, "anexo_tab_quiebres.tex")

tab_quiebres %>%
  filter(!is.na(`supF (p)`)) %>%
  summarise(
    series_evaluadas   = n(),
    rechaza_constancia = sum(`supF (p)` < 0.05),
    con_quiebre_BP     = sum(Quiebres != "Sin quiebres")
  )

# Cifras citadas en el texto LaTeX (verificación al recompilar)
list(
  series_evaluadas   = nrow(resultados),
  modelo_predominante = frecuencia_modelos$Modelo[1],
  n_predominante     = frecuencia_modelos$`Series ganadas`[1],
  ljung_ok           = sum(resultados$LjungBox > 0.05, na.rm = TRUE),
  ljung_evaluables   = sum(!is.na(resultados$LjungBox)),
  mase_menor_1       = sum(resultados$MASE < 1, na.rm = TRUE)
)