[![Planning Design Pattern](../../../translated_images/sk/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

# Návrh plánu

## Úvod

Táto lekcia pokryje

* Definovanie jasného celkového cieľa a rozdelenie zložitej úlohy na zvládnuteľné úlohy.
* Využitie štruktúrovaného výstupu pre spoľahlivejšie a strojovo čitateľné odpovede.
* Použitie prístupu riadeného udalosťami na zvládanie dynamických úloh a neočakávaných vstupov.

## Výukové ciele

Po dokončení tejto lekcie budete mať pochopenie o:

* Identifikovaní a nastavení celkového cieľa pre AI agenta, zabezpečiť, že presne vie, čo treba dosiahnuť.
* Rozklade zložitej úlohy na zvládnuteľné podúlohy a ich usporiadaní do logickej postupnosti.
* Vybavenie agentov správnymi nástrojmi (napr. nástroje na vyhľadávanie alebo nástroje pre analýzu dát), rozhodovanie kedy a ako ich použiť a zvládanie neočakávaných situácií.
* Hodnotení výsledkov podúloh, meraní výkonu a opakovaní akcií na zlepšenie konečného výsledku.

## Definovanie celkového cieľa a rozklad úlohy

![Definovanie cieľov a úloh](../../../translated_images/sk/defining-goals-tasks.d70439e19e37c47a.webp)

Väčšina reálnych úloh je príliš zložitá na to, aby sa riešila v jednom kroku. AI agent potrebuje stručný cieľ, ktorý ho bude viesť pri plánovaní a činnostiach. Napríklad zvážte cieľ:

    "Vygenerovať trojdňový cestovný itinerár."

Aj keď je to jednoduché na vyjadrenie, stále to vyžaduje upresnenie. Čím jasnejší je cieľ, tým lepšie sa agent (a akýkoľvek ľudský spolupracovník) môže zamerať na dosiahnutie správneho výsledku, ako je vytvorenie komplexného itinerára s možnosťami letov, odporúčaniami hotelov a návrhmi aktivít.

### Rozklad úlohy

Veľké alebo zložité úlohy sa stanú zvládnuteľnejšími, keď sa rozdelia na menšie, cieľovo orientované podúlohy.
Pre príklad cestovného itinerára by ste mohli rozložiť cieľ na:

* Rezervácia letu
* Rezervácia hotela
* Prenájom auta
* Personalizácia

Každú podúlohu potom môže riešiť vyhradený agent alebo proces. Jeden agent môže špecializovať na vyhľadávanie najlepších letových ponúk, iný sa zameria na rezervácie hotelov a tak ďalej. Koordinačný alebo „downstream“ agent potom môže tieto výsledky spojiť do jedného koherentného itinerára pre koncového používateľa.

Tento modulárny prístup tiež umožňuje postupné vylepšenia. Napríklad môžete pridať špecializovaných agentov pre odporúčania jedla alebo miestne aktivity a itinerár postupne dolaďovať.

### Štruktúrovaný výstup

Veľké jazykové modely (LLM) môžu generovať štruktúrovaný výstup (napr. JSON), ktorý je ľahšie spracovateľný pre downstream agentov alebo služby. To je obzvlášť užitočné v kontexte viacagentového systému, kde môžeme vykonať tieto úlohy po prijatí plánovacieho výstupu.

Nasledujúci ukážkový Python kód demonštruje jednoduchého plánovacieho agenta, ktorý rozkladá cieľ na podúlohy a generuje štruktúrovaný plán:

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

# Model pomocnej úlohy pre cestovanie
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # chceme priradiť úlohu agentovi

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Definujte správu používateľa
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

### Plánovací agent s multi-agentnou orchestráciou

V tomto príklade Semantic Router Agent prijíma požiadavku používateľa (napr. „Potrebujem plán hotelov na moju cestu.“).

Plánovač potom:

* Prijme plán hotela: Plánovač vezme správu používateľa a na základe systémového promptu (vrátane dostupných detailov o agentoch) vygeneruje štruktúrovaný cestovný plán.
* Zoznam agentov a ich nástrojov: Register agentov obsahuje zoznam agentov (napr. pre lety, hotely, prenájom áut a aktivity) spolu s funkciami alebo nástrojmi, ktoré ponúkajú.
* Presmeruje plán k príslušným agentom: V závislosti od počtu podúloh plánovač buď odošle správu priamo vyhradenému agentovi (v scenári s jednou úlohou), alebo koordinuje cez manažéra skupinového chatu pre viacagentovú spoluprácu.
* Zhrnie výsledok: Nakoniec plánovač zhrnie vygenerovaný plán pre prehľadnosť.
Nasledujúci príklad kódu v Pythone ilustruje tieto kroky:

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

# Model podúlohy cesty

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # chceme priradiť úlohu agentovi

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Vytvorte klienta

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Definujte správu používateľa

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

# Vytlačte obsah odpovede po načítaní ako JSON

pprint(json.loads(response_content))
```

Nižšie je výstup z predchádzajúceho kódu a potom môžete použiť tento štruktúrovaný výstup na nasmerovanie na `assigned_agent` a zhrnutie cestovného plánu pre koncového používateľa.

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

Príklad notebooku s predchádzajúcim príkladom kódu je dostupný [tu](07-python-agent-framework.ipynb).

### Iteratívne plánovanie

Niektoré úlohy vyžadujú opakované plánovanie alebo spätnú väzbu, kde výsledok jednej podúlohy ovplyvňuje ďalšiu. Napríklad, ak agent zistí neočakávaný formát dát pri rezervácii leteniek, môže potrebovať prispôsobiť svoju stratégiu pred začatím rezervácie hotela.

Okrem toho spätná väzba používateľa (napr. človek sa rozhodne, že uprednostňuje skorší let) môže vyvolať čiastočné preplánovanie. Tento dynamický, iteratívny prístup zaisťuje, že konečné riešenie zodpovedá reálnym obmedzeniam a meniacim sa preferenciám používateľa.

napr. ukážkový kód

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. rovnaké ako predchádzajúci kód a preniesť históriu používateľa, aktuálny plán

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
# .. preplánovať a odoslať úlohy príslušným agentom
```

Pre rozsiahlejšie plánovanie si pozrite Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> pre riešenie komplexných úloh.

## Zhrnutie

V tomto článku sme sa pozreli na príklad, ako môžeme vytvoriť plánovač, ktorý dokáže dynamicky vyberať dostupných definovaných agentov. Výstup plánovača rozkladá úlohy a priraďuje agentov, aby mohli byť vykonané. Predpokladá sa, že agenti majú prístup k funkciám/nástrojom potrebným na vykonanie úlohy. Okrem agentov môžete zahrnúť aj ďalšie vzory ako reflexiu, sumarizátor a round robin chat pre ďalšiu prispôsobenosť.

## Ďalšie zdroje

Magentic One - Všeobecný multi-agentný systém pre riešenie komplexných úloh, ktorý dosiahol pôsobivé výsledky v viacerých náročných agentných benchmarkoch. Referencia: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. V tejto implementácii orchestrátor tvorí úlohové špecifické plány a deleguje tieto úlohy dostupným agentom. Okrem plánovania orchestrátor tiež používa mechanizmus sledovania na monitorovanie pokroku úlohy a v prípade potreby preplánuje.

### Máte ďalšie otázky o vzore plánovania?

Pridajte sa do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) a stretávajte sa s inými študentmi, zúčastňujte sa konzultačných hodín a získavajte odpovede na otázky o AI agentoch.

## Predchádzajúca lekcia

[Budovanie dôveryhodných AI agentov](../06-building-trustworthy-agents/README.md)

## Nasledujúca lekcia

[Multi-agentný návrhový vzor](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladačskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, berte, prosím, na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->