# Governance Action Reopen Flow

## Purpose
会議アクションを一度Closed判定した後に再オープンが必要になった場合の運用を標準化し、責任所在と再発防止記録を一貫化する。

## Trigger
- 既存actionのエビデンス不備が監査で判明した
- Carry-over/Blocked の解消報告が虚偽または不完全だった
- 外部依存の変更で再対応が必要になった

## Reopen Rules
1. Source minutes と action id を必ず特定する
2. Reopen reason を3分類（Evidence Gap / Scope Change / Regression）で記録する
3. 新しい due と owner を同一報告内で確定する
4. closure report に相互リンクを残す

## Operating Steps
1. manager が reopen 判定を実施し、対象actionを特定
2. `governance-action-reopen` report を作成
3. action register の current status を `Reopened` に更新
4. 次回 kickoff brief へ carry-over 連携
5. 週次risk reviewで再オープン件数を追跡

## Exit Criteria
- Reopen reason / new due / owner が記録済み
- closure report と reopen report が双方向リンク
- 次サイクルhandoff先が記載済み
