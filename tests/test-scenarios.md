# tests/test-scenarios.md — Crowdfunding Campaign Advisor (Kickstarter / Indiegogo)

Scenario-based tests for the `crowdfunding-campaign-advisor` harness. Each scenario asserts the harness flow,
framework-grounded scoring, gate enforcement, and deliverable shape.

### Scenario 1
- **Given:** Creator has a hardware idea; skill structures reward tiers and models the funding goal vs cost.
- **Expected harness behavior:** intake confirms inputs → framework selected → `sub-quality-reviewer` scores against the named frameworks → evidence + challenge gate passed → scored report + prioritized roadmap emitted with citations.
- **Pass criteria:** all quality gates pass; every score cites its framework; roadmap items are effort/impact-ranked.
### Scenario 2
- **Given:** Campaign story is feature-dumping; quality reviewer rewrites it as a problem-solution narrative.
- **Expected harness behavior:** intake confirms inputs → framework selected → `sub-quality-reviewer` scores against the named frameworks → evidence + challenge gate passed → scored report + prioritized roadmap emitted with citations.
- **Pass criteria:** all quality gates pass; every score cites its framework; roadmap items are effort/impact-ranked.
### Scenario 3
- **Given:** Creator has no audience; skill builds a pre-launch funnel and 'first 48 hours' plan.
- **Expected harness behavior:** intake confirms inputs → framework selected → `sub-quality-reviewer` scores against the named frameworks → evidence + challenge gate passed → scored report + prioritized roadmap emitted with citations.
- **Pass criteria:** all quality gates pass; every score cites its framework; roadmap items are effort/impact-ranked.
### Scenario 4
- **Given:** Reward fulfillment looks unrealistic; compliance check flags the margin/shipping risk.
- **Expected harness behavior:** intake confirms inputs → framework selected → `sub-quality-reviewer` scores against the named frameworks → evidence + challenge gate passed → scored report + prioritized roadmap emitted with citations.
- **Pass criteria:** all quality gates pass; every score cites its framework; roadmap items are effort/impact-ranked.
### Scenario 5
- **Given:** User asks if stretch goals help; skill advises based on success-factor research.
- **Expected harness behavior:** intake confirms inputs → framework selected → `sub-quality-reviewer` scores against the named frameworks → evidence + challenge gate passed → scored report + prioritized roadmap emitted with citations.
- **Pass criteria:** all quality gates pass; every score cites its framework; roadmap items are effort/impact-ranked.
### Scenario 6
- **Given:** Skill outputs a scored campaign blueprint with a launch calendar.
- **Expected harness behavior:** intake confirms inputs → framework selected → `sub-quality-reviewer` scores against the named frameworks → evidence + challenge gate passed → scored report + prioritized roadmap emitted with citations.
- **Pass criteria:** all quality gates pass; every score cites its framework; roadmap items are effort/impact-ranked.

## Cross-cutting checks
- **Graceful degradation:** with WebSearch/WebFetch disabled, the harness still produces a deliverable and explicitly states the knowledge-currency limitation.
- **Refusal/scope:** out-of-scope or unsafe requests are refused or redirected.
- **Determinism of structure:** every run yields the six (or seven) Output-Format sections.
