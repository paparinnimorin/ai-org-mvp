# Automation Notes

## KPI report generation
```bash
make kpi-report
```

## Ticket completion check
```bash
make ticket-check
```

If KPI generation fails, check:
1. CSV header matches spec
2. ratio fields are 0..1
3. `week` is `YYYY-Www`
