"""TGF de registros, 2010-2024: Costa Rica, Colombia y Chile. Parte 1, ¿una sexta fase?
Fuente: GrandPlan/DFD/research/fertility_collapse_abm/data/national (cada fila trae fuente y método)."""
import os, pandas as pd
N = os.path.expanduser("~/Dalila/GrandPlan/DFD/research/fertility_collapse_abm/data/national")
OUT = os.path.dirname(os.path.abspath(__file__))
cri = pd.read_csv(f"{N}/CRI_tfr_national.csv").set_index("year").value
col = pd.read_csv(f"{N}/COL_tfr_national.csv").set_index("year").value
chi = pd.read_csv(f"{N}/CHL_tfr_national.csv").set_index("year").value
imp = pd.read_csv(f"{N}/CHL_tfr_implied.csv"); print(imp.columns.tolist()); print(imp.tail(16).iloc[:, :4].to_string(index=False))
v = [c for c in imp.columns if "tfr" in c.lower() or c == "value"][0]
imp = imp.set_index("year")[v]
chl = imp.reindex(range(2010, 2025)); chl.update(chi)
t = pd.DataFrame({"cri": cri, "col": col, "chl": chl}).loc[2010:2024].round(2)
t.index.name = "anio"; t.to_csv(f"{OUT}/p1_desplome.csv", na_rep="nan"); print(t.to_string())
print("Costa Rica", round((1 - cri[2024] / cri[2010]) * 100), "% | Colombia", round((1 - col[2024] / col[2015]) * 100), "% | Chile", round((1 - chl[2024] / chl[2010]) * 100), "%")
