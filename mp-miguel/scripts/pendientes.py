"""Añade filas a la tabla de Pendientes de un Doc de mes, con el formato de sus filas.

    python pendientes.py <entrada.docx> <filas.json> <salida.docx>

filas.json: lista de [pieza, qué falta, a quién se le pide, qué bloquea].
"""
import copy, json, sys
import docx
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from docxedit import body_els, ptext, style, W_P, qn
from piezas import fill_cell

doc = docx.Document(sys.argv[1])
h = next(e for e in body_els(doc) if e.tag == W_P and style(e) == 'Heading2' and ptext(e).strip() == 'Pendientes')
t = h.getnext(); trs = t.findall(qn('w:tr')); proto = trs[-1]
# antes de la fila «Todo el mes», que cierra la tabla, si existe
ultima = trs[-1] if ptext(trs[-1].findall(qn('w:tc'))[0]).strip() == 'Todo el mes' else None
for fila in json.load(open(sys.argv[2])):
    tr = copy.deepcopy(proto)
    for tc, v in zip(tr.findall(qn('w:tc')), fila): fill_cell(tc, [v])
    (ultima.addprevious(tr) if ultima is not None else t.append(tr))
doc.save(sys.argv[3]); print('guardado', sys.argv[3])
