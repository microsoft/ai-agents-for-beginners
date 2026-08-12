# 筆記本結構

Jupyter 筆記本是具有以下高階結構的 JSON 文件：

- `nbformat` and `nbformat_minor`
- `metadata`
- `cells`（一個由 Markdown 與程式碼儲存格組成的清單）

當以程式方式編輯 `.ipynb` 檔案時：

- 保留範本中的 `nbformat` 與 `nbformat_minor`。
- 將 `cells` 保持為有序清單；除非有意，否則不要重新排序。
- 對於程式碼儲存格，若未知則將 `execution_count` 設為 `null`。
- 對於程式碼儲存格，建立樣板時將 `outputs` 設為空清單。
- 對於 Markdown 儲存格，保持 `cell_type="markdown"` 及 `metadata={}`。

與其手動撰寫原始 notebook JSON，建議使用捆綁的範本或 `new_notebook.py` 來產生樣板（例如 `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`）。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但自動翻譯可能包含錯誤或不準確之處。應以原始語言的原文為準。如涉及重要資訊，建議採用專業人工翻譯。我們不對因使用此翻譯而引致的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->