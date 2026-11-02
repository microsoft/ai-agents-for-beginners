[![Planning Design Pattern](../../../translated_images/ne/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(यो पाठको भिडियो हेर्न माथिको तस्बिरमा क्लिक गर्नुहोस्)_

# योजना डिजाइन

## परिचय

यो पाठले समेट्नेछ

* स्पष्ट समग्र लक्ष्य परिभाषित गर्ने र एक जटिल कार्यलाई व्यवस्थापनयोग्य कार्यहरूमा विभाजन गर्ने।
* अधिक विश्वसनीय र मेसिन-पठनीय प्रतिक्रिया को लागि संरचित आउटपुटको उपयोग गर्ने।
* गतिशील कार्यहरू र अप्रत्याशित इनपुटहरू सामना गर्न घटना-चालित दृष्टिकोण लागू गर्ने।

## सिक्ने लक्ष्यहरू

यो पाठ पूरा गरेपछि तपाईंसँग निम्न कुराहरूको बुझाइ हुनेछ:

* AI एजेन्टको लागि समग्र लक्ष्य पहिचान गर्ने र सेट गर्ने, जसले के हासिल गर्नु पर्ने स्पष्ट रूपमा थाहा पाओस्।
* जटिल कार्यलाई व्यवस्थापनयोग्य उपकार्यहरूमा विभाजन गर्ने र तिनीहरूलाई तार्किक अनुक्रममा व्यवस्थित गर्ने।
* एजेन्टहरूलाई सही उपकरणहरू (जस्तै, खोज उपकरण वा डाटा विश्लेषण उपकरणहरू) द्वारा सुसज्जित गर्ने, कहिले र कसरी प्रयोग गर्ने निर्णय गर्ने, र उत्पन्न भएकाप अप्रत्याशित अवस्थाहरूलाई सामना गर्ने।
* उपकार्यहरूको नतिजा मूल्याङ्कन गर्ने, प्रदर्शन मापन गर्ने, र अन्तिम आउटपुट सुधार गर्न कार्यहरू पुनरावृत्ति गर्ने।

## समग्र लक्ष्य परिभाषित गर्ने र कार्यलाई विभाजन गर्ने

![Defining Goals and Tasks](../../../translated_images/ne/defining-goals-tasks.d70439e19e37c47a.webp)

धेरै वास्तविक-विश्व कार्यहरू एकैचोटि समाधान गर्न धेरै जटिल हुन्छन्। AI एजेन्टलाई यसको योजना र कार्यहरूलाई मार्गदर्शन गर्न संक्षिप्त उद्देश्य आवश्यक हुन्छ। उदाहरणका लागि, लक्ष्य विचार गर्नुहोस्:

    "एक ३-दिने यात्रा यात्रा तालिका तयार पार्नु।"

यो सरल देखिए पनि यसलाई अझ स्पष्ट बनाउन आवश्यक छ। जब लक्ष्य स्पष्ट हुन्छ, एजेन्ट (र कुनै पनि मानव सहकर्मीहरू) उचित परिणाम हासिल गर्न बढी ध्यान केन्द्रित गर्न सक्छन्, जस्तै उडान विकल्प, होटल सिफारिसहरू र क्रियाकलाप सुझावहरू सहित एक समग्र यात्रा तालिका तयार पार्ने।

### कार्य विभाजन

ठूलो वा जटिल कार्यहरू साना, लक्ष्य-केंद्रित उपकार्यहरूमा विभाजन गर्दा थप व्यवस्थापनयोग्य हुन्छन्।
यात्रा तालिका उदाहरणका लागि, तपाईँ लक्ष्यलाई यसरी विभाजन गर्न सक्नुहुन्छ:

* उडान बुकिङ
* होटल बुकिङ
* कार भाडामा लिने
* अनुकूलन

प्रत्येक उपकार्यलाई समर्पित एजेन्टहरू वा प्रक्रियाहरूले समाधान गर्न सक्छन्। एउटा एजेन्टले सबैभन्दा राम्रो उडान सम्झौता खोज्नमा विशेषज्ञता राख्न सक्छ, अर्को होटल बुकिङमा केन्द्रित हुन्छ, र यस्तै। समन्वय गर्ने वा "डाउनस्ट्रीम" एजेन्टले यी नतिजाहरूलाई प्रयोगकर्ता अन्तिममा एक सुसंगत यात्रा तालिकामा संकलन गर्न सक्छ।

यो मोड्युलर दृष्टिकोणले क्रमिक सुधारहरूको पनि अनुमति दिन्छ। उदाहरणका लागि, तपाईँ खाद्य सिफारिसहरू वा स्थानीय गतिविधि सुझावहरूको लागि विशेष एजेन्टहरू थप्न सक्नुहुन्छ र समयक्रमसँगै यात्रा तालिकालाई सुधार्न सक्नुहुन्छ।

### संरचित आउटपुट

ठूलो भाषा मोडेलहरू (LLMs) ले संरचित आउटपुट (जस्तो JSON) उत्पादन गर्न सक्छन् जुन डाउनस्ट्रीम एजेन्टहरू वा सेवाहरूले पार्स र प्रक्रिया गर्न सजिलो हुन्छ। यो विशेष गरी बहु-एजेन्ट सन्दर्भमा उपयोगी हुन्छ, जहाँ हामी योजना आउटपुट प्राप्त भएपछि यी कार्यहरू सञ्चालन गर्न सक्छौं।

तलको Python स्निपेटले देखाउँछ कसरी एक साधारण योजना एजेन्टले लक्ष्यलाई उपकार्यहरूमा विभाजन गरी संरचित योजना बनाउँछ:

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

# यात्रा उपकार्य मोडेल
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # हामी कार्य एजेन्टलाई दिन चाहन्छौं

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# प्रयोगकर्ता सन्देश परिभाषित गर्नुहोस्
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

### बहु-एजेन्ट समन्वयसहित योजना एजेन्ट

यस उदाहरणमा, एक सेमेन्टिक राउटर एजेन्टले प्रयोगकर्ताको अनुरोध प्राप्त गर्छ (जस्तै, "म मेरो यात्राको लागि होटल योजना चाहन्छु।")।

योजनाकार त्यसपछि:

* होटल योजना प्राप्त गर्छ: योजनाकारले प्रयोगकर्ताको सन्देशलाई लिन्छ र प्रणाली प्रॉम्प्ट (उपलब्ध एजेन्ट विवरण सहित) को आधारमा एक संरचित यात्रा योजना उत्पन्न गर्छ।
* एजेन्टहरू र तिनका उपकरणहरूको सूची बनाउँछ: एजेन्ट रजिस्ट्रीमा एजेन्टहरूको सूची हुन्छ (जस्तै, उडान, होटल, कार भाडामा लिने, र क्रियाकलापहरूका लागि) र तिनीहरूले प्रस्ताव गर्ने कार्यहरू वा उपकरणहरू।
* योजनालाई सम्बन्धित एजेन्टहरूतर्फ पठाउँछ: उपकार्यहरूको संख्याको आधारमा, योजनाकारले सन्देशलाई सिधै समर्पित एजेन्टलाई पठाउन सक्छ (एकल-कार्य परिस्थितिहरूमा) वा बहु-एजेन्ट सहकार्यका लागि समूह च्याट प्रबन्धक मार्फत समन्वय गर्छ।
* परिणाम सारांश बनाउँछ: अन्ततः, योजनाकारले उत्पन्न योजनाको स्पष्टताको लागि सारांश बनाउँछ।
तलको Python कोड उदाहरण यी चरणहरू देखाउँछ:

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

# यात्रा सबटास्क मोडेल

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # हामी एजेन्टलाई काम असाइन गर्न चाहन्छौं

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# क्लाइन्ट सिर्जना गर्नुहोस्

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

from pprint import pprint

# प्रयोगकर्ता सन्देश परिभाषित गर्नुहोस्

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

# JSON रूपमा लोड गरेपछि प्रतिक्रिया सामग्री प्रिन्ट गर्नुहोस्

pprint(json.loads(response_content))
```

यसपछि आउँने आउटपुट हो र तपाईं यस संरचित आउटपुटलाई `assigned_agent` मा मार्गदर्शन गर्न र अन्तिम प्रयोगकर्तालाई यात्रा योजना सारांशमा प्रयोग गर्न सक्नुहुन्छ।

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

पहिलेको कोड नमूना सहितको उदाहरण नोटबुक [यहाँ](./code_samples/07-python-agent-framework.ipynb) उपलब्ध छ।

### पुनरावृत्त योजना

केही कार्यहरूले पछाडि फिर्ता जान वा पुन: योजना बनाउने आवश्यकता पर्छ, जहाँ एउटा उपकार्यको परिणामले अर्कोमा प्रभाव पार्छ। उदाहरणका लागि, यदि एजेन्टले उडान बुकिङ गर्दा अप्रत्याशित डाटा ढाँचा पत्ता लगाउँछ भने, यसले होटल बुकिङ अघि आफ्नो रणनीति परिमार्जन गर्न सक्छ।

यसै गरी, प्रयोगकर्ता प्रतिक्रिया (जस्तै, मानिसले पहिलेको उडान रोज्न चाहन्छ) ले आंशिक पुन: योजनालाई ट्रिगर गर्न सक्छ। यो गतिशील, पुनरावृत्त दृष्टिकोणले अन्तिम समाधान वास्तविक-विश्व सीमा र विकासशील प्रयोगकर्ता प्राथमिकतासँग मेल खान्छ भन्ने सुनिश्चित गर्छ।

जस्तै नमूना कोड

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. पहिलेको कोड जस्तै र प्रयोगकर्ता इतिहास, वर्तमान योजना पठाउनुहोस्

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
# .. पुन: योजना बनाउनुहोस् र कार्यहरू सम्बन्धित एजेन्टहरूलाई पठाउनुहोस्
```

बढी व्यापक योजनाका लागि Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">ब्लगपोस्ट</a> हेर्नुहोस्, जसले जटिल कार्यहरू समाधान गर्दछ।

## सारांश

यस लेखमा हामीले कसरी एक योजना बनाउने जसले परिभाषित उपलब्ध एजेन्टहरूलाई गतिशील रूपमा चयन गर्न सक्छ भन्ने उदाहरण हेर्यौं। योजनाकारको आउटपुटले कार्यहरूलाई विभाजन गरी एजेन्टहरूलाई जिम्मेवारी दिनेछ ताकि ती कार्यहरू कार्यान्वयन गर्न सकियोस। एजेन्टहरूले कार्य गर्ने लागि आवश्यक कार्यहरू/उपकरणहरूमा पहुँच राख्छन् भन्ने मानिएको छ। एजेन्टहरूका साथै तपाईंले परावर्तन, सारांशकर्ता, र राउन्ड रोबिन च्याट जस्ता अन्य ढाँचाहरू पनि समावेश गर्न सक्नुहुन्छ।

## थप स्रोतहरू

Magentic One - जटिल कार्यहरू समाधान गर्न सामान्य बहु-एजेन्ट प्रणाली हो र यसले धेरै चुनौतीपूर्ण एजेन्टिक बेंचमार्कहरूमा प्रभावशाली परिणामहरू प्राप्त गरेको छ। सन्दर्भ: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. यस कार्यान्वयनमा, समन्वयकर्ताले कार्य-विशिष्ट योजना बनाउन र ती कार्यहरू उपलब्ध एजेन्टहरूलाई दिन्छ। योजनाबद्ध नगरेर, समन्वयकर्ताले कार्यको प्रगति ट्रयाक गर्न र आवश्यक परे पुन: योजना बनाउने तरिका पनि प्रयोग गर्छ।

### योजना डिजाइन ढाँचाबारे थप प्रश्न छ?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) मा सहभागी हुनुहोस् अन्य सिक्नेहरूसँग भेट्न, कार्यालय समयहरूमा जान, र AI एजेन्टहरू सम्बन्धी प्रश्नहरूको उत्तर पाउन।

## अघिल्लो पाठ

[विश्वसनीय AI एजेन्टहरू निर्माण](../06-building-trustworthy-agents/README.md)

## अर्को पाठ

[बहु-एजेन्ट डिजाइन ढाँचा](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->