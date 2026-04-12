# KUBRIK Harness Optimizer

> Meta-Harness подход к оптимизации pipeline: оптимизируем не отдельные промпты,
> а всю цепочку агентов как единую систему (harness).

## Ключевой инсайт

AutoResearch оптимизирует один промпт по 5 критериям.
Harness Optimizer оптимизирует **6 агентов + межагентные форматы** по end-to-end метрике.

Валидатор KUBRIK проверяет только копирайтера (char limits, policy).
Harness Optimizer оценивает **весь выход pipeline** - от стратегии до финального пакета.

## Архитектура

```
test-briefs.json          <- 5 тестовых брифов (human-controlled, immutable)
scoring-rubric.md         <- 12 критериев end-to-end качества (human-controlled)
config.json               <- что варьируем, лимиты, target score
harness-log.md            <- лог раундов (append-only)
agent-traces/             <- input/output каждого агента за раунд
  round-N/
    strategist-out.md
    targeting-out.md
    contextologist-out.md
    media-buyer-out.md
    copywriter-out.md
    validator-out.md
    scores.json           <- per-agent + end-to-end scores
```

## Что оптимизируем (Harness Variables)

### Уровень 1: Промпты агентов
- Инструкции в `agents/*/skill.md`
- Примеры и антипримеры
- Правила приоритизации знаний (T1>T2>T3>T4 веса)

### Уровень 2: Межагентные форматы
- Формат передачи strategy.md -> targeting/contextologist
- Какие секции стратегии видит каждый агент
- Формат handoff между targeting+context -> media-buyer
- Какой контекст получает copywriter (full strategy vs summary)

### Уровень 3: Pipeline topology
- Порядок агентов (параллельный vs последовательный)
- Включение/выключение fact-checker
- Количество итераций validator auto-fix

## Цикл оптимизации

```
┌─────────────────────────────────────────────┐
│  1. BASELINE                                │
│  Прогнать pipeline на 5 тестовых брифах     │
│  Сохранить output каждого агента            │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  2. SCORE                                   │
│  Оценить 12 критериев (LLM-as-judge)       │
│  Per-agent score + end-to-end score         │
│  Записать в harness-log.md                  │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  3. TARGET CHECK                            │
│  score >= 54/60 (4.5/5 avg)? -> STOP        │
│  score < 54/60? -> continue                 │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  4. DIAGNOSE                                │
│  Найти bottleneck-агента (lowest score)     │
│  Найти bottleneck-критерий                  │
│  Найти bottleneck-бриф (worst test case)    │
│  Attribution: какой агент "сломал" выход?   │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  5. MUTATE                                  │
│  Одно изменение в одном месте:              │
│  - Промпт агента (Level 1)                  │
│  - Межагентный формат (Level 2)             │
│  - Pipeline config (Level 3)                │
│  Записать гипотезу в лог                    │
└──────────────────┬──────────────────────────┘
                   │
                   └──→ Повторить с шага 1
```

## Scoring: 12 критериев × 5 баллов

### Strategy Quality (агент: strategist)
1. **Market depth** - конкретика рынка, не generic advice (0-5)
2. **Segment clarity** - JTBD, pain points, не demographics-only (0-5)
3. **Channel logic** - обоснование выбора каналов, budget fit (0-5)

### Targeting/Context Quality (агенты: targeting + contextologist)
4. **Audience architecture** - cold/warm/hot funnel, не flat list (0-5)
5. **Platform expertise** - использование KB, не model hallucination (0-5)
6. **Test design** - hypothesis-driven, measurable, actionable (0-5)

### Media Plan Quality (агент: media-buyer)
7. **Budget coherence** - суммы сходятся, min thresholds respected (0-5)
8. **Cross-channel logic** - нет конфликтов, sequencing makes sense (0-5)

### Creative Quality (агент: copywriter)
9. **Hook strength** - первая строка останавливает скролл (0-5)
10. **Brief alignment** - тексты соответствуют стратегии и сегментам (0-5)

### Pipeline Coherence (end-to-end)
11. **Information flow** - каждый агент использует output предыдущего (0-5)
12. **Consistency** - нет противоречий между документами (0-5)

### Бонус/штраф (автоматический)
- Validator PASS rate: % креативов прошедших валидацию
- KB citation rate: % утверждений с источником T1-T3

**Max score:** 60 points (12 × 5)
**Target:** >= 54/60 (4.5/5 average)

## Диагностика: Attribution Analysis

Ключевое отличие от AutoResearch - нужно понять **какой агент виноват**
в проблеме end-to-end:

```
Проблема: "Креативы не соответствуют стратегии" (Q10 low)

Возможные причины:
A) Copywriter игнорирует strategy.md -> мутация в copywriter prompt
B) Strategy.md слишком абстрактная -> мутация в strategist prompt
C) Media-plan потерял сегменты -> мутация в media-buyer prompt
D) Формат передачи strategy->copywriter неудачный -> мутация Level 2
```

Правило: **читать agent traces** перед мутацией.
Если output стратега хороший, но копирайтер его не использовал -
проблема в копирайтере или в формате передачи.

## Мутации: приоритет

1. **Антипример в prompt агента** - если агент делает конкретную ошибку
2. **Уточнение правила** - если правило двусмысленно
3. **Изменение межагентного формата** - если данные теряются при передаче
4. **Добавление required section** - если агент пропускает важный блок
5. **Изменение KB reading order** - если агент читает не те источники
6. **Pipeline topology** - только если 3+ раундов мелких правок не помогают

## Связь с AutoResearch

| Аспект | AutoResearch | Harness Optimizer |
|--------|-------------|-------------------|
| Target | 1 промпт | 6 агентов + форматы |
| Criteria | 5 binary | 12 scored (0-5) |
| Test data | 10 лидов | 5 брифов |
| Evaluator | Self-eval | LLM-as-judge |
| Attribution | N/A (1 prompt) | Per-agent diagnosis |
| Mutation | Prompt only | Prompt + format + topology |
| Log | autoresearch-log.md | harness-log.md |

## Ограничения

- **Не автоматический:** требует Claude Code сессию для каждого раунда
- **Cost:** ~$2-5 за полный прогон pipeline на 5 брифах
- **Время:** ~15-30 мин за раунд (5 брифов × 6 агентов)
- **Human-in-the-loop:** scoring rubric и test briefs контролирует человек
