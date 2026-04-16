"""KUBRIK Audit Report Generator.

Takes structured audit data (JSON) and produces a styled HTML report.

Usage:
    python generate_audit_report.py audit-data.json -o report.html

Input JSON format:
{
    "account_name": "Client Name",
    "date": "2026-04-16",
    "period": {"from": "2026-03-16", "to": "2026-04-16"},
    "health_score": 62,
    "categories": {
        "account_structure": {"score": 75, "status": "WARN", "findings": [...]},
        "keywords": {"score": 55, "status": "FAIL", "findings": [...]},
        "negative_keywords": {"score": 40, "status": "FAIL", "findings": [...]},
        "ad_copy": {"score": 70, "status": "WARN", "findings": [...]},
        "performance": {"score": 65, "status": "WARN", "findings": [...]},
        "budget_bidding": {"score": 80, "status": "OK", "findings": [...]}
    },
    "landing": {"score": 72, "status": "WARN", "findings": [...]},
    "creative_fatigue": {"score": 45, "status": "FAIL", "findings": [...]},
    "estimated_waste_monthly": 45000,
    "waste_breakdown": [
        {"source": "Irrelevant keywords", "amount": 25000},
        {"source": "Fatigued creatives", "amount": 20000}
    ],
    "critical": [...],
    "warnings": [...],
    "recommendations": [...]
}
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import datetime

TEMPLATE = """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>KUBRIK Audit: {account_name}</title>
<style>
:root {{
    --bg: #0a0a0a;
    --surface: #141414;
    --border: #2a2a2a;
    --text: #e5e5e5;
    --text-muted: #888;
    --accent: #3b82f6;
    --green: #22c55e;
    --yellow: #eab308;
    --red: #ef4444;
    --orange: #f97316;
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
    font-family: 'Inter', -apple-system, sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.6;
    padding: 40px 20px;
}}
.container {{ max-width: 900px; margin: 0 auto; }}
.header {{
    text-align: center;
    margin-bottom: 48px;
    padding-bottom: 32px;
    border-bottom: 1px solid var(--border);
}}
.header h1 {{ font-size: 28px; font-weight: 600; margin-bottom: 8px; }}
.header .meta {{ color: var(--text-muted); font-size: 14px; }}
.score-ring {{
    width: 160px;
    height: 160px;
    margin: 24px auto;
    position: relative;
}}
.score-ring svg {{ width: 100%; height: 100%; transform: rotate(-90deg); }}
.score-ring circle {{
    fill: none;
    stroke-width: 8;
    stroke-linecap: round;
}}
.score-ring .bg {{ stroke: var(--border); }}
.score-ring .fg {{ transition: stroke-dashoffset 1s ease; }}
.score-value {{
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 48px;
    font-weight: 700;
}}
.score-label {{
    text-align: center;
    font-size: 14px;
    color: var(--text-muted);
    margin-top: 8px;
}}
.section {{ margin-bottom: 40px; }}
.section h2 {{
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 16px;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--border);
}}
.categories {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 16px;
    margin-bottom: 32px;
}}
.cat-card {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 20px;
}}
.cat-card .name {{ font-size: 14px; color: var(--text-muted); margin-bottom: 8px; }}
.cat-card .score {{ font-size: 32px; font-weight: 700; }}
.cat-card .bar {{
    height: 4px;
    background: var(--border);
    border-radius: 2px;
    margin-top: 12px;
    overflow: hidden;
}}
.cat-card .bar-fill {{ height: 100%; border-radius: 2px; transition: width 0.5s; }}
.status-ok {{ color: var(--green); }}
.status-warn {{ color: var(--yellow); }}
.status-fail {{ color: var(--red); }}
.bar-ok {{ background: var(--green); }}
.bar-warn {{ background: var(--yellow); }}
.bar-fail {{ background: var(--red); }}
.issues {{ list-style: none; }}
.issues li {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 16px;
    margin-bottom: 8px;
}}
.issues li.critical {{ border-left: 3px solid var(--red); }}
.issues li.warning {{ border-left: 3px solid var(--yellow); }}
.issues li.info {{ border-left: 3px solid var(--accent); }}
.issue-title {{ font-weight: 600; margin-bottom: 4px; }}
.issue-impact {{ font-size: 13px; color: var(--text-muted); }}
.issue-fix {{ font-size: 13px; color: var(--accent); margin-top: 4px; }}
.waste-box {{
    background: var(--surface);
    border: 1px solid var(--red);
    border-radius: 8px;
    padding: 24px;
    text-align: center;
    margin-bottom: 32px;
}}
.waste-amount {{
    font-size: 36px;
    font-weight: 700;
    color: var(--red);
}}
.waste-label {{ font-size: 14px; color: var(--text-muted); margin-top: 4px; }}
.waste-breakdown {{ margin-top: 16px; }}
.waste-breakdown table {{ width: 100%; border-collapse: collapse; }}
.waste-breakdown td {{ padding: 8px 12px; border-bottom: 1px solid var(--border); }}
.waste-breakdown td:last-child {{ text-align: right; font-weight: 600; color: var(--red); }}
.footer {{
    text-align: center;
    padding-top: 32px;
    border-top: 1px solid var(--border);
    color: var(--text-muted);
    font-size: 13px;
}}
</style>
</head>
<body>
<div class="container">
    <div class="header">
        <h1>KUBRIK Audit Report</h1>
        <div class="meta">{account_name} | {period_from} - {period_to} | Generated {date}</div>
    </div>

    <div class="score-ring">
        <svg viewBox="0 0 160 160">
            <circle class="bg" cx="80" cy="80" r="70"/>
            <circle class="fg" cx="80" cy="80" r="70"
                stroke="{score_color}"
                stroke-dasharray="{circumference}"
                stroke-dashoffset="{score_offset}"/>
        </svg>
        <div class="score-value" style="color: {score_color}">{health_score}</div>
    </div>
    <div class="score-label">Health Score</div>

    {waste_section}

    <div class="section">
        <h2>Score by Category</h2>
        <div class="categories">
            {category_cards}
        </div>
    </div>

    {critical_section}
    {warnings_section}
    {recommendations_section}

    <div class="footer">
        Generated by KUBRIK Audit | kubrik.ai
    </div>
</div>
</body>
</html>"""


def score_color(score: int) -> str:
    if score >= 80:
        return "#22c55e"
    if score >= 60:
        return "#eab308"
    if score >= 40:
        return "#f97316"
    return "#ef4444"


def status_class(status: str) -> str:
    s = status.upper()
    if s in ("OK", "PASS", "GOOD"):
        return "ok"
    if s in ("WARN", "WARNING"):
        return "warn"
    return "fail"


CATEGORY_NAMES = {
    "account_structure": "Account Structure",
    "keywords": "Keywords",
    "negative_keywords": "Negative Keywords",
    "ad_copy": "Ad Copy",
    "performance": "Performance",
    "budget_bidding": "Budget & Bidding",
    "landing": "Landing Page",
    "creative_fatigue": "Creative Fatigue",
}


def render_category_cards(data: dict) -> str:
    cards = []
    categories = data.get("categories", {})
    for key in ["landing", "creative_fatigue"]:
        if key in data and data[key]:
            categories[key] = data[key]

    for key, cat in categories.items():
        name = CATEGORY_NAMES.get(key, key.replace("_", " ").title())
        score = cat.get("score", 0)
        status = cat.get("status", "FAIL")
        sc = status_class(status)
        cards.append(f"""
        <div class="cat-card">
            <div class="name">{name}</div>
            <div class="score status-{sc}">{score}</div>
            <div class="bar"><div class="bar-fill bar-{sc}" style="width: {score}%"></div></div>
        </div>""")
    return "\n".join(cards)


def render_issues(items: list, css_class: str) -> str:
    if not items:
        return ""
    lines = []
    for item in items:
        if isinstance(item, str):
            lines.append(f'<li class="{css_class}"><div class="issue-title">{item}</div></li>')
        else:
            title = item.get("issue", item.get("title", ""))
            impact = item.get("impact", "")
            fix = item.get("fix", item.get("how_to_fix", ""))
            lines.append(f"""<li class="{css_class}">
                <div class="issue-title">{title}</div>
                {"<div class='issue-impact'>" + impact + "</div>" if impact else ""}
                {"<div class='issue-fix'>" + fix + "</div>" if fix else ""}
            </li>""")
    return "\n".join(lines)


def render_waste(data: dict) -> str:
    amount = data.get("estimated_waste_monthly", 0)
    if not amount:
        return ""
    breakdown = data.get("waste_breakdown", [])
    rows = ""
    for item in breakdown:
        rows += f'<tr><td>{item["source"]}</td><td>{item["amount"]:,} RUB</td></tr>'

    return f"""
    <div class="waste-box">
        <div class="waste-amount">{amount:,} RUB/month</div>
        <div class="waste-label">Estimated budget waste based on audit findings</div>
        {"<div class='waste-breakdown'><table>" + rows + "</table></div>" if rows else ""}
    </div>"""


def generate(data: dict) -> str:
    hs = data.get("health_score", 0)
    circumference = 2 * 3.14159 * 70
    offset = circumference * (1 - hs / 100)

    critical = data.get("critical", [])
    warnings = data.get("warnings", [])
    recommendations = data.get("recommendations", [])

    critical_section = ""
    if critical:
        critical_section = f"""
    <div class="section">
        <h2>Critical Issues</h2>
        <ul class="issues">{render_issues(critical, "critical")}</ul>
    </div>"""

    warnings_section = ""
    if warnings:
        warnings_section = f"""
    <div class="section">
        <h2>Warnings</h2>
        <ul class="issues">{render_issues(warnings, "warning")}</ul>
    </div>"""

    recs_section = ""
    if recommendations:
        recs_section = f"""
    <div class="section">
        <h2>Recommendations</h2>
        <ul class="issues">{render_issues(recommendations, "info")}</ul>
    </div>"""

    period = data.get("period", {})

    return TEMPLATE.format(
        account_name=data.get("account_name", "Unknown"),
        date=data.get("date", datetime.now().strftime("%Y-%m-%d")),
        period_from=period.get("from", ""),
        period_to=period.get("to", ""),
        health_score=hs,
        score_color=score_color(hs),
        circumference=f"{circumference:.1f}",
        score_offset=f"{offset:.1f}",
        waste_section=render_waste(data),
        category_cards=render_category_cards(data),
        critical_section=critical_section,
        warnings_section=warnings_section,
        recommendations_section=recs_section,
    )


def main():
    parser = argparse.ArgumentParser(description="Generate KUBRIK Audit HTML report")
    parser.add_argument("input", help="Path to audit data JSON file")
    parser.add_argument("-o", "--output", default="audit-report.html", help="Output HTML file")
    args = parser.parse_args()

    with open(args.input) as f:
        data = json.load(f)

    html = generate(data)

    with open(args.output, "w") as f:
        f.write(html)

    print(f"Report generated: {args.output}")
    print(f"Health Score: {data.get('health_score', '?')}/100")


if __name__ == "__main__":
    main()
