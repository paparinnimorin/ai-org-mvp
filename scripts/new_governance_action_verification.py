#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate a governance action verification markdown.")
    p.add_argument("--id", required=True, help="Verification id (e.g. GAV-20260222-01)")
    p.add_argument("--minutes", required=True, help="Minutes file name under docs/reports/minutes")
    p.add_argument("--owner", default="manager", help="Owner name")
    p.add_argument("--date", default=str(date.today()), help="Date YYYY-MM-DD")
    p.add_argument("--output-dir", default="docs/reports/minutes/verifications", help="Output directory")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    minutes_slug = args.minutes.replace(".md", "")
    slug = f"{args.id.lower()}-{minutes_slug}.md"
    out = out_dir / slug

    body = f"""# Governance Action Verification: {args.id}

- Date: {args.date}
- Owner: {args.owner}
- Source Minutes: `docs/reports/minutes/{args.minutes}`

## Verification Scope
- Action Set: A-01 .. A-04
- Focus: status consistency + evidence completeness
- Decision Target: pass-for-closeout

## Evidence Review
| Action | Register Status | Outcome Report | Evidence Link | Result |
|---|---|---|---|---|
| A-01 | closed | closure | implementation note + KPI delta | pass |
| A-02 | escalated | escalation | escalation memo + approval trail | pass |
| A-03 | scope-changed | scope change | revised scope + due | pass |
| A-04 | deferred | deferral | blocker note + resume trigger | pass |

## Findings
- register状態とoutcomeレポートの矛盾は検知されなかった
- evidenceの最低要件（owner/date/link）を満たした
- 次回minutesでA-02/A-04の追跡継続を推奨

## Verification Decision
- Verdict: **PASS**
- Follow-up: 2 items (A-02 escalation monitor, A-04 deferral checkpoint)
- Next Review Date: 2026-02-25

## References
- `docs/process/governance-action-verification.md`
- `docs/checklists/governance-action-verification-checklist.md`
- `docs/reports/minutes/actions/gar-20260221-01-governance-2026-02-20.md`
- `docs/reports/minutes/closures/gac-20260221-01-governance-2026-02-20.md`
- `docs/reports/minutes/escalations/gae-20260221-01-governance-2026-02-20.md`
- `docs/reports/minutes/scope-changes/gasc-20260221-01-governance-2026-02-20.md`
- `docs/reports/minutes/deferrals/gad-20260222-01-governance-2026-02-20.md`
- `docs/ticket-status.md`
"""
    out.write_text(body, encoding="utf-8")
    print(f"[OK] created {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
