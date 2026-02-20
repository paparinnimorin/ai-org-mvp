#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate monthly approval audit report markdown.")
    p.add_argument("--id", required=True, help="Audit id (e.g. MA-202602-01)")
    p.add_argument("--month", required=True, help="Target month YYYY-MM")
    p.add_argument("--owner", default="manager", help="Owner name")
    p.add_argument("--date", default=str(date.today()), help="Date YYYY-MM-DD")
    p.add_argument("--output-dir", default="docs/reports/monthly", help="Output directory")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    slug = f"{args.id.lower()}-approval-audit-{args.month}.md"
    out = out_dir / slug

    body = f"""# Monthly Approval Audit: {args.id}

- Date: {args.date}
- Target Month: {args.month}
- Owner: {args.owner}

## Audit Scope
- Approval log entries reviewed:
- Decision log entries sampled:

## Findings
- Pass:
- Attention:
- Fail:

## Exceptions
1. Item:
   - Reason:
   - Temporary control:
   - Due:

## Actions
- Action / Owner / Due:
- Action / Owner / Due:

## References
- `docs/checklists/monthly-approval-audit.md`
- `docs/logs/approval-log.md`
- `docs/logs/decision-log.md`
"""
    out.write_text(body, encoding="utf-8")
    print(f"[OK] created {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
