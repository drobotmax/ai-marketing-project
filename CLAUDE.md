# KUBRIK - Knowledge Base & Pipeline

## Команда
- **Максим Дробот** - AI-архитектура, разработка, knowledge base
- **Дмитрий** - трафик, таргетинг, рекламные кабинеты (Meta/Google/Yandex)
- **Антон Новиков** - стратегия, клиенты, позиционирование

## Что это за репо
Общая база знаний и рабочие материалы команды. Здесь живут:
- Knowledge base для AI-агентов (книги, курсы, справочники платформ)
- Клиентские папки с брифами, стратегиями, креативами и контент-планами
- KUBRIK Pipeline агентов (стратег -> фактчекер -> таргетолог -> media planner -> копирайтер -> char-guard -> валидатор)

## Навигация

```
knowledge/                  - база знаний (главный актив)
  books/                    - 7 книг: Schwartz, JTBD, StoryBrand, Sugarman, Cialdini, Blue Ocean, Positioning
  bali-market/              - рынок Бали: цены, локации, девелоперы, регуляции
  targeting-course/         - курс по таргету Meta/Instagram (27 уроков, транскрипты)
  targeting-course-2/       - продвинутый курс по таргету (~51 видео)
  copywriting-course/       - курс копирайтинга "Сделаем" (40 уроков)
  meta-ads/                 - справка Meta Ads Help Center (1200+ страниц)
  seo-course/               - SEO курс

agents/                     - определения AI-агентов (pipeline)
  strategist/skill.md       - агент-стратег (анализ рынка, ЦА, позиционирование)
  fact-checker/skill.md     - агент-фактчекер (верификация claims после стратега)
  targeting/skill.md        - агент-таргетолог (аудитории, гипотезы, тесты, оптимизация Meta/Instagram)
  media-buyer/skill.md      - агент media planner (budget arbitration, cross-channel planning, launch calendar)
  copywriter/skill.md       - агент-копирайтер (paid creatives + organic content plan при наличии SMM budget)
  validator/skill.md        - агент-валидатор (QA: лимиты, policy, бриф)
  sales-qa/skill.md         - агент sales QA (разбор звонков, ICP fit, objections, next step)
  references/platform-specs.md - техтребования Meta/Google/Yandex
  references/sales-qa-checklist.md - чеклист quality review для отдела продаж

clients/                    - результаты работы по клиентам
  [client-slug]/            - brief.md, strategy.md, media-plan.md, creatives.md, content-plan.md, creatives.char-guard.md, validation.md

strategy/                   - стратегии и аналитика
  positioning-analysis.md   - утвержденное позиционирование (2026-03-26)

creatives/                  - рекламные креативы
copy/                       - тексты объявлений
landing/                    - посадочные страницы
```

## Позиционирование (утверждено командой)
- Центр: экспертиза людей, усиленная AI (не технология в центре)
- "Встраиваем команду маркетинговых экспертов с AI в отдел застройщика"
- Фокус: недвижимость, 1-3 клиента, undeniable value
- НЕ говорить "AI-агенты" клиентам - говорить языком их проблем

## Правила для Claude Code

### Язык
- Общение с командой: русский
- Код, технические файлы: английский
- Креативы: язык целевой аудитории (определяется в стратегии)

### Копирайтинг
- Стиль: профессиональный, современный, без канцелярита
- Конкретика: цифры, факты, примеры - без воды
- Избегать клише и штампов
- НИКОГДА не использовать длинное тире - только дефис (-) или короткое тире

### При генерации стратегий и текстов - опираться на knowledge base:
- **Awareness levels** (Schwartz) - уровень осведомленности ЦА
- **JTBD** (Christensen) - позиционирование через работу клиента
- **SB7** (Miller) - клиент = герой, бренд = наставник
- **Slippery Slide** (Sugarman) - каждый элемент тянет к следующему
- **7 принципов** (Cialdini) - принципы убеждения в каждый текст
- **ERRC** (Blue Ocean) - незанятое пространство
- **Positioning** (Trout/Ries) - владей одним словом в голове клиента

### Дизайн (HTML-артефакты)
- Self-contained HTML (inline CSS/JS)
- Темная тема, минимализм
- Палитра: #6c5ce7 (accent), #00cec9 (green), #fdcb6e (orange)
- Адаптив: мобайл + десктоп

### Клиентские материалы
Результаты работы сохранять в:
```
clients/[client-slug]/
  brief.md          - исходный бриф
  strategy.md       - стратегия
  fact-check.md     - результат фактчека
  media-plan.md     - медиаплан
  creatives.md      - креативы
  content-plan.md   - organic / SMM план, если в стратегии есть community budget
  creatives.char-guard.md - креативы после программного пересчёта лимитов
  validation.md     - результат валидации
  sales-qa.md       - разбор sales-call / переписки / оффера
```

Если в стратегии или медиаплане есть строка SMM / organic / community, обязательны два артефакта:
- `creatives.md` для paid placements
- `content-plan.md` для owned channels и прогрева

### Минимальный contract для `brief.md`

Перед запуском pipeline в `brief.md` должны быть заполнены обязательные поля. Если их нет, стратег не должен додумывать недостающие данные, а валидатор должен пометить запуск как `BLOCKED`.

Минимальная структура:

```markdown
## Объект
- Название:
- Застройщик:
- Локация:
- Класс:
- Этажность / объём:
- Срок сдачи:

## Продукт
- Квартирография / продуктовые лоты:
- УТП:

## Целевая аудитория
- Основные сегменты:

## Бюджет и цели
- Бюджет:
- Гео:
- Цели / KPI:

## Инфраструктура запуска (обязательно)
- Landing page URL:
- CRM система: AmoCRM / Bitrix / другая / нет
- Фид / карточки квартир на сайте: есть / нет
- 152-ФЗ: чекбокс согласия в лид-формах есть / нет
- Колтрекинг: есть / нет
- Яндекс Метрика: есть / нет, ID счётчика
```

Правила:
- `Landing page URL` - обязательный источник правды для performance-каналов
- `CRM система` - обязательное поле даже если интеграции ещё нет
- `Фид / карточки квартир` - определяет, можно ли планировать товарные кампании
- `152-ФЗ` - без подтверждённого consent нельзя считать лид-формы launch-ready
- `Колтрекинг` и `Яндекс Метрика` влияют на readiness и measurement plan, их нельзя оставлять неизвестными

## Post-processing: Character Guard

После генерации `creatives.md` не полагаться на LLM-подсчёт символов как на source of truth.

Обязательный шаг перед валидацией:

```bash
python3 scripts/creative_char_guard.py clients/<client-slug>/creatives.md \
  --mode fix \
  --overflow-policy trim \
  --output clients/<client-slug>/creatives.char-guard.md \
  --report clients/<client-slug>/creatives.char-guard.report.md
```

Правила:
- `creatives.md` - сырой output копирайтера
- `creatives.char-guard.md` - файл для валидатора и ручного ревью
- скрипт программно пересчитывает char count, обновляет `(X chars)` и отмечает остаточные overflow
- если безопасно, скрипт сокращает текст до лимита; если нет - оставляет overflow в отчёте для доработки человеком/LLM

## GitHub Project
Задачи и спринты: https://github.com/users/drobotmax/projects/1
