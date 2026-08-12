# Istruktura ng Notebook

Ang mga Jupyter notebook ay mga dokumentong JSON na may ganitong pangkalahatang anyo:

- `nbformat` at `nbformat_minor`
- `metadata`
- `cells` (isang listahan ng mga markdown at code na cell)

Kapag ina-edit ang mga `.ipynb` na file sa pamamagitan ng programa:

- Panatilihin ang `nbformat` at `nbformat_minor` mula sa template.
- Panatilihin ang `cells` bilang nakaayos na listahan; huwag baguhin ang pagkakasunud-sunod maliban kung sinadya.
- Para sa mga code cell, itakda ang `execution_count` sa `null` kapag hindi alam.
- Para sa mga code cell, itakda ang `outputs` sa isang walang laman na listahan kapag gumagawa ng paunang balangkas.
- Para sa mga markdown cell, panatilihin ang `cell_type="markdown"` at `metadata={}`.

Mas mainam kumuha ng paunang balangkas mula sa mga naka-bundle na template o `new_notebook.py` (halimbawa, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) sa halip na mano-manong pagsulat ng raw notebook JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Paunawa:

Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI para sa pagsasalin [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kaming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o kamalian. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na awtoritatibong sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin na ginawa ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na magmumula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->