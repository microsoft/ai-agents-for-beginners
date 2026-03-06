[![Planning Design Pattern](../../../translated_images/fi/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Klikkaa yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

# Suunnittelumalli

## Johdanto

Tässä oppitunnissa käsitellään

* Yhtenäisen tavoitteen määrittäminen ja monimutkaisen tehtävän jakaminen hallittaviin osiin.
* Rakenteellisen tulosteen hyödyntäminen luotettavampien ja koneellisesti luettavien vastausten aikaansaamiseksi.
* Tapahtumalähtöisen lähestymistavan soveltaminen dynaamisten tehtävien ja odottamattomien syötteiden käsittelyyn.

## Oppimistavoitteet

Oppitunnin suoritettuasi ymmärrät:

* Tunnistaa ja asettaa tekoälyagentille kokonaisvaltainen tavoite varmistaen, että se tietää selkeästi, mitä pitää saavuttaa.
* Hajottaa monimutkainen tehtävä hallittaviin alatehtäviin ja järjestää ne loogiseksi kokonaisuudeksi.
* Varustaa agentit oikeilla työkaluilla (esim. hakutyökalut tai data-analytiikkatyökalut), päättää milloin ja miten niitä käytetään sekä käsitellä odottamattomia tilanteita.
* Arvioida alatehtävien tuloksia, mitata suorituskykyä ja iteratiivisesti parantaa lopputulosta.

## Kokonaisvaltaisen tavoitteen määrittäminen ja tehtävän pilkkominen

![Defining Goals and Tasks](../../../translated_images/fi/defining-goals-tasks.d70439e19e37c47a.webp)

Useimmat todellisen elämän tehtävät ovat liian monimutkaisia ratkaistavaksi yhdellä askeleella. Tekoälyagentilla tulee olla ytimekäs tavoite, joka ohjaa sen suunnittelua ja toimia. Esimerkiksi tavoite:

    "Laadi 3 päivän matkaohjelma."

Vaikka se on yksinkertainen ilmaista, se vaatii silti tarkennusta. Mitä selkeämpi tavoite on, sitä paremmin agentti (ja mahdolliset ihmiskumppanit) voivat keskittyä saavuttamaan oikean lopputuloksen, kuten kattavan reittisuunnitelman lentovaihtoehtoineen, hotellisuosituksineen ja aktiviteettiehdotuksineen.

### Tehtävän hajottaminen

Suurista tai monimutkaisista tehtävistä tulee hallittavampia, kun ne jaetaan pienempiin, tavoitesuuntautuneisiin alatehtäviin.
Matkaohjelman esimerkin tapauksessa tavoite voidaan jakaa seuraaviin osiin:

* Lentojen varaaminen
* Hotellin varaaminen
* Auton vuokraus
* Personalisointi

Jokainen alatehtävä voidaan käsitellä omistautuneiden agenttien tai prosessien toimesta. Yksi agentti voi erikoistua parhaiden lentotarjousten etsimiseen, toinen hotellivarauksiin, ja niin edelleen. Koordinoiva tai "alemman tason" agentti voi sitten koota nämä tulokset yhdeksi johdonmukaiseksi matkasuunnitelmaksi käyttäjälle.

Tämä modulaarinen lähestymistapa myös mahdollistaa asteittaiset parannukset. Esimerkiksi voit lisätä erikoistuneita agentteja ruoka- tai paikallisten aktiviteettien suosituksiin ja hioa reissusuunnitelmaa ajan myötä.

### Rakenteellinen tuloste

Suuret kielimallit (LLM:t) voivat tuottaa rakenteellista tulostetta (esim. JSON), joka on helpompi käsitellä ja jäsentää alempitasoisissa agenteissa tai palveluissa. Tämä on erityisen hyödyllistä monen agentin tilanteissa, joissa voimme suorittaa tehtävät suunnittelun tuottaman tuloksen jälkeen.

Seuraava Python-koodikatkelma havainnollistaa yksinkertaista suunnitteluagenttia, joka pilkkoo tavoitteen alatehtäviin ja tuottaa rakenteellisen suunnitelman:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Matkan osatehtävämalli
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # haluamme antaa tehtävän agentille

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Määrittele käyttäjän viesti
system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Provide your response in JSON format with the following structure:
{'main_task': 'Plan a family trip from Singapore to Melbourne.',
 'subtasks': [{'assigned_agent': 'flight_booking',
               'task_details': 'Book round-trip flights from Singapore to '
                               'Melbourne.'}
    Below are the available agents specialised in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text
pprint(json.loads(response_content))
```

### Suunnitteluagentti monen agentin orkestroinnilla

Tässä esimerkissä Semanttinen Reititin -agentti vastaanottaa käyttäjän pyynnön (esim. "Tarvitsen hotellisuunnitelman matkalleni.").

Suunnittelija sitten:

* Vastaanottaa hotellisuunnitelman: Suunnittelija ottaa käyttäjän viestin ja järjestelmän promptin (sisältäen saatavilla olevat agentin tiedot) perusteella tuottaa rakenteellisen matkasuunnitelman.
* Listaa agentit ja niiden työkalut: Agenttirekisterissä on lista agenteista (esim. lento, hotelli, autonvuokraus ja aktiviteetit) sekä niille tarjottavista toiminnoista tai työkaluista.
* Reitittää suunnitelman asianmukaisille agenteille: Alatehtävien määrän perusteella suunnittelija joko lähettää viestin suoraan omistautuneelle agentille (yksittäistehtävissä) tai koordinoi ryhmäkeskustelun kautta monen agentin yhteistyötä varten.
* Tiivistää lopputuloksen: Lopuksi suunnittelija tiivistää luodun suunnitelman selkeyden vuoksi.
Seuraava Python-koodiesimerkki havainnollistaa nämä vaiheet:

```python

from pydantic import BaseModel

from enum import Enum
from typing import List, Optional, Union

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Matkan alitehtävän malli

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # haluamme osoittaa tehtävän agentille

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Luo asiakas

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Määritä käyttäjän viesti

system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text

# Tulosta vastaussisältö ladattuaan se JSON-muodossa

pprint(json.loads(response_content))
```

Seuraava on edellisen koodin tuotos, ja voit käyttää tätä rakenteellista tulostetta reitittääksesi viestit `assigned_agent` -kohteeseen ja tiivistääksesi matkasuunnitelman käyttäjälle.

```json
{
    "is_greeting": "False",
    "main_task": "Plan a family trip from Singapore to Melbourne.",
    "subtasks": [
        {
            "assigned_agent": "flight_booking",
            "task_details": "Book round-trip flights from Singapore to Melbourne."
        },
        {
            "assigned_agent": "hotel_booking",
            "task_details": "Find family-friendly hotels in Melbourne."
        },
        {
            "assigned_agent": "car_rental",
            "task_details": "Arrange a car rental suitable for a family of four in Melbourne."
        },
        {
            "assigned_agent": "activities_booking",
            "task_details": "List family-friendly activities in Melbourne."
        },
        {
            "assigned_agent": "destination_info",
            "task_details": "Provide information about Melbourne as a travel destination."
        }
    ]
}
```

Esimerkkimateriaali yllä olevaan koodiin löytyy [täältä](07-python-agent-framework.ipynb).

### Iteratiivinen suunnittelu

Joissakin tehtävissä tarvitaan edestakaista kommunikaatiota tai uudelleensuunnittelua, jossa yhden alatehtävän tulos vaikuttaa seuraavaan. Esimerkiksi, jos agentti havaitsee odottamattoman tiedostomuodon lentovarauksia tehdessään, se voi joutua mukauttamaan strategiaansa ennen hotellivarauksia.

Lisäksi käyttäjän palaute (esim. ihmisen päätös haluta aikaisempi lento) voi käynnistää osittaisen uudelleensuunnittelun. Tämä dynaaminen, iteratiivinen lähestymistapa varmistaa, että lopullinen ratkaisu vastaa todellisen maailman rajoitteita ja käyttäjän muuttuvia mieltymyksiä.

esim. koodia

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. sama kuin edellisessä koodissa ja siirrä käyttäjän historia, nykyinen suunnitelma

system_prompt = """You are a planner agent to optimize the
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(
    input=user_message,
    instructions=system_prompt,
    context=f"Previous travel plan - {TravelPlan}",
)
# .. tee uusi suunnitelma ja lähetä tehtävät vastaaville agenteille
```

Laajempaan suunnitteluun tutustu Magnetic One - <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">blogikirjoitukseen</a> monimutkaisten tehtävien ratkaisemiseksi.

## Yhteenveto

Tässä artikkelissa olemme tarkastelleet esimerkkiä siitä, miten suunnittelija pystyy dynaamisesti valitsemaan määritellyt saatavilla olevat agentit. Suunnittelijan tuotos hajottaa tehtävät ja määrittää agentit, jotta ne voidaan suorittaa. Oletetaan, että agenteilla on pääsy tehtävän suorittamiseen vaadittuihin toimintoihin/työkaluihin. Agenttien lisäksi voit sisällyttää myös muita malleja, kuten reflektoinnin, tiivistäjän ja pyörivän keskustelun mukauttamaan prosessia lisää.

## Lisäresurssit

Magentic One - Yleiskäyttöinen monien agenttien järjestelmä monimutkaisten tehtävien ratkaisuun, joka on saavuttanut vaikuttavia tuloksia useissa haastavissa agenttiparametreissa. Lähde: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. Tässä toteutuksessa orkestroija laatii tehtäväkohtaiset suunnitelmat ja delegoi ne saatavilla oleville agenteille. Suunnittelun lisäksi orkestroija käyttää myös seurantamekanismia tehtävän etenemisen tarkkailuun ja tarvittaessa uudelleensuunnitteluun.

### Lisää kysymyksiä Suunnittelumallista?

Liity [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) -kanavalle tavata muita oppijoita, osallistua työaikoihin ja saada vastauksia AI-agenttikysymyksiisi.

## Edellinen oppitunti

[Luotettavien AI-agenttien rakentaminen](../06-building-trustworthy-agents/README.md)

## Seuraava oppitunti

[Moni-agentin suunnittelumalli](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulisi pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattilaisen tekemää ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->