#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def latest_match(base: Path, pattern: str) -> Path | None:
    items = sorted(base.glob(pattern))
    return items[-1] if items else None


def main() -> int:
    p = argparse.ArgumentParser(description="Check governance action scope-change bundle.")
    p.add_argument("--minutes", required=True, help="Minutes file name, e.g. governance-2026-02-20.md")
    p.add_argument("--actions-dir", default="docs/reports/minutes/actions")
    p.add_argument("--escalations-dir", default="docs/reports/minutes/escalations")
    p.add_argument("--scope-changes-dir", default="docs/reports/minutes/scope-changes")
    p.add_argument("--minutes-dir", default="docs/reports/minutes")
    p.add_argument("--process", default="docs/process/governance-action-scope-change.md")
    p.add_argument("--checklist", default="docs/checklists/governance-action-scope-change-checklist.md")
    p.add_argument("--status", default="docs/ticket-status.md")
    args = p.parse_args()

    minutes_file = Path(args.minutes_dir) / args.minutes
    actions_dir = Path(args.actions_dir)
    escalations_dir = Path(args.escalations_dir)
    scope_changes_dir = Path(args.scope_changes_dir)
    process_file = Path(args.process)
    checklist_file = Path(args.checklist)
    status_file = Path(args.status)

    key = args.minutes.replace('.md', '')
    action_register = latest_match(actions_dir, f"*{key}.md")
    escalation_report = latest_match(escalations_dir, f"*{key}.md")
    scope_change_report = latest_match(scope_changes_dir, f"*{key}.md")
    ok = True

    if minutes_file.exists():
        print(f"[OK] minutes found: {minutes_file}")
    else:
        print(f"[NG] minutes missing: {minutes_file}")
        ok = False

    if action_register and action_register.exists():
        print(f"[OK] action register found: {action_register}")
    else:
        print(f"[NG] action register missing for minutes {args.minutes} in {actions_dir}")
        ok = False

    if escalation_report and escalation_report.exists():
        print(f"[OK] escalation report found: {escalation_report}")
    else:
        print(f"[NG] escalation report missing for minutes {args.minutes} in {escalations_dir}")
        ok = False

    if scope_change_report and scope_change_report.exists():
        print(f"[OK] scope change report found: {scope_change_report}")
    else:
        print(f"[NG] scope change report missing for minutes {args.minutes} in {scope_changes_dir}")
        ok = False

    if process_file.exists():
        print(f"[OK] scope change process found: {process_file}")
    else:
        print(f"[NG] scope change process missing: {process_file}")
        ok = False

    if checklist_file.exists():
        print(f"[OK] scope change checklist found: {checklist_file}")
    else:
        print(f"[NG] scope change checklist missing: {checklist_file}")
        ok = False

    if status_file.exists():
        print(f"[OK] ticket status found: {status_file}")
    else:
        print(f"[NG] ticket status missing: {status_file}")
        ok = False

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
