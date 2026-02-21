#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate a governance action scope change markdown.")
    p.add_argument("--id", required=True, help="Scope change id (e.g. GASC-20260221-01)")
    p.add_argument("--minutes", required=True, help="Minutes file name under docs/reports/minutes")
    p.add_argument("--owner", default="manager", help="Owner name")
    p.add_argument("--date", default=str(date.today()), help="Date YYYY-MM-DD")
    p.add_argument("--output-dir", default="docs/reports/minutes/scope-changes", help="Output directory")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    minutes_slug = args.minutes.replace(".md", "")
    slug = f"{args.id.lower()}-{minutes_slug}.md"
    out = out_dir / slug

    body = f"""# Governance Action Scope Change: {args.id}

- Date: {args.date}
- Owner: {args.owner}
- Source Minutes: `docs/reports/minutes/{args.minutes}`

## Scope Change Summary
- Action ID: A-03
- Change Type: deliverable refinement + due realignment
- Previous Due: 2026-02-22
- New Due: 2026-02-26
- KPI Impact: approval trace completeness target 85% -> 95%

## Impact Matrix
| Dimension | Before | After |
|---|---|---|
| Deliverables | manual evidence補填 | API log export + evidence summary |
| Owner | bizdev | tech (primary), bizdev (review) |
| Due Date | 2026-02-22 | 2026-02-26 |
| Risk | 再オープン反復 | 実装依存に集約（管理可能） |

## Options & Decision
- Option A: ownerをtechへ移管し、自動証跡を実装
- Option B: bizdev継続でmanual運用を延長
- Recommended: Option A
- Decision Owner: governance lead
- Decision Due: 2026-02-23

## Acceptance Criteria
- [x] action registerの対象行にowner/due/deliverables更新を反映
- [x] KPI impact noteをminutes follow-upに追記
- [x] next review dateを設定（2026-02-24）

## References
- `docs/process/governance-action-scope-change.md`
- `docs/checklists/governance-action-scope-change-checklist.md`
- `docs/reports/minutes/actions/gar-20260221-01-governance-2026-02-20.md`
- `docs/reports/minutes/escalations/gae-20260221-01-governance-2026-02-20.md`
- `docs/ticket-status.md`
"""
    out.write_text(body, encoding="utf-8")
    print(f"[OK] created {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
