# Governance Action Verification

## Purpose
governance minutes由来のアクションについて、実行完了後に「証跡の妥当性」を検証し、再オープンや監査差戻しを未然に防ぐ。

## Trigger
- closure/escalation/scope-change/deferral のいずれかを実施した週次ガバナンスサイクル
- Managerが「完了扱い」へ遷移させる直前

## Inputs
- `docs/reports/minutes/<minutes>.md`
- `docs/reports/minutes/actions/*.md`
- 関連 outcome レポート（closures / reopens / escalations / scope-changes / deferrals）
- `docs/ticket-status.md`

## Verification Steps (30 min)
1. **Scope確認**: 当該minutesに紐づくaction id一覧を確定
2. **Evidence確認**: 対象actionごとに成果物リンク・担当者・日付を確認
3. **Consistency確認**: action registerとoutcome reportの状態遷移が一致するか確認
4. **Risk確認**: KPI/リスクへの影響と次回レビュー日を確認
5. **Decision記録**: verification reportを作成し、Pass/Needs-Fixで判定

## Output
- verification report (`docs/reports/minutes/verifications/*.md`)
- 必要に応じた修正依頼（manager board / action register更新）

## Exit Criteria
- 全actionが evidence + owner + due/next-review を満たす
- register と outcome の矛盾がない
- verification reportが保存され、次回minutesへ参照リンクを残した
