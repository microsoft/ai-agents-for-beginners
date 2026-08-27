# Eksempel på kvitteringsfiler

Tre forhåndsgenererte kvitteringsfiler for inspeksjon uten å kjøre notatboken.

| Fil | Hva det er |
|---|---|
| `01_valid_receipt.json` | En gyldig signert kvittering for en `lookup_flights` verktøysanrop. Verifiseringen returnerer True. |
| `02_tampered_receipt.json` | Den samme kvitteringen med ett felt endret etter signering. Verifiseringen returnerer False. |
| `03_chain_three_receipts.json` | En kjede på tre gyldige kvitteringer (søk, hold, bestilling) med `previous_receipt_hash` som lenker hver til den forrige. |

Fiksturene signerer nyttelastens kanoniske JCS-bytes direkte med Ed25519.
SHA-256 brukes fortsatt for innholdsdigester og kjedelenker i kvitteringene, ikke som en
ekstra forhånds-hash før signering.

## Verifisering av eksemplene

Notatboken går gjennom verifisering i fire seksjoner. For å verifisere disse fiksturene
direkte uten å følge notatbokens forklaring:

```python
import json
from pathlib import Path

# Antar at du har fullført importene og hjelpefunksjonene
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

Fiksturene bruker samme kodevei som notatboken, med én fast signeringsnøkkel
og faste tidsstempel for byte-reproduserbarhet. For å regenerere:

```bash
python3 generate_fixtures.py
```

(Scriptet ligger i `generate_fixtures.py` i denne mappen.)

## Hva studentene lærer av å inspisere rå JSON

Å lese rå kvitteringsformat bygger opp intuisjon som cellene i notatboken
ikke alltid gir. Studenter som raskt skumer JSON-en merker ofte:

1. Signaturen er en ugjennomsiktig base64url-streng, men hvert annet felt er klar
   lesbar JSON. Signaturen krypterer ikke innholdet; den bevitner det.
2. `public_key` er innebygd i kvitteringen. En revisor trenger ingenting annet
   for å verifisere (forutsatt at nøkkelen faktisk tilhører den påståtte
   utstederen; se leksjonens README om identitetsinfrastruktur).
3. Å endre ett tegn i et hvilket som helst felt, og så sammenligne denne filen med
   `02_tampered_receipt.json`, gjør byte-nivå mekanismen konkret.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->