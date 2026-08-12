---
name: jupyter-notebook
description: Naudokite, kai vartotojas prašo sukurti, paruošti arba redaguoti Jupyter
  užrašų knygeles (`.ipynb`) eksperimentams, tyrimams arba pamokoms; teikite pirmenybę
  pridedamiems šablonams ir paleiskite pagalbinį scenarijų `new_notebook.py`, kad
  sugeneruotumėte švarų pradinį užrašų knygelę.
---
# Jupyter Notebook įgūdis

Kurti tvarkingas, reprodukuojamas Jupyter užrašų knygeles dviem pagrindiniais režimais:

- Eksperimentai ir tyrinėjamoji analizė
- Pamokos ir mokymui skirtos žingsnis po žingsnio instrukcijos

Teikite pirmenybę pridedamiems šablonams ir pagalbiniam skriptui dėl nuoseklios struktūros ir mažiau JSON klaidų.

## Kada naudoti
- Sukurti naują `.ipynb` užrašų knygelę nuo pradžių.
- Paversti užrašus ar skriptus į struktūrizuotą užrašų knygelę.
- Refaktorizuoti esamą užrašų knygelę, kad ji būtų labiau reprodukuojama ir lengvai peržvelgiama.
- Kurti eksperimentus ar pamokas, kurias skaitys ar vėl paleis kiti žmonės.

## Sprendimų medis
- Jei užklausa yra tyrinėjamoji, analitinė arba grindžiama hipoteze, pasirinkite `experiment`.
- Jei užklausa yra instruktyvinė, žingsnis po žingsnio arba skirta konkrečiai auditorijai, pasirinkite `tutorial`.
- Redaguodami esamą užrašų knygelę, traktaukite tai kaip refaktoringą: išsaugokite paskirtį ir pagerinkite struktūrą.

## Įgūdžio kelias (nustatyti vieną kartą)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

Vartotojo lygio įgūdžiai įdiegiami po `$CODEX_HOME/skills` (numatytasis: `~/.codex/skills`).

## Darbo eiga
1. Užfiksuokite ketinimą.
Nustatykite užrašų knygelės tipą: `experiment` arba `tutorial`.
Apibrėžkite tikslą, auditoriją ir kaip atrodytų "užbaigta".

2. Sukurkite karkasą iš šablono.
Naudokite pagalbinį skriptą, kad išvengtumėte rankinio notebook JSON rašymo.

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

3. Užpildykite užrašų knygelę mažais, paleidžiamais žingsniais.
Kiekvieną kodo ląstelę orientuokite į vieną žingsnį.
Pridėkite trumpas markdown ląsteles, kurios paaiškina paskirtį ir tikėtiną rezultatą.
Venkite didelių, triukšmingų išvesčių, kai pakanka trumpo santraukos.

4. Taikykite tinkamą modelį.
Eksperimentams vadovaukitės `references/experiment-patterns.md`.
Pamokoms vadovaukitės `references/tutorial-patterns.md`.

5. Redaguokite saugiai dirbdami su esamomis užrašų knygelėmis.
Išsaugokite užrašų knygelės struktūrą; venkite ląstelių pertvarkymo, nebent tai pagerina pasakojimą nuo viršaus žemyn.
Teikite pirmenybę tiksliems redagavimams, o ne pilniems perrašymams.
Jei privalote redaguoti neapdorotą JSON, pirmiausia peržiūrėkite `references/notebook-structure.md`.

6. Patikrinkite rezultatą.
Paleiskite užrašų knygelę nuo pradžios iki pabaigos, kai aplinka leidžia.
Jei vykdyti neįmanoma, aiškiai apie tai praneškite ir nurodykite, kaip patikrinti vietoje.
Naudokite galutinį patikros sąrašą `references/quality-checklist.md`.

## Šablonai ir pagalbinis skriptas
- Šablonai yra `assets/experiment-template.ipynb` ir `assets/tutorial-template.ipynb`.
- Pagalbinis skriptas įkelia šabloną, atnaujina pavadinimo ląstelę ir įrašo užrašų knygelę.

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (įdiegtas numatytasis: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Laikinos ir išvesties konvencijos
- Naudokite `tmp/jupyter-notebook/` tarpinėms byloms; ištrinkite pabaigus.
- Galutinius artefaktus įrašykite į `output/jupyter-notebook/` dirbant šiame repozitorijoje.
- Naudokite stabilias, aprašomas failų pavadinimus (pavyzdžiui, `ablation-temperature.ipynb`).

## Priklausomybės (įdiekite tik kai reikia)
Pirmenybę skirkite `uv` priklausomybių valdymui.

Pasirenkami Python paketai vietiniam užrašų knygelės vykdymui:

```bash
uv pip install jupyterlab ipykernel
```

Pridėtas šablono skriptas naudoja tik Python standartinę biblioteką ir nereikalauja papildomų priklausomybių.

## Aplinka
Nėra privalomų aplinkos kintamųjų.

## Nuorodų žemėlapis
- `references/experiment-patterns.md`: eksperimento struktūra ir heuristika.
- `references/tutorial-patterns.md`: pamokos struktūra ir mokymo eiga.
- `references/notebook-structure.md`: užrašų knygelės JSON forma ir saugaus redagavimo taisyklės.
- `references/quality-checklist.md`: galutinis patikrinimo sąrašas.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama kreiptis į profesionalų žmogaus vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą aiškinimą, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->