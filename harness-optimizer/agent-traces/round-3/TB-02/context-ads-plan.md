# Context Ads Plan: Serenity Villas, Ubud, Bali

## 1. Channel & Platform

- **Platform:** Google Ads (Search + Display) [Strategy - international market, Google Ads для международных рынков]
- **Market:** International (EN + RU) [Brief]
- **Hard cap:** $1,750/month [Strategy]
- **Role:** Demand capture - ловить горячий intent от людей, уже ищущих недвижимость на Бали [KB: contextologist skill - intent first]

## 2. Measurement Stack

- **Google Tag:** Required on serenity-bali.com [Platform docs: Google Ads]
- **GA4:** Setup with key events (lead_form_submit, phone_click, whatsapp_click) [KB: contextologist skill - GA4 events]
- **Enhanced conversions:** Hash email/phone for better matching [Platform docs: Google Ads enhanced conversions]
- **Offline conversion import:** Required after CRM setup - load lead -> qualified -> viewing -> deal [KB: contextologist skill - offline conversion tracking обязателен для недвижимости]
- **Attribution:** Data-driven attribution in GA4 [KB: contextologist skill - GA4 attribution]

## 3. Account Structure

### Semantic Core Architecture [KB: contextologist skill - структура = контроль]

**Campaign 1: Search - Hot Intent (EN)**
Budget: $700/month ($23/day)

| Ad Group | Keywords (Phrase Match) | Intent |
|----------|----------------------|--------|
| AG1: Buy Villa Ubud | "buy villa ubud", "villa for sale ubud", "ubud villa purchase" | Hot - direct purchase intent |
| AG2: Bali Investment Property | "bali investment property", "invest in bali real estate", "bali property roi" | Hot - investment intent |
| AG3: Bali Villa Management | "bali managed villa", "bali property management investment", "passive income bali" | Warm - management-focused |
| AG4: Competitor Brand | "bali home immo", "exotiq property bali", "kibarer property" | Hot - competitive capture |

**Campaign 2: Search - Hot Intent (RU)**
Budget: $500/month ($17/day)

| Ad Group | Keywords (Phrase Match) | Intent |
|----------|----------------------|--------|
| AG1: Купить виллу Бали | "купить виллу на бали", "вилла бали купить", "недвижимость убуд" | Hot |
| AG2: Инвестиции Бали | "инвестиции в недвижимость бали", "доходность бали", "roi бали недвижимость" | Hot |
| AG3: Вилла с управлением | "вилла бали с управлением", "пассивный доход бали", "управление виллой бали" | Warm |

**Campaign 3: Display - Remarketing**
Budget: $300/month ($10/day)

- Website visitors 7-30 days
- GA4 audiences: engaged visitors (2+ pages, 60+ sec)
- Lead form starters who didn't submit

**Campaign 4: Display - Cold Prospecting**
Budget: $250/month ($8/day)

- In-market: "Real Estate" + "Vacation Properties" [KB: contextologist skill - In-market audiences]
- Custom audiences: по URL конкурентов (balihomeimmo.com, exotiqproperty.com, kibarer.com) [KB: contextologist skill - Custom audiences по URL конкурентов]
- Geo: worldwide with emphasis on Russia, CIS, Europe, Australia

## 4. Negative Keywords [KB: contextologist skill - 80% успеха = чистка мусора]

### Universal negatives (pre-launch):
- rent, rental, airbnb, booking, hotel, hostel, cheap, free, job, work visa, volunteer
- аренда, снять, хостел, дешёвый, работа, виза, бесплатно
- "bali tour", "bali holiday", "bali vacation package"
- youtube, wiki, news, reddit, forum, review

### Category negatives:
- land, plot, commercial, office, warehouse
- участок, земля, коммерческая, офис

**Cleaning schedule:** Every 3 days for first 2 weeks, then weekly [KB: contextologist skill - первые 1-2 недели чистка каждые 3 дня]

## 5. Bid Strategy

- **Phase 1 (Days 1-14):** Maximize Clicks with daily budget cap - collect data [KB: contextologist skill - ручные ставки на старте для сбора данных]
- **Phase 2 (Days 15-30):** Switch to Maximize Conversions once 15+ conversions accumulated [KB: contextologist skill - Smart Bidding требует минимум 30 конверсий за 30 дней]
- **Phase 3 (Month 2+):** Target CPA once stable baseline established [Platform docs: Google Ads Smart Bidding]
- **Note:** With $1,750/month budget, accumulating 30 conversions in 30 days requires CPL ~$58 - tight but feasible [Assumption]

## 6. Ad Copy Direction

### Search Ads (EN) - Per Ad Group [KB: contextologist skill - ключевое слово в Headline 1]

**AG1: Buy Villa Ubud**
- H1: Villa in Ubud from $180K (keyword match)
- H2: 8% Guaranteed ROI - 2 Years (USP)
- H3: Book a Consultation Today (CTA)
- D1: Premium villas 120-280m2 in Ubud with full property management included. 25-year leasehold.
- D2: PT Serenity Bali. Transparent investment with guaranteed returns. Schedule a call.

**AG2: Bali Investment Property**
- H1: Bali Property - 8% ROI
- H2: Full Management Included
- H3: Get Investment Details
- D1: Premium Ubud villas from $180K. Guaranteed 8% return for first 2 years. 25-year leasehold.
- D2: No hassle ownership. Professional management handles everything. Request ROI breakdown.

**AG3: Competitor Brand**
- H1: Premium Villas in Ubud
- H2: 8% Guaranteed - 2 Years
- H3: Compare & Choose
- D1: Looking for Bali property? Consider Serenity Villas in Ubud. 120-280m2, full management.
- D2: Transparent pricing from $180K. No hidden fees. Download comparison sheet.

### Search Ads (RU)

**AG1: Купить виллу**
- H1: Вилла в Убуде от $180K
- H2: Гарантия дохода 8% - 2 года
- H3: Получить презентацию
- D1: Премиум виллы 120-280 м2 в Убуде. Полное управление включено. Leasehold 25 лет.
- D2: PT Serenity Bali. Прозрачная инвестиция с гарантированным доходом. Запишитесь на звонок.

## 7. Quality Score Optimization [KB: contextologist skill - Quality Score matters]

- **Relevance:** Keyword in H1, in description, on landing page
- **Landing page:** serenity-bali.com must load < 3 sec, mobile-optimized, contain keyword clusters
- **CTR optimization:** Test 3+ RSA variants per ad group, pin critical headlines to positions 1-3 [Platform docs: Google Ads RSA best practices]
- **Ad strength target:** "Good" to "Excellent" [KB: contextologist skill - Excellent = +12% конверсий vs Poor]

## 8. Optimization Rules

- **If CPC > $5 (EN) or > $3 (RU):** Review keyword relevance, add negatives, test new ad copy [Assumption - premium real estate CPC benchmarks]
- **If CTR < 3% (Search):** Weak ad copy or wrong keywords, test new headlines [KB: contextologist skill]
- **If CPL ok but quality weak:** Add qualifying questions to form, tighten keyword match types [KB: contextologist skill]
- **If Display CTR < 0.3%:** Refresh banners, tighten audience [Assumption]
- **Search term mining:** Every 3 days week 1-2, weekly after [KB: contextologist skill]

## 9. 14-Day Action Plan

| Day range | Action | Expected signal |
|-----------|--------|-----------------|
| 1-2 | Setup: Google Tag, GA4, conversion events, account structure | Clean tracking |
| 3-4 | Launch Search EN + RU campaigns (Maximize Clicks) | First clicks, CTR data |
| 5-7 | First search term review, add negatives, launch Display remarketing | CPC, CTR direction |
| 8-10 | Second search term cleanup, launch Display prospecting | CPL estimates |
| 11-14 | Pause low-CTR ad groups, reallocate to winners | CPL < $60 trend |

## 10. Budget Compliance

- **Channel hard cap:** $1,750/month [Strategy]
- **Planned spend:** $1,750/month ($700 Search EN + $500 Search RU + $300 Remarketing + $250 Display Cold)
- **Delta vs cap:** $0
- **Status:** PASS
