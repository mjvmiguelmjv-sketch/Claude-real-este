"""Edición de los .docx de Miguel sin tocar su formato.

Se trabaja a nivel de párrafo (w:p): el texto de un párrafo es la suma de sus w:t,
y una sustitución cambia solo los caracteres que tocan, dentro de los runs que ya
existen, así que negritas, colores y estilos se quedan como estaban.
"""
import copy, json, sys, re
import docx
from docx.oxml.ns import qn

W_P, W_T, W_TBL = qn('w:p'), qn('w:t'), qn('w:tbl')

def ptext(p):
    return ''.join(t.text or '' for t in p.iter(W_T))

def style(el):
    ps = el.find(qn('w:pPr'))
    if ps is None or ps.find(qn('w:pStyle')) is None:
        return ''
    return ps.find(qn('w:pStyle')).get(qn('w:val'))

def body_els(d):
    return list(d.element.body.iterchildren())

def piece_code(el):
    if el.tag == W_P and style(el) == 'Heading3':
        return ptext(el).split(' ')[0]
    return None

def scopes(d):
    """Devuelve {ámbito: [elementos]}: cada pieza por su código; CABECERA (antes del índice),
    INDICE, y cada Heading2 de después de las piezas por su texto en mayúsculas."""
    out, cur = {}, 'CABECERA'
    for el in body_els(d):
        if el.tag == W_P and style(el) == 'Heading2':
            t = ptext(el).strip()
            if t == 'Índice': cur = 'INDICE'
            elif t in ('Reels', 'Secuencias de historias'): cur = None
            else: cur = t.upper()
        code = piece_code(el)
        if code: cur = code
        if cur: out.setdefault(cur, []).append(el)
    return out

def paragraphs(els):
    for el in els:
        if el.tag == W_P: yield el
        else:
            for p in el.iter(W_P): yield p

def replace_in_p(p, old, new):
    ts = list(p.iter(W_T))
    full = ''.join(t.text or '' for t in ts)
    i = full.find(old)
    if i < 0: return False
    j = i + len(old); pos = 0; done = False
    for t in ts:
        s = t.text or ''; a, b = pos, pos + len(s); pos = b
        if b <= i or a >= j:
            continue
        ls, le = max(i, a) - a, min(j, b) - a
        if not done:
            t.text = s[:ls] + new + s[le:]; done = True
        else:
            t.text = s[:ls] + s[le:]
        t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    return True

def apply_edits(d, edits, strict=True):
    sc = scopes(d); errors = []
    for e in edits:
        els = sc.get(e['ambito'])
        if els is None:
            errors.append(('sin ámbito', e)); continue
        hits = [p for p in paragraphs(els) if e['old'] in ptext(p)]
        if len(hits) != 1:
            errors.append((f'{len(hits)} coincidencias', e)); continue
        replace_in_p(hits[0], e['old'], e['new'])
    return errors

if __name__ == '__main__':
    # comprobar: python docxedit.py check doc.docx edits.json
    cmd, path, spec = sys.argv[1:4]
    d = docx.Document(path)
    edits = json.load(open(spec))
    errs = apply_edits(d, edits)
    for msg, e in errs:
        print('ERROR', msg, e['ambito'], repr(e['old'][:80]))
    print(f'{len(edits)} cambios, {len(errs)} con error')
    if cmd == 'apply' and not errs:
        d.save(sys.argv[4]); print('guardado', sys.argv[4])
