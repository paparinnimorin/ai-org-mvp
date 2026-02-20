#!/usr/bin/env python3
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
ticket_dir = root / 'docs' / 'tickets'
pat = re.compile(r'- \[( |x)\] ')

rows = []
for p in sorted(ticket_dir.glob('*.md')):
    txt = p.read_text(encoding='utf-8')
    marks = pat.findall(txt)
    total = len(marks)
    done = txt.count('- [x] ')
    open_ = txt.count('- [ ] ')
    status = 'DONE' if open_ == 0 and total > 0 else 'OPEN'
    rows.append((p.name, done, total, status))

print('# Ticket Progress')
for name, done, total, status in rows:
    print(f'- {name}: {done}/{total} [{status}]')

open_items = [r for r in rows if r[3] != 'DONE']
if open_items:
    raise SystemExit(1)
