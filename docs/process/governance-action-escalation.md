# Governance Action Escalation Flow

## Purpose
Reopen後も解消しない会議アクションを正式にescalationし、意思決定と再配分を最短で実行する標準フロー。

## Trigger
- Reopened action が再dueを超過した
- Blocked要因が2営業日以上解消されない
- 依存チーム判断待ちでmanager権限を超える

## Escalation Rules
1. Source minutes / action id / reopen report を必ず紐付ける
2. Escalation level を L1(Manager) / L2(Governance Lead) / L3(Executive) で明記する
3. 意思決定期限（decision due）を48時間以内で設定する
4. owner再配分またはscope変更のどちらかを必ず確定する

## Operating Steps
1. manager が escalation要否を判定し level を選定
2. escalation report を作成し、blocking factor を1行で要約
3. action register に `Escalated` を記録し decision due を追記
4. governance meeting agenda に escalation item を追加
5. 決定結果を closure または reopen flow に連結する

## Exit Criteria
- escalation level / decision due / accountable owner が記録済み
- action register と escalation report が相互参照
- 次アクション（close/reopen/scope change）が明文化されている
