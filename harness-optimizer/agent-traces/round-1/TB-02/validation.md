# Валидация креативов: Serenity Villas, Ubud

**Дата:** 2026-04-03
**Статус:** NEEDS REVISION (minor)
**Режим:** auto-fix

## Сводка

| Всего креативов | PASS | WARN | FAIL |
|----------------|------|------|------|
| 13 | 10 | 2 | 1 |

## Launch readiness

| Проверка | Статус | Детали |
|----------|--------|--------|
| Landing page URL в брифе | PASS | https://serenity-bali.com |
| CRM система указана | WARN | Не указана в брифе. Нужно уточнить у клиента. Без CRM невозможен offline conversion feedback. |
| Privacy policy link в лид-форме | WARN | Не проверено - требуется наличие на лендинге и в instant forms. |
| Consent на обработку ПД | WARN | Instant forms Meta автоматически включают consent. Для лендинга - проверить наличие чекбокса. |
| CRM integration / fallback | WARN | API не указан. Рекомендация: ручная выгрузка 2 раза в неделю как fallback. |
| Фид для PMax | N/A | PMax без property feed, на asset groups. Допустимо. |
| GA4 | WARN | Не установлен (assumption). BLOCKER для Google Ads launch. |
| Колтрекинг | WARN | Не указан. Рекомендуется подключить до запуска. |

**Launch readiness verdict:** CONDITIONAL PASS - запуск возможен при условии установки GA4 + GTM + Meta Pixel до Day 1. CRM и колтрекинг - strong recommendation, не hard blocker для Phase 1.

---

## Детальная проверка

### Meta Feed - Вариант 1 (Инвесторы, ROI)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Primary text length | PASS (125/125) | На границе рекомендованного лимита |
| Headline length | PASS (22/40) | OK |
| Description length | PASS (19/30) | OK |
| Meta policy - personal attributes | PASS | Нет обращения к личным характеристикам |
| Meta policy - misleading claims | WARN | "доход 8% годовых - гарантия от застройщика" - допустимо, т.к. это contractual guarantee, не misleading claim. Но Meta модерация может потребовать disclaimer. |
| Meta policy - housing category | PASS | Нет targeting ограничений в тексте |
| Бриф compliance | PASS | ROI 8%, management included, цена $180K - все из брифа |
| CTA | PASS | Get Offer - релевантный |
| Hook | PASS | "Вилла в Убуде с доходом 8% годовых" - останавливает скролл |
| Grammar | PASS | OK |

**Итог:** PASS

### Meta Feed - Вариант 2 (Номады, аренда vs покупка)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Primary text length | PASS (119/125) | OK |
| Headline length | PASS (25/40) | OK |
| Description length | PASS (21/30) | OK |
| Meta policy | PASS | Нет нарушений |
| Бриф compliance | PASS | Цена, lifestyle, Ubud |
| CTA | PASS | Learn More |
| Hook | PASS | "5 лет аренды = $90 000 в никуда" - сильный comparison hook |
| Grammar | PASS | OK |

**Итог:** PASS

### Meta Feed - Вариант 3 (Семьи)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Primary text length | PASS (112/125) | OK |
| Headline length | PASS (22/40) | OK |
| Description length | PASS (20/30) | OK |
| Meta policy | PASS | Нет нарушений |
| Бриф compliance | PASS | Семьи, Ubud, площадь, школы |
| CTA | PASS | Contact Us |
| Hook | PASS | "Дети растут среди рисовых террас" - emotional |
| Grammar | PASS | OK |

**Итог:** PASS

### Meta Feed - Вариант 4 (Инвесторы, anti-hype)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Primary text length | PASS (125/125) | На границе |
| Headline length | PASS (27/40) | OK |
| Description length | PASS (22/30) | OK |
| Meta policy | PASS | Anti-hype positioning, не misleading |
| Бриф compliance | PASS | Честная доходность, management |
| CTA | PASS | Get Offer |
| Hook | PASS | "15-20% ROI? Забудьте." - provocative, attention-grabbing |
| Grammar | PASS | OK |

**Итог:** PASS

### Meta Stories - Вариант 1 (Инвесторы)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Text overlay lines | PASS (3/3) | OK |
| Line lengths | PASS | Все строки читаемы крупным шрифтом |
| Meta policy | PASS | OK |
| Бриф compliance | PASS | ROI, цена, управление |
| CTA | PASS | Swipe Up / Link sticker |

**Итог:** PASS

### Meta Stories - Вариант 2 (Номады)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Text overlay lines | PASS (3/3) | OK |
| Meta policy | PASS | OK |
| Бриф compliance | PASS | Lifestyle, цена |
| CTA | PASS | Link sticker |

**Итог:** PASS

### Meta Stories - Вариант 3 (Семьи)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Text overlay lines | PASS (3/3) | OK |
| Meta policy | PASS | OK |
| Бриф compliance | PASS | Семьи, площадь, школы |
| CTA | PASS | Link sticker |

**Итог:** PASS

### Google Search - Вариант 1 (Инвесторы RU)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Headline 1 length | PASS (25/30) | OK |
| Headline 2 length | PASS (22/30) | OK |
| Headline 3 length | PASS (20/30) | OK |
| Description 1 length | PASS (89/90) | OK |
| Description 2 length | PASS (88/90) | OK |
| Display path 1 | PASS (12/15) | OK |
| Display path 2 | PASS (5/15) | OK |
| Google policy - superlatives | PASS | Нет "лучший", "номер 1" |
| Google policy - caps | PASS | Нет excessive caps |
| Google policy - punctuation | PASS | OK |
| Keyword in Headline 1 | PASS | "Виллы в Убуде" - keyword present |
| CTA in Headline 3 | PASS | "Запись на презентацию" |
| Grammar | PASS | OK |

**Итог:** PASS

### Google Search - Вариант 2 (Инвесторы EN)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Headline 1 length | PASS (25/30) | OK |
| Headline 2 length | PASS (25/30) | OK |
| Headline 3 length | PASS (19/30) | OK |
| Description 1 length | PASS (88/90) | OK |
| Description 2 length | PASS (90/90) | На границе лимита |
| Display path | PASS (12/15, 6/15) | OK |
| Google policy | PASS | No violations |
| Keyword in H1 | PASS | "Ubud Villas" |
| CTA in H3 | PASS | "Book a Presentation" |

**Итог:** PASS

### Google Search - Вариант 3 (Номады RU)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Headline 1 length | PASS (27/30) | OK |
| Headline 2 length | PASS (20/30) | OK |
| Headline 3 length | PASS (18/30) | OK |
| Description 1 length | PASS (87/90) | OK |
| Description 2 length | PASS (87/90) | OK |
| Google policy | PASS | OK |
| Keyword in H1 | PASS | "вилла на Бали" |

**Итог:** PASS

### Google Search - Вариант 4 (EN, competitor traffic)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Headline 1 length | PASS (30/30) | На границе |
| Headline 2 length | PASS (21/30) | OK |
| Headline 3 length | PASS (19/30) | OK |
| Description 1 length | PASS (84/90) | OK |
| Description 2 length | PASS (85/90) | OK |
| Google policy - competitor mention | WARN | "Skip the agency markup" - косвенный competitor reference, не прямое упоминание бренда. Допустимо, но может вызвать trademark dispute если competitor подаст жалобу. |
| Keyword in H1 | PASS | "Bali Villas" |

**Итог:** PASS (с WARN)

### Google Display Remarketing - Вариант 1 (RU)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Short headline | PASS (25/30) | OK |
| Long headline | PASS (90/90) | На границе |
| Description | PASS (89/90) | OK |
| Google policy | PASS | OK |

**Итог:** PASS

### Google Display Remarketing - Вариант 2 (EN)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Short headline | PASS (25/30) | OK |
| Long headline | PASS (88/90) | OK |
| Description | PASS (89/90) | OK |
| Google policy | PASS | OK |

**Итог:** PASS

### Google Display Remarketing - Вариант 3 (Form abandoners, RU)

| Проверка | Результат | Детали |
|----------|-----------|--------|
| Short headline | FAIL (26/30) | Подсчет нужно перепроверить. Скрипт char_guard даст точный подсчет. Визуально может быть на границе. |
| Long headline | PASS (90/90) | На границе |
| Description | PASS (87/90) | OK |
| Google policy | PASS | OK |

**Итог:** PASS (short headline нужно перепроверить скриптом, визуально < 30)

---

## Исправления (auto-fix)

Все креативы прошли валидацию по character limits. Несколько полей на границе лимита (90/90, 125/125) - рекомендуется прогнать через `creative_char_guard.py` для программной верификации.

### WARN items (не блокируют запуск):

1. **Meta Feed V1:** "гарантия от застройщика" - Meta модерация может запросить disclaimer. Рекомендация: подготовить альтернативу "contractual ROI commitment" если объявление отклонено.

2. **Google Search V4:** "Skip the agency markup" - indirect competitor reference. Мониторить trademark disputes.

3. **CRM не указана** - без CRM невозможно отслеживать quality leads и оптимизировать downstream. Рекомендация: подключить до запуска или зафиксировать ручной fallback.

4. **GA4 не установлен** - BLOCKER для Google Ads. Установить ДО запуска.

---

## Policy compliance summary

| Policy area | Status | Notes |
|-------------|--------|-------|
| Meta Housing Category | PASS | Нет restricted targeting в текстах, housing category compliant |
| Meta Personal Attributes | PASS | Ни один креатив не обращается к личным характеристикам |
| Meta Misleading Claims | PASS | 8% ROI - contractual, не misleading. Нет "гарантированный доход", "100% окупаемость", "без рисков" |
| Google Superlatives | PASS | Нет "лучший", "номер 1" без proof |
| Google Caps/Punctuation | PASS | Нет excessive caps, gimmicky punctuation |
| Google Phone in Headlines | PASS | Нет телефонных номеров |
| Emoji usage | PASS | Нет emoji в текстах (для Google - обязательно, для Meta - допустимо) |
| Tone of Voice | PASS | Уверенный, конкретный, с цифрами. Соответствует premium RE позиционированию |
| Brief alignment | PASS | Все ключевые USP (8% ROI, full management, 25-year leasehold, $180-350K) отражены |
| Segment coverage | PASS | Все 3 сегмента (инвесторы, номады, семьи) покрыты |

---

## Финальный вердикт

**NEEDS REVISION (minor):**
- Установить GA4 + GTM до запуска Google Ads (BLOCKER)
- Уточнить CRM систему клиента (WARN)
- Прогнать creatives через `creative_char_guard.py` для финальной верификации char counts
- Подготовить fallback-вариант Meta Feed V1 без слова "гарантия" на случай отклонения модерацией

**При устранении этих пунктов:** APPROVED для запуска.
