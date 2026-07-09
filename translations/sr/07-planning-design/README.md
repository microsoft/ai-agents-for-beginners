[![Плански дизајн шаблон](../../../translated_images/sr/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Кликните на слику изнад да бисте погледали видео о овом часу)_

# Плански дизајн

## Увод

Овај час ће обухватити

* Дефинисање јасног општег циља и разлагање сложеног задатка на управљиве задатке.
* Коришћење структурисаног излаза за поузданије и машински читљиве одговоре.
* Примена приступа вођеног догађајима за руковање динамичким задацима и неочекиваним уносима.

## Циљеви учења

Након завршетка овог часа, имаћете разумевање о:

* Идентификовању и постављању општег циља за AI агента, обезбеђујући да јасно зна шта треба постићи.
* Разлагању сложеног задатка на управљиве подзадатке и организовању у логичан низ.
* Опремању агената правим алатима (нпр. алатима за претрагу или анализу података), одлучивању када и како се користе, и руковању неочекиваним ситуацијама које се појаве.
* Процени резултата подзадатака, мери перформансе и итеративном унапређењу акција ради побољшања коначног излаза.

## Дефинисање општег циља и разлагање задатка

![Дефинисање циљева и задатака](../../../translated_images/sr/defining-goals-tasks.d70439e19e37c47a.webp)

Већина стварних задатака је превише сложена да би се приступило у једном кораку. AI агенту је потребан концизан циљ који ће га усмеравати у планирању и деловању. На пример, размотрите циљ:

    "Креирај тродневни план путовања."

Иако је једноставан за изражавање, и даље захтева прецизирање. Што је циљ јаснији, то агент (и било који људски сарадници) могу боље да се усредсреде на постизање правог резултата, као што је прављење свеобухватног плана са опцијама за лет, препорукама за хотел и предлозима за активности.

### Разлагање задатка

Велики или сложени задаци постају управљивији када се поделе на мање, усмерене подзадатке.
За пример плана путовања, можете разложити циљ у:

* Резервација лета
* Резервација хотела
* Изнајмљивање аутомобила
* Персонализација

Сваки подзадатак онда могу обављати посвећени агенти или процеси. Један агент се може специјализовати за проналажење најбољих понуда за летове, други за резервације хотела и тако даље. Координаторски или „доњи“ агент може сабрати ове резултате у један кохерентни план за крајњег корисника.

Овај модуларни приступ такође омогућава постепена унапређења. На пример, можете додати специјализоване агенте за препоруке хране или локалне активности и временом побољшавати план.

### Структурисани излаз

Велики језички модели (LLM) могу генерисати структурисани излаз (нпр. JSON) који је лакши за разумевање и обраду од стране доњих агената или сервиса. Ово је посебно корисно у контексту са више агената, где можемо извршити ове задатке након што се добије план.

Следећи пример у Python-у показује једноставан агент планирања који разлаже циљ на подзадатке и генерише структурирани план:

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

# Модел потзадаће путовања
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # Желимо да доделимо задатак агенту

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

### Плански агент са вишеагентском оркестрацијом

У овом примеру, Семантички рутер агент прима кориснички захтев (нпр. "Потребан ми је план хотела за моје путовање.").

Планирач затим:

* Прима план хотела: Планирач узима поруку корисника и, на основу системског упита (укључујући детаље доступних агената), генерише структурирани план путовања.
* Листује агенте и њихове алате: Регистар агената садржи листу агената (нпр. за летове, хотел, изнајмљивање аутомобила и активности) заједно са функцијама или алатима које они нуде.
* Прослеђује план одговарајућим агентима: У зависности од броја подзадатака, планирач или шаље поруку директно посвећеном агенту (за сценарије са једним задатком), или координише преко менаџера групног ћаскања за сарадњу више агената.
* Сумира резултат: На крају, планирач прави резиме генерисаног плана ради јасноће.
Следећи пример Python кода илуструје ове кораке:

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

# Модел подзадатка путовања

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

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Креирајте клијента

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

from pprint import pprint

# Дефинишите корисничку поруку

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

# Испишите садржај одговора након учитавања као JSON

pprint(json.loads(response_content))
```

Следи излаз из претходног кода и онда можете користити овај структурисани излаз за прослеђивање `assigned_agent` и сажимање плана путовања крајњем кориснику.

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

Пример notebook-а са претходним примером кода доступан је [овде](./code_samples/07-python-agent-framework.ipynb).

### Итеративно планирање

Неки задаци захтевају додатну размену или поновно планирање, где резултат једног подзадатка утиче на следећи. На пример, ако агент открије неочекиван формат података током резервације летова, можда ће морати да прилагоди стратегију пре него што пређе на резервацију хотела.

Поред тога, повратне информације корисника (нпр. да људски корисник одлучи да више воли ранији лет) могу покренути делимично поновно планирање. Овај динамичан, итеративни приступ осигурава да коначна решења буду усклађена са стварним ограничењима и еволуирајућим преференцама корисника.

на пример код

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. исто као и претходни код и проследи историју корисника, тренутни план

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

За обимније планирање погледајте Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Блог пост</a> за решавање сложених задатака.

## Резиме

У овом чланку смо видели пример како можемо направити планирача који динамички бира доступне дефинисане агенте. Излаз планирача разлаже задатке и додељује агенте како би се они могли извршити. Претпоставља се да агенти имају приступ функцијама/алатима који су потребни за обављање задатка. Поред агената, можете укључити и друге шаблоне као што су рефлексија, сумарајзер и ротациони ћаскање за даљу прилагодбу.

## Додатни ресурси

Magnetic One - Генералистички вишеагентски систем за решавање сложених задатака и постигао је импресивне резултате на више изазовних бенчмаркова за агенте. Референца: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. У овој имплементацији оркестратор креира планове специфичне за задатке и делегира их доступним агентима. Поред планирања, оркестратор користи и механизам праћења напретка задатка и по потреби препланира.

### Имаш још питања о Планском дизајн шаблону?

Придружите се [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) да се сретнете са другим ученицима, посетите консултације и добијете одговоре на питања о AI агентима.

## Претходни час

[Прављење поузданих AI агената](../06-building-trustworthy-agents/README.md)

## Следећи час

[Вишеагентски дизајн шаблон](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->