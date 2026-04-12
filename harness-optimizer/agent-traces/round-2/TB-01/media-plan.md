# Media Plan: ЖК Горизонт (Краснодар)

## Общие параметры
- Бюджет: 300,000 руб/мес
- Гео: Краснодар, Прикубанский округ, Россия
- Период: запуск через 2 недели, первый месяц = тест + стабилизация
- Цель: 150+ лидов/мес при CPL < 2,000 руб

## Роль каналов

| Канал | Роль в воронке | Причина включения | Launch phase |
|-------|-----------------|-------------------|--------------|
| Яндекс Директ | Demand capture (горячий поиск) + demand creation (МК, РСЯ) + retargeting | Основной канал для РФ-рынка, ловит intent-based спрос | Phase 1 (Day 1) |
| VK Ads | Demand creation + lead generation | Лучший paid social для РФ, лид-формы, широкий охват | Phase 1 (Day 3) |
| VK Community (SMM) | Trust building + warm-up + retargeting seed | Поддержка paid, social proof, прогрев | Phase 1 (Day 1) |
| Google Ads | NOT included | Рынок = РФ, Google Ads не в committed plan | Optional (Month 3+) |

## Budget Reconciliation

| Канал | Strategy hard cap | Specialist requested | Approved committed budget | Delta | Статус |
|-------|-------------------|----------------------|---------------------------|-------|--------|
| Яндекс Директ | 165,000 | 165,000 | 165,000 | 0 | PASS |
| VK Ads | 105,000 | 105,000 | 105,000 | 0 | PASS |
| SMM / VK Community | 30,000 | 30,000 | 30,000 | 0 | PASS |
| **Total** | **300,000** | **300,000** | **300,000** | **0** | **PASS** |

Reconciliation notes:
- Оба специалиста уложились в hard caps без превышения
- Google Ads исключён из committed plan (рынок РФ)
- Бюджеты арифметически сходятся: 165K + 105K + 30K = 300K

## Conflict Resolution

| Конфликт | Что предложили агенты | Решение planner | Почему |
|----------|------------------------|-----------------|--------|
| Sequencing: Яндекс и VK старт | Контекстолог: МК Day 1, Поиск Day 4. Таргетолог: VK Day 3 | Яндекс МК + Brand Day 1, VK Lead Forms Day 3, Яндекс Поиск Day 4 | Яндекс МК собирают данные первыми, VK стартует параллельно с небольшим лагом для QA лид-форм |
| Ретаргетинг ownership | Оба агента закладывают ретаргетинг | Яндекс ретаргетинг = контекстолог (РСЯ + RLSA). VK ретаргетинг = таргетолог (клики на лид-формы, посетители) | Каждый канал ретаргетит свою аудиторию, cross-channel ретаргетинг = Phase 2 |
| CPL expectations | Контекстолог: CPL 1,500-2,500. Таргетолог: CPL 1,200-2,000 | Blended CPL target: < 2,000 руб (из брифа). Допустим Яндекс дороже (до 2,500) если qualified rate выше | Search даёт более горячие лиды, VK - больший объём. Blended = OK если total < 2,000 |
| SMM ownership | Стратег: 30K на SMM. Таргетолог: organic support layer | SMM = отдельный content stream, контент готовит копирайтер, VK Community management = таргетолог координирует | Таргетолог ближе к VK-платформе, знает что ретаргетить из community |

## Approved Channel Plans

### Channel 1: Яндекс Директ
- **Owner:** Контекстолог
- **Objective:** demand capture (поиск) + demand creation (МК, РСЯ) + retargeting
- **Approved budget:** 165,000 руб/мес (5,500 руб/день на режиме)
- **Why now:** основной канал для горячего спроса в РФ, весна = пик сезона
- **Key dependencies:**
  - Яндекс Метрика установлена и цели настроены - BLOCKER
  - Колтрекинг подключён - BLOCKER
  - CRM интеграция для офлайн-конверсий - CRITICAL (первые 2 недели можно без неё, но нужна к Day 14)
  - Landing page gorizont-dev.ru работает корректно на мобильных
- **Success signal for Phase 2:** CPL < 2,500 руб, qualified lead rate > 30%, 70+ лидов/мес
- **Included specialist components:**
  - 7 кампаний: 2 МК, 2 поисковые, 1 brand, 1 РСЯ, 1 ретаргетинг
  - 5 кластеров семантики: brand, комнатность, ипотека, конкуренты, гео
  - Алгоритм запуска по Прайсу
- **Deferred / cut items:**
  - Товарный МК (нет фида - отложен до создания)
  - Баннер на поиске (Phase 2, когда brand campaign стабилизируется)
  - Google Ads (Optional Experiment, Month 3+)

### Channel 2: VK Ads
- **Owner:** Таргетолог
- **Objective:** demand creation + lead generation + community building
- **Approved budget:** 105,000 руб/мес (3,500 руб/день)
- **Why now:** лучший paid social для РФ, лид-формы дают быстрый lead volume
- **Key dependencies:**
  - Пиксель VK установлен на сайте - BLOCKER
  - Лид-формы настроены с ручным вводом - BLOCKER
  - Креативы (рендеры, фото, планировки) готовы - BLOCKER
  - CRM-интеграция для выгрузки лидов из VK
- **Success signal for Phase 2:** CPL < 2,000 руб, qualified lead rate > 25%, 55+ лидов/мес
- **Included specialist components:**
  - 4 кампании: интересы, ключевые фразы, конкуренты, ретаргетинг
  - Лид-формы с ручным вводом + квалифицирующим вопросом
  - VK Community organic support layer
- **Deferred / cut items:**
  - VK Клипы (нет вертикального видео - отложен)
  - Одноклассники (Phase 2, отдельная группа для теста)
  - Расширение аудитории (только после тестирования основных)

### Channel 3: SMM / VK Community
- **Owner:** Копирайтер (контент) + Таргетолог (координация с paid)
- **Objective:** trust building, social proof, прогрев для ретаргетинга
- **Approved budget:** 30,000 руб/мес (продакшн контента + продвижение лучших постов)
- **Why now:** community нужен с Day 1 для прогрева и social proof
- **Key dependencies:**
  - Фото/видео со стройки от клиента
  - Доступ к VK Community
  - Рендеры и планировки
- **Success signal:** engagement rate > 3%, community growth 50+/week, warm leads from community
- **Included components:**
  - 12 постов/мес (ход стройки, Q&A, планировки, кейсы)
  - Pinned post с основным оффером
  - Response SLA < 15 мин

## Cross-Channel Optimization Rules

- Если Яндекс даёт CPL > 3,000 руб после 14 дней - не масштабировать, сначала проверить landing page и quality score
- Если VK даёт CPL < 1,500 руб но qualified rate < 15% - не считать это успехом, ужесточить лид-форму
- Если sales team не успевает обрабатывать лиды (speed-to-lead > 30 мин) - не scale paid, сначала fix процесс
- Если оба канала каннибализируют brand-запросы - разделить: Яндекс берёт brand поиск, VK не таргетируется на brand keywords
- Если CRM не подключена к Day 14 - остановить масштабирование и зафиксировать как BLOCKER

## Launch Calendar

| Неделя | День | Действие | Канал | Бюджет/день |
|--------|------|----------|-------|-------------|
| Pre-launch | -14 to -1 | Setup: Метрика, пиксель VK, колтрекинг, лид-формы, креативы, VK Community | All | 0 |
| 1 | Day 1-2 | Запуск МК (2 шт) + Brand (Яндекс), VK Community pinned post | Яндекс + SMM | 2,100 |
| 1 | Day 3 | Запуск VK Lead Forms (Campaign 1 + 2) | VK Ads | 2,100 + 2,450 = 4,550 |
| 1 | Day 4-7 | Запуск Яндекс Поиск (горячий + конкуренты), первая чистка запросов МК | Яндекс + VK | 4,300 + 3,500 = 7,800 |
| 2 | Day 8-10 | Запуск VK Campaign 3 (конкуренты), Яндекс РСЯ, первый read | All | 5,500 + 3,500 = 9,000 |
| 2 | Day 11-14 | Запуск ретаргетинга (оба канала), первая оптимизация, отключение losers | All | 5,500 + 3,500 + 1,000 = 10,000 |
| 3 | Day 15-21 | Reallocate budget к winners, тест offer angles, CRM quality check | All | 10,000 |
| 4 | Day 22-30 | Стабилизация, расширение семантики Яндекс, масштабирование VK winners | All | 10,000 |

Trigger для каждой фазы:
- Phase 1 -> Phase 2: CPL стабилизировался, qualified lead rate > 25%, CRM feedback loop работает
- Phase 2 -> Scale: CPL < 2,000, 150+ лидов/мес, sales team справляется с объёмом

## Optional Scale Scenarios

| Сценарий | Условие активации | Доп. бюджет | Что добавляем |
|----------|-------------------|-------------|---------------|
| Scale VK | CPL < 1,500 руб + qualified rate > 30% | +50,000 руб/мес | Новые аудитории VK, ОК, расширение |
| Scale Яндекс | CPL < 2,000 + qualified rate > 40% | +50,000 руб/мес | Тёплые кластеры, товарный МК (нужен фид) |
| Google Ads test | Month 3+, свободный бюджет внутри cap | 30,000 руб/мес | Brand + горячий поиск Google (проверка incremental demand) |
| VK Клипы | Вертикальное видео готово | 0 (из текущего VK бюджета) | Новый плейсмент в существующих кампаниях |

## Budget Compliance

- **Total strategy budget:** 300,000 руб/мес
- **Total approved committed budget:** 300,000 руб/мес
  - Яндекс Директ: 165,000
  - VK Ads: 105,000
  - SMM / VK Community: 30,000
- **Budget mismatch:** 0
- **Status:** PASS
