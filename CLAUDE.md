# KUBRIK - Knowledge Base & Pipeline

## Команда
- **Максим Дробот** - AI-архитектура, разработка, knowledge base
- **Дмитрий** - трафик, таргетинг, рекламные кабинеты (Meta/Google/Yandex)
- **Антон Новиков** - стратегия, клиенты, позиционирование

## Что это за репо
Общая база знаний и рабочие материалы команды. Здесь живут:
- Knowledge base для AI-агентов (книги, курсы, справочники платформ)
- Клиентские папки с брифами, стратегиями, креативами
- KUBRIK Pipeline агентов (стратег -> таргетолог -> медиабайер -> копирайтер -> валидатор)

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
  targeting/skill.md        - агент-таргетолог (аудитории, гипотезы, тесты, оптимизация Meta/Instagram)
  media-buyer/skill.md      - агент-медиабайер (кампании, аудитории, бюджеты)
  copywriter/skill.md       - агент-копирайтер (тексты под каждый плейсмент)
  validator/skill.md        - агент-валидатор (QA: лимиты, policy, бриф)
  sales-qa/skill.md         - агент sales QA (разбор звонков, ICP fit, objections, next step)
  references/platform-specs.md - техтребования Meta/Google/Yandex
  references/sales-qa-checklist.md - чеклист quality review для отдела продаж

clients/                    - результаты работы по клиентам
  [client-slug]/            - brief.md, strategy.md, media-plan.md, creatives.md, validation.md

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
  media-plan.md     - медиаплан
  creatives.md      - креативы
  validation.md     - результат валидации
  sales-qa.md       - разбор sales-call / переписки / оффера
```

## GitHub Project
Задачи и спринты: https://github.com/users/drobotmax/projects/1
