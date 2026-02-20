#!/usr/bin/env python3
import argparse
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('--day', required=True, help='e.g. day1')
a = p.parse_args()

out = Path('docs/logs/dryrun') / f'{a.day}.md'
out.parent.mkdir(parents=True, exist_ok=True)
if out.exists():
    print(f'[SKIP] exists: {out}')
    raise SystemExit(0)

out.write_text(f"""# Dryrun {a.day.upper()}\n\n## Executed\n- \n\n## Issues\n- \n\n## Escalations\n- \n\n## KPI Notes\n- \n""")
print(f'[OK] created {out}')
