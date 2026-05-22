# Näidisarvete konksud

Kolm eelnevalt genereeritud arve faili kontrollimiseks ilma märkmetega töökava läbita.

| Fail | Mis see on |
|---|---|
| `01_valid_receipt.json` | Kehtiv allkirjastatud arve `lookup_flights` tööriista kõne jaoks. Kontrollimine tagastab True. |
| `02_tampered_receipt.json` | Sama arve ühe välja muutmisega pärast allkirjastamist. Kontrollimine tagastab False. |
| `03_chain_three_receipts.json` | Kolme kehtiva arve ahel (otsing, reserveerimine, broneerimine), kus `previous_receipt_hash` lingib iga eelneva arvega. |

## Näidiste kontrollimine

Märkmik läbib kontrolli neljas jaotises. Nende konksude otsene kontroll ilma märkmetega töökava jutustust läbi tegemata:

```python
import json
from pathlib import Path

# Eeldab, et olete lõpetanud impordid ja abifunktsioonid
# alates 18-signed-receipts.ipynb 1. ja 2. osast.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Tõene

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Väär

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Kuidas need genereeriti

Konksud kasutavad sama koodirada kui märkmetega töökava, ühe fikseeritud allkirjastamisvõtmega
ja fikseeritud ajatemplitena baitide taasesitatavuse saavutamiseks. Taasgenereerimiseks:

```bash
python3 generate_fixtures.py
```

(Skript on selles kataloogis failis `generate_fixtures.py`.)

## Mida õpilased õpivad toores JSON-i uurides

Tooressarve vormingu lugemine loob tunnetuse, mida märkmiku lahtrid alati ei paku. Õpilased, kes JSON-i üle sirvivad, märkavad sageli:

1. Allkiri on opakne base64url string, kuid iga teine väli on selge ja loetav JSON. Allkiri ei krüpteeri sisu; see kinnitab seda.
2. `public_key` on arvel manustatud. Audiitoril pole vaja muud, et kontrollida (tingimusel, et võti kuulub tõepoolest väidetud väljastajale; vt õppetunni README identiteedi infrastruktuuri kohta).
3. Ühe tähemärgi muutmine lõppemiseks mis tahes väljas ning selle faili võrdlemine `02_tampered_receipt.json`-ga teeb baitide tasandi mehhanismi konkreetseks.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->