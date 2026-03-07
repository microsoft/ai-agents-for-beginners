[![Planning Design Pattern](../../../translated_images/pcm/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Click di pikshua we dey top to watch video for dis lesson)_

# Planning Design

## Introduction

Dis lesson go cover

* How to define clear overall goal and break big task into small small work wey person fit handle.
* How to use structured output for get correct and machine-readable responses.
* How to use event-driven way to handle tasks wey dey change and sudden inputs.

## Learning Goals

After you finish dis lesson, you go sabi about:

* How to find and set overall goal for AI agent, make e clear so e sabi wetin e suppose achieve.
* How to break big big work into small small task dem wey make sense and arrange dem well well.
* How to give agents correct tools (like search tools or data analytics tools), decide when and how dem go use am, plus how dem go handle sudden wahala.
* How to check how subtasks perform, measure result, plus do am again to improve final outcome.

## Defining the Overall Goal and Breaking Down a Task

![Defining Goals and Tasks](../../../translated_images/pcm/defining-goals-tasks.d70439e19e37c47a.webp)

Plenty tasks for real life too hard to do for one step. AI agent need clear aim to guide how e go plan and do things. For example, make we look di goal:

    "Generate a 3-day travel itinerary."

Even though e simple to talk, e still need to be clear. The more clear the goal, the better the agent (and any human wey dey work together) fit focus to achieve the correct result, like to make complete travel plan with flight options, hotel choice, and things to do.

### Task Decomposition

Big or hard task dem go easier to handle if you divide dem into small small tasks wey get clear goal.
For the travel plan example, you fit break the goal into:

* Flight Booking
* Hotel Booking
* Car Rental
* Personalization

Each small task fit be handle by special agents or processes. One agent fit sabi how to find best flight deals, another one fit handle hotel booking, and so on. One agent go fit put all dis results together into one correct travel plan for the person.

This way we dey do things fit also allow make e improve small small. For example, you fit add special agents for Food Recommendations or Local Activity Suggestions and improve di travel plan with time.

### Structured output

Big Language Models (LLMs) fit give structured output (like JSON) wey easier for other agents or services to understand and process. This one good especially when many agents dey work together, because after planning output don come, we fit take action on the tasks.

Di Python snippet wey follow show how simple planning agent fit break goal into smaller task and make structured plan:

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

# Travel SubTask Model
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # we wan assign di task to di agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Define di user message
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

### Planning Agent with Multi-Agent Orchestration

For dis example, one Semantic Router Agent go receive user request (e.g., "I need a hotel plan for my trip.").

The planner go then:

* Receive the Hotel Plan: The planner go take the user message and, based on system prompt (wey include info of available agents), go make one structured travel plan.
* List Agents and Their Tools: The agent registry get list of agents (like for flight, hotel, car rental, and activities) plus the functions or tools wey dem get.
* Route the Plan to the Respective Agents: Depending on the number of subtasks, the planner fit send the message directly to one special agent (for one-task case) or arrange am via group chat manager for multi-agent teamwork.
* Summarize the Outcome: At last, the planner go summarize the plan to make am clear.
Di Python code wey follow show these steps:

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
    assigned_agent: AgentEnum # we want to assign di task to di agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Make di client

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Define di user message

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

# Print di response content after we load am as JSON

pprint(json.loads(response_content))
```

Wetyn follow after na the output from the code above, and you fit use dis structured output take send to `assigned_agent` and summarize the travel plan to the person wey dey use am.

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

One example notebook with the Python code way I talk about before dey available [here](07-python-agent-framework.ipynb).

### Iterative Planning

Some task need to do back-and-forth or re-planning, where the result of one subtask fit affect the next one. For example, if agent find strange data format while e dey book flight, e fit need change im plan before e begin book hotel.

Also, if user talk (like person say e want earlier flight), e fit make agent do small re-plan. This kind dynamic, iterative plan make sure final answer fit the real-life condition and change as user preference change.

e.g sample code

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. same like di previous code and carry di user history, current plan go

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
# .. re-plan and send di tasks go di correct agents dem
```

For better planning, check Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> wey dey talk about how to solve complex task.

## Summary

For dis article, we don see example how we fit make planner wey fit choose agents wey dey available. The planner output break task into smaller task and assign agents make dem do am. We assume say agents fit get the functions/tools wey dem need to perform the task. Besides the agents, you fit also add other patterns like reflection, summarizer, and round robin chat to customize more.

## Additional Resources

Magentic One - Na generalist multi-agent system to solve big big task and e don do well for many tough agentic benchmarks. Reference: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. For this implementation, the orchestrator dey create task-specific plans and dey assign these task to available agents. Besides planning, the orchestrator also get tracking mechanism to follow how the task dey go and e dey re-plan if e need.

### Got More Questions about the Planning Design Pattern?

Join [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet other learners, attend office hours and clear your AI Agents questions.

## Previous Lesson

[Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)

## Next Lesson

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis dokument don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we try make am correct, abeg sabi say automated translation fit get errors or mistakes. Di original dokument wey dem write for e own language na di real correct one. If na serious matter, make you use professional human translation. We no go carry last if any misunderstanding or mix-up happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->