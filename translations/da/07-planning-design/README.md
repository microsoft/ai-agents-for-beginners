[![Planning Design Pattern](../../../translated_images/da/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Klik på billedet ovenfor for at se videoen af denne lektion)_

# Planning Design

## Introduktion

Denne lektion vil dække

* At definere et klart overordnet mål og bryde en kompleks opgave ned i håndterbare delopgaver.
* At udnytte struktureret output for mere pålidelige og maskinlæsbare svar.
* At anvende en hændelsesdrevet tilgang til at håndtere dynamiske opgaver og uventede input.

## Læringsmål

Efter at have gennemført denne lektion vil du have en forståelse om:

* At identificere og sætte et overordnet mål for en AI-agent, så den tydeligt ved, hvad der skal opnås.
* At nedbryde en kompleks opgave i håndterbare delopgaver og organisere dem i en logisk rækkefølge.
* At udstyre agenter med de rette værktøjer (f.eks. søgeværktøjer eller dataanalyseværktøjer), beslutte hvornår og hvordan de bruges, og håndtere uventede situationer der opstår.
* At evaluere resultaterne af delopgaver, måle ydelsen og iterere på handlinger for at forbedre det endelige output.

## Definere det Overordnede Mål og Nedbryde en Opgave

![Defining Goals and Tasks](../../../translated_images/da/defining-goals-tasks.d70439e19e37c47a.webp)

De fleste opgaver i den virkelige verden er for komplekse til at håndtere i ét trin. En AI-agent har brug for et kortfattet mål for at styre sin planlægning og handlinger. For eksempel, overvej målet:

    "Generer en 3-dages rejseplan."

Selvom det er enkelt at angive, kræver det stadig præcisering. Jo klarere målet er, desto bedre kan agenten (og eventuelle menneskelige samarbejdspartnere) fokusere på at opnå det rette resultat, såsom at skabe en omfattende rejseplan med flymuligheder, hotelanbefalinger og aktivitetsforslag.

### Opgavenedbrydning

Store eller indviklede opgaver bliver mere håndterbare, når de deles op i mindre, målrettede delopgaver.  
For rejseplan-eksemplet kan du nedbryde målet i:

* Flyreservation
* Hotelreservation
* Biludlejning
* Personalisering

Hver delopgave kan derefter håndteres af dedikerede agenter eller processer. Én agent kan specialisere sig i at søge efter de bedste flytilbud, en anden fokuserer på hotelreservationer osv. En koordinerende eller "nedstrøms" agent kan så samle disse resultater til en samlet og sammenhængende rejseplan for slutbrugeren.

Denne modulære tilgang tillader også løbende forbedringer. For eksempel kan du tilføje specialiserede agenter til madanbefalinger eller lokale aktivitetstilbud og forfine rejseplanen over tid.

### Struktureret output

Større sprogmodeller (LLMs) kan generere struktureret output (f.eks. JSON), som er nemmere for nedstrøms agenter eller tjenester at fortolke og behandle. Dette er især nyttigt i en multi-agent-sammenhæng, hvor vi kan udføre disse opgaver, når planlægningsoutputtet modtages.

Følgende Python-udsnit viser en simpel planlægningsagent, der nedbryder et mål i delopgaver og genererer en struktureret plan:

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

# Rejseunderopgave model
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # vi vil tildele opgaven til agenten

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Definer brugermeddelelsen
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

### Planlægningsagent med Multi-Agent Orkestrering

I dette eksempel modtager en Semantic Router Agent en brugerforespørgsel (f.eks. "Jeg har brug for en hotelplan til min rejse.").

Planlæggeren:

* Modtager Hotelplanen: Planlæggeren tager brugerens besked og, baseret på en systemprompt (inklusive tilgængelige agentdetaljer), genererer en struktureret rejseplan.
* Lister Agenter og Deres Værktøjer: Agentregistret indeholder en liste over agenter (f.eks. for fly, hotel, biludlejning og aktiviteter) sammen med de funktioner eller værktøjer, de tilbyder.
* Sender Planen til de Respektive Agenter: Afhængigt af antallet af delopgaver sender planlæggeren enten beskeden direkte til en dedikeret agent (ved enkeltopgaver) eller koordinerer via en gruppechatsmanager for multi-agent samarbejde.
* Opsummerer Resultatet: Til sidst opsummerer planlæggeren den genererede plan for klarhed.
Følgende Python-kodeeksempel illustrerer disse trin:

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

# Rejse SubTask Model

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # vi vil tildele opgaven til agenten

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Opret klienten

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Definer brugermeddelelsen

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

# Udskriv responsens indhold efter at have indlæst det som JSON

pprint(json.loads(response_content))
```

Det følgende er outputtet fra den tidligere kode, og du kan derefter bruge dette strukturerede output til at sende til `assigned_agent` og opsummere rejseplanen for slutbrugeren.

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

En eksempelnotebook med det tidligere kodeeksempel er tilgængelig [her](07-python-agent-framework.ipynb).

### Iterativ Planlægning

Nogle opgaver kræver frem-og-tilbage eller omplanlægning, hvor resultatet af en delopgave påvirker den næste. For eksempel, hvis agenten opdager et uventet dataformat ved booking af fly, kan det være nødvendigt at tilpasse sin strategi, inden den går videre til hotelreservationer.

Derudover kan brugerfeedback (f.eks. at en person beslutter sig for, at de foretrækker et tidligere fly) udløse en delvis omplanlægning. Denne dynamiske, iterative tilgang sikrer, at den endelige løsning stemmer overens med virkelige begrænsninger og skiftende brugerpræferencer.

f.eks. eksempelkode

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. det samme som den tidligere kode og videregiv brugerens historik, nuværende plan

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
# .. planlæg igen og send opgaverne til de respektive agenter
```

For mere omfattende planlægning, se Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> for løsning af komplekse opgaver.

## Resumé

I denne artikel har vi set et eksempel på, hvordan vi kan skabe en planlægger, der dynamisk kan vælge de definerede tilgængelige agenter. Outputtet fra planlæggeren nedbryder opgaverne og tildeler agenter, så de kan udføres. Det antages, at agenterne har adgang til de funktioner/værktøjer, der er nødvendige for at udføre opgaven. Ud over agenterne kan du inkludere andre mønstre som refleksion, opsummering og round robin chat for yderligere tilpasning.

## Yderligere Ressourcer

Magentic One - Et generalist multi-agent system til løsning af komplekse opgaver, der har opnået imponerende resultater på flere krævende agentiske benchmarks. Reference: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. I denne implementering skaber orkestratoren opgavespecifikke planer og delegerer disse opgaver til de tilgængelige agenter. Ud over planlægning anvender orkestratoren også en sporingsmekanisme til at overvåge opgavens fremskridt og omplanlægge efter behov.

### Har du flere spørgsmål om Planning Design Pattern?

Deltag i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for at møde andre elever, deltage i kontortid og få svar på dine spørgsmål om AI-agenter.

## Forrige lektion

[Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)

## Næste lektion

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->