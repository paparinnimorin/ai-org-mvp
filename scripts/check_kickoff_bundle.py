#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def latest_match(base: Path, pattern: str) -> Path | None:
    items = sorted(base.glob(pattern))
    return items[-1] if items else None


def main() -> int:
    p = argparse.ArgumentParser(description="Check cycle kickoff bundle.")
    p.add_argument("--cycle", required=True, help="Cycle range, e.g. 047-050")
    p.add_argument("--kickoff-dir", default="docs/reports/kickoffs")
    p.add_argument("--status", default="docs/ticket-status.md")
    p.add_argument("--process", default="docs/process/cycle-kickoff-readiness.md")
    args = p.parse_args()

    kickoff_dir = Path(args.kickoff_dir)
    status_file = Path(args.status)
    process_file = Path(args.process)

    kickoff = latest_match(kickoff_dir, f"*cycle-{args.cycle}.md")
    ok = True

    if kickoff and kickoff.exists():
        print(f"[OK] kickoff brief: {kickoff}")
    else:
        print(f"[NG] kickoff brief missing for cycle {args.cycle} in {kickoff_dir}")
        ok = False

    if process_file.exists():
        print(f"[OK] kickoff process found: {process_file}")
    else:
        print(f"[NG] kickoff process missing: {process_file}")
        ok = False

    if status_file.exists():
        print(f"[OK] ticket status found: {status_file}")
    else:
        print(f"[NG] ticket status missing: {status_file}")
        ok = False

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
