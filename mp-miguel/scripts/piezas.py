"""Monta piezas nuevas con el formato exacto de un Doc de mes de Miguel.

Lee una pieza de otro documento (la crítica del 19 oct o la sustitución) como datos
—su ficha, sus disparadores, su gancho, sus fases y su pie— y la vuelve a construir
clonando los párrafos y las tablas de una pieza del propio mes. Así la pieza nueva
lleva la misma letra, los mismos colores y las mismas tablas que las de alrededor.
"""
import copy, re
from lxml import etree
from docxedit import qn, W_P, W_T, ptext, style, body_els, piece_code

W_TR, W_TC, W_R = qn('w:tr'), qn('w:tc'), qn('w:r')

# Lo que no entra en un Doc de mes: CALMA va por dentro (reglas de la casa, P21),
# y lo que solo servía para elegir sitio ya está decidido en el calendario.
FUERA = ('Trabajo CALMA', 'Contra qué práctica va', 'Puede sustituir a',
         'Lo que ya existe cerca', 'Lo que le falta a la estrategia')


# ---------- leer una pieza de origen ----------

def cell_paras(tc):
    return [ptext(p) for p in tc.iter(W_P) if ptext(p).strip()]

def table_rows(tbl):
    out = []
    for tr in tbl.iter(W_TR):
        tcs = tr.findall(W_TC)
        out.append([cell_paras(tc) for tc in tcs])
    return out

def read_piece(doc, code):
    """Devuelve la pieza como lista de bloques: ('p', texto) o ('t', filas)."""
    els = body_els(doc); out = []; inside = False
    for el in els:
        c = piece_code(el)
        if c is not None or (el.tag == W_P and style(el) in ('Heading1', 'Heading2')):
            if inside: break
            inside = (c == code)
            if inside: out.append(('h', ptext(el)))
            continue
        if not inside: continue
        if el.tag == W_P:
            t = ptext(el).strip()
            if t: out.append(('p', t))
        else:
            out.append(('t', table_rows(el)))
    if not out:
        raise KeyError(code)
    return out


# ---------- plantillas del mes ----------

class Plantilla:
    """Los elementos de una pieza de reel y una de secuencias del mes, para clonar."""
    def __init__(self, doc, reel, secuencia):
        r = self._grab(doc, reel); s = self._grab(doc, secuencia)
        self.h3 = r[0]
        self.linea = r[1]                      # «Autoridad · TOFU»
        self.etiqueta = r[2]                   # «Ficha de la pieza»
        self.ficha = r[3]                      # tabla de dos columnas larga
        self.fase_p = next(e for e in r if e.tag == W_P and ptext(e).startswith('FASE'))
        self.fase_t = r[r.index(self.fase_p) + 1]
        self.pie_t = r[-1]                     # tabla de una celda
        self.trig_t = r[5]                     # Grupo | Cuál y dónde se activa
        self.pant_p = next(e for e in s if e.tag == W_P and ptext(e).startswith('PANTALLA'))
        self.pant_t = s[s.index(self.pant_p) + 1]
        self.ficha_s = s[3]

    @staticmethod
    def _grab(doc, code):
        els = body_els(doc); out = []; inside = False
        for el in els:
            c = piece_code(el)
            if c is not None or (el.tag == W_P and style(el) in ('Heading1', 'Heading2')):
                if inside: break
                inside = (c == code)
            if inside: out.append(el)
        return out


def set_p(p, text):
    """Deja el párrafo con un solo run (el primero, con su formato) y el texto dado."""
    runs = p.findall(W_R)
    for r in runs[1:]: p.remove(r)
    if not runs:
        return p
    ts = runs[0].findall(W_T)
    for t in ts[1:]: runs[0].remove(t)
    ts[0].text = text
    ts[0].set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    return p

def para(tpl_p, text):
    return set_p(copy.deepcopy(tpl_p), text)

def fill_cell(tc, texts):
    ps = [p for p in tc.iter(W_P)]
    proto = ps[0]
    for p in ps: p.getparent().remove(p)
    for t in texts or ['']:
        tc.append(set_p(copy.deepcopy(proto), t))

def table(tpl_t, rows):
    """rows: lista de filas; cada fila, lista de celdas; cada celda, lista de párrafos.
    El número de columnas sale de la plantilla; si la fila trae más, se juntan en la última."""
    t = copy.deepcopy(tpl_t)
    trs = t.findall(W_TR)
    # cada fila copia la de la plantilla con su misma etiqueta (en el mes, «Estructura»
    # va en letra de código y el resto no); si no la hay, una fila de texto normal
    por_etiqueta = {ptext(tr.findall(W_TC)[0]).strip(): tr for tr in trs}
    normal = [tr for tr in trs if 'Mono' not in etree.tostring(tr).decode()]
    proto = (normal[1] if len(normal) > 1 else normal[0]) if normal else trs[0]
    for tr in trs: t.remove(tr)
    ncol = len(proto.findall(W_TC))
    for row in rows:
        etiqueta = ' '.join(row[0]).strip() if row and ncol > 1 else None
        base = por_etiqueta.get(etiqueta, proto)
        if len(base.findall(W_TC)) != ncol: base = proto
        tr = copy.deepcopy(base)
        tcs = tr.findall(W_TC)
        cells = list(row)
        if len(cells) > ncol:
            cells = cells[:ncol - 1] + [sum(cells[ncol - 1:], [])]
        while len(cells) < ncol: cells.append([''])
        for tc, texts in zip(tcs, cells): fill_cell(tc, texts)
        t.append(tr)
    return t


# ---------- construir la pieza en el formato del mes ----------

RENOMBRA = {
    'Idea raíz y concepto': 'Concepto', 'Anillo': 'Anillo de audiencia', 'Dolor o deseo': 'Dolor exacto',
    'Deseo y su dolor': 'Dolor exacto', 'Destino': 'Destino del CTA', 'Molde y disparador': 'Molde y trigger',
    'Material propio que lleva': 'Material propio que lleva dentro',
}
ORDEN_REEL = ['Guion del banco', 'Estructura', 'Idea', 'Frase de la pieza', 'Concepto', 'Formato', 'Pilar',
              'Anillo de audiencia', 'ICP', 'Dolor exacto', 'Fase', 'Destino del CTA', 'Objetivo y métrica',
              'Fuentes', 'Crédito', 'Transformación', 'Vídeos de referencia']
ORDEN_SEC = ['Guion del banco', 'Estructura', 'Idea', 'Frase de la pieza', 'Concepto', 'Formato', 'ICP',
             'Dolor exacto', 'Pilar', 'Anillo', 'Fase', 'Tipo de cierre', 'CTA', 'Objetivo y métrica', 'Fuentes',
             'Crédito', 'Transformación', 'Referencia', 'Triggers usados', 'Número de pantallas']
ICP_FICHA = ('Fundador o socio visible de una agencia o consultora B2B, de cinco a treinta personas, '
             'con clientes que le pagan varios miles de euros y no le compran sin hablar antes.')
BANCO_NUEVO = 'Nuevo: crítica CALMA… '  # se sustituye abajo


def _ficha_dict(rows, secuencia):
    d = {}
    for row in rows:
        if len(row) < 2: continue
        k = ' '.join(row[0]).strip()
        if any(k.startswith(f) for f in FUERA): continue
        k = RENOMBRA.get(k, k)
        if secuencia and k == 'Anillo de audiencia': k = 'Anillo'
        if k == 'Vídeos de referencia' and secuencia: k = 'Referencia'
        d[k] = sum(row[1:], [])
    return d


def build(piece, plantilla, origen, sitio):
    """piece: bloques de read_piece. Devuelve la lista de elementos XML listos para insertar."""
    P = plantilla
    titulo = piece[0][1]
    secuencia = titulo.startswith(('S', 'NS'))
    out = [para(P.h3, titulo)]
    blocks = piece[1:]
    # línea de pilar y fase
    out.append(para(P.linea, blocks[0][1])); blocks = blocks[1:]
    blocks = [b for b in blocks if not (b[0] == 'p' and b[1].startswith(FUERA))]

    # localizar secciones
    def idx(label):
        for i, b in enumerate(blocks):
            if b[0] == 'p' and b[1].startswith(label): return i
        return None
    i_ficha = idx('Ficha de la')
    ficha = _ficha_dict(blocks[i_ficha + 1][1], secuencia)
    i_disp = idx('Disparadores usados')
    disp = blocks[i_disp + 1][1] if i_disp is not None else []
    i_gancho = idx('El gancho')
    i_guion = idx('Guion de producción')
    if i_guion is None:  # algunas secuencias de la crítica pasan del gancho a la primera pantalla
        i_guion = min(i for i, b in enumerate(blocks) if b[0] == 'p' and b[1].startswith(('FASE', 'PANTALLA'))) - 1
    i_pie = idx('Pie de publicación')

    origen_txt = {'critica': 'la crítica del 19 oct 2026', 'sust': 'los guiones de sustitución del 9 oct 2026'}[origen]
    banco = ficha.get('Guion del banco', [''])
    banco = [f'Nuevo, de {origen_txt}; entra en el calendario el {sitio}. PENDIENTE: darlo de alta como guion en el banco.'] \
        if not banco or not ''.join(banco).strip() else banco + [f'Entra en el calendario el {sitio}.']
    ficha['Guion del banco'] = banco
    if not secuencia and 'ICP' not in ficha:
        ficha['ICP'] = [ICP_FICHA + ' (ficha 4.1)']

    if secuencia:
        if disp:
            ficha['Triggers usados'] = [f'{r[0][0]}: {" ".join(r[1])}' for r in disp[1:] if r and r[0]]
        orden = ORDEN_SEC
    else:
        orden = ORDEN_REEL
    filas = [[[k], ficha[k]] for k in orden if k in ficha]
    filas += [[[k], v] for k, v in ficha.items() if k not in orden]
    out.append(para(P.etiqueta, 'Ficha de la secuencia' if secuencia else 'Ficha de la pieza'))
    out.append(table(P.ficha_s if secuencia else P.ficha, filas))

    if not secuencia:
        out.append(para(P.etiqueta, 'Triggers usados'))
        out.append(table(P.trig_t, [[r[0], sum(r[1:], [])] for r in disp]))
        # el gancho: una sola tabla, como en el mes
        g = {}
        for b in blocks[i_gancho + 1:i_guion + 1]:
            if b[0] != 't': continue
            rows = b[1]
            if rows and len(rows[0]) > 2:   # tabla de versiones A, B, C…: se queda fuera
                continue
            for row in rows:
                if len(row) >= 2:
                    k = RENOMBRA.get(' '.join(row[0]).strip(), ' '.join(row[0]).strip())
                    g[k] = sum(row[1:], [])
        out.append(para(P.etiqueta, 'El gancho'))
        out.append(table(P.ficha, [[[k], v] for k, v in g.items()]))

    out.append(para(P.etiqueta, 'Guion de producción'))
    end = i_pie if i_pie is not None else len(blocks)
    for b in blocks[i_guion + 1:end]:
        if b[0] == 'p':
            if b[1].startswith(('FASE', 'PANTALLA', 'REMATE')):
                out.append(para(P.pant_p if secuencia else P.fase_p, b[1]))
            # las notas sueltas («LA MENCIÓN no va…») no entran: son de la crítica
        else:
            out.append(table(P.pant_t if secuencia else P.fase_t, [[r[0], sum(r[1:], [])] for r in b[1]]))
    if i_pie is not None:
        out.append(para(P.etiqueta, 'Pie de publicación'))
        pie = blocks[i_pie + 1][1]
        out.append(table(P.pie_t, [[sum(sum(pie, []), [])]]))
    return out
