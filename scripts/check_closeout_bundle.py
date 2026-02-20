#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def latest_match(base: Path, pattern: str) -> Path | None:
    items = sorted(base.glob(pattern))
    return items[-1] if items else None


def main() -> int:
    p = argparse.ArgumentParser(description="Check cycle closeout handoff bundle.")
    p.add_argument("--cycle", required=True, help="Cycle range, e.g. 043-046")
    p.add_argument("--closeout-dir", default="docs/reports/closeouts")
    p.add_argument("--handoff-dir", default="docs/reports/handoffs")
    p.add_argument("--status", default="docs/ticket-status.md")
    args = p.parse_args()

    closeout_dir = Path(args.closeout_dir)
    handoff_dir = Path(args.handoff_dir)
    status_file = Path(args.status)

    closeout = latest_match(closeout_dir, f"*cycle-{args.cycle}.md")
    handoff = latest_match(handoff_dir, "*.md")

    ok = True

    if closeout and closeout.exists():
        print(f"[OK] closeout report: {closeout}")
    else:
        print(f"[NG] closeout report missing for cycle {args.cycle} in {closeout_dir}")
        ok = False

    if handoff and handoff.exists():
        print(f"[OK] latest handoff note: {handoff}")
    else:
        print(f"[NG] handoff note missing in {handoff_dir}")
        ok = False

    if status_file.exists():
        print(f"[OK] ticket status found: {status_file}")
    else:
        print(f"[NG] ticket status missing: {status_file}")
        ok = False

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
