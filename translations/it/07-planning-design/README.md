[![Planning Design Pattern](../../../translated_images/it/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Clicca sull'immagine sopra per vedere il video di questa lezione)_

# Progettazione della Pianificazione

## Introduzione

Questa lezione tratterà

* Definire un obiettivo chiaro e suddividere un compito complesso in compiti gestibili.
* Sfruttare output strutturati per risposte più affidabili e leggibili da macchina.
* Applicare un approccio guidato dagli eventi per gestire compiti dinamici e input imprevisti.

## Obiettivi di Apprendimento

Dopo aver completato questa lezione, avrai una comprensione di:

* Identificare e impostare un obiettivo complessivo per un agente AI, assicurandoti che sappia chiaramente cosa deve essere raggiunto.
* Decomporre un compito complesso in sotto-compiti gestibili e organizzarli in una sequenza logica.
* Dotare gli agenti degli strumenti giusti (ad esempio, strumenti di ricerca o di analisi dati), decidere quando e come utilizzarli e gestire situazioni inaspettate che si presentano.
* Valutare i risultati dei sotto-compiti, misurare le prestazioni e iterare sulle azioni per migliorare il risultato finale.

## Definire l'Obiettivo Complessivo e Suddividere un Compito

![Definire Obiettivi e Compiti](../../../translated_images/it/defining-goals-tasks.d70439e19e37c47a.webp)

La maggior parte dei compiti del mondo reale è troppo complessa per essere affrontata in un solo passaggio. Un agente AI necessita di un obiettivo conciso per guidare la sua pianificazione e le sue azioni. Ad esempio, considera l'obiettivo:

    "Genera un itinerario di viaggio di 3 giorni."

Anche se è semplice da enunciare, necessita comunque di una rifinitura. Più l'obiettivo è chiaro, meglio l’agente (e qualsiasi collaboratore umano) può concentrarsi sul raggiungimento del risultato giusto, come creare un itinerario completo con opzioni di volo, raccomandazioni per hotel e suggerimenti per attività.

### Decomposizione del Compito

Compiti grandi o complessi diventano più gestibili se suddivisi in sotto-compiti più piccoli e orientati all'obiettivo.
Per l'esempio dell'itinerario di viaggio, si potrebbe decomporre l'obiettivo in:

* Prenotazione voli
* Prenotazione hotel
* Noleggio auto
* Personalizzazione

Ogni sotto-compito può poi essere affrontato da agenti o processi dedicati. Un agente potrebbe specializzarsi nella ricerca delle migliori offerte di volo, un altro concentrarsi sulle prenotazioni di hotel e così via. Un agente coordinatore o “downstream” può quindi compilare questi risultati in un unico itinerario coerente per l’utente finale.

Questo approccio modulare consente anche miglioramenti incrementali. Ad esempio, si potrebbero aggiungere agenti specializzati per Raccomandazioni di Cibo o Suggerimenti per Attività Locali e perfezionare l’itinerario nel tempo.

### Output strutturato

I modelli linguistici di grandi dimensioni (LLM) possono generare output strutturati (ad esempio JSON) che sono più facili da analizzare e processare per agenti o servizi downstream. Questo è particolarmente utile in un contesto multi-agente, dove possiamo eseguire questi compiti dopo che è stato ricevuto l’output della pianificazione.

Il seguente snippet Python dimostra un semplice agente pianificatore che scompone un obiettivo in sotto-compiti e genera un piano strutturato:

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

# Modello di Sottocompito di Viaggio
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # vogliamo assegnare il compito all'agente

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

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

In questo esempio, un Semantic Router Agent riceve una richiesta utente (ad esempio, "Ho bisogno di un piano hotel per il mio viaggio.").

Il pianificatore quindi:

* Riceve il Piano Hotel: Il pianificatore prende il messaggio dell'utente e, basandosi su un prompt di sistema (inclusi i dettagli degli agenti disponibili), genera un piano di viaggio strutturato.
* Elenca Agenti e Loro Strumenti: Il registro degli agenti contiene una lista di agenti (ad esempio per volo, hotel, noleggio auto e attività) insieme alle funzioni o strumenti che offrono.
* Smista il Piano agli Agenti Rispettivi: A seconda del numero di sotto-compiti, il pianificatore invia il messaggio direttamente a un agente dedicato (per scenari a singolo compito) o coordina tramite un gestore di chat di gruppo per la collaborazione multi-agente.
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

# Modello di Sottoattività di Viaggio

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

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Crea il client

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

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

Segue l’output del codice precedente e puoi quindi usare questo output strutturato per indirizzare l’`assigned_agent` e riassumere il piano di viaggio all’utente finale.

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

Un notebook di esempio con il codice precedente è disponibile [qui](07-python-agent-framework.ipynb).

### Pianificazione Iterativa

Alcuni compiti richiedono un’andata e ritorno o una ripianificazione, dove l’esito di un sotto-compito influenza il successivo. Ad esempio, se l’agente scopre un formato dati inatteso durante la prenotazione dei voli, potrebbe dover adattare la sua strategia prima di passare alle prenotazioni degli hotel.

Inoltre, il feedback dell’utente (ad esempio, un umano che preferisce un volo più presto) può innescare una ripianificazione parziale. Questo approccio dinamico e iterativo garantisce che la soluzione finale sia allineata con i vincoli del mondo reale e le preferenze in evoluzione dell’utente.

esempio di codice

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. stesso codice precedente e passa la cronologia dell'utente, piano corrente

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

Per una pianificazione più completa, consulta il blog post di Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> per la risoluzione di compiti complessi.

## Riepilogo

In questo articolo abbiamo visto un esempio di come possiamo creare un pianificatore che può selezionare dinamicamente gli agenti disponibili definiti. L’output del Pianificatore scompone i compiti e assegna gli agenti affinché possano essere eseguiti. Si presuppone che gli agenti abbiano accesso alle funzioni/strumenti necessari per svolgere il compito. Oltre agli agenti, è possibile includere altri pattern come riflessione, sintetizzatore e chat a round robin per personalizzare ulteriormente.

## Risorse Aggiuntive

Magentic One - Un sistema multi-agente generalista per risolvere compiti complessi che ha ottenuto risultati impressionanti in molteplici benchmark agentici sfidanti. Riferimento: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. In questa implementazione l’orchestratore crea piani specifici per i compiti e delega questi compiti agli agenti disponibili. Oltre alla pianificazione, l’orchestratore impiega anche un meccanismo di monitoraggio per seguire il progresso del compito e ripianificare se necessario.

### Hai altre domande sul Modello di Progettazione per la Pianificazione?

Unisciti al [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) per incontrare altri studenti, partecipare alle ore d’ufficio e avere risposte alle tue domande sugli AI Agents.

## Lezione Precedente

[Creare Agenti AI Affidabili](../06-building-trustworthy-agents/README.md)

## Lezione Successiva

[Modello di Progettazione Multi-Agente](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur facendo del nostro meglio per garantire l’accuratezza, si prega di tenere presente che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale effettuata da un traduttore umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->