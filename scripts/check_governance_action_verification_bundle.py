#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def latest_match(base: Path, pattern: str) -> Path | None:
    items = sorted(base.glob(pattern))
    return items[-1] if items else None


def main() -> int:
    p = argparse.ArgumentParser(description="Check governance action verification bundle.")
    p.add_argument("--minutes", required=True, help="Minutes file name, e.g. governance-2026-02-20.md")
    p.add_argument("--actions-dir", default="docs/reports/minutes/actions")
    p.add_argument("--closures-dir", default="docs/reports/minutes/closures")
    p.add_argument("--escalations-dir", default="docs/reports/minutes/escalations")
    p.add_argument("--scope-changes-dir", default="docs/reports/minutes/scope-changes")
    p.add_argument("--deferrals-dir", default="docs/reports/minutes/deferrals")
    p.add_argument("--verifications-dir", default="docs/reports/minutes/verifications")
    p.add_argument("--minutes-dir", default="docs/reports/minutes")
    p.add_argument("--process", default="docs/process/governance-action-verification.md")
    p.add_argument("--checklist", default="docs/checklists/governance-action-verification-checklist.md")
    p.add_argument("--status", default="docs/ticket-status.md")
    args = p.parse_args()

    minutes_file = Path(args.minutes_dir) / args.minutes
    actions_dir = Path(args.actions_dir)
    closures_dir = Path(args.closures_dir)
    escalations_dir = Path(args.escalations_dir)
    scope_changes_dir = Path(args.scope_changes_dir)
    deferrals_dir = Path(args.deferrals_dir)
    verifications_dir = Path(args.verifications_dir)
    process_file = Path(args.process)
    checklist_file = Path(args.checklist)
    status_file = Path(args.status)

    key = args.minutes.replace('.md', '')
    action_register = latest_match(actions_dir, f"*{key}.md")
    closure_report = latest_match(closures_dir, f"*{key}.md")
    escalation_report = latest_match(escalations_dir, f"*{key}.md")
    scope_change_report = latest_match(scope_changes_dir, f"*{key}.md")
    deferral_report = latest_match(deferrals_dir, f"*{key}.md")
    verification_report = latest_match(verifications_dir, f"*{key}.md")

    ok = True

    def check(path: Path | None, label: str) -> None:
        nonlocal ok
        if path and path.exists():
            print(f"[OK] {label} found: {path}")
        else:
            print(f"[NG] {label} missing")
            ok = False

    if minutes_file.exists():
        print(f"[OK] minutes found: {minutes_file}")
    else:
        print(f"[NG] minutes missing: {minutes_file}")
        ok = False

    check(action_register, "action register")
    check(closure_report, "closure report")
    check(escalation_report, "escalation report")
    check(scope_change_report, "scope change report")
    check(deferral_report, "deferral report")
    check(verification_report, "verification report")

    if process_file.exists():
        print(f"[OK] verification process found: {process_file}")
    else:
        print(f"[NG] verification process missing: {process_file}")
        ok = False

    if checklist_file.exists():
        print(f"[OK] verification checklist found: {checklist_file}")
    else:
        print(f"[NG] verification checklist missing: {checklist_file}")
        ok = False

    if status_file.exists():
        print(f"[OK] ticket status found: {status_file}")
    else:
        print(f"[NG] ticket status missing: {status_file}")
        ok = False

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
