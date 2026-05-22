# Esimerkkikuitti-fixtuurit

Kolme ennalta luotua kuittitiedostoa tarkastelua varten ilman, että notebookia tarvitsee ajaa.

| Tiedosto | Mikä se on |
|---|---|
| `01_valid_receipt.json` | Kelvollinen allekirjoitettu kuitti `lookup_flights`-työkalukutsulle. Varmistus palauttaa True. |
| `02_tampered_receipt.json` | Sama kuitti, jossa yksi kenttä on muutettu allekirjoituksen jälkeen. Varmistus palauttaa False. |
| `03_chain_three_receipts.json` | Kolmen kelvollisen kuitin ketju (haku, varaaminen, varmistus), jossa `previous_receipt_hash` linkittää kukin edelliseen. |

## Näytteiden varmentaminen

Notebook käy varmistuksen läpi neljässä osassa. Todistaakseen nämä fixtuurit suoraan
ilman notebook-kertomusta:

```python
import json
from pathlib import Path

# Oletetaan, että olet suorittanut tuonnit ja apufunktiot
# kohdista 1 ja 2 tiedostossa 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Tosi

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Epätosi

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Miten nämä on luotu

Fixtuurit käyttävät samaa koodipolkua kuin notebook, yhdellä kiinteällä allekirjoitusavaimella
ja kiinteillä aikaleimoilla tavutasovarmistettavuuden takaamiseksi. Uudelleen luomiseksi:

```bash
python3 generate_fixtures.py
```

(Skripti löytyy `generate_fixtures.py`-tiedostosta tässä hakemistossa.)

## Mitä opiskelijat oppivat raakan JSONin tutkimisesta

Raakamuotoisen kuitin lukeminen rakentaa intuitiota, mitä notebookin solut eivät aina anna. Opiskelijat, jotka silmäilevät JSONia, usein huomaavat:

1. Allekirjoitus on suljettu base64url-merkkijono, mutta kaikki muut kentät ovat selkeästi luettavaa JSONia. Allekirjoitus ei salaa sisältöä; se todistaa sen.
2. `public_key` on upotettu kuittiin. Tarkastajan ei tarvitse muuta varmistaakseen (edellyttäen että avain todella kuuluu väitetyille julkaisijalle; katso tunnistusinfrastruktuuria koskeva oppitunnin README).
3. Yhden merkin muuttaminen missä tahansa kentässä ja tämän tiedoston vertaaminen `02_tampered_receipt.json`-tiedostoon tekee tavutason mekanismin konkreettiseksi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->