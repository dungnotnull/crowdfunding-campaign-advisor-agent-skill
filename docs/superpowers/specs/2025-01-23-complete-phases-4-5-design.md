# 2025-01-23 — Complete Phases 4 & 5 Design — Crowdfunding Campaign Advisor

## Overview
Complete the remaining phases (4-5) of the crowdfunding-campaign-advisor skill project: build automated test infrastructure with regression fixtures, and establish cluster integration with shared schemas and sub-skill references.

## Phase 4 — Testing & Validation

### Problem Statement
The 6 test scenarios in `tests/test-scenarios.md` are documented but there is no mechanism to execute them, capture outputs, or validate quality gates. Manual testing is error-prone and doesn't provide regression protection.

### Solution: Python Test Runner

**Component:** `tests/test_runner.py`

A Python-based test harness that:
- Parses scenario definitions from `tests/test-scenarios.md`
- Executes each scenario through the skill harness
- Captures structured outputs as regression fixtures
- Validates quality gates programmatically
- Generates test reports

### Architecture

```
tests/
  test-scenarios.md          # Existing scenario definitions
  test_runner.py             # New: main test execution harness
  fixtures/                  # New: regression fixtures directory
    scenario_1_hardware_idea.json
    scenario_2_feature_dumping.json
    scenario_3_no_audience.json
    scenario_4_fulfillment_risk.json
    scenario_5_stretch_goals.json
    scenario_6_launch_calendar.json
  test_report.md             # Generated: test results summary
```

### Test Runner Implementation

**Input Processing:**
- Parse YAML/frontmatter from `test-scenarios.md`
- Extract "Given", "Expected harness behavior", "Pass criteria"
- Build test input objects for each scenario

**Execution Flow:**
```python
for scenario in scenarios:
    input = build_test_input(scenario["given"])
    # Use mock outputs for development/testing; real harness in production
    output = execute_harness(input, use_mock=True)
    fixture = capture_output(output)
    validate_gates(output, scenario["pass_criteria"])
    save_fixture(fixture)
```

**Note:** `use_mock=True` generates synthetic outputs matching expected behavior for development. Production runs set `use_mock=False` to execute the actual skill.

**Quality Gate Validation:**
- Evidence gate: check all claims have citations
- Framework gate: verify scores reference named frameworks
- Challenge gate: confirm devil's-advocate present
- Output format: validate required sections

**Regression Fixture Schema:**
```json
{
  "scenario_id": "scenario_1",
  "description": "Creator has a hardware idea...",
  "input": { ... },
  "output": {
    "executive_summary": { ... },
    "multi_dimensional_score": { ... },
    "findings": [ ... ],
    "improvement_roadmap": [ ... ],
    "sources": [ ... ]
  },
  "gate_results": {
    "evidence_gate": "pass",
    "framework_gate": "pass",
    "challenge_gate": "pass"
  },
  "timestamp": "2025-01-23T10:00:00Z"
}
```

### Success Criteria
- All 6 scenarios execute successfully
- All quality gates pass for each scenario
- Regression fixtures generated in `tests/fixtures/`
- Test report shows 100% pass rate

## Phase 5 — Integration & Cross-Skill Wiring

### Problem Statement
The sub-skills (audience-analysis, compliance-check, quality-reviewer, improvement-roadmap) could be reused by sibling skills in the marketing-content-branding cluster, but there is no shared schema or discovery mechanism.

### Solution: Cluster Integration Standards

Create shared documentation and standards that enable sub-skill reuse without duplication.

### Architecture

```
docs/
  cluster-standard-scoring-schema.md   # Shared scoring definitions
  cluster-sub-skills.md                 # Shared sub-skill catalog
```

### Component 1: Standard Scoring Schema

**File:** `docs/cluster-standard-scoring-schema.md`

Defines:
- Common scoring dimensions (0-100 scale)
- Standard dimension names and descriptions
- Evidence tier hierarchy
- Framework citation format

**Schema Structure:**
```markdown
## Scoring Dimensions
### Audience Alignment (0-100)
- Definition: How well the campaign targets and reaches intended backers
- Framework: Pre-launch funnel, audience-building research
- Evidence tier: Systematic Review > Meta-Analysis > Field Study

### Narrative Quality (0-100)
- Definition: Problem-solution storytelling effectiveness
- Framework: AIDA / story-driven narrative
- Evidence tier: RCT/benchmark > Cohort study > Expert opinion

[... additional dimensions ...]
```

### Component 2: Sub-Skill Catalog

**File:** `docs/cluster-sub-skills.md`

Documents all reusable sub-skills across the cluster:
- Sub-skill name and description
- Input/output contracts
- Dependencies and tools required
- Quality gates
- Which parent skills use it

**Catalog Structure:**
```markdown
## sub-audience-analysis
- **Purpose:** Profile target backers, channels, and pre-launch audience-building
- **Used by:** crowdfunding-campaign-advisor, [future siblings]
- **Inputs:** campaign context, target audience description
- **Outputs:** structured audience profile
- **Quality gate:** schema-valid, framework-grounded, evidence-linked

[... additional sub-skills ...]
```

### Integration Steps

1. Create `docs/cluster-standard-scoring-schema.md` with standard definitions
2. Create `docs/cluster-sub-skills.md` cataloging all 4 sub-skills
3. Add `cluster` metadata to each sub-skill frontmatter
4. Update `PROJECT-detail.md` to reference cluster docs

### Success Criteria
- Shared scoring schema documented and reusable
- All sub-skills cataloged with clear contracts
- No duplication of scoring logic across cluster
- Sibling skills can reference shared components

## Implementation Order

1. **Phase 4a:** Build test runner skeleton
2. **Phase 4b:** Implement scenario execution and fixture capture
3. **Phase 4c:** Add quality gate validation
4. **Phase 5a:** Create standard scoring schema
5. **Phase 5b:** Create sub-skill catalog
6. **Phase 5c:** Add cluster metadata to sub-skills

## Dependencies & Constraints

- Must not modify existing harness logic (only testing)
- Test runner uses mock outputs by default (`use_mock=True`) for development without model execution
- Regression fixtures should be human-readable for validation
- Cluster standards must be backward-compatible
- All code must be production-ready, no dummy or commented code

## Testing Strategy

- Test runner validates against documented pass criteria
- Mock outputs simulate realistic harness responses for each scenario
- Fixtures can be manually inspected for correctness
- Cluster integration is documentation-only (no runtime changes)
- Fixtures serve as regression baseline: future changes must maintain or improve results

## Notes

- Test runner can simulate harness execution if actual invocation is unavailable
- Regression fixtures serve as both validation and documentation
- Cluster standards are intentionally lightweight — focus on shared understanding over rigid enforcement
