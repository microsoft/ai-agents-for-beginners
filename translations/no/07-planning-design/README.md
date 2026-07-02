[![Planning Design Pattern](../../../translated_images/no/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Klikk på bildet over for å se video av denne leksjonen)_

# Planleggingsdesign

## Introduksjon

Denne leksjonen vil dekke

* Å definere et klart overordnet mål og bryte en kompleks oppgave ned i håndterbare oppgaver.
* Å utnytte strukturert output for mer pålitelige og maskinlesbare svar.
* Å bruke en hendelsesdrevet tilnærming for å håndtere dynamiske oppgaver og uventede innspill.

## Læringsmål

Etter å ha fullført denne leksjonen vil du ha forståelse for:

* Å identifisere og sette et overordnet mål for en AI-agent, og sikre at den tydelig vet hva som skal oppnås.
* Å dele opp en kompleks oppgave i håndterbare deloppgaver og organisere dem i en logisk rekkefølge.
* Å utstyre agenter med riktige verktøy (f.eks. søkeverktøy eller dataanalytiske verktøy), bestemme når og hvordan de brukes, og håndtere uventede situasjoner som oppstår.
* Å evaluere resultatene av deloppgaver, måle ytelse og iterere på handlinger for å forbedre sluttresultatet.

## Definere det overordnede målet og bryte ned en oppgave

![Defining Goals and Tasks](../../../translated_images/no/defining-goals-tasks.d70439e19e37c47a.webp)

De fleste virkelige oppgaver er for komplekse til å løses i ett steg. En AI-agent trenger et konsist mål for å styre sin planlegging og handlinger. For eksempel, vurder målet:

    "Lag en reiserute for 3 dager."

Selv om det er enkelt å si, trenger det fortsatt presisering. Jo klarere målet er, desto bedre kan agenten (og eventuelle menneskelige samarbeidspartnere) fokusere på å oppnå riktig resultat, slik som å lage en omfattende reiserute med flyalternativer, hotell anbefalinger og aktivitetsforslag.

### Oppgavedekomponering

Store eller komplekse oppgaver blir lettere å håndtere når de deles opp i mindre, målrettede deloppgaver.  
For eksempelet med reiseruten kan du dele opp målet i:

* Flybestilling
* Hotellbestilling
* Leiebil
* Personlig tilpasning

Hver deloppgave kan deretter håndteres av dedikerte agenter eller prosesser. En agent kan spesialisere seg på å finne de beste flytilbudene, en annen på hotellbestillinger, og så videre. En koordinerende eller «nedstrøms» agent kan deretter sette sammen disse resultatene til en samlet reiserute for sluttbrukeren.

Denne modulære tilnærmingen tillater også trinnvise forbedringer. For eksempel kan du legge til spesialiserte agenter for Matanbefalinger eller Lokale Aktivitetsforslag og forbedre reiseruten over tid.

### Strukturert output

Store språkmodeller (LLMs) kan generere strukturert output (f.eks. JSON) som er enklere for nedstrøms agenter eller tjenester å tolke og behandle. Dette er spesielt nyttig i en multi-agent kontekst, hvor vi kan utføre disse oppgavene etter at planleggingsresultatet er mottatt.

Følgende Python-eksempel demonstrerer en enkel planleggingsagent som deler et mål opp i deloppgaver og genererer en strukturert plan:

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

# Reise deloppgave modell
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # vi vil tildele oppgaven til agenten

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Definer brukermeldingen
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

### Planleggingsagent med multi-agent orkestrering

I dette eksempelet mottar en Semantisk Router Agent en brukerforespørsel (f.eks. "Jeg trenger en hotellplan for turen min.").

Planleggeren gjør så:

* Mottar hotellplanen: Planleggeren tar brukerens melding og, basert på et systemprompt (inkludert tilgjengelige agentdetaljer), genererer en strukturert reiseplan.
* Lister opp agenter og deres verktøy: Agentregisteret inneholder en liste over agenter (f.eks. for fly, hotell, leiebil og aktiviteter) sammen med funksjonene eller verktøyene de tilbyr.
* Ruter planen til de respektive agentene: Avhengig av antallet deloppgaver sender planleggeren enten meldingen direkte til en dedikert agent (for enkeltsoppgaver) eller koordinerer via en gruppechattsjef for samarbeid mellom flere agenter.
* Oppsummerer resultatet: Til slutt oppsummerer planleggeren den genererte planen for klarhet.
Følgende Python-kodeeksempel illustrerer disse trinnene:

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

# Reise Underoppgave Modell

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # vi ønsker å tildele oppgaven til agenten

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Opprett klienten

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Definer brukermeldingen

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

# Skriv ut responsinnholdet etter å ha lastet det som JSON

pprint(json.loads(response_content))
```
  
Det som følger er output fra den forrige koden, og du kan så bruke denne strukturerte outputen til å rute til `assigned_agent` og oppsummere reiseplanen for sluttbrukeren.

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
  
Et eksempel-notatbok med forrige kodeeksempel er tilgjengelig [her](07-python-agent-framework.ipynb).

### Iterativ planlegging

Noen oppgaver krever en frem og tilbake-prosess eller ny planlegging, der resultatet av én deloppgave påvirker den neste. For eksempel, hvis agenten oppdager et uventet dataformat under flybestilling, kan det være nødvendig å tilpasse strategien før man går videre til hotellbestillinger.

I tillegg kan brukerfeedback (f.eks. at et menneske bestemmer seg for at de foretrekker en tidligere flyvning) utløse en delvis ny planlegging. Denne dynamiske, iterative tilnærmingen sikrer at sluttløsningen samsvarer med virkelige begrensninger og endrende brukerpreferanser.

f.eks. eksempel kode

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. det samme som forrige kode og videreformidle brukerhistorikken, nåværende plan

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
# .. omplanlegg og send oppgavene til respektive agenter
```
  
For mer omfattende planlegging, ta en titt på Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogginnlegg</a> for å løse komplekse oppgaver.

## Oppsummering

I denne artikkelen har vi sett på et eksempel på hvordan vi kan lage en planlegger som dynamisk kan velge de tilgjengelige agentene som er definert. Outputen fra planleggeren bryter ned oppgavene og tildeler agentene slik at de kan utføres. Det forutsettes at agentene har tilgang til funksjonene/verktøyene som kreves for å utføre oppgaven. I tillegg til agentene kan du inkludere andre mønstre som refleksjon, oppsummering og rundetalls-samtale for ytterligere tilpasning.

## Flere ressurser

Magentic One - Et generalist multi-agent system for å løse komplekse oppgaver og har oppnådd imponerende resultater på flere utfordrende agentiske referanser. Referanse: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. I denne implementeringen lager orkestratoren oppgavespesifikke planer og delegerer disse oppgavene til de tilgjengelige agentene. I tillegg til planlegging benytter orkestratoren også en sporingsmekanisme for å overvåke fremdriften i oppgaven og foretar ny planlegging ved behov.

### Har du flere spørsmål om planleggingsdesignmønsteret?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre lærende, delta på kontortimer og få svar på dine spørsmål om AI-agenter.

## Forrige leksjon

[Bygge pålitelige AI-agenter](../06-building-trustworthy-agents/README.md)

## Neste leksjon

[Multi-agent designmønster](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->