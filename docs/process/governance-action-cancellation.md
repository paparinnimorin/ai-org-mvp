# Governance Action Cancellation

## Purpose
誤登録・重複・前提崩壊などで継続不能となったactionを正式にcancelし、監査時に「未実施放置」と誤認されない状態を作る。

## Trigger
- action registerで duplicate / invalid / obsolete が判定されたとき
- owner不在や外部制約により、再計画よりcancelのほうが妥当とmanagerが判断したとき

## Inputs
- `docs/reports/minutes/<minutes>.md`
- `docs/reports/minutes/actions/*.md`
- `docs/reports/minutes/verifications/*.md`（存在する場合）
- `docs/ticket-status.md`

## Cancellation Steps (30 min)
1. **対象確定**: cancel候補action ID・理由・影響範囲を確定
2. **妥当性確認**: reopen/scope-change/deferralで代替できないかを確認
3. **承認記録**: manager承認と監査メモを記録
4. **状態反映**: action registerにcancelled理由・日付・再開条件を反映
5. **通知/共有**: 次回minutesにcancel decisionと影響を記載

## Output
- cancellation report (`docs/reports/minutes/cancellations/*.md`)
- action register更新（cancelled理由・再開条件）

## Exit Criteria
- cancel対象と理由が明文化されている
- register状態が `cancelled` で整合している
- cancellation reportが保存され、次回minutesから参照可能
