#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate monthly governance review markdown.")
    p.add_argument("--id", required=True, help="Review id (e.g. MR-202602-01)")
    p.add_argument("--month", required=True, help="Target month YYYY-MM")
    p.add_argument("--owner", default="manager", help="Owner name")
    p.add_argument("--date", default=str(date.today()), help="Date YYYY-MM-DD")
    p.add_argument("--output-dir", default="docs/reports/monthly", help="Output directory")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    slug = f"{args.id.lower()}-monthly-governance-review-{args.month}.md"
    out = out_dir / slug

    body = f"""# Monthly Governance Review: {args.id}

- Date: {args.date}
- Target Month: {args.month}
- Owner: {args.owner}

## KPI Summary
- Throughput:
- Quality:
- SLA/Latency:

## Approval & Risk Summary
- Approval exceptions:
- Top risks:
- Incident trend:

## Process Tuning Decisions
- Keep:
- Change:
- Stop:

## Next Month Focus (Top 3)
1.
2.
3.

## References
- `docs/process/monthly-governance-review.md`
- `docs/templates/monthly-tuning-review.md`
- `docs/ticket-status.md`
"""
    out.write_text(body, encoding="utf-8")
    print(f"[OK] created {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
