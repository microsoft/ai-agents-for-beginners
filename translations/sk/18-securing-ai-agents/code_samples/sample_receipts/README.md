# Príklady účteniek

Štyri predvytvorené súbory účteniek na kontrolu bez spustenia notebooku.

| Súbor | Čo to je |
|---|---|
| `01_valid_receipt.json` | Platná podpísaná účtenka pre volanie nástroja `lookup_flights`. Overenie vráti True. |
| `02_tampered_receipt.json` | Tá istá účtenka s jedným poľa upraveným po podpise. Overenie vráti False. |
| `03_chain_three_receipts.json` | Reťaz troch platných účteniek (search, hold, book) s `previous_receipt_hash` spájajúcim každú s predchádzajúcou. |
| `04_resigned_receipt.json` | Tá istá účtenka pozmenená a potom opätovne podpísaná útočníkom, s vloženým vlastným verejným kľúčom útočníka. Overuje sa voči kľúču v nej obsiahnutom. Nezlyháva voči kľúču vydavateľa. |

Tento príklad priamo podpisuje kanonické JCS bajty zaťaženia pomocou Ed25519.
SHA-256 sa naďalej používa pre obsahové digesty a odkazy v reťazci účteniek, nie ako
extra pred-hash pred podpisom.

## Overenie príkladov

V `18-signed-receipts.ipynb` najprv spustite Setup a sekcie 1 až 3.
Sekcia 3 definuje `verify_chain`; samotné sekcie 1 a 2 nestačia.
Potom spustite nasledujúci blok v novej bunke, pričom pracovný adresár notebooku
nastavte na `18-securing-ai-agents/code_samples`. Cesty k príkladom nižšie sú relatívne
k tomuto adresáru.

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

### Kontrola príkladu bez Jupyteru

Z koreňového adresára repozitára nainštalujte závislosti lekcie a spustite:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Tieto testy spúšťajú Python príklady z notebooku a presne ten blok README
vyššie. Tiež kontrolujú, že pozmenené údaje a nepovolené kľúče sú z odmietnuté
overovačmi. Testy preskakujú setup bunku `%pip` v notebooku, pretože závislosti
sú nainštalované samostatne. Nezmenia notebook ani príklady.

## Ako boli vygenerované

Príklady používajú rovnakú cestu kódu ako notebook, s jedným pevným podpisovacím kľúčom
a pevným časovým pečiatkam pre reprodukovateľnosť na úrovni bajtov. Na regeneráciu:

```bash
python3 generate_fixtures.py
```

(Skript je v `generate_fixtures.py` v tomto adresári.)

`../test_signed_receipts.py` to všetko automaticky kontroluje: spúšťa kód notebooku,
overuje tieto štyri príklady pomocou notebookových
`verify_receipt` a `verify_chain` a potvrdzuje, že regenerovaním
príkladov vzniknú totožné bajty. Z `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Čo sa študenti naučia z kontroly surového JSON

Čítanie surového formátu účtenky buduje intuíciu, ktorú bunky v notebooku
nie vždy poskytnú. Študenti, ktorí preorderujú JSON, často vycítia:

1. Podpis je nepriehľadný base64url reťazec, ale každé iné pole je obyčajný
   čitateľný JSON. Podpis nešifruje obsah; potvrdzuje ho.
2. `public_key` je vložený v účtenke, čo robí súbor
   kompletným, ale nie je to, proti čomu auditor overuje. Porovnajte
   `02_tampered_receipt.json` s `04_resigned_receipt.json`: obidva boli
   pozmenené po podpise, ale druhý bol opätovne podpísaný s útočníkovým
   vlastným kľúčom, takže sa overuje pomocou kľúča, ktorý nesie. Vložený kľúč
   hovorí, že súbor je interne konzistentný. Iba kľúč získaný
   inde umožňuje identifikovať vydavateľa.
3. Úprava jedného znaku v ľubovoľnom poli mimo `signature`, a potom
   opätovné porovnanie tohto súboru s `02_tampered_receipt.json`,
   konkretizuje mechanizmus na úrovni bajtov.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->