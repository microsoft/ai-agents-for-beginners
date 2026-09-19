# Eksempel på kvitteringsdata

Tre forudgenererede kvitteringsfiler til inspektion uden at køre notebook'en.

| Fil | Hvad det er |
|---|---|
| `01_valid_receipt.json` | En gyldig signeret kvittering til et `lookup_flights` værktøjsopkald. Verifikation returnerer True. |
| `02_tampered_receipt.json` | Den samme kvittering med et felt ændret efter signering. Verifikation returnerer False. |
| `03_chain_three_receipts.json` | En kæde af tre gyldige kvitteringer (søg, hold, book) med `previous_receipt_hash` som forbinder hver til den forrige. |

Dataene signerer payload'ets kanoniske JCS-bytes direkte med Ed25519.
SHA-256 bruges stadig til indholdsdigests og kvitteringskæde-links, ikke som en
ekstra for-hash før signering.

## Verificering af eksemplerne

Notebook'en gennemgår verifikation i fire sektioner. For at verificere disse data
direkte uden at køre notebook-fortællingen:

```python
import json
from pathlib import Path

# Antager, at du har gennemført importerne og hjælpefunktionerne
# fra sektionerne 1 og 2 af 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Sand

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Falsk

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Hvordan disse blev genereret

Dataene bruger den samme kodevej som notebook'en, med en fast signeringsnøgle
og faste tidsstempler for byte-reproducerbarhed. For at regenerere:

```bash
python3 generate_fixtures.py
```

(Scriptet findes i `generate_fixtures.py` i denne mappe.)

## Hvad studerende lærer ved at inspicere rå JSON

At læse det rå kvitteringsformat bygger intuition, som cellerne i notebook'en
ikke altid giver. Studerende, der hurtigt gennemser JSON'en, bemærker ofte:

1. Signaturen er en opak base64url-streng, men alle andre felter er almindelig
   læsbar JSON. Signaturen krypterer ikke indholdet; den bevidner det.
2. `public_key` er indlejret i kvitteringen. En revisor behøver intet andet
   for at verificere (med forbehold for troen på, at nøglen faktisk tilhører den påståede
   udsteder; se lektionens README om identitetsinfrastruktur).
3. Ændring af et enkelt tegn i et hvilket som helst felt, og derefter at sammenligne denne fil med
   `02_tampered_receipt.json`, gør byte-niveau mekanismen konkret.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->