# 09 — Métricas y Cadencia Operativa

> Qué medimos, los objetivos a fijar, y el ritual semanal que convierte los datos en el
> contenido de la semana siguiente. Mantenlo simple: unos pocos indicadores líderes por
> canal y una métrica estrella.

## Métrica estrella (north-star)
**Registros cualificados en el dashboard** = un comercio crea una cuenta Y conecta una
tienda / checkout (dispara el evento `StoreConnected`). Esta es la activación que predice
ingresos, no los registros en bruto. Todo lo que está aguas arriba es un medio para esto.

Métricas de negocio secundarias: CAC (mezclado + solo-pago), payback, tasa registro→activación,
tasa activación→primer-pago.

## Métricas del embudo (la cadena)
Impresiones/Visualizaciones → Visionado completo → Visitas al perfil → Clics en enlace →
Registro iniciado → **Tienda conectada (north-star)** → Primer pago procesado.
Mide la tasa de conversión **entre cada paso** mensualmente para encontrar la fuga.

## Indicadores líderes por canal

### TikTok
- **Tasa de finalización** (señal líder de calidad) y **tiempo medio de visionado**.
- **Compartidos** y **comentarios** (distribución + resonancia).
- Crecimiento de seguidores, visitas al perfil, clics en link-in-bio.
- Vigila qué **hooks** superan tu listón de tasa de finalización — esos pasan a anuncios.

### Instagram
- **Guardados + compartidos** (el north-star de calidad de IG — esp. carruseles).
- Reproducciones de Reels, alcance, tiempo medio de visionado.
- Visitas al perfil → clics en enlace; conversaciones de DM iniciadas.
- Toques en sticker de enlace de Story; tasa de respuesta de encuestas/quizzes.

### YouTube
- Shorts: visualizaciones, visto-vs-deslizado, suscriptores ganados.
- Formato largo: **duración media de visionado / %**, CTR de la miniatura, tráfico de búsqueda,
  y clics al dashboard desde la descripción/tarjetas.

### Meta Ads (ver `07`)
- TOFU: tasa de ThruPlay, **hook rate** (3s/visualizaciones), CPM, coste por ThruPlay, tasa de retención.
- MOFU: CTR de salida, coste por visita a página de destino, frecuencia (fatiga de visionado).
- BOFU: **coste por registro cualificado (CPA)**, ROAS cuando los ingresos sean atribuibles, frecuencia.
- A nivel de creatividad: ata cada resultado a un **ID-AD** vía `utm_content`.

## Objetivos (fija números reales en la semana 1, luego supéralos)
No inventes objetivos de vanidad — **establece una línea base en las semanas 1–2, luego fija
metas de mejora.** Enfoque sugerido para fijar objetivos:
- Semana 2: registra tus medianas (tasa de finalización, tasa de guardado, CTR, CPA).
- Semanas 3+: apunta a **superar tu propia mediana**; promociona cualquier activo >1,5× la mediana a "escalar/anuncios".
- Define un **CPA máximo** que pagarás por registro cualificado según el LTV del comercio; deja que gobierne el escalado de ads.

## Higiene de seguimiento
- **UTMs en cada enlace:** `utm_source/medium/campaign/content` — `utm_content` = ID de activo/AD
  para que orgánico y pago se atribuyan ambos a una creatividad concreta.
- **Pixel + CAPI** vivos antes del gasto pagado; verifica que `StoreConnected` dispara.
- Mantén una **hoja de tracking** simple: una fila por activo (ID, canal, fecha, hook, pilar,
  visualizaciones, % visionado, guardados/compartidos, clics, registros). Esta es la memoria de lo que funciona.

## Cadencia semanal (el ritual)
- **Lunes:** publica build-in-public; confirma que los huecos del calendario de la semana están llenos (`04`).
- **Mar–Jue:** publica según el calendario; responde a todos los comentarios en la primera hora (voz del founder donde se pueda).
- **Viernes — Revisión (30–45 min):**
  1. Saca el tracking. Identifica los 3 mejores + 3 peores activos por indicador líder.
  2. **Dobla la apuesta:** haz 1–2 variaciones de cada hook top para la semana siguiente.
  3. **Retira:** deja de re-publicar los flops; anota por qué fallaron.
  4. **Gradúa ganadores a anuncios** (o sube el presupuesto de los ads ganadores +20%).
  5. Actualiza el número north-star; publícalo como build-in-public (transparencia = contenido).
- **Mensual:** revisión completa de conversión del embudo; refresca el set always-on perenne;
  rota creatividades de ads fatigadas; planifica el formato largo del mes siguiente (YT).

## Reglas de decisión (para que actúes, no agonices)
- Un hook orgánico **>1,5× la mediana de finalización/guardado** → haz variantes + prueba como anuncio.
- Una creatividad de anuncio **por debajo del CPA objetivo tras suficiente gasto/aprendizaje** → córtala; reasigna a las ganadoras.
- Un anuncio ganador → **duplícalo para escalar** (no edites el original).
- Frecuencia subiendo + CTR bajando → **fatiga de creatividad**; rota un hook fresco.
- Cualquier activo que falle en la checklist de cumplimiento → **retíralo de inmediato**, corrige, documenta.

## Cómo se ve "bien" por fase
- **Semanas 1–4:** publicación consistente, ≥3–5 hooks superando la base, primeros registros, pools de ads construyéndose.
- **Semanas 5–8:** escalando ganadores, velocidad creciente de guardados/compartidos + seguidores, retargeting MOFU convirtiendo más barato que el frío.
- **Semanas 9–12:** coste predecible por registro cualificado, lookalikes rindiendo, un set perenne
  de ~10 hooks orgánicos + 3 ads cargando el peso, marca del founder impulsando la confianza de forma reconocible.
