#!/usr/bin/env python3
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
ticket_dir = root / 'docs' / 'tickets'
status_file = root / 'docs' / 'ticket-status.md'
pat = re.compile(r'- \[( |x)\] ')

rows = []
for p in sorted(ticket_dir.glob('*.md')):
    txt = p.read_text(encoding='utf-8')
    total = len(pat.findall(txt))
    done = txt.count('- [x] ')
    open_ = txt.count('- [ ] ')
    status = 'DONE' if open_ == 0 and total > 0 else 'OPEN'
    rows.append((p.name, status, done, total))

open_count = sum(1 for _, s, _, _ in rows if s != 'DONE')

snapshot = ['## Current Snapshot']
for name, status, _, _ in rows:
    snapshot.append(f'- {name}: {status}')
snapshot.append('')
snapshot.append('## Summary')
snapshot.append(f'- Total tickets: {len(rows)}')
snapshot.append(f'- Open tickets: {open_count}')
snapshot_txt = '\n'.join(snapshot)

old = status_file.read_text(encoding='utf-8')
new = re.sub(
    r'## Current Snapshot\n[\s\S]*?(?=\n## Next Development Focus)',
    snapshot_txt + '\n',
    old,
)
status_file.write_text(new, encoding='utf-8')

print(f'[OK] updated {status_file}')
print(f'[INFO] total={len(rows)} open={open_count}')
