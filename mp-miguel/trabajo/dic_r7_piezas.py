"""Diciembre r7: las piezas del 22 al 25 de diciembre, que a Miguel no le gustaban (20 oct, noche).

    python dic_r7_piezas.py <diciembre r6 .docx> <sustitución r2 .docx> <salida.docx>

Salen N22 y R38 (reels) y S22 y NS4 (historias). Entran, en los mismos sitios:
- N05, «La pieza que le cambia el problema», de la sustitución, con sus frases del 18 oct;
- N16, «El director de una agencia que tú pagas», de la sustitución: la otra opción que la
  crítica del 19 oct proponía para el sitio de R38;
- NS8 y NS9, secuencias nuevas con dos ideas de su documento del 8 oct sin usar
  (3.2.4, el boca a boca; 3.3.2, los proyectos terminados).
Las piezas de la sustitución se montan con piezas.build, como en la primera pasada, y las
secuencias nuevas, con las tablas de NS7. El índice pone al día sus cuatro filas.
"""
import copy, sys
import docx
sys.path.insert(0, '/home/user/Claude-real-este/mp-miguel/scripts')
from docxedit import body_els, ptext, style, W_P, qn
from piezas import Plantilla, read_piece, build, para, table, fill_cell
from mover_pieza import grupo, tabla_indice, fila

W_TR, W_TC = qn('w:tr'), qn('w:tc')
ICP = ('Fundador o socio visible de una agencia o consultora B2B, de cinco a treinta personas, con clientes '
       'que le pagan varios miles de euros y no le compran sin hablar antes. (ficha 4.1)')
MOTIVO = '20 oct, noche: las piezas del 22 al 25 no te gustaban'
CTA_RUTA = ('DIAGNÓSTICO por WhatsApp (comentario o respuesta → mensaje privado automático con el enlace a '
            'WhatsApp → contestas tú → el diagnóstico, una página con tres hallazgos)')


# ---------- utilidades sobre los bloques de read_piece ----------

def tabla_tras(blocks, etiqueta):
    i = next(i for i, b in enumerate(blocks) if b[0] == 'p' and b[1].startswith(etiqueta))
    return blocks[i + 1][1]

def pon(rows, etiqueta, textos):
    for r in rows:
        if r and r[0] and r[0][0].strip() == etiqueta:
            r[1:] = [textos if isinstance(textos, list) else [textos]]
            return
    raise KeyError(etiqueta)

def fase(blocks, empieza):
    i = next(i for i, b in enumerate(blocks) if b[0] == 'p' and b[1].startswith(empieza))
    return i


# ---------- N05 ----------

def n05(b):
    f = tabla_tras(b, 'Ficha de la')
    pon(f, 'Guion del banco', 'Nuevo: sale de tu documento de ideas raíz del 8 oct (raíz 1, concepto 3). '
                              'PENDIENTE: darlo de alta como guion en el banco.')
    pon(f, 'Frase de la pieza', '«Tu contenido debe enseñar a tu comprador que su problema no era el que pensaba.» '
                                'Es tu frase de la fase 3.')
    pon(f, 'ICP', ICP)
    pon(f, 'Dolor exacto', '«Tengo que explicar mucho lo que hago antes de que alguien lo entienda» — fuente: ficha.md, '
                           'dolor 9 (Miguel). Va contado como escena, la de tu fase 1: el cliente que llega a la llamada '
                           'convencido de que sabe lo que le pasa.')
    pon(f, 'Destino del CTA', f'{CTA_RUTA}, mirando si tus piezas le enseñan a tu comprador lo que realmente le pasa. '
                              'Encaja: el diagnóstico mira primero qué vende, quién le compra y qué pregunta antes de '
                              'hacerlo, y después las últimas piezas (ficha 8.3).')
    d = tabla_tras(b, 'Disparadores usados')
    pon(d, 'Atención', 'Patrón roto. El hablado separa lo que pide el cliente de lo que le pasa, cuando lo habitual es '
                       'contestar lo que pide')
    pon(d, 'Identificación', 'Dolor identitario. Fase 1: el dolor 9 contado como escena, «tu cliente llega a la llamada '
                             'convencido de que sabe lo que le pasa»')
    pon(d, 'Tensión', 'Aversión a la pérdida. Fase 1: te pasas la llamada reforzando lo que pensaba tu cliente, y después '
                      'ves que no tenía ese problema')
    pon(d, 'Credibilidad', 'Autoridad en activo. Fase 2: lo que piensa tu comprador que le pasa (le faltan visitas), lo que '
                           'le pasa de verdad y lo que por eso no publicas (ficha 2.2 y 2.3). Afirma, así que lleva '
                           'credibilidad')
    g = tabla_tras(b, 'El gancho')
    pon(g, 'Escrito', 'Cómo enseñarle a tu cliente que su problema no era el que pensaba.')
    pon(g, 'Hablado', '«Lo que tu cliente pide y lo que le pasa casi nunca coinciden.»')
    pon(g, 'Molde y disparador', '«Cómo» muy concreto en el escrito, con tu frase de la fase 3; en el hablado, la frase '
                                 'con la que abres tu locución · disparador de atención: patrón roto.')
    pon(g, 'De dónde sale cada uno', 'escrito: propio, tu frase de la fase 3 vuelta «Cómo» · hablado: tuyo, la primera '
                                     'frase de tu locución (era el hablado del gancho B) · visual: molde ajeno de oficio '
                                     '(la pizarra que ya se está escribiendo cuando entra el plano), de reels de pizarra '
                                     'de cualquier nicho.')
    pon(g, 'Las tres comprobaciones', '¿Funciona solo? Sí: promete cómo enseñarle algo que su cliente no ve, y no lo dice · '
                                      '¿Sobrevive sin la sorpresa? Sí: aunque lo sepa, le falta cómo encontrar esa '
                                      'distancia en su caso · ¿Lo entiende quien llega hoy? Sí: «cliente» y «problema» '
                                      'son palabras de cualquiera que venda.')
    viejo = next(r for r in g if r[0][0].strip() == 'Descartados')[1]
    pon(g, 'Descartados', ['«Tu cliente pide una cosa. Su problema es otra.» (el escrito de antes: es un paralelismo, y '
                           'tu voz los corta) · «Tu cliente llega a la llamada convencido de que sabe lo que le pasa.» (el '
                           'hablado de antes: tu locución abre con otra frase) · ' + ' '.join(viejo)])
    pon(g, 'Gancho B, para probar', 'Escrito: «¿Qué le pasa de verdad al cliente que llega a tu llamada de ventas?» · '
                                    'Hablado: «Tu cliente llega a la llamada convencido de que sabe lo que le pasa.» '
                                    '(familia: pregunta del comprador).')
    pon(g, 'Elección', 'Elegida el 20 oct, por la noche: el escrito pasa a un «Cómo» con tu frase de la fase 3, y el '
                       'hablado es la frase con la que abres tu locución. Si prefieres el de antes, está en Descartados.')
    i1 = fase(b, 'FASE 1.')
    t1 = b[i1 + 1][1]
    pon(t1, 'Locución', '«Lo que tu cliente pide y lo que le pasa casi nunca coinciden. Te ha pasado que tu cliente llega a '
                        'la llamada convencido de que sabe lo que le pasa y tú te has pasado toda la llamada reforzando lo '
                        'que él pensaba. Y luego más tarde pensaste que realmente no tenía ese problema.»')
    pon(t1, 'Nota de edición', 'Los primeros segundos, el gancho escrito como rótulo de entrada, en texto simple: «Cómo '
                               'enseñarle a tu cliente que su problema no era el que pensaba.» Se va al terminar la primera '
                               'frase. Sin música.')
    i2 = fase(b, 'FASE 2.')
    b[i2] = ('p', 'FASE 2. EL TRUCO (Hack / Tip), lo que piensa tu comprador y lo que le pasa')
    t2 = b[i2 + 1][1]
    pon(t2, 'Locución', '«Mi comprador normalmente piensa que le faltan visitas. Lo que le falta casi siempre es que el que '
                        'puede pagarle vea lo que ya tiene. Por eso no publico cómo tener más visitas.»')
    pon(t2, 'Fondo, a cámara (A-ROLL)', 'Escribe «LE PASA» debajo de «PIDE» y traza una flecha de una a otra. En «le faltan '
                                        'visitas» escribe «VISITAS» junto a «PIDE»; en «vea lo que ya tiene», «LO QUE YA '
                                        'TIENE» junto a «LE PASA».')
    pon(t2, 'Nota de edición', 'Sin rótulo: se lee la pizarra.')
    i3 = fase(b, 'FASE 3.')
    b[i3] = ('p', 'FASE 3. EL CRITERIO (How-To), lo que tiene que hacer tu contenido')
    t3 = b[i3 + 1][1]
    pon(t3, 'Fondo, a cámara (A-ROLL)', 'Golpea dos veces la flecha con el capuchón y vuelve a la lente con la frase.')
    pon(t3, 'Nota de edición', 'Rótulo a dos líneas con la voz: «Tu contenido debe enseñar a tu comprador / que su '
                               'problema no era el que pensaba». Sin animación.')
    llamada = ('«Si quieres que personalmente analice si tus piezas le enseñan a tu comprador lo que realmente le pasa, '
               'comenta DIAGNÓSTICO y hablamos por privado.»')
    b[i3 + 2:i3 + 2] = [
        ('p', 'FASE 4. LA PETICIÓN (CTA), el diagnóstico'),
        ('t', [[['Locución'], [llamada]],
               [['Fondo, a cámara (A-ROLL)'], ['Mismo plano, la pizarra entera detrás. Corte seco al terminar.']],
               [['Nota de edición'], ['«DIAGNÓSTICO» en grande al decirlo, hasta el corte. La palabra solo va en '
                                      'Instagram: en TikTok, Shorts y Facebook el reel termina en la fase 3.']]]),
        ('p', 'Pie de publicación'),
        ('t', [[[llamada.strip('«»'), '—',
                 'Tu contenido debe enseñar a tu comprador que su problema no era el que pensaba.',
                 'Mi comprador normalmente piensa que le faltan visitas. Lo que le falta casi siempre es que el que puede '
                 'pagarle vea lo que ya tiene. Por eso no publico cómo tener más visitas.']]]),
    ]
    return b


# ---------- N16 ----------

def n16(b):
    f = tabla_tras(b, 'Ficha de la')
    pon(f, 'Guion del banco', 'Nuevo: sale de tu documento de ideas raíz del 8 oct (raíz 4, concepto 2). '
                              'PENDIENTE: darlo de alta como guion en el banco.')
    pon(f, 'Estructura', 'EL AVANCE, bloques: EL PROBLEMA (Problem) → LA REVELACIÓN (Breakthrough) → EL DESGLOSE (Fix / '
                         'Takeaway) · difícil. Elegida aquí, porque es una pieza suelta: lo que entrega es un cambio de '
                         'forma de ver la delegación, que cabe en una frase. Sin CTA: termina en el desglose, y el pie, en '
                         'la tesis.')
    pon(f, 'ICP', ICP)
    pon(f, 'Dolor exacto', '«He intentado delegar y fue un desastre» — fuente: ficha.md, dolor 33 (Miguel). Va contado '
                           'como escena, la del lunes. Literal era el hablado de R38, que sale del mes.')
    pon(f, 'Destino del CTA', 'Ninguno: termina en la tesis. El diagnóstico no mira quién decide qué en tu contenido '
                              '(ficha 8.3), así que una llamada prometería algo que no da.')
    pon(f, 'Objetivo y métrica', 'Que llegue a empresarios que han delegado su contenido y lo siguen decidiendo todo. Se '
                                 'mide en alcance cualificado: quién comenta y quién te escribe después de verla.')
    d = tabla_tras(b, 'Disparadores usados')
    pon(d, 'Atención', 'Concreción escénica. Hablado: cada lunes te pregunta qué publicar')
    g = tabla_tras(b, 'El gancho')
    pon(g, 'Escrito', 'Cómo delegar el contenido de tu empresa sin seguir decidiéndolo todo tú.')
    pon(g, 'Hablado', '«Contrataste a alguien para hacer tu contenido, y cada lunes te pregunta qué publicar.»')
    pon(g, 'Visual', 'Cámara frontal en mano, sentado al escritorio: Miguel pasa con el pulgar una lista larga de mensajes '
                     'en un segundo móvil, difuminada, y lo deja boca abajo sobre la mesa en «qué publicar». El móvil '
                     'cayendo boca abajo es lo primero que se ve.')
    pon(g, 'Molde y disparador', '«Cómo» muy concreto en el escrito, con «de tu empresa» para que pare al que paga y no '
                                 'al que lo hace; en el hablado, la escena del lunes, con lo que ya probó tu comprador '
                                 '(contratar a alguien) · disparador de atención: concreción escénica.')
    pon(g, 'De dónde sale cada uno', 'escrito: propio, de tu frase del concepto 2 de la raíz 4, vuelta «Cómo» · hablado: '
                                     'propio, la escena del dolor 33 · visual: molde ajeno de oficio (el gesto de dejar el '
                                     'móvil boca abajo), de reels espontáneos de cualquier nicho.')
    pon(g, 'Anillos', 'gancho 3 / pieza 3 / cierre 3. El rótulo lo para el que paga a alguien por el contenido de su '
                      'empresa; el cuerpo le habla al empresario que lo ha delegado; el pie lleva la condición, la llamada '
                      'de ventas.')
    pon(g, 'Las tres comprobaciones', '¿Funciona solo? Sí: promete cómo dejar de decidirlo todo, y no lo dice · '
                                      '¿Sobrevive sin la sorpresa? Sí: aunque lo sepa, le falta qué decisiones son suyas '
                                      'y cuáles no · ¿Lo entiende quien llega hoy? Sí: «delegar» y «decidir» son palabras '
                                      'de cualquier empresario.')
    pon(g, 'Descartados', '«Pagas a alguien y sigues decidiendo tú.» (el escrito de antes: no es un «Cómo» ni una pregunta, '
                          'que es lo que deja tu voz) · «Delegar no puede darte más trabajo» (era el escrito de R38, que '
                          'sale del mes) · «Has intentado delegar y fue un desastre» (era el hablado de R38, y es el de R58 '
                          'y R78) · «Veinte decisiones cada semana» (lleva cifra) · «Tu equipo de contenido no debería '
                          'necesitarte» (niega en seco).')
    pon(g, 'Gancho B, para probar', 'Escrito: «Qué partes de tu contenido no tendrías que tocar.» · Hablado: «Tú deberías '
                                    'aparecer únicamente donde tu experiencia es imprescindible.» (familia: «cómo» muy '
                                    'concreto). Si se elige el B, la fase 1 sigue con «Pero contrataste a alguien para '
                                    'hacer tu contenido, y cada lunes te pregunta qué publicar», y la fase 3 queda como eco '
                                    'del hablado.')
    pon(g, 'Elección', 'Elegida el 20 oct, por la noche: el escrito pasa a un «Cómo» con el filtro dentro («de tu '
                       'empresa»), como dejas tú los escritos; el hablado es el de la favorita, con «qué publicar». Si '
                       'prefieres el de antes, está en Descartados.')
    i1 = fase(b, 'FASE 1.')
    t1 = b[i1 + 1][1]
    pon(t1, 'Locución', '«Contrataste a alguien para hacer tu contenido, y cada lunes te pregunta qué publicar. Entonces '
                        'revisas el guion, el rótulo y la música, y al final decides tú.»')
    pon(t1, 'Fondo, a cámara (A-ROLL)', 'Cámara frontal del móvil, en mano, sentado al escritorio. Deja el segundo móvil '
                                        'boca abajo en «qué publicar» y cuenta con los dedos en «el guion, el rótulo y la '
                                        'música».')
    pon(t1, 'Nota de edición', 'Los primeros segundos, el gancho escrito como rótulo de entrada, en texto simple: «Cómo '
                               'delegar el contenido de tu empresa sin seguir decidiéndolo todo tú.» La lista de mensajes, '
                               'difuminada entera. Sin música.')
    i2 = fase(b, 'FASE 2.')
    pon(b[i2 + 1][1], 'Nota de edición', 'Rótulo a dos líneas en la pausa del final: «Director de una agencia / que tú '
                                         'mismo pagas».')
    i3 = fase(b, 'FASE 3.')
    t3 = b[i3 + 1][1]
    pon(t3, 'Locución', '«Delegar debería quitar decisiones de tu agenda, no añadir reuniones. Tú deberías aparecer '
                        'únicamente donde tu experiencia es imprescindible, y desaparecer del resto del proceso. Y la '
                        'persona que lleva tu contenido debería aprender cada mes más sobre tu negocio, y preguntarte '
                        'menos.»')
    pon(t3, 'Nota de edición', 'Rótulo a dos líneas en «no añadir reuniones»: «Quitar decisiones de tu agenda / no añadir '
                               'reuniones». Se deja un segundo de aire al final.')
    ip = next(i for i, x in enumerate(b) if x[0] == 'p' and x[1].startswith('Pie de publicación'))
    b[ip + 1] = ('t', [[['Si tienes que revisar veinte decisiones pequeñas cada semana, te has convertido en director de '
                         'una agencia que tú mismo pagas.',
                         'Delegar debería quitar decisiones de tu agenda, no añadir reuniones. Si vendes un servicio que '
                         'se cierra en una llamada de ventas, tu tiempo vale más en esa llamada que revisando rótulos.']]])
    return b


# ---------- NS8 y NS9: secuencias nuevas ----------

def r(etiqueta, *textos):
    return [[etiqueta], list(textos)]

NS8 = {
    'titulo': 'NS8 Te recomiendan, y te buscan',
    'linea': 'Demostración · MOFU · cierre blando',
    'ficha': [
        r('Guion del banco', 'Nuevo, sin código todavía: la idea 3.2.4 de tu documento del 8 oct, la 20 del banco de '
                             'ideas del 13 oct, contada con DETRÁS DE LA PANTALLA. PENDIENTE: darlo de alta como guion en '
                             'el banco.'),
        r('Guion del banco', f'Entra en el calendario el martes 22 de diciembre, en el sitio de S22 ({MOTIVO}).'),
        r('Estructura', 'DETRÁS DE LA PANTALLA, 4 pantallas: 1 la grabación de pantalla ya empezada, sin explicar todavía '
                        'qué se ve → 2 lo que acaba de pasar y por qué le importa → 3 qué se hace con eso → 4 el cierre. '
                        'Hueco que abre la 1: qué es eso que está en pantalla. Va con ella porque el argumento se ve en '
                        'directo: una búsqueda. Cierre blando: el CTA una vez, en la 4. Sin elemento interactivo: la '
                        'estructura no lo pide (20 oct).'),
        r('Idea', 'Cuando alguien te recomienda, el recomendado te busca antes de escribirte, y lo que encuentra confirma '
                  'la recomendación o la deja en un nombre. Es tu frase 3.2.4: «El boca a boca funciona mejor cuando, '
                  'después de recomendarte, el comprador encuentra algo que confirma la recomendación.»'),
        r('Idea', 'De dónde sale. Tu frase 3.2.4, literal en la pantalla 3; el dolor 8 de tu ficha (4.6); y tu método: el '
                  'contenido sale de lo que te preguntan en la llamada de ventas (6.4), que es lo que tendría que '
                  'encontrar quien te busca. El banco de ideas del 13 oct la proponía como una de las tres de muestra.'),
        r('Idea', 'Material real. La búsqueda de tu propio nombre, grabada por ti en tu móvil, como la haría el '
                  'recomendado, y tu perfil. Ningún dato de nadie más: si la búsqueda saca a otra persona, se difumina.'),
        r('Idea', 'Nivel de entrega. Criterio: qué tiene que encontrar quien te busca después de una recomendación, y '
                  'cómo comprobarlo hoy.'),
        r('Idea', 'Estado. Concepto vivo · idea disponible · este guion, escrito y no publicado.'),
        r('Idea', 'Autor que se acredita. Propia: la frase es tuya (documento del 8 oct, 3.2.4).'),
        r('Frase de la pieza', 'El boca a boca funciona mejor cuando, después de recomendarte, el comprador encuentra algo '
                               'que confirma la recomendación.'),
        r('Concepto', 'Raíz 3 · No creamos autoridad. Hacemos visible la que ya tienes · concepto 3.2 · El coste de la '
                      'autoridad invisible.'),
        r('Formato', 'Secuencia de historias (8.9), muda: grabación de la pantalla de tu móvil, vídeo tuyo sin sonido y '
                     'fondo liso en el azul de la casa.'),
        r('ICP', 'El de la ficha (4.1), que ya sigue la cuenta.'),
        r('Dolor exacto', '«Dependo del boca a boca y es impredecible» — fuente: ficha.md, dolor 8 (Miguel). Va en la '
                          'pantalla 1 como escena, lo que ya vive quien depende de él: que le recomienden. No lo usa '
                          'ninguna otra pieza de noviembre ni de diciembre.'),
        r('Pilar', 'Demostración: la búsqueda se ve en directo.'),
        r('Anillo', '2: el que vende con llamada de ventas y vive de recomendaciones. La pantalla 1 abre en el 3 (cualquiera '
                    'al que recomienden) y la 3 vuelve al 2, con la llamada de ventas dentro.'),
        r('Fase', 'MOFU.'),
        r('Tipo de cierre', 'Blando. La semana cierra en duro el sábado 26, con S24.'),
        r('CTA', 'Responde DIAGNÓSTICO → el mensaje automático con el enlace a tu WhatsApp → contestas tú → la página con '
                 'tres hallazgos (8.5), mirando qué encuentra de ti quien te busca después de que le hablen de ti. Sin '
                 'decir si es gratis ni cuándo contestas. El mensaje automático ya está montado en Instagram (20 oct).'),
        r('Objetivo y métrica', 'Que el que vive de recomendaciones se busque como le buscaría el recomendado, y responda. '
                                'Se mide en respuestas con DIAGNÓSTICO.'),
        r('Fuentes', 'Sin cifras.'),
        r('Crédito', 'Ninguno.'),
        r('Transformación', 'De confiar en que la recomendación basta a comprobar qué encuentra quien le busca después.'),
        r('Referencia', 'Ninguna. Vídeos de referencia: por formato, no por pieza (12 oct); no frena la escritura ni el '
                        'rodaje.'),
        r('Triggers usados', 'Atención: Bucle de curiosidad. Pantalla 1: la búsqueda ya empezada y «antes de escribirte, '
                             'hace esto», sin decir qué; lo paga la 2'),
        r('Triggers usados', 'Identificación: Dolor identitario. Pantalla 1: que te recomienden, que es lo que ya vive quien '
                             'depende del boca a boca'),
        r('Triggers usados', 'Tensión: Aversión a la pérdida. Pantalla 2: si no encuentra nada que confirme lo que le '
                             'contaron, probablemente no te escriba'),
        r('Triggers usados', 'Credibilidad: Demostración en directo. Pantallas 1 y 2: tu propia búsqueda, en tu móvil, sin '
                             'cortes'),
        r('Triggers usados', 'Acción: Siguiente paso único. Pantalla 4: una palabra y lo que analizas'),
        r('Número de pantallas', '4.'),
        r('¿Es nueva de verdad?', 'Sí. Ninguna pieza de noviembre ni de diciembre habla del boca a boca ni de lo que '
                                  'encuentra quien te busca después de una recomendación. Lo más cerca: NS2 (13 nov), que '
                                  'enseña tu bio con tus tres preguntas, y R28 (9 dic), el perfil en semáforo; aquí no se '
                                  'audita un perfil, se enseña lo que hace el recomendado. N05, el mismo día, va del '
                                  'problema que cree tener tu cliente: otra idea.'),
    ],
    'pantallas': [
        ('PANTALLA 1, la grabación de pantalla ya empezada, sin explicar todavía qué se ve', [
            r('Texto en pantalla', '«Te han recomendado. / Y antes de escribirte, hace esto.»'),
            r('Fondo', 'Grabación de la pantalla de tu móvil, ya empezada: en el buscador de Instagram se va escribiendo tu '
                       'nombre, letra a letra, y sale tu perfil. La grabas tú, despacio y sin cortes. Si sale otra persona '
                       'con tu nombre, se difumina.'),
            r('Nota de edición', 'Un bloque en dos renglones, arriba, por debajo de la franja del nombre. Nada en el tercio '
                                 'de abajo. Se sube como vídeo de diez segundos.'),
        ]),
        ('PANTALLA 2, lo que acaba de pasar y por qué le importa', [
            r('Texto en pantalla', '«Si en tu perfil no encuentra nada que confirme lo que le contaron de ti, probablemente '
                                   'no te escriba.»'),
            r('Fondo', 'La misma grabación sigue: entra en tu perfil y baja despacio por tus piezas.'),
            r('Nota de edición', 'Un bloque, arriba, en tres renglones como mucho. Todo en los dos tercios de arriba.'),
        ]),
        ('PANTALLA 3, qué se hace con eso', [
            r('Texto en pantalla', '«El boca a boca funciona mejor cuando, después de recomendarte, el comprador encuentra '
                                   'algo que confirma la recomendación.» · «Haz esto hoy: busca tu nombre como te buscaría '
                                   'él, y mira si alguna pieza contesta lo que te preguntaría en la llamada de ventas.»'),
            r('Fondo', 'Fondo liso en el azul de la casa: es la pantalla de valor y manda el texto. Se sube como vídeo quieto '
                       'de doce segundos, para que dé tiempo a leerla sin pararla.'),
            r('Nota de edición', 'Dos bloques. El primero, tu frase, en cuerpo mayor, con «confirma la recomendación» en '
                                 'negrita; el segundo, la orden, debajo. Todo en los dos tercios de arriba.'),
        ]),
        ('PANTALLA 4, el cierre', [
            r('Texto en pantalla', '«Responde DIAGNÓSTICO / y analizo qué encuentra de ti quien te busca.»'),
            r('Fondo', 'Vídeo mudo: tú en la mesa, mirando el móvil y apuntando algo en el cuaderno, sin que se lea.'),
            r('Nota de edición', 'Una sola frase, en dos renglones, y nada más en la pantalla. En el primero, «Responde '
                                 'DIAGNÓSTICO», con DIAGNÓSTICO en grande y la flecha apuntando a la barra de respuesta; en '
                                 'el segundo, «y analizo qué encuentra de ti quien te busca.», en cuerpo de rótulo. La '
                                 'frase, en el tercio de en medio: al tercio de abajo solo baja la flecha.'),
        ]),
    ],
}

NS9 = {
    'titulo': 'NS9 Las ideas que ya tienes en tus proyectos',
    'linea': 'Autoridad · MOFU · cierre blando',
    'ficha': [
        r('Guion del banco', 'Nuevo, sin código todavía: la idea 3.3.2 de tu documento del 8 oct, la 24 del banco de ideas '
                             'del 13 oct, contada con EL AVANCE. PENDIENTE: darlo de alta como guion en el banco.'),
        r('Guion del banco', f'Entra en el calendario el jueves 24 de diciembre, en el sitio de NS4 ({MOTIVO}). Se '
                             'programa por la mañana.'),
        r('Estructura', 'EL AVANCE, 4 pantallas: 1 el problema tal y como lo ve quien mira, con sus palabras → 2 la '
                        'revelación, dicha sin adornos → 3 el desglose: qué cambia si se acepta → 4 el cierre. Hueco que '
                        'abre la 1: si lo tengo tan claro, qué se me está escapando. La revelación se puede discutir: casi '
                        'todo el mundo busca ideas en lo que funciona en su sector. Cierre blando: el CTA una vez, en la 4. '
                        'Sin elemento interactivo: la estructura no lo pide (20 oct).'),
        r('Idea', 'Antes de buscar ideas para enero en lo que funciona en tu sector, abre el último proyecto que cerraste: '
                  'las preguntas que te hizo ese cliente antes de contratarte y las decisiones que tomaste son tu '
                  'contenido. Es tu frase 3.3.2: «Tus mejores ideas probablemente están enterradas en proyectos '
                  'terminados.»'),
        r('Idea', 'De dónde sale. Tu frase 3.3.2, literal en la pantalla 2; el dolor 24 de tu ficha (4.6); y tu método: el '
                  'contenido sale de las preguntas y objeciones de tus clientes (6.4). El banco de ideas del 13 oct la '
                  'contaba como consejo, en pantalla dividida; aquí va en historias, el último jueves antes de fin de año.'),
        r('Idea', 'Material real. Tu carpeta de proyectos en el ordenador, abierta, con los nombres de archivo y de cliente '
                  'desenfocados. No se lee ningún documento de un cliente.'),
        r('Idea', 'Nivel de entrega. Criterio y un paso: dónde buscar las ideas de enero y qué apuntar.'),
        r('Idea', 'Estado. Concepto vivo · idea disponible · este guion, escrito y no publicado.'),
        r('Idea', 'Autor que se acredita. Propia: la frase es tuya (documento del 8 oct, 3.3.2).'),
        r('Frase de la pieza', 'Tus mejores ideas probablemente están enterradas en proyectos terminados.'),
        r('Concepto', 'Raíz 3 · No creamos autoridad. Hacemos visible la que ya tienes · concepto 3.3 · Tu banco de '
                      'autoridad ya existe. Sale S22, que era de este concepto, y lo sigue cubriendo esta.'),
        r('Formato', 'Secuencia de historias (8.9), muda: vídeo tuyo sin sonido y fondo liso en el azul de la casa.'),
        r('ICP', 'El de la ficha (4.1), que ya sigue la cuenta.'),
        r('Dolor exacto', '«Publico contenido de valor y no pasa nada» — fuente: ficha.md, dolor 24 (Miguel). Va en la '
                          'pantalla 1 pasado a tú, con lo que el comprador ya probó: buscar ideas en lo que funciona en su '
                          'sector. Lo usó S04 (10 nov): otro mes.'),
        r('Pilar', 'Autoridad.'),
        r('Anillo', '2: el que vende servicios por proyectos y ya tiene clientes. La pantalla 1 abre en el 3 (cualquiera '
                    'que publique para su negocio) y la 3 vuelve al 2, con lo que te pregunta un cliente antes de '
                    'contratarte.'),
        r('Fase', 'MOFU.'),
        r('Tipo de cierre', 'Blando. Es Nochebuena: sin tensión, y la semana cierra en duro el sábado 26, con S24.'),
        r('CTA', 'Responde DIAGNÓSTICO → el mensaje automático con el enlace a tu WhatsApp → contestas tú → la página con '
                 'tres hallazgos (8.5), mirando si tus piezas salen de lo que te preguntan tus clientes o de lo que '
                 'publica tu sector. Sin decir si es gratis ni cuándo contestas. El mensaje automático ya está montado en '
                 'Instagram (20 oct).'),
        r('Objetivo y métrica', 'Que el que busca ideas para enero en su sector mire primero sus proyectos, y responda. Se '
                                'mide en respuestas con DIAGNÓSTICO.'),
        r('Fuentes', 'Sin cifras.'),
        r('Crédito', 'Ninguno.'),
        r('Transformación', 'De buscar ideas en lo que funciona en su sector a sacarlas de las preguntas y las decisiones de '
                            'sus propios proyectos.'),
        r('Referencia', 'Ninguna. Vídeos de referencia: por formato, no por pieza (12 oct); no frena la escritura ni el '
                        'rodaje.'),
        r('Triggers usados', 'Atención: Patrón roto. Pantalla 1: buscar ideas en lo que funciona en tu sector, contado como '
                             'lo normal; la 2 dice que las tienes en otro sitio'),
        r('Triggers usados', 'Identificación: Dolor identitario. Pantalla 1: publicar contenido de valor y que no pase nada'),
        r('Triggers usados', 'Credibilidad: Contraste creencia contra realidad. Pantallas 1 y 2: la creencia (las ideas '
                             'están en lo que funciona fuera) frente a tu frase'),
        r('Triggers usados', 'Acción: Siguiente paso único. Pantalla 4: una palabra y lo que analizas'),
        r('Número de pantallas', '4.'),
        r('¿Es nueva de verdad?', 'Sí. Ninguna pieza de noviembre ni de diciembre manda a buscar las ideas en los proyectos '
                                  'terminados. Lo más cerca: N17 (23 nov), que manda revisar lo que ya grabaste antes de '
                                  'grabar más, y N18 (21 dic), que saca las ideas de una grabación; aquí el material no '
                                  'está grabado: son las preguntas y las decisiones de un proyecto. N07 (1 dic) saca '
                                  'piezas de las propuestas que no salieron; esta, de los proyectos que sí.'),
    ],
    'pantallas': [
        ('PANTALLA 1, el problema tal y como lo ve quien mira', [
            r('Texto en pantalla', '«Publicas contenido de valor y no pasa nada.» · «Y para enero vuelves a buscar ideas en '
                                   'lo que le funciona a tu sector.»'),
            r('Fondo', 'Vídeo mudo: tú en la mesa, pasando con el dedo el inicio de Instagram en el móvil; la pantalla, '
                       'desenfocada, que no se lea ninguna cuenta.'),
            r('Nota de edición', 'Dos bloques, arriba, por debajo de la franja del nombre; cada uno en dos renglones como '
                                 'mucho. Nada en el tercio de abajo.'),
        ]),
        ('PANTALLA 2, la revelación, dicha sin adornos', [
            r('Texto en pantalla', '«Tus mejores ideas probablemente están enterradas en proyectos terminados.»'),
            r('Fondo', 'Vídeo mudo: tú abriendo en el ordenador la carpeta de tus proyectos; los nombres, desenfocados.'),
            r('Nota de edición', 'La frase sola, en cuerpo mayor, en los dos tercios de arriba. «proyectos terminados» en '
                                 'negrita.'),
        ]),
        ('PANTALLA 3, el desglose: qué cambia si se acepta', [
            r('Texto en pantalla', '«Abre el último proyecto que cerraste y apunta dos cosas: las preguntas que te hizo ese '
                                   'cliente antes de contratarte y las decisiones que tomaste.» · «Cada una es una pieza que '
                                   'únicamente puedes contar tú, porque ninguna cuenta de tu sector la ha vivido.»'),
            r('Fondo', 'Fondo liso en el azul de la casa: es la pantalla de valor y manda el texto. Se sube como vídeo quieto '
                       'de doce segundos, para que dé tiempo a leerla sin pararla.'),
            r('Nota de edición', 'Dos bloques; el primero, la orden, en cuerpo mayor. «preguntas» y «decisiones» en negrita. '
                                 'Todo en los dos tercios de arriba.'),
        ]),
        ('PANTALLA 4, el cierre', [
            r('Texto en pantalla', '«Responde DIAGNÓSTICO / y analizo si tus piezas salen de tus clientes o de tu sector.»'),
            r('Fondo', 'Vídeo mudo: tú cerrando la carpeta y mirando a cámara.'),
            r('Nota de edición', 'Una sola frase, en dos renglones, y nada más en la pantalla. En el primero, «Responde '
                                 'DIAGNÓSTICO», con DIAGNÓSTICO en grande y la flecha apuntando a la barra de respuesta; en '
                                 'el segundo, «y analizo si tus piezas salen de tus clientes o de tu sector.», en cuerpo de '
                                 'rótulo. La frase, en el tercio de en medio: al tercio de abajo solo baja la flecha.'),
        ]),
    ],
}


def secuencia(P, s):
    out = [para(P.h3, s['titulo']), para(P.linea, s['linea']), para(P.etiqueta, 'Ficha de la secuencia'),
           table(P.ficha_s, s['ficha']), para(P.etiqueta, 'Guion de producción')]
    for titulo, filas in s['pantallas']:
        out += [para(P.pant_p, titulo), table(P.pant_t, filas)]
    return out


FILAS = {  # código viejo → celdas nuevas del índice
    'N22': ['N05', 'Reel · mar 22 dic', 'Autoridad', 'MOFU', '2', 'La pieza que le cambia el problema',
            'r7 · de la sustitución, entra por N22 (20 oct, noche) · gancho: elegido el 20 oct'],
    'S22': ['NS8', 'Historias · mar 22 dic', 'Demostración', 'MOFU', '2', 'Te recomiendan, y te buscan',
            'r7 · nueva, entra por S22 (20 oct, noche)'],
    'R38': ['N16', 'Reel · mié 23 dic', 'Autoridad', 'TOFU', '3', 'El director de una agencia que tú pagas',
            'r7 · de la sustitución, entra por R38 (20 oct, noche) · gancho: elegido el 20 oct'],
    'NS4': ['NS9', 'Historias · jue 24 dic (se programa por la mañana)', 'Autoridad', 'MOFU', '2',
            'Las ideas que ya tienes en tus proyectos', 'r7 · nueva, entra por NS4 (20 oct, noche)'],
}


def main(dic, sust, salida):
    d = docx.Document(dic); s = docx.Document(sust)
    P = Plantilla(d, 'N18', 'NS7')
    nuevos = {
        'N22': build(n05(read_piece(s, 'N05')), P, 'sust', f'martes 22 de diciembre, en el sitio de N22 ({MOTIVO})'),
        'R38': build(n16(read_piece(s, 'N16')), P, 'sust', f'miércoles 23 de diciembre, en el sitio de R38 ({MOTIVO})'),
        'S22': secuencia(P, NS8),
        'NS4': secuencia(P, NS9),
    }
    for viejo, els in nuevos.items():
        g = grupo(d, viejo)
        for el in els: g[0].addprevious(el)
        for el in g: el.getparent().remove(el)
    t = tabla_indice(d)
    for viejo, celdas in FILAS.items():
        tr = fila(t, viejo)
        for tc, v in zip(tr.findall(W_TC), celdas): fill_cell(tc, [v])
    d.save(salida)
    print('diciembre r7: salen N22, S22, R38 y NS4; entran N05, NS8, N16 y NS9 ->', salida)


if __name__ == '__main__':
    main(*sys.argv[1:4])
