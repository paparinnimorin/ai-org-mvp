# Ticket 086 — Governance Action Scope Change Bundle Check CLI

## Goal
Scope change時の成果物欠落を防ぐため、bundle検証CLIを追加する。

## Deliverables
- `scripts/check_governance_action_scope_change_bundle.py`
- `docs/automation/README.md` 更新

## Todo
- [x] `scripts/check_governance_action_scope_change_bundle.py` を実装
- [x] 新CLIを1回以上実行し、minutes/action register/escalation/scope-change/process/checklist/statusの存在確認を実施
- [x] `docs/automation/README.md` に実行例を追記
- [x] `docs/README.md` Scriptsセクションに `scripts/check_governance_action_scope_change_bundle.py` を追加
