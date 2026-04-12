# Targeting Plan: Serenity Villas, Ubud

## 1. Objective & Conversion Setup

- **Business goal:** 60+ leads/month из Meta Ads при CPL < $40, с qualified lead rate > 25%
- **Meta objective:** Leads (Lead Generation)
- **Conversion location:** Instant Form (primary) + Website landing page (secondary)
- **Primary optimization event:** lead (instant form submission)
- **Secondary signals:** qualified lead (CRM feedback), phone call, WhatsApp message
- **Tracking status:** partial (assumption - нужно настроить до запуска)
- **Key measurement gaps:**
  - Meta Pixel + Conversions API на лендинге serenity-bali.com - требуется установка
  - CRM integration для offline conversion upload - статус неизвестен
  - Колтрекинг - не указан в брифе
  - Speed-to-lead SLA - не зафиксирован

## 2. ICP & Segments

### Segment 1: Русскоязычные инвесторы в зарубежную недвижимость
- **Who:** 30-55, РФ/СНГ/эмиграция, доход $5K+/мес, опыт инвестиций
- **Trigger:** Ищет диверсификацию капитала за рубежом, разочарован в РФ-рынке или крипто
- **Pain:** Страх мошенничества, непрозрачная доходность, удаленное управление
- **Offer angle:** Гарантированный 8% ROI + полное управление + лицензированный объект
- **Funnel temperature:** Cold -> Warm (через контент и ретаргетинг)

### Segment 2: Диджитал-номады на Бали / планирующие переезд
- **Who:** 25-45, фрилансеры/предприниматели, живут или планируют жить на Бали
- **Trigger:** Устал платить $1,500-3,000/мес аренду, хочет якорь на Бали
- **Pain:** Нестабильность аренды, деньги уходят в никуда, нет привязки
- **Offer angle:** Своя вилла дешевле 6 лет аренды, живи + сдавай при отъезде
- **Funnel temperature:** Cold -> Warm

### Segment 3: Семьи, релоцирующиеся на Бали
- **Who:** Пары 30-50 с детьми, удаленная работа, бюджет $200-400K
- **Trigger:** Решение о переезде принято, ищут постоянное жилье
- **Pain:** Безопасность, школы, пространство для детей, комьюнити
- **Offer angle:** Виллы 200+ м2 в Ubud, рисовые террасы, Green School 15 мин
- **Funnel temperature:** Warm (высокий intent, но длинный цикл решения)

## 3. Audience Matrix

| Audience | Type | Source | Funnel stage | Hypothesis | Priority |
|----------|------|--------|--------------|------------|----------|
| Broad Bali RE investors | Cold | Geo: RU/CIS + broad targeting | Cold | Housing category limits targeting; strong offer + creative filter audience | High |
| Interest: Real estate investment | Cold | Interest: Real estate investing, Property investment, Passive income | Cold | Intent-based cold audience, housing category compliant | High |
| Interest: Bali lifestyle | Cold | Interest: Bali, Ubud, Digital nomad, Expat life | Cold | Lifestyle-aligned audience for segments 2-3 | Medium |
| IG engagers 30d | Warm | Instagram account interaction | Warm | Cheaper re-engagement, already showed interest | High |
| Video viewers 50%+ | Warm | Video view custom audience | Warm | High attention = high intent signal | Medium |
| Site visitors 30d | Warm | Meta Pixel (serenity-bali.com) | Warm | Already explored the product | High |
| Form openers non-submit | Hot | Lead form custom audience | Hot | High intent, friction stopped them | High |
| Qualified leads LAL 1-3% | Cold | CRM upload -> LAL | Cold | Closest to buyer pattern (needs data) | Medium (Phase 2) |

**Note:** Housing category (Special Ad Category) ограничивает targeting - нельзя использовать возраст, пол, zip code. Компенсируем через сильный оффер в креативе и broad targeting с Advantage+.

## 4. Campaign Logic

### Campaign 1: Cold Acquisition - Investor angle
- **Goal:** Генерация лидов из холодной аудитории инвесторов
- **Ad sets:**
  - AS1: Broad + Advantage+ (Geo: Russia, Kazakhstan, Uzbekistan, UAE, Thailand, Indonesia, Georgia, Turkey, Armenia) - $25/day
  - AS2: Interest-based (Real estate investment + Passive income + Property abroad) - $20/day
- **Placements:** Advantage+ Placements (let Meta optimize)
- **Budget:** $45/day ($1,350/мес)
- **Creative requirement:** 3 варианта - ROI-focused, lifestyle-focused, comparison (аренда vs покупка)
- **Form:** Instant form с 3 вопросами: бюджет, срок покупки, контакт (WhatsApp/Telegram)

### Campaign 2: Cold Acquisition - Lifestyle/Nomad angle
- **Goal:** Привлечение номадов и семей
- **Ad sets:**
  - AS1: Interest-based (Bali + Ubud + Digital nomad + Expat) - $15/day
  - AS2: Broad Bali lifestyle (Geo: same + worldwide RU-speakers) - $10/day
- **Placements:** Advantage+ Placements
- **Budget:** $25/day ($750/мес)
- **Creative requirement:** Stories/Reels-first, lifestyle visuals (рисовые террасы, бассейн, утро на вилле)

### Campaign 3: Retargeting
- **Audience windows:** IG engagers 30d, Video viewers 50%+, Site visitors 14d, Form openers 7d
- **Message shift:** Social proof (кейсы), urgency (ограниченное количество), детали проекта, FAQ
- **Budget:** $13/day ($400/мес) из retargeting hard cap
- **Placements:** Feed + Stories

**Total Meta spend:** $45 + $25 + $13 = $83/day = $2,500/мес = hard cap. PASS.

## 5. Experiment Plan

| Test | Variable | Hypothesis | Success metric | Minimum run condition | Next action |
|------|----------|------------|----------------|-----------------------|------------|
| T1 | Audience: Broad vs Interest | Broad с Advantage+ даст более дешевый CPL при housing category | CPL + qualified lead rate | 5 days, min 1,000 impressions/ad set | Scale winner, kill loser |
| T2 | Offer angle: ROI vs Lifestyle | Инвестиционный угол даст более квалифицированные лиды | Qualified lead rate | 7 days | Scale winner |
| T3 | Form friction: 3 questions vs 2 | Меньше вопросов = больше лидов, но хуже качество | Lead volume vs qualified rate | 7 days, min 30 leads per variant | Pick best balance |
| T4 | Creative format: Static vs Video | Video даст ниже CPL на cold | CPL + form completion rate | 5 days | Scale winner format |

## 6. Optimization Rules

- **If CPM high (>$15):** Расширить гео, проверить creative fatigue, обновить креативы. Для housing category CPM $8-15 - норма.
- **If CTR low (<0.8%):** Тестировать новые hooks, менять визуал, проверить offer-audience fit
- **If CPL ok (<$40) but quality weak (<15% qualified):** Добавить qualifying вопросы в форму, сузить гео, проверить offer alignment
- **If lead-to-contact weak (>48h response):** Эскалация на клиента - speed-to-lead критичен для RE. Рекомендовать auto-reply + WhatsApp bot
- **If frequency >2.5:** Обновить креативы, расширить audience, перераспределить бюджет

## 7. Risks & Dependencies

- **Tracking risk:** Meta Pixel + CAPI не установлены (assumption) - BLOCKER для оптимизации. Нужно установить до запуска.
- **Sales process risk:** Скорость обработки лидов не зафиксирована. Для недвижимости speed-to-lead < 5 мин критичен.
- **Creative dependency:** Нужны качественные фото/видео вилл и Ubud. Renders допустимы для off-plan.
- **Policy / housing category:** Meta Housing Special Category ограничивает таргетинг. Компенсируем через creative quality и broad targeting.
- **CRM dependency:** Без CRM feedback loop невозможно оптимизировать по качеству лида. Минимум - ручная обратная связь 2 раза в неделю.
- **Landing page:** serenity-bali.com - не проверена на качество, конверсию, скорость загрузки. Если слабый лендинг - CPL вырастет.

## 8. Organic Support Layer

- **Need:** No (в стратегии нет SMM budget, весь бюджет на paid)
- **Recommendation:** При наличии Instagram-аккаунта Serenity Villas - минимальный organic: 2-4 поста в неделю (ход строительства, lifestyle Ubud, Q&A). Это бесплатно улучшает ретаргетинг (IG engagers audience) и trust.
- **Primary owned channel:** Instagram (если есть)
- **Paid sync:** Organic engagement feed retargeting campaigns

## 9. 14-Day Action Plan

| Day range | Action | Owner | Expected signal |
|-----------|--------|-------|-----------------|
| Day -3 to 0 | Setup: Pixel, CAPI, instant forms, creative production, CRM setup | Targeting + Dev | Clean infrastructure |
| Day 1-3 | Launch Campaign 1 (Investor cold) + Campaign 3 (Retargeting seed) | Targeting | Delivery, impressions, first clicks |
| Day 4-5 | Launch Campaign 2 (Lifestyle/Nomad) | Targeting | Expand reach |
| Day 4-7 | Early signal: CTR, CPL, form completion rate | Targeting | CTR > 0.8%, CPL < $50 |
| Day 8-10 | First pruning: kill weak ad sets, reallocate | Targeting | Remove losers |
| Day 11-14 | Scale winners, evaluate lead quality with sales team | Targeting + Sales | CPL < $40, qualified rate > 25% |

## 10. Budget Compliance

- **Channel hard cap:** $2,500/мес (Meta Ads)
- **Planned spend:** $2,500/мес ($83/день: $45 + $25 + $13)
- **Delta vs cap:** $0
- **Status:** PASS
