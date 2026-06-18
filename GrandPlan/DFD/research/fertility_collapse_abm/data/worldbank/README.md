---
type: corpus_entry
tier: data_source
project_scope: [DFD]
authors: [World Bank]
year: 2026
title: "World Bank WDI backbone — fertility, population, migration, Calles-Vogl covariates (5 countries)"
venue: "World Bank World Development Indicators v2 API"
doi: "https://api.worldbank.org/v2"
date_added: 2026-06-17
added_by: ClaudeCode
endorsed_by:
build_instruction: "STAGE1_data_acquisition_fertility_collapse.md"
---

# World Bank WDI backbone

Tidy long format: `year, value, source, methodology_flag, provisional_flag`. Long consistent
historical series (1960–2024) + structural covariates. Per-file inventory in `_fetch_log.csv`.

**Forensic caveat:** WB fertility/vital series are WPP-derived, model-smoothed, and lagged — they
do NOT capture the 2020–2024 collapse tail (Colombia WB 2024 = 1.63 vs DANE 1.1). Use as backbone
and for **covariate inputs** only; the collapse tail comes from `../national/`.

**Identification discipline:** the covariate files here (urban_pct, female_lfp_pct, agri_emp_pct,
agri_va_pct_gdp, fem_attain_*) are the ABM's calibration **inputs** — acquired strictly separately
from the TFR output series and never adjusted to fit TFR. The WB tfr/crude_birth_rate files are the
historical backbone only; the authoritative TFR *output* series for matching are the national ones.
