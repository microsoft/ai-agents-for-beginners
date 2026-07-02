[![Planning Design Pattern](../../../translated_images/fi/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Napsauta yllä olevaa kuvaa katsoaksesi tämän oppitunnin videon)_

# Suunnittelumalli

## Johdanto

Tämä oppitunti kattaa

* Selkeän yleistavoitteen määrittämisen ja monimutkaisen tehtävän jakamisen hallittaviin osatehtäviin.
* Rakenteellisen tuotoksen hyödyntämisen luotettavampien ja koneellisesti luettavien vastausten saamiseksi.
* Tapahtumapohjaisen lähestymistavan soveltamisen dynaamisten tehtävien ja odottamattomien syötteiden käsittelemiseksi.

## Oppimistavoitteet

Oppitunnin suorittamisen jälkeen ymmärrät:

* Miten tunnistaa ja asettaa yleistavoite tekoälyagentille, varmistaen, että se tietää selkeästi, mitä pitää saavuttaa.
* Miten hajottaa monimutkainen tehtävä hallittaviksi osatehtäviksi ja järjestää ne loogiseen järjestykseen.
* Miten varustaa agentit oikeilla työkaluilla (esim. hakutyökalut tai data-analytiikkatyökalut), päättää milloin ja miten niitä käytetään sekä käsitellä odottamattomia tilanteita.
* Miten arvioida osatehtävien tuloksia, mitata suorituskykyä ja toistaa toimenpiteitä lopputuloksen parantamiseksi.

## Yleistavoitteen määrittäminen ja tehtävän pilkkominen

![Defining Goals and Tasks](../../../translated_images/fi/defining-goals-tasks.d70439e19e37c47a.webp)

Useimmat todellisen maailman tehtävät ovat liian monimutkaisia toteutettavaksi yhdellä askeleella. Tekoälyagentilla on tarve tiiviille tavoitteelle, joka ohjaa sen suunnittelua ja toimia. Esimerkiksi tavoite:

    "Laadi 3 päivän matkasuunnitelma."

Vaikka se on yksinkertainen ilmaista, se tarvitsee silti tarkennusta. Mitä selkeämpi tavoite on, sitä paremmin agentti (ja mahdolliset ihmiskumppanit) voivat keskittyä saavuttamaan oikean lopputuloksen, kuten luoda kattava matkasuunnitelma lentovaihtoehdoilla, hotellisuosituksilla ja aktiviteettiehdotuksilla.

### Tehtävän jakaminen osatehtäviin

Suuret tai monimutkaiset tehtävät muuttuvat hallittavammiksi, kun ne jaetaan pienempiin, tavoitelähtöisiin osatehtäviin.  
Matkasuunnitelman esimerkissä tavoitteen voisi pilkkoa seuraaviin:

* Lentovaraukset
* Hotellivaraukset
* Autonvuokraus
* Personalisointi

Jokainen osatehtävä voidaan sitten osoittaa erillisille agenteille tai prosesseille. Yksi agentti voi erikoistua hakemaan parhaat lentotarjoukset, toinen keskittyy hotellivarauksiin ja niin edelleen. Koordinoiva tai "alavirran" agentti voi koota nämä tulokset yhdeksi yhtenäiseksi matkasuunnitelmaksi loppukäyttäjälle.

Tämä modulaarinen lähestymistapa mahdollistaa myös asteittaiset parannukset. Esimerkiksi voit lisätä erikoistuneita agenteja ruoka- tai paikallisten aktiviteettien suosituksiin ja kehittää suunnitelmaa ajan myötä.

### Rakenteellinen tulostus

Laajamittaiset kielimallit (LLM:t) voivat tuottaa rakenteellista tulostetta (esim. JSON), jota alavirran agentit tai palvelut voivat helpommin jäsentää ja käsitellä. Tämä on erityisen hyödyllistä moniagenttiympäristössä, jossa nämä tehtävät voidaan toteuttaa suunnittelutuloksen vastaanoton jälkeen.

Seuraava Python-koodinäyte demonstroi yksinkertaista suunnitteluagenttia, joka pilkkoo tavoitteen osatehtäviin ja luo rakenteellisen suunnitelman:

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

# Matkan AlaTehtävä Malli
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # haluamme määrittää tehtävän agentille

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Määritä käyttäjän viesti
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

### Suunnitteluagentti moniagenttien orkestroinnilla

Tässä esimerkissä Semanttinen Reititin Agentti vastaanottaa käyttäjän pyynnön (esim. "Tarvitsen hotellisuunnitelman matkalleni").

Suunnittelija sitten:

* Vastaanottaa Hotellisuunnitelman: Suunnittelija ottaa käyttäjän viestin ja järjestelmäkehotteen (sisältäen käytettävissä olevien agenttien tiedot) perusteella luo rakenteellisen matkasuunnitelman.
* Listaa Agentit ja Niiden Työkalut: Agenttirekisteri sisältää listan agenteista (esim. lento, hotelli, autonvuokraus ja aktiviteetit) ja niiden tarjoamista toiminnoista tai työkaluista.
* Reitittää Suunnitelman Vastaaville Agenteille: Osatehtävien määrän mukaan suunnittelija joko lähettää viestin suoraan omistetulle agentille (yksittäisten tehtävien tapauksissa) tai koordinoi ryhmäkeskustelun kautta moniagenttisen yhteistyön.
* Yhteenveto Lopputuloksesta: Lopuksi suunnittelija tiivistää luodun suunnitelman selkeyden vuoksi.  
Seuraava Python-koodiesimerkki havainnollistaa näitä vaiheita:

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

# Matkustus osatehtävä malli

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # haluamme antaa tehtävän agentille

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

# Määrittele käyttäjän viesti

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

# Tulosta vastaussisältö ladattua JSON-muodossa

pprint(json.loads(response_content))
```

Seuraavaksi esitetään edellisen koodin tuotos, ja tätä rakenteellista tulostetta voit käyttää reitittämiseen `assigned_agent` -kenttään ja matkasuunnitelman yhteenvetoon loppukäyttäjälle.

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

Esimerkkinotebook edelliseen koodiesimerkkiin on saatavilla [täällä](07-python-agent-framework.ipynb).

### Iteratiivinen suunnittelu

Jotkin tehtävät vaativat edestakaista vuorovaikutusta tai uudelleensuunnittelua, jossa yhden osatehtävän tulos vaikuttaa seuraavaan. Esimerkiksi jos agentti kohtaa odottamattoman tietomuodon lentovarauksia tehdessään, sen täytyy ehkä mukauttaa strategiaansa ennen hotellivarauksiin siirtymistä.

Lisäksi käyttäjäpalaute (esim. ihmisen päätös valita aikaisempi lento) voi laukaista osittaisen uudelleensuunnittelun. Tämä dynaaminen ja iteratiivinen lähestymistapa varmistaa, että lopullinen ratkaisu vastaa todellisen maailman vaatimuksia ja muuttuvia käyttäjätoiveita.

esim. koodinäyte

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
# .. suunnittele uudelleen ja lähetä tehtävät asianomaisille agenteille
```

Laajempaa suunnittelua varten tutustu Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogipostaukseen</a>, joka käsittelee monimutkaisten tehtävien ratkaisemista.

## Yhteenveto

Tässä artikkelissa olemme tarkastelleet esimerkkiä siitä, miten luoda suunnittelija, joka voi dynaamisesti valita määritellyt agentit. Suunnittelijan tuotos pilkkoo tehtävät ja osoittaa agenteille suorittaakseen ne. Oletetaan, että agenteilla on pääsy tarvittaviin toimintoihin/työkaluihin tehtävän suorittamiseksi. Agenttien lisäksi voit sisällyttää muita malleja, kuten reflektiota, yhteenvetotyökaluja ja pyöröchat-systeemiä mukautuksen parantamiseksi.

## Lisäresurssit

Magnetic One - Yleiskäyttöinen moniagenttijärjestelmä monimutkaisten tehtävien ratkaisuun ja se on saavuttanut vaikuttavia tuloksia useilla haastavilla agenttitutkimusvertailuilla. Viite: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. Tässä toteutuksessa orkestroija luo tehtäväkohtaiset suunnitelmat ja delegoi ne käytettävissä oleville agenteille. Suunnittelun lisäksi orkestroija käyttää seurantamekanismia tehtävän etenemisen valvomiseksi ja uudelleensuunnittelee tarvittaessa.

### Onko sinulla lisäkysymyksiä Suunnittelumallista?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tavata muita oppijoita, osallistua toimistoaikoihin ja saada vastauksia AI-agenttikysymyksiisi.

## Edellinen oppitunti

[Luotettavien tekoälyagenttien rakentaminen](../06-building-trustworthy-agents/README.md)

## Seuraava oppitunti

[Moniagenttisuunnittelumalli](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->