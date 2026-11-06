# Voorbeeld Kwitanties Fixtures

Drie vooraf gegenereerde kwitantiebestanden om te inspecteren zonder de notebook uit te voeren.

| Bestand | Wat het is |
|---|---|
| `01_valid_receipt.json` | Een geldige ondertekende kwitantie voor een `lookup_flights` tool-aanroep. Verificatie geeft True terug. |
| `02_tampered_receipt.json` | Dezelfde kwitantie met één veld gewijzigd na ondertekening. Verificatie geeft False terug. |
| `03_chain_three_receipts.json` | Een keten van drie geldige kwitanties (search, hold, book) waarbij `previous_receipt_hash` elke kwitantie aan de voorgaande koppelt. |

De fixtures ondertekenen de kanonieke JCS-bytes van de payload rechtstreeks met Ed25519.
SHA-256 blijft in gebruik voor inhouds-digests en kwitantieketenlinks, niet als een
extra pre-hash vóór ondertekening.

## Het verifiëren van de voorbeelden

Voer in `18-signed-receipts.ipynb` eerst Setup en Secties 1 tot en met 3 uit.
Sectie 3 definieert `verify_chain`; alleen Secties 1 en 2 zijn niet voldoende.
Voer daarna het volgende blok in een nieuwe cel uit, met de werkmap van de notebook
ingesteld op `18-securing-ai-agents/code_samples`. De paden van de fixtures hieronder zijn relatief
ten opzichte van die map.

```python
import json
from pathlib import Path

fixture_dir = Path("sample_receipts")

# This fixture key is pinned by the verifier, outside the receipt under test.
FIXTURE_ISSUER_PUBLIC_KEY = "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo"
fixture_trusted_public_keys = {FIXTURE_ISSUER_PUBLIC_KEY}

valid = json.loads((fixture_dir / "01_valid_receipt.json").read_text())
print(
    f"Valid receipt: {verify_receipt(valid, fixture_trusted_public_keys)}"
)  # True

tampered = json.loads((fixture_dir / "02_tampered_receipt.json").read_text())
print(
    f"Tampered receipt: {verify_receipt(tampered, fixture_trusted_public_keys)}"
)  # False

chain = json.loads((fixture_dir / "03_chain_three_receipts.json").read_text())
for r in verify_chain(chain, fixture_trusted_public_keys):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

### De voorbeeldcontrole zonder Jupyter

Installeer vanuit de hoofdmap van de repository de lesafhankelijkheden en voer uit:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Deze tests voeren de Python-voorbeelden van de notebook en het exacte README-blok hierboven uit.
Ze controleren ook of manipulatie en niet-gespinde sleutels worden afgewezen door de
verificateurs. De tests slaan de `%pip` setup-cel van de notebook over omdat afhankelijkheden
apart worden geïnstalleerd. Ze wijzigen de notebook of fixtures niet.

## Hoe deze werden gegenereerd

De fixtures gebruiken hetzelfde codepad als de notebook, met één vaste ondertekeningssleutel
en vaste tijdstempels voor byte-reproduceerbaarheid. Om opnieuw te genereren:

```bash
python3 generate_fixtures.py
```

(Script staat in `generate_fixtures.py` in deze map.)

## Wat studenten leren door de ruwe JSON te inspecteren

Het lezen van het ruwe kwitantieformaat bouwt intuïtie op die de cellen in de notebook
niet altijd bieden. Studenten die door de JSON bladeren merken vaak het volgende op:

1. De handtekening is een ondoorzichtige base64url-string, maar elk ander veld is gewone
   leesbare JSON. De handtekening versleutelt de inhoud niet; ze getuigt ervan.
2. De `public_key` is ingebed in de kwitantie, wat voldoende is om
   zelfconsistentie te controleren maar niet voor vertrouwen in de uitgever. Een auditor moet het vergelijken met een sleutel
   die buiten de kwitantie is gespind of via een vertrouwd register is opgelost.
3. Het wijzigen van één enkel teken in een veld en vervolgens dit bestand opnieuw vergelijken met
   `02_tampered_receipt.json` maakt het mechanisme op byte-niveau concreet.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->