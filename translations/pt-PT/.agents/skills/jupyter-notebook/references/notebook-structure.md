# Estrutura do Notebook

Os notebooks Jupyter são documentos JSON com a seguinte estrutura de alto nível:

- `nbformat` and `nbformat_minor`
- `metadata`
- `cells` (uma lista de células markdown e de código)

Ao editar ficheiros `.ipynb` programaticamente:

- Preservar `nbformat` e `nbformat_minor` a partir do modelo.
- Manter `cells` como uma lista ordenada; não reordenar a menos que seja intencional.
- Para células de código, defina `execution_count` como `null` quando for desconhecido.
- Para células de código, defina `outputs` como uma lista vazia ao criar o esqueleto.
- Para células de markdown, mantenha `cell_type="markdown"` e `metadata={}`.

Prefira criar o esqueleto a partir dos templates incluídos ou de `new_notebook.py` (por exemplo, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) em vez de escrever manualmente o JSON bruto do notebook.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:
Este documento foi traduzido com o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua de origem deve ser considerado a fonte oficial. Para informação crítica, recomenda-se uma tradução profissional realizada por um tradutor humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->