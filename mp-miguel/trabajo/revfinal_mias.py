"""Arreglos de la revisión final (21 oct) que salen de mi pasada propia, en texto de Claude.
Escribe nov_rev_mias.json y dic_rev_mias.json (formato de docxedit.py)."""
import json

def e(ambito, old, new='', porque='', **kw):
    d = dict(ambito=ambito, old=old, new=new, porque=porque); d.update(kw); return d

FR = 'Es tu frase de la locución (21 oct): la de antes era una máxima mía.'

NOV = [
    # R01: el pie decía lo mismo que el gancho escrito; van tus frases de la locución
    e('R01', '«La marca personal no empieza en las redes sociales: empieza en lo que piensan los demás cuando oyen tu nombre.»',
      '«La marca personal no empieza en las redes sociales. Empieza en lo que piensan los demás cuando oyen tu nombre.» Es tu frase de la fase 2, con tu puntuación (21 oct).', 'frase de la pieza'),
    e('R01', 'La marca personal no empieza en las redes sociales: empieza en lo que piensan los demás cuando oyen tu nombre.',
      'Si cuando le das un consejo a tus clientes, lo hacen sin cuestionarte, te consideran un referente.',
      'el pie repetía el gancho escrito (SOP-11)', fila=''),
    e('R01', 'Si tus clientes te hacen caso en todo, esa marca ya la tienes. Lo que falta es que la vea el que todavía no te ha contratado.',
      'La próxima vez que estés reunido con un cliente, analiza esto: qué es lo que frecuentemente te preguntan, en qué te hacen caso sin prácticamente cuestionarte y qué resultados concretos has conseguido con ellos. Y lo comunicas en tu estrategia de contenido.',
      'remate mío; van tus frases de la fase 3'),
    # R01: la comilla de cierre de tu fase 3 estaba a media locución
    e('R01', 'tu cliente ideal?». La próxima vez', 'tu cliente ideal? La próxima vez', 'errata: comilla de cierre a media locución'),
    e('R01', 'Y lo comunicas en tu estrategia de contenido. ', 'Y lo comunicas en tu estrategia de contenido.»', 'errata: la comilla de cierre va al final', fila='Locución'),
    # R06: fuera la máxima mía del pie
    e('R06', '«El volumen no es el valor: nadie te contrata porque publiques mucho.»',
      '«Entonces llegué a la conclusión de que el volumen no tiene por qué ser la mejor estrategia de contenido.» ' + FR, 'frase de la pieza'),
    e('R06', 'El volumen no es el valor: nadie te contrata porque publiques mucho.', 'Nadie te contrata porque publiques mucho.', 'máxima mía con dos puntos de revelación; va tu frase de la fase 4'),
    # R11
    e('R11', '«Antes de que te conozcan por muchas cosas, te tienen que conocer por una.»',
      '«Aunque pareciera que cierras puertas, anicharte es lo mejor que puedes hacer para empezar la marca personal de un empresario B2B.» ' + FR, 'frase de la pieza'),
    e('R11', 'Antes de que te conozcan por muchas cosas, te tienen que conocer por una.',
      'Aunque pareciera que cierras puertas, anicharte es lo mejor que puedes hacer para empezar la marca personal de un empresario B2B.',
      'máxima mía; va tu frase de la fase 2', fila=''),
    # R12: el pie repetía el gancho escrito
    e('R12', 'El coste de la autoridad invisible: cuando la mayoría de tus clientes te piden descuentos y realmente no es por el precio de tu servicio.',
      '', 'repetía el gancho escrito (SOP-11)', borrar=True),
    e('R12', 'No significa que tu producto sea malo: lo que está fallando es el marketing.',
      'No significa que tu producto sea malo. De hecho, en la mayoría de los casos ocurre lo contrario: tu producto es bueno, pero lo que está fallando es el marketing.',
      'como lo dices tú en la fase 5, sin los dos puntos de revelación'),
    # R14
    e('R14', '«El problema de un viral fuera de tu público no es ese vídeo: es el siguiente.»',
      '«La mejor estrategia es hacer contenido de nicho para resolver los problemas de tu cliente ideal.» ' + FR, 'frase de la pieza'),
    e('R14', 'El problema de un viral fuera de tu público no es ese vídeo: es el siguiente.',
      'La viralidad es óptima cuando vendes cosas que no necesitan precualificación.',
      'máxima mía; va tu frase de la fase 2', fila=''),
    e('R14', ' La trampa viral es de Kallaway (@kallawaymarketing).', '', 'tu locución no cuenta la trampa viral: no hay nada que acreditar'),
    e('R14', '; la trampa viral de Kallaway (ficha 2.8) queda acreditada en el pie', '', 'el pie ya no la cuenta'),
    e('R14', '; la trampa viral con su crédito a Kallaway, en el pie', '', 'el pie ya no la cuenta'),
    # R18
    e('R18', '«Un podcast no te trae nada hasta que alguien con criterio elige sus minutos.»',
      '«Cuando vas a un podcast tienes una oportunidad de sacar ideas de contenido que van dirigidas a tu cliente ideal: una sola respuesta te da varias.» ' + FR, 'frase de la pieza'),
    e('R18', 'Un podcast no te trae nada hasta que alguien con criterio elige sus minutos.',
      'Te invitaron a un podcast, fuiste, subiste los reels que te etiquetaron a Instagram, y ya está. Eso es lo que la mayoría hace.',
      'máxima mía; van tus frases de las fases 1 y 2', fila=''),
    e('R18', 'Es el modelo del clipper de Alex Hormozi.',
      'Es el modelo de Alex Hormozi, que tiene a una persona que decide qué reels hay que sacar.', '«clipper» sin explicar'),
    e('PENDIENTES', 'R11: una comilla. «subóptima» se queda: es de Fer y la aceptaste.',
      'R11: una comilla. R01: la comilla de cierre de la fase 3, que estaba a media locución, va al final (21 oct). «subóptima» se queda: es de Fer y la aceptaste.', 'tu voz'),
    e('PENDIENTES', 'la frase que tú cambiaste en la locución: ya no vuelve.',
      'la frase que tú cambiaste en la locución: ya no vuelve. En la revisión final (21 oct), lo mismo en R01, R06, R11, R14 y R18: fuera las máximas mías, y en su lugar frases de tu locución, también en la frase de la pieza. En R12 sale del pie tu frase de la fase 2, porque decía lo mismo que el gancho escrito; y en R14 sale el crédito a Kallaway, porque tu locución no cuenta la trampa viral.', 'pies'),
]

DIC = [
    # N05: el escrito prometía un cómo que la pieza no da y repetía la frase de la fase 3
    e('N05', 'Cómo enseñarle a tu cliente que su problema no era el que pensaba.',
      '¿Qué le pasa de verdad al cliente que llega a tu llamada de ventas?', 'gancho B', fila='Escrito'),
    e('N05', '«Cómo enseñarle a tu cliente que su problema no era el que pensaba.» Se va',
      '«¿Qué le pasa de verdad al cliente que llega a tu llamada de ventas?» Se va', 'rótulo de entrada'),
    e('N05', '«Cómo» muy concreto en el escrito, con tu frase de la fase 3; en el hablado',
      'Pregunta del comprador en el escrito, con la llamada de ventas dentro; en el hablado', 'molde'),
    e('N05', 'escrito: propio, tu frase de la fase 3 vuelta «Cómo» · hablado: tuyo, la primera frase de tu locución (era el hablado del gancho B)',
      'escrito: propio, el del gancho B de la propuesta, que pasa a ser el A en la revisión final (21 oct) · hablado: tuyo, la primera frase de tu locución', 'de dónde sale'),
    e('N05', 'gancho 3 / pieza 2 / cierre 2. El rótulo lo para cualquiera que tenga clientes; el cuerpo le habla al que vende en una llamada; el pie lleva la condición.',
      'gancho 2 / pieza 2 / cierre 2. El rótulo ya lleva la llamada de ventas, así que lo para el que vende en una llamada; el cuerpo le habla a él; el pie lleva la condición.', 'anillos'),
    e('N05', '¿Funciona solo? Sí: promete cómo enseñarle algo que su cliente no ve, y no lo dice · ¿Sobrevive sin la sorpresa? Sí: aunque lo sepa, le falta cómo encontrar esa distancia en su caso · ¿Lo entiende quien llega hoy? Sí: «cliente» y «problema» son palabras de cualquiera que venda.',
      '¿Funciona solo? Sí: pregunta qué le pasa de verdad a su cliente, y no lo dice · ¿Sobrevive sin la sorpresa? Sí: aunque lo intuya, le falta tu ejemplo y qué tiene que hacer su contenido con eso · ¿Lo entiende quien llega hoy? Sí: «cliente» y «llamada de ventas» son palabras de quien vende con llamada.', 'comprobaciones'),
    e('N05', '«Tu cliente pide una cosa. Su problema es otra.» (el escrito de antes:',
      '«Cómo enseñarle a tu cliente que su problema no era el que pensaba.» (el escrito del 20 oct: prometía un cómo que la pieza no da, y decía casi lo mismo que tu frase de la fase 3, que va en el rótulo y en el pie) · «Tu cliente pide una cosa. Su problema es otra.» (el escrito de antes:', 'descartados'),
    e('N05', 'Escrito: «¿Qué le pasa de verdad al cliente que llega a tu llamada de ventas?» · Hablado: «Tu cliente llega a la llamada convencido de que sabe lo que le pasa.» (familia: pregunta del comprador).',
      'Escrito: «¿Tu cliente llega a la llamada convencido de lo que le pasa?» · Hablado: el mismo, la primera frase de tu locución (familia: pregunta del comprador).', 'gancho B'),
    e('N05', 'Elegida el 20 oct, por la noche: el escrito pasa a un «Cómo» con tu frase de la fase 3, y el hablado es la frase con la que abres tu locución. Si prefieres el de antes, está en Descartados.',
      'Elegida en la revisión final (21 oct): el escrito pasa a la pregunta del gancho B, porque el «Cómo» del 20 oct prometía algo que la pieza no da y repetía tu frase de la fase 3; el hablado sigue siendo la frase con la que abres tu locución. Los de antes están en Descartados.', 'elección'),
    e('INDICE', 'gancho: elegido el 20 oct', 'gancho: el B, desde la revisión final (21 oct)', 'estado', fila='N05'),
    # N16: el pie decía lo que la voz no dice
    e('N16', 'Si vendes un servicio que se cierra en una llamada de ventas, tu tiempo vale más en esa llamada que revisando rótulos.',
      'Si vendes un servicio que se cierra en una llamada de ventas, a ti te toca contar tus casos, tus cifras y cómo ves tu sector. Lo demás lo tiene que llevar la persona que hace tu contenido.',
      'comparación que se cierra sola; va lo que te toca a ti, con las palabras de tu web'),
    # NS8: la pantalla 1 no decía quién hace la búsqueda
    e('NS8', 'Te han recomendado. / Y antes de escribirte, hace esto.', 'A un posible cliente le han hablado de ti. / Y antes de escribirte, hace esto.', 'regla 4 de tu voz: el quién'),
    e('NS8', 'Pantalla 1: que te recomienden, que es lo que ya vive quien depende del boca a boca',
      'Pantalla 1: que a un posible cliente le hablen de ti, que es lo que ya vive quien depende del boca a boca', 'disparador'),
    # NS9: misma salida que NS8 dos días antes; va a las decisiones
    e('NS9', 'Y para enero vuelves a buscar ideas en lo que le funciona a tu sector.', 'Y para enero vuelves a buscar ideas en lo que más visitas tuvo en tu sector.', 'tus palabras'),
    e('NS9', 'Abre el último proyecto que cerraste y apunta dos cosas: las preguntas que te hizo ese cliente antes de contratarte y las decisiones que tomaste.',
      'Abre el último proyecto que cerraste y apunta qué decidiste en cada momento, y por qué.', 'no repetir la salida de NS8'),
    e('NS9', 'Cada una es una pieza que únicamente puedes contar tú, porque ninguna cuenta de tu sector la ha vivido.',
      'Cada decisión es una pieza que únicamente puedes contar tú, porque ninguna cuenta de tu sector ha vivido ese proyecto.', 'pantalla 3'),
    e('NS9', '«preguntas» y «decisiones» en negrita.', '«qué decidiste» y «por qué» en negrita.', 'nota'),
    e('NS9', 'y analizo si tus piezas salen de tus clientes o de tu sector.', 'y analizo si tus piezas salen de tus proyectos o de tu sector.', 'pantalla 4', todas=True),
    e('NS9', 'abre el último proyecto que cerraste: las preguntas que te hizo ese cliente antes de contratarte y las decisiones que tomaste son tu contenido.',
      'abre el último proyecto que cerraste: lo que decidiste en cada momento, y por qué, es tu contenido.', 'idea'),
    e('NS9', 'y tu método: el contenido sale de las preguntas y objeciones de tus clientes (6.4).',
      'y el concepto 3.3 de tu documento: tu banco de autoridad ya existe, en lo que ya decidiste para tus clientes. Va a las decisiones, y no a las preguntas de la llamada de ventas, porque esas las lleva NS8 dos días antes.', 'de dónde sale'),
    e('NS9', 'y la 3 vuelve al 2, con lo que te pregunta un cliente antes de contratarte.', 'y la 3 vuelve al 2, con las decisiones de un proyecto para un cliente.', 'anillo'),
    e('NS9', 'mirando si tus piezas salen de lo que te preguntan tus clientes o de lo que publica tu sector.',
      'mirando si tus piezas salen de tu trabajo con tus clientes o de lo que publica tu sector.', 'CTA'),
    e('NS9', 'a sacarlas de las preguntas y las decisiones de sus propios proyectos.', 'a sacarlas de las decisiones de sus propios proyectos.', 'transformación'),
    e('NS9', 'aquí el material no está grabado: son las preguntas y las decisiones de un proyecto.',
      'aquí el material no está grabado: son las decisiones de un proyecto. Y NS8, dos días antes, va a lo que encuentra quien te busca.', 'es nueva'),
    # R21
    e('R21', 'Un viral solo suma si lo ve el que puede pagarte.', '', 'máxima mía', borrar=True),
    e('R21', 'Kallaway (@kallawaymarketing) lo llama la trampa viral.',
      'Kallaway (@kallawaymarketing) lo llama la trampa viral. La estrategia que yo sigo con mi marca personal es la viralidad de nicho: menos visitas, pero cada una le enseña al algoritmo quién es el público que cumple las condiciones para pagarte tu servicio.',
      'tu frase de la fase 4'),
    e('R21', '«Un viral solo suma si lo ve el que puede pagarte.»', '«La estrategia que yo sigo con mi marca personal es la viralidad de nicho.» ' + FR, 'frase de la pieza'),
    # R25
    e('R25', 'que de los que sí', 'que los que sí', 'errata mía del 8 oct', todas=True),
    e('INDICE', 'que de los que sí', 'que los que sí', 'errata mía del 8 oct', fila='R25'),
    e('R25', 'Si vendes con reunión, el primero es una minoría, y cada vídeo hecho para gustarle a la mayoría lo aleja.',
      'Si haces contenido que le habla a cualquiera, estás atrayendo a las personas que no pueden pagar tu servicio.', 'máxima mía; va tu frase de la fase 1'),
    e('R25', 'Rótulo: «Primero quién. Después qué».', 'Rótulo: «Decide primero quién tiene que verte».', 'paralelismo mío; va tu frase'),
    # R26
    e('R26', 'Si esperas a tener resultados para contarlo, dentro de un año nadie sabrá de dónde salieron.', '', 'máxima mía que repetía tu escrito', borrar=True),
    e('R26', 'Trabajo con dos empresas a la vez, y lo cuento aquí cada mes, también si no sale.',
      'A día de hoy, trabajo con dos empresas a la vez, para invertir todo el tiempo en conseguirles resultados.', 'promesa que no hiciste; va tu frase de la fase 3'),
    e('R26', ' Rótulo a dos líneas al terminar la fase, después de «resultados»: «Si esperas a tener resultados, / nadie sabrá de dónde salieron».', '', 'rótulo con una máxima que tu voz no dice'),
    e('R26', 'Coste de la inacción. El rótulo de la fase 3 pone plazo a callarse: si espera a tener resultados, nadie sabrá de dónde salieron',
      'Coste de la inacción. El rótulo de entrada, tu escrito: esperar a tener resultados te deja sin historia', 'disparador'),
    e('R26', '«Si esperas a tener resultados para contarlo, dentro de un año nadie sabrá de dónde salieron.»',
      '«Quiero que con esa grabación podamos sacar contenido diario para 120 días.» ' + FR, 'frase de la pieza'),
    e('R26', ', y contar cada mes qué pasa, sin precio.', ', sin precio.', 'promesa que no hiciste'),
    # R28: tu voz nombra cuatro bloques, y «Empieza por tu enlace» era la fase 3 que quitaste el 18 oct
    e('R28', 'Foto, nombre, bio, enlace y destacadas: es lo primero que miro en cada diagnóstico, y lo que ve tu próximo cliente antes de la reunión.',
      'Analizo lo que ve tu próximo cliente antes de agendarte una llamada de ventas.', 'tu voz no mira la foto'),
    e('R28', 'Empieza por tu enlace: debe llevar a algo que solo pide quien encaja contigo.',
      'Nombre: ¿lleva lo que haces? Bio: ¿a quién ayudas? Enlace: ¿lleva a algo que solo pide quien encaja? Destacadas: ¿enseñan lo que has hecho?',
      'era la fase 3 que quitaste el 18 oct; van tus cuatro preguntas'),
    e('R28', 'mirando tu perfil bloque a bloque: foto, nombre, bio, enlace y destacadas.', 'mirando tu perfil bloque a bloque: nombre, bio, enlace y destacadas.', 'destino'),
    e('R28', 'Abajo, el cursor va de bloque en bloque: foto, nombre, bio, enlace, destacadas.', 'Abajo, el cursor va de bloque en bloque: nombre, bio, enlace, destacadas.', 'fondo'),
    e('R28', 'Un rótulo por bloque, arriba: «Foto» / «Nombre» / «Bio» / «Enlace» / «Destacadas».', 'Un rótulo por bloque, arriba: «Nombre» / «Bio» / «Enlace» / «Destacadas».', 'rótulos'),
    e('R28', 'el cursor lo recorre de arriba abajo y vuelve a la foto.', 'el cursor lo recorre de arriba abajo y vuelve al nombre.', 'fondo'),
    e('R28', '(foto, nombre, bio, enlace, destacadas, cada uno en verde, ámbar o rojo)', '(nombre, bio, enlace y destacadas, cada uno en verde, ámbar o rojo)', 'idea'),
    e('R28', 'La salida se cierra en un solo bloque, el enlace, y va en el pie: la fase 3, que la decía, la quitaste en tu versión del 18 oct.',
      'La salida no va ni en la pieza ni en el pie: la fase 3, que la decía («empieza por tu enlace»), la quitaste en tu versión del 18 oct.', 'no volver a lo que quitaste'),
    # R31
    e('R31', 'Lo que tu sector ya dice de ti es tu primer vídeo.', '', 'máxima mía', borrar=True),
    e('R31', ' Lo demás llegó después.', '', 'frase de pausa mía'),
    e('R31', 'Pregúntate con qué te asocian tus clientes: eso es lo que debe contar tu marca.',
      'Pregúntate con qué te asocian tus clientes, y eso es lo que debe contar tu marca.', 'como lo dices tú, sin dos puntos de revelación'),
    e('R31', '«Lo que tu sector ya dice de ti es tu primer vídeo.»',
      '«Primero hay que empezar cerrado, buscar asociarte solo con una cosa muy concreta, luego vas abriendo según vas creciendo.» ' + FR, 'frase de la pieza'),
    # R35: la voz solo habla de la agencia
    e('R35', 'Un perfil que se repite: contrató una agencia, hizo un podcast, publicó. Y te comparan por precio con gente que no ha hecho ni la mitad. ',
      '', 'tu voz solo habla de la agencia'),
    # N15: el pie repetía el escrito; van tus tres pasos
    e('N15', 'No llegues a grabar con ideas: llega con lo que tu comprador quiere saber antes de contratarte, y unos puntos de apoyo debajo.',
      'Lo que vas a contestar sale de lo que tu comprador quiere saber antes de contratarte. Debajo, unos puntos de apoyo, para que no tengas que pensar tanto. Y contestas como le contestarías a un cliente en una reunión.',
      'repetía el gancho escrito (SOP-11); van tus tres pasos'),
    # Pendientes
    e('PENDIENTES', 'R37 (va N22), R39 (ese jueves va NS4, tu historia)', 'R37 (en su sitio va N05), R39 (ese jueves va NS9)', 'desfasado'),
    e('PENDIENTES', 'y en N05 y N16 el gancho escrito pasa a un «Cómo», como dejas tú los escritos.',
      'en N16 el gancho escrito pasa a un «Cómo», y en N05, en la revisión final, a la pregunta de su gancho B, como dejas tú los escritos.', 'N05'),
    e('PENDIENTES', 'que pasa a tu principio («Mi estrategia de contenido parte de este principio: primero las ideas, y después los cortes.»).',
      'que pasa a tu principio («Mi estrategia de contenido parte de este principio: primero las ideas, y después los cortes.»). En la revisión final (21 oct), lo mismo en R21, R25, R26, R28, R31, R35, N15 y N16: fuera las máximas mías y lo que tu voz ya no dice, y en su lugar frases de tu locución, también en la frase de la pieza. En R28 sale «Empieza por tu enlace», que era la fase que quitaste el 18 oct, y la foto, que tu voz no mira; en R26, «lo cuento aquí cada mes, también si no sale», que no lo has dicho tú. Ningún pie repite ya el gancho escrito de su pieza.', 'pies'),
]

base = '/tmp/claude-0/-home-user-Claude-real-este/bb8756ca-7159-57b4-84fe-165cd7e375cc/scratchpad/work/'
json.dump(NOV, open(base + 'nov_rev_mias.json', 'w'), ensure_ascii=False, indent=1)
json.dump(DIC, open(base + 'dic_rev_mias.json', 'w'), ensure_ascii=False, indent=1)
print(len(NOV), len(DIC))
