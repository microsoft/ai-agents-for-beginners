<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e06d3b5d6207459a019c05fee5eb4b",
  "translation_date": "2025-07-11T14:37:33+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "ru"
}
-->
[![Планирование Дизайна Шаблона](../../../07-planning-design/images/lesson-7-thumbnail.png)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Нажмите на изображение выше, чтобы посмотреть видео этого урока)_

# Планирование Дизайна

## Введение

Этот урок охватывает

* Определение четкой общей цели и разбиение сложной задачи на управляемые задачи.
* Использование структурированного вывода для более надежных и машиночитаемых ответов.
* Применение событийно-ориентированного подхода для обработки динамических задач и неожиданных вводных данных.

## Цели обучения

После завершения этого урока вы будете понимать:

* Как определить и установить общую цель для AI-агента, чтобы он четко знал, что нужно достичь.
* Как разложить сложную задачу на управляемые подзадачи и организовать их в логическую последовательность.
* Как снабдить агентов необходимыми инструментами (например, инструментами поиска или анализа данных), решить, когда и как их использовать, и справляться с неожиданными ситуациями.
* Как оценивать результаты подзадач, измерять производительность и повторять действия для улучшения конечного результата.

## Определение общей цели и разбиение задачи

![Определение целей и задач](../../../07-planning-design/images/defining-goals-tasks.png)

Большинство реальных задач слишком сложны, чтобы справиться с ними за один шаг. AI-агенту нужна краткая цель, чтобы направлять его планирование и действия. Например, рассмотрим цель:

    "Создать 3-дневный план путешествия."

Хотя это просто сформулировать, цель все же нуждается в уточнении. Чем яснее цель, тем лучше агент (и любые человеческие сотрудники) могут сосредоточиться на достижении правильного результата, например, создании комплексного маршрута с вариантами перелетов, рекомендациями по отелям и предложениями по мероприятиям.

### Декомпозиция задачи

Большие или сложные задачи становятся более управляемыми, когда их разбивают на меньшие, ориентированные на цель подзадачи.
Для примера с планом путешествия, вы можете разложить цель на:

* Бронирование авиабилетов
* Бронирование отеля
* Аренда автомобиля
* Персонализация

Каждую подзадачу затем могут выполнять специализированные агенты или процессы. Один агент может специализироваться на поиске лучших предложений на авиабилеты, другой — на бронировании отелей и так далее. Координирующий или "второстепенный" агент затем может собрать эти результаты в один целостный маршрут для конечного пользователя.

Этот модульный подход также позволяет вносить постепенные улучшения. Например, вы можете добавить специализированных агентов для рекомендаций по питанию или местным мероприятиям и со временем уточнять маршрут.

### Структурированный вывод

Большие языковые модели (LLM) могут генерировать структурированный вывод (например, JSON), который легче анализировать и обрабатывать последующим агентам или службам. Это особенно полезно в контексте многоагентной системы, где мы можем выполнять эти задачи после получения результата планирования. Обратитесь к этому
Вы обучены на данных до октября 2023 года для быстрого обзора.

Следующий фрагмент кода на Python демонстрирует простого планирующего агента, разбивающего цель на подзадачи и создающего структурированный план:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
from autogen_ext.models.azure import AzureAIChatCompletionClient
from azure.core.credentials import AzureKeyCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Travel SubTask Model
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # we want to assign the task to the agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

client = AzureAIChatCompletionClient(
    model="gpt-4o-mini",
    endpoint="https://models.inference.ai.azure.com",
    # To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings.
    # Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
    model_info={
        "json_output": False,
        "function_calling": True,
        "vision": True,
        "family": "unknown",
    },
)

# Define the user message
messages = [
    SystemMessage(content="""You are an planner agent.
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
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(
        content="Create a travel plan for a family of 2 kids from Singapore to Melboune", source="user"),
]

response = await client.create(messages=messages, extra_create_args={"response_format": 'json_object'})

response_content: Optional[str] = response.content if isinstance(
    response.content, str) else None
if response_content is None:
    raise ValueError("Response content is not a valid JSON string" )

pprint(json.loads(response_content))

# # Ensure the response content is a valid JSON string before loading it
# response_content: Optional[str] = response.content if isinstance(
#     response.content, str) else None
# if response_content is None:
#     raise ValueError("Response content is not a valid JSON string")

# # Print the response content after loading it as JSON
# pprint(json.loads(response_content))

# Validate the response content with the MathReasoning model
# TravelPlan.model_validate(json.loads(response_content))
```

### Планирующий агент с многоагентной оркестрацией

В этом примере агент Semantic Router получает запрос пользователя (например, "Мне нужен план отеля для моей поездки.").

Планировщик затем:

* Получает план отеля: Планировщик берет сообщение пользователя и, основываясь на системной подсказке (включая доступные данные агентов), генерирует структурированный план путешествия.
* Перечисляет агентов и их инструменты: Реестр агентов содержит список агентов (например, для перелетов, отелей, аренды автомобилей и мероприятий) вместе с функциями или инструментами, которые они предлагают.
* Направляет план соответствующим агентам: В зависимости от количества подзадач планировщик либо отправляет сообщение непосредственно выделенному агенту (для одноцелевых сценариев), либо координирует через менеджера группового чата для многоагентного сотрудничества.
* Резюмирует результат: Наконец, планировщик резюмирует сгенерированный план для ясности.
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

# Travel SubTask Model

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # we want to assign the task to the agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient

# Create the client with type-checked environment variables

client = AzureOpenAIChatCompletionClient(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
)

from pprint import pprint

# Define the user message

messages = [
    SystemMessage(content="""You are an planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(content="Create a travel plan for a family of 2 kids from Singapore to Melbourne", source="user"),
]

response = await client.create(messages=messages, extra_create_args={"response_format": TravelPlan})

# Ensure the response content is a valid JSON string before loading it

response_content: Optional[str] = response.content if isinstance(response.content, str) else None
if response_content is None:
    raise ValueError("Response content is not a valid JSON string")

# Print the response content after loading it as JSON

pprint(json.loads(response_content))
```

Ниже приведен вывод из предыдущего кода, и вы можете использовать этот структурированный вывод для маршрутизации к `assigned_agent` и резюмирования плана путешествия для конечного пользователя.

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

Пример блокнота с предыдущим примером кода доступен [здесь](../../../07-planning-design/07-autogen.ipynb).

### Итеративное планирование

Некоторые задачи требуют обратной связи или перепланирования, когда результат одной подзадачи влияет на следующую. Например, если агент обнаруживает неожиданный формат данных при бронировании авиабилетов, ему может потребоваться адаптировать свою стратегию перед переходом к бронированию отелей.

Кроме того, обратная связь от пользователя (например, человек решает, что предпочитает более ранний рейс) может вызвать частичное перепланирование. Этот динамичный, итеративный подход гарантирует, что конечное решение соответствует реальным ограничениям и изменяющимся предпочтениям пользователя.

например, пример кода

```python
from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
#.. same as previous code and pass on the user history, current plan
messages = [
    SystemMessage(content="""You are a planner agent to optimize the
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(content="Create a travel plan for a family of 2 kids from Singapore to Melbourne", source="user"),
    AssistantMessage(content=f"Previous travel plan - {TravelPlan}", source="assistant")
]
# .. re-plan and send the tasks to respective agents
```

Для более комплексного планирования ознакомьтесь с Magnetic One для решения сложных задач.

## Резюме

В этой статье мы рассмотрели пример того, как мы можем создать планировщик, который может динамически выбирать доступных агентов. Вывод планировщика разбивает задачи и назначает агентов, чтобы они могли быть выполнены. Предполагается, что агенты имеют доступ к функциям/инструментам, необходимым для выполнения задачи. В дополнение к агентам вы можете включить другие шаблоны, такие как рефлексия, резюмирование и круговой чат, для дальнейшей настройки.

## Дополнительные ресурсы

* AutoGen Magentic One - Универсальная многоагентная система для решения сложных задач, которая достигла впечатляющих результатов на множестве сложных агентных тестов. Ссылка: . В этой реализации оркестратор создает план, специфичный для задачи, и делегирует эти задачи доступным агентам. В дополнение к планированию оркестратор также использует механизм отслеживания для мониторинга прогресса задачи и перепланирования по мере необходимости.

## Предыдущий урок

[Создание надежных AI-агентов](../06-building-trustworthy-agents/README.md)

## Следующий урок

[Шаблон многоагентного дизайна](../08-multi-agent/README.md)

**Отказ от ответственности**:  
Этот документ был переведен с помощью службы автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникающие в результате использования этого перевода.