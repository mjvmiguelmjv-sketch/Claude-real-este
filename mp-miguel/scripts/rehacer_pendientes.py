"""Rehace la parte de Pendientes de un Doc de mes, con el formato de sus filas.

    python rehacer_pendientes.py <entrada.docx> <pendientes.json> <salida.docx>

pendientes.json: {"filas": [[pieza, qué falta, a quién se le pide, qué bloquea], ...],
                  "parrafos": ["…", ...]}
La tabla se queda con su cabecera y sus filas pasan a ser las del json; los párrafos
sueltos de debajo de la tabla se sustituyen por los del json, con el formato del primero.
"""
import copy, json, sys
import docx
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from docxedit import body_els, ptext, style, W_P, qn
from piezas import fill_cell, para

W_TR, W_TC = qn('w:tr'), qn('w:tc')

doc = docx.Document(sys.argv[1])
spec = json.load(open(sys.argv[2]))
h = next(e for e in body_els(doc) if e.tag == W_P and style(e) == 'Heading2' and ptext(e).strip() == 'Pendientes')
t = h.getnext()
trs = t.findall(W_TR); proto = trs[1]
for tr in trs[1:]: t.remove(tr)
for f in spec['filas']:
    tr = copy.deepcopy(proto)
    for tc, v in zip(tr.findall(W_TC), f): fill_cell(tc, v if isinstance(v, list) else [v])
    t.append(tr)
sig = t.getnext(); proto_p = None
while sig is not None and sig.tag == W_P:
    nxt = sig.getnext()
    if ptext(sig).strip():
        if proto_p is None: proto_p = copy.deepcopy(sig)
        sig.getparent().remove(sig)
    sig = nxt
last = t
for txt in spec.get('parrafos', []):
    p = para(proto_p, txt); last.addnext(p); last = p
doc.save(sys.argv[3])
print('Pendientes rehechos:', len(spec['filas']), 'filas,', len(spec.get('parrafos', [])), 'párrafos ->', sys.argv[3])
