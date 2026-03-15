[![Planning Design Pattern](../../../translated_images/sr/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Кликните на слику изнад да бисте погледали видео о овој лекцији)_

# Планирање дизајна

## Увод

Ова лекција ће обухватити

* Дефинисање јасног укупног циља и раздвајање сложеног задатка на управљиве задатке.
* Користећи структурисани излаз за поузданије и машински читљиве одговоре.
* Примену приступа вођеног догађајима за руковање динамичким задацима и неочекиваним уносима.

## Циљеви учења

Након завршетка ове лекције, разумећете:

* Идентификовати и поставити укупни циљ за АИ агента, обезбеђујући да јасно зна шта треба постићи.
* Разложити сложен задатак на управљиве подзадатке и организовати их у логичан низ.
* Оспособити агенте одговарајућим алатима (нпр. алатке за претрагу или алатке за анализу података), одлучити кад и како се користе и обратити пажњу на неочекиване ситуације које се појављују.
* Проценити резултате подзадатака, измерити перформансе и итерирати акције како би се побољшао коначни резултат.

## Дефинисање укупног циља и раздвајање задатка

![Defining Goals and Tasks](../../../translated_images/sr/defining-goals-tasks.d70439e19e37c47a.webp)

Већина стварних задатака је превише сложена да се реши у једном кораку. АИ агенту је потребан концизан циљ да би водио своје планирање и радње. На пример, узмимо циљ:

    "Направити план путовања за 3 дана."

Иако је једноставан за изражавање, ипак захтева прецизнију дефиницију. Што је циљ јаснији, то агент (а и сви људски сарадници) могу боље да се фокусирају на постизање исправног резултата, као што је стварање свеобухватног плана са опцијама летења, препорукама за хотеле и предлозима активности.

### Разлагање задатка

Велики или сложени задаци постају управљивији када се поделе на мање, циљно оријентисане подзадатке.
За пример плана путовања, можете разложити циљ на:

* Резервација лета
* Резервација хотела
* Изнајмљивање аутомобила
* Персонализација

Сваки подзадатак тада може обрадити посебан агент или процес. Један агент може бити специјализован за претрагу најбољих понуда летова, други за резервацију хотела итд. Координатор или „доњи“ агент може компајлирати ове резултате у један кохезивни план за крајњег корисника.

Ова модуларна стратегија такође дозвољава инкременталне надоградње. На пример, можете додати специјализоване агенте за препоруке хране или локалне активности и временом усавршавати план путовања.

### Структурисани излаз

Велики језички модели (LLM) могу генерисати структурирани излаз (нпр. JSON) који је лакши за анализу и обраду од стране доњих агената или услуга. Ово је посебно корисно у мулти-агентском контексту, где можемо извршити ове задатке након пријема плана.

Следећи пример у Питону демонстрира једноставног планирајућег агента који разлага циљ на подзадатке и генерише структурисани план:

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

# Модел потзадаће путовања
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # желимо да доделимо задатак агенту

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Дефиниши поруку корисника
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

### Планирајући агент са мулти-агентском организацијом

У овом примеру, Семантички рутер агент прима кориснички захтев (нпр. „Потребан ми је план хотела за моје путовање.“).

Планирајући тада:

* Прима план хотела: Планирајући узима поруку корисника и, на основу системске поруке (укључујући детаље о расположивим агентима), генерише структурисани план путовања.
* Листује агенте и њихове алатке: Регистар агената држи листу агената (нпр. за лет, хотел, изнајмљивање аутомобила и активности) заједно са функцијама или алаткама које нуде.
* Рутује план до релевантних агената: У зависности од броја подзадатака, планирајући или шаље поруку директно посебном агенту (за сценарије са једним задатком) или координише путем менаџера групног четa за мулти-агентску сарадњу.
* Сажима резултат: На крају, планирајући сажима генерисани план ради јасноће.
Следећи Python пример илуструје ове кораке:

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

# Модел подсистема за путовања

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # желимо да доделимо задатак агенту

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Креирај клијента

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Дефиниши поруку корисника

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

# Испиши садржај одговора након учитавања као JSON

pprint(json.loads(response_content))
```

Онај излаз који следи је резултат претходног кода и можете тада користити овај структурирани излаз за рутирање ка `assigned_agent` и сажети план путовања крајњем кориснику.

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

Пример ноутбука са претходним примером кода доступан је [овде](07-python-agent-framework.ipynb).

### Итеративно планирање

Неки задаци захтевају преплитање или поновно планирање, где резултат једног подзадатка утиче на следећи. На пример, ако агент открије неочекивани формат података приликом резервације летова, можда ће морати да прилагоди своју стратегију пре него што настави резервацију хотела.

Поред тога, повратне информације корисника (нпр. ако човек одлучи да више воли ранији лет) могу покренути делимично поновно планирање. Ова динамична, итеративна метода осигурава да коначна решења одговарају стварним ограничењима и развијајућим корисничким преференцама.

нпр. пример кода

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. исто као претходни код и проследи корисничку историју, тренутни план

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
# .. поново испланирај и пошаљи задатке одговарајућим агентима
```

За свеобухватније планирање погледајте Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Блогпост</a> за решавање сложених задатака.

## Резиме

У овом чланку смо видели пример како можемо направити планирача који динамички бира расположиве дефинисане агенте. Излаз планирача раздваја задатке и додељује агенте тако да они могу извршити задатак. Претпоставља се да агенти имају приступ функцијама/алатима који су потребни за извршење задатка. Поред агената можете укључити и друге шаблоне попут рефлексије, сумаризатора и ротационог четовања за даље прилагођавање.

## Додатни ресурси

Magentic One - Генералистички мулти-агентски систем за решавање сложених задатака који је постигао импресивне резултате на више захтевних агенцких тестова. Референца: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. У овом имплементацији оркестратор креира планове специфичне за задатке и делегира задатке расположивим агентима. Поред планирања, оркестратор такође користи механизам праћења напретка задатка и поново планира по потреби.

### Имате још питања у вези са узорком планирања?

Придружите се [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) да упознате друге ученике, присуствујете канцеларијским часовима и добијете одговоре на питања о АИ агенатима.

## Претходна лекција

[Грађење поузданих АИ агената](../06-building-trustworthy-agents/README.md)

## Следећа лекција

[Узорaк мулти-агента](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо прецизност, имајте у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални превод који обавља људски стручњак. Нисмо одговорни за било каква неспоразумевања или погрешне тумачења која могу произаћи из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->