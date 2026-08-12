---
name: jupyter-notebook
description: Použite, keď používateľ požiada o vytvorenie, vygenerovanie kostry alebo
  úpravu Jupyter notebookov (`.ipynb`) pre experimenty, prieskumy alebo tutoriály;
  uprednostnite zabudované šablóny a spustite pomocný skript `new_notebook.py` na
  vygenerovanie čistého východiskového notebooku.
---
# Zručnosť Jupyter Notebook

Vytvárajte čisté, reprodukovateľné Jupyter notebooky pre dva hlavné režimy:

- Experimenty a prieskumná analýza
- Tutoriály a prehľady zamerané na výučbu

Uprednostňujte dodávané šablóny a pomocný skript pre konzistentnú štruktúru a menej chýb v JSON.

## Kedy použiť
- Vytvorte nový `.ipynb` notebook od začiatku.
- Preveďte hrubé poznámky alebo skripty do štruktúrovaného notebooku.
- Refaktorujte existujúci notebook, aby bol viac reprodukovateľný a prehľadnejší.
- Vytvárajte experimenty alebo tutoriály, ktoré budú čítať alebo znovu spúšťať iní ľudia.

## Rozhodovací strom
- Ak je požiadavka prieskumná, analytická alebo riadená hypotézou, zvoľte `experiment`.
- Ak je požiadavka inštruktážna, krok za krokom alebo špecifická pre publikum, zvoľte `tutorial`.
- Pri úprave existujúceho notebooku ho považujte za refaktor: zachovajte zámer a zlepšite štruktúru.

## Cesta zručnosti (nastaviť raz)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

Zručnosti obmedzené na používateľa sa inštalujú do `$CODEX_HOME/skills` (predvolené: `~/.codex/skills`).

## Pracovný postup
1. Uzamknite zámer.
Určite typ notebooku: `experiment` alebo `tutorial`.
Zaznamenajte cieľ, publikum a to, ako vyzerá „hotovo“.

2. Vytvorte kostru zo šablóny.
Použite pomocný skript, aby ste sa vyhli ručnému písaniu surového JSON notebooku.

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

3. Vyplňte notebook malými, spustiteľnými krokmi.
Udržujte každú kódovú bunku zameranú na jeden krok.
Pridajte krátke markdown bunky, ktoré vysvetlia účel a očakávaný výsledok.
Vyhnite sa veľkým, hlučným výstupom, keď postačuje krátke zhrnutie.

4. Použite správny vzor.
Pre experimenty postupujte podľa `references/experiment-patterns.md`.
Pre tutoriály postupujte podľa `references/tutorial-patterns.md`.

5. Pri práci s existujúcimi notebookmi upravujte bezpečne.
Zachovajte štruktúru notebooku; vyhnite sa preusporiadaniu buniek, pokiaľ to nezlepší príbeh zhora nadol.
Uprednostňujte cielené úpravy pred úplnými prepismi.
Ak musíte upravovať surový JSON, najprv si prezrite `references/notebook-structure.md`.

6. Overte výsledok.
Spustite notebook od začiatku do konca, keď to prostredie umožňuje.
Ak vykonanie nie je možné, uveďte to explicitne a popíšte, ako overiť lokálne.
Použite kontrolný zoznam finálnej kontroly v `references/quality-checklist.md`.

## Šablóny a pomocný skript
- Šablóny sa nachádzajú v `assets/experiment-template.ipynb` a `assets/tutorial-template.ipynb`.
- Pomocný skript načíta šablónu, aktualizuje titulnú bunku a zapíše notebook.

Cesta ku skriptu:
- `$JUPYTER_NOTEBOOK_CLI` (predvolené umiestnenie inštalácie: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Konvencie dočasných súborov a výstupov
- Používajte `tmp/jupyter-notebook/` pre medzistupňové súbory; po dokončení ich odstráňte.
- Ukladajte finálne artefakty do `output/jupyter-notebook/` pri práci v tomto repozitári.
- Používajte stabilné, výstižné názvy súborov (napríklad `ablation-temperature.ipynb`).

## Závislosti (inštalujte len keď je to potrebné)
Uprednostňujte `uv` na správu závislostí.

Voliteľné Python balíky pre lokálne spúšťanie notebooku:

```bash
uv pip install jupyterlab ipykernel
```

Dodávaný scaffold skript používa iba štandardnú knižnicu Pythonu a nevyžaduje ďalšie závislosti.

## Prostredie
Nie sú potrebné žiadne premenné prostredia.

## Mapa referencií
- `references/experiment-patterns.md`: štruktúra experimentu a heuristiky.
- `references/tutorial-patterns.md`: štruktúra tutoriálu a výukový tok.
- `references/notebook-structure.md`: tvar JSON notebooku a pravidlá bezpečnej úpravy.
- `references/quality-checklist.md`: kontrolný zoznam finálneho overenia.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, berte prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by sa mal považovať za rozhodujúci zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->