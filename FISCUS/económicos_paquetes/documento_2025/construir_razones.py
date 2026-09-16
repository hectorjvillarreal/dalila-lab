"""Construye datos/razones_estructurales.csv, las comparaciones de la casa.

Son lo que hace que el documento sea de ITED y no una imitación del género. Cada
una con numerador, denominador, fuente de cada lado y perímetro declarado. Nunca
una línea híbrida: aprobado contra aprobado en toda la serie.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fiscus import an, mdp, emitir

p24, p25 = an(2024, "gf_pp"), an(2025, "gf_pp")
e24, e25 = an(2024, "ent_pp"), an(2025, "ent_pp")
g24, g25 = an(2024, "gf_f"), an(2025, "gf_f")
ef24, ef25 = an(2024, "ent_f"), an(2025, "ent_f")

def ent(d, pref, tg=None, f=None, fn=None):
    s = d[d.ENTIDAD.astype(str).str.startswith(pref)]
    if tg is not None: s = s[s.TG == tg]
    if f is not None:  s = s[(s.F == f) & (s.FN == fn)]
    return s["IMPORTE"].sum()

def pens_cons(gf, en):
    directo = gf[(gf.TG == 4) & (~gf.PE.astype(str).str.startswith("45203"))]["IMPORTE"].sum()
    return directo + en[en.TG == 4]["IMPORTE"].sum()

V = {}
V["pens_cons_24"], V["pens_cons_25"] = mdp(pens_cons(p24, e24)), mdp(pens_cons(p25, e25))
V["imss_pens_24"], V["imss_pens_25"] = mdp(ent(e24, "GYR", tg=4)), mdp(ent(e25, "GYR", tg=4))
V["isss_pens_24"], V["isss_pens_25"] = mdp(ent(e24, "GYN", tg=4)), mdp(ent(e25, "GYN", tg=4))
V["imss_sal_24"] = mdp(ent(ef24, "GYR", f=2, fn=3)); V["imss_sal_25"] = mdp(ent(ef25, "GYR", f=2, fn=3))
V["isss_sal_24"] = mdp(ent(ef24, "GYN", f=2, fn=3)); V["isss_sal_25"] = mdp(ent(ef25, "GYN", f=2, fn=3))
V["educ_24"] = mdp(g24[(g24.F == 2) & (g24.FN == 5)]["IMPORTE"].sum())
V["educ_25"] = mdp(g25[(g25.F == 2) & (g25.FN == 5)]["IMPORTE"].sum())

# Pensiones no contributivas del Ramo 20 Bienestar, por CLAVE y no por nombre.
# Trampa que costo una vuelta: el programa se llama "Personas ADULTAS Mayores", en
# femenino, y un patron con "Adultos Mayores" no lo encuentra. Se usan las claves.
#   S176 Pension para el Bienestar de las Personas Adultas Mayores
#   S286 Pension para el Bienestar de las Personas con Discapacidad Permanente
#   U316 Pension Mujeres Bienestar  <- NUEVA en 2025, 15,000.0 mdp
NOCONTRIB = ["S176", "S286", "U316"]
def pbien(d):
    s = d[d.RAMO.astype(str).str.startswith("20")]
    return s[s.CLAVE_PP.isin(NOCONTRIB)].groupby("CLAVE_PP")["IMPORTE"].sum()
V["nocontrib_24"] = mdp(pbien(p24).sum()); V["nocontrib_25"] = mdp(pbien(p25).sum())

# Fuentes oficiales que no salen de los analiticos.
LIF = {"impuestos_24": 4942030.3, "impuestos_25": 5297812.9,
       "cuotas_22": 411852.5, "cuotas_23": 470845.4,
       "cuotas_24": 535254.7, "cuotas_25": 603077.9}
DEC = {"oblig_pens_24": 7327588.8, "oblig_pens_25": 7684111.9}
CGPE = {"cf_24": 1263994.1, "cf_25": 1388373.6, "trib_24": 4941540.8, "trib_25": 5296426.4,
        "shrfsp_24": 16787906.1, "shrfsp_25": 18591005.5}
PREV = {"imss_pens_22": 636461.8, "imss_pens_23": 750252.1}

r = lambda a, b, n=3: round(a / b, n) if b else ""
filas = []
def fila(cap, nombre, serie, num, den, nota):
    filas.append([cap, nombre, num, den] + serie + [nota])

fila("2", "Impuestos / gastos obligatorios con pensiones",
     ["0.671", "0.674", "", r(LIF["impuestos_24"], DEC["oblig_pens_24"]),
      r(LIF["impuestos_25"], DEC["oblig_pens_25"])],
     "LIF art. 1o. numeral 1", "DEC Anexo 3",
     "Serie 2021-2022 de la corrida 2022. 2023 no calculado.")
fila("2", "Impuestos + cuotas IMSS / gastos obligatorios con pensiones",
     ["0.743", "0.745", "", r(LIF["impuestos_24"] + LIF["cuotas_24"], DEC["oblig_pens_24"]),
      r(LIF["impuestos_25"] + LIF["cuotas_25"], DEC["oblig_pens_25"])],
     "LIF art. 1o. numerales 1 y 2", "DEC Anexo 3", "Segunda linea de la misma razon.")
fila("4", "Pensiones y jubilaciones + costo financiero / impuestos",
     ["", "", "RETIRADO", r(V["pens_cons_24"] + CGPE["cf_24"], LIF["impuestos_24"]),
      r(V["pens_cons_25"] + CGPE["cf_25"], LIF["impuestos_25"])],
     "clasificacion economica + CGPE", "LIF art. 1o. numeral 1",
     "El punto de 0.60 para 2023 se RETIRA: no se reproduce con ninguna de las dos "
     "definiciones de pensiones (dan 0.583 y 0.522). La serie arranca en 2024 con la "
     "definicion declarada aqui. Detalle en la bitacora de la corrida 2024.")
fila("5", "Pensiones IMSS / cuotas IMSS (serie aprobada)",
     ["", r(PREV["imss_pens_22"], LIF["cuotas_22"]), r(PREV["imss_pens_23"], LIF["cuotas_23"]),
      r(V["imss_pens_24"], LIF["cuotas_24"]), r(V["imss_pens_25"], LIF["cuotas_25"])],
     "PEF aprobado, tipo de gasto 4 del IMSS", "LIF aprobada art. 1o. renglon 2.22",
     "Aprobado contra aprobado en los cuatro puntos. La serie ex ante (1.31 en 2020, "
     "1.46 en 2021) esta congelada: la exposicion de motivos del PPEF no existe desde 2022.")
fila("6", "Gasto en salud del IMSS / cuotas IMSS",
     ["0.85", "", "", r(V["imss_sal_24"], LIF["cuotas_24"]), r(V["imss_sal_25"], LIF["cuotas_25"])],
     "funcion 2.3 Salud del IMSS", "LIF aprobada art. 1o. renglon 2.22",
     "El punto de 2021 viene de la corrida 2021 y usa la misma construccion.")
fila("6", "Pensiones IMSS+ISSSTE / salud IMSS+ISSSTE",
     ["2.11", "", "", r(V["imss_pens_24"] + V["isss_pens_24"], V["imss_sal_24"] + V["isss_sal_24"]),
      r(V["imss_pens_25"] + V["isss_pens_25"], V["imss_sal_25"] + V["isss_sal_25"])],
     "tipo de gasto 4 de IMSS e ISSSTE", "funcion 2.3 Salud de IMSS e ISSSTE",
     "Dentro de los institutos, cuanto pesa la pension contra el servicio.")
fila("7", "Funcion Educacion / pensiones y jubilaciones",
     ["", "", "0.709", r(V["educ_24"], V["pens_cons_24"]), r(V["educ_25"], V["pens_cons_25"])],
     "funcion 2.5 Educacion, GF bruto", "pensiones y jubilaciones, clasificacion economica",
     "Las dos transferencias de los extremos opuestos del ciclo de vida.")
fila("7", "Funcion Educacion / pensiones totales (con no contributivas)",
     ["", "", "0.558", r(V["educ_24"], V["pens_cons_24"] + V["nocontrib_24"]),
      r(V["educ_25"], V["pens_cons_25"] + V["nocontrib_25"])],
     "funcion 2.5 Educacion, GF bruto",
     "pensiones y jubilaciones + adultos mayores + personas con discapacidad",
     "Segunda linea de la comparacion adoptada para educacion.")
fila("12", "Costo financiero / impuestos",
     ["", "0.20", "0.23", r(CGPE["cf_24"], LIF["impuestos_24"]), r(CGPE["cf_25"], LIF["impuestos_25"])],
     "CGPE, costo financiero del sector publico", "LIF art. 1o. numeral 1", "")
fila("12", "SHRFSPF / impuestos, en anios de recaudacion",
     ["", "3.6", "3.4", r(CGPE["shrfsp_24"], LIF["impuestos_24"], 2),
      r(CGPE["shrfsp_25"], LIF["impuestos_25"], 2)],
     "CGPE, SHRFSPF", "LIF art. 1o. numeral 1",
     "Complemento del marco autoral (Cantu, Ramones y Villarreal 2016).")

emitir("razones_estructurales.csv", filas,
       ["capitulo", "razon", "numerador", "denominador",
        "2021", "2022", "2023", "2024", "2025", "nota"],
       {"cuadro": "razones de la casa, en el capitulo que indica la primera columna",
        "documento": "Analiticos del PEF aprobado; LIF aprobada; DEC Anexo 3; CGPE 2025",
        "ubicacion": "ver columnas numerador y denominador",
        "tier": "oficial_primaria",
        "nota": "Aprobado contra aprobado en toda la serie. Ninguna linea hibrida. "
                "Los puntos anteriores a 2024 vienen de las corridas 2021-2023 y llevan "
                "su origen en la nota de cada fila."})

print("componentes:")
for k in sorted(V): print(f"  {k:16s} {V[k]:>12,.1f}")
print("\nemitido: razones_estructurales")
