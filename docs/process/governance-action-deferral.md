# Governance Action Deferral Flow

## Purpose
未完了Actionを無理にclose/reopenせず、期限後ろ倒しと再評価条件を明確化して運用するためのdeferral標準フローを定義する。

## Trigger Conditions
- 依存タスク未完了により、現在サイクル内でDone条件を満たせない
- リソース再配分で優先度が一時的に低下した
- Scope change実施後も、受け入れ条件到達まで追加時間が必要

## Inputs
- 最新のMinutes（`docs/reports/minutes/*.md`）
- 最新のAction Register（`docs/reports/minutes/actions/*.md`）
- 必要に応じてEscalation / Scope Changeレポート

## Deferral Flow (30-min governance window)
1. Deferral理由を分類（dependency / capacity / risk）
2. 延期期間（old due -> new due）と影響範囲（KPI/owner）を明記
3. Deferral中の最小進捗義務（checkpoint deliverable）を設定
4. 再開条件（resume trigger）を定義
5. 次回review dateを設定しminutes/action registerに記録

## Output Artifacts
- Deferral Report（`docs/reports/minutes/deferrals/*.md`）
- 更新済みAction Registerへの参照
- 実行チェック結果（bundle check）

## Guardrails
- deferralは無期限延期を禁止（必ずnew dueを設定）
- owner責任は維持し、"保留中"でも進捗確認責任を残す
- KPI影響（遅延コスト）を最低1行で定量/定性記録する

## Completion Criteria
- [ ] deferral理由が1行で説明できる
- [ ] old due/new due/checkpoint/resume triggerが埋まっている
- [ ] 次回review dateが設定済み
- [ ] ticket status と docs index が更新済み
