#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate a governance action deferral markdown.")
    p.add_argument("--id", required=True, help="Deferral id (e.g. GAD-20260222-01)")
    p.add_argument("--minutes", required=True, help="Minutes file name under docs/reports/minutes")
    p.add_argument("--owner", default="manager", help="Owner name")
    p.add_argument("--date", default=str(date.today()), help="Date YYYY-MM-DD")
    p.add_argument("--output-dir", default="docs/reports/minutes/deferrals", help="Output directory")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    minutes_slug = args.minutes.replace(".md", "")
    slug = f"{args.id.lower()}-{minutes_slug}.md"
    out = out_dir / slug

    body = f"""# Governance Action Deferral: {args.id}

- Date: {args.date}
- Owner: {args.owner}
- Source Minutes: `docs/reports/minutes/{args.minutes}`

## Deferral Summary
- Action ID: A-04
- Deferral Type: dependency wait
- Previous Due: 2026-02-23
- New Due: 2026-02-28
- Checkpoint Deliverable: blocker list + integration test precheck
- Resume Trigger: Tech deliverable T-042 merged
- KPI Impact: cycle completion rate forecast 0.82 -> 0.78

## Rationale
- 依存先の実装が未マージで、現時点のDoD達成が不可能。
- 無理なclose/reopenを避け、期限を明示して監視可能な状態にする。

## Governance Alignment
- Decision Owner: governance lead
- Decision Due: 2026-02-23
- Next Review Date: 2026-02-25
- Register Update Owner: ops manager

## Acceptance Criteria
- [x] action registerにold/new dueとcheckpointを反映
- [x] minutes follow-upにresume triggerを記録
- [x] 次回review日を設定

## References
- `docs/process/governance-action-deferral.md`
- `docs/checklists/governance-action-deferral-checklist.md`
- `docs/reports/minutes/actions/gar-20260221-01-governance-2026-02-20.md`
- `docs/reports/minutes/scope-changes/gasc-20260221-01-governance-2026-02-20.md`
- `docs/ticket-status.md`
"""
    out.write_text(body, encoding="utf-8")
    print(f"[OK] created {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
