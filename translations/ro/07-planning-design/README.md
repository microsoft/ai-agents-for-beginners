[![Model de proiectare pentru planificare](../../../translated_images/ro/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

# Designul planificării

## Introducere

Această lecție va acoperi

* Definirea unui obiectiv general clar și împărțirea unei sarcini complexe în sarcini gestionabile.
* Valorificarea output-ului structurat pentru răspunsuri mai fiabile și ușor de procesat de către mașini.
* Aplicarea unei abordări orientate pe evenimente pentru a gestiona sarcini dinamice și intrări neașteptate.

## Obiectivele de învățare

După parcurgerea acestei lecții, veți înțelege:

* Identificarea și stabilirea unui obiectiv general pentru un agent AI, asigurându-vă că acesta știe clar ce trebuie realizat.
* Decomponerea unei sarcini complexe în sub-sarcini gestionabile și organizarea acestora într-o succesiune logică.
* Echiparea agenților cu instrumentele potrivite (de ex., instrumente de căutare sau instrumente de analiză a datelor), deciderea când și cum sunt folosite și gestionarea situațiilor neașteptate care apar.
* Evaluarea rezultatelor sub-sarcinilor, măsurarea performanței și iterarea acțiunilor pentru a îmbunătăți rezultatul final.

## Definirea obiectivului general și descompunerea unei sarcini

![Definirea obiectivelor și a sarcinilor](../../../translated_images/ro/defining-goals-tasks.d70439e19e37c47a.webp)

Majoritatea sarcinilor din lumea reală sunt prea complexe pentru a fi abordate într-un singur pas. Un agent AI are nevoie de un obiectiv concis pentru a ghida planificarea și acțiunile sale. De exemplu, luați în considerare obiectivul:

    "Generează un itinerariu de călătorie de 3 zile."

Deși este simplu de enunțat, acesta necesită în continuare rafinare. Cu cât obiectivul este mai clar, cu atât agentul (și eventualii colaboratori umani) se pot concentra mai bine pe realizarea rezultatului corect, cum ar fi crearea unui itinerar cuprinzător cu opțiuni de zbor, recomandări de hotel și sugestii de activități.

### Decompozarea sarcinii

Sarcinile mari sau complexe devin mai ușor de gestionat atunci când sunt împărțite în sub-sarcini mai mici orientate pe obiective.
Pentru exemplul itinerariului de călătorie, ați putea descompune obiectivul în:

* Rezervare zboruri
* Rezervare hotel
* Închiriere auto
* Personalizare

Fiecare sub-sarcină poate fi apoi abordată de agenți sau procese dedicate. Un agent s-ar putea specializa în căutarea celor mai bune oferte la zboruri, altul se concentrează pe rezervări de hotel și așa mai departe. Un agent coordonator sau „downstream” poate apoi să compileze aceste rezultate într-un itinerar coerent pentru utilizatorul final.

Această abordare modulară permite, de asemenea, îmbunătățiri incrementale. De exemplu, ați putea adăuga agenți specializați pentru Recomandări culinare sau Sugestii de activități locale și să rafinați itinerarul în timp.

### Output structurat

Large Language Models (LLMs) pot genera output structurat (de ex. JSON) care este mai ușor pentru agenții sau serviciile downstream de a parsa și procesa. Acest lucru este deosebit de util într-un context multi-agent, unde putem acționa asupra acestor sarcini după ce output-ul planificării este primit.

The following Python snippet demonstrates a simple planning agent decomposing a goal into subtasks and generating a structured plan:

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

# Model de sub-sarcină de călătorie
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # vrem să atribuim sarcina agentului

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

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

În acest exemplu, un Semantic Router Agent primește o cerere de la utilizator (de ex., "Am nevoie de un plan pentru hotel pentru călătoria mea.").

Planificatorul apoi:

* Primește planul pentru hotel: Planificatorul preia mesajul utilizatorului și, pe baza unui prompt de sistem (inclusiv detalii despre agenții disponibili), generează un plan de călătorie structurat.
* Listează agenții și instrumentele lor: Registrul de agenți conține o listă de agenți (de ex., pentru zboruri, hotel, închiriere auto și activități) împreună cu funcțiile sau instrumentele pe care le oferă.
* Direcționează planul către agenții respectivi: În funcție de numărul de sub-sarcini, planificatorul fie trimite mesajul direct unui agent dedicat (pentru scenarii cu o singură sarcină), fie coordonează printr-un manager de chat de grup pentru colaborare multi-agent.
* Resumează rezultatul: În final, planificatorul rezumă planul generat pentru claritate.
The following Python code sample illustrates these steps:

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

# Model pentru sub-sarcină de călătorie

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # dorim să atribuim această sarcină agentului

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Creează clientul

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

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

# Afișează conținutul răspunsului după ce îl încarci ca JSON

pprint(json.loads(response_content))
```

Ce urmează este rezultatul codului anterior și apoi puteți folosi acest rezultat structurat pentru a direcționa către `assigned_agent` și a rezuma planul de călătorie pentru utilizatorul final.

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

Un exemplu de notebook cu exemplul de cod anterior este disponibil [aici](07-python-agent-framework.ipynb).

### Planificare iterativă

Unele sarcini necesită un schimb de informații înainte sau o re-planificare, unde rezultatul unei sub-sarcini influențează pe cea următoare. De exemplu, dacă agentul descoperă un format de date neașteptat în timpul rezervării zborurilor, ar putea fi nevoie să își adapteze strategia înainte de a trece la rezervările de hotel.

În plus, feedback-ul utilizatorului (de ex., un om care decide că preferă un zbor mai devreme) poate declanșa o re-planificare parțială. Această abordare dinamică și iterativă asigură că soluția finală se aliniază cu constrângerile din lumea reală și cu preferințele utilizatorului care evoluează.

de ex., exemplu de cod

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. la fel ca în codul anterior și transmite istoricul utilizatorului, planul curent

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
# .. replanifică și trimite sarcinile agenților corespunzători
```

For more comprehensive planning do checkout Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">postare pe blog</a> for solving complex tasks.

## Rezumat

În acest articol am analizat un exemplu despre cum putem crea un planificator care poate selecta dinamic agenții disponibili definiți. Output-ul Planner-ului descompune sarcinile și atribuie agenții astfel încât acestea să poată fi executate. Se presupune că agenții au acces la funcțiile/instrumentele necesare pentru a efectua sarcina. Pe lângă agenți, puteți include și alte pattern-uri precum reflecție, sumarizator și chat rotativ pentru a personaliza în continuare.

## Resurse suplimentare

Magentic One - un sistem multi-agent generalist pentru rezolvarea sarcinilor complexe, care a obținut rezultate impresionante pe multiple benchmark-uri provocatoare pentru agenți. Referință: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. În această implementare, orchestratorul creează planuri specifice sarcinii și delegă aceste sarcini agenților disponibili. Pe lângă planificare, orchestratorul folosește și un mecanism de urmărire pentru a monitoriza progresul sarcinii și re-planifică după cum este necesar.

### Aveți mai multe întrebări despre modelul de proiectare pentru planificare?

Alăturați-vă [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pentru a întâlni alți cursanți, a participa la ore de consiliere și a primi răspunsuri la întrebările despre agenții AI.

## Lecția anterioară

[Construirea agenților AI de încredere](../06-building-trustworthy-agents/README.md)

## Următoarea lecție

[Modelul de proiectare multi-agent](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autorizată. Pentru informații critice, se recomandă o traducere profesională realizată de un traducător uman. Nu ne asumăm răspunderea pentru nicio neînțelegere sau interpretare greșită care rezultă din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->