# Targeting Plan: ЖК Горизонт (VK Ads)

## 1. Objective & Conversion Setup

- **Business goal:** Генерация квалифицированных лидов на просмотр квартир [Strategy]
- **Platform:** VK Ads (рынок РФ, Meta недоступна) [Strategy - гео РФ]
- **VK objective:** Целевые действия - лиды через лидформу и переход на сайт [KB: Voronin VK course, урок 1 - целевые действия vs охват]
- **Conversion location:** VK Lead Forms (primary) + Landing page gorizont-dev.ru (secondary) [Strategy]
- **Primary optimization event:** Заявка (лид) [Strategy]
- **Tracking status:** Требует настройки - пиксель VK на сайт + интеграция лидформ с CRM [Assumption]
- **Key measurement gaps:**
  - Пиксель VK на лендинге: нужно установить [Assumption]
  - CRM-интеграция для оценки качества лидов [Strategy - офлайн-конверсии]
  - Квалификация лидов: требуется обратная связь от отдела продаж [Assumption]

## 2. ICP & Segments

### Segment 1: Молодые семьи-переезжающие
- **Who:** Семьи 25-40 лет, переезд из регионов в Краснодар [Strategy]
- **Trigger:** Одобрение ипотеки, переезд по работе, рождение ребенка [Strategy]
- **Pain:** Незнание района, страх ошибиться с застройщиком, безопасность детей [Strategy]
- **Offer angle:** "Закрытый двор + подземный паркинг + своя УК = 3 вещи, которых нет у соседних ЖК" [Strategy - позиционирование]
- **Funnel temperature:** Cold -> Warm (через прогрев контентом)

### Segment 2: Инвесторы в арендный бизнес
- **Who:** 30-55 лет, капитал 3-5 млн, ищут пассивный доход [Strategy]
- **Trigger:** Снижение ставок депозитов, рост арендных цен в Краснодаре [Strategy]
- **Pain:** Непонятная доходность, управление арендой [Strategy]
- **Offer angle:** "Студия 25 м2 за 3.2 млн: расчет арендной доходности на реальных цифрах" [Strategy]
- **Funnel temperature:** Cold (awareness) -> Warm (расчет ROI)

### Segment 3: Местные улучшатели
- **Who:** Краснодарцы 28-45, живут во вторичке, хотят новостройку [Strategy]
- **Trigger:** Продажа текущей квартиры, одобрение ипотеки [Strategy]
- **Pain:** Нет парковки, шум, старый фонд [Strategy]
- **Offer angle:** "Из вторички в новостройку с подземным паркингом" [Strategy]
- **Funnel temperature:** Warm (уже в поиске)

## 3. Audience Matrix

| Audience | Type | Source | Funnel stage | Hypothesis | Priority |
|----------|------|--------|--------------|------------|----------|
| Гео Краснодар + интересы "недвижимость" | Cold | VK Interests | Cold | Широкий охват потенциальных покупателей | High |
| Ключевые слова "купить квартиру Краснодар" | Cold | VK Keywords | Cold | Intent-based таргетинг через ключевые слова [KB: Voronin VK course, урок 1 - таргет по ключевым словам] | High |
| Подписчики сообществ конкурентов | Cold | VK Communities | Cold | Уже интересуются новостройками в Краснодаре [KB: Voronin VK course - таргет на подписчиков сообществ] | Medium |
| Пиксель VK - посетители сайта 30d | Warm | VK Pixel | Warm | Ретаргетинг на заинтересованных [KB: Voronin VK course - ретаргетинг через пиксель] | High |
| Engagers VK сообщества Горизонт | Warm | VK Community | Warm | Уже взаимодействовали с контентом | Medium |
| Родители + гео Краснодар | Cold | VK Interests | Cold | Сегмент "молодые семьи" [KB: Voronin VK course - таргет на родителей] | Medium |

## 4. Campaign Logic

### Campaign 1: Cold acquisition - лидформа (семьи)
- **Goal:** Тестировать angle "безопасность + инфраструктура" для семей-переезжающих [Strategy - Сегмент 1]
- **Ad sets:**
  - AS1: Ключевые слова "новостройки Краснодар", "квартира Прикубанский" [KB: Voronin - ключевые слова]
  - AS2: Интересы "недвижимость" + гео Краснодар + возраст 25-40 [Assumption]
  - AS3: Подписчики сообществ ЮгСтройИмпериал, СпецСтрой, ВКБ [Strategy - конкуренты]
- **Placements:** VK Feed (primary), Одноклассники (secondary) [KB: Voronin VK course - реклама показывается на проектах Mail Group]
- **Budget split:** 50% бюджета VK = 45,000 руб/мес (1,500 руб/день) [Strategy hard cap 90,000]
- **Creative requirement:** Hook с конкретикой про закрытый двор + подземный паркинг, разные angles [Strategy]

### Campaign 2: Cold acquisition - лидформа (инвесторы)
- **Goal:** Тестировать ROI-angle для инвесторов [Strategy - Сегмент 2]
- **Ad sets:**
  - AS1: Ключевые слова "инвестиции недвижимость Краснодар" [Assumption]
  - AS2: Интересы "инвестиции", "бизнес", "финансы" + гео Краснодар [Assumption]
- **Budget split:** 25% бюджета VK = 22,500 руб/мес (750 руб/день) [Strategy]
- **Creative requirement:** Расчет доходности, конкретные цифры [Strategy]

### Campaign 3: Retargeting
- **Audience windows:** Пиксель 7d, 14d, 30d + engagers VK community [KB: Voronin VK course - ретаргетинг]
- **Message shift:** Social proof (отзывы, ход стройки), urgency (осталось N квартир), CTA (запишитесь на экскурсию) [KB: Cialdini - Social Proof + Scarcity]
- **Budget split:** 15% бюджета VK = 13,500 руб/мес (450 руб/день) [Assumption]

### Campaign 4: Smart-кампания (тест)
- **Goal:** Дать алгоритму VK возможность найти оптимальную аудиторию [KB: Voronin VK course, урок 1 - смарт-кампания]
- **Budget split:** 10% бюджета VK = 9,000 руб/мес (300 руб/день) [Assumption]

## 5. Experiment Plan

| Test | Variable | Hypothesis | Success metric | Minimum run | Next action |
|------|----------|------------|----------------|-------------|------------|
| T1 | Audience: ключевые слова vs интересы | Ключевые слова дадут более горячие лиды | Cost per qualified lead | 7 дней, 50+ лидов | Scale winner, pause loser |
| T2 | Offer angle: безопасность vs инвестиции | Семейный angle даст больший объем | CPL + qualified rate | 7 дней | Перераспределить бюджет |
| T3 | Creative format: карусель vs одно изображение | Карусель покажет USP полнее | CTR + CPL | 5 дней | Scale format winner |
| T4 | Лидформа vs лендинг | Лидформа дешевле, лендинг качественнее | CPL + qualified rate | 7 дней | Оптимальный split |

## 6. Optimization Rules

- **If CPM high:** Расширить аудиторию или сменить плейсменты [Assumption - VK standard practice]
- **If CTR low (<0.5%):** Менять креатив, тестировать новые hooks [KB: Voronin VK course - тестирование объявлений]
- **If CPL ok but quality weak:** Добавить квалифицирующие вопросы в лидформу, сузить аудиторию [KB: Voronin VK course - лидформы]
- **If lead-to-contact weak:** Проверить speed-to-lead, настроить автоответ в CRM [Strategy - speed-to-lead < 15 мин]
- **If frequency too high (>5):** Обновить креативы, расширить аудиторию [Assumption]

## 7. Risks & Dependencies

- **Tracking risk:** Пиксель VK должен быть установлен до запуска [Assumption]
- **Sales process risk:** Скорость обработки лидов критична для конверсии [Strategy]
- **Creative dependency:** Нужны минимум 3 варианта креативов на запуск [Strategy]
- **Лидформа:** Нужна ссылка на политику конфиденциальности + 152-ФЗ [Platform docs: VK Ads policy]
- **CRM:** Без CRM-интеграции невозможна оценка качества лидов [Strategy]

## 8. Organic Support Layer

- **Need:** Yes - VK Community необходимо для прогрева и ретаргетинга [Strategy - 30,000 руб/мес SMM budget]
- **Primary owned channel:** VK Community [Strategy]
- **Role in funnel:** Trust-building, FAQ, social proof, warm-up для ретаргетинга [Strategy]
- **Required rubrics:**
  - Ход стройки (еженедельно) - снижает anxiety [KB: JTBD - Anxiety force]
  - Q&A по покупке / ипотеке - снимает objections [KB: Cialdini - Authority]
  - Обзоры планировок - продуктовый контент [Assumption]
  - Кейсы / отзывы покупателей - social proof [KB: Cialdini - Social Proof]
  - Инфраструктура района - для переезжающих [Strategy - Сегмент 1]
- **Paid sync:** Посты с ходом стройки и кейсами продвигать через paid для ретаргетинга [Assumption]
- **Community ops:** Response SLA <= 15 мин в рабочее время, pinned post с описанием ЖК и CTA [Assumption]

## 9. 14-Day Action Plan

| Day range | Action | Owner | Expected signal |
|-----------|--------|-------|-----------------|
| 1-2 | Установить пиксель VK, создать лидформу, настроить CRM | Targeting + Dev | Tracking ready |
| 3-4 | Запуск Campaign 1 (семьи) + Campaign 4 (smart) | Targeting | Первые показы, CTR |
| 5-7 | Запуск Campaign 2 (инвесторы) + Campaign 3 (retargeting) | Targeting | CPL baseline |
| 8-10 | Первый анализ CPL + quality, отключить слабые ad sets | Targeting | Remove losers |
| 11-14 | Перераспределить бюджет на winners, запросить sales feedback | Targeting + Sales | Stabilize CPL < 2500 |

## 10. Budget Compliance

- **Channel hard cap:** 90,000 руб/мес [Strategy]
- **Planned spend:** 90,000 руб/мес (45,000 + 22,500 + 13,500 + 9,000) [Plan]
- **Delta vs cap:** 0
- **Status:** PASS
