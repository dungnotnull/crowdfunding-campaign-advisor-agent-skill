# Cluster Sub-Skills Catalog — Marketing, Content & Branding

> Reusable sub-skills for the marketing-content-branding cluster. Shared across sibling skills to avoid duplication.

## Available Sub-Skills

### sub-audience-analysis

**Purpose:** Profile target audience, their channels, and pre-launch audience-building strategy.

**Used By:** `crowdfunding-campaign-advisor`, [future: landing-page-advisor, email-campaign-advisor]

**Inputs:**
- Campaign context and description
- Target audience description (if available)
- Current audience assets (email list, social following, etc.)

**Outputs:**
- Structured audience profile with demographics and psychographics
- Channel recommendations with evidence
- Pre-launch audience-building plan
- Audience alignment score (0-100)

**Tools Required:**
- WebSearch (for audience research)
- WebFetch (for platform analytics)
- Read, Write, Bash

**Quality Gates:**
- Output is schema-valid (structured JSON/object)
- Every claim cites a framework or source
- Recommendations are specific and actionable

**Framework References:**
- Pre-launch funnel research
- Platform audience analytics
- Audience-building best practices

---

### sub-compliance-check

**Purpose:** Screen platform rules, fulfillment realism, and claims for misleading/regulated content.

**Used By:** `crowdfunding-campaign-advisor`, [future: product-launch-advisor, ad-copy-reviewer]

**Inputs:**
- Campaign claims and promises
- Reward tiers or product specifications
- Fulfillment plan and cost estimates
- Target jurisdictions

**Outputs:**
- Compliance risk assessment
- Platform rule violations flagged
- Fulfillment realism check
- Recommended disclaimers

**Tools Required:**
- WebSearch (for platform rules)
- WebFetch (for legal/regulatory references)
- Read, Write, Bash

**Quality Gates:**
- Schema-valid output
- Claims traceable to platform rules or regulations
- Clear distinction between guidance and legal advice

**Compliance Rules:**
- Do not present output as binding legal/official advice
- Identify governing jurisdiction(s)
- Recommend qualified professional for regulated content
- Block deliverable if mandatory compliance element missing

**Framework References:**
- Platform terms of service
- Consumer protection regulations
- Truth-in-advertising guidelines

---

### sub-quality-reviewer

**Purpose:** Score content across multiple dimensions against frameworks; flag weak elements.

**Used By:** `crowdfunding-campaign-advisor`, [future: landing-page-advisor, pitch-deck-advisor]

**Inputs:**
- Content to review (campaign, page, deck, etc.)
- Target audience context
- Business goals and constraints

**Outputs:**
- Multi-dimensional scores (0-100 each)
- Findings by dimension (strengths, risks, gaps)
- Framework citations per score
- Overall quality assessment

**Tools Required:**
- WebSearch (for benchmarks and case studies)
- WebFetch (for competitive analysis)
- Read, Write, Bash

**Quality Gates:**
- All scores reference named frameworks
- Every material claim cites evidence
- Findings are specific and actionable

**Framework References:**
- AIDA / narrative structure
- Value proposition clarity
- CTA effectiveness research
- Visual hierarchy principles

---

### sub-improvement-roadmap

**Purpose:** Recommend prioritized fixes with impact/effort ranking.

**Used By:** `crowdfunding-campaign-advisor`, [future: all quality-reviewer users]

**Inputs:**
- Quality review findings and scores
- User constraints (time, budget, resources)
- Priority dimensions

**Outputs:**
- Prioritized improvement list
- Impact/effort matrix for each action
- Sequencing recommendations
- Expected score improvement estimates

**Tools Required:**
- Read, Write, Bash

**Quality Gates:**
- Recommendations follow from findings
- Impact/effort assessments are realistic
- Roadmap is sequenced logically

**Framework References:**
- Impact/effort prioritization
- Minimum viable product principles
- Iterative improvement best practices

---

## Integration Guidelines

### When Adding a New Skill to the Cluster

1. Check if existing sub-skills can be reused
2. Add your skill to "Used By" lists for relevant sub-skills
3. Follow the standard scoring schema for dimensions
4. Document any new sub-skills in this catalog

### When Modifying an Existing Sub-Skill

1. Ensure backward compatibility for existing users
2. Update this catalog with any changes to inputs/outputs
3. Run regression tests on all dependent skills
4. Update version if breaking changes are necessary

## Cluster Coherence

All sub-skills in this cluster share:
- **Standard scoring schema** (see `cluster-standard-scoring-schema.md`)
- **Evidence-first approach** — claims cite sources
- **Framework grounding** — no ad-hoc criteria
- **Quality gates** — validated before output
- **Tool dependencies** — WebSearch, WebFetch, Read, Write, Bash
