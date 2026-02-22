# Ticket 097 — Governance Action Cancellation CLI

## Goal
cancellation report作成をCLIで定型化し、minutes単位のcancel監査証跡を再現可能にする。

## Deliverables
- `scripts/new_governance_action_cancellation.py`
- `docs/reports/minutes/cancellations/gax-20260222-01-governance-2026-02-20.md`
- `docs/automation/README.md` 更新

## Todo
- [x] `scripts/new_governance_action_cancellation.py` を実装
- [x] 新CLIを1回以上実行し、cancellation reportを生成
- [x] `docs/automation/README.md` に実行例を追記
- [x] `docs/README.md` Scripts/Reportsセクションにリンク追加
