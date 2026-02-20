# Weekly Risk Review Process

## Purpose
`risk-register.md` を週次でメンテし、運用リスクの早期検知・対応を行う。

## Cadence
- Every Friday after KPI close
- 30 minutes max

## Inputs
- `docs/risk-register.md`
- `docs/logs/approval-log.md`
- `docs/logs/decision-log.md`
- `docs/reports/weekly-kpi-snapshot.md`

## Procedure
1. **Collect**: 今週の事象（incident/near-miss/delay）を抽出
2. **Re-score**: Likelihood / Impact を再評価
3. **Prioritize**: Top3 risks を確定
4. **Mitigate**: owner / due / next step を更新
5. **Log**: `templates/risk-review-note.md` で記録

## Scoring Rule
- Likelihood: 1 (Rare) 〜 5 (Almost certain)
- Impact: 1 (Minor) 〜 5 (Critical)
- Priority = Likelihood x Impact
- 15以上は governance meeting で必ず確認

## Exit Criteria
- Top3 risks が更新済み
- 各Top riskに owner / due が設定済み
- 次週フォロー項目が最低1件記録済み
