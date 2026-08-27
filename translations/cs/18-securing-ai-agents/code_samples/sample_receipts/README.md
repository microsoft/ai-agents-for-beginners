# Ukázkové soubory účtenek

Tři předgenerované soubory účtenek k nahlédnutí bez spuštění notebooku.

| Soubor | Co to je |
|---|---|
| `01_valid_receipt.json` | Platná podepsaná účtenka pro volání nástroje `lookup_flights`. Ověření vrací True. |
| `02_tampered_receipt.json` | Stejná účtenka s jedním po podpisu změněným polem. Ověření vrací False. |
| `03_chain_three_receipts.json` | Řetězec tří platných účtenek (vyhledávání, rezervace, potvrzení) s `previous_receipt_hash` propojujícím každou s předchozí. |

Tyto soubory podepisují přímo kanonické bajty JCS v datech pomocí Ed25519.
SHA-256 se stále používá pro obsahové digesty a odkazy v řetězci účtenek, nikoli jako
dodatečný před-hash před podpisem.

## Ověření ukázek

Notebook provází ověřovacím procesem ve čtyřech sekcích. Pro ověření těchto souborů
přímo, bez spuštění vyprávění v notebooku:

```python
import json
from pathlib import Path

# Předpokládá se, že jste dokončili importy a pomocné funkce
# z částí 1 a 2 souboru 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Pravda

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Nepravda

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Jak byly tyto soubory vytvořeny

Tyto soubory používají stejnou cestu v kódu jako notebook, s jedním pevným podpisovým klíčem
a pevnými časovými razítky pro obnovitelnost bajtů. Pro regeneraci:

```bash
python3 generate_fixtures.py
```

(Skript je v `generate_fixtures.py` v tomto adresáři.)

## Co se studenti naučí při prohlížení surového JSON

Čtení surového formátu účtenky buduje intuici, kterou buňky v notebooku
ne vždy poskytnou. Studenti, kteří rychle prohlíží JSON, často poznamenají:

1. Podpis je neprůhledný řetězec base64url, ale každé jiné pole je čistý,
   čitelný JSON. Podpis nešifruje obsah; pouze ho potvrzuje.
2. `public_key` je v účtence vložen. Auditor nepotřebuje nic dalšího,
   aby ověřil (za předpokladu důvěry, že klíč skutečně patří uváděnému
   vydavateli; viz README lekce o identitní infrastruktuře).
3. Úprava jediného znaku jakéhokoli pole a následné porovnání s
   `02_tampered_receipt.json` činí konkrétním mechanismus na úrovni bajtů.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->