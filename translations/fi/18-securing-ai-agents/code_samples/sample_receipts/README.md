# Näytekuittien testitiedostot

Neljä ennalta luotua kuittitiedostoa tarkastelua varten ilman, että tarvitsee suorittaa muistikirjaa.

| Tiedosto | Mikä se on |
|---|---|
| `01_valid_receipt.json` | Voimassa oleva allekirjoitettu kuitti `lookup_flights`-työkalukutsulle. Varmistus palauttaa True. |
| `02_tampered_receipt.json` | Sama kuitti, jossa yksi kenttä on muutettu allekirjoituksen jälkeen. Varmistus palauttaa False. |
| `03_chain_three_receipts.json` | Kolmen voimassa olevan kuitin ketju (etsi, varaa, kirjaa), joissa `previous_receipt_hash` linkittää kunkin edelliseen. |
| `04_resigned_receipt.json` | Sama kuitti, jota hyökkääjä on muokannut ja allekirjoittanut uudelleen omalla julkisella avaimellaan. Varmistaa sen sisällä olevalla avaimella. Epäonnistuu julkaisijan avaimella. |

Testit allekirjoittavat kuorman kanoniset JCS-tavujoukot suoraan Ed25519:llä.
SHA-256 on edelleen käytössä sisällön tiivisteissä ja kuittiketjun linkeissä, ei
ylimääräisenä esitiivisteenä ennen allekirjoitusta.

## Näytteiden varmistaminen

`18-signed-receipts.ipynb`-osiossa suorita ensin Setup ja osiot 1–3.
Osio 3 määrittelee `verify_chain`; osiot 1 ja 2 yksinään eivät riitä.
Suorita sitten seuraava koodi uudessa solussa, kun muistikirjan työhakemistoksi on asetettu
`18-securing-ai-agents/code_samples`. Alla olevat testitiedostopolut ovat suhteellisia
siihen hakemistoon.

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

### Esimerkin tarkistaminen ilman Jupyteria

Arkistohakemiston juuresta asenna oppitunnin riippuvuudet ja suorita:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Nämä testit suorittavat muistikirjan Python-esimerkit ja tarkan README-lohkon
yllä. Ne tarkistavat myös, että peukalointi ja kiinnittämättömät avaimet hylätään varmennuksessa.
Testit ohittavat muistikirjan `%pip` asetussolun, koska riippuvuudet
asennetaan erikseen. Ne eivät muuta muistikirjaa tai testiaineistoja.

## Kuinka nämä on luotu

Testiaineistot käyttävät samaa koodipolkua kuin muistikirja, yhdellä kiinteällä allekirjoitusavaimella
ja kiinteillä aikaleimoilla tavutasoisen toistettavuuden vuoksi. Uudelleenluomiseksi:

```bash
python3 generate_fixtures.py
```

(Skripti on hakemistossa `generate_fixtures.py`.)

`../test_signed_receipts.py` tarkistaa tämän kaiken automaattisesti: se suorittaa
muistikirjan koodin, tarkistaa nämä neljä testiaineistoa muistikirjan
`verify_receipt` ja `verify_chain` avulla, ja vahvistaa, että testiaineistojen
uudelleenluominen tuottaa identtiset tavut. Lähteestä `code_samples`:

```bash
python -m unittest test_signed_receipts
```

## Mitä opiskelijat oppivat raakalaisen JSON:n tarkastelusta

Raakamuotoisen kuittidatan lukeminen rakentaa intuitiota, mitä muistikirjan solut eivät
aina tarjoa. Opiskelijat, jotka selaavat JSON:ia, usein huomaavat:

1. Allekirjoitus on läpinäkymätön base64url-merkkijono, mutta kaikki muut kentät ovat selkeää ja
   luettavaa JSON:ia. Allekirjoitus ei salaa sisältöä; se todistaa sen aitouden.
2. `public_key` on upotettu kuittiin, mikä tekee tiedostosta
   on itsenäinen, mutta se ei ole se, mitä tarkastaja vahvistaa vastaan. Vertaa
   `02_tampered_receipt.json` ja `04_resigned_receipt.json`: molempia muutettiin allekirjoituksen jälkeen,
   mutta toinen allekirjoitettiin uudelleen hyökkääjän omalla avaimella,
   joten se vahvistuu kantamansa avaimen perusteella. Upotettu avain
   kertoo, että tiedosto on sisäisesti johdonmukainen. Vain avain, joka on saatu
   muualla kertoo, kuka sen on myöntänyt.
3. Muuttamalla yhtä merkkiä missä tahansa kentässä `signature`:n ulkopuolella ja
   vertaamalla tämän tiedoston uudelleen `02_tampered_receipt.json`:ään,
   tavutasolla toimiva mekanismi käy konkreettiseksi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->