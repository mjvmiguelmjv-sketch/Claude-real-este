"""Vuelca un .docx por ámbitos y párrafos, para escribir sustituciones exactas.
Cada línea es un párrafo: [ámbito] texto. En las tablas: [ámbito] <etiqueta de la fila> ¶ texto del párrafo."""
import sys, docx
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from docxedit import scopes, ptext, W_P, qn
d = docx.Document(sys.argv[1])
for name, els in scopes(d).items():
    for el in els:
        if el.tag == W_P:
            print(f'[{name}] {ptext(el)}')
        else:
            for tr in el.iter(qn('w:tr')):
                cells = tr.findall(qn('w:tc'))
                label = ptext(cells[0]) if len(cells) > 1 else ''
                for c in cells[1:] if len(cells) > 1 else cells:
                    for p in c.iter(W_P):
                        t = ptext(p)
                        if t.strip(): print(f'[{name}] <{label[:40]}> ¶ {t}')
