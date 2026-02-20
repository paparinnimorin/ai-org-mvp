# KPI Data Pipeline Spec

## CSV Header (required)
`week,operating_margin,availability,automation_rate,content_throughput,learning_completion`

## Validation Rules
- `week`: `YYYY-Www` format
- ratio fields: `0.0 - 1.0`
- `content_throughput`: non-negative integer
- 欠損値がある行は集計対象外（エラー終了）

## Command
```bash
python3 scripts/generate_weekly_kpi_report.py --input data/kpi/weekly-input.csv --output docs/reports/weekly-kpi-snapshot.md
```
