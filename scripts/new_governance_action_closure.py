#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate a governance action closure markdown.")
    p.add_argument("--id", required=True, help="Closure id (e.g. GAC-20260221-01)")
    p.add_argument("--minutes", required=True, help="Minutes file name under docs/reports/minutes")
    p.add_argument("--owner", default="manager", help="Owner name")
    p.add_argument("--date", default=str(date.today()), help="Date YYYY-MM-DD")
    p.add_argument("--output-dir", default="docs/reports/minutes/closures", help="Output directory")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    minutes_slug = args.minutes.replace(".md", "")
    slug = f"{args.id.lower()}-{minutes_slug}.md"
    out = out_dir / slug

    body = f"""# Governance Action Closure: {args.id}

- Date: {args.date}
- Owner: {args.owner}
- Source Minutes: `docs/reports/minutes/{args.minutes}`

## Closure Summary
- Total actions: 3
- Closed: 1
- Carry Over: 1
- Blocked: 1

## Action Disposition
| Action ID | Owner | Previous Due | Current Status | Evidence | Next Step | Escalation |
|---|---|---|---|---|---|---|
| A-01 | ops | 2026-02-24 | Closed | KPI note updated in weekly brief | none | none |
| A-02 | tech | 2026-02-25 | Carry Over | mitigation mapping draft shared | finalize by 2026-02-28 | manager |
| A-03 | bizdev | 2026-02-26 | Blocked | approval-log gap identified | data fix then re-run | governance lead (2026-02-27) |

## Carry-over Plan
- A-02 を次サイクル kickoff brief の重点項目へ転記
- A-03 は blocked解除まで毎日ステータス確認

## Closure Criteria
- [x] 各actionの最終statusを確定
- [x] Blocked項目に escalation を設定
- [x] 次サイクルへの引継ぎ先を明記

## References
- `docs/process/governance-action-closure.md`
- `docs/checklists/governance-action-closure-checklist.md`
- `docs/process/governance-minutes-followup.md`
- `docs/ticket-status.md`
"""
    out.write_text(body, encoding="utf-8")
    print(f"[OK] created {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
