# RACI & Authority Matrix (MVP)

## 1. Roles
- **HUMAN CEO**
- **PRIME AI**
- **Division Lead** (Content/BizDev/Tech/Ops)
- **Execution Agent**

## 2. RACI (Core Processes)

| Process | HUMAN CEO | PRIME AI | Division Lead | Execution Agent |
| --- | --- | --- | --- | --- |
| KPI設定/改定 | A | R | C | I |
| 週次運用レビュー | A | R | C | I |
| 日次タスク配分 | I | A | R | C |
| コンテンツ制作/配信 | I | C | A | R |
| リード獲得/営業実行 | I | C | A | R |
| 開発/デプロイ | I | C | A | R |
| 問い合わせ一次対応 | I | C | A | R |
| 支出承認（>=1万円） | A | C | R(起案) | I |
| 外部公開・契約変更 | A | C | R(起案) | I |
| インシデント対応 | A | R | C | R |

A=Accountable, R=Responsible, C=Consulted, I=Informed

## 3. Authority Rules
- **Execution Agent**: 定常業務のみ実行可（低リスク）
- **Division Lead**: 業務優先順位変更・工数再配分可
- **PRIME AI**: 事業部横断の調整・停止判断可
- **HUMAN CEO**: 重要事項の最終決裁

## 4. Approval Policy
### Human approval mandatory
1. 1万円以上の支出
2. 外部公開（公式声明、広告出稿、対外投稿の方針変更）
3. 契約・課金・価格改定
4. 法務/規約/個人情報への影響

## 5. Stop Conditions (Safety)
- 同一フロー3連続失敗
- 主要KPIが週次で閾値を下回る
- 外部クレーム重大化
