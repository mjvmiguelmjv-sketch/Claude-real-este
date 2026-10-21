"""Mueve una pieza de un Doc de mes a otro, con su formato, y pone al día los dos índices.

    python mover_pieza.py <origen.docx> <destino.docx> <código> <antes_de_código> "<soporte con su día>" <origen_salida.docx> <destino_salida.docx>

La pieza sale del origen entera (título, ficha, pantallas o fases y pie) y entra en el
destino justo antes de la pieza <antes_de_código>, que tiene que ser del mismo soporte.
En el índice del destino, su fila entra justo antes de la fila de esa misma pieza, con
el soporte y el día que se le dan; en el del origen, su fila sale.
"""
import copy, sys
import docx
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from docxedit import body_els, piece_code, ptext, style, W_P, qn
from piezas import fill_cell

W_TR, W_TC = qn('w:tr'), qn('w:tc')


def grupo(doc, code):
    out, dentro = [], False
    for el in body_els(doc):
        c = piece_code(el)
        if c is not None or (el.tag == W_P and (style(el) in ('Heading1', 'Heading2') or ptext(el).startswith('PARTE '))):
            if dentro: break
            dentro = (c == code)
        if dentro: out.append(el)
    if not out: raise KeyError(code)
    return out


def tabla_indice(doc):
    h = next(e for e in body_els(doc) if e.tag == W_P and style(e) == 'Heading2' and ptext(e).strip() == 'Índice')
    return h.getnext()


def fila(tabla, code):
    for tr in tabla.findall(W_TR):
        tcs = tr.findall(W_TC)
        if tcs and ptext(tcs[0]).strip() == code: return tr
    raise KeyError(f'{code} no está en el índice')


def main(origen, destino, code, antes, soporte, origen_out, destino_out):
    a, b = docx.Document(origen), docx.Document(destino)
    els = grupo(a, code)
    ancla = grupo(b, antes)[0]
    for el in els:
        ancla.addprevious(copy.deepcopy(el))
    for el in els:
        el.getparent().remove(el)
    # índices
    ta, tb = tabla_indice(a), tabla_indice(b)
    fa = fila(ta, code)
    nueva = copy.deepcopy(fa)
    fill_cell(nueva.findall(W_TC)[1], [soporte])
    fila(tb, antes).addprevious(nueva)
    ta.remove(fa)
    a.save(origen_out); b.save(destino_out)
    print(f'{code} movida: sale de {origen_out} y entra en {destino_out} antes de {antes}, como «{soporte}»')


if __name__ == '__main__':
    main(*sys.argv[1:8])
