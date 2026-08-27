# Esimerkkitositteet

Kolme esituotettua tositetiedostoa tarkastelua varten ilman, että tarvitsee ajaa muistikirjaa.

| Tiedosto | Mikä se on |
|---|---|
| `01_valid_receipt.json` | Kelvollinen allekirjoitettu kuitti `lookup_flights`-työkalukutsulle. Varmistus palauttaa True. |
| `02_tampered_receipt.json` | Sama kuitti, johon on tehty muutos yhden kentän jälkeen allekirjoituksen. Varmistus palauttaa False. |
| `03_chain_three_receipts.json` | Kolmen kelvollisen kuitin ketju (haku, varaus, kirjaus) jossa `previous_receipt_hash` linkittää jokaisen edelliseen. |

Tositteet allekirjoittavat hyötykuorman kanoniset JCS-tavut suoraan Ed25519:llä.
SHA-256 on edelleen käytössä sisällön tiivisteissä ja tositeteketin linkeissä, ei ylimääräisenä
esikäsittelytiivisteenä ennen allekirjoitusta.

## Näytteiden varmentaminen

Muistikirja käy varmentamisen läpi neljässä osassa. Tarkastaaksesi nämä tositteet
suoraan ilman muistikirjan läpikäyntiä:

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

## Miten nämä on luotu

Tositteet käyttävät samaa koodipolkua kuin muistikirja, kiinteällä allekirjoitusavaimella
ja kiinteillä aikaleimoilla tavutasollisen toistettavuuden takaamiseksi. Uudelleenluontiin:

```bash
python3 generate_fixtures.py
```

(Skripti on tässä hakemistossa nimellä `generate_fixtures.py`.)

## Mitä opiskelijat oppivat tarkastellessaan raakaa JSONia

Raakamuotoisen kuittitiedoston lukeminen rakentaa intuitiota, jota muistikirjan solut eivät aina tarjoa.
Opiskelijat, jotka vilkaisevat JSONia, huomaavat usein:

1. Allekirjoitus on läpinäkymätön base64url-merkkijono, mutta kaikki muut kentät ovat selkeää
   luettavaa JSONia. Allekirjoitus ei salaa sisältöä; se todentaa sen.
2. `public_key` on upotettu tositteeseen. Tarkastajan ei tarvitse muuta
   tarkistaaakseen (edellyttäen, että avaimen omistajuuteen voi luottaa;
   katso oppitunnin README identiteettiinfrastruktuurista).
3. Yhden merkin muuttaminen missä tahansa kentässä ja sitten tämän tiedoston vertaaminen
   tiedostoon `02_tampered_receipt.json` konkretisoi tavutasotason mekanismin.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->