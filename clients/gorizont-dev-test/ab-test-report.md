# A/B Test Report: KUBRIK Strategist v1 (Static KB) vs v2 (RLM)

**Date:** 2026-04-12
**Brief:** ЖК "Парковый", Горизонт Девелопмент, Краснодар, 500К руб/мес
**Agent:** Strategist
**Model:** Claude Opus 4.6

---

## Resource Consumption

| Metric | v1 (Static KB) | v2 (RLM) | Delta |
|--------|----------------|-----------|-------|
| KB files read | 22 | 10 | **-55%** |
| Lines read (approx) | ~2,800 | ~1,383 | **-51%** |
| Tool calls | 47 | 23 | **-51%** |
| Total tokens | 90,308 | 59,499 | **-34%** |
| Duration (ms) | 243,673 | 241,891 | ~same |

**Verdict:** RLM uses ~34% fewer tokens and ~51% fewer tool calls for comparable output.

---

## Quality Comparison

### 1. Market Analysis

| Criteria | v1 | v2 | Winner |
|----------|----|----|--------|
| Market overview | Good - competitive landscape, trends | Good - same level of detail | Tie |
| Schwartz stage applied | Yes (Stage 3-4) | Yes (Stage 3-4) + per-segment breakdown | **v2** |
| Competitor analysis | 3 competitors with strengths | 3 competitors with strengths AND weaknesses | **v2** |

### 2. Target Audience (ЦА)

| Criteria | v1 | v2 | Winner |
|----------|----|----|--------|
| Segments defined | 3 (families, relocants, investors) | 3 (same) | Tie |
| JTBD framework | Basic JTBD per segment | Full JTBD with 4 forces (push/pull/habit/anxiety) | **v2** |
| Budget allocation | 60/25/15% | Same implied | Tie |
| Depth of personas | Good - triggers, pains | Deep - 3 levels of JTBD (functional/emotional/social) | **v2** |

### 3. Positioning

| Criteria | v1 | v2 | Winner |
|----------|----|----|--------|
| Main message | Strong - park 3ha + center + price | Strong - same core | Tie |
| Competitor repositioning | Differentiation described | Explicit repositioning per competitor (Trout/Ries style) | **v2** |
| ERRC matrix (Blue Ocean) | Yes - 4 elements | No | **v1** |
| "Own a word" (Trout) | Implicit | Explicit: "ПАРК" | **v2** |
| Schwartz levels per segment | No | Yes - 3 segments mapped to stages | **v2** |

### 4. Landing Page Audit

| Criteria | v1 | v2 | Winner |
|----------|----|----|--------|
| Blockers identified | 2 (Метрика, коллтрекинг) | 2 (same) | Tie |
| Recommendations | 5 items | 6 items | Tie |
| StoryBrand framework applied | Yes | No | **v1** |
| 152-ФЗ check | Basic | Detailed (text of policy, link verification) | **v2** |

### 5. Channels & Budget

| Criteria | v1 | v2 | Winner |
|----------|----|----|--------|
| Channel selection | YD + VK + classifieds + retargeting | Same + explicit reserve/test budget | **v2** |
| Budget split logic | 55% YD, 30% VK, 13% classifieds, 2% retarget | 45% YD, 25% VK, 20% classifieds, 5% retarget, 5% reserve | **v2** (more balanced) |
| YD structure (Prais) | Described in roadmap | Detailed month 1 structure with exact campaign types | **v2** |
| VK structure | Basic - 2 campaigns | 7-point structure with audience groups, formats, budgets | **v2** |
| Anti-patterns applied | 3 (Google Ads, ОЗК, Товарный МК) | Same 3 | Tie |

### 6. Messaging

| Criteria | v1 | v2 | Winner |
|----------|----|----|--------|
| Messages per segment | 7 rows | 7 rows | Tie |
| Ad formula models | 3 (AIDA, ODC, 4U) | 3 (same) + creative matrix by audience temperature | **v2** |
| Quality of hooks | Good | Good, slightly more emotional | **v2** (marginal) |

### 7. KPI & Roadmap

| Criteria | v1 | v2 | Winner |
|----------|----|----|--------|
| KPI targets | CPL, conversions, timeline | Same + explicit lead quality recommendation (CRM training) | **v2** |
| Roadmap | Monthly (3 months) | Weekly (month 1) + monthly (months 2-3) | **v2** |
| Operational metrics | 5 items for first 3 weeks | Focused on same items | Tie |

---

## Scorecard Summary

| Category | v1 wins | v2 wins | Tie |
|----------|---------|---------|-----|
| Market Analysis | 0 | 2 | 1 |
| Target Audience | 0 | 2 | 2 |
| Positioning | 1 | 3 | 1 |
| Landing Page | 1 | 1 | 2 |
| Channels & Budget | 0 | 3 | 2 |
| Messaging | 0 | 2 | 1 |
| KPI & Roadmap | 0 | 1 | 2 |
| **TOTAL** | **2** | **14** | **11** |

---

## Key Findings

### RLM Advantages:
1. **Deeper framework application** - v2 applied JTBD 4 forces, Schwartz per-segment, Trout "own a word" more precisely. By reading targeted sections, the agent absorbed and applied them better.
2. **More structured channel plans** - VK structure had 7 points vs generic 2 campaigns. YD structure followed Prais algorithm more precisely.
3. **Better budget allocation** - v2 included test/reserve budget (5%), more realistic retargeting budget (5% vs 2%), better classifieds allocation.
4. **Creative matrix** - v2 added temperature-based creative strategy (hot/warm/broad/retarget), absent in v1.
5. **34% fewer tokens** - significant cost savings at scale.

### v1 Advantages:
1. **ERRC matrix** (Blue Ocean) - v1 included it, v2 didn't. Because v2 didn't read Blue Ocean book (decided it wasn't needed). Minor loss.
2. **StoryBrand on landing page** - v1 applied StoryBrand framework to LP audit recommendation. v2 didn't read StoryBrand.
3. **Predictability** - v1 always reads the same sources, so output quality is more predictable.

### Neutral:
1. **Duration was nearly identical** (~4 min each). RLM's savings in tokens are offset by grep/navigation overhead. At scale with bigger KB, RLM should be faster.
2. **Both respected all T1 anti-patterns** (no Google Ads, no ОЗК, no Товарный МК month 1).
3. **Both hit the same KPI targets** and overall strategy direction.

---

## Verdict

**v2 (RLM) wins 14:2** on quality while consuming 34% fewer tokens and 51% fewer tool calls.

The concern that RLM agents might miss relevant KB sections proved partially valid (Blue Ocean, StoryBrand were skipped), but the impact was marginal - v2 compensated by going deeper on the sources it DID read.

### Recommendation:
- **Switch default to v2 (RLM) for strategist agent**
- Add Blue Ocean and StoryBrand to the "must-read for strategist" list in the startup-sequence
- Monitor "KB Sources Used" in first 5 real briefs to catch any systematic gaps
- Keep v1 as fallback
