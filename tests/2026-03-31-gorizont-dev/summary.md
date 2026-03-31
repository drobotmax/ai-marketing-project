# Pipeline Test: ЖК "Парковый" - Горизонт Девелопмент

**Date:** 2026-03-31
**Type:** Full pipeline end-to-end test
**Client:** Fictional (test case)

## Test Parameters
- Object: residential complex, comfort+ class, Krasnodar
- Budget: 500K RUB/month
- Segments: young families, investors, relocators
- Channels: Yandex Direct, VK Ads, Avito, Telegram Ads, SMM

## Results

| Metric | Value |
|--------|-------|
| Pipeline score | 6.5/10 |
| Total tokens | ~400-450K |
| Wall-clock time | ~17 min |
| Agent tool calls | 49 |
| Creatives generated | 43 |
| Critical bugs found | 8 (4x P0, 4x P1) |
| Validation status | NEEDS REVISION |

## Critical Bugs (P0)
1. No VK Ads, Avito, Telegram Ads agents - pipeline covers Meta/Google only
2. Targeting agent knows Meta only - useless for Russian market without VK
3. platform-specs.md missing VK Ads specifications
4. No fact-check step - misleading claims propagate through pipeline

## Critical Bugs (P1)
5. Copywriter char counting errors (80% of fields)
6. Media buyer role is redundant (compiler, not expert)
7. Budget conflicts between agents not resolved
8. No creatives for Telegram Ads and Avito (30% of budget)

## What Works Well
- Pipeline flow: each agent uses previous agent's output
- Strategist: JTBD, Cialdini, Trout/Ries applied properly
- Contextologist: strongest agent, deep Yandex Direct expertise
- Validator: found real issues, auto-fix works
- Output format: consistent, client-readable

## Files
- [report.html](report.html) - full HTML report
- [clients/gorizont-dev-test/](../../clients/gorizont-dev-test/) - all pipeline outputs
