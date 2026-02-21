#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate a governance action escalation markdown.")
    p.add_argument("--id", required=True, help="Escalation id (e.g. GAE-20260221-01)")
    p.add_argument("--minutes", required=True, help="Minutes file name under docs/reports/minutes")
    p.add_argument("--owner", default="manager", help="Owner name")
    p.add_argument("--date", default=str(date.today()), help="Date YYYY-MM-DD")
    p.add_argument("--output-dir", default="docs/reports/minutes/escalations", help="Output directory")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    minutes_slug = args.minutes.replace(".md", "")
    slug = f"{args.id.lower()}-{minutes_slug}.md"
    out = out_dir / slug

    body = f"""# Governance Action Escalation: {args.id}

- Date: {args.date}
- Owner: {args.owner}
- Source Minutes: `docs/reports/minutes/{args.minutes}`

## Escalation Summary
- Total reviewed actions: 3
- Escalated: 1
- Level: L2 (Governance Lead)
- Decision Due: 2026-02-23

## Escalated Action
| Action ID | Previous State | Blocker | Escalation Level | Accountable Owner | Required Decision | Target Date |
|---|---|---|---|---|---|---|
| A-03 | Reopened | approval-log trace still missing | L2 | governance lead | owner reassignment + due reset | 2026-02-23 |

## Decision Packet
- Option A: ownerをtechへ再配分し、自動取得ログに置換
- Option B: bizdev継続でmanual evidence補填、dueを+5営業日延長
- 推奨: Option A（再発リスク最小）

## Checklist
- [x] escalation level を確定
- [x] decision due を設定
- [x] next flow（close/reopen/scope change）を定義

## References
- `docs/process/governance-action-escalation.md`
- `docs/checklists/governance-action-escalation-checklist.md`
- `docs/reports/minutes/reopens/garo-20260221-01-governance-2026-02-20.md`
- `docs/ticket-status.md`
"""
    out.write_text(body, encoding="utf-8")
    print(f"[OK] created {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
