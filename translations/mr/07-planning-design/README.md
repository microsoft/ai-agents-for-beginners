<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "43069833a0412210ad5c3cc93d9c2146",
  "translation_date": "2025-09-18T14:38:00+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "mr"
}
-->
[![Planning Design Pattern](../../../translated_images/lesson-7-thumbnail.f7163ac557bea1236242cc86b178c3f1bbf5eb07b87f9cd7c256b366e32bcbb6.mr.png)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(वरील प्रतिमेवर क्लिक करून या धड्याचा व्हिडिओ पहा)_

# नियोजन डिझाइन

## परिचय

या धड्यात आपण शिकणार आहोत:

* स्पष्ट एकूण उद्दिष्ट निश्चित करणे आणि जटिल कार्याचे व्यवस्थापनीय कार्यांमध्ये विभाजन करणे.
* संरचित आउटपुटचा उपयोग करून अधिक विश्वासार्ह आणि मशीन-वाचनीय प्रतिसाद मिळवणे.
* गतिशील कार्ये आणि अनपेक्षित इनपुट हाताळण्यासाठी इव्हेंट-ड्रिव्हन दृष्टिकोन लागू करणे.

## शिकण्याची उद्दिष्टे

हा धडा पूर्ण केल्यानंतर, तुम्हाला खालील गोष्टींची समज होईल:

* AI एजंटसाठी एकूण उद्दिष्ट ओळखणे आणि निश्चित करणे, ज्यामुळे त्याला काय साध्य करायचे आहे हे स्पष्टपणे समजेल.
* जटिल कार्याचे व्यवस्थापनीय उपकार्यांमध्ये विभाजन करणे आणि त्यांना तर्कसंगत क्रमात आयोजित करणे.
* एजंट्सना योग्य साधने (उदा. शोध साधने किंवा डेटा विश्लेषण साधने) प्रदान करणे, ती कधी आणि कशी वापरायची हे ठरवणे आणि उद्भवणाऱ्या अनपेक्षित परिस्थिती हाताळणे.
* उपकार्यांचे परिणाम मूल्यांकन करणे, कार्यक्षमता मोजणे आणि अंतिम आउटपुट सुधारण्यासाठी कृतींवर पुनरावृत्ती करणे.

## एकूण उद्दिष्ट निश्चित करणे आणि कार्याचे विभाजन करणे

![उद्दिष्टे आणि कार्ये निश्चित करणे](../../../translated_images/defining-goals-tasks.d70439e19e37c47ac76c48b209a4eb515bea5b8a5207f6b2e7b5e597f09ccf6a.mr.png)

बहुतेक वास्तविक-जगातील कार्ये एका चरणात हाताळण्यासाठी खूप जटिल असतात. AI एजंटला त्याच्या नियोजन आणि कृतींना मार्गदर्शन करण्यासाठी संक्षिप्त उद्दिष्ट आवश्यक असते. उदाहरणार्थ, खालील उद्दिष्ट विचार करा:

    "3 दिवसांचा प्रवासाचा कार्यक्रम तयार करा."

हे सांगणे सोपे असले तरी, त्याला अजून स्पष्टता आवश्यक आहे. उद्दिष्ट जितके स्पष्ट असेल तितके एजंट (आणि कोणतेही मानवी सहकारी) योग्य परिणाम साध्य करण्यावर लक्ष केंद्रित करू शकतात, जसे की फ्लाइट पर्याय, हॉटेल शिफारसी आणि क्रियाकलापांच्या सूचनांसह एक व्यापक कार्यक्रम तयार करणे.

### कार्याचे विभाजन

मोठी किंवा गुंतागुंतीची कार्ये लहान, उद्दिष्ट-केंद्रित उपकार्यांमध्ये विभाजित केल्यास अधिक व्यवस्थापनीय होतात. प्रवासाच्या कार्यक्रमाच्या उदाहरणासाठी, तुम्ही उद्दिष्ट खालीलप्रमाणे विभाजित करू शकता:

* फ्लाइट बुकिंग
* हॉटेल बुकिंग
* कार भाड्याने घेणे
* वैयक्तिकरण

प्रत्येक उपकार्य समर्पित एजंट्स किंवा प्रक्रियांद्वारे हाताळले जाऊ शकते. एक एजंट सर्वोत्तम फ्लाइट डील शोधण्यात तज्ज्ञ असू शकतो, तर दुसरा हॉटेल बुकिंगवर लक्ष केंद्रित करतो, इत्यादी. समन्वयक किंवा "डाउनस्ट्रीम" एजंट नंतर या परिणामांना एकत्र करून अंतिम वापरकर्त्यासाठी एक सुसंगत कार्यक्रम तयार करू शकतो.

या मॉड्यूलर दृष्टिकोनामुळे टप्प्याटप्प्याने सुधारणा करणे शक्य होते. उदाहरणार्थ, तुम्ही खाद्य शिफारसी किंवा स्थानिक क्रियाकलापांच्या सूचनांसाठी विशेष एजंट्स जोडू शकता आणि वेळोवेळी कार्यक्रम अधिक परिष्कृत करू शकता.

### संरचित आउटपुट

मोठ्या भाषा मॉडेल्स (LLMs) संरचित आउटपुट (उदा. JSON) तयार करू शकतात जे डाउनस्ट्रीम एजंट्स किंवा सेवांसाठी पार्स आणि प्रक्रिया करणे सोपे असते. हे विशेषतः मल्टी-एजंट संदर्भात उपयुक्त आहे, जिथे आम्ही नियोजन आउटपुट प्राप्त झाल्यानंतर या कार्यांवर कृती करू शकतो. 

द्रुत आढावा घेण्यासाठी खालील Python कोड स्निपेट एक साधा नियोजन एजंट उद्दिष्ट उपकार्यांमध्ये विभाजित करून संरचित योजना तयार करत असल्याचे दाखवते:

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

### मल्टी-एजंट ऑर्केस्ट्रेशनसह नियोजन एजंट

या उदाहरणात, एक सेमॅंटिक राउटर एजंट वापरकर्त्याचा विनंती प्राप्त करतो (उदा., "माझ्या प्रवासासाठी मला हॉटेल योजना हवी आहे.").

नियोजक नंतर:

* हॉटेल योजना प्राप्त करतो: नियोजक वापरकर्त्याचा संदेश घेतो आणि सिस्टम प्रॉम्प्ट (उपलब्ध एजंट तपशीलांसह) आधारित संरचित प्रवास योजना तयार करतो.
* एजंट्स आणि त्यांच्या साधनांची यादी करतो: एजंट रजिस्ट्रीत एजंट्सची यादी असते (उदा., फ्लाइट, हॉटेल, कार भाड्याने घेणे आणि क्रियाकलाप) आणि त्यांनी ऑफर केलेल्या फंक्शन्स किंवा साधनांसह.
* योजना संबंधित एजंट्सकडे पाठवतो: उपकार्यांच्या संख्येवर अवलंबून, नियोजक संदेश थेट समर्पित एजंटकडे (सिंगल-टास्क परिस्थितीसाठी) पाठवतो किंवा मल्टी-एजंट सहकार्यासाठी ग्रुप चॅट मॅनेजरद्वारे समन्वय साधतो.
* परिणामाचा सारांश तयार करतो: शेवटी, नियोजक स्पष्टतेसाठी तयार केलेल्या योजनेचा सारांश तयार करतो.

खालील Python कोड नमुना या चरणांचे चित्रण करतो:

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

वरील कोडमधून मिळालेला आउटपुट खालीलप्रमाणे आहे आणि तुम्ही नंतर `assigned_agent` कडे रूट करून अंतिम वापरकर्त्यासाठी प्रवास योजना सारांशित करू शकता.

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

वरील कोड नमुन्यासह एक उदाहरण नोटबुक [येथे](07-autogen.ipynb) उपलब्ध आहे.

### पुनरावृत्ती नियोजन

काही कार्यांसाठी परत-परत किंवा पुनर्नियोजन आवश्यक असते, जिथे एका उपकार्याचा परिणाम पुढील उपकार्यावर परिणाम करतो. उदाहरणार्थ, जर एजंट फ्लाइट बुक करताना अनपेक्षित डेटा स्वरूप शोधतो, तर त्याला हॉटेल बुकिंगवर जाण्यापूर्वी त्याची रणनीती बदलावी लागेल.

याशिवाय, वापरकर्त्याचा अभिप्राय (उदा. एखाद्या व्यक्तीने त्यांना लवकर फ्लाइट हवे असल्याचे ठरवले) आंशिक पुनर्नियोजन ट्रिगर करू शकतो. हा गतिशील, पुनरावृत्ती दृष्टिकोन सुनिश्चित करतो की अंतिम समाधान वास्तविक-जगातील अडचणी आणि विकसित होणाऱ्या वापरकर्ता प्राधान्यांशी जुळते.

उदा. नमुना कोड:

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

अधिक व्यापक नियोजनासाठी Magnetic One तपासा, जटिल कार्ये सोडवण्यासाठी.

## सारांश

या लेखात आपण पाहिले की कसे एक नियोजक तयार करता येतो जो उपलब्ध एजंट्सची निवड करून कार्य विशिष्ट योजना तयार करतो आणि ही कार्ये संबंधित एजंट्सकडे सोपवतो. असे गृहीत धरले जाते की एजंट्सकडे कार्य पूर्ण करण्यासाठी आवश्यक फंक्शन्स/साधनांपर्यंत प्रवेश आहे. एजंट्स व्यतिरिक्त, तुम्ही रिफ्लेक्शन, सारांशकार, आणि राउंड रॉबिन चॅट यासारख्या इतर पॅटर्न्स समाविष्ट करून अधिक सानुकूलित करू शकता.

## अतिरिक्त संसाधने

AutoGen Magnetic One - जटिल कार्ये सोडवण्यासाठी एक सामान्यत: मल्टी-एजंट प्रणाली आहे आणि अनेक आव्हानात्मक एजंटिक बेंचमार्कवर प्रभावी परिणाम साध्य केले आहेत. संदर्भ:

. या अंमलबजावणीत ऑर्केस्ट्रेटर कार्य-विशिष्ट योजना तयार करतो आणि ही कार्ये उपलब्ध एजंट्सकडे सोपवतो. नियोजनाशिवाय ऑर्केस्ट्रेटर प्रगतीचे निरीक्षण करण्यासाठी ट्रॅकिंग यंत्रणा देखील वापरतो आणि आवश्यक असल्यास पुनर्नियोजन करतो.

### नियोजन डिझाइन पॅटर्नबद्दल अधिक प्रश्न आहेत?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) मध्ये सामील व्हा, इतर शिकणाऱ्यांशी भेटा, ऑफिस तासांमध्ये सहभागी व्हा आणि तुमचे AI एजंट्स संबंधित प्रश्न विचारून उत्तर मिळवा.

## मागील धडा

[विश्वसनीय AI एजंट्स तयार करणे](../06-building-trustworthy-agents/README.md)

## पुढील धडा

[मल्टी-एजंट डिझाइन पॅटर्न](../08-multi-agent/README.md)

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून निर्माण होणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.