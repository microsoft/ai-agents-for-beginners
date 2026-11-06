# Eksempel på kvitterings-fixtures

Tre forudgenererede kvitteringsfiler til inspektion uden at køre notebook'en.

| Fil | Hvad det er |
|---|---|
| `01_valid_receipt.json` | En gyldig underskrevet kvittering for et `lookup_flights` værktøjskald. Verifikation returnerer True. |
| `02_tampered_receipt.json` | Samme kvittering med ét felt ændret efter underskrift. Verifikation returnerer False. |
| `03_chain_three_receipts.json` | En kæde af tre gyldige kvitteringer (search, hold, book) med `previous_receipt_hash`, der forbinder hver til den forrige. |

Fixtures underskriver payload'ens kanoniske JCS-bytes direkte med Ed25519.
SHA-256 bruges fortsat til indholdsdigests og kvitteringskædelinks, ikke som en
ekstra for-hash før signering.

## Verificering af prøverne

I `18-signed-receipts.ipynb`, kør først Setup og sektionerne 1 til 3.
Sektion 3 definerer `verify_chain`; sektionerne 1 og 2 alene er ikke nok.
Kør derefter følgende blok i en ny celle, hvor notebook'ens arbejdsmappen
er sat til `18-securing-ai-agents/code_samples`. Fixture-stierne nedenfor er relative
til denne mappe.

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

### Tjek af eksemplet uden Jupyter

Fra repository-roden, installer lektionens afhængigheder og kør:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Disse tests udfører notebook'ens Python-eksempler og den præcise README-blok
ovenfor. De tjekker også, at manipulation og ikke-fastlåste nøgler afvises af
verificatorerne. Testene springer notebook'ens `%pip` setup-celle over, fordi afhængigheder
installeres separat. De ændrer ikke notebook'en eller fixtures.

## Hvordan disse blev genereret

Fixtures bruger samme kodevej som notebook'en, med en fast underskriftsnøgle
og faste tidsstempler for byte-reproducerbarhed. For at regenerere:

```bash
python3 generate_fixtures.py
```

(Scriptet er ved `generate_fixtures.py` i denne mappe.)

## Hvad studerende lærer ved at inspicere rå JSON

At læse det rå kvitteringsformat opbygger en intuition, som cellerne i notebook'en
ikke altid giver. Studerende, der hurtigt kigger på JSON'en, bemærker ofte:

1. Signaturen er en uigennemsigtig base64url-streng, men hver andet felt er almindelig
   læsbar JSON. Signaturen krypterer ikke indholdet; den bevidner det.
2. `public_key` er indlejret i kvitteringen, hvilket er nok til at tjekke
   selv-konsistens men ikke udsteder-tillid. En revisor må sammenligne det med en nøgle,
   der er fastlåst uden for kvitteringen eller fundet via et betroet register.
3. At ændre et enkelt tegn i et hvilket som helst felt og derefter gen-sammenligne denne fil med
   `02_tampered_receipt.json` gør byte-niveau mekanismen konkret.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->