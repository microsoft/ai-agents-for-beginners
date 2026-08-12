[![Паттерн проектирования планирования](../../../translated_images/ru/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Нажмите на изображение выше, чтобы посмотреть видео этого урока)_

# Проектирование Планирования

## Введение

В этом уроке будет рассмотрено

* Определение чёткой общей цели и разбиение сложной задачи на управляемые подзадачи.
* Использование структурированного вывода для более надёжных и машинно-читаемых ответов.
* Применение событийно-ориентированного подхода для обработки динамических задач и неожиданных вводов.

## Цели обучения

После завершения этого урока вы будете понимать:

* Как определить и установить общую цель для ИИ-агента, чтобы он чётко понимал, что нужно достичь.
* Как разложить сложную задачу на управляемые подзадачи и организовать их в логическую последовательность.
* Как оснащать агентов правильными инструментами (например, поисковыми или аналитическими), решать, когда и как их использовать, а также справляться с неожиданными ситуациями.
* Как оценивать результаты подзадач, измерять эффективность и повторять действия для улучшения итогового результата.

## Определение общей цели и разбиение задачи

![Определение целей и задач](../../../translated_images/ru/defining-goals-tasks.d70439e19e37c47a.webp)

Большинство реальных задач слишком сложны, чтобы решать их за один шаг. Для ИИ-агента нужна чёткая цель, которая направляет его планирование и действия. Например, рассмотрим цель:

    "Создать маршрут путешествия на 3 дня."

Хотя это просто заявление, его всё же нужно уточнить. Чем яснее цель, тем лучше агент (и любые участвующие люди) смогут сосредоточиться на достижении правильного результата, например создание комплексного маршрута с вариантами перелётов, рекомендациями отелей и предложениями активностей.

### Декомпозиция задачи

Большие или сложные задачи становятся более управляемыми, когда их разбивают на меньшие, ориентированные на цель подзадачи.
Для примера маршрута путешествия можно разложить цель на:

* Бронирование авиабилетов
* Бронирование отеля
* Аренда автомобиля
* Персонализация

Затем каждая подзадача может обрабатываться выделенными агентами или процессами. Один агент может специализироваться на поиске лучших авиарейсов, другой — на бронировании отелей и т.д. Координирующий или «следующий» агент может затем собрать эти результаты в единый связный маршрут для конечного пользователя.

Такой модульный подход также позволяет поэтапно улучшать систему. Например, можно добавить специализированных агентов для рекомендаций по еде или местным развлечениям и со временем улучшать маршрут.

### Структурированный вывод

Большие языковые модели (LLM) могут генерировать структурированный вывод (например, JSON), который легче парсить и обрабатывать следующим агентам или сервисам. Это особенно полезно в контексте мультиагентной системы, где можно выполнять задачи после получения плана.

Следующий фрагмент Python демонстрирует простого агента планирования, который разлагает цель на подзадачи и генерирует структурированный план:

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

# Модель подзадачи путешествия
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # мы хотим назначить задачу агенту

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Определить сообщение пользователя
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

### Агент планирования с мультиагентной оркестрацией

В этом примере Semantiс Router Agent получает запрос от пользователя (например, «Мне нужен план отеля для моей поездки.»).

Планировщик затем:

* Получает план отеля: планировщик берёт сообщение пользователя и, основываясь на системном запросе (включая детали доступных агентов), генерирует структурированный план поездки.
* Составляет список агентов и их инструментов: реестр агентов содержит список агентов (например, для авиабилетов, отелей, аренды автомобилей и активностей) вместе с предлагаемыми функциями или инструментами.
* Направляет план соответствующим агентам: в зависимости от количества подзадач планировщик либо отправляет сообщение напрямую выделенному агенту (для одиночных задач), либо координирует через менеджер группового чата для сотрудничества нескольких агентов.
* Резюмирует результат: в конце планировщик подводит итог сгенерированного плана для ясности.
Следующий пример кода на Python иллюстрирует эти шаги:

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

# Модель подзадачи путешествия

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # мы хотим назначить задачу агенту

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Создать клиента

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

from pprint import pprint

# Определить сообщение пользователя

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

# Вывести содержимое ответа после загрузки его как JSON

pprint(json.loads(response_content))
```

Далее приведён вывод с предыдущего кода, и вы можете использовать этот структурированный вывод для передачи `assigned_agent` и подведения итогов плана поездки конечному пользователю.

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

Пример ноутбука с предыдущим кодом доступен [здесь](./code_samples/07-python-agent-framework.ipynb).

### Итеративное планирование

Некоторые задачи требуют взаимодействия или перепланирования, когда результат одной подзадачи влияет на следующую. Например, если агент обнаруживает неожиданный формат данных при бронировании авиабилетов, ему может понадобиться адаптировать стратегию перед тем, как продолжить с бронированием отеля.

Кроме того, обратная связь пользователя (например, если человек решает, что предпочитает более ранний рейс) может вызвать частичное перепланирование. Такой динамичный итеративный подход гарантирует, что итоговое решение соответствует реальным ограничениям и изменяющимся предпочтениям пользователя.

например, исходный код

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. то же, что и в предыдущем коде, и передать историю пользователя, текущий план

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
# .. перепланировать и отправить задачи соответствующим агентам
```

Для более комплексного планирования ознакомьтесь с Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> для решения сложных задач.

## Резюме

В этой статье мы рассмотрели пример, как можно создать планировщика, который динамически выбирает доступных агентов. Вывод планировщика разбивает задачи и назначает агентов для их выполнения. Предполагается, что агенты имеют доступ к необходимым функциям/инструментам для выполнения задачи. Дополнительно можно использовать другие паттерны, такие как рефлексия, суммаризатор и круговой чат, для дальнейшей настройки.

## Дополнительные ресурсы

Magnetic One — универсальная мультиагентная система для решения сложных задач, которая достигла впечатляющих результатов на нескольких сложных агентных тестах. Ссылка: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. В этой реализации оркестратор создаёт специфичные для задач планы и делегирует их доступным агентам. Помимо планирования оркестратор использует механизм отслеживания прогресса задачи и перепланирует по мере необходимости.

### Хотите узнать больше о паттерне проектирования планирования?

Присоединяйтесь к [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), чтобы встретиться с другими обучающимися, посетить часы работы и получить ответы на вопросы по ИИ-агентам.

## Предыдущий урок

[Создание надёжных ИИ-агентов](../06-building-trustworthy-agents/README.md)

## Следующий урок

[Паттерн проектирования мультиагентов](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->