---
name: sub-compliance-check
description: Screen platform rules, reward-fulfillment realism, and claims for misleading/regulated content.
cluster: marketing-content-branding
reusable: true
used_by:
  - crowdfunding-campaign-advisor
---

## Role
Sub-skill of `crowdfunding-campaign-advisor`. Screen platform rules, reward-fulfillment realism, and claims for misleading/regulated content.

## Inputs
- The user-provided context plus the outputs of the preceding harness stage.
- Campaign claims and promises
- Reward tiers with descriptions and pricing
- Fulfillment plan and cost estimates
- Target jurisdictions for delivery

## Procedure

### Step 1: Platform Rules Compliance
Check against Kickstarter and Indiegogo platform rules:

**Forbidden Content Check:**
```yaml
prohibited_content_check:
  gambling_betting: false  # Cannot involve gambling or betting
  alcohol_tobacco: false  # May have restrictions depending on jurisdiction
  drugs_controlled_substances: false  # Strictly prohibited
  weapons_explosives: false  # Strictly prohibited
  hate_speech: false  # Strictly prohibited
  illegal_activities: false  # Strictly prohibited
  adult_content: false  # May have restrictions
  political_campaigning: false  # Platform may restrict
  pyramid_schemes: false  # Strictly prohibited
```

**Required Elements Check:**
```yaml
required_elements:
  clear_project_description: true
  realistic_funding_goal: true  # Will verify in fulfillment check
  tangible_rewards_or_deliverable: true
  honest_communication: true
  creator_identity_disclosure: true
  no_misleading_claims: true
```

**For each prohibited or required element:**
- Cite specific platform rule (e.g., "Kickstarter Prohibited Projects: Section 3")
- Flag severity: CRITICAL (must fix) / WARNING (should fix)
- Provide recommendation for compliance

### Step 2: Reward Fulfillment Realism
Analyze each reward tier for fulfillment feasibility:

**For each reward tier, assess:**
```yaml
reward_tier_analysis:
  tier_name: "Early Bird - $50"
  price: 50
  fulfillment_cost_breakdown:
    production_cost: 25
    packaging: 3
    shipping_domestic: 8
    platform_fees: 5  # ~8-10% of reward price
    payment_processing: 2  # ~3-5%
    total_cost: 43
    margin_per_unit: 7  # 14% margin
  margin_status: "ACCEPTABLE"  # ACCEPTABLE if >10%, THIN if 5-10%, NEGATIVE if <5%
  shipping_complexity: "Medium"  # Low/medium/high
  international_shipping: true
  international_pricing: "Add $15 for shipping"  # Must account for higher costs
  fulfillment_timeline: "6 months after campaign"
  timeline_realism: "REALISTIC"  # REALISTIC / AGGRESSIVE / UNREALISTIC
  volume_risk: "Medium"  # Assess if volume surge could break fulfillment
```

**Aggregate Fulfillment Assessment:**
```yaml
fulfillment_health:
  overall_margin_status: "ACCEPTABLE"
  average_margin_percentage: 18
  lowest_margin_tier: "Early Bird - $50 (14% margin)"
  shipping_complexity: "Medium - single-item rewards, manageable"
  timeline_feasibility: "Realistic based on product complexity"
  international_coverage: "All major markets with shipping add-ons"
  risks:
    - "Volume surge could strain logistics - consider fulfillment partner"
    - "International shipping costs may increase - build in buffer"
  recommendations:
    - "Increase lowest margin tier to $55 or reduce cost by $2"
    - "Consider fulfillment partner for orders >1000 units"
    - "Build 10% buffer into international shipping estimates"
```

### Step 3: Claims Validation and Regulatory Screening
Screen all claims for misleading statements or regulatory issues:

**Claims Analysis:**
```yaml
claims_review:
  performance_claims:
    claim: "30-day battery life"
    evidence_required: true
    status: "NEEDS_TESTING"  # VERIFIED / NEEDS_TESTING / MISLEADING
    recommendation: "Provide test data or qualify claim (e.g., 'up to 30 days')"
  regulatory_claims:
    claim: "FDA approved"
    status: "CRITICAL_ISSUE"
    recommendation: "Do not use without official FDA clearance. Consider 'Designed to meet FDA standards' instead."
  environmental_claims:
    claim: "100% sustainable"
    status: "POTENTIALLY_MISLEADING"
    recommendation: "Qualify with specifics: 'Made with 80% recycled materials'"
  guarantees_warranties:
    claim: "Lifetime warranty"
    status: "HIGH_RISK"
    recommendation: "Specify what 'lifetime' means and what's covered. Consider limited warranty instead."
```

**Regulated Categories Check:**
```yaml
regulated_categories:
  medical_devices:
    is_regulated: false
    guidance: "If making health claims, consult regulatory requirements"
  financial_products:
    is_regulated: false
    guidance: "Investment products have strict disclosure requirements"
  children_products:
    is_regulated: false
    guidance: "Products for children under 13 have safety and privacy requirements"
  food_beverage:
    is_regulated: false
    guidance: "May require ingredient disclosure, allergen warnings, certifications"
  software_apps:
    is_regulated: false
    guidance: "Privacy policy, terms of service required for data collection"
```

### Step 4: Jurisdiction and Legal Considerations
Identify legal requirements by target jurisdiction:

```yaml
jurisdiction_review:
  target_markets: ["United States", "European Union", "United Kingdom"]
  compliance_requirements:
    United_States:
      consumer_protection: "FTC truth-in-advertising guidelines apply"
      tax_obligations: "Sales tax may apply to rewards"
      certifications: "None required for this category"
    European_Union:
      consumer_protection: "EU Consumer Rights Cooperation regulations"
      tax_obligations: "VAT may apply to rewards"
      certifications: "CE marking required for electronic products"
    United_Kingdom:
      consumer_protection: "Consumer Protection from Unfair Trading Regulations"
      tax_obligations: "VAT registration if >£85,000 annually"
      certifications: "UKCA marking for certain products"
  disclaimer_requirement: true
  disclaimer_text: "This campaign does not constitute an offer to sell securities. Rewards are pre-orders, not investments. Delivery timelines are estimates and not guaranteed."
```

### Step 5: Compliance Scoring
Score overall compliance (0-100):

**Scoring Criteria:**
- **Platform rules adherence (0-30):** No prohibited content, all required elements present
- **Fulfillment realism (0-35):** All tiers have >10% margin, realistic timelines
- **Claims integrity (0-20):** No misleading claims, proper qualifications
- **Jurisdictional compliance (0-15):** Proper disclaimers, regulatory awareness

**Score Interpretation:**
- 90-100: Excellent compliance, minimal risk
- 70-89: Good compliance with minor issues to address
- 50-69: Moderate compliance issues, some fixes required before launch
- <50: Significant compliance problems, major revisions needed

### Step 6: Self-Check Against Quality Gate
Before returning control to the harness:

**Verify:**
- [ ] All platform rules were checked (both Kickstarter and Indiegogo)
- [ ] Each reward tier has cost breakdown and margin calculation
- [ ] All claims were screened for misleading statements
- [ ] Regulatory categories were checked and flagged if applicable
- [ ] Jurisdictions identified with specific compliance notes
- [ ] Disclaimers recommended where required
- [ ] Output is structured and parseable by next stage

**If any check fails:** Address the issue before proceeding. Flag CRITICAL issues that block launch.

## Outputs
- A structured result object consumed by the next stage:
```yaml
compliance_check_result:
  platform_rules_compliance:
    status: "COMPLIANT"  # COMPLIANT / MINOR_ISSUES / MAJOR_ISSUES
    prohibited_content_check: {all_clear: true}
    required_elements_check: {all_present: true}
    flagged_items: []
  fulfillment_analysis:
    status: "HEALTHY"  # HEALTHY / THIN_MARGINS / RISKY
    overall_margin_percentage: 18
    tier_analysis: [{tier, margin, status}]
    recommendations: ["Consider fulfillment partner for volume surge"]
  claims_review:
    status: "NEEDS_ATTENTION"  # CLEAR / NEEDS_QUALIFICATION / MISLEADING
    reviewed_claims: 5
    problematic_claims: 2
    required_qualifications: ["'30-day battery' -> 'up to 30 days'"]
  regulatory_screening:
    regulated_categories: false
    jurisdiction_requirements: {US: {...}, EU: {...}}
    disclaimer_required: true
    disclaimer_text: "..."
  compliance_score: 75  # 0-100
  critical_issues: []  # Empty if no critical blockers
  framework_citations:
    - "Kickstarter Prohibited Projects Guidelines"
    - "Indiegogo Trust & Safety Policy"
    - "FTC Truth-in-Advertising Guidelines"
  risks: ["Volume surge could strain fulfillment", "International shipping costs may vary"]
  recommendations: ["Add shipping buffer for international", "Qualify battery life claim"]
```

## Tools
WebSearch, WebFetch, Read, Write, Bash

## Quality Gate
- Output is schema-valid, framework-grounded, and every material claim is traceable to a source or a prior step.

## Compliance Rules
- Do not present output as binding legal/official advice.
- Identify the governing jurisdiction(s) and flag where they materially differ.
- Attach a disclaimer recommending a qualified, licensed professional.
- Block the final deliverable if a mandatory compliance element is missing.

## Framework References
- Platform terms of service (Kickstarter, Indiegogo)
- Consumer protection regulations (FTC, EU CPC, UK CPUTRs)
- Truth-in-advertising guidelines (FTC Endorsement Guides)
- Import/export regulations (customs, certifications)
