# Eksempel på kvitterings-fixtures

Fire forudgenererede kvitteringsfiler til inspektion uden at køre notebooken.

| Fil | Hvad det er |
|---|---|
| `01_valid_receipt.json` | En gyldig underskrevet kvittering for et `lookup_flights` værktøjsopkald. Verifikation returnerer Sandt. |
| `02_tampered_receipt.json` | Samme kvittering med ét felt ændret efter underskrivelse. Verifikation returnerer Falsk. |
| `03_chain_three_receipts.json` | En kæde af tre gyldige kvitteringer (search, hold, book) med `previous_receipt_hash`, der forbinder hver til den foregående. |
| `04_resigned_receipt.json` | Samme kvittering manipuleret og derefter genunderskrevet af en angriber, med angriberens egen offentlige nøgle indlejret. Verificeres mod nøglen inde i den. Fejler mod udstederens nøgle. |

Fixtures underskriver payloadens kanoniske JCS-bytes direkte med Ed25519.
SHA-256 anvendes fortsat til indholdsgenveje og kvitteringskædelinks, ikke som en
ekstra for-hash før underskrivelse.

## Verificering af eksemplerne

I `18-signed-receipts.ipynb`, kør Setup og sektionerne 1 til 3 først.
Sektion 3 definerer `verify_chain`; sektionerne 1 og 2 alene er ikke nok.
Kør derefter følgende blok i en ny celle, med notebookens arbejdsmappe
sat til `18-securing-ai-agents/code_samples`. Fixtures-stierne nedenfor er relative
til den mappe.

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

### Tjek af eksemplet uden Jupyter

Fra repositories rod, installer lektionsafhængighederne og kør:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Disse tests eksekverer notebookens Python-eksempler og den præcise README-blok
ovenfor. De tjekker også, at manipulation og ikke-fastlåste nøgler afvises af
verificatorerne. Testene springer notebookens `%pip` setup-celle over, fordi afhængigheder
installeres separat. De ændrer ikke notebook eller fixtures.

## Hvordan disse blev genereret

Fixtures bruger samme kodevej som notebooken, med én fast underskriftsnøgle
og faste tidsstempler for byte-reproducerbarhed. For at regenerere:

```bash
python3 generate_fixtures.py
```

(Scriptet findes i `generate_fixtures.py` i denne mappe.)

`../test_signed_receipts.py` tjekker alt dette automatisk: den kører
notebookens kode, verificerer disse fire fixtures med notebookens
`verify_receipt` og `verify_chain`, og bekræfter at regenerering af
fixtures giver identiske bytes. Fra `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Hvad studerende lærer ved at inspicere rå JSON

At læse det rå kvitteringsformat opbygger intuition, som cellerne i notebooken
ikke altid giver. Studerende, som skimmer JSON, bemærker ofte:

1. Underskriften er en uigennemsigtig base64url-streng, men alle andre felter er almindelig
   læsbar JSON. Underskriften krypterer ikke indholdet; den bekræfter det.
2. `public_key` er indlejret i kvitteringen, hvilket gør filen
   selvstændig, men ikke det, en revisor verificerer imod. Sammenlign
   `02_tampered_receipt.json` med `04_resigned_receipt.json`: begge blev
   ændret efter underskrivelse, men den anden blev genunderskrevet med angriberens
   egen nøgle, så den verificerer mod den medfølgende nøgle. Den indlejrede nøgle
   fortæller, at filen er internt konsistent. Kun en nøgle opnået
   andetsteds fortæller, hvem der udstedte den.
3. At ændre ét enkelt tegn i et hvilket som helst felt uden for `signature`, og derefter
   sammenligne denne fil igen med `02_tampered_receipt.json`, gør
   byte-niveauet mekanismen konkret.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->