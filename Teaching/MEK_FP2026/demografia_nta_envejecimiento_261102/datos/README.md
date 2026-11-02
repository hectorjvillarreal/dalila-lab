# datos/

`prep_p1.py` genera con el entorno `dalila` los datos de las gráficas de la Parte 1.

- `p1_tasas_mex.csv`: natalidad, mortalidad y TGF de México, 1950–2023 (WPP 2024).
- `p1_dependencia.csv`: relación de dependencia total, América Latina y el Caribe y México, 1950–2050 (WPP 2024). Lo posterior a 2024 es proyección.
- `p1_piramides.csv` y `p1_piramide_*.tex`: pirámides de México. 1970, WPP 2024; 2020, Censo de INEGI; 2050, escenario central del motor nacional (`GrandPlan/DFD/outputs/public/2026-10_population_mex_bra_usa/projection_national.py`, TGF 1.23). El guion no toca los resultados del motor.
- `p1_velocidad.csv`: año en que 65+ cruza 10 % y 20 % (WPP 2024). Para Francia y Suecia, 1950 es cota: ya tenían más de 10 %.

## Parte 2

- `baja_ntaccounts.sh`: baja perfiles de la base pública de ntaccounts.org. `ntaccounts_perfiles.csv` y `ntaccounts_documentacion.csv` son la salida (descargados el 1 de noviembre de 2026).
- `prep_p2.py`: normaliza los perfiles por el ingreso laboral medio de 30–49 años y escribe `p2_*.csv`. El reparto del déficit de 65+ pondera con población de WPP 2024.

## Parte 3

- `prep_p3.py`: 65+ por regiones (WPP 2024), razón de sostenimiento con pesos fijos, aritmética de perfiles fijos por población, perfil de salud de México 2014 y mujeres de 45–64 por persona de 80+. Escribe `p3_*.csv`. Las poblaciones de 2025 y 2050 de México vienen del motor nacional; las demás, de WPP 2024 repartida en partes iguales dentro de cada grupo quinquenal.
