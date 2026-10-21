"""Pone al día la columna «Estado» del índice de un Doc de mes.

    python estado_indice.py <entrada.docx> <estados.json> <salida.docx>

estados.json: {"<código>": "<estado>", ..., "*": "<estado para las demás>"}
"""
import json, sys
import docx
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from docxedit import body_els, ptext, style, W_P, qn
from piezas import fill_cell

d = docx.Document(sys.argv[1]); est = json.load(open(sys.argv[2]))
h = next(e for e in body_els(d) if e.tag == W_P and style(e) == 'Heading2' and ptext(e).strip() == 'Índice')
n = 0
for tr in h.getnext().iter(qn('w:tr')):
    tcs = tr.findall(qn('w:tc')); code = ptext(tcs[0]).strip()
    if code == 'Código': continue
    nuevo = est.get(code, est.get('*'))
    if nuevo: fill_cell(tcs[-1], [nuevo]); n += 1
d.save(sys.argv[3]); print(n, 'estados al día ->', sys.argv[3])
