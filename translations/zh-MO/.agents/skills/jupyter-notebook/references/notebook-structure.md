# 筆記本結構

Jupyter 筆記本是具有以下高階結構的 JSON 文件：

- `nbformat` and `nbformat_minor`
- `metadata`
- `cells`（一個包含 Markdown 與程式碼儲存格的清單）

當以程式方式編輯 `.ipynb` 檔案時：

- 保留範本中的 `nbformat` 與 `nbformat_minor`。
- 將 `cells` 保持為有序清單；除非刻意，否則勿重新排序。
- 對於程式碼儲存格，當未知時將 `execution_count` 設為 `null`。
- 對於程式碼儲存格，在建立骨架時將 `outputs` 設為空清單。
- 對於 Markdown 儲存格，保持 `cell_type="markdown"` 與 `metadata={}`。

建議使用捆綁範本或 `new_notebook.py`（例如 `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`）來建立骨架，而非手動撰寫原始的筆記本 JSON。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責聲明：
本文件已使用 AI 翻譯服務 Co-op Translator（https://github.com/Azure/co-op-translator）進行翻譯。雖然我們力求準確，但自動翻譯可能包含錯誤或不精確之處。原始語言的原文應被視為具權威性的來源。若涉及關鍵資訊，建議採用專業人工翻譯。我們對因使用此翻譯而導致的任何誤解或錯誤詮釋概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->