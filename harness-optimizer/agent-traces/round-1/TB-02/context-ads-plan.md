# Контекстная реклама: Serenity Villas, Ubud

**Платформа:** Google Ads (международный рынок, Bali)
**Язык объявлений:** Русский (primary) + English (secondary, Phase 2)
**Hard cap:** $2,000/мес + $500/мес retargeting share (совместно с Meta)

## 1. Measurement Setup

### Текущий статус (assumption - требуется подтверждение)
- GA4: нет | Goals: не настроены
- GTM: нет
- Колтрекинг: нет
- CRM integration: нет
- Offline conversion import: нет

### Что нужно настроить (до запуска)
1. GA4 property + настройка key events: form_submit, phone_click, whatsapp_click
2. GTM container на serenity-bali.com: GA4 tag, Google Ads conversion tracking, scroll tracking
3. Google Ads conversion tracking: primary = form_submit, secondary = phone_click
4. Enhanced conversions: hash email + phone для лучшего matching
5. Offline conversion import setup (Phase 2, после накопления CRM данных)

### Ключевые конверсии для оптимизации

| Event | Type | Value | Platform |
|-------|------|-------|----------|
| form_submit | Macro | $50 proxy | GA4 + Google Ads |
| phone_click | Macro | $50 proxy | GA4 + Google Ads |
| whatsapp_click | Macro | $40 proxy | GA4 + Google Ads |
| plan_view | Micro | - | GA4 |
| scroll_50 | Micro | - | GA4 |
| video_play_50 | Micro | - | GA4 |

## 2. Семантическое ядро

### Google Ads

#### Кластер 1: Brand [Serenity Villas / Serenity Bali]
| Keyword | Match Type | Est. CPC | Monthly Volume | Intent |
|---------|-----------|----------|----------------|--------|
| serenity villas bali | Exact | $0.50 | 10-50 | Hot |
| serenity villas ubud | Exact | $0.50 | 10-50 | Hot |
| serenity bali | Phrase | $0.40 | 10-50 | Hot |

**Note:** Бренд новый, volume минимальный. Brand-кампания нужна для защиты, но бюджет минимальный.

#### Кластер 2: Гео + Коммерческий (RU)
| Keyword | Match Type | Est. CPC | Monthly Volume | Intent |
|---------|-----------|----------|----------------|--------|
| купить виллу на бали | Exact | $2.50 | 200-500 | Hot |
| вилла на бали цена | Phrase | $2.00 | 300-600 | Hot |
| недвижимость бали | Phrase | $1.80 | 500-1000 | Warm |
| виллы убуд купить | Exact | $2.20 | 50-150 | Hot |
| инвестиции в недвижимость бали | Phrase | $2.80 | 200-400 | Hot |
| купить дом на бали | Phrase | $2.00 | 300-500 | Hot |
| новостройки бали | Phrase | $1.50 | 100-200 | Warm |

#### Кластер 3: Коммерческий (EN)
| Keyword | Match Type | Est. CPC | Monthly Volume | Intent |
|---------|-----------|----------|----------------|--------|
| buy villa ubud bali | Exact | $3.00 | 200-400 | Hot |
| bali property investment | Phrase | $3.50 | 500-800 | Hot |
| ubud villas for sale | Exact | $2.80 | 300-500 | Hot |
| bali real estate | Phrase | $2.50 | 1000-2000 | Warm |
| invest in bali property | Phrase | $3.00 | 200-400 | Hot |

#### Кластер 4: Конкуренты
| Keyword | Match Type | Est. CPC | Monthly Volume | Intent |
|---------|-----------|----------|----------------|--------|
| bali home immo | Exact | $1.50 | 200-500 | Hot |
| exotiq property bali | Exact | $1.50 | 100-300 | Hot |
| kibarer property | Exact | $1.20 | 200-400 | Hot |

#### Кластер 5: Информационный с коммерческим подтекстом (RU)
| Keyword | Match Type | Est. CPC | Monthly Volume | Intent |
|---------|-----------|----------|----------------|--------|
| доходность недвижимости бали | Phrase | $1.50 | 100-200 | Warm |
| переезд на бали | Phrase | $1.00 | 500-1000 | Warm |
| жизнь на бали стоимость | Phrase | $0.80 | 300-600 | Warm |
| leasehold бали | Phrase | $1.20 | 50-150 | Warm |

#### Минус-слова (базовый список)
- аренда, снять, rent, rental
- бесплатно, free, cheap
- отзывы, review, blog
- работа, вакансии, jobs
- виза, visa
- отель, hotel, hostel, хостел
- туры, tour, путевка, экскурсия
- фото, photo, wallpaper, обои
- курс, course, обучение
- б/у, secondhand
- forex, трейдинг, биткоин, bitcoin

## 3. Структура аккаунта

### Google Ads

| Campaign | Type | Match Types | Daily Budget | Bid Strategy | Priority |
|----------|------|-------------|--------------|--------------|----------|
| Brand - Serenity | Search | Exact + Phrase | $3 | Manual CPC | Medium |
| Non-Brand - Hot Intent RU | Search | Exact + Phrase | $20 | Manual CPC -> tCPA (после 30 conv) | High |
| Non-Brand - Hot Intent EN | Search | Exact + Phrase | $15 | Manual CPC -> tCPA | High |
| Competitors | Search | Exact | $5 | Manual CPC | Low |
| Display - Remarketing | Display | - | $7 | tCPA | High |
| PMax - Bali Property | PMax | - | $17 | Max Conversions | Medium |

**Budget check:**
- Daily total: $3 + $20 + $15 + $5 + $7 + $17 = $67/день
- Monthly: $67 x 30 = $2,010/мес
- Hard cap: $2,000/мес (Google context) + часть retargeting cap
- Delta: -$10 (retargeting Display покрывается из $500 retargeting cap)
- **Status: PASS** (Display remarketing $7/day = $210/мес берется из retargeting cap $500)
- Net Google context spend: $60/day = $1,800/мес < $2,000 cap. PASS.

## 4. Объявления

### Google Search RSA - Non-Brand Hot Intent RU

**Ad Group: Купить виллу Бали**

Headlines (15):
1. "Виллы в Убуде от $180 000" - PIN 1 (25 chars)
2. "Доход 8% первые 2 года" - PIN 2 (22 chars)
3. "Запишитесь на презентацию" - PIN 3 (25 chars)
4. "Serenity Villas Ubud" (20 chars)
5. "Полное управление включено" (26 chars)
6. "Leasehold 25 лет + продление" (28 chars)
7. "120-280 м2 с бассейном" (22 chars)
8. "Рассрочка от застройщика" (24 chars)
9. "Лицензированный проект" (22 chars)
10. "Убуд: рисовые террасы" (22 chars)
11. "Без комиссии УК сверху" (22 chars)
12. "Премиальный комплекс" (20 chars)
13. "PT Serenity Bali" (17 chars)
14. "От застройщика напрямую" (23 chars)
15. "Виллы на Бали под ключ" (22 chars)

Descriptions (4):
1. "Премиальные виллы 120-280 м2 в сердце Убуда. Гарантированный доход 8% первые 2 года. Полное управление." (90 chars - подсчет предварительный)
2. "Serenity Villas: leasehold 25 лет с продлением, бассейн, рисовые террасы. От $180 000. Запись на презентацию." (90 chars - подсчет предварительный)
3. "Забудьте об управлении. Мы строим, сдаем в аренду и гарантируем 8% годовых. Осталось 15 вилл." (86 chars)
4. "5.47 млн туристов на Бали в 2025. Убуд - центр wellness-туризма. Инвестируйте в растущий рынок." (88 chars)

Display URL path: /villas-ubud (12 chars) / roi-8 (5 chars)

Extensions:
- Sitelinks: "Планировки вилл" (15 chars), "Калькулятор дохода" (18 chars), "О застройщике" (13 chars), "Локация Убуд" (12 chars)
- Callouts: "Гарантия 8% ROI" (15 chars), "Полное управление" (17 chars), "От $180 000" (11 chars), "25 лет leasehold" (16 chars)
- Structured snippets: Типы: "1BR вилла, 2BR вилла, 3BR вилла, Пентхаус"

### Google Search RSA - Non-Brand Hot Intent EN

**Ad Group: Buy Villa Ubud**

Headlines (15):
1. "Ubud Villas From $180,000" - PIN 1 (25 chars)
2. "8% ROI Guaranteed 2 Years" - PIN 2 (25 chars)
3. "Book a Presentation" - PIN 3 (19 chars)
4. "Serenity Villas Bali" (20 chars)
5. "Full Property Management" (24 chars)
6. "25-Year Leasehold" (17 chars)
7. "120-280 sqm With Pool" (21 chars)
8. "Directly From Developer" (23 chars)
9. "Licensed & Compliant" (20 chars)
10. "Ubud Rice Terrace Views" (23 chars)
11. "Premium Villa Complex" (21 chars)
12. "Investment in Bali" (18 chars)
13. "No Hidden Fees" (14 chars)
14. "Turnkey Bali Property" (21 chars)
15. "Start Earning From Day 1" (24 chars)

Descriptions (4):
1. "Premium villas 120-280 sqm in Ubud, Bali. Guaranteed 8% ROI for 2 years. Full property management included." (89 chars - подсчет предварительный)
2. "Serenity Villas: 25-year leasehold with extension. Private pool, rice terrace views. From $180,000." (86 chars)
3. "Forget about management hassles. We build, rent out and guarantee 8% annual returns. Limited units." (87 chars)
4. "5.47M tourists visited Bali in 2025. Ubud is the heart of wellness tourism. Invest in a growing market." (90 chars - подсчет предварительный)

Display URL path: /ubud-villas (12 chars) / roi-8 (5 chars)

Extensions:
- Sitelinks: "Villa Floor Plans" (17 chars), "ROI Calculator" (14 chars), "About Developer" (15 chars), "Ubud Location" (13 chars)
- Callouts: "8% Guaranteed ROI" (17 chars), "Full Management" (15 chars), "From $180,000" (13 chars), "25-Year Lease" (13 chars)

### Google Display - Remarketing

**Ad Group: Site Visitors**

Short headlines (5):
1. "Still Considering Ubud?" (23 chars)
2. "Your Bali Villa Awaits" (21 chars)
3. "8% ROI - Limited Villas" (23 chars)
4. "Serenity Villas Ubud" (20 chars)
5. "Виллы в Убуде от $180K" (22 chars)

Long headline (1):
"Premium Ubud villas with guaranteed 8% returns and full management - book your private presentation today" (90 chars - подсчет предварительный)

Descriptions (5):
1. "You explored Serenity Villas. Book a private presentation and see floor plans. Limited units available." (88 chars)
2. "Guaranteed 8% ROI for 2 years. Full property management. 25-year leasehold. From $180,000." (80 chars)
3. "Виллы в Убуде с гарантированным доходом 8%. Запишитесь на презентацию. Осталось ограниченное число." (86 chars)
4. "Wake up to rice terrace views. Earn 8% annually. Zero management hassle. Serenity Villas, Ubud." (84 chars)
5. "120-280 sqm premium villas in Ubud. Pool, garden, full management. Investment starts at $180,000." (85 chars)

### Performance Max - Asset Group: Bali Property Investment

Headlines (5):
1. "Ubud Villas From $180,000" (25 chars)
2. "8% Guaranteed ROI" (17 chars)
3. "Serenity Villas Bali" (20 chars)
4. "Invest in Ubud Property" (23 chars)
5. "Виллы на Бали от $180K" (22 chars)

Long headlines (5):
1. "Premium Ubud villas with guaranteed 8% returns and full management from developer PT Serenity Bali" (87 chars)
2. "Own a villa in Ubud, Bali - 120-280 sqm, private pool, rice terrace views, from $180,000" (78 chars)
3. "Инвестиции в Бали: виллы в Убуде с гарантированным доходом 8% первые 2 года и полным управлением" (87 chars)
4. "Forget Canggu crowds - Ubud villas offer higher yields, better lifestyle and real serenity" (80 chars)
5. "25-year leasehold with extension, full property management, licensed and compliant project in Ubud" (87 chars)

Descriptions (5):
1. "Premium villas 120-280 sqm in the heart of Ubud. 8% guaranteed ROI, full management. Book a presentation." (90 chars - подсчет предварительный)
2. "Serenity Villas: the smart Bali investment. Licensed, managed, profitable. From $180K. Limited availability." (90 chars - подсчет предварительный)
3. "5.47M tourists in Bali 2025. Ubud yields +30% for view villas. Invest smart with Serenity Villas." (87 chars)
4. "Виллы в Убуде от застройщика. Доход 8% гарантия, полное управление, leasehold 25 лет." (75 chars)
5. "Skip the Canggu oversupply. Ubud premium villas with pool, management and guaranteed returns." (82 chars)

Audience signals:
- In-market: Real Estate
- Custom: keywords (buy villa bali, bali investment property, ubud real estate)
- Custom: URLs (bali-home-immo.com, exotiqproperty.com, kibarer.com)

## 5. Аудитории и ремаркетинг

### Remarketing Lists

| Audience | Window | Est. Size | Use Case | Platform |
|----------|--------|-----------|----------|----------|
| All site visitors | 30d | ~500-1000 | Awareness recall | Display + RLSA |
| Plan/pricing page viewers | 14d | ~150-300 | Push to form submit | Display |
| Form page visitors no submit | 7d | ~50-100 | Recovery | Display + RLSA |
| Converters (form submitters) | 180d | ~30-60 | Exclude | All campaigns |

### Custom Audiences (Google)

| Audience | Type | Signals |
|----------|------|---------|
| Bali RE Seekers | Keywords | купить виллу бали, bali villa investment, ubud property |
| Competitor visitors | URL | bali-home-immo.com, exotiqproperty.com, kibarer.com |
| Relocation intent | Keywords | переезд на бали, moving to bali, bali expat life |

## 6. Experiment Plan

| # | Variable | Hypothesis | Success Metric | Duration | Next Action |
|---|----------|------------|----------------|----------|-------------|
| 1 | RU vs EN campaigns | RU audience даст дешевле CPL (менее конкурентный аукцион) | CPL by language | 14 days | Перераспределить бюджет к winner |
| 2 | Search vs PMax | PMax даст больший объем при сопоставимом CPL | CPL + volume + qualified rate | 21 days | Scale winner, reduce loser budget |
| 3 | Competitor keywords | Competitor terms конвертируют по цене < 2x non-brand CPL | CPL + conversion rate | 14 days | Keep if profitable, kill if >2x CPL |
| 4 | Manual CPC vs tCPA | tCPA (после 30 conv) снизит CPL на 15%+ | CPL comparison | 14 days post-switch | Stay on tCPA if winning |

## 7. Optimization Rules

### Ежедневно (первые 2 недели)
- Чистка поисковых запросов (Search Terms Report) - каждые 3 дня минимум
- Проверка статуса показа и одобрения объявлений
- Мониторинг бюджета (не исчерпывается ли раньше 18:00 по целевому часовому поясу)

### Еженедельно
- Анализ CPL по кампаниям / группам / ключевым словам
- Корректировка ставок по устройствам (mobile vs desktop)
- Обновление минус-слов
- Проверка Ad Strength (target: Good или Excellent)

### Ежемесячно
- Full audit: waste spend, top performers, expansion opportunities
- Решение о переходе на Smart Bidding (если 30+ конверсий)
- Обновление объявлений: новые углы, свежие данные
- Синхронизация с CRM: qualified lead rate, cost per qualified lead

### Decision Matrix

| Сигнал | Действие |
|--------|----------|
| CTR < 2% (Search) | Ревизия заголовков, проверить релевантность ключ-объявление |
| CPC растет, CTR стабильный | Проверить конкуренцию (Auction Insights), тестировать новые углы |
| CPL ок, но качество слабое | Сузить семантику, добавить минус-слова, проверить landing page alignment |
| CPL высокий, CTR высокий | Проблема в конверсии сайта - audit landing page |
| Ad Strength < Good | Добавить разнообразие в headlines, использовать keyword insertion |
| Budget exhaustion до 14:00 | Сузить гео, время показа, или перераспределить от слабых кампаний |
| PMax spending but no conversions (7d) | Проверить audience signals, landing page, conversion tracking |

## 8. Risks & Dependencies

- **Tracking:** GA4 + GTM не установлены (assumption). BLOCKER - нужно настроить ДО запуска.
- **Landing page:** serenity-bali.com не проверен на скорость, мобильную адаптацию, конверсионные элементы. Если Pagespeed < 50, это blocker.
- **Конкуренция в аукционе:** Bali real estate - competitive niche в Google. CPC $2-4 нормально для premium сегмента.
- **Сезонность:** Q1-Q2 (январь-июнь) - high season для Bali RE interest. Q3 (июль-сентябрь) - спад.
- **CRM feedback:** Без CRM data невозможно оптимизировать по qualified leads. Минимум - ручная выгрузка 2 раза в неделю.
- **PMax data dependency:** Performance Max требует 30+ конверсий за 30 дней для стабильной работы. На старте может быть нестабилен.

## 9. Launch Calendar

| Период | Действие | Бюджет/день |
|--------|----------|-------------|
| Day -3 to 0 | Setup: GA4, GTM, conversion tracking, Google Ads account structure, QA | $0 |
| Day 1-3 | Launch: Brand + Non-Brand Hot RU + Remarketing | $30 |
| Day 4-7 | Add: Non-Brand Hot EN | $48 |
| Day 8-14 | Add: Competitors + PMax. Первая чистка запросов. | $60 |
| Day 15-21 | Analyze CPL/quality. Prune losers. Consider Display expansion. | $67 |
| Day 22-30 | Full $67/day run. Evaluate Smart Bidding readiness. | $67 |

## 10. Budget Compliance

- **Channel hard cap:** $2,000/мес (Google Ads context) + $290/мес (Google remarketing из retargeting pool)
- **Planned daily spend:** $67/день ($60 context + $7 remarketing)
- **Planned monthly spend:** $2,010/мес ($1,800 context + $210 remarketing)
- **Context only:** $1,800/мес vs $2,000 cap = -$200 buffer
- **Remarketing:** $210/мес из $500 retargeting cap (остальные $290 - на Meta retargeting)
- **Status: PASS**
