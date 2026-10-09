# Cálculos de la Sección 6 (P4): brecha de balance primario estabilizador (§6.2)
# y presión demográfica mecánica (§6.3). Fuente: WEO abril 2025 + base_analisis_P3.csv
import pandas as pd, numpy as np
iso=['BRA','CHL','COL','CRI','MEX','PAN']
nom={'BRA':'Brasil','CHL':'Chile','COL':'Colombia','CRI':'Costa Rica','MEX':'México','PAN':'Panamá'}
w=pd.read_csv('weo/weo_apr2025_6paises_subset.tsv',sep='\t',dtype=str)
yrs=[str(y) for y in range(2000,2031)]
def ser(code):
    d=w[w['WEO Subject Code']==code].set_index('ISO')[yrs]
    return d.apply(lambda c: pd.to_numeric(c.str.replace(',',''),errors='coerce'))
ngdp=ser('NGDP'); ob=ser('GGXCNL_NGDP'); pb=ser('GGXONLB_NGDP'); bn=ser('GGXWDN_NGDP'); bg=ser('GGXWDG_NGDP')
esa=w[w['WEO Subject Code']=='GGXWDN_NGDP'].set_index('ISO')['Estimates Start After']
g=ngdp.T.pct_change().T*100          # crecimiento nominal del PIB, %
intr=pb-ob                           # pago neto de intereses, % del PIB
intr_weo=intr.copy()
# México (revisión final, 8 oct 2026): pb-ob del WEO arrastra partidas de los RFSP que no son intereses
# (5,9 % del PIB en 2024). Se sustituye 2015-2024 por los intereses del sector público federal en el
# perímetro RFSP (SHCP), mismo perímetro que la deuda neta (SHRFSP). No hay serie SHCP equivalente para
# 2025-2030, por lo que la ventana de proyección de México no se calcula.
shcp=pd.read_csv('weo/shcp_rfsp_intereses_mex.csv').set_index('anio')['intereses_mmdp']
for y in range(2015,2025): intr.loc['MEX',str(y)]=100*shcp[y]/ngdp.loc['MEX',str(y)]
for y in range(2025,2031): intr.loc['MEX',str(y)]=np.nan
bl=bn.T.shift(1).T                   # deuda neta en t-1, % del PIB
def rg_window(c, win):
    # r implícita agregada: suma de intereses (reescalados a PIB t-1) / suma de deuda neta t-1
    if intr.loc[c,win].isna().any(): return np.nan,np.nan
    num=(intr.loc[c,win]*(1+g.loc[c,win]/100)).sum(); den=bl.loc[c,win].sum()
    r=100*num/den
    gg=100*((1+g.loc[c,win]/100).prod()**(1/len(win))-1)   # media geométrica
    return r,gg
H=[str(y) for y in range(2015,2025)]; P=[str(y) for y in range(2025,2031)]
rows=[]
for c in iso:
    rH,gH=rg_window(c,H); rP,gP=rg_window(c,P)
    b24=bn.loc[c,'2024']; pb24=pb.loc[c,'2024']
    pbH=b24*(rH-gH)/100/(1+gH/100); pbP=b24*(rP-gP)/100/(1+gP/100)
    # sensibilidad (revisión final): deuda bruta 2024 con la misma r y g de la ventana histórica
    bg24=bg.loc[c,'2024']; pbG=bg24*(rH-gH)/100/(1+gH/100)
    rows.append(dict(iso=c,pais=nom[c],b_2024=b24,pb_2024=pb24,r_H=rH,g_H=gH,rg_H=rH-gH,pbs_H=pbH,brecha_H=pbH-pb24,
                     r_P=rP,g_P=gP,rg_P=rP-gP,pbs_P=pbP,brecha_P=pbP-pb24,esa=esa[c],int_2024=intr.loc[c,'2024'],bg_2024=bg24,brecha_G=pbG-pb24))
t=pd.DataFrame(rows).sort_values('brecha_H',ascending=False)
pd.set_option('display.width',220); print(t.round(2).to_string(index=False))
t.to_csv('seccion6_espacio_fiscal.csv',index=False)
# series WEO nuevas para la base P4
out=[]
for c in iso:
    for y in range(2001,2025):
        out.append(dict(pais=nom[c],iso3=c,anio=y,indicador='Crecimiento nominal del PIB',codigo_indicador='NGDP',
            tipo='Observado' if y<=int(w[(w.ISO==c)&(w['WEO Subject Code']=='NGDP')]['Estimates Start After'].iloc[0]) else 'Estimación de la fuente',
            modelo=np.nan,valor=round(g.loc[c,str(y)],4),unidad='% (variación anual, moneda nacional a precios corrientes)',
            cobertura_institucional='Nacional',fuente='FMI, World Economic Outlook, abril 2025',nota='Calculado como variación del PIB nominal en moneda nacional (serie NGDP)'))
    for y in range(2000,2025):
        v=ob.loc[c,str(y)]
        if pd.isna(v): continue
        out.append(dict(pais=nom[c],iso3=c,anio=y,indicador='Balance fiscal global',codigo_indicador='GGXCNL_NGDP',
            tipo='Observado' if y<=int(esa[c]) else 'Estimación de la fuente',modelo=np.nan,valor=round(v,4),unidad='% del PIB',
            cobertura_institucional='Gobierno general',fuente='FMI, World Economic Outlook, abril 2025',
            nota='Préstamo/endeudamiento neto; la diferencia con el balance primario es el pago neto de intereses' if c!='MEX'
                 else 'Préstamo/endeudamiento neto. Para México la diferencia con el balance primario no es una medida de intereses (incluye partidas de los RFSP); los intereses se toman de la SHCP'))
for y in range(2015,2025):
    out.append(dict(pais='México',iso3='MEX',anio=y,indicador='Pago de intereses del sector público',codigo_indicador='SHCP_RF213000SPFC',
        tipo='Observado',modelo=np.nan,valor=round(intr.loc['MEX',str(y)],4),unidad='% del PIB',
        cobertura_institucional='Sector público federal (perímetro RFSP)',
        fuente='SHCP, Estadísticas Oportunas de Finanzas Públicas (RFSP, clave RF213000SPFC); PIB nominal del WEO abril 2025',
        nota='Intereses, comisiones y gastos de la deuda, pagado, suma anual; mismo perímetro que la deuda neta (SHRFSP). Sustituye a balance primario menos balance global del WEO en el cálculo de r'))
pd.DataFrame(out).to_csv('weo/series_nuevas_P4.csv',index=False)
# --- 6.3 presión demográfica ---
b=pd.read_csv('base_analisis_P3.csv')
rd=b[b.codigo_indicador=='WPP_RDSEN'].pivot(index='pais',columns='anio',values='valor')
fac=(rd[2050]/rd[2025])
obs=b[(b.tipo!='Proyección propia')&(b.codigo_indicador.isin(['GFS_PENSIONES','GFS_SALUD']))]
last=obs.sort_values('anio').groupby(['pais','codigo_indicador']).tail(1).pivot(index='pais',columns='codigo_indicador',values=['anio','valor'])
p=pd.DataFrame({'RD_2025':rd[2025],'RD_2050':rd[2050],'factor':fac,
   'pen_anio':last[('anio','GFS_PENSIONES')],'pen':last[('valor','GFS_PENSIONES')],
   'sal_anio':last[('anio','GFS_SALUD')],'sal':last[('valor','GFS_SALUD')]})
p['d_pen']=p.pen*(p.factor-1); p['d_sal_05']=p.sal*0.5*(p.factor-1); p['d_sal_10']=p.sal*1.0*(p.factor-1)
p=p.join(t.set_index('pais')[['brecha_H','brecha_P']])
p['frac_min_H']=(p.d_pen+p.d_sal_05)/p.brecha_H; p['frac_max_H']=(p.d_pen+p.d_sal_10)/p.brecha_H
print("\n",p.round(3).to_string()); p.to_csv('seccion6_presion_demografica.csv')
