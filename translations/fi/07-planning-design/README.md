[![Planning Design Pattern](../../../translated_images/fi/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Napsauta yllä olevaa kuvaa katsellaksesi tämän oppitunnin videon)_

# Suunnittelumalli

## Johdanto

Tässä oppitunnissa käsitellään

* Selkeän yleisen tavoitteen määrittäminen ja monimutkaisen tehtävän pilkkominen hallittaviin osatehtäviin.
* Rakenteellisen tuotoksen hyödyntäminen luotettavampien ja koneellisesti luettavien vastausten tuottamiseksi.
* Tapahtumapohjaisen lähestymistavan soveltaminen dynaamisten tehtävien ja odottamattomien syötteiden käsittelemiseksi.

## Oppimistavoitteet

Oppitunnin suorittamisen jälkeen ymmärrät:

* Miten tunnistaa ja asettaa yleinen tavoite tekoälyagentille varmistaen, että se tietää selvästi, mitä on saavutettava.
* Miten pilkkoa monimutkainen tehtävä hallittaviin osatehtäviin ja järjestää ne loogiseen järjestykseen.
* Miten varustaa agentit oikeilla työkaluilla (esim. hakutyökalut tai data-analytiikkatyökalut), päättää, milloin ja miten niitä käytetään, ja käsitellä odottamattomia tilanteita.
* Miten arvioida osatehtävien tuloksia, mitata suorituskykyä ja toistaa toimia parantaakseen lopputulosta.

## Yleisen tavoitteen määrittäminen ja tehtävän pilkkominen

![Määrittelytavoitteet ja tehtävät](../../../translated_images/fi/defining-goals-tasks.d70439e19e37c47a.webp)

Useimmat todelliset tehtävät ovat liian monimutkaisia ratkaistavaksi yhdellä vaiheella. Tekoälyagentilla täytyy olla ytimekäs päämäärä ohjaamaan suunnittelua ja toimia. Esimerkiksi tavoite:

    "Laadi 3 päivän matkaohjelma."

Vaikka tavoite on helppo ilmaista, se tarvitsee täsmentämistä. Mitä selkeämpi tavoite on, sitä paremmin agentti (ja myös ihmiset yhteistyökumppaneina) voivat keskittyä oikean lopputuloksen saavuttamiseen, kuten kattavan matkasuunnitelman laatimiseen lentovaihtoehtoineen, hotellisuosituksineen ja aktiviteettiehdotuksineen.

### Tehtävän pilkkominen

Suuret tai monimutkaiset tehtävät muuttuvat hallittavammiksi, kun ne jaetaan pienempiin, tavoitekeskeisiin osatehtäviin.
Matkaohjelmaesimerkissä voit pilkkoa tavoitteen seuraaviin osiin:

* Lentojen varaaminen
* Hotellivaraus
* Autonvuokraus
* Personalisointi

Jokainen osatehtävä voidaan toteuttaa omistautuneiden agenttien tai prosessien toimesta. Yksi agentti voi erikoistua parhaiden lentotarjousten etsimiseen, toinen hotellivarausten hoitamiseen ja niin edelleen. Koordinoiva tai "jatkotoimintoja tekevä" agentti kokoaa nämä tulokset yhdeksi yhtenäiseksi matkasuunnitelmaksi loppukäyttäjälle.

Tämä modulaarinen lähestymistapa mahdollistaa myös asteittaiset parannukset. Voit esimerkiksi lisätä erikoistuneita agentteja ruoka- tai paikallisia aktiviteetteja koskeville suosituksille ja hioa matkasuunnitelmaa ajan mittaan.

### Rakenteellinen tuotanto

Suuret kielimallit (LLM) voivat tuottaa rakenteellista sisältöä (esim. JSON), jota on helpompi käsitellä ja tulkita seuraavissa agenttien tai palveluiden vaiheissa. Tämä on erityisen hyödyllistä monianturaympäristössä, jossa nämä tehtävät voidaan toteuttaa sen jälkeen, kun suunnitelma on saatu.

Seuraava Python-esimerkki osoittaa yksinkertaisen suunnitteluagentin, joka pilkkoo tavoitteen osatehtäviin ja luo rakenteellisen suunnitelman:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Matkasuorite-malli
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # haluamme määrätä tehtävän agentille

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

### Suunnitteluagentti monianturien orkestroinnilla

Tässä esimerkissä Semantic Router Agent vastaanottaa käyttäjän pyynnön (esim. "Tarvitsen hotellisuunnitelman matkalleni.").

Suunnittelija sitten:

* Vastaanottaa hotellisuunnitelman: Suunnittelija ottaa käyttäjän viestin ja järjestelmäkehotteen (mukaan lukien käytettävissä olevien agenttien tiedot) perusteella luo rakenteellisen matkasuunnitelman.
* Listaa agentit ja niiden työkalut: Agentin rekisterissä on lista agenteista (esim. lento, hotelli, autonvuokraus, aktiviteetit) sekä niiden tarjoamista toiminnoista tai työkaluista.
* Reitittää suunnitelman asianmukaisille agenteille: Osatehtävien määrän perusteella suunnittelija joko lähettää viestin suoraan omistautuneelle agentille (yksityisen tehtävän tilanteissa) tai koordinoi ryhmäkeskustelun hallinnan kautta monianturayhteistyötä.
* Tiivistää lopputuloksen: Lopuksi suunnittelija tiivistää luodun suunnitelman selkeyden takaamiseksi.
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

# Matkailualitehtävän malli

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # Haluamme osoittaa tehtävän agentille

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Luo asiakas

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

# Tulosta vastaussisältö sen lataamisen jälkeen JSON-muodossa

pprint(json.loads(response_content))
```

Alla on edellisen koodin tuloste, ja tätä rakenteellista tuotosta voidaan käyttää reitittämään `assigned_agent` -agentille ja tiivistämään matkasuunnitelma loppukäyttäjälle.

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

Esimerkkimuistio edelliseen koodiesimerkkiin löytyy [tästä](./code_samples/07-python-agent-framework.ipynb).

### Iteratiivinen suunnittelu

Joissain tehtävissä tarvitaan edestakaista vuorovaikutusta tai uudelleensuunnittelua, jossa yhden osatehtävän tulos vaikuttaa seuraavaan. Esimerkiksi jos agentti kohtaa odottamattoman tietomuodon lentojen varauksessa, sen voi olla tarpeen muuttaa strategiaansa ennen hotellivarausten aloittamista.

Lisäksi käyttäjän palaute (esim. ihminen päättää suosia aikaisempaa lentoa) voi laukaista osittaisen uudelleensuunnittelun. Tämä dynaaminen ja iteratiivinen lähestymistapa varmistaa, että lopullinen ratkaisu vastaa todellisia rajoituksia ja muuttuvia käyttäjän mieltymyksiä.

esim. esimerkkikoodi

```python
import os
from agent_framework.foundry import FoundryChatClient
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
# .. tee uudelleen suunnitelma ja lähetä tehtävät kyseisille agenteille
```

Laajemman suunnittelun osalta kannattaa tutustua Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogikirjoitus</a>, joka käsittelee monimutkaisten tehtävien ratkaisua.

## Yhteenveto

Tässä artikkelissa olemme tarkastelleet esimerkkiä siitä, kuinka voimme luoda suunnittelijan, joka voi dynaamisesti valita määritellyt käytettävissä olevat agentit. Suunnittelijan tuotos pilkkoo tehtävät ja nimeää agentit niiden suorittamista varten. Oletuksena on, että agenteilla on käytettävissään tehtävän suorittamiseen tarvittavat toiminnot/työkalut. Agenttien lisäksi mukaan voi liittää muita malleja kuten reflektio, tiivistäjä ja pyörivä keskustelu lisämuokkausta varten.

## Lisäresurssit

Magnetic One - Yleistarkoituksen monianturijärjestelmä monimutkaisten tehtävien ratkaisuun ja on saavuttanut vaikuttavia tuloksia useilla haastavilla agenttitehtävävertailuilla. Viite: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. Tässä toteutuksessa orkestroija luo tehtäväkohtaiset suunnitelmat ja delegoi ne käytettävissä oleville agenteille. Suunnittelun lisäksi orkestroija käyttää myös seurantamekanismia seuratakseen tehtävän etenemistä ja tarvittaessa uudelleensuunnittelee.

### Onko sinulla lisää kysymyksiä suunnittelumallista?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tavata oppijoita, osallistua aukioloaikoihin ja saada vastauksia AI-agentteihin liittyviin kysymyksiisi.

## Edellinen oppitunti

[Rakentamalla luotettavia AI-agentteja](../06-building-trustworthy-agents/README.md)

## Seuraava oppitunti

[Monianturimalli](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->