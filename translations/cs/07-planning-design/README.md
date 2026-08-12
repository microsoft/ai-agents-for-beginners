[![Návrhový vzor plánování](../../../translated_images/cs/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Klikněte na obrázek výše pro zobrazení videa této lekce)_

# Návrh plánování

## Úvod

Tato lekce pokryje

* Definování jasného celkového cíle a rozdělení složitého úkolu na zvládnutelné podúkoly.
* Využití strukturovaného výstupu pro spolehlivější a strojově čitelnou odpověď.
* Aplikaci událostmi řízeného přístupu k řešení dynamických úkolů a neočekávaných vstupů.

## Cíle učení

Po dokončení této lekce budete rozumět:

* Jak identifikovat a nastavit celkový cíl pro AI agenta, aby jasně věděl, čeho má dosáhnout.
* Jak rozdělit složitý úkol na zvládnutelné podúkoly a uspořádat je do logické posloupnosti.
* Jak vybavit agenty správnými nástroji (např. nástroji pro vyhledávání nebo analytiku dat), rozhodnout, kdy a jak je použít, a zvládat neočekávané situace, které vzniknou.
* Jak vyhodnotit výsledky podúkolů, měřit výkon a iterativně zlepšovat konečný výstup.

## Definování celkového cíle a rozdělení úkolu

![Definování cílů a úkolů](../../../translated_images/cs/defining-goals-tasks.d70439e19e37c47a.webp)

Většina reálných úkolů je příliš složitá na řešení v jednom kroku. AI agent potřebuje stručný cíl, který ho bude vést při plánování a činnostech. Například zvažte cíl:

    "Vytvořit cestovní plán na 3 dny."

Přestože je jednoduché ho vyjádřit, stále vyžaduje upřesnění. Čím jasnější je cíl, tím lépe se agent (a případní lidskí spolupracovníci) mohou zaměřit na dosažení správného výsledku, jako je vytvoření komplexního itineráře s možnosti letenek, doporučení hotelů a návrhů aktivit.

### Rozklad úkolu

Velké nebo složité úkoly se stávají zvládnutelnými, když je rozdělíme na menší, cílené podúkoly.
Pro příklad cestovního plánu můžete rozdělit cíl na:

* Rezervace letu
* Rezervace hotelu
* Půjčení auta
* Personalizace

Každý podúkol může pak řešit specializovaný agent nebo proces. Jeden agent se může zaměřit na hledání nejlepších letenek, jiný na rezervace hotelů, a tak dále. Koordinující nebo „downstream“ agent pak může tyto výsledky zkombinovat do jednoho soudržného itineráře pro koncového uživatele.

Tento modulární přístup také umožňuje postupná vylepšení. Například můžete přidat specializované agenty na doporučení jídla nebo místních aktivit a itinerář v průběhu času zdokonalovat.

### Strukturovaný výstup

Velké jazykové modely (LLMs) mohou generovat strukturovaný výstup (např. JSON), který je snazší pro downstream agenty nebo služby zpracovat a analyzovat. Je to zvláště užitečné v kontextu více agentů, kde můžeme tyto úkoly realizovat po obdržení plánovacího výstupu.

Následující Python ukázka demonstruje jednoduchého plánovacího agenta, který rozkládá cíl na podúkoly a vytváří strukturovaný plán:

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

# Model podúkolu cestování
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # chceme přiřadit úkol agentovi

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

V tomto příkladu Semantic Router Agent přijímá uživatelský požadavek (např. "Potřebuji plán hotelu pro svou cestu.").

Plánovač pak:

* Přijme Plán hotelu: Plánovač vezme uživatelovu zprávu a na základě systémového promptu (včetně dostupných agentů) vytvoří strukturovaný cestovní plán.
* Vyjmenuje agenty a jejich nástroje: Registr agentů obsahuje seznam agentů (např. pro lety, hotely, půjčení auta a aktivity) a nástroje nebo funkce, které nabízejí.
* Přesměruje plán příslušným agentům: V závislosti na počtu podúkolů plánovač buď pošle zprávu přímo specializovanému agentu (pro scénáře s jedním úkolem), nebo koordinuje přes správce skupinového chatu pro spolupráci více agentů.
* Shrne výsledek: Nakonec plánovač shrne vytvořený plán pro přehlednost.
Následující ukázka v Pythonu ilustruje tyto kroky:

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

# Model podúkolu cesty

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # chceme úkol přiřadit agentovi

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Vytvořit klienta

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

from pprint import pprint

# Definovat uživatelskou zprávu

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

# Vytisknout obsah odpovědi po jeho načtení jako JSON

pprint(json.loads(response_content))
```

Následuje výstup z předchozího kódu, který můžete pak použít k přesměrování na `assigned_agent` a shrnutí cestovního plánu koncovému uživateli.

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

Příklad notebooku s předchozím kódem je k dispozici [zde](./code_samples/07-python-agent-framework.ipynb).

### Iterativní plánování

Některé úkoly vyžadují zpětnou vazbu nebo přeplánování, kdy výsledek jednoho podúkolu ovlivňuje další. Například pokud agent narazí na neočekávaný formát dat při rezervaci letů, může potřebovat upravit svoji strategii před přechodem k rezervacím hotelů.

Navíc uživatelská zpětná vazba (např. člověk rozhodující, že preferuje dřívější let) může spustit částečné přeplánování. Tento dynamický, iterativní přístup zajišťuje, že konečné řešení odpovídá reálným omezením a vyvíjejícím se preferencím uživatele.

např. ukázkový kód

```python
import os
from agent_framework.foundry import FoundryChatClient
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
# .. přeplánovat a poslat úkoly příslušným agentům
```

Pro komplexnější plánování si prohlédněte Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> pro řešení složitých úkolů.

## Shrnutí

V tomto článku jsme se podívali na příklad, jak můžeme vytvořit plánovač, který dokáže dynamicky vybrat dostupné definované agenty. Výstup plánovače rozkládá úkoly a přiděluje agenty tak, aby mohly být provedeny. Předpokládá se, že agenti mají přístup k funkcím/nástrojům potřebným k vykonání úkolu. Kromě agentů můžete zahrnout i další vzory jako reflexe, shrnovač a round robin chat pro další přizpůsobení.

## Další zdroje

Magnetic One - Generalistický multi-agentní systém pro řešení složitých úkolů, který dosáhl působivých výsledků na několika náročných agentních benchmarkech. Reference: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. V této implementaci orchestrátor vytváří úkolově specifické plány a deleguje tyto úkoly dostupným agentům. Kromě plánování orchestrátor také využívá mechanismus sledování průběhu úkolu a podle potřeby přeplánovává.

### Máte další otázky ohledně vzoru plánování?

Připojte se na [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), setkejte se s dalšími studenty, zúčastněte se konzultačních hodin a nechte si zodpovědět své otázky týkající se AI agentů.

## Předchozí lekce

[Vytváření důvěryhodných AI agentů](../06-building-trustworthy-agents/README.md)

## Následující lekce

[Víceagentní návrhový vzor](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->