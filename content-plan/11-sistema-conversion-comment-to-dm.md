# 11 — Sistema de Conversión: Comment-to-DM + Click-to-Message

> Cómo convertimos atención en clientes **sin depender del "link in bio"**. El DM convierte
> 3–5x más que el enlace en bio, y cada interacción genera un evento barato que alimenta el
> píxel (ver `12`). Este es el mecanismo central de conversión para orgánico y para anuncios.

## La idea en una frase
El contenido no manda a la web: **inicia una conversación**. La persona comenta una palabra
clave → recibe un DM automático → se cualifica sola → pasa al registro (o a Hugo). El propio
flujo **filtra** a quien no es ICP y **calienta** a quien sí lo es.

## Flujo orgánico (comment-to-DM)
1. **Publicas** un Reel (testimonio / objeción de confianza / dolor LATAM). CTA verbal + texto:
   *"Comenta **ZENO** y te mando cómo funciona."* (palabra clave en mayúsculas, fácil de recordar).
2. La herramienta (ManyChat / Inrō / nativo de IG) detecta el comentario y:
   - Responde públicamente al comentario (señal de actividad para el algoritmo): *"¡Te lo mando al DM! 📩"*.
   - Manda un **DM automático** con el primer mensaje del flujo (abajo).
3. El DM **cualifica con 1–2 preguntas** (plataforma, volumen, país) — esto autofiltra y nos
   dice si es ICP.
4. Según la respuesta:
   - **ICP claro** → enlace a `dashboard.zenobank.io` + oferta de que Hugo conteste dudas.
   - **Dudas/desconfianza** → se le manda el contenido de la objeción (`14`) antes del enlace.
   - **No-ICP** → respuesta útil y cordial, sin gastar más esfuerzo.

## Flujo pagado (Click-to-Message)
En Meta Ads se puede usar el objetivo donde el clic **abre el DM directamente** (Instagram
Direct / Messenger) en vez de ir a una web. ManyChat recoge esa conversación y corre el mismo
flujo de cualificación. Ventajas para Zeno:
- Ideal para **B2B y para vencer la desconfianza**: la conversación humaniza antes de pedir el registro.
- Genera el **evento puente** (lead de DM) que el píxel necesita para aprender al principio (ver `12`).
- Se puede combinar con anuncios que **también** van a web (conversión directa) y repartir presupuesto.

## Guion del DM (plantilla — automático con entrada de Hugo)
> Sustituye los `[MARCADORES]` con datos reales de Hugo (`13`).

**Mensaje 1 (auto, inmediato):**
"¡Hey! Soy el equipo de Zeno (y a veces el propio Hugo 👋). Te mando cómo aceptar cripto al
0,1% sin chargebacks. Antes, para no hacerte perder el tiempo: ¿vendes con **Shopify,
WooCommerce u otra cosa**?"

**Mensaje 2 (según respuesta):**
"Genial. Última: ¿más o menos **cuánto facturas al mes** y **desde qué país** te compran?
(así te digo exactamente cuánto ahorrarías y si te encaja)."

**Mensaje 3A (ICP, confianza ok):**
"Perfecto, esto te encaja. Aquí montas tu checkout en minutos 👉 dashboard.zenobank.io —
si quieres, Hugo te resuelve cualquier duda por aquí mismo antes de empezar."

**Mensaje 3B (desconfianza / 'demasiado barato'):**
"Te entiendo, suena demasiado barato. Mira esto de 60s sobre dónde está (y dónde NO está) la
trampa: [enlace al contenido de `14`]. Y si quieres, te lo enseño en directo. Sin presión."

**Mensaje 3C (LATAM / necesidad):**
"Si tus clientes ya te pagan en USDT o por Binance Pay, Zeno te lo unifica en un checkout y,
si quieres, el dinero va directo a TU wallet (tus claves, nadie te lo congela). Te enseño 👉 [enlace]."

## Reglas de oro del flujo
- **Responde rápido:** el 75% espera respuesta en <24h; en DM, cuanto más rápido, más convierte. Automatiza el primer toque.
- **Cualifica antes de vender:** 1–2 preguntas máximo. Sirven para filtrar Y para que el píxel aprenda quién es buen lead.
- **Hugo aparece:** que el lead sienta que hay una persona real detrás (refuerza la cuña de transparencia). Aunque el inicio sea automático, los leads calientes los toca Hugo.
- **Un solo CTA por pieza:** siempre la misma palabra clave por campaña para no liar el flujo.
- **Cumplimiento:** nada de promesas de rentabilidad ni de "esquivar Hacienda" en el DM; si surge lo fiscal, se enlaza el contenido educativo con su disclaimer.

## Herramientas (elige una)
- **ManyChat** — el estándar, multiplataforma, integra Click-to-Message. Recomendado para empezar.
- **Inrō / Chatfuel** — fuertes si Instagram es la prioridad absoluta.
- **Nativo de Instagram** (respuestas automáticas a palabras clave) — gratis y básico; sirve para validar antes de pagar una herramienta.

## Qué medir aquí (enlaza con `09` y `12`)
- Comentarios con palabra clave → DMs iniciados → leads cualificados → clics a dashboard → **tienda conectada**.
- Tasa de cualificación (qué % de los que comentan son ICP) — afina hooks y lenguaje de autofiltrado.
- El **lead de DM** se envía a Meta como evento (vía API) para optimizar las campañas (ver `12`).
