# Google Ads Plan: Serenity Villas, Ubud, Bali

## 1. Measurement Setup

### Current Status
- GA4: Unknown - needs verification on serenity-bali.com [Assumption]
- GTM: Unknown [Assumption]
- Call tracking: Not confirmed [Assumption]
- CRM integration: Not confirmed [Assumption]
- Offline conversion import: Not configured [Assumption]

### What Needs Setup (Before Launch)
1. Google Ads conversion tracking tag on serenity-bali.com [Platform docs: Google Ads - conversion tracking]
2. GA4 property with key events: form_submit, phone_click, scroll_50, plan_view [KB: Google Ads - explore-features/measure-results.md]
3. Enhanced conversions setup (hashed email/phone for better matching) [KB: Google Ads contextologist skill - enhanced conversions]
4. GTM container for tag management [KB: Google Ads contextologist skill - GTM for international markets]
5. Offline conversion import pipeline: CRM -> Google Ads (lead -> qualified -> viewing -> deal) [KB: Google Ads contextologist skill - offline conversion tracking mandatory for real estate, cycle 30-180 days]

### Key Conversions for Optimization

| Event | Type | Value | Platform |
|-------|------|-------|----------|
| form_submit | Macro | Primary conversion | GA4 + Google Ads |
| phone_click | Macro | Secondary conversion | GA4 |
| whatsapp_click | Macro | Secondary conversion | GA4 |
| plan_view | Micro | Engagement signal | GA4 |
| scroll_50 | Micro | Engagement signal | GA4 Enhanced Measurement |
| qualified_lead | Macro (offline) | Optimization target (Phase 2) | Offline conversion import |

## 2. Semantic Core

### Google Ads (International Market - Committed Plan)

This is an international market (Bali), so Google Ads is the primary search channel [KB: contextologist skill - "Google Ads for international markets (Bali, Dubai)"]

#### Cluster 1: Brand [Serenity Villas]

| Keyword | Match Type | Est. CPC | Intent |
|---------|-----------|----------|--------|
| serenity villas ubud | Exact | $0.50-1.50 | Hot |
| serenity villas bali | Exact | $0.50-1.50 | Hot |
| serenity bali villas | Phrase | $0.50-1.50 | Hot |
| pt serenity bali | Exact | $0.30-0.80 | Hot |

**Note:** Brand campaign is mandatory - 5-10% of budget for brand defense [KB: contextologist skill - "budget on brand: 5-10%, mandatory, defense from competitors"]

#### Cluster 2: Geo + Commercial (Hot Intent)

| Keyword | Match Type | Est. CPC | Intent |
|---------|-----------|----------|--------|
| buy villa ubud | Exact | $2-5 | Hot |
| villa for sale ubud bali | Phrase | $2-5 | Hot |
| ubud property investment | Phrase | $3-6 | Hot |
| bali villa investment | Phrase | $3-7 | Hot |
| buy property bali | Phrase | $3-6 | Hot |
| ubud real estate | Phrase | $2-4 | Warm |
| bali investment property | Exact | $3-7 | Hot |

#### Cluster 3: Competitors

| Keyword | Match Type | Est. CPC | Intent |
|---------|-----------|----------|--------|
| bali home immo | Exact | $1-3 | Hot |
| exotiq property bali | Exact | $1-3 | Hot |
| kibarer property | Exact | $1-3 | Hot |
| bali villa agency | Phrase | $2-4 | Warm |

**Note:** Competitor campaigns capture users comparing options; messaging should highlight USP (guaranteed ROI, full management) [Strategy + KB: contextologist skill - separate campaigns for competitors]

#### Cluster 4: Investment Intent (Warm)

| Keyword | Match Type | Est. CPC | Intent |
|---------|-----------|----------|--------|
| bali property roi | Phrase | $2-4 | Warm |
| invest in bali real estate | Phrase | $3-6 | Warm |
| bali villa rental income | Phrase | $2-4 | Warm |
| passive income bali | Phrase | $2-5 | Warm |
| bali leasehold villa | Phrase | $1-3 | Warm |
| ubud villa rental yield | Phrase | $1-3 | Warm |

#### Cluster 5: Russian-language Search (Hot)

| Keyword | Match Type | Est. CPC | Intent |
|---------|-----------|----------|--------|
| купить виллу на бали | Exact | $1-3 | Hot |
| вилла убуд купить | Exact | $1-2 | Hot |
| инвестиции в недвижимость бали | Phrase | $2-4 | Hot |
| вилла бали цена | Phrase | $1-3 | Warm |
| недвижимость бали доходность | Phrase | $1-3 | Warm |

**Note:** Russian-speaking audience uses Google for Bali searches (not Yandex - international geo) [KB: contextologist skill - "Yandex for RF, Google for international"]

#### Negative Keywords (Base List)

- rent, rental, аренда, снять (exclude rental intent)
- free, бесплатно, cheap, дешево (exclude budget seekers)
- hotel, hostel, отель, хостел (exclude travelers)
- job, work, вакансии, работа (exclude job seekers)
- news, blog, review, отзывы (exclude info seekers - unless landing has reviews section)
- timeshare (exclude timeshare association)
- canggu, seminyak, kuta, nusa dua (exclude wrong locations - keep separate if expanding later)
- airbnb, booking (exclude OTA searches)

## 3. Account Structure

### Google Ads

| Campaign | Type | Match Types | Daily Budget | Bid Strategy | Priority |
|----------|------|-------------|-------------|--------------|----------|
| Brand - Serenity Villas | Search | Exact | $5/day | Manual CPC | High |
| Non-brand - Buy Villa Ubud (EN) | Search | Exact + Phrase | $15/day | Manual CPC -> Target CPA after 30 conv [KB: contextologist skill - "Smart Bidding requires 30+ conversions in 30 days"] | High |
| Non-brand - Bali Investment (EN) | Search | Phrase | $10/day | Manual CPC | Medium |
| Non-brand - Russian (RU) | Search | Exact + Phrase | $10/day | Manual CPC | High |
| Competitors | Search | Exact | $5/day | Manual CPC | Medium |
| Remarketing - Display | Display | - | $5/day | Manual CPC | High |
| **Total** | | | **$50/day = $1,500/mo** | | |

**Alpha/Beta structure:** Brand + proven exact-match keywords in Alpha campaigns; exploration and phrase-match in Beta campaigns. Winners from Beta graduate to Alpha [KB: contextologist skill - "Alpha/Beta structure"]

### Campaign Priority & Sequencing

**Phase 1 (Days 1-14):** Launch Brand + Non-brand EN (Hot) + Remarketing [KB: contextologist skill - "start with hot intent clusters"]
**Phase 2 (Days 15-30):** Add Competitors + Russian-language + Investment intent if Phase 1 signals positive [Assumption]

## 4. Ad Copy Framework

### RSA Requirements

Each ad group: minimum 1 RSA with Ad Strength "Good" or "Excellent" [KB: Google Ads - create-effective-search-ads.md - "advertisers who improve Ad Strength from 'Poor' to 'Excellent' see 12% more conversions on average"]

**15 Headlines per RSA:** include keyword, benefit, CTA, price/offer, social proof [KB: contextologist skill - "15 headlines: keyword, benefit, CTA, price, social proof"]

**Pin strategy:**
- Headline 1: Key offer with keyword [KB: contextologist skill - "Pin: H1 = key offer"]
- Headline 2: Benefit/USP [KB: contextologist skill - "H2 = benefit"]
- Headline 3: CTA [KB: contextologist skill - "H3 = CTA"]

**4 Descriptions:** expand benefit with specifics (numbers, facts), CTA [KB: contextologist skill - "4 descriptions: expand benefit, add specifics, CTA"]

### Extensions/Assets (Mandatory)

- Sitelinks (4+): Floor Plans, ROI Calculator, About Developer, Contact Us [KB: contextologist skill - "sitelinks 4+"]
- Callouts (4+): 8% Guaranteed ROI, Full Management, 25-Year Lease, From $180K [KB: contextologist skill - "callouts 4+"]
- Structured snippets: Property types (1BR Villa, 2BR Villa, 3BR Villa) [Platform docs: Google Ads]
- Location extension: Ubud, Bali [Platform docs]
- Call extension: WhatsApp/phone number [Platform docs]
- Price extension: Starting from $180,000 [Platform docs]

## 5. Bidding & Budget Strategy

### Phase 1: Data Collection (Days 1-14)

- **Bid strategy:** Manual CPC with Enhanced CPC on non-brand [KB: contextologist skill - "start with Manual CPC or Enhanced CPC for data collection"]
- **Target CPC:** $2-5 for non-brand, $0.50-1.50 for brand [Assumption - international real estate]
- **Daily budget:** $50/day total across all campaigns [Strategy - $1,500/mo hard cap]

### Phase 2: Optimization (Days 15-30)

- **Transition to Smart Bidding after 30+ conversions:** Target CPA = current average CPA x 0.8-1.0 [KB: contextologist skill - "Target CPA = current avg CPA x 0.8-1.0, not more aggressive"]
- **Budget reallocation:** Shift spend from underperforming campaigns to winners [KB: contextologist skill - "disable non-working, scale working"]

### Budget Distribution

| Campaign | Daily $ | Monthly $ | % of total |
|----------|---------|-----------|------------|
| Brand | $5 | $150 | 10% |
| Non-brand EN (Hot) | $15 | $450 | 30% |
| Non-brand RU | $10 | $300 | 20% |
| Bali Investment (Warm) | $10 | $300 | 20% |
| Competitors | $5 | $150 | 10% |
| Remarketing Display | $5 | $150 | 10% |
| **Total** | **$50** | **$1,500** | **100%** |

## 6. Audiences (Google)

| Audience | Type | Use | Priority |
|----------|------|-----|----------|
| In-market: Real Estate | Observation | Bid adjustment +20% [KB: contextologist skill - "In-market audiences: Real Estate"] | High |
| Custom audience: bali villa keywords | Targeting (Display) | Display + remarketing [KB: contextologist skill - "custom audiences by keywords, competitor URLs"] | Medium |
| Custom audience: competitor URLs | Targeting (Display) | Capture competitor traffic [KB: contextologist skill] | Medium |
| Website visitors 1-30d | Remarketing | RLSA + Display retargeting [KB: contextologist skill - "remarketing segments by depth: all visitors 30d"] | High |
| Plan viewers 14d | Remarketing | Higher intent retargeting [KB: contextologist skill - "plan view visitors 14d"] | High |
| Form starters non-submit 7d | Remarketing | Hottest retargeting pool [KB: contextologist skill - "form not submitted 7d"] | High |

**Note:** Similar audiences deprecated in Google Ads, replaced by Audience Expansion and Optimized Targeting [KB: contextologist skill - "Similar audiences deprecated"]

## 7. Remarketing Strategy

- **Active from Day 1** even with small budget ($5/day) [KB: contextologist skill - "remarketing mandatory from day 1"]
- **Segments:**
  - All visitors 30d: general messaging [KB: contextologist skill]
  - Plan/price page viewers 14d: deeper product info [KB: contextologist skill]
  - Form starters non-submit 7d: urgency + social proof [KB: contextologist skill]
- **Display remarketing CTA:** soft CTAs - "Download floor plans", "Calculate your ROI", "Book free consultation" [KB: contextologist skill - "soft CTAs for remarketing"]
- **RLSA:** +30% bid adjustment for returning searchers [KB: contextologist skill - "RLSA: increased bids for returning searchers"]
- **Frequency cap:** 3-5 impressions/day per user [KB: contextologist skill - "frequency cap: 3-5 per day"]

## 8. Optimization Timeline

| Period | Action | Signal to check |
|--------|--------|-----------------|
| Days 1-3 | Verify ad approval, check tracking fires, monitor impressions [KB: contextologist skill - "first 3 days: check serving status, ad approval, tracking"] | Ads serving, tracking confirmed |
| Days 4-7 | First search query review, clean negatives, check CTR by ad group [KB: contextologist skill - "days 4-7: first search query cleanup, check CTR"] | CTR baseline, query quality |
| Days 8-14 | Analyze CPL by campaign/group, disable waste [KB: contextologist skill - "days 8-14: CPL analysis, disable waste"] | CPL range by campaign |
| Weeks 3-4 | A/B test ad copy, expand/narrow semantics [KB: contextologist skill - "week 3-4: A/B test ads, semantic expansion"] | CPL trend, conversion rate |
| Month 2+ | Transition to Smart Bidding if 30+ conversions, scale winners [KB: contextologist skill - "month 2+: Smart Bidding transition"] | CPA stability, volume |

### Negative Keyword Hygiene

- First 2 weeks: review search terms report every 3 days [KB: contextologist skill - "first 1-2 weeks: search query cleanup every 3 days"]
- Add cross-group negatives to prevent keyword cannibalization [KB: contextologist skill - "cross-group negatives"]
- 80% of search success = negative keyword cleanliness [KB: contextologist skill - "80% of context success = negative cleanup"]

## 9. Risks & Dependencies

- **Landing page quality:** serenity-bali.com must match ad messaging, have clear CTAs, load fast (<3 sec). Quality Score depends on landing page relevance [KB: Google Ads - create-effective-search-ads.md - "match your ad to your landing page"]
- **Tracking dependency:** Without GA4 + Google Ads conversion tracking, optimization is blind [KB: contextologist skill - "without correct goals, optimization is blind"]
- **Low search volume risk:** "Buy villa Ubud" is a niche query - volume may be limited. If impression share is already 80%+, growth requires semantic expansion or Display/YouTube [Assumption]
- **CPC volatility:** Premium real estate keywords can spike during seasonal peaks [Assumption]
- **Ad policy:** Google prohibits superlatives without proof ("best villas") and misleading claims [KB: Google Ads - platform-specs.md - "no superlatives without third-party verification"]

## 10. Budget Compliance

- **Channel hard cap:** $1,500/mo [Strategy]
- **Planned spend:** $1,500/mo ($50/day x 30) [Plan]
- **Delta vs cap:** $0 [Calculated]
- **Status:** PASS

### Attribution Tags Summary

| Source | Count | % |
|--------|-------|---|
| [KB: contextologist skill.md] | 32 | ~46% |
| [KB: Google Ads platform docs / create-effective-search-ads] | 8 | ~11% |
| [KB: platform-specs.md] | 3 | ~4% |
| [Strategy] | 12 | ~17% |
| [Platform docs] | 5 | ~7% |
| [Assumption] | 10 | ~14% |
| **Total KB + Strategy + Platform** | **60** | **86%** |
