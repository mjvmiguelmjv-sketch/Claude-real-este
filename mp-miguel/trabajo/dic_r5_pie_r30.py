"""Ronda r5 de diciembre: añade a R30 el pie que no tiene (docxedit solo sustituye).
Clona el título «Pie de publicación» y la tabla del pie de R31 (mismo formato) y los
pone al final de R30. Uso: python3 dic_r5_pie_r30.py entrada.docx salida.docx
Se aplica DESPUÉS de dic_r5_edits.json."""
import sys, copy, docx
sys.path.insert(0, '/home/user/Claude-real-este/mp-miguel/scripts')
from docxedit import scopes, ptext, W_P, qn
from piezas import set_p  # deja un solo run con el formato del primero

PIE = [
    'Te enseñan el vídeo de tu competencia con más visitas y te dicen: «hagamos uno así». Seguro que te ha pasado.',
    'Antes hay que ver qué le funciona a esa cuenta según a quién le habla: cuál es su producto, High Ticket o Low Ticket. Si vendes High Ticket y contratas a alguien que mira qué es viral en tu sector y lo copia, te va a llenar el embudo de curiosos.',
    'En vez de copiar el vídeo, analiza qué defiende esa cuenta y en qué de esas cosas no estás de acuerdo. El error es copiarlo sin haberlo analizado antes.',
]

d = docx.Document(sys.argv[1]); sc = scopes(d)
if any(el.tag == W_P and ptext(el) == 'Pie de publicación' for el in sc['R30']):
    sys.exit('R30 ya tiene pie: no se toca')
r31 = sc['R31']
i = next(k for k, el in enumerate(r31) if el.tag == W_P and ptext(el) == 'Pie de publicación')
head, tbl = copy.deepcopy(r31[i]), copy.deepcopy(r31[i + 1])
tc = tbl.findall(qn('w:tr'))[0].findall(qn('w:tc'))[-1]
ps = list(tc.iter(W_P)); proto = ps[0]
for p in ps: p.getparent().remove(p)
for txt in PIE:
    tc.append(set_p(copy.deepcopy(proto), txt))
last = sc['R30'][-1]
last.addnext(head); head.addnext(tbl)
d.save(sys.argv[2]); print('pie de R30 añadido ->', sys.argv[2])
