#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate a cycle midcheck report markdown.")
    p.add_argument("--id", required=True, help="Midcheck report id (e.g. MC-20260221-01)")
    p.add_argument("--cycle", required=True, help="Cycle range (e.g. 051-054)")
    p.add_argument("--owner", default="manager", help="Owner name")
    p.add_argument("--date", default=str(date.today()), help="Date YYYY-MM-DD")
    p.add_argument("--output-dir", default="docs/reports/midchecks", help="Output directory")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    slug = f"{args.id.lower()}-cycle-{args.cycle}.md"
    out = out_dir / slug

    body = f"""# Cycle Midcheck Report: {args.id}

- Date: {args.date}
- Cycle: {args.cycle}
- Owner: {args.owner}

## Progress Snapshot
- Done:
- In Progress:
- Blocked:

## KPI Proxy
- Completed tickets:
- Delayed tickets:
- Blocked tickets:

## Risk Review
1. Risk:
   - Impact:
   - Owner:
   - Mitigation:

## Replan (Next 48h)
- Action / Owner / Due:
- Action / Owner / Due:

## Decisions
- Scope:
- Priority changes:
- Approval needed:

## References
- `docs/process/cycle-midcheck-review.md`
- `docs/checklists/manager-cycle-midcheck-checklist.md`
- `docs/ticket-status.md`
"""
    out.write_text(body, encoding="utf-8")
    print(f"[OK] created {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
