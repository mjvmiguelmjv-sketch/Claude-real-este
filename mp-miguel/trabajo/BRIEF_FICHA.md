# Encargo: la ficha de marca v7 de Miguel, con su crítica del 20 oct aplicada

Carpeta: `/tmp/claude-0/-home-user-Claude-real-este/bb8756ca-7159-57b4-84fe-165cd7e375cc/scratchpad/work/`
Lee antes: `/home/user/Claude-real-este/mp-miguel/MEMORIA.md` (secciones 3 y 4 mandan).

## Fuentes
- `ficha_v6.docx`: la v6 de Miguel, que es la base. `ficha_p.txt` es el volcado por párrafos, con el ámbito entre corchetes: cada línea es un párrafo; en las tablas, `<etiqueta> ¶ texto`. `ficha_dump.txt` es el volcado por elementos, con las tablas enteras.
- `critica_ficha.txt`: la crítica de la v6 del 20 oct. **Es lo que se aplica.**
- `crit_2_4.txt` y `crit_6_9.txt`: la crítica de los guiones del 19 oct (contexto: su tono y sus decisiones).

## Lo que decidió Miguel: delegó la puerta («sigue tú con todo»)
Las cuatro preguntas de la parte 7 de la crítica van con la recomendación:
1. Se aplica todo lo de las partes 3, 4 y 5.
2. Se recorta lo de la parte 6 y la ficha se abre con el bloque «Para escribir».
3. Las frases de Caleb Ralston que iban como voz de sus clientes se marcan como de Caleb, traducidas.
4. La mezcla de nicho es el 80 %.

Todo lo demás de la parte 7 («Lo demás va a la v7 como Por decidir») va a **una sola lista «Por decidir»**, en la parte de Por resolver. Mientras no decida, cada punto se queda como está, salvo donde la crítica da su lectura. Lo de la parte 8 (lo que solo puede traer él) sustituye a los formularios.

## Qué produces
Un JSON de operaciones para `/home/user/Claude-real-este/mp-miguel/scripts/ficha_ops.py`. Lee su docstring: las operaciones son `sustituir`, `parrafo`, `borrar` e `insertar`, con bloques `titulo`, `etiqueta`, `texto`, `vineta` y `tabla`. Compruébalo con:

`python3 /home/user/Claude-real-este/mp-miguel/scripts/ficha_ops.py check ficha_v6.docx <tu.json>` hasta que dé 0 errores.

- Toca **solo tus partes**. Los anclajes de `borrar` e `insertar` se buscan entre los párrafos de primer nivel por su comienzo, así que elige comienzos únicos (si un comienzo se repite, alarga el prefijo). Para `sustituir` dentro de tablas, usa `ambito` = el Heading2 en mayúsculas, tal como sale entre corchetes en `ficha_p.txt` (por ejemplo `"A · ATENCIÓN: A QUIÉN LE HABLAS Y QUÉ LE DUELE"`), y `fila` si el texto se repite.
- Lo que se quita no desaparece: si la crítica dice que algo «va al banco» o «va al registro», copia ese texto tal cual en el `.md` que te digo en tu lote. La v6 sigue intacta en su Doc.
- Castellano peninsular, sin inventar nada. Lo que es suyo y no está decidido, «Por decidir». La ficha la lee Miguel: en ella CALMA sí puede nombrarse (es su estructura), pero **no se inventan notas nuevas** ni la ficha se puntúa a sí misma (la crítica pide sacar la nota).
- Las citas: si una cita está retocada, se deja el arreglo, pero se lista en 10.8 (esto lo hace el lote D con lo que le pasen los demás: pon en tu informe las que toques).

## Entrega
1. `work/ficha_<lote>.json`, comprobado con 0 errores.
2. En tu respuesta final, en castellano y corto: lo que cambiaste por apartado, en una línea cada uno; las citas retocadas que hayas tocado; y lo que dejas como «Por decidir», para que el lote D lo junte en la lista única.
