#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate annual strategy charter markdown.")
    p.add_argument("--id", required=True, help="Charter id (e.g. ASC-2026-01)")
    p.add_argument("--year", required=True, help="Target year (e.g. 2026)")
    p.add_argument("--owner", default="manager", help="Owner name")
    p.add_argument("--date", default=str(date.today()), help="Date YYYY-MM-DD")
    p.add_argument("--output-dir", default="docs/reports/annual", help="Output directory")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    slug = f"{args.id.lower()}-annual-strategy-charter-{args.year}.md"
    out = out_dir / slug

    body = f"""# Annual Strategy Charter: {args.id}

- Date: {args.date}
- Target Year: {args.year}
- Owner: {args.owner}

## Last Year Retrospective
- Wins:
- Misses:
- Carry-over:

## Strategic Themes (Top 3)
1.
2.
3.

## Division Operating Priorities
- Content:
- BizDev:
- Tech:
- Ops:

## Governance Targets
- KPI target shifts:
- Approval guardrails:
- Decision cadence:

## References
- `docs/process/annual-governance-planning.md`
- `docs/risk-register.md`
- `docs/ticket-status.md`
"""
    out.write_text(body, encoding="utf-8")
    print(f"[OK] created {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
