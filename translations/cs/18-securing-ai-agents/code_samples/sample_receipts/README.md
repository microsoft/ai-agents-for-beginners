# Ukázkové příklady účtenek

Čtyři předgenerované soubory účtenek pro kontrolu bez spouštění notebooku.

| Soubor | Co to je |
|---|---|
| `01_valid_receipt.json` | Platná podepsaná účtenka pro volání nástroje `lookup_flights`. Ověření vrací True. |
| `02_tampered_receipt.json` | Ta samá účtenka s jedním polem změněným po podepsání. Ověření vrací False. |
| `03_chain_three_receipts.json` | Řetězec tří platných účtenek (vyhledávání, držení, rezervace) s `previous_receipt_hash` propojujícím každou s předchozím. |
| `04_resigned_receipt.json` | Ta samá účtenka pozměněná a následně znovu podepsaná útočníkem s vloženým veřejným klíčem útočníka. Ověřuje se podle klíče v ní. Na klíč vydavatele selhává. |

Příklady podepisují kánonické bajty JCS přenosu přímo pomocí Ed25519.
Pro obsahové digesty a odkazy v řetězci účtenek se nadále používá SHA-256,
nikoli však jako dodatečný před-hash před podepsáním.

## Ověření příkladů

V `18-signed-receipts.ipynb` spusťte nejdříve Nastavení a sekce 1 až 3.
Sekce 3 definuje `verify_chain`; samotné sekce 1 a 2 nestačí.
Poté spusťte následující blok v nové buňce s pracovním adresářem notebooku
nastaveným na `18-securing-ai-agents/code_samples`. Níže uvedené cesty k příkladům jsou relativní
vůči tomuto adresáři.

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

### Kontrola příkladu bez Jupyteru

Z kořenového adresáře repozitáře nainstalujte závislosti lekce a spusťte:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Tyto testy spouštějí ukázky Pythonu z notebooku a přesný blok z README výše.
Také kontrolují, že pozměnění a nepřipnuté klíče jsou ověřovači zamítnuty.
Testy vynechávají buňku s nastavením `%pip` notebooku, protože závislosti
se instalují samostatně. Notebook ani příklady nemění.

## Jak byly tyto příklady vytvořeny

Příklady používají stejnou cestu kódu jako notebook, se jedním pevně daným podepisovacím klíčem
a pevnými časovými razítky pro bajtovou reprodukovatelnost. Pro regeneraci:

```bash
python3 generate_fixtures.py
```

(Skript je v `generate_fixtures.py` v tomto adresáři.)

`../test_signed_receipts.py` toto vše automaticky kontroluje: spouští kód
notebooku, ověřuje těchto čtyři příkladů pomocí notebookových
`verify_receipt` a `verify_chain`, a potvrzuje, že regenerace
příkladů dává identické bajty. Z `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Co se studenti naučí při zkoumání surového JSON

Čtení surového formátu účtenky buduje intuici, kterou buňky v notebooku
nemusí vždy poskytnout. Studenti, kteří prohlížejí JSON, často zaznamenají:

1. Podpis je nečitelný řetězec base64url, ale všechna ostatní pole jsou jasně
   čitelný JSON. Podpis nešifruje obsah; potvrzuje ho.
2. `public_key` je vložen v účtence, což činí soubor
   samostatným, ale zároveň není tím, vůči čemu auditor ověřuje. Porovnejte
   `02_tampered_receipt.json` a `04_resigned_receipt.json`: oba byly
   po podepsání pozměněny, ale druhý byl znovu podepsán útočníkovým
   vlastním klíčem, takže se ověřuje vůči klíči, který obsahuje. Vložený klíč
   vám říká, že soubor je interně konzistentní. Pouze klíč získaný
   jinde vám řekne, kdo ho vydal.
3. Změna jediného znaku v jakémkoli poli mimo `signature`, a poté
   opětovné porovnání tohoto souboru s `02_tampered_receipt.json`, činí
   mechanismus na úrovni bajtů konkrétním.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->