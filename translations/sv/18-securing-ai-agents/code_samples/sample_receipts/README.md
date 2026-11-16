# Exempelkvittofiler

Fyra förgenererade kvittofiler för inspektion utan att köra notebooken.

| Fil | Vad det är |
|---|---|
| `01_valid_receipt.json` | Ett giltigt signerat kvitto för ett `lookup_flights` verktygssamtal. Verifiering returnerar Sant. |
| `02_tampered_receipt.json` | Samma kvitto med ett fält ändrat efter signering. Verifiering returnerar Falskt. |
| `03_chain_three_receipts.json` | En kedja av tre giltiga kvitton (sök, håll, boka) med `previous_receipt_hash` som länkar varje till föregående. |
| `04_resigned_receipt.json` | Samma kvitto manipulerat och sedan omsignerat av en angripare, med angriparens egen publika nyckel inbäddad. Verifierar mot den nyckel som finns inuti. Fungerar inte mot utfärdarens nyckel. |

Filerna signerar lasten som kanoniska JCS-bytes direkt med Ed25519.
SHA-256 används fortfarande för innehålls-summer och kvittokedjelänkar, inte som en
extra förhash innan signering.

## Verifiera exemplen

I `18-signed-receipts.ipynb`, kör Setup och Sektionerna 1 till 3 först.
Sektion 3 definierar `verify_chain`; Sektion 1 och 2 räcker inte ensamma.
Kör sedan följande block i en ny cell, med notebookens arbetskatalog
satt till `18-securing-ai-agents/code_samples`. Filsökvägarna för exemplen är relativa
till den katalogen.

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

### Kontrollera exemplet utan Jupyter

Från repository-roten, installera lektionens beroenden och kör:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Dessa tester kör notebookens Python-exempel och exakt README-block
ovan. De kontrollerar också att manipulation och icke-fasta nycklar avvisas av
verifierarna. Tester hoppar över notebookens `%pip` setup-cell eftersom beroenden
installeras separat. De ändrar inte notebook eller filer.

## Hur dessa genererades

Exemplen använder samma kodväg som notebooken, med en fast signeringsnyckel
och fasta tidsstämplar för byte-reproducerbarhet. För att återskapa:

```bash
python3 generate_fixtures.py
```

(Skriptet finns på `generate_fixtures.py` i denna katalog.)

`../test_signed_receipts.py` kontrollerar allt detta automatiskt: den kör
notebookens kod, verifierar dessa fyra filer med notebookens
`verify_receipt` och `verify_chain`, och bekräftar att återskapande av
exemplen ger identiska bytes. Från `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Vad studenter lär sig av att inspektera rå JSON

Att läsa rå kvittoformat bygger upp intuition som cellerna i notebooken
inte alltid ger. Studenter som skummar JSON märker ofta:

1. Signaturen är en ogenomskinlig base64url-sträng, men varje annat fält är vanlig
   läsbar JSON. Signaturen krypterar inte innehållet; den intygar det.
2. `public_key` är inbäddad i kvittot, vilket gör filen
   självförsörjande men är inte vad en granskare verifierar mot. Jämför
   `02_tampered_receipt.json` med `04_resigned_receipt.json`: båda ändrades
   efter signering, men det andra signerades om med angriparens
   egen nyckel, så den verifierar mot den nyckel den bär. Den inbäddade nyckeln
   visar att filen är internt konsekvent. Endast en nyckel erhållen
   någon annanstans visar vem som utfärdade den.
3. Att ändra ett enda tecken i något fält utanför `signature`, sedan
   jämföra denna fil med `02_tampered_receipt.json` gör
   bytesnivåmekanismen konkret.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->