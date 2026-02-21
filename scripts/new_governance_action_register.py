#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate a governance action register markdown.")
    p.add_argument("--id", required=True, help="Register id (e.g. GAR-20260221-01)")
    p.add_argument("--minutes", required=True, help="Minutes file name under docs/reports/minutes")
    p.add_argument("--owner", default="manager", help="Owner name")
    p.add_argument("--date", default=str(date.today()), help="Date YYYY-MM-DD")
    p.add_argument("--output-dir", default="docs/reports/minutes/actions", help="Output directory")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    minutes_slug = args.minutes.replace(".md", "")
    slug = f"{args.id.lower()}-{minutes_slug}.md"
    out = out_dir / slug

    body = f"""# Governance Action Register: {args.id}

- Date: {args.date}
- Owner: {args.owner}
- Source Minutes: `docs/reports/minutes/{args.minutes}`

## Summary
- Total actions: 3
- High priority: 1
- Blocked: 0
- Overdue: 0

## Actions
| Action ID | Action | Owner | Priority | Due | Status | Dependency | Escalation | Notes |
|---|---|---|---|---|---|---|---|---|
| A-01 | Update KPI trend note for next cycle brief | ops | High | 2026-02-24 | Open | weekly KPI input | manager | tie to kickoff section 2 |
| A-02 | Refresh risk register mitigation owner mapping | tech | Med | 2026-02-25 | Open | risk register | governance lead | sync with weekly risk review |
| A-03 | Validate approval log completeness for pending items | bizdev | Med | 2026-02-26 | Open | approval log | manager | include rejected cases |

## Review Cadence
- T+24h owner確認: pending
- T+48h blocked対応: pending
- Next governance touchpoint: weekly governance rhythm

## Closure Criteria
- [ ] すべてのActionに owner / due / status が設定済み
- [ ] Blocked項目に escalation と期限が設定済み
- [ ] 次サイクル資料（brief/checklist/task card）へ必要項目を転記済み

## References
- `docs/process/governance-minutes-followup.md`
- `docs/templates/governance-action-register.md`
- `docs/ticket-status.md`
"""
    out.write_text(body, encoding="utf-8")
    print(f"[OK] created {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
