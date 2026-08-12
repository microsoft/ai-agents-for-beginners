# Estrutura do Notebook

Os notebooks Jupyter são documentos JSON com esta estrutura de alto nível:

- `nbformat` e `nbformat_minor`
- `metadata`
- `cells` (uma lista de células markdown e de código)

Ao editar arquivos `.ipynb` programaticamente:

- Preservar `nbformat` e `nbformat_minor` a partir do modelo.
- Mantenha `cells` como uma lista ordenada; não reordene a menos que seja intencional.
- Para células de código, defina `execution_count` como `null` quando desconhecido.
- Para células de código, defina `outputs` como uma lista vazia ao gerar o esqueleto.
- Para células markdown, mantenha `cell_type="markdown"` e `metadata={}`.

Prefira scaffolding a partir dos templates incluídos ou `new_notebook.py` (por exemplo, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) em vez de redigir manualmente o JSON bruto do notebook.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Isenção de responsabilidade**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para alcançar precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional realizada por um tradutor humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->