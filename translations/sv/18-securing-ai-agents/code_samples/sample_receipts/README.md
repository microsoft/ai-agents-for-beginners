# Exempelkvitto-fixtures

Tre förgenererade kvittofiler för inspektion utan att köra notebooken.

| Fil | Vad det är |
|---|---|
| `01_valid_receipt.json` | Ett giltigt signerat kvitto för ett verktygskall `lookup_flights`. Verifiering returnerar Sant. |
| `02_tampered_receipt.json` | Samma kvitto med ett fält ändrat efter signering. Verifiering returnerar Falskt. |
| `03_chain_three_receipts.json` | En kedja av tre giltiga kvitton (sök, håll, boka) med `previous_receipt_hash` som länkar varje till det föregående. |

## Verifiera exemplen

Notebooken går igenom verifiering i fyra avsnitt. För att verifiera dessa fixtures
direkt utan att köra genom notebook-berättelsen:

```python
import json
from pathlib import Path

# Antar att du har slutfört importerna och hjälpfunktionerna
# från avsnitten 1 och 2 i 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Sant

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Falskt

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Hur dessa genererades

Fixtures använder samma kodväg som notebooken, med en fast signeringsnyckel
och fasta tidsstämplar för byte-reproducerbarhet. För att regenerera:

```bash
python3 generate_fixtures.py
```

(Skriptet finns i `generate_fixtures.py` i denna katalog.)

## Vad studenter lär sig genom att inspektera rå JSON

Att läsa råa kvittotsformatet bygger upp en intuition som cellerna i notebooken
inte alltid ger. Studenter som skummar JSON märker ofta:

1. Signaturen är en ogenomskinlig base64url-sträng, men varje annat fält är vanlig
   läsbar JSON. Signaturen krypterar inte innehållet; den intygar det.
2. `public_key` är inbäddad i kvittot. En granskare behöver inget annat
   för att verifiera (med förutsättning att man litar på att nyckeln faktiskt tillhör den påstådda
   utfärdaren; se lektionens README om identitetsinfrastruktur).
3. Att ändra ett enda tecken i något fält, och sedan jämföra denna fil med
   `02_tampered_receipt.json`, gör mekanismen på byte-nivå konkret.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->