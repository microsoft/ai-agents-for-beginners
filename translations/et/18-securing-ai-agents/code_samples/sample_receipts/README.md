# Näidisarvete fikstuurid

Neli eelnevalt genereeritud arvefaili, mida saab uurida ilma märkmikku käivitamata.

| Fail | Mis see on |
|---|---|
| `01_valid_receipt.json` | Kehtiv allkirjastatud arve `lookup_flights` tööriista kutse jaoks. Kontroll tagastab True. |
| `02_tampered_receipt.json` | Sama arve, mille ühte välja on pärast allkirjastamist muudetud. Kontroll tagastab False. |
| `03_chain_three_receipts.json` | Kolme kehtiva arve ahel (otsi, hoia, broneeri), kus igaüks on eelnevaga seotud `previous_receipt_hash` abil. |
| `04_resigned_receipt.json` | Sama arve on rikutud ja seejärel ründaja poolt uuesti allkirjastatud, millel on ründaja enda avalik võti manustatud. Kontrollib selle sees oleva võtmega. Ebaõnnestub väljaandja võtme vastu. |

Fikstuurid allkirjastavad kandeotstarbelised kanonilised JCS-baidid otse Ed25519-ga.
SHA-256 jääb kasutusse sisusegmentide ja arve-ahelate linkide jaoks, mitte
täiendava eel-tiheduse jaoks enne allkirjastamist.

## Näidiste kontrollimine

Käivitage `18-signed-receipts.ipynb` juures esmalt Setup ja sektsioonid 1 kuni 3.
Sektsioon 3 määratleb `verify_chain`; üksnes sektsioonid 1 ja 2 ei ole piisavad.
Seejärel käivitage järgmine plokk uues lahtris, kasutades sülearvuti töökaustana
`18-securing-ai-agents/code_samples`. Allpool olevad fikstuuride teed on suhtelised
selle kataloogi suhtes.

```python
import json
from pathlib import Path

fixture_dir = Path("sample_receipts")

# The issuer's key, pinned here rather than read from any receipt. In a real
# deployment it comes from the issuer's JWK Set or a pinned config value.
# This is the public half of the fixed signing key in generate_fixtures.py.
ISSUER_KEY = "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo"

valid = json.loads((fixture_dir / "01_valid_receipt.json").read_text(encoding="utf-8"))
print(f"Valid receipt: {verify_receipt(valid, ISSUER_KEY)}")        # True

tampered = json.loads((fixture_dir / "02_tampered_receipt.json").read_text(encoding="utf-8"))
print(f"Tampered receipt: {verify_receipt(tampered, ISSUER_KEY)}")  # False

chain = json.loads((fixture_dir / "03_chain_three_receipts.json").read_text(encoding="utf-8"))
for r in verify_chain(chain, ISSUER_KEY):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")

# The forgery. Verified against the key it carries, it passes. Against the
# issuer's key, it fails. Only the second question is worth asking.
forged = json.loads((fixture_dir / "04_resigned_receipt.json").read_text(encoding="utf-8"))
print(f"Forged, checked against its own key: "
      f"{verify_receipt(forged, forged['signature']['public_key'])}")  # True
print(f"Forged, checked against issuer key:  "
      f"{verify_receipt(forged, ISSUER_KEY)}")                        # False
```

### Näite kontrollimine ilma Jupyteri kasutamata

Hoidla juurkataloogist installige tunni sõltuvused ja käivitage:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Need testid käivitavad märkmiku Pythoni näited ja eespool oleva täpse README ploki.
Samuti kontrollivad nad, et kontrollijad lükkavad tagasi manipuleeritud ja kinnitamata võtmed.
Testid vahele jätavad märkmiku `%pip` häälestuslähtri, kuna sõltuvused
paigaldatakse eraldi. Need ei muuda märkmikku ega fikatuure.

## Kuidas need genereeriti

Fiksatuurid kasutavad sama koodirada kui märkmik, kus on üks fikseeritud allkirjastamise võti
ja fikseeritud ajatemplid baitide kordustootmise tagamiseks. Genereerimiseks:

```bash
python3 generate_fixtures.py
```

(Skript on selles kataloogis aadressil `generate_fixtures.py`.)

`../test_signed_receipts.py` kontrollib kõike seda automaatselt: see käivitab
märkmiku koodi, kinnitab neid nelja fiksatuuri märkmiku
`verify_receipt` ja `verify_chain` abil ning kinnitab, et fiksatuuride
uuesti genereerimine annab täpselt samad baidid. Alates `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Mida õpilased õpivad, kui uurivad toorest JSON-i

Toore kviitungiformaadi lugemine arendab intuitsiooni, mida märkmiku lahtrid
alati ei avalda. Õpilased, kes sirvivad JSON-i, märkavad sageli:

1. Allkiri on opakne base64url-string, kuid kõik teised väljad on lihtsad
   loetavad JSON-id. Allkiri ei krüpteeri sisu; see tunnistab selle õigsust.
2. `public_key` on kviitungisse manustatud, mis teeb faili
   iseseisvaks, kuid see ei ole, mille vastu audiitor kontrollib. Võrrelge
   `02_tampered_receipt.json` ja `04_resigned_receipt.json`: mõlemad muudeti pärast allkirjastamist,
   kuid teist allkirjastati ründaja omavõtmega uuesti,
   nii et see kinnitab enda kanda oleva võtme vastu. Manustatud võti
   näitab, et fail on sisemiselt kooskõlas. Ainult teistelt
   saadud võti ütleb, kes selle välja andis.
3. Ühe tähemärgi muutmine mistahes väljal väljaspool `signature` ja selle faili uuesti
   võrdlemine `02_tampered_receipt.json`-ga teeb
   bait-tasandi mehhanismi käegakatsutavaks.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->