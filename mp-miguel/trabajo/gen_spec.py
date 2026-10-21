import json, sys, docx
sys.path.insert(0,'/home/user/Claude-real-este/mp-miguel/scripts')
from docxedit import *
W='/tmp/claude-0/-home-user-Claude-real-este/bb8756ca-7159-57b4-84fe-165cd7e375cc/scratchpad/work/'
def index_rows(path):
    d=docx.Document(path); h=[e for e in body_els(d) if e.tag==W_P and style(e)=='Heading2' and ptext(e)=='Índice'][0]
    rows={}
    for tr in h.getnext().iter(qn('w:tr')):
        v=[ptext(tc) for tc in tr.findall(qn('w:tc'))]
        rows[v[0]]=v
    return rows
NEW={ # código: (pilar, fase, anillo)
 'N21':('Descubrimiento','TOFU',2),'N22':('Autoridad','MOFU',2),'N23':('Demostración','MOFU',2),'N24':('Conversión','BOFU',1),
 'N25':('Descubrimiento','TOFU',2),'N26':('Autoridad','MOFU',2),'N27':('Descubrimiento','MOFU',2),
 'NS1':('Descubrimiento','MOFU',2),'NS2':('Demostración','BOFU',2),'NS3':('Demostración','MOFU',2),'NS4':('Humanización','MOFU',2),
 'NS5':('Descubrimiento','MOFU',2),'NS6':('Autoridad','MOFU',2),'NS7':('Descubrimiento','MOFU',2)}
def titles(path,codes):
    d=docx.Document(path); out={}
    for e in body_els(d):
        c=piece_code(e)
        if c in codes: out[c]=ptext(e)[len(c)+1:]
    return out
def gen(mes, base, cal, salen, entran, edits, pend, pend_p, salida, ronda):
    old=index_rows(W+base)
    sust=index_rows(W+'sust_r2.docx')
    tit={**titles(W+'critica.docx',NEW), **titles(W+'sust_r2.docx',sust)}
    edited=set()
    for f in edits:
        for e in json.load(open(W+f)): edited.add(e['ambito'])
    out=[]
    for code,sop in cal:
        if code in old:
            r=old[code]; est=r[6]
            if code in edited: est=f'{ronda} · ajustada con la crítica del 19 oct'
            # quita marcas que ya no aplican
            out.append(dict(codigo=code,soporte=sop,pilar=r[2],fase=r[3],anillo=r[4],titulo=r[5],estado=est))
        elif code in NEW:
            p,f,a=NEW[code]
            out.append(dict(codigo=code,soporte=sop,pilar=p,fase=f,anillo=a,titulo=tit[code],estado=f'{ronda} · nueva (crítica del 19 oct) · gancho: va el favorito, Por decidir'))
        else:
            r=sust[code]
            out.append(dict(codigo=code,soporte=sop,pilar=r[2],fase=r[3],anillo=r[4],titulo=r[5],estado=f'{ronda} · de la sustitución, ajustada · gancho: Por decidir'))
    spec=dict(base=W+base, edits=[W+f for f in edits], plantilla_reel=cal[0][0] if cal[0][0] in old else 'R01',
              plantilla_secuencia=[c for c,s in cal if c in old and s.startswith('Historias')][0],
              fuentes={'critica':W+'critica.docx','sust':W+'sust_r3.docx'}, salen=salen, entran=entran,
              calendario=out, pendientes=pend, pendientes_parrafos=pend_p, salida=salida)
    json.dump(spec,open(W+f'spec_{mes}.json','w'),ensure_ascii=False,indent=1)
    return spec
