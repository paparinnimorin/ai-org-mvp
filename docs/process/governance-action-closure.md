# Governance Action Closure Flow

## Purpose
ガバナンス会議で起票されたアクションを、期限内にクローズし、次サイクルへ確実に反映するための標準フロー。

## Scope
- 対象: `docs/reports/minutes/actions/*.md` に登録された action
- 起点: governance minutes確定後（action register作成済み）
- 終点: closure report作成 + ticket/status反映 + 必要エスカレーション完了

## Roles
- **Manager**: 全体進行、期限管理、最終承認
- **Action Owner**: 実行・証跡提出・自己評価
- **Reviewer**: 完了条件確認、差戻し判断

## Entry Criteria
- governance minutes が存在
- action register が作成済み
- 各 action に owner / due / status が設定済み

## Exit Criteria
- closure report が作成済み
- Open/Blocked action に再計画（owner/due/escalation）が設定済み
- 次サイクルに持ち越す action がmanager brief/checklistへ転記済み

## SLA
- T+24h: owner確認と初回更新
- T+48h: Blocked項目の要因分析とエスカレーション
- T+72h: closure report作成

## Procedure
1. **Intake**: action registerの最新状態を確認
2. **Verification**: 完了主張 action の証跡（リンク/ログ/成果物）を確認
3. **Disposition**: `Closed / Carry Over / Blocked` に分類
4. **Escalation**: Blocked項目は責任者・期限付きで再設定
5. **Reporting**: closure reportを作成し、referencesを更新
6. **Handoff**: 次サイクル資料へ引継ぎ項目を転記

## Data Fields (Minimum)
- action id
- owner
- due date
- status
- evidence link
- carry-over decision
- escalation owner/due (if blocked)

## References
- `docs/templates/governance-action-register.md`
- `docs/checklists/governance-action-closure-checklist.md`
- `docs/reports/minutes/actions/`
- `docs/reports/minutes/closures/`
