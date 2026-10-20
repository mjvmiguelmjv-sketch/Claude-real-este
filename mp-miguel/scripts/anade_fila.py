"""Añade una fila a una tabla de una pieza, clonando una fila que ya está (con su formato).

    python anade_fila.py <entrada.docx> <código> <etiqueta de la fila modelo> <etiqueta nueva> "<texto>" <salida.docx>

La fila nueva va justo después de la fila modelo (la primera con esa etiqueta dentro de la pieza).
"""
import copy, sys
import docx
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from docxedit import scopes, ptext, qn
from piezas import fill_cell

W_TR, W_TC = qn('w:tr'), qn('w:tc')
src, code, modelo, nueva, texto, out = sys.argv[1:7]
d = docx.Document(src)
for el in scopes(d)[code]:
    for tr in el.iter(W_TR):
        tcs = tr.findall(W_TC)
        if tcs and ptext(tcs[0]).strip() == modelo:
            n = copy.deepcopy(tr)
            ncs = n.findall(W_TC)
            fill_cell(ncs[0], [nueva]); fill_cell(ncs[-1], [texto])
            tr.addnext(n)
            d.save(out); print(f'{code}: fila «{nueva}» después de «{modelo}» -> {out}')
            sys.exit(0)
sys.exit(f'no encuentro la fila «{modelo}» en {code}')
