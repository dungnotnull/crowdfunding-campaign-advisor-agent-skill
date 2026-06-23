# Crowdfunding Campaign Advisor

> Design and score crowdfunding campaigns: rewards, story, funding goal, and launch plan.

A research-first AI skill that turns campaign ideas into professional-grade deliverables. Every judgment is grounded in named, citable frameworks from crowdfunding success research, and the system continuously updates with record-breaking campaign structures.

## Overview

First-time creators launch crowdfunding campaigns with weak stories, mispriced rewards, and no pre-launch audience—then fail to fund. This skill designs and scores campaigns across proven success factors, models funding goal and reward economics, and recommends prioritized improvements.

## Features

- **Multi-dimensional scoring** across story, video, rewards, goal, and launch readiness
- **Framework-grounded analysis**—every score cites its research source
- **Compliance screening** for platform rules and fulfillment realism
- **Audience profiling** with channel strategy and pre-launch planning
- **Prioritized improvement roadmap** with impact/effort ranking
- **Regression testing** with automated test fixtures
- **Knowledge pipeline** that continuously learns from new research

## Use Cases

1. **Campaign design:** Structure reward tiers and model funding goal vs cost
2. **Story improvement:** Rewrite feature-dumping as problem-solution narrative
3. **Audience building:** Build pre-launch funnel and 'first 48 hours' plan
4. **Risk screening:** Flag fulfillment margin and shipping risks
5. **Stretch goal strategy:** Advise based on success-factor research
6. **Launch readiness:** Score campaign blueprint with launch calendar

## Installation

### Requirements

- Python 3.8 or higher
- Claude Code CLI or compatible Claude Agent runtime

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/crowdfunding-campaign-advisor.git
cd crowdfunding-campaign-advisor

# Install dependencies (for knowledge updater)
pip install -r requirements.txt

# Verify installation
python tests/test_runner.py --help
```

### Dependencies

See `requirements.txt` for full list. Key dependencies:
- No external dependencies required for core skill files
- `urllib3`, `hashlib` for knowledge updater (Python stdlib)
- Optional: `crawl4ai` for enhanced knowledge fetching

## Usage

### As a Claude Skill

The primary use is through the Claude Code CLI or compatible runtime:

```bash
claude skill crowdfunding-campaign-advisor
```

The skill will prompt for campaign information and generate a scored deliverable.

### Running Tests

Execute the test suite to verify functionality:

```bash
# Run all test scenarios
python tests/test_runner.py

# Run with custom options
python tests/test_runner.py --scenarios tests/test-scenarios.md --fixtures-dir tests/fixtures --report tests/test_report.md
```

### Knowledge Updater

Keep the knowledge base current with latest research:

```bash
# Run knowledge updater (recommended: weekly cron)
python tools/knowledge_updater.py
```

## Project Structure

```
crowdfunding-campaign-advisor/
├── CLAUDE.md                          # Project instructions
├── README.md                          # This file
├── PROJECT-detail.md                  # Technical specification
├── PROJECT-DEVELOPMENT-PHASE-TRACKING.md  # Development progress
├── SECOND-KNOWLEDGE-BRAIN.md          # Self-improving knowledge base
├── requirements.txt                   # Python dependencies
├── CHANGELOG.md                       # Version history
├── LICENSE                            # MIT License
├── skills/
│   ├── main.md                        # Main harness entry point
│   ├── sub-audience-analysis.md      # Audience profiling sub-skill
│   ├── sub-compliance-check.md       # Compliance screening sub-skill
│   ├── sub-quality-reviewer.md       # Quality scoring sub-skill
│   └── sub-improvement-roadmap.md    # Improvement recommendations sub-skill
├── tools/
│   └── knowledge_updater.py           # Knowledge pipeline crawler
├── tests/
│   ├── test-scenarios.md              # Test scenario definitions
│   ├── test_runner.py                 # Test execution harness
│   ├── test_report.md                # Generated test results
│   └── fixtures/                     # Regression fixtures
│       ├── scenario_1_fixture.json
│       ├── scenario_2_fixture.json
│       └── ...
└── docs/
    ├── cluster-standard-scoring-schema.md    # Shared scoring definitions
    ├── cluster-sub-skills.md                  # Reusable sub-skills catalog
    └── superpowers/
        ├── plans/                              # Implementation plans
        └── specs/                              # Design specifications
```

## Architecture

The skill operates as a harness with four sub-skills:

1. **Intake & framing** → Confirm inputs and scope
2. **Framework selection & screening** → Select governing frameworks
3. **Sub-skill execution:**
   - `sub-audience-analysis` → Profile backers, channels, pre-launch plan
   - `sub-compliance-check` → Screen platform rules, fulfillment realism
   - `sub-quality-reviewer` → Score across story, video, rewards, goal, launch
   - `sub-improvement-roadmap` → Recommend prioritized fixes with impact
4. **Knowledge refresh** → Update from latest research if stale
5. **Quality gates** → Evidence, framework, challenge gates
6. **Synthesis** → Emit scored deliverable + roadmap

## Governing Frameworks

All scoring is grounded in named frameworks:

1. Crowdfunding success-factor research (early-backer momentum, video, social proof)
2. Reward-tier laddering and price-anchoring economics
3. Pre-launch funnel (landing page, email list, 'first 48 hours' momentum)
4. AIDA / story-driven campaign narrative (problem-solution-credibility)
5. Funding-goal modeling vs fulfillment cost & margin
6. Backer-psychology: scarcity, social proof, stretch goals

## Quality Assurance

The project includes comprehensive testing:

- **6 test scenarios** covering typical use cases
- **Regression fixtures** for consistent validation
- **Quality gate validation** (evidence, framework, challenge, format)
- **Automated test reporting** with markdown output

Run tests: `python tests/test_runner.py`

## Cluster Integration

This skill is part of the `marketing-content-branding` cluster:

- **Shared scoring schema** across cluster siblings
- **Reusable sub-skills** documented in catalog
- **Standardized evidence citations** and framework grounding

See `docs/cluster-standard-scoring-schema.md` and `docs/cluster-sub-skills.md`

## Contributing

Contributions are welcome! Please see `CONTRIBUTING.md` for guidelines.

### Development Setup

```bash
# Fork and clone
git clone https://github.com/yourusername/crowdfunding-campaign-advisor.git

# Create a feature branch
git checkout -b feature/your-feature-name

# Make your changes
# ... edit files ...

# Run tests
python tests/test_runner.py

# Submit pull request
```

## Version History

See `CHANGELOG.md` for detailed version history.

### Current Version: 1.0.0

- ✅ Complete implementation of all 5 development phases
- ✅ Production-ready test infrastructure
- ✅ Cluster integration and scoring standards
- ✅ Comprehensive documentation

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Ethan Mollick's foundational crowdfunding research
- Kickstarter and Indiegogo platform creator resources
- The crowdfunding community for shared learning

## Support

For questions, issues, or contributions:
- Open an issue on GitHub
- See `CONTRIBUTING.md` for contribution guidelines
- Review `PROJECT-detail.md` for technical details

## Roadmap

Future enhancements:
- [ ] Real-time campaign data integration
- [ ] Additional platform support (Patreon, GoFundMe)
- [ ] Multilingual support
- [ ] Advanced analytics dashboard
