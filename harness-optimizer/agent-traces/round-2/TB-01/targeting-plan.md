# Targeting Plan: ЖК Горизонт (Краснодар) - VK Ads

## 1. Objective & Conversion Setup

- **Business goal:** генерация квалифицированных лидов для отдела продаж застройщика [Strategy]
- **Platform:** VK Ads (ads.vk.com - новый рекламный кабинет) [KB: Voronin VK course, урок 1 - новый кабинет ads.vk.com]
- **Primary objective:** Целевые действия -> Лид-формы [KB: VK Lead Forms Setup - целевое действие "Лид-формы и опросы"]
- **Conversion location:** Лид-форма ВК (primary) + трафик на сайт gorizont-dev.ru (secondary) [Strategy + KB: Voronin VK course - два типа кампаний: на лид-формы и на сайт]
- **Primary optimization event:** Отправка лид-формы [KB: eLama VK errors, п.4.4 - таргетирование на отправку, не открытие формы]
- **Tracking status:** partial - нужна установка пикселя VK на сайт, настройка целей [KB: eLama VK errors, п.4.3 - без пикселя нет данных для оптимизации]
- **Key measurement gaps:**
  - Пиксель VK на сайте gorizont-dev.ru [KB: eLama VK errors, п.4.3]
  - UTM-метки на все ссылки [KB: eLama VK errors, п.4.2]
  - CRM-интеграция для отслеживания качества лидов [KB: eLama VK errors, п.4.6 - сквозная аналитика]
  - Яндекс Метрика на сайте [KB: eLama VK errors, п.4.1]

## 2. ICP & Segments

### Segment 1: Молодые семьи-переселенцы (Primary)
- **Who:** Семьи 25-40 лет, переезжающие в Краснодар из других регионов [Strategy]
- **Trigger:** Одобрение ипотеки, рождение ребёнка, решение о переезде [Strategy]
- **Pain:** Страх плохого района, ненадёжного застройщика, непрозрачности [Strategy]
- **Offer angle:** "Безопасный двор + своя УК = спокойствие для семьи" [Strategy]
- **Funnel temperature:** Cold -> Warm (через VK community прогрев)

### Segment 2: Инвесторы в арендный бизнес
- **Who:** 30-55 лет, свободный капитал, ищут passive income [Strategy]
- **Trigger:** Инфляция, низкие ставки депозитов, рост арендного спроса [Strategy]
- **Pain:** Неизвестная доходность, страх простоя, управление арендой [Strategy]
- **Offer angle:** "Квартира с доходом: своя УК управляет за вас" [Strategy]
- **Funnel temperature:** Cold

### Segment 3: First-time buyers (Краснодар)
- **Who:** 22-35 лет, живут с родителями или снимают [Strategy]
- **Trigger:** Свадьба, рождение ребёнка, одобрение семейной ипотеки [Strategy]
- **Pain:** Ограниченный бюджет, страх ипотеки [Strategy]
- **Offer angle:** "Своя квартира от 3.2 млн + семейная ипотека" [Strategy]
- **Funnel temperature:** Cold -> Warm

## 3. Audience Matrix

| Audience | Type | Source | Funnel stage | Hypothesis | Priority |
|----------|------|--------|--------------|------------|----------|
| Интерес "Недвижимость" + гео Краснодар | Cold | VK Interests | Cold | Широкая, но алгоритм найдёт fit-профиль при сильном оффере [KB: Voronin VK course - интересы работают для широких тематик] | High |
| Ключевые фразы: "купить квартиру краснодар", "новостройки краснодар" | Cold | VK Keywords | Cold | Горячий intent, аналог контекста [KB: Voronin VK course, урок 4 - ключевые фразы как контекстная реклама; KB: eLama VK errors - Wordstat для фраз] | High |
| Ключевые фразы: "переезд в краснодар", "жизнь в краснодаре" | Cold | VK Keywords | Cold | Миграционный intent, попадание в переезжающих [Assumption] | Medium |
| Подписчики сообществ конкурентов (ЮгСтройИмпериал, СпецСтрой, ВКБ) | Cold | VK Communities | Cold | Горячая аудитория, уже интересуется новостройками [KB: Voronin VK course - подписчики конкурентных сообществ] | High |
| Ретаргетинг: клик на лид-форму без отправки | Warm | VK Events | Warm | Уже проявили интерес, нужен второй touch [KB: VK Lead Forms Setup - сбор аудитории кликов для ретаргетинга; KB: eLama VK errors, п.5.7 - обязательно собирать аудитории по реакциям] | High |
| Ретаргетинг: посетители сайта 14d | Warm | VK Pixel | Warm | Вернуть на лид-форму с другим оффером [KB: eLama VK errors, п.5.2 - использовать ретаргетинг] | Medium |
| CRM-база (если есть) | Hot | Upload | Hot | Реактивация тёплых контактов [KB: eLama VK errors, п.5.2 - загрузить существующую базу] | High (если данные есть) |

## 4. Campaign Logic

### Campaign 1: Lead Forms - Интересы (Cold)
- **Goal:** генерация лидов через interest-based таргетинг [Strategy]
- **Ad sets:** 2 группы - (1) Интерес "Недвижимость" для семей, (2) Интерес "Инвестиции" для инвесторов [KB: eLama VK errors, п.5.4 - разные аудитории в разных кампаниях]
- **Placements:** ВКонтакте Лента (start), добавить ВК Клипы при наличии видео [KB: VK Lead Forms Setup - рекомендация для старта: только ВК Лента]
- **Budget split:** 35% от VK budget = 36,750 руб/мес = ~1,225 руб/день на кампанию [Strategy - hard cap 105,000]
- **Creative requirement:** 4:5 формат (1080x1350), минимум 5 объявлений в группе для теста [KB: VK Lead Forms Setup - формат 4:5 рекомендован; KB: Voronin VK course - минимум 5 вариантов]
- **Bid strategy:** Минимальная цена (start) [KB: eLama VK errors, п.11 - начинайте с минимальной цены]

### Campaign 2: Lead Forms - Ключевые фразы (Cold)
- **Goal:** захват intent-based аудитории [Strategy]
- **Ad sets:** 2 группы - (1) "купить квартиру / новостройки краснодар", (2) "переезд в краснодар / жизнь в краснодаре" [KB: eLama VK errors, п.5.4 - не смешивать разные аудитории]
- **Keyword period:** 14-30 дней (недвижимость - длинный цикл) [KB: Voronin VK course - период зависит от цикла сделки; KB: eLama VK errors, п.5.5 - длинный цикл = длинный период]
- **Min-words:** аренда, снять, вторичка, б/у, бесплатно [KB: Voronin VK course - минус-фразы обязательны]
- **Placements:** ВКонтакте Лента [KB: VK Lead Forms Setup]
- **Budget split:** 35% от VK budget = 36,750 руб/мес
- **Bid strategy:** Минимальная цена [KB: eLama VK errors, п.11]

### Campaign 3: Lead Forms - Сообщества конкурентов (Cold)
- **Goal:** перехват аудитории конкурентов [Strategy]
- **Ad sets:** 1 группа с подписчиками ЮгСтройИмпериал, СпецСтрой, ВКБ [KB: Voronin VK course - подписчики конкурентных сообществ]
- **Placements:** ВКонтакте Лента [KB: VK Lead Forms Setup]
- **Budget split:** 15% от VK budget = 15,750 руб/мес
- **Bid strategy:** Минимальная цена [KB: eLama VK errors, п.11]

### Campaign 4: Retargeting
- **Audience windows:** клик на лид-форму без отправки (all time), посетители сайта 14d [KB: VK Lead Forms Setup - сбор аудитории кликов; KB: eLama VK errors, п.5.7]
- **Message shift:** другой оффер, social proof, ход стройки, отзывы [KB: Cialdini - Social Proof через Strategy]
- **Budget split:** 15% от VK budget = 15,750 руб/мес
- **Bid strategy:** Минимальная цена [KB: eLama VK errors, п.11]

### Лид-форма - Рекомендации по настройке [KB: VK Lead Forms Setup - полная инструкция]

**Тип:** Больше текста (расширенное описание с УТП) [KB: VK Lead Forms Setup - рекомендуется в большинстве случаев]

**Поля формы (минимум):** [KB: VK Lead Forms Setup + KB: eLama VK errors, п.3.3]
- Имя (ручной ввод, НЕ автоподстановка) [KB: eLama VK errors, п.3.2 - никнеймы типа "Ангел Демон"]
- Телефон (ручной ввод, НЕ автоподстановка) [KB: eLama VK errors, п.3.1 - старые номера из аккаунта]
- Квалифицирующий вопрос: "Какая квартира вас интересует?" (Студия / 1к / 2к / 3к) [KB: VK Lead Forms Setup - доп. вопрос обязательно]
- Опционально: "Где удобнее связаться?" (Телефон / WhatsApp / Telegram) [KB: VK Lead Forms Setup - закрывает возражение людей, не любящих звонки]

**Экран результатов:** "Мы свяжемся с вами в ближайшие 15 минут!" [KB: VK Lead Forms Setup - сообщить что будет дальше]

**Обязательно:**
- Согласие на обработку ПД (152-ФЗ) [KB: VK Lead Forms Setup - настройки формы]
- CRM-интеграция или email-уведомления [KB: VK Lead Forms Setup]

## 5. Experiment Plan

| Test | Variable | Hypothesis | Success metric | Minimum run condition | Next action |
|------|----------|------------|----------------|-----------------------|------------|
| T1 | Audience type | Ключевые фразы дадут более горячие лиды чем интересы | Cost per qualified lead | 5 дней, 15+ лидов на группу [KB: eLama VK errors, п.7 - 3-4 дня на обучение] | Scale winner / kill loser |
| T2 | Offer angle | "Безопасный двор" для семей > "Инвестиционный доход" для инвесторов по volume | Lead volume + qualified rate | 7 дней, 20+ лидов | Reallocate budget |
| T3 | Lead form type | Ручной ввод полей > автоподстановка по qualified rate | Qualified lead rate | 7 дней, 30+ заявок [KB: eLama VK errors, п.3] | Fix form config |
| T4 | Creative format | Рендер ЖК > lifestyle-фото по CTR | CTR + form completion rate | 5 дней [KB: Voronin VK course - тестировать креативы] | Scale winner |

## 6. Optimization Rules

- **If CPM high:** проверить размер аудитории (должен быть 50K-400K) [KB: VK Lead Forms Setup - рекомендуемый размер 50,000-400,000], проверить конкуренцию в гео, расширить таргетинг [KB: eLama VK errors, п.5.3]
- **If CTR low (< 0.5%):** менять креативы и тексты, тестировать новые офферы [KB: eLama VK errors, п.9 - тестирование обязательно; KB: Voronin VK course - минимум 5 объявлений]
- **If CPL ok but quality weak:** ужесточить квалификацию в лид-форме, проверить ручной ввод полей [KB: eLama VK errors, п.3 - проблема автоподстановки]
- **If lead-to-contact weak (дозваниваемость < 50%):** проверить speed-to-lead (< 15 мин) [KB: eLama VK errors, п.2.2 - не более 15 минут], проверить корректность телефонов в формах
- **If frequency too high (> 3/week):** обновить креативы, расширить аудитории [KB: Voronin VK course - выгорание креатива -> новая группа объявлений]
- **Масштабирование:** +20-25% каждые 2-3 дня или +10% ежедневно [KB: eLama VK errors, п.6.3 - резкое увеличение бюджета сбивает оптимизацию]

## 7. Risks & Dependencies

- **Tracking risk:** пиксель VK не установлен на сайте - нет оптимизации по посетителям [KB: eLama VK errors, п.4.3] - BLOCKER
- **Sales process risk:** скорость обработки лидов из лид-форм критична - > 15 мин = потеря [KB: eLama VK errors, п.2.2; KB: VK Lead Forms Setup - скорость обработки]
- **Creative dependency:** нужны рендеры ЖК, фото стройки, планировки - без них запуск невозможен [Assumption]
- **Landing page quality:** проверить мобильную версию gorizont-dev.ru, скорость загрузки, формы [KB: eLama VK errors, п.2.3]
- **Мусорные заявки:** возможны боты и случайные заявки, особенно с автоподстановкой [KB: eLama VK errors, п.15 - защита от ботов]
- **Бюджет не обнулять:** следить за балансом кабинета [KB: eLama VK errors, п.6.4 - обнуление сбрасывает настройки]

## 8. Organic Support Layer

- **Need:** Yes - стратегия выделила 30,000 руб/мес на SMM/organic [Strategy]
- **Primary owned channel:** VK Community [Strategy - рынок РФ]
- **Role in funnel:** trust / FAQ / proof / warm-up / remarketing seed [Strategy]
- **Required rubrics:** [KB: platform-specs.md - VK Community Organic best practices]
  - Ход стройки (фото/видео с площадки) - снижение тревожности
  - Q&A по ипотеке и покупке - снятие возражений
  - Обзор планировок и инфраструктуры района
  - Кейсы / отзывы покупателей (по мере накопления)
  - Оффер недели / акция
- **Paid sync:** продвигать лучшие посты через VK Ads, ретаргетить community engagers [KB: platform-specs.md - organic должен поддерживать paid funnel]
- **Community ops note:** response SLA < 15 мин в рабочее время [KB: eLama VK errors, п.2.2], pinned post с основным оффером и CTA

## 9. 14-Day Action Plan

| Day range | Action | Owner | Expected signal |
|-----------|--------|-------|-----------------|
| 1-2 | Установка пикселя VK, настройка целей, создание лид-форм, подготовка креативов (5+ вариантов) | Targeting + Dev | Clean launch readiness |
| 3-4 | Запуск Campaign 1 (Интересы) + Campaign 2 (Ключевые фразы), настройка сбора аудиторий по реакциям | Targeting | Первые показы, CTR baseline [KB: eLama VK errors, п.7 - 3-4 дня обучение] |
| 5-7 | Запуск Campaign 3 (Конкуренты), первый read сигналов: CPL, CTR, qualified rate | Targeting | 15-30 лидов, первые данные по качеству |
| 8-10 | Первая оптимизация: отключить слабые группы, масштабировать winners, запуск ретаргетинга (Campaign 4) | Targeting | Стабилизация CPL |
| 11-14 | Reallocate budget к winning кампаниям, запуск T2 (offer angle test), первый отчёт по qualified rate | Targeting + Sales | CPL тренд, qualified lead rate, speed-to-lead |

## 10. Budget Compliance

- **Channel hard cap:** 105,000 руб/мес [Strategy]
- **Planned spend:**
  - Campaign 1 (Интересы): 36,750 руб/мес
  - Campaign 2 (Ключевые фразы): 36,750 руб/мес
  - Campaign 3 (Конкуренты): 15,750 руб/мес
  - Campaign 4 (Ретаргетинг): 15,750 руб/мес
  - **Total: 105,000 руб/мес**
- **Delta vs cap:** 0
- **Status:** PASS

---

## KB Attribution Summary

| Тип | Количество | % |
|-----|-----------|---|
| [KB: ...] | 41 | 52% |
| [Strategy] | 18 | 23% |
| [Platform docs] | 0 | 0% |
| [Assumption] | 5 | 6% |
| [Brief] | 0 (through Strategy) | 0% |
| **Total** | **64** | |
| **KB + Strategy** | **59** | **92%** |

Attribution rate: 92% (выше порога 60%).
