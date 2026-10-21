"""Noviembre r8: R12 recupera su fase 1, que no estaba en el guion de producción.

    python fase_r12.py <entrada.docx> <salida.docx>

El gancho de R12 ya decía qué se oye y qué se ve en el segundo cero (su tabla «El
gancho»: el hablado «Cada mes pagas facturas que nadie te manda.» y el visual de
«FACTURA 1» escrito y subrayado en la pizarra), pero ninguna fase lo recogía y la voz
no decía «factura». Se clona la fase 2, con su formato, y se rellena con lo que ya
estaba escrito en el gancho. No se escribe ninguna frase nueva.
"""
import copy, sys
import docx
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from docxedit import scopes, ptext, W_P, qn
from piezas import set_p, fill_cell

W_TR, W_TC = qn('w:tr'), qn('w:tc')

d = docx.Document(sys.argv[1])
els = scopes(d)['R12']
if any(el.tag == W_P and ptext(el).startswith('FASE 1') for el in els):
    sys.exit('R12 ya tiene fase 1: no se toca')
gancho = {}
for el in els:
    if el.tag != W_P:
        for tr in el.iter(W_TR):
            tcs = tr.findall(W_TC)
            if len(tcs) == 2: gancho.setdefault(ptext(tcs[0]).strip(), ptext(tcs[1]).strip())
f2 = next(el for el in els if el.tag == W_P and ptext(el).startswith('FASE 2'))
t2 = f2.getnext()
f1, t1 = copy.deepcopy(f2), copy.deepcopy(t2)
set_p(f1, 'FASE 1. Hook, la factura que nadie te manda')
textos = {
    'Locución': gancho['Hablado'],
    'Fondo, A-ROLL': gancho['Visual'].replace('Miguel de pie escribe', 'De pie, escribe'),
    'Fondo, NOTA DE EDICIÓN': f"El escrito del gancho en pantalla desde el segundo cero hasta el final de la fase: «{gancho['Escrito']}»",
}
for tr in t1.findall(W_TR):
    tcs = tr.findall(W_TC)
    k = ptext(tcs[0]).strip()
    if k in textos: fill_cell(tcs[1], [textos[k]])
f2.addprevious(f1); f2.addprevious(t1)
d.save(sys.argv[2])
print('R12: fase 1 añadida ->', sys.argv[2])
