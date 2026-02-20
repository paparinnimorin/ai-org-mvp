#!/usr/bin/env python3
from pathlib import Path
import argparse
import re

ROOT = Path(__file__).resolve().parents[1]


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-') or 'brief'


def main() -> None:
    ap = argparse.ArgumentParser(description='Create a manager brief markdown under docs/briefs/')
    ap.add_argument('--id', required=True, help='Brief id, e.g. MB-20260221-01')
    ap.add_argument('--title', required=True, help='Brief title')
    ap.add_argument('--ticket', default='TBD', help='Related ticket numbers')
    ap.add_argument('--owner', default='unassigned')
    ap.add_argument('--due', default='TBD')
    args = ap.parse_args()

    out_dir = ROOT / 'docs' / 'briefs'
    out_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{args.id.lower()}-{slugify(args.title)}.md"
    out = out_dir / filename

    content = f"""# Manager Brief: {args.id} {args.title}

- Ticket(s): {args.ticket}
- Owner: {args.owner}
- Due: {args.due}
- Priority: P1

## Goal
- <達成条件を1-2行で記述>

## Deliverables
- <artifact-path-1>

## Todo (fine-grained)
- [ ] <実装項目1>
- [ ] docs/README.md にリンク追加
- [ ] 検証コマンド実行

## Verify
- `python3 scripts/check_tickets.py`
- `python3 scripts/check_readme_links.py`
- `python3 scripts/check_manager_board.py`

## Risks / Dependencies
- dependency: <ticket/file>
- risk: <note>
"""
    out.write_text(content, encoding='utf-8')
    print(out)


if __name__ == '__main__':
    main()
