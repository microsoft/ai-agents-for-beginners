# Sample Receipt Fixtures

Tre forudgenererede kvitteringsfiler til inspektion uden at køre notebooken.

| File | Hvad det er |
|---|---|
| `01_valid_receipt.json` | En gyldig underskrevet kvittering for et `lookup_flights` værktøjsopkald. Verificering returnerer Sandt. |
| `02_tampered_receipt.json` | Samme kvittering med ét felt ændret efter signering. Verificering returnerer Falsk. |
| `03_chain_three_receipts.json` | En kæde af tre gyldige kvitteringer (søg, hold, book) med `previous_receipt_hash` som forbinder hver til den forrige. |

## Verifikation af prøverne

Notebooken gennemgår verifikation i fire sektioner. For at verificere disse fixtures
direkte uden at køre gennem notebook-fortællingen:

```python
import json
from pathlib import Path

# Antager at du har gennemført importerne og hjælpefunktionerne
# fra sektionerne 1 og 2 i 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Sandt

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Falsk

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Hvordan disse blev genereret

Fixtures bruger samme kodevej som notebooken, med én fast underskrivningsnøgle
og faste tidsstempler for byte-reproducerbarhed. For at regenerere:

```bash
python3 generate_fixtures.py
```

(Scriptet findes i `generate_fixtures.py` i denne mappe.)

## Hvad studerende lærer ved at inspicere rå JSON

At læse det rå kvitteringsformat opbygger intuition, som cellerne i notebooken
ikke altid giver. Studerende, der hurtigt kigger på JSON, bemærker ofte:

1. Signaturen er en uigennemtrængelig base64url-streng, men alle andre felter er almindelig
   læsbar JSON. Signaturen krypterer ikke indholdet; den bekræfter det.
2. `public_key` er indlejret i kvitteringen. En revisor behøver ikke andet
   for at verificere (med forbehold for tillid til, at nøglen faktisk tilhører den angivne
   udsteder; se lektionens README om identitetsinfrastruktur).
3. At ændre et enkelt tegn i et hvilket som helst felt og herefter sammenligne denne fil med
   `02_tampered_receipt.json` gør byte-niveau mekanismen håndgribelig.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->