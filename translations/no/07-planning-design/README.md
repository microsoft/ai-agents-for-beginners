[![Planning Design Pattern](../../../translated_images/no/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Klikk på bildet over for å se video av denne leksjonen)_

# Planning Design

## Introduksjon

Denne leksjonen vil dekke

* Å definere et klart overordnet mål og bryte ned en kompleks oppgave i håndterbare deloppgaver.
* Å utnytte strukturert output for mer pålitelige og maskinlesbare svar.
* Å anvende en hendelsesdrevet tilnærming for å håndtere dynamiske oppgaver og uventede input.

## Læringsmål

Etter å ha gjennomført denne leksjonen vil du ha forståelse for:

* Identifisere og sette et overordnet mål for en AI-agent, slik at den tydelig vet hva som skal oppnås.
* Dele opp en kompleks oppgave i håndterbare deloppgaver og organisere dem i en logisk rekkefølge.
* Utstyre agenter med riktige verktøy (f.eks. søkeverktøy eller dataanalyseverktøy), bestemme når og hvordan de brukes, og håndtere uventede situasjoner som oppstår.
* Evaluere resultatene av deloppgaver, måle ytelse og iterere på handlinger for å forbedre sluttresultatet.

## Definere det overordnede målet og bryte ned en oppgave

![Defining Goals and Tasks](../../../translated_images/no/defining-goals-tasks.d70439e19e37c47a.webp)

De fleste oppgaver i den virkelige verden er for komplekse til å løses i et enkelt steg. En AI-agent trenger et konsist mål for å styre planlegging og handlinger. For eksempel, vurder målet:

    "Generer en reiserute for 3 dager."

Selv om det er enkelt å uttrykke, krever det fortsatt presisering. Jo klarere målet er, desto bedre kan agenten (og eventuelle menneskelige samarbeidspartnere) fokusere på å oppnå riktig resultat, som å lage en omfattende reiserute med flyalternativer, hotellanbefalinger og aktivitetsforslag.

### Oppgavedeling

Store eller kompliserte oppgaver blir mer håndterbare når de deles opp i mindre, målrettede deloppgaver.
For eksemplet med reiseruten kan du dele opp målet i:

* Flybestilling
* Hotellbestilling
* Bilutleie
* Personalisering

Hver deloppgave kan deretter håndteres av dedikerte agenter eller prosesser. En agent kan spesialisere seg på å finne de beste flytilbudene, en annen fokuserer på hotellbestillinger, og så videre. En koordinerende eller «nedstrøms» agent kan deretter samle disse resultatene til én sammenhengende reiserute for sluttbrukeren.

Denne modulære tilnærmingen tillater også trinnvise forbedringer. For eksempel kan du legge til spesialiserte agenter for matanbefalinger eller lokale aktivitetsforslag og forbedre reiseruten over tid.

### Strukturert output

Store språkmodeller (LLMs) kan generere strukturert output (f.eks. JSON) som er enklere for nedstrøms agenter eller tjenester å tolke og behandle. Dette er spesielt nyttig i en multi-agent kontekst, der vi kan iverksette oppgaver etter at planleggingsoutput er mottatt.

Følgende Python-eksempel viser en enkel planleggingsagent som bryter ned et mål i deloppgaver og genererer en strukturert plan:

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

# Reise deloppgave modell
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # vi ønsker å tilordne oppgaven til agenten

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

I dette eksempelet mottar en Semantisk Rutingsagent en brukerforespørsel (f.eks. "Jeg trenger en hotellplan for reisen min.").

Planleggeren gjør deretter:

* Mottar Hotellplanen: Planleggeren tar brukerens melding og, basert på et systemprompt (inkludert tilgjengelige agentdetaljer), genererer en strukturert reiseplan.
* Lister opp agenter og deres verktøy: Agentregisteret inneholder en liste over agenter (f.eks. for fly, hotell, bilutleie og aktiviteter) sammen med funksjoner eller verktøy de tilbyr.
* Ruter planen til respektive agenter: Avhengig av antall deloppgaver sender planleggeren meldingen direkte til en dedikert agent (for enkel-oppgave scenarier) eller koordinerer via en gruppekontakt for multi-agent samarbeid.
* Oppsummerer resultatet: Til slutt oppsummerer planleggeren den genererte planen for klarhet.
Følgende Python-kode viser disse trinnene:

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

# Reise deloppgavemodell

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

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Opprett klienten

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

# Skriv ut svarets innhold etter å ha lastet det som JSON

pprint(json.loads(response_content))
```

Det som følger er output fra forrige kode, og du kan deretter bruke denne strukturerte outputen til å rute til `assigned_agent` og oppsummere reiseplanen for sluttbrukeren.

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

Et eksempel-notatbok med forrige kodeeksempel er tilgjengelig [her](./code_samples/07-python-agent-framework.ipynb).

### Iterativ planlegging

Noen oppgaver krever fram-og-tilbake eller omplanlegging, der utfallet av én deloppgave påvirker neste. For eksempel, hvis agenten oppdager et uventet dataformat under flybestilling, kan den måtte tilpasse strategien før den fortsetter med hotellbestillinger.

I tillegg kan brukerfeedback (f.eks. en person som bestemmer seg for at de foretrekker en tidligere flyvning) utløse en delvis omplanlegging. Denne dynamiske, iterative tilnærmingen sikrer at sluttløsningen samsvarer med virkelige begrensninger og utviklende brukerpreferanser.

f.eks. eksempel kode

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. samme som forrige kode og videresend brukerhistorikk, gjeldende plan

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
# .. planlegg på nytt og send oppgavene til respektive agenter
```

For mer omfattende planlegging kan du sjekke ut Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogginnlegg</a> for å løse komplekse oppgaver.

## Oppsummering

I denne artikkelen har vi sett på et eksempel på hvordan vi kan lage en planlegger som dynamisk kan velge tilgjengelige agenter definert. Outputen fra planleggeren deler oppgavene og tildeler agentene slik at de kan utføres. Det antas at agentene har tilgang til funksjonene/verktøyene som kreves for å utføre oppgaven. I tillegg til agentene kan du inkludere andre mønstre som refleksjon, oppsummerer, og rundtom-chat for ytterligere tilpasning.

## Ytterligere ressurser

Magnetic One - Et generalist multi-agent system for å løse komplekse oppgaver og har oppnådd imponerende resultater på flere krevende agentiske benchmarks. Referanse: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. I denne implementeringen skaper orkestratoren oppgave-spesifikke planer og delegerer disse oppgavene til tilgjengelige agenter. I tillegg til planlegging benytter orkestratoren også en sporingsmekanisme for å overvåke fremdriften i oppgaven og omplanlegge etter behov.

### Har du flere spørsmål om Planning Design Pattern?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre lærende, delta på kontortid og få svar på dine AI Agents-spørsmål.

## Forrige leksjon

[Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)

## Neste leksjon

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->