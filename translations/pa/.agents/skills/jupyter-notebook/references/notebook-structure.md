# ਨੋਟਬੁੱਕ ਦੀ ਸੰਰਚਨਾ

Jupyter notebooks JSON ਦਸਤਾਵੇਜ਼ ਹਨ ਜੋ ਇਸ ਉੱਚ-ਸਤਰੀ ਆਕਾਰ ਦੇ ਹੁੰਦੇ ਹਨ:

- `nbformat` and `nbformat_minor`
- `metadata`
- `cells` (markdown ਅਤੇ ਕੋਡ ਸੈੱਲਾਂ ਦੀ ਇੱਕ ਸੂਚੀ)

When editing `.ipynb` files programmatically:

- ਟੈਂਪਲੇਟ ਤੋਂ `nbformat` ਅਤੇ `nbformat_minor` ਨੂੰ ਬਰਕਰਾਰ ਰੱਖੋ।
- `cells` ਨੂੰ ਇੱਕ ਕ੍ਰਮਬੱਧ ਸੂਚੀ ਵਜੋਂ ਰੱਖੋ; ਸਿਵਾਏ ਜਦੋਂ ਇਹ ਇਰਾਦਾਤਮਕ ਹੋਵੇ, ਦੁਬਾਰਾ ਕ੍ਰਮਬੱਧ ਨਾ ਕਰੋ।
- ਕੋਡ ਸੈੱਲਾਂ ਲਈ, ਜਦੋਂ ਅਣਜਾਣ ਹੋਵੇ ਤਾਂ `execution_count` ਨੂੰ `null` ਤੇ ਸੈੱਟ ਕਰੋ।
- ਕੋਡ ਸੈੱਲਾਂ ਲਈ, ਰੂਪ ਰੇਖਾ ਬਣਾਉਣ ਵੇਲੇ `outputs` ਨੂੰ ਖਾਲੀ ਸੂਚੀ ਤੇ ਸੈੱਟ ਕਰੋ।
- ਮਾਰਕਡਾਊਨ ਸੈੱਲਾਂ ਲਈ, `cell_type="markdown"` ਅਤੇ `metadata={}` ਨੂੰ ਰੱਖੋ।

ਬੰਡਲ ਕੀਤੀਆਂ ਟੈਂਪਲੇਟਾਂ ਜਾਂ `new_notebook.py` (for example, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) ਤੋਂ ਰੂਪ ਰੇਖਾ ਲੈਣਾ ਹੱਥੋਂ ਕੱਚਾ ਨੋਟਬੁੱਕ JSON ਲਿਖਣ ਦੀ ਥਾਂ ਤਰਜੀਹ ਦਿਓ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ਅਸਵੀਕਾਰ:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ Co-op Translator (https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਪਰ ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਤਰੁਟੀਆਂ ਜਾਂ ਗਲਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਉਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਧਾਨ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਕਾਰਨ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->