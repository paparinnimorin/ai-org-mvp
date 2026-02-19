# Org Layer Definitions (L0-L4)

## L0 — Human CEO
- 責務: 最終意思決定と重大リスク承認
- 非責務: 日次オペレーションの直接実行
- Escalation Trigger: 法務/契約/外部公開/1万円以上支出

## L1 — PRIME AI
- 責務: 全体オーケストレーション、KPI監視、部門間調整
- 非責務: 最終法務判断
- Escalation Trigger: SEV1・KPI red・連続失敗

## L2 — Division Leads
- 責務: 部門目標達成、優先順位管理、実行品質担保
- 非責務: 企業横断の最終優先順位変更
- Escalation Trigger: 部門で閉じない依存/予算/人員不足

## L3 — Managers
- 責務: 実行計画作成、進捗管理、一次レビュー
- 非責務: 承認ゲート越え判断
- Escalation Trigger: SLA違反、品質劣化、ブロッカー継続

## L4 — Execution Agents
- 責務: 定常タスク実行、ログ記録、異常検知
- 非責務: 重大変更・対外方針決定
- Escalation Trigger: 同一フロー3連続失敗、入力不備、権限不足
