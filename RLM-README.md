# KUBRIK RLM (Recursive Language Models) Integration

## What is RLM?

RLM - подход, при котором LLM не получает весь контекст (KB) в промпт сразу, а навигирует по нему динамически через REPL (Read/Grep/Glob), подтягивая только нужные секции.

Paper: https://arxiv.org/abs/2512.24601v1
Blog: https://alexzhang13.github.io/blog/2025/rlm/

## Architecture

```
v1 (Static KB):
  Agent prompt + [ALL KB files] -> Generate output

v2 (RLM):
  Agent prompt + [KB-INDEX.md] -> Agent reads index
    -> Agent greps/reads relevant sections on demand
    -> Agent generates output
    -> Agent logs "KB Sources Used"
```

## Files

### New files (RLM v2):
- `knowledge/KB-INDEX.md` - structured manifest of all 127K lines of KB
- `~/.claude/skills/kubrik-pipeline/agents/rlm/kb-navigator.md` - shared navigation rules
- `~/.claude/skills/kubrik-pipeline/agents/rlm/strategist.md` - RLM strategist
- `~/.claude/skills/kubrik-pipeline/agents/rlm/copywriter.md` - RLM copywriter
- `~/.claude/skills/kubrik-pipeline/agents/rlm/targeting.md` - RLM targeting
- `~/.claude/skills/kubrik-pipeline/agents/rlm/contextologist.md` - RLM contextologist
- `~/.claude/skills/kubrik-pipeline/agents/rlm/media-buyer.md` - RLM media buyer
- `~/.claude/skills/kubrik-pipeline/agents/rlm/validator.md` - RLM validator

### Modified files:
- `~/.claude/skills/kubrik-pipeline/SKILL.md` - added version switch section, `| RLM:` references

### Untouched (v1):
- `~/.claude/skills/kubrik-pipeline/agents/strategist/skill.md`
- `~/.claude/skills/kubrik-pipeline/agents/copywriter/skill.md`
- `~/.claude/skills/kubrik-pipeline/agents/targeting/skill.md`
- `~/.claude/skills/kubrik-pipeline/agents/contextologist/skill.md`
- `~/.claude/skills/kubrik-pipeline/agents/media-buyer/skill.md`
- `~/.claude/skills/kubrik-pipeline/agents/validator/skill.md`

## Usage

```bash
# v1 (default, unchanged behavior)
/kubrik-pipeline
/kubrik-pipeline strategist

# v2 (RLM mode)
/kubrik-pipeline --rlm
/kubrik-pipeline strategist --rlm
```

## Rollback

RLM is **fully additive** - no existing files were modified except SKILL.md (which only got new sections added).

### Quick rollback (just stop using --rlm):
Don't pass `--rlm` flag. Pipeline uses v1 agents by default.

### Full cleanup (remove all RLM files):
```bash
# Remove RLM agent files
rm -rf ~/.claude/skills/kubrik-pipeline/agents/rlm/

# Remove KB index
rm ~/kubrik/knowledge/KB-INDEX.md

# Remove this README
rm ~/kubrik/RLM-README.md

# Revert SKILL.md changes (remove version switch section and | RLM: references)
# Or: git checkout ~/.claude/skills/kubrik-pipeline/SKILL.md
```

## Testing Plan

### Phase 1: A/B comparison on one agent (Strategist)
1. Take an existing brief (e.g., from clients/)
2. Run: `/kubrik-pipeline strategist` (v1) -> save output as strategy-v1.md
3. Run: `/kubrik-pipeline strategist --rlm` (v2) -> save output as strategy-v2.md
4. Compare: quality, relevance, KB coverage, missed info

### Phase 2: A/B comparison on full pipeline
1. Run full pipeline v1 and v2 on same brief
2. Compare final packages

### Phase 3: Measure on 3-5 real briefs
Key metrics:
- **Quality:** does the output cover all required sections?
- **KB relevance:** did RLM agent pull the right sources?
- **KB waste:** did v1 agent load unnecessary sources?
- **KB Sources Used section:** is the audit trail useful?
- **Cost:** context tokens consumed (v1 loads everything, v2 loads selectively)

## Expected Benefits

1. KB can grow to 500K+ lines without quality degradation
2. Agents use only relevant knowledge per task
3. Audit trail (KB Sources Used) shows what informed each decision
4. Cheaper per-run (less context = fewer tokens)
5. Each agent can develop its own navigation strategy

## Known Limitations

1. Agent may miss relevant KB if KB-INDEX.md description is insufficient
2. Extra tool calls (Read/Grep) add latency
3. No caching between agents in same pipeline run (each re-reads KB-INDEX)
4. Requires KB-INDEX.md to be maintained as KB grows
