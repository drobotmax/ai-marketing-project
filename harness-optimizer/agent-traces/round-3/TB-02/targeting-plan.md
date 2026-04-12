# Targeting Plan: Serenity Villas, Ubud, Bali

## 1. Objective & Conversion Setup

- **Business goal:** Generate 70+ qualified leads/month for premium villas in Ubud ($180K-$350K) [Strategy]
- **Meta objective:** Leads [KB: generatsiya-lidov.md - цель "Лиды" для сбора информации о лидах]
- **Conversion location:** Instant Form (primary) + WhatsApp (secondary for warm/hot) [KB: generatsiya-lidov.md - моментальная форма + переписка в WhatsApp]
- **Primary optimization event:** Lead submission (instant form) [KB: targeting-course-knowledge.md]
- **Tracking status:** Partial - need to verify Pixel on serenity-bali.com + CAPI setup [Assumption]
- **Key measurement gaps:**
  - CRM integration status unknown [Assumption]
  - Offline conversion upload not confirmed [Assumption]
  - No historical data for LAL audiences [Assumption]

## 2. ICP & Segments

### Segment 1: Russian-speaking Investors
- **Who:** RU-speaking, 30-55, capital $200K+, considering Bali real estate [Strategy]
- **Trigger:** Market correction in Canggu (-20% price drops), search for stable returns [KB: market-overview.md - Alex Villas Complex 7 dropped 20%]
- **Pain:** Fear of scam (Domogatsky scandal, SWOI frozen project), inflated ROI claims [KB: market-insights-mityuhin.md]
- **Offer angle:** "Guaranteed 8% ROI + full management = predictable passive income" [Strategy]
- **Funnel temperature:** Cold -> Warm via content

### Segment 2: Digital Nomads / Remote Workers
- **Who:** EN/RU-speaking, 25-40, remote income $3K-$10K/month [Strategy]
- **Trigger:** Tired of renting, want a home base, Canggu overcrowded [KB: locations.md]
- **Pain:** Instability, rising rent prices, noise and traffic in popular areas [KB: locations.md - Canggu 90% built]
- **Offer angle:** "Your own villa in Ubud - peace, nature, investment that pays for itself" [Strategy]
- **Funnel temperature:** Cold

### Segment 3: Families Relocating
- **Who:** Families with children, considering Bali move, budget $250K+ [Strategy]
- **Trigger:** Kids growing up, want nature + safety + international schooling [Strategy]
- **Pain:** Construction quality, safety, school access [Strategy]
- **Offer angle:** "280 m2 among rice terraces, 15 min to school, full management" [Strategy]
- **Funnel temperature:** Cold

## 3. Audience Matrix

| Audience | Type | Source | Funnel stage | Hypothesis | Priority |
|----------|------|--------|--------------|------------|----------|
| Broad International - Bali Interest | Cold | Geo: worldwide, RU + EN, interest: Bali, real estate investment | Cold | Algo finds fit-profile with strong offer [KB: targeting-course - broad targeting при сильном оффере] | High |
| RU-speaking Investors | Cold | Language: RU, interests: real estate investment, passive income, Bali | Cold | Highest intent segment [Strategy] | High |
| IG Engagers 30d | Warm | Instagram account engagers | Warm | Cheaper to convert to lead [KB: targeting-course - IG engagers тёплые] | High |
| Website Visitors 30d | Warm | Pixel - serenity-bali.com visitors | Warm | Already showed intent | Medium |
| Lead Form Openers Non-Submit | Warm | Meta - lead form openers who didn't submit | Warm | Remove friction, re-engage | Medium |
| CRM LAL 1-3% | Cold | CRM upload when available (after 100+ leads) | Cold | Closer to SQL pattern [Assumption] | Low (Phase 2) |

**Housing category note:** Meta Special Ad Categories apply - no targeting by age, gender, zip code [Platform docs: Meta Special Ad Categories]. Compensate with strong offer-driven creatives [KB: targeting-course].

## 4. Campaign Logic

### Campaign 1: Cold Acquisition
- **Goal:** Generate leads from cold audiences at CPL < $40 [Strategy]
- **Ad sets:** 3
  - AS1: Broad Bali Interest (worldwide, EN + RU)
  - AS2: RU-speaking Investors (RU language, real estate interests)
  - AS3: Digital Nomad cluster (remote work, Bali, property)
- **Placements:** Advantage+ placements [KB: targeting-course - Advantage+ для wider reach с housing ads ограничениями]
- **Budget split:** 70% of $2,750 = $1,925/month ($64/day), split evenly across 3 ad sets initially
- **Creative requirement:** 3+ variants per ad set, different hooks per segment (see creatives.md)

### Campaign 2: Retargeting
- **Audience windows:** IG engagers 30d, website visitors 14d, lead form openers non-submit 7d [KB: targeting-course]
- **Message shift:** Social proof (testimonials, ROI data), urgency (limited units), deeper info (floor plans, virtual tour) [KB: cialdini-influence.md - Social Proof + Scarcity]
- **Budget split:** 20% of $2,750 = $550/month ($18/day)
- **Note:** Start retargeting from day 1 even with small budget [KB: targeting-course - ретаргетинг с первого дня]

### Campaign 3: WhatsApp Leads (Phase 2)
- **Goal:** Higher quality leads via direct conversation
- **Budget split:** 10% of $2,750 = $275/month ($9/day)
- **When:** After 2 weeks, once cold campaigns stabilize

## 5. Experiment Plan

| Test | Variable | Hypothesis | Success metric | Minimum run condition | Next action |
|------|----------|------------|----------------|-----------------------|-------------|
| T1 | Audience: Broad vs Interest clusters | Broad with strong offer outperforms narrow interests for housing ads | CPL + lead quality (response rate) | 7 days, $300 spend per ad set | Scale winner, pause loser |
| T2 | Offer angle: ROI-focused vs Lifestyle-focused | ROI hook converts investors better, lifestyle converts nomads | Form completion rate | 7 days, $200 spend per variant | Apply winning angle per segment |
| T3 | Form friction: Short (3 fields) vs Long (5 fields) | Short form = more leads, long form = higher quality | Cost per qualified lead | 10 days, 50+ leads per variant | Balance volume vs quality |

## 6. Optimization Rules

- **If CPM high (>$15):** Check creative fatigue, refresh creatives, broaden audience [KB: targeting-course]
- **If CTR low (<0.5%):** Weak hook or wrong audience-creative match, test new angles [KB: targeting-course]
- **If CPL ok but quality weak:** Increase form friction, add qualifying questions, test WhatsApp objective [KB: targeting-course - signal quality > cheap leads]
- **If lead-to-contact weak (<30% reachable):** Check form UX, add phone validation, verify contact timing [Assumption]
- **If frequency >3:** Rotate creatives, exclude converted leads [KB: targeting-course]

## 7. Risks & Dependencies

- **Tracking risk:** Pixel and CAPI setup on serenity-bali.com must be verified before launch [Assumption]
- **Sales process risk:** Speed-to-lead critical for international real estate; SLA < 2 hours recommended [Assumption]
- **Creative dependency:** Need 9+ creative variants for 3 segments x 3 angles [Strategy]
- **Policy limitation:** Housing category restricts targeting - compensate with offer strength [Platform docs: Meta]
- **No historical data:** LAL audiences unavailable at launch; broad + interest targeting only [Assumption]

## 8. Organic Support Layer

- **Need:** Yes - trust building critical for $180K-$350K purchase decisions [Strategy]
- **Primary owned channel:** Instagram (international audience) [Assumption]
- **Role in funnel:** Trust / social proof / FAQ / warm-up for retargeting [KB: targeting-course]
- **Required rubrics:**
  - Construction progress updates
  - Ubud lifestyle content (rice terraces, cafes, yoga, community)
  - Investor testimonials / case studies
  - Q&A about leasehold, management, ROI
  - "Day in the life at Serenity Villas" content
- **Paid sync:** Boost top organic posts for retargeting, use IG engagers as warm audience
- **Community ops note:** Response SLA < 1 hour during business hours, FAQ highlights in bio

## 9. 14-Day Action Plan

| Day range | Action | Owner | Expected signal |
|-----------|--------|-------|-----------------|
| 1-2 | Verify Pixel + CAPI on serenity-bali.com, setup instant form | Targeting + Dev | Clean tracking |
| 3-4 | Launch Campaign 1 (3 cold ad sets) + Campaign 2 (retargeting) | Targeting | First impressions |
| 5-7 | Early signal read: CTR, CPM, form open rate | Targeting | CPL direction |
| 8-10 | First pruning: pause worst ad set, reallocate budget | Targeting | Remove losers |
| 11-14 | Stabilize winner, launch T2 (offer angle test) | Targeting | CPL < $40 trend |

## 10. Budget Compliance

- **Channel hard cap:** $2,750/month [Strategy]
- **Planned spend:** $2,750/month ($1,925 cold + $550 retargeting + $275 WhatsApp)
- **Delta vs cap:** $0
- **Status:** PASS
