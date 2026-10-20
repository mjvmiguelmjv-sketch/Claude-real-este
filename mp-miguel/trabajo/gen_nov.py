from gen_spec import gen
R=lambda d:'Reel · '+d; H=lambda d:'Historias · '+d
cal=[('R01',R('lun 2 nov')),('N01',R('mar 3 nov')),('S01',H('mar 3 nov')),('N23',R('mié 4 nov')),('R04',R('jue 5 nov')),
('S03',H('vie 6 nov')),('R06',R('lun 9 nov')),('N04',R('mar 10 nov')),('S04',H('mar 10 nov')),('N25',R('jue 12 nov')),('NS1',H('jue 12 nov')),
('NS2',H('vie 13 nov')),('R11',R('lun 16 nov')),('R12',R('mar 17 nov')),('S07',H('mar 17 nov')),('R13',R('mié 18 nov')),('R14',R('jue 19 nov')),
('NS5',H('jue 19 nov')),('S09',H('vie 20 nov')),('N17',R('lun 23 nov')),('N24',R('mar 24 nov')),('S10',H('mar 24 nov')),('R18',R('mié 25 nov')),
('N21',R('jue 26 nov')),('S11',H('jue 26 nov')),('S12',H('vie 27 nov'))]
salen=['R02','R03','R05','R08','S02','S05','S06']
entran={'N01':('sust','martes 3 de noviembre, en el sitio de R02'),'N23':('critica','miércoles 4 de noviembre, en el sitio de R03'),
'N04':('sust','martes 10 de noviembre, en el hueco de R07'),'N25':('critica','jueves 12 de noviembre, en el hueco de R09'),
'NS1':('critica','jueves 12 de noviembre, en el hueco de S05'),'NS2':('critica','viernes 13 de noviembre, en el sitio de S06'),
'NS5':('critica','jueves 19 de noviembre, en el hueco de S08'),'N17':('sust','lunes 23 de noviembre, en el hueco de R16'),
'N24':('critica','martes 24 de noviembre, en el hueco de R17'),'N21':('critica','jueves 26 de noviembre, en el hueco de R19')}
M='Miguel'
pend=[
['Todas las que piden','El mensaje automático de DIAGNÓSTICO montado y probado, y la página del diagnóstico maquetada (ficha 8.11)',M,'La publicación de toda pieza que pide DIAGNÓSTICO'],
['N01, N04, N17, N21, N23, N24, N25; NS1, NS2, NS5','El gancho de cada pieza: va escrito el favorito de la propuesta; la elección es tuya (Por decidir)',M,'La grabación y el diseño'],
['Los reels','Los vídeos de referencia, por formato y no por pieza (12 oct)','Claude, con referencias-pieza; Miguel valida','La grabación'],
['N23','Por decidir: quién analizó tus 144 guiones y qué cifra sale. Los analizó Claude por encargo tuyo, así que la pieza no puede decir «analicé»: va «puse a una inteligencia artificial a analizar uno a uno» (la otra opción: «pedí que me analizaran uno a uno»). Y la cifra: 79 de 144, o «más de la mitad»',M,'La grabación'],
['NS1','Por decidir: si el Método Reflejo se nombra en la pantalla 3 (hoy no va); la caja de preguntas sale de esta secuencia',M,'No bloquea'],
['NS2','Tu bio nueva, si va a estar puesta el 13 de noviembre, o una línea tuya sobre si la vas a cambiar: el día que salga NS2, la bio de tu perfil no puede ser la del 11 oct',M,'La publicación'],
['N21, N25, NS5','Frases de compradores de verdad, de tus primeras conversaciones: el dolor de N21 y el deseo de N25. Hoy son tuyas (fuente 4)',M,'No bloquea'],
['N17','Por decidir: qué cifra de la propuesta de abril se deja ver en pantalla (las reales; nunca «180 reels por 1.200 €») y si la conservas. Si no se enseña, sale la frase «La propuesta sigue en una carpeta…»',M,'La grabación'],
['NS1, NS5','Por decidir: qué interacciones usan tus historias (reglas de la casa, apartado 7, punto 6). Van escritas como pide cada estructura',M,'No bloquea'],
['N24','Comprobar con el VSL entero que N24 no repite sus frases','Claude','La grabación'],
['R04, R11, R14','Terminan en la tesis, sin pedir, como tu locución. Si quieres llamada: «Si quieres que personalmente analice por qué no te funcionó lo que probaste, comenta DIAGNÓSTICO y hablamos por privado.»',M,'No bloquea'],
['R04, R14','Usaban la foto de la diana de R02, que sale del mes: o se hace esa foto suelta o sale del montaje',M,'El montaje'],
['R04','Confirmar que el permiso de PDC cubre el fragmento del minuto 52:50 de Diego Abreu en un reel propio','Miguel, con PDC','La publicación'],
['R11, S04, S10','Por decidir: el gancho de voz de R11 abre con Hormozi y no filtra; S04 abre con una creencia del oficio; S10 abre con «el estratega de Hormozi» sin nombrar a Caleb. La crítica no trae frase concreta y no se ha inventado',M,'No bloquea'],
['R06, ranura del domingo','Las cifras reales de la propuesta de abril, y si se enseña difuminada. Fuera «1.200 €»',M,'El inserto de R06 y la ranura del domingo'],
['R14','El segundo exacto del corte 1 del reel de Luis (DZdK0rOxDKI) y el usuario exacto de su cuenta','Miguel, al verlo','La grabación'],
['R18, S09, S11, ranura del miércoles','Qué grabación de PDC se enseña, las notas reales y el permiso del invitado o su nombre difuminado','Miguel, con PDC','La grabación de R18 y el diseño de S09, S11 y la ranura'],
['S03','Que «En 30 minutos analizo…» de tu pantalla 4 se quede así. La primera llamada hecha, para la captura del diagnóstico; hasta entonces, la plantilla vacía',M,'La publicación'],
['S09, S12','Las capturas reales: la lista de episodios de un podcast con permiso (S09) y la bandeja de enviados con tres presupuestos difuminados (S12)',M,'El diseño'],
['Ranura, lunes y miércoles','El permiso de Luis, reconfirmado; sus documentos se enseñan como método, nunca como resultado',M,'Esas ranuras'],
['Ranura, sábado','La frase exacta de 6sense, Edelman y Gartner como está en la ficha, para los rótulos. Y el censo: dice «23 proveedores» y «autoridad en 9 webs», y la crítica habla de 22 webs: una sola cifra',M,'La ranura del sábado'],
['Jueves 5 de noviembre','Sin secuencia (era S02). Si quieres una personal, con otra pregunta de tu banco; la crítica propone «¿Qué viste en Píldoras que te hizo cambiar de oficio?»',M,'No bloquea'],
['Todo el mes','auditoria-marca sobre lo nuevo y lo ajustado; ningún texto está aprobado hasta pasarla','Claude, con auditoria-marca; Miguel decide los hallazgos','La aprobación de la puerta'],
]
pp=['Salen de noviembre y siguen en tus Docs anteriores, sin borrar nada: R02 (la sostenían Kallaway y un 80 % sin fuente; va N01), R03 (fórmula de bio genérica y «HT»; va N23), R05 (dos promesas con cifra sin dato y era un trozo de V1; su sitio queda vacío), R08 (núcleo de Caleb y el plan de Luis sin ejecutar como demostración; su sitio queda vacío), S06 (dos cifras sin fuente y la escasez inventada; va NS2), y S02 y S05 (anunciaban o troceaban un vídeo de YouTube: tu decisión del 19 oct).',
'Huecos sin pieza: viernes 6 (R05), miércoles 11 (R08), viernes 13 (R10, era un corte de V1), viernes 20 (R15) y viernes 27 (R20), los dos últimos, cortes de vídeo largo.',
'Piezas marcadas DEVOLVER AL REPARTO: ninguna.']
gen('nov','nov_r5.docx',cal,salen,entran,['nov_edits.json','nov_edits2.json'],pend,pp,
 '/home/user/Claude-real-este/mp-miguel/entregas/MP Miguel · Guiones · noviembre 2026 · r6 · 20 oct 2026.docx','r6')
