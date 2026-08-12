---
name: jupyter-notebook
description: 當使用者要求建立、搭建或編輯用於實驗、探索或教學的 Jupyter 筆記本 (`.ipynb`) 時使用；優先採用內建範本並執行輔助腳本
  `new_notebook.py` 以產生一個乾淨的起始筆記本。
---
# Jupyter Notebook 技能

為兩種主要模式建立乾淨、可重現的 Jupyter 筆記本：

- 實驗與探索性分析
- 教學及導覽式示範

優先使用隨附的範本和輔助腳本，以獲得一致的結構並減少 JSON 錯誤。

## 何時使用
- 從頭建立新的 `.ipynb` 筆記本。
- 將草稿筆記或腳本轉換為結構化的筆記本。
- 重構現有的筆記本，使其更具可重現性且易於瀏覽。
- 建立會被他人閱讀或重新執行的實驗或教學範例。

## 決策樹
- 如果請求是探索性、分析性或以假設為驅動，選擇 `experiment`。
- 如果請求是教學型、逐步或針對特定受眾，選擇 `tutorial`。
- 如果編輯現有筆記本，將其視為重構：保留意圖並改進結構。

## 技能路徑（設定一次）

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## 工作流程
1. 鎖定意圖。
Identify the notebook kind: `experiment` or `tutorial`.
Capture the objective, audience, and what "done" looks like.

2. 從範本建立骨架。
Use the helper script to avoid hand-authoring raw notebook JSON.

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind experiment \
  --title "Compare prompt variants" \
  --out output/jupyter-notebook/compare-prompt-variants.ipynb
```

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind tutorial \
  --title "Intro to embeddings" \
  --out output/jupyter-notebook/intro-to-embeddings.ipynb
```

3. 用小而可執行的步驟填充筆記本。
Keep each code cell focused on one step.
Add short markdown cells that explain the purpose and expected result.
Avoid large, noisy outputs when a short summary works.

4. 套用正確的範式。
For experiments, follow `references/experiment-patterns.md`.
For tutorials, follow `references/tutorial-patterns.md`.

5. 在處理現有筆記本時安全地編輯。
Preserve the notebook structure; avoid reordering cells unless it improves the top-to-bottom story.
Prefer targeted edits over full rewrites.
If you must edit raw JSON, review `references/notebook-structure.md` first.

6. 驗證結果。
Run the notebook top-to-bottom when the environment allows.
If execution is not possible, say so explicitly and call out how to validate locally.
Use the final pass checklist in `references/quality-checklist.md`.

## 範本與輔助腳本
- 範本位於 `assets/experiment-template.ipynb` 與 `assets/tutorial-template.ipynb`。
- 輔助腳本會載入範本、更新標題儲存格，並寫出筆記本。

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (預設安裝位置: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## 暫存與輸出慣例
- 使用 `tmp/jupyter-notebook/` 做為中間檔案位置；完成後刪除。
- 在此 repo 中工作時，將最終產物寫在 `output/jupyter-notebook/` 下。
- 使用穩定且具描述性的檔名（例如，`ablation-temperature.ipynb`）。

## 相依套件（僅在需要時安裝）
Prefer `uv` for dependency management.

Optional Python packages for local notebook execution:

```bash
uv pip install jupyterlab ipykernel
```

隨附的骨架腳本僅使用 Python 標準函式庫，不需要額外相依套件。

## 環境
沒有必須的環境變數。

## 參考地圖
- `references/experiment-patterns.md`: 實驗結構與啟發式準則。
- `references/tutorial-patterns.md`: 教學結構與教學流程。
- `references/notebook-structure.md`: 筆記本 JSON 格式與安全編輯規則。
- `references/quality-checklist.md`: 最終驗證檢查清單。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責聲明：
本文件已使用 AI 翻譯服務 Co-op Translator（https://github.com/Azure/co-op-translator）進行翻譯。儘管我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原文之母語版本應視為具權威性的來源。若涉及重要資訊，建議採用專業人工翻譯。我們對因使用本翻譯而產生的任何誤解或曲解不承擔任何責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->