from gen_spec import gen
R=lambda d:'Reel · '+d; H=lambda d:'Historias · '+d
cal=[('R21',R('lun 30 nov')),('N07',R('mar 1 dic')),('S13',H('mar 1 dic')),('N13',R('mié 2 dic')),('NS6',H('jue 3 dic')),
('R25',R('vie 4 dic')),('S15',H('vie 4 dic')),('R26',R('lun 7 dic')),('N26',R('mar 8 dic')),('S16',H('mar 8 dic')),('R28',R('mié 9 dic')),
('NS7',H('jue 10 dic')),('R30',R('vie 11 dic')),('S18',H('vie 11 dic')),('R31',R('lun 14 dic')),('N27',R('mar 15 dic')),
('N15',R('jue 17 dic')),('NS3',H('jue 17 dic')),('R35',R('vie 18 dic')),('S21',H('vie 18 dic')),('N18',R('lun 21 dic')),
('N22',R('mar 22 dic')),('S22',H('mar 22 dic')),('R38',R('mié 23 dic')),('NS4',H('jue 24 dic (se programa por la mañana)')),
('S24',H('sáb 26 dic')),('SP1',H('mar 29 dic (semana de puente)')),('SP2',H('jue 31 dic (semana de puente)'))]
salen=['R23','R24','R33','R37','R39','S14','S17','S19','S20','S23']
entran={'N07':('sust','martes 1 de diciembre, en el hueco de R22'),'N13':('sust','miércoles 2 de diciembre, en el sitio de R23'),
'NS6':('critica','jueves 3 de diciembre, en el hueco de S14'),'N26':('critica','martes 8 de diciembre, en el hueco de R27'),
'NS7':('critica','jueves 10 de diciembre, en el hueco de S17'),'N27':('critica','martes 15 de diciembre, en el hueco de R32'),
'N15':('sust','jueves 17 de diciembre, en el hueco de R34'),'NS3':('critica','jueves 17 de diciembre, en el hueco de S20'),
'N18':('sust','lunes 21 de diciembre, en el hueco de R36'),'N22':('critica','martes 22 de diciembre, en el sitio de R37'),
'NS4':('critica','jueves 24 de diciembre, en el hueco de S23')}
M='Miguel'
pend=[
['Todas las que piden','El mensaje automático de DIAGNÓSTICO montado y probado, y la página del diagnóstico maquetada (ficha 8.11)',M,'La publicación de toda pieza que pide DIAGNÓSTICO'],
['N07, N13, N15, N18, N22, N26, N27; NS3, NS4, NS6, NS7','El gancho de cada pieza: va escrito el favorito de la propuesta; la elección es tuya (Por decidir)',M,'La grabación y el diseño'],
['Los reels','Los vídeos de referencia, por formato y no por pieza (12 oct)','Claude, con referencias-pieza; Miguel valida','La grabación'],
['N13, NS3','El visto bueno de Fernando al texto de su testimonio y a que salga en historias; qué se hace con «mineralización»','Miguel, con Fernando','La publicación de las dos'],
['NS4','Tus respuestas: en la pantalla 2, qué viste y con qué cliente para dejar de vender reels por volumen; en la 3, lo que haces hoy en vez de volumen. Y la carpeta de los reels de abril, si la conservas',M,'Sin ellas no sale'],
['N22','Por decidir: por qué se llama Método Reflejo. Si es tu porqué, vuelve a la fase 2 y al pie',M,'No bloquea'],
['N26','Por decidir: lo concreto de cada paso (entender, comprobar, confiar) sale de la ficha 8.4, donde es una propuesta. Que lo valides',M,'La grabación'],
['N27','Por decidir: la fase 3 («en un anuncio eliges a quién se le enseña, pero no cambias a quién le habla el vídeo») es una lectura de tu oferta, no frase tuya; y la idea de anunciar solo lo que ya funcionó: tuya o con el crédito a Fernando',M,'La grabación de la fase 3'],
['NS3','Por decidir: la pantalla 4 (la llamada que mira qué ha visto de tu trabajo el que te escribe, o la otra mitad de la frase de tu web). La web publicada con la frase y el testimonio que usa (la v40 está sin subir)',M,'La publicación'],
['NS4, NS6, NS7','Por decidir: qué interacciones usan tus historias (reglas de la casa, apartado 7, punto 6). Van escritas como pide cada estructura',M,'No bloquea'],
['R21, R25, R30, R35','Por decidir: si tu regla de no anunciar ni trocear un vídeo de YouTube vale también para reels (el pie de R21, «El jueves desmonto esta práctica y dos más, en un vídeo entero.»; «El vídeo entero, en YouTube» y «Práctica 1 de 3» en R25, R30 y R35). Y si V3 y V4 se graban: si no, R25, R30 y R35 se graban sueltos',M,'La publicación de las cuatro'],
['Ranura, jueves 3 y 17','Por decidir: la captura de V3 y V4 publicados anuncia el vídeo largo',M,'La ranura de esos jueves'],
['R28','El veredicto real de un bloque del perfil, con una cuenta con permiso por escrito o la tuya de abril. Y si en tu voz «llamada de diagnóstico» pasa a «diagnóstico» (el hablado y la fase 1 son tuyos y no se han tocado)',M,'La grabación'],
['R30','Si el final (la llamada y el pie) se borró sin querer: hoy termina sin cierre. Su escrito sigue siendo de oficio',M,'La publicación'],
['R26','El estado real a 7 de diciembre: cuántos de los dos clientes (aunque sea cero). «Dejé de editar 180 reels al mes» se deja como tu error, con tus palabras',M,'La grabación'],
['R31','La red y la fecha en que José Elías empezó a publicar (ficha 11.3); la pieza se sigue apoyando en la prueba de otro',M,'La publicación'],
['S16','Una consulta real (mensaje, correo o llamada); si no llega, va la versión MITO, escrita al pie de la ficha',M,'Nada: hay versión MITO'],
['S18, SP1','El cierre real de noviembre, con alcance y conversaciones por separado','Miguel, con cierre-mes','El diseño: las cifras van en los huecos'],
['S21, S24','Confirmar que la agenda de diagnósticos cierra del 23 de diciembre al 7 de enero. Los fondos «con los huecos que quedan» rozan la regla de la escasez («trabajo con dos empresas a la vez»)',M,'Si no es real, la pantalla 4 de S21 pasa a coste de la inacción y el cierre a blando (está escrito)'],
['S22','Confirmar la frase añadida en la pantalla 3: «Yo todavía no tengo el mío: cuando lo tenga, lo verás aquí.»',M,'La publicación'],
['SP2','La captura del perfil del 2 de noviembre, la de hoy y lo que hubo entre tus dos perfiles. La pantalla 3 sigue explicando el cambio con el recorrido de marca de Caleb Ralston',M,'El diseño'],
['S24','La prueba es la anécdota de Caleb, teniendo tú tus 180 reels: si la cambias por la tuya',M,'No bloquea'],
['Ranura, lunes y sábado; domingo','El permiso de Luis, reconfirmado. Y las cifras reales de la propuesta de abril, si quieres que vuelva al domingo (hoy no sale)',M,'Esas ranuras'],
['Huecos sin pieza','Jueves 3 (R24: tu nota pide rehacerla como reacción, viendo antes el vídeo), jueves 10 (R29), martes 15 (la secuencia del podcast, D12, sin escribir, en el sitio de S19), miércoles 16 (R33, la reunión no ha llegado) y sábado 26 (R40). Si se escribe algo, lo decides tú',M,'No bloquea'],
['Todo el mes','auditoria-marca sobre lo nuevo y lo ajustado; ningún texto está aprobado hasta pasarla','Claude, con auditoria-marca; Miguel decide los hallazgos','La aprobación de la puerta'],
]
pp=['Notas de edición que tus cambios de locución han dejado desfasadas, sin tocar: R21 (los rótulos de la fase 3), R25 (la «Estructura» dice que el CTA no se habla), R26 (la nota de la fase 2) y S13 («Kallaway» en negrita en la pantalla 3).',
'Salen de diciembre y siguen en tus Docs anteriores, sin borrar nada: R23 (va N13 en su sitio, el mismo caso de Fernando con su testimonio), R24 (tu nota: rehacerla como reacción), R33 (la reunión con permiso no ha llegado), R37 (va N22), R39 (ese jueves va NS4, tu historia), S19 (le pregunta al que graba, no al fundador) y S14, S17, S20 y S23 (anunciaban o troceaban un vídeo de YouTube: tu decisión del 19 oct).',
'Piezas marcadas DEVOLVER AL REPARTO: ninguna.']
gen('dic','dic_r3.docx',cal,salen,entran,['dic_edits.json','dic_edits2.json'],pend,pp,
 '/home/user/Claude-real-este/mp-miguel/entregas/MP Miguel · Guiones · diciembre 2026 · r4 · 20 oct 2026.docx','r4')
