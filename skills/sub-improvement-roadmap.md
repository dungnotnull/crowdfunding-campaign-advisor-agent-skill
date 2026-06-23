---
name: sub-improvement-roadmap
description: Recommend prioritized fixes to rewards, narrative, goal, and launch sequencing with impact.
cluster: marketing-content-branding
reusable: true
used_by:
  - crowdfunding-campaign-advisor
---

## Role
Sub-skill of `crowdfunding-campaign-advisor`. Recommend prioritized fixes to rewards, narrative, goal, and launch sequencing with impact.

## Inputs
- The user-provided context plus the outputs of the preceding harness stage.
- Quality review results (dimension scores, strengths, weaknesses)
- User constraints (timeline, budget, resources)
- Priority dimensions (if user specified)

## Procedure

### Step 1: Analyze Quality Review Findings
Process the quality review output to identify improvement opportunities:

```yaml
improvement_opportunities:
  from_quality_review:
    - dimension: "narrative_quality"
      score: 77.5
      issues: ["Missing emotional hook", "No backer transformation"]
      potential_score_gain: 15  # Points if fixed
    - dimension: "video_quality"
      score: 72
      issues: ["Opening not attention-grabbing", "Limited use cases shown"]
      potential_score_gain: 12
    - dimension: "reward_structure"
      score: 80
      issues: ["No stretch goals", "Shipping clarity needed"]
      potential_score_gain: 8
    - dimension: "goal_realism"
      score: 85
      issues: ["Minimal - goal is well-justified"]
      potential_score_gain: 3
    - dimension: "launch_readiness"
      score: 65
      issues: ["Insufficient pre-launch audience", "No first-48h plan"]
      potential_score_gain: 20
  from_compliance_check:
    - issue: "International shipping costs unclear"
      severity: "HIGH"
      impact: "Could cause backer complaints"
    - issue: "Battery life claim needs qualification"
      severity: "MEDIUM"
      impact: "Platform policy risk"
  from_audience_analysis:
    - gap: "Email list at 0, target is 500"
      severity: "CRITICAL"
      impact: "Launch success at risk"
```

### Step 2: Categorize and Prioritize Improvements
Organize improvements by impact/effort matrix:

**Impact/Effort Matrix Framework:**
```yaml
improvement_prioritization:
  quick_wins:  # High impact, Low effort
    - action: "Add emotional hook to story opening"
      impact: "HIGH"
      effort: "LOW"
      time_estimate: "1-2 hours"
      score_impact: "+8 to narrative score"
      description: "Open with personal anecdote or surprising statistic"
    - action: "Define 2-3 stretch goals"
      impact: "HIGH"
      effort: "LOW"
      time_estimate: "1 hour"
      score_impact: "+5 to reward score"
      description: "Define stretch goals at $2K and $5K with new rewards"

  high_value:  # High impact, Medium effort
    - action: "Build pre-launch email list to 500+"
      impact: "CRITICAL"
      effort: "MEDIUM"
      time_estimate: "4-6 weeks"
      score_impact: "+20 to launch readiness score"
      description: "Create landing page, social media push, content marketing"
    - action: "Add product use case scenarios to video"
      impact: "MEDIUM"
      effort: "MEDIUM"
      time_estimate: "1 week"
      score_impact: "+10 to video score"
      description: "Film 2-3 real-world usage demonstrations"

  fill_in:  # Low impact, Low effort
    - action: "Qualify battery life claim ('up to 30 days')"
      impact: "LOW"
      effort: "LOW"
      time_estimate: "30 minutes"
      score_impact: "+3 to compliance score"
      description: "Add qualification to manage expectations"
    - action: "Add shipping clarity to reward descriptions"
      impact: "MEDIUM"
      effort: "LOW"
      time_estimate: "1 hour"
      score_impact: "+5 to reward score"
      description: "Specify 'shipping included for US, add $15 international'"

  major_projects:  # High impact, High effort
    - action: "Re-shoot video with stronger opening"
      impact: "HIGH"
      effort: "HIGH"
      time_estimate: "2-3 weeks"
      score_impact: "+15 to video score"
      description: "New hook, better pacing, professional editing"
      deferrable: true  # Can launch without, improve later

  low_priority:  # Low impact, Medium/High effort
    - action: "Psychological pricing adjustment ($75 -> $79)"
      impact: "LOW"
      effort: "LOW"
      time_estimate: "30 minutes"
      score_impact: "+2 to reward score"
      description: "Minor pricing tweak for psychological appeal"
```

### Step 3: Sequence Improvements by Timeline
Create a phased roadmap based on time until launch:

```yaml
improvement_timeline:
  pre_launch_phase:
    weeks_remaining: 8
    immediate_actions:  # Week 1-2 (Critical path)
      - priority: 1
        action: "Launch landing page with email capture"
        impact: "CRITICAL for launch success"
        effort: "MEDIUM"
        deadline: "Week 1"
        owner: "Founder"
        status: "NOT_STARTED"
      - priority: 2
        action: "Add emotional hook to story"
        impact: "HIGH for conversion"
        effort: "LOW"
        deadline: "Week 1"
        owner: "Content writer"
        status: "NOT_STARTED"
      - priority: 3
        action: "Define stretch goals and rewards"
        impact: "HIGH for momentum"
        effort: "LOW"
        deadline: "Week 2"
        owner: "Founder"
        status: "NOT_STARTED"

    short_term_actions:  # Week 3-4
      - priority: 4
        action: "Social media content strategy and posting"
        impact: "HIGH for audience building"
        effort: "MEDIUM"
        deadline: "Week 4"
        owner: "Marketing lead"
        status: "NOT_STARTED"
      - priority: 5
        action: "Add shipping clarity to all rewards"
        impact: "MEDIUM for backer clarity"
        effort: "LOW"
        deadline: "Week 3"
        owner: "Founder"
        status: "NOT_STARTED"

    medium_term_actions:  # Week 5-8
      - priority: 6
        action: "Film additional use case scenarios for video"
        impact: "MEDIUM for video quality"
        effort: "MEDIUM"
        deadline: "Week 6"
        owner: "Video production"
        status: "NOT_STARTED"
      - priority: 7
        action: "Press outreach and relationship building"
        impact: "HIGH for launch day coverage"
        effort: "MEDIUM"
        deadline: "Week 7"
        owner: "PR/Founder"
        status: "NOT_STARTED"

  launch_phase:
    day_0_actions:
      - priority: 8
        action: "Email list blast with early-bird reminder"
        impact: "CRITICAL for first 48h"
        effort: "LOW"
        timing: "Launch day morning"
      - priority: 9
        action: "Social media announcement across all platforms"
        impact: "HIGH for initial momentum"
        effort: "LOW"
        timing: "Launch day morning"
      - priority: 10
        action: "Personal network outreach"
        impact: "HIGH for first-day backers"
        effort: "MEDIUM"
        timing: "Launch day morning"

  post_launch_phase:
    ongoing_actions:
      - priority: 11
        action: "Update stretch goal progress at 50%, 75%, 100%"
        impact: "HIGH for momentum"
        effort: "LOW"
        frequency: "As milestones reached"
      - priority: 12
        action: "Weekly backer updates"
        impact: "MEDIUM for backer retention"
        effort: "LOW"
        frequency: "Every Friday"
```

### Step 4: Calculate Expected Score Improvements
Project the impact of recommended improvements:

```yaml
projected_score_improvement:
  current_scores:
    narrative_quality: 77.5
    video_quality: 72
    reward_structure: 80
    goal_realism: 85
    launch_readiness: 65
    overall: 76

  if_quick_wins_completed:  # 2-3 hours work
    narrative_quality: 85  # +7.5
    reward_structure: 88  # +8
    overall: 81  # +5

  if_high_value_completed:  # 4-6 weeks work
    launch_readiness: 85  # +20
    video_quality: 82  # +10
    overall: 86  # +10

  if_all_recommended_completed:  # Full roadmap
    narrative_quality: 90
    video_quality: 85
    reward_structure: 92
    goal_realism: 88
    launch_readiness: 85
    overall: 88  # +12 points

  success_probability:
    current_state: "60% chance of funding"
    with_quick_wins: "75% chance of funding"
    with_high_value: "85% chance of funding"
    with_all_recommended: "90% chance of funding"

  framework: "Impact/effort prioritization and MVP principles"
  evidence_sources:
    - "Platform data: campaigns with 80+ overall scores have 90%+ success rate"
    - "Research: pre-launch audience building is #1 success factor"
```

### Step 5: Generate Actionable Recommendations
Create prioritized, specific recommendations:

```yaml
prioritized_recommendations:
  do_before_launch:  # Non-negotiable
    - recommendation: "Build email list to minimum 500 subscribers"
      priority: "CRITICAL"
      impact: "20-point increase in launch readiness"
      effort: "4-6 weeks"
      how: "1. Create landing page with email capture, 2. Social media content strategy, 3. Community engagement"
      resources_needed: "Landing page tool ($50/mo), content creation time"
      deadline: "1 week before launch"
    - recommendation: "Add emotional hook to campaign story opening"
      priority: "HIGH"
      impact: "8-point increase in narrative score"
      effort: "1-2 hours"
      how: "Replace current opening with personal anecdote or surprising statistic"
      resources_needed: "Writer/editor time"
      deadline: "Before campaign submission"

  do_if_time_permits:  # High value but can defer
    - recommendation: "Film additional product use case scenarios"
      priority: "MEDIUM"
      impact: "10-point increase in video score"
      effort: "1 week"
      how: "Identify 3 use cases, film user demonstrations, edit into video"
      resources_needed: "Video equipment, editing software"
      deadline: "2 weeks before launch"

  do_for_better_odds:  # Nice to have
    - recommendation: "Re-shoot video with professional production"
      priority: "LOW"
      impact: "15-point increase in video score"
      effort: "2-3 weeks"
      how: "Hire videographer, plan storyboard, film and edit"
      resources_needed: "$2000-5000 production budget"
      deadline: "Can launch without, improve for stretch goal"
```

### Step 6: Self-Check Against Quality Gate
Before returning control to the harness:

**Verify:**
- [ ] All quality review findings were addressed in recommendations
- [ ] Improvements are categorized by impact/effort
- [ ] Timeline is sequenced and realistic
- [ ] Recommendations are specific and actionable (not vague)
- [ ] Resources needed are identified
- [ ] Expected score improvements are calculated
- [ ] Output is structured and parseable for final synthesis

**If any check fails:** Address the issue before proceeding.

## Outputs
- A structured result object consumed by the next stage:
```yaml
improvement_roadmap_result:
  prioritized_improvements:
    - {action, impact, effort, timeline, resources_needed, score_impact}
  improvement_matrix:
    quick_wins: [...]
    high_value: [...]
    fill_in: [...]
    major_projects: [...]
    low_priority: [...]
  phased_roadmap:
    pre_launch_phase: {weeks: [], actions: [...]}
    launch_phase: {days: [], actions: [...]}
    post_launch_phase: {ongoing: [...]}
  projected_score_improvement:
    current_overall_score: 76
    with_quick_wins: 81
    with_all_recommended: 88
    success_probability_increase: "60% -> 90%"
  critical_actions: [...]  # Must-do before launch
  recommended_actions: [...]  # Should-do if time permits
  optional_actions: [...]  # Nice-to-have
  framework_citations:
    - "Impact/effort prioritization framework"
    - "Minimum viable product principles"
    - "Platform success factor research"
  evidence_sources:
    - "Campaign analysis: pre-launch audience correlates with success"
    - "A/B testing: emotional hooks increase conversion 2-3x"
```

## Tools
Read, Write, Bash

## Quality Gate
- Output is schema-valid, framework-grounded, and every material claim is traceable to a source or a prior step.

## Framework References
- Impact/effort prioritization matrix
- Minimum viable product (MVP) principles
- Iterative improvement best practices
- Platform success factor research
