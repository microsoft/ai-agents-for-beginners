[![Planning Design Pattern](../../../translated_images/sk/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

# Návrh plánovania

## Úvod

Táto lekcia bude pokrývať

* Definovanie jasného celkového cieľa a rozdelenie zložitej úlohy na zvládnuteľné úlohy.
* Využitie štruktúrovaného výstupu pre spoľahlivejšie a strojovo čitateľné odpovede.
* Použitie prístupu riadeného udalosťami na zvládanie dynamických úloh a nečakaných vstupov.

## Ciele učenia

Po absolvovaní tejto lekcie budete mať pochopenie o:

* Identifikácii a nastavení celkového cieľa pre AI agenta, zabezpečiť, aby jasne vedel, čo je potrebné dosiahnuť.
* Rozloženie zložitej úlohy na zvládnuteľné podúlohy a ich organizovanie do logickej postupnosti.
* Vybaviť agentov správnymi nástrojmi (napr. vyhľadávacie nástroje alebo nástroje na analýzu dát), rozhodnúť, kedy a ako sa používajú, a zvládať neočakávané situácie, ktoré môžu vzniknúť.
* Hodnotiť výsledky podúloh, merať výkonnosť a opakovane meniť kroky pre zlepšenie konečného výstupu.

## Definovanie celkového cieľa a rozdelenie úlohy

![Definovanie cieľov a úloh](../../../translated_images/sk/defining-goals-tasks.d70439e19e37c47a.webp)

Väčšina reálnych úloh je príliš zložitá na riešenie v jednom kroku. AI agent potrebuje stručný cieľ, ktorý bude viesť jeho plánovanie a činnosti. Napríklad zvážte cieľ:

    "Vytvoriť trojdňový cestovný itinerár."

Aj keď je to jednoduché na vyjadrenie, stále je potrebné ho upresniť. Čím jasnejší cieľ, tým lepšie sa agent (a akýkoľvek ľudský spolupracovník) môže zamerať na dosiahnutie správneho výsledku, ako je vytvorenie komplexného itinerára s možnosťami letov, odporúčaniami hotelov a návrhmi aktivít.

### Rozklad úlohy

Veľké alebo zložité úlohy sa stanú ovládateľnejšie, keď sa rozdelia na menšie, cieľ-orientované podúlohy.
Pre príklad cestovného itinerára by ste mohli rozložiť cieľ na:

* Rezervácia letu
* Rezervácia hotela
* Prenájom auta
* Personalizácia

Každú podúlohu môže potom riešiť určený agent alebo proces. Jeden agent sa môže špecializovať na hľadanie najlepších leteniek, iný na rezervácie hotelov a tak ďalej. Koordinujúci alebo „následný“ agent potom môže tieto výsledky skombinovať do jedného súdržného itinerára pre koncového používateľa.

Tento modulárny prístup tiež umožňuje inkrementálne vylepšenia. Napríklad by ste mohli pridať špecializovaných agentov na odporúčania jedla alebo návrhy miestnych aktivít a itinerár priebežne zdokonaľovať.

### Štruktúrovaný výstup

Veľké jazykové modely (LLM) môžu generovať štruktúrovaný výstup (napr. JSON), ktorý je ľahšie spracovateľný následnými agentmi alebo službami. To je obzvlášť užitočné v kontexte multi-agentov, kde môžeme vykonať úlohy po prijatí plánovacieho výstupu.

Nasledujúci ukážkový kód v Pythone demonštruje jednoduchého plánovacieho agenta, ktorý rozkladá cieľ na podúlohy a vytvára štruktúrovaný plán:

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

# Model podúlohy cesty
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # chceme priradiť úlohu agentovi

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Definovať správu používateľa
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

### Plánovací agent s orchestráciou viacerých agentov

V tomto príklade Semantic Router Agent prijme požiadavku používateľa (napr. "Potrebujem hotelový plán na moju cestu.").

Plánovač potom:

* Prijíma Hotelový plán: plánovač berie správu používateľa a na základe systémovej výzvy (vrátane detailov dostupných agentov) generuje štruktúrovaný cestovný plán.
* Vypisuje agentov a ich nástroje: registr agentov obsahuje zoznam agentov (napr. na lety, hotely, prenájom áut a aktivity) spolu s funkciami alebo nástrojmi, ktoré ponúkajú.
* Smeruje plán príslušným agentom: v závislosti od počtu podúloh plánovač buď odošle správu priamo vyhradenému agentovi (pre scenáre s jedinou úlohou), alebo koordinuje cez správcu skupinového chatu pre spoluprácu viacerých agentov.
* Zhrnie výsledok: nakoniec plánovač zhrnie vytvorený plán pre prehľadnosť.
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

# Model čiastkovej úlohy cestovania

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # Chceme priradiť úlohu agentovi

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

Nasleduje výstup z predchádzajúceho kódu a tento štruktúrovaný výstup môžete potom použiť na smerovanie k `assigned_agent` a zhrnutie cestovného plánu pre koncového používateľa.

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

Príklad notebooku s predchádzajúcim kódom je k dispozícii [tu](07-python-agent-framework.ipynb).

### Iteratívne plánovanie

Niektoré úlohy vyžadujú spätnú väzbu alebo preplánovanie, kde výsledok jednej podúlohy ovplyvňuje ďalšiu. Napríklad, ak agent zistí neočakávaný formát dát počas rezervácie letov, môže byť potrebné upraviť stratégiu pred pokračovaním k rezervácii hotelov.

Okrem toho spätná väzba používateľa (napr. keď človek rozhodne, že uprednostňuje skorší let) môže spustiť čiastočné preplánovanie. Tento dynamický, iteratívny prístup zabezpečuje, že konečné riešenie je v súlade s reálnymi obmedzeniami a vyvíjajúcimi sa preferenciami používateľa.

napr. ukážkový kód

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. rovnaké ako predchádzajúci kód a odovzdanie histórie používateľa, aktuálneho plánu

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
# .. preplánuj a pošli úlohy príslušným agentom
```

Pre komplexnejšie plánovanie si pozrite Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> pre riešenie zložitých úloh.

## Zhrnutie

V tomto článku sme si ukázali príklad, ako môžeme vytvoriť plánovač, ktorý dokáže dynamicky vybrať dostupných definovaných agentov. Výstup plánovača rozkladá úlohy a priraďuje agentov, aby mohli byť vykonané. Predpokladá sa, že agenti majú prístup k funkciám/nástrojom, ktoré sú potrebné na vykonanie úlohy. Okrem agentov môžete zahrnúť aj iné vzory ako reflexiu, sumarizátor a rotujúci chat pre ďalšiu prispôsobivosť.

## Dodatočné zdroje

Magentic One - Všeobecný multi-agentný systém na riešenie zložitých úloh, ktorý dosiahol pôsobivé výsledky na viacerých náročných agentných testoch. Referencia: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. V tejto implementácii orchestrátor vytvára úlohové plány špecifické pre dané úlohy a deleguje ich dostupným agentom. Okrem plánovania orchestrátor používa mechanizmus sledovania pokroku úlohy a podľa potreby preplánuje.

### Máte viac otázok o návrhu plánovania?

Pridajte sa k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby ste sa stretli s inými študentmi, zúčastnili sa konzultačných hodín a dostali odpovede na vaše otázky o AI agentoch.

## Predchádzajúca lekcia

[Budovanie dôveryhodných AI agentov](../06-building-trustworthy-agents/README.md)

## Nasledujúca lekcia

[Návrh multi-agentov](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->