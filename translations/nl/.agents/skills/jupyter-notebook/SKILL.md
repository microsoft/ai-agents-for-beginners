---
name: jupyter-notebook
description: Gebruik dit wanneer de gebruiker vraagt om Jupyter-notebooks (`.ipynb`)
  te maken, op te zetten of te bewerken voor experimenten, verkenningen of tutorials;
  geef de voorkeur aan de meegeleverde sjablonen en voer het hulpscript `new_notebook.py`
  uit om een schoon startnotebook te genereren.
---
# Jupyter Notebook-vaardigheid

Maak schone, reproduceerbare Jupyter-notebooks voor twee hoofdmodi:

- Experimenten en verkennende analyse
- Tutorials en onderwijsgerichte stapsgewijze handleidingen

Geef de voorkeur aan de bijgeleverde sjablonen en het hulpscript voor een consistente structuur en minder JSON-fouten.

## Wanneer te gebruiken
- Maak een nieuw `.ipynb`-notebook vanaf nul.
- Zet ruwe aantekeningen of scripts om in een gestructureerd notebook.
- Refactor een bestaand notebook om het beter reproduceerbaar en makkelijker te scannen te maken.
- Bouw experimenten of tutorials die door anderen gelezen of opnieuw uitgevoerd zullen worden.

## Beslissingsboom
- Als het verzoek verkennend, analytisch of hypothese-gedreven is, kies `experiment`.
- Als het verzoek instructief, stap-voor-stap of doelgroepgericht is, kies `tutorial`.
- Als je een bestaand notebook bewerkt, behandel het als een refactor: behoud de intentie en verbeter de structuur.

## Vaardigheidspad (eenmalig instellen)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

Gebruikersgebonden skills worden geïnstalleerd onder `$CODEX_HOME/skills` (standaard: `~/.codex/skills`).

## Werkwijze
1. Leg de intentie vast.
Identificeer het notebooktype: `experiment` of `tutorial`.
Leg het doel, de doelgroep en hoe "done" eruitziet vast.

2. Bouw op vanuit het sjabloon.
Gebruik het hulpscript om handmatig bewerken van ruwe notebook-JSON te vermijden.

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

3. Vul het notebook met kleine, uitvoerbare stappen.
Houd elke codecel gericht op één stap.
Voeg korte markdown-cellen toe die het doel en het verwachte resultaat uitleggen.
Vermijd grote, rommelige outputs wanneer een korte samenvatting volstaat.

4. Pas het juiste patroon toe.
Voor experimenten, volg `references/experiment-patterns.md`.
Voor tutorials, volg `references/tutorial-patterns.md`.

5. Bewerk veilig bij het werken met bestaande notebooks.
Behoud de notebook-structuur; vermijd het herschikken van cellen, tenzij het de opbouw van boven naar beneden verbetert.
Geef de voorkeur aan gerichte aanpassingen boven volledige herschrijvingen.
Als je de ruwe JSON moet bewerken, bekijk eerst `references/notebook-structure.md`.

6. Valideer het resultaat.
Voer het notebook van boven naar beneden uit wanneer de omgeving dit toelaat.
Als uitvoering niet mogelijk is, geef dit dan expliciet aan en vermeld hoe lokaal gevalideerd kan worden.
Gebruik de eindcontrolelijst in `references/quality-checklist.md`.

## Sjablonen en hulpscript
- Sjablonen bevinden zich in `assets/experiment-template.ipynb` en `assets/tutorial-template.ipynb`.
- Het hulpscript laadt een sjabloon, werkt de titeldcel bij en schrijft een notebook.

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (standaard geïnstalleerd: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Tijdelijke en uitvoerconventies
- Gebruik `tmp/jupyter-notebook/` voor tussenbestanden; verwijder wanneer klaar.
- Schrijf uiteindelijke artefacten naar `output/jupyter-notebook/` wanneer je in deze repo werkt.
- Gebruik stabiele, beschrijvende bestandsnamen (bijvoorbeeld `ablation-temperature.ipynb`).

## Afhankelijkheden (alleen installeren wanneer nodig)
Geef de voorkeur aan `uv` voor afhankelijkheidsbeheer.

Optionele Python-pakketten voor lokale notebook-uitvoering:

```bash
uv pip install jupyterlab ipykernel
```

Het bijgeleverde scaffold-script gebruikt alleen de Python-standaardbibliotheek en vereist geen extra afhankelijkheden.

## Omgeving
Geen vereiste omgevingsvariabelen.

## Referentiemap
- `references/experiment-patterns.md`: structuur van experimenten en heuristieken.
- `references/tutorial-patterns.md`: structuur van tutorials en lesopbouw.
- `references/notebook-structure.md`: notebook-JSON-structuur en regels voor veilig bewerken.
- `references/quality-checklist.md`: eindcontrolelijst.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, kan een automatische vertaling fouten of onnauwkeurigheden bevatten. Het oorspronkelijke document in de brontaal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->