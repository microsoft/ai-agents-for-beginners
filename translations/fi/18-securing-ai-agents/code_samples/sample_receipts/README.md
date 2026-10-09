# Esimerkkikuittien esimerkit

Kolme valmiiksi luotua kuittitiedostoa tarkastelua varten ilman, että tarvitsee ajaa muistikirjaa.

| Tiedosto | Mitä se on |
|---|---|
| `01_valid_receipt.json` | Voimassa oleva allekirjoitettu kuitti `lookup_flights`-työkalukutsulle. Varmennus palauttaa True. |
| `02_tampered_receipt.json` | Sama kuitti muokatulla yhdellä kentällä allekirjoituksen jälkeen. Varmennus palauttaa False. |
| `03_chain_three_receipts.json` | Kolmen kelvollisen kuitin ketju (haku, varaus, varaa) jossa `previous_receipt_hash` linkittää ne toisiinsa. |

Esimerkeissä allekirjoitetaan suoraan hyötykuorman kanoniset JCS-tavut Ed25519:llä.
SHA-256:tä käytetään edelleen sisällön tiivisteissä ja kuittiketjun linkeissä, ei
ylimääräisenä esitiivisteenä ennen allekirjoitusta.

## Esimerkkien varmennus

Muistikirja esittelee varmentamisen neljässä osassa. Näiden esimerkkien
suora varmentaminen ilman muistikirjan ajamista:

```python
import json
from pathlib import Path

# Oletetaan, että olet suorittanut tuonnit ja apufunktiot
# kohdista 1 ja 2 tiedostosta 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # Tosi

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # Epätosi

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## Näin ne on luotu

Esimerkeissä käytetään samaa koodireittiä kuin muistikirjassa, yhdellä kiinteällä allekirjoitusavaimella
ja kiinteillä ajoituksilla tavutasolla toistettavuuden varmistamiseksi. Uudelleenluomiseen:

```bash
python3 generate_fixtures.py
```

(Skripti löytyy tästä kansiosta nimellä `generate_fixtures.py`.)

## Mitä opiskelijat oppivat lukemalla raakaa JSON-muotoa

Raakatilan lukeminen muodostaa intuitiota, jota muistikirjan solut eivät aina tarjoa. 
Opiskelijat, jotka selaavat JSON:ia, huomaavat usein:

1. Allekirjoitus on läpinäkymätön base64url-merkkijono, mutta kaikki muut kentät ovat selkeästi
   luettavaa JSON:ia. Allekirjoitus ei salaa sisältöä; se todentaa sen.
2. `public_key` sisältyy kuittiin. Tarkastajan ei tarvitse mitään muuta
   varmistaakseen (edellyttäen, että avain todella kuuluu väitetyille
   myöntäjälle; katso oppitunnin README identiteettirakenteista).
3. Yhden merkin muuttaminen missä tahansa kentässä ja sitten tämän tiedoston vertaaminen
   tiedostoon `02_tampered_receipt.json` tekee tavutason mekanismin konkreettiseksi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->