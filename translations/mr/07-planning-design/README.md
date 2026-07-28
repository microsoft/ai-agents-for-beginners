[![Planning Design Pattern](../../../translated_images/mr/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(या धड्याच्या व्हिडिओसाठी वरील प्रतिमा क्लिक करा)_

# नियोजन डिझाइन

## परिचय

हा धडा पुढील गोष्टींचा आढावा घेतो

* एक स्पष्ट एकूण उद्दिष्ट निश्चित करणे आणि जटिल कामे व्यवस्थापनीय कार्यांमध्ये विभाजित करणे.
* अधिक विश्वसनीय आणि मशीन-वाचनीय प्रतिसादांसाठी संरचित आउटपुटचा वापर करणे.
* गतिशील कार्ये आणि अनपेक्षित इनपुट्स हाताळण्यासाठी इव्हेंट-चालित दृष्टिकोन लागू करणे.

## शिकण्याचे उद्दिष्ट

हा धडा पूर्ण केल्यानंतर, आपल्याला खालील बाबींचा समज असेल:

* AI एजंटसाठी एकूण उद्दिष्ट ओळखणे आणि सेट करणे, ज्यामुळे एजंटला स्पष्टपणे काय साध्य करायचे आहे ते माहीत असेल.
* जटिल कार्य व्यवस्थापनीय उपकार्यांमध्ये decomposition करणे आणि त्यांना तार्किक क्रमाने आयोजित करणे.
* एजंट्सना योग्य उपकरणे (उदा. शोध उपकरणे किंवा डेटा विश्लेषण उपकरणे) देणे, ते कधी आणि कसे वापरायचे ठरवणे आणि अनपेक्षित परिस्थिती हाताळणे.
* उपकार्यांचे निकाल मोजणे, कामगिरीचे मूल्यांकन करणे आणि अंतिम आउटपुट सुधारण्यासाठी क्रिया पुनःआकलन करणे.

## एकूण उद्दिष्ट निश्चित करणे आणि कार्य decomposition करणे

![Defining Goals and Tasks](../../../translated_images/mr/defining-goals-tasks.d70439e19e37c47a.webp)

बहुतेक प्रत्यक्ष कामे एकाच टप्प्यात हाताळणे खूप जटिल असतात. AI एजंटला त्याच्या नियोजन आणि कृतींसाठी एक संक्षिप्त उद्दिष्ट हवा असतो. उदाहरणादाखल, हे उद्दिष्ट विचार करा:

    "3 दिवसांच्या प्रवासाचा आराखडा तयार करा."

जरी हे उद्दिष्ट सोपे वाटत असले तरी, त्याला अजून सुधारणा करण्याची गरज आहे. जितके स्पष्ट उद्दिष्ट असेल, तितके एजंट (आणि मनुष्य सहकारी) योग्य निकाल साध्य करण्यावर अधिक लक्ष केंद्रित करू शकतील, जसे की व्यापक आराखडा ज्यामध्ये फ्लाइट पर्याय, हॉटेल शिफारसी आणि क्रियाकलापांची सुचना असते.

### कार्य decomposition

मोठी किंवा गुंतागुंतीची कामे लहान, उद्दिष्टवादी उपकार्यांमध्ये विभागल्यास ती अधिक व्यवस्थापनीय बनतात.
प्रवास आराखड्याच्या उदाहरणासाठी, उद्दिष्ट खालीलप्रमाणे decomposition करू शकता:

* फ्लाइट बुकिंग
* हॉटेल बुकिंग
* कार भाड्याने घेणे
* वैयक्तिकरण

प्रत्येक उपकार्य वेगळ्या एजंट्स किंवा प्रक्रियांद्वारे हाताळले जाऊ शकते. एक एजंट सर्वोत्तम फ्लाइट डील शोधण्यात तज्ज्ञ असू शकतो, दुसरा हॉटेल बुकिंगवर लक्ष केंद्रित करेल, इत्यादी. एक समन्वयक किंवा "डाउनस्ट्रीम" एजंट नंतर हे परिणाम एकत्र करून अंतिम वापरकर्त्यासाठी एक संयुक्त आराखडा तयार करेल.

हा मॉड्युलर दृष्टिकोन हळूहळू सुधारणा करण्यास अनुमती देखील देतो. उदाहरणार्थ, तुम्ही खाद्य शिफारसी किंवा स्थानिक क्रियाकलाप सुचवणारे तज्ज्ञ एजंट्स जोडू शकता आणि वेळोवेळी अधिक चांगला आराखडा तयार करू शकता.

### संरचित आउटपुट

लार्ज लँग्वेज मॉडेल्स (LLMs) संरचित आउटपुट (उदा. JSON) निर्माण करू शकतात जे डाउनस्ट्रीम एजंट्स किंवा सेवा सहज पार्स आणि प्रक्रिया करू शकतात. हे बहु-एजंट संदर्भात विशेषतः उपयुक्त आहे, जिथे नियोजन आउटपुट मिळाल्यानंतर आपण या कार्यांवर कृती करू शकतो.

खालील Python स्निपेट साध्या नियोजन एजंटचे उद्दिष्ट उपकार्यांमध्ये decomposition करण्याचे आणि संरचित योजना निर्माण करण्याचे उदाहरण दाखवते:

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

# प्रवास उपटास्क मॉडेल
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # आम्हाला एजंटला टास्क देऊ इच्छितो

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# वापरकर्त्याचा संदेश परिभाषित करा
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

### बहु-एजंट संचालनासह नियोजन एजंट

या उदाहरणात, एक Semantic Router Agent वापरकर्त्याच्या विनंती (उदा. "मला माझ्या प्रवासासाठी हॉटेल आराखडा हवा आहे.") प्राप्त करतो.

नंतर नियोजक:

* हॉटेल आराखडा प्राप्त करतो: वापरकर्त्याचा संदेश घेऊन, सिस्टम प्रॉम्प्ट (उपलब्ध एजंट तपशीलांसह) वर आधारित एक संरचित प्रवास आराखडा तयार करतो.
* एजंट्स आणि त्यांच्या उपकरणांची यादी करतो: एजंट रजिस्ट्रीमध्ये एजंट्सची यादी असते (उदा. फ्लाइट, हॉटेल, कार भाड्याने घेणे, क्रियाकलापांसाठी) आणि ते जे कार्ये/उपकरणे देतात ती समाविष्ट असतात.
* योजना संबंधित एजंट्सकडे मार्गदर्शित करतो: उपकार्यांच्या संख्येनुसार, नियोजक संदेश एखाद्या खास एजंटला थेट पाठवू शकतो (एकाच कामासाठी) किंवा बहु-एजंट सहकार्यासाठी ग्रुप चॅट व्यवस्थापकाद्वारे समन्वयित करतो.
* निकालांचा सारांश करतो: शेवटी, नियोजक स्पष्टतेसाठी तयार केलेल्या योजना सारांश करतो.
खालील Python कोड याप्रकारे दर्शवितो:

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

# प्रवास उपकार्य मॉडेल

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # आम्हाला एजंटला कार्य नियुक्त करायचे आहे

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# क्लायंट तयार करा

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

from pprint import pprint

# वापरकर्ता संदेश परिभाषित करा

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

# JSON म्हणून लोड केल्यावर प्रतिसाद सामग्री छापा

pprint(json.loads(response_content))
```

पुढील कोडमधील आउटपुट खाली आहे आणि तुम्ही नंतर हा संरचित आउटपुट `assigned_agent` कडे मार्गदर्शन करण्यासाठी आणि अंतिम वापरकर्त्यास प्रवास आराखडा सारांश रूपात देण्यासाठी वापरू शकता.

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

मागील कोड नमुन्यासह एक उदाहरण नोटबुक [येथे](./code_samples/07-python-agent-framework.ipynb) उपलब्ध आहे.

### पुनरावृत्ती नियोजन

काही कार्यांसाठी एका उपकार्याचा निकाल पुढील कार्यावर प्रभाव टाकतो अशा पारस्परिक किंवा पुनर-योजनांची गरज असते. उदाहरणार्थ, जर एजंट फ्लाइट बुक करताना अनपेक्षित डेटा स्वरूप शोधत असेल, तर त्याला हॉटेल बुकिंग करता येण्यापूर्वी आपली रणनीती बदलावी लागू शकते.

तसेच, वापरकर्त्याचा अभिप्राय (उदा. एखाद्या व्यक्तीने आधीचा फ्लाइट पसंती दिली तर) अंशतः पुनःयोजना सुरू करू शकतो. हा गतिशील, पुनरावृत्ती दृष्टिकोन अंतिम निराकरणाने प्रत्यक्ष अडचणी व बदलत्या वापरकर्त्यांच्या प्राधान्यांसह जुळवून घेतल्याची खात्री करतो.

उदा. नमुना कोड

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. अगोदरच्या कोडसारखेच आणि वापरकर्त्याचा इतिहास, सध्याचा योजना पुढे पाठवा

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
# .. पुन्हा योजना तयार करा आणि संबंधित एजंटांना कामे पाठवा
```

अधिक व्यापक नियोजनासाठी, Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">ब्लॉगपोस्ट</a> पहा, जे जटिल कार्ये सोडवण्यासाठी आहे.

## सारांश

या लेखात आपण कसा योजना तयार करता येतो ज्यात उपलब्ध एजंट्स डायनॅमिकली निवडले जातात हे पाहिले. नियोजकाचे आउटपुट कार्य decomposition करून एजंट्सना असाइन करते जेणेकरून ते अंमलात आणता येतील. एजंट्सना कार्य करण्यासाठी आवश्यक फंक्शन्स/टूल्सची उपलब्धता गृहीत धरली जाते. एजंट्सव्यतिरिक्त, तुम्ही आरसा, सारांशकार आणि राऊंड रॉबिन चॅटसारखे इतर नमुने देखील समाविष्ट करू शकता ज्यामुळे अधिक वैयक्तिकृत करता येते.

## अतिरिक्त साधने

Magnetic One - जटिल कार्ये सोडवण्यासाठी एक सामान्य मल्टी-एजंट प्रणाली असून, अनेक आव्हानात्मक एजंटिक बेंचमार्कवर जबरदस्त निकाल मिळाले आहेत. संदर्भ: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. या अंमलबजावणीत ऑर्केस्ट्रेटर कार्य-विशिष्ट योजना तयार करतो आणि या कार्यांसाठी उपलब्ध एजंट्सना प्रतिनिधीत्व देतो. नियोजनाशिवाय ऑर्केस्ट्रेटर एक ट्रॅकिंग यंत्रणा देखील वापरतो ज्यामुळे कार्याची प्रगती तपासली जाते आणि गरज भासल्यास पुनःयोजना केली जाते.

### नियोजन डिझाइन पॅटर्नबद्दल अधिक प्रश्न आहेत का?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) मध्ये सामील व्हा, जेथे तुम्ही इतर शिकणाऱ्यांशी भेटू शकता, ऑफिस तासांना उपस्थित राहू शकता आणि तुमचे AI एजंट्सबाबत प्रश्न विचारू शकता.

## मागील धडा

[विश्वसनीय AI एजंट्स तयार करणे](../06-building-trustworthy-agents/README.md)

## पुढील धडा

[मल्टी-एजंट डिझाइन पॅटर्न](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->