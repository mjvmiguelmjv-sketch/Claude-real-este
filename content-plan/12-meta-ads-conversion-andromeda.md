# 12 — Meta Ads: Conversión-first bajo Andromeda + Píxeles (explicado de cero)

> Reemplaza el enfoque clásico de embudo por audiencias. Bajo **Andromeda** (el motor de
> Meta, global desde oct-2025), **el creativo elige la audiencia**, no tú. Esto valida la
> intuición del usuario: ir directo a **conversión**, con **lenguaje específico que autofiltra**
> al ICP, y **maximizar resultado, no minimizar CPC**. Aquí está cómo, y la parte de medición
> explicada desde cero.

## 1. Qué cambió con Andromeda (y por qué nos conviene)
- Antes: tú definías la audiencia (intereses, lookalikes) y Meta entregaba dentro de ella.
- Ahora: Andromeda **lee tu creativo** (formato, hook, tono, tema, idioma) y **predice a quién
  enseñárselo** según el comportamiento real de cada usuario.
- **Consecuencia práctica:** el targeting lo hace el **guion y el lenguaje del vídeo**. Si hablas
  con la jerga del comercio cripto-fluido (o del comerciante venezolano que usa USDT), Andromeda
  se lo enseña a ese perfil y descarta al resto. **El autofiltrado por lenguaje ahora es la estrategia, no un truco.**
- Por eso **no montamos escaleras TOFU/MOFU manuales**: corremos conversión y dejamos que
  creativo + señal hagan el trabajo. (Sí mantenemos retargeting básico de quien ya interactuó — barato y rinde.)

## 2. La estructura de campañas (simple a propósito)
- **1 campaña de conversión** (objetivo: Ventas/Conversiones) optimizada por nuestro evento.
- **Estructura Advantage+** (campaña de conversión automatizada), pocos conjuntos de anuncios.
- **Mucha diversidad creativa:** Meta recomienda **15–20 anuncios activos** con hooks/formatos
  distintos. Aquí es donde entran nuestros guiones de testimonio + objeción + LATAM (`05`, `08`).
- **Retargeting (1 conjunto):** quien comentó/escribió DM, vio 50%+ de un vídeo, o visitó la web.
- **Sin obsesión por CPC:** se optimiza por el **evento de conversión**, no por clics baratos.

## 3. El problema del arranque (y cómo lo resolvemos)
Una campaña de conversión necesita **muchos eventos por semana** para "aprender" (salir de fase
de aprendizaje). Al principio "tienda conectada" ocurrirá poco. Solución: **evento puente**.
- Arrancamos optimizando por el **lead de DM** (comment-to-DM / Click-to-Message) o "registro
  iniciado" — ocurren mucho y son baratos. Así la campaña aprende.
- Cuando hay volumen de "tienda conectada", subimos la optimización a ese evento de valor.
- Este puente es la razón por la que el **sistema comment-to-DM (`11`) y los anuncios van de la mano**.

## 4. Píxeles y medición — desde cero (para quien no tiene ni idea)
**¿Qué es el Píxel?** Un trocito de código en la web de Zeno que le avisa a Meta de lo que hace
la gente: visitó, empezó el registro, conectó tienda. Sin esto, Meta entrega "a ciegas".

**¿Por qué el píxel solo ya no basta?** Los navegadores bloquean cookies y rastreo. Mucha
señal se pierde. Resultado: Meta optimiza peor y **Andromeda penaliza** a quien solo usa píxel.

**La solución: Conversions API (CAPI).** Es el **servidor** de Zeno mandándole los eventos a
Meta directamente (no el navegador). Píxel + CAPI **a la vez**, con **deduplicación** (para no
contar el mismo evento dos veces). Esto mejora cuánto pasa tu anuncio por el filtro de Andromeda.

**Event Match Quality (EMQ).** Una nota de 0–10 de cómo de bien casa Meta tus eventos con
usuarios reales (mejora mandando email/teléfono hasheado, IP, etc., con consentimiento).
**Objetivo: EMQ > 7.** Cuanto más alto, mejor entrega y menor coste.

**Los eventos que definimos (en orden de valor):**
| Evento | Qué significa | Uso |
|---|---|---|
| `PageView` | visita la web | base / retargeting |
| `ViewContent` | ve "cómo funciona" / demo | señal de interés |
| `Lead` (DM) | inicia conversación cualificada | **evento puente de arranque** |
| `InitiateRegistration` | empieza el registro en el dashboard | optimización intermedia |
| `StoreConnected` (personalizado) | conecta tienda/checkout = activación | **conversión de valor (north-star)** |

## 5. Creatividades: el framework de anuncio-testimonio
El usuario quiere **testimonios** que digan que un negocio implementó Zeno y siga hablando con
**lenguaje específico** del ICP. Estructura recomendada (15–25s):
1. **Hook con lenguaje de iniciado (autofiltra):** una frase que solo "le suena" al ICP
   (p. ej. "Llevaba meses comiéndome los chargebacks y reservas de Stripe…" o, LATAM:
   "Mis clientes ya me pagaban en USDT, pero cobrarlo limpio era un lío…").
2. **Testimonio:** el comercio cuenta el dolor + que implementó Zeno + el resultado concreto. `[TESTIMONIO]`
3. **Prueba en pantalla:** dashboard real, 0,1%, tx on-chain (refuerza confianza — ver `14`).
4. **CTA de conversación:** "comenta ZENO" o "toca para escribirnos" (Click-to-Message).

Variar el **hook** y el **ángulo** (ahorro / chargebacks / desconfianza-0,1% / LATAM-necesidad)
da los 15–20 creativos que Andromeda necesita, y cada uno autofiltra a un sub-perfil.

## 6. Presupuesto y escalado (orientado a resultado)
- **Validación:** presupuesto pequeño, 15–20 creativos, optimizando por el evento puente. Mata
  lo que no genera leads cualificados; conserva los hooks que sí.
- **Escalado:** sube ~20% cada 3–4 días sobre lo que convierte (no resetees el aprendizaje);
  duplica ganadores en vez de editarlos.
- **Métrica que manda:** **coste por lead cualificado** y luego **coste por tienda conectada**
  (CPA). Define un CPA máximo según el valor de un comercio (LTV) y deja que gobierne el gasto.
- Frecuencia alta + CTR cayendo = fatiga → rota hook nuevo.

## 7. Cumplimiento de política (cripto en Meta)
- Posicionar como **software de pagos para comercios (B2B)**, no inversión ni "gana dinero con cripto".
- Sin rentabilidades garantizadas, sin "hazte rico", sin urgencia falsa, sin "evita Hacienda".
- Confirmar estado de **anunciante cripto aprobado** en Business Manager y licencias por geo antes de escalar.

## 8. Checklist de puesta en marcha
- [ ] Píxel + CAPI instalados y deduplicados; `StoreConnected` y `Lead` (DM) disparando.
- [ ] EMQ > 7 verificado en Events Manager.
- [ ] ManyChat conectado para Click-to-Message + comment-to-DM (`11`).
- [ ] 15–20 creativos cargados (testimonio/objeción/LATAM), cada uno con su `utm_content`=ID.
- [ ] Campaña de conversión optimizando primero por evento puente; plan para subir a `StoreConnected`.
- [ ] Aprobación de política cripto en regla para España + LATAM objetivo.
