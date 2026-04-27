# KUBRIK Knowledge Base Index

> This file is the entry point for RLM (Recursive Language Model) agents.
> Instead of reading all KB files, agents read THIS index and then pull only what they need.

## How to use this index

1. Read this file to understand what knowledge is available
2. Based on your task, decide which sections are relevant
3. Use `Glob` and `Read` to pull specific files/sections
4. If a file is large (500+ lines) - read its README first, then relevant sections

## Knowledge Hierarchy

**T1 > T2 > T3 > T4** - when sources conflict, higher tier wins.

- **T1: Team Playbooks** - real experience from campaigns (anti-patterns, what didn't work)
- **T2: Courses & Books** - structured training materials
- **T3: Platform Reference** - technical specs, policies, limits
- **T4: Model Knowledge** - LLM's own training data (last resort)

---

## Wiki Layer (синтез поверх sources)

### wiki/ (synthesis layer)
Синтезированные страницы с cross-links, поддерживаемые агентом.
Сырые sources не меняются. Wiki - компактные, actionable, с привязкой к KUBRIK.

- `_schema.md` - правила формата, типы страниц, правила поддержки
- **concepts/** - атомарные концепции и фреймворки:
  - `awareness-levels.md` - 5 уровней осведомленности (Schwartz)
  - `jtbd.md` - Jobs to Be Done (Christensen + Miller)
  - `slippery-slide.md` - Скользкая горка (Sugarman)
  - `positioning.md` - Позиционирование + Blue Ocean (Trout/Ries + Kim/Mauborgne)
  - `persuasion-principles.md` - 7 принципов убеждения (Cialdini)
  - `storybrand.md` - StoryBrand SB7 framework (Miller)
- **comparisons/** - X vs Y с практическими выводами:
  - `meta-vs-vk-targeting.md` - Meta vs VK: таргетинг, аудитории, CPL
- **playbooks/** - синтез из нескольких источников в процесс:
  - `write-cold-copy.md` - копирайтинг для холодной аудитории (4 книги + курс + anti-patterns)

**When to read:** Wiki pages FIRST, raw sources only when deeper detail needed.
**Tier:** наследует от самого высокого источника (если включает T1 - значит T1).

---

## T1: Team Experience

### team-playbooks/ (81 lines)
- `anti-patterns.md` - what didn't work in real campaigns
- `README.md` - index
- **When to read:** ALWAYS for any campaign generation. Small file, high value.

---

## T2: Courses & Books

### books/ (1274 lines, 12 files)
Canonical marketing frameworks extracted from key books.
- `README.md` - index of all books
- `breakthrough-advertising.md` - Schwartz: 5 levels of awareness
- `competing-against-luck.md` - Christensen: JTBD framework
- `building-a-storybrand.md` - Miller: StoryBrand 7-part framework
- `advert-secrets-written-word.md` - Sugarman: 24 psychological triggers, slippery slide
- `cialdini-influence.md` - Cialdini: 7 principles of persuasion
- `blue-ocean-strategy.md` - Kim/Mauborgne: ERRC grid, value innovation
- `positioning-battle-for-mind.md` - Trout/Ries: positioning
- `100m-offers.md` - Hormozi: offer construction, value equation
- **When to read:** Strategist reads all. Copywriter reads Sugarman, Cialdini, Schwartz.

### copywriting-course/ (16979 lines, 41 files)
Full copywriting course "Sdelaem" - 40 lessons.
- `copywriting-course-full.md` (8572 lines) - compiled version, all lessons
- `lesson-XX.md` - individual lessons
- **Key lessons for ads:**
  - Lessons 01-05: fundamentals, research, structure
  - Lessons 10-15: headlines, hooks, AIDA
  - Lessons 20-25: emotional triggers, storytelling
  - Lessons 30-35: platform-specific writing
  - Lessons 36-40: testing, iteration
- **When to read:** Copywriter agent. Read lesson index, then relevant lessons by task.

### targeting-course/ (195 lines)
Weberg targeting course - Meta/VK targeting fundamentals.
- `targeting-course-knowledge.md` - compiled KB from 27 video transcripts
- **When to read:** Targeting agent for Meta/VK campaigns.

### targeting-course-2/ (377 lines)
Advanced targeting - 51 videos, lookalikes, retargeting.
- `targeting-course-2-knowledge.md` - compiled KB
- `README.md` - index
- **When to read:** Targeting agent for advanced audience strategies.

### seo-course/ (2905 lines, 9 files)
SEO course with AI-era focus.
- `README.md` - index
- `seo-course-knowledge.md` (703 lines) - compiled KB
- Topic files: AI content ops, brand monitoring, technical hygiene, link building
- **When to read:** Only when SEO is part of the strategy.

---

## T2: Platform Courses (by market)

### yandex-direct-course/ (1715 lines) [MARKET: RF]
Prais launch algorithm + Yandex Metrica + real estate verticals.
- `README.md` - index
- `prais_launch_algorithm.md` - THE launch playbook for Yandex Direct
- `real-estate-primary/primary-real-estate-direct-playbook.md` (320 lines) - primary RE specifics
- `metrica-advanced/` - 3 files on Metrica: segmentation, reports, attribution
- **When to read:** Any RF campaign using Yandex Direct.

### vk-ads/ (1144 lines, 3 files) [MARKET: RF]
VK advertising: targeting course + lead forms + common errors.
- `voronin-vk-targeting-course.md` (631 lines) - Voronin 2025 course
- `vk-lead-forms-setup.md` - lead form best practices
- `elama-vk-common-errors.md` (294 lines) - anti-patterns from eLama
- **When to read:** Any RF campaign using VK.

### meta-ads/ (92140 lines, 17 files) [MARKET: International]
Meta Ads reference - audiences, deep links, policies.
- `README.md` - index
- `auditorii/polzovatelskie-auditorii.md` - custom audiences
- `auditorii/pohozhie-auditorii.md` - lookalike audiences
- `deep-links/` (14 files, ~90K lines) - Meta deep link reference docs
- **When to read:** International campaigns with Meta. Start with README. Deep-links only if specifically needed.
- **WARNING:** deep-links/ is 90K+ lines. NEVER read all at once. Grep for specific topic.

### google-ads/ (1313 lines) [MARKET: International only]
Google Ads account management, billing, security.
- `README.md` - index with sub-sections
- Sub-dirs: account-billing, campaigns, measurement, optimization
- **When to read:** International campaigns using Google Ads. NOT for RF market.

### google-analytics/ (3126 lines) [MARKET: Both]
GA4 setup, attribution, reporting.
- `README.md` - index
- Sub-dirs: advertising-attribution, analytics-360, policies-privacy
- **When to read:** When strategy includes analytics setup or attribution modeling.

### google-tagmanager/ (1321 lines) [MARKET: Both]
GTM setup, data layer, consent mode.
- `README.md` - index
- **When to read:** When strategy includes tag management or tracking setup.

### google-search-console/ (1315 lines) [MARKET: International]
GSC tasks, crawling, sitemaps.
- `README.md` - index
- **When to read:** Only for SEO-focused strategies.

### google-merchant-center/ (1555 lines) [MARKET: International]
Product feeds, shopping campaigns.
- `README.md` - index
- **When to read:** Only for e-commerce / product feed campaigns.

---

## T2: Market Data

### bali-market/ (1676 lines, 8 files)
Bali real estate market: developers, locations, listings, insights.
- `_index.md` - market overview
- `developers.md` (396 lines) - developer profiles
- `locations.md` - area comparisons
- `market-insights-mityuhin.md` (370 lines) - expert analysis
- `blackpoint-listings.md` - sample listings data
- **When to read:** Any Bali market campaign. Start with _index.md.

---

## T2: Methodology

### web-structure-methodology/
Reference process for designing websites: passport -> structure -> prototype -> TS. Based on UPH case (B2B industrial equipment catalog with B2G, dealers, scientific partners).
- `README.md` - when to apply + navigation
- `process.md` - stage-by-stage flow with artifacts, checkpoints, anti-patterns
- `structure-patterns.md` - blocks checklist for every page type of a B2B catalog site
- `client-questions.md` - questions to ask the client at each stage
- `transcripts/` - raw Whisper transcripts of the UPH case (structure walkthrough + client demo)
- **When to read:** Any request to design a website, landing, B2B catalog, or produce a site structure/prototype/TS. Especially for B2B / gov sector / manufacturing.

---

## T3: Platform Reference

### agents/references/platform-specs.md
Technical requirements for all ad platforms: character limits, image sizes, CTA options.
- **When to read:** Copywriter and Validator agents - for compliance checks.

---

## Quick Reference: Agent -> KB Mapping

| Agent | Always Read | Read if RF | Read if International |
|-------|------------|------------|----------------------|
| Strategist | team-playbooks/, **wiki/concepts/**, wiki/playbooks/ | yandex-direct-course/, vk-ads/, targeting-course/ | bali-market/ (or market/), meta-ads/README, google-ads/ |
| Targeting | team-playbooks/, **wiki/comparisons/**, targeting-course/, targeting-course-2/ | vk-ads/ | meta-ads/auditorii/ |
| Contextologist | team-playbooks/, yandex-direct-course/ | (RF-only agent) | N/A |
| Copywriter | team-playbooks/, **wiki/playbooks/write-cold-copy.md**, wiki/concepts/ | vk-ads/lead-forms, vk-ads/errors | meta-ads/README |
| Media Buyer | team-playbooks/, **wiki/comparisons/** | yandex-direct-course/prais | google-ads/, meta-ads/README |
| Validator | team-playbooks/, platform-specs.md | vk-ads/errors | meta-ads/README |

**Note:** wiki/ pages are compact synthesized summaries. If wiki covers a topic - read wiki first, go to raw sources only for deep detail.
