"""Cambios en un documento largo de Miguel (la ficha), sin tocar su formato.

    python ficha_ops.py check|apply <doc.docx> <ops1.json> [ops2.json …] [--salida out.docx]

Cada operación es un objeto JSON:
- {"op": "sustituir", "ambito", "old", "new"[, "fila", "todas"]}: como docxedit.
- {"op": "parrafo", "empieza": "…", "texto": "…"}: cambia el texto entero del párrafo
  del cuerpo que empieza así (tiene que haber uno solo).
- {"op": "borrar", "desde": "…", "hasta": "…"}: borra los elementos del cuerpo desde el
  párrafo que empieza por «desde» (incluido) hasta el que empieza por «hasta» (sin incluir).
  «hasta» puede ser "FIN_DE_PARTE": hasta el siguiente «PARTE N» o Heading2.
- {"op": "insertar", "antes_de": "…" | "despues_de": "…", "bloques": [...]}: inserta bloques
  clonados del propio documento. Cada bloque es ["titulo", texto] (como «3.1 …»),
  ["etiqueta", texto] (como «Lo más importante, en cinco»), ["texto", texto],
  ["vineta", texto] o ["tabla", {"cabecera": [...], "filas": [[...], ...]}].
  Para «despues_de» con un apartado entero, usa el primer párrafo del apartado siguiente con «antes_de».
Los textos de anclaje se buscan entre los párrafos de primer nivel del cuerpo (no dentro de tablas).
"""
import copy, json, sys
import docx
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from docxedit import apply_edits, body_els, ptext, style, W_P, qn
from piezas import set_p, fill_cell

W_TR, W_TC, W_TBL, W_HL = qn('w:tr'), qn('w:tc'), qn('w:tbl'), qn('w:hyperlink')


class Plantillas:
    def __init__(self, doc, titulo, etiqueta, texto, vineta):
        els = body_els(doc)
        def find(prefix):
            return copy.deepcopy(next(e for e in els if e.tag == W_P and ptext(e).startswith(prefix)))
        self.p = {'titulo': find(titulo), 'etiqueta': find(etiqueta), 'texto': find(texto), 'vineta': find(vineta)}
        self.tablas = {}
        for e in els:
            if e.tag == W_TBL:
                trs = e.findall(W_TR)
                n = len(trs[0].findall(W_TC))
                if len(trs) >= 2 and n not in self.tablas:
                    t = copy.deepcopy(e)
                    # un enlace de la celda de plantilla no lo borra set_p y se quedaba
                    # delante del texto nuevo («6sense, nov 2025…»): fuera los enlaces
                    for h in list(t.iter(W_HL)):
                        h.getparent().remove(h)
                    self.tablas[n] = t

    def bloque(self, tipo, valor):
        if tipo == 'tabla':
            cab, filas = valor.get('cabecera'), valor['filas']
            n = len(cab or filas[0])
            t = copy.deepcopy(self.tablas[n]); trs = t.findall(W_TR)
            head, body = trs[0], trs[1]
            for tr in trs: t.remove(tr)
            if cab:
                h = copy.deepcopy(head)
                for tc, v in zip(h.findall(W_TC), cab): fill_cell(tc, [v])
                t.append(h)
            for f in filas:
                r = copy.deepcopy(body)
                for tc, v in zip(r.findall(W_TC), f): fill_cell(tc, v if isinstance(v, list) else [v])
                t.append(r)
            return t
        return set_p(copy.deepcopy(self.p[tipo]), valor)


def top_p(doc, prefix):
    hits = [e for e in body_els(doc) if e.tag == W_P and ptext(e).startswith(prefix)]
    if len(hits) != 1:
        raise LookupError(f'{len(hits)} párrafos empiezan por {prefix[:60]!r}')
    return hits[0]


def run(doc, ops, P):
    errores = []
    for o in ops:
        try:
            k = o.get('op', 'sustituir')
            if k == 'sustituir':
                errores += [(m, e['old'][:60]) for m, e in apply_edits(doc, [o])]
            elif k == 'parrafo':
                set_p(top_p(doc, o['empieza']), o['texto'])
            elif k == 'borrar':
                a = top_p(doc, o['desde'])
                el = a; quitar = []
                while el is not None:
                    if el is not a and el.tag == W_P:
                        t = ptext(el)
                        if o['hasta'] == 'FIN_DE_PARTE':
                            if t.startswith('PARTE ') or style(el) in ('Heading1', 'Heading2'): break
                        elif t.startswith(o['hasta']): break
                    if el.tag == qn('w:sectPr'): break
                    quitar.append(el); el = el.getnext()
                if el is None and o['hasta'] != 'FIN_DE_PARTE':
                    raise LookupError(f"no encuentro el final {o['hasta'][:60]!r}")
                for x in quitar: x.getparent().remove(x)
            elif k == 'insertar':
                nuevos = [P.bloque(t, v) for t, v in o['bloques']]
                if 'antes_de' in o:
                    ancla = top_p(doc, o['antes_de'])
                    for n in nuevos: ancla.addprevious(n)
                else:
                    ancla = top_p(doc, o['despues_de'])
                    for n in reversed(nuevos): ancla.addnext(n)
            else:
                raise ValueError(f'operación desconocida {k}')
        except Exception as ex:
            errores.append((str(ex), json.dumps(o, ensure_ascii=False)[:120]))
    return errores


if __name__ == '__main__':
    args = sys.argv[1:]
    salida = None
    if '--salida' in args:
        i = args.index('--salida'); salida = args[i + 1]; del args[i:i + 2]
    cmd, path, specs = args[0], args[1], args[2:]
    doc = docx.Document(path)
    P = Plantillas(doc, '3.1 ', 'Lo más importante, en cinco', 'Vendes «por ti»', 'La pieza enseña el criterio')
    ops = sum((json.load(open(s)) for s in specs), [])
    err = run(doc, ops, P)
    for e in err: print('ERROR', *e)
    print(f'{len(ops)} operaciones, {len(err)} con error')
    if cmd == 'apply' and not err and salida:
        doc.save(salida); print('guardado', salida)
