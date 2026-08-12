---
name: jupyter-notebook
description: Kasuta, kui kasutaja palub luua, üles ehitada või redigeerida Jupyteri
  märkmikke (`.ipynb`) katsetuste, uurimiste või juhendite jaoks; eelista kaasasolevaid
  malle ja käivita abiskript `new_notebook.py`, et genereerida puhas algne märkmik.
---
# Jupyter Notebooki oskus

Loo puhtaid, reprodutseeritavaid Jupyter-märkmikke kahe peamise režiimi jaoks:

- Eksperimendid ja avastuslik analüüs
- Õpetused ja õpetamisele suunatud samm-sammult juhendid

Eelista kaasasolevaid malle ja abiskripti ühtlase struktuuri ja vähem JSON-vigade saavutamiseks.

## Millal kasutada
- Loo uus `.ipynb` märkmik nullist.
- Muuda toored märkmed või skriptid struktureeritud märkmikuks.
- Refaktoreeri olemasolev märkmik, et see oleks reprodutseeritavam ja kiiremini läbitav.
- Loo eksperimente või õpetusi, mida teised saavad lugeda või uuesti käivitada.

## Otsustuspuu
- Kui päring on avastuslik, analüütiline või hüpoteesikeskne, vali `experiment`.
- Kui päring on juhendav, samm-sammult või sihtrühmale suunatud, vali `tutorial`.
- Kui redigeerid olemasolevat märkmikku, käsitle seda kui refaktoreerimist: säilita eesmärk ja paranda struktuuri.

## Oskuse rada (määratakse üks kord)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## Töövoog
1. Lukusta eesmärk.
Tuvasta märkmiku liik: `experiment` või `tutorial`.
Kirjuta üles eesmärk, sihtrühm ja kuidas näeb välja "valmis".

2. Skafoldi mallist.
Kasuta abiskripti, et vältida märkmiku JSON-i käsitsi kirjutamist.

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

3. Täida märkmik väikeste, käivitatavate sammudega.
Hoia iga koodirakk keskendunud ühele sammule.
Lisa lühikesed markdown-rakud, mis selgitavad eesmärki ja oodatavat tulemust.
Väldi suuri, mürarikkaid väljundeid, kui lühike kokkuvõte on piisav.

4. Kasuta õiget mustrit.
Eksperimentide puhul järgi `references/experiment-patterns.md`.
Õpetuste puhul järgi `references/tutorial-patterns.md`.

5. Redigeeri turvaliselt, kui töötad olemasolevate märkmikutega.
Säilita märkmiku struktuur; väldi rakkude ümberjärjestamist, välja arvatud juhul, kui see parandab loogilist ülalt alla voogu.
Eelista sihitud muudatusi täieliku ümberkirjutamise asemel.
Kui pead redigeerima toorest JSON-i, vaata esmalt üle `references/notebook-structure.md`.

6. Kinnita tulemus.
Käivita märkmik ülalt alla, kui keskkond seda lubab.
Kui käivitamine ei ole võimalik, teavita sellest selgelt ja täpsusta, kuidas seda lokaalselt kinnitada.
Kasuta lõplikku kontrollnimekirja failist `references/quality-checklist.md`.

## Mallid ja abiskript
- Mallid asuvad `assets/experiment-template.ipynb` ja `assets/tutorial-template.ipynb`.
- Abiskript laeb malli, uuendab pealkirjarakku ja kirjutab märkmiku.

Skripti asukoht:
- `$JUPYTER_NOTEBOOK_CLI` (vaikimisi paigaldus: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Ajutiste ja väljundi konventsioonid
- Kasuta vahelfailide jaoks `tmp/jupyter-notebook/`; kustuta pärast kasutamist.
- Kirjuta lõplikud artefaktid kataloogi `output/jupyter-notebook/`, kui töötad selles hoidlas.
- Kasuta stabiilseid, kirjeldavaid failinimesid (näiteks `ablation-temperature.ipynb`).

## Sõltuvused (paigalda ainult vajadusel)
Eelista sõltuvuste haldamisel `uv`.

Valikulised Python-paketid lokaalse märkmiku käivitamiseks:

```bash
uv pip install jupyterlab ipykernel
```

Kaasasolev skafoldi skript kasutab ainult Python-i standardteeki ega vaja täiendavaid sõltuvusi.

## Keskkond
Pole nõutud keskkonnamuutujaid.

## Viidete kaart
- `references/experiment-patterns.md`: eksperimendi struktuur ja heuristikad.
- `references/tutorial-patterns.md`: õpetuse struktuur ja õpetamisvoog.
- `references/notebook-structure.md`: märkmiku JSON-kuju ja ohutu redigeerimise reeglid.
- `references/quality-checklist.md`: lõplik kontrollnimekiri.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vastutusest loobumine:
See dokument on tõlgitud tehisintellektil põhineva tõlketeenuse Co-op Translator abil (https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta mis tahes selle tõlke kasutamisest tulenevate arusaamatuste või väärtõlgenduste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->