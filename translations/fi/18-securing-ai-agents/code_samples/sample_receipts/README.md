# Esimerkkikuitin testitiedostot

Kolme valmiiksi luotua kuittitiedostoa tarkastelua varten ilman, että tarvitsee ajaa muistikirjaa.

| Tiedosto | Mikä se on |
|---|---|
| `01_valid_receipt.json` | Kelvollinen allekirjoitettu kuitti `lookup_flights` työkalukutsulle. Varmistus palauttaa True. |
| `02_tampered_receipt.json` | Sama kuitti, jossa yksi kenttä muutettu allekirjoittamisen jälkeen. Varmistus palauttaa False. |
| `03_chain_three_receipts.json` | Kolmen kelvollisen kuitin ketju (etsintä, varaus, varaa) kutsuineen, joissa `previous_receipt_hash` linkittää jokaisen edelliseen. |

Testit allekirjoittavat kuorman kanoniset JCS-tavut suoraan Ed25519:llä.
SHA-256:tä käytetään edelleen sisältötiivisteissä ja kuituketjun linkeissä, ei ylimääräisenä esitiivisteenä ennen allekirjoitusta.


## Esimerkkien varmistaminen

`18-signed-receipts.ipynb`:ssa suorita ensin Setup ja osiot 1–3.
Osio 3 määrittelee `verify_chain`; osiot 1 ja 2 yksinään eivät riitä.
Sitten suorita seuraava lohko uudessa solussa, asettaen muistikirjan työhakemistoksi
`18-securing-ai-agents/code_samples`. Alla olevat testitiedostojen polut ovat suhteellisia
kyseiseen hakemistoon.

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

### Esimerkin tarkistaminen ilman Jupyteria

Repositorion juuresta asenna oppitunnin riippuvuudet ja aja:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

Nämä testit suorittavat muistikirjan Python-esimerkit ja yllä tarkennetun README-lohkon.
Ne myös tarkistavat, että manipulointi ja sipulointi ilman kiinnitettyjä avaimia hylätään varmistaessa.
Testit ohittavat muistikirjan `%pip` setup-solun, koska riippuvuudet asennetaan erikseen. Ne eivät muuta muistikirjaa tai testitiedostoja.


## Miten nämä luotiin

Testit käyttävät samaa koodipolkua kuin muistikirja, yhdellä kiinteällä allekirjoitusavaimella
ja kiinteillä aikaleimoilla tavujen toistettavuuden varmistamiseksi. Uudelleenluonti:

```bash
python3 generate_fixtures.py
```

(Skripti on `generate_fixtures.py` tässä hakemistossa.)

## Mitä opiskelijat oppivat raakan JSONin tarkastelussa

Raakamuotoisen kuitin lukeminen luo intuitiota, mitä muistikirjan solut eivät aina tarjoa.
JSONia nopeasti selaavat opiskelijat havaitsevat usein:

1. Allekirjoitus on läpinäkymätön base64url-merkkijono, mutta kaikki muut kentät ovat puhdasta
   luettavaa JSONia. Allekirjoitus ei salaa sisältöä; se vakuuttaa siitä.
2. `public_key` on sisällytetty kuittiin, mikä riittää tarkistamaan
   itsejohdonmukaisuuden mutta ei julkaisijan luotettavuutta. Tarkastajan täytyy verrata sitä avaimella,
   joka on kiinnitetty kuitin ulkopuolelle tai ratkaistu luotettavan rekisterin kautta.
3. Yhden merkin muuttaminen missä tahansa kentässä ja sitten tämän tiedoston uudelleen vertaaminen
   `02_tampered_receipt.json`:iin konkretisoi tavutasolla toimivan mekanismin.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->