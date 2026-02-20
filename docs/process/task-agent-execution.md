# Task-Agent Execution Process

## Purpose
strict task-agent execution を標準化し、Plan品質と検証品質を固定化する。

## Flow (Plan → Implement → Verify → Record)
1. **Plan**
   - Ticket Goal/Deliverables/Todo を 1件ずつ分解
   - 依存関係と完了条件（Definition of Done）を明文化
2. **Implement**
   - 実装は ultra-fine 単位で進める（1 Todo = 1 artifact/1 change）
   - 変更後すぐに関連ドキュメントへ反映
3. **Verify**
   - 必須: `python3 scripts/check_tickets.py`
   - 追加したCLIは最低1回実行し、エラーなしを確認
   - link guard（README掲載確認）を実行
4. **Record**
   - docs/README.md へ新規artifactリンク追加
   - 必要なら report template へ実績を記録
   - Ticket Todo を [x] へ更新

## Definition of Done (DoD)
- 実装artifactが実在する
- 実装artifactが `docs/README.md` に掲載されている
- 検証コマンドが成功している
- チケットTodoが実装状態と一致している

## Review Checkpoints
- Ticketに記載したpathと実ファイルpathが一致
- Script usageが `docs/automation/README.md` に存在
- 手作業運用が必要な場合は checklist/template がある
