# Manager Handoff Protocol

## Purpose
manager稼働の切替時に、進行中タスク・リスク・次アクションを確実に引き継ぐ。

## Trigger
- 日次の業務終了時
- 12時間以上の離席前
- 重大インシデント対応の担当交代時

## Inputs
- 最新 `docs/process/manager-task-board.md`
- 直近の manager brief
- 当日生成した task report / decision log

## Required Handoff Sections
1. Current State: 進行中チケットと状態
2. Risks/Blockers: 未解決リスクと依存
3. Next 24h Actions: 次担当が最初に実行する3-5項目
4. Escalation Flags: 即時エスカレーション条件

## Completion Criteria
- handoff noteが `docs/reports/handoffs/` に保存済み
- manager board上の最優先タスクが最新状態
- blockerが存在する場合、ownerと期限が明記されている

## Cadence
- 定常運用: 1日1回（業務終了時）
- 高負荷週: 朝夕2回
