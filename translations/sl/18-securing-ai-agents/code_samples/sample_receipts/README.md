# Vzorčne datoteke potrdil

Tri vnaprej ustvarjene datoteke potrdil za pregled brez zagona zvezka.

| Datoteka | Kaj je |
|---|---|
| `01_valid_receipt.json` | Veljavno podpisano potrdilo za klic orodja `lookup_flights`. Preverjanje vrne True. |
| `02_tampered_receipt.json` | Enako potrdilo s spremenjeno eno polje po podpisu. Preverjanje vrne False. |
| `03_chain_three_receipts.json` | Veriga treh veljavnih potrdil (iskanje, rezerviranje, potrjevanje) z `previous_receipt_hash`, ki povezuje vsak s prejšnjim. |

Vzorci neposredno podpisujejo canonical JCS bajte vsebine z Ed25519.
SHA-256 se še vedno uporablja za izvlečke vsebine in zveze v verigi potrdil, ne kot
dodaten pre-izvleček pred podpisom.

## Preverjanje vzorcev

Zvezek vodi skozi preverjanje v štirih poglavjih. Za neposredno preverjanje teh vzorcev
brez zagona zvezka:

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

Vzorci uporabljajo enako kodo kot zvezek, z enim fiksnim podpisnim ključem
in fiksnimi časovnimi žigi za ponovljivost bajtov. Za ustvarjanje:

```bash
python3 generate_fixtures.py
```

(Skripta je v `generate_fixtures.py` v tem imeniku.)

## Kaj se študentje naučijo z ogledom surovega JSON-a

Branje surovega formata potrdil gradi intuicijo, ki jo celice zvezka
včasih ne nudijo. Študentje, ki pobrskajo po JSON-u, pogosto opazijo:

1. Podpis je neprozoren niz base64url, toda vsako drugo polje je preprost
   berljiv JSON. Podpis ne šifrira vsebine; le potrjuje njeno pristnost.
2. `public_key` je vgrajen v potrdilo. Revizor ne potrebuje ničesar drugega
   za preverjanje (pogonjen le s predpostavko, da ključ dejansko pripada trditvi
   izdajatelja; glej README lekcije o identitetni infrastrukturi).
3. Sprememba enega samega znaka poljubnega polja in nato primerjava te datoteke z
   `02_tampered_receipt.json` naredi mehanizem na ravni bajtov bolj otipljiv.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->