---
name: jupyter-notebook
description: 當使用者要求建立、搭建或編輯 Jupyter 筆記本（`.ipynb`）以進行實驗、探索或教學範例時使用；優先使用隨附的範本，並執行輔助腳本
  `new_notebook.py` 來產生一個乾淨的起始筆記本。
---
# Jupyter Notebook 技能

建立清晰、可重現的 Jupyter 筆記本，以兩種主要模式為主：

- 實驗與探索性分析
- 教學導向的教學步驟

優先使用內建範本與輔助腳本，以維持一致的結構並減少 JSON 錯誤。

## 何時使用
- 從頭建立新的 `.ipynb` 筆記本。
- 將草稿筆記或腳本轉換為結構化的筆記本。
- 重構現有筆記本，使其更具可重現性與易讀性。
- 建立會被其他人閱讀或重新執行的實驗或教學。

## 決策流程
- 如果請求屬於探索性、分析性或以假設為驅動，選擇 `experiment`。
- 如果請求是教學性的、逐步說明或針對特定受眾，選擇 `tutorial`。
- 如果是編輯現有筆記本，視為重構：保留原意並改善結構。

## 技能路徑（設定一次）

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## 工作流程
1. Lock the intent.
Identify the notebook kind: `experiment` or `tutorial`.
Capture the objective, audience, and what "done" looks like.

2. Scaffold from the template.
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

3. Fill the notebook with small, runnable steps.
Keep each code cell focused on one step.
Add short markdown cells that explain the purpose and expected result.
Avoid large, noisy outputs when a short summary works.

4. Apply the right pattern.
For experiments, follow `references/experiment-patterns.md`.
For tutorials, follow `references/tutorial-patterns.md`.

5. Edit safely when working with existing notebooks.
Preserve the notebook structure; avoid reordering cells unless it improves the top-to-bottom story.
Prefer targeted edits over full rewrites.
If you must edit raw JSON, review `references/notebook-structure.md` first.

6. Validate the result.
Run the notebook top-to-bottom when the environment allows.
If execution is not possible, say so explicitly and call out how to validate locally.
Use the final pass checklist in `references/quality-checklist.md`.

## 範本與輔助腳本
- 範本位於 `assets/experiment-template.ipynb` 與 `assets/tutorial-template.ipynb`。
- 輔助腳本會載入範本、更新標題儲存格，並寫出筆記本。

腳本路徑：
- `$JUPYTER_NOTEBOOK_CLI` (installed default: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## 暫存和輸出慣例
- 將 `tmp/jupyter-notebook/` 用作中間檔案；完成後刪除。
- 在此專案內工作時，將最終產物寫到 `output/jupyter-notebook/`。
- 使用穩定且具描述性的檔名（例如，`ablation-temperature.ipynb`）。

## 相依套件（僅在需要時安裝）
偏好使用 `uv` 來管理相依性。

可選的本地執行筆記本用 Python 套件：

```bash
uv pip install jupyterlab ipykernel
```

The bundled scaffold script uses only the Python standard library and does not require extra dependencies.

## 環境
不需要任何環境變數。

## 參考清單
- `references/experiment-patterns.md`: 實驗結構與啟發式準則。
- `references/tutorial-patterns.md`: 教學結構與教學流程。
- `references/notebook-structure.md`: 筆記本 JSON 結構與安全編輯規則。
- `references/quality-checklist.md`: 最終驗證清單。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責聲明：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。以原始語言撰寫的原文應被視為具權威性的版本。對於重要資訊，建議採用專業人工翻譯。我們對因使用本翻譯而導致的任何誤解或錯誤詮釋概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->