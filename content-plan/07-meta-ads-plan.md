# 07 — Plan de Meta Ads (Instagram + Facebook)

> La capa de adquisición pagada. Estrategia: deja que el **orgánico encuentre barato los
> hooks ganadores**, y luego pon presupuesto detrás de creatividades probadas en un embudo
> estructurado TOFU→MOFU→BOFU que impulse **registros cualificados en el dashboard**.
> Los copys/creatividades están en `08-meta-ads-copy.md`.

## ⚠️ Política primero (léelo antes de gastar un euro)
Meta restringe la publicidad de **productos y servicios de criptomonedas**. Requisitos probables:
- El anunciante/empresa puede necesitar **permiso por escrito / estar en la lista de
  anunciantes cripto aprobados de Meta**, y aportar las licencias/registros requeridos para las regiones objetivo.
- Los anuncios deben evitar afirmaciones prohibidas (sin rentabilidades garantizadas, sin
  "hazte rico", sin encuadre de evasión fiscal — alineado de todos modos con nuestros guardrails).
- Posiciona Zeno como **pasarela de pago / software para comercios** (encuadre B2B SaaS),
  no como inversión ni "gana dinero con cripto".
- **Acción:** confirma el estado de aprobación en Business Manager y envía la documentación
  requerida **antes** de lanzar. Si la aprobación está pendiente, corre objetivos de
  interacción/tráfico de menor riesgo mientras esperas, y mantén las landing pages limpias y conformes.

## Estructura de la cuenta
- 1 Business Manager → 1 Cuenta Publicitaria → 3 campañas por etapa del embudo (abajo).
- Convención de nombres: `ZB | [ETAPA] | [Objetivo] | [Audiencia] | [ID-Creatividad]`
  p. ej. `ZB | TOFU | VideoViews | BroadCrypto | AD-V-01`.
- Consolida presupuestos (Advantage+ CBO) a nivel de campaña para eficiencia de aprendizaje.

## El embudo

### TOFU — Conocimiento (arranca en la Semana 2)
- **Objetivo:** Reproducciones de vídeo / Alcance (y ThruPlay). Atención barata + construye pools de retargeting.
- **Audiencias:** Amplio + stacks de intereses de `00b` (Shopify, WooCommerce, e-commerce,
  dropshipping, Binance, crypto, stablecoin, Stripe, SaaS). Deja que Advantage+ amplíe.
- **Creatividades:** hooks orgánicos probados — AD-V-01 (choque de comisiones), AD-V-02
  (chargebacks), AD-V-04 (transfronterizo), AD-V-06 (confianza del founder). 9:16, subtitulados, 15–30s.
- **Ubicaciones:** Reels + Stories + Feed (ubicaciones Advantage+).
- **Meta:** ThruPlays baratos, hacer crecer las audiencias personalizadas de espectadores + interactores.

### MOFU — Consideración (arranca ~Semana 5)
- **Objetivo:** Tráfico / Interacción (o Visitas a la Página de Destino).
- **Audiencias (retargeting):** 25–95% de espectadores de vídeo (últimos 30–90d), interactores IG/FB (365d).
- **Creatividades:** demos (AD-V-03 setup), comparativa/prueba (AD-V-05), build-in-public del
  founder (AD-V-07). Carruseles (cuenta de comisiones, "por qué se cambiaron") como anuncios estáticos/carrusel.
- **Destino:** web / demo / "cómo funciona" → CTA suave "Mira cómo funciona".
- **Meta:** generar clics considerados; sembrar el pool de visitantes web para BOFU.

### BOFU — Conversión (arranca ~Semana 9, una vez los pools estén calientes)
- **Objetivo:** Conversiones (Lead o Ventas / evento de registro). Optimiza por **registro en dashboard**.
- **Audiencias:** visitantes web (30d), **registro iniciado pero no completado en dashboard**
  (la más caliente), eventos tipo carrito/checkout, más **lookalikes 1–3%** de los registros y visitantes de alto valor.
- **Creatividades:** testimonio/prueba (AD-V-05), confianza del founder + CTA directo (AD-V-06),
  rompe-objeciones ("¿es seguro? / tus claves") + un "Empieza en minutos" claro.
- **Destino:** dashboard.zenobank.io (registro sin fricción).
- **Meta:** maximizar registros cualificados al CPA objetivo.

## Seguimiento y medición
- **Meta Pixel + Conversions API (CAPI)** en la web y el dashboard. El CAPI del lado del
  servidor es importante en cripto/fintech, donde la señal del navegador es deficiente.
- **Eventos estándar:** PageView, ViewContent (cómo funciona), Lead/CompleteRegistration
  (registro iniciado), y un evento personalizado **`StoreConnected`** = activación cualificada.
- **Convención UTM:** `utm_source=meta&utm_medium=paid&utm_campaign=[etapa]&utm_content=[ID-AD]`
  — debe coincidir con los IDs de `08` y los IDs de activo de `04` para una atribución limpia.
- Usa el mismo `utm_content` que el ID de la creatividad para atar gasto → creatividad → registro.

## Marco de presupuesto (escala, no adivines)
- **Validación (Semanas 2–4):** presupuesto TOFU pequeño en 3–4 creatividades; mata las de
  baja tasa de ThruPlay, escala las ganadoras. Busca 2–3 creatividades con buena retención + ThruPlay barato.
- **Reparto por fase una vez el embudo está vivo (Semanas 5+):** ~60% TOFU / 25% MOFU / 15% BOFU,
  desplazándose hacia BOFU según se llenen los pools calientes. Ajusta al CPA, no a métricas de vanidad.
- **Regla de escalado:** sube el presupuesto ~20% cada 3–4 días en una ganadora (evita
  resetear el aprendizaje); duplica las ganadoras en audiencias nuevas en vez de sobre-editar un anuncio que rinde.
- Fija un **CPA objetivo = el máximo que pagarás por registro cualificado**; déjalo gobernar el escalado.

## Ángulos creativos (mapean a los copys de `08`)
1. Choque de comisiones "0,1% vs 2,9%" (AD-V-01) — el ganador TOFU más amplio.
2. Chargebacks/fondos congelados (AD-V-02) — dolor segmento A/B.
3. Demo de setup de 5 minutos (AD-V-03) — el "cómo" de MOFU.
4. Transfronterizo / cualquier país (AD-V-04) — segmento C + global.
5. Prueba / testimonio (AD-V-05) — confianza MOFU/BOFU.
6. **Confianza del founder: "Soy Hugo, construí Zeno"** (AD-V-06) — el diferencial que la
   mayoría de competidores cripto literalmente no pueden correr (sin cara). Pruébalo en todas las etapas; suele cerrar en BOFU.
7. Build-in-public / transparencia (AD-V-07) — credibilidad para audiencia caliente.

## Matriz de tests A/B (prueba UNA variable a la vez)
| Test | Variable | Mantén la ganadora, varía la siguiente |
|---|---|---|
| 1 | Hook (primer 1,5s) | número de comisión vs fondos congelados vs cara del founder |
| 2 | Formato de creatividad | talking-head vs screen-demo vs texto-sobre-movimiento |
| 3 | Longitud del texto principal | golpe corto vs historia |
| 4 | CTA | "Empieza gratis" vs "Mira cómo funciona" vs "Calcula tu ahorro" |
| 5 | Audiencia | interés amplio vs lookalike vs retargeting |
| 6 | Ángulo | liderado por dolor vs por confianza vs por ahorro |

## Anti-patrones
- No lances BOFU antes de que existan pools calientes (gasto desperdiciado).
- No edites un anuncio ganador a mitad de vuelo (resetea el aprendizaje) — duplícalo en su lugar.
- No corras una sola creatividad — la fatiga es rápida en Reels; mantén 3–5 activas por etapa.
- No violes la política cripto/financiera ni los guardrails (sin garantías, sin esquivar impuestos, sin urgencia falsa).
