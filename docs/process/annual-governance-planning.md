# Annual Governance Planning Flow

## Purpose
年次単位で戦略・リスク・運用体制を再設計し、次年度の実行方針を確定する。

## Entry Criteria
- 当年の四半期レビューが完了している
- `docs/reports/annual/` に年次成果物の保管先がある
- KPI年次サマリ（throughput/quality/SLA）が更新済み

## Steps
1. **Year Retrospective (45m)**
   - 年間KPIの達成状況と主要イベントを確認
   - 継続課題と再発課題を分類
2. **Strategy Reset (45m)**
   - 次年度の重点テーマをDivision別に定義
   - Keep/Change/Stop を確定
3. **Risk Posture Review (45m)**
   - 主要リスクの年次再評価と許容水準を更新
   - 緩和・監視・エスカレーションの責任分担を再設定
4. **Operating Model Plan (45m)**
   - 次年度のサイクル設計（4-ticket単位）を更新
   - オーナー/期限/承認ポイントを割り当て

## Exit Criteria
- 年次戦略チャーターが作成済み
- 年次リスクポスチャーレポートが作成済み
- bundle checkがPASSし、`docs/ticket-status.md` が最新

## Outputs
- `docs/reports/annual/*annual-strategy-charter-<year>.md`
- `docs/reports/annual/*annual-risk-posture-<year>.md`
- `scripts/check_annual_governance_bundle.py` の実行ログ
