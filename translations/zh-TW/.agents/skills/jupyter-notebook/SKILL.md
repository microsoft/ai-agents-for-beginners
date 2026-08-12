---
name: jupyter-notebook
description: 當使用者要求建立、搭建或編輯 Jupyter 筆記本（`.ipynb`）用於實驗、探索或教學時使用；優先使用隨附範本並執行輔助腳本 `new_notebook.py`
  來產生一個乾淨的起始筆記本。
---
# Jupyter Notebook 技能

為兩種主要模式建立乾淨、可重現的 Jupyter 筆記本：

- 實驗與探索性分析
- 教學與教學導向的逐步示範

優先使用內建的範本與輔助腳本，以維持一致的結構並減少 JSON 錯誤。

## 何時使用
- 從頭建立新的 `.ipynb` 筆記本。
- 將粗略筆記或腳本轉換為結構化的筆記本。
- 將現有筆記本重構為更可重現且易於瀏覽的版本。
- 建立將由其他人閱讀或重新執行的實驗或教學內容。

## 決策樹
- 如果請求是探索性、分析性或以假設為驅動，選擇 `experiment`。
- 如果請求是教學性、逐步導引或針對特定觀眾，選擇 `tutorial`。
- 如果是在編輯現有筆記本，視為重構：保留原意並改善結構。

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

3. 填充筆記本，使用小且可執行的步驟。
保持每個程式碼儲存格專注於單一步驟。
新增簡短的 markdown 儲存格來說明目的與預期結果。
當簡短摘要足夠時，避免產生大量嘈雜的輸出。

4. 應用正確的模式。
對於實驗，請遵循 `references/experiment-patterns.md`。
對於教學，請遵循 `references/tutorial-patterns.md`。

5. 在處理現有筆記本時安全地編輯。
保留筆記本結構；除非能改善從上到下的敘事流程，否則避免重新排序儲存格。
偏好有針對性的編輯而非全部重寫。
如果必須編輯原始 JSON，先檢閱 `references/notebook-structure.md`。

6. 驗證結果。
在環境允許時，從上到下執行筆記本。
如果無法執行，請明確說明並指出如何在本機驗證。
使用 `references/quality-checklist.md` 中的最終檢查清單。

## 範本與輔助腳本
- 範本位於 `assets/experiment-template.ipynb` 與 `assets/tutorial-template.ipynb`。
- 輔助腳本會載入範本、更新標題儲存格，並寫出筆記本。

腳本路徑：
- `$JUPYTER_NOTEBOOK_CLI` (installed default: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## 暫存與輸出慣例
- 對於中間檔案，使用 `tmp/jupyter-notebook/`；完成後刪除。
- 在此 repo 工作時，將最終產物寫入 `output/jupyter-notebook/`。
- 使用穩定且具描述性的檔名（例如，`ablation-temperature.ipynb`）。

## 相依性（僅在需要時安裝）
偏好使用 `uv` 進行相依性管理。

供本機筆記本執行的可選 Python 套件：

```bash
uv pip install jupyterlab ipykernel
```

The bundled scaffold script uses only the Python standard library and does not require extra dependencies.

## 環境
沒有必需的環境變數。

## 參考對照表
- `references/experiment-patterns.md`: 實驗結構與啟發式規則。
- `references/tutorial-patterns.md`: 教學結構與教學流程。
- `references/notebook-structure.md`: 筆記本 JSON 形態與安全編輯規則。
- `references/quality-checklist.md`: 最終驗證檢查清單。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責聲明：
本文件已透過 AI 翻譯服務 Co-op Translator (https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始語言版本的文件應被視為具權威性的來源。對於重要資訊，建議採用專業人工翻譯。因使用本翻譯而產生的任何誤解或誤譯，我們不承擔任何責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->