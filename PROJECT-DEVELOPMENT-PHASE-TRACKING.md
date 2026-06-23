# PROJECT-DEVELOPMENT-PHASE-TRACKING.md — Crowdfunding Campaign Advisor (Kickstarter / Indiegogo)

## Phase 0 — Research & Skill Architecture  ✅
- Tasks: identify domain frameworks (Crowdfunding success-factor research (early-backer momentum, video, social proof); …), map cluster sub-skill patterns, define knowledge sources.
- Deliverables: framework shortlist, source list, harness sketch.
- Success criteria: every scoring dimension maps to a named framework.
- Effort: S.

## Phase 1 — Core Sub-Skills  ✅
- Tasks: implement 4 sub-skills (sub-audience-analysis, sub-compliance-check, sub-quality-reviewer, sub-improvement-roadmap).
- Deliverables: `skills/sub-*.md` with explicit quality gates.
- Success criteria: each sub-skill has typed inputs/outputs and a gate.
- Effort: M.

## Phase 2 — Main Harness + Quality Gates  ✅
- Tasks: write `skills/main.md`, wire sub-skill invocation order, add evidence + challenge gates.
- Deliverables: runnable harness entry point.
- Success criteria: harness refuses/degrades correctly on bad or out-of-scope input.
- Effort: M.

## Phase 3 — SECOND-KNOWLEDGE-BRAIN Pipeline  ✅ (scaffold)
- Tasks: implement `tools/knowledge_updater.py` (crawl4ai + WebSearch, score, dedupe, append).
- Deliverables: working updater + seeded brain.
- Success criteria: a dry run produces deduplicated, date-stamped entries.
- Effort: M. Status: scaffold complete; first live crawl batch pending.

## Phase 4 — Testing & Validation  ✅
- Tasks: run the 6 test scenarios; capture expected vs actual.
- Deliverables: `tests/test-scenarios.md` + regression fixtures.
- Success criteria: all scenarios pass the quality gates.
- Effort: M. Status: complete — test runner implemented, fixtures generated, all gates passing.

## Phase 5 — Integration & Cross-Skill Wiring  ✅
- Tasks: share cluster sub-skills with sibling `marketing-content-branding` skills; standardize scoring schema.
- Deliverables: shared sub-skill references.
- Success criteria: no duplicated logic across cluster siblings.
- Effort: S. Status: complete — standard scoring schema documented, sub-skills cataloged and metadata added.
