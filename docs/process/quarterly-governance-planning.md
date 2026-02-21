# Quarterly Governance Planning Flow

## Purpose
四半期単位で戦略・リスク・実行能力を再調整し、次四半期の運用計画を確定する。

## Entry Criteria
- 当四半期の月次レビューが完了している
- `docs/reports/quarterly/` に四半期成果物の保管先がある
- 主要KPI（throughput/quality/SLA）のトレンドが更新済み

## Steps
1. **Trend Review (30m)**
   - KPIトレンドと主要インシデントを確認
   - ボトルネック候補を3件以内に絞る
2. **Strategy Alignment (30m)**
   - Division別の次四半期優先テーマを定義
   - Stop/Keep/Start を明文化
3. **Risk Rebalance (30m)**
   - Top risksの確率×影響を再評価
   - 監視強化対象と緩和施策を更新
4. **Execution Plan (30m)**
   - 次サイクル（4-ticket単位）の着手順を決定
   - オーナーと期限を割り当て

## Exit Criteria
- 四半期戦略ブリーフが作成済み
- 四半期リスク再配分レポートが作成済み
- bundle checkがPASSし、`docs/ticket-status.md` が最新

## Outputs
- `docs/reports/quarterly/*quarterly-strategy-brief-<quarter>.md`
- `docs/reports/quarterly/*quarterly-risk-rebalance-<quarter>.md`
- `scripts/check_quarterly_governance_bundle.py` の実行ログ
