# KUBRIK Wiki Schema

> Wiki layer поверх сырых источников.
> Sources - неизменяемые. Wiki - синтезированные, с cross-links, поддерживаемые агентом.

## Три типа wiki-страниц

### concepts/
Атомарные концепции, фреймворки, принципы. Одна страница = одна идея.
- `jtbd.md` - Jobs to Be Done
- `slippery-slide.md` - Скользкая горка Шугермана
- `social-proof.md` - Социальное доказательство

### comparisons/
Сравнительные страницы: X vs Y с практическими выводами для KUBRIK.
- `meta-vs-vk-targeting.md`
- `yandex-vs-google-ads.md`

### playbooks/
Синтез из нескольких источников в actionable процесс.
- `cold-audience-copy.md` - как писать для холодной аудитории (Sugarman + Cialdini + StoryBrand)
- `rf-launch-checklist.md` - чеклист запуска РФ кампании (Prais + anti-patterns + VK)

---

## Формат wiki-страницы

```markdown
# {Название концепции}

> Источники: [[books/file.md]], [[targeting-course/file.md]]
> Последнее обновление: YYYY-MM-DD
> Тип: concept | comparison | playbook

## Суть (2-3 предложения)

{Краткое определение, понятное без контекста}

## Ключевые идеи

{Основной контент - фреймворк, список принципов, сравнительная таблица}

## Применение в KUBRIK

{Как конкретно это использовать в рекламных кампаниях KUBRIK.
Примеры для недвижимости, Bali, РФ рынка.}

## Cross-links

- Связанные концепции: [[concept-1]], [[concept-2]]
- Связанные playbooks: [[playbook-1]]
- Anti-patterns: [[team-playbooks/anti-patterns.md#section]]
```

---

## Правила поддержки

### При добавлении нового источника (/kubrik-kb)
1. Положить сырой файл в соответствующую папку sources (books/, courses/, etc.)
2. Извлечь новые концепции -> создать или обновить wiki/concepts/
3. Проверить существующие comparisons - нужны ли новые сравнения?
4. Проверить playbooks - добавляет ли источник новые actionable шаги?
5. Обновить cross-links на затронутых страницах
6. Если новый источник противоречит существующей wiki-странице - отметить в секции "Противоречия" и указать tier обоих источников

### При обнаружении противоречия
```markdown
## Противоречия
- **{Источник A} (T{N})** утверждает X
- **{Источник B} (T{N})** утверждает Y
- **Резолюция:** Побеждает T{меньший номер}. {Пояснение}
```

### Именование файлов
- kebab-case, только латиница
- Концепции: существительное или фраза (`jtbd.md`, `slippery-slide.md`)
- Сравнения: `x-vs-y.md`
- Playbooks: глагол-объект (`launch-rf-campaign.md`, `write-cold-copy.md`)

### Размер страницы
- Concept: 50-150 строк (больше - разбить на суб-концепции)
- Comparison: 80-200 строк
- Playbook: 100-300 строк

---

## Tier наследование

Wiki-страницы наследуют tier самого высокого источника:
- Если playbook основан на T1 (team-playbooks) + T2 (books) -> tier = T1
- Если concept основан только на T2 (books) -> tier = T2
- При конфликте wiki-страницы с anti-patterns.md -> anti-patterns побеждает (T1)
