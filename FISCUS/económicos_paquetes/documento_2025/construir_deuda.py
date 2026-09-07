"""Construye los .csv del capítulo 12: techos, y la descomposición de cuatro
variables del cambio de la razón SHRFSPF/PIB.

La descomposición no existe en el género. Es la aportación propia del capítulo y
por eso lleva su propia prueba de aceptación antes de aplicarse a 2025.

Marco:  d_t = d_{t-1}/(1+n) + rfspf + fx + otros,  con  n = (1+g)(1+pi) - 1
Reparto del efecto denominador, con la convención declarada de la casa:
    crecimiento  = -d * g / (1+n)
    inflación    = -d * pi * (1+g) / (1+n)
y, por separado, la compensación por inflación que el sector público PAGA y que
viaja dentro del costo financiero y de las adecuaciones a registros:
    compensación = +d * pi / (1+n)
de modo que el efecto NETO de la inflación es la suma de los dos, y no el primero
solo. Ese fue el hallazgo de la corrida 2023 y es lo que separa este marco del de
manual.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fiscus import emitir

def descomponer(d_prev, d_t, rfspf, g, pi, deuda_externa_pp, apreciacion):
    """Todo en puntos del PIB salvo g, pi y apreciacion, que son tasas."""
    n = (1 + g) * (1 + pi) - 1
    ef_g = -d_prev * g / (1 + n)
    ef_pi = -d_prev * pi * (1 + g) / (1 + n)
    compensacion = d_prev * pi / (1 + n)
    ef_fx = -deuda_externa_pp * apreciacion
    suma = rfspf + ef_g + ef_pi + ef_fx
    return {
        "d_prev": round(d_prev, 2), "d_t": round(d_t, 2),
        "cambio_observado": round(d_t - d_prev, 2),
        "rfspf": round(rfspf, 2),
        "efecto_crecimiento": round(ef_g, 2),
        "efecto_inflacion_denominador": round(ef_pi, 2),
        "compensacion_por_inflacion_pagada": round(compensacion, 2),
        "efecto_inflacion_neto": round(ef_pi + compensacion, 2),
        "efecto_tipo_de_cambio": round(ef_fx, 2),
        "suma_del_marco": round(suma, 2),
        "residuo": round((d_t - d_prev) - suma, 2),
    }

filas = []
def añadir(caso, r, nota):
    filas.append([caso] + [r[k] for k in
        ("d_prev", "d_t", "cambio_observado", "rfspf", "efecto_crecimiento",
         "efecto_inflacion_denominador", "compensacion_por_inflacion_pagada",
         "efecto_inflacion_neto", "efecto_tipo_de_cambio", "suma_del_marco", "residuo")] + [nota])

# ---------------------------------------- PRUEBA DE ACEPTACION, ejercicio 2022 ---
# La instruccion pide reproducir la caida de 2022 y nombra una añada (50.7 -> 49.4
# con RFSPF de 4.5). La rubrica de 2023 registra la validacion con OTRA añada, la
# del CGPE 2024 (49.2 -> 47.7 con RFSPF de 4.3), y anota que las demas dan -1.4 y
# -1.3. Son tres vintages del mismo año y dan resultados distintos, asi que se
# corren los dos y se declara cual es cual. No se elige uno en silencio.
añadir("Prueba 2022, añada del CGPE 2024 (la validada en la rubrica 2023)",
       descomponer(d_prev=49.2, d_t=47.7, rfspf=4.3, g=0.039, pi=0.067,
                   deuda_externa_pp=14.6, apreciacion=0.055),
       "Reproduce -1.5 observado. Es la añada con la que la rubrica dio -1.7 en 2023; "
       "aqui cierra mejor porque el efecto de tipo de cambio se calcula sobre la deuda "
       "externa del sector publico y no sobre la del Gobierno Federal.")
añadir("Prueba 2022, añada que nombra la instruccion 2025 (50.7 -> 49.4)",
       descomponer(d_prev=50.7, d_t=49.4, rfspf=4.5, g=0.039, pi=0.067,
                   deuda_externa_pp=15.0, apreciacion=0.055),
       "Misma mecanica, otra añada del mismo año. La diferencia entre este renglon y el "
       "anterior es exactamente el problema de vintage que el documento denuncia en otros.")

# ------------------------------------------------------- APLICACION A 2025 ---
# Base: CGPE 2025, Anexo III.2 (p. 85) y Anexo III.1 (p. 84).
#   SHRFSPF 2024 estimado 51.4 -> 2025 51.4;  RFSPF 2025 3.9
#   PIB nominal 33,927.7 -> 36,166.4  =>  n = 6.598 %
#   deflactor 4.3 %  =>  g implicito = (1+n)/(1+pi) - 1 = 2.21 %
#   deuda externa 2024 estimado 12.9 pp del PIB
#   tipo de cambio fin de periodo 19.7 -> 18.5 = apreciacion de 6.09 %
n_2025 = 36166.4 / 33927.7 - 1
g_2025 = (1 + n_2025) / 1.043 - 1
añadir("Aplicacion a 2025 (SHRFSPF 51.4 -> 51.4)",
       descomponer(d_prev=51.4, d_t=51.4, rfspf=3.9, g=g_2025, pi=0.043,
                   deuda_externa_pp=12.9, apreciacion=(19.7 - 18.5) / 19.7),
       f"Crecimiento implicito en el PIB nominal publicado: {100*g_2025:.2f} %, dentro del "
       f"rango [2.0,3.0] que declara el CGPE pero por debajo de su punto medio. "
       "El acervo no se mueve porque el requerimiento de 3.9 puntos lo compensan el "
       "crecimiento del PIB nominal y la apreciacion del peso.")

emitir("descomposicion.csv", filas,
       ["caso", "d_inicial", "d_final", "cambio_observado", "rfspf",
        "efecto_crecimiento", "efecto_inflacion_denominador",
        "compensacion_por_inflacion_pagada", "efecto_inflacion_neto",
        "efecto_tipo_de_cambio", "suma_del_marco", "residuo", "nota"],
       {"cuadro": "C12.4", "documento": "CGPE 2025 Anexos III.1 y III.2; CGPE 2024 para la prueba",
        "ubicacion": "p. 84 y 85; construccion propia",
        "tier": "autoral_ited",
        "nota": "Todo en puntos del PIB. La convencion de reparto del efecto denominador "
                "se declara en el encabezado del script y en la nota de metodo: otra "
                "convencion movería decimas entre crecimiento e inflacion sin cambiar la "
                "suma. NO es el marco de manual (primario + r - g), que este documento no "
                "presenta."})

# --------------------------------------------------------------- C12.3 techos ---
techos = [
    ["Endeudamiento neto interno del Gobierno Federal (techo)", 1990000.0, 1580000.0,
     "ILIF art. 2o.", "autorizacion, no gasto"],
    ["Endeudamiento neto externo del sector publico (techo, millones de dolares)", 18000.0, 15500.0,
     "ILIF art. 2o.", "en dolares, no en pesos"],
    ["Endeudamiento neto interno del Gobierno Federal (partida informativa)", 1906069.4, 1576170.0,
     "LIF art. 1o. renglon 0.01.01", "lo que se preve ejercer"],
    ["Deficit presupuestario", 1693000.0, 1170566.5,
     "DEC art. 2 y CGPE", "el flujo, distinto de los dos anteriores"],
]
emitir("techos.csv", techos,
       ["objeto", "mdp_2024", "mdp_2025", "fuente", "que_es"],
       {"cuadro": "C12.3", "documento": "ILIF y LIF aprobada 2024 y 2025; decretos",
        "tier": "oficial_primaria", "ubicacion": "articulos 1o. y 2o.",
        "nota": "TRES OBJETOS DISTINTOS que se confunden habitualmente: el techo es una "
                "autorizacion, el endeudamiento informativo es lo que se preve ejercer, y "
                "el deficit es el flujo. En 2025 valen 1,580,000, 1,576,170.0 y 1,170,566.5 "
                "y ninguno es el otro. El renglon en dolares no se suma con los de pesos."})

print("emitidos: descomposicion, techos\n")
for r in filas:
    print(f"  {r[0][:56]:56s} obs {r[3]:>6}  suma {r[10]:>6}  residuo {r[11]:>6}")
