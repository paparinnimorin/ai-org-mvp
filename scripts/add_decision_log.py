#!/usr/bin/env python3
import argparse
from pathlib import Path
from datetime import date

p = argparse.ArgumentParser()
p.add_argument('--topic', required=True)
p.add_argument('--decision', required=True)
p.add_argument('--owner', required=True)
p.add_argument('--due', required=True)
p.add_argument('--status', default='Open')
a = p.parse_args()

log = Path('docs/logs/decision-log.md')
if not log.exists():
    log.write_text('# Decision Log\n\n')
entry = f"""- Date: {date.today()}
  - Topic: {a.topic}
  - Decision: {a.decision}
  - Owner: {a.owner}
  - Due: {a.due}
  - Status: {a.status}

"""
log.write_text(log.read_text() + entry)
print('[OK] appended decision log')
