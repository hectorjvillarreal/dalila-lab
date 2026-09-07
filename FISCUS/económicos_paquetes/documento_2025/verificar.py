"""verificar.py — cierre contable de los datos.

Doble propósito. (1) Es el criterio 3 de la rúbrica, cierre contable, aplicado a
nuestras propias cifras y no a las de otro. (2) Es el control de calidad de la
LECTURA DE IMAGEN: el CGPE 2025 no tiene capa de texto, así que sus cifras se
leyeron de páginas renderizadas. Si una identidad no cierra al mdp, lo más
probable es un dígito mal leído, no un error de la SHCP.

Se corre después de cada cambio en datos/.
"""
import sys, os, csv
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
DATOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "datos")

def cargar(nombre, clave):
    with open(os.path.join(DATOS, nombre), newline="", encoding="utf-8") as f:
        return {r[clave]: r for r in csv.DictReader(f)}

def num(x):
    try:
        return float(str(x).replace(",", ""))
    except ValueError:
        return float("nan")

fallos, pruebas = [], 0

def chk(nombre, izq, der, tol=0.15):
    global pruebas
    pruebas += 1
    if abs(izq - der) > tol:
        fallos.append(f"  FALLA  {nombre}: {izq:,.1f} vs {der:,.1f}  (dif {izq-der:,.1f})")
    else:
        print(f"  ok     {nombre}: {izq:,.1f}")

# ------------------------------------------------- identidades de II.6, 2025 ---
ff = cargar("finanzas_publicas.csv", "concepto")
g = lambda c, col="mdp_2025": num(ff[c][col])

print("Cierre contable, CGPE 2025 Anexo II.6, columna 2025 (mdp):")
chk("RFSP = extrapresupuestarios + balance presupuestario",
    g("RFSP"), g("Recursos financieros extrapresupuestarios") + g("Balance presupuestario"))
chk("Balance presupuestario = ingresos - gasto neto pagado",
    g("Balance presupuestario"), g("Ingresos presupuestarios") - g("Gasto neto pagado"))
chk("Gasto neto = programable pagado + no programable",
    g("Gasto neto pagado"), g("Gasto programable pagado") + g("Gasto no programable"))
chk("No programable = costo financiero + participaciones + Adefas",
    g("Gasto no programable"), g("Costo financiero") + g("Participaciones") + g("Adefas"))
chk("Balance primario = balance presupuestario + costo financiero",
    g("Balance primario presupuestario"), g("Balance presupuestario") + g("Costo financiero"))
chk("Programable devengado = pagado - diferimiento",
    g("Gasto programable devengado"), g("Gasto programable pagado") - g("Diferimiento de pagos"))
chk("Ingresos = petroleros + no petroleros",
    g("Ingresos presupuestarios"), g("Ingresos petroleros") + g("Ingresos no petroleros"))
chk("No petroleros = Gobierno Federal + organismos y empresas",
    g("Ingresos no petroleros"), g("Gobierno Federal (no petroleros)") + g("Organismos y empresas"))
chk("Gobierno Federal = tributarios + no tributarios",
    g("Gobierno Federal (no petroleros)"), g("Tributarios") + g("No tributarios"))

# ------------------------------------- razones a PIB contra el PIB declarado ---
mm = cargar("macro_marco.csv", "variable")
PIB25 = num(mm["PIB nominal (miles de millones de pesos)"]["proyecto_2025"]) * 1000.0
print(f"\nRazones a PIB con el PIB nominal declarado de 2025 ({PIB25:,.1f} mdp):")
for concepto, publicado in [("Ingresos presupuestarios", 22.3), ("Gasto neto pagado", 25.5),
                            ("Gasto programable pagado", 17.8), ("Costo financiero", 3.8),
                            ("Participaciones", 3.7), ("SHRFSP", 51.4),
                            ("Balance presupuestario", -3.2), ("RFSP", -3.9),
                            ("Balance primario presupuestario", 0.6)]:
    pruebas += 1
    calc = round(100.0 * g(concepto) / PIB25, 1)
    if abs(calc - publicado) > 0.05:
        fallos.append(f"  FALLA  {concepto} % PIB: calculado {calc} vs publicado {publicado}")
    else:
        print(f"  ok     {concepto}: {calc} % del PIB")

# ------------------------- coherencia entre los dos anexos, II.6 contra III.2 ---
pf = cargar("perspectivas_2024_2030.csv", "concepto")
print("\nCoherencia entre el Anexo II.6 (p. 82) y el Anexo III.2 (p. 85), % del PIB 2025:")
pares = [("RFSP", "I. RFSP"), ("Balance presupuestario", "III. Balance presupuestario"),
         ("Ingresos presupuestarios", "III.A Ingresos presupuestarios"),
         ("Gasto neto pagado", "III.B Gasto neto pagado"),
         ("Gasto programable pagado", "Gasto programable pagado"),
         ("Costo financiero", "Costo financiero"), ("Participaciones", "Participaciones"),
         ("SHRFSP", "SHRFSP"), ("Balance primario presupuestario", "IV. Balance primario")]
for a, b in pares:
    pruebas += 1
    va, vb = num(ff[a]["pib_2025"]), num(pf[b]["2025"])
    if abs(va - vb) > 0.05:
        fallos.append(f"  FALLA  {a}: II.6 dice {va}, III.2 dice {vb}")
    else:
        print(f"  ok     {a}: {va}")

# ------------------------------------ el marco macro repetido en dos anexos ---
mp = cargar("macro_medianoplazo.csv", "variable")
print("\nCoherencia entre el Anexo II.5 (p. 81) y el Anexo III.1 (p. 84), 2024 y 2025:")
for var in ["PIB nominal (miles de millones de pesos)", "Deflactor del PIB (%)",
            "Inflacion dic/dic (%)", "Inflacion promedio (%)", "Tipo de cambio promedio",
            "Cetes 28 nominal promedio (%)", "Petroleo, precio promedio (dls/barril)",
            "Plataforma de produccion (mbd)", "Plataforma de exportacion (mbd)"]:
    var_mp = var.replace("Deflactor del PIB (%)", "Deflactor del PIB promedio (%)")
    if var not in mm or var_mp not in mp:
        continue
    for col_a, col_b, etiq in [("estimado_2024", "2024", "2024 est."), ("proyecto_2025", "2025", "2025")]:
        pruebas += 1
        va, vb = num(mm[var][col_a]), num(mp[var_mp][col_b])
        if va != va or vb != vb:
            pruebas -= 1
            continue
        if abs(va - vb) > 0.051:
            fallos.append(f"  FALLA  {var} {etiq}: II.5 dice {va}, III.1 dice {vb}")
print(f"  {pruebas} pruebas corridas en total")

print("\n" + "=" * 62)
if fallos:
    print(f"{len(fallos)} FALLAS de {pruebas} pruebas:")
    for f_ in fallos:
        print(f_)
    sys.exit(1)
print(f"Las {pruebas} pruebas cierran. Ninguna identidad falla.")
