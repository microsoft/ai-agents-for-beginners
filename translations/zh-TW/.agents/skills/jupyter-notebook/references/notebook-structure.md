# 筆記本結構

Jupyter 筆記本是具有下列高階結構的 JSON 文件：

- `nbformat` and `nbformat_minor`
- `metadata`
- `cells`（包含 markdown 與 code 儲存格的清單）

當以程式編輯 `.ipynb` 檔案時：

- 保留範本中的 `nbformat` 與 `nbformat_minor`。
- 將 `cells` 保持為有序的清單；除非有意為之，否則不要重新排序。
- 對於程式碼儲存格，當未知時將 `execution_count` 設為 `null`。
- 對於程式碼儲存格，在建立骨架時將 `outputs` 設為空清單。
- 對於 markdown 儲存格，保持 `cell_type="markdown"` 與 `metadata={}`。

建議使用捆綁範本或 `new_notebook.py`（例如 `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`）來建立骨架，而不是手動撰寫原始的 notebook JSON。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責聲明：
本文件經由 AI 翻譯服務「Co‑op Translator」(https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不精確之處。原始文件的母語版本應被視為具權威性的依據。若為重要資訊，建議採用專業人工翻譯。對於因使用本翻譯而產生的任何誤解或誤譯，我們不承擔任何責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->