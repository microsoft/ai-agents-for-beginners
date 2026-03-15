[![Planning Design Pattern](../../../translated_images/ne/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(यो पाठको भिडियो हेर्न माथिको तस्वीरमा क्लिक गर्नुहोस्)_

# योजना डिजाइन

## परिचय

यस पाठले समावेश गर्नेछ

* स्पष्ट समग्र लक्ष्य परिभाषित गर्ने र जटिल कार्यलाई व्यवस्थापन योग्य कार्यहरूमा विभाजन गर्ने।
* भरपर्दो र मेसिन-पढ्न मिल्ने प्रतिक्रिया को लागि संरचित आउटपुट प्रयोग गर्ने।
* गतिशील कार्यहरू र अप्रत्याशित इनपुटहरूलाई सामना गर्न कार्यक्रम-सञ्चालित दृष्टिकोण लागू गर्ने।

## सिकाई उद्देश्यहरू

यस पाठ पूरा गरेपछि, तपाईंलाई निम्न बारेमा बुझाइ हुनेछ:

* AI एजेन्टको लागि समग्र लक्ष्य पहिचान गर्ने र सेट गर्ने, जसले के प्राप्त गर्नुपर्छ स्पष्ट रूपले जान्न सकोस्।
* जटिल कार्यलाई व्यवस्थापन योग्य उपकार्यहरूमा विभाजन गर्ने र तिनीहरूलाई तार्किक अनुक्रममा व्यवस्थित गर्ने।
* एजेन्टहरूलाई सही उपकरणहरू (जस्तै, खोज उपकरणहरू वा डेटा विश्लेषण उपकरणहरू) लेसकेर, कहिले र कसरी प्रयोग गर्ने निर्णय गर्ने, र आउन सक्ने अप्रत्याशित स्थिति सम्हाल्ने।
* उपकार्य परिणामहरूको मूल्यांकन गर्ने, प्रदर्शन मापन गर्ने, र अन्तिम आउटपुट सुधार गर्न कार्यहरू दोहोर्याउने।

## समग्र लक्ष्य परिभाषित गर्ने र कार्य विभाजन गर्ने

![Defining Goals and Tasks](../../../translated_images/ne/defining-goals-tasks.d70439e19e37c47a.webp)

धेरै वास्तविक-विश्व कार्यहरूलाई एक पटकमा समाधान गर्न धेरै जटिल हुन्छ। AI एजेन्टले आफ्ना योजना र क्रियाकलापहरू निर्देशन गर्न संक्षिप्त उद्देश्य चाहिन्छ। उदाहरणको रूपमा, लक्ष्य विचार गर्नुहोस्:

    "3-दिने यात्रा योजना तयार गर्नुहोस्।"

यो सरल छ भनिने, तर अझ परिस्कृत आवश्यक छ। लक्ष्य जति स्पष्ट हुन्छ, एजेन्ट (र कुनै पनि मानव सहयोगीहरू) ले सही नतिजा प्राप्त गर्न सजिलो हुन्छ, जस्तै उडान विकल्पहरू, होटल सिफारिसहरू, र गतिविधि सुझावहरूसहित व्यापक यात्रा योजना बनाउने।

### कार्य विभाजन

ठूला वा जटिल कार्यहरू साना, लक्ष्यमुखी उपकार्यहरूमा विभाजन गर्दा व्यवस्थापन गर्न सजिलो हुन्छ।
यात्रा योजनाको उदाहरणका लागि, तपाईं लक्ष्यलाई निम्नमा विभाजन गर्न सक्नुहुन्छ:

* उडान बुकिङ
* होटल बुकिङ
* कार भाडामा लिने
* व्यक्तिगतकरण

हरेक उपकार्य त्यस कार्यमा विशेषज्ञ एजेन्टहरू वा प्रक्रियाहरूले काम गर्न सक्छन्। एउटा एजेन्टले उत्कृष्ट उडान सम्झौताहरू खोज्नमा केन्द्रित हुन सक्छ, अर्को होटल बुकिङमा, आदि। एक समन्वयक वा “डाउन्स्ट्रीम” एजेन्टले यी परिणामहरूलाई एकसाथ मिलाएर अन्तिम प्रयोगकर्तालाई प्रस्तुत गर्न सक्छ।

यो मोड्युलर दृष्टिकोणले क्रमिक सुधारहरूलाई पनि अनुमति दिन्छ। उदाहरणका लागि, तपाईं खाना सिफारिस वा स्थानीय गतिविधि सुझावका लागि विशेषज्ञ एजेन्टहरू थप्न सक्नुहुन्छ र योजनालाई समयसंग संशोधन गर्न सक्नुहुन्छ।

### संरचित आउटपुट

ठूला भाषा मोडेलहरूले (LLMs) संरचित आउटपुट (जस्तै JSON) उत्पादन गर्न सक्छन्, जुन डाउन्स्ट्रीम एजेन्टहरू वा सेवाहरूले सजिलै पार्स र प्रक्रिया गर्न सजिलो हुन्छ। यो विशेष गरी बहु-एजेन्ट सन्दर्भमा उपयोगी छ, जहाँ हामी योजना आउटपुट प्राप्त भएपछि यी कार्यहरू सञ्चालन गर्न सक्छौं।

तलको Python स्निपेटले एउटा सरल योजना एजेन्टले लक्ष्यलाई उपकार्यहरूमा विभाजित गर्दै संरचित योजना तयार गर्ने देखाउँछ:

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

# यात्रा उपकार्य मोडेल
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # हामी एजेन्टलाई कार्य जिम्मा दिन चाहन्छौं

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

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

### बहु-एजेन्ट समन्वयका साथ योजना एजेन्ट

यस उदाहरणमा, एक सेमेन्टिक राउटर एजेन्टले प्रयोगकर्ता अनुरोध (जस्तै, "मेरो यात्राको लागि होटल योजना चाहिन्छ।") प्राप्त गर्दछ।

योजनाकारले त्यसपछि:

* होटल योजना प्राप्त गर्दछ: योजनाकारले प्रयोगकर्ताको सन्देश लिन्छ र सिस्टम प्रम्प्ट (उपलब्ध एजेन्ट विवरणहरु सहित) को आधारमा संरचित यात्रा योजना तयार गर्दछ।
* एजेन्ट र तिनीहरूको उपकरणहरूको सूची बनाउँछ: एजेन्ट रजिष्ट्रिले एजेन्टहरूको सूची राख्छ (जस्तै उडान, होटल, कार भाडामा लिने, र गतिविधिहरूका लागि) र तिनीहरूले प्रस्ताव गर्ने कार्यहरू वा उपकरणहरू।
* योजना सम्बद्ध एजेन्टहरूलाई पठाउँछ: उपकार्यहरूको संख्याको आधारमा, योजनाकारले सन्देश सिधै विशेष एजेन्टलाई पठाउँछ (एकल-कार्य अवस्थामा) वा बहु-एजेन्ट सहयोगको लागि समूह कुरा व्यवस्थापक मार्फत समन्वय गर्दछ।
* नतिजा सारांश गर्छ: अन्तमा, योजनाकारले स्पष्टताका लागि तयार गरेको योजना सारांश गर्छ।
तलको Python कोड नमुना यी चरणहरू देखाउँछ:

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

# यात्रा उपकार्य मोडेल

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # हामीले एजेन्टलाई काम सुम्पन चाहन्छौं

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# क्लाइन्ट सिर्जना गर्नुहोस्

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

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

अघिल्लो कोडबाट प्राप्त आउटपुट तल प्रस्तुत गरिएको छ र तपाईं यस संरचित आउटपुटलाई `assigned_agent` मा मार्गनिर्देशन गर्न र अन्तिम प्रयोगकर्ताका लागि यात्रा योजना सारांश गर्न प्रयोग गर्न सक्नुहुन्छ।

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

अघिल्लो कोड नमुनासहित उदाहरण नोटबुक यहाँ उपलब्ध छ [here](07-python-agent-framework.ipynb)।

### पुनरावृत्त योजना बनाउने

केही कार्यहरूमा एक उपकार्यको नतिजाले अर्को उपकार्यलाई प्रभावित गर्दै पुनः योजना आवश्यक पर्न सक्छ। उदाहरणका लागि, यदि एजेन्टले उडान बुकिङ गर्दा अप्रत्याशित डेटा ढाँचा खोज्छ भने, त्यसले होटल बुकिङमा जानु अघि आफ्नो रणनीति अनुकूलन गर्न आवश्यक पर्न सक्छ।

थपमा, प्रयोगकर्ता प्रतिक्रिया (जस्तै मान्छेले छिटो उडान रोज्न चाहँदा) आंशिक पुनः योजनालाई ट्रिगर गर्न सक्छ। यो गतिशील, पुनरावृत्त दृष्टिकोणले अन्तिम समाधान वास्तविक-विश्व सीमितता र विकासशील प्रयोगकर्ता प्राथमिकतासँग मेल खान्छ।

उदाहरण कोड

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. पहिलेको कोड जस्तै र प्रयोगकर्ता इतिहास, वर्तमान योजना पास गर्नुहोस्

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

अझ व्यापक योजना बनाउने चाहनुहुन्छ भने, जटिल कार्यहरू समाधान गर्न Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">ब्लगपोस्ट</a> अवश्य हेर्नुहोस्।

## सारांश

यस लेखमा हामीले कसरी एक योजनाकार सिर्जना गर्न सकिन्छ जसले उपलब्ध एजेन्टहरूलाई गतिशील रूपमा चयन गर्न सक्छ भन्ने उदाहरण हेर्यौं। योजनाकारको आउटपुटले कार्यहरू विभाजित गरी एजेन्टहरूलाई जिम्मा दिन्छ ताकि तिनीहरू कार्यान्वयन गर्न सकून्। मानिएको छ कि एजेन्टहरूले आवस्यक कार्यहरू/उपकरणहरू पहुँच गर्न सक्छन्। एजेन्टहरूका अतिरिक्त, तपाईं परावर्तन, सारांशकर्ता, र राउन्ड रोबिन च्याट जस्ता अन्य ढाँचाहरू समावेश गरेर थप अनुकूलन गर्न सक्नुहुन्छ।

## अतिरिक्त स्रोतहरू

Magentic One - जटिल कार्यहरू समाधान गर्ने बहु-एजेन्ट प्रणाली हो र यसले विभिन्न चुनौतीपूर्ण एजेन्टिक बेन्चमार्कहरूमा प्रभावशाली नतिजा प्राप्त गरेको छ। संदर्भ: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. यस कार्यान्वयनमा, आयोजकले कार्य-विशिष्ट योजना बनाउँछ र उपलब्ध एजेन्टहरूलाई ती कार्यहरू हस्तान्तरण गर्दछ। योजनाको अतिरिक्त, आयोजकले कार्य प्रगति निगरानी गर्न र आवश्यक परे पुनः योजना बनाउन ट्र्याकिङ म्याकेनिज़म पनि प्रयोग गर्दछ।

### योजना डिजाइन ढाँचा सम्बन्धी थप प्रश्नहरू छन्?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) मा सामेल हुनुहोस् र अन्य सिक्नेहरूबाट भेटघाट गर्नुहोस्, कार्यालय घण्टामा जानुहोस् र AI एजेन्ट सम्बन्धी प्रश्नहरूको उत्तर पाउनुहोस्।

## अघिल्लो पाठ

[विश्वसनीय AI एजेन्टहरू निर्माण गर्ने](../06-building-trustworthy-agents/README.md)

## अर्को पाठ

[बहु-एजेन्ट डिजाइन ढाँचा](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यस दस्तावेजलाई AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज यसको मूल भाषामै आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण सूचनाका लागि, पेशेवर मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->