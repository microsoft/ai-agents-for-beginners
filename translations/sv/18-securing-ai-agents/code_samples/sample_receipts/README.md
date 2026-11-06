# Exempel på kvitto-fixtures

Tre förgenererade kvittofiler för inspektion utan att köra notebooken.

| Fil | Vad det är |
|---|---|
| `01_valid_receipt.json` | Ett giltigt signerat kvitto för ett `lookup_flights` verktygsanrop. Verifiering returnerar True. |
| `02_tampered_receipt.json` | Samma kvitto med ett fält ändrat efter signering. Verifiering returnerar False. |
| `03_chain_three_receipts.json` | En kedja av tre giltiga kvitton (search, hold, book) med `previous_receipt_hash` som länkar varje till det föregående. |

Fixtures signerar nyttolastens kanoniska JCS-bytes direkt med Ed25519.
SHA-256 används fortfarande för innehålls-digest och kvittokedjelänkar, inte som en
extra för-hash före signering.

## Verifiering av exemplen

I `18-signed-receipts.ipynb`, kör Setup och avsnitten 1 till 3 först.
Avsnitt 3 definierar `verify_chain`; avsnitt 1 och 2 ensam räcker inte.
Kör sedan följande block i en ny cell, med notebookens arbetskatalog
satt till `18-securing-ai-agents/code_samples`. Fixture-sökvägarna nedan är relativa
till den katalogen.

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

### Kontroll av exemplet utan Jupyter

Från repositorys rotnivå, installera lektionens beroenden och kör:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Dessa tester kör notebookens Python-exempel och det exakta README-blocket
ovan. De kontrollerar också att manipulation och icke-pinnade nycklar avvisas av
verifierarna. Tester hoppar över notebookens `%pip` setup-cell eftersom beroenden
installeras separat. De ändrar inte notebooken eller fixtures.

## Hur dessa genererades

Fixtures använder samma kodväg som notebooken, med en fast signeringsnyckel
och fasta tidsstämplar för byte-reproducerbarhet. För att återgenerera:

```bash
python3 generate_fixtures.py
```

(Script finns på `generate_fixtures.py` i denna katalog.)

## Vad studenter lär sig av att inspektera rå JSON

Att läsa råkvittots format bygger upp intuition som cellerna i notebooken
inte alltid ger. Studenter som snabbt skummar JSON märker ofta:

1. Signaturen är en ogenomskinlig base64url-sträng, men varje annat fält är ren
   läsbar JSON. Signaturen krypterar inte innehållet; den intygar det.
2. `public_key` är inbäddat i kvittot, vilket räcker för att kontrollera
   självkonsistens men inte utfärdarens förtroende. En revisor måste jämföra det med en nyckel
   pinnad utanför kvittot eller löst via ett betrott register.
3. Att ändra ett enda tecken i något fält, och sedan jämföra denna fil med
   `02_tampered_receipt.json` gör byte-nivå mekanismen konkret.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->