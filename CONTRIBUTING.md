# Contributing to Crowdfunding Campaign Advisor

Thank you for your interest in contributing! This document provides guidelines for contributing to the Crowdfunding Campaign Advisor project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Documentation Standards](#documentation-standards)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project adheres to a code of conduct that all contributors must follow:

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards other contributors

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates.

**Bug Report Template:**
```
**Description:** Clear description of the bug
**Steps to reproduce:** Steps to reproduce the behavior
**Expected behavior:** What you expected to happen
**Actual behavior:** What actually happened
**Environment:** OS, Python version, etc.
**Screenshots:** If applicable
**Additional context:** Any other relevant information
```

### Suggesting Enhancements

Enhancement suggestions are welcome! Please:

- Use a clear and descriptive title
- Provide a detailed description of the suggested enhancement
- Explain why this enhancement would be useful
- List potential implementation approaches if possible

### Pull Requests

Pull requests are the best way to contribute changes. See [Pull Request Process](#pull-request-process) below.

## Development Setup

### Prerequisites

- Python 3.8 or higher
- Git
- Familiarity with markdown and YAML
- Understanding of the project structure

### Getting Started

```bash
# Fork and clone the repository
git clone https://github.com/yourusername/crowdfunding-campaign-advisor.git
cd crowdfunding-campaign-advisor

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests to verify setup
python tests/test_runner.py
```

### Project Structure

```
skills/          # Main skill and sub-skill files
tools/           # Knowledge updater and utilities
tests/           # Test suite and fixtures
docs/            # Documentation and specifications
```

## Coding Standards

### General Guidelines

- **Write clear, readable code** with descriptive names
- **Add comments** for complex logic (explain "why", not "what")
- **Follow existing patterns** in the codebase
- **Keep functions focused** on a single responsibility
- **Use type hints** where appropriate
- **No emojis** in code or comments
- **English only** for all text and comments

### Skill File Format

All skill files must use YAML frontmatter:

```yaml
---
name: skill-name
description: Clear description of purpose
cluster: marketing-content-branding  # If applicable
reusable: true  # If applicable
used_by:  # If applicable
  - parent-skill-name
---
```

### Python Code

For Python files (test runner, knowledge updater):

- Follow PEP 8 style guide
- Use 4 spaces for indentation
- Maximum line length: 100 characters
- Use descriptive variable and function names
- Add docstrings to functions

Example:
```python
def parse_scenarios(scenarios_path: str) -> List[Dict[str, Any]]:
    """Parse test scenarios from test-scenarios.md.
    
    Args:
        scenarios_path: Path to the scenarios markdown file
        
    Returns:
        List of scenario dictionaries with id, given, expected_behavior, pass_criteria
    """
    # Implementation here
```

## Testing Guidelines

### Running Tests

```bash
# Run all test scenarios
python tests/test_runner.py

# Run with custom options
python tests/test_runner.py --scenarios tests/test-scenarios.md --fixtures-dir tests/fixtures
```

### Adding New Tests

When adding new functionality:

1. Add test scenario to `tests/test-scenarios.md`
2. Run test runner to generate new fixture
3. Verify fixture output is correct
4. Update `tests/test_report.md` with results

### Test Scenarios Format

```markdown
### Scenario N
- **Given:** [Test condition]
- **Expected harness behavior:** [What should happen]
- **Pass criteria:** [Success conditions]
```

## Documentation Standards

### README Updates

When adding features, update README.md:

- Add feature to Features section
- Update usage instructions if needed
- Add new dependencies to requirements.txt

### Skill Documentation

Each sub-skill must include:

- **Role:** Clear purpose statement
- **Inputs:** Required and optional inputs
- **Procedure:** Detailed step-by-step process
- **Outputs:** Structure of returned data
- **Tools:** Tools required (WebSearch, WebFetch, etc.)
- **Quality Gate:** Validation criteria

### Framework Citations

All scoring must cite frameworks:

```yaml
framework_citations:
  - "AIDA (Attention-Interest-Desire-Action) model"
  - "Platform creator handbooks and best practices"
```

## Pull Request Process

### Before Submitting

1. **Test your changes:** Run `python tests/test_runner.py`
2. **Update documentation:** README, CHANGELOG, etc.
3. **Follow coding standards:** See above
4. **Keep changes focused:** One feature or fix per PR
5. **Write clear commit messages:** Summarize what and why

### Submitting a Pull Request

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add: your feature description"`
4. Push to branch: `git push origin feature/your-feature-name`
5. Open a pull request on GitHub

### Pull Request Template

```markdown
## Description
Clear description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tests pass locally
- [ ] New tests added (if applicable)
- [ ] Documentation updated

## Checklist
- [ ] Code follows project standards
- [ ] Self-reviewed before submission
- [ ] Commented complex code sections
- [ ] Updated documentation as needed
- [ ] No new warnings generated
- [ ] Added units/updates to CHANGELOG.md
```

### Review Process

- Maintainers will review your PR
- Address feedback in a timely manner
- Keep discussion focused and constructive
- Multiple commits may be requested

## Recognition

Contributors will be recognized in the project's CONTRIBUTORS section.

## Questions?

- Open an issue for questions
- Check existing documentation first
- Be specific and provide context

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Crowdfunding Campaign Advisor!
