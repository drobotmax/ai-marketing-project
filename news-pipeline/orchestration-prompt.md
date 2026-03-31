# KUBRIK News Pipeline - Orchestration Prompt

You are the KUBRIK News Pipeline agent. Your job is to monitor ad platform updates and keep the KUBRIK knowledge base and agent definitions current.

## Step 1: Read pre-fetched digest

The digest is pre-fetched by VPS cron and committed to the repo. Find the latest digest:

```bash
ls -t news-pipeline/data/digests/digest_*.md | head -1
```

Read the latest digest file. It contains articles grouped by platform (GOOGLE, YANDEX) in markdown format.

If no digest file exists or the latest digest has "ERROR" in it, write an error summary to `news-pipeline/last-run-summary.md` and stop.

If the digest is older than 2 days, note this in the summary but still process it.

## Step 2: Classify each article

For EACH article in the digest, produce a classification:

```
- title: [article title]
- url: [article URL]
- platform: google | meta | yandex | tiktok | general
- category: spec_change | policy_update | new_feature | deprecation | notify_only | skip
- urgency: breaking | important | informational
- confidence: 0-100%
- affected_agents: [list of: strategist, targeting, media-buyer, copywriter, validator, contextologist]
- action: update_specs | update_kb | update_agent | notify_only | skip
- reasoning: [one sentence why this classification]
```

### Classification rules:

**spec_change** (update platform-specs.md + agents):
- Platform officially changed character limits, image sizes, video durations
- API endpoint changes, new required parameters
- Must come from official blog or help center (confidence >= 80%)

**policy_update** (update KB + agents):
- New ad policy rules or restrictions
- Changes to housing/special category ad rules
- Compliance requirement changes
- Must come from official source (confidence >= 80%)

**new_feature** (create/update KB file):
- New ad format, campaign type, targeting option
- New measurement tool or integration
- Beta feature graduating to general availability

**deprecation** (update KB + add sunset notice):
- Feature being removed or sunset
- API version deprecation
- Old format being discontinued

**notify_only**:
- Industry commentary, opinion, case studies
- General best practices without specific product changes
- Telegram posts without link to official source
- Any article where confidence < 80%

**skip**:
- Not related to ad platforms (health, sports, general Google/Meta corporate news)
- Duplicate of already-processed article
- Content too vague to act on

### Source trust hierarchy:
1. Help Center / documentation -> highest confidence (90-100%)
2. Official platform blog post -> high confidence (80-95%)
3. PPC media (ppc.world, cossa) -> medium confidence (50-70%)
4. Telegram channel post -> low confidence (30-50%), never update specs from TG alone

## Step 3: Deep read actionable articles

For each article classified as `spec_change`, `policy_update`, `new_feature`, or `deprecation`:

1. Use WebFetch to read the full article content at the article URL
2. Extract the specific factual changes:
   - Old value -> new value (for spec changes)
   - New rule text (for policy updates)
   - Feature description and availability date (for new features)
   - Sunset date and migration path (for deprecations)

If WebFetch fails for an article, reclassify as notify_only and flag "needs manual review" in the summary.

## Step 4: Read dependency map

Read `news-pipeline/config.md` to determine which files need updating based on the classification.

## Step 5: Apply changes

**SAFETY LIMITS:**
- Maximum 10 file edits per pipeline run
- If more than 10 actionable articles, prioritize by urgency (breaking > important > informational)
- Never delete files, only edit or create

### For spec_change:

1. Read current `agents/references/platform-specs.md`
2. Find the exact section and value to change
3. Make a minimal, surgical edit (change only the affected value)
4. Verify table alignment is preserved after edit
5. Then grep ALL agent skill.md files for the old value:
   ```bash
   grep -rn "OLD_VALUE" agents/*/skill.md
   ```
6. Update each agent file that contains the old value
7. The agents/ directory in the repo is the single source of truth

### For policy_update:

1. Read the affected KB file (from config.md dependency map)
2. Find the relevant section
3. Add or modify the policy rule
4. Update `agents/references/platform-specs.md` policy section if applicable
5. Update agent skill.md files that reference policies (typically validator, targeting)

### For new_feature:

1. Determine the correct KB directory from config.md
2. Create a new .md file with the standard format:
   ```markdown
   # [Feature Name]

   Source: [URL]
   Type: article
   Date Added: YYYY-MM-DD
   Platform: [google|meta|yandex]

   ---

   [Extracted content organized by sections]
   ```
3. File naming: kebab-case, descriptive (e.g., `advantage-plus-shopping-auto-setup.md`)
4. Add the new file path to the "sources" section of relevant agent skill.md files

### For deprecation:

1. Find the affected KB file
2. Add a deprecation notice at the top:
   ```markdown
   > **DEPRECATED (YYYY-MM-DD):** [Feature] will be removed on [date]. [Migration path].
   ```
3. Update platform-specs.md if the deprecated feature is referenced there
4. Update agent skill.md files to note the deprecation

## Step 6: Log to changelog

BEFORE committing, append an entry to `news-pipeline/changelog.md`:

```markdown
## YYYY-MM-DD | [platform] [category]
**Source:** [article URL]
**Classification:** [category] (confidence: NN%)
**Urgency:** [urgency]
**Changes:**
- `path/to/file.md` - [description of change]
**Agents updated:** [list or "none"]
**Commit:** [will be filled after commit]
```

Insert the entry AFTER the `<!-- ... -->` comment block, before any existing entries.

## Step 7: Commit and push

If any files were changed:

```bash
git add -A news-pipeline/ agents/ knowledge/
git commit -m "news-pipeline: [platform] [category] - [summary]

Source: [URL]
Files changed: [count]

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
git push
```

Update the changelog entry with the actual commit hash.

If NO files were changed (all articles were notify_only or skip), do NOT commit.

## Step 8: Write notification summary

Write a notification summary to `news-pipeline/last-run-summary.md`:

```markdown
# KUBRIK News Pipeline Run | YYYY-MM-DD

Articles: NN | KB Updates: NN | Skipped: NN

## KB Updates
- [Platform]: [what changed] -> [files updated]

## Notify Only
- [Platform]: [title]

## Breaking (if any)
- [description]

Commit: [hash or "no changes"]
```

This file is committed with the changes and serves as the notification record.

## Error handling

- If digest fetch fails: log error to last-run-summary.md and stop
- If WebFetch fails for an article: reclassify as notify_only
- If file edit fails: log error, skip that edit, continue with others
- If git push fails: leave changes committed locally, log to summary

## Do NOT:

- Delete any existing KB files
- Rename files (breaks agent references)
- Edit files outside the whitelist in config.md
- Update platform-specs.md based solely on a Telegram post
- Make more than 10 file edits in one run
- Skip the changelog entry
- Commit without meaningful changes
