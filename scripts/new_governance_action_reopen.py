#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate a governance action reopen markdown.")
    p.add_argument("--id", required=True, help="Reopen id (e.g. GARO-20260221-01)")
    p.add_argument("--minutes", required=True, help="Minutes file name under docs/reports/minutes")
    p.add_argument("--owner", default="manager", help="Owner name")
    p.add_argument("--date", default=str(date.today()), help="Date YYYY-MM-DD")
    p.add_argument("--output-dir", default="docs/reports/minutes/reopens", help="Output directory")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    minutes_slug = args.minutes.replace(".md", "")
    slug = f"{args.id.lower()}-{minutes_slug}.md"
    out = out_dir / slug

    body = f"""# Governance Action Reopen: {args.id}

- Date: {args.date}
- Owner: {args.owner}
- Source Minutes: `docs/reports/minutes/{args.minutes}`

## Reopen Summary
- Total reviewed actions: 3
- Reopened: 1
- Kept Closed: 2

## Reopened Action
| Action ID | Previous State | Reopen Reason | New Owner | New Due | Evidence Gap | Next Escalation |
|---|---|---|---|---|---|---|
| A-03 | Closed | Evidence Gap | bizdev | 2026-03-02 | approval-log trace missing | governance lead (2026-02-28) |

## Recovery Plan
- action register を `Reopened` に更新
- 次サイクル kickoff brief のtop riskへ記載
- 週次risk reviewでclose可否を再判定

## Checklist
- [x] reopen reason を記録
- [x] owner/due を再設定
- [x] closure report 参照を残す

## References
- `docs/process/governance-action-reopen.md`
- `docs/checklists/governance-action-reopen-checklist.md`
- `docs/reports/minutes/closures/gac-20260221-01-governance-2026-02-20.md`
- `docs/ticket-status.md`
"""
    out.write_text(body, encoding="utf-8")
    print(f"[OK] created {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
