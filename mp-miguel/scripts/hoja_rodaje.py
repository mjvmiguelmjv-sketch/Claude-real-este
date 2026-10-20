"""Hoja de rodaje por formatos, con el formato exacto de la hoja v3 de Miguel (13 oct).

    python hoja_rodaje.py <hoja_plantilla.docx> <guiones_mes.docx> <salida.docx> "<mes>" "<nota de cabecera>"

Saca de los guiones del mes cada reel —pilar, formato, gancho escrito y lo que se dice
en cada fase— y los agrupa por montaje de cámara para grabarlos del tirón. No va en
orden de publicación. Las secuencias de historias no entran: no se graban a cámara.
"""
import copy, re, sys
import docx
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from docxedit import body_els, piece_code, ptext, style, W_P, qn
from piezas import table, para, cell_paras

W_TR, W_TC = qn('w:tr'), qn('w:tc')

BLOQUES = [
    ('Sentado, plano medio', 'Pantalla dividida y reacción comparten cámara: tú, sentado y en plano medio; la pantalla o el clip de arriba se montan después.'),
    ('De pie, en la pizarra', 'Plano medio, la pizarra a tu derecha. Se escribe en directo lo que pide cada guion.'),
    ('Espontáneo, con el móvil en mano', 'Cámara frontal y el móvil en mano, como dice cada guion: en casa, de pie y con luz de ventana, salvo donde pone otro sitio.'),
]


def clasifica(formato):
    # manda la primera frase: el resto describe el plano y puede nombrar otros formatos
    cabeza = formato.split('.')[0].lower()
    f = formato.lower()
    if cabeza.startswith('a cámara con objeto'):
        return (0, 'A cámara con objeto, sentado') if 'sentado' in f else (2, 'A cámara con objeto, de pie en casa')
    for clave, res in (('horizontal', (1, 'Horizontal + texto (corte de YouTube)')), ('reacción', (0, 'Reacción')),
                       ('pantalla dividida', (0, 'Pantalla dividida')), ('pizarra', (1, 'Pizarra'))):
        if cabeza.startswith(clave): return res
    if 'reacción' in f: return 0, 'Reacción'
    if 'pantalla dividida' in f: return 0, 'Pantalla dividida'
    if 'pizarra' in f: return 1, 'Pizarra'
    if 'horizontal' in f: return 1, 'Horizontal + texto (corte de YouTube)'
    if 'espontáneo' in f or 'móvil' in f:
        donde = 'en el coche' if 'coche' in f else 'en la calle' if 'calle' in f else 'en casa'
        return 2, f'Espontáneo (móvil), {donde}'
    return 0, 'A cámara, sentado'


def reels(path):
    d = docx.Document(path); out = []; cur = None
    for el in body_els(d):
        c = piece_code(el)
        if c:
            cur = None
            if not c.startswith(('S', 'NS')):
                cur = {'codigo': c, 'titulo': ptext(el), 'ficha': {}, 'gancho': {}, 'dices': [], 'sec': None}
                out.append(cur)
            continue
        if el.tag == W_P and style(el) in ('Heading1', 'Heading2'):
            cur = None
        if cur is None: continue
        if el.tag == W_P:
            t = ptext(el).strip()
            if t.startswith('Ficha de la'): cur['sec'] = 'ficha'
            elif t == 'El gancho': cur['sec'] = 'gancho'
            elif t.startswith(('FASE', 'REMATE')): cur['sec'] = 'fase'
            elif t in ('Pie de publicación', 'Triggers usados', 'Disparadores usados', 'Guion de producción'):
                cur['sec'] = None
            continue
        for tr in el.iter(W_TR):
            tcs = tr.findall(W_TC)
            if len(tcs) < 2: continue
            k = ptext(tcs[0]).strip(); v = ' '.join(cell_paras(tcs[1]))
            if cur['sec'] == 'ficha': cur['ficha'][k] = v
            elif cur['sec'] == 'gancho': cur['gancho'][k] = v
            elif cur['sec'] == 'fase' and k == 'Locución': cur['dices'].append(v)
    return out


def main(plantilla, guiones, salida, mes, nota):
    doc = docx.Document(plantilla)
    els = body_els(doc)
    h1, intro, resumen = els[0], els[1], els[2]
    parte = els[3]; h2 = els[4]; h2_intro = els[5]
    h3, linea, etiqueta, ficha_t = els[6], els[7], els[8], els[9]
    gancho_t, dices_t = els[11], els[13]
    tpl = [copy.deepcopy(x) for x in (parte, h2, h2_intro, h3, linea, etiqueta, ficha_t, gancho_t, dices_t)]
    parte, h2, h2_intro, h3, linea, etiqueta, ficha_t, gancho_t, dices_t = tpl
    body = doc.element.body
    for el in els[3:]:
        if el.tag != qn('w:sectPr'): body.remove(el)

    piezas = reels(guiones)
    grupos = {}
    for p in piezas:
        b, sub = clasifica(p['ficha'].get('Formato', ''))
        p['bloque'], p['sub'] = b, sub
        grupos.setdefault(b, {}).setdefault(sub, []).append(p)

    # cabecera y tabla resumen
    from piezas import set_p
    set_p(h1, f'Hoja de rodaje · {mes}')
    total = len(piezas)
    set_p(intro, f'Va por formato, para grabarlo todo del tirón: no va en orden de publicación. {nota} '
                 f'{total} reels en {len(grupos)} bloques. Al grabar, una carpeta por pieza con su código (R01, N01…).')
    filas = [[['Bloque'], ['Formato'], ['Piezas, en orden de grabación']]]
    for b in sorted(grupos):
        for sub, ps in grupos[b].items():
            filas.append([[f'{b + 1} · {BLOQUES[b][0]}'], [sub], [' · '.join(p['codigo'] for p in ps)]])
    nuevo = table(resumen, filas[1:])
    # la fila de cabecera de la plantilla se conserva
    head = copy.deepcopy(resumen.findall(W_TR)[0])
    nuevo.insert(list(nuevo).index(nuevo.findall(W_TR)[0]), head)
    resumen.addprevious(nuevo); body.remove(resumen)

    last = nuevo
    def add(el):
        nonlocal last
        last.addnext(el); last = el
    numeros = ['1', '2', '3', '4', '5', '6']
    for n, b in enumerate(sorted(grupos)):
        add(para(parte, f'PARTE {n + 1}'))
        add(para(h2, BLOQUES[b][0]))
        add(para(h2_intro, BLOQUES[b][1]))
        for sub, ps in grupos[b].items():
            for p in ps:
                pilar = p['ficha'].get('Pilar', '').split('.')[0].split(' (')[0].strip()
                add(para(h3, p['titulo']))
                add(para(linea, f'{pilar} · {p["sub"].split(",")[0]}'))
                add(para(etiqueta, 'Ficha de la pieza'))
                add(table(ficha_t, [[['Pilar'], [pilar]], [['Formato'], [p['ficha'].get('Formato', 'PENDIENTE: sin formato en el guion')]]]))
                add(para(etiqueta, 'El gancho'))
                add(table(gancho_t, [[['Escrito'], [p['gancho'].get('Escrito', 'PENDIENTE')]]]))
                add(para(etiqueta, 'Lo que dices'))
                add(table(dices_t, [[[str(i + 1)], [t]] for i, t in enumerate(p['dices'])]))
    doc.save(salida)
    print('guardado', salida, total, 'reels')


if __name__ == '__main__':
    main(*sys.argv[1:6])
