# Ticket 011 — Safety & Stop Conditions

## Goal
暴走・品質低下時に自動停止/人間介入できる仕組みを明文化する。

## Deliverables
- Stop条件一覧
- Incident response手順
- 復旧判定チェックリスト

## Stop Conditions (MVP)
1. **同一フロー3連続失敗**
   - 例: 自動返信失敗、投稿失敗、同期失敗
2. **重要KPIの急落**
   - 週次で事前定義したred閾値を下回る
3. **外部影響を伴う重大ミス**
   - 誤送信、誤公開、誤請求、誤契約更新
4. **セキュリティ異常**
   - 不正アクセス兆候、資格情報漏えい疑い、改ざん検知

## Incident Severity
- **SEV1**: 外部影響大（法務/課金/顧客被害）→ 即時停止 + Human CEO連絡
- **SEV2**: サービス劣化（KPI急落/広範囲遅延）→ 部分停止 + PRIME AI判断
- **SEV3**: 局所障害（単機能の連続失敗）→ 自動リトライ後に担当Lead介入

## Response Flow
1. 検知（Execution Agent / Monitoring）
2. 一時停止（対象フローのみ）
3. エスカレーション（Ops Lead -> PRIME AI -> Human CEO）
4. 影響範囲特定
5. 復旧実行（ロールバック/再実行/手動運用切替）
6. 事後レビュー（RCA + 再発防止）

## Todo
- [x] 連続失敗3回の対象フロー一覧を定義
- [x] KPI red閾値をKPI定義書と同期
- [x] SEV判定基準を運用手順へ反映
- [x] Human連絡チャネル/一次連絡文面テンプレを定義
- [x] 復旧条件（Go/No-Go）チェックリストを作成
