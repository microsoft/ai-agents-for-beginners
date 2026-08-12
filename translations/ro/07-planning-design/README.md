[![Planning Design Pattern](../../../translated_images/ro/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

# Planificarea Design-ului

## Introducere

Această lecție va acoperi

* Definirea unui scop clar general și împărțirea unei sarcini complexe în sarcini gestionabile.
* Valorificarea unui output structurat pentru răspunsuri mai fiabile și ușor de citit de mașină.
* Aplicarea unei abordări bazate pe evenimente pentru a gestiona sarcini dinamice și intrări neașteptate.

## Obiective de Învățare

După finalizarea acestei lecții, veți înțelege:

* Identificarea și stabilirea unui scop general pentru un agent AI, asigurându-se că acesta știe clar ce trebuie realizat.
* Descompunerea unei sarcini complexe în subtasks gestionabile și organizarea lor într-o secvență logică.
* Echiparea agenților cu uneltele potrivite (de exemplu, instrumente de căutare sau de analiză a datelor), decizia când și cum sunt folosite și gestionarea situațiilor neașteptate care apar.
* Evaluarea rezultatelor subtask-urilor, măsurarea performanței și iterarea acțiunilor pentru a îmbunătăți rezultatul final.

## Definirea Scopului General și Descompunerea unei Sarcini

![Definirea Scopurilor și Sarcinilor](../../../translated_images/ro/defining-goals-tasks.d70439e19e37c47a.webp)

Majoritatea sarcinilor din lumea reală sunt prea complexe pentru a fi abordate într-un singur pas. Un agent AI are nevoie de un obiectiv concis pentru a-și ghida planificarea și acțiunile. De exemplu, luați în considerare scopul:

    "Generează un itinerariu de călătorie pentru 3 zile."

Deși este simplu de enunțat, acesta necesită rafinare. Cu cât scopul este mai clar, cu atât agentul (și orice colaboratori umani) pot să se concentreze mai bine pe realizarea rezultatului corect, cum ar fi crearea unui itinerar complet cu opțiuni de zboruri, recomandări de hoteluri și sugestii de activități.

### Descompunerea Sarcinilor

Sarcinile mari sau complicate devin mai gestionabile când sunt împărțite în subtasks orientate spre scop.
Pentru exemplul itinerarului de călătorie, scopul poate fi descompus în:

* Rezervarea zborurilor
* Rezervarea hotelului
* Închirierea mașinii
* Personalizarea

Fiecare subtask poate fi apoi abordat de agenți dedicați sau procese. Un agent poate fi specializat în căutarea celor mai bune oferte de zbor, altul se poate concentra pe rezervarea hotelurilor și așa mai departe. Un agent coordonator sau „downstream” poate apoi să compileze aceste rezultate într-un itinerar coerent pentru utilizatorul final.

Această abordare modulară permite, de asemenea, îmbunătățiri incremental. De exemplu, s-ar putea adăuga agenți specializați pentru Recomandări culinare sau Sugestii pentru activități locale și să se rafineze itinerarul în timp.

### Output Structurat

Modelele mari de limbaj (LLM-uri) pot genera output structurat (de exemplu JSON) care este mai ușor de interpretat și procesat de către agenții sau serviciile downstream. Acest lucru este deosebit de util într-un context multi-agent, unde aceste sarcini pot fi acționate după ce output-ul de planificare este primit.

Fragmentul Python următor demonstrează un agent de planificare simplu care descompune un scop în subtasks și generează un plan structurat:

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

# Model de SubSarcină pentru Călătorie
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # dorim să atribuim sarcina agentului

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Definește mesajul utilizatorului
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

### Agent de Planificare cu Orchestrare Multi-Agent

În acest exemplu, un Agent Semantic Router primește o cerere a utilizatorului (de exemplu, „Am nevoie de un plan de hotel pentru călătoria mea.”).

Planificatorul apoi:

* Primește planul de hotel: Planificatorul preia mesajul utilizatorului și, pe baza unui prompt de sistem (inclusiv detalii despre agenții disponibili), generează un plan de călătorie structurat.
* Listează Agenții și Uneltele lor: Registrul de agenți ține o listă cu agenți (de ex. pentru zbor, hotel, închiriere mașină și activități) împreună cu funcțiile sau uneltele pe care le oferă.
* Direcționează Planul către Agenții respectivi: În funcție de numărul de subtasks, planificatorul trimite mesajul fie direct unui agent dedicat (pentru scenarii cu o singură sarcină), fie coordonează printr-un manager de chat de grup pentru colaborare multi-agent.
* Rezumă Rezultatul: În final, planificatorul rezumă planul generat pentru claritate.
Următorul exemplu de cod Python ilustrează acești pași:

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

# Modelul SubSarcină de Călătorie

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # vrem să atribuim sarcina agentului

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Creează clientul

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

from pprint import pprint

# Definește mesajul utilizatorului

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

# Afișează conținutul răspunsului după încărcarea acestuia ca JSON

pprint(json.loads(response_content))
```

Ce urmează este output-ul din codul anterior și puteți apoi utiliza acest output structurat pentru a direcționa către `assigned_agent` și a rezuma planul de călătorie pentru utilizatorul final.

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

Un notebook exemplu cu codul anterior este disponibil [aici](./code_samples/07-python-agent-framework.ipynb).

### Planificare Iterativă

Unele sarcini necesită un schimb de informații sau o re-planificare, unde rezultatul unui subtask influențează următorul. De exemplu, dacă agentul descoperă un format neașteptat al datelor în timpul rezervării zborurilor, ar putea fi necesar să-și adapteze strategia înainte de a trece la rezervarea hotelului.

În plus, feedback-ul utilizatorului (de exemplu, o persoană care decide că preferă un zbor mai devreme) poate declanșa o replanificare parțială. Această abordare dinamică, iterativă asigură că soluția finală se aliniază cu constrângerile din lumea reală și cu preferințele utilizatorului în evoluție.

ex. cod exemplu

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. la fel ca în codul anterior și transmite istoricul utilizatorului, planul actual

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
# .. replanifică și trimite sarcinile agenților respectivi
```

Pentru o planificare mai cuprinzătoare consultați Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> pentru rezolvarea sarcinilor complexe.

## Rezumat

În acest articol am analizat un exemplu despre cum putem crea un planificator care poate selecta dinamic agenții disponibili definiți. Output-ul planificatorului descompune sarcinile și atribuie agenții pentru ca acestea să poată fi executate. Se presupune că agenții au acces la funcțiile/uneltele necesare pentru a îndeplini sarcina. În plus față de agenți, puteți include și alte pattern-uri precum reflection, summarizer și round robin chat pentru personalizare suplimentară.

## Resurse Suplimentare

Magnetic One - Un sistem multi-agent generalist pentru rezolvarea sarcinilor complexe și care a obținut rezultate impresionante pe multiple benchmark-uri agentice provocatoare. Referință: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. În această implementare, orchestratorul creează planuri specifice sarcinilor și delegă aceste sarcini agenților disponibili. În plus față de planificare, orchestratorul utilizează și un mecanism de urmărire pentru a monitoriza progresul sarcinii și replanifică dacă este necesar.

### Aveți Mai Multe Întrebări despre Designul Planificării?

Alăturați-vă [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la orele de consultanță și pentru a obține răspunsuri la întrebările voastre despre AI Agenți.

## Lecția Anterioară

[Construirea Agenților AI de Încredere](../06-building-trustworthy-agents/README.md)

## Lecția Următoare

[Design Pattern Multi-Agent](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->