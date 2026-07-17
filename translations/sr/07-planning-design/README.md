[![Планирање дизајн обрасца](../../../translated_images/sr/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Кликните на слику изнад да бисте погледали видео о овом лекцији)_

# Планирање дизајна

## Увод

Ова лекција ће обухватити

* Дефинисање јасног укупног циља и раздвајање сложеног задатка на управљиве задатке.
* Коришћење структурисаног излаза за поузданије и машинама читљиве одговоре.
* Примена приступа који се заснива на догађајима за руковање динамичким задацима и неочекиваним улазима.

## Циљеви учења

Након завршетка ове лекције, разумећете:

* Идентификовати и поставити укупни циљ за AI агента, осигуравајући да јасно зна шта треба постићи.
* Разложити сложен задатак на управљиве подзадатке и организовати их у логички низ.
* Опрометити агенте правим алатима (нпр. алати за претрагу или алати за анализу података), одлучити када и како се користе и руковати неочекиваним ситуацијама које се појаве.
* Проценити резултате подзадатака, мерити перформансе и поновити акције у циљу побољшања коначног излаза.

## Дефинисање укупног циља и раздвајање задатка

![Дефинисање циљева и задатака](../../../translated_images/sr/defining-goals-tasks.d70439e19e37c47a.webp)

Већина задатака из стварног света је превише сложена да би се решила у једном кораку. AI агенту је потребан концизан циљ који ће водити његово планирање и акције. На пример, размотрите циљ:

    "Направити 3-дневни план путовања."

Иако је једноставан за изјаву, и даље захтева прецизирање. Што је циљ јаснији, тим боље агент (и било који људски сарадници) могу да се концентришу на постизање исправног резултата, као што је креирање детаљног плана са опцијама летења, препорукама за хотел и предлозима за активности.

### Разлагање задатка

Велики или сложени задаци постају управљивији када се поделе на мање, циљано оријентисане подзадатке.
За пример плана путовања можете разложити циљ на:

* Резервација лета
* Резервација хотела
* Изнајмљивање аутомобила
* Персонализација

Сваки подзадатак онда може бити решаван од стране посебних агената или процеса. Један агент може бити специјализован за претраживање најбољих понуда летења, други за резервацију хотела и тако даље. Координациони или „низводни“ агент може онда саставити те резултате у једну кохерентну маршруту за крајњег корисника.

Овај модуларни приступ омогућава и постепена унапређења. На пример, можете додати специјализоване агенте за препоруке хране или предлоге локалних активности и временом дотерати план.

### Структурисани излаз

Велики језички модели (LLMs) могу генерисати структурисани излаз (нпр. JSON) који је лакши за разграђивање и процесирање од стране других агената или сервиса. Ово је посебно корисно у контексту вишеструких агената, где можемо извршавати ове задатке након што добијемо излаз плана.

Следећи пример у Python-у демонстрира једноставног агента за планирање који раздваја циљ на подзадатке и генерише структурирани план:

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

# Модел путне подзадатке
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # желимо да доделимо задатак агенту

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Дефиниши корисничку поруку
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

### АГЕНТ ЗА ПЛАНИРАЊЕ СА МУЛТИ-АГЕНТСКОМ ОРКЕСТРАЦИЈОМ

У овом примеру, агент Семантичког рутирања прима кориснички захтев (нпр. "Потребан ми је хотелски план за моје путовање.").

Планирач онда:

* Прима хотелски план: Планирач узима корисничку поруку и, на основу системског упита (укључујући детаље о расположивим агентима), генерише структуриран путнички план.
* Листује агенте и њихове алате: Регистар агената садржи листу агената (нпр. за лет, хотел, изнајмљивање аутомобила и активности) заједно са функцијама или алатима које нуде.
* Усмерава план ка одговарајућим агентима: У зависности од броја подзадатака, планирач или директно шаље поруку посебном агенту (за сценарије са једним задатком) или координира преко менаџера групног разговора за сарадњу више агената.
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

# Модел потзадаће путовања

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

# Креирај клијента

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

Оно што следи јесте излаз из претходног кода и можете потом користити овај структурисани излаз да усмерите ка `assigned_agent` и резимирате план путовања крајњем кориснику.

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

Пример бележнице са претходним примером кода доступан је [овде](./code_samples/07-python-agent-framework.ipynb).

### Итеративно планирање

Неки задаци захтевају повратну комуникацију или поновно планирање, где резултат једног подзадатка утиче на следећи. На пример, ако агент открије неочекивани формат података приликом резервације летова, мораће да прилагоди своју стратегију пре него што пређе на резервацију хотела.

Поред тога, повратне информације корисника (нпр. човек који одлучи да преферира ранији лет) могу покренути делимично поновно планирање. Овај динамични, итеративни приступ осигурава да коначна решења буду у складу са стварним ограничењима и еволуирајућим корисничким преференцама.

нпр. пример кода

```python
import os
from agent_framework.foundry import FoundryChatClient
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
# .. препланирај и пошаљи задатке одговарајућим агентима
```

За свеобухватније планирање погледајте Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">пост на блогу</a> за решавање сложених задатака.

## Резиме

У овом чланку смо погледали пример како можемо направити планирача који динамички бира расположиве дефинисане агенте. Излаз планирача раздваја задатке и додељује агенте тако да могу бити извршени. Сматра се да агенти имају приступ функцијама/алатима потребним за извођење задатка. Поред агената можете укључити и друге обрасце као што су рефлексија, сумаризатор и кругови разговора за додатно прилагођавање.

## Додатни ресурси

Magnetic One - генералистички мулти-агентски систем за решавање сложених задатака који је постигао импресивне резултате на више изазовних агенцијских бенчмаркова. Референца: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. У овој имплементацији оркестратор креира планове специфичне за задатке и делегира те задатке расположивим агентима. Поред планирања, оркестратор користи и механизам праћења напретка задатка и поновног планирања по потреби.

### Имате још питања о Обрасцу планирања?

Придружите се [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) да упознате друге учеснике, присуствујете канцеларијским сатима и добијете одговоре на питања о AI агентима.

## Претходна лекција

[Израда поузданих AI агената](../06-building-trustworthy-agents/README.md)

## Следећа лекција

[Образац за вишеструке агенте](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->