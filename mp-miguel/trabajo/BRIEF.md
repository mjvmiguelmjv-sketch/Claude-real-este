# Encargo: sustituciones exactas para aplicar la crítica CALMA del 19 oct a los guiones de Miguel

Carpeta de trabajo: `/tmp/claude-0/-home-user-Claude-real-este/bb8756ca-7159-57b4-84fe-165cd7e375cc/scratchpad/work/`
Scripts: `/home/user/Claude-real-este/mp-miguel/scripts/` (`docxedit.py`, `volcado.py`). Lee `/home/user/Claude-real-este/mp-miguel/MEMORIA.md` primero: secciones 3 y 4 son las reglas que mandan.

## Qué produces
Un archivo JSON (lista) de sustituciones, cada una:
```json
{"ambito": "R13", "old": "texto exacto", "new": "texto nuevo", "porque": "razón corta, con la parte de la crítica"}
```
- `ambito` es el código de la pieza (R01, S03…) o `CABECERA` o `RANURA DIARIA DE PRUEBA SOCIAL`.
- `old` tiene que estar **dentro de un solo párrafo** y aparecer **una sola vez** en el ámbito. Cópialo del volcado por párrafos (`*_p.txt`: cada línea es un párrafo; en tablas, `<etiqueta> ¶ texto`). No incluyas la etiqueta ni el `¶`.
- `new` vacío borra. Para cambiar un párrafo entero, `old` = el párrafo entero.
- Comprueba tu JSON con: `python3 /home/user/Claude-real-este/mp-miguel/scripts/docxedit.py check <doc.docx> <tu.json>` hasta que dé 0 errores.

## Lo que se aplica (Miguel delegó la puerta: se aplica lo que la crítica marca como «Propongo»/«Sí»/«Qué haría»; lo que es suyo de verdad NO se inventa)
Fuentes, por orden de autoridad:
1. `crit_2_4.txt` — su tono (parte 2), la crítica mes a mes con el veredicto de cada pieza (parte 3) y «Lo que falta», con la tabla «Tu filtro, pieza a pieza» (parte 4): aplica las frases marcadas «Sí» (no las «Alternativa»).
2. `crit_6_9.txt` — parte 9, «Las peores, y qué haría con cada una»: aplica el «Qué haría» de las piezas que se AJUSTAN (no de las que se quitan, que las quito yo).
3. `plan_mejora_y_sop.txt` (plan de mejora del 15 oct, parte 3) para las piezas que la crítica del 19 solo resume en «Lo principal».

Reglas que van en TODAS las piezas de tu lote:
- **La ronda de llamadas**: todas las llamadas, rótulos, notas de edición, pies y fichas que mandan a FRÍAS, VALOR, PILARES, IMPROVISO, CURIOSOS, PRÁCTICAS, «sígueme», «la web», el formulario de tres preguntas o «la llamada de treinta minutos» pasan a **DIAGNÓSTICO por WhatsApp**: en reels, «Si quieres que personalmente analice X, comenta DIAGNÓSTICO y hablamos por privado.», donde X es lo que esa pieza acaba de enseñar (concreto, no «tu estrategia»); en historias, «Responde DIAGNÓSTICO» + lo que miras. En el campo «Destino del CTA»/«CTA» de la ficha: «DIAGNÓSTICO por WhatsApp (comentario o respuesta → mensaje privado automático con el enlace a WhatsApp → contestas tú → el diagnóstico, una página con tres hallazgos), mirando X.» La palabra y la llamada, solo en Instagram (como ya dicen las notas). Si la locución hablada ya es de Miguel y ya dice DIAGNÓSTICO, respeta sus palabras y solo arregla lo que no casa (rótulo, pie, nota).
- La escasez solo como «Trabajo con dos empresas a la vez.» Fuera «huecos esta semana», «Solo puedo revisar 2».
- «HT» → «High Ticket» (con todas sus letras). «la trampa viral» se acredita a Kallaway la primera vez que sale en la pieza.
- Fuera cifras retiradas o sin fuente: «180 reels al mes por 1.200 €», «de 1 año a 3 meses», el 80 % sin fuente, «Más del 70%», resultados prometidos sin prueba.
- Nada que anuncie un vídeo de YouTube o diga que la pieza es un trozo del vídeo largo **en las secuencias** (decidido). En reels es «Por decidir» de Miguel: NO lo quites; solo lista esas líneas en tu informe.
- No reescribas lo que la crítica dice que se queda; no metas frases de comprador inventadas; no metas CALMA, «Carlos Draghici» ni notas en nada. Respeta las frases de Miguel (sus erratas incluidas) salvo donde la crítica pide cambiarlas.
- Castellano peninsular, tono de Miguel (MEMORIA, sección 4).

## Entrega
1. El JSON en `work/<lote>_edits.json`, comprobado con 0 errores.
2. Un informe corto (en tu respuesta final, en castellano): por pieza, qué cambiaste y por qué en una línea; y lo que NO pudiste hacer porque necesita material o decisión de Miguel (eso irá a «Por decidir»). No apliques nada a los .docx: solo el JSON.
