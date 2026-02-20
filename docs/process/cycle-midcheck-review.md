# Cycle Midcheck Review Flow

cycle中盤（day2-3想定）で進捗/リスク/依存を再同期するための標準フロー。

## Entry Criteria
- kickoff briefが作成済み
- cycle対象ticketがtask boardに反映済み
- 最低1回の実行ログ（PR/タスク更新）が存在する

## 1) Progress Snapshot
1. ticketごとに `Done / In Progress / Blocked` を記録
2. KPI proxy（完了件数、遅延件数、blocked件数）を収集
3. carry-over見込み項目を抽出

## 2) Risk & Dependency Review
1. Blocked項目の原因を `依存待ち / 要件不明 / 工数不足` に分類
2. manager承認が必要な項目を抽出
3. 24h以内に解消するアクションをowner付きで確定

## 3) Replan Decision
- scope維持 / 優先度変更 / 切り戻しのいずれかを選択
- 変更がある場合は `docs/logs/decision-log.md` に記録

## 4) Midcheck Report Publish
- `scripts/new_cycle_midcheck_report.py` でmidcheck reportを生成
- `docs/reports/midchecks/` に保存
- 関連リンクをticketとtask boardに追記

## Exit Criteria
- midcheck reportが作成済み
- blocked ticketのowner/action/dueが明確
- 次の48h実行計画が定義済み
