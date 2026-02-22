#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def latest_match(base: Path, pattern: str) -> Path | None:
    items = sorted(base.glob(pattern))
    return items[-1] if items else None


def main() -> int:
    p = argparse.ArgumentParser(description="Check governance action cancellation bundle.")
    p.add_argument("--minutes", required=True, help="Minutes file name, e.g. governance-2026-02-20.md")
    p.add_argument("--actions-dir", default="docs/reports/minutes/actions")
    p.add_argument("--verifications-dir", default="docs/reports/minutes/verifications")
    p.add_argument("--cancellations-dir", default="docs/reports/minutes/cancellations")
    p.add_argument("--minutes-dir", default="docs/reports/minutes")
    p.add_argument("--process", default="docs/process/governance-action-cancellation.md")
    p.add_argument("--checklist", default="docs/checklists/governance-action-cancellation-checklist.md")
    p.add_argument("--status", default="docs/ticket-status.md")
    args = p.parse_args()

    minutes_file = Path(args.minutes_dir) / args.minutes
    actions_dir = Path(args.actions_dir)
    verifications_dir = Path(args.verifications_dir)
    cancellations_dir = Path(args.cancellations_dir)
    process_file = Path(args.process)
    checklist_file = Path(args.checklist)
    status_file = Path(args.status)

    key = args.minutes.replace('.md', '')
    action_register = latest_match(actions_dir, f"*{key}.md")
    verification_report = latest_match(verifications_dir, f"*{key}.md")
    cancellation_report = latest_match(cancellations_dir, f"*{key}.md")

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
    check(verification_report, "verification report")
    check(cancellation_report, "cancellation report")

    if process_file.exists():
        print(f"[OK] cancellation process found: {process_file}")
    else:
        print(f"[NG] cancellation process missing: {process_file}")
        ok = False

    if checklist_file.exists():
        print(f"[OK] cancellation checklist found: {checklist_file}")
    else:
        print(f"[NG] cancellation checklist missing: {checklist_file}")
        ok = False

    if status_file.exists():
        print(f"[OK] ticket status found: {status_file}")
    else:
        print(f"[NG] ticket status missing: {status_file}")
        ok = False

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
