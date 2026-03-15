[![Planleggingsdesign](../../../translated_images/no/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Klikk på bildet ovenfor for å se videoen av denne leksjonen)_

# Planleggingsdesign

## Introduksjon

Denne leksjonen vil dekke

* Definere et klart overordnet mål og bryte en kompleks oppgave ned i håndterbare oppgaver.
* Utnytte strukturert utdata for mer pålitelige og maskinlesbare svar.
* Anvende en hendelsesdrevet tilnærming for å håndtere dynamiske oppgaver og uventede inndata.

## Læringsmål

Etter å ha fullført denne leksjonen vil du ha forståelse for:

* Identifisere og sette et overordnet mål for en AI-agent, slik at den tydelig vet hva som må oppnås.
* Dele opp en kompleks oppgave i håndterbare deloppgaver og organisere dem i en logisk rekkefølge.
* Utstyre agenter med riktige verktøy (f.eks. søkeverktøy eller verktøy for dataanalyse), avgjøre når og hvordan de skal brukes, og håndtere uventede situasjoner som oppstår.
* Vurdere resultatene av deloppgaver, måle ytelse og iterere handlinger for å forbedre sluttresultatet.

## Definere det overordnede målet og bryte ned en oppgave

![Definere mål og oppgaver](../../../translated_images/no/defining-goals-tasks.d70439e19e37c47a.webp)

De fleste oppgaver i den virkelige verden er for komplekse til å løses i ett trinn. En AI-agent trenger et klart og konsist mål for å styre planleggingen og handlingene sine. For eksempel, vurder målet:

    "Generer en 3-dagers reiserute."

Selv om det er enkelt å formulere, trenger det fortsatt presisering. Jo klarere målet er, desto bedre kan agenten (og eventuelle menneskelige samarbeidspartnere) fokusere på å oppnå riktig resultat, som å lage en omfattende reiserute med flyalternativer, hotellanbefalinger og aktivitetsforslag.

### Oppgavedekomponering

Store eller komplekse oppgaver blir mer håndterbare når de deles opp i mindre, målrettede deloppgaver.
For reiserute-eksempelet kan du dele opp målet i:

* Flybestilling
* Hotellbestilling
* Bilutleie
* Personalisering

Hver deloppgave kan deretter håndteres av dedikerte agenter eller prosesser. En agent kan spesialisere seg på å finne de beste flytilbudene, en annen fokuserer på hotellbestillinger, og så videre. En koordinerende eller "nedstrøms" agent kan så samle disse resultatene til en helhetlig reiserute for sluttbrukeren.

Denne modulære tilnærmingen tillater også inkrementelle forbedringer. For eksempel kan du legge til spesialiserte agenter for matanbefalinger eller lokale aktivitetsforslag og forbedre reiseruten over tid.

### Strukturert utdata

Store språkmodeller (LLMs) kan generere strukturert utdata (f.eks. JSON) som er enklere for nedstrømsagenter eller -tjenester å parse og bearbeide. Dette er spesielt nyttig i en multi-agent-kontekst, hvor vi kan iverksette disse oppgavene etter at planleggingsutdataene er mottatt.

Følgende Python-utdrag demonstrerer en enkel planleggingsagent som deler et mål inn i deloppgaver og genererer en strukturert plan:

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

# Reise deloppgavemodell
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # vi ønsker å tildele oppgaven til agenten

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

### Planleggingsagent med fleragentorkestrering

I dette eksempelet mottar en Semantic Router Agent en brukerforespørsel (f.eks. "Jeg trenger en hotellplan for turen min.").

Planleggeren gjør deretter:

* Mottar hotellplanen: Planleggeren tar brukerens melding og, basert på et systemprompt (inkludert tilgjengelige agentdetaljer), genererer en strukturert reiseplan.
* Lister agenter og deres verktøy: Agentregisteret inneholder en liste over agenter (f.eks. for fly, hotell, bilutleie og aktiviteter) sammen med funksjonene eller verktøyene de tilbyr.
* Ruter planen til de respektive agentene: Avhengig av antall deloppgaver sender planleggeren enten meldingen direkte til en dedikert agent (for enkeltoppgave-scenarier) eller koordinerer via en gruppechattsjef for fler-agent-samarbeid.
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

# Modell for reise-underoppgave

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

# Skriv ut responsinnholdet etter å ha lastet det inn som JSON

pprint(json.loads(response_content))
```

Det som følger er utdataene fra forrige kode, og du kan deretter bruke disse strukturerte utdataene til å rute til `assigned_agent` og oppsummere reiseplanen for sluttbrukeren.

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

Et eksempel på en notatbok med kodeeksempelet ovenfor er tilgjengelig [her](07-python-agent-framework.ipynb).

### Iterativ planlegging

Noen oppgaver krever fram-og-tilbake eller replanlegging, hvor utfallet av én deloppgave påvirker den neste. For eksempel, hvis agenten oppdager et uventet dataformat under flybestilling, kan det være nødvendig å tilpasse strategien før den går videre til hotellbestillinger.

I tillegg kan brukerfeedback (f.eks. en person som bestemmer at de foretrekker et tidligere fly) utløse en delvis replanlegging. Denne dynamiske, iterative tilnærmingen sikrer at den endelige løsningen samsvarer med virkelige begrensninger og endrede brukerpreferanser.

f.eks. eksempelkode

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. det samme som forrige kode og gi videre brukerens historikk og nåværende plan

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
# .. omplanlegg og send oppgavene til de respektive agentene
```

For mer omfattende planlegging, sjekk ut Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogginnlegg</a> for å løse komplekse oppgaver.

## Sammendrag

I denne artikkelen har vi sett på et eksempel på hvordan vi kan lage en planlegger som dynamisk kan velge de tilgjengelige agenter som er definert. Planleggerens utdata bryter ned oppgavene og tildeler agentene slik at de kan utføres. Det forutsettes at agentene har tilgang til funksjonene/verktøyene som kreves for å utføre oppgaven. I tillegg til agentene kan du inkludere andre mønstre som refleksjon, oppsummering og round-robin-chat for å tilpasse ytterligere.

## Ytterligere ressurser

Magentic One - Et generalist fler-agent-system for å løse komplekse oppgaver som har oppnådd imponerende resultater på flere utfordrende agent-benchmarks. Referanse: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. I denne implementeringen oppretter orkestratoren oppgavespesifikke planer og delegerer disse oppgavene til tilgjengelige agenter. I tillegg til planlegging bruker orkestratoren også en sporingsmekanisme for å overvåke fremdriften i oppgaven og re-planlegge etter behov.

### Har du flere spørsmål om planleggingsdesignmønsteret?

Bli med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for å møte andre lærende, delta på kontortid og få spørsmål om AI-agenter besvart.

## Forrige leksjon

[Bygge pålitelige AI-agenter](../06-building-trustworthy-agents/README.md)

## Neste leksjon

[Designmønster for fleragenter](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Ansvarsfraskrivelse:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten Co-op Translator (https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Originaldokumentet på dets opprinnelige språk skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som måtte oppstå ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->