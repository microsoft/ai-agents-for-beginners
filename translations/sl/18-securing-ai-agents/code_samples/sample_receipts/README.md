# Primerne predloge prejemkov

Tri vnaprej ustvarjene datoteke prejemkov za pregled brez zagona beležnice.

| Datoteka | Kaj je |
|---|---|
| `01_valid_receipt.json` | Veljaven podpisan prejemek za klic orodja `lookup_flights`. Preverjanje vrne True. |
| `02_tampered_receipt.json` | Enak prejemek z enim poljem spremenjenim po podpisu. Preverjanje vrne False. |
| `03_chain_three_receipts.json` | Veriga treh veljavnih prejemkov (iskanje, rezervacija, potrdi) z `previous_receipt_hash`, ki povezuje vsak z prejšnjim. |

Predloge podpisujejo canonical JCS bajtne podatke obremenitve neposredno z Ed25519.
SHA-256 se še vedno uporablja za vsebinski digest in povezave verige prejemkov, ne kot
dodaten prej-hash pred podpisom.

## Preverjanje vzorcev

Beležnica vodi skozi preverjanje v štirih delih. Če želite neposredno preveriti te predloge
brez zagona pripovedi v beležnici:

```python
import json
from pathlib import Path

# Predpostavlja, da ste končali uvoze in pomožne funkcije
# iz razdelkov 1 in 2 datoteke 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Res

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Neresnica

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Kako so bili ustvarjeni

Predloge uporabljajo isto kodo kot beležnica, z enim fiksnim podpisnim ključem
in fiksnim časovnim žigom za ponovljivost bajtov. Za ponovno ustvarjanje:

```bash
python3 generate_fixtures.py
```

(Skript je v `generate_fixtures.py` v tej mapi.)

## Kaj se študentje naučijo z ogledom surovega JSON-a

Branje surovega formata prejemkov gradi intuicijo, ki je celice v beležnici
ne zagotavljajo vedno. Študentje, ki pregledajo JSON, pogosto opazijo:

1. Podpis je neprozoren niz base64url, a vsako drugo polje je jasno
   berljiv JSON. Podpis ne šifrira vsebine; potrjuje jo.
2. `public_key` je vgrajen v prejemek. Revident ne potrebuje ničesar drugega
   za preverjanje (ob predpostavki, da zaupa, da ključ dejansko pripada
   navedenemu izdajatelju; glej README lekcije o infrastrukturi identitete).
3. Spreminjanje enega znaka v katerem koli polju in nato primerjava te datoteke z
   `02_tampered_receipt.json` naredi mehanizem na ravni bajtov konkreten.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->