# 07 — Meta Ads Plan (Instagram + Facebook)

> The paid acquisition layer. Strategy: let **organic find the winning hooks cheaply**,
> then put spend behind proven creatives in a structured TOFU→MOFU→BOFU funnel that
> drives **qualified dashboard signups**. Copy/creatives live in `08-meta-ads-copy.md`.

## ⚠️ Policy first (read before spending a dollar)
Meta restricts **cryptocurrency products & services** advertising. Likely requirements:
- The advertiser/business may need **written permission / be on Meta's approved crypto
  advertiser list**, and provide any required licenses/registrations for targeted regions.
- Ads must avoid prohibited claims (no guaranteed returns, no "get rich," no
  tax-avoidance framing — aligns with our guardrails anyway).
- Position Zeno as a **payment gateway / software for merchants** (B2B SaaS framing),
  not as investing or "make money with crypto."
- **Action:** confirm approval status in Business Manager and submit any required docs
  **before** launch. If approval is pending, run engagement/traffic objectives that are
  lower-risk while waiting, and keep landing pages clean and compliant.

## Account structure
- 1 Business Manager → 1 Ad Account → 3 campaigns by funnel stage (below).
- Naming convention: `ZB | [STAGE] | [Objective] | [Audience] | [Creative-ID]`
  e.g. `ZB | TOFU | VideoViews | BroadCrypto | AD-V-01`.
- Consolidate budgets (Advantage+ CBO) at campaign level for learning efficiency.

## The funnel

### TOFU — Awareness (start Week 2)
- **Objective:** Video views / Reach (and ThruPlay). Cheap attention + builds retargeting pools.
- **Audiences:** Broad + interest stacks from `00b` (Shopify, WooCommerce, e-commerce,
  dropshipping, Binance, crypto, stablecoin, Stripe, SaaS). Let Advantage+ broaden.
- **Creatives:** proven organic hooks — AD-V-01 (fee-shock), AD-V-02 (chargebacks),
  AD-V-04 (cross-border), AD-V-06 (founder trust). 9:16, subtitled, 15–30s.
- **Placements:** Reels + Stories + Feed (Advantage+ placements).
- **Goal:** cheap ThruPlays, grow video-viewer + engager custom audiences.

### MOFU — Consideration (start ~Week 5)
- **Objective:** Traffic / Engagement (or Landing Page Views).
- **Audiences (retargeting):** 25–95% video viewers (last 30–90d), IG/FB engagers (365d).
- **Creatives:** demos (AD-V-03 setup), comparison/proof (AD-V-05), founder build-in-public
  (AD-V-07). Carousels (fee math, "why merchants switched") as static/carousel ads.
- **Destination:** site / demo / "how it works" → soft CTA "See how it works."
- **Goal:** drive considered clicks; seed site-visitor pool for BOFU.

### BOFU — Conversion (start ~Week 9, once pools are warm)
- **Objective:** Conversions (Lead or Sales / signup event). Optimize for **dashboard signup**.
- **Audiences:** site visitors (30d), **dashboard signup-started but not completed** (hottest),
  cart/checkout-style events, plus **1–3% lookalikes** off signups & high-value visitors.
- **Creatives:** testimonial/proof (AD-V-05), founder trust + direct CTA (AD-V-06),
  objection-buster ("is it safe / your keys") + a clear "Start in minutes."
- **Destination:** dashboard.zenobank.io (frictionless signup).
- **Goal:** maximize qualified signups at target CPA.

## Tracking & measurement
- **Meta Pixel + Conversions API (CAPI)** on the site and dashboard. Server-side CAPI is
  important for crypto/fintech where browser signal is lossy.
- **Standard events:** PageView, ViewContent (how-it-works), Lead/CompleteRegistration
  (signup started), and a custom **`StoreConnected`** event = qualified activation.
- **UTM convention:** `utm_source=meta&utm_medium=paid&utm_campaign=[stage]&utm_content=[AD-ID]`
  — must match the IDs in `08` and the asset IDs in `04` so attribution is clean.
- Use the same UTM `utm_content` as the creative ID to tie spend → creative → signup.

## Budget framework (scale, don't guess)
- **Validation (Weeks 2–4):** small TOFU budget across 3–4 creatives; kill <X ThruPlay rate,
  scale the winners. Aim to find 2–3 creatives with strong hold rate + cheap ThruPlay.
- **Phase split once funnel is live (Weeks 5+):** ~60% TOFU / 25% MOFU / 15% BOFU,
  shifting toward BOFU as warm pools fill. Adjust to CPA, not vanity metrics.
- **Scaling rule:** raise budget ~20% every 3–4 days on a winner (avoid resetting learning);
  duplicate winners into new audiences rather than over-editing a performing ad.
- Set a target **CPA = max you'll pay per qualified signup**; let it govern scaling.

## Creative angles (map to `08` copy)
1. Fee-shock "0.1% vs 2.9%" (AD-V-01) — broadest TOFU winner.
2. Chargebacks/frozen funds (AD-V-02) — segment A/B pain.
3. 5-minute setup demo (AD-V-03) — MOFU "how."
4. Cross-border / any country (AD-V-04) — segment C + global.
5. Proof / testimonial (AD-V-05) — MOFU/BOFU trust.
6. **Founder trust: "I'm Hugo, I built Zeno"** (AD-V-06) — the differentiator most
   crypto competitors literally can't run (no face). Test in all stages; often the BOFU closer.
7. Build-in-public / transparency (AD-V-07) — warm-audience credibility.

## A/B test matrix (test ONE variable at a time)
| Test | Variable | Hold winner, vary next |
|---|---|---|
| 1 | Hook (first 1.5s) | fee number vs frozen-funds vs founder face |
| 2 | Creative format | talking-head vs screen-demo vs text-on-motion |
| 3 | Primary text length | short punch vs story |
| 4 | CTA | "Start free" vs "See how it works" vs "Calculate savings" |
| 5 | Audience | broad interest vs lookalike vs retargeting |
| 6 | Angle | pain-led vs trust-led vs savings-led |

## Anti-patterns
- Don't launch BOFU before warm pools exist (wasted spend).
- Don't edit a winning ad mid-flight (resets learning) — duplicate instead.
- Don't run a single creative — fatigue is fast on Reels; keep 3–5 live per stage.
- Don't violate crypto/financial policy or the guardrails (no guarantees, no tax-dodging, no fake urgency).
