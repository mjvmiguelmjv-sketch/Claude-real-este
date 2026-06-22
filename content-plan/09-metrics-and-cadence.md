# 09 — Metrics & Operating Cadence

> What we measure, the targets to set, and the weekly ritual that turns data into the
> next week's content. Keep it simple: a few leading indicators per channel and one
> north-star.

## North-star metric
**Qualified dashboard signups** = a merchant creates an account AND connects a store /
checkout (fires the `StoreConnected` event). This is the activation that predicts revenue,
not raw signups. Everything upstream is a means to this.

Secondary business metrics: CAC (blended + paid-only), payback, signup→activation rate,
activation→first-payment rate.

## Funnel metrics (the chain)
Impressions/Views → Watch-through → Profile visits → Link clicks → Signup started →
**Store connected (north-star)** → First payment processed.
Track conversion rate **between each step** monthly to find the leak.

## Per-channel leading indicators

### TikTok
- **Completion rate** (leading quality signal) and **average watch time**.
- **Shares** and **comments** (distribution + resonance).
- Follower growth, profile visits, link-in-bio clicks.
- Watch which **hooks** clear your completion-rate bar — those graduate to ads.

### Instagram
- **Saves + shares** (the IG quality north-star — esp. carousels).
- Reels plays, reach, average watch time.
- Profile visits → link clicks; DM conversations started.
- Story link-sticker taps; poll/quiz response rate.

### YouTube
- Shorts: views, viewed-vs-swiped, subscribers gained.
- Long-form: **average view duration / %**, CTR on thumbnail, traffic from search,
  and clicks to dashboard from description/cards.

### Meta Ads (see `07`)
- TOFU: ThruPlay rate, **hook rate** (3s/views), CPM, cost per ThruPlay, hold rate.
- MOFU: outbound CTR, cost per landing-page view, frequency (watch fatigue).
- BOFU: **cost per qualified signup (CPA)**, ROAS once revenue is attributable, frequency.
- Creative-level: tie every result to an **AD-ID** via `utm_content`.

## Targets (set real numbers in week 1, then beat them)
Don't invent vanity targets — **baseline in weeks 1–2, then set improvement goals.**
Suggested target-setting approach:
- Week 2: record your medians (completion rate, save rate, CTR, CPA).
- Weeks 3+: aim to **beat your own median**; promote any asset >1.5× median to "scale/ads."
- Define a **max CPA** you'll pay per qualified signup based on merchant LTV; let it govern ad scaling.

## Tracking hygiene
- **UTMs on every link:** `utm_source/medium/campaign/content` — `utm_content` = asset/AD-ID
  so organic and paid both trace to a specific creative.
- **Pixel + CAPI** live before paid spend; verify `StoreConnected` fires.
- Maintain a simple **tracker sheet:** one row per asset (ID, channel, date, hook, pillar,
  views, watch%, saves/shares, clicks, signups). This is the memory of what works.

## Weekly cadence (the ritual)
- **Monday:** publish build-in-public; confirm the week's calendar slots are filled (`04`).
- **Tue–Thu:** post per calendar; reply to all comments within the first hour (founder voice where possible).
- **Friday — Review (30–45 min):**
  1. Pull the tracker. Identify top 3 + bottom 3 assets by leading indicator.
  2. **Double down:** make 1–2 variations of each top hook for next week.
  3. **Retire:** stop reposting flops; note why they missed.
  4. **Graduate winners to ads** (or raise budget on existing ad winners +20%).
  5. Update the north-star number; post it as build-in-public (transparency = content).
- **Monthly:** full funnel-conversion review; refresh the evergreen always-on set; rotate
  fatigued ad creatives; plan next month's long-form (YT).

## Decision rules (so you act, not agonize)
- An organic hook **>1.5× median completion/save rate** → make variants + test as an ad.
- An ad creative **below target CPA after enough spend/learning** → cut; reallocate to winners.
- A winning ad → **duplicate to scale** (don't edit the original).
- Frequency climbing + CTR dropping → **creative fatigue**; rotate in a fresh hook.
- Any asset flags on the compliance checklist → **pull immediately**, fix, document.

## What "good" looks like by phase
- **Weeks 1–4:** consistent posting, ≥3–5 hooks beating baseline, first signups, ad pools building.
- **Weeks 5–8:** scaling winners, rising save/share + follower velocity, MOFU retargeting converting cheaper than cold.
- **Weeks 9–12:** predictable cost per qualified signup, lookalikes performing, an evergreen
  set of ~10 organic hooks + 3 ads carrying the load, founder brand recognizably driving trust.
