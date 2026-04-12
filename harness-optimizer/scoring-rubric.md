# Scoring Rubric - KUBRIK Harness Optimizer

> Этот файл контролирует ТОЛЬКО человек.
> Агент использует его как инструкцию для LLM-as-judge оценки.

## Инструкция для оценщика

Ты получаешь полный output KUBRIK pipeline (strategy.md, targeting-plan.md,
context-ads-plan.md, media-plan.md, creatives.md, validation.md) и оригинальный бриф.

Оцени каждый критерий от 0 до 5:
- **5** = отлично, профессиональный уровень агентства
- **4** = хорошо, мелкие недочёты
- **3** = удовлетворительно, есть пробелы
- **2** = слабо, серьёзные пробелы
- **1** = плохо, не соответствует задаче
- **0** = отсутствует или полностью неверно

---

## Критерии

### S1: Market Depth (strategist)
**Вопрос:** Стратегия содержит конкретику по рынку или generic advice?
- 5: Конкретные данные по локации, ценовому сегменту, конкурентам, спросу
- 3: Общие наблюдения с парой конкретных фактов
- 1: Шаблонные фразы, применимые к любому рынку
- **Red flag:** "рынок недвижимости растёт" без цифр

### S2: Segment Clarity (strategist)
**Вопрос:** Сегменты описаны через JTBD/pain points или только demographics?
- 5: JTBD + triggers + pain points + решение для каждого сегмента
- 3: Demographics + пара pain points
- 1: Только "мужчины 30-45 с доходом выше среднего"
- **Red flag:** сегменты без triggers и motivations

### S3: Channel Logic (strategist)
**Вопрос:** Выбор каналов обоснован стратегически?
- 5: Каждый канал привязан к сегменту, funnel stage, бюджету
- 3: Каналы перечислены с общим обоснованием
- 1: Просто список каналов без логики
- **Red flag:** Google Ads для России, бюджет <30K на канал

### T1: Audience Architecture (targeting/contextologist)
**Вопрос:** Есть ли cold/warm/hot funnel architecture?
- 5: Чёткая воронка с progression logic, retargeting windows, lookalikes
- 3: Разделение на cold/warm, но без деталей progression
- 1: Flat list аудиторий без funnel logic
- **Red flag:** нет retargeting strategy

### T2: Platform Expertise (targeting/contextologist)
**Вопрос:** Агент использует знания из KB или галлюцинирует?
- 5: Цитирует курсы/книги, использует platform-specific best practices
- 3: Правильные рекомендации, но без attribution
- 1: Общие советы, не учитывающие специфику платформы
- **Red flag:** OZK рекомендуется для первого месяца, нет ссылок на KB

### T3: Test Design (targeting/contextologist)
**Вопрос:** Эксперименты hypothesis-driven и measurable?
- 5: Гипотеза + переменная + метрика + duration + stopping rules
- 3: Есть что тестировать, но нет чётких метрик
- 1: "Будем тестировать разные аудитории"
- **Red flag:** нет success criteria

### M1: Budget Coherence (media-buyer)
**Вопрос:** Бюджет сходится, min thresholds соблюдены?
- 5: Суммы точно = brief budget, каждый канал >= 30K, unit economics
- 3: Суммы примерно сходятся, есть мелкие расхождения
- 1: Бюджет превышен или каналы underfunded
- **Red flag:** канал с <30K/мес, сумма != brief

### M2: Cross-Channel Logic (media-buyer)
**Вопрос:** Нет конфликтов между каналами, sequencing логичен?
- 5: Launch calendar, channel dependencies, scaling rules
- 3: Каналы не конфликтуют, но sequencing не обоснован
- 1: Все каналы "запустить одновременно" без логики
- **Red flag:** contradictions с targeting/context plans

### C1: Hook Strength (copywriter)
**Вопрос:** Первая строка останавливает скролл?
- 5: Конкретный hook с цифрой/вопросом/провокацией, разный для каждого сегмента
- 3: Неплохой hook, но generic
- 1: "Мечтаете о квартире?" шаблон
- **Red flag:** одинаковый hook для всех вариантов

### C2: Brief Alignment (copywriter)
**Вопрос:** Тексты соответствуют стратегии и сегментам?
- 5: Каждый креатив привязан к сегменту из стратегии, использует key messages
- 3: Общее соответствие, но не все сегменты покрыты
- 1: Тексты "сами по себе", не связаны со стратегией
- **Red flag:** messaging противоречит positioning

### E1: Information Flow (end-to-end)
**Вопрос:** Каждый агент использует output предыдущего?
- 5: Чёткая преемственность - сегменты стратега видны в таргетинге, медиаплане, текстах
- 3: Частичная преемственность, некоторые insights потеряны
- 1: Агенты работают "в вакууме"
- **Red flag:** copywriter игнорирует сегменты стратега

### E2: Consistency (end-to-end)
**Вопрос:** Нет противоречий между документами?
- 5: Все документы coherent, цифры совпадают, messaging единый
- 3: Мелкие расхождения (разные названия сегментов)
- 1: Прямые противоречия (стратег: premium, копирайтер: mass market)
- **Red flag:** бюджет в медиаплане != бюджет в стратегии

---

## Автоматические метрики (бонус/штраф)

### Validator Pass Rate
```
validator_pass_rate = PASS_count / total_creatives
```
- >= 90%: +2 bonus
- 70-89%: +0
- < 70%: -2 penalty

### KB Citation Rate
```
kb_citation_rate = statements_with_T1_T3_source / total_claims
```
- >= 60%: +1 bonus
- 30-59%: +0
- < 30%: -1 penalty

---

## Итого

**Base max:** 60 (12 × 5)
**Bonus max:** +3
**Penalty max:** -3
**Effective range:** 57-63

**Target:** >= 54/60 base (4.5/5 avg) AND validator_pass_rate >= 70%
