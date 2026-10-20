"""Monta la versión nueva de un Doc de mes de Miguel sobre su propio .docx.

    python montar_mes.py <spec.json>

El spec dice: el Doc de partida, las sustituciones (las de las piezas que se quedan),
las piezas que salen, las que entran (de la crítica o de la sustitución, con su día)
y el calendario completo, que ordena el índice y las piezas dentro de cada soporte.
Los Pendientes se reescriben con las filas del spec. Todo lo demás —la cabecera, la
ranura, los estilos— es el Doc de Miguel.
"""
import copy, json, sys
import docx
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from docxedit import apply_edits, body_els, piece_code, ptext, style, W_P, qn
from piezas import Plantilla, read_piece, build, table, para, fill_cell

W_TR, W_TC = qn('w:tr'), qn('w:tc')


def grupos(doc):
    """{código: [elementos]} de cada pieza, sin los «PARTE N» que separan secciones."""
    out, cur = {}, None
    for el in body_els(doc):
        c = piece_code(el)
        if c: cur = c; out[cur] = [el]; continue
        if el.tag == W_P and (style(el) in ('Heading1', 'Heading2') or ptext(el).startswith('PARTE ')):
            cur = None; continue
        if cur: out[cur].append(el)
    return out


def heading2(doc, text):
    return next(el for el in body_els(doc) if el.tag == W_P and style(el) == 'Heading2' and ptext(el).strip() == text)


def montar(spec):
    doc = docx.Document(spec['base'])
    errs = []
    for f in spec.get('edits', []):
        errs += apply_edits(doc, json.load(open(f)))
    if errs:
        for m, e in errs: print('ERROR', m, e['ambito'], repr(e['old'][:70]))
        raise SystemExit('hay sustituciones que no casan')

    P = Plantilla(doc, spec['plantilla_reel'], spec['plantilla_secuencia'])
    fuentes = {k: docx.Document(v) for k, v in spec['fuentes'].items()}
    g = grupos(doc)

    # fuera las que salen
    for code in spec['salen']:
        for el in g.pop(code): el.getparent().remove(el)

    # dentro las nuevas, construidas con las plantillas del mes
    for code, (origen, sitio) in spec['entran'].items():
        g[code] = build(read_piece(fuentes[origen], code), P, origen, sitio)

    # cada pieza a su sitio, en el orden del calendario y dentro de su soporte
    for els in g.values():
        for el in els:
            if el.getparent() is not None: el.getparent().remove(el)
    cal = spec['calendario']
    faltan = set(g) ^ {c['codigo'] for c in cal}
    if faltan: raise SystemExit(f'calendario y piezas no casan: {sorted(faltan)}')
    anclas = {'Reel': heading2(doc, 'Reels'), 'Historias': heading2(doc, 'Secuencias de historias')}
    for soporte, ancla in anclas.items():
        last = ancla
        for c in cal:
            if not c['soporte'].startswith(soporte): continue
            for el in g[c['codigo']]:
                last.addnext(el); last = el

    # el índice, rehecho con el calendario
    idx_h = heading2(doc, 'Índice'); tbl = idx_h.getnext()
    trs = tbl.findall(W_TR); proto = trs[1]
    for tr in trs[1:]: tbl.remove(tr)
    for c in cal:
        tr = copy.deepcopy(proto)
        vals = [c['codigo'], c['soporte'], c['pilar'], c['fase'], str(c['anillo']), c['titulo'], c['estado']]
        for tc, v in zip(tr.findall(W_TC), vals): fill_cell(tc, [v])
        tbl.append(tr)

    # Pendientes: la tabla con las filas del spec y los párrafos de debajo
    pen_h = heading2(doc, 'Pendientes'); ptbl = pen_h.getnext()
    trs = ptbl.findall(W_TR); proto = trs[1]
    for tr in trs[1:]: ptbl.remove(tr)
    for fila in spec['pendientes']:
        tr = copy.deepcopy(proto)
        for tc, v in zip(tr.findall(W_TC), fila): fill_cell(tc, [v])
        ptbl.append(tr)
    # los párrafos sueltos de después de la tabla se sustituyen por los del spec
    sig = ptbl.getnext(); proto_p = None
    while sig is not None and sig.tag == W_P:
        nxt = sig.getnext()
        if ptext(sig).strip():
            proto_p = proto_p if proto_p is not None else copy.deepcopy(sig)
            sig.getparent().remove(sig)
        sig = nxt
    last = ptbl
    for t in spec.get('pendientes_parrafos', []):
        p = para(proto_p, t); last.addnext(p); last = p

    doc.save(spec['salida'])
    print('guardado', spec['salida'])


if __name__ == '__main__':
    montar(json.load(open(sys.argv[1])))
