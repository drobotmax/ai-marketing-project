# Targeting Plan: ЖК Горизонт (VK Ads + Community)

## 1. Objective & Conversion Setup

- **Business goal:** генерация квалифицированных лидов на покупку квартир в ЖК Горизонт
- **VK objective:** Целевые действия - Лидформы + Сайт
- **Conversion location:** VK Лид-форма (primary) + Landing page gorizont-dev.ru (secondary)
- **Primary optimization event:** отправка лид-формы / заявка на сайте
- **Tracking status:** partial (assumption) - требуется установка VK Pixel на сайт
- **Key measurement gaps:**
  - VK Pixel на сайте: уточнить статус
  - CRM интеграция с VK Lead Ads: уточнить
  - Offline conversion feedback: не настроен

## 2. ICP & Segments

### Segment 1: Молодые семьи-переезжанцы
- **Who:** 25-40, семьи с детьми, переезд в Краснодар из регионов
- **Trigger:** одобрение ипотеки, решение о переезде, рождение ребенка
- **Pain:** страх недостроя, незнакомый город, непонятная ипотека
- **Offer angle:** "Новый дом для семьи в Краснодаре - закрытый двор, своя УК, от 3.2 млн"
- **Funnel temperature:** cold -> warm через контент

### Segment 2: Инвесторы в аренду
- **Who:** 30-55, имеют жилье, ищут объект для вложений
- **Trigger:** накопления, рост арендных ставок, желание пассивного дохода
- **Pain:** неуверенность в доходности, не хочет управлять сам
- **Offer angle:** "Студия от 3.2 млн - собственная УК берет аренду на себя"
- **Funnel temperature:** cold

### Segment 3: Местные улучшители
- **Who:** 30-45, живут в Краснодаре, хотят из вторички в новостройку
- **Trigger:** рождение ребенка, рост семьи, износ текущего жилья
- **Pain:** нужно продать текущее, привязка к району
- **Offer angle:** "Новая квартира в Прикубанском - паркинг и закрытый двор в каждом корпусе"
- **Funnel temperature:** warm (уже знают рынок)

## 3. Audience Matrix

| Audience | Type | Source | Funnel stage | Hypothesis | Priority |
|----------|------|--------|--------------|------------|----------|
| Интересы: Недвижимость + Ипотека, Гео: Краснодар + регионы-доноры | Cold | VK interests | Cold | Захват intent через платформенные сигналы | High |
| Ключевые слова: "купить квартиру краснодар", "новостройки краснодар", "жк краснодар" | Cold | VK keyword targeting | Cold | Поисковый intent внутри VK экосистемы | High |
| Подписчики сообществ конкурентов: ЮгСтройИмпериал, СпецСтрой, ВКБ-Новостройки | Cold | VK community targeting | Cold | Уже интересуются новостройками в городе | Medium |
| Lookalike от лидов (после сбора 100+ лидов) | Cold | VK LAL | Cold | Профиль похож на конвертированных | Medium |
| VK Pixel - посетители сайта 30d | Warm | VK Pixel retargeting | Warm | Были на сайте, не оставили заявку | High |
| VK Community engagers 30d | Warm | VK engagement | Warm | Взаимодействовали с контентом | Medium |
| Lead form openers non-submit | Warm | VK lead form | Warm | Начали заполнять, бросили | High |

## 4. Campaign Logic

### Campaign 1: Cold - Лид-формы (Семьи + Улучшители)
- **Goal:** генерация лидов через VK Lead Forms
- **Ad sets:**
  - AS1: Интересы Недвижимость + Ипотека, Гео Краснодар + регионы (Новосибирск, Екатеринбург, Красноярск, Тюмень)
  - AS2: Ключевые слова "купить квартиру краснодар", "новостройки краснодар"
  - AS3: Подписчики сообществ конкурентов
- **Placements:** лента VK, Одноклассники, рекламная сеть
- **Budget split:** 50% от VK таргет hard cap = 30,000 руб/мес (1,000 руб/день)
- **Creative requirement:** lifestyle + семья, планировки + цена, рендер ЖК
- **Lead form:**
  - Поля: Имя (авто), Телефон (авто), "Какая квартира интересует?" (студия / 1-к / 2-к / 3-к)
  - Privacy policy: обязательная ссылка + чекбокс согласия 152-ФЗ
  - Thank you page: "Наш менеджер свяжется с вами в течение 30 минут"

### Campaign 2: Cold - Инвесторы
- **Goal:** привлечение инвестиционных лидов
- **Ad sets:**
  - AS1: Интересы Инвестиции + Недвижимость, возраст 30-55, доход выше среднего
  - AS2: Ключевые слова "инвестиции в недвижимость", "квартира под аренду краснодар"
- **Placements:** лента VK
- **Budget split:** 25% = 15,000 руб/мес (500 руб/день)
- **Creative requirement:** цифры доходности, УК как аргумент, компактные форматы

### Campaign 3: Retargeting
- **Audience windows:** посетители сайта 14d, lead form openers 7d, community engagers 14d
- **Message shift:** social proof (отзывы, ход стройки), срочность (рост цен), конкретный оффер (планировка + цена)
- **Budget split:** 25% = 15,000 руб/мес (500 руб/день)

## 5. Experiment Plan

| Test | Variable | Hypothesis | Success metric | Minimum run condition | Next action |
|------|----------|------------|----------------|-----------------------|------------|
| T1 | Audience: Interests vs Keywords | Keywords дадут более горячие лиды | Cost per qualified lead | 7 дней, мин. 20 лидов на группу | Scale winner |
| T2 | Offer angle: Семья vs Инвестиция | Семейный angle дешевле по CPL | CPL + qualified rate | 7 дней, мин. 15 лидов | Scale winner, keep both if both work |
| T3 | Format: Lead form vs Site traffic | Lead form дешевле, site - качественнее | CPL + qualified rate | 14 дней | Определить основной формат |
| T4 | Creative: Lifestyle vs Планировка vs Рендер | Планировка конвертит горячее | Form completion rate | 7 дней, мин. 1000 показов на вариант | Scale winner |

## 6. Optimization Rules

- **If CPM high (> 300 руб):** расширить гео или интересы, проверить частоту показов
- **If CTR low (< 0.5%):** пересмотреть креативы, протестировать новые hooks, проверить релевантность аудитории
- **If CPL ok but quality weak (qualified rate < 30%):** добавить квалифицирующий вопрос в лид-форму, сузить аудиторию, тестировать site traffic вместо lead forms
- **If lead-to-contact weak (дозвон < 50%):** проверить скорость обработки лидов, уменьшить volume пока sales не наладит процесс
- **If frequency > 3:** обновить креативы, расширить аудиторию, исключить уже сконвертированных

## 7. Risks & Dependencies

- **Tracking risk:** VK Pixel может быть не установлен - блокирует ретаргетинг и оптимизацию
- **Sales process risk:** скорость обработки лидов критична для VK lead forms (лиды остывают за 2-4 часа)
- **Creative dependency:** нужны качественные рендеры, планировки, фото хода стройки от застройщика
- **CRM integration:** без CRM нет feedback loop - договориться о ручной выгрузке статусов минимум 2 раза в неделю
- **Конкуренты в VK:** ЮгСтройИмпериал активен, может быть высокий CPM в аукционе

## 8. Organic Support Layer

- **Need:** yes - VK Community обязателен как trust-building layer для paid funnel
- **Primary owned channel:** VK Community (группа ЖК Горизонт)
- **Role in funnel:** доверие, FAQ, social proof, warm-up для ретаргетинга
- **Required rubrics:**
  - Ход стройки (еженедельно) - снижает тревожность
  - Q&A по покупке и ипотеке - снимает objections
  - Обзоры планировок - помогает с выбором
  - Район и инфраструктура - для переезжающих
  - Отзывы / кейсы - social proof
- **Paid sync:**
  - Посты "ход стройки" продвигать за 2-3K руб для охвата
  - Community engagers ретаргетить paid ads с конкретным оффером
  - Pinned post: оффер + CTA "написать в сообщения"
- **Community ops note:**
  - Response SLA: < 15 минут в рабочее время
  - Pinned post: главный оффер + ссылка на лид-форму + ссылка на сайт
  - Модерация: ответы на вопросы по ипотеке, срокам, инфраструктуре

## 9. 14-Day Action Plan

| Day range | Action | Owner | Expected signal |
|-----------|--------|-------|-----------------|
| 1-3 | Установка VK Pixel, создание лид-форм, настройка аудиторий, подготовка креативов | Targeting | Готовность к запуску |
| 4-5 | Запуск Campaign 1 (Cold - Семьи) + Campaign 3 (Retargeting) | Targeting | Первые показы и клики |
| 6-7 | Запуск Campaign 2 (Cold - Инвесторы), первый read по CTR и CPM | Targeting | CTR > 0.5%, CPM < 300 руб |
| 8-10 | Первый анализ CPL, качества лидов, первая оптимизация | Targeting | CPL < 2,500 руб |
| 11-14 | Отключение слабых ad sets, перераспределение бюджета на winners | Targeting + Media Planner | Стабилизация CPL < 2,000 руб |

## 10. Budget Compliance

- **Channel hard cap:** 60,000 руб/мес (VK таргет) + 20,000 руб/мес (VK SMM) = 80,000 руб/мес total VK
- **Planned spend (таргет):** 60,000 руб/мес (30,000 + 15,000 + 15,000)
- **Delta vs cap (таргет):** 0
- **Planned spend (SMM):** 20,000 руб/мес (производство контента + продвижение постов)
- **Delta vs cap (SMM):** 0
- **Status:** PASS
