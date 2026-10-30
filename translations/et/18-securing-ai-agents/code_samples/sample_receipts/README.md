# Näidiskviitungite komplektid

Kolm eelnevalt genereeritud kviitungifaili ülevaatamiseks ilma märkmikku käivitamata.

| Fail | Mis see on |
|---|---|
| `01_valid_receipt.json` | Kehtiv allkirjadega kviitung `lookup_flights` tööriista kutsele. Kontrollimine tagastab Tõene. |
| `02_tampered_receipt.json` | Sama kviitung, millel üks väli muudatud pärast allkirjastamist. Kontrollimine tagastab Väär. |
| `03_chain_three_receipts.json` | Kolme kehtiva kviitungi ahel (otsi, hoia, broneeri), kus `previous_receipt_hash` seob iga eelnevaga. |

Komplektil allkirjastatakse otse sõnumi kanoonilised JCS-baidid Ed25519-ga.
SHA-256 jääb kasutusse sisu kokkuvõtete ja kviitungi ahela linkide jaoks, mitte
lisa eel-tiheduse sammuna enne allkirjastamist.

## Näidiste kontrollimine

`18-signed-receipts.ipynb` sees käivita esmalt Seadistused ja jaotised 1 kuni 3.
Jaotis 3 määratleb `verify_chain`; üksnes jaotised 1 ja 2 ei ole piisavad.
Seejärel käivitage järgmine plokk uues lahtris, mille töökaust on notebooki
kaustaks seatud `18-securing-ai-agents/code_samples`. Allolevad proovifailide teed on suhtelised
selle kaustaga.

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

### Näite kontroll ilma Jupyterita

Repositooriumi juurest installige tunni sõltuvused ja käivitage:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Need testid käivitavad notebooki Python näited ja täpselt ülal oleva README ploki.
Samuti kontrollitakse, et pettusega seotud ja kinnitamata võtmed lükatakse tuvastajate poolt tagasi.
Testid jätavad notebooki lahtris `%pip` asuva seadistuse vahele, kuna sõltuvused
paigaldatakse eraldi. Need muudatusi notebookis ega proovifailides ei tee.

## Kuidas need genereeriti

Proovifailid kasutavad sama kooditeed nagu notebook, ühe fikseeritud allkirjavõtme
ja fikseeritud ajatemplitena baiti-taasloetavuse huvides. Kõrvalgenereerimiseks:

```bash
python3 generate_fixtures.py
```

(Skript asub selles kaustas aadressil `generate_fixtures.py`.)

## Mida õpilased õpivad toore JSON-i uurimisest

Toore kviitungi formaadi lugemine arendab intuitsiooni, mida notebooki lahtrid
alati ei paku. Õpilased, kes JSON-i sirvivad, märkavad sageli:

1. Allkiri on opakne base64url string, kuid kõik teised väljad on tavaline
   loetav JSON. Allkiri ei krüpteeri sisu; see kinnitab selle.
2. `public_key` on kviitungisse manustatud, mis võimaldab kontrollida
   iseendaga seost, kuid mitte väljastaja usaldust. Audiitor peab seda
   võrdlema väljast väljaspool kviitungi kinnitatud võtmega või usaldusväärse registri kaudu lahendatud võtmega.
3. Ühe tähe muutmine suvalises väljas ja seejärel selle faili uuesti võrdlemine
   `02_tampered_receipt.json` näitab baiti-tasandi mehhanismi konkreetset mõju.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->