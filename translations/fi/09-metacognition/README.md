<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f0deef171fc3a68d5d3d770a8bfb03d",
  "translation_date": "2025-08-29T17:07:02+00:00",
  "source_file": "09-metacognition/README.md",
  "language_code": "fi"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-9-thumbnail.38059e8af1a5b71d890c92f576f933c6a307c691339dca7e8ca6ea75a8d857a1.fi.png)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Klikkaa yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_
# Metakognitio tekoälyagenteissa

## Johdanto

Tervetuloa oppitunnille, joka käsittelee metakognitiota tekoälyagenteissa! Tämä luku on suunniteltu aloittelijoille, jotka haluavat ymmärtää, miten tekoälyagentit voivat ajatella omia ajatteluprosessejaan. Oppitunnin lopussa ymmärrät keskeiset käsitteet ja saat käytännön esimerkkejä metakognition soveltamisesta tekoälyagenttien suunnittelussa.

## Oppimistavoitteet

Oppitunnin jälkeen osaat:

1. Ymmärtää päättelysilmukoiden vaikutukset agenttien määrittelyssä.
2. Käyttää suunnittelu- ja arviointitekniikoita itseään korjaavien agenttien tukemiseksi.
3. Luoda omia agentteja, jotka pystyvät muokkaamaan koodia tehtävien suorittamiseksi.

## Johdatus metakognitioon

Metakognitio viittaa korkeampiin kognitiivisiin prosesseihin, jotka liittyvät oman ajattelun tarkasteluun. Tekoälyagenteille tämä tarkoittaa kykyä arvioida ja mukauttaa toimintaansa itsetietoisuuden ja aiempien kokemusten perusteella. Metakognitio eli "ajattelu ajattelusta" on tärkeä käsite agenttisten tekoälyjärjestelmien kehittämisessä. Se tarkoittaa, että tekoälyjärjestelmät ovat tietoisia omista sisäisistä prosesseistaan ja pystyvät seuraamaan, säätelemään ja mukauttamaan käyttäytymistään. Aivan kuten me teemme, kun luemme tilannetta tai tarkastelemme ongelmaa. Tämä itsetietoisuus voi auttaa tekoälyjärjestelmiä tekemään parempia päätöksiä, tunnistamaan virheitä ja parantamaan suorituskykyään ajan myötä – jälleen kerran viitaten Turingin testiin ja keskusteluun siitä, valtaako tekoäly maailman.

Agenttisten tekoälyjärjestelmien kontekstissa metakognitio voi auttaa ratkaisemaan useita haasteita, kuten:
- Läpinäkyvyys: Varmistetaan, että tekoälyjärjestelmät voivat selittää päättelynsä ja päätöksensä.
- Päättely: Parannetaan tekoälyjärjestelmien kykyä yhdistää tietoa ja tehdä järkeviä päätöksiä.
- Mukautuminen: Mahdollistetaan tekoälyjärjestelmien sopeutuminen uusiin ympäristöihin ja muuttuviin olosuhteisiin.
- Havainnointi: Parannetaan tekoälyjärjestelmien tarkkuutta ympäristön datan tunnistamisessa ja tulkinnassa.

### Mitä metakognitio on?

Metakognitio eli "ajattelu ajattelusta" on korkeampi kognitiivinen prosessi, joka sisältää itsetietoisuuden ja omien kognitiivisten prosessien itsesäätelyn. Tekoälyn alalla metakognitio antaa agenteille mahdollisuuden arvioida ja mukauttaa strategioitaan ja toimiaan, mikä johtaa parempiin ongelmanratkaisu- ja päätöksentekokykyihin. Ymmärtämällä metakognitiota voit suunnitella tekoälyagentteja, jotka ovat paitsi älykkäämpiä myös mukautuvampia ja tehokkaampia. Aidossa metakognitiossa tekoäly ajattelisi eksplisiittisesti omaa päättelyään.

Esimerkki: “Priorisoin halvempia lentoja, koska… Saatan jättää huomiotta suorat lennot, joten tarkistan uudelleen.”
Seurataan, miten tai miksi tietty reitti valittiin.
- Huomataan, että virheitä tehtiin, koska luotettiin liikaa käyttäjän aiempiin mieltymyksiin, ja muutetaan päätöksentekostrategiaa, ei vain lopullista suositusta.
- Diagnosoidaan kaavoja, kuten: “Aina kun käyttäjä mainitsee ‘liian ruuhkainen’, minun pitäisi paitsi poistaa tiettyjä kohteita myös huomioida, että menetelmäni ‘suosituimpien kohteiden’ valinnassa on virheellinen, jos aina arvioin suosiota korkeimmaksi.”

### Metakognition merkitys tekoälyagenteissa

Metakognitiolla on keskeinen rooli tekoälyagenttien suunnittelussa useista syistä:

![Metakognition merkitys](../../../translated_images/importance-of-metacognition.b381afe9aae352f7734c8628ea3f4b23084634b791c5a120c76a02bb7eeeb7ec.fi.png)

- Itsearviointi: Agentit voivat arvioida omaa suorituskykyään ja tunnistaa parannuskohteita.
- Mukautuvuus: Agentit voivat muuttaa strategioitaan aiempien kokemusten ja muuttuvien ympäristöjen perusteella.
- Virheiden korjaus: Agentit voivat havaita ja korjata virheitä itsenäisesti, mikä johtaa tarkempiin tuloksiin.
- Resurssien hallinta: Agentit voivat optimoida resurssien, kuten ajan ja laskentatehon, käyttöä suunnittelemalla ja arvioimalla toimiaan.

## Tekoälyagentin komponentit

Ennen kuin sukellamme metakognitiivisiin prosesseihin, on tärkeää ymmärtää tekoälyagentin peruskomponentit. Tekoälyagentti koostuu yleensä seuraavista:

- Persoona: Agentin persoonallisuus ja ominaisuudet, jotka määrittelevät, miten se on vuorovaikutuksessa käyttäjien kanssa.
- Työkalut: Agentin suorittamat kyvyt ja toiminnot.
- Taidot: Agentin hallussa oleva tieto ja asiantuntemus.

Nämä komponentit toimivat yhdessä muodostaen "asiantuntijayksikön", joka voi suorittaa tiettyjä tehtäviä.

**Esimerkki**:
Ajatellaan matkatoimistoagenttia, joka ei ainoastaan suunnittele lomasi, vaan myös mukauttaa reittiään reaaliaikaisen datan ja aiempien asiakaskokemusten perusteella.

### Esimerkki: Metakognitio matkatoimistoagentissa

Kuvittele, että suunnittelet tekoälyllä toimivaa matkatoimistoagenttia. Tämä agentti, "Matkatoimisto", auttaa käyttäjiä lomien suunnittelussa. Metakognition sisällyttämiseksi Matkatoimiston täytyy arvioida ja mukauttaa toimintaansa itsetietoisuuden ja aiempien kokemusten perusteella. Näin metakognitio voisi vaikuttaa:

#### Nykyinen tehtävä

Nykyinen tehtävä on auttaa käyttäjää suunnittelemaan matka Pariisiin.

#### Tehtävän suorittamisen vaiheet

1. **Kerää käyttäjän mieltymykset**: Kysy käyttäjältä matkustuspäivistä, budjetista, kiinnostuksen kohteista (esim. museot, ruoka, ostokset) ja erityisvaatimuksista.
2. **Hae tietoa**: Etsi lento-, majoitus-, nähtävyys- ja ravintolavaihtoehtoja, jotka vastaavat käyttäjän mieltymyksiä.
3. **Luo suosituksia**: Tarjoa henkilökohtainen matkasuunnitelma, joka sisältää lentotiedot, hotellivaraukset ja ehdotetut aktiviteetit.
4. **Mukauta palautteen perusteella**: Pyydä käyttäjältä palautetta suosituksista ja tee tarvittavat muutokset.

#### Tarvittavat resurssit

- Pääsy lento- ja hotellivaraustietokantoihin.
- Tietoa pariisilaisista nähtävyyksistä ja ravintoloista.
- Käyttäjäpalautedata aiemmista vuorovaikutuksista.

#### Kokemus ja itsearviointi

Matkatoimisto käyttää metakognitiota arvioidakseen suorituskykyään ja oppiakseen aiemmista kokemuksista. Esimerkiksi:

1. **Käyttäjäpalautteen analysointi**: Matkatoimisto tarkastelee käyttäjäpalautetta selvittääkseen, mitkä suositukset olivat onnistuneita ja mitkä eivät. Se mukauttaa tulevia ehdotuksiaan sen mukaan.
2. **Mukautuvuus**: Jos käyttäjä on aiemmin maininnut, ettei pidä ruuhkaisista paikoista, Matkatoimisto välttää suosittelemasta suosittuja turistikohteita ruuhka-aikoina tulevaisuudessa.
3. **Virheiden korjaus**: Jos Matkatoimisto teki virheen aiemmassa varauksessa, kuten suositteli täyteen varattua hotellia, se oppii tarkistamaan saatavuuden huolellisemmin ennen suositusten tekemistä.

#### Käytännön kehittäjäesimerkki

Tässä yksinkertaistettu esimerkki siitä, miltä Matkatoimiston koodi voisi näyttää metakognition sisällyttämisessä:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Search for flights, hotels, and attractions based on preferences
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
        # Analyze feedback and adjust future recommendations
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Example usage
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

- **Itsearviointi**: Agentit voivat analysoida suorituskykyään ja tunnistaa parannuskohteita.
- **Mukautuvuus**: Agentit voivat muuttaa strategioita palautteen ja muuttuvien olosuhteiden perusteella.
- **Virheiden korjaus**: Agentit voivat havaita ja korjata virheitä itsenäisesti.
- **Resurssien hallinta**: Agentit voivat optimoida resurssien käyttöä, kuten aikaa ja laskentatehoa.

Metakognition sisällyttämällä Matkatoimisto voi tarjota henkilökohtaisempia ja tarkempia matkasuosituksia, mikä parantaa käyttäjäkokemusta.

---

## 2. Suunnittelu agenteissa

Suunnittelu on keskeinen osa tekoälyagenttien käyttäytymistä. Se sisältää tarvittavien vaiheiden hahmottamisen tavoitteen saavuttamiseksi, ottaen huomioon nykytilanne, resurssit ja mahdolliset esteet.

### Suunnittelun elementit

- **Nykyinen tehtävä**: Määrittele tehtävä selkeästi.
- **Tehtävän suorittamisen vaiheet**: Pilko tehtävä hallittaviin osiin.
- **Tarvittavat resurssit**: Tunnista tarvittavat resurssit.
- **Kokemus**: Hyödynnä aiempia kokemuksia suunnittelun tueksi.

**Esimerkki**:
Tässä ovat vaiheet, jotka Matkatoimiston täytyy suorittaa auttaakseen käyttäjää matkan suunnittelussa tehokkaasti:

### Matkatoimiston vaiheet

1. **Kerää käyttäjän mieltymykset**
   - Kysy käyttäjältä matkustuspäivistä, budjetista, kiinnostuksen kohteista ja erityisvaatimuksista.
   - Esimerkkejä: "Milloin aiot matkustaa?" "Mikä on budjettisi?" "Mistä aktiviteeteista nautit lomalla?"

2. **Hae tietoa**
   - Etsi käyttäjän mieltymyksiin perustuvia matkavaihtoehtoja.
   - **Lennot**: Etsi saatavilla olevia lentoja käyttäjän budjetin ja mieltymyksien mukaisesti.
   - **Majoitus**: Löydä hotelleja tai vuokrakohteita, jotka vastaavat käyttäjän sijainti-, hinta- ja mukavuusvaatimuksia.
   - **Nähtävyydet ja ravintolat**: Tunnista suosittuja nähtävyyksiä, aktiviteetteja ja ruokailuvaihtoehtoja, jotka sopivat käyttäjän kiinnostuksen kohteisiin.

3. **Luo suosituksia**
   - Koosta haettu tieto henkilökohtaiseksi matkasuunnitelmaksi.
   - Tarjoa yksityiskohtia, kuten lentovaihtoehtoja, hotellivarauksia ja ehdotettuja aktiviteetteja, varmistaen, että suositukset ovat käyttäjän mieltymysten mukaisia.

4. **Esitä matkasuunnitelma käyttäjälle**
   - Jaa ehdotettu matkasuunnitelma käyttäjälle tarkistettavaksi.
   - Esimerkki: "Tässä on ehdotettu matkasuunnitelma Pariisin matkaasi varten. Se sisältää lentotiedot, hotellivaraukset ja listan suositelluista aktiviteeteista ja ravintoloista. Kerro mielipiteesi!"

5. **Kerää palaute**
   - Pyydä käyttäjältä palautetta ehdotetusta matkasuunnitelmasta.
   - Esimerkkejä: "Pidätkö lentovaihtoehdoista?" "Onko hotelli sopiva tarpeisiisi?" "Onko aktiviteetteja, joita haluaisit lisätä tai poistaa?"

6. **Mukauta palautteen perusteella**
   - Muokkaa matkasuunnitelmaa käyttäjän palautteen perusteella.
   - Tee tarvittavat muutokset lento-, majoitus- ja aktiviteettisuosituksiin, jotta ne vastaavat paremmin käyttäjän mieltymyksiä.

7. **Lopullinen vahvistus**
   - Esitä päivitetty matkasuunnitelma käyttäjälle lopullista vahvistusta varten.
   - Esimerkki: "Olen tehnyt muutokset palautteesi perusteella. Tässä on päivitetty matkasuunnitelma. Näyttääkö kaikki hyvältä?"

8. **Varaa ja vahvista varaukset**
   - Kun käyttäjä hyväksyy matkasuunnitelman, jatka lentojen, majoitusten ja mahdollisten etukäteen suunniteltujen aktiviteettien varaamista.
   - Lähetä vahvistustiedot käyttäjälle.

9. **Tarjoa jatkuvaa tukea**
   - Ole käytettävissä auttamaan käyttäjää muutoksissa tai lisäpyynnöissä ennen matkaa ja sen aikana.
   - Esimerkki: "Jos tarvitset lisäapua matkan aikana, ota yhteyttä milloin tahansa!"

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

# Example usage within a booing request
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

Aloitetaan ymmärtämällä ero RAG-työkalun ja ennakoivan kontekstilatauksen välillä.

![RAG vs kontekstilataus](../../../translated_images/rag-vs-context.9eae588520c00921f531e4dc788992e8a7b69b6ff7c9eaa69fb9bc83ad243504.fi.png)

### Retrieval-Augmented Generation (RAG)

RAG yhdistää hakujärjestelmän generatiiviseen malliin. Kun kysely tehdään, hakujärjestelmä hakee asiaankuuluvia dokumentteja tai dataa ulkoisesta lähteestä, ja tämä haettu tieto käytetään generatiivisen mallin syötteenä. Tämä auttaa mallia tuottamaan tarkempia ja kontekstuaalisesti relevantteja vastauksia.

RAG-järjestelmässä agentti hakee asiaankuuluvaa tietoa tietokannasta ja käyttää sitä tuottaakseen sopivia vastauksia tai toimintoja.

### Korjaava RAG-lähestymistapa

Korjaava RAG-lähestymistapa keskittyy RAG-tekniikoiden käyttöön virheiden korjaamiseksi ja tekoälyagenttien tarkkuuden parantamiseksi. Tämä sisältää:

1. **Kehotusmenetelmä**: Käytetään erityisiä kehotuksia ohjaamaan agenttia hakemaan asiaankuuluvaa tietoa.
2. **Työkalu**: Toteutetaan algoritmeja ja mekanismeja, jotka mahdollistavat agentin arvioida haetun tiedon relevanssia ja tuottaa tarkkoja vastauksia.
3. **Arviointi**: Agentin suorituskyvyn jatkuva arviointi ja säätöjen tekeminen tarkkuuden ja tehokkuuden parantamiseksi.

#### Esimerkki: Korjaava RAG hakijassa

Ajatellaan hakijaa, joka hakee tietoa verkosta vastatakseen käyttäjän kyselyihin. Korjaava RAG-lähestymistapa voisi sisältää:

1. **Kehotusmenetelmä**: Muotoillaan hakukyselyt käyttäjän syötteen perusteella.
2. **Työkalu**: Käytetään luonnollisen kielen käsittelyä ja koneoppimisalgoritmeja hakutulosten järjestämiseen ja suodattamiseen.
3. **Arviointi**: Käyttäjäpalautteen analysointi virheiden tunnistamiseksi ja haetun tiedon epätarkkuuksien korjaamiseksi.

### Korjaava RAG matkatoimistoagentissa

Korjaava RAG (Retrieval-Augmented Generation) parantaa tekoälyn kykyä hakea ja tuottaa tietoa samalla korjaten mahdollisia epätarkkuuksia. Katsotaan, miten Matkatoimisto voi käyttää korjaavaa RAG-lähestymistapaa tarjotakseen tarkempia ja relevantimpia matkasuosituksia.

Tämä sisältää:

- **Kehotusmenetelmä:** Käytetään erityisiä kehotuksia ohjaamaan agenttia hakemaan asiaankuuluvaa tietoa.
- **Työkalu:** Toteutetaan algoritmeja ja mekanismeja, jotka mahdollistavat agentin arvioida haetun tiedon relevanssia ja tuottaa tarkkoja vastauksia.
- **Arviointi:** Agentin suorituskyvyn jatkuva arviointi ja säätöjen tekeminen tarkkuuden ja tehokkuuden parantamiseksi.

#### Vaiheet korjaavan RAG:n toteuttamiseksi Matkatoimistossa

1. **Alustava käyttäjävuorovaikutus**
   - Matkatoimisto kerää käyttäjän alkuperäiset mieltymykset, kuten kohde, matkustuspäivät, budjetti ja kiinnostuksen kohteet.
   - Esimerkki:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Tiedon
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

# Example usage
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

Ennakoiva kontekstin lataus tarkoittaa, että mallille ladataan etukäteen olennaista taustatietoa ennen kyselyn käsittelyä. Tämä antaa mallille pääsyn kyseiseen tietoon jo alusta alkaen, mikä voi auttaa sitä tuottamaan paremmin informoituja vastauksia ilman, että sen tarvitsee hakea lisätietoa prosessin aikana.

Tässä on yksinkertaistettu esimerkki siitä, miltä ennakoiva kontekstin lataus voisi näyttää matkatoimistosovelluksessa Pythonilla:

```python
class TravelAgent:
    def __init__(self):
        # Pre-load popular destinations and their information
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Fetch destination information from pre-loaded context
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Example usage
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### Selitys

1. **Alustaminen (`__init__`-metodi)**: `TravelAgent`-luokka lataa etukäteen sanakirjan, joka sisältää tietoa suosituista matkakohteista, kuten Pariisista, Tokiosta, New Yorkista ja Sydneystä. Sanakirja sisältää tietoja, kuten maan, valuutan, kielen ja tärkeimmät nähtävyydet kullekin kohteelle.

2. **Tiedon hakeminen (`get_destination_info`-metodi)**: Kun käyttäjä kysyy tietoa tietystä kohteesta, `get_destination_info`-metodi hakee asiaankuuluvat tiedot esiladatusta kontekstisanakirjasta.

Esilataamalla kontekstin matkatoimistosovellus voi vastata käyttäjän kyselyihin nopeasti ilman, että sen tarvitsee hakea tietoa ulkoisesta lähteestä reaaliajassa. Tämä tekee sovelluksesta tehokkaamman ja reagoivamman.

### Suunnitelman käynnistäminen tavoitteella ennen iterointia

Suunnitelman käynnistäminen tavoitteella tarkoittaa, että aloitetaan selkeästi määritellyllä päämäärällä tai tavoiteltavalla lopputuloksella. Määrittelemällä tavoite etukäteen malli voi käyttää sitä ohjaavana periaatteena koko iterointiprosessin ajan. Tämä auttaa varmistamaan, että jokainen iterointi vie lähemmäs haluttua lopputulosta, tehden prosessista tehokkaamman ja keskittyneemmän.

Tässä on esimerkki siitä, miten matkasuunnitelma voidaan käynnistää tavoitteella ennen iterointia matkatoimistosovelluksessa Pythonilla:

### Tilanne

Matkatoimisto haluaa suunnitella asiakkaalle räätälöidyn loman. Tavoitteena on luoda matkasuunnitelma, joka maksimoi asiakkaan tyytyväisyyden heidän mieltymystensä ja budjettinsa perusteella.

### Vaiheet

1. Määrittele asiakkaan mieltymykset ja budjetti.
2. Käynnistä alkuperäinen suunnitelma näiden mieltymysten perusteella.
3. Iteroi suunnitelmaa, optimoiden asiakkaan tyytyväisyyttä.

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

# Example usage
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

1. **Alustaminen (`__init__`-metodi)**: `TravelAgent`-luokka alustetaan listalla mahdollisia matkakohteita, joilla on ominaisuuksia, kuten nimi, kustannukset ja aktiviteettityyppi.

2. **Suunnitelman käynnistäminen (`bootstrap_plan`-metodi)**: Tämä metodi luo alkuperäisen matkasuunnitelman asiakkaan mieltymysten ja budjetin perusteella. Se käy läpi kohdelistan ja lisää suunnitelmaan kohteita, jotka vastaavat asiakkaan mieltymyksiä ja mahtuvat budjettiin.

3. **Mieltymysten vastaavuus (`match_preferences`-metodi)**: Tämä metodi tarkistaa, vastaako kohde asiakkaan mieltymyksiä.

4. **Suunnitelman iterointi (`iterate_plan`-metodi)**: Tämä metodi tarkentaa alkuperäistä suunnitelmaa yrittämällä korvata suunnitelman kohteita paremmilla vaihtoehdoilla, ottaen huomioon asiakkaan mieltymykset ja budjettirajoitukset.

5. **Kustannusten laskeminen (`calculate_cost`-metodi)**: Tämä metodi laskee nykyisen suunnitelman kokonaiskustannukset, mukaan lukien mahdollinen uusi kohde.

#### Esimerkkikäyttö

- **Alkuperäinen suunnitelma**: Matkatoimisto luo alkuperäisen suunnitelman asiakkaan mieltymysten (esim. nähtävyyksien katselu) ja 2000 dollarin budjetin perusteella.
- **Tarkennettu suunnitelma**: Matkatoimisto iteroi suunnitelmaa, optimoiden asiakkaan mieltymysten ja budjetin mukaan.

Käynnistämällä suunnitelman selkeällä tavoitteella (esim. asiakkaan tyytyväisyyden maksimointi) ja iteroinnin avulla tarkentamalla suunnitelmaa matkatoimisto voi luoda asiakkaalle räätälöidyn ja optimoidun matkasuunnitelman. Tämä lähestymistapa varmistaa, että matkasuunnitelma vastaa asiakkaan mieltymyksiä ja budjettia alusta alkaen ja paranee jokaisen iteroinnin myötä.

### LLM:n hyödyntäminen uudelleenjärjestelyssä ja pisteytyksessä

Suuret kielimallit (LLM:t) voivat auttaa uudelleenjärjestelyssä ja pisteytyksessä arvioimalla haettujen dokumenttien tai luotujen vastausten relevanssia ja laatua. Näin se toimii:

**Haku:** Alkuperäinen hakuvaihe tuo esiin joukon ehdokkaita dokumentteja tai vastauksia kyselyn perusteella.

**Uudelleenjärjestely:** LLM arvioi nämä ehdokkaat ja järjestää ne uudelleen niiden relevanssin ja laadun perusteella. Tämä varmistaa, että tärkein ja laadukkain tieto esitetään ensin.

**Pisteytys:** LLM antaa jokaiselle ehdokkaalle pisteet, jotka heijastavat niiden relevanssia ja laatua. Tämä auttaa valitsemaan käyttäjälle parhaan vastauksen tai dokumentin.

Hyödyntämällä LLM:ää uudelleenjärjestelyssä ja pisteytyksessä järjestelmä voi tarjota tarkempaa ja kontekstuaalisesti osuvampaa tietoa, parantaen kokonaiskäyttäjäkokemusta.

Tässä on esimerkki siitä, miten matkatoimisto voisi käyttää suurta kielimallia (LLM) matkakohteiden uudelleenjärjestelyyn ja pisteytykseen käyttäjän mieltymysten perusteella Pythonilla:

#### Tilanne - Matkustaminen mieltymysten mukaan

Matkatoimisto haluaa suositella asiakkaalle parhaita matkakohteita heidän mieltymystensä perusteella. LLM auttaa uudelleenjärjestelemään ja pisteyttämään kohteet varmistaakseen, että relevantimmat vaihtoehdot esitetään ensin.

#### Vaiheet:

1. Kerää käyttäjän mieltymykset.
2. Hae lista mahdollisista matkakohteista.
3. Käytä LLM:ää kohteiden uudelleenjärjestelyyn ja pisteytykseen käyttäjän mieltymysten perusteella.

Näin voit päivittää aiemman esimerkin käyttämään Azure OpenAI -palveluita:

#### Vaatimukset

1. Sinulla on oltava Azure-tilaus.
2. Luo Azure OpenAI -resurssi ja hanki API-avaimesi.

#### Esimerkkikoodi Pythonilla

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Generate a prompt for the Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Define headers and payload for the request
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Call the Azure OpenAI API to get the re-ranked and scored destinations
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Extract and return the recommendations
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

# Example usage
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

#### Koodin selitys - Mieltymyspohjainen varaaja

1. **Alustaminen**: `TravelAgent`-luokka alustetaan listalla mahdollisia matkakohteita, joilla on ominaisuuksia, kuten nimi ja kuvaus.

2. **Suositusten hakeminen (`get_recommendations`-metodi)**: Tämä metodi luo kehotteen Azure OpenAI -palvelulle käyttäjän mieltymysten perusteella ja tekee HTTP POST -pyynnön Azure OpenAI API:lle saadakseen uudelleenjärjestellyt ja pisteytetyt kohteet.

3. **Kehotteen luominen (`generate_prompt`-metodi)**: Tämä metodi rakentaa kehotteen Azure OpenAI:lle, sisältäen käyttäjän mieltymykset ja listan kohteista. Kehote ohjaa mallia uudelleenjärjestelemään ja pisteyttämään kohteet annettujen mieltymysten perusteella.

4. **API-kutsu**: `requests`-kirjastoa käytetään tekemään HTTP POST -pyyntö Azure OpenAI API -päätepisteeseen. Vastaus sisältää uudelleenjärjestellyt ja pisteytetyt kohteet.

5. **Esimerkkikäyttö**: Matkatoimisto kerää käyttäjän mieltymykset (esim. kiinnostus nähtävyyksiin ja monipuoliseen kulttuuriin) ja käyttää Azure OpenAI -palvelua saadakseen uudelleenjärjestellyt ja pisteytetyt suositukset matkakohteista.

Muista korvata `your_azure_openai_api_key` todellisella Azure OpenAI API -avaimellasi ja `https://your-endpoint.com/...` todellisella Azure OpenAI -käyttöönoton päätepisteen URL-osoitteella.

Hyödyntämällä LLM:ää uudelleenjärjestelyssä ja pisteytyksessä matkatoimisto voi tarjota asiakkailleen henkilökohtaisempia ja relevantimpia matkasuosituksia, parantaen heidän kokonaiskokemustaan.
#### Käytännön esimerkki: Hakeminen tarkoituksenmukaisesti matkatoimistossa

Käytetään matkatoimistoa esimerkkinä, jotta nähdään, miten hakeminen tarkoituksenmukaisesti voidaan toteuttaa.

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

3. **Kontekstin huomioiminen**

   ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Hakeminen ja tulosten personointi**

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
       # Example search logic for informational intent
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Example search logic for navigational intent
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Example search logic for transactional intent
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Example personalization logic
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Return top 10 personalized results
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

Koodia generoivat agentit käyttävät tekoälymalleja koodin kirjoittamiseen ja suorittamiseen, ratkaisten monimutkaisia ongelmia ja automatisoiden tehtäviä.

### Koodia generoivat agentit

Koodia generoivat agentit hyödyntävät generatiivisia tekoälymalleja koodin kirjoittamiseen ja suorittamiseen. Nämä agentit voivat ratkaista monimutkaisia ongelmia, automatisoida tehtäviä ja tarjota arvokkaita oivalluksia generoimalla ja suorittamalla koodia eri ohjelmointikielillä.

#### Käytännön sovellukset

1. **Automaattinen koodin generointi**: Generoi koodinpätkiä tiettyihin tehtäviin, kuten data-analyysiin, verkkosivujen tietojen keräämiseen tai koneoppimiseen.
2. **SQL RAG-tekniikkana**: Käytä SQL-kyselyitä tietojen hakemiseen ja käsittelyyn tietokannoista.
3. **Ongelmanratkaisu**: Luo ja suorita koodia tiettyjen ongelmien ratkaisemiseksi, kuten algoritmien optimointi tai datan analysointi.

#### Esimerkki: Koodia generoiva agentti data-analyysiin

Kuvitellaan, että suunnittelet koodia generoivaa agenttia. Näin se voisi toimia:

1. **Tehtävä**: Analysoi datasettiä tunnistaaksesi trendejä ja kuvioita.
2. **Vaiheet**:
   - Lataa datasetti data-analyysityökaluun.
   - Generoi SQL-kyselyitä datan suodattamiseen ja aggregointiin.
   - Suorita kyselyt ja hae tulokset.
   - Käytä tuloksia visualisointien ja oivallusten luomiseen.
3. **Tarvittavat resurssit**: Pääsy datasettiin, data-analyysityökalut ja SQL-ominaisuudet.
4. **Kokemus**: Hyödynnä aiempia analyysituloksia parantaaksesi tulevien analyysien tarkkuutta ja osuvuutta.

### Esimerkki: Koodia generoiva agentti matkatoimistossa

Tässä esimerkissä suunnittelemme koodia generoivan agentin, matkatoimiston, joka auttaa käyttäjiä matkasuunnittelussa generoimalla ja suorittamalla koodia. Tämä agentti voi hoitaa tehtäviä, kuten matkavaihtoehtojen hakeminen, tulosten suodattaminen ja matkasuunnitelman kokoaminen generatiivisen tekoälyn avulla.

#### Koodia generoivan agentin yleiskatsaus

1. **Käyttäjän mieltymysten kerääminen**: Kerää käyttäjän syötteitä, kuten kohde, matkustuspäivät, budjetti ja kiinnostuksen kohteet.
2. **Koodin generointi datan hakemiseen**: Generoi koodinpätkiä lentojen, hotellien ja nähtävyyksien tietojen hakemiseen.
3. **Generoidun koodin suorittaminen**: Suorittaa generoidun koodin reaaliaikaisten tietojen hakemiseksi.
4. **Matkasuunnitelman generointi**: Kokoaa haetut tiedot henkilökohtaiseksi matkasuunnitelmaksi.
5. **Mukauttaminen palautteen perusteella**: Saa käyttäjän palautetta ja generoi koodia uudelleen tarvittaessa tulosten tarkentamiseksi.

#### Vaiheittainen toteutus

1. **Käyttäjän mieltymysten kerääminen**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Koodin generointi datan hakemiseen**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Example: Generate code to search for flights based on user preferences
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Example: Generate code to search for hotels
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
       # Execute the generated code using exec
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
       # Adjust preferences based on user feedback
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Regenerate and execute code with updated preferences
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Ympäristötietoisuuden ja päättelyn hyödyntäminen

Taulukon skeeman perusteella voidaan parantaa kyselyjen generointiprosessia hyödyntämällä ympäristötietoisuutta ja päättelyä.

Tässä esimerkki siitä, miten tämä voidaan tehdä:

1. **Skeeman ymmärtäminen**: Järjestelmä ymmärtää taulukon skeeman ja käyttää tätä tietoa kyselyjen generoinnin pohjana.
2. **Mukauttaminen palautteen perusteella**: Järjestelmä mukauttaa käyttäjän mieltymyksiä palautteen perusteella ja päättää, mitkä skeeman kentät tulee päivittää.
3. **Kyselyjen generointi ja suorittaminen**: Järjestelmä generoi ja suorittaa kyselyjä päivitettyjen lentojen ja hotellien tietojen hakemiseksi uusien mieltymysten perusteella.

Tässä päivitetty Python-koodiesimerkki, joka sisältää nämä konseptit:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Adjust preferences based on user feedback
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Reasoning based on schema to adjust other related preferences
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Custom logic to adjust preferences based on schema and feedback
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Generate code to fetch flight data based on updated preferences
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Generate code to fetch hotel data based on updated preferences
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simulate execution of code and return mock data
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Generate itinerary based on flights, hotels, and attractions
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Example schema
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Example usage
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Regenerate and execute code with updated preferences
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Selitys - Varaaminen palautteen perusteella

1. **Skeematietoisuus**: `schema`-sanakirja määrittää, miten mieltymyksiä tulisi mukauttaa palautteen perusteella. Se sisältää kenttiä, kuten `favorites` ja `avoid`, sekä vastaavat mukautukset.
2. **Mieltymysten mukauttaminen (`adjust_based_on_feedback`-metodi)**: Tämä metodi mukauttaa mieltymyksiä käyttäjän palautteen ja skeeman perusteella.
3. **Ympäristöön perustuvat mukautukset (`adjust_based_on_environment`-metodi)**: Tämä metodi räätälöi mukautukset skeeman ja palautteen perusteella.
4. **Kyselyjen generointi ja suorittaminen**: Järjestelmä generoi koodia päivitettyjen lentojen ja hotellien tietojen hakemiseksi mukautettujen mieltymysten perusteella ja simuloi näiden kyselyjen suorittamista.
5. **Matkasuunnitelman generointi**: Järjestelmä luo päivitetyn matkasuunnitelman uusien lentojen, hotellien ja nähtävyyksien tietojen perusteella.

Ympäristötietoisuuden ja skeeman perusteella päättelyn avulla järjestelmä voi generoida tarkempia ja osuvampia kyselyjä, mikä johtaa parempiin matkasuosituksiin ja henkilökohtaisempaan käyttäjäkokemukseen.

### SQL:n käyttö Retrieval-Augmented Generation (RAG) -tekniikkana

SQL (Structured Query Language) on tehokas työkalu tietokantojen käsittelyyn. Kun sitä käytetään osana Retrieval-Augmented Generation (RAG) -lähestymistapaa, SQL voi hakea relevantteja tietoja tietokannoista tekoälyagenttien vastauksia tai toimintoja varten. Tarkastellaan, miten SQL:ää voidaan käyttää RAG-tekniikkana matkatoimiston yhteydessä.

#### Keskeiset käsitteet

1. **Tietokantayhteys**:
   - SQL:ää käytetään tietokantojen kyselyihin, relevanttien tietojen hakemiseen ja datan käsittelyyn.
   - Esimerkki: Lentotietojen, hotellitietojen ja nähtävyyksien hakeminen matkustustietokannasta.

2. **Integraatio RAG:n kanssa**:
   - SQL-kyselyt generoidaan käyttäjän syötteiden ja mieltymysten perusteella.
   - Haettu data käytetään henkilökohtaisten suositusten tai toimintojen generointiin.

3. **Dynaaminen kyselygenerointi**:
   - Tekoälyagentti generoi dynaamisia SQL-kyselyitä kontekstin ja käyttäjän tarpeiden perusteella.
   - Esimerkki: SQL-kyselyiden räätälöinti budjetin, päivämäärien ja kiinnostuksen kohteiden perusteella.

#### Sovellukset

- **Automaattinen koodin generointi**: Generoi koodinpätkiä tiettyihin tehtäviin.
- **SQL RAG-tekniikkana**: Käytä SQL-kyselyitä datan käsittelyyn.
- **Ongelmanratkaisu**: Luo ja suorita koodia ongelmien ratkaisemiseksi.

**Esimerkki**:
Data-analyysiagentti:

1. **Tehtävä**: Analysoi datasettiä löytääkseen trendejä.
2. **Vaiheet**:
   - Lataa datasetti.
   - Generoi SQL-kyselyitä datan suodattamiseen.
   - Suorita kyselyt ja hae tulokset.
   - Generoi visualisointeja ja oivalluksia.
3. **Resurssit**: Datasetin pääsy, SQL-ominaisuudet.
4. **Kokemus**: Hyödynnä aiempia tuloksia tulevien analyysien parantamiseksi.

#### Käytännön esimerkki: SQL:n käyttö matkatoimistossa

1. **Käyttäjän mieltymysten kerääminen**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **SQL-kyselyiden generointi**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **SQL-kyselyiden suorittaminen**

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

SQL:n hyödyntäminen osana Retrieval-Augmented Generation (RAG) -tekniikkaa mahdollistaa tekoälyagenttien, kuten matkatoimiston, dynaamisen tiedon hakemisen ja hyödyntämisen tarkkojen ja henkilökohtaisten suositusten tarjoamiseksi.

### Esimerkki metakognitiosta

Metakognition toteutuksen havainnollistamiseksi luodaan yksinkertainen agentti, joka *reflektoi päätöksentekoprosessiaan* ongelmaa ratkaistessaan. Tässä esimerkissä rakennamme järjestelmän, jossa agentti pyrkii optimoimaan hotellivalinnan, mutta arvioi omaa päättelyään ja mukauttaa strategiaansa, kun se tekee virheitä tai huonoja valintoja.

Simuloimme tätä yksinkertaisella esimerkillä, jossa agentti valitsee hotellit hinnan ja laadun perusteella, mutta "reflektoi" päätöksiään ja mukauttaa toimintaansa.

#### Miten tämä havainnollistaa metakognitiota:

1. **Alkuperäinen päätös**: Agentti valitsee halvimman hotellin ymmärtämättä laadun vaikutusta.
2. **Reflektio ja arviointi**: Alkuperäisen valinnan jälkeen agentti tarkistaa, oliko hotelli "huono" valinta käyttäjän palautteen perusteella. Jos laatu oli liian alhainen, agentti reflektoi päättelyään.
3. **Strategian mukauttaminen**: Agentti mukauttaa strategiaansa reflektiosta oppien ja siirtyy "halvimmasta" "parhaaseen laatuun", parantaen päätöksentekoprosessiaan tulevissa iteroinneissa.

Tässä esimerkki:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Stores the hotels chosen previously
        self.corrected_choices = []  # Stores the corrected choices
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Available strategies

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
        # Let's assume we have some user feedback that tells us whether the last choice was good or not
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Adjust strategy if the previous choice was unsatisfactory
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

# Simulate a list of hotels (price and quality)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Create an agent
agent = HotelRecommendationAgent()

# Step 1: The agent recommends a hotel using the "cheapest" strategy
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Step 2: The agent reflects on the choice and adjusts strategy if necessary
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Step 3: The agent recommends again, this time using the adjusted strategy
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Agentin metakognitiiviset kyvyt

Tärkeää tässä on agentin kyky:
- Arvioida aiempia valintojaan ja päätöksentekoprosessiaan.
- Mukauttaa strategiaansa reflektiosta oppien eli metakognitio käytännössä.

Tämä on yksinkertainen muoto metakognitiosta, jossa järjestelmä pystyy mukauttamaan päättelyprosessiaan sisäisen palautteen perusteella.

### Yhteenveto

Metakognitio on tehokas työkalu, joka voi merkittävästi parantaa tekoälyagenttien kyvykkyyksiä. Sisällyttämällä metakognitiivisia prosesseja voit suunnitella agentteja, jotka ovat älykkäämpiä, mukautuvampia ja tehokkaampia. Käytä lisäresursseja tutkiaksesi tekoälyagenttien metakognition kiehtovaa maailmaa.

### Onko sinulla lisää kysymyksiä metakognition suunnittelumallista?

Liity [Azure AI Foundry Discordiin](https://aka.ms/ai-agents/discord) tapaamaan muita oppijoita, osallistumaan toimistoaikoihin ja saamaan vastauksia tekoälyagentteihin liittyviin kysymyksiisi.

## Edellinen oppitunti

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

## Seuraava oppitunti

[AI Agents in Production](../10-ai-agents-production/README.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.