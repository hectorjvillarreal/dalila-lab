import re, csv, sys, json, unicodedata
SCR=sys.argv[1]; OUT=sys.argv[2]
docs={'Resultados':f'{SCR}/work/res/accept.md','Recomendaciones':f'{SCR}/work/rec/accept.md'}
# page map: find which pdf page contains a sentence's first 40 chars
import glob
def load_pages(prefix,n):
    pages={}
    for i in range(1,n+1):
        t=open(f'{SCR}/pdf/{prefix}_p{i:02d}.txt',encoding='utf-8').read()
        pages[i]=re.sub(r'\s+',' ',t)
    return pages
pages={'Resultados':load_pages('res',68),'Recomendaciones':load_pages('rec',15)}
def find_page(doc,snippet):
    s=re.sub(r'\s+',' ',snippet)[:45]
    s=s.replace('−','-').replace('‑','-')
    for p,t in pages[doc].items():
        if s in t.replace('−','-'): return p
    # try shorter
    s=s[:25]
    for p,t in pages[doc].items():
        if s in t.replace('−','-'): return p
    return ''
MAG=[('derechohabientes','derechohabiente'),('cotizantes','cotizante'),('ingresos del SEM','ingresos del sem'),('gasto corriente en salud','gasto corriente'),
 ('gasto en trazadores','procedimientos trazadores'),('casos','casos'),('brecha Δ','brecha'),('saldo','saldo'),('déficit GMP','déficit'),('cuota','cuota'),
 ('tasa de utilización','por 100 mil'),('costo por caso','costo por caso'),('costo por persona','por persona'),('quirófano','quirófano'),('masa salarial','masa salarial'),
 ('población CONAPO','conapo'),('afiliados','afilia'),('hogares','hogares'),('reserva','reserva'),('cuidados','cuidados'),('prima','prima'),('PIB','pib'),('UMA','uma'),('salario','salario')]
num_re=re.compile(r'(?<![\w.])[−\-+]?\d{1,3}(?:[,\.]\d{3})*(?:\.\d+)?\s?(%|mil millones|millones|puntos|pesos|miles|veces|años|casos|M)?',re.U)
year_re=re.compile(r'\b(20[2-7]\d)\b')
rows=[]; nid=0
for doc,path in docs.items():
    sec='(portada)'; sub=''
    for line in open(path,encoding='utf-8'):
        line=line.rstrip('\n')
        m=re.match(r'^(#+)\s*(.*)',line)
        if m:
            sec=m.group(2).strip(); continue
        if line.startswith('!['): continue
        txt=line.strip()
        if not txt: continue
        intable = txt.startswith('  ') or line.startswith('  ')
        # split into sentences
        sents=re.split(r'(?<=[\.\;])\s+(?=[A-ZÁÉÍÓÚ¿«(])',txt) if not intable else [txt]
        for s in sents:
            s=s.strip()
            nums=list(num_re.finditer(s))
            if not nums: continue
            years=year_re.findall(s)
            low=s.lower()
            mags=[m for m,k in MAG if k in low]
            for n in nums:
                val=n.group(0).strip()
                if re.fullmatch(r'[−\-+]?20[2-7]\d',val) or re.fullmatch(r'[−\-+]?19\d\d',val): continue
                if re.fullmatch(r'\d{1,2}',val) and ('sección' in low or 'tabla' in low or 'figura' in low or 'anexo' in low) and len(nums)<=2: continue
                unit=n.group(1) or ''
                nid+=1
                rows.append({'id':nid,'documento':doc,'seccion':sec,'pagina_aprox':find_page(doc,s),'oracion':s[:400],'valor':val.replace(unit,'').strip(),'unidad':unit,'magnitud':';'.join(mags),'anio':';'.join(sorted(set(years))),'en_tabla':'sí' if intable else 'no'})
with open(f'{OUT}/tablas/cifras.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['id','documento','seccion','pagina_aprox','oracion','magnitud','valor','unidad','anio','en_tabla']); w.writeheader(); w.writerows(rows)
print('cifras',len(rows))
# ---- language checks
terms=['costo para el patr','costo laboral','costo de la formalidad','abarat','sin que los patrones paguen','lo que pagan los patrones','que no cueste','paga el patr','pagan los patrones','pague más','pagar más','cuesta más a','autofinanci','se paga sol','sostenib','insostenib','proyección del IMSS','propuesta del IMSS','incidencia']
res=[]
for doc,path in docs.items():
    sec=''
    for ln,line in enumerate(open(path,encoding='utf-8'),1):
        m=re.match(r'^(#+)\s*(.*)',line)
        if m: sec=m.group(2).strip()
        low=line.lower()
        for t in terms:
            for mm in re.finditer(re.escape(t.lower()),low):
                a=max(0,mm.start()-90); b=min(len(line),mm.end()+90)
                res.append((doc,sec,ln,t,line[a:b].strip().replace('\n',' ')))
with open(f'{SCR}/lenguaje_hits.tsv','w',encoding='utf-8') as f:
    for r in res: f.write('\t'.join(map(str,r))+'\n')
print('lenguaje hits',len(res))
# ---- siglas: uppercase tokens 2-7 letters, first occurrence, check if expanded nearby
for doc,path in docs.items():
    text=open(path,encoding='utf-8').read()
    body=text
    seen={}
    for m in re.finditer(r'\b([A-ZÁÉÍÓÚ]{2,8}(?:-[A-Z]{1,4})?)\b',body):
        s=m.group(1)
        if s in seen or s in ('II','III','IV','VI','VII','CC','CCM','MDP','PP','E0','HTML','PNG','CSV'): continue
        ctx=body[max(0,m.start()-200):m.end()+200]
        expanded = bool(re.search(r'\(\s*'+re.escape(s)+r'\s*[\)\s]',ctx)) or bool(re.search(re.escape(s)+r'\s*\(',ctx))
        sec=''
        for hm in re.finditer(r'^(#+)\s*(.*)$',body[:m.start()],re.M): sec=hm.group(2)
        seen[s]=(sec,expanded,body[max(0,m.start()-60):m.end()+60].replace('\n',' '))
    with open(f'{SCR}/siglas_{doc}.tsv','w',encoding='utf-8') as f:
        for s,(sec,e,c) in seen.items(): f.write(f'{s}\t{sec}\t{"definida" if e else "NO"}\t{c}\n')
    print(doc,'siglas',len(seen),'sin definir',sum(1 for v in seen.values() if not v[1]))
# ---- Fernández Huerta readability per top-level section
def syll(word):
    w=word.lower()
    w=re.sub(r'[^a-záéíóúü]','',w)
    if not w: return 0
    # count vowel groups with diphthong handling
    strong='aeoáéó'; weak='iuúíü'
    count=0; prev=None
    for ch in w:
        isv = ch in strong+weak
        if isv:
            if prev is None: count+=1
            elif prev in weak and ch in weak: pass
            elif (prev in strong and ch in weak) or (prev in weak and ch in strong): pass
            elif prev in strong and ch in strong: count+=1
            else: count+=1
            prev=ch
        else: prev=None
    # accented weak vowels break diphthongs
    count+=len(re.findall(r'[íú][aeo]|[aeo][íú]',w))
    return max(1,count)
for doc,path in docs.items():
    secs={}; cur='(portada)'
    for line in open(path,encoding='utf-8'):
        m=re.match(r'^(#)\s+(.*)',line)
        if m: cur=m.group(2).strip(); continue
        if line.startswith('  ') or line.startswith('![') or line.startswith('**Tabla') or line.startswith('**Figura') or line.startswith('*Fuente') or line.startswith('Fuente'): continue
        if line.strip(): secs.setdefault(cur,[]).append(line.strip())
    out=[]
    for sname,lines in secs.items():
        t=' '.join(lines)
        t=re.sub(r'\[\^?\d+\]','',t)
        sents=[s for s in re.split(r'(?<=[\.\?\!:])\s+',t) if len(s.split())>=3]
        words=[w for w in re.findall(r"[A-Za-zÁÉÍÓÚáéíóúñÑüÜ]+",t)]
        if not sents or len(words)<30: continue
        P=sum(syll(w) for w in words)/len(words)*100
        F=len(sents)/len(words)*100
        L=206.84-0.60*P-1.02*F
        out.append((sname,len(words),len(sents),round(len(words)/len(sents),1),round(L,1)))
    with open(f'{SCR}/legibilidad_{doc}.tsv','w',encoding='utf-8') as f:
        f.write('seccion\tpalabras\toraciones\tpalabras_por_oracion\tfernandez_huerta\n')
        for r in out: f.write('\t'.join(map(str,r))+'\n')
    print(doc,'legibilidad secciones',len(out))
