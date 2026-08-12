[![Moni-agenttisuunnittelu](../../../translated_images/fi/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Napsauta yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_
# Metakognitio tekoälyagenteissa

## Johdanto

Tervetuloa oppitunnille metakognitiosta tekoälyagenteissa! Tämä luku on suunnattu aloittelijoille, jotka ovat uteliaita siitä, miten tekoälyagentit voivat ajatella omia ajatteluprosessejaan. Oppitunnin lopussa ymmärrät keskeiset käsitteet ja saat käytännön esimerkkejä metakognition soveltamisesta tekoälyagenttien suunnittelussa.

## Oppimistavoitteet

Oppitunnin suorittamisen jälkeen osaat:

1. Ymmärtää päättelysilmukoiden vaikutukset agenttien määrittelyissä.
2. Käyttää suunnittelu- ja arviointitekniikoita itsekorjaavien agenttien tukemiseksi.
3. Luoda omia agentteja, jotka kykenevät manipuloimaan koodia tehtävien suorittamiseksi.

## Johdatus metakognitioon

Metakognitio viittaa korkeampiin kognitiivisiin prosesseihin, jotka sisältävät oman ajattelun pohtimisen. Tekoälyagenteille tämä tarkoittaa kykyä arvioida ja mukauttaa toimintaansa itsetietoisuuden ja menneiden kokemusten perusteella. Metakognitio eli "ajattelu ajattelemisesta" on tärkeä käsite agenttipohjaisten tekoälyjärjestelmien kehityksessä. Se tarkoittaa, että tekoälyjärjestelmät ovat tietoisia omista sisäisistä prosesseistaan ja kykenevät valvomaan, säätelemään ja mukauttamaan käyttäytymistään vastaavasti. Samoin kuin me teemme luetessamme tilanteita tai tarkastellessamme ongelmaa. Tämä itsetietoisuus voi auttaa tekoälyjärjestelmiä tekemään parempia päätöksiä, tunnistamaan virheitä ja parantamaan suorituskykyään ajan myötä – palaten jälleen Turingin testiin ja keskusteluun siitä, aikooko tekoäly ottaa vallan.

Agenttipohjaisissa tekoälyjärjestelmissä metakognitio voi auttaa ratkaisemaan useita haasteita, kuten:
- Läpinäkyvyys: Varmistamaan, että tekoälyjärjestelmät pystyvät selittämään päättelynsä ja päätöksensä.
- Päättely: Parantamaan tekoälyjärjestelmien kykyä yhdistellä tietoa ja tehdä järkeviä päätöksiä.
- Sopeutuminen: Antamaan tekoälyjärjestelmille mahdollisuuden mukautua uusiin ympäristöihin ja muuttuviin olosuhteisiin.
- Havaitseminen: Parantamaan tekoälyjärjestelmien tarkkuutta ympäristöstään saadun datan tunnistamisessa ja tulkinnassa.

### Mitä on metakognitio?

Metakognitio eli "ajattelu ajattelemisesta" on korkeampaa kognitiivista prosessia, joka sisältää itsetietoisuuden ja oman ajattelun säätelemisen. Tekoälyn alalla metakognitio antaa agenteille kyvyn arvioida ja mukauttaa strategioitaan ja toimiaan, mikä johtaa parantuneisiin ongelmanratkaisu- ja päätöksentekokykyihin. Ymmärtämällä metakognition voit suunnitella tekoälyagentteja, jotka ovat paitsi älykkäämpiä myös mukautuvampia ja tehokkaampia. Aidossa metakognitiossa tekoäly nimenomaan perustelee omaa päättelyään.

Esimerkki: "Priorisoin halvemmat lennot, koska… Voin jäädä paitsi suorin lennoista, joten tarkistanpa uudelleen."
Pitää kirjaa siitä, miten tai miksi se valitsi tietyn reitin.
- Huomaa, että se teki virheitä, koska se luotti liikaa käyttäjän edellisiin mieltymyksiin, joten se muuttaa päätöksentekostrategiaansa, ei vain lopullista suositusta.
- Diagnosoi malleja, kuten "Aina kun näen käyttäjän mainitsevan 'liian ruuhkainen', en pelkästään poista tiettyjä nähtävyyksiä, vaan myös pohdin, että tapani valita 'top nähtävyydet' on virheellinen, jos aina järjestän suosituimpien mukaan."

### Metakognition merkitys tekoälyagenteissa

Metakognitiolla on tärkeä rooli tekoälyagenttien suunnittelussa monista syistä:

![Metakognition merkitys](../../../translated_images/fi/importance-of-metacognition.b381afe9aae352f7.webp)

- Itsetutkiskelu: Agentit voivat arvioida omaa suorituskykyään ja tunnistaa parannettavia alueita.
- Sopeutumiskyky: Agentit voivat muuttaa strategioitaan aiempien kokemusten ja muuttuvien olosuhteiden perusteella.
- Virheiden korjaaminen: Agentit voivat havaita ja korjata virheitä itsenäisesti, mikä johtaa tarkempiin tuloksiin.
- Resurssien hallinta: Agentit voivat optimoida resurssien, kuten ajan ja laskentatehon, käyttöä suunnittelemalla ja arvioimalla toimiaan.

## Tekoälyagentin osat

Ennen metakognitiivisiin prosesseihin sukeltamista on tärkeää ymmärtää tekoälyagentin perusosat. Tekoälyagentti koostuu tyypillisesti:

- Persoona: Agentin persoona ja ominaisuudet, jotka määrittävät sen vuorovaikutuksen käyttäjien kanssa.
- Työkalut: Kyvyt ja toiminnot, joita agentti voi suorittaa.
- Taidot: Tieto ja asiantuntemus, jotka agentilla on.

Nämä osat toimivat yhdessä muodostaen "asiantuntijayksikön", joka voi suorittaa tiettyjä tehtäviä.

**Esimerkki**:
Ajattele matkatoimistoagenttia, joka ei ainoastaan suunnittele lomasi, vaan myös mukauttaa reittinsä reaaliaikaisten tietojen ja aiempien asiakkaiden matkokokemusten perusteella.

### Esimerkki: Metakognitio matkatoimistoagenttipalvelussa

Kuvittele suunnittelevasi tekoälyllä toimivaa matkatoimistoagenttipalvelua. Tämä agentti, "Matkatoimistoagentti", auttaa käyttäjiä lomamatkojen suunnittelussa. Metakognition sisällyttämiseksi Matkatoimistoagentin tulee arvioida ja mukauttaa toimintaansa itsetietoisuuden ja menneiden kokemusten perusteella. Näin metakognitio voi toimia:

#### Nykyinen tehtävä

Nykyinen tehtävä on auttaa käyttäjää suunnittelemaan matka Pariisiin.

#### Tehtävän suorittamisen vaiheet

1. **Käyttäjän mieltymysten kerääminen**: Kysy käyttäjältä matkan päivämäärät, budjetti, kiinnostuksen kohteet (esim. museot, ruoka, ostokset) ja mahdolliset erityisvaatimukset.
2. **Tiedon hakeminen**: Etsi lentovaihtoehtoja, majoituksia, nähtävyyksiä ja ravintoloita, jotka vastaavat käyttäjän mieltymyksiä.
3. **Suositusten laatiminen**: Tarjoa henkilökohtainen matkasuunnitelma, johon sisältyy lentotiedot, hotellivaraukset ja ehdotetut aktiviteetit.
4. **Mukauttaminen palautteen perusteella**: Kysy käyttäjältä palautetta suosituksista ja tee tarvittavat muutokset.

#### Tarvittavat resurssit

- Pääsy lento- ja hotelli-varausrekistereihin.
- Tietoa pariisilaisista nähtävyyksistä ja ravintoloista.
- Käyttäjäpalautedata aiemmista vuorovaikutuksista.

#### Kokemus ja itsetutkiskelu

Matkatoimistoagentti käyttää metakognitiota arvioidakseen suorituskykyään ja oppiakseen menneistä kokemuksista. Esimerkiksi:

1. **Käyttäjäpalautteen analysointi**: Matkatoimistoagentti tarkastelee käyttäjäpalautetta sen selvittämiseksi, mitkä suositukset olivat hyvin vastaanotettuja ja mitkä eivät. Se mukauttaa tulevia ehdotuksiaan tämän perusteella.
2. **Sopeutumiskyky**: Jos käyttäjä on aiemmin maininnut, ettei pidä ruuhkaisista paikoista, Matkatoimistoagentti välttää suosittelemasta suosittuja turistikohteita ruuhka-aikoina tulevaisuudessa.
3. **Virheiden korjaaminen**: Jos Matkatoimistoagentti on tehnyt virheen aiemmassa varauksessa, kuten ehdottanut täyteen varattua hotellia, se oppii tarkistamaan saatavuuden huolellisemmin ennen suositusten antamista.

#### Käytännön kehittäjäesimerkki

Tässä on yksinkertaistettu esimerkki siitä, miltä Matkatoimistoagentin koodi voisi näyttää metakognition sisällyttämisen yhteydessä:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Etsi lentoja, hotelleja ja nähtävyyksiä mieltymysten perusteella
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        # Analysoi palautetta ja säädä tulevia suosituksia
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Esimerkkikäyttö
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

#### Miksi metakognitio on tärkeää

- **Itsetutkiskelu**: Agentit voivat analysoida suorituskykyään ja tunnistaa parannettavat kohteet.
- **Sopeutumiskyky**: Agentit voivat muuttaa strategioitaan palautteen ja muuttuvien olosuhteiden perusteella.
- **Virheiden korjaaminen**: Agentit voivat itsenäisesti havaita ja korjata virheitä.
- **Resurssien hallinta**: Agentit voivat optimoida resurssien, kuten ajan ja laskentatehon, käyttöä.

Sisällyttämällä metakognition Matkatoimistoagentti voi tarjota henkilökohtaisempia ja tarkempia matkasuosituksia, parantaen käyttäjäkokemusta.

---

## 2. Suunnittelu agenteissa

Suunnittelu on keskeinen osa tekoälyagentin käyttäytymistä. Se sisältää tavoitteeseen pääsemiseksi tarvittavien askelten hahmottamisen ottaen huomioon nykytilan, resurssit ja mahdolliset esteet.

### Suunnittelun osa-alueet

- **Nykyinen tehtävä**: Määrittele tehtävä selkeästi.
- **Tehtävän suorittamisen vaiheet**: Jaa tehtävä hallittaviin osiin.
- **Tarvittavat resurssit**: Tunnista tarvittavat resurssit.
- **Kokemus**: Hyödynnä aiempia kokemuksia suunnittelussa.

**Esimerkki**:
Tässä ovat vaiheet, jotka Matkatoimistoagentin tulee suorittaa auttaakseen käyttäjää matkasuunnittelussa tehokkaasti:

### Vaiheet Matkatoimistoagentille

1. **Käyttäjän mieltymysten kerääminen**
   - Kysy käyttäjältä tietoja matkapäivämääristä, budjetista, kiinnostuksen kohteista ja erityisvaatimuksista.
   - Esimerkit: "Milloin aiot matkustaa?" "Mikä on budjettisi?" "Mistä aktiviteeteista pidät lomalla?"

2. **Tiedon hakeminen**
   - Etsi matkavaihtoehtoja käyttäjän mieltymysten perusteella.
   - **Lennot**: Etsi saatavilla olevia lentoja käyttäjän budjetissa ja halutuilla päivämäärillä.
   - **Majoitukset**: Löydä hotelleja tai vuokrakohteita, jotka vastaavat käyttäjän mieltymyksiä sijainnin, hinnan ja palveluiden osalta.
   - **Nähtävyydet ja ravintolat**: Tunnista suosittuja nähtävyyksiä, aktiviteetteja ja ruokailumahdollisuuksia, jotka sopivat käyttäjän kiinnostuksen kohteisiin.

3. **Suositusten laatiminen**
   - Koosta haettu tieto henkilökohtaiseksi matkasuunnitelmaksi.
   - Tarjoa tietoja, kuten lentovaihtoehtoja, hotellivarauksia ja ehdotettuja aktiviteetteja käyttäjän mieltymykset huomioiden.

4. **Matkasuunnitelman esittäminen käyttäjälle**
   - Jaa ehdotettu matkasuunnitelma käyttäjän tarkasteltavaksi.
   - Esimerkki: "Tässä on ehdotettu matkasuunnitelma Pariisin-matkallesi. Se sisältää lentotiedot, hotellivaraukset sekä suositellut aktiviteetit ja ravintolat. Kerro mielipiteesi!"

5. **Palautteen kerääminen**
   - Kysy käyttäjältä palautetta ehdotetusta matkasuunnitelmasta.
   - Esimerkit: "Pidätkö lentovaihtoehdoista?" "Sopiiko hotelli tarpeisiisi?" "Haluatko lisätä tai poistaa aktiviteetteja?"

6. **Mukauttaminen palautteen perusteella**
   - Muokkaa matkasuunnitelmaa käyttäjän palautteen mukaan.
   - Tee tarvittavat muutokset lento-, majoitus- ja aktiviteettisuosituksiin, jotta ne vastaavat paremmin käyttäjän mieltymyksiä.

7. **Lopullinen vahvistus**
   - Esitä päivitetty matkasuunnitelma käyttäjälle lopullista vahvistusta varten.
   - Esimerkki: "Tein muutokset palautteesi perusteella. Tässä päivitetty suunnitelma. Onko kaikki ok?"

8. **Varausten tekeminen ja vahvistaminen**
   - Kun käyttäjä hyväksyy suunnitelman, tee lentojen, majoituksen ja etukäteen suunniteltujen aktiviteettien varaukset.
   - Lähetä vahvistustiedot käyttäjälle.

9. **Jatkuva tuki**
   - Ole käytettävissä auttamaan käyttäjää mahdollisissa muutoksissa tai lisäpyynnöissä ennen matkaa ja matkan aikana.
   - Esimerkki: "Jos tarvitset apua matkan aikana, ota rohkeasti yhteyttä milloin tahansa!"

### Esimerkkivuorovaikutus

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Esimerkkikäyttö booauspyynnön yhteydessä
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

## 3. Korjaava RAG-järjestelmä

Aloitetaan ymmärtämällä ero RAG-työkalun ja ennakoivan kontekstin latauksen välillä.

![RAG vs kontekstin lataus](../../../translated_images/fi/rag-vs-context.9eae588520c00921.webp)

### Hakuavusteinen generointi (RAG)

RAG yhdistää hakujärjestelmän ja generatiivisen mallin. Kun kysely tehdään, hakujärjestelmä hakee asiaankuuluvat dokumentit tai tiedot ulkoisesta lähteestä, ja löydettyä tietoa käytetään generatiivisen mallin syötteen täydentämiseen. Tämä auttaa mallia tuottamaan tarkempia ja kontekstuaalisesti merkityksellisiä vastauksia.

RAG-järjestelmässä agentti hakee relevanttia tietoa tietokannasta ja käyttää tätä tietoa tuottaakseen sopivia vastauksia tai toimia.

### Korjaava RAG-lähestymistapa

Korjaava RAG-lähestymistapa keskittyy RAG-tekniikoiden käyttöön virheiden korjaamiseksi ja tekoälyagenttien tarkkuuden parantamiseksi. Tämä sisältää:

1. **Muistutusmenetelmä**: Käytetään tiettyjä kehotteita, jotka ohjaavat agenttia hakemaan asiaankuuluvaa tietoa.
2. **Työkalu**: Toteutetaan algoritmeja ja mekanismeja, jotka antavat agentille mahdollisuuden arvioida haetun tiedon merkityksellisyyttä ja tuottaa tarkkoja vastauksia.
3. **Arviointi**: Agentin suorituskyvyn jatkuva arviointi ja säätö tarkkuuden ja tehokkuuden parantamiseksi.

#### Esimerkki: Korjaava RAG hakuprosessissa

Mieti hakutoimintoa, joka hakee tietoa verkosta vastatakseen käyttäjän kyselyihin. Korjaava RAG-lähestymistapa voi sisältää:

1. **Muistutusmenetelmä**: Laadi hakukyselyitä käyttäjän syötteen perusteella.
2. **Työkalu**: Käytä luonnollisen kielen käsittelyä ja koneoppimisalgoritmeja hakutulosten lajitteluun ja suodattamiseen.
3. **Arviointi**: Analysoi käyttäjäpalautetta epäkohtien tunnistamiseksi ja haetun tiedon virheiden korjaamiseksi.

### Korjaava RAG matkatoimistoagentissa

Korjaava RAG (Retrieval-Augmented Generation) parantaa tekoälyn kykyä hakea ja tuottaa tietoa korjaten samalla virheitä. Tarkastellaan, miten Matkatoimistoagentti voi käyttää korjaavaa RAG-lähestymistapaa tarjotakseen tarkempia ja merkityksellisempiä matkasuosituksia.

Tämä sisältää:

- **Muistutusmenetelmä:** Käytetään tiettyjä kehotteita ohjaamaan agenttia hakemaan asiaankuuluvaa tietoa.
- **Työkalu:** Toteutetaan algoritmeja ja mekanismeja, jotka antavat agentille mahdollisuuden arvioida haetun tiedon merkityksellisyyttä ja tuottaa tarkkoja vastauksia.
- **Arviointi:** Agentin suorituskyvyn jatkuva arviointi ja säätö tarkkuuden ja tehokkuuden parantamiseksi.

#### Korjaavan RAG:n käyttöönoton vaiheet Matkatoimistoagentissa

1. **Alkuperäinen käyttäjävuorovaikutus**
   - Matkatoimistoagentti kerää käyttäjän alkuperäiset mieltymykset, kuten kohteen, matkustuspäivät, budjetin ja kiinnostuksen kohteet.
   - Esimerkki:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Tiedon haku**
   - Matkatoimistoagentti hakee tietoa lennoista, majoituksista, nähtävyyksistä ja ravintoloista käyttäjän mieltymysten perusteella.
   - Esimerkki:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Alkuperäisten suositusten luominen**
   - Matkatoimistoagentti käyttää haettua tietoa luodakseen henkilökohtaisen matkasuunnitelman.
   - Esimerkki:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Käyttäjäpalautteen kerääminen**
   - Matkatoimistoagentti pyytää käyttäjältä palautetta alkuperäisistä suosituksista.
   - Esimerkki:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Korjaava RAG-prosessi**
   - **Muistutusmenetelmä**: Matkatoimistoagentti laatii uusia hakukyselyitä käyttäjäpalautteen perusteella.
     - Esimerkki:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Työkalu**: Matkatoimistoagentti käyttää algoritmeja uusien hakutulosten lajitteluun ja suodattamiseen, korostaen merkityksellisyyttä käyttäjäpalautteen mukaan.
     - Esimerkki:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Arviointi**: Matkatoimistoagentti arvioi jatkuvasti suositustensa merkityksellisyyttä ja tarkkuutta analysoimalla käyttäjäpalautetta ja tekemällä tarvittavat muutokset.
     - Esimerkki:

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```

#### Käytännön esimerkki

Tässä on yksinkertaistettu Python-koodiesimerkki, jossa korjaava RAG-lähestymistapa on sisällytetty Matkatoimistoagenttiin:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)
        new_itinerary = self.generate_recommendations()
        return new_itinerary

# Esimerkkikäyttö
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
new_itinerary = travel_agent.adjust_based_on_feedback(feedback)
print("Updated Itinerary:", new_itinerary)
```

### Ennakoiva kontekstin lataus


Ennakoiva kontekstin lataaminen tarkoittaa olennaisen kontekstin tai taustatiedon lataamista malliin ennen kyselyn käsittelyä. Tämä tarkoittaa, että mallilla on pääsy tähän tietoon alusta alkaen, mikä voi auttaa sitä tuottamaan paremmin informoituja vastauksia ilman, että sen tarvitsee hakea lisätietoja prosessin aikana.

Tässä on yksinkertaistettu esimerkki siitä, miltä ennakoiva kontekstin lataaminen voisi näyttää matkatoimiston sovelluksessa Pythonilla:

```python
class TravelAgent:
    def __init__(self):
        # Esilataa suosittuja kohteita ja niiden tiedot
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Hae kohdetiedot esiladatuista konteksteista
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Esimerkki käytöstä
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### Selitys

1. **Alustaminen (`__init__`-metodi)**: `TravelAgent`-luokka esilataa sanakirjan, joka sisältää tietoa suosituista kohteista, kuten Pariisi, Tokio, New York ja Sydney. Tämä sanakirja sisältää tietoja kuten maa, valuutta, kieli ja tärkeimmät nähtävyydet kullekin kohteelle.

2. **Tietojen hakeminen (`get_destination_info`-metodi)**: Kun käyttäjä kysyy tietystä kohteesta, `get_destination_info`-metodi hakee olennaiset tiedot esiladattusta kontekstisanakirjasta.

Esilataamalla konteksti matkatoimiston sovellus voi vastata käyttäjän kyselyihin nopeasti ilman, että sen tarvitsee hakea tietoja ulkoisesta lähteestä reaaliajassa. Tämä tekee sovelluksesta tehokkaamman ja reagoivamman.

### Suunnitelman käynnistäminen tavoitteella ennen iteraatiota

Suunnitelman käynnistäminen tavoitteella tarkoittaa aloittamista selkeällä päämäärällä tai tavoitellulla lopputuloksella mielessä. Määrittelemällä tämän tavoitteen etukäteen malli voi käyttää sitä ohjenuorana koko iteratiivisen prosessin ajan. Tämä auttaa varmistamaan, että jokainen iteraatio vie lähemmäksi haluttua lopputulosta, tehden prosessista tehokkaamman ja kohdistetumman.

Tässä on esimerkki siitä, miten matkasuunnitelman voi käynnistää tavoitteella ennen iterointia matkatoimistolle Pythonissa:

### Tilanne

Matkatoimisto haluaa suunnitella räätälöidyn loman asiakkaalle. Tavoitteena on luoda matkareitti, joka maksimoi asiakkaan tyytyväisyyden perustuen asiakkaan mieltymyksiin ja budjettiin.

### Vaiheet

1. Määrittele asiakkaan mieltymykset ja budjetti.
2. Käynnistä alkuperäinen suunnitelma näiden mieltymysten pohjalta.
3. Iteroi suunnitelmaa parantaen sitä asiakkaan tyytyväisyyden optimoimiseksi.

#### Python-koodi

```python
class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def bootstrap_plan(self, preferences, budget):
        plan = []
        total_cost = 0

        for destination in self.destinations:
            if total_cost + destination['cost'] <= budget and self.match_preferences(destination, preferences):
                plan.append(destination)
                total_cost += destination['cost']

        return plan

    def match_preferences(self, destination, preferences):
        for key, value in preferences.items():
            if destination.get(key) != value:
                return False
        return True

    def iterate_plan(self, plan, preferences, budget):
        for i in range(len(plan)):
            for destination in self.destinations:
                if destination not in plan and self.match_preferences(destination, preferences) and self.calculate_cost(plan, destination) <= budget:
                    plan[i] = destination
                    break
        return plan

    def calculate_cost(self, plan, new_destination):
        return sum(destination['cost'] for destination in plan) + new_destination['cost']

# Esimerkkikäyttö
destinations = [
    {"name": "Paris", "cost": 1000, "activity": "sightseeing"},
    {"name": "Tokyo", "cost": 1200, "activity": "shopping"},
    {"name": "New York", "cost": 900, "activity": "sightseeing"},
    {"name": "Sydney", "cost": 1100, "activity": "beach"},
]

preferences = {"activity": "sightseeing"}
budget = 2000

travel_agent = TravelAgent(destinations)
initial_plan = travel_agent.bootstrap_plan(preferences, budget)
print("Initial Plan:", initial_plan)

refined_plan = travel_agent.iterate_plan(initial_plan, preferences, budget)
print("Refined Plan:", refined_plan)
```

#### Koodin selitys

1. **Alustaminen (`__init__`-metodi)**: `TravelAgent`-luokka alustetaan listalla mahdollisista matkakohteista, joilla on ominaisuuksia kuten nimi, kustannus ja aktiviteettityyppi.

2. **Suunnitelman käynnistäminen (`bootstrap_plan`-metodi)**: Tämä metodi luo alkuperäisen matkasuunnitelman perustuen asiakkaan mieltymyksiin ja budjettiin. Se käy läpi kohdelistan ja lisää kohteet suunnitelmaan, jos ne vastaavat asiakkaan mieltymyksiä ja mahtuvat budjettiin.

3. **Mieltymysten vastaavuus (`match_preferences`-metodi)**: Tämä metodi tarkistaa, vastaako kohde asiakkaan mieltymyksiä.

4. **Suunnitelman uudelleenarviointi (`iterate_plan`-metodi)**: Tämä metodi tarkentaa alkuperäistä suunnitelmaa yrittämällä korvata jokainen suunnitelman kohde paremmin sopivalla, ottaen huomioon asiakkaan mieltymykset ja budjettirajoitteet.

5. **Kustannuksen laskeminen (`calculate_cost`-metodi)**: Tämä metodi laskee nykyisen suunnitelman kokonaiskustannuksen, mukaan lukien mahdollinen uusi kohde.

#### Esimerkin käyttö

- **Alkuperäinen suunnitelma**: Matkatoimisto luo alkuperäisen suunnitelman perustuen asiakkaan mieltymyksiin sightseeingistä ja budjettiin 2000 dollaria.
- **Tarkennettu suunnitelma**: Matkatoimisto uudelleenarvioi suunnitelman, optimoiden asiakkaan mieltymyksiä ja budjettia.

Käynnistämällä suunnitelma selkeällä tavoitteella (esim. asiakkaan tyytyväisyyden maksimointi) ja toistamalla sen parannuksia, matkatoimisto voi luoda asiakkaalle räätälöidyn ja optimoidun matkareitin. Tämä lähestymistapa varmistaa, että matkasuunnitelma vastaa asiakkaan mieltymyksiä ja budjettia alusta alkaen ja paranee jokaisella iteraatiolla.

### LLM:n hyödyntäminen uudelleenjärjestämisessä ja pisteyttämisessä

Suuret kielimallit (LLM) voidaan hyödyntää uudelleenjärjestämisessä ja pisteytyksessä arvioimalla haettujen dokumenttien tai tuotettujen vastausten olennaisuutta ja laatua. Näin se toimii:

**Haku:** Alkuperäinen hakuvaihe hakee joukon ehdokasdokumentteja tai vastauksia kyselyn perusteella.

**Uudelleenjärjestäminen:** LLM arvioi nämä ehdokkaat ja järjestää ne uudelleen niiden olennaisuuden ja laadun mukaan. Tämä vaihe varmistaa, että kaikkein olennaisimmat ja laadukkaimmat tiedot esitetään ensin.

**Pisteytys:** LLM antaa pisteitä jokaiselle ehdokkaalle, jotka heijastavat niiden olennaisuutta ja laatua. Tämä auttaa valitsemaan parhaan vastauksen tai dokumentin käyttäjälle.

Hyödyntämällä LLM:ää uudelleenjärjestämisessä ja pisteytyksessä järjestelmä voi tarjota tarkempaa ja kontekstuaalisesti relevantimpaa tietoa, parantaen kokonaiskäyttäjäkokemusta.

Tässä on esimerkki siitä, miten matkatoimisto voi käyttää suurta kielimallia (LLM) matkakohteiden uudelleenjärjestämiseen ja pisteyttämiseen käyttäjän mieltymysten perusteella Pythonissa:

#### Tilanne - Matkustus mieltymysten perusteella

Matkatoimisto haluaa suositella parhaita matkakohteita asiakkaalle perustuen tämän mieltymyksiin. LLM auttaa uudelleenjärjestämään ja pisteyttämään kohteet varmistaakseen, että osuvimmat vaihtoehdot esitellään.

#### Vaiheet:

1. Kerää käyttäjän mieltymykset.
2. Hae lista mahdollisista matkakohteista.
3. Käytä LLM:ää uudelleenjärjestämään ja pisteyttämään kohteet käyttäjän mieltymysten perusteella.

Näin voit päivittää aiemman esimerkin käyttämään Azure OpenAI -palveluita:

#### Vaatimukset

1. Sinulla tulee olla Azure-tilaus.
2. Luo Azure OpenAI -resurssi ja hanki API-avain.

#### Esimerkkikoodi Pythonissa

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Luo kehotus Azure OpenAI:lle
        prompt = self.generate_prompt(preferences)
        
        # Määritä pyynnön otsikot ja sisältö
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Kutsu Azure OpenAI -rajapintaa saadaksesi uudelleenjärjestellyt ja pisteytetyt kohteet
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Poimi ja palauta suositukset
        recommendations = response_data['choices'][0]['text'].strip().split('\n')
        return recommendations

    def generate_prompt(self, preferences):
        prompt = "Here are the travel destinations ranked and scored based on the following user preferences:\n"
        for key, value in preferences.items():
            prompt += f"{key}: {value}\n"
        prompt += "\nDestinations:\n"
        for destination in self.destinations:
            prompt += f"- {destination['name']}: {destination['description']}\n"
        return prompt

# Esimerkkikäyttö
destinations = [
    {"name": "Paris", "description": "City of lights, known for its art, fashion, and culture."},
    {"name": "Tokyo", "description": "Vibrant city, famous for its modernity and traditional temples."},
    {"name": "New York", "description": "The city that never sleeps, with iconic landmarks and diverse culture."},
    {"name": "Sydney", "description": "Beautiful harbour city, known for its opera house and stunning beaches."},
]

preferences = {"activity": "sightseeing", "culture": "diverse"}
api_key = 'your_azure_openai_api_key'
endpoint = 'https://your-endpoint.com/openai/deployments/your-deployment-name/completions?api-version=2022-12-01'

travel_agent = TravelAgent(destinations)
recommendations = travel_agent.get_recommendations(preferences, api_key, endpoint)
print("Recommended Destinations:")
for rec in recommendations:
    print(rec)
```

#### Koodin selitys - Mieltymysten varaus

1. **Alustaminen**: `TravelAgent`-luokka alustetaan listalla mahdollisia matkakohteita, joilla on ominaisuuksia kuten nimi ja kuvaus.

2. **Suositusten hakeminen (`get_recommendations`-metodi)**: Tämä metodi muodostaa kehotteen Azure OpenAI -palvelulle käyttäjän mieltymysten perusteella ja tekee HTTP POST -pyynnön Azure OpenAI API:lle saadakseen uudelleenjärjestetyt ja pisteytetyt kohteet.

3. **Kehotteen luominen (`generate_prompt`-metodi)**: Tämä metodi rakentaa kehotteen Azure OpenAI:lle, joka sisältää käyttäjän mieltymykset ja kohdelistan. Kehote ohjaa mallia uudelleenjärjestämään ja pisteyttämään kohteet annettujen mieltymysten mukaan.

4. **API-kutsu**: `requests`-kirjastoa käytetään tekemään HTTP POST -pyyntö Azure OpenAI API:n päätepisteeseen. Vastauksessa ovat uudelleenjärjestetyt ja pisteytetyt kohteet.

5. **Esimerkin käyttö**: Matkatoimisto kerää käyttäjän mieltymykset (esim. kiinnostus sightseeingiin ja monipuoliseen kulttuuriin) ja käyttää Azure OpenAI -palvelua saadakseen uudelleenjärjestellyt ja pisteytetyt matkakohdesuositukset.

Muista vaihtaa `your_azure_openai_api_key` oikeaan Azure OpenAI API -avaimeesi ja `https://your-endpoint.com/...` Azure OpenAI -käyttöönoton oikeaan päätepisteosoitteeseen.

Hyödyntämällä LLM:ää uudelleenjärjestämiseen ja pisteytykseen matkatoimisto voi tarjota henkilökohtaisempia ja relevantimpia matkasuosituksia asiakkaille, parantaen heidän kokonaiskokemustaan.

### RAG: Kehotustekniikka vs Työkalu

Hakuun pohjautuva generaatiotekniikka (Retrieval-Augmented Generation, RAG) voi olla sekä kehotustekniikka että työkalu tekoälyagenttien kehityksessä. Erottelun ymmärtäminen voi auttaa käyttämään RAG:ia tehokkaammin projekteissasi.

#### RAG kehotustekniikkana

**Mikä se on?**

- Kehotustekniikkana RAG tarkoittaa tiettyjen kyselyiden tai kehotteiden muodostamista ohjaamaan olennaisen tiedon hakua suuresta kokoelmasta tai tietokannasta. Tätä tietoa käytetään sitten vastausten tai toimintojen tuottamiseen.

**Miten se toimii:**

1. **Kehota muodostamaan kehotteita**: Luo hyvin jäsenneltyjä kehotteita tai kyselyjä tehtävän tai käyttäjän syötteen perusteella.
2. **Hae tietoa**: Käytä kehotteita haun tekemiseen esexisting tietopohjasta tai tietojoukosta.
3. **Luo vastaus**: Yhdistä haettu tieto generatiivisten tekoälymallien kanssa tuottaaksesi kattavan ja yhtenäisen vastauksen.

**Esimerkki matkatoimistosta**:

- Käyttäjän syöte: "Haluan vierailla museoissa Pariisissa."
- Kehote: "Etsi Pariisin parhaat museot."
- Haettu tieto: Tietoa Louvre-museosta, Musée d'Orsayn museosta jne.
- Luotu vastaus: "Tässä on joitakin Pariisin parhaista museoista: Louvre-museo, Musée d'Orsay ja Centre Pompidou."

#### RAG työkaluna

**Mikä se on?**

- Työkaluna RAG on integroitu järjestelmä, joka automatisoi haku- ja generaatioprosessin, tehden kehittäjien helpommaksi toteuttaa monimutkaisia tekoälytoimintoja ilman, että jokaiselle kyselylle tarvitsee manuaalisesti laatia kehotteita.

**Miten se toimii:**

1. **Integraatio**: Upota RAG tekoälyagentin arkkitehtuuriin, jolloin se hoitaa automaattisesti haku- ja generaatiotehtävät.
2. **Automaatio**: Työkalu hallinnoi koko prosessin käyttäjän syötteestä lopullisen vastauksen tuottamiseen ilman että jokaiselle vaiheelle tarvitsee erikseen kehotteita.
3. **Tehokkuus**: Parantaa agentin suorituskykyä virtaviivaistamalla haku- ja generaatioprosessin, mahdollistaen nopeammat ja tarkemmat vastaukset.

**Esimerkki matkatoimistosta**:

- Käyttäjän syöte: "Haluan vierailla museoissa Pariisissa."
- RAG-työkalu: Hakee automaattisesti tietoa museoista ja tuottaa vastauksen.
- Luotu vastaus: "Tässä on joitakin Pariisin parhaista museoista: Louvre-museo, Musée d'Orsay ja Centre Pompidou."

### Vertailu

| Näkökulma            | Kehotustekniikka                                  | Työkalu                                            |
|---------------------|--------------------------------------------------|---------------------------------------------------|
| **Manuaalinen vs Automaattinen** | Manuaalinen kehotteiden muodostus jokaiselle kyselylle. | Automaattinen haku- ja generaatioprosessi.        |
| **Ohjattavuus**      | Tarjoaa enemmän kontrollia hakuprosessiin.       | Virtaviivaistaa ja automatisoi haku- ja generaation.|
| **Joustavuus**       | Mahdollistaa mukautetut kehotteet erityistarpeisiin. | Tehokkaampi suuriin käyttöönottoihin.              |
| **Monimutkaisuus**  | Vaatinee kehotteiden laatimista ja hienosäätöä. | Helpompi integroida tekoälyagentin arkkitehtuuriin.|

### Käytännön esimerkkejä

**Esimerkki kehotustekniikasta:**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**Esimerkki työkalusta:**

```python
class Travel_Agent:
    def __init__(self):
        self.rag_tool = RAGTool()

    def get_museums_in_paris(self):
        user_input = "I want to visit museums in Paris."
        response = self.rag_tool.retrieve_and_generate(user_input)
        return response

travel_agent = Travel_Agent()
museums = travel_agent.get_museums_in_paris()
print("Top Museums in Paris:", museums)
```

### Olennaisuuden arviointi

Olennaisuuden arviointi on ratkaiseva osa tekoälyagentin suorituskykyä. Se varmistaa, että agentin hakema ja tuottama tieto on tarkoituksenmukaista, tarkkaa ja hyödyllistä käyttäjälle. Tarkastellaan, miten olennaisuutta voi arvioida tekoälyagenteissa, käytännön esimerkkien ja tekniikoiden avulla.

#### Olennaisuuden arvioinnin keskeiset käsitteet

1. **Kontekstin ymmärrys**:
   - Agentin tulee ymmärtää käyttäjän kyselyn konteksti hakeakseen ja tuottaakseen relevanttia tietoa.
   - Esimerkki: Jos käyttäjä kysyy "parhaat ravintolat Pariisissa," agentin tulee ottaa huomioon käyttäjän mieltymykset, kuten ruokakulttuuri ja budjetti.

2. **Tarkkuus**:
   - Agentin tarjoamien tietojen tulee olla tosiasiallisesti oikeita ja ajantasaisia.
   - Esimerkki: Suositella tällä hetkellä auki olevia, hyviä arvosteluja saaneita ravintoloita sen sijaan, että suosittelee vanhentuneita tai suljettuja vaihtoehtoja.

3. **Käyttäjän tarkoitus**:
   - Agentin tulee päätellä käyttäjän kyselyn takana oleva tarkoitus tarjotakseen relevantimpaa tietoa.
   - Esimerkki: Jos käyttäjä kysyy "edulliset hotellit," agentin tulisi priorisoida edulliset vaihtoehdot.

4. **Palautejärjestelmä**:
   - Jatkuva käyttäjäpalautteen keruu ja analysointi auttaa agenttia hienosäätämään olennaisuuden arviointiprosessia.
   - Esimerkki: Käyttää käyttäjien arvioita ja palautetta aiemmista suosituksista parantaakseen tulevia vastauksia.

#### Käytännön tekniikoita olennaisuuden arviointiin

1. **Olennaisuuspisteytys**:
   - Anna jokaiselle haetulle kohteelle pistemäärä sen mukaan, kuinka hyvin se vastaa käyttäjän kyselyä ja mieltymyksiä.
   - Esimerkki:

     ```python
     def relevance_score(item, query):
         score = 0
         if item['category'] in query['interests']:
             score += 1
         if item['price'] <= query['budget']:
             score += 1
         if item['location'] == query['destination']:
             score += 1
         return score
     ```

2. **Suodatus ja lajittelu**:
   - Poista epäolennaiset kohteet ja järjestä jäljelle jääneet olennaisuuspisteiden mukaan.
   - Esimerkki:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Palauta 10 parasta aiheeseen liittyvää kohdetta
     ```

3. **Luonnollisen kielen käsittely (NLP)**:
   - Käytä NLP-tekniikoita ymmärtämään käyttäjän kysely ja hakemaan relevanttia tietoa.
   - Esimerkki:

     ```python
     def process_query(query):
         # Käytä luonnollisen kielen käsittelyä (NLP) avaintietojen poimimiseen käyttäjän kyselystä
         processed_query = nlp(query)
         return processed_query
     ```

4. **Käyttäjäpalautteen integrointi**:
   - Kerää käyttäjäpalautetta annetuista suosituksista ja hyödynnä sitä tulevien olennaisuusarvioiden säätämiseen.
   - Esimerkki:

     ```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```

#### Esimerkki: Olennaisuuden arviointi matkatoimistossa

Tässä on käytännön esimerkki siitä, miten Travel Agent voi arvioida matkasuositusten olennaisuutta:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        ranked_hotels = self.filter_and_rank(hotels, self.user_preferences)
        itinerary = create_itinerary(flights, ranked_hotels, attractions)
        return itinerary

    def filter_and_rank(self, items, query):
        ranked_items = sorted(items, key=lambda item: self.relevance_score(item, query), reverse=True)
        return ranked_items[:10]  # Palauta 10 parasta asiaankuuluvaa kohdetta

    def relevance_score(self, item, query):
        score = 0
        if item['category'] in query['interests']:
            score += 1
        if item['price'] <= query['budget']:
            score += 1
        if item['location'] == query['destination']:
            score += 1
        return score

    def adjust_based_on_feedback(self, feedback, items):
        for item in items:
            if item['name'] in feedback['liked']:
                item['relevance'] += 1
            if item['name'] in feedback['disliked']:
                item['relevance'] -= 1
        return items

# Esimerkkikäyttö
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_items = travel_agent.adjust_based_on_feedback(feedback, itinerary['hotels'])
print("Updated Itinerary with Feedback:", updated_items)
```

### Hakeminen tarkoituksen mukaan

Hakeminen tarkoituksen mukaan tarkoittaa käyttäjän kyselyn taustalla olevan tarkoituksen tai päämäärän ymmärtämistä ja tulkintaa, jotta voidaan hakea ja tuottaa kaikkein relevantinta ja hyödyllisintä tietoa. Tämä lähestymistapa menee pelkästään avainsanojen vastaamisen ohi ja keskittyy käyttäjän todellisten tarpeiden ja kontekstin hahmottamiseen.

#### Hakemisen keskeiset käsitteet tarkoituksen mukaan

1. **Käyttäjän tarkoituksen ymmärtäminen**:
   - Käyttäjän tarkoitus voidaan jakaa kolmeen päätyyppiin: informatiivinen, navigointiin liittyvä ja transaktiivinen.
     - **Informatiivinen tarkoitus**: Käyttäjä hakee tietoa aiheesta (esim. "Mitkä ovat Pariisin parhaat museot?").
     - **Navigointitarkoitus**: Käyttäjä haluaa siirtyä tietylle verkkosivulle tai sivulle (esim. "Louvre-museon virallinen sivu").
     - **Transaktiivinen tarkoitus**: Käyttäjä haluaa suorittaa toimenpiteen, kuten lentolipun varauksen tai ostoksen tekemisen (esim. "Varaa lento Pariisiin").

2. **Kontekstin ymmärtäminen**:
   - Käyttäjän kyselyn kontekstin analysointi auttaa tarkoituksen tarkassa tunnistamisessa. Tämä sisältää aiemmat vuorovaikutukset, käyttäjän mieltymykset ja nykyisen kyselyn yksityiskohdat.

3. **Luonnollisen kielen käsittely (NLP)**:
   - NLP-tekniikoita käytetään ymmärtämään ja tulkitsemaan käyttäjien antamia luonnollisen kielen kyselyitä. Tämä sisältää tehtäviä kuten entiteettien tunnistus, sentimenttianalyysi ja kyselyiden jäsentäminen.

4. **Personalisointi**:
   - Hakutulosten personointi käyttäjän historian, mieltymysten ja palautteen perusteella parantaa haetun tiedon relevanssia.

#### Käytännön esimerkki: Hakeminen tarkoituksen mukaan matkatoimistossa

Otetaan Travel Agent -esimerkki nähdäksesi, miten hakeminen tarkoituksen mukaan voidaan toteuttaa.

1. **Käyttäjän mieltymysten keruu**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Käyttäjän tarkoituksen ymmärtäminen**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Kontekstin ymmärtäminen**


   ```python
   def analyze_context(query, user_history):
       # Yhdistä nykyinen kysely käyttäjän historiallisen tiedon kanssa ymmärtääksesi yhteyden
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Etsi ja personoi tuloksia**

   ```python
   def search_with_intent(query, preferences, user_history):
       intent = identify_intent(query)
       context = analyze_context(query, user_history)
       if intent == "informational":
           search_results = search_information(query, preferences)
       elif intent == "navigational":
           search_results = search_navigation(query)
       elif intent == "transactional":
           search_results = search_transaction(query, preferences)
       personalized_results = personalize_results(search_results, user_history)
       return personalized_results

   def search_information(query, preferences):
       # Esimerkki hakulogiikasta tiedonhankintatarkoitukseen
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Esimerkki hakulogiikasta navigointitarkoitukseen
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Esimerkki hakulogiikasta kaupalliseen tarkoitukseen
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Esimerkki personointilogiikasta
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Palauta 10 parasta personoitua tulosta
   ```

5. **Esimerkkikäyttö**

   ```python
   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   user_history = ["Louvre Museum website", "Book flight to Paris"]
   query = "best museums in Paris"
   results = search_with_intent(query, preferences, user_history)
   print("Search Results:", results)
   ```

---

## 4. Koodin generointi työkaluna

Koodia generoivat agentit käyttävät tekoälymalleja kirjoittaakseen ja suorittaakseen koodia, ratkaistakseen monimutkaisia ongelmia ja automatisoidakseen tehtäviä.

### Koodia generoivat agentit

Koodia generoivat agentit käyttävät generatiivisia tekoälymalleja kirjoittaakseen ja suorittaakseen koodia. Nämä agentit voivat ratkaista monimutkaisia ongelmia, automatisoida tehtäviä ja tarjota arvokkaita oivalluksia generoimalla ja suorittamalla koodia eri ohjelmointikielillä.

#### Käytännön sovelluksia

1. **Automaattinen koodin generointi**: Generoi koodinpätkiä tiettyihin tehtäviin, kuten data-analyysiin, web-scrapaukseen tai koneoppimiseen.
2. **SQL RAG:ina**: Käytä SQL-kyselyitä tietokantojen tietojen hakemiseen ja käsittelyyn.
3. **Ongelmanratkaisu**: Luo ja suorita koodia ratkaistaksesi tiettyjä ongelmia, kuten algoritmien optimointia tai datan analysointia.

#### Esimerkki: Koodia generoiva agentti data-analyysiin

Kuvittele, että suunnittelet koodia generoivaa agenttia. Näin se voisi toimia:

1. **Tehtävä**: Analysoi tietojoukkoa trendien ja mallien tunnistamiseksi.
2. **Vaiheet**:
   - Lataa tietojoukko data-analyysityökaluun.
   - Generoi SQL-kyselyt datan suodattamiseksi ja yhdistelemiseksi.
   - Suorita kyselyt ja hae tulokset.
   - Käytä tuloksia luodaksesi visualisointeja ja oivalluksia.
3. **Vaadittavat resurssit**: Pääsy tietojoukkoon, data-analyysityökalut ja SQL-osaaminen.
4. **Kokemus**: Käytä aiempia analyysituloksia parantaaksesi tulevien analyysien tarkkuutta ja merkityksellisyyttä.

### Esimerkki: Koodia generoiva agentti matkatoimistolle

Tässä esimerkissä suunnittelemme koodia generoivan agentin, Travel Agentin, auttamaan käyttäjiä matkasuunnitelman tekemisessä generoimalla ja suorittamalla koodia. Tämä agentti voi hoitaa tehtäviä kuten matkavaihtoehtojen hakeminen, tulosten suodattaminen ja matkasuunnitelman kokoaminen generatiivisen tekoälyn avulla.

#### Koodia generoivan agentin yleiskuvaus

1. **Käyttäjän mieltymysten kerääminen**: Kokoaa käyttäjän syötteitä, kuten määränpää, matkustuspäivät, budjetti ja kiinnostuksen kohteet.
2. **Koodin generointi tiedon hakemiseen**: Generoi koodinpätkiä lentojen, hotellien ja nähtävyyksien tietojen hakemiseksi.
3. **Generoidun koodin suoritus**: Suorittaa generoidun koodin reaaliaikaisen tiedon hakemiseksi.
4. **Matkasuunnitelman laadinta**: Kokoaa haetut tiedot personoiduksi matkasuunnitelmaksi.
5. **Palauteperusteiset säädöt**: Vastaanottaa käyttäjäpalautetta ja generoi koodin uudelleen tarvittaessa tulosten tarkentamiseksi.

#### Askel askeleelta toteutus

1. **Käyttäjän mieltymysten kerääminen**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Koodin generointi tiedon hakemiseen**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Esimerkki: Luo koodi lentojen etsimiseen käyttäjän mieltymysten perusteella
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Esimerkki: Luo koodi hotellien etsimiseen
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **Generoidun koodin suoritus**

   ```python
   def execute_code(code):
       # Suorita luotu koodi käyttämällä execiä
       exec(code)
       result = locals()
       return result

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   
   flight_code = generate_code_to_fetch_data(preferences)
   hotel_code = generate_code_to_fetch_hotels(preferences)
   
   flights = execute_code(flight_code)
   hotels = execute_code(hotel_code)

   print("Flight Options:", flights)
   print("Hotel Options:", hotels)
   ```

4. **Matkasuunnitelman laadinta**

   ```python
   def generate_itinerary(flights, hotels, attractions):
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   attractions = search_attractions(preferences)
   itinerary = generate_itinerary(flights, hotels, attractions)
   print("Suggested Itinerary:", itinerary)
   ```

5. **Palauteperusteiset säädöt**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Säädä asetuksia käyttäjäpalautteen perusteella
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Luo ja suorita koodi uudelleen päivitettyjen asetusten kanssa
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Ympäristötietoisuuden ja päättelyn hyödyntäminen

Taulun skeeman perusteella voidaan todella parantaa kyselyjen generointiprosessia hyödyntämällä ympäristötietoisuutta ja päättelyä.

Tässä esimerkki siitä, miten tämä voidaan tehdä:

1. **Skeeman ymmärtäminen**: Järjestelmä ymmärtää taulun skeeman ja käyttää tätä tietoa kyselyjen perustana.
2. **Palauteperusteiset säädöt**: Järjestelmä säätää käyttäjän mieltymyksiä palautteen perusteella ja päättää, mitkä skeeman kentät täytyy päivittää.
3. **Kyselyjen generointi ja suoritus**: Järjestelmä generoi ja suorittaa kyselyjä päivitettyjen mieltymysten perusteella lentojen ja hotellien tietojen hakemiseksi.

Tässä päivitetty Python-koodiesimerkki, joka sisältää nämä käsitteet:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Säädä asetuksia käyttäjäpalautteen perusteella
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Päättely kaavion perusteella muiden siihen liittyvien asetusten säätämiseksi
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Mukautettu logiikka asetusten säätämiseksi kaavion ja palautteen perusteella
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Luo koodi lentotietojen hakemiseen päivitettyjen asetusten perusteella
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Luo koodi hotellitietojen hakemiseen päivitettyjen asetusten perusteella
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simuloi koodin suorittamista ja palauta näytetietoja
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Luo matkareitti lentojen, hotellien ja nähtävyyksien perusteella
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Esimerkkikaavio
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Esimerkkikäyttö
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Luo uudelleen ja suorita koodi päivitettyjen asetusten kanssa
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Selitys – Varaaminen palautteen perusteella

1. **Skeematietoisuus**: `schema`-sanakirja määrittelee, miten mieltymyksiä säädetään palautteen perusteella. Se sisältää kenttiä kuten `favorites` ja `avoid`, niiden vastaavine säädöksineen.
2. **Mieltymysten säätö (`adjust_based_on_feedback`-metodi)**: Tämä metodi säätää mieltymyksiä käyttäjäpalautteen ja skeeman perusteella.
3. **Ympäristöperusteiset säädöt (`adjust_based_on_environment`-metodi)**: Tämä metodi mukauttaa säädöt skeeman ja palautteen pohjalta.
4. **Kyselyjen generointi ja suoritus**: Järjestelmä generoi koodin päivitetyistä mieltymyksistä lentojen ja hotellien tietojen hankkimiseksi ja simuloi kyselyjen suorittamista.
5. **Matkasuunnitelman generointi**: Järjestelmä luo päivitetyn matkasuunnitelman uusien lentojen, hotellien ja nähtävyyksien tietojen perusteella.

Tekemällä järjestelmästä ympäristötietoinen ja päättelyyn perustuvan skeeman avulla, se pystyy generoimaan tarkempia ja merkityksellisempiä kyselyitä, mikä johtaa parempiin matkasuosituksiin ja henkilökohtaisempaan käyttäjäkokemukseen.

### SQL:n käyttö Retrieval-Augmented Generation (RAG) -tekniikkana

SQL (Structured Query Language) on tehokas työkalu tietokantojen kanssa kommunikointiin. Retrieval-Augmented Generation (RAG) -lähestymistavassa SQL voi hakea asiaankuuluvaa tietoa tietokannoista informoimaan ja generoimaan vastauksia tai toimintoja AI-agenteille. Tarkastellaan, miten SQL:ää voidaan käyttää RAG-tekniikkana Travel Agentin kontekstissa.

#### Keskeiset käsitteet

1. **Tietokantainteraktio**:
   - SQL:ää käytetään tietokantojen kyselyyn, asianmukaisen tiedon hakemiseen ja datan käsittelyyn.
   - Esimerkki: Lentojen tiedot, hotellitiedot ja nähtävyydet matkailutietokannasta.

2. **Integraatio RAG:n kanssa**:
   - SQL-kyselyt generoidaan käyttäjän syötteen ja mieltymysten perusteella.
   - Haettua tietoa käytetään personoitujen suositusten tai toimintojen generointiin.

3. **Dynaaminen kyselyjen generointi**:
   - AI-agentti generoi dynaamisia SQL-kyselyitä kontekstin ja käyttäjän tarpeiden mukaan.
   - Esimerkki: Räätälöidyt SQL-kyselyt tulosten suodattamiseen budjetin, päivien ja kiinnostuksen kohteiden mukaan.

#### Sovellukset

- **Automaattinen koodin generointi**: Generoi koodinpätkiä tiettyihin tehtäviin.
- **SQL RAG:ina**: Käytä SQL-kyselyjä datan käsittelyyn.
- **Ongelmanratkaisu**: Luo ja suorita koodia ongelmien ratkaisemiseksi.

**Esimerkki**:
Data-analyysiagentti:

1. **Tehtävä**: Analysoi tietojoukkoa trendien löytämiseksi.
2. **Vaiheet**:
   - Lataa tietojoukko.
   - Generoi SQL-kyselyt datan suodattamiseksi.
   - Suorita kyselyt ja hae tulokset.
   - Generoi visualisointeja ja oivalluksia.
3. **Resurssit**: Tietojoukkojen pääsy, SQL-osaaminen.
4. **Kokemus**: Käytä aiempia tuloksia parantaaksesi tulevia analyysejä.

#### Käytännön esimerkki: SQL:n käyttö Travel Agentissa

1. **Käyttäjän mieltymysten kerääminen**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **SQL-kyselyjen generointi**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **SQL-kyselyjen suoritus**

   ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ```

4. **Suositusten generointi**

   ```python
   def generate_recommendations(preferences):
       flight_query = generate_sql_query("flights", preferences)
       hotel_query = generate_sql_query("hotels", preferences)
       attraction_query = generate_sql_query("attractions", preferences)
       
       flights = execute_sql_query(flight_query)
       hotels = execute_sql_query(hotel_query)
       attractions = execute_sql_query(attraction_query)
       
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   itinerary = generate_recommendations(preferences)
   print("Suggested Itinerary:", itinerary)
   ```

#### Esimerkkejä SQL-kyselyistä

1. **Lentohaku**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Hotellihaku**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Nähtävyyshaku**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Hyödyntämällä SQL:ää osana Retrieval-Augmented Generation (RAG) -tekniikkaa, AI-agentit kuten Travel Agent voivat dynaamisesti palauttaa ja hyödyntää asiaankuuluvaa dataa tarjotakseen tarkkoja ja personoituja suosituksia.

### Esimerkki metakognitiosta

Metakognition toteutuksen demonstroimiseksi luodaan yksinkertainen agentti, joka *reflektoi päätöksentekoprosessiaan* ongelman ratkaisemisen aikana. Tässä esimerkissä rakennamme järjestelmän, jossa agentti yrittää optimoida hotellivalintaa, mutta arvioi sitten omaa päättelyään ja säätää strategiaansa virheiden tai alisuoriutumisen ilmetessä.

Simuloimme tätä yksinkertaisella esimerkillä, jossa agentti valitsee hotellit hinnan ja laadun yhdistelmän perusteella, mutta "reflektoi" päätöksiään ja säätää toimintaa sen mukaisesti.

#### Miten tämä havainnollistaa metakognitiota:

1. **Alustava päätös**: Agentti valitsee halviten hotellin ymmärtämättä laatutekijöitä.
2. **Reflektio ja arviointi**: Alkuvalinnan jälkeen agentti tarkistaa käyttäjäpalautteen perusteella, onko hotelli ollut "huono" valinta. Jos laatu on ollut heikko, agentti reflektoi päättelyään.
3. **Strategian säätö**: Agentti säätää strategiaansa reflektioperusteisesti siirtyen "halvimpaan" valinnasta "parhaaseen laatuun", parantaen päätöksentekoa tulevilla kerroilla.

Tässä esimerkki:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Tallentaa aiemmin valitut hotellit
        self.corrected_choices = []  # Tallentaa korjatut valinnat
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Saatavilla olevat strategiat

    def recommend_hotel(self, hotels, strategy):
        """
        Recommend a hotel based on the chosen strategy.
        The strategy can either be 'cheapest' or 'highest_quality'.
        """
        if strategy == 'cheapest':
            recommended = min(hotels, key=lambda x: x['price'])
        elif strategy == 'highest_quality':
            recommended = max(hotels, key=lambda x: x['quality'])
        else:
            recommended = None
        self.previous_choices.append((strategy, recommended))
        return recommended

    def reflect_on_choice(self):
        """
        Reflect on the last choice made and decide if the agent should adjust its strategy.
        The agent considers if the previous choice led to a poor outcome.
        """
        if not self.previous_choices:
            return "No choices made yet."

        last_choice_strategy, last_choice = self.previous_choices[-1]
        # Oletetaan, että meillä on käyttäjäpalautetta, joka kertoo oliko viimeinen valinta hyvä vai ei
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Säädä strategiaa, jos edellinen valinta oli tyydyttämätön
            new_strategy = 'highest_quality' if last_choice_strategy == 'cheapest' else 'cheapest'
            self.corrected_choices.append((new_strategy, last_choice))
            return f"Reflecting on choice. Adjusting strategy to {new_strategy}."
        else:
            return "The choice was good. No need to adjust."

    def get_user_feedback(self, hotel):
        """
        Simulate user feedback based on hotel attributes.
        For simplicity, assume if the hotel is too cheap, the feedback is "bad".
        If the hotel has quality less than 7, feedback is "bad".
        """
        if hotel['price'] < 100 or hotel['quality'] < 7:
            return "bad"
        return "good"

# Simuloi hotellilista (hinta ja laatu)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Luo agentti
agent = HotelRecommendationAgent()

# Vaihe 1: Agentti suosittelee hotellia käyttäen "halvin" -strategiaa
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Vaihe 2: Agentti arvioi valinnan uudelleen ja säätää strategiaa tarvittaessa
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Vaihe 3: Agentti suosittelee uudelleen, tällä kertaa käyttäen säädettyä strategiaa
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Agenttien metakognitiotaidot

Keskeistä on agentin kyky:
- Arvioida aiempia valintojaan ja päätöksentekoprosessiaan.
- Säätää strategiaansa sen reflektioperusteisesti eli metakognition ilmentymänä.

Tämä on yksinkertainen metakognition muoto, jossa järjestelmä pystyy säätämään päättelyään sisäisen palautteen perusteella.

### Yhteenveto

Metakognitio on voimakas työkalu, joka voi merkittävästi parantaa tekoälyagenttien kyvykkyyksiä. Sisällyttämällä metakognitiiviset prosessit voit suunnitella agentteja, jotka ovat älykkäämpiä, sopeutuvampia ja tehokkaampia. Hyödynnä lisäresursseja tutkiaksesi metakognition kiehtovaa maailmaa tekoälyagenteissa.

### Onko sinulla lisää kysymyksiä metakognition suunnittelumallista?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tavata muita oppijoita, osallistu toimistoaikoihin ja saa vastauksia AI-agenttikysymyksiisi.

## Edellinen oppitunti

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

## Seuraava oppitunti

[AI Agents in Production](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->