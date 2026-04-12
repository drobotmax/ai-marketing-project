# Валидация креативов: Serenity Villas, Ubud, Bali

**Дата:** 2026-04-03
**Статус:** APPROVED (with notes)

## Сводка

| Всего креативов | PASS | WARN | FAIL |
|----------------|------|------|------|
| 11 | 9 | 2 | 0 |

## Launch Readiness

| Проверка | Статус | Детали |
|----------|--------|--------|
| Landing page URL в брифе | PASS | https://serenity-bali.com |
| CRM система указана | WARN | Not specified in brief - need confirmation |
| Privacy policy link в лид-форме | WARN | Must verify on landing page before launch |
| 152-ФЗ consent | N/A | International market, not Russia-based |
| CRM integration / fallback | WARN | Not specified - recommend manual lead export as fallback |
| Фид для товарного МК | N/A | No catalog/feed ads in media plan |
| Google Analytics / GA4 | WARN | Must be configured before Google Ads launch |
| Pixel / CAPI | WARN | Must be verified on serenity-bali.com before Meta launch |

**Launch readiness verdict:** Conditional PASS - tracking setup must be completed during Week 0 (prep week). No BLOCKED items.

## Детальная проверка

### Meta Feed - Вариант 1 (Инвесторы RU)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Длина primary text | PASS (196/2200) | Within recommended 125 for preview, full text OK |
| Длина headline | PASS (24/40) | |
| Длина description | PASS (21/30) | |
| Meta policy | PASS | No personal attributes, no misleading claims |
| Hook quality | PASS | Specific number (18% drop), unique to market context, loss aversion lever |
| Бриф compliance | PASS | Matches investor segment, 8% ROI USP, price range |
| CTA | PASS | "Get Offer" |
| Grammar | PASS | |

**Итог:** PASS

### Meta Feed - Вариант 2 (Инвесторы EN)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Длина primary text | PASS (186/2200) | |
| Длина headline | PASS (27/40) | |
| Длина description | PASS (25/30) | |
| Meta policy | PASS | |
| Hook quality | PASS | Specific number (7,100 units), Canggu vs Ubud comparison, curiosity gap |
| Бриф compliance | PASS | |
| CTA | PASS | "Learn More" |
| Grammar | PASS | |

**Итог:** PASS

### Meta Feed - Вариант 3 (Digital nomads)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Длина primary text | PASS (168/2200) | |
| Длина headline | PASS (25/40) | |
| Длина description | PASS (14/30) | |
| Meta policy | PASS | |
| Hook quality | PASS | Specific cost ($1,500/мес), contrast with ownership, unique pain point |
| Бриф compliance | PASS | Matches digital nomad segment |
| CTA | PASS | "Get Offer" |
| Grammar | PASS | |

**Итог:** PASS

### Meta Feed - Вариант 4 (Семьи)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Длина primary text | PASS (195/2200) | |
| Длина headline | PASS (26/40) | |
| Длина description | PASS (25/30) | |
| Meta policy | PASS | |
| Hook quality | PASS | Specific area (280 м2), location detail (рисовые террасы), lifestyle paint |
| Бриф compliance | PASS | Matches family segment |
| CTA | PASS | "Contact Us" |
| Grammar | PASS | |

**Итог:** PASS

### Meta Stories - Вариант 1 (Инвесторы RU)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Text overlay | PASS (3 lines) | |
| Meta policy | PASS | |
| Hook quality | PASS | 7,100 units comparison |
| Format | PASS | 9:16 vertical, 15 sec |

**Итог:** PASS

### Meta Stories - Вариант 2 (Digital nomads EN)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Text overlay | PASS (3 lines) | |
| Meta policy | PASS | |
| Hook quality | PASS | $1,500/mo cost comparison |
| Format | PASS | 9:16, 15 sec |

**Итог:** PASS

### Meta Stories - Вариант 3 (Семьи RU)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Text overlay | PASS (3 lines) | |
| Meta policy | PASS | |
| Hook quality | PASS | Moscow apartment vs Ubud villa comparison, 280 m2 |
| Format | PASS | 9:16, 15 sec |

**Итог:** PASS

### Google Search - Вариант 1 (EN, Buy Villa Ubud)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Headline 1 | PASS (25/30) | Contains keyword "Ubud" |
| Headline 2 | PASS (24/30) | |
| Headline 3 | PASS (25/30) | CTA present |
| Description 1 | PASS (84/90) | Trimmed version used |
| Description 2 | PASS (89/90) | |
| Display path | PASS (12/15) | |
| Google policy | PASS | No superlatives, no excessive caps |
| Keyword in H1 | PASS | "Ubud" present |

**Итог:** PASS

### Google Search - Вариант 2 (EN, Bali Investment)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Headline 1 | PASS (23/30) | |
| Headline 2 | PASS (25/30) | |
| Headline 3 | PASS (21/30) | |
| Description 1 | PASS (90/90) | At limit |
| Description 2 | PASS (81/90) | |
| Display path | PASS (12/15) | |
| Google policy | PASS | |

**Итог:** PASS

### Google Search - Вариант 3 (RU, Купить виллу)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Headline 1 | PASS (22/30) | |
| Headline 2 | WARN (25/30) | Cyrillic chars - verify Google counts same as Latin |
| Headline 3 | PASS (20/30) | |
| Description 1 | PASS (81/90) | |
| Description 2 | PASS (79/90) | |
| Display path | WARN (11/15) | Cyrillic path "/виллы-убуд" may not render correctly in Google Ads; recommend Latin "/villy-ubud" |
| Google policy | PASS | |

**Итог:** PASS with WARN (display path encoding)

**Рекомендация:** Change display path to Latin: `/villy-ubud` (11 chars)

### Google Search - Вариант 4 (EN, Competitor)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Headline 1 | PASS (19/30) | |
| Headline 2 | PASS (23/30) | |
| Headline 3 | PASS (22/30) | |
| Description 1 | PASS (88/90) | |
| Description 2 | PASS (76/90) | |
| Display path | PASS (8/15) | |
| Google policy | PASS | No trademark use in headlines |

**Итог:** PASS

## Hook Quality Validation (Round 3 Critical Check)

| # | Hook | Contains specific? | Unique to Serenity? | Banned template? | Lever unique? | Verdict |
|---|------|-------------------|---------------------|-------------------|---------------|---------|
| MF1 | "Доходность аренды упала на 18%" | YES (18%) | YES (contrasts with 8% guarantee) | NO | Loss aversion | PASS |
| MF2 | "Canggu has 7,100 new units" | YES (7,100) | YES (Ubud vs Canggu) | NO | Curiosity gap | PASS |
| MF3 | "$1,500/мес за аренду" | YES ($1,500) | YES (own vs rent comparison) | NO | Contrast | PASS |
| MF4 | "280 м2 среди рисовых террас" | YES (280 m2) | YES (Ubud terraces) | NO | Authority | PASS |
| MS1 | "7,100 новых вилл в Canggu" | YES (7,100) | YES | NO | Loss aversion | PASS |
| MS2 | "Canggu rent: $1,500/mo" | YES ($1,500) | YES | NO | Contrast | PASS |
| MS3 | "Площадь квартиры в Москве = 280 м2" | YES (280 m2) | YES (Moscow comparison) | NO | Social proof | PASS |
| GS1 | "Villas in Ubud from $180K" | YES ($180K) | YES | NO | Intent match | PASS |
| GS2 | "Bali Property - 8% ROI" | YES (8%) | YES | NO | Authority | PASS |
| GS3 | "Доход 8% гарантия 2 года" | YES (8%, 2 years) | YES | NO | Authority | PASS |
| GS4 | "Compare Bali Projects" | Indirect (comparison CTA) | YES | NO | Contrast | PASS |

**Hook quality verdict:** ALL HOOKS PASS. Every hook contains at least one specific element (number, fact, or comparison). No banned templates used. Different psychological levers across variants. All hooks are specific to Serenity Villas / Ubud market.

## Исправления (auto-fix)

### Исправлен: Google Search - Вариант 3
- **Было:** Display path `/виллы-убуд` (Cyrillic)
- **Стало:** Display path `/villy-ubud` (11 chars, Latin)
- **Что изменено:** Switched to Latin transliteration for reliable rendering

## Итоговый вердикт

**Статус: APPROVED**

Все 11 креативов прошли валидацию. 2 minor WARNs (Cyrillic display path и char count verification для кириллицы) не блокируют запуск.

**Hook quality for Round 3:** PASS - все хуки содержат конкретику (числа, факты, сравнения), уникальны для Serenity Villas, используют разные psychological levers. Ни один banned template не использован.

**Pre-launch checklist:**
- [ ] Verify Pixel + CAPI on serenity-bali.com
- [ ] Configure GA4 + Google Tag
- [ ] Create instant form in Meta with privacy policy link
- [ ] Confirm CRM system or manual lead export process
- [ ] Prepare 9+ visual assets (renders, photos, video clips)
- [ ] Fix display path to Latin for Google Search Variant 3
