# `cuna_legal.py`

Sección 1.5: contribuciones obligatorias sobre la nómina por nivel de salario, en 2026 y 2030. Mide incidencia legal, no incidencia económica.

- **Columnas:** (a) ley vigente; (b) sin el 5 % del Infonavit y con 2 % del nuevo seguro; (c) = (b) con la cuota fija del SEM (20.40 % de la UMA) sustituida por la tasa D2 de 3.467 % del salario.
- **Componentes patronales:** cuota fija, excedente, prestaciones en dinero, GMP, IV, RT (1.9078 % en v1.1, Cuadro A.3; 1.80 % en la regresión v1.0), GPS, Retiro, cesantía y vejez (calendario del DOF 16-12-2020), Infonavit, nuevo seguro y, en el salario mínimo, la cuota obrera a cargo del patrón (art. 36 LSS).
- **Por separado:** las cuotas obreras y la aportación federal (cuota fija, PD, GMP, IV y cuota social por tramo), y la cuña legal total.
- **Escalón:** el nivel 1.01 SM se reporta con dos lecturas, por UMA y primer tramo tras el mínimo.
- **Verificaciones 3.5 y 7.5:** (b) = (a) − 3; tasas de cesantía y vejez iguales a la tabla de 1.5 y, en 2030, al art. 168 fr. II a). **7.1:** con RT de 1.80 % reproduce la tabla de la v1.0.
- **Lectura agregada (v1.1, 3.4):** registra (c) − (a) en el mínimo, el promedio y 25 UMA.
- **Salida:** `tablas/cuna_legal_por_salario.csv`
- **Instrucciones:** `..._build_v1.0`, `20261018_BDH_N13_experimento2-seguro-salud-cuidados_build_v1.1`
