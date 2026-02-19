# Approval Gate Workflow

## 1. Approval-required Actions

### Always require Human approval
- 外部公開方針の変更（声明、広告、重要投稿）
- 契約・課金・価格改定
- 法務/規約/個人情報に影響する変更

### Conditional (threshold-based)
- 1万円以上の支出

## 2. Workflow (Draft -> Approve -> Execute)
1. **Draft（起案）**
   - Division Lead が起案書を作成
2. **Review（一次確認）**
   - PRIME AI がリスク・整合性チェック
3. **Approve（最終承認）**
   - Human CEO が承認/差し戻し
4. **Execute（実行）**
   - Execution Agent が実行
5. **Log（監査記録）**
   - `docs/logs/approval-log.md` に記録

## 3. Resubmission Rule
- 差し戻し時は以下を必須修正:
  - リスク評価
  - 代替案
  - KPI影響
- 再提出は原則24時間以内

## 4. Approval Request Template
- Request ID:
- Requester:
- Action Type:
- Amount (JPY):
- Why now:
- Risk:
- KPI impact:
- Deadline:

## 5. Approval Log Template
- Date:
- Request ID:
- Decision: Approved / Rejected / Rework
- Approver:
- Notes:
