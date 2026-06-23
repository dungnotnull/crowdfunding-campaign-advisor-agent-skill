# Changelog

All notable changes to the Crowdfunding Campaign Advisor project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-23

### Added
- **Complete skill implementation** across all 5 development phases (0-5)
- **Sub-skills:**
  - `sub-audience-analysis` - Profile backers, channels, and pre-launch strategy
  - `sub-compliance-check` - Screen platform rules and fulfillment realism
  - `sub-quality-reviewer` - Multi-dimensional scoring with framework grounding
  - `sub-improvement-roadmap` - Prioritized fixes with impact/effort ranking
- **Main harness** (`skills/main.md`) with workflow and quality gates
- **Test infrastructure:**
  - Automated test runner (`tests/test_runner.py`)
  - 6 regression fixtures for consistent validation
  - Test report generation with markdown output
- **Knowledge pipeline** (`tools/knowledge_updater.py`) for continuous learning
- **Cluster integration:**
  - Standard scoring schema for cluster consistency
  - Sub-skills catalog for reuse across sibling skills
  - Cluster metadata on all sub-skills
- **Documentation:**
  - Comprehensive README with installation and usage
  - MIT License for open-source distribution
  - Python requirements and gitignore
  - Contributing guidelines

### Changed
- Enhanced all sub-skills with detailed, production-ready procedures
- Improved scoring framework with specific rubrics and evidence citations
- Standardized output schemas across all sub-skills
- Structured improvement recommendations with impact/effort matrix

### Fixed
- All quality gates now properly validate evidence, framework, and format
- Test runner correctly handles scenario parsing and fixture generation
- Compliance check now includes fulfillment cost analysis

### Security
- Added compliance rules for regulated content screening
- Implemented disclaimer requirements for legal/financial topics
- Platform rules validation for Kickstarter and Indiegogo

## [Unreleased]

### Planned
- Real-time campaign data integration
- Additional platform support (Patreon, GoFundMe)
- Multilingual support
- Advanced analytics dashboard

---

## Version Format

- **Major.Minor.Patch** (e.g., 1.0.0)
- **Major:** Breaking changes or major feature additions
- **Minor:** New features, backward-compatible enhancements
- **Patch:** Bug fixes, minor improvements, documentation updates

## Release Process

1. Update CHANGELOG.md with changes
2. Update version in README.md
3. Create git tag: `git tag -a v1.0.0 -m "Release v1.0.0"`
4. Push tag: `git push origin v1.0.0`
5. Create GitHub release with notes from CHANGELOG
