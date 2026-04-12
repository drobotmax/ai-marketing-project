# Harness Optimizer Runner

> Slash command: `/kubrik-pipeline optimize`
> Оптимизирует KUBRIK pipeline end-to-end по Meta-Harness подходу.

## Файлы

| Файл | Роль | Кто меняет |
|------|------|-----------|
| `test-briefs.json` | 5 тестовых брифов | Только человек |
| `scoring-rubric.md` | 12 критериев оценки | Только человек |
| `config.json` | Настройки оптимизации | Человек (начальные), агент (mutations log) |
| `harness-log.md` | Лог раундов с оценками | Агент (append-only) |
| `agent-traces/round-N/` | Input/output каждого агента | Агент (write per round) |

## Режимы запуска

### Full round (default)
Прогнать все 5 брифов через pipeline, оценить, мутировать.
```
> Запусти harness optimizer round
```

### Single brief (debug)
Прогнать один бриф, оценить только его.
```
> Запусти harness optimizer на TB-03
```

### Score only
Оценить уже сгенерированные traces без прогона pipeline.
```
> Оцени traces из round-2
```

### Diagnose only
Проанализировать scores и предложить мутацию без применения.
```
> Диагностируй round-2 и предложи мутацию
```

## Цикл

### Шаг 1: Подготовка (первый раз)

1. Создать `harness-log.md` с заголовком
2. Создать `agent-traces/` директорию
3. Снапшот текущих промптов агентов:
```
agent-traces/baseline/
  strategist-prompt.md    <- copy of agents/strategist/skill.md
  targeting-prompt.md     <- copy of agents/targeting/skill.md
  contextologist-prompt.md <- copy of agents/contextologist/skill.md
  media-buyer-prompt.md   <- copy of agents/media-buyer/skill.md
  copywriter-prompt.md    <- copy of agents/copywriter/skill.md
  validator-prompt.md     <- copy of agents/validator/skill.md
```

### Шаг 2: Pipeline run

Для КАЖДОГО тестового брифа (TB-01 ... TB-05):
1. Прочитать brief из `test-briefs.json`
2. Прогнать через KUBRIK pipeline (стандартный skill)
3. Сохранить output каждого агента:
```
agent-traces/round-N/
  TB-01/
    strategy.md
    targeting-plan.md
    context-ads-plan.md
    media-plan.md
    creatives.md
    validation.md
  TB-02/
    ...
```

**Важно:** прогонять можно по одному брифу (экономия токенов).
Minimum viable round = 2 брифа (один РФ + один international).

### Шаг 3: Scoring (LLM-as-judge)

Для каждого брифа:
1. Прочитать `scoring-rubric.md`
2. Прочитать все outputs из `agent-traces/round-N/TB-XX/`
3. Оценить 12 критериев (0-5 каждый)
4. Посчитать validator pass rate и KB citation rate
5. Записать в `agent-traces/round-N/TB-XX/scores.json`:

```json
{
  "brief_id": "TB-01",
  "round": 1,
  "scores": {
    "S1_market_depth": 4,
    "S2_segment_clarity": 3,
    "S3_channel_logic": 5,
    "T1_audience_architecture": 3,
    "T2_platform_expertise": 4,
    "T3_test_design": 2,
    "M1_budget_coherence": 5,
    "M2_cross_channel_logic": 4,
    "C1_hook_strength": 3,
    "C2_brief_alignment": 4,
    "E1_information_flow": 3,
    "E2_consistency": 4
  },
  "base_score": 44,
  "validator_pass_rate": 0.85,
  "kb_citation_rate": 0.45,
  "bonus": 0,
  "total_score": 44,
  "notes": "T3 weakest - experiments lack stopping rules"
}
```

6. Агрегировать scores по всем брифам → средний score
7. Записать summary в `harness-log.md`

### Шаг 4: Target check

```
avg_base_score >= 54/60 AND min_validator_pass_rate >= 70%
  -> STOP, record final result
  -> else continue
```

### Шаг 5: Diagnose

1. **Weakest criterion:** Найти критерий с наименьшим средним score
2. **Weakest brief:** Найти бриф с наименьшим total score
3. **Bottleneck agent:** Определить какой агент виноват:

```
Attribution logic:
- S1, S2, S3 low -> strategist
- T1, T2, T3 low -> targeting/contextologist
- M1, M2 low -> media-buyer
- C1, C2 low -> copywriter
- E1, E2 low -> нужен trace analysis (кто потерял данные?)
```

4. Для E1/E2 (pipeline coherence):
   - Прочитать output bottleneck-брифа step by step
   - Найти WHERE информация теряется
   - Определить: проблема в source agent или в receiving agent

### Шаг 6: Mutate

1. Сформулировать ОДНУ гипотезу
2. Определить уровень мутации:
   - **Level 1 (prompt):** Изменить `agents/[agent]/skill.md`
   - **Level 2 (format):** Изменить output template агента
   - **Level 3 (topology):** Изменить config.json (agent order, parallelism)
3. Внести ОДНО изменение
4. Записать в harness-log.md:

```markdown
## Round N - [дата]

**Avg score:** XX/60 (X.X/5)
**Weakest criterion:** TX (X.X avg)
**Weakest brief:** TB-XX (XX/60)
**Bottleneck agent:** [agent]

**Per-brief scores:**
| Brief | S1 | S2 | S3 | T1 | T2 | T3 | M1 | M2 | C1 | C2 | E1 | E2 | Total |
|-------|----|----|----|----|----|----|----|----|----|----|----|----|-------|
| TB-01 | .. | .. | .. | .. | .. | .. | .. | .. | .. | .. | .. | .. | XX/60 |
...

**Diagnosis:** [что не так и почему]
**Hypothesis:** [что изменить и почему это должно помочь]
**Mutation:** [конкретное изменение, файл, diff]
**Level:** 1/2/3
```

### Шаг 7: Повторить с шага 2

## Правила

### Immutable (человек контролирует)
- `test-briefs.json` - тестовые данные
- `scoring-rubric.md` - критерии оценки
- Агентские файлы в `agents/` - мутации ТОЛЬКО через optimizer с логом

### One mutation per round
- Не менять 2+ агентов одновременно
- Не менять prompt + format в одном раунде
- Исключение: если мутация Level 2 (format) требует обновления двух агентов
  (sender и receiver) - это считается одной мутацией

### Rollback
- Если score упал после мутации -> откатить изменение
- Baseline prompts всегда доступны в `agent-traces/baseline/`
- Каждая мутация записывается как diff в harness-log.md

### Cost management
- Minimum viable round: 2 брифа (1 РФ + 1 intl)
- Можно пропустить scoring если уже знаешь проблему (diagnose-only)
- Pipeline run = самая дорогая операция, scoring = дешёвая

## Интеграция с AutoResearch

Harness Optimizer и AutoResearch - разные инструменты для разных задач:

- **AutoResearch:** оптимизация одного промпта (outreach message)
- **Harness Optimizer:** оптимизация pipeline из 6 агентов

Но паттерны общие:
- Append-only log
- Human-controlled evaluation criteria
- One mutation per round
- Target score -> STOP
- Anti-examples как основной тип мутации
