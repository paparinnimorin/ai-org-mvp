#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def latest_match(base: Path, pattern: str) -> Path | None:
    items = sorted(base.glob(pattern))
    return items[-1] if items else None


def main() -> int:
    p = argparse.ArgumentParser(description="Check governance action closure bundle.")
    p.add_argument("--minutes", required=True, help="Minutes file name, e.g. governance-2026-02-20.md")
    p.add_argument("--actions-dir", default="docs/reports/minutes/actions")
    p.add_argument("--closures-dir", default="docs/reports/minutes/closures")
    p.add_argument("--minutes-dir", default="docs/reports/minutes")
    p.add_argument("--process", default="docs/process/governance-action-closure.md")
    p.add_argument("--checklist", default="docs/checklists/governance-action-closure-checklist.md")
    p.add_argument("--status", default="docs/ticket-status.md")
    args = p.parse_args()

    minutes_file = Path(args.minutes_dir) / args.minutes
    actions_dir = Path(args.actions_dir)
    closures_dir = Path(args.closures_dir)
    process_file = Path(args.process)
    checklist_file = Path(args.checklist)
    status_file = Path(args.status)

    key = args.minutes.replace('.md', '')
    action_register = latest_match(actions_dir, f"*{key}.md")
    closure_report = latest_match(closures_dir, f"*{key}.md")
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

    if closure_report and closure_report.exists():
        print(f"[OK] closure report found: {closure_report}")
    else:
        print(f"[NG] closure report missing for minutes {args.minutes} in {closures_dir}")
        ok = False

    if process_file.exists():
        print(f"[OK] closure process found: {process_file}")
    else:
        print(f"[NG] closure process missing: {process_file}")
        ok = False

    if checklist_file.exists():
        print(f"[OK] closure checklist found: {checklist_file}")
    else:
        print(f"[NG] closure checklist missing: {checklist_file}")
        ok = False

    if status_file.exists():
        print(f"[OK] ticket status found: {status_file}")
    else:
        print(f"[NG] ticket status missing: {status_file}")
        ok = False

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
