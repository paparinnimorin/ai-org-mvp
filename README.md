# ai-org-mvp

AI組織MVP（日本語メイン + English keywords）

## Scope
- 4事業部（Content / BizDev / Tech / Ops）
- 初期体制: 12〜16 agents
- Deliverables:
  - `docs/ai-org-mvp.md`
  - `docs/raci-authority-matrix.md`

## Guardrails
- 1万円以上の支出・契約・公開系変更は Human approval 必須
- 外部公開・課金変更・法務影響は金額に関わらず承認必須

## KPI (First 90 days)
1. 営業利益率 (Operating Margin)
2. 稼働率 (Availability)
3. 自動化率 (Automation Rate)
4. コンテンツ公開本数 (Content Throughput)
5. 学習完了率 (Learning Completion)

## Utilities
- `python3 scripts/check_tickets.py`
  - `docs/tickets/*.md` のTodo完了状況を検査（未完了があれば終了コード1）

## Commands
```bash
make kpi-report
make ticket-check
```
