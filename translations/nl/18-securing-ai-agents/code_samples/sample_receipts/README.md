# Voorbeeld ontvangstbewijzen Fixtures

Vier voorgegenereerde ontvangstbewijsbestanden voor inspectie zonder het notebook uit te voeren.

| Bestand | Wat het is |
|---|---|
| `01_valid_receipt.json` | Een geldig ondertekend ontvangstbewijs voor een `lookup_flights` tool-aanroep. Verificatie retourneert True. |
| `02_tampered_receipt.json` | Hetzelfde ontvangstbewijs met één veld aangepast na ondertekening. Verificatie retourneert False. |
| `03_chain_three_receipts.json` | Een keten van drie geldige ontvangstbewijzen (search, hold, book) met `previous_receipt_hash` die elk aan de voorgaande koppelt. |
| `04_resigned_receipt.json` | Hetzelfde ontvangstbewijs gemanipuleerd en vervolgens opnieuw ondertekend door een aanvaller, met de eigen openbare sleutel van de aanvaller ingebed. Verifieert tegen de sleutel binnenin. Faalt tegen de sleutel van de uitgever. |

De fixtures ondertekenen direct de kanonieke JCS-bytes van de payload met Ed25519.
SHA-256 blijft in gebruik voor inhoudsdigesten en ontvangstbewijs-ketenlinks, niet als een
extra pre-hash vóór ondertekening.

## Verificatie van de voorbeelden

In `18-signed-receipts.ipynb`, voer eerst Setup en Secties 1 tot en met 3 uit.
Sectie 3 definieert `verify_chain`; slechts Secties 1 en 2 zijn niet genoeg.
Voer daarna het volgende blok uit in een nieuwe cel, met de werkmap van het notebook
ingesteld op `18-securing-ai-agents/code_samples`. De fixturepaden hieronder zijn relatief
ten opzichte van die map.

```python
import json
from pathlib import Path

fixture_dir = Path("sample_receipts")

# The issuer's key, pinned here rather than read from any receipt. In a real
# deployment it comes from the issuer's JWK Set or a pinned config value.
# This is the public half of the fixed signing key in generate_fixtures.py.
ISSUER_KEY = "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo"

valid = json.loads((fixture_dir / "01_valid_receipt.json").read_text(encoding="utf-8"))
print(f"Valid receipt: {verify_receipt(valid, ISSUER_KEY)}")        # True

tampered = json.loads((fixture_dir / "02_tampered_receipt.json").read_text(encoding="utf-8"))
print(f"Tampered receipt: {verify_receipt(tampered, ISSUER_KEY)}")  # False

chain = json.loads((fixture_dir / "03_chain_three_receipts.json").read_text(encoding="utf-8"))
for r in verify_chain(chain, ISSUER_KEY):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")

# The forgery. Verified against the key it carries, it passes. Against the
# issuer's key, it fails. Only the second question is worth asking.
forged = json.loads((fixture_dir / "04_resigned_receipt.json").read_text(encoding="utf-8"))
print(f"Forged, checked against its own key: "
      f"{verify_receipt(forged, forged['signature']['public_key'])}")  # True
print(f"Forged, checked against issuer key:  "
      f"{verify_receipt(forged, ISSUER_KEY)}")                        # False
```

### Controle van het voorbeeld zonder Jupyter

Vanaf de root van het repository, installeer de lesafhankelijkheden en voer uit:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Deze tests voeren de Python-voorbeelden in het notebook uit en exact het README-blok
hierboven. Ze controleren ook dat manipulatie en niet-geverifieerde sleutels door de
verifiers worden afgewezen. De tests slaan de `%pip` setup-cel van het notebook over omdat afhankelijkheden
apart worden geïnstalleerd. Ze veranderen het notebook of de fixtures niet.

## Hoe deze werden gegenereerd

De fixtures gebruiken hetzelfde codepad als het notebook, met één vaste ondertekeningsleutel
en vaste tijdstempels voor byte-herhaalbaarheid. Om te regenereren:

```bash
python3 generate_fixtures.py
```

(Script bevindt zich op `generate_fixtures.py` in deze map.)

`../test_signed_receipts.py` controleert dit allemaal automatisch: het voert de
code van het notebook uit, verifieert deze vier fixtures met de
`verify_receipt` en `verify_chain` van het notebook, en bevestigt dat het regenereren van de
fixtures identieke bytes oplevert. Vanaf `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Wat studenten leren door het inspecteren van rauwe JSON

Het lezen van het rauwe ontvangstbewijsformaat bouwt intuïtie op die de cellen in het notebook
niet altijd geven. Studenten die de JSON doorlezen merken vaak:

1. De handtekening is een ondoorzichtige base64url-string, maar elk ander veld is gewone
   leesbare JSON. De handtekening versleutelt de inhoud niet; ze bevestigt deze.
2. De `public_key` is ingebed in het ontvangstbewijs, wat het bestand
   zelfstandig maakt, maar het is niet wat een auditor verifieert. Vergelijk
   `02_tampered_receipt.json` met `04_resigned_receipt.json`: beide werden
   aangepast na ondertekening, maar de tweede werd opnieuw ondertekend met de eigen sleutel van de aanvaller,
   dus het verifieert tegen de sleutel die het draagt. De ingebedde sleutel
   vertelt je dat het bestand intern consistent is. Alleen een op een andere manier verkregen sleutel
   vertelt je wie het heeft uitgegeven.
3. Het wijzigen van één karakter van een veld buiten `signature`, en daarna
   het vergelijken van dit bestand met `02_tampered_receipt.json`, maakt het
   mechanisme op byte-niveau tastbaar.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->