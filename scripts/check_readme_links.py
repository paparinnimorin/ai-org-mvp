#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / 'docs' / 'README.md').read_text(encoding='utf-8')
TICKET_DIR = ROOT / 'docs' / 'tickets'

path_pat = re.compile(r'`((?:docs|scripts|data)/[^`]+)`')

def readme_key(ref: str) -> str | None:
    if ref == 'docs/README.md':
        return None
    if ref.startswith('docs/'):
        return ref[len('docs/'):]
    return ref

missing = []
for ticket in sorted(TICKET_DIR.glob('*.md')):
    text = ticket.read_text(encoding='utf-8')
    refs = sorted(set(path_pat.findall(text)))
    for ref in refs:
        key = readme_key(ref)
        if key is None:
            continue
        if key not in README:
            missing.append((ticket.name, ref))

if missing:
    print('# README Link Check: FAILED')
    for name, ref in missing:
        print(f'- {name}: missing in docs/README.md -> {ref}')
    raise SystemExit(1)

print('# README Link Check: PASS')
print(f'- checked tickets: {len(list(TICKET_DIR.glob("*.md")))}')
