# CLAUDE.md — Crowdfunding Campaign Advisor (Kickstarter / Indiegogo)

**Skill slug:** `crowdfunding-campaign-advisor`
**Source idea:** #186 (Vietnamese backlog `ideas.md`)
**Cluster:** marketing-content-branding — Marketing, Content & Branding
**Tagline:** Design and score crowdfunding campaigns: rewards, story, funding goal, and launch plan.
**Current phase:** Phase 4 — Testing & Validation (initial build complete)

## Problem This Skill Solves
First-time creators launch crowdfunding campaigns with weak stories, mispriced rewards, and no pre-launch audience, then fail to fund. This skill designs and scores a campaign across the proven success factors, models the funding goal and reward economics, and continuously updates with record-breaking campaign structures.

## Harness Flow (Summary)
1. **Intake** → `sub-audience-analysis` gathers inputs and frames the problem.
2. **Screen / select** → `sub-compliance-check` selects the governing framework and screens risk/scope.
3. **Score / analyze** → `sub-quality-reviewer` produces a multi-dimensional score against named frameworks.
4. **Knowledge refresh** → optional `tools/knowledge_updater.py` run keeps SECOND-KNOWLEDGE-BRAIN.md current.
5. **Gate** → quality / evidence gates must pass.
6. **Synthesize** → main harness emits the scored deliverable + prioritized improvement roadmap.

## Sub-skills
- `skills/sub-audience-analysis.md` — Profile the target backers, their channels, and the pre-launch audience-building plan.
- `skills/sub-compliance-check.md` — Screen platform rules, reward-fulfillment realism, and claims for misleading/regulated content.
- `skills/sub-quality-reviewer.md` — Score the campaign across story, video, rewards, goal, and launch plan; flag weak elements.
- `skills/sub-improvement-roadmap.md` — Recommend prioritized fixes to rewards, narrative, goal, and launch sequencing with impact.

## Tools Required
WebSearch, WebFetch, Read, Write, Bash

## Knowledge Sources (for crawl + reasoning)
- Kickstarter / Indiegogo platform guidelines and stats
- Academic crowdfunding-success research (Mollick et al.)
- Reputable campaign post-mortems and case studies
- Google Scholar for crowdfunding-dynamics studies
- Marketing/funnel best-practice publications

## Supporting Python Tools
- `tools/knowledge_updater.py` — crawl4ai + WebSearch pipeline that fetches latest papers/reports from the domain sources above, scores by recency + relevance, deduplicates by URL/DOI hash, and appends to `SECOND-KNOWLEDGE-BRAIN.md`. Recommended schedule: weekly cron.

## Active Development Tasks
- [x] Scaffold all required deliverables
- [x] Define >=3 sub-skills with quality gates
- [x] Ground scoring in named world-renowned frameworks
- [x] Wire knowledge_updater crawl sources
- [ ] Expand SECOND-KNOWLEDGE-BRAIN with first live crawl batch
- [ ] Add regression fixtures from the test scenarios

## Reference Docs (this folder)
- `PROJECT-detail.md` — full technical spec
- `PROJECT-DEVELOPMENT-PHASE-TRACKING.md` — phase roadmap
- `SECOND-KNOWLEDGE-BRAIN.md` — self-improving knowledge base
- `skills/main.md` — harness entry point
