# Ukázkové příklady účtenek

Tři předgenerované soubory účtenek pro prohlížení bez spuštění notebooku.

| Soubor | Co to je |
|---|---|
| `01_valid_receipt.json` | Platná podepsaná účtenka pro volání nástroje `lookup_flights`. Ověření vrací True. |
| `02_tampered_receipt.json` | Ta samá účtenka s jedním polem změněným po podepsání. Ověření vrací False. |
| `03_chain_three_receipts.json` | Řetězec tří platných účtenek (hledat, držet, rezervovat), kde `previous_receipt_hash` spojuje každou s předchozí. |

Příklady přímo podepisují kanonické JCS bajty obsahu pomocí Ed25519.
SHA-256 se používá pro otisky obsahu a odkazy řetězců účtenek, ne jako
dodatečný před-hash před podpisem.

## Ověření ukázek

V `18-signed-receipts.ipynb` spusťte nejprve Setup a sekce 1 až 3.
Sekce 3 definuje `verify_chain`; samotné sekce 1 a 2 nestačí.
Poté spusťte následující blok v nové buňce s pracovní složkou notebooku
nastavenou na `18-securing-ai-agents/code_samples`. Cesty ke vzorům jsou relativní
k této složce.

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

### Kontrola příkladu bez Jupyteru

Z kořenového adresáře repozitáře nainstalujte závislosti lekce a spusťte:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Tyto testy spouštějí příklady v Pythonu v notebooku a přesný blok README
výše. Také kontrolují, že změny a nepřipnuté klíče jsou overovateli zamítnuty.
Testy přeskočí buňku `%pip` pro nastavení v notebooku, protože závislosti
jsou nainstalované samostatně. Notebook ani vzory nemění.

## Jak byly generovány

Vzory používají stejnou cestu kódu jako notebook, s jedním pevně daným podpisovým klíčem
a pevnými časovými značkami pro reprodukovatelnost bajtů. Pro regeneraci:

```bash
python3 generate_fixtures.py
```

(Skript je v `generate_fixtures.py` v tomto adresáři.)

## Co se studenti naučí z prohlížení surového JSONu

Čtení surového formátu účtenky buduje intuici, kterou buňky v notebooku
ne vždy poskytnou. Studenti, kteří JSON často prohlížejí, si všimnou:

1. Podpis je neprůhledný base64url řetězec, ale každé jiné pole je prostý
   čitelný JSON. Podpis nešifruje obsah; potvrzuje ho.
2. `public_key` je vložen v účtence, což stačí pro kontrolu
   vnitřní konzistence, ale ne důvěry v vystavovatele. Auditor musí porovnat s klíčem
   připnutým mimo účtenku nebo získaným přes důvěryhodný registr.
3. Změna jediného znaku v jakémkoli poli a následné opětovné porovnání souboru s
   `02_tampered_receipt.json` činí mechanismus na úrovni bajtů konkrétním.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->