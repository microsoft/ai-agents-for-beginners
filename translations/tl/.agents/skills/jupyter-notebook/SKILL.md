---
name: jupyter-notebook
description: Gamitin kapag humihiling ang gumagamit na gumawa, mag-scaffold, o mag-edit
  ng mga Jupyter notebook (`.ipynb`) para sa mga eksperimento, eksplorasyon, o tutorial;
  mas piliin ang mga naka-bundle na template at patakbuhin ang helper script na `new_notebook.py`
  upang makabuo ng malinis na panimulang notebook.
---
# Kasanayan sa Jupyter Notebook

Gumawa ng malinis, nare-reproduce na mga Jupyter notebook para sa dalawang pangunahing modo:

- Mga eksperimento at pagsusuring eksploratoryo
- Mga tutorial at mga hakbang-hakbang na gabay na nakatuon sa pagtuturo

Mas mainam gamitin ang mga kalakip na template at ang script na tumutulong para sa magkakatugmang istruktura at mas kaunting pagkakamali sa JSON.

## Kailan gagamitin
- Gumawa ng bagong `.ipynb` notebook mula sa simula.
- I-convert ang magaspang na mga tala o mga script sa isang istrukturadong notebook.
- I-refactor ang umiiral na notebook upang maging mas reproducible at madaling silipin.
- Bumuo ng mga eksperimento o tutorial na babasahin o muling patatakbuhin ng ibang tao.

## Puno ng desisyon
- Kung ang kahilingan ay eksploratoryo, analitikal, o pinapatakbo ng hipotesis, piliin `experiment`.
- Kung ang kahilingan ay instruksiyonal, hakbang-hakbang, o tiyak sa madla, piliin `tutorial`.
- Kung ine-edit ang umiiral na notebook, ituring ito bilang refactor: panatilihin ang layunin at pagbutihin ang istruktura.

## Landas ng kasanayan (itakda nang isang beses)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

Ang mga skill na naka-scope sa user ay ini-install sa ilalim ng `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## Daloy ng trabaho
1. I-lock ang intensyon.
   Tukuyin ang uri ng notebook: `experiment` o `tutorial`.
   Itala ang layunin, madla, at kung ano ang itsura ng "tapos".

2. Gumawa ng balangkas mula sa template.
   Gamitin ang helper script upang maiwasan ang manu-manong paglikha ng raw notebook JSON.

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind experiment \
  --title "Compare prompt variants" \
  --out output/jupyter-notebook/compare-prompt-variants.ipynb
```

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind tutorial \
  --title "Intro to embeddings" \
  --out output/jupyter-notebook/intro-to-embeddings.ipynb
```

3. Punuan ang notebook ng maliliit at maaaring patakbuhing mga hakbang.
   Panatilihin ang bawat code cell na nakatuon sa isang hakbang.
   Magdagdag ng maiikling markdown cell na nagpapaliwanag ng layunin at inaasahang resulta.
   Iwasan ang malalaki at maingay na outputs kapag sapat ang maikling buod.

4. Gamitin ang tamang pattern.
   Para sa mga eksperimento, sundin ang `references/experiment-patterns.md`.
   Para sa mga tutorial, sundin ang `references/tutorial-patterns.md`.

5. Mag-edit nang ligtas kapag nagtatrabaho sa umiiral na mga notebook.
   Panatilihin ang istruktura ng notebook; iwasang i-reorder ang mga cell maliban kung pinapabuti nito ang daloy mula itaas pababa.
   Mas piliin ang tumpak na pag-edit kaysa sa buong muling pagsusulat.
   Kung kailangan mong i-edit ang raw JSON, repasuhin muna ang `references/notebook-structure.md`.

6. I-validate ang resulta.
   Patakbuhin ang notebook mula itaas pababa kapag pinapayagan ng kapaligiran.
   Kung hindi posible ang pag-e-execute, sabihin ito nang malinaw at ilahad kung paano i-validate nang lokal.
   Gamitin ang final pass checklist sa `references/quality-checklist.md`.

## Mga template at helper script
- Matatagpuan ang mga template sa `assets/experiment-template.ipynb` at `assets/tutorial-template.ipynb`.
- Ina-load ng helper script ang isang template, ina-update ang title cell, at sumusulat ng notebook.

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (default na naka-install: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Mga konbensyon para sa temp at output
- Gamitin ang `tmp/jupyter-notebook/` para sa mga pansamantalang file; tanggalin kapag tapos.
- Isulat ang mga huling artifact sa ilalim ng `output/jupyter-notebook/` kapag nagtatrabaho sa repo na ito.
- Gumamit ng matatag at naglalarawang mga filename (halimbawa, `ablation-temperature.ipynb`).

## Mga dependency (i-install lamang kapag kailangan)
Mas mainam gamitin ang `uv` para sa pamamahala ng dependency.

Opsyonal na mga Python package para sa lokal na pag-execute ng notebook:

```bash
uv pip install jupyterlab ipykernel
```

Ang kalakip na scaffold script ay gumagamit lamang ng Python standard library at hindi nangangailangan ng dagdag na mga dependency.

## Kapaligiran
Walang kinakailangang environment variables.

## Mapa ng sanggunian
- `references/experiment-patterns.md`: istruktura ng eksperimento at heuristika.
- `references/tutorial-patterns.md`: istruktura ng tutorial at daloy ng pagtuturo.
- `references/notebook-structure.md`: hugis ng notebook JSON at mga patakarang ligtas sa pag-edit.
- `references/quality-checklist.md`: panghuling checklist para sa pag-validate.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Paunawa:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakitandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o mga di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling‑tao. Hindi kami mananagot para sa anumang hindi pagkakaunawaan o maling interpretasyon na magmumula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->