# Ticket 010 — Operations Division MVP

## Goal
タスク/連絡/データ運用の自動化ベースを作り、Humanの定常負荷を大幅に下げる。

## MVP Positioning (14 agents plan)
フル構成（CALENDAR/TODO/COMM/DATAの各部門）をそのまま持たず、MVPでは **Ops 3ロール** に圧縮する。

- **Ops Lead (FLOW PRIME lite)**
- **Task & Calendar Agent**
- **Comms & Data Ops Agent**

## Role Mapping (Full -> MVP)
- CALENDAR PRIME + SCHEDULER AI + MEETING AI
  - → Task & Calendar Agent に統合
- TODO PRIME + TASK AI + PROJECT AI
  - → Ops Lead / Task & Calendar Agent に分割
- COMM PRIME + EMAIL/PHONE/CHAT AI
  - → Comms & Data Ops Agent に統合
- DATA PRIME + DATABASE/BACKUP/SECURITY AI
  - → Comms & Data Ops Agent（運用） + Tech Division（高度対応）に分担

## Deliverables
- Ops runbook（daily/weekly/monthly）
- 優先順位ルール + 例外対応フロー
- Ops責務境界（Ops vs Tech）

## KPI Link
- 自動化率（Automation Rate）
- 稼働率（Availability）
- 未読/未処理ゼロ率（Backlog Zero Ratio: 補助指標）

## Todo
- [x] Task & Calendarの統合手順を定義（会議調整/リマインド/優先順位）
- [x] Comms分類ルールを定義（即時対応/要承認/保留/スパム）
- [x] Data運用の最低基準を定義（毎日バックアップ、30日世代管理）
- [x] セキュリティ対応の責務分界を定義（Ops一次対応、Tech二次対応）
- [x] Ops例外対応フローを作成（障害・誤送信・未返信滞留）
- [x] Human向け週次サマリー様式を作成（節約時間/自動化率/残課題）
