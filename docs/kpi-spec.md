# KPI Spec (90 Days)

## Thresholds
- Operating Margin: yellow < plan-10%, red < plan-20%
- Availability: yellow < 99.5%, red < 99.0%
- Automation Rate: yellow < 70%, red < 60%
- Content Throughput: yellow < 週目標-1本, red < 週目標-2本
- Learning Completion: yellow < 80%, red < 70%

## Data Sources
- Margin: 会計データ（週速報/月確定）
- Availability: 監視ログ
- Automation: 実行ジョブログ
- Throughput: 配信管理表
- Learning Completion: スクール進捗管理表

## Audit Log Policy
- KPI原票は週次スナップショット保存
- 改ざん防止のため履歴追記（append-only）
