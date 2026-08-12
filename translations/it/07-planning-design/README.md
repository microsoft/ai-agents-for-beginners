[![Planning Design Pattern](../../../translated_images/it/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Clicca sull’immagine sopra per vedere il video di questa lezione)_

# Pianificazione del Design

## Introduzione

Questa lezione tratterà

* Definire un obiettivo chiaro e generale e suddividere un compito complesso in attività gestibili.
* Sfruttare un output strutturato per risposte più affidabili e leggibili da macchine.
* Applicare un approccio guidato dagli eventi per gestire compiti dinamici e input imprevisti.

## Obiettivi di Apprendimento

Dopo aver completato questa lezione, avrai compreso:

* Come identificare e stabilire un obiettivo complessivo per un agente AI, assicurandoti che sappia chiaramente cosa deve essere raggiunto.
* Come decomporre un compito complesso in sottocompiti gestibili e organizzarli in una sequenza logica.
* Come dotare gli agenti degli strumenti giusti (es. strumenti di ricerca o di analisi dati), decidere quando e come usarli e gestire situazioni impreviste che si presentano.
* Come valutare i risultati dei sottocompiti, misurare le prestazioni e iterare le azioni per migliorare il risultato finale.

## Definire l’Obiettivo Generale e Suddividere un Compito

![Definizione Obiettivi e Compiti](../../../translated_images/it/defining-goals-tasks.d70439e19e37c47a.webp)

La maggior parte dei compiti nel mondo reale sono troppo complessi per essere affrontati in un singolo passaggio. Un agente AI necessita di un obiettivo conciso per guidare la sua pianificazione e le sue azioni. Ad esempio, considera l’obiettivo:

    "Generare un itinerario di viaggio di 3 giorni."

Sebbene sia semplice da enunciare, necessita comunque di un affinamento. Più è chiaro l’obiettivo, meglio l’agente (e qualsiasi collaboratore umano) potrà concentrarsi per raggiungere il risultato giusto, come creare un itinerario completo con opzioni di volo, raccomandazioni per hotel e suggerimenti di attività.

### Decomposizione del Compito

Compiti grandi o complessi diventano più gestibili se suddivisi in sottocompiti più piccoli e orientati all’obiettivo.
Per l’esempio dell’itinerario di viaggio, potresti scomporre l’obiettivo in:

* Prenotazione Voli
* Prenotazione Hotel
* Noleggio Auto
* Personalizzazione

Ogni sottocompito può quindi essere affrontato da agenti o processi dedicati. Un agente potrebbe specializzarsi nella ricerca delle migliori offerte di volo, un altro concentrarsi sulle prenotazioni di hotel, e così via. Un agente coordinatore o “downstream” può quindi assemblare questi risultati in un unico itinerario coerente per l’utente finale.

Questo approccio modulare consente anche miglioramenti incrementali. Ad esempio, potresti aggiungere agenti specializzati per Raccomandazioni Alimentari o Suggerimenti di Attività Locali e affinare l’itinerario nel tempo.

### Output Strutturato

I Large Language Model (LLM) possono generare un output strutturato (es. JSON) che è più facile da analizzare e processare per agenti o servizi a valle. Questo è particolarmente utile in un contesto multi-agente, dove possiamo agire su questi compiti una volta ricevuto il risultato della pianificazione.

Il seguente frammento di codice Python dimostra un agente pianificatore semplice che scompone un obiettivo in sottocompiti e genera un piano strutturato:

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

# Modello di Sottoattività di Viaggio
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # vogliamo assegnare il compito all'agente

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Definisci il messaggio dell'utente
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

### Agente Pianificatore con Orchestrazione Multi-Agente

In questo esempio, un Agente Semantic Router riceve una richiesta dell’utente (es. "Ho bisogno di un piano hotel per il mio viaggio.").

Il pianificatore quindi:

* Riceve il Piano Hotel: Il pianificatore prende il messaggio dell’utente e, basandosi su un prompt di sistema (inclusi i dettagli degli agenti disponibili), genera un piano di viaggio strutturato.
* Elenca gli Agenti e i loro Strumenti: Il registro degli agenti contiene una lista di agenti (es. per volo, hotel, noleggio auto e attività) insieme alle funzioni o strumenti che offrono.
* Invia il Piano agli Agenti Rispetti: A seconda del numero di sottocompiti, il pianificatore o invia il messaggio direttamente a un agente dedicato (per scenari a compito singolo) o coordina tramite un gestore di chat di gruppo per collaborazione multi-agente.
* Riassume il Risultato: Infine, il pianificatore riassume il piano generato per chiarezza.
Il seguente esempio di codice Python illustra questi passaggi:

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

# Modello di SottoAttività di Viaggio

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # vogliamo assegnare il compito all'agente

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Crea il client

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

from pprint import pprint

# Definisci il messaggio dell'utente

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

# Stampa il contenuto della risposta dopo averlo caricato come JSON

pprint(json.loads(response_content))
```

Ciò che segue è l’output dal codice precedente e puoi quindi usare questo output strutturato per indirizzare a `assigned_agent` e riassumere il piano di viaggio per l’utente finale.

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

Un notebook di esempio con il codice precedente è disponibile [qui](./code_samples/07-python-agent-framework.ipynb).

### Pianificazione Iterativa

Alcuni compiti richiedono un avanti e indietro o una ripianificazione, dove il risultato di un sottocompito influenza il successivo. Ad esempio, se l’agente scopre un formato di dati imprevisto durante la prenotazione dei voli, potrebbe dover adattare la sua strategia prima di passare alla prenotazione degli hotel.

Inoltre, il feedback dell’utente (es. un umano che decide di preferire un volo precedente) può innescare una ripianificazione parziale. Questo approccio dinamico e iterativo garantisce che la soluzione finale sia allineata con le limitazioni del mondo reale e le preferenze utente in evoluzione.

es. codice di esempio

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. stesso del codice precedente e passa la storia dell'utente, piano corrente

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
# .. ripianifica e invia i compiti agli agenti rispettivi
```

Per una pianificazione più completa consulta il post sul blog Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> per risolvere compiti complessi.

## Riepilogo

In questo articolo abbiamo esaminato un esempio di come possiamo creare un pianificatore che può selezionare dinamicamente gli agenti disponibili definiti. L’output del pianificatore scompone i compiti e assegna gli agenti affinché possano essere eseguiti. Si presuppone che gli agenti abbiano accesso alle funzioni/strumenti necessari per svolgere il compito. Oltre agli agenti puoi includere altri pattern come reflection, summarizer e round robin chat per personalizzare ulteriormente.

## Risorse Aggiuntive

Magnetic One - Un sistema multi-agente generalista per risolvere compiti complessi che ha ottenuto risultati impressionanti su molteplici benchmark agentici sfidanti. Riferimento: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. In questa implementazione l’orchestratore crea piani specifici per i compiti e delega questi compiti agli agenti disponibili. Oltre alla pianificazione, l’orchestratore impiega anche un meccanismo di monitoraggio per seguire i progressi del compito e ripianificare se necessario.

### Hai altre domande sul Planning Design Pattern?

Unisciti al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) per incontrare altri studenti, partecipare alle office hours e ottenere risposte alle tue domande sugli AI Agents.

## Lezione Precedente

[Costruire Agenti AI Affidabili](../06-building-trustworthy-agents/README.md)

## Lezione Successiva

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->