# 笔记本结构

Jupyter 笔记本是具有以下高层结构的 JSON 文档:

- `nbformat` 和 `nbformat_minor`
- `metadata`
- `cells` (一个由 Markdown 和代码单元组成的列表)

在以编程方式编辑 `.ipynb` 文件时:

- 保持模板中的 `nbformat` 和 `nbformat_minor`.
- 将 `cells` 保持为有序列表；除非有意，否则不要重新排序.
- 对于代码单元，当未知时将 `execution_count` 设置为 `null`.
- 对于代码单元，在搭建脚手架时将 `outputs` 设置为空列表.
- 对于 Markdown 单元，保持 `cell_type="markdown"` 和 `metadata={}`.

优先从捆绑的模板或 `new_notebook.py` (例如 `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) 进行脚手架搭建，而不是手工编写原始笔记本 JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免责声明：
本文件使用 AI 翻译服务 Co‑op Translator (https://github.com/Azure/co-op-translator) 翻译而成。尽管我们尽力确保准确，但请注意自动翻译可能包含错误或不准确之处。应将原始语言的文档视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而导致的任何误解或错误解读，我们概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->