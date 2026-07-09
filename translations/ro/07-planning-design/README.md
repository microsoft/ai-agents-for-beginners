[![Planning Design Pattern](../../../translated_images/ro/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

# Proiectarea planificării

## Introducere

Această lecție va acoperi

* Definirea unui scop general clar și descompunerea unei sarcini complexe în sarcini gestionabile.
* Valorificarea unei ieșiri structurate pentru răspunsuri mai fiabile și lizibile de către mașini.
* Aplicarea unei abordări bazate pe evenimente pentru a gestiona sarcini dinamice și intrări neașteptate.

## Obiective de învățare

După finalizarea acestei lecții, veți avea o înțelegere despre:

* Identificarea și stabilirea unui scop general pentru un agent AI, asigurându-vă că acesta știe clar ce trebuie să realizeze.
* Descompunerea unei sarcini complexe în sub-sarcini gestionabile și organizarea lor într-o secvență logică.
* Echiparea agenților cu instrumentele potrivite (de exemplu, instrumente de căutare sau instrumente de analiză de date), decizia când și cum sunt folosite și gestionarea situațiilor neașteptate care apar.
* Evaluarea rezultatelor sub-sarcinilor, măsurarea performanței și iterarea asupra acțiunilor pentru a îmbunătăți rezultatul final.

## Definirea scopului general și descompunerea unei sarcini

![Definirea obiectivelor și sarcinilor](../../../translated_images/ro/defining-goals-tasks.d70439e19e37c47a.webp)

Majoritatea sarcinilor din viața reală sunt prea complexe pentru a fi rezolvate într-un singur pas. Un agent AI are nevoie de un obiectiv concis pentru a-i ghida planificarea și acțiunile. De exemplu, luați în considerare obiectivul:

    "Generează un itinerar de călătorie de 3 zile."

Deși este simplu de enunțat, acesta necesită totuși rafinare. Cu cât obiectivul este mai clar, cu atât agentul (și orice colaboratori umani) se pot concentra mai bine pe realizarea rezultatului dorit, precum crearea unui itinerar cuprinzător cu opțiuni de zbor, recomandări de hoteluri și sugestii de activități.

### Descompunerea sarcinii

Sarcinile mari sau complicate devin mai ușor de gestionat atunci când sunt împărțite în sub-sarcini mai mici, orientate spre obiective.
Pentru exemplul itinerarului de călătorie, puteți descompune obiectivul în:

* Rezervare zbor
* Rezervare hotel
* Închiriere mașină
* Personalizare

Fiecare sub-sarcină poate fi apoi prelucrată de agenți sau procese dedicate. Un agent se poate specializa în căutarea celor mai bune oferte de zboruri, altul se poate concentra pe rezervările de hoteluri și așa mai departe. Un agent coordonator sau „downstream” poate apoi compila aceste rezultate într-un itinerar coerent pentru utilizatorul final.

Această abordare modulară permite și îmbunătățiri incrementale. De exemplu, puteți adăuga agenți specializați pentru recomandări culinare sau sugestii pentru activități locale și rafina itinerarul în timp.

### Ieșire structurată

Modelele de limbaj mari (LLM) pot genera o ieșire structurată (de exemplu JSON) care este mai ușor de analizat și procesat de agenții sau servicii downstream. Acest lucru este deosebit de util într-un context multi-agent, unde putem acționa aceste sarcini după ce este primită ieșirea planificării.

Fragmentul de cod Python următor demonstrează un agent simplu de planificare care descompune un obiectiv în sub-sarcini și generează un plan structurat:

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

# Model subtask călătorie
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

### Agent de planificare cu orchestrare multi-agent

În acest exemplu, un Agent Semantic Router primește o cerere de la utilizator (de ex., "Am nevoie de un plan de hotel pentru călătoria mea.").

Planificatorul apoi:

* Primește Planul Hotelului: Planificatorul preia mesajul utilizatorului și, pe baza unui prompt de sistem (inclusiv detalii despre agenții disponibili), generează un plan de călătorie structurat.
* Listează Agenții și Instrumentele lor: Registrul de agenți deține o listă de agenți (de ex., pentru zbor, hotel, închiriere mașină și activități) împreună cu funcțiile sau instrumentele pe care le oferă.
* Direcționează Planul către Agenții Respectivi: În funcție de numărul sub-sarcinilor, planificatorul trimite mesajul direct unui agent dedicat (pentru scenarii cu o singură sarcină) sau coordonează printr-un manager grup chat pentru colaborare multi-agent.
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

# Modelul Subtask de Călătorie

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # dorim să atribuim sarcina agentului

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

# Afișează conținutul răspunsului după ce a fost încărcat ca JSON

pprint(json.loads(response_content))
```

Ce urmează este ieșirea codului anterior și apoi puteți folosi această ieșire structurată pentru a direcționa către `assigned_agent` și a rezuma planul de călătorie pentru utilizatorul final.

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

### Planificare iterativă

Unele sarcini necesită un proces de back-and-forth sau replanificare, unde rezultatul unei sub-sarcini influențează următoarea. De exemplu, dacă agentul descoperă un format de date neașteptat în timpul rezervării zborurilor, ar putea fi necesar să își adapteze strategia înainte de a trece la rezervările de hoteluri.

În plus, feedback-ul utilizatorului (de ex. un om decidând că preferă un zbor mai devreme) poate declanșa o replanificare parțială. Această abordare dinamică, iterativă asigură că soluția finală este aliniată cu constrângerile din lumea reală și preferințele utilizatorului în evoluție.

de ex. cod exemplu

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. la fel ca și codul anterior și transmite istoricul utilizatorului, planul curent

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

Pentru o planificare mai cuprinzătoare verificați Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> pentru rezolvarea sarcinilor complexe.

## Rezumat

În acest articol am analizat un exemplu despre cum putem crea un planificator care poate selecta dinamic agenții disponibili definiți. Ieșirea planificatorului descompune sarcinile și atribuie agenții astfel încât acestea să poată fi executate. Se presupune că agenții au acces la funcțiile/instrumentele necesare pentru a îndeplini sarcina. În plus față de agenți, puteți include alte modele cum ar fi reflecția, sumarizatorul și chat-ul round robin pentru personalizare suplimentară.

## Resurse suplimentare

Magnetic One - Un sistem multi-agent generalist pentru rezolvarea sarcinilor complexe și care a atins rezultate impresionante la multiple benchmark-uri provocatoare pentru agenți. Referință: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. În această implementare, orchestratorul creează planuri specifice sarcinilor și delegă aceste sarcini agenților disponibili. Pe lângă planificare, orchestratorul folosește și un mecanism de urmărire pentru a monitoriza progresul sarcinii și replanifică după cum este necesar.

### Aveți mai multe întrebări despre patternul de design Planificare?

Alăturați-vă [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pentru a întâlni alți cursanți, a participa la ore de consultanță și a obține răspunsuri la întrebările voastre despre agenții AI.

## Lecția precedentă

[Construirea agenților AI de încredere](../06-building-trustworthy-agents/README.md)

## Lecția următoare

[Pattern-ul multi-agent](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->