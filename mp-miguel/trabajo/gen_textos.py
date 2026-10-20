"""Monta el markdown de los textos de publicación de noviembre y diciembre.

    python gen_textos.py <volcado noviembre> <volcado diciembre> <salida.md> "<fecha>"

El pie de Instagram, el gancho escrito, el día, el pilar, la fase, el destino y el crédito de
cada reel salen del volcado de su Doc (scripts/volcado.py). Lo demás, de textos_plataformas.py.
"""
import re, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from textos_plataformas import T, FIJOS, MARCA, LANDING

CREDITOS = {  # los reels de Miguel no llevan la fila «Crédito»: va en su pie
    'R04': 'Diego Abreu, en Píldoras del Conocimiento (minuto 52:50), dicho en el vídeo, en el pie y en los textos.',
    'R11': 'Alex Hormozi, por su nombre, con la fuente de las fechas (acquisition.com/firm).',
    'R14': 'Luis Villanueva (Webpositer), el reel del ejemplo, con su permiso.',
    'R18': 'El modelo del clipper, de Alex Hormozi; las notas, de Píldoras del Conocimiento, con permiso.',
    'R21': 'La trampa viral, de Kallaway (@kallawaymarketing).',
    'R25': 'Kallaway (@kallawaymarketing), la idea de los dos tipos de personas.',
    'R31': 'Los datos de José Elías, con su fuente: The Objective, octubre de 2024 y agosto de 2025.',
}


def reels(path):
    L = open(path, encoding='utf-8').read().split('\n')
    idx = {}
    for l in L:
        m = re.match(r'\[INDICE\] <([A-Z]+\d+)> ¶ (.*)', l)
        if m: idx.setdefault(m.group(1), []).append(m.group(2))
    out = []
    for code, c in idx.items():
        if not c[0].startswith('Reel'): continue
        def get(lab):
            return [re.sub(r'^\[[^\]]+\] <[^>]*> ¶ ', '', l) for l in L if l.startswith(f'[{code}] <{lab}>')]
        pie, dentro = [], False
        for l in L:
            if l.startswith(f'[{code}] Pie de publicación'): dentro = True; continue
            if dentro:
                if l.startswith(f'[{code}] <> ¶ '): pie.append(l.split('¶ ', 1)[1])
                else: dentro = False
        destino = ' '.join(get('Destino del CTA'))
        pide = not re.match(r'(Ninguno|Sin llamada)', destino)
        cred = ' '.join(get('Crédito')).strip() or CREDITOS.get(code, 'No hace falta.')
        out.append(dict(code=code, dia=c[0].replace('Reel · ', ''), pilar=c[1], fase=c[2], titulo=c[4],
                        escrito=(get('Escrito') or [''])[0], pide=pide, credito=cred, pie=pie))
    return out


def pieza(r):
    t = T[r['code']]
    md = [f"### {r['code']} · {r['dia']}, {r['pilar']}, {r['fase']} · {r['titulo']}", '']
    md.append(f"- **Gancho escrito.** «{r['escrito'].strip('«»')}» (ningún texto lo repite)")
    md.append(f"- **Trabajo del pie.** {t['trabajo']}")
    if r['pide']:
        md.append('- **Plataformas.** Las cuatro. En Instagram, con la palabra; en TikTok, YouTube Shorts y Facebook, '
                  'el vídeo termina antes de la llamada hablada, como dicen sus notas de edición.')
        md.append('- **Destino.** DIAGNÓSTICO por WhatsApp. En YouTube contestas tú al comentario y mandas a tu landing; '
                  'en Facebook, el enlace a tu landing va en el texto.')
        md.append('- **Mensaje de respuesta a la palabra.** El automático de DIAGNÓSTICO, montado por ti en Instagram.')
    else:
        md.append('- **Plataformas.** Las cuatro, con el mismo vídeo.')
        md.append('- **Destino.** Ninguno: termina en la tesis, así que ningún texto pide nada.')
    md.append(f"- **Crédito.** {r['credito']}")
    pie = [p for p in r['pie'] if p.strip()]
    md.append(f"- **Instagram.** {pie[0]}")
    for p in pie[1:]: md.append(f"    - {p}")
    md.append(f"- **TikTok.** {t['tiktok']}")
    md.append(f"- **YouTube Shorts.** Título: «{t['titulo']}»")
    md.append(f"    - Texto: {t['yt']}")
    md.append('    - Vídeo relacionado: ninguno (no hay vídeo largo publicado al que mandar, y no se anuncia ninguno).')
    md.append(f"- **Facebook.** {t['facebook']}")
    md.append(f"- **Hashtags.** {' · '.join(FIJOS + t['cola'] + [MARCA])}")
    md.append('')
    return md


def main(nov, dic, salida, fecha):
    md = ['# Textos de publicación · noviembre y diciembre 2026', '',
          f'~~ MP Miguel · los textos de cada reel, uno por plataforma · v1 · {fecha}', '',
          'Los textos que van debajo de cada reel de noviembre y diciembre, uno por plataforma, listos para copiar: '
          'Instagram, TikTok, YouTube Shorts y Facebook. Salen de los guiones de noviembre r9 y diciembre r7. Las '
          'historias no llevan texto: lo que se lee va en la pantalla. No se ha programado nada en Metricool: es tu '
          'puerta. Y se han escrito semanas antes, así que el día de publicar se mira si hay algo de esa semana que '
          'contextualizar.', '',
          '## Cómo están escritos', '',
          '- **Instagram.** Es el pie de cada guion. Si la pieza pide, lleva tu llamada con DIAGNÓSTICO, y la palabra '
          'solo va aquí.',
          '- **YouTube Shorts.** Casi todo el peso en el título. Si la pieza pide, invita a comentar y contestas tú con '
          'tu landing, como dijiste el 20 oct; ningún enlace, porque en Shorts no se pueden pulsar.',
          f'- **Facebook.** Si la pieza pide, el enlace a tu landing va en el texto, porque ahí sí se pulsa: {LANDING} '
          '(confírmalo en los pendientes).',
          '- **TikTok.** Corto y sin pedir nada, hasta saber si tienes enlace en el perfil.',
          '- **Las piezas que no piden** no piden en ninguna plataforma.',
          '- **Ningún texto repite el gancho escrito**, y cada plataforma lleva el suyo.',
          '- **Hashtags.** En cuatro capas, y ninguno lleva fuera de tu cliente: la tabla está al final.',
          '- **Las horas** las decides tú: no se proponen.', '']
    for mes, path in (('Noviembre', nov), ('Diciembre', dic)):
        md += [f'## {mes}', '']
        for r in reels(path): md += pieza(r)
    md += ['## Los hashtags, por capas', '',
           'Una o dos de cada capa. No suben una pieza floja: le dicen a la plataforma de qué va y para quién es. Ninguno '
           'lleva a creadores de contenido ni a gestores de redes, que no te compran.', '',
           '| Capa | Cuáles | A quién llevan |', '|---|---|---|',
           '| De tendencia | #empresarios | A cualquier empresario: el más ancho de los cuatro |',
           '| De nicho | #marketingB2B · #ventasB2B | Al que vende a empresas: fundadores y socios de agencias y consultoras |',
           '| De cola larga | Dos por pieza: #servicioshighticket, #llamadadeventas, #ventasconsultivas, #clientesB2B, '
           '#marcapersonalB2B, #contenidoB2B, #contenidodenicho, #viralidaddenicho o #podcastB2B | Al que vende con '
           'llamada de ventas y tickets altos, que es tu cliente |',
           f'| De marca | {MARCA} | A quien ya te sigue. Por decidir |', '',
           '## Pendientes', '',
           '| Pieza | Qué falta | Qué bloquea |', '|---|---|---|',
           f'| Facebook, las que piden | Confirmar que tu landing es {LANDING}: es tu web publicada, y la v40 está sin subir | El enlace de Facebook |',
           '| Las que piden | El texto de tu mensaje automático de DIAGNÓSTICO, para revisarlo: está montado en Instagram y no está en el proyecto | No bloquea |',
           '| YouTube Shorts y Facebook | Tus reglas decían que las piezas con palabra van solo a Instagram; el 20 oct dijiste que en YouTube contestas tú y mandas a tu landing. Van a las cuatro, y en TikTok y Facebook, sin la llamada hablada. Por decidir si te vale | No bloquea |',
           '| TikTok | Si tienes enlace en tu perfil de TikTok: entonces las piezas que piden pueden cerrar con «el diagnóstico, en el enlace de mi perfil» | No bloquea |',
           f'| Todas | El hashtag de tu marca: {MARCA}. Por decidir | No bloquea |',
           '| R04 | El permiso de Píldoras del Conocimiento para el fragmento de Diego Abreu | La publicación de R04 |',
           '| R14 | El permiso de Luis, reconfirmado, y su usuario exacto | La publicación de R14 |',
           '| R18 | Qué grabación de Píldoras se enseña y el permiso del invitado | La publicación de R18 |',
           '| Todas | Las horas, que las decides tú; y tu visto bueno a estos textos antes de tocar Metricool | La programación |',
           '| Todas | El día de publicar, mirar si hay algo de esa semana que contextualizar | No bloquea |', '']
    open(salida, 'w', encoding='utf-8').write('\n'.join(md))
    print('textos:', salida)


if __name__ == '__main__':
    main(*sys.argv[1:5])
