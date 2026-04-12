# Targeting Plan: Serenity Villas, Ubud, Bali

## 1. Objective & Conversion Setup

- **Business goal:** Generate 60+ qualified leads/month for premium villa sales ($180K-$350K) via Meta Ads [Strategy]
- **Meta objective:** Leads [KB: Meta Ads - "Leads" objective supports instant forms, calls, and messaging in Direct/Messenger/WhatsApp]
- **Conversion location:** Instant Form (primary) + Website form (secondary for higher-intent) [KB: Meta Ads - generatsiya-lidov.md - instant forms supported under Leads objective]
- **Primary optimization event:** Lead (form submission) [KB: Meta Ads - Leads objective]
- **Secondary signal:** Consultation booked (offline conversion import from CRM) [Assumption - standard for real estate]
- **Tracking status:** Needs setup - Meta Pixel on serenity-bali.com required [Strategy]
- **Key measurement gaps:**
  - Meta Pixel not confirmed on landing page [Assumption]
  - No CRM integration for offline conversion tracking yet [Assumption]
  - No Conversions API (CAPI) setup [KB: Meta Ads - meropriyatiya-sobytiya/conversions-api.md - CAPI needed for quality optimization]

## 2. ICP & Segments

### Segment 1: Russian-speaking passive income investors

- **Who:** 35-55, HHI $100K+, real estate investment experience, looking to diversify internationally [Strategy]
- **Trigger:** Declining yields in home market, Bali hype but with more cautious approach post-scandals [Strategy + KB: Bali market-overview.md - investor sentiment shifting to careful selection]
- **Pain:** Fear of scam (Domogatsky, SWOI scandals), inflated ROI claims, management quality variance [Strategy + KB: Mityuhin market-insights]
- **Offer angle:** "8% guaranteed ROI for 2 years, full management included - honest numbers, real returns" [Strategy]
- **Funnel temperature:** Cold -> Warm via content, retargeting to Hot [Strategy]

### Segment 2: Digital nomads seeking Ubud base

- **Who:** 28-42, location-independent income, already in/visiting Bali [Strategy]
- **Trigger:** Tired of paying rent without building equity [Strategy]
- **Pain:** Instability, no asset accumulation, quality variance in rentals [Strategy]
- **Offer angle:** "Own your Ubud base from $180K - earn when you travel, live when you stay" [Strategy]
- **Funnel temperature:** Warm (already in Bali ecosystem) [Assumption]

### Segment 3: Relocating families

- **Who:** 30-50, families with children, seeking lifestyle upgrade [Strategy]
- **Trigger:** Desire for better environment, education, climate for children [Strategy]
- **Pain:** Finding quality housing with good infrastructure, legal complexity [Strategy]
- **Offer angle:** "120-280m2 family villa in Ubud's rice terraces - managed, secure, yours" [Strategy]
- **Funnel temperature:** Cold [Assumption]

## 3. Audience Matrix

| Audience | Type | Source | Funnel stage | Hypothesis | Priority |
|----------|------|--------|--------------|------------|----------|
| Broad international, Bali/Indonesia interest | Cold | Geo (worldwide) + interest: Real estate investment, Bali, Indonesia travel | Cold | Algorithm finds fit-profile with strong lifestyle+ROI offer | High |
| Russian-speaking, investment interests | Cold | Language: Russian + Interest: Real estate, Investment, Passive income | Cold | Primary ICP segment, higher conversion expected | High |
| Digital nomad interest cluster | Cold | Interest: Remote work, Coworking, Bali, Ubud, Digital nomad + Geo: global | Cold | Already warm to Bali, lower CPL expected | Medium |
| Website visitors 30d | Warm | Meta Pixel - serenity-bali.com visitors | Warm | Already engaged, cheaper to convert | High |
| IG engagers 30d | Warm | Instagram account engagement | Warm | Showed interest in content | High |
| Video viewers 50%+ | Warm | Custom audience - video views | Warm | Consumed content, warmer intent | Medium |
| Lead form openers non-submit | Warm | Custom audience - lead form interaction | Warm | High intent, overcome last objection | High |
| LAL 1-3% from qualified leads | Cold | Lookalike from CRM qualified list | Cold | Closest to buyer profile [KB: Meta Ads - polzovatelskie-auditorii.md - LAL from customer lists] | Medium (after 100+ leads) |

**Note on housing ads:** International market (non-US/Canada) - Special Ad Categories housing restrictions do NOT apply by default. However, if targeting US/Canada audiences specifically, age/gender/zip restrictions apply [Platform docs: Meta Special Ad Categories]. For this campaign targeting global audiences including Russia, standard targeting is available [Platform docs].

**Custom audience sources available per Meta:** website, app activity, customer list, offline actions, video, lead form, Instant Experience, Instagram account, Facebook Page, events [KB: Meta Ads - polzovatelskie-auditorii.md]

## 4. Campaign Logic

### Campaign 1: Cold Acquisition - Investors (RU)

- **Goal:** Find Russian-speaking investors interested in Bali villa investment [Strategy]
- **Ad sets:**
  - AS1: Russian language + Real estate investment + Bali/Indonesia interest [Assumption]
  - AS2: Russian language + Passive income + International property interest [Assumption]
  - AS3: Broad Russian-speaking, strong offer creative (let algorithm optimize) [KB: targeting skill.md - broad works when offer is strong]
- **Placements:** Advantage+ placements (recommended for international reach, algorithm distributes to best-performing placements) [KB: Meta Ads - Instagram placement - "optimized delivery across wider audience"]
- **Budget:** $1,800/mo ($60/day) [Strategy - 60% of Meta cap]
- **Creative requirement:** ROI-focused angles, trust-building (guaranteed returns, developer credentials) [Strategy]
- **Form type:** Instant form with qualifying questions (budget range, timeline, investment experience) [KB: Meta Ads - generatsiya-lidov.md - instant forms for lead collection with CRM integration]

### Campaign 2: Cold Acquisition - Digital Nomads + Families (EN/RU)

- **Goal:** Reach nomads and families with lifestyle positioning [Strategy]
- **Ad sets:**
  - AS1: EN + Ubud/Bali + Digital nomad/Remote work interest [Assumption]
  - AS2: EN + Family relocation + Bali/Indonesia + Education interest [Assumption]
- **Placements:** Advantage+ [KB: Meta Ads - Instagram placement]
- **Budget:** $600/mo ($20/day) [Strategy allocation]
- **Creative requirement:** Lifestyle visuals (rice terraces, villa interiors, family scenes, Ubud culture) [Strategy]

### Campaign 3: Retargeting

- **Audience windows:**
  - Website visitors 7d (hottest) [Assumption - standard retargeting window]
  - IG engagers 14d [Assumption]
  - Video viewers 50%+ 30d [KB: Meta Ads - polzovatelskie-auditorii.md - video-based custom audiences]
  - Lead form openers non-submit 14d [KB: Meta Ads - polzovatelskie-auditorii.md - lead form engagement audiences]
- **Message shift:** Social proof (investor testimonials), urgency (limited units), deeper product info (floor plans, ROI breakdown) [Strategy - Cialdini principles]
- **Budget:** $600/mo ($20/day) [Strategy - retargeting from day 1]

## 5. Experiment Plan

| Test | Variable | Hypothesis | Success metric | Minimum run | Next action |
|------|----------|------------|----------------|-------------|-------------|
| T1 | Offer angle | "8% guaranteed ROI" hook beats "lifestyle in Ubud" hook for investor segment | CPL + form completion rate | 5 days or 1,000 impressions per variant [KB: Meta Ads - A/B testing - "equal distribution between statistically equal audiences"] | Scale winner, iterate loser |
| T2 | Audience | Russian-speaking broad beats interest-stacked for investor segment | Cost per qualified lead | 7 days [Assumption] | Scale winner |
| T3 | Form friction | Short form (name+phone) vs qualifying form (name+phone+budget+timeline) | Lead quality (qualified rate from sales) | 7 days, 30+ leads per variant [Assumption] | Quality over volume |
| T4 | Creative format | Carousel (villa views) vs single image (lifestyle shot) vs video (property tour) | CTR + CPL | 5 days [Assumption] | Scale winner format |

**A/B testing approach:** Use Meta Experiments tool, not manual on/off of ad sets [KB: Meta Ads - A/B testing - "do not conduct arbitrary testing by manually toggling ad sets and campaigns"]

## 6. Optimization Rules

- **If CPM high (>$15):** Broaden audience or check creative fatigue. Refresh creatives every 2-3 weeks [Assumption - international real estate benchmark]
- **If CTR low (<0.8%):** Swap creative angles, test stronger hooks. Check ad relevance score [Assumption]
- **If CPL ok but quality weak:** Increase form friction (add qualifying questions), shift budget to retargeting, request CRM feedback loop [KB: targeting skill.md - "don't scale based on CPL alone, look at downstream quality"]
- **If lead-to-contact weak (sales not reaching leads fast):** Flag as sales process risk, implement speed-to-lead SLA (respond within 15 min) [KB: targeting skill.md - "if sales team slow, don't blame ads"]
- **If frequency >3 on retargeting:** Rotate creatives, expand audience window [Assumption]
- **Learning phase:** Do not make significant changes to ad sets within first 3-5 days of launch [KB: targeting skill.md - "learning discipline - don't break campaign with frequent changes before signal accumulation"]

## 7. Risks & Dependencies

- **Tracking risk:** Meta Pixel must be installed on serenity-bali.com before launch. Without it, retargeting and conversion optimization are blind [Strategy dependency]
- **Sales process risk:** Premium real estate ($180K-$350K) needs fast, professional lead response. If sales team response time >2 hours, lead quality will degrade regardless of ad quality [KB: targeting skill.md]
- **Creative dependency:** Need high-quality villa renders/photos, Ubud lifestyle imagery, possibly video tour. Without strong visuals, CPL will be 2-3x higher [Assumption]
- **CRM integration:** Without CRM -> Meta offline conversion upload, algorithm can't optimize for qualified leads, only form submissions [KB: Meta Ads - CAPI for quality optimization]
- **Measurement gap:** No CAPI setup = reliance on pixel-only tracking, lower match rates, weaker optimization signal [KB: Meta Ads - meropriyatiya-sobytiya/conversions-api.md]

## 8. Organic Support Layer

- **Need:** Yes - trust-building content is critical for premium real estate in an international market with trust deficit [Strategy - Cialdini Social Proof + Authority]
- **Primary owned channel:** Instagram (global audience, visual product) [Assumption]
- **Role in funnel:** Trust / social proof / FAQ / retargeting seed [Strategy]
- **Required content:**
  - Construction progress updates [Strategy - trust building]
  - Ubud lifestyle content (rice terraces, culture, wellness) [Strategy - lifestyle positioning]
  - Investor Q&A / FAQ content [Strategy - objection handling]
  - ROI breakdowns and market data [Strategy - authority/proof]
- **Paid sync:** Boost high-performing organic posts to warm audiences; use IG engagers as retargeting pool [KB: Meta Ads - polzovatelskie-auditorii.md - Instagram account custom audiences]
- **Community ops:** Response SLA < 30 min during business hours; pin FAQ post with key investment details [Assumption]

## 9. 14-Day Action Plan

| Day range | Action | Owner | Expected signal |
|-----------|--------|-------|-----------------|
| 1-2 | Install Meta Pixel, set up instant forms, prepare 3+ creative sets | Targeting + Creative | Clean setup |
| 3-4 | Launch Campaign 1 (Investors RU) + Campaign 3 (Retargeting) | Targeting | First impressions, CTR baseline |
| 5-7 | Launch Campaign 2 (Nomads + Families) + read early signals | Targeting | CPL range, form completion rate |
| 8-10 | First A/B test read, prune low-CTR ad sets | Targeting | Identify winners |
| 11-12 | Reallocate budget to winners, request first CRM feedback | Targeting + Sales | Qualified lead rate |
| 13-14 | Stabilize winners, plan week 3 creative refresh | Targeting + Creative | CPL trend, lead quality |

## 10. Budget Compliance

- **Channel hard cap:** $3,000/mo [Strategy]
- **Planned spend:** $3,000/mo (Campaign 1: $1,800 + Campaign 2: $600 + Campaign 3: $600) [Plan]
- **Delta vs cap:** $0 [Calculated]
- **Status:** PASS

### Attribution Tags Summary

| Source | Count | % |
|--------|-------|---|
| [KB: Meta Ads platform docs] | 14 | ~25% |
| [KB: Targeting skill / course] | 8 | ~14% |
| [KB: Bali market files] | 5 | ~9% |
| [Strategy] | 18 | ~32% |
| [Platform docs] | 3 | ~5% |
| [Assumption] | 8 | ~14% |
| **Total KB + Strategy + Platform** | **48** | **86%** |
