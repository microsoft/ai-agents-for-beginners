# Ukázkové příklady účtenek

Tři předgenerované soubory účtenek k nahlédnutí bez spuštění notebooku.

| Soubor | Co to je |
|---|---|
| `01_valid_receipt.json` | Platná podepsaná účtenka pro volání nástroje `lookup_flights`. Ověření vrací True. |
| `02_tampered_receipt.json` | Ta samá účtenka s jedním polem pozměněným po podpisu. Ověření vrací False. |
| `03_chain_three_receipts.json` | Řetězec tří platných účtenek (vyhledání, rezervace, potvrzení) s `previous_receipt_hash` propojujícím každou s předchozí. |

## Ověření vzorků

Notebook prochází ověřování ve čtyřech sekcích. K ověření těchto vzorků přímo bez procházení textu notebooku:

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

## Jak byly tyto vytvořeny

Vzorky používají stejnou cestu kódu jako notebook, s jedním pevným klíčem pro podpis
a pevnými časovými razítky kvůli reprodukovatelnosti na úrovni bytů. K opětovnému vygenerování:

```bash
python3 generate_fixtures.py
```

(Skript je v souboru `generate_fixtures.py` v tomto adresáři.)

## Co se studenti naučí prohlížením surového JSONu

Čtení surového formátu účtenky buduje intuitivní pochopení, které buňky v notebooku
nezaručeně neposkytují. Studenti, kteří prohlíží JSON, často zaznamenají:

1. Podpis je neprůhledný base64url řetězec, ale každé jiné pole je běžný čitelný JSON. Podpis nešifruje obsah; potvrzuje jej.
2. `public_key` je vložen v účtence. Auditor nepotřebuje nic dalšího
   k ověření (s výhradou důvěry, že klíč skutečně patří nárokovanému
   vydavateli; viz lekce README o infrastruktuře identity).
3. Úprava jediného znaku v jakémkoli poli a následné porovnání tohoto souboru s
   `02_tampered_receipt.json` přibližuje mechanismus na úrovni bytů.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->