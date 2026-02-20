.PHONY: kpi-report ticket-check link-check manager-board-check

kpi-report:
	python3 scripts/generate_weekly_kpi_report.py --input data/kpi/weekly-input.csv --output docs/reports/weekly-kpi-snapshot.md

ticket-check:
	python3 scripts/check_tickets.py

link-check:
	python3 scripts/check_readme_links.py

manager-board-check:
	python3 scripts/check_manager_board.py
