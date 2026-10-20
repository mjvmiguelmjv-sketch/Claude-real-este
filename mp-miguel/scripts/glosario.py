"""Pasa el glosario de la casa (reglas, apartado 8) al texto libre de un Doc de mes.

    python glosario.py <entrada.docx> <salida.docx>

Solo cambia expresiones concretas del texto que escribió Claude (fichas y notas);
las etiquetas del formato de Miguel («Triggers usados», «Molde y trigger») no se tocan.
"""
import sys
import docx
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from docxedit import body_els, paragraphs, ptext, replace_in_p

CAMBIOS = [
    (' (SOP-08a)', ''),
    ('con la regla del 5x o un outlier score de 5 o más por ser Alcance',
     'con cinco veces sus seguidores o un múltiplo de 5 o más, por ser Alcance'),
    ('umbral de Alcance: outlier ≥ 5 o regla del 5x',
     'umbral de Alcance: múltiplo de 5 o más, o cinco veces sus seguidores'),
    ('trigger de atención', 'disparador de atención'),
    ('rótulos, triggers y pies', 'rótulos, disparadores y pies'),
]

d = docx.Document(sys.argv[1])
n = {}
for p in paragraphs(body_els(d)):
    for old, new in CAMBIOS:
        while old in ptext(p):
            replace_in_p(p, old, new); n[old] = n.get(old, 0) + 1
d.save(sys.argv[2])
for old, k in n.items(): print(f'{k:3d} × {old!r}')
print('->', sys.argv[2])
