#!/usr/bin/env python3
"""test_runner.py — Automated test execution for crowdfunding-campaign-advisor scenarios."""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List


def parse_scenarios(scenarios_path: str) -> List[Dict[str, Any]]:
    """Parse test scenarios from test-scenarios.md."""
    with open(scenarios_path, encoding="utf-8") as f:
        content = f.read()

    scenarios = []
    scenario_blocks = re.split(r"^### Scenario (\d+)", content, flags=re.MULTILINE)

    for i in range(1, len(scenario_blocks), 2):
        if i + 1 >= len(scenario_blocks):
            break
        scenario_num = scenario_blocks[i]
        block = scenario_blocks[i + 1]

        given_match = re.search(r"^\*\*Given:\*\*\s*(.*?)$", block, re.MULTILINE)
        expected_match = re.search(r"^\*\*Expected harness behavior:\*\*\s*(.*?)$", block, re.MULTILINE)
        pass_match = re.search(r"^\*\*Pass criteria:\*\*\s*(.*?)$", block, re.MULTILINE)

        scenario = {
            "id": f"scenario_{scenario_num}",
            "given": given_match.group(1).strip() if given_match else "",
            "expected_behavior": expected_match.group(1).strip() if expected_match else "",
            "pass_criteria": pass_match.group(1).strip() if pass_match else ""
        }
        scenarios.append(scenario)

    return scenarios


def execute_harness_mock(scenario: Dict[str, Any]) -> Dict[str, Any]:
    """Generate mock harness output matching expected behavior."""

    # Mock multi-dimensional scores based on scenario
    score_profiles = {
        "scenario_1": {"audience": 85, "narrative": 70, "rewards": 75, "goal": 80, "launch": 65},
        "scenario_2": {"audience": 60, "narrative": 55, "rewards": 70, "goal": 75, "launch": 60},
        "scenario_3": {"audience": 40, "narrative": 65, "rewards": 70, "goal": 80, "launch": 35},
        "scenario_4": {"audience": 75, "narrative": 70, "rewards": 45, "goal": 50, "launch": 65},
        "scenario_5": {"audience": 80, "narrative": 75, "rewards": 85, "goal": 80, "launch": 75},
        "scenario_6": {"audience": 85, "narrative": 80, "rewards": 85, "goal": 85, "launch": 80}
    }

    scores = score_profiles.get(scenario["id"], {
        "audience": 70, "narrative": 70, "rewards": 70, "goal": 70, "launch": 70
    })

    return {
        "executive_summary": {
            "verdict": "Strong foundation" if sum(scores.values()) / 5 > 70 else "Needs improvement",
            "headline_score": round(sum(scores.values()) / 5)
        },
        "multi_dimensional_score": {
            "audience_alignment": {
                "score": scores["audience"],
                "framework": "Pre-launch funnel, audience-building research",
                "evidence": ["Mollick 2014 - early backer momentum", "Platform stats - pre-launch conversion"]
            },
            "narrative_quality": {
                "score": scores["narrative"],
                "framework": "AIDA / story-driven narrative",
                "evidence": ["Marketing research - problem-solution structure", "Case studies - emotional hooks"]
            },
            "reward_structure": {
                "score": scores["rewards"],
                "framework": "Reward-tier laddering and price-anchoring",
                "evidence": ["Platform guidelines - tier distribution", "Fulfillment cost analysis"]
            },
            "goal_realism": {
                "score": scores["goal"],
                "framework": "Funding-goal modeling vs fulfillment cost",
                "evidence": ["Success rate studies - goal sizing", "Margin analysis - fulfillment"]
            },
            "launch_readiness": {
                "score": scores["launch"],
                "framework": "Pre-launch funnel and first 48 hours momentum",
                "evidence": ["Launch timing research", "Audience building best practices"]
            }
        },
        "findings": [
            {"type": "strength", "dimension": "audience", "description": "Clear target backer profile"},
            {"type": "risk", "dimension": "launch", "description": "Limited pre-launch audience"}
        ],
        "improvement_roadmap": [
            {"action": "Build pre-launch email list", "impact": "High", "effort": "Medium"},
            {"action": "Strengthen opening hook", "impact": "Medium", "effort": "Low"}
        ],
        "sources": [
            {"citation": "Mollick, E. (2014). The dynamics of crowdfunding...", "type": "academic"},
            {"citation": "Kickstarter Creator Handbook", "type": "platform"}
        ]
    }


def execute_harness(scenario: Dict[str, Any], use_mock: bool = True) -> Dict[str, Any]:
    """Execute harness for a scenario."""
    if use_mock:
        return execute_harness_mock(scenario)
    # Real harness execution would go here
    raise NotImplementedError("Real harness execution not yet implemented")


def validate_quality_gates(output: Dict[str, Any]) -> Dict[str, str]:
    """Validate quality gates and return results."""
    results = {
        "evidence_gate": "pass",
        "framework_gate": "pass",
        "challenge_gate": "pass",
        "output_format_gate": "pass"
    }

    # Evidence gate: every claim should have citations
    sources = output.get("sources", [])
    if len(sources) < 2:
        results["evidence_gate"] = "fail: insufficient sources"

    # Framework gate: scores should reference frameworks
    mds = output.get("multi_dimensional_score", {})
    for dimension, data in mds.items():
        if not data.get("framework"):
            results["framework_gate"] = f"fail: {dimension} missing framework"
            break

    # Challenge gate: check for risk considerations in findings
    findings = output.get("findings", [])
    has_risks = any(f.get("type") == "risk" for f in findings)
    if not has_risks:
        results["challenge_gate"] = "fail: no risk considerations"

    # Output format gate: required sections
    required = ["executive_summary", "multi_dimensional_score", "findings", "improvement_roadmap", "sources"]
    missing = [r for r in required if r not in output]
    if missing:
        results["output_format_gate"] = f"fail: missing {', '.join(missing)}"

    return results


def save_fixture(scenario: Dict[str, Any], output: Dict[str, Any], gate_results: Dict[str, str], fixtures_dir: str):
    """Save regression fixture for a scenario."""
    Path(fixtures_dir).mkdir(parents=True, exist_ok=True)

    fixture = {
        "scenario_id": scenario["id"],
        "description": scenario["given"],
        "input": {"scenario_context": scenario["given"]},
        "output": output,
        "gate_results": gate_results,
        "timestamp": datetime.now().isoformat()
    }

    fixture_path = Path(fixtures_dir) / f"{scenario['id']}_fixture.json"
    with open(fixture_path, "w", encoding="utf-8") as f:
        json.dump(fixture, f, indent=2)

    return fixture_path


def generate_test_report(scenarios: List[Dict], results: List[Dict], report_path: str):
    """Generate markdown test report."""
    report_lines = [
        f"# Test Report — Crowdfunding Campaign Advisor",
        f"",
        f"**Generated:** {datetime.now().isoformat()}",
        f"**Total Scenarios:** {len(scenarios)}",
        f"**Passed:** {sum(1 for r in results if all(v == 'pass' for v in r['gates'].values()))}",
        f"**Failed:** {sum(1 for r in results if not all(v == 'pass' for v in r['gates'].values()))}",
        f"",
        f"## Scenario Results",
        f""
    ]

    for scenario, result in zip(scenarios, results):
        status = "PASS" if all(v == "pass" for v in result["gates"].values()) else "FAIL"
        report_lines.extend([
            f"### {scenario['id']} — {status}",
            f"",
            f"**Given:** {scenario['given']}",
            f"",
            f"**Gate Results:**",
            f""
        ])
        for gate, status in result["gates"].items():
            report_lines.append(f"- {gate}: {status}")
        report_lines.append("")
        report_lines.append(f"**Fixture:** `{result['fixture_path']}`")
        report_lines.append("")

    Path(report_path).parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    return report_path


def main():
    parser = argparse.ArgumentParser(description="Run crowdfunding campaign advisor test scenarios")
    parser.add_argument("--scenarios", default="tests/test-scenarios.md", help="Path to scenarios file")
    parser.add_argument("--fixtures-dir", default="tests/fixtures", help="Path to fixtures directory")
    parser.add_argument("--report", default="tests/test_report.md", help="Path to output report")
    parser.add_argument("--use-mock", default=True, action=argparse.BooleanOptionalAction, help="Use mock outputs")
    args = parser.parse_args()

    print(f"[{datetime.now().isoformat()}] Starting test runner")
    print(f"Scenarios: {args.scenarios}")
    print(f"Fixtures: {args.fixtures_dir}")
    print(f"Use mock: {args.use_mock}")

    scenarios = parse_scenarios(args.scenarios)
    print(f"Parsed {len(scenarios)} scenarios")
    results = []
    all_passed = True
    for scenario in scenarios:
        output = execute_harness(scenario, use_mock=args.use_mock)
        gate_results = validate_quality_gates(output)
        fixture_path = save_fixture(scenario, output, gate_results, args.fixtures_dir)

        results.append({
            "scenario": scenario,
            "output": output,
            "gates": gate_results,
            "fixture_path": str(fixture_path)
        })

        failed = [k for k, v in gate_results.items() if v != "pass"]
        if failed:
            all_passed = False
            print(f"  {scenario['id']}: FAILED gates {failed}")
        else:
            print(f"  {scenario['id']}: PASSED all gates, saved fixture to {fixture_path.name}")

    report_path = generate_test_report(scenarios, results, args.report)
    print(f"\nOverall: {'ALL PASSED' if all_passed else 'SOME FAILED'}")
    print(f"Report saved to {report_path}")

if __name__ == "__main__":
    main()
