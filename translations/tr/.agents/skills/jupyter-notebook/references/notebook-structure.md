# Notebook Yapısı

Jupyter notebook'ları şu yüksek seviyeli yapıya sahip JSON belgeleridir:

- `nbformat` and `nbformat_minor`
- `metadata`
- `cells` (markdown ve kod hücrelerinden oluşan bir liste)

When editing `.ipynb` files programmatically:

- Şablondan `nbformat` ve `nbformat_minor` öğelerini koruyun.
- `cells`'i sıralı bir liste olarak tutun; kasıtlı olmadıkça yeniden sıraya koymayın.
- Kod hücreleri için, `execution_count` bilinmiyorsa `null` olarak ayarlayın.
- Kod hücreleri için, iskelet oluştururken `outputs`'u boş bir listeye ayarlayın.
- Markdown hücreleri için, `cell_type="markdown"` ve `metadata={}` olarak bırakın.

Prefer scaffolding from the bundled templates or `new_notebook.py` (for example, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) instead of hand-authoring raw notebook JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Sorumluluk Reddi:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk konusunda çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilindeki metin yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel bir insan çevirisi önerilir. Bu çevirinin kullanılmasından doğan herhangi bir yanlış anlama veya yanlış yorumlamadan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->