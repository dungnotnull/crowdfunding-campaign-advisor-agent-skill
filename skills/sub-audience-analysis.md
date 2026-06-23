---
name: sub-audience-analysis
description: Profile the target backers, their channels, and the pre-launch audience-building plan.
cluster: marketing-content-branding
reusable: true
used_by:
  - crowdfunding-campaign-advisor
---

## Role
Sub-skill of `crowdfunding-campaign-advisor`. Profile the target backers, their channels, and the pre-launch audience-building plan.

## Inputs
- The user-provided context plus the outputs of the preceding harness stage.
- Campaign description, product/service details
- Any existing audience data (email list size, social media following, etc.)

## Procedure

### Step 1: Intake and Validation
Ask the user targeted questions to gather required information:

**Essential Questions:**
1. What is your campaign about? (product/service description)
2. Who is your ideal backer? (age, location, interests, behaviors)
3. What channels do you currently have? (email list size, social media followers, website traffic)
4. How long until launch? (pre-launch timeline)

**If any answer is missing:** Request the specific information before proceeding. Document assumptions clearly.

### Step 2: Audience Profile Development
Build a structured audience profile based on the inputs:

**Demographics:**
- Age range, location (countries/cities), income level, occupation/industry

**Psychographics:**
- Interests, values, pain points, motivations for backing
- Where they spend time online (platforms, communities, publications)

**Backing Behavior:**
- Previous crowdfunding experience
- Average pledge amount range
- Decision factors (social proof, rewards, mission, updates)

**Output Structure:**
```yaml
audience_profile:
  demographics:
    age_range: "25-45"
    locations: ["US", "UK", "Germany", "Canada"]
    income_level: "Middle to upper-middle"
    interests: ["technology", "sustainability", "innovation"]
  psychographics:
    values: ["early adoption", "supporting creators", "product innovation"]
    pain_points: ["existing solutions are inadequate", "need for this product"]
    motivations: ["being first", "supporting innovation", "product utility"]
  backing_behavior:
    experience: "Mixed - some backers are experienced, others are first-timers"
    average_pledge: "$50-150"
    decision_factors: ["Creator credibility", "Social proof", "Reward appeal", "Project timeline"]
```

### Step 3: Channel Analysis and Recommendations
Analyze existing channels and recommend acquisition strategies:

**For each channel, assess:**
- Current reach (follower count, email list size)
- Engagement rate (likes, comments, opens, clicks)
- Conversion potential (backer likelihood)
- Growth opportunities

**Recommendation Framework:**
```yaml
channel_strategy:
  email_list:
    status: "Building"  # Existing/None/Building/Mature
    current_size: 0
    target_size: 500
    tactics:
      - "Create landing page with email capture"
      - "Offer pre-launch exclusive updates"
      - "Provide early-bird reward notification"
    expected_conversion: "8-12% of subscribers become backers"
  social_media:
    platforms:
      - name: "Instagram"
        followers: 0
        engagement_target: "3-5%"
        content_strategy: "Behind-the-scenes, product development updates"
      - name: "Twitter/X"
        followers: 0
        engagement_target: "2-4%"
        content_strategy: "Industry commentary, founder journey"
      - name: "LinkedIn"
        followers: 0
        engagement_target: "1-3%"
        content_strategy: "Professional audience, innovation angle"
  communities:
    target_subreddits: ["r/crowdfunding", "r/technology", niche_relevant_subs]
    forums: ["Indiegogo community", Kickstarter forum", industry_forums]
    engagement_approach: "Value-first, not direct promotion"
  press_outlets:
    target_publications: ["TechCrunch", "Wired", niche_industry_pubs]
    pitch_angle: "Innovation story, founder journey, problem-solution"
```

### Step 4: Pre-Launch Audience Building Plan
Create a phased timeline for audience building:

**Timeline Structure (by weeks until launch):**
```yaml
pre_launch_plan:
  weeks_8_to_4:
    focus: "Foundation building"
    actions:
      - "Launch landing page with email capture (target: 200 subscribers)"
      - "Establish social media presence (3 platforms, consistent posting)"
      - "Identify and engage with target communities"
    kpi_target: "200 email subscribers, 500 combined social followers"
  weeks_4_to_2:
    focus: "Engagement and teaser content"
    actions:
      - "Share behind-the-scenes content"
      - "Teaser campaign reveals"
      - "Influencer/press outreach begins"
    kpi_target: "400 email subscribers, 1000 social followers"
  weeks_2_to_0:
    focus: "Pre-launch momentum"
    actions:
      - "Launch announcement with countdown"
      - "Early-bird reward preview for email list"
      - "Press outreach wave 1"
    kpi_target: "500+ email subscribers, 2000+ social followers"
  launch_week:
    focus: "First 48 hours push"
    actions:
      - "Launch day email blast"
      - "Social media announcement across all channels"
      - "Founder personal network outreach"
    target_first_48h_percentage: "30% of funding goal"
```

### Step 5: Audience Alignment Scoring
Score the campaign's audience alignment (0-100):

**Scoring Criteria:**
- **Audience definition clarity (0-20):** Is the target audience clearly defined?
- **Channel match (0-25):** Are chosen channels where the audience actually exists?
- **Pre-launch plan realism (0-25):** Is the building plan achievable given timeline?
- **First-48h readiness (0-30):** Can the campaign achieve 30% of goal in first 48 hours?

**Score Interpretation:**
- 90-100: Excellent audience targeting with strong pre-launch foundation
- 70-89: Good audience fit with solid channel strategy
- 50-69: Moderate alignment, gaps in strategy or timeline
- <50: Weak audience definition or unrealistic acquisition plan

### Step 6: Self-Check Against Quality Gate
Before returning control to the harness:

**Verify:**
- [ ] All required inputs were collected (no assumptions without documentation)
- [ ] Audience profile is specific (not vague or generic)
- [ ] Channel recommendations are evidence-based (cite platform benchmarks)
- [ ] Pre-launch timeline is realistic (given resources and timeline)
- [ ] Score is justified with clear reasoning
- [ ] Output is structured and parseable by next stage

**If any check fails:** Address the issue before proceeding. Note any limitations in data or assumptions made.

## Outputs
- A structured result object consumed by the next stage:
```yaml
audience_analysis_result:
  audience_profile: {demographics, psychographics, backing_behavior}
  channel_strategy: {email_list, social_media, communities, press_outlets}
  pre_launch_plan: {timeline_by_week, kpi_targets, first_48h_target}
  audience_alignment_score: 75  # 0-100
  framework_citations:
    - "Pre-launch funnel research: first 48h momentum critical"
    - "Platform conversion benchmarks: email 8-12%, social 1-3%"
  recommendations: ["Prioritize email list building", "Focus on 2-3 channels, not all"]
  risks: ["Limited time for pre-launch building", "Channel reach may be insufficient"]
```

## Tools
WebSearch, WebFetch, Read, Write, Bash

## Quality Gate
- Output is schema-valid, framework-grounded, and every material claim is traceable to a source or a prior step.

## Framework References
- Pre-launch funnel research (Mollick 2014: early backer momentum)
- Platform conversion benchmarks (Kickstarter/Indiegogo creator handbooks)
- Audience acquisition best practices (digital marketing research)
