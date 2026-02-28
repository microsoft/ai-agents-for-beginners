[![Planning Design Pattern](../../../translated_images/da/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Klik på billedet ovenfor for at se videoen af denne lektion)_

# Planlægningsdesign

## Introduktion

Denne lektion vil dække

* At definere et klart overordnet mål og opdele en kompleks opgave i håndterbare opgaver.
* At udnytte struktureret output for mere pålidelige og maskinlæselige svar.
* At anvende en hændelsesdrevet tilgang til at håndtere dynamiske opgaver og uforudsete input.

## Læringsmål

Efter at have gennemført denne lektion vil du have en forståelse af:

* At identificere og sætte et overordnet mål for en AI-agent, og sikre at den klart ved, hvad der skal opnås.
* At opdele en kompleks opgave i håndterbare delopgaver og organisere dem i en logisk rækkefølge.
* At udstyre agenter med de rette værktøjer (f.eks. søgeværktøjer eller dataanalyseværktøjer), beslutte hvornår og hvordan de skal bruges, og håndtere uventede situationer, der opstår.
* At evaluere delopgavernes resultater, måle ydeevne og gennemføre iterationer på handlinger for at forbedre det endelige output.

## Definere det overordnede mål og opdele en opgave

![Definere mål og opgaver](../../../translated_images/da/defining-goals-tasks.d70439e19e37c47a.webp)

De fleste opgaver i den virkelige verden er for komplekse til at tackle i ét enkelt trin. En AI-agent har brug for et kortfattet mål for at kunne styre sin planlægning og handlinger. For eksempel overvej målet:

    "Generer en rejseplan for 3 dage."

Selvom det er enkelt at formulere, kræver det stadig forfining. Jo klarere målet er, desto bedre kan agenten (og eventuelle menneskelige samarbejdspartnere) fokusere på at opnå det rigtige resultat, såsom at skabe en omfattende rejseplan med flymuligheder, hotelanbefalinger og aktivitetsforslag.

### Opgaveopdeling

Store eller indviklede opgaver bliver lettere at håndtere, når de opdeles i mindre, målrettede delopgaver.
For rejseplaneksemplet kan du opdele målet i:

* Flybestilling
* Hotelbestilling
* Biludlejning
* Personalisering

Hver delopgave kan derefter håndteres af dedikerede agenter eller processer. Én agent kan specialisere sig i at søge efter de bedste flytilbud, en anden fokuserer på hotelbestillinger osv. En koordinerende eller "nedstrøms" agent kan så samle disse resultater til én sammenhængende rejseplan til slutbrugeren.

Denne modulære tilgang tillader også løbende forbedringer. For eksempel kan du tilføje specialiserede agenter til Madanbefalinger eller Lokale aktivitetsforslag og forbedre rejseplanen over tid.

### Struktureret output

Store sprogmodeller (LLMs) kan generere struktureret output (f.eks. JSON), som er nemmere for nedstrømsagenter eller services at analysere og bearbejde. Dette er især nyttigt i en multi-agent kontekst, hvor vi kan iværksætte disse opgaver, efter planlægningsoutputtet er modtaget.

Følgende Python-udsnit viser en simpel planlægningsagent, der opdeler et mål i delopgaver og genererer en struktureret plan:

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

# Rejse delopgave model
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

### Planlægningsagent med multi-agent orkestrering

I dette eksempel modtager en Semantic Router Agent en brugerforespørgsel (f.eks. "Jeg har brug for en hotelplan til min rejse.").

Planlæggeren:

* Modtager hotelplanen: Planlæggeren tager brugerens besked og genererer baseret på et systemprompt (inklusive tilgængelige agentdetaljer) en struktureret rejseplan.
* Oplister agenter og deres værktøjer: Agentregisteret indeholder en liste over agenter (f.eks. til fly, hotel, biludlejning og aktiviteter) sammen med funktioner eller værktøjer, de tilbyder.
* Ruter planen til de respektive agenter: Afhængigt af antallet af delopgaver sender planlæggeren enten beskeden direkte til en dedikeret agent (ved én-opgave scenarier) eller koordinerer via en gruppechatmanager til multi-agent samarbejde.
* Opsummerer resultatet: Til sidst opsummerer planlæggeren den genererede plan for klarhed.
Følgende Python-kodesample illustrerer disse trin:

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

# Rejse delopgave model

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

# Udskriv svarindholdet efter indlæsning som JSON

pprint(json.loads(response_content))
```

Det følgende er outputtet fra den tidligere kode, og du kan derefter bruge dette strukturerede output til at rute til `assigned_agent` og opsummere rejseplanen for slutbrugeren.

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

Et eksempel-notebook med den tidligere kode er tilgængeligt [her](07-python-agent-framework.ipynb).

### Iterativ planlægning

Nogle opgaver kræver frem og tilbage eller omplanlægning, hvor resultatet af én delopgave påvirker den næste. For eksempel, hvis agenten opdager et uventet dataformat under flybestilling, kan det være nødvendigt at tilpasse sin strategi, før der fortsættes med hotelbestillinger.

Derudover kan brugerfeedback (f.eks. en person, der beslutter, at de foretrækker et tidligere fly) udløse en delvis omplanlægning. Denne dynamiske, iterative tilgang sikrer, at den endelige løsning stemmer overens med virkelige begrænsninger og brugernes skiftende præferencer.

f.eks. eksempel på kode

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. det samme som forrige kode og overfør brugerens historik, nuværende plan

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

For mere omfattende planlægning kan du tjekke Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> for løsning af komplekse opgaver.

## Resumé

I denne artikel har vi set et eksempel på, hvordan vi kan skabe en planlægger, der dynamisk kan vælge de tilgængelige agenter, der er defineret. Outputtet fra planlæggeren opdeler opgaverne og tildeler agenter, så de kan udføres. Det forudsættes, at agenterne har adgang til de funktioner/værktøjer, der er nødvendige for at udføre opgaven. Udover agenterne kan du inkludere andre mønstre som refleksion, opsummering og round robin chat for yderligere tilpasning.

## Yderligere ressourcer

Magnetic One - Et generalistisk multi-agent system til løsning af komplekse opgaver, som har opnået imponerende resultater på flere udfordrende agentiske benchmarks. Reference: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. I denne implementering skaber orkestratoren opgavespecifikke planer og delegerer disse opgaver til de tilgængelige agenter. Ud over planlægning anvender orkestratoren også en sporingsmekanisme til at overvåge opgavens fremdrift og omplanlægger efter behov.

### Har du flere spørgsmål om Planlægningsdesignmønsteret?

Deltag i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for at møde andre lærende, deltage i kontortimer og få svar på dine AI-agent-spørgsmål.

## Forrige lektion

[Opbygning af pålidelige AI-agenter](../06-building-trustworthy-agents/README.md)

## Næste lektion

[Multi-agent designmønster](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->