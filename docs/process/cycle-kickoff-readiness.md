# Cycle Kickoff Readiness

## Purpose
次サイクル開始前に必要な入力/担当/依存関係を30分で確認し、初動遅延を防ぐ。

## Inputs
- 直前cycleのcloseout report（`docs/reports/closeouts/`）
- 最新ticket status（`docs/ticket-status.md`）
- manager handoff note（`docs/reports/handoffs/`）

## Readiness Flow
1. **Scope lock (5m)**
   - 今cycleで扱うticket範囲を確定
   - carry-over項目を明示
2. **Owner assign (10m)**
   - 各ticketの一次責任者を決定
   - 依存関係の先行/後続を明示
3. **Execution check (10m)**
   - 必要テンプレ/チェックリスト/CLIの有無確認
   - 不足があればkickoff前に補完
4. **Kickoff publish (5m)**
   - kickoff briefを発行し、task boardへ反映

## Exit Criteria
- cycle範囲のticketが明文化済み
- owner/期限/依存が埋まっている
- kickoff briefが `docs/reports/kickoffs/` に保存されている
- task board上でin-progress開始可能な状態
