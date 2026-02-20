#!/usr/bin/env python3
import argparse
from pathlib import Path
from datetime import datetime

p = argparse.ArgumentParser()
p.add_argument('--date', default=datetime.now().strftime('%Y-%m-%d'))
p.add_argument('--attendees', default='')
p.add_argument('--duration', default='30m')
a = p.parse_args()

out = Path('docs/reports/minutes') / f'governance-{a.date}.md'
out.parent.mkdir(parents=True, exist_ok=True)

if out.exists():
    print(f'[SKIP] exists: {out}')
    raise SystemExit(0)

out.write_text(f'''# Governance Meeting Minutes ({a.date})

- Date: {a.date}
- Duration: {a.duration}
- Attendees: {a.attendees}

## Agenda
1. KPI quick review
2. Risks/Incidents
3. Approval items
4. Next actions

## Decisions
- 

## Follow-ups
- [ ] owner / due
''', encoding='utf-8')

print(f'[OK] created {out}')
