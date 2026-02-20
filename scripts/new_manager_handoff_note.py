#!/usr/bin/env python3
from pathlib import Path
import argparse
import re

ROOT = Path(__file__).resolve().parents[1]


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-') or 'handoff'


def main() -> None:
    ap = argparse.ArgumentParser(description='Create a manager handoff note under docs/reports/handoffs/')
    ap.add_argument('--id', required=True, help='Handoff id, e.g. HN-20260221-01')
    ap.add_argument('--from-owner', required=True, dest='from_owner')
    ap.add_argument('--to-owner', required=True, dest='to_owner')
    ap.add_argument('--date', required=True, help='YYYY-MM-DD')
    ap.add_argument('--focus', default='daily handoff')
    args = ap.parse_args()

    out_dir = ROOT / 'docs' / 'reports' / 'handoffs'
    out_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{args.id.lower()}-{slugify(args.focus)}.md"
    out = out_dir / filename

    content = f"""# Manager Handoff Note: {args.id}

- Date: {args.date}
- From: {args.from_owner}
- To: {args.to_owner}
- Focus: {args.focus}

## Current State
- Active tickets:
- In-flight deliverables:

## Risks / Blockers
- Risk:
  - Impact:
  - Owner:
  - ETA:

## Next 24h Actions
1.
2.
3.

## Escalation Flags
- [ ] Approval gate breach risk
- [ ] KPI update delay (>24h)
- [ ] Safety/incident review required

## References
- `docs/process/manager-handoff-protocol.md`
- `docs/checklists/manager-handoff-checklist.md`
"""
    out.write_text(content, encoding='utf-8')
    print(out)


if __name__ == '__main__':
    main()
