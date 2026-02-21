#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate quarterly strategy brief markdown.")
    p.add_argument("--id", required=True, help="Brief id (e.g. QSB-2026Q1-01)")
    p.add_argument("--quarter", required=True, help="Target quarter (e.g. 2026-Q1)")
    p.add_argument("--owner", default="manager", help="Owner name")
    p.add_argument("--date", default=str(date.today()), help="Date YYYY-MM-DD")
    p.add_argument("--output-dir", default="docs/reports/quarterly", help="Output directory")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    slug = f"{args.id.lower()}-quarterly-strategy-brief-{args.quarter.lower()}.md"
    out = out_dir / slug

    body = f"""# Quarterly Strategy Brief: {args.id}

- Date: {args.date}
- Target Quarter: {args.quarter}
- Owner: {args.owner}

## Quarter Retrospective
- Wins:
- Misses:
- Carry-over:

## Next Quarter Priorities (Top 3)
1.
2.
3.

## Capacity & Allocation
- Content:
- BizDev:
- Tech:
- Ops:

## Decision Log (Summary)
- Keep:
- Change:
- Stop:

## References
- `docs/process/quarterly-governance-planning.md`
- `docs/templates/monthly-tuning-review.md`
- `docs/ticket-status.md`
"""
    out.write_text(body, encoding="utf-8")
    print(f"[OK] created {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
