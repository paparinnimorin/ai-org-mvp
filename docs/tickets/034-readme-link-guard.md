# Ticket 034 — README Link Guard

## Goal
「実装済みだが index 未掲載」を防ぐため、README link guardを自動化する。

## Deliverables
- READMEリンク検証CLI
- 運用ルール

## Todo
- [x] `scripts/check_readme_links.py` を実装（ticket内参照pathがREADMEにあるか検証）
- [x] `Makefile` に link-check target を追加
- [x] `docs/automation/README.md` に運用手順を追加
- [x] `docs/README.md` にlink guardスクリプトの説明を追加
