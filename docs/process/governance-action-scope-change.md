# Governance Action Scope Change Flow

## Purpose
既存Governance Actionの目的は維持しつつ、実行範囲（deliverables / timeline / owner allocation）を変更する際の標準フローを定義する。

## Trigger Conditions
- 既存Actionをclose/reopen/escalateでは解決できない
- 依存関係の変化により、成果物や期限の再設計が必要
- KPIの優先順位変更に伴い、Actionの対象範囲を縮小・拡張する

## Inputs
- 最新のMinutes（`docs/reports/minutes/*.md`）
- 最新のAction Register（`docs/reports/minutes/actions/*.md`）
- 必要に応じてReopen/Escalationレポート

## Scope Change Flow (30-min governance window)
1. 変更理由の確認（Why now）
2. 影響範囲の特定（owner / due / deliverables / KPI）
3. 変更案の合意（Option A/B + 推奨案）
4. Action Registerの更新方針を決定
5. 変更後の受け入れ条件（Definition of Done）を明文化
6. 次回review dateを設定し、minutesに記録

## Output Artifacts
- Scope Change Report（`docs/reports/minutes/scope-changes/*.md`）
- 更新済みAction Registerへの参照
- 実行チェック結果（bundle check）

## Guardrails
- scope changeは「責任の曖昧化」に使わない（ownerは必ず明記）
- due変更は根拠（依存関係・工数・承認待ち）を記録
- KPI影響の定量メモを最低1行残す

## Completion Criteria
- [ ] scope change理由が1行で説明できる
- [ ] impact matrix（owner / due / KPI / deliverables）が埋まっている
- [ ] 次回review dateが設定済み
- [ ] ticket status と docs index が更新済み
