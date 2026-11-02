[![Planning Design Pattern](../../../translated_images/kn/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(ಈ ಪಾಠದ ವಿಡಿಯೋವನ್ನು ವೀಕ್ಷಿಸಲು ಮೇಲಿನ ಚಿತ್ರವನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ)_

# ಯೋಜನೆ ವಿನ್ಯಾಸ

## ಪರಿಚಯ

ಈ ಪಾಠವು ಒಳಗೊಂಡಿದೆ

* ಸ್ಪಷ್ಟ ಒಟ್ಟು ಗುರಿಯನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುವುದು ಮತ್ತು ಸಂಕೀರ್ಣ ಕಾರ್ಯವನ್ನು ನಿರ್ವಹಿಸಲು ಸಾಧ್ಯವಾದ ಕಾರ್ಯಗಳಲ್ಲಿ ಭಜಿಸುವುದು.
* ಹೆಚ್ಚಿನ ನಂಬಿಗಸ್ತ ಮತ್ತು ಯಂತ್ರ ಓದಲು ಸಾಧ್ಯವಿರುವ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ಪಡೆಯಲು ಸಂಘಟಿತ ಔಟ್‌ಪುಟ್ ಬಳಸುವುದು.
* ಡೈನಾಮಿಕ್ ಕಾರ್ಯಗಳು ಮತ್ತು ಅನಿರೀಕ್ಷಿತ ಇನ್‌ಪುಟ್‌ಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಘಟನಾ-ಚಾಲಿತ ವಿಧಾನವನ್ನು ಅನ್ವಯಿಸುವುದು.

## ಕಲಿಕೆಯ ಗುರಿಗಳು

ಈ ಪಾಠವನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನೀವು ಈ ವಿಷಯಗಳ ಮೇಲೆ ಅರಿವು ಹೊಂದಿರುತ್ತೀರಿ:

* ಎಐ ಏಜೆಂಟ್‌ಗೆ ಒಟ್ಟು ಗುರಿಯನ್ನು ಗುರುತಿಸಿ ಹಾಗೂ ಅದನ್ನು ಸ್ಪಷ್ಟವಾಗಿ ಏನು ಸಾಧಿಸಬೇಕೆಂದು ತಿಳಿದುಕೊಳ್ಳುವಂತೆ ಇರಿಸಲು ನಿರ್ಧರಿಸಿ.
* ಸಂಕೀರ್ಣ ಕಾರ್ಯವನ್ನು ನಿರ್ವಹಿಸಲು ಸಾಧ್ಯವಾದ ಉಪಕಾರ್ಯಗಳಾಗಿ ವಿಭಜಿಸಿ ಹಾಗೂ ಅವುಗಳನ್ನು ತಾರ್ಕಿಕ ಕ್ರಮದಲ್ಲಿ ಸಂಘಟಿಸಿ.
* ಏಜೆಂಟ್‌ಗಳಿಗೆ ಸರಿಯಾದ ಉಪಕರಣಗಳನ್ನು (ಉದಾಹರಣೆಗೆ, ಹುಡುಕಾಟ ಉಪಕರಣಗಳು ಅಥವಾ ಡೇಟಾ ವಿಶ್ಲೇಷಣೆ ಉಪಕರಣಗಳು) ಒದಗಿಸಿ, ಅವುಗಳನ್ನು ಯಾವಾಗ ಮತ್ತು ಹೇಗೆ ಬಳಸಬೇಕು ಎಂದು ತೀರ್ಮಾನಿಸಿ, ಮತ್ತು ಉಂಟಾಗುವ ಅನಿರೀಕ್ಷಿತ ಪರಿಸ್ಥಿತಿಗಳನ್ನು ನಿರ್ವಹಿಸಿ.
* ಉಪಕಾರ್ಯಗಳ ಫಲಿತಾಂಶಗಳನ್ನು ಮೌಲ್ಯಮಾಪನ ಮಾಡಿ, ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಅಳತೆ ಮಾಡಿ, ಮತ್ತು ಚದರಿಸಿದ ಕ್ರಿಯೆಗಳೊಂದಿಗೆ ಅಂತಿಮ ಔಟ್‌ಪುಟ್ ಉತ್ತಮಗೊಳಿಸಿ.

## ಒಟ್ಟು ಗುರಿಯನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುವುದು ಮತ್ತು ಕಾರ್ಯವನ್ನು ಬರೆಹವಾಗಿ ವಿಭಜಿಸುವುದು

![Defining Goals and Tasks](../../../translated_images/kn/defining-goals-tasks.d70439e19e37c47a.webp)

ಬಹುತೇಕ ನಿಜ ಜೀವನದ ಕಾರ್ಯಗಳು ಒಂದು ಹಂತದಲ್ಲಿ ನಿಭಾಯಿಸಲು ತುಂಬಾ ಸಂಕೀರ್ಣವಾಗಿವೆ. ಏಐ ಏಜೆಂಟ್‌ಗೆ ತನ್ನ ಯೋಜನೆ ಮತ್ತು ಕಾರ್ಯಗಳನ್ನು ಮಾರ್ಗದರ್ಶನ ಮಾಡಲು ಸಂಕ್ಷಿಪ್ತ ಗುರಿಯ ಅಗತ್ಯವಿದೆ. ಉದಾಹರಣೆಗೆ, ಗುರಿ ಪರಿಗಣಿಸಿ:

    "3-ದಿನಗಳ ಪ್ರಯಾಣ ಯೋಜನೆಯನ್ನು ರಚಿಸಿ."

ಇದನ್ನು ಹೇಳುವುದೆಂದರೆ ಸರಳವಾಗಿದೆ, ಆದರೆ ಇನ್ನೂ ಸುಧಾರಣೆ ಅಗತ್ಯವಿದೆ. ಗುರಿ ಸ್ಪಷ್ಟವಾಗಿದ್ದರೆ, ಏಜೆಂಟ್ (ಮತ್ತು ಯಾವುದೇ ಮಾನವ ಸಹಯೋಗಿಗಳು) ಸರಿಯಾದ ಫಲಿತಾಂಶವನ್ನು ಸಾಧಿಸಲು ಹೆಚ್ಚು ಗಮನ ಹರಿಸಬಹುದು, ಉದಾಹರಣೆಗೆ ವಿಮಾನ ಆಯ್ಕೆ, ಹೋಟೆಲ್ ಶಿಫಾರಸುಗಳು ಮತ್ತು ಚಟುವಟಿಕೆಯ ಸಲಹೆಗಳೊಂದಿಗೆ ವಿಮರ್ಶಿತ ಪ್ರಯಾಣ ಯೋಜನೆಯನ್ನು ಸೃಷ್ಟಿಸುವುದು.

### ಕಾರ್ಯ ವಿಭಜನೆ

ದೊಡ್ಡ ಅಥವಾ ಜಟಿಲ ಕಾರ್ಯಗಳು ಸಣ್ಣ, ಗುರಿ-ಮುಖಿವಾದ ಉಪಕಾರ್ಯಗಳಾಗಿ ವಿಭಜಿಸುವಾಗ ನಿರ್ವಹಿಸಲು ಸುಲಭವಾಗುತ್ತವೆ.
ಪ್ರಯಾಣ ಯೋಜನೆಯ ಉದಾಹರಣೆಗೆ, ನೀವು ಗುರಿಯನ್ನು ಈ ಕೆಳಗಿನ ಉಪಕಾರ್ಯಗಳಾಗಿ ವಿಭಜಿಸಬಹುದು:

* ವಿಮಾನ ಬುಕ್ಕಿಂಗ್
* ಹೋಟೆಲ್ ಬುಕ್ಕಿಂಗ್
* ಕಾರು ಬಾಡಿಗೆ
* ವೈಯಕ್ತೀಕರಣ

ಪ್ರತಿಯೊಂದು ಉಪಕಾರ್ಯವನ್ನು ನಿಬಂಧಿತ ಏಜೆಂಟುಗಳು ಅಥವಾ ಪ್ರಕ್ರಿಯೆಗಳು ನಿಭಾಯಿಸಬಹುದು. ಒಬ್ಬ ಏಜೆಂಟ್ ಉತ್ತಮ ವಿಮಾನ ಡೀಲ್ಗಳಿಗಾಗಿ ಹುಡುಕುವಲ್ಲಿ ಪರಿಣತಿ ಹೊಂದಿರಬಹುದು, ಇನ್ನೊಬ್ಬ ಹೋಟೆಲ್ ಬುಕ್ಕಿಂಗ್‌ಗಳನ್ನು ಗಮನಿಸುತ್ತದೆ, ಮತ್ತು ಹೀಗೇ ಮುಂದಾಗಿದೆ. ಸಮನ್ವಯ ಅಥವಾ "ಡೌನ್ ಸ್ಟ್ರೀಮ್" ಏಜೆಂಟ್ ನಂತರ ಈ ಫಲಿತಾಂಶಗಳನ್ನು ಒಟ್ಟುಗೂಡಿಸಿ, ಅಂತಿಮ ಬಳಕೆದಾರರಿಗೆ ಒಕ್ಕೂಟ ರೀತಿಯ ಪ್ರಯಾಣ ಯೋಜನೆಯನ್ನು ನೀಡಬಹುದು.

ಈ ಘಟಕೀಕೃತ ವಿಧಾನವು ಕ್ರಮೇಣ ಸುಧಾರಣೆಗಳನ್ನು ಅನುಮತಿಸುತ್ತದೆ. ಉದಾಹರಣೆಗೆ, ಆಹಾರ ಶಿಫಾರಸುಗಳು ಅಥವಾ ಸ್ಥಳೀಯ ಚಟುವಟಿಕೆ ಸಲಹೆಗಳಿಗಾಗಿ ವಿಶೇಷ ಏಜೆಂಟ್‌ಗಳನ್ನು ಸೇರಿಸಬಹುದು ಮತ್ತು ಕಾಲಕ್ರಮೇಣ ಯೋಜನೆಯನ್ನು ಸುಧಾರಿಸಬಹುದು.

### ಸಂಘಟಿತ ಔಟ್‌ಪುಟ್

ದೊಡ್ಡ ಭಾಷಾ ಮಾದರಿಗಳು (LLMs) downstream ಏಜೆಂಟ್‌ಗಳು ಅಥವಾ ಸೇವೆಗಳಿಗಾಗಿ ಸುಲಭವಾಗಿ ಪಾರ್ಸ್ ಮತ್ತು ಪ್ರಕ್ರಿಯೆ ಮಾಡಲು ಸಾಧ್ಯವಾದ JSON-ಸ್ಟೈಲ್ ಸಂಘಟಿತ ಔಟ್‌ಪುಟ್ ರಚಿಸಬಹುದು. ಇದು ಬಹು-ಏಜೆಂಟ್ ಸಂತೋಷದಲ್ಲಿ ಬಹಳ ಉಪಯುಕ್ತವಾಗಿದೆ, ಇಲ್ಲಿ ನಾವು ಯೋಜನಾ ಔಟ್‌ಪುಟ್ ಪಡೆದ ನಂತರ ಈ ಕಾರ್ಯಗಳನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಬಹುದು.

ಕೆಳಗಿನ ಪೈಥಾನ್ ಸ್ನಿಪೆಟ್ ಗುರಿಯನ್ನು ಉಪಕಾರ್ಯಗಳಾಗಿ ವಿಭಜಿಸುವ ಮತ್ತು ಸಂಘಟಿತ ಯೋಜನೆಯನ್ನು ರಚಿಸುವ ಸರಳ ಯೋಜನಾ ಏಜೆಂಟನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತದೆ:

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

# ಪ್ರಯಾಣ ಉಪಕಾರ್ಯ ಮಾದರಿ
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # ನಮಗೆ ಕಾರ್ಯವನ್ನು ಏಜೆಂಟ್‌ಗೆ ನಿಯೋಜಿಸಲು ಇಚ్ఛೆ ಇದೆ

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# ಬಳಕೆದಾರ ಸಂದೇಶವನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ
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

### ಬಹು-ಏಜೆಂಟ್ ವ್ಯವಸ್ಥಾಪನೆಯೊಂದಿಗೆ ಯೋಜನಾ ಏಜೆಂಟ್

ಈ ಉದಾಹರಣೆಯಲ್ಲಿ, ಸಿಮೆಂಟಿಕ್ ರೂಟರ್ ಏಜೆಂಟ್ ಬಳಕೆದಾರ ವಿನಂತಿಯನ್ನು (ಉದಾ., "ನನಗೆ ನನ್ನ ಪ್ರವಾಸಕ್ಕೆ ಹೋಟೆಲ್ ಯೋಜನೆ ಬೇಕು.") ಸ್ವೀಕರಿಸುತ್ತದೆ.

ನಂತರ ಯೋಜಕ:

* ಹೋಟೆಲ್ ಯೋಜನೆಯನ್ನು ಸ್ವೀಕರಿಸುತ್ತದೆ: ಬಳಕೆದಾರ ಸಂದೇಶವನ್ನು ಮತ್ತು ಲಭ್ಯವಿರುವ ಏಜೆಂಟ್ ವಿವರಣೆಗಳನ್ನು ಒಳಗೊಂಡಿರುವ ಸಿಸ್ಟಮ್ ಪ್ರಾಂಪ್ಟ್ ಆಧಾರದಲ್ಲಿ, ಯೋಜಕ ಸಂಘಟಿತ ಪ್ರಯಾಣ ಯೋಜನೆಯನ್ನು ರಚಿಸುತ್ತದೆ.
* ಏಜೆಂಟ್‌ಗಳು ಮತ್ತು ಅವುಗಳ ಉಪಕರಣಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುತ್ತದೆ: ಏಜೆಂಟ್ ರೆಜಿಸ್ಟ್ರಿ ವಿಮಾನ, ಹೋಟೆಲ್, ಕಾರು ಬಾಡಿಗೆ ಮತ್ತು ಚಟುವಟಿಕೆಗಳಿಗೆ ಸಂಬಂಧಿಸಿದ ಏಜೆಂಟ್‌ಗಳ ಪಟ್ಟಿ ಮತ್ತು ಅವರು ಒದಗಿಸುವ ಕಾರ್ಯಗಳು ಅಥವಾ ಉಪಕರಣಗಳನ್ನೊಳಗೊಂಡಿದೆ.
* ಯೋಜನೆಯನ್ನು ಕ್ರಮಾಂಕದ ಏಜೆಂಟ್‌ಗಳಿಗೆ ಮಾರ್ಗದರ್ಶನ ಮಾಡುತ್ತದೆ: ಉಪಕಾರ್ಯದ ಸಂಖ್ಯೆ ಆಧರಿಸಿ, ಯೋಜಕ ಸಂದೇಶವನ್ನು ನೇರವಾಗಿ ನಿರ್ದಿಷ್ಟ ಏಜೆಂಟ್‌ಗೆ ಕಳುಹಿಸುತ್ತದೆ (ಒಂದು ಕಾರ್ಯದ ಸಂದರ್ಭಗಳಲ್ಲಿ) ಅಥವಾ ಬಹು-ಏಜೆಂಟ್ ಸಹಕಾರಕ್ಕಾಗಿ ಗುಂಪು ಚಾಟ್ ನಿರ್ವಾಹಕ ಮೂಲಕ ಸಂಯೋಜಿಸುತ್ತದೆ.
* ಫಲಿತಾಂಶ ಸಂಕ್ಷಿಪ್ತವನ್ನು ಒದಗಿಸುತ್ತದೆ: ಕೊನೆಗೆ, ಯೋಜಕ ಸರ್ಷಿಪ್ತಗೊಳಿಸಿದ ಯೋಜನೆಯನ್ನು ಸ್ಪಷ್ಟತೆಗಾಗಿ ಒದಗಿಸುತ್ತದೆ.
ಕೆಳಗಿನ ಪೈಥಾನ್ ಕೋಡ್ ಉದಾಹರಣೆ ಈ ಹಂತಗಳನ್ನು ತೋರಿಸುತ್ತದೆ:

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

# ಪ್ರಯಾಣ ಉಪಕಾರ್ಯ ಮಾದರಿ

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # ನಾವು ಟಾಸ್ಕ್ ಅನ್ನು ಏಜೆಂಟ್ ಗೆ ನೀಡಲು ಬಯಸುತ್ತೇವೆ

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# ಗ್ರಾಹಕನನ್ನು ರಚಿಸಿ

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

from pprint import pprint

# ಬಳಕೆದಾರ ಸಂದೇಶವನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ

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

# JSON ಆಗಿ ಲೋಡ್ ಮಾಡಿದ ನಂತರ ಪ್ರತಿಕ್ರಿಯೆಯ ವಿಷಯವನ್ನು ಮುದ್ರಿಸಿ

pprint(json.loads(response_content))
```

ಮುಂದಿನ ವಿವರವು ಹಿಂದಿನ ಕೋಡ್‌ನ ಔಟ್‌ಪುಟ್ ಆಗಿದ್ದು ನಂತರ ನೀವು ಈ ಸಂಘಟಿತ ಔಟ್‌ಪುಟ್ ಅನ್ನು `assigned_agent` ಗೆ ಮಾರ್ಗದರ್ಶನ ಮಾಡಲು ಮತ್ತು ಪ್ರಯಾಣದ ಯೋಜನೆಯನ್ನು ಅಂತಿಮ ಬಳಕೆದಾರರಿಗೆ ಸಾರಾಂಶ ಮಾಡಬಹುದು.

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

ಹಿಂದಿನ ಕೋಡ್ ಉದಾಹರಣೆಯೊಂದಿಗೆ ಒಂದು ನೋಟ್ಬುಕ್ [ಇಲ್ಲಿ](./code_samples/07-python-agent-framework.ipynb) ಲಭ್ಯವಿದೆ.

### ಇಟರೇಟಿವ್ ಯೋಜನೆ

ಕೆಲವು ಕಾರ್ಯಗಳು ಒಂದರಿಂದ ಮತ್ತೊಂದಕ್ಕೆ ಫಲಿತಾಂಶ ಪ್ರಭಾವ ಬೀರುವಂತಾದ ಹಿಂತಿರುಗುವ ಅಥವಾ ಪುನರಾಯೋಜನೆಯ ಅಗತ್ಯವಿರಬಹುದು. ಉದಾಹರಣೆಗೆ, ಏಜೆಂಟ್ ವಿಮಾನ ಬುಕ್ಕಿಂಗ್ ಮಾಡಲು ಪ್ರಯತ್ನಿಸುವಾಗ ಅನಿರೀಕ್ಷಿತ ಡೇಟಾ ಫಾರ್ಮ್ಯಾಟ್ ಕಂಡುಹಿಡಿದರೆ, ಅದು ಹೋಟೆಲ್ ಬುಕ್ಕಿಂಗ್‌ಗೆ ಮುಂದಾಗುವುದಕ್ಕೆ ಮುಂಚೆ ತನ್ನ ತಂತ್ರವನ್ನು ಹೊಂದಿಕೊಳ್ಳಬೇಕು.

ಜೊತೆಗೆ, ಬಳಕೆದಾರ ಪ್ರತಿಕ್ರಿಯೆ (ಉದಾ., ಮಾನವನು ಬೇಗಗಿನ ವಿಮಾನವನ್ನು ಆಯ್ಕೆಮಾಡಬೇಕೆಂದು ನಿರ್ಧರಿಸಿ) ಭಾಗಶಃ ಪುನರಾಯೋಜನೆಯನ್ನು ಪ್ರೇರೇಪಿಸಬಹುದು. ಈ ಡೈನಾಮಿಕ್, ಇಟರೇಟಿವ್ ವಿಧಾನವು ಅಂತಿಮ ಪರಿಹಾರವು ನಿಜ ಜೀವನದ ನಿಯಮಗಳು ಮತ್ತು ಬದಲಾಗುತ್ತಿರುವ ಬಳಕೆದಾರ priya ತೃಪ್ತತೆಗಳಿಗೆ ಹೊಂದಿಕೆಯಾಗುವಂತೆ ಮಾಡುತ್ತದೆ.

ಉದಾಹರಣಾ ಕೋಡ್

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. ಮುಂಚಿನ ಕೋಡ್‌ನಂತೆ ಮತ್ತು ಬಳಕೆದಾರರ ಇತಿಹಾಸ, ಪ್ರಸ್ತುತ ಯೋಜನೆಯನ್ನು ಮುಂದುವರೆಸಿರಿ

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
# .. ಮರು-ಯೋಜನೆ ಮಾಡಿ ಹಾಗೂ ಕಾರ್ಯಗಳನ್ನು ಪ್ರತ್ಯೇಕ ಏಜೆಂಟ್‌ಗಳಿಗೆ ಕಳುಹಿಸಿ
```

ಹೆಚ್ಚಿನ ಸಮಗ್ರ ಯೋಜನೆಗಾಗಿ ನಿಮ್ಮ ಪರಿಶೀಲನೆಗೆ Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">ಬ್ಲಾಗ್‌ಪೋಸ್ಟ್</a> ನೋಡಿ, ಇದು ಸಂಕೀರ್ಣ ಕಾರ್ಯಗಳನ್ನು ಪರಿಹರಿಸಲು ಒಂದು ಸಾಮಾನ್ಯ ಬಹು-ಏಜೆಂಟ್ ವ್ಯವಸ್ಥೆಯಾಗಿದೆ.

## ಸಾರಾಂಶ

ಈ ಲೇಖನದಲ್ಲಿ ನಾವು ಹೇಗೆ ಲಭ್ಯವಿರುವ ಏಜೆಂಟ್‌ಗಳನ್ನು ಡೈನಾಮಿಕ್ ಆಗಿ ಆಯ್ಕೆಮಾಡುವ ಯೋಜಕವನ್ನು ರಚಿಸಬಹುದು ಎಂಬುದರ ಉದಾಹರಣೆಯನ್ನು ನೋಡಿದೆವು. ಯೋಜಕದ ಔಟ್‌ಪುಟ್ ಕಾರ್ಯಗಳನ್ನು ವಿಭಜಿಸಿ ಅವುಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಏಜೆಂಟ್‌ಗಳಿಗೆ ಕೊಡುಗೆ ಮಾಡುತ್ತದೆ. ಕಾರ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಅಗತ್ಯವಿರುವ ಕಾರ್ಯಗಳು/ಪರಿಕರಗಳು ಏಜೆಂಟ್‌ಗಳ ಬಳಿ ಹೊಂದಿರುವ ನಿರೀಕ್ಷೆಯಿದೆ. ಏಜೆಂಟ್‌ಗಳ ಜೊತೆಗೆ, ಪ್ರತಿಬಿಂಬ, ಸಾರಾಂಶ ಕಾರಕ ಮತ್ತು ರೌಂಡ್ ರಾಬಿನ್ ಚಾಟ್ ಸೇರಿದಂತೆ ಇತರೆ ಮಾದರಿಗಳನ್ನು ಸೇರಿಸಿ ಹೆಚ್ಚಿನ ವೈಯಕ್ತೀಕರಣ ಮಾಡಬಹುದು.

## ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

Magnetic One - ಸಂಕೀರ್ಣ ಕಾರ್ಯಗಳನ್ನು ಪರಿಹರಿಸಲು ಸಾಮಾನ್ಯ ಬಹು-ಏಜೆಂಟ್ ವ್ಯವಸ್ಥೆ ಮತ್ತು ಅನೇಕ ಸವಾಲಿನ ಏಜೆಂಟ್ ಬೆಂಚ್‌ಮಾರ್ಕ್‌ಗಳಲ್ಲಿ ಸಾಧನೆಯನ್ನು ಸಾಧಿಸಿದೆ. ಉಲ್ಲೇಖ: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. ಈ ಅನುಷ್ಠಾನದಲ್ಲಿ ವ್ಯವಸ್ಥಾಪಕ ಕಾರ್ಯವಿಶೇಷ ಯೋಜನೆಗಳನ್ನು ಸೃಷ್ಟಿಸಿ ಲಭ್ಯವಿರುವ ಏಜೆಂಟ್‌ಗಳಿಗೆ ಆ ಕಾರ್ಯಗಳನ್ನು ನಿಯೋಜಿಸುತ್ತದೆ. ಯೋಜನೆಗೆ ಜೊತೆಗೆ, ವ್ಯವಸ್ಥಾಪಕ ಕಾರ್ಯದ ಪ್ರಗತಿಯನ್ನು מעקב ಮಾಡಲು ಟ್ರ್ಯಾಕಿಂಗ್ ವ್ಯವಸ್ಥೆಯನ್ನು ಉಪಯೋಗಿಸುತ್ತಾನೆ ಮತ್ತು ಅಗತ್ಯವಿದ್ದಲ್ಲಿ ಪುನರಾಯೋಜನೆ ಮಾಡುತ್ತಾನೆ.

### ಯೋಜನೆ ವಿನ್ಯಾಸ ಮಾದರಿಯ ಬಗ್ಗೆ ಇನ್ನಷ್ಟು ಪ್ರಶ್ನೆಗಳಿವೆಯಾ?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) ಸೇರಿ, ಇತರ ಕಲಿಕೆದಾರರೊಂದಿಗೆ ಭೇಟಿಯಾಗಲು, ಕಚೇರಿ ಸಮಯಗಳಲ್ಲಿ ಭಾಗವಹಿಸಲು ಮತ್ತು ನಿಮ್ಮ ಎಐ ಏಜೆಂಟ್ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರ ಪಡೆಯಿರಿ.

## ಹಿಂದಿನ ಪಾಠ

[ನಂಬಲಾಯಕ ಏಜೆಂಟ್‌ಗಳ ನಿರ್ಮಾಣ](../06-building-trustworthy-agents/README.md)

## ಮುಂದಿನ ಪಾಠ

[ಬಹು-ಏಜೆಂಟ್ ವಿನ್ಯಾಸ ಮಾದರಿ](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->