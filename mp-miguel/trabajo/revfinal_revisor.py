"""Segunda tanda de la revisión final (21 oct): lo que encontró el revisor a ciegas y no estaba
en mi pasada, los escritos de N04, N07, N13, N15 y N18 al de su gancho B, y los Pendientes.
Se aplica sobre nov_r9_g.docx y dic_r7_i.docx (ya con revfinal_mias.py)."""
import json

def e(ambito, old, new='', porque='', **kw):
    d = dict(ambito=ambito, old=old, new=new, porque=porque); d.update(kw); return d

def cambio_escrito(code, viejo, nuevo, molde, dds_viejo, dds_nuevo, compr_vieja, compr_nueva, desc_ancla, porque_viejo,
                   b_viejo, b_nuevo, elec_vieja, elec_nueva, anillos=None):
    out = [
        e(code, viejo, nuevo, 'escrito al del gancho B', fila='Escrito'),
        e(code, molde[0], molde[1], 'molde'),
        e(code, dds_viejo, dds_nuevo, 'de dónde sale'),
        e(code, compr_vieja, compr_nueva, 'comprobaciones'),
        e(code, desc_ancla, f'«{viejo}» ({porque_viejo}) · ' + desc_ancla, 'descartados'),
        e(code, b_viejo, b_nuevo, 'gancho B'),
        e(code, elec_vieja, elec_nueva, 'elección'),
    ]
    if anillos: out.append(e(code, anillos[0], anillos[1], 'anillos'))
    return out

ELEC_20 = 'Elegida la favorita (20 oct): Miguel delegó la elección («prueba tú»). Si prefieres otra, está en Descartados o en la crítica del 19 oct.'

def elec(motivo):
    return ('Elegida en la revisión final (21 oct): el escrito pasa al de su gancho B, como dejas tú los escritos, '
            f'{motivo}; el hablado no cambia. El del 20 oct está en Descartados.')

NOV = [
    e('NS3', 'prometo Leads.', 'prometo leads.', 'errata copiada', todas=True),
    e('S03', 'la pregunta es: ¿has conseguido resultados?', 'la pregunta es ¿has conseguido resultados?', 'tu texto no llevaba esos dos puntos'),
    e('S03', '«Tu marca personal ya te cuesta tiempo cada mes: la pregunta es para qué.»',
      '«Tu marca personal ya te está quitando tiempo cada mes: la pregunta es ¿has conseguido resultados?» Es tu frase de la pantalla 3 (21 oct).', 'frase de la pieza'),
    e('R06', '180 reels / mes', '180 reels en un mes', 'tu voz dice «en un mes»'),
    e('S04', 'Foto de la pizarra con «¿qué trabajo?» escrito y las cuatro palabras debajo: «crean / encuentran / trabajo hecho / conocen».',
      'Foto de la pizarra con la frase de la pantalla 1 tachada.', 'el texto no explica esas palabras'),
    e('S04', '«Una pieza tiene un trabajo: un vídeo hecho para convertir que se hace viral y no trae un lead no ha funcionado.»',
      '«El contenido de la pieza seguro que es bueno, pero probablemente vaya dirigido a quien quiera aprender a hacerlo, en vez de a tu público, a quien quieres ayudar.» Es tu frase de la pantalla 3 (21 oct).', 'frase de la pieza'),
    e('R13', 'FASE 4. Step 1, 2 y 3 · la segunda pregunta, a quién', 'FASE 4. Step 1, 2 y 3 · una mañana para un trimestre', 'la voz no dice esa pregunta'),
    e('R13', 'FASE 5. Step 1, 2 y 3 · la tercera pregunta, a dónde manda', 'FASE 5. CTA, el diagnóstico', 'la voz no dice esa pregunta'),
    e('S09', 'La frase entre comillas, serif de la casa, grande, centrada.',
      'La primera frase entre comillas, serif de la casa, grande, centrada. La segunda, tu orden, sin comillas y en cuerpo menor, debajo.', 'nota'),
]
NOV += cambio_escrito('N04',
    'Repetir los vídeos virales de tu competencia te aleja de la venta.', 'Cómo elegir qué repetir si quieres que te compren.',
    ('Error o peligro (en el escrito: repetir lo que más se vio tiene un coste), con lo que ya vivió el comprador en el hablado y el dolor detrás · disparador de atención: sesgo de negatividad.',
     '«Cómo» muy concreto en el escrito, con la condición dentro («si quieres que te compren»); en el hablado, lo que ya vivió el comprador, con el dolor detrás · disparador de atención: sesgo de negatividad, en el hablado.'),
    'escrito: propio, de tu frase del concepto 1 de la raíz 1',
    'escrito: el del gancho B de la propuesta, que pasa a ser el A en la revisión final (21 oct); detrás, tu frase del concepto 1 de la raíz 1',
    '¿Funciona solo? Sí: dice que algo que todo el mundo hace tiene un coste y deja abierto cuál · ¿Sobrevive sin la sorpresa? Sí: aunque lo sepa, le falta qué mirar antes de quitar una pieza · ¿Lo entiende quien llega hoy? Sí: «repetir», «visitas» y «comprador» son palabras de cualquiera que venda.',
    '¿Funciona solo? Sí: promete un criterio para elegir qué repetir, y no lo dice · ¿Sobrevive sin la sorpresa? Sí: aunque lo intuya, le falta qué mirar antes de repetir o quitar una pieza · ¿Lo entiende quien llega hoy? Sí: «repetir» y «que te compren» son palabras de cualquiera que venda.',
    '«Publicas contenido, pero nadie cualificado te ve.» (el hablado de antes:',
    'el escrito del 20 oct: hablaba de los virales de tu competencia, y la pieza habla de repetir lo tuyo más visto',
    'Escrito: «Cómo elegir qué repetir si quieres que te compren.» · Hablado: «Cada mes miras qué vídeo tuvo más visitas, y haces otro igual.» (familia: «cómo» muy concreto). Si se elige el B, la fase 1 es solo esta frase, y la fase 2 sigue igual.',
    'Escrito: «Repetir lo que más visitas tuvo te aleja de la venta.» (el del 20 oct, corregido para que case con la pieza) · Hablado: el mismo (familia: error o peligro).',
    ELEC_20, elec('y porque el del 20 oct hablaba de los virales de tu competencia y la pieza, de repetir lo tuyo más visto'),
    anillos=('gancho 4 / pieza 3 / cierre 3. El rótulo lo para cualquiera que publique para un negocio;',
             'gancho 3 / pieza 3 / cierre 3. El rótulo lo para cualquiera que publique para vender;'))
NOV += [
    # Pendientes de noviembre
    e('PENDIENTES', 'S10 acredita a Caleb Ralston; la propuesta de abril se enseña difuminada entera, sin cifras; y la bio de NS2 es una propuesta.',
      'S10 acredita a Caleb Ralston; la propuesta de abril se enseña difuminada entera, sin cifras; y la bio de NS2 es una propuesta. En la revisión final (21 oct), el escrito de N04 pasa al de su gancho B («Cómo elegir qué repetir si quieres que te compren.»), como dejas tú los escritos. Los de N01 y N17 tampoco son un «Cómo», una pregunta ni una orden, pero sus ganchos B hablan del oficio sin filtro, así que se quedan: dime si los cambias.', 'decidido'),
    e('PENDIENTES', 'y en su lugar frases tuyas de cada locución (N01, N04, R12 y N17).',
      'y en su lugar frases de cada locución: tuyas en N01, N04 y R12, y en N17 las que escribí con tu documento del 8 oct y no cambiaste.', 'precisión'),
    e('PENDIENTES', '¿era «de la que puede salir»? No se han tocado',
      '¿era «de la que puede salir»? R11: «Así es como monto cada marca, también la mía.» suena a mención de rutina. S01: «La respuesta más frecuente es sí y no» se dice antes de que vote nadie. S03, pantalla 4: «en 30 minutos analizo qué partes de tu contenido pueden mejorarse» pone un plazo y pide otra cosa que la pantalla 3. N23: la prueba es un análisis que hizo una inteligencia artificial, y la llamada vende que analizas tú. No se han tocado', 'dudas'),
]

DIC = [
    e('S13', 'Eso es la trampa viral, como la llama Kallaway. ¿Te ha pasado?', '«Eso es la trampa viral, como la llama Kallaway. ¿Te ha pasado?»', 'comillas, como las demás pantallas'),
    e('N13', 'Esta es mi web. Los logos dicen con quién he trabajado. Debajo, un caso.', 'En mi web, los logos dicen con quién he trabajado, y debajo hay un caso.', 'frases de pausa'),
    e('N13', 'Lo que hice: un recurso por episodio', 'Lo que hice fue un recurso por episodio', 'dos puntos de revelación'),
    e('N13', 'La prueba social no es llenar una página de logos: es explicar qué hiciste y qué cambió.',
      'La prueba social no es llenar una página de logos. Es explicar qué hiciste y qué cambió.', 'dos puntos de revelación', todas=True),
    e('NS6', 'Pero vuelven, porque el siguiente sigue sin ver lo que sabes.', 'Pero vuelven, porque tu siguiente cliente sigue sin ver lo que sabes.', 'el quién'),
    e('NS6', 'y analizo qué no ve de ti el siguiente antes de la llamada.', 'y analizo qué no ve de ti tu siguiente cliente antes de la llamada.', 'el quién', todas=True),
    e('NS7', 'eso debe verlo el siguiente.', 'eso debe verlo tu siguiente cliente.', 'el quién', todas=True),
    e('R25', 'que no pueden pagar tu servicio»', 'que no pueden pagar tu servicio.»', 'el punto que faltaba'),
    e('R25', 'Y cuanto más sientan que el mensaje resuena con ellos,', '«Y cuanto más sientan que el mensaje resuena con ellos,', 'comillas de la fase 5', fila='Locución'),
    e('R25', 'atraen ya a tu cliente ideal, comenta DIAGNÓSTICO y hablamos por privado.', 'atraen ya a tu cliente ideal, comenta DIAGNÓSTICO y hablamos por privado.»', 'comillas de la fase 5', fila='Locución'),
    e('N26', 'y D10 es el dolor que diciembre perdía al salir R37 (entró N22).', 'y D10 es el dolor que diciembre perdía al salir R37.', 'N22 ya no está'),
    e('N26', 'Ninguno: el modelo es tuyo (ficha 6.7, «Tuyo (8 oct)»).',
      'Ninguno en la pieza: no dice de quién es el modelo ni lo llama tu método. Sale de la revisión del 8 oct que aceptaste, y si lo das por tuyo está POR DECIDIR (ficha v7, 6.7).', 'al día con la ficha v7'),
    e('N26', 'Tu modelo con su nombre, escrito en el folio,', 'El modelo con su nombre, escrito en el folio (si lo das por tuyo, POR DECIDIR, ficha 6.7),', 'al día con la ficha v7'),
    e('R30', 'Si vendes High Ticket y contratas a alguien que mira qué es viral en tu sector y lo copia, te va a llenar el embudo de curiosos.',
      'Si vendes High Ticket y contratas a alguien que mira qué es viral en tu sector y lo copia, te va a llenar la cuenta de curiosos.', '«embudo» no va en un pie (L6)'),
    e('R35', 'escribe «AGENCIA / PODCAST / PUBLICAR» con la voz y los tacha de un trazo', 'escribe «AGENCIA» con la voz y la tacha de un trazo', 'la voz solo dice la agencia'),
    e('R35', 'debajo de la lista tachada:', 'debajo de la palabra tachada:', 'la voz solo dice la agencia'),
    e('N15', 'Y lo que sale es largo, flojo y sin gancho.', 'Y lo que sale es largo y flojo.', '«gancho» es palabra del oficio'),
    e('N15', 'lo que sale improvisando es largo, flojo y sin gancho,', 'lo que sale improvisando es largo y flojo,', '«gancho» es palabra del oficio'),
    e('SP1', 'En enero cuento qué pasó con cada una de estas decisiones, con los números. ', '', 'enero no se toca'),
]
DIC += cambio_escrito('N07',
    'En el CRM apuntas que perdiste la propuesta, no por qué.', 'Cómo leer lo que te dicen cuando no te compran.',
    ('Filtro o a la contra (en el escrito: lo que apunta en el CRM quien pierde una propuesta, la escena de tu comprador), con la escena de la propuesta en el hablado · disparador de atención: bucle de curiosidad.',
     '«Cómo» muy concreto en el escrito; la escena de la propuesta rechazada y el CRM, en tu hablado · disparador de atención: bucle de curiosidad.'),
    'escrito: propio, tu escena del CRM del hablado, contada desde el comprador',
    'escrito: el del gancho B de la propuesta, que pasa a ser el A en la revisión final (21 oct)',
    '¿Funciona solo? Sí: dice que alguien que no le compró le está diciendo algo, y deja abierto qué · ¿Sobrevive sin la sorpresa? Sí: aunque lo sepa, le falta cómo convertir cada razón en una pieza · ¿Lo entiende quien llega hoy? Sí: «compró» y «contar» son palabras de cualquiera.',
    '¿Funciona solo? Sí: promete leer lo que te dice quien no te compra, y no dice cómo · ¿Sobrevive sin la sorpresa? Sí: aunque lo intuya, le falta qué apuntar y qué hacer con cada razón · ¿Lo entiende quien llega hoy? Sí: «leer» y «no te compran» son palabras de cualquiera que venda.',
    '«Cómo crear contenido resolviendo objeciones» (el escrito de antes:',
    'el escrito del 20 oct: contaba la misma escena que tu hablado, y el rótulo se gastaba en repetirla',
    'Escrito: «Cómo leer lo que te dicen cuando no te compran.» · Hablado: «Pierdes una propuesta y lo único que apuntas es el precio.» (familia: «cómo» muy concreto). Si se elige el B, la segunda frase de la fase 1 pasa a «Y no ves la pieza que había dentro, porque ni siquiera sabes contar por qué te eligen los que sí firman.»',
    'Escrito: el del 20 oct, «En el CRM apuntas que perdiste la propuesta, no por qué.» (en Descartados) · Hablado: el mismo, el tuyo (familia: filtro o a la contra).',
    ELEC_20, elec('y porque el del 20 oct contaba la misma escena que tu hablado'))
DIC += cambio_escrito('N13',
    'Un logo dice con quién. No dice qué cambió.', 'Qué contar de un cliente, además de su logo.',
    ('Filtro o a la contra (en el escrito: lo que se suele enseñar no cuenta lo que importa), con el dolor dicho como un hecho en el hablado',
     '«Cómo» muy concreto en el escrito (qué contar además del logo), con el dolor dicho como un hecho en el hablado'),
    'escrito: propio, de tu frase del concepto 3 de la raíz 3',
    'escrito: el del gancho B de la propuesta, que pasa a ser el A en la revisión final (21 oct), sobre tu frase del concepto 3 de la raíz 3',
    '¿Funciona solo? Sí: dice lo que no hace un logo y deja abierto qué lo hace · ¿Sobrevive sin la sorpresa? Sí: aunque lo sepa, le falta cómo contar su caso · ¿Lo entiende quien llega hoy? Sí: «logo» y «qué cambió» son palabras de cualquiera.',
    '¿Funciona solo? Sí: promete qué contar de un cliente además del logo, y no lo dice · ¿Sobrevive sin la sorpresa? Sí: aunque lo intuya, le falta cómo contar su caso, en orden · ¿Lo entiende quien llega hoy? Sí: «cliente» y «logo» son palabras de cualquiera.',
    '«Tus logos no le dicen nada a tu comprador»',
    'el escrito del 20 oct: es un paralelismo, y tu voz los corta',
    'Escrito: «Qué contar de un cliente, además de su logo.» · Hablado: «Las cifras de un cliente son contenido si puedes explicar qué hiciste para conseguirlas.» (familia: «cómo» muy concreto). Si se elige el B, la segunda frase de la fase 1 pasa a «Y aun así pones solo los logos de tus clientes, y esperas que con eso baste», y la fase 3 pierde «Las cifras de un cliente son contenido…».',
    'Escrito: el del 20 oct, «Un logo dice con quién. No dice qué cambió.» (en Descartados, por paralelismo) · Hablado: el mismo (familia: filtro o a la contra).',
    ELEC_20, elec('porque el del 20 oct era un paralelismo'))
DIC += cambio_escrito('N15',
    'No grabes ideas. Graba lo que contestas a tus clientes.', 'Cómo preparo la grabación de un empresario.',
    ('Filtro o a la contra (en el escrito: no se graban ideas, se graban respuestas), con la escena de la grabación en el hablado',
     '«Cómo» muy concreto en el escrito, en primera persona, como tu «Cómo decido qué contenido publicar en servicios B2B.»; la escena de la grabación, en el hablado'),
    'escrito: propio, de tu frase del concepto 1 de la raíz 4',
    'escrito: el del gancho B de la propuesta, que pasa a ser el A en la revisión final (21 oct); detrás, tu frase del concepto 1 de la raíz 4',
    '¿Funciona solo? Sí: dice qué grabar en lugar de lo que todos intentan · ¿Sobrevive sin la sorpresa? Sí: aunque lo sepa, le falta cómo se prepara esa pregunta · ¿Lo entiende quien llega hoy? Sí: «grabar» y «contestar» son palabras de cualquiera.',
    '¿Funciona solo? Sí: promete enseñar cómo preparas una grabación, y no lo dice · ¿Sobrevive sin la sorpresa? Sí: aunque lo intuya, le falta la página del guion y los tres pasos · ¿Lo entiende quien llega hoy? Sí: «grabación» y «empresario» son palabras de cualquiera.',
    '«Llega a grabar sin ninguna idea»',
    'el escrito del 20 oct: es un paralelismo, y tu voz los corta',
    'Escrito: «Cómo preparo la grabación de un empresario.» · Hablado: «Si puedes contestarle bien a un cliente en una reunión, ya puedes hacer contenido.» (familia: «cómo» muy concreto). Si se elige el B, la segunda frase de la fase 1 pasa a «Pero si te sientas a improvisar, lo que sale es largo, flojo y sin gancho.»',
    'Escrito: el del 20 oct, «No grabes ideas. Graba lo que contestas a tus clientes.» (en Descartados, por paralelismo) · Hablado: el mismo (familia: filtro o a la contra).',
    ELEC_20, elec('porque el del 20 oct era un paralelismo'))
DIC += cambio_escrito('N18',
    'Cortar más clips no te da más ideas.', 'Cómo sacar todas las ideas de una grabación.',
    ('Error o peligro (en el escrito: lo que parece la solución no lo es), con lo que ya vivió el comprador en el hablado · disparador de atención: patrón roto.',
     '«Cómo» muy concreto en el escrito; lo que ya vivió el comprador (la agencia que le devolvió la entrevista en clips), en el hablado · disparador de atención: patrón roto, en el hablado.'),
    'escrito: propio, de tu frase del concepto 4 de la raíz 4',
    'escrito: el del gancho B de la propuesta, que pasa a ser el A en la revisión final (21 oct); detrás, tu frase del concepto 4 de la raíz 4',
    '¿Funciona solo? Sí: dice que lo que todo el mundo hace para tener más contenido no le da más · ¿Sobrevive sin la sorpresa? Sí: aunque lo sepa, le falta qué hacer antes de cortar · ¿Lo entiende quien llega hoy? Sí: «clips» e «ideas» son palabras de cualquiera que grabe.',
    '¿Funciona solo? Sí: promete sacar todas las ideas de una grabación, y no dice cómo · ¿Sobrevive sin la sorpresa? Sí: aunque lo intuya, le falta qué hacer antes de cortar · ¿Lo entiende quien llega hoy? Sí: «ideas» y «grabación» son palabras de cualquiera que grabe.',
    '«No tienes tiempo para estar en todas las plataformas.»',
    'el escrito del 20 oct: no es un «Cómo», una pregunta ni una orden, que es lo que deja tu voz',
    'Escrito: «Cómo sacar todas las ideas de una grabación.» · Hablado: «Una respuesta buena da varias piezas porque tiene varias ideas, no porque la cortes en trozos.» (familia: «cómo» muy concreto). Si se elige el B, la fase 1 es el hablado B seguido de «Y aun así cortas tu última grabación en todos los clips que puedes», y la fase 3 pierde su primera frase.',
    'Escrito: el del 20 oct, «Cortar más clips no te da más ideas.» (en Descartados) · Hablado: el mismo (familia: error o peligro).',
    ELEC_20, elec('porque el del 20 oct era una frase que se cierra sola'),
    anillos=('El rótulo lo para cualquiera que corte vídeos;', 'El rótulo lo para cualquiera que grabe;'))
DIC += [
    # Pendientes de diciembre
    e('PENDIENTES', 'en N16 el gancho escrito pasa a un «Cómo», y en N05, en la revisión final, a la pregunta de su gancho B, como dejas tú los escritos.',
      'en N16 el gancho escrito pasa a un «Cómo»; y en la revisión final (21 oct), N05 pasa a la pregunta de su gancho B, y N07, N13, N15 y N18, al escrito de su gancho B, como dejas tú los escritos (los del 20 oct, en Descartados). La revisión final también quita «sin gancho» de N15, que es palabra del oficio, y de SP1 la promesa de contar en enero qué pasó, porque enero no se toca.', 'decidido'),
    e('PENDIENTES', 'y en su lugar frases tuyas de cada locución (N07, N13, R28, N15, R35 y N18).',
      'y en su lugar frases de cada locución: tuyas en N07, R28 y R35, y en N13, N15 y N18 las que escribí con tu documento del 8 oct y no cambiaste.', 'precisión'),
    e('PENDIENTES', 'y en su lugar frases de tu locución, también en la frase de la pieza. En R28 sale',
      'y en su lugar frases de la locución (en N15, la que escribí y no cambiaste; en N16, las palabras de tu web), también en la frase de la pieza. En R28 sale', 'precisión'),
    e('PENDIENTES', 'y el punto final que faltaba en la fase 2.',
      'y el punto final que faltaba en la fase 2. R25 (21 oct): el punto que faltaba al final de la fase 1 y las comillas de la fase 5.', 'tu voz'),
    e('PENDIENTES', 'y suena a acertijo. No se han tocado',
      'y suena a acertijo. R25: «Da igual que no tenga miles de visitas», ¿era «tengas»? N05: tu locución abre con una frase que se cierra sola («Lo que tu cliente pide y lo que le pasa casi nunca coinciden.») y la escena va en la segunda; si abres con la escena, el hablado filtra en los tres primeros segundos. R26: «180 reels al mes» choca con «en un mes» de R06; «A día de hoy, trabajo con dos empresas a la vez» se lee como cuántos clientes tienes (falta el número real del 7 dic); y tu nota del vídeo borrado sigue dentro de la pieza. «embudo», en tu voz de R21 y R30, es palabra del método (en el pie de R30 ya va «cuenta»). N16: las dos frases de tu documento en la fase 3 son paralelismos. S24, pantalla 2: «no le faltó constancia. Le faltó destino.» es un paralelismo, y junta «Doce meses» con «en marzo». No se han tocado', 'dudas'),
    e('PENDIENTES', 'Están en la última parte de la hoja de rodaje',
      'Están en la última parte de la hoja de rodaje. Lo que más subiría NS8: un mensaje real de alguien que te escribió después de buscarte, con su permiso', 'material'),
    e('PENDIENTES', 'R38 y NS4 eran la demostración y la humanización de esa semana.',
      'R38 y NS4 eran la demostración y la humanización de esa semana, y ninguna de las seis enseña una prueba tuya.', 'semana'),
]

NOV_EST = {
    'R01': 'r9 · el pie, con tu voz, y una comilla de tu fase 3 (revisión final, 21 oct)',
    'R06': 'r9 · el pie y un rótulo, como tu voz (revisión final, 21 oct)',
    'R11': 'r9 · el pie, con tu voz (revisión final, 21 oct)',
    'R12': 'r9 · el pie, con tu voz y sin repetir el gancho (revisión final, 21 oct)',
    'R13': 'r9 · los títulos de las fases 4 y 5, como tu voz (revisión final, 21 oct)',
    'R14': 'r9 · el pie, con tu voz y sin el crédito que no tocaba (revisión final, 21 oct)',
    'R18': 'r9 · el pie, con tu voz (revisión final, 21 oct)',
    'N04': 'r9 · el pie, con tu voz, y el gancho escrito, el del B (revisión final, 21 oct)',
    'NS3': 'r9 · ajustada: N22 y R38 salen de diciembre; «leads», sin mayúscula (revisión final, 21 oct)',
    'S03': 'r9 · tu pantalla 3, sin los dos puntos que puse yo (revisión final, 21 oct)',
    'S04': 'r9 · el fondo de la pantalla 3 y la frase de la pieza, como tu texto (revisión final, 21 oct)',
    'S09': 'r9 · la nota de la pantalla 1 (revisión final, 21 oct)',
}
DIC_EST = {
    'N07': 'r7 · el pie, con tu voz, y el gancho escrito, el del B (revisión final, 21 oct)',
    'S13': 'r7 · comillas en la pantalla 2 (revisión final, 21 oct)',
    'N13': 'r7 · el gancho escrito, el del B, y la locución sin frases de pausa (revisión final, 21 oct)',
    'NS6': 'r7 · «tu siguiente cliente», en las pantallas 3 y 4 (revisión final, 21 oct)',
    'R25': 'r7 · el pie, con tu voz, y una errata mía del título (revisión final, 21 oct)',
    'R26': 'r7 · el pie y un rótulo, sin lo que tu voz no dice (revisión final, 21 oct)',
    'N26': 'r7 · el crédito, al día con tu ficha v7 (revisión final, 21 oct)',
    'R28': 'r7 · sin «foto» ni «Empieza por tu enlace», como tu voz (revisión final, 21 oct)',
    'NS7': 'r7 · «tu siguiente cliente», en la pantalla 3 (revisión final, 21 oct)',
    'R30': 'r7 · el pie, sin «embudo» (revisión final, 21 oct)',
    'R21': 'r7 · el pie, con tu voz (revisión final, 21 oct)',
    'R31': 'r7 · el pie, con tu voz (revisión final, 21 oct)',
    'N15': 'r7 · el gancho escrito, el del B, y el pie, con los tres pasos (revisión final, 21 oct)',
    'R35': 'r7 · el pie y la pizarra, como tu voz (revisión final, 21 oct)',
    'N18': 'r7 · el pie y dos frases mías, con tu voz, y el gancho escrito, el del B (revisión final, 21 oct)',
    'N05': 'r7 · de la sustitución, entra por N22 (20 oct, noche) · gancho: el B, desde la revisión final (21 oct)',
    'NS8': 'r7 · nueva, entra por S22 (20 oct, noche) · la pantalla 1 dice quién busca (revisión final, 21 oct)',
    'N16': 'r7 · de la sustitución, entra por R38 (20 oct, noche) · gancho: elegido el 20 oct · el pie, en la revisión final (21 oct)',
    'NS9': 'r7 · nueva, entra por NS4 (20 oct, noche) · va a tus decisiones, no a las preguntas de NS8 (revisión final, 21 oct)',
    'SP1': 'r7 · sin la promesa de contar en enero (revisión final, 21 oct)',
}

base = '/tmp/claude-0/-home-user-Claude-real-este/bb8756ca-7159-57b4-84fe-165cd7e375cc/scratchpad/work/'
for nombre, obj in (('nov_rev_b.json', NOV), ('dic_rev_b.json', DIC), ('nov_estados_b.json', NOV_EST), ('dic_estados_b.json', DIC_EST)):
    json.dump(obj, open(base + nombre, 'w'), ensure_ascii=False, indent=1)
print(len(NOV), len(DIC))
