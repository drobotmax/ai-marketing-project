# News Pipeline - Dependency Map

Which files to update when platform changes are detected.

## File Whitelist

The pipeline is ONLY allowed to edit these files/directories:

### Platform specs (central reference)
- `agents/references/platform-specs.md`

### Knowledge base
- `knowledge/meta-ads/**/*.md`
- `knowledge/google-ads/**/*.md`
- `knowledge/yandex-direct-course/**/*.md`

### Agent definitions
- `agents/strategist/skill.md`
- `agents/targeting/skill.md`
- `agents/media-buyer/skill.md`
- `agents/copywriter/skill.md`
- `agents/validator/skill.md`
- `agents/contextologist/skill.md`
- `agents/sales-qa/skill.md`

### Pipeline own files
- `news-pipeline/changelog.md`

## Dependency Map

### Meta Ads changes

| Change type | platform-specs.md | KB path | Agent files |
|-------------|-------------------|---------|-------------|
| Char limits (feed, stories, reels) | Update table row | `meta-ads/formaty-reklamy/` | copywriter, validator |
| Policy changes | Update policy section | `meta-ads/pravila/` | validator, targeting |
| Housing ad restrictions | Update housing section | `meta-ads/pravila/` | targeting |
| New ad format | Add new section | Create file in `meta-ads/formaty-reklamy/` | copywriter, media planner |
| CTA button list | Update CTA list | `meta-ads/formaty-reklamy/` | copywriter |
| Audience/targeting changes | - | `meta-ads/auditorii/` | targeting |
| Conversions API changes | - | `meta-ads/meropriyatiya-sobytiya/` | targeting, contextologist |

### Google Ads changes

| Change type | platform-specs.md | KB path | Agent files |
|-------------|-------------------|---------|-------------|
| RSA char limits | Update table row | `google-ads/campaigns/search-campaigns.md` | copywriter, validator, contextologist |
| Display char limits | Update table row | `google-ads/campaigns/display-campaigns.md` | copywriter, validator |
| Policy changes | Update policy section | `google-ads/fix-issues/policy-issues.md` | validator, contextologist |
| Smart Bidding threshold | - | `google-ads/explore-features/bidding.md` | contextologist |
| Performance Max changes | - | `google-ads/campaigns/` | contextologist, media planner |
| AI Max for Search | - | `google-ads/campaigns/ai-max-for-search-campaigns.md` | contextologist |
| Keyword match type changes | - | `google-ads/explore-features/keywords.md` | contextologist |
| New campaign type | Add section | Create file in `google-ads/campaigns/` | contextologist, media planner |

### Yandex Direct changes

| Change type | platform-specs.md | KB path | Agent files |
|-------------|-------------------|---------|-------------|
| Char limits (search, YAN) | Update table row | `yandex-direct-course/` | contextologist, validator |
| New ad format | Add section | Create file in `yandex-direct-course/` | contextologist, copywriter |
| Bidding strategy changes | - | `yandex-direct-course/` | contextologist |
| Master of campaigns | - | `yandex-direct-course/` | contextologist |

## Classification Rules

### When to update KB (actionable)
- **spec_change**: platform officially changed character limits, API specs, technical requirements
- **policy_update**: new ad policy rules, restrictions, compliance requirements
- **new_feature**: new ad format, campaign type, targeting option, measurement tool
- **deprecation**: feature being removed, API sunset, format discontinued

### When NOT to update KB (notify only)
- Industry commentary or opinion pieces
- Case studies or best practices (unless they reveal undocumented features)
- Conference announcements without specific product changes
- Blog posts about general trends
- Telegram posts without official source reference

### Confidence rules
- Official blog post (Google, Meta, Yandex) -> high confidence, can update specs
- Help Center / documentation update -> highest confidence
- Telegram channel post -> low confidence, notify_only unless links to official source
- If confidence < 80% -> classify as notify_only, flag for human review
