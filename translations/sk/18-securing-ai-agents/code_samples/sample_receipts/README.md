# Ukážkové fixtures príjmov

Tri predvygenerované súbory príjmov na kontrolu bez spustenia notebooku.

| Súbor | Čo to je |
|---|---|
| `01_valid_receipt.json` | Platný podpísaný príjem pre volanie nástroja `lookup_flights`. Overenie vracia True. |
| `02_tampered_receipt.json` | Ten istý príjem s jedným po podpise zmeneným poľom. Overenie vracia False. |
| `03_chain_three_receipts.json` | Reťazec troch platných príjmov (vyhľadávanie, držanie, rezervovanie) s `previous_receipt_hash`, ktorý každý spája s predchádzajúcim. |

## Overenie ukážok

Notebook prechádza overením v štyroch častiach. Ak chcete overiť tieto fixtures
priamo bez prechádzania cez text notebooku:

```python
import json
from pathlib import Path

# Predpokladá sa, že ste dokončili importy a pomocné funkcie
# z častí 1 a 2 súboru 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Pravda

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Nepravda

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Ako boli tieto vygenerované

Fixtures používajú rovnakú cestu kódu ako notebook, s jedným pevne daným kľúčom na podpisovanie
a fixnými časovými značkami pre bitovo reprodukovateľný výsledok. Pre regenerovanie:

```bash
python3 generate_fixtures.py
```

(Skript je v `generate_fixtures.py` v tomto adresári.)

## Čo sa študenti naučia z kontroly surového JSONu

Čítanie surového formátu príjmu buduje intuíciu, ktorú bunky v notebooku
nie vždy zabezpečujú. Študenti, ktorí si ľahko prehliadnu JSON, často všimnú:

1. Podpis je nepriehľadný base64url reťazec, ale každé iné pole je obyčajný
   čitateľný JSON. Podpis nešifruje obsah; potvrdzuje ho.
2. `public_key` je vložený v príjme. Auditujúci nepotrebuje nič iné
   na overenie (s výhradou dôvery, že kľúč skutočne patrí tvrdenému
   vystavovateľovi; pozri lekciu v README o identitnej infraštruktúre).
3. Zmena jediného znaku v ktoromkoľvek poli, a následné porovnanie tohto súboru s
   `02_tampered_receipt.json`, robí mechanizmus na úrovni bajtov konkrétnym.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->