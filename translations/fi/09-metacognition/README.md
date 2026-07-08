[![Moniagenttinen suunnittelu](../../../translated_images/fi/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Klikkaa yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_
# Metakognitio tekoälyagenttien parissa

## Johdanto

Tervetuloa oppitunnille tekoälyagenttien metakognitiosta! Tämä luku on suunnattu aloittelijoille, jotka ovat uteliaita siitä, miten tekoälyagentit voivat ajatella omia ajatteluprosessejaan. Oppitunnin lopussa ymmärrät keskeiset käsitteet ja saat käytännön esimerkkejä metakognition soveltamisesta tekoälyagenttien suunnittelussa.

## Oppimistavoitteet

Oppitunnin suorittamisen jälkeen osaat:

1. Ymmärtää päättelysilmukoiden vaikutukset agenttien määritelmissä.
2. Käyttää suunnittelu- ja arviointitekniikoita itsekorjaavien agenttien tukemiseksi.
3. Luoda omia agenteja, jotka osaavat käsitellä koodia tehtävien suorittamiseksi.

## Johdatus metakognitioon

Metakognitio tarkoittaa korkeammantasoista kognitiivista prosessia, jossa ajatellaan omaa ajattelua. Tekoälyagenttien kohdalla tämä tarkoittaa kykyä arvioida ja säätää toimintaansa itsetietoisuuden ja aiempien kokemusten perusteella. Metakognitio eli "ajatteleminen ajattelemisesta" on tärkeä käsite agenttipohjaisten tekoälyjärjestelmien kehityksessä. Se tarkoittaa, että tekoälyjärjestelmät ovat tietoisia omista sisäisistä prosesseistaan ja pystyvät seuraamaan, säätelemään ja sopeuttamaan käytöstään sen mukaisesti. Aivan kuten me teemme, kun luemme tilannetta tai tarkastelemme ongelmaa. Tämä itsetietoisuus voi auttaa tekoälyjärjestelmiä tekemään parempia päätöksiä, havaitsemaan virheitä ja parantamaan suorituskykyään ajan mittaan – mikä yhdistää tämän Turingin testiin ja keskusteluun siitä, valtaavatko tekoälyt vallan.

Agenttipohjaisten tekoälyjärjestelmien yhteydessä metakognitio voi auttaa ratkaisemaan useita haasteita, kuten:
- Läpinäkyvyys: Varmistaa, että tekoälyjärjestelmät voivat selittää päättelynsä ja päätöksensä.
- Päättely: Parantaa tekoälyjärjestelmien kykyä yhdistää tietoa ja tehdä perusteltuja päätöksiä.
- Sopeutuminen: Mahdollistaa tekoälyjärjestelmien mukautumisen uusiin ympäristöihin ja muuttuviin olosuhteisiin.
- Havaitseminen: Parantaa tekoälyjärjestelmien tarkkuutta tunnistaa ja tulkita ympäristöstään saatua dataa.

### Mitä on metakognitio?

Metakognitio eli "ajatteleminen ajattelusta" on korkeantasoista kognitiivista prosessia, johon kuuluu itsetietoisuus ja oman kognitioprosessinsa itseohjaus. Tekoälyn alalla metakognitio antaa agenteille mahdollisuuden arvioida ja mukauttaa strategioitaan ja toimiaan, mikä johtaa parempiin ongelmanratkaisu- ja päätöksentekokykyihin. Ymmärtämällä metakognition voit suunnitella tekoälyagentteja, jotka eivät ole vain älykkäämpiä vaan myös sopeutuvampia ja tehokkaampia. Todellisessa metakognitiossa tekoäly siis selvästi pohdiskelee omaa päättelyään.

Esimerkki: "Priorisoin edullisempia lentoja, koska… saatankin jäädä paitsi suorista lennoista, joten tarkistan vielä uudelleen."
Seuraa, miten tai miksi se valitsi tietyn reitin.
- Huomaa tehneensä virheitä, koska se luotti liikaa käyttäjän aiempiin mieltymyksiin, joten se muuttaa päätöksentekostrategiaansa, ei vain lopullista suositusta.
- Diagnosoi malleja kuten: "Aina kun vastaan käsitelee 'liian tungosta', minun ei pitäisi ainoastaan poistaa tiettyjä nähtävyyksiä, vaan myös heijastaa, että tapani valita 'top nähtävyydet' on virheellinen, jos arvotan aina suosion perusteella."

### Metakognition merkitys tekoälyagenteissa

Metakognitio näyttelee ratkaisevaa roolia tekoälyagenttien suunnittelussa useista syistä:

![Metakognition merkitys](../../../translated_images/fi/importance-of-metacognition.b381afe9aae352f7.webp)

- Itsetutkiskelu: Agentit voivat arvioida omaa suorituskykyään ja tunnistaa parantamisen kohteita.
- Sopeutumiskyky: Agentit voivat muuttaa strategioitaan aiempien kokemusten ja muuttuvien ympäristöjen mukaan.
- Virheiden korjaus: Agentit voivat itse havaita ja korjata virheitä, mikä johtaa tarkempiin tuloksiin.
- Resurssien hallinta: Agentit voivat optimoida resurssien, kuten ajan ja laskentatehon, käyttöä suunnittelemalla ja arvioimalla toimintaansa.

## Tekoälyagentin osat

Ennen kuin sukellamme metakognitiivisiin prosesseihin, on tärkeää ymmärtää tekoälyagentin perusosat. Tekoälyagentti koostuu tyypillisesti:

- Persoona: Agentin persoonallisuus ja ominaisuudet, jotka määrittävät sen vuorovaikutuksen käyttäjien kanssa.
- Työkalut: Kyvyt ja toiminnot, joita agentti voi suorittaa.
- Taidot: Agentin hallussa oleva tieto ja asiantuntemus.

Nämä osat toimivat yhdessä luodakseen "asiantuntijayksikön", joka voi suorittaa tiettyjä tehtäviä.

**Esimerkki**:
Ajattele matka-agenttia, agenttipalvelua joka ei ainoastaan suunnittele lomasi, vaan myös mukauttaa reittiään reaaliaikaisen datan ja aiempien asiakkaiden kokemusten perusteella.

### Esimerkki: Metakognitio matka-agenttipalvelussa

Kuvittele, että suunnittelet tekoälyllä toimivaa matka-agenttipalvelua. Tämä agentti, "Matka Agentti", auttaa käyttäjiä lomien suunnittelussa. Metakognition sisällyttämiseksi Matka Agentin on arvioitava ja muutettava toimintaansa itsetietoisuuden ja aiempien kokemusten perusteella. Näin metakognitio voisi näkyä:

#### Nykyinen tehtävä

Nykyinen tehtävä on auttaa käyttäjää suunnittelemaan matka Pariisiin.

#### Vaiheet tehtävän suorittamiseksi

1. **Käyttäjän mieltymyksien kerääminen**: Kysytään käyttäjältä matkapäivät, budjetti, kiinnostuksen kohteet (esim. museot, ruoka, shoppailu) ja erityisvaatimukset.
2. **Tiedon hakeminen**: Etsitään lentovaihtoehtoja, majoituksia, nähtävyyksiä ja ravintoloita, jotka vastaavat käyttäjän mieltymyksiä.
3. **Suositusten luominen**: Tarjotaan henkilökohtainen matkasuunnitelma, johon sisältyy lentotiedot, hotellivaraukset ja ehdotetut aktiviteetit.
4. **Palautteen perusteella säätäminen**: Kysytään käyttäjältä palautetta suosituksista ja tehdään tarvittavat muutokset.

#### Vaadittavat resurssit

- Pääsy lento- ja hotellivarauksia koskeviin tietokantoihin.
- Tietoa pariisilaisista nähtävyyksistä ja ravintoloista.
- Käyttäjäpalautetiedot aiemmista vuorovaikutuksista.

#### Kokemus ja itsetutkiskelu

Matka Agentti käyttää metakognitiota arvioidakseen suorituskykyään ja oppiakseen aiemmista kokemuksista. Esimerkiksi:

1. **Käyttäjäpalautteen analysointi**: Matka Agentti tarkastelee käyttäjäpalautetta määrittääkseen, mitkä suositukset otettiin hyvin vastaan ja mitkä eivät. Se säätää tulevia ehdotuksiaan sen mukaisesti.
2. **Sopeutumiskyky**: Jos käyttäjä on aiemmin maininnut viihtyvänsä ei-ruuhkaisissa paikoissa, Matka Agentti välttää suosittelemasta suosittuja turistinähtävyyksiä ruuhka-aikoina tulevaisuudessa.
3. **Virheiden korjaus**: Jos Matka Agentti teki virheen aiemmassa varauksessa, kuten ehdotti täyteen varattua hotellia, se oppii tarkistamaan saatavuuden huolellisemmin ennen suosituksia.

#### Käytännön kehittäjäesimerkki

Tässä on yksinkertaistettu esimerkki siitä, miltä Matka Agentin koodi voi näyttää metakognition sisällyttämisen yhteydessä:

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

- **Itsetutkiskelu**: Agentit voivat analysoida omaa suorituskykyään ja tunnistaa parannuskohteita.
- **Sopeutumiskyky**: Agentit voivat muuttaa strategioitaan palautteen ja muuttuvien olosuhteiden perusteella.
- **Virheiden korjaus**: Agentit voivat itsenäisesti havaita ja korjata virheitä.
- **Resurssien hallinta**: Agentit voivat optimoida resurssien, kuten ajan ja laskentatehon, käyttöä.

Sisällyttämällä metakognition Matka Agentti voi tarjota henkilökohtaisempia ja tarkempia matkasuosituksia, parantaen käyttäjäkokemusta kokonaisuudessaan.

---

## 2. Suunnittelu agenteissa

Suunnittelu on keskeinen osa tekoälyagenttien käyttäytymistä. Se sisältää tavoitteeseen tähtäävien vaiheiden kuvaamisen ottaen huomioon nykyinen tila, resurssit ja mahdolliset esteet.

### Suunnittelun elementit

- **Nykyinen tehtävä**: Määritä tehtävä selkeästi.
- **Vaiheet tehtävän suorittamiseksi**: Pilko tehtävä hallittaviksi osiksi.
- **Vaadittavat resurssit**: Tunnista tarvittavat resurssit.
- **Kokemus**: Hyödynnä aiempia kokemuksia suunnittelun tukena.

**Esimerkki**:
Tässä ovat vaiheet, jotka Matka Agentin tulee ottaa auttaessaan käyttäjää suunnittelemaan matkaa tehokkaasti:

### Vaiheet Matka Agentille

1. **Käyttäjän mieltymyksien kerääminen**
   - Kysy käyttäjältä tietoja matkapäivistä, budjetista, kiinnostuksen kohteista ja erityisvaatimuksista.
   - Esimerkkejä: "Milloin aiot matkustaa?" "Mikä on budjettisi?" "Mitä aktiviteetteja nautit lomalla?"

2. **Tiedon hakeminen**
   - Etsi käyttäjän mieltymysten mukaiset matkavaihtoehdot.
   - **Lennot**: Etsi käyttäjän budjettiin ja matkustusajankohtaan sopivia lentoja.
   - **Majoitus**: Löydä hotelleja tai vuokrakohteita, jotka vastaavat käyttäjän sijainti-, hinta- ja palvelutoiveita.
   - **Nähtävyydet ja ravintolat**: Tunnista suosittuja nähtävyyksiä, aktiviteetteja ja ruokapaikkoja, jotka sopivat käyttäjän kiinnostuksen kohteisiin.

3. **Suositusten luominen**
   - Koosta kerätty tieto henkilökohtaiseksi matkasuunnitelmaksi.
   - Sisällytä tiedot, kuten lentovaihtoehdot, hotellivaraukset ja ehdotetut aktiviteetit, huolehtien, että suositukset ovat käyttäjän mieltymysten mukaisia.

4. **Esittele matkasuunnitelma käyttäjälle**
   - Jaa ehdotettu matkasuunnitelma käyttäjän arvioitavaksi.
   - Esimerkki: "Tässä on ehdotettu matkasuunnitelma Pariisin matkallesi. Se sisältää lentotiedot, hotellivaraukset ja listan suositelluista aktiviteeteista ja ravintoloista. Kerro mielipiteesi!"

5. **Palautteen kerääminen**
   - Kysy käyttäjältä palautetta ehdotetusta matkasuunnitelmasta.
   - Esimerkkejä: "Pidätkö lentovaihtoehdoista?" "Sopiiko hotelli tarpeisiisi?" "Haluatko lisätä tai poistaa jotain aktiviteetteja?"

6. **Säätäminen palautteen perusteella**
   - Muokkaa matkasuunnitelmaa käyttäjän palautteen mukaisesti.
   - Tee tarvittavat muutokset lentojen, majoituksen ja aktiviteettien suosituksiin, jotta ne vastaavat paremmin käyttäjän mieltymyksiä.

7. **Lopullinen vahvistus**
   - Esittele päivitetty matkasuunnitelma käyttäjälle lopullista vahvistusta varten.
   - Esimerkki: "Teen muutokset palautteesi perusteella. Tässä on päivitetty matkasuunnitelma. Näyttääkö kaikki hyvältä?"

8. **Varaukset ja vahvistukset**
   - Kun käyttäjä hyväksyy suunnitelman, etene lentojen, majoituksen ja suunniteltujen aktiviteettien varaamiseen.
   - Lähetä vahvistustiedot käyttäjälle.

9. **Jatkuva tuki**
   - Ole käytettävissä auttamaan käyttäjää muutoksissa tai lisäpyynnöissä ennen ja matkan aikana.
   - Esimerkki: "Jos tarvitset lisäapua matkan aikana, ota rohkeasti yhteyttä milloin tahansa!"

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

# Esimerkki käytöstä buukkauksia pyytäessä
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

RAG yhdistää haun ja generatiivisen mallin. Kun tehdään kysely, hakujärjestelmä hakee asiaankuuluvia dokumentteja tai tietoja ulkoisesta lähteestä, ja tämä haettu tieto lisätään syötteeseen generatiiviselle mallille. Tämä auttaa mallia luomaan tarkempia ja kontekstin mukaisia vastauksia.

RAG-järjestelmässä agentti hakee tietoa tietokannasta ja käyttää sitä sopivien vastausten tai toimien luomiseen.

### Korjaava RAG-lähestymistapa

Korjaava RAG keskittyy käyttämään RAG-tekniikoita virheiden korjaamiseen ja tekoälyagenttien tarkkuuden parantamiseen. Tämä sisältää:

1. **Kehotusmenetelmä**: Käytetään erityisiä kehotteita ohjaamaan agenttia hakemaan relevanttia tietoa.
2. **Työkalu**: Toteutetaan algoritmeja ja mekanismeja, joiden avulla agentti arvioi haetun tiedon merkitystä ja luo tarkkoja vastauksia.
3. **Arviointi**: Jatkuva agentin suorituskyvyn arviointi ja säätöjen tekeminen tarkkuuden ja tehokkuuden parantamiseksi.

#### Esimerkki: Korjaava RAG hakutagentissa

Mieti hakutagenttia, joka hakee tietoa verkosta vastatakseen käyttäjän kyselyihin. Korjaava RAG -lähestymistapa voisi sisältää:

1. **Kehotusmenetelmä**: Muodostaa hakulausekkeet käyttäjän syötteen perusteella.
2. **Työkalu**: Käyttää luonnollisen kielen käsittelyä ja koneoppimisalgoritmeja hakutulosten järjestämiseen ja suodattamiseen.
3. **Arviointi**: Analysoi käyttäjäpalautetta virheiden tunnistamiseksi ja korjaamiseksi haetussa tiedossa.

### Korjaava RAG matkatoimistossa

Korjaava RAG (Retrieval-Augmented Generation) parantaa tekoälyn kykyä hakea ja tuottaa tietoa samalla korjaten virheellisyydet. Katsotaan miten Matka Agentti voi käyttää Korjaavaa RAG-lähestymistapaa tarjotakseen tarkempia ja olennaisia matkasuosituksia.

Tämä sisältää:

- **Kehotusmenetelmä:** Käytetään erityisiä kehotteita ohjaamaan agenttia hakemaan relevanttia tietoa.
- **Työkalu:** Toteutetaan algoritmeja ja mekanismeja, joiden avulla agentti arvioi haetun tiedon merkitystä ja luo tarkkoja vastauksia.
- **Arviointi:** Jatkuva agentin suorituskyvyn arviointi ja säätöjen tekeminen tarkkuuden ja tehokkuuden parantamiseksi.

#### Vaiheet korjaavan RAG:n toteuttamiseksi Matka Agentissa

1. **Alkuperäinen käyttäjävuorovaikutus**
   - Matka Agentti kerää käyttäjän alkuperäiset mieltymykset, kuten kohteen, matkustuspäivät, budjetin ja kiinnostuksen kohteet.
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
   - Matka Agentti hakee tietoa lennoista, majoituksista, nähtävyyksistä ja ravintoloista käyttäjän mieltymysten perusteella.
   - Esimerkki:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Alkuperäisten suositusten luominen**
   - Matka Agentti käyttää haettua tietoa luodakseen henkilökohtaisen matkasuunnitelman.
   - Esimerkki:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Käyttäjäpalautteen keruu**
   - Matka Agentti pyytää käyttäjältä palautetta alkuperäisistä suosituksista.
   - Esimerkki:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Korjaava RAG-prosessi**
   - **Kehotusmenetelmä**: Matka Agentti muodostaa uudet hakulausekkeet käyttäjäpalautteen perusteella.
     - Esimerkki:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Työkalu**: Matka Agentti käyttää algoritmeja uusien hakutulosten järjestämiseen ja suodattamiseen korostaen käyttäjäpalautteen merkitystä.
     - Esimerkki:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Arviointi**: Matka Agentti arvioi jatkuvasti suositustensa relevanssia ja tarkkuutta analysoimalla käyttäjäpalautetta ja tekemällä tarvittavat säädöt.
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

Tässä on yksinkertaistettu Python-koodi, joka sisältää korjaavan RAG-lähestymistavan Matka Agentissa:

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


Ennakoiva kontekstin lataus tarkoittaa, että mallille ladataan sopiva konteksti tai taustatietoa ennen kyselyn käsittelyä. Tämä tarkoittaa, että mallilla on pääsy tähän tietoon alusta alkaen, mikä auttaa sitä tuottamaan paremmin informoituja vastauksia ilman tarvetta hakea lisätietoja prosessin aikana.

Tässä on yksinkertaistettu esimerkki siitä, miltä ennakoiva kontekstin lataus voisi näyttää matkatoimisto-sovelluksessa Pythonilla:

```python
class TravelAgent:
    def __init__(self):
        # Esilataa suosittuja kohteita ja niiden tietoja
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Hae kohdetiedot esiloadatusta kontekstista
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Esimerkkikäyttö
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### Selitys

1. **Alustus (`__init__`-metodi)**: `TravelAgent`-luokka esilataa sanakirjan, joka sisältää tietoa suosituista kohteista, kuten Pariisista, Tokiossa, New Yorkissa ja Sydneyssä. Tämä sanakirja sisältää yksityiskohtia kuten maa, valuutta, kieli ja tärkeimmät nähtävyydet kutakin kohdetta varten.

2. **Tiedon hakeminen (`get_destination_info`-metodi)**: Kun käyttäjä kysyy tietystä kohteesta, `get_destination_info`-metodi hakee asiaankuuluvat tiedot esiladattusta kontekstisanakirjasta.

Esilataamalla konteksti, matkatoimisto-sovellus voi vastata käyttäjän kyselyihin nopeasti ilman, että sen tarvitsee hakea tätä tietoa ulkoisesta lähteestä reaaliajassa. Tämä tekee sovelluksesta tehokkaamman ja nopeamman.

### Suunnitelman käynnistäminen tavoitteella ennen iteraatiota

Suunnitelman käynnistäminen tavoitteella tarkoittaa, että aloitetaan selkeällä päämäärällä tai halutulla lopputuloksella mielessä. Määrittelemällä tämä tavoite aluksi, malli voi käyttää sitä ohjenuorana koko toistuvassa prosessissa. Tämä auttaa varmistamaan, että jokainen iteraatio vie lähemmäs halutun lopputuloksen saavuttamista, tehden prosessista tehokkaamman ja kohdennetumman.

Tässä on esimerkki siitä, kuinka voit käynnistää matkasuunnitelman tavoitteella ennen iteraatiota matkatoimistolle Pythonilla:

### Tilannekuvaus

Matkatoimisto haluaa suunnitella asiakkaalle räätälöidyn lomamatkan. Tavoitteena on luoda matkasuunnitelma, joka maksimoidaan asiakkaan tyytyväisyyden perusteella heidän mieltymystensä ja budjettinsa mukaan.

### Vaiheet

1. Määritä asiakkaan mieltymykset ja budjetti.
2. Käynnistä alkuperäinen suunnitelma näiden mieltymysten perusteella.
3. Iteroi suunnitelmaa sen jalostamiseksi ja asiakkaan tyytyväisyyden optimoimiseksi.

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

1. **Alustus (`__init__`-metodi)**: `TravelAgent`-luokka alustetaan listalla mahdollisia kohteita, joilla on ominaisuuksia kuten nimi, kustannus ja aktiviteettityyppi.

2. **Suunnitelman käynnistäminen (`bootstrap_plan`-metodi)**: Tämä metodi luo alkuperäisen matkasuunnitelman asiakkaan mieltymysten ja budjetin perusteella. Se käy läpi kohdelistan ja lisää kohteet suunnitelmaan, jos ne vastaavat asiakkaan mieltymyksiä ja sopivat budjettiin.

3. **Mieltymysten tarkistaminen (`match_preferences`-metodi)**: Tämä metodi tarkistaa, vastaako kohde asiakkaan mieltymyksiä.

4. **Suunnitelman iterointi (`iterate_plan`-metodi)**: Tämä metodi jalostaa alkuperäistä suunnitelmaa yrittämällä korvata jokainen kohde suunnitelmassa paremmalla vaihtoehdolla, ottaen huomioon asiakkaan mieltymykset ja budjettirajoitukset.

5. **Kustannuksen laskeminen (`calculate_cost`-metodi)**: Tämä metodi laskee nykyisen suunnitelman kokonaiskustannuksen mukaan lukien mahdollinen uusi kohde.

#### Esimerkkikäyttö

- **Alkuperäinen suunnitelma**: Matkatoimisto luo alkuperäisen suunnitelman perustuen asiakkaan nähtävyyksien katselun mieltymyksiin ja 2000 dollarin budjettiin.
- **Jalostettu suunnitelma**: Matkatoimisto iteroi suunnitelmaa optimoiden asiakkaan mieltymyksiä ja budjettia.

Käynnistämällä suunnitelman selkeällä tavoitteella (esim. asiakkaan tyytyväisyyden maksimointi) ja iteroimalla sen jalostamiseksi, matkatoimisto voi luoda asiakkaalle räätälöidyn ja optimoidun matkasuunnitelman. Tämä lähestymistapa varmistaa, että matkasuunnitelma vastaa asiakkaan mieltymyksiä ja budjettia alusta alkaen ja paranee jokaisen iteraation myötä.

### LLM:n hyödyntäminen uudelleenjärjestelyssä ja pisteytyksessä

Suuret kielimallit (LLM:t) voidaan hyödyntää uudelleenjärjestelyssä ja pisteytyksessä arvioimalla haettujen dokumenttien tai tuotettujen vastausten relevanssia ja laatua. Tässä miten se toimii:

**Haku:** Alkuperäinen hakuvaihe tuo joukon ehdokasdokumentteja tai vastauksia kyselyn perusteella.

**Uudelleenjärjestely:** LLM arvioi nämä ehdokkaat ja järjestää ne uudelleen relevanssin ja laadun perusteella. Tämä vaihe varmistaa, että kaikkein relevantin ja laadukkain tieto esitetään ensin.

**Pisteytys:** LLM antaa pisteet jokaiselle ehdokkaalle, heijastaen niiden relevanssia ja laatua. Tämä auttaa valitsemaan parhaan vastauksen tai dokumentin käyttäjälle.

Hyödyntämällä LLM-malleja uudelleenjärjestelyssä ja pisteytyksessä, järjestelmä voi tarjota tarkempaa ja kontekstuaalisesti relevantimpaa tietoa, parantaen käyttäjäkokemusta kokonaisuudessaan.

Tässä on esimerkki siitä, kuinka matkatoimisto voisi käyttää suurta kielimallia (LLM) uudelleenjärjestelyyn ja pisteytykseen matkakohteiden osalta käyttäjän mieltymysten mukaan Pythonilla:

#### Tilannekuvaus – Matkustaminen mieltymysten perusteella

Matkatoimisto haluaa suositella parhaita matkakohteita asiakkaalle hänen mieltymystensä perusteella. LLM auttaa uudelleenjärjestelyssä ja pisteytyksessä varmistaakseen, että kaikkein relevantimmat vaihtoehdot esitetään.

#### Vaiheet:

1. Kerää käyttäjän mieltymykset.
2. Hae lista mahdollisista matkakohteista.
3. Käytä LLM:ää uudelleenjärjestelyyn ja pisteytykseen matkakohteiden perusteella käyttäjän mieltymysten mukaisesti.

Tässä on tapa päivittää edellinen esimerkki käyttämään Azure OpenAI -palveluita:

#### Vaatimukset

1. Sinulla tulee olla Azure-tilaus.
2. Luo Azure OpenAI -resurssi ja hanki API-avain.

#### Esimerkkikoodi Pythonilla

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Luo kehotus Azure OpenAI:lle
        prompt = self.generate_prompt(preferences)
        
        # Määritä otsikot ja sisältö pyynnölle
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

#### Koodin selitys – Mieltymysvaraus

1. **Alustus**: `TravelAgent`-luokka alustetaan listalla mahdollisia matkakohteita, joilla on ominaisuuksia kuten nimi ja kuvaus.

2. **Suositusten hakeminen (`get_recommendations`-metodi)**: Tämä metodi luo kehotuksen Azure OpenAI -palvelulle käyttäjän mieltymysten perusteella ja tekee HTTP POST -pyynnön Azure OpenAI API:hin saadakseen uudelleenjärjestellyt ja pisteytetyt kohteet.

3. **Kehotuksen luominen (`generate_prompt`-metodi)**: Tämä metodi rakentaa kehotuksen Azure OpenAI:lle, mukaan lukien käyttäjän mieltymykset ja kohdelistan. Kehotus ohjaa mallia uudelleenjärjestelemään ja pisteyttämään kohteet annettujen mieltymysten perusteella.

4. **API-kutsu**: `requests`-kirjastoa käytetään tekemään HTTP POST -pyyntö Azure OpenAI -API-päätepisteeseen. Vastaus sisältää uudelleenjärjestellyt ja pisteytetyt kohteet.

5. **Esimerkkikäyttö**: Matkatoimisto kerää käyttäjän mieltymyksiä (esim. kiinnostus nähtävyyksiin ja monipuoliseen kulttuuriin) ja käyttää Azure OpenAI -palvelua saadakseen uudelleenjärjestellyt ja pisteytetyt suositukset matkakohteista.

Varmista, että korvaat `your_azure_openai_api_key` todellisella Azure OpenAI API-avaimellasi ja `https://your-endpoint.com/...` todellisella päätepisteen URL-osoitteella Azure OpenAI -käyttöönotossasi.

Hyödyntämällä LLM:ää uudelleenjärjestelyyn ja pisteytykseen, matkatoimisto voi tarjota henkilökohtaisempia ja relevantimpia matkasuosituksia asiakkaille, parantaen heidän kokonaiskokemustaan.

### RAG: Kehotusmenetelmä vs Työkalu

Hakuun pohjautuva generointi (Retrieval-Augmented Generation, RAG) voi olla sekä kehotusmenetelmä että työkalu AI-agenttien kehityksessä. Ymmärtäminen näiden erosta voi auttaa sinua hyödyntämään RAGia tehokkaammin projekteissasi.

#### RAG kehotusmenetelmänä

**Mikä se on?**

- Kehotusmenetelmänä RAG tarkoittaa tiettyjen kyselyjen tai kehotteiden muodostamista, jotka ohjaavat asiaankuuluvan tiedon hakua suuresta kokoelmasta tai tietokannasta. Tätä tietoa käytetään sitten vastausten tai toimintojen tuottamiseen.

**Miten se toimii:**

1. **Kehota muodostamaan kehotteita**: Luo hyvin jäsenneltyjä kehotteita tai kyselyitä tehtävän tai käyttäjän syötteen perusteella.
2. **Hae tietoa**: Käytä kehotteita hakeaksesi relevanttia dataa olemassa olevasta tietokannasta tai datasetistä.
3. **Tuota vastaus**: Yhdistä haettu tieto generatiivisten AI-mallien kanssa tuottaaksesi kattavan ja johdonmukaisen vastauksen.

**Esimerkki matkatoimistossa**:

- Käyttäjän syöte: "Haluan käydä museoissa Pariisissa."
- Kehotus: "Etsi parhaat museot Pariisissa."
- Haettu tieto: Tietoja Louvre-museosta, Musée d'Orsaysta jne.
- Tuotettu vastaus: "Tässä on joitakin Pariisin parhaista museoista: Louvre, Musée d'Orsay ja Centre Pompidou."

#### RAG työkaluna

**Mikä se on?**

- Työkaluna RAG on integroitu järjestelmä, joka automatisoi hakemisen ja generoinnin prosessin, helpottaen kehittäjiä toteuttamaan monimutkaisia AI-ominaisuuksia ilman yksittäisten kehotteiden käsin luomista.

**Miten se toimii:**

1. **Integrointi**: Upota RAG AI-agentin arkkitehtuuriin, jolloin se hoitaa automaattisesti hakemisen ja generoinnin tehtävät.
2. **Automaatio**: Työkalu hallinnoi koko prosessin käyttäjän syötteen vastaanottamisesta lopullisen vastauksen tuottamiseen ilman erillisiä kehotteita jokaiseen vaiheeseen.
3. **Tehokkuus**: Parantaa agentin suorituskykyä virtaviivaistamalla hakemisen ja generoinnin prosessia, mahdollistaen nopeammat ja tarkemmat vastaukset.

**Esimerkki matkatoimistossa**:

- Käyttäjän syöte: "Haluan käydä museoissa Pariisissa."
- RAG-työkalu: Hakee automaattisesti tietoa museoista ja generoi vastauksen.
- Tuotettu vastaus: "Tässä on joitakin Pariisin parhaista museoista: Louvre, Musée d'Orsay ja Centre Pompidou."

### Vertailu

| Näkökulma              | Kehotusmenetelmä                                      | Työkalu                                               |
|------------------------|-------------------------------------------------------|-------------------------------------------------------|
| **Manuaalinen vs Automaattinen** | Kyselyä kohden manuaalinen kehotteiden laatiminen.     | Hakemisen ja generoinnin automatisoitu prosessi.       |
| **Hallinta**            | Tarjoaa enemmän hallintaa hakuprosessiin.              | Virtaviivaistaa ja automatisoi hakemisen ja generoinnin.|
| **Joustavuus**          | Mahdollistaa räätälöidyt kehotteet tarpeen mukaan.     | Tehokkaampaa laajamittaisissa toteutuksissa.           |
| **Monimutkaisuus**     | Vaatii kehotteiden suunnittelua ja hienosäätöä.        | Helpompi integroida AI-agentin arkkitehtuuriin.         |

### Käytännön esimerkkejä

**Kehotusmenetelmän esimerkki:**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**Työkaluesimerkki:**

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

### Relevanssin arviointi

Relevanssin arviointi on keskeinen osa AI-agentin suorituskykyä. Se varmistaa, että agentin hakema ja tuottama tieto on asianmukaista, tarkkaa ja hyödyllistä käyttäjälle. Tarkastellaan, miten relevanssia arvioidaan AI-agenteissa, mukaan lukien käytännön esimerkkejä ja tekniikoita.

#### Keskeiset käsitteet relevanssin arvioinnissa

1. **Kontekstin ymmärtäminen**:
   - Agentin tulee ymmärtää käyttäjän kyselyn konteksti hakeakseen ja tuottaakseen relevanttia tietoa.
   - Esimerkki: Jos käyttäjä kysyy "parhaat ravintolat Pariisissa," agentin tulee ottaa huomioon käyttäjän mieltymykset, kuten keittiötyyppi ja budjetti.

2. **Tarkkuus**:
   - Agentin tarjoaman tiedon tulee olla tosiasiallisesti oikeaa ja ajantasaista.
   - Esimerkki: Suositellut tällä hetkellä avoinna olevat ravintolat, joilla on hyvät arvostelut, eivät vanhentuneet tai suljetut vaihtoehdot.

3. **Käyttäjän tarkoitus**:
   - Agentin tulee päätellä käyttäjän kyselyn takana oleva tarkoitus tarjotakseen parhaan mahdollisen tiedon.
   - Esimerkki: Jos käyttäjä kysyy "budjettiystävälliset hotellit," agentin tulee priorisoida edulliset vaihtoehdot.

4. **Palautejärjestelmä**:
   - Jatkuva käyttäjäpalautteen keruu ja analysointi auttaa agenttia parantamaan relevanssin arviointiprosessia.
   - Esimerkki: Aiempiin suosituksiin annettujen arvosanojen ja palautteen hyödyntäminen tulevien vastausten parantamiseksi.

#### Käytännön tekniikoita relevanssin arviointiin

1. **Relevanssipisteytys**:
   - Anna jokaiselle haetulle kohteelle relevanssipiste sen mukaan, kuinka hyvin se vastaa käyttäjän kyselyä ja mieltymyksiä.
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
   - Suodata pois epäolennaiset kohteet ja järjestä jäljelle jääneet relevanssipisteiden mukaan.
   - Esimerkki:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Palauta 10 parasta olennaista kohdetta
     ```

3. **Luonnollisen kielen käsittely (NLP)**:
   - Käytä NLP-tekniikoita ymmärtämään käyttäjän kyselyä ja hakemaan relevanttia tietoa.
   - Esimerkki:

     ```python
     def process_query(query):
         # Käytä NLP:tä avaininformaation poimimiseen käyttäjän kyselystä
         processed_query = nlp(query)
         return processed_query
     ```

4. **Käyttäjäpalautteen integrointi**:
   - Kerää käyttäjäpalautetta annetuista suosituksista ja käytä sitä säätämään tulevia relevanssin arviointeja.
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

#### Esimerkki: Relevanssin arviointi matkatoimistossa

Tässä käytännön esimerkki siitä, miten Travel Agent voi arvioida matkasuositusten relevanssia:

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

### Hakeminen käyttötarkoituksen mukaan

Hakeminen käyttötarkoituksen mukaan tarkoittaa käyttäjän kyselyn taustalla olevan tarkoituksen tai tavoitteen ymmärtämistä ja tulkintaa, jotta hakuratkaisu tuottaa kaikkein relevantimman ja hyödyllisimmän tiedon. Tämä lähestymistapa menee pidemmälle kuin pelkkä avainsanojen löytäminen ja keskittyy käyttäjän todellisiin tarpeisiin ja kontekstiin.

#### Keskeiset käsitteet hakemisessa käyttötarkoituksen mukaan

1. **Käyttäjän tarkoituksen ymmärtäminen**:
   - Käyttäjän tarkoitus voidaan jakaa kolmeen päätyyppiin: informatiivinen, navigointiin liittyvä ja transaktioon liittyvä.
     - **Informatiivinen tarkoitus**: Käyttäjä etsii tietoa tietystä aiheesta (esim. "Mitkä ovat parhaat museot Pariisissa?").
     - **Navigointitarkoitus**: Käyttäjä haluaa siirtyä tietylle sivustolle tai sivulle (esim. "Louvre-museon virallinen verkkosivu").
     - **Transaktiotarkoitus**: Käyttäjä haluaa tehdä toimenpiteen, kuten varata lennon tai ostaa tuotteen (esim. "Varaa lento Pariisiin").

2. **Kontekstin ymmärtäminen**:
   - Käyttäjän kyselyn kontekstin analysointi auttaa tunnistamaan tarkasti hänen tarkoituksensa. Tämä sisältää aiemmat vuorovaikutukset, käyttäjän mieltymykset ja kyselyn tarkat yksityiskohdat.

3. **Luonnollisen kielen käsittely (NLP)**:
   - NLP-tekniikoita käytetään ymmärtämään ja tulkitsemaan käyttäjien luonnollisen kielen kyselyitä. Tämä sisältää tehtäviä kuten entiteettien tunnistaminen, tunneanalyysi ja kyselyjen jäsentäminen.

4. **Personalisointi**:
   - Hakutulosten personointi käyttäjän historian, mieltymysten ja palautteen perusteella parantaa haetun tiedon relevanssia.

#### Käytännön esimerkki: Hakeminen käyttötarkoituksen mukaan matkatoimistossa

Otetaan Travel Agent esimerkkinä nähdäksesi, kuinka hakeminen käyttötarkoituksen mukaan voidaan toteuttaa.

1. **Käyttäjän mieltymysten kerääminen**

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
       # Yhdistä nykyinen kysely käyttäjän historian kanssa ymmärtääksesi kontekstin
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Hae ja personoi tuloksia**

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
       # Esimerkkihakulogiikka tiedolliselle tarkoitukselle
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Esimerkkihakulogiikka navigointitarkoitukselle
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Esimerkkihakulogiikka kaupalliselle tarkoitukselle
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Esimerkki personointilogiikka
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Palauta 10 parasta personoitua tulosta
   ```

5. **Käyttöesimerkki**

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

Koodin generoivat agentit käyttävät tekoälymalleja kirjoittaakseen ja suorittaakseen koodia, ratkaisten monimutkaisia ongelmia ja automatisoiden tehtäviä.

### Koodin generoivat agentit

Koodin generoivat agentit käyttävät generatiivisia tekoälymalleja kirjoittaakseen ja suorittaakseen koodia. Nämä agentit voivat ratkaista monimutkaisia ongelmia, automatisoida tehtäviä ja tarjota arvokkaita näkemyksiä generoimalla ja suorittamalla koodia eri ohjelmointikielillä.

#### Käytännön sovellukset

1. **Automaattinen koodin generointi**: Generoi koodipätkiä tiettyihin tehtäviin, kuten data-analyysiin, web-kaavintaan tai koneoppimiseen.
2. **SQL RAG-menetelmänä**: Käytä SQL-kyselyjä tietojen hakemiseen ja muokkaamiseen tietokannoista.
3. **Ongelmanratkaisu**: Luo ja suorita koodia ratkaistaksesi tiettyjä ongelmia, esimerkiksi optimoidaksesi algoritmeja tai analysoidaksesi dataa.

#### Esimerkki: Koodin generoiva agentti data-analyysiin

Kuvitellaan, että suunnittelet koodin generoivaa agenttia. Näin se voisi toimia:

1. **Tehtävä**: Analysoi tietojoukko tunnistaaksesi trendejä ja malleja.
2. **Vaiheet**:
   - Lataa tietojoukko data-analyysityökaluun.
   - Generoi SQL-kyselyt datan suodattamiseen ja aggregointiin.
   - Suorita kyselyt ja hae tulokset.
   - Käytä tuloksia visualisointien ja näkemysten luomiseen.
3. **Tarvittavat resurssit**: Pääsy tietojoukkoon, data-analyysityökalut ja SQL-osaaminen.
4. **Kokemus**: Käytä aiempia analyysituloksia parantaaksesi tulevien analyysien tarkkuutta ja merkityksellisyyttä.

### Esimerkki: Koodin generoiva agentti Matkatoimistolle

Tässä esimerkissä suunnittelemme koodin generoivan agentin, Matkatoimiston, auttamaan käyttäjiä matkojen suunnittelussa generoimalla ja suorittamalla koodia. Tämä agentti voi käsitellä tehtäviä kuten matkamahdollisuuksien hakemista, tulosten suodattamista ja matkasuunnitelman koostamista generatiivista tekoälyä hyödyntäen.

#### Yleiskatsaus koodin generoivaan agenttiin

1. **Käyttäjäasetusten kerääminen**: Kerää käyttäjän syötteitä, kuten kohde, matkustusajat, budjetti ja kiinnostuksen kohteet.
2. **Koodin generointi tiedon hakua varten**: Generoi koodipätkiä lentojen, hotellien ja nähtävyyksien tiedon hakemiseksi.
3. **Generoidun koodin suorittaminen**: Suorittaa generoitu koodi reaaliaikaisen tiedon hakemiseksi.
4. **Matkasuunnitelman luominen**: Koostaa haetusta datasta personoidun matkasuunnitelman.
5. **Palauteen perusteella mukauttaminen**: Saa käyttäjäpalautetta ja regeneroi koodin tarpeen mukaan tulosten hienosäätöön.

#### Vaiheittainen toteutus

1. **Käyttäjäasetusten kerääminen**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Koodin generointi tiedon hakua varten**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Esimerkki: Luo koodi lentojen hakemiseen käyttäjän mieltymysten perusteella
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Esimerkki: Luo koodi hotellien hakemiseen
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **Generoidun koodin suorittaminen**

   ```python
   def execute_code(code):
       # Suorita generoitu koodi käyttäen execiä
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

4. **Matkasuunnitelman generointi**

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

5. **Mukauttaminen palautteen perusteella**

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

Taulun skeemaan perustuva tieto todella voi parantaa kyselyjen generointiprosessia hyödyntämällä ympäristötietoisuutta ja päättelyä.

Tässä on esimerkki siitä, miten tämä voidaan toteuttaa:

1. **Skeeman ymmärtäminen**: Järjestelmä ymmärtää taulun skeeman ja käyttää tätä tietoa kyselyjen generoinnin perustana.
2. **Palautteen perusteella mukauttaminen**: Järjestelmä säätää käyttäjäasetuksia palautteen perusteella ja päättelyllä siitä, mitkä kentät skeemassa tulee päivittää.
3. **Kyselyjen generointi ja suorittaminen**: Järjestelmä generoi ja suorittaa kyselyt päivitettyjen matkustusasetusten pohjalta lentojen ja hotellien tietojen hakemiseksi.

Tässä on päivitetty Python-esimerkki, joka sisällyttää nämä käsitteet:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Mukauta asetuksia käyttäjäpalautteen perusteella
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Päätelmiä skeeman perusteella muiden siihen liittyvien asetusten säätämiseksi
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Räätälöity logiikka skeeman ja palautteen perusteella asetusten säätämiseen
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
    # Simuloi koodin suoritus ja palauta mallidata
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Luo matkasuunnitelma lentojen, hotellien ja nähtävyyksien perusteella
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Esimerkkiskeema
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Esimerkkikäyttö
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Luo koodi uudelleen ja suorita se päivitettyjen asetusten kanssa
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Selitys – Varaaminen palautteen perusteella

1. **Skeemantietoisuus**: `schema`-sanakirja määrittelee, miten asetuksia tulee säätää palautteen perusteella. Siinä on kenttiä kuten `favorites` ja `avoid`, joihin liittyvät säätöohjeet.
2. **Asetusten säätäminen (`adjust_based_on_feedback`-metodi)**: Tämä metodi säätää asetuksia käyttäjäpalautteen ja skeeman perusteella.
3. **Ympäristöperusteiset säädöt (`adjust_based_on_environment`-metodi)**: Tämä metodi mukauttaa säädöt skeeman ja palautteen mukaan.
4. **Kyselyjen generointi ja suorittaminen**: Järjestelmä generoi koodin päivitettyjen lentojen ja hotellien tietojen hakemiseksi sekä simuloi näiden kyselyjen suorittamista.
5. **Matkasuunnitelman generointi**: Järjestelmä luo päivittyneen matkasuunnitelman uusien lentojen, hotellien ja nähtävyyksien tietojen pohjalta.

Tekemällä järjestelmästä ympäristötietoinen ja käyttämällä päättelyä skeeman perusteella se voi tuottaa tarkempia ja merkityksellisempiä kyselyjä, mikä johtaa parempiin matkasuosituksiin ja henkilökohtaisempaan käyttökokemukseen.

### SQL:n käyttäminen hakua tukevana generointitekniikkana (RAG)

SQL (Structured Query Language) on tehokas väline tietokantojen kanssa vuorovaikutuksessa. Sitä käytettäessä osana Retrieval-Augmented Generation (RAG) -lähestymistapaa SQL voi hakea asiaankuuluvaa dataa tietokannoista AI-agenttien vastausten tai toimenpiteiden tuottamiseksi. Tarkastellaan, miten SQL:ää voidaan käyttää RAG-teknikkana Matkatoimiston kontekstissa.

#### Keskeiset käsitteet

1. **Tietokantayhteys**:
   - SQL:ää käytetään tietokantakyselyihin, olennaisen tiedon hakemiseen ja tiedon muokkaamiseen.
   - Esimerkki: Lentotietojen, hotellitietojen ja nähtävyyksien hakeminen matkailutietokannasta.

2. **Integraatio RAG:n kanssa**:
   - SQL-kyselyt generoidaan käyttäjän syötteen ja mieltymysten pohjalta.
   - Haettuja tietoja käytetään henkilökohtaisten suositusten tai toimenpiteiden tuottamiseen.

3. **Dynaaminen kyselygenerointi**:
   - AI-agentti tuottaa dynaamisia SQL-kyselyjä tilanteen ja käyttäjän tarpeiden mukaan.
   - Esimerkki: SQL-kyselyjen räätälöinti budjetin, päivämäärien ja kiinnostuksen kohteiden mukaan.

#### Sovellukset

- **Automaattinen koodin generointi**: Generoi koodipätkiä tiettyihin tehtäviin.
- **SQL RAG-menetelmänä**: Käytä SQL-kyselyjä datan käsittelyyn.
- **Ongelmanratkaisu**: Luo ja suorita koodia ongelmien ratkaisemiseksi.

**Esimerkki**:
Data-analyysia tekevä agentti:

1. **Tehtävä**: Analysoi tietojoukko trendien löytämiseksi.
2. **Vaiheet**:
   - Lataa tietojoukko.
   - Generoi SQL-kyselyt datan suodattamiseksi.
   - Suorita kyselyt ja hae tulokset.
   - Generoi visualisoinnit ja näkemykset.
3. **Resurssit**: Pääsy tietojoukkoon, SQL-osaaminen.
4. **Kokemus**: Käytä aiempia tuloksia parantaaksesi tulevia analyysejä.

#### Käytännön esimerkki: SQL:n käyttäminen Matkatoimistossa

1. **Käyttäjäasetusten kerääminen**

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

3. **SQL-kyselyjen suorittaminen**

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

#### Esimerkkikyselyt SQL:llä

1. **Lentokysely**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Hotellikysely**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Nähtävyyskysely**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Hyödyntämällä SQL:ää Retrieval-Augmented Generation (RAG) -tekniikan osana, tekoälyagentit kuten Matkatoimisto voivat dynaamisesti hakea ja käyttää relevanttia dataa tarjotakseen tarkkoja ja personoituja suosituksia.

### Esimerkki metakognition käytöstä

Havainnollistaaksemme metakognition toteutusta, luodaan yksinkertainen agentti, joka *reflektoi päätöksentekoprosessiaan* ongelman ratkaisuun aikana. Tässä esimerkissä rakennamme järjestelmän, jossa agentti yrittää optimoida hotellin valintaa, mutta arvioi omaa päättelyään ja säätää strategiaansa, kun tekee virheitä tai vähemmän optimaalisia valintoja.

Simuloimme tätä käyttämällä perustason esimerkkiä, jossa agentti valitsee hotelleja hinnan ja laadun yhdistelmän perusteella, mutta "reflektoi" päätöksiään ja mukautuu sen mukaan.

#### Miten tämä havainnollistaa metakognitiota:

1. **Alkuperäinen päätös**: Agentti valitsee halvimman hotellin ymmärtämättä laadun vaikutusta.
2. **Reflektio ja arviointi**: Alkuperäisen valinnan jälkeen agentti tarkistaa käyttäjäpalautteen avulla, oliko hotelli "huono" valinta. Jos hotellin laatu oli liian alhainen, agentti reflektoi päättelyään.
3. **Strategian säätäminen**: Agentti säätää strategiaansa reflektionsa perusteella vaihtamalla "halvin" -valinnasta "paras_laatus" -valintaan, parantaen päätöksentekoprosessiaan tulevissa iteraatioissa.

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
        # Oletetaan, että meillä on käyttäjäpalautetta, joka kertoo, oliko viimeinen valinta hyvä vai ei
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Säädä strategiaa, jos edellinen valinta oli tyytymätön
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

# Vaihe 1: Agentti suosittelee hotellia käyttäen "halvin" strategiaa
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Vaihe 2: Agentti arvioi valinnan ja säätää strategiaa tarvittaessa
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Vaihe 3: Agentti suosittelee uudelleen, tällä kertaa käyttäen säädettyä strategiaa
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Agentin metakognitiiviset kyvyt

Tärkeää tässä on agentin kyky:
- Arvioida aiemmat valinnat ja päätöksentekoprosessi.
- Säätää strategiaansa tämän reflektion pohjalta eli metakognition käyttö käytännössä.

Tämä on yksinkertainen muoto metakognitiosta, jossa järjestelmä pystyy säätämään päättelyprosessiaan sisäisen palautteen perusteella.

### Yhteenveto

Metakognitio on tehokas työkalu, joka voi merkittävästi parantaa tekoälyagenttien kykyjä. Sisällyttämällä metakognitiiviset prosessit voit suunnitella älykkäämpiä, sopeutuvampia ja tehokkaampia agentteja. Käytä lisäresursseja tutustuaksesi syvällisemmin metakognition kiehtovaan maailmaan tekoälyagenteissa.

### Onko sinulla lisää kysyttävää metakognition suunnittelumallista?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tavata muita oppijoita, osallistu toimistoaikoihin ja saa vastauksia tekoälyagenttien kysymyksiisi.

## Edellinen oppitunti

[Multi-Agent Suunnittelumalli](../08-multi-agent/README.md)

## Seuraava oppitunti

[Tekoälyagentit tuotannossa](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->