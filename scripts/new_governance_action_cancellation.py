#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate a governance action cancellation markdown.")
    p.add_argument("--id", required=True, help="Cancellation id (e.g. GAX-20260222-01)")
    p.add_argument("--minutes", required=True, help="Minutes file name under docs/reports/minutes")
    p.add_argument("--owner", default="manager", help="Owner name")
    p.add_argument("--date", default=str(date.today()), help="Date YYYY-MM-DD")
    p.add_argument("--output-dir", default="docs/reports/minutes/cancellations", help="Output directory")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    minutes_slug = args.minutes.replace(".md", "")
    slug = f"{args.id.lower()}-{minutes_slug}.md"
    out = out_dir / slug

    body = f"""# Governance Action Cancellation: {args.id}

- Date: {args.date}
- Owner: {args.owner}
- Source Minutes: `docs/reports/minutes/{args.minutes}`

## Cancellation Scope
- Action Set: A-05 .. A-06
- Decision Type: cancellation
- Audit Focus: reason traceability + restart condition

## Cancellation Decisions
| Action | Previous Status | Cancel Reason | Approval | Restart Condition |
|---|---|---|---|---|
| A-05 | open | duplicate with A-03 scope-change path | manager-approved | reopen only if A-03 split is rejected |
| A-06 | deferred | external dependency retired (obsolete) | manager-approved | create new action only when strategy changes |

## Risk / KPI Impact
- cancellationにより短期負荷は減少、ただしA-03側の依存度が上がる
- KPI影響: throughputは維持、pending件数を2件減算
- 監査観点: cancel理由と再開条件が明示されていれば問題なし

## Cancellation Decision
- Verdict: **APPROVED**
- Follow-up: next minutesでA-03の単一点依存リスクを再確認
- Next Review Date: 2026-02-26

## References
- `docs/process/governance-action-cancellation.md`
- `docs/checklists/governance-action-cancellation-checklist.md`
- `docs/reports/minutes/actions/gar-20260221-01-governance-2026-02-20.md`
- `docs/reports/minutes/verifications/gav-20260222-01-governance-2026-02-20.md`
- `docs/ticket-status.md`
"""
    out.write_text(body, encoding="utf-8")
    print(f"[OK] created {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
