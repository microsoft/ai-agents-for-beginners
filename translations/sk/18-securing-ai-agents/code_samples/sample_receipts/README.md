# Ukážkové príklady príjmov

Tri predgenerované súbory príjmov na kontrolu bez spustenia notebooku.

| Súbor | Čo to je |
|---|---|
| `01_valid_receipt.json` | Platný podpísaný príjem pre volanie nástroja `lookup_flights`. Overenie vráti True. |
| `02_tampered_receipt.json` | Ten istý príjem s jedným poľa zmeneným po podpise. Overenie vráti False. |
| `03_chain_three_receipts.json` | Reťaz troch platných príjmov (vyhľadávanie, držanie, rezervácia) s `previous_receipt_hash` spájajúcim každý s predchádzajúcim. |

Príklady priamo podpisujú kanonické bajty JCS zaťaženia pomocou Ed25519.
Šifrovací algoritmus SHA-256 sa naďalej používa na obsahové digesty a prepojenia v reťazci príjmov, nie ako 
extra pred-hash pred podpisom.

## Overovanie príkladov

Notebook vedie overovanie v štyroch sekciách. Na priamu kontrolu týchto príkladov 
bez spustenia vyučovacej časti notebooku:

```python
import json
from pathlib import Path

# Predpokladá sa, že ste dokončili importy a pomocné funkcie
# zo sekcií 1 a 2 súboru 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Pravda

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Nepravda

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Ako boli tieto vygenerované

Príklady používajú tú istú cestu kódu ako notebook, s jedným fixným podpisovým kľúčom 
a fixnými časovými pečiatkami pre byte-reprodukovateľnosť. Na opätovné vygenerovanie:

```bash
python3 generate_fixtures.py
```

(Skript je v súbore `generate_fixtures.py` v tomto adresári.)

## Čo sa študenti naučia z kontroly surového JSON

Čítanie surového formátu príjmu buduje intuíciu, ktorú bunky v notebooku 
často neposkytujú. Študenti, ktorí preletia JSON, si často všimnú:

1. Podpis je nepriehľadný reťazec base64url, ale každé iné pole je obyčajný 
   čitateľný JSON. Podpis nešifruje obsah; len ho potvrdzuje.
2. `public_key` je vložený v príjme. Auditor nepotrebuje nič iné na overenie 
   (za predpokladu, že dôveruje, že kľúč naozaj patrí deklarovanému 
   vydavateľovi; pozri README lekcie o infraštruktúre identity).
3. Zmena jediného znaku v ľubovoľnom poli a následné porovnanie tohto súboru 
   so súborom `02_tampered_receipt.json` konkretizuje mechanizmus na úrovni bajtov.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->