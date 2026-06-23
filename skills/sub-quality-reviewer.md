---
name: sub-quality-reviewer
description: Score the campaign across story, video, rewards, goal, and launch plan; flag weak elements.
cluster: marketing-content-branding
reusable: true
used_by:
  - crowdfunding-campaign-advisor
---

## Role
Sub-skill of `crowdfunding-campaign-advisor`. Score the campaign across story, video, rewards, goal, and launch plan; flag weak elements.

## Inputs
- The user-provided context plus the outputs of the preceding harness stage.
- Campaign content (story, video script, reward descriptions, funding goal)
- Audience analysis results
- Compliance check results

## Procedure

### Step 1: Story and Narrative Quality Assessment
Evaluate the campaign narrative structure and effectiveness:

**AIDA Framework Application:**
```yaml
narrative_assessment:
  attention_hook:
    score: 75  # 0-100
    analysis: "Opening statement creates curiosity but could be stronger"
    what_works: "Problem identification is clear and relatable"
    what_needs_work: "Missing emotional hook or surprising statistic"
    recommendation: "Start with a compelling personal story or surprising fact about the problem"
  interest_building:
    score: 80
    analysis: "Problem explanation is thorough and relevant"
    what_works: "Clear explanation of why current solutions fall short"
    what_needs_work: "Could emphasize personal stakes more"
    recommendation: "Add personal anecdote about encountering this problem"
  desire_creation:
    score: 70
    analysis: "Solution is described but emotional appeal could be stronger"
    what_works: "Benefits are listed clearly"
    what_needs_work: "Missing 'why it matters' emotional connection"
    recommendation: "Emphasize transformation/backer impact: 'How backers' lives improve'"
  action_clarity:
    score: 85
    analysis: "Call to back is clear and direct"
    what_works: "Funding purpose is well explained"
    what_needs_work: "Could create more urgency"
    recommendation: "Add limited early-bird reward or time-bound goal"
  overall_narrative_score: 77.5  # Average of four dimensions
  framework: "AIDA (Attention-Interest-Desire-Action) model"
  evidence_sources:
    - "Marketing research: emotional storytelling increases conversion by 2-3x"
    - "Campaign studies: problem-solution structure outperforms feature-focused narratives"
```

**Story Structure Check:**
```yaml
story_structure:
  problem_identification: true  # Clear problem stated
  problem_relevance: true  # Problem matters to target audience
  solution_introduction: true  # Solution is explained
  differentiation: true  # What makes this solution unique
  credibility_elements: true  # Team background, prototype, endorsements
  emotional_connection: false  # MISSING: No emotional hook
  backer_transformation: false  # MISSING: How backers benefit/transform
```

### Step 2: Video Content Evaluation
If video script or description is provided, assess:

```yaml
video_assessment:
  length_appropriateness:
    score: 70
    analysis: "2:30 is within optimal range (2:00-3:00)"
    recommendation: "Good length, ensure every second adds value"
  hook_strength:
    score: 65
    analysis: "Opening is informative but not attention-grabbing"
    recommendation: "Start with product demo or emotional moment, not talking head"
  visual_demonstration:
    score: 75
    analysis: "Product shown clearly, could show more use cases"
    recommendation: "Add 2-3 real-world usage scenarios"
  team_introduction:
    score: 80
    analysis: "Team is introduced with credentials"
    recommendation: "Add personal story about why this matters to you"
  production_quality:
    score: 70
    analysis: "Audio clear, lighting adequate"
    recommendation: "Consider adding graphics/text overlays for key points"
  overall_video_score: 72
  framework: "Video best practices from platform creator handbooks"
  evidence_sources:
    - "Platform data: videos 2:00-3:00 have highest completion rates"
    - "Research: product demos increase funding by 20-30%"
```

### Step 3: Reward Structure Evaluation
Analyze reward tiers and pricing strategy:

**Tier Structure Assessment:**
```yaml
reward_structure:
  tier_count: 6
  optimal_range: true  # 4-8 tiers is optimal
  ladder_structure:
    - tier: "No Reward"
      price: 5
      purpose: "Supporter-only, no product"
      placement: "APPRIATE"
    - tier: "Early Bird"
      price: 50
      purpose: "Early adopter incentive"
      placement: "APPRIATE"
      scarcity_element: true  # Limited quantity
    - tier: "Standard Reward"
      price: 75
      purpose: "Main product offering"
      placement: "APPRIATE"
      anchor_effect: true  # Makes $50 seem like deal, $125 seem premium
    - tier: "Bundle Pack"
      price: 150
      purpose: "Multi-unit or enhanced version"
      placement: "APPRIATE"
      value_proposition: "2 units at 15% discount"
    - tier: "Premium Experience"
      price: 250
      purpose: "High-touch, limited edition"
      placement: "APPRIATE"
      exclusivity: true
    - tier: "VIP Partnership"
      price: 500
      purpose: "Founder-level involvement"
      placement: "APPRIATE"
      involvement_level: "High"
```

**Pricing Psychology Check:**
```yaml
pricing_analysis:
  price_anchoring:
    standard_reward: 75
    anchor_comparison: "Positions $50 as good deal, $125 as premium"
    effectiveness: "STRONG"
  psychological_pricing:
    ends_in_9: false  # $75 vs $79?
    recommendation: "Consider $79 instead of $75 for psychological appeal"
  early_bird_incentive:
    discount_percentage: 33  # (75-50)/75
    scarcity_message: true
    effectiveness: "STRONG - creates urgency"
  stretch_goal_rewards: false  # MISSING: No stretch goals defined
  recommendation: "Add 1-2 stretch goals at $2K and $5K to maintain momentum"
```

**Reward Clarity and Desirability:**
```yaml
reward_quality:
  descriptions_clear: true  # Each reward clearly explained
  delivery_timeline: true  # Dates specified
  shipping_included: false  # ADD SHIPPING CLARIFICATION
  limit_quantities: true  # Limited tiers flagged
  visual_renderings: true  # Images provided
  overall_reward_score: 80
```

### Step 4: Funding Goal Realism Assessment
Evaluate the funding goal against benchmarks and fulfillment costs:

```yaml
goal_analysis:
  funding_goal: 50000
  goal_justification:
    minimum_viable_product: true
    production_costs: 35000
    fulfillment_costs: 8000
    platform_fees: 4000
    contingency: 3000
    total_required: 50000
  goal_realism_score: 85
  analysis:
    what_works: "Goal is grounded in actual costs with contingency"
    what_needs_work: "Consider building in buffer for over-fulfillment"
  benchmark_comparison:
    similar_campaigns:
      - category: "Consumer Electronics"
        average_goal: 45000
        success_rate: "42%"
        this_campaign_percentile: 60  # Higher than 60% of similar campaigns
    category_average: 38000
    this_campaign_vs_average: 1.32  # 32% above category average
  risk_assessment:
    goal_ambition: "MODERATE"  # CONSERVATIVE / MODERATE / AGGRESSIVE
    audience_reach_required: "500 backers at $100 average"
    pre_launch_audience: "Estimated 200 interested prospects"
    conversion_required: "35% of prospects to back"
    feasibility: "ACHIEVABLE with strong pre-launch"
  framework: "Funding goal modeling vs fulfillment cost"
  evidence_sources:
    - "Platform data: campaigns $30K-60K have 2x higher success rate than $100K+"
    - "Research: goal within 3x of audience size is achievable"
```

### Step 5: Launch Readiness Evaluation
Assess pre-launch preparation and launch strategy:

```yaml
launch_assessment:
  pre_launch_audience:
    email_list_size: 0
    target_minimum: 500
    gap: "Need 500 more subscribers"
    social_followers: 0
    target_minimum: 2000
    gap: "Need 2000 more followers"
    press_relationships: "Not established"
    recommendation: "Priority: Build email list through landing page"
  first_48h_plan:
    target_percentage: 30  # Aim for 30% of goal in first 48h
    target_amount: 15000
    backers_required: 150  # At $100 average pledge
    achievability: "MODERATE - depends on pre-launch success"
  launch_timing:
    month: "October"
    seasonality: "GOOD - post-summer spending, pre-holiday"
    day_of_week: "Tuesday"
    optimal: true  # Tuesday/Wednesday are optimal
  launch_plan_score: 65  # Lower due to audience gaps
  framework: "Pre-launch funnel and first 48 hours momentum"
  evidence_sources:
    - "Mollick research: campaigns reaching 30% in first 48h have 80%+ success rate"
    - "Platform data: Tuesday launches have 12% higher success rate"
```

### Step 6: Overall Quality Scoring and Synthesis
Combine all dimension scores:

```yaml
overall_quality_assessment:
  dimension_scores:
    narrative_quality: 77.5
    video_quality: 72
    reward_structure: 80
    goal_realism: 85
    launch_readiness: 65
  overall_score: 76  # Weighted average
  strengths:
    - "Funding goal is realistic and well-justified"
    - "Reward structure has good ladder with psychological pricing"
    - "Story follows problem-solution framework effectively"
  weaknesses:
    - "Launch readiness is below optimal - needs pre-launch audience building"
    - "Narrative missing emotional hook and backer transformation"
    - "No stretch goals defined for momentum maintenance"
  critical_improvements:
    - "Build email list to 500+ before launch"
    - "Add emotional hook to story opening"
    - "Define stretch goals to maintain post-launch momentum"
  nice_to_have_improvements:
    - "Add product usage scenarios to video"
    - "Consider $79 pricing for psychological appeal"
    - "Add visual mockups for all rewards"
```

### Step 7: Self-Check Against Quality Gate
Before returning control to the harness:

**Verify:**
- [ ] All five dimensions were scored (narrative, video, rewards, goal, launch)
- [ ] Each score cites its governing framework
- [ ] Evidence sources are provided for major claims
- [ ] Strengths and weaknesses are specific (not generic)
- [ ] Recommendations are actionable and prioritized
- [ ] Output is structured and parseable by next stage

**If any check fails:** Address the issue before proceeding.

## Outputs
- A structured result object consumed by the next stage:
```yaml
quality_review_result:
  dimension_scores:
    narrative_quality: {score: 77.5, framework: "AIDA model", findings: [...]}
    video_quality: {score: 72, framework: "Platform video best practices", findings: [...]}
    reward_structure: {score: 80, framework: "Reward-tier laddering", findings: [...]}
    goal_realism: {score: 85, framework: "Funding goal modeling", findings: [...]}
    launch_readiness: {score: 65, framework: "Pre-launch funnel", findings: [...]}
  overall_score: 76
  verdict: "Strong foundation with clear improvement path"
  strengths: [...]
  weaknesses: [...]
  critical_improvements: [...]  # High-priority fixes
  nice_to_have_improvements: [...]  # Lower-priority enhancements
  framework_citations:
    - "AIDA (Attention-Interest-Desire-Action) model"
    - "Platform creator handbooks and best practices"
    - "Mollick crowdfunding research"
  evidence_sources:
    - "Platform data: goal ranges, success rates"
    - "Marketing research: emotional storytelling impact"
    - "Behavioral economics: pricing psychology"
```

## Tools
WebSearch, WebFetch, Read, Write, Bash

## Quality Gate
- Output is schema-valid, framework-grounded, and every material claim is traceable to a source or a prior step.

## Framework References
- AIDA / narrative structure (Attention-Interest-Desire-Action)
- Video best practices (platform creator handbooks)
- Reward-tier laddering and price-anchoring economics
- Funding-goal modeling vs fulfillment cost & margin
- Pre-launch funnel and first 48 hours momentum research
