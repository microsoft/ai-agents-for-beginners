# Ukázkové fixture účtenek

Tři předvygenerované soubory účtenek k nahlédnutí bez spouštění notebooku.

| Soubor | Co to je |
|---|---|
| `01_valid_receipt.json` | Platná podepsaná účtenka pro volání nástroje `lookup_flights`. Ověření vrací True. |
| `02_tampered_receipt.json` | Stejná účtenka s jedním polem změněným po podpisu. Ověření vrací False. |
| `03_chain_three_receipts.json` | Řetězec tří platných účtenek (vyhledání, držení, rezervace) s `previous_receipt_hash` propojujícím každou s předchozí. |

Fixture přímo podepisují kanonické JCS bajty payloadu pomocí Ed25519.
SHA-256 zůstává v použití pro obsahové digesty a odkazy v řetězci účtenek, nikoli jako
dodatečný předhash před podpisem.

## Ověření vzorků

Notebook provádí ověření ve čtyřech částech. Chcete-li tyto fixture ověřit
přímo bez procházení vyprávění notebooku:

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

## Jak byly generovány

Fixture používají stejnou cestu kódu jako notebook, s jedním pevným podpisovým klíčem
a pevnými časovými značkami pro byte-reprodukčnost. Pro opětovné generování:

```bash
python3 generate_fixtures.py
```

(Skript je v `generate_fixtures.py` v tomto adresáři.)

## Co studenti získají prohlížením čistého JSON

Čtení surového formátu účtenky buduje intuici, kterou buňky v notebooku
ne vždy poskytují. Studenti, kteří si JSON projdou, často zaznamenají:

1. Podpis je neprůhledný base64url řetězec, ale každé jiné pole je obyčejný
   čitelný JSON. Podpis nešifruje obsah; stvrzuje ho.
2. `public_key` je vložen v účtence. Auditor nepotřebuje nic dalšího
   k ověření (s výhradou důvěry, že klíč skutečně patří deklarovanému
   vydavateli; viz README lekce o infrastruktuře identity).
3. Změna jediného znaku v libovolném poli a následné srovnání tohoto souboru s
   `02_tampered_receipt.json` činí mechanismus na úrovni bajtů konkrétním. 

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->