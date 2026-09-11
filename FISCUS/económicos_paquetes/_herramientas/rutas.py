#!/usr/bin/env python3
"""Registro de rutas de descarga del paquete económico, y su sonda.

Precarga §3.8 de INSTRUCCIONES_preparacion_2027.md. La corrida en vivo NO explora:
lee este archivo, sustituye el ejercicio y descarga. Cada ruta trae su veredicto de
la última sonda y la trampa que la acompaña.

    python rutas.py            # imprime el registro para el ejercicio 2027
    python rutas.py --sondear  # prueba contra 2026, que ya cerró, y escribe el CSV
    python rutas.py --sondear --ejercicio 2027

Conducta de red: una petición cada 2 segundos, secuencial, verificación TLS SIEMPRE
activa. El bundle lo prepara `preparar_bundle.sh`.
"""
from __future__ import annotations
import argparse, csv, subprocess, sys, time
from datetime import date
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BUNDLE = AQUI / "_certs" / "bundle.pem"
SALIDA = AQUI / "rutas_probadas.csv"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/128.0 Safari/537.36")
PAUSA = 2.0

# El día de entrega del paquete del ejercicio t es en septiembre del año t-1.
# 2026: lunes 8 de septiembre de 2025, legislatura LXVI, Gaceta 6871.
ENTREGA = {2026: date(2025, 9, 8), 2027: date(2026, 9, 8)}
LEGISLATURA = {2026: 66, 2027: 66}

FP = "https://www.finanzaspublicas.hacienda.gob.mx/work/models/Finanzas_Publicas/docs/paquete_economico"
PEF = "https://www.pef.hacienda.gob.mx/work/models/PEF/Analiticos_Historico"
ATDT = "https://repodatos.atdt.gob.mx/api_update"
CKAN = "https://www.datos.gob.mx/api/3/action"

# orden = prioridad de descarga el día de la entrega. Menor primero.
RUTAS = [
 # ---- 1. La Gaceta Parlamentaria: el paquete entero, el mismo día ----------
 dict(orden=1, id="gaceta_indice", pieza="paquete completo", metodo="GET",
      url="https://gaceta.diputados.gob.mx/Gaceta/{leg}/{anio_entrega}/sep/{fecha}.html",
      nota="PRIMERA PARADA. Índice del día de la entrega; los anexos cuelgan de él. "
           "La URL es estable; EL CONTENIDO NO. Se reescribe en las horas y el día "
           "siguientes a la entrega: en 2027 cambió entre las 18:51 del día 8 y la "
           "mañana del 9, y arrastra un bloque comentado con las letras del año "
           "anterior. GUÁRDALO CON MARCA DE TIEMPO CADA VEZ y quédate con las dos "
           "copias: la diferencia es evidencia. En 2026 fueron doce anexos, A-L; en "
           "2027, catorce servidos, A-N, y el índice sólo listaba hasta J. SE REESCRIBE "
           "MÁS DE UNA VEZ: en 2027 hubo tres versiones ---18:51 del día 8, mañana del 9 "
           "y noche del 10---, y la tercera DESCOMENTÓ el bloque del año anterior y le "
           "corrigió letras y año, quedando idéntica al mapa que nosotros habíamos leído "
           "de la primera página de cada PDF. El índice converge, pero tarda dos días: "
           "el día de la corrida la única fuente fiable sigue siendo el PDF."),
 dict(orden=2, id="gaceta_ilif", pieza="ILIF", metodo="GET",
      url="https://gaceta.diputados.gob.mx/PDF/{leg}/{anio_entrega}/sep/{fecha}-A.pdf",
      nota="Anexo A. CONTIENE SU PROPIA EXPOSICIÓN DE MOTIVOS: no la busques aparte. "
           "240 pp en 2026."),
 dict(orden=3, id="gaceta_ppef", pieza="PPEF, proyecto de decreto", metodo="GET",
      url="https://gaceta.diputados.gob.mx/PDF/{leg}/{anio_entrega}/sep/{fecha}-B.pdf",
      nota="Anexo B. SOLO EL DECRETO: la exposición de motivos del PPEF no viene aquí "
           "ni en la Gaceta. 194 pp en 2026."),
 dict(orden=4, id="gaceta_cgpe", pieza="CGPE", metodo="GET",
      url="https://gaceta.diputados.gob.mx/PDF/{leg}/{anio_entrega}/sep/{fecha}-C.pdf",
      nota="Anexo C."),
 dict(orden=5, id="gaceta_miscelanea", pieza="miscelánea fiscal", metodo="GET",
      url="https://gaceta.diputados.gob.mx/PDF/{leg}/{anio_entrega}/sep/{fecha}-D.pdf",
      nota="LA LETRA NO IDENTIFICA NADA. Lección de la corrida 2027, más dura que la "
           "de 2026: no basta con leer las letras del índice, porque EL ÍNDICE SE "
           "REESCRIBE DESPUÉS DE LA ENTREGA y las letras se reasignan. El 8-sep-2026 el "
           "índice daba F = Código Fiscal y G = informe arancelario; el 9-sep esa "
           "iniciativa había desaparecido del índice, F era Ley Aduanera, se habían "
           "insertado G = Ley de Economía Digital y H = Ley Catastral y Registral, y el "
           "informe arancelario se había recorrido a J. Identifica cada anexo POR LA "
           "PRIMERA PÁGINA DEL PDF y guarda el índice con marca de tiempo cada vez que "
           "lo consultes. En 2026: D = Derechos, E = IEPS, F = Código Fiscal, "
           "G = arancelario. En 2027: D = Derechos, E = ISR, F = Aduanera, G = Economía "
           "Digital, H = Catastral, J = arancelario, K-N = Bienestar (ZAP y vivienda)."),
 dict(orden=5.1, id="gaceta_cola", pieza="anexos de la cola del paquete (ZAP, vivienda)",
      metodo="GET",
      url="https://gaceta.diputados.gob.mx/PDF/{leg}/{anio_entrega}/sep/{fecha}-K.pdf",
      nota="LA COLA LLEGA AL DÍA SIGUIENTE. En 2027 los cuatro anexos de la Secretaría "
           "de Bienestar ---nota metodológica y declaratoria ZAP, listados rural y "
           "urbano, y la estimación de subsidios de vivienda del art. 61 de la Ley de "
           "Vivienda--- se generaron entre las 05:29 y las 05:46 del DÍA SIGUIENTE a la "
           "entrega, y el índice vivo seguía sin listarlos. Recorre K, L, M, N... hasta "
           "el primer 404 firme. Éstos SÍ traen capa de texto completa; las iniciativas "
           "de ley de la misma tanda vienen escaneadas."),
 dict(orden=5.2, id="bienestar_zap_urbanas", pieza="ZAP urbanas con variables (AGEB)",
      metodo="GET",
      url="https://sisge.bienestar.gob.mx/dae/zap{t}/zap_urbanas_{t}_43636_variables_descarga.zip",
      nota="HALLAZGO 2026-09-09, DESCARGADA Y VERIFICADA EL 2026-09-10. La nota "
           "metodológica de la ZAP publica esta ruta. Las 43.636 AGEB urbanas "
           "prioritarias de 2027 con sus variables, legibles por máquina: ZIP de 2,1 "
           "MB con un solo xlsx, ENCABEZADO EN EL RENGLÓN 5 y doce columnas. El conteo "
           "va EN EL NOMBRE del archivo, así que cambia cada año: léelo de la nota "
           "metodológica, no lo supongas. Y NO ES PIEZA DE COLA: el last-modified del "
           "servidor es 2026-07-15, DOS MESES ANTES de la entrega. Lo que llega con el "
           "paquete es el nombre, no el archivo. Cuenta municipios y localidades sobre "
           "la CLAVE ACTUAL A JUNIO DE t-1 (última columna), no sobre las claves de sus "
           "propias columnas: con ésas dan 2.416 y 4.540, no los 2.423 y 4.531 que "
           "declara la nota."),
 # ---- 2. Analíticos del proyecto, en el portal de la Secretaría -----------
 dict(orden=6, id="analitico_p_gf_prog", pieza="analítico proyecto GF ramo-programa-UR-objeto",
      metodo="GET", url=PEF + "/{t}/Proyecto/ac01_ra_pp_ur_og.xlsx",
      nota="Datos en la hoja «Hoja1», NO en la primera, que es una carátula de 45 filas "
           "por ramo. Código de programa = MOD[0] + PP[:3]."),
 dict(orden=7, id="analitico_p_gf_func", pieza="analítico proyecto GF ramo-función-UR-objeto",
      metodo="GET", url=PEF + "/{t}/Proyecto/ac01_ra_f_ur_og.xlsx",
      nota="F y FN vienen como texto con nombre («2 Desarrollo Social»); en los cortes "
           "por programa, como número."),
 dict(orden=8, id="analitico_p_ef_prog", pieza="analítico proyecto entidades ramo-programa",
      metodo="GET", url=PEF + "/{t}/Proyecto/ac01_ra_pp_ur_og_efe.xlsx", nota=""),
 dict(orden=9, id="analitico_p_ef_func", pieza="analítico proyecto entidades ramo-función",
      metodo="GET", url=PEF + "/{t}/Proyecto/ac01_ra_f_ur_og_efe.xlsx", nota=""),
 # ---- 3. La base del proyecto en datos abiertos: RANURA ÚNICA -------------
 dict(orden=10, id="ckan_ppef", pieza="catálogo: dónde está el PPEF en datos abiertos",
      metodo="GET", url=CKAN + "/package_search?q=PPEF&rows=20",
      nota="datos.gob.mx REDIRIGE 308 a www.datos.gob.mx: usa -L o el host con www. "
           "Sin User-Agent de navegador, Akamai responde 403."),
 dict(orden=11, id="atdt_ppef", pieza="PPEF por clave (partida, cartera, entidad)",
      metodo="GET", url=ATDT + "/secretaria_hacienda/proyecto_presupuesto_egresos_federacion/PPEF_{t}.csv",
      nota="RANURA ÚNICA. Trae partida específica, clave de cartera y entidad federativa, "
           "que los xlsx no traen. Los años anteriores devuelven 503, verificado: "
           "PPEF_2025.csv ya no existe. LO QUE NO SE DESCARGUE ESE DÍA DESAPARECE."),
 dict(orden=12, id="atdt_transversales", pieza="anexos transversales por programa",
      metodo="GET", url=ATDT + "/secretaria_hacienda/analitico_plazas_remuneraciones_apf_ppef/anexos_transversales_ppef{t}.csv",
      nota="RANURA ÚNICA, misma advertencia. Es la única fuente del etiquetado transversal "
           "desglosado; sin ella no hay capítulo de anexos."),
 dict(orden=13, id="atdt_plazas", pieza="analítico de plazas y remuneraciones",
      metodo="GET", url=ATDT + "/secretaria_hacienda/analitico_plazas_remuneraciones_apf_ppef/analitico_plazas_apf_PPEF.csv",
      nota="RANURA ÚNICA sin año en el nombre: se sobrescribe en silencio."),
 # ---- 4. El año anterior: aprobado, para la línea G -----------------------
 dict(orden=14, id="analitico_a_gf_prog", pieza="analítico APROBADO t-1, GF ramo-programa",
      metodo="GET", url=PEF + "/{t_1}/Autorizado/ac01_ra_pp_ur_og.xlsx",
      nota="Para la línea de comparación G (proyecto contra aprobado). Descargable ANTES "
           "de la entrega: no depende del paquete."),
 dict(orden=15, id="analitico_a_ef_prog", pieza="analítico APROBADO t-1, entidades ramo-programa",
      metodo="GET", url=PEF + "/{t_1}/Autorizado/ac01_ra_pp_ur_og_efe.xlsx", nota=""),
 # ---- 5. El portal de la Secretaría, como respaldo -----------------------
 dict(orden=16, id="shcp_cgpe", pieza="CGPE (respaldo)", metodo="GET",
      url=FP + "/cgpe/cgpe_{t}.pdf",
      nota="Patrón estable 2018-2026. Respaldo de la Gaceta, no primera parada."),
 dict(orden=17, id="shcp_ilif", pieza="ILIF (respaldo)", metodo="GET",
      url=FP + "/ilif/ilif_{t}.pdf", nota="Patrón estable 2018-2026."),
 # ---- 6. Denominadores demográficos --------------------------------------
 dict(orden=18, id="conapo_pob", pieza="CONAPO población a mitad de año 1950-2070",
      metodo="GET", url="https://repodatos.atdt.gob.mx/CONAPO/proyecciones/00_Pob_Mitad_1950_2070.csv",
      nota="45 MB. Edad simple x sexo x entidad x año. NO depende del paquete: "
           "descargar antes."),
 dict(orden=19, id="conapo_ind", pieza="CONAPO indicadores demográficos 1950-2070",
      metodo="GET", url="https://repodatos.atdt.gob.mx/CONAPO/proyecciones/05_Indicadores_demograficos_proyecciones.csv",
      nota="TGF, esperanza de vida, tasas. Si falla, el mismo recurso vive bajo "
           "www.datos.gob.mx/dataset/f2b9b220-.../download/."),
 dict(orden=20, id="issste_padron", pieza="ISSSTE, padrón de derechohabientes activos",
      metodo="GET", url=CKAN + "/package_search?q=padron_derechohabientes_activos&rows=3",
      nota="HALLAZGO 2026-09-07: el padrón del ISSSTE SÍ está en el catálogo nacional, "
           "mensual, org «issste». Era una de las carencias de la corrida 2026."),
 dict(orden=21, id="imssb_padron", pieza="IMSS-Bienestar, personas sin seguridad social",
      metodo="GET", url=CKAN + "/package_search?q=personas_sin_seguridad_social&rows=3",
      nota="Trimestral, org «imss-bienestar». Cobertura parcial: en 2T2025 eran "
           "23 entidades, no las 32. Declararlo siempre."),
 dict(orden=22, id="sep_matricula", pieza="SEP, matrícula por tipo y nivel educativo",
      metodo="POST", url="https://www.planeacion.sep.gob.mx/principalescifras/",
      nota="HALLAZGO 2026-09-07: la ruta que faltaba en 2026. ASP.NET WebForms con "
           "__VIEWSTATE: hay que GET la página, conservar los campos ocultos y POSTear. "
           "Los desplegables son en cascada. Lo hace `descargar_demografia.py`. "
           "Ciclo 2025-2026 disponible; fuente, Formato 911."),
 dict(orden=23, id="imss_datos", pieza="IMSS, asegurados (NO RESUELTA)", metodo="GET",
      url="https://datos.imss.gob.mx/",
      nota="SIGUE ABIERTA. El host de datos abiertos del IMSS respondió 503 el "
           "2026-09-07 y el catálogo nacional no tiene asegurados del IMSS (q=asegurados "
           "devuelve dos datasets de la CNSF). Y www.imss.gob.mx da SOFT-404: 200 con "
           "120 KB de HTML para rutas inexistentes. Sin esto no hay gasto por afiliado."),
 dict(orden=24, id="transparencia", pieza="Transparencia Presupuestaria (último recurso)",
      metodo="GET", url="https://www.transparenciapresupuestaria.gob.mx/es/PTP/Datos_Abiertos",
      nota="Comparte la cadena TLS rota de la SHCP; el mismo bundle la arregla. Devuelve "
           "cáscara JS sin un solo enlace a archivo. No esperes nada de aquí."),
]


def resolver(r: dict, t: int) -> str:
    e = ENTREGA.get(t, date(t - 1, 9, 8))
    return r["url"].format(t=t, t_1=t - 1, leg=LEGISLATURA.get(t, 66),
                           anio_entrega=e.year, fecha=e.strftime("%Y%m%d"))


def sondear(url: str, metodo: str) -> tuple[str, str, str]:
    """Devuelve (código http, content-type, veredicto). Nunca desactiva TLS."""
    if metodo == "POST":
        return ("n/a", "n/a", "SONDA MANUAL — ver descargar_demografia.py")
    cmd = ["curl", "-sSL", "-A", UA, "--max-time", "45", "-o", "/dev/null",
           "-w", "%{http_code}\t%{content_type}", "-r", "0-1023", url]
    if BUNDLE.exists():
        cmd[1:1] = ["--cacert", str(BUNDLE)]
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        return ("", "", f"FALLA DE RED: {p.stderr.strip().splitlines()[-1][:80]}")
    cod, _, tipo = p.stdout.partition("\t")
    ok = cod.startswith("2")
    html = "text/html" in tipo
    if ok and html and url.endswith((".pdf", ".xlsx", ".csv")):
        return (cod, tipo, "SOSPECHA: 200 con HTML donde se esperaba archivo (soft-404)")
    return (cod, tipo, "responde" if ok else "no responde")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sondear", action="store_true")
    ap.add_argument("--ejercicio", type=int, default=2026,
                    help="ejercicio contra el que se sondea (2026 es el que ya cerró)")
    a = ap.parse_args()

    if not a.sondear:
        print(f"Registro de rutas — resuelto para el ejercicio {a.ejercicio}\n")
        for r in sorted(RUTAS, key=lambda x: x["orden"]):
            print(f"{r['orden']:>3}. {r['pieza']}\n     {resolver(r, a.ejercicio)}")
            if r["nota"]:
                print(f"     · {r['nota']}")
            print()
        return 0

    if not BUNDLE.exists():
        print(f"AVISO: no existe {BUNDLE}. Corre preparar_bundle.sh primero.", file=sys.stderr)
    filas, bien, mal = [], 0, 0
    print(f"Sonda contra el ejercicio {a.ejercicio}, {len(RUTAS)} rutas, "
          f"una cada {PAUSA:.0f} s. Verificación TLS activa.\n")
    for r in sorted(RUTAS, key=lambda x: x["orden"]):
        url = resolver(r, a.ejercicio)
        cod, tipo, ver = sondear(url, r["metodo"])
        bien += ver == "responde"
        mal += ver not in ("responde", "SONDA MANUAL — ver descargar_demografia.py")
        print(f"  [{'OK ' if ver == 'responde' else '   '}] {r['id']:<22} {cod:>4}  {ver[:60]}")
        filas.append(dict(orden=r["orden"], id=r["id"], pieza=r["pieza"], metodo=r["metodo"],
                          url_probada=url, http=cod, content_type=tipo.strip(),
                          veredicto=ver, fecha_sonda=date.today().isoformat(), nota=r["nota"]))
        time.sleep(PAUSA)
    with SALIDA.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0]))
        w.writeheader(); w.writerows(filas)
    print(f"\n{bien} responden, {mal} no. Escrito {SALIDA.name}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
