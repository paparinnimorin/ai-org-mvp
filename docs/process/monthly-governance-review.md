# Monthly Governance Review Flow

## Purpose
月次で承認運用・KPI・リスク対策を再評価し、翌月の運用方針を確定する。

## Scope
- Approval Log運用（月次監査）
- KPIトレンド（月次サマリ）
- RACI/運用ルールの改善提案

## Entry Criteria
- 当月分の `docs/logs/approval-log.md` が更新済み
- 週次KPIレポートが最新化済み
- 主要インシデント・変更点が `docs/logs/decision-log.md` に反映済み

## Workflow
1. **Prep（前日）**
   - managerが監査担当を指名
   - 対象期間（YYYY-MM）を確定
2. **Audit（当日）**
   - `docs/checklists/monthly-approval-audit.md` に沿って証跡確認
   - 異常/未承認/遅延承認を抽出
3. **Review（同日）**
   - KPI差分、リスク、改善案をレビュー
   - 来月の重点アクションを3件以内で決定
4. **Publish（当日〜翌日）**
   - 月次レビュー報告を保存
   - 必要な承認・RACI変更を起票

## Exit Criteria
- 月次レビュー報告が `docs/reports/monthly/` に作成済み
- 監査結果（Pass/Attention/Fail）と改善アクションが明記済み
- 次月オーナーと期限が設定済み

## Cadence
- 毎月最終営業日（または翌営業日）
- 所要 30〜45分
