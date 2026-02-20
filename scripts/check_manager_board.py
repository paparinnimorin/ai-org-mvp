#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
board = ROOT / 'docs' / 'process' / 'manager-task-board.md'

text = board.read_text(encoding='utf-8')
rows = [line for line in text.splitlines() if line.startswith('|')][2:]

path_pat = re.compile(r'`([^`]+)`')
errors = []
checked = 0

for row in rows:
    paths = path_pat.findall(row)
    for rel in paths:
        checked += 1
        p = ROOT / rel
        if not p.exists():
            errors.append(rel)

print(f'[INFO] checked artifact links: {checked}')
if errors:
    print('[ERROR] missing artifacts:')
    for e in errors:
        print(f'- {e}')
    raise SystemExit(1)

print('[OK] manager board artifact links are valid')
