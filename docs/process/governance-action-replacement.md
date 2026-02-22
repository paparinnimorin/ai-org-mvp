# Governance Action Replacement

## Purpose
cancelled/obsoleteになったactionを放置せず、代替actionへ置換して成果責任と監査トレースを維持する。

## Trigger
- cancellation後に成果責任が未充足のまま残るとき
- verificationで「目標は有効だが手段のみ無効」と判定されたとき

## Inputs
- `docs/reports/minutes/<minutes>.md`
- `docs/reports/minutes/actions/*.md`
- `docs/reports/minutes/cancellations/*.md`
- `docs/reports/minutes/verifications/*.md`
- `docs/ticket-status.md`

## Replacement Steps (30 min)
1. **欠損責務の特定**: cancel済みactionで失われる成果/KPI責務を特定
2. **代替案設計**: replacement action候補（owner/due/dependency）を設計
3. **承認判定**: managerが置換妥当性（実行可能性・影響）を承認
4. **register更新**: 旧actionを`replaced`として紐づけ、新action IDを登録
5. **共有**: minutesとfollow-up reportに旧→新マッピングを明記

## Output
- replacement report (`docs/reports/minutes/replacements/*.md`)
- action register更新（旧action= `replaced`、新action参照）

## Exit Criteria
- 旧actionと新actionのマッピングが明示されている
- 新actionにowner/due/statusが設定されている
- replacement reportが保存され、次回minutesで追跡可能
