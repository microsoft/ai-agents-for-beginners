# Vzorčni prejemniki

Tri vnaprej ustvarjene datoteke s prejemniki za pregled brez zagona zvezka.

| Datoteka | Kaj je to |
|---|---|
| `01_valid_receipt.json` | Veljaven podpisan prejemnik za klic orodja `lookup_flights`. Preverjanje vrne True. |
| `02_tampered_receipt.json` | Enak prejemnik z enim spremenjenim poljem po podpisu. Preverjanje vrne False. |
| `03_chain_three_receipts.json` | Veriga treh veljavnih prejemnikov (iskanje, rezervacija, potrdi) s `previous_receipt_hash`, ki vsak povezuje s predhodnim. |

## Preverjanje vzorcev

Zvezek vodi skozi preverjanje v štirih delih. Če želite te vnaprej ustvarjene datoteke preveriti neposredno brez zagona zgodbe v zvezku:

```python
import json
from pathlib import Path

# Predpostavlja, da ste zaključili uvoze in pomožne funkcije
# iz odsekov 1 in 2 datoteke 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Resnično

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Neresnično

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Kako so bili ustvarjeni

Vzorce ustvarja enaka koda kot zvezek, z eno fiksno podpisno ključno
in fiksnimi časovnimi žigi za enako ponovljivost bajtov. Za ponovno ustvarjanje:

```bash
python3 generate_fixtures.py
```

(Skripta je v `generate_fixtures.py` v tem imeniku.)

## Kaj se študenti naučijo s pregledovanjem surove JSON

Branje surove oblike prejemnika gradi intuicijo, ki je celice v zvezku
ne nudijo vedno. Študentje, ki hitro pregledajo JSON, pogosto opazijo:

1. Podpis je neprozoren niz base64url, vendar je vsak drug podatek v preprostem
   berljivem JSON formatu. Podpis ne šifrira vsebine; potrjuje jo.
2. `public_key` je vključen v prejemniku. Revizor ne potrebuje ničesar drugega
   za preverjanje (ob predpostavki zaupanja, da ključ dejansko pripada trditvenemu
   izdajatelju; glej README lekcije o identitetni infrastrukturi).
3. Sprememba enega znaka v katerem koli polju in nato primerjava te datoteke z
   `02_tampered_receipt.json` naredi mehanizem na nivoju bajtov otipljiv.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->