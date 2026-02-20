#!/usr/bin/env python3
import argparse
import csv
import re
from pathlib import Path

REQ = [
    'week','operating_margin','availability','automation_rate','content_throughput','learning_completion'
]

def fail(msg):
    raise SystemExit(f'[ERROR] {msg}')

def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', default='data/kpi/weekly-input.csv')
    ap.add_argument('--output', default='docs/reports/weekly-kpi-snapshot.md')
    return ap.parse_args()

def validate_row(r):
    for k in REQ:
        if k not in r or r[k] == '':
            fail(f'missing value: {k}')
    if not re.match(r'^\d{4}-W\d{2}$', r['week']):
        fail('week must be YYYY-Www')
    for k in ('operating_margin','availability','automation_rate','learning_completion'):
        v = float(r[k])
        if v < 0 or v > 1:
            fail(f'{k} must be 0..1')
    if int(r['content_throughput']) < 0:
        fail('content_throughput must be >=0')

def main():
    a=parse_args()
    inp=Path(a.input)
    out=Path(a.output)
    if not inp.exists():
        fail(f'input not found: {inp}')

    with inp.open() as f:
        reader=csv.DictReader(f)
        if reader.fieldnames != REQ:
            fail('header mismatch')
        rows=list(reader)
    if not rows:
        fail('no data rows')

    for r in rows:
        validate_row(r)

    r=rows[-1]
    md=f"""# Weekly KPI Snapshot ({r['week']})

| KPI | Value |
|---|---:|
| Operating Margin | {float(r['operating_margin'])*100:.1f}% |
| Availability | {float(r['availability'])*100:.2f}% |
| Automation Rate | {float(r['automation_rate'])*100:.1f}% |
| Content Throughput | {r['content_throughput']} |
| Learning Completion | {float(r['learning_completion'])*100:.1f}% |

_Generated from `{inp}`._
"""
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md)
    print(f'[OK] wrote {out}')

if __name__=='__main__':
    main()
