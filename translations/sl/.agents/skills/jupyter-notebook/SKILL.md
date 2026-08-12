---
name: jupyter-notebook
description: Uporabite, ko uporabnik prosi za ustvarjanje, pripravo ogrodja ali urejanje
  Jupyterjevih zvezkov (`.ipynb`) za poskuse, raziskovanja ali vadnice; prednost dajte
  priloženim predlogam in za ustvarjanje čistega začetnega zvezka zaženite pripomočni
  skript `new_notebook.py`.
---
# Spretnost Jupyter Notebook

Ustvarjajte čiste, ponovljive Jupyter zvezke za dva glavna načina:

- Eksperimenti in raziskovalna analiza
- Vadnice in učni vodniki

Raje uporabljajte priložene predloge in pomočni skript za dosledno strukturo in manj napak v JSON-u.

## Kdaj uporabiti
- Ustvarite nov `.ipynb` zvezek iz nič.
- Pretvorite grobe zapiske ali skripte v strukturiran zvezek.
- Refaktorirajte obstoječ zvezek, da bo bolj ponovljiv in lažje pregleden.
- Zgradite eksperimente ali vadnice, ki jih bodo drugi prebrali ali ponovno zagnali.

## Drevo odločanja
- Če je zahteva raziskovalna, analitična ali vodena s hipotezo, izberite `experiment`.
- Če je zahteva poučevalna, korak-po-koraku ali osredotočena na določeno občinstvo, izberite `tutorial`.
- Če urejate obstoječi zvezek, ga obravnavajte kot refaktoriranje: ohranite namen in izboljšajte strukturo.

## Pot spretnosti (nastavi enkrat)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

Spretnosti, omejene na uporabnika, se namestijo pod `$CODEX_HOME/skills` (privzeto: `~/.codex/skills`).

## Potek dela
1. Zaklenite namen.
Določite vrsto zvezka: `experiment` ali `tutorial`.
Zabeležite cilj, občinstvo in kako izgleda "done".

2. Ustvarite ogrodje iz predloge.
Uporabite pomočni skript, da se izognete ročnemu ustvarjanju surovega JSON-a zvezka.

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

3. Zapolnite zvezek z majhnimi, izvedljivimi koraki.
Naj bo vsaka celica s kodo osredotočena na en korak.
Dodajte kratke markdown celice, ki pojasnijo namen in pričakovani rezultat.
Izogibajte se velikim, hrupnim izhodom, kadar zadostuje kratek povzetek.

4. Uporabite pravi vzorec.
Za eksperimente sledite `references/experiment-patterns.md`.
Za vadnice sledite `references/tutorial-patterns.md`.

5. Urejajte varno pri delu z obstoječimi zvezki.
Ohranite strukturo zvezka; izogibajte se prerazporejanju celic, razen če to izboljša zgodbo od zgoraj navzdol.
Raje izberite ciljane popravke kot popolne ponovne zapise.
Če morate urejati surov JSON, najprej preglejte `references/notebook-structure.md`.

6. Preverite rezultat.
Zaženite zvezek od vrha do dna, ko okolje to omogoča.
Če izvajanje ni mogoče, to izrecno navedite in pojasnite, kako preveriti lokalno.
Uporabite kontrolni seznam zadnjega pregleda v `references/quality-checklist.md`.

## Predloge in pomočni skript
- Predloge se nahajajo v `assets/experiment-template.ipynb` in `assets/tutorial-template.ipynb`.
- Pomožni skript naloži predlogo, posodobi celico z naslovom in zapiše zvezek.

Pot do skripta:
- `$JUPYTER_NOTEBOOK_CLI` (privzeto nameščen: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Konvencije začasnih in izhodnih datotek
- Uporabljajte `tmp/jupyter-notebook/` za vmesne datoteke; izbrišite po končanju.
- Zapišite končne artefakte v `output/jupyter-notebook/`, ko delate v tem repozitoriju.
- Uporabljajte stabilna, opisna imena datotek (na primer, `ablation-temperature.ipynb`).

## Odvisnosti (namestite le po potrebi)
Za upravljanje odvisnosti raje uporabljajte `uv`.

Neobvezni paketi Python za lokalno izvajanje zvezkov:

```bash
uv pip install jupyterlab ipykernel
```

Vgrajeni skript za ogrodje uporablja samo standardno knjižnico Pythona in ne zahteva dodatnih odvisnosti.

## Okolje
Ni potrebnih okoljskih spremenljivk.

## Zemljevid referenc
- `references/experiment-patterns.md`: struktura eksperimenta in heuristike.
- `references/tutorial-patterns.md`: struktura vadnic in potek poučevanja.
- `references/notebook-structure.md`: obliko JSON-a zvezka in pravila varnega urejanja.
- `references/quality-checklist.md`: kontrolni seznam za končno preverjanje.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Izjava o omejitvi odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje, ki temelji na umetni inteligenci, [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvor‑nem jeziku se šteje za avtoritativni vir. Za kritične informacije priporočamo strokovni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->