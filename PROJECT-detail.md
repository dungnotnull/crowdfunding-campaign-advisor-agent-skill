# PROJECT-detail.md — Crowdfunding Campaign Advisor (Kickstarter / Indiegogo)

## Executive Summary
This skill is a full Claude harness that turns design and score crowdfunding campaigns: rewards, story, funding goal, and launch plan. It operates research-first: every material judgment is grounded in a named, citable framework and, where possible, a freshly retrieved source. It produces a professional-grade deliverable: a multi-dimensional score against the chosen framework plus a prioritized, effort/impact-ranked improvement roadmap.

## Problem Statement
First-time creators launch crowdfunding campaigns with weak stories, mispriced rewards, and no pre-launch audience, then fail to fund. This skill designs and scores a campaign across the proven success factors, models the funding goal and reward economics, and continuously updates with record-breaking campaign structures.

## Target Users & Use Cases
Primary users are practitioners and decision-makers in the **Marketing, Content & Branding** domain. Trigger examples:
1. Creator has a hardware idea; skill structures reward tiers and models the funding goal vs cost.
2. Campaign story is feature-dumping; quality reviewer rewrites it as a problem-solution narrative.
3. Creator has no audience; skill builds a pre-launch funnel and 'first 48 hours' plan.
4. Reward fulfillment looks unrealistic; compliance check flags the margin/shipping risk.
5. User asks if stretch goals help; skill advises based on success-factor research.
6. Skill outputs a scored campaign blueprint with a launch calendar.

## Harness Architecture
```
/crowdfunding-campaign-advisor (main.md harness)
  -> sub-audience-analysis              [intake / framing]
  -> sub-compliance-check              [framework selection / risk-scope screen]
  -> knowledge refresh   [SECOND-KNOWLEDGE-BRAIN via knowledge_updater.py]
  -> sub-quality-reviewer              [multi-dimensional scoring]
  -> evidence + challenge gate
  -> improvement roadmap [prioritized, effort/impact]
  -> SYNTHESIZE          [final scored deliverable]
```

## Full Sub-Skill Catalog
### sub-audience-analysis
- **Purpose:** Profile the target backers, their channels, and the pre-launch audience-building plan.
- **Inputs:** outputs of the prior stage + user-provided context.
- **Outputs:** structured findings passed to the next stage.
- **Tools:** WebSearch, WebFetch, Read, Write, Bash
- **Quality gate:** output is schema-valid, evidence-linked, and framework-grounded before the harness proceeds.
### sub-compliance-check
- **Purpose:** Screen platform rules, reward-fulfillment realism, and claims for misleading/regulated content.
- **Inputs:** outputs of the prior stage + user-provided context.
- **Outputs:** structured findings passed to the next stage.
- **Tools:** WebSearch, WebFetch, Read, Write, Bash
- **Quality gate:** output is schema-valid, evidence-linked, and framework-grounded before the harness proceeds.
### sub-quality-reviewer
- **Purpose:** Score the campaign across story, video, rewards, goal, and launch plan; flag weak elements.
- **Inputs:** outputs of the prior stage + user-provided context.
- **Outputs:** structured findings passed to the next stage.
- **Tools:** WebSearch, WebFetch, Read, Write, Bash
- **Quality gate:** output is schema-valid, evidence-linked, and framework-grounded before the harness proceeds.
### sub-improvement-roadmap
- **Purpose:** Recommend prioritized fixes to rewards, narrative, goal, and launch sequencing with impact.
- **Inputs:** outputs of the prior stage + user-provided context.
- **Outputs:** structured findings passed to the next stage.
- **Tools:** WebSearch, WebFetch, Read, Write, Bash
- **Quality gate:** output is schema-valid, evidence-linked, and framework-grounded before the harness proceeds.

## Skill File Format Specification
Every skill file uses YAML frontmatter (`name`, `description`) followed by the required sections: Role & Persona, Workflow (Harness Flow), Sub-skills Available, Tools, Output Format, Quality Gates. The main harness invokes sub-skills via the Skill tool in the order shown above.

## E2E Execution Flow
1. Parse the user request; if inputs are insufficient, `sub-audience-analysis` asks targeted intake questions.
2. `sub-compliance-check` selects the governing framework(s) and screens scope/risk; branch to a refusal or disclaimer if out of scope.
3. Refresh knowledge if the brain is stale (>7 days) and WebSearch/WebFetch are available; otherwise degrade gracefully to internal knowledge with a stated limitation.
4. `sub-quality-reviewer` scores each dimension, citing evidence per claim.
5. Run the evidence/quality gate(s) and a devil's-advocate challenge pass.
6. Emit the scored report + roadmap in the Output Format below.

## SECOND-KNOWLEDGE-BRAIN Integration
- **Sources:** Kickstarter / Indiegogo platform guidelines and stats; Academic crowdfunding-success research (Mollick et al.); Reputable campaign post-mortems and case studies; Google Scholar for crowdfunding-dynamics studies; Marketing/funnel best-practice publications
- **Crawl config:** see `tools/knowledge_updater.py` (ArXiv categories econ.GN, cs.CY; domain queries seeded from the idea).
- **Append format:** date-stamped entries with Title, Authors, Year, Venue, DOI/URL, key finding, relevance note; deduplicated by URL/DOI hash.

## Supporting Tools Spec — knowledge_updater.py
- **Inputs:** search queries + source list (in-file config), optional `--since` date.
- **Outputs:** appended entries in `SECOND-KNOWLEDGE-BRAIN.md` + a run log.
- **Schedule:** weekly cron (graceful no-op when offline).

## Quality Gates
- **Evidence gate:** every material claim is traceable to a cited source or a prior step; prefer the highest evidence tier available.
- **Framework gate:** all scoring is grounded in the named frameworks below — never ad-hoc criteria.
- **Challenge gate:** a devil's-advocate pass has stress-tested the recommendation before it is shown.

## Test Scenarios
See `tests/test-scenarios.md` (>=5 concrete scenarios with expected harness behavior).

## Key Design Decisions
1. Framework-grounded scoring only — no ad-hoc rubrics.
2. Research-first with graceful degradation when offline.
3. Composable sub-skills (>=3) so cluster siblings can reuse them.
4. Deliverable is an artifact (scored report + roadmap), not a chat reply.
5. Evidence/quality gate enforced before any sensitive/regulated output.
