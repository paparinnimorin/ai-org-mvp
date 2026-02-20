#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def latest_match(base: Path, pattern: str) -> Path | None:
    items = sorted(base.glob(pattern))
    return items[-1] if items else None


def main() -> int:
    p = argparse.ArgumentParser(description="Check cycle midcheck bundle.")
    p.add_argument("--cycle", required=True, help="Cycle range, e.g. 051-054")
    p.add_argument("--midcheck-dir", default="docs/reports/midchecks")
    p.add_argument("--status", default="docs/ticket-status.md")
    p.add_argument("--process", default="docs/process/cycle-midcheck-review.md")
    p.add_argument("--checklist", default="docs/checklists/manager-cycle-midcheck-checklist.md")
    args = p.parse_args()

    midcheck_dir = Path(args.midcheck_dir)
    status_file = Path(args.status)
    process_file = Path(args.process)
    checklist_file = Path(args.checklist)

    midcheck = latest_match(midcheck_dir, f"*cycle-{args.cycle}.md")
    ok = True

    if midcheck and midcheck.exists():
        print(f"[OK] midcheck report: {midcheck}")
    else:
        print(f"[NG] midcheck report missing for cycle {args.cycle} in {midcheck_dir}")
        ok = False

    if process_file.exists():
        print(f"[OK] midcheck process found: {process_file}")
    else:
        print(f"[NG] midcheck process missing: {process_file}")
        ok = False

    if checklist_file.exists():
        print(f"[OK] midcheck checklist found: {checklist_file}")
    else:
        print(f"[NG] midcheck checklist missing: {checklist_file}")
        ok = False

    if status_file.exists():
        print(f"[OK] ticket status found: {status_file}")
    else:
        print(f"[NG] ticket status missing: {status_file}")
        ok = False

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
