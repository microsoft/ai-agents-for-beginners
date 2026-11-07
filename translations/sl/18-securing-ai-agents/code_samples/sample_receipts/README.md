# Prednastavitve vzorcev prejemkov

Štiri vnaprej ustvarjene datoteke prejemkov za pregled brez zagona zvezka.

| Datoteka | Kaj je |
|---|---|
| `01_valid_receipt.json` | Veljaven podpisan prejemek za klic orodja `lookup_flights`. Preverjanje vrne True. |
| `02_tampered_receipt.json` | Enak prejemek z enim poljem spremenjenim po podpisu. Preverjanje vrne False. |
| `03_chain_three_receipts.json` | Veriga treh veljavnih prejemkov (iskanje, zadržanje, knjiga) z `previous_receipt_hash`, ki vsakega poveže s prejšnjim. |
| `04_resigned_receipt.json` | Enak prejemek je bil spremenjen in nato ponovno podpisan z napadalčevim javnim ključem, vgrajenim vanj. Preveri se glede na ključ v njem. Ne uspe glede na ključ izdajatelja. |

Prednastavitve neposredno podpisujejo kanonične JCS bajte vsebine z Ed25519.
SHA-256 se še vedno uporablja za odtise vsebine in povezave verige prejemkov, ne pa kot
dodatno predhodno zgoščevanje pred podpisom.

## Preverjanje vzorcev

V `18-signed-receipts.ipynb` najprej zaženite Nastavitev in Razdelke 1 do 3.
Razdelek 3 definira `verify_chain`; sami Razdelki 1 in 2 niso dovolj.
Nato zaženite naslednji blok v novi celici, pri čemer naj bo delovni imenik zvezka
nastavljen na `18-securing-ai-agents/code_samples`. Poti do prednastavitev spodaj so relativne
do tega imenika.

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

### Preverjanje primera brez Jupyterja

Iz korena repozitorija namestite odvisnosti lekcije in zaženite:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Ti testi izvajajo Python primere iz zvezka in natančen blok README.
zgoraj. Prav tako preverijo, da preverjevalniki zavrnejo posege in nepripete ključe.
Preizkusi preskočijo nastavitev celice `%pip` zvezka, ker so odvisnosti
nameščene posebej. Ne spreminjajo zvezka ali fiksnih nastavitev.

## Kako so bili ustvarjeni

Fiksne nastavitve uporabljajo isto kodo kot zvezek, z enim fiksnim podpisnim ključem
in fiksnimi časovnimi žigi za bitno ponovljivost. Za ponovno ustvarjanje:

```bash
python3 generate_fixtures.py
```

(Skript je v `generate_fixtures.py` v tem imeniku.)

`../test_signed_receipts.py` vse to samodejno preverja: zažene
kodo zvezka, preveri te štiri fiksne nastavitve s pomočjo zvezkovih
`verify_receipt` in `verify_chain`, in potrdi, da ponovna izdelava
fiksnih nastavitev da enake bite. Iz `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Kaj se študenti naučijo z raziskovanjem surovega JSON-a

Branje surovega formata potrdila gradi intuicijo, ki jo celice v zvezku
ne vedno nudijo. Študenti, ki hitro pogledajo JSON, pogosto opazijo:

1. Podpis je neprozoren niz base64url, vendar je vsako drugo polje preprost
   berljiv JSON. Podpis ne šifrira vsebine; potrjuje jo.
2. `public_key` je vključen v potrdilo, zaradi česar je datoteka
   samostojna, vendar ni to tisto, kar revident preverja. Primerjaj
   `02_tampered_receipt.json` z `04_resigned_receipt.json`: oba sta bila
   spremenjena po podpisu, a je bil drugi podpisan znova z napadalčevim
   lastnim ključem, zato je preverljiv z ključem, ki ga nosi. Vgrajeni ključ
   pove, da je datoteka notranje skladna. Samo ključ, pridobljen
   od drugod, pove, kdo jo je izdal.
3. Spreminjanje enega samega znaka kateregakoli polja zunaj `signature`, nato
   ponovno primerjanje te datoteke z `02_tampered_receipt.json`, naredi
   bitni mehanizem konkreten.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->