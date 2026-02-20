#!/usr/bin/env python3
from pathlib import Path
import argparse
import re

ROOT = Path(__file__).resolve().parents[1]


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-') or 'task'


def main() -> None:
    ap = argparse.ArgumentParser(description='Create a task card markdown under docs/checklists/tasks/')
    ap.add_argument('--id', required=True, help='Task id, e.g. T-031A')
    ap.add_argument('--title', required=True, help='Task title')
    ap.add_argument('--owner', default='unassigned')
    ap.add_argument('--due', default='TBD')
    args = ap.parse_args()

    out_dir = ROOT / 'docs' / 'checklists' / 'tasks'
    out_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{args.id.lower()}-{slugify(args.title)}.md"
    out = out_dir / filename

    content = f"""# Task Card: {args.id} {args.title}

- Owner: {args.owner}
- Due: {args.due}
- Status: TODO

## Goal
- <what to achieve>

## Deliverables
- <artifact-1>

## Todo (ultra-fine)
- [ ] <implement item-1>
- [ ] docs/README.md にリンク追記
- [ ] 検証コマンド実行

## Verify
- `python3 scripts/check_tickets.py`
- `python3 scripts/check_readme_links.py`

## Notes
- <risks/dependencies>
"""
    out.write_text(content, encoding='utf-8')
    print(out)


if __name__ == '__main__':
    main()
