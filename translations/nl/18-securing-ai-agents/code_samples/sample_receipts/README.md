# Voorbeeld Bon Fixtures

Drie vooraf gegenereerde bonbestanden voor inspectie zonder de notebook uit te voeren.

| Bestand | Wat het is |
|---|---|
| `01_valid_receipt.json` | Een geldige ondertekende bon voor een `lookup_flights` toolaanroep. Verificatie geeft True terug. |
| `02_tampered_receipt.json` | Dezelfde bon met één veld gewijzigd na ondertekening. Verificatie geeft False terug. |
| `03_chain_three_receipts.json` | Een keten van drie geldige bonnen (zoeken, reserveren, boeken) met `previous_receipt_hash` die elke bon aan de vorige koppelt. |

## De voorbeelden verifiëren

De notebook doorloopt verificatie in vier secties. Om deze fixtures direct te verifiëren zonder door de notebook tekst te gaan:

```python
import json
from pathlib import Path

# Gaat ervan uit dat je de imports en hulpfuncties hebt voltooid
# uit secties 1 en 2 van 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Waar

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Onwaar

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Hoe deze zijn gegenereerd

De fixtures gebruiken dezelfde codepad als de notebook, met één vaste ondertekeningssleutel
en vaste tijdstempels voor byte-reproduceerbaarheid. Om opnieuw te genereren:

```bash
python3 generate_fixtures.py
```

(Script bevindt zich in `generate_fixtures.py` in deze map.)

## Wat studenten leren door het inspecteren van ruwe JSON

Het lezen van het ruwe bonformaat bouwt intuïtie op die de cellen in de notebook niet altijd bieden. Studenten die de JSON snel doorlezen merken vaak:

1. De handtekening is een ondoorzichtige base64url-string, maar elk ander veld is gewone leesbare JSON. De handtekening versleutelt de inhoud niet; het getuigt ervan.
2. De `public_key` is ingebed in de bon. Een controleur heeft verder niets nodig om te verifiëren (mits vertrouwd wordt dat de sleutel daadwerkelijk van de opgegeven uitgever is; zie de les README over identiteitsinfrastructuur).
3. Het wijzigen van één enkel teken in een veld en daarna dit bestand vergelijken met `02_tampered_receipt.json` maakt het Byte-niveau mechanisme concreet.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->