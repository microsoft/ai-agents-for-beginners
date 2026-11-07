# Eksempel Kvittofiler

Fire forhåndsgenererte kvittofiler for inspeksjon uten å kjøre notatboken.

| Fil | Hva det er |
|---|---|
| `01_valid_receipt.json` | Et gyldig signert kvittering for en `lookup_flights` verktøy-anrop. Verifisering returnerer True. |
| `02_tampered_receipt.json` | Den samme kvitteringen med ett felt endret etter signering. Verifisering returnerer False. |
| `03_chain_three_receipts.json` | En kjede av tre gyldige kvitteringer (search, hold, book) med `previous_receipt_hash` som lenker hver til den forrige. |
| `04_resigned_receipt.json` | Den samme kvitteringen tuklet med og deretter re-signert av en angriper, med angriperens egen offentlige nøkkel innebygd. Verifiserer med nøkkelen inne i den. Feiler mot utstederens nøkkel. |

Filene signerer payloadens kanoniske JCS-bytes direkte med Ed25519.
SHA-256 brukes fortsatt for innholdsoppsummeringer og kvitto-kjedelenker, ikke som en
ekstra forhånds-hash før signering.

## Verifisere eksemplene

I `18-signed-receipts.ipynb`, kjør Setup og Seksjon 1 til 3 først.
Seksjon 3 definerer `verify_chain`; Seksjon 1 og 2 alene er ikke nok.
Deretter kjør følgende blokk i en ny celle, med notatbokens arbeidskatalog
satt til `18-securing-ai-agents/code_samples`. Filbanene nedenfor er relative
til den katalogen.

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

### Sjekke eksempelet uten Jupyter

Fra repository-roten, installer lekasjonsavhengigheter og kjør:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Disse testene kjører notatbokens Python-eksempler og den nøyaktige README-blokken
over. De sjekker også at manipulasjoner og ufestede nøkler blir forkastet av
verifikatorene. Testene hopper over notatbokens `%pip` setup-celle fordi avhengigheter
installeres separat. De endrer ikke notatboken eller filene.

## Hvordan disse ble generert

Filene bruker samme kodebane som notatboken, med en fast signeringsnøkkel
og faste tidsstempler for byte-reproduserbarhet. For å regenerere:

```bash
python3 generate_fixtures.py
```

(Scriptet er ved `generate_fixtures.py` i denne katalogen.)

`../test_signed_receipts.py` sjekker alt dette automatisk: det kjører
notatbokens kode, verifiserer disse fire filene med notatbokens
`verify_receipt` og `verify_chain`, og bekrefter at regenerering av
filene gir identiske bytes. Fra `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Hva studentene lærer av å inspisere rå JSON

Å lese rå kvitteringsformat bygger opp intuisjon som cellene i notatboken
ikke alltid gir. Studenter som skummer JSON legger ofte merke til:

1. Signaturen er en ugjennomsiktig base64url-streng, men alle andre felt er ren
   lesbar JSON. Signaturen krypterer ikke innholdet; den bekrefter det.
2. `public_key` er innebygd i kvitteringen, noe som gjør filen
   selvstendig, men det er ikke hva en revisor verifiserer mot. Sammenlign
   `02_tampered_receipt.json` med `04_resigned_receipt.json`: begge ble
   endret etter signering, men den andre ble re-signert med angriperens
   egen nøkkel, så den verifiseres med nøkkelen den bærer. Den innebygde nøkkelen
   forteller deg at filen er internt konsistent. Bare en nøkkel oppnådd
   fra et annet sted forteller hvem som utstedte den.
3. Å endre ett enkelt tegn i et felt utenfor `signature`, og deretter
   sammenligne denne filen med `02_tampered_receipt.json`, gjør
   byte-nivå-mekanismen konkret.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->