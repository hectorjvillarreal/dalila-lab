"""Construye los tres .csv que faltaban: ingresos energéticos (cap. 3), detalle de
Pemex y CFE por el lado del gasto (cap. 9) y la tríada de NTA (cap. 13).

Se escriben antes de declarar ningún capítulo no redactable, porque la regla es
agotar rutas antes de declarar ausencias.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fiscus import an, mdp, real, dif_real, dif_nominal, emitir

DEF = 1.043
ENC = ["concepto", "mdp_2024", "mdp_2025", "dif_nominal_mdp", "dif_real_mdp", "var_real_pct"]

def f(etq, v24, v25):
    v24, v25 = round(v24, 1), round(v25, 1)
    return [etq, v24, v25, round(v25 - v24, 1), round(v25 - v24 * DEF, 1),
            round(100 * (v25 / (v24 * DEF) - 1), 1) if v24 else ""]

# ============================================ C3.1 INGRESOS ENERGETICOS ====
# Fuente: Ley de Ingresos aprobada 2024 y 2025, articulo 1o. Se separan las tres
# vias por las que el sector energetico entra al presupuesto, que es la pregunta
# del capitulo: renta petrolera via el Fondo Mexicano del Petroleo, ingreso propio
# de las empresas, e impuesto especifico a la actividad extractiva.
filas = [
    f("Transferencias del Fondo Mexicano del Petroleo (ordinarias)", 277774.3, 279766.8),
    f("Ingreso propio de Petroleos Mexicanos", 769805.6, 860868.2),
    f("Ingreso propio de la Comision Federal de Electricidad", 446951.3, 539145.6),
    f("Impuesto por la actividad de exploracion y extraccion de hidrocarburos", 7811.0, 7140.1),
    f("SUMA de las cuatro vias", 277774.3 + 769805.6 + 446951.3 + 7811.0,
      279766.8 + 860868.2 + 539145.6 + 7140.1),
]
emitir("energia_ingresos.csv", filas, ENC,
       {"cuadro": "C3.1", "documento": "LIF aprobada 2024 y 2025",
        "ubicacion": "articulo 1o., renglones 9.97.01, 7.72.01, 7.72.02 y 1.18.01",
        "tier": "oficial_primaria",
        "nota": "Aprobado contra aprobado. Deflactor 1.043. dif_real en pesos de 2025. "
                "PERIMETRO: no es 'ingresos petroleros' del CGPE, que consolida distinto; "
                "es la entrada bruta del sector energetico al articulo 1o. por sus cuatro "
                "vias, cada una nombrada. La suma NO se compara con el agregado del CGPE "
                "sin declarar el neteo."})

# =================================== C9.1b PEMEX Y CFE POR EL LADO DEL GASTO ====
e24, e25 = an(2024, "ent_pp"), an(2025, "ent_pp")
p24, p25 = an(2024, "gf_pp"), an(2025, "gf_pp")
filas = []
for pref, nom in (("TYY", "Pemex"), ("TVV", "CFE")):
    s24 = e24[e24.ENTIDAD.astype(str).str.startswith(pref)]
    s25 = e25[e25.ENTIDAD.astype(str).str.startswith(pref)]
    filas.append(f(f"{nom}: gasto total (bruto)", mdp(s24["IMPORTE"].sum()), mdp(s25["IMPORTE"].sum())))
    for etq, cond in [("pensiones (tipo de gasto 4)", lambda d: d[d.TG == 4]),
                      ("obra publica (capitulo 6000)", lambda d: d[d.PE.astype(str).str.startswith("6")]),
                      ("servicios personales (capitulo 1000)", lambda d: d[d.PE.astype(str).str.startswith("1")]),
                      ("deuda publica (capitulo 9000)", lambda d: d[d.PE.astype(str).str.startswith("9")])]:
        filas.append(f(f"  {nom}: {etq}", mdp(cond(s24)["IMPORTE"].sum()), mdp(cond(s25)["IMPORTE"].sum())))
# Lo que el Gobierno Federal les pone por el Ramo 18.
r18_24 = p24[p24.RAMO.astype(str).str.startswith("18")]
r18_25 = p25[p25.RAMO.astype(str).str.startswith("18")]
filas.append(f("Ramo 18 Energia (aportacion del Gobierno Federal)",
               mdp(r18_24["IMPORTE"].sum()), mdp(r18_25["IMPORTE"].sum())))
emitir("energia_empresas.csv", filas, ENC,
       {"cuadro": "C9.1b", "documento": "Analiticos del PEF aprobado 2024 y 2025",
        "ubicacion": "entidades TYY y TVV; ramo 18 del Gobierno Federal",
        "tier": "oficial_primaria",
        "nota": "PEF aprobado, no proyecto. Bruto. La pregunta del capitulo es por que via "
                "entra el dinero a las empresas: aportacion del Ramo 18, ingreso propio "
                "(ver C3.1) o deuda. dif_real en pesos de 2025."})

# ================================================= C13.1 TRIADA DE NTA ====
# Sintesis de los tres verticies con los mismos perimetros que sus capitulos.
g24, g25 = an(2024, "gf_f"), an(2025, "gf_f")
ef24, ef25 = an(2024, "ent_f"), an(2025, "ent_f")
PIB24, PIB25 = 34374000.0, 36166400.0

def pens_cons(gf, en):
    d = gf[(gf.TG == 4) & (~gf.PE.astype(str).str.startswith("45203"))]["IMPORTE"].sum()
    return d + en[en.TG == 4]["IMPORTE"].sum()

pen24, pen25 = mdp(pens_cons(p24, e24)), mdp(pens_cons(p25, e25))
NOCONTRIB = ["S176", "S286", "U316"]
nc24 = mdp(p24[p24.CLAVE_PP.isin(NOCONTRIB)]["IMPORTE"].sum())
nc25 = mdp(p25[p25.CLAVE_PP.isin(NOCONTRIB)]["IMPORTE"].sum())
sal24 = mdp(g24[(g24.F == 2) & (g24.FN == 3)]["IMPORTE"].sum() +
            ef24[(ef24.F == 2) & (ef24.FN == 3)]["IMPORTE"].sum())
sal25 = mdp(g25[(g25.F == 2) & (g25.FN == 3)]["IMPORTE"].sum() +
            ef25[(ef25.F == 2) & (ef25.FN == 3)]["IMPORTE"].sum())
edu24 = mdp(g24[(g24.F == 2) & (g24.FN == 5)]["IMPORTE"].sum())
edu25 = mdp(g25[(g25.F == 2) & (g25.FN == 5)]["IMPORTE"].sum())

filas = []
for nom, v24, v25, perfil, direccion, denominador, horizonte in [
    ("Pensiones contributivas (clasificacion economica)", pen24, pen25,
     "vejez", "la transicion lo empuja al alza", "poblacion de 65 anos y mas",
     "SI: el CGPE proyecta pensiones y jubilaciones a 2030 (4.5 a 4.8 % del PIB)"),
    ("Pensiones no contributivas (ramo 20)", nc24, nc25,
     "vejez y discapacidad", "la transicion lo empuja al alza", "poblacion beneficiaria",
     "NO: el paquete no proyecta el padron"),
    ("Salud (funcion 2.3, GF + entidades, bruta)", sal24, sal25,
     "todo el ciclo, con joroba en los extremos", "al alza por envejecimiento",
     "poblacion por afiliacion", "NO: ninguna proyeccion por funcion"),
    ("Educacion (funcion 2.5, GF, bruta)", edu24, edu25,
     "juventud", "LA TRANSICION LO EMPUJA A LA BAJA", "matricula, no poblacion total",
     "NO: el paquete no declara matricula, cobertura, planteles ni docentes"),
]:
    filas.append([nom, v24, v25,
                  round(100 * v24 / PIB24, 2), round(100 * v25 / PIB25, 2),
                  round(100 * (v25 / (v24 * DEF) - 1), 1),
                  perfil, direccion, denominador, horizonte])
emitir("triada_nta.csv", filas,
       ["vertice", "mdp_2024", "mdp_2025", "pct_pib_2024", "pct_pib_2025", "var_real_pct",
        "perfil_de_edad", "direccion_demografica", "denominador_que_le_corresponde",
        "horizonte_en_el_paquete"],
       {"cuadro": "C13.1", "documento": "Analiticos del PEF aprobado; CGPE 2025",
        "ubicacion": "perimetros de los capitulos 5, 6 y 7 de este documento",
        "tier": "oficial_primaria",
        "nota": "Los tres verticies con los MISMOS perimetros de sus capitulos, para que "
                "la comparacion no sea entre objetos distintos. La ultima columna es el "
                "hallazgo: el paquete tiene horizonte demografico donde la demografia "
                "presiona al alza y no lo tiene donde presiona a la baja."})

print("emitidos: energia_ingresos, energia_empresas, triada_nta")
for r in filas:
    print(f"   {r[0][:52]:52s} {r[1]:>11,.1f} -> {r[2]:>11,.1f}  {r[3]:>5} -> {r[4]:>5} % PIB  real {r[5]:>6}")
