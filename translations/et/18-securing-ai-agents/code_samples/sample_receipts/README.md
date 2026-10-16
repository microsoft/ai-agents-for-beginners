# Näidistšeki seadistused

Kolm eelnevalt genereeritud tšekifaili kontrollimiseks ilma märkmikku käivitamata.

| Fail | Mis see on |
|---|---|
| `01_valid_receipt.json` | Kehtiv allkirjastatud tšekk tööriistakutse `lookup_flights` jaoks. Kontroll tagastab True. |
| `02_tampered_receipt.json` | Sama tšekk koos ühe välja muutmisega pärast allkirjastamist. Kontroll tagastab False. |
| `03_chain_three_receipts.json` | Kolme kehtiva tšeki ahel (otsing, hoidmine, broneerimine) koos `previous_receipt_hash`-iga, mis seob iga eelnevaga. |

Seadistused allkirjastavad otse kasutahtlikud JCS baitide ahelad Ed25519-ga.
SHA-256 jääb kasutusele sisu räsina ja tšekiahela linkide jaoks, mitte kui
täiendav eelhõive enne allkirjastamist.

## Näidiste kontrollimine

Märkmik juhib läbi kontrolli neljas osas. Nende seadistuste otseseks kontrollimiseks
ilma märkmiku narratiivi läbimata:

```python
import json
from pathlib import Path

# Eeldab, et olete lõpetanud importide ja abifunktsioonide kirjutamise
# 18-signed-receipts.ipynb faili 1. ja 2. jaotise alusel.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Õige

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Vale

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Kuidas need genereeriti

Seadistused kasutavad sama koodirada mis märkmik, kus on üks fikseeritud allkirjastamisvõti
ja fikseeritud ajatempleid baitide reprodutseeritavuse jaoks. Taasloomiseks:

```bash
python3 generate_fixtures.py
```

(Skript on selles kataloogis failis `generate_fixtures.py`.)

## Mida õpilased õpivad toore JSON-i uurimisel

Toore tšeki formaadi lugemine loob intuitsiooni, mida märkmiku lahtrid
alati ei paku. Õpilased, kes JSON-i sirvivad, märkavad tihti:

1. Allkiri on opaakne base64url string, kuid kõik teised väljad on lihtsad
   loetavad JSON-id. Allkiri ei krüpteeri sisu; see kinnitab seda.
2. `public_key` on tšekis sees. Auditi läbiviija ei vaja telefonimulli
   muu kui kindlustuse selle kohta, et võti kuulub tõepoolest väidetud
   väljastajale; vt õppetunni README identiteedistruktuuri kohta).
3. Iga välja üksiku tähe muutmine ja seejärel selle faili võrdlemine
   failiga `02_tampered_receipt.json` teeb baitide taseme mehhanismi konkreetseks.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->