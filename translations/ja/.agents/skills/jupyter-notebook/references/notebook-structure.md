# ノートブックの構造

Jupyter ノートブックは、次のようなハイレベルな構成を持つ JSON ドキュメントです:

- `nbformat` and `nbformat_minor`
- `metadata`
- `cells` (マークダウンとコードセルのリスト)

When editing `.ipynb` files programmatically:

- テンプレートから `nbformat` と `nbformat_minor` を保持してください。
- `cells` を順序付きリストとして保持してください; 意図的でない限り順序を変更しないでください。
- コードセルでは、`execution_count` を不明な場合は `null` に設定してください。
- コードセルでは、スキャフォルディング時に `outputs` を空のリストに設定してください。
- マークダウンセルでは、`cell_type="markdown"` と `metadata={}` を保持してください。

生のノートブック JSON を手作業で作成するのではなく、バンドルされたテンプレートや `new_notebook.py`（例えば `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`）からスキャフォルディングすることを推奨します。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責事項:
本書はAI翻訳サービス「Co‑op Translator」(https://github.com/Azure/co-op-translator) を使用して翻訳されました。正確性には努めておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があることをご承知おきください。原文（原言語）が正確な情報源として優先されます。重要な情報については、専門の翻訳者による翻訳をお勧めします。本翻訳の利用により生じたいかなる誤解や誤訳についても、当社は責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->