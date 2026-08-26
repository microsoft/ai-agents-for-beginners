# Näidistõendite mallid

Kolm eelnevalt genereeritud tšeki faili kontrollimiseks ilma märkmiku käivitamiseta.

| Fail | Mis see on |
|---|---|
| `01_valid_receipt.json` | Kehtiv allkirjastatud tšekk `lookup_flights` tööriista kõne jaoks. Kontroll annab True. |
| `02_tampered_receipt.json` | Sama tšekk, mille üks väli on pärast allkirjastamist muudetud. Kontroll annab False. |
| `03_chain_three_receipts.json` | Kolme kehtiva tšeki (otsing, broneerimine, kinnitamine) ahel koos `previous_receipt_hash`-ga, mis lingib igaühe eelnenuga. |

Mallid allkirjastavad otse Ed25519-ga koormuse kanonilised JCS-baidid.
SHA-256 jääb kasutusele sisu digesti ja tšeki ahela linkide jaoks, mitte lisaks
enne allkirjastamist eelhäälestamiseks.

## Näidete kontrollimine

Märkmik tutvustab kontrolli neljas osas. Kui soovite neid malle kontrollida
otse ilma märmiku narratiivis käimata:

```python
import json
from pathlib import Path

# Eeldab, et olete lõpetanud impordid ja abifunktsioonid
# failidest 1 ja 2 18-signed-receipts.ipynb-st.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Tõene

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Väär

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Kuidas need genereeriti

Mallid kasutavad sama koodi rada mis märkmik, ühe fikseeritud allkirjastamisvõtme
ja fikseeritud ajatemplitena baitide taastekitatavuse jaoks. Taastekitamiseks:

```bash
python3 generate_fixtures.py
```

(Skript asub selles kataloogis `generate_fixtures.py` failis.)

## Mida õpilased õpivad JSON-i lugemise käigus

Tšeki puhta vormingu lugemine loob intuitsiooni, mida märkmiku lahtrid alati ei anna.
Õpilased, kes JSON-i silmad mööda lasevad, märkavad sageli:

1. Allkiri on läbipaistev base64url-string, kuid iga teine väli on tavaline
   loetav JSON. Allkiri ei krüpteeri sisu; see kinnitab seda.
2. `public_key` on tšeki sees. Audiitoril ei ole kontrolliks muud tarvis
   (tingimusel, et usaldab, et võti kuulub tõepoolest väidetud
   väljastajale; vt oppematerjalidega README-d identiteedi infrastruktuuri kohta).
3. Ühe märgi muutmine ükskõik millises väljas ja seejärel selle faili
   võrdlemine `02_tampered_receipt.json` failiga teeb baitidel põhineva mehhanismi konkreetseks.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->