[![Planning Design Pattern](../../../translated_images/cs/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Klikněte na obrázek výše pro zobrazení videa této lekce)_

# Návrh plánování

## Úvod

Tato lekce pokryje

* Definování jasného celkového cíle a rozdělení složitého úkolu na zvládnutelné dílčí úkoly.
* Využití strukturovaného výstupu pro spolehlivější a strojově čitelnou odpověď.
* Aplikaci přístupu řízeného událostmi pro zvládání dynamických úkolů a neočekávaných vstupů.

## Cíle učení

Po absolvování této lekce budete mít přehled o:

* Identifikaci a stanovení celkového cíle pro AI agenta, tak aby jasně věděl, čeho má být dosaženo.
* Rozložení složitého úkolu na zvládnutelné dílčí úkoly a jejich uspořádání do logické sekvence.
* Vybavení agentů správnými nástroji (např. nástroji pro vyhledávání nebo nástroji pro analýzu dat), rozhodování kdy a jak je použít a zvládání neočekávaných situací, které vzniknou.
* Vyhodnocování výsledků dílčích úkolů, měření výkonu a iterování činností pro zlepšení konečného výstupu.

## Definování celkového cíle a rozdělení úkolu

![Definování cílů a úkolů](../../../translated_images/cs/defining-goals-tasks.d70439e19e37c47a.webp)

Většina reálných úkolů je příliš složitá na to, aby byla řešena jedním krokem. AI agent potřebuje stručný cíl, který bude řídit jeho plánování a akce. Například zvažte cíl:

    "Vytvořit 3denní cestovní itinerář."

I když je to jednoduše formulován, stále potřebuje upřesnění. Čím jasnější je cíl, tím lépe se agent (a i případní lidskí spolupracovníci) může soustředit na dosažení správného výsledku, jako je vytvoření komplexního itineráře s možnostmi letenek, doporučeními hotelů a návrhy aktivit.

### Rozklad úkolu

Velké nebo složité úkoly se stávají lépe zvládnutelnými, když jsou rozděleny na menší dílčí úkoly orientované na cíl.
Pro příklad cestovního itineráře lze cíl rozdělit na:

* Rezervaci letu
* Rezervaci hotelu
* Půjčení auta
* Personalizaci

Každý dílčí úkol pak může být zpracován speciálními agenty nebo procesy. Jeden agent se může specializovat na hledání nejlepších nabídek na letenky, další na rezervace hotelu a tak dále. Koordinující nebo „následný“ agent pak může tyto výsledky sestavit do jednoho uceleného itineráře pro koncového uživatele.

Tento modulární přístup také umožňuje postupné vylepšení. Například můžete přidat specializované agenty pro doporučení jídla nebo místních aktivit a itinerář postupně zdokonalovat.

### Strukturovaný výstup

Velké jazykové modely (LLMs) mohou generovat strukturovaný výstup (např. JSON), který je jednodušší pro následné agenty nebo služby k parsování a zpracování. To je zvlášť užitečné v multi-agentním kontextu, kde můžeme provádět úkoly po obdržení výstupu z plánování.

Následující ukázka v Pythonu demonstruje jednoduchého plánovacího agenta, který rozkládá cíl na dílčí úkoly a generuje strukturovaný plán:

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

# Model cestovního podúkolu
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # chceme přiřadit úkol agentovi

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Definujte uživatelskou zprávu
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

### Plánovací agent s multi-agentní orchestrací

V tomto příkladu agent Semantic Router přijímá uživatelský požadavek (např. "Potřebuji plán hotelu pro mou cestu.").

Plánovač pak:

* Přijímá plán hotelu: Plánovač vezme uživatelovu zprávu a na základě systémové výzvy (včetně dostupných agentů) vygeneruje strukturovaný cestovní plán.
* Vypíše agenty a jejich nástroje: Registr agentů obsahuje seznam agentů (např. pro lety, hotely, půjčení auta a aktivity) spolu s funkcemi nebo nástroji, které poskytují.
* Směruje plán ke konkrétním agentům: V závislosti na počtu dílčích úkolů plánovač buď zprávu pošle přímo vyhrazenému agentovi (pro scénáře s jedním úkolem), nebo koordinuje přes manažera skupinového chatu pro multi-agentní spolupráci.
* Shrnuje výsledek: Nakonec plánovač shrne vygenerovaný plán pro přehlednost.
Následující ukázkový kód v Pythonu ilustruje tyto kroky:

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

# Model podúkolu cestování

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # chceme přiřadit úkol agentovi

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Vytvořte klienta

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Definujte uživatelskou zprávu

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

# Vytiskněte obsah odpovědi po načtení jako JSON

pprint(json.loads(response_content))
```

Následuje výstup z předchozího kódu, který pak můžete použít ke směrování na `assigned_agent` a shrnutí cestovního plánu pro koncového uživatele.

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

Příklad notebooku s předchozím kódem je k dispozici [zde](07-python-agent-framework.ipynb).

### Iterativní plánování

Některé úkoly vyžadují zpětnou vazbu nebo přeplánování, kdy výsledek jednoho dílčího úkolu ovlivňuje následující. Například pokud agent objeví neočekávaný formát dat při rezervaci letů, může být potřeba upravit strategii před pokračováním na rezervaci hotelu.

Navíc uživatelská zpětná vazba (např. když člověk rozhodne, že preferuje dřívější let) může spustit částečné přeplánování. Tento dynamický, iterativní přístup zajišťuje, že konečné řešení odpovídá reálným omezením a měnícím se preferencím uživatele.

např. ukázkový kód

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. stejné jako předchozí kód a předat historii uživatele, aktuální plán

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
# .. přeplánovat a odeslat úkoly příslušným agentům
```

Pro komplexnější plánování doporučujeme navštívit Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> pro řešení složitých úkolů.

## Shrnutí

V tomto článku jsme se podívali na příklad, jak můžeme vytvořit plánovač, který dokáže dynamicky vybírat definované dostupné agenty. Výstup plánovače rozkládá úkoly a přiřazuje agenty tak, aby mohly být vykonány. Předpokládá se, že agenti mají přístup k funkcím/nástrojům potřebným k provedení úkolu. Navíc ke agentům můžete přidat další vzory jako reflexi, shrnování a round robin chat pro další přizpůsobení.

## Další zdroje

Magentic One - Generalistický multi-agentní systém pro řešení složitých úkolů, který dosáhl impozantních výsledků v několika náročných agentních benchmarkech. Reference: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. V této implementaci orchestrátor vytváří úkolově specifické plány a deleguje tyto úkoly dostupným agentům. Kromě plánování orchestrátor používá i mechanismus sledování postupu úkolu a přeplánovává podle potřeby.

### Máte další otázky ohledně návrhového vzoru plánování?

Připojte se k [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kde se setkáte s dalšími studenty, zúčastníte se konzultačních hodin a získáte odpovědi na své otázky ohledně AI agentů.

## Předchozí lekce

[Budování důvěryhodných AI agentů](../06-building-trustworthy-agents/README.md)

## Další lekce

[Multi-agentní návrhový vzor](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo chybné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->