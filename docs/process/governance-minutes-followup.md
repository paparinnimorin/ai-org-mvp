# Governance Minutes Follow-up

## Purpose
ガバナンス会議のminutesで確定したアクションを、期限内に実行・可視化・エスカレーションする。

## Entry Criteria
- 会議minutesが `docs/reports/minutes/` に作成済み
- 会議IDと対象期間（week/month/quarter）が明確
- Manager ownerが当番として割り当て済み

## Exit Criteria
- Action registerが作成され、全アクションにowner/due/statusが設定済み
- Blocked項目のエスカレーション先が記録済み
- 重要アクションが次回kickoff/midcheck/closeoutのいずれかに接続済み

## SLA
- T+4h: action register 初版作成
- T+24h: owner承認完了
- T+48h: Blocked項目のエスカレーション完了

## Standard Flow
1. **Capture (T+0h〜4h)**
   - minutesのDecision/Action候補を抽出
   - `scripts/new_governance_action_register.py` で初版を生成
2. **Assign (T+4h〜24h)**
   - 各ActionにOwnerとDueを設定
   - Priorityと依存関係を明記
3. **Review (T+24h〜48h)**
   - Managerが遅延・未割当・曖昧スコープをレビュー
   - BlockedはEscalation先と期限を指定
4. **Integrate (T+48h〜72h)**
   - 次サイクルのtask card/briefへ反映
   - 必要なら `docs/logs/decision-log.md` を更新

## Escalation Rules
- Due超過見込み > 48h: Managerへ即時エスカレーション
- Cross-team依存でowner不在: governance lead仮アサイン
- High-risk action未着手: weekly risk reviewで最優先議題化

## KPI Proxy
- Action register発行リードタイム（hours）
- T+24h時点 owner確定率（%）
- Due内完了率（%）
- Blocked項目の平均解消時間（hours）

## References
- `docs/templates/governance-action-register.md`
- `docs/reports/minutes/governance-2026-02-20.md`
- `docs/ticket-status.md`
