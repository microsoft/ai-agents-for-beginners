# Eksempel på kvitteringsmaler

Tre forhåndsgenererte kvitteringsfiler for inspeksjon uten å kjøre notatboken.

| Fil | Hva det er |
|---|---|
| `01_valid_receipt.json` | En gyldig signert kvittering for et `lookup_flights` verktøys kall. Verifisering gir True. |
| `02_tampered_receipt.json` | Den samme kvitteringen med ett felt endret etter signering. Verifisering gir False. |
| `03_chain_three_receipts.json` | En kjede med tre gyldige kvitteringer (search, hold, book) med `previous_receipt_hash` som kobler hver til den forrige. |

## Verifisering av eksemplene

Notatboken går gjennom verifisering i fire seksjoner. For å verifisere disse malene
direkte uten å kjøre gjennom notatbokfortellingen:

```python
import json
from pathlib import Path

# Forutsetter at du har fullført importene og hjelpefunksjonene
# fra seksjonene 1 og 2 i 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Sant

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Usant

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Hvordan disse ble generert

Malene bruker samme kodebane som notatboken, med én fast signeringsnøkkel
og faste tidsstempler for byte-reproduserbarhet. For å gjenskape:

```bash
python3 generate_fixtures.py
```

(Skriptet ligger i `generate_fixtures.py` i denne katalogen.)

## Hva studenter lærer ved å inspisere rå JSON

Å lese det råe kvitteringsformatet bygger intuisjon som cellene i notatboken
ikke alltid gir. Studenter som skummer JSON-en legger ofte merke til:

1. Signaturen er en ugjennomsiktig base64url-streng, men alle andre felt er vanlig,
   lesbar JSON. Signaturen krypterer ikke innholdet; den bekrefter det.
2. `public_key` er innebygd i kvitteringen. En revisor trenger ikke noe annet
   for å verifisere (med forbehold om å stole på at nøkkelen faktisk tilhører den påståtte
   utstederen; se leksjonens README om identitetsinfrastruktur).
3. Å endre ett enkelt tegn i hvilket som helst felt, og så sammenligne denne filen med
   `02_tampered_receipt.json`, gjør mekanismen på bytenivå konkret.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->