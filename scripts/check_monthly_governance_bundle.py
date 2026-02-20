#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def latest_match(base: Path, pattern: str) -> Path | None:
    items = sorted(base.glob(pattern))
    return items[-1] if items else None


def main() -> int:
    p = argparse.ArgumentParser(description="Check monthly governance bundle.")
    p.add_argument("--month", required=True, help="Target month, e.g. 2026-02")
    p.add_argument("--report-dir", default="docs/reports/monthly")
    p.add_argument("--process", default="docs/process/monthly-governance-review.md")
    p.add_argument("--checklist", default="docs/checklists/monthly-approval-audit.md")
    p.add_argument("--status", default="docs/ticket-status.md")
    args = p.parse_args()

    report_dir = Path(args.report_dir)
    process_file = Path(args.process)
    checklist_file = Path(args.checklist)
    status_file = Path(args.status)

    audit = latest_match(report_dir, f"*approval-audit-{args.month}.md")
    review = latest_match(report_dir, f"*monthly-governance-review-{args.month}.md")
    ok = True

    if audit and audit.exists():
        print(f"[OK] monthly approval audit: {audit}")
    else:
        print(f"[NG] monthly approval audit missing for {args.month} in {report_dir}")
        ok = False

    if review and review.exists():
        print(f"[OK] monthly governance review: {review}")
    else:
        print(f"[NG] monthly governance review missing for {args.month} in {report_dir}")
        ok = False

    if process_file.exists():
        print(f"[OK] monthly process found: {process_file}")
    else:
        print(f"[NG] monthly process missing: {process_file}")
        ok = False

    if checklist_file.exists():
        print(f"[OK] monthly checklist found: {checklist_file}")
    else:
        print(f"[NG] monthly checklist missing: {checklist_file}")
        ok = False

    if status_file.exists():
        print(f"[OK] ticket status found: {status_file}")
    else:
        print(f"[NG] ticket status missing: {status_file}")
        ok = False

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
