---
name: jupyter-notebook
description: Käytetään, kun käyttäjä pyytää luomaan, alustamaan tai muokkaamaan Jupyter-muistikirjoja
  (`.ipynb`) kokeita, tutkimuksia tai opetusohjelmia varten; käytä mieluummin mukana
  olevia mallipohjia ja suorita apuohjelmaskripti `new_notebook.py` luodaksesi puhtaan
  aloitusmuistikirjan.
---
# Jupyter Notebook -taito

Luo siistejä, toistettavia Jupyter-muistikirjoja kahteen pääasialliseen tilaan:

- Kokeilut ja tutkiva analyysi
- Opetus ja opastetut läpikäynnit

Suosi mukana tulevia malleja ja apuskriptiä yhtenäisen rakenteen ja vähempien JSON-virheiden vuoksi.

## Milloin käyttää
- Luo uusi `.ipynb`-muistikirja alusta alkaen.
- Muunna karkeat muistiinpanot tai skriptit rakenteelliseksi muistikirjaksi.
- Refaktoroi olemassa oleva muistikirja entistä toistettavammaksi ja helposti silmäiltäväksi.
- Rakenna kokeiluja tai opastuksia, joita muut ihmiset lukevat tai suorittavat uudelleen.

## Päätöspuu
- Jos pyyntö on tutkivaa, analyyttistä tai hypoteesikeskeistä, valitse `experiment`.
- Jos pyyntö on opastava, vaiheittainen tai kohderyhmäspezifi, valitse `tutorial`.
- Jos muokkaat olemassa olevaa muistikirjaa, käsittele sitä refaktorointina: säilytä tarkoitus ja paranna rakennetta.

## Taitopolku (määritä kerran)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## Työnkulku
1. Vahvista tarkoitus.
Tunnista muistikirjan tyyppi: `experiment` tai `tutorial`.
Kirjaa tavoite, yleisö ja milloin työ on valmis.

2. Luo runko mallista.
Käytä apuskriptiä välttääksesi raakamuotoisen muistikirjan JSON:n käsin kirjoittamisen.

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

3. Täytä muistikirja pienillä, ajettavilla askelilla.
Pidä kukin koodisolu keskittyneenä yhteen askelmaan.
Lisää lyhyitä markdown-soluja, jotka selittävät tarkoituksen ja odotetun tuloksen.
Vältä suuria, meluisia tulosteita, kun lyhyt yhteenveto riittää.

4. Käytä oikeaa mallia.
Kokeiluille seuraa `references/experiment-patterns.md`.
Opastuksille seuraa `references/tutorial-patterns.md`.

5. Muokkaa turvallisesti olemassa olevia muistikirjoja käsitellessäsi.
Säilytä muistikirjan rakenne; vältä solujen uudelleenjärjestelyä, ellei se paranna ylhäältä alas -kertomusta.
Suosi kohdennettuja muutoksia täysien uudelleenkirjoitusten sijaan.
Jos sinun on pakko muokata raakaa JSON:ia, tutustu ensin `references/notebook-structure.md`.

6. Varmista tulos.
Suorita muistikirja ylhäältä alas, kun ympäristö sen sallii.
Jos suoritusta ei voi tehdä, mainitse se selkeästi ja kerro miten validoida paikallisesti.
Käytä lopullista tarkistuslistaa `references/quality-checklist.md`.

## Mallit ja apuskripti
- Mallit sijaitsevat tiedostoissa `assets/experiment-template.ipynb` ja `assets/tutorial-template.ipynb`.
- Apuskripti lataa mallin, päivittää otsikkosolun ja kirjoittaa muistikirjan.

Skriptin polku:
- `$JUPYTER_NOTEBOOK_CLI` (installed default: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Väliaikaistiedostot ja tulostuskäytännöt
- Käytä `tmp/jupyter-notebook/` väliaikaisiin tiedostoihin; poista käytön jälkeen.
- Kirjoita lopulliset artefaktit kansioon `output/jupyter-notebook/` työskennellessäsi tässä repossa.
- Käytä stabiileja, kuvaavia tiedostonimiä (esimerkiksi `ablation-temperature.ipynb`).

## Riippuvuudet (asenna vain tarvittaessa)
Prefer `uv` for dependency management.

Optional Python packages for local notebook execution:

```bash
uv pip install jupyterlab ipykernel
```

Mukana oleva scaffold-skripti käyttää vain Pythonin standardikirjastoa eikä vaadi lisäriippuvuuksia.

## Ympäristö
Ei vaadittavia ympäristömuuttujia.

## Viitemappi
- `references/experiment-patterns.md`: kokeilun rakenne ja heuristiikat.
- `references/tutorial-patterns.md`: opastusrakenne ja opetuksen kulku.
- `references/notebook-structure.md`: muistikirjan JSON-rakenne ja turvallisen muokkauksen säännöt.
- `references/quality-checklist.md`: lopullinen validointitarkistuslista.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vastuuvapauslauseke:
Tämä asiakirja on käännetty tekoälypohjaisella käännöspalvelulla [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattisissa käännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää määräävänä lähteenä. Tärkeiden tietojen osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnasta.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->