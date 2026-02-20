# Cycle Closeout Handoff Flow

## Purpose
cycle完了時に、manager間handoffへ渡す情報を最小セットで固定化し、次サイクル開始遅延を防ぐ。

## Inputs
- 完了ticket範囲（例: 043-046）
- handoff note (`docs/reports/handoffs/*.md`)
- cycle closeout report (`docs/reports/closeouts/*.md`)
- 更新済み `docs/ticket-status.md`

## Flow (15-20 min)
1. **Closeout report作成**
   - `scripts/new_cycle_closeout_report.py` で下書きを生成
   - 実施内容 / 未解決課題 / 次サイクル提案を埋める
2. **Handoff note更新**
   - 現在のowner→次ownerのcontext差分を追記
3. **Bundle check実行**
   - `scripts/check_closeout_bundle.py` で必須成果物の存在確認
4. **最終承認**
   - managerがチェックリスト完了を確認しdispatch可能にする

## Exit Criteria
- closeout reportが1件以上あり、対象cycleが明記されている
- handoff noteが1件以上あり、focusに対象cycleが含まれる
- bundle checkが `[OK]` で終了
- `make ticket-check` / `make link-check` が成功
