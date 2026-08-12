# Märkmiku struktuur

Jupyter märkmikud on JSON dokumendid, millel on järgmine kõrgetasemeline kuju:

- `nbformat` ja `nbformat_minor`
- `metadata`
- `cells` (markdowni ja koodi lahtrite nimekiri)

Kui redigeerite `.ipynb` faile programmiliselt:

- Säilitage mallist `nbformat` ja `nbformat_minor`.
- Hoidke `cells` tellitud nimekirjana; ärge muutke järjekorda, kui see pole tahtlik.
- Koodi lahtrite puhul määrake `execution_count` väärtuseks `null`, kui see on teadmata.
- Koodi lahtrite puhul määrake `outputs` väärtuseks tühi nimekiri, kui koostate alust.
- Markdown lahtrite puhul hoidke `cell_type="markdown"` ja `metadata={}`.

Eelistage alust keskselt kaasasolevatest mallidest või `new_notebook.py` failist (näiteks `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`), selle asemel et käsitsi kirjeldada toore märkmiku JSON-i.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:  
See dokument on tõlgitud kasutades tehisintellektil põhinevat tõlke teenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument oma algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul soovitatakse professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tekkida võivate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->