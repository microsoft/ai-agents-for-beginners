# Eksempelkvitteringer

Tre forhåndsgenererte kvitteringsfiler for inspeksjon uten å kjøre notatboken.

| Fil | Hva det er |
|---|---|
| `01_valid_receipt.json` | En gyldig signert kvittering for et `lookup_flights` verktøysanrop. Verifisering returnerer True. |
| `02_tampered_receipt.json` | Den samme kvitteringen med ett felt endret etter signering. Verifisering returnerer False. |
| `03_chain_three_receipts.json` | En kjede på tre gyldige kvitteringer (søk, hold, book) med `previous_receipt_hash` som kobler hver til den forrige. |

Fixture-filene signerer nyttelastens kanoniske JCS-byter direkte med Ed25519.
SHA-256 brukes fortsatt for innholdsdigester og kvitteringskjede-lenker, ikke som en
ekstra forhåndshash før signering.

## Verifisere eksemplene

I `18-signed-receipts.ipynb`, kjør Setup og Seksjonene 1 til 3 først.
Seksjon 3 definerer `verify_chain`; kun Seksjon 1 og 2 er ikke nok.
Deretter kjører du følgende blokk i en ny celle, med notatbokens arbeidsmappe
satt til `18-securing-ai-agents/code_samples`. Fixture-filene nedenfor er relative
til den mappen.

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

### Sjekke eksempelet uten Jupyter

Fra repository-roten, installer leksjonens avhengigheter og kjør:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Disse testene kjører notatbokens Python-eksempler og den eksakte README-blokken
ovenfor. De sjekker også at manipulering og usikrede nøkler avvises av
verifiseringsfunksjonene. Testene hopper over notatbokens `%pip` oppsettscelle fordi avhengigheter
installeres separat. De endrer ikke notatboken eller fixture-filene.

## Hvordan disse ble generert

Fixture-filene bruker samme kodebane som notatboken, med én fast signeringsnøkkel
og faste tidsstempler for byte-reproduserbarhet. For å generere på nytt:

```bash
python3 generate_fixtures.py
```

(Scriptet ligger i `generate_fixtures.py` i denne mappen.)

## Hva studenter lærer ved å inspisere rå JSON

Å lese rå kvitteringsformat bygger opp en intuisjon som cellene i notatboken
ikke alltid gir. Studenter som skummer JSON ser ofte:

1. Signaturen er en ugjennomsiktig base64url-streng, men alle andre felt er vanlig
   lesbar JSON. Signaturen krypterer ikke innholdet; den bekrefter det.
2. `public_key` er innebygd i kvitteringen, det er nok til å sjekke
   selvkonsistens, men ikke utstederens tillit. En revisor må sammenligne den med en nøkkel
   som er lenket utenfor kvitteringen eller hentet gjennom et betrodd register.
3. Å endre et enkelt tegn i noe felt, og deretter sammenligne denne filen med
   `02_tampered_receipt.json`, gjør byte-nivå mekanismen konkret.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->