.PHONY: kpi-report ticket-check

kpi-report:
	python3 scripts/generate_weekly_kpi_report.py --input data/kpi/weekly-input.csv --output docs/reports/weekly-kpi-snapshot.md

ticket-check:
	python3 scripts/check_tickets.py
