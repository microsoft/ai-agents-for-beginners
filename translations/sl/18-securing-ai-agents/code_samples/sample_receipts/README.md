# Vzorec prejemniških datotek

Tri vnaprej ustvarjene prejemniške datoteke za pregled brez zagona zvezka.

| Datoteka | Kaj je |
|---|---|
| `01_valid_receipt.json` | Veljavna podpisana prejemnica za klic orodja `lookup_flights`. Preverjanje vrne True. |
| `02_tampered_receipt.json` | Ista prejemnica z eno spremenjeno polje po podpisu. Preverjanje vrne False. |
| `03_chain_three_receipts.json` | Veriga treh veljavnih prejemnic (iskanje, zadržanje, rezervacija) z `previous_receipt_hash` povezovanjem vsake s prejšnjo. |

Vzorec neposredno podpise kanonične JCS bajte vsebine z Ed25519.
SHA-256 se ohranja pri uporabi za vsebinski povzetek in povezave verige prejemnic, ne kot
dodatni predhodni povzetek pred podpisom.

## Preverjanje vzorcev

V `18-signed-receipts.ipynb` najprej zaženite Nastavitev in Odseke 1 do 3.
Odsek 3 definira `verify_chain`; sami odseki 1 in 2 niso dovolj.
Nato zaženite naslednji blok v novi celici, pri čemer je delovni imenik zvezka
nastavljen na `18-securing-ai-agents/code_samples`. Spodnje poti do vzorcev so relativne
do tega imenika.

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

### Preverjanje primera brez Jupyterja

Iz korenske mape repozitorija namestite odvisnosti lekcije in zaženite:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Ti testi izvajajo Python primere iz zvezka in točno zgornji blok README.
Prav tako preverjajo, da overitelji zavrnejo manipulacije in nepovezane ključe.
Testi preskočijo nastavitev celice `%pip` iz zvezka, ker so odvisnosti
nameščene ločeno. Ne spreminjajo zvezka ali vzorcev.

## Kako so bile ustvarjene

Vzorci uporabljajo enako kodo kot zvezek, z enim fiksenim ključem za podpis
in fiksnimi časovnimi žigi za bajtno reproducibilnost. Za ponovno ustvarjanje:

```bash
python3 generate_fixtures.py
```

(Skript je v `generate_fixtures.py` v tem imeniku.)

## Kaj se študenti naučijo z ogledom surovega JSON-a

Branje surovega formata prejemnice gradi intuicijo, ki je celice v zvezku
ne vedno nudijo. Študenti, ki pogledajo JSON, pogosto opazijo:

1. Podpis je neprozorna base64url nizka, a vsako drugo polje je preprost
   berljiv JSON. Podpis ne šifrira vsebine; ga potrjuje.
2. `public_key` je vdelan v prejemnico, kar je dovolj za preverjanje
   samoskladnosti, ne pa zaupanja izdajatelja. Revizor mora primerjati s ključem,
   pritrjenim zunaj prejemnice ali rešenim prek zaupanja vrednega registra.
3. Spreminjanje ene same črke katerega koli polja in ponovno primerjanje te datoteke z
   `02_tampered_receipt.json` naredi mehanizem na nivoju bajtov otipljiv.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->