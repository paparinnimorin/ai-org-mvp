#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def latest_match(base: Path, pattern: str) -> Path | None:
    items = sorted(base.glob(pattern))
    return items[-1] if items else None


def main() -> int:
    p = argparse.ArgumentParser(description="Check governance action escalation bundle.")
    p.add_argument("--minutes", required=True, help="Minutes file name, e.g. governance-2026-02-20.md")
    p.add_argument("--actions-dir", default="docs/reports/minutes/actions")
    p.add_argument("--reopens-dir", default="docs/reports/minutes/reopens")
    p.add_argument("--escalations-dir", default="docs/reports/minutes/escalations")
    p.add_argument("--minutes-dir", default="docs/reports/minutes")
    p.add_argument("--process", default="docs/process/governance-action-escalation.md")
    p.add_argument("--checklist", default="docs/checklists/governance-action-escalation-checklist.md")
    p.add_argument("--status", default="docs/ticket-status.md")
    args = p.parse_args()

    minutes_file = Path(args.minutes_dir) / args.minutes
    actions_dir = Path(args.actions_dir)
    reopens_dir = Path(args.reopens_dir)
    escalations_dir = Path(args.escalations_dir)
    process_file = Path(args.process)
    checklist_file = Path(args.checklist)
    status_file = Path(args.status)

    key = args.minutes.replace('.md', '')
    action_register = latest_match(actions_dir, f"*{key}.md")
    reopen_report = latest_match(reopens_dir, f"*{key}.md")
    escalation_report = latest_match(escalations_dir, f"*{key}.md")
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

    if reopen_report and reopen_report.exists():
        print(f"[OK] reopen report found: {reopen_report}")
    else:
        print(f"[NG] reopen report missing for minutes {args.minutes} in {reopens_dir}")
        ok = False

    if escalation_report and escalation_report.exists():
        print(f"[OK] escalation report found: {escalation_report}")
    else:
        print(f"[NG] escalation report missing for minutes {args.minutes} in {escalations_dir}")
        ok = False

    if process_file.exists():
        print(f"[OK] escalation process found: {process_file}")
    else:
        print(f"[NG] escalation process missing: {process_file}")
        ok = False

    if checklist_file.exists():
        print(f"[OK] escalation checklist found: {checklist_file}")
    else:
        print(f"[NG] escalation checklist missing: {checklist_file}")
        ok = False

    if status_file.exists():
        print(f"[OK] ticket status found: {status_file}")
    else:
        print(f"[NG] ticket status missing: {status_file}")
        ok = False

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
