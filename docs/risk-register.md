# Risk Register

| ID | Risk | Impact(1-5) | Probability(1-5) | Mitigation | Owner | Status |
|---|---|---:|---:|---|---|---|
| R-001 | KPI入力漏れ | 3 | 3 | 入力チェック自動化 | Ops Lead | Open |
| R-002 | 承認ログ未記録 | 4 | 2 | 月次監査チェック | PRIME AI | Open |
| R-003 | 連続投稿失敗 | 4 | 3 | 3回失敗で停止 | Content Lead | Open |
| R-004 | 営業返信遅延 | 3 | 4 | SLAアラート | BizDev Lead | Open |
| R-005 | デプロイ障害 | 5 | 2 | ロールバック手順 | Tech Lead | Open |
| R-006 | セキュリティ異常検知遅延 | 5 | 2 | 監視強化 | Tech Lead | Open |
| R-007 | Dry runで責務衝突 | 3 | 3 | RACI差分レビュー | PRIME AI | Open |
| R-008 | 自動化率停滞 | 3 | 3 | ボトルネック分析 | Ops Lead | Open |
| R-009 | 学習完了率低下 | 4 | 3 | 伴走強化 | BizDev Lead | Open |
| R-010 | 重大判断の承認遅延 | 4 | 2 | 週次ガバナンス短縮版 | Human CEO | Open |

## Scoring Guide
- Impact: 1(low) - 5(critical)
- Probability: 1(rare) - 5(frequent)

## Update Rule
- 月次レビューで更新
- 新規高リスクは週次会議で先行対処
