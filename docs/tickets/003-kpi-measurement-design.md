# Ticket 003 — KPI Measurement Design

## Goal
90日KPI 5項目の計測仕様を統一し、週次で意思決定できる状態を作る。

## Scope (Fixed 5 KPIs)
- 営業利益率 (Operating Margin)
- 稼働率 (Availability)
- 自動化率 (Automation Rate)
- コンテンツ公開本数 (Content Throughput)
- 学習完了率 (Learning Completion)

## Deliverables
- KPI定義書（計算式/集計周期/責任者/アラート閾値）
- 週次レビュー表（PRIME AI提出）

## KPI Definitions (Draft)
1. **営業利益率** = 営業利益 / 売上高
   - 集計: 月次（速報は週次）
   - Owner: BizDev Lead
2. **稼働率** = (総稼働時間 - 障害時間) / 総稼働時間
   - 集計: 日次・週次
   - Owner: Tech Lead
3. **自動化率** = 自動処理件数 / 全処理件数
   - 集計: 週次
   - Owner: Ops Lead
4. **コンテンツ公開本数** = 週の公開完了本数
   - 集計: 週次
   - Owner: Content Lead
5. **学習完了率** = 完了者数 / 受講開始者数
   - 集計: 週次・月次
   - Owner: BizDev Lead (Academy)

## Ops-derived Supporting Metrics (Reference)
- 未読/未処理ゼロ率（Inbox & Task Backlog Zero）
- 自動返信率（Email/Chat）
- データ精度（エラー率）

## Todo
- [x] KPIごとのデータ取得元（ツール/DB）を確定
- [x] KPIの警戒閾値（yellow/red）を設定
- [x] 週次レビュー用テンプレートを作成
- [x] KPI値の監査可能ログ保管先を確定
- [x] Ops補助指標をKPI本体と切り分けて定義
