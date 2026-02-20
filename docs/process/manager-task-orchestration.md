# Manager Task Orchestration

## 目的
managerが複数タスクを同時進行させるときの標準運用を固定化する。

## 1. Intake
1. 要求を1行Goalに分解
2. 依存関係を確認（前提ticket / ファイル / checker）
3. 30分以内で終わる単位まで分割

## 2. Plan
1. `docs/process/manager-task-board.md` にチケット行を追加
2. owner / due / blocked-by を埋める
3. 成果物パスを先に確定する

## 3. Dispatch
1. `docs/templates/manager-brief.md` でbrief作成
2. dispatch前に `docs/checklists/manager-dispatch-checklist.md` を実行
3. 受け手に Goal / Deliverables / Todo / Verify を明示

## 4. Review
1. Todoの `[x]` と実ファイルを突合
2. `make ticket-check` と `make link-check` を実行
3. 必要時 `make manager-board-check` でboardリンク検証

## 5. Close
1. `docs/tickets/*.md` のTodoを更新
2. `python3 scripts/update_ticket_status.py` で状態更新
3. commit messageにticket番号を含める（例: `feat: complete tickets 035-038`）
