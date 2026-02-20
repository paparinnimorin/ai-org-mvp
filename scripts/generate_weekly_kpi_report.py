#!/usr/bin/env python3
import csv
from pathlib import Path

root = Path(__file__).resolve().parents[1]
input_csv = root / 'data' / 'kpi' / 'weekly-input.example.csv'
out = root / 'docs' / 'reports' / 'weekly-kpi-snapshot.md'
out.parent.mkdir(parents=True, exist_ok=True)

with input_csv.open() as f:
    row = list(csv.DictReader(f))[-1]

md = f"""# Weekly KPI Snapshot ({row['week']})

| KPI | Value |
|---|---:|
| Operating Margin | {float(row['operating_margin'])*100:.1f}% |
| Availability | {float(row['availability'])*100:.2f}% |
| Automation Rate | {float(row['automation_rate'])*100:.1f}% |
| Content Throughput | {row['content_throughput']} |
| Learning Completion | {float(row['learning_completion'])*100:.1f}% |
"""
out.write_text(md)
print(f"[OK] wrote {out}")
