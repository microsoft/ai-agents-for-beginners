# Ukážkové súbory dokladov

Tri vopred vygenerované súbory dokladov na kontrolu bez spustenia notebooku.

| Súbor | Čo to je |
|---|---|
| `01_valid_receipt.json` | Platný podpísaný doklad pre volanie nástroja `lookup_flights`. Overenie vráti True. |
| `02_tampered_receipt.json` | Ten istý doklad s jedným po podpise zmeneným poľom. Overenie vráti False. |
| `03_chain_three_receipts.json` | Reťaz troch platných dokladov (search, hold, book) s `previous_receipt_hash` prepojujúcim každý s predchádzajúcim. |

Súbory priamo podpisujú kanonické JCS bajty nákladu pomocou Ed25519.
SHA-256 sa stále používa pre hašovanie obsahu a prepojenia v reťazci dokladov, nie ako
dodatočný pred-hash pred podpisom.

## Overenie vzoriek

V `18-signed-receipts.ipynb` najskôr spustite Setup a Sekcie 1 až 3.
Sekcia 3 definuje `verify_chain`; Sekcie 1 a 2 samé o sebe nie sú dostatočné.
Potom spustite nasledujúci blok v novej bunke, pričom pracovný adresár notebooku
nastavte na `18-securing-ai-agents/code_samples`. Cesty k súborom nižšie sú relatívne
k tomuto adresáru.

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

### Kontrola príkladu bez Jupyteru

Z koreňa repozitára nainštalujte závislosti lekcie a spustite:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Tieto testy vykonajú Python príklady z notebooku a presný blok README
vyššie. Tiež overujú, že manipulácie a nepřipnuté kľúče sú overovacími nástrojmi zamietnuté.
Testy vynechávajú setup bunku `%pip` notebooku, pretože závislosti sú
inštalované samostatne. Notebook ani vzorové súbory nemenia.

## Ako boli tieto súbory vytvorené

Súbory používajú rovnakú cestu kódu ako notebook, s jedným fixným podpisovým kľúčom
a fixnými časovými značkami pre bitovú reprodukovateľnosť. Na opätovné vytvorenie:

```bash
python3 generate_fixtures.py
```

(Skript je v `generate_fixtures.py` v tomto adresári.)

## Čo sa študenti naučia pri skúmaní surového JSON

Čítanie surového formátu dokladu buduje intuíciu, ktorú bunky v notebooku
nie vždy poskytujú. Študenti, ktorí preletia JSON, si často všimnú:

1. Podpis je nečitateľný reťazec v base64url, ale každý iný prvok je obyčajný
   čitateľný JSON. Podpis nešifruje obsah; potvrdzuje ho.
2. `public_key` je vložené v doklade, čo stačí na overenie
   vnútornú konzistenciu, ale nie dôveru vydavateľa. Auditor ho musí
   porovnať s kľúčom pripevneným mimo dokladu alebo vyriešeným cez dôveryhodný register.
3. Zmena jediného znaku v ľubovoľnom poli a následné porovnanie tohto súboru
   s `02_tampered_receipt.json` robí mechanizmus na úrovni bajtov konkrétnym.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->