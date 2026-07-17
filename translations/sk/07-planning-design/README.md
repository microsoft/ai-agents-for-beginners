[![Vzory plánovania](../../../translated_images/sk/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

# Plánovací vzor

## Úvod

Táto lekcia pokryje

* Definovanie jasného celkového cieľa a rozdelenie komplexnej úlohy na zvládnuteľné úlohy.
* Využitie štruktúrovaného výstupu pre spoľahlivejšie a strojovo čitateľné odpovede.
* Použitie event-driven prístupu na spracovanie dynamických úloh a neočakávaných vstupov.

## Ciele učenia

Po dokončení tejto lekcie budete rozumieť:

* Identifikovať a nastaviť celkový cieľ pre AI agenta, zabezpečiť, aby jasne vedel, čo treba dosiahnuť.
* Rozložiť komplexnú úlohu na zvládnuteľné podúlohy a usporiadať ich do logickej postupnosti.
* Vybaviť agentov správnymi nástrojmi (napr. vyhľadávacie nástroje alebo nástroje na analýzu dát), rozhodnúť, kedy a ako ich použiť, a zvládnuť neočakávané situácie, ktoré nastanú.
* Vyhodnotiť výsledky podúloh, merať výkon a iterovať činnosti na zlepšenie konečného výstupu.

## Definovanie celkového cieľa a rozklad úlohy

![Definovanie cieľov a úloh](../../../translated_images/sk/defining-goals-tasks.d70439e19e37c47a.webp)

Väčšina úloh v reálnom svete je príliš zložitá na vyriešenie jedným krokom. AI agent potrebuje stručný cieľ, ktorý ho navádza pri plánovaní a činoch. Napríklad zvážme cieľ:

    "Vytvoriť 3-dňový cestovný itinerár."

Aj keď je to jednoduché vyjadrenie, stále potrebuje upresnenie. Čím jasnejší cieľ, tým lepšie sa agent (a akýkoľvek ľudský spolupracovník) môže sústrediť na dosiahnutie správneho výsledku, ako je vytvorenie komplexného itinerára s možnosťami letov, odporúčaniami hotelov a návrhmi aktivít.

### Rozklad úlohy

Veľké alebo zložité úlohy sa stanú zvládnuteľnejšími, ak ich rozdelíme na menšie, cieľovo orientované podúlohy.
Pre príklad cestovného itinerára môžete cieľ rozdeliť na:

* Rezervácia letu
* Rezervácia hotela
* Prenájom auta
* Personalizácia

Každú podúlohu potom môže riešiť vyhradený agent alebo proces. Jeden agent sa môže špecializovať na vyhľadávanie najlepších leteniek, iný sa zameriava na rezervácie hotelov a tak ďalej. Koordinujúci alebo „downstream“ agent potom môže tieto výsledky skombinovať do jedného zjednoteného itinerára pre koncového používateľa.

Tento modulárny prístup tiež umožňuje postupné vylepšenia. Napríklad môžete pridať špecializovaných agentov pre odporúčania jedla alebo návrhy miestnych aktivít a časom itinerár vylepšovať.

### Štruktúrovaný výstup

Veľké jazykové modely (LLM) môžu generovať štruktúrovaný výstup (napr. JSON), ktorý je pre následných agentov alebo služby ľahšie spracovateľný. To je obzvlášť užitočné v kontexte viacerých agentov, kde môžeme vykonať tieto úlohy po prijatí plánovacieho výstupu.

Nasledujúci útržok kódu v Pythone demonštruje jednoduchého plánovacieho agenta, ktorý rozkladá cieľ na podúlohy a generuje štruktúrovaný plán:

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

# Model podúlohy cestovania
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # Chceme priradiť úlohu agentovi

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

V tomto príklade agent Semantic Router prijíma požiadavku používateľa (napr. „Potrebujem plán hotela na svoju cestu.“).

Plánovač potom:

* Prijíma plán hotela: Plánovač berie správu používateľa a na základe systémového promptu (vrátane dostupných detailov agentov) generuje štruktúrovaný cestovný plán.
* Zoznam agentov a ich nástrojov: Registr agentov obsahuje zoznam agentov (napr. pre lety, hotely, prenájom áut a aktivity) spolu s funkciami alebo nástrojmi, ktoré ponúkajú.
* Posiela plán príslušným agentom: Podľa počtu podúloh plánovač buď odošle správu priamo vyhradenému agentovi (pri jednoulohovej situácii), alebo koordinuje cez manažéra skupinového chatu pre multi-agentnú spoluprácu.
* Zhrnie výsledok: Nakoniec plánovač zhrnie vygenerovaný plán pre prehľadnosť.
Nasledujúci ukážkový kód v Pythone ilustruje tieto kroky:

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

# Model podúlohy cestovania

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

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Vytvorte klienta

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

Čo nasleduje, je výstup z predchádzajúceho kódu a potom môžete použiť tento štruktúrovaný výstup na smerovanie k `assigned_agent` a zhrnúť cestovný plán pre koncového používateľa.

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

Príklad notebooku s predchádzajúcim kódom je dostupný [tu](./code_samples/07-python-agent-framework.ipynb).

### Iteratívne plánovanie

Niektoré úlohy vyžadujú spätnú väzbu alebo preplánovanie, kde výsledok jednej podúlohy ovplyvňuje ďalšiu. Napríklad, ak agent pri rezervácii letu zistí neočakávaný formát dát, môže byť potrebné upraviť stratégiu pred pokračovaním k rezerváciám hotelov.

Okrem toho spätná väzba používateľa (napr. človek rozhodne, že uprednostňuje skorší let) môže spustiť čiastočné preplánovanie. Tento dynamický, iteratívny prístup zabezpečuje, že konečné riešenie zodpovedá reálnym obmedzeniam a vyvíjajúcim sa preferenciám používateľa.

napr. ukážkový kód

```python
import os
from agent_framework.foundry import FoundryChatClient
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
# .. preplánovať a poslať úlohy príslušným agentom
```

Pre komplexnejšie plánovanie si pozrite Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> pre riešenie komplexných úloh.

## Zhrnutie

V tomto článku sme si ukázali príklad, ako môžeme vytvoriť plánovač, ktorý dynamicky vyberá dostupných definovaných agentov. Výstup plánovača rozkladá úlohy a priraďuje agentov, aby mohli byť vykonané. Predpokladá sa, že agenti majú prístup k funkciám/nástrojom potrebným na vykonanie úlohy. Okrem agentov môžete zahrnúť aj ďalšie vzory ako reflexiu, sumarizátor a round robin chat pre ďalšie prispôsobenie.

## Dodatočné zdroje

Magnetic One - Generálny multi-agentný systém na riešenie komplexných úloh, ktorý dosiahol pôsobivé výsledky na viacerých náročných agentových benchmarkoch. Referencia: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. V tejto implementácii orchestrátor vytvára plány špecifické pre úlohy a deleguje tieto úlohy dostupným agentom. Okrem plánovania orchestrátor používa aj sledovací mechanizmus na monitorovanie priebehu úlohy a pre-plánuje podľa potreby.

### Máte ďalšie otázky o plánovacom vzore?

Pridajte sa k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby ste sa stretli s ďalšími študentmi, zúčastnili sa konzultačných hodín a dostali odpovede na otázky o AI agentoch.

## Predchádzajúca lekcia

[Budovanie dôveryhodných AI agentov](../06-building-trustworthy-agents/README.md)

## Ďalšia lekcia

[Vzory multi-agentného plánovania](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->