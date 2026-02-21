#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def latest_match(base: Path, pattern: str) -> Path | None:
    items = sorted(base.glob(pattern))
    return items[-1] if items else None


def main() -> int:
    p = argparse.ArgumentParser(description="Check annual governance bundle.")
    p.add_argument("--year", required=True, help="Target year, e.g. 2026")
    p.add_argument("--report-dir", default="docs/reports/annual")
    p.add_argument("--process", default="docs/process/annual-governance-planning.md")
    p.add_argument("--risk-register", default="docs/risk-register.md")
    p.add_argument("--status", default="docs/ticket-status.md")
    args = p.parse_args()

    year_key = args.year.lower()
    report_dir = Path(args.report_dir)
    process_file = Path(args.process)
    risk_register_file = Path(args.risk_register)
    status_file = Path(args.status)

    charter = latest_match(report_dir, f"*annual-strategy-charter-{year_key}.md")
    posture = latest_match(report_dir, f"*annual-risk-posture-{year_key}.md")

    ok = True

    if charter and charter.exists():
        print(f"[OK] annual strategy charter: {charter}")
    else:
        print(f"[NG] annual strategy charter missing for {args.year} in {report_dir}")
        ok = False

    if posture and posture.exists():
        print(f"[OK] annual risk posture: {posture}")
    else:
        print(f"[NG] annual risk posture missing for {args.year} in {report_dir}")
        ok = False

    if process_file.exists():
        print(f"[OK] annual process found: {process_file}")
    else:
        print(f"[NG] annual process missing: {process_file}")
        ok = False

    if risk_register_file.exists():
        print(f"[OK] risk register found: {risk_register_file}")
    else:
        print(f"[NG] risk register missing: {risk_register_file}")
        ok = False

    if status_file.exists():
        print(f"[OK] ticket status found: {status_file}")
    else:
        print(f"[NG] ticket status missing: {status_file}")
        ok = False

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
