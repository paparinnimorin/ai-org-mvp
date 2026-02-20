#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate a cycle kickoff brief markdown.")
    p.add_argument("--id", required=True, help="Kickoff brief id (e.g. KB-20260221-01)")
    p.add_argument("--cycle", required=True, help="Cycle range (e.g. 047-050)")
    p.add_argument("--owner", default="manager", help="Owner name")
    p.add_argument("--date", default=str(date.today()), help="Date YYYY-MM-DD")
    p.add_argument("--output-dir", default="docs/reports/kickoffs", help="Output directory")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    slug = f"{args.id.lower()}-cycle-{args.cycle}.md"
    out = out_dir / slug

    body = f"""# Cycle Kickoff Brief: {args.id}

- Date: {args.date}
- Cycle: {args.cycle}
- Owner: {args.owner}

## Goals
1. Define cycle priorities and owners.
2. Confirm dependencies and first 48h actions.
3. Start execution without kickoff delay.

## Ticket Scope
- {args.cycle}

## Ownership
- Ticket: <fill> / Owner: <fill> / Due: <fill>

## Dependencies
1. 
2. 

## Early Risks
1. Risk:
   - Impact:
   - Mitigation:

## First 48h Plan
- Day1:
- Day2:

## References
- `docs/process/cycle-kickoff-readiness.md`
- `docs/checklists/manager-cycle-kickoff-checklist.md`
- `docs/ticket-status.md`
"""
    out.write_text(body, encoding="utf-8")
    print(f"[OK] created {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
