#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def latest_match(base: Path, pattern: str) -> Path | None:
    items = sorted(base.glob(pattern))
    return items[-1] if items else None


def main() -> int:
    p = argparse.ArgumentParser(description="Check quarterly governance bundle.")
    p.add_argument("--quarter", required=True, help="Target quarter, e.g. 2026-Q1")
    p.add_argument("--report-dir", default="docs/reports/quarterly")
    p.add_argument("--process", default="docs/process/quarterly-governance-planning.md")
    p.add_argument("--risk-register", default="docs/risk-register.md")
    p.add_argument("--status", default="docs/ticket-status.md")
    args = p.parse_args()

    quarter_key = args.quarter.lower()
    report_dir = Path(args.report_dir)
    process_file = Path(args.process)
    risk_register_file = Path(args.risk_register)
    status_file = Path(args.status)

    strategy = latest_match(report_dir, f"*quarterly-strategy-brief-{quarter_key}.md")
    rebalance = latest_match(report_dir, f"*quarterly-risk-rebalance-{quarter_key}.md")

    ok = True

    if strategy and strategy.exists():
        print(f"[OK] quarterly strategy brief: {strategy}")
    else:
        print(f"[NG] quarterly strategy brief missing for {args.quarter} in {report_dir}")
        ok = False

    if rebalance and rebalance.exists():
        print(f"[OK] quarterly risk rebalance: {rebalance}")
    else:
        print(f"[NG] quarterly risk rebalance missing for {args.quarter} in {report_dir}")
        ok = False

    if process_file.exists():
        print(f"[OK] quarterly process found: {process_file}")
    else:
        print(f"[NG] quarterly process missing: {process_file}")
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
