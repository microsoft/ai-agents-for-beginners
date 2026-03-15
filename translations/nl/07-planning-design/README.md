[![Planning Design Pattern](../../../translated_images/nl/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

# Planning Ontwerp

## Introductie

Deze les behandelt

* Het definiëren van een duidelijk overkoepelend doel en het opsplitsen van een complexe taak in beheersbare taken.
* Het benutten van gestructureerde output voor betrouwbaardere en machineleesbare antwoorden.
* Het toepassen van een event-driven aanpak om dynamische taken en onverwachte input te verwerken.

## Leerdoelen

Na het voltooien van deze les zul je inzicht hebben in:

* Het identificeren en vaststellen van een overkoepelend doel voor een AI-agent, zodat deze precies weet wat moet worden bereikt.
* Het ontleden van een complexe taak in beheersbare subtaken en deze organiseren in een logische volgorde.
* Het voorzien van agenten van de juiste tools (bijv. zoektools of data-analysetools), beslissen wanneer en hoe deze worden gebruikt, en omgaan met onverwachte situaties die zich voordoen.
* Het evalueren van de uitkomsten van subtaken, het meten van prestaties en het itereren van acties om het eindresultaat te verbeteren.

## Het definieren van het overkoepelende doel en het opsplitsen van een taak

![Definiëren van doelen en taken](../../../translated_images/nl/defining-goals-tasks.d70439e19e37c47a.webp)

De meeste taken in de echte wereld zijn te complex om in één stap aan te pakken. Een AI-agent heeft een beknopt doel nodig om zijn planning en acties te leiden. Overweeg bijvoorbeeld het doel:

    "Genereer een reisschema voor 3 dagen."

Hoewel dit eenvoudig te omschrijven is, moet het nog worden verfijnd. Hoe duidelijker het doel, hoe beter de agent (en eventuele menselijke samenwerkers) zich kunnen richten op het bereiken van het juiste resultaat, zoals het maken van een uitgebreid reisschema met vluchtopties, hotelaanbevelingen en activiteitensuggesties.

### Taakopsplitsing

Grote of ingewikkelde taken worden beter beheersbaar wanneer ze worden opgesplitst in kleinere, doelgerichte subtaken.
Voor het voorbeeld van het reisschema zou je het doel kunnen opsplitsen in:

* Vluchtreservering
* Hotelreservering
* Autohuur
* Personalisatie

Elke subtaak kan dan worden aangepakt door gespecialiseerde agenten of processen. De ene agent is mogelijk gespecialiseerd in het zoeken naar de beste vliegticketdeals, een andere richt zich op hotelreserveringen, enzovoort. Een coördinerende of “downstream” agent kan deze resultaten vervolgens samenvoegen tot één samenhangend reisschema voor de eindgebruiker.

Deze modulaire aanpak maakt ook stapsgewijze verbeteringen mogelijk. Zo kan je gespecialiseerde agenten toevoegen voor Voedselaanbevelingen of Lokale Activiteitensuggesties en het reisschema na verloop van tijd verfijnen.

### Gestructureerde output

Grote taalmodellen (LLM’s) kunnen gestructureerde output genereren (bijv. JSON) die makkelijker te parseren en verwerken is door downstream-agenten of -diensten. Dit is vooral nuttig in een multi-agent context, waarin we deze taken kunnen uitvoeren nadat de planningsuitvoer is ontvangen.

De volgende Python-code toont een eenvoudige planning agent die een doel opsplitst in subtaken en een gestructureerd plan genereert:

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

# Reis SubTaak Model
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # we willen de taak aan de agent toewijzen

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Definieer het gebruikersbericht
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

### Planning Agent met Multi-Agent Orkestratie

In dit voorbeeld ontvangt een Semantic Router Agent een gebruikersverzoek (bijv. "Ik heb een hotelplan nodig voor mijn reis.").

De planner:

* Ontvangt het hotelplan: De planner neemt het bericht van de gebruiker en genereert op basis van een system prompt (inclusief beschikbare agentdetails) een gestructureerd reisplan.
* Lijst agenten en hun tools op: Het agentregister bevat een lijst van agenten (bijv. voor vlucht, hotel, autohuur en activiteiten) met de functies of tools die ze bieden.
* Routeert het plan naar de respectievelijke agenten: Afhankelijk van het aantal subtaken stuurt de planner het bericht direct naar een toegewijde agent (bij enkelvoudige taken) of coördineert via een groepschat-manager voor samenwerking tussen meerdere agenten.
* Vat het resultaat samen: Tot slot vat de planner het gegenereerde plan samen ter verduidelijking.
De volgende Python-code illustreert deze stappen:

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

# Reissubtaakmodel

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # we willen de taak toewijzen aan de agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Maak de client aan

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Definieer het gebruikersbericht

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

# Druk de reactie-inhoud af nadat deze als JSON is geladen

pprint(json.loads(response_content))
```

Wat volgt is de uitvoer van bovenstaande code en je kunt deze gestructureerde output vervolgens gebruiken om naar `assigned_agent` te routeren en het reisplan aan de eindgebruiker samen te vatten.

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

Een voorbeeldnotebook met bovenstaande code is beschikbaar [hier](07-python-agent-framework.ipynb).

### Iteratieve planning

Sommige taken vereisen een heen-en-weer of herplanning, waarbij de uitkomst van de ene subtaak de volgende beïnvloedt. Bijvoorbeeld, als de agent een onverwacht dataformaat ontdekt bij het boeken van vluchten, moet hij mogelijk zijn strategie aanpassen voordat hij verdergaat met hotelreserveringen.

Daarnaast kan feedback van de gebruiker (bijv. een mens die besluit een vroegere vlucht te verkiezen) een gedeeltelijke herplanning triggeren. Deze dynamische, iteratieve aanpak zorgt ervoor dat de uiteindelijke oplossing aansluit bij de realiteit en veranderende gebruikersvoorkeuren.

bijv voorbeeldcode

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. hetzelfde als de vorige code en geef de gebruikersgeschiedenis, huidig plan door

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
# .. herplannen en de taken naar de respectieve agenten sturen
```

Voor uitgebreidere planning kun je de Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> raadplegen voor het oplossen van complexe taken.

## Samenvatting

In dit artikel hebben we gekeken naar een voorbeeld van hoe we een planner kunnen maken die dynamisch de beschikbare gedefinieerde agenten selecteert. De output van de Planner splitst de taken op en wijst de agenten toe zodat ze uitgevoerd kunnen worden. Er wordt aangenomen dat de agenten toegang hebben tot de functies/tools die nodig zijn om de taak uit te voeren. Naast de agenten kun je ook andere patronen opnemen, zoals reflectie, samenvatting en round robin chat, om het verder aan te passen.

## Aanvullende bronnen

Magentic One – Een Generalistische multi-agent systeem voor het oplossen van complexe taken en die indrukwekkende resultaten heeft behaald op meerdere uitdagende agent benchmarks. Referentie: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. In deze implementatie maakt de orkestrator taak specifieke plannen en delegeert deze taken aan de beschikbare agenten. Naast planning hanteert de orkestrator ook een tracking mechanisme om de voortgang van de taak te monitoren en waar nodig te herplannen.

### Heb je meer vragen over het Planning Ontwerp Patroon?

Sluit je aan bij de [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) om andere lerenden te ontmoeten, deel te nemen aan spreekuren en je AI Agents-vragen beantwoord te krijgen.

## Vorige les

[Betrouwbare AI Agents bouwen](../06-building-trustworthy-agents/README.md)

## Volgende les

[Multi-Agent Ontwerp Patroon](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->