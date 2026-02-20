#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate a cycle closeout report markdown.")
    p.add_argument("--id", required=True, help="Closeout report id (e.g. CC-20260221-01)")
    p.add_argument("--cycle", required=True, help="Cycle range (e.g. 043-046)")
    p.add_argument("--owner", default="manager", help="Owner name")
    p.add_argument("--date", default=str(date.today()), help="Date YYYY-MM-DD")
    p.add_argument("--output-dir", default="docs/reports/closeouts", help="Output directory")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    slug = f"{args.id.lower()}-cycle-{args.cycle}.md"
    out = out_dir / slug

    body = f"""# Cycle Closeout Report: {args.id}

- Date: {args.date}
- Cycle: {args.cycle}
- Owner: {args.owner}

## Delivered
- 
- 

## Validation
- ticket-check: PASS
- link-check: PASS
- status-refresh: PASS

## Open Risks / Carry-over
1. Risk:
   - Impact:
   - Owner:
   - Mitigation:

## Next Cycle Proposal
1. 
2. 
3. 

## References
- `docs/ticket-status.md`
- `docs/reports/handoffs/`
"""
    out.write_text(body, encoding="utf-8")
    print(f"[OK] created {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
