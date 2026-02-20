# Automation Notes

## KPI report generation
```bash
make kpi-report
```

## Ticket completion check
```bash
make ticket-check
```

## Task card generation (strict task-agent)
```bash
python3 scripts/new_task_card.py --id T-034A --title "link guard rollout" --owner ops --due 2026-02-21
```

## README link guard
```bash
make link-check
# or
python3 scripts/check_readme_links.py
```

## Manager brief generation
```bash
python3 scripts/new_manager_brief.py --id MB-20260221-01 --title "week2 dispatch" --ticket 035-038 --owner manager --due 2026-02-22
```

## Manager board link check
```bash
make manager-board-check
# or
python3 scripts/check_manager_board.py
```

If KPI generation fails, check:
1. CSV header matches spec
2. ratio fields are 0..1
3. `week` is `YYYY-Www`

## Manager handoff note generation
```bash
python3 scripts/new_manager_handoff_note.py --id HN-20260221-01 --from-owner manager-a --to-owner manager-b --date 2026-02-21 --focus "cycle 039-042 close"
```

## Cycle closeout report generation
```bash
python3 scripts/new_cycle_closeout_report.py --id CC-20260221-01 --cycle 043-046 --owner manager --date 2026-02-21
```

## Closeout bundle check
```bash
python3 scripts/check_closeout_bundle.py --cycle 043-046
```

## Cycle kickoff brief generation
```bash
python3 scripts/new_cycle_kickoff_brief.py --id KB-20260221-01 --cycle 047-050 --owner manager --date 2026-02-21
```

## Kickoff bundle check
```bash
python3 scripts/check_kickoff_bundle.py --cycle 047-050
```
