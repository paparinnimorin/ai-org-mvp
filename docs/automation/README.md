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

## Cycle midcheck report generation
```bash
python3 scripts/new_cycle_midcheck_report.py --id MC-20260221-01 --cycle 051-054 --owner manager --date 2026-02-21
```

## Midcheck bundle check
```bash
python3 scripts/check_midcheck_bundle.py --cycle 051-054
```

## Monthly approval audit generation
```bash
python3 scripts/new_monthly_approval_audit.py --id MA-202602-01 --month 2026-02 --owner manager --date 2026-02-21
```

## Monthly governance review generation
```bash
python3 scripts/new_monthly_governance_review.py --id MR-202602-01 --month 2026-02 --owner manager --date 2026-02-21
```

## Monthly governance bundle check
```bash
python3 scripts/check_monthly_governance_bundle.py --month 2026-02
```

## Quarterly strategy brief generation
```bash
python3 scripts/new_quarterly_strategy_brief.py --id QSB-2026Q1-01 --quarter 2026-Q1 --owner manager --date 2026-02-21
```

## Quarterly risk rebalance generation
```bash
python3 scripts/new_quarterly_risk_rebalance.py --id QRR-2026Q1-01 --quarter 2026-Q1 --owner manager --date 2026-02-21
```

## Quarterly governance bundle check
```bash
python3 scripts/check_quarterly_governance_bundle.py --quarter 2026-Q1
```

## Annual strategy charter generation
```bash
python3 scripts/new_annual_strategy_charter.py --id ASC-2026-01 --year 2026 --owner manager --date 2026-02-21
```

## Annual risk posture generation
```bash
python3 scripts/new_annual_risk_posture.py --id ARP-2026-01 --year 2026 --owner manager --date 2026-02-21
```

## Annual governance bundle check
```bash
python3 scripts/check_annual_governance_bundle.py --year 2026
```

## Governance action register generation
```bash
python3 scripts/new_governance_action_register.py --id GAR-20260221-01 --minutes governance-2026-02-20.md --owner manager --date 2026-02-21
```

## Governance action bundle check
```bash
python3 scripts/check_governance_action_bundle.py --minutes governance-2026-02-20.md
```

## Governance action closure generation
```bash
python3 scripts/new_governance_action_closure.py --id GAC-20260221-01 --minutes governance-2026-02-20.md --owner manager --date 2026-02-21
```

## Governance action closure bundle check
```bash
python3 scripts/check_governance_action_closure_bundle.py --minutes governance-2026-02-20.md
```

## Governance action reopen generation
```bash
python3 scripts/new_governance_action_reopen.py --id GARO-20260221-01 --minutes governance-2026-02-20.md --owner manager --date 2026-02-21
```

## Governance action reopen bundle check
```bash
python3 scripts/check_governance_action_reopen_bundle.py --minutes governance-2026-02-20.md
```

## Governance action escalation generation
```bash
python3 scripts/new_governance_action_escalation.py --id GAE-20260221-01 --minutes governance-2026-02-20.md --owner manager --date 2026-02-21
```

## Governance action escalation bundle check
```bash
python3 scripts/check_governance_action_escalation_bundle.py --minutes governance-2026-02-20.md
```

## Governance action scope change generation
```bash
python3 scripts/new_governance_action_scope_change.py --id GASC-20260221-01 --minutes governance-2026-02-20.md --owner manager --date 2026-02-21
```

## Governance action scope change bundle check
```bash
python3 scripts/check_governance_action_scope_change_bundle.py --minutes governance-2026-02-20.md
```

## Governance action deferral generation
```bash
python3 scripts/new_governance_action_deferral.py --id GAD-20260222-01 --minutes governance-2026-02-20.md --owner manager --date 2026-02-22
```

## Governance action deferral bundle check
```bash
python3 scripts/check_governance_action_deferral_bundle.py --minutes governance-2026-02-20.md
```


## Governance action verification generation
```bash
python3 scripts/new_governance_action_verification.py --id GAV-20260222-01 --minutes governance-2026-02-20.md --owner manager --date 2026-02-22
```

## Governance action verification bundle check
```bash
python3 scripts/check_governance_action_verification_bundle.py --minutes governance-2026-02-20.md
```

## Governance action cancellation generation
```bash
python3 scripts/new_governance_action_cancellation.py --id GAX-20260222-01 --minutes governance-2026-02-20.md --owner manager --date 2026-02-22
```

## Governance action cancellation bundle check
```bash
python3 scripts/check_governance_action_cancellation_bundle.py --minutes governance-2026-02-20.md
```
