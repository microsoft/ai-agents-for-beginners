[![Planning Design Pattern](../../../translated_images/hi/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(इस पाठ का वीडियो देखने के लिए ऊपर की छवि पर क्लिक करें)_

# योजना डिज़ाइन

## परिचय

यह पाठ निम्नलिखित विषयों को कवर करेगा

* एक स्पष्ट समग्र लक्ष्य को परिभाषित करना और एक जटिल कार्य को प्रबंधनीय कार्यों में विभाजित करना।
* अधिक विश्वसनीय और मशीन-पठनीय प्रतिक्रियाओं के लिए संरचित आउटपुट का उपयोग करना।
* गतिशील कार्यों और अप्रत्याशित इनपुट को संभालने के लिए एक घटना-चालित दृष्टिकोण लागू करना।

## सीखने के लक्ष्य

इस पाठ को पूरा करने के बाद, आप निम्न विषयों को समझ पाएंगे:

* एक AI एजेंट के लिए समग्र लक्ष्य निर्धारित करना और सेट करना, यह सुनिश्चित करना कि इसे स्पष्ट रूप से पता हो कि क्या प्राप्त करना है।
* एक जटिल कार्य को प्रबंधनीय उप-कार्यों में विभाजित करना और उन्हें तार्किक क्रम में व्यवस्थित करना।
* एजेंट्स को सही उपकरणों (जैसे खोज उपकरण या डेटा एनालिटिक्स उपकरण) से लैस करना, यह तय करना कि उन्हें कब और कैसे उपयोग किया जाए, और उत्पन्न होने वाली अप्रत्याशित परिस्थितियों को संभालना।
* उप-कार्य परिणामों का मूल्यांकन करना, प्रदर्शन मापना, और अंतिम आउटपुट सुधारने के लिए कार्यों को पुनः करना।

## समग्र लक्ष्य को परिभाषित करना और कार्य को विभाजित करना

![Defining Goals and Tasks](../../../translated_images/hi/defining-goals-tasks.d70439e19e37c47a.webp)

अधिकांश वास्तविक दुनिया के कार्य एक एकल चरण में निपटाना बहुत जटिल होते हैं। एक AI एजेंट को अपनी योजना और क्रियाओं का मार्गदर्शन करने के लिए एक संक्षिप्त उद्देश्य की आवश्यकता होती है। उदाहरण के लिए, लक्ष्य पर विचार करें:

    "3-दिन की यात्रा कार्यक्रम बनाएं।"

हालांकि इसे व्यक्त करना सरल है, फिर भी इसे और परिष्कृत करने की आवश्यकता होती है। लक्ष्य जितना स्पष्ट होगा, एजेंट (और कोई भी मानव सहयोगी) उतना बेहतर सही परिणाम प्राप्त करने पर ध्यान केंद्रित कर सकते हैं, जैसे कि उड़ान विकल्पों, होटल की सिफारिशों, और गतिविधि सुझावों के साथ एक व्यापक यात्रा कार्यक्रम बनाना।

### कार्य विखंडन

बड़े या जटिल कार्य छोटे, लक्ष्य-उन्मुख उप-कार्य में विभाजित करने से अधिक प्रबंधनीय हो जाते हैं। यात्रा कार्यक्रम के उदाहरण के लिए, आप लक्ष्य को निम्न में विभाजित कर सकते हैं:

* फ्लाइट बुकिंग
* होटल बुकिंग
* कार किराया
* निजीकृत करना

प्रत्येक उप-कार्य को समर्पित एजेंट या प्रक्रियाओं द्वारा सामना किया जा सकता है। एक एजेंट उत्कृष्ट फ्लाइट डील खोजने में विशेषज्ञ हो सकता है, दूसरा होटल बुकिंग पर केंद्रित हो सकता है, और इसी प्रकार। एक समन्वयक या "डाउनस्ट्रीम" एजेंट इन परिणामों को एक सटीक यात्रा कार्यक्रम में अंतिम उपयोगकर्ता के लिए संकलित कर सकता है।

यह मॉड्यूलर दृष्टिकोण क्रमिक सुधारों की अनुमति भी देता है। उदाहरण के लिए, आप भोजन सिफारिशों या स्थानीय गतिविधि सुझावों के लिए विशेषज्ञ एजेंट जोड़ सकते हैं और समय के साथ यात्रा कार्यक्रम को बेहतर बना सकते हैं।

### संरचित आउटपुट

बड़े भाषा मॉडल (LLMs) संरचित आउटपुट (जैसे JSON) उत्पन्न कर सकते हैं जो डाउनस्ट्रीम एजेंट या सेवाओं के लिए पार्स और संसाधित करना आसान होता है। यह विशेष रूप से एक मल्टी-एजेंट संदर्भ में उपयोगी होता है, जहां हम योजना आउटपुट प्राप्त होने के बाद इन कार्यों को क्रियान्वित कर सकते हैं।

निम्नलिखित पायथन स्निपेट एक सरल योजना एजेंट को दिखाता है जो एक लक्ष्य को उप-कार्यों में विभाजित करता है और एक संरचित योजना उत्पन्न करता है:

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

# यात्रा उपकार्य मॉडल
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # हम कार्य को एजेंट को सौंपना चाहते हैं

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# उपयोगकर्ता संदेश परिभाषित करें
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

### मल्टी-एजेंट संचालन के साथ योजना एजेंट

इस उदाहरण में, एक सेमांटिक राउटर एजेंट उपयोगकर्ता अनुरोध (जैसे, "मुझे मेरी यात्रा के लिए होटल योजना चाहिए।") प्राप्त करता है।

फिर योजनाकार:

* होटल योजना प्राप्त करता है: योजनाकार उपयोगकर्ता के संदेश को लेता है और सिस्टम प्रॉम्प्ट (उपलब्ध एजेंट विवरण सहित) के आधार पर एक संरचित यात्रा योजना बनाता है।
* एजेंट्स और उनके उपकरणों की सूची बनाता है: एजेंट रजिस्ट्री पास एजेंटों की एक सूची रखती है (जैसे, फ्लाइट, होटल, कार किराया, और गतिविधियों के लिए) साथ ही उनके द्वारा प्रदान किए जाने वाले फ़ंक्शन या उपकरण।
* योजना को संबंधित एजेंटों को भेजता है: उप-कार्य की संख्या के आधार पर, योजनाकार सीधे समर्पित एजेंट को संदेश भेजता है (एकल-कार्य परिदृश्यों के लिए) या मल्टी-एजेंट सहयोग के लिए समूह चैट प्रबंधक के माध्यम से समन्वय करता है।
* परिणाम का सारांश बनाता है: अंत में, योजनाकार उत्पन्न योजना का स्पष्टता के लिए सारांश बनाता है।
निम्नलिखित पायथन कोड नमूना इन चरणों को दर्शाता है:

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

# यात्रा उपकार्य मॉडल

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # हम एजेंट को कार्य सौंपना चाहते हैं

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# क्लाइंट बनाएं

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# उपयोगकर्ता संदेश परिभाषित करें

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

# इसे JSON के रूप में लोड करने के बाद प्रतिक्रिया सामग्री प्रिंट करें

pprint(json.loads(response_content))
```

जो नीचे दिया गया है वह पिछले कोड से आउटपुट है और आप फिर इस संरचित आउटपुट का उपयोग करके `assigned_agent` को रूट कर सकते हैं और यात्रा योजना को अंतिम उपयोगकर्ता को सारांशित कर सकते हैं।

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

पिछले कोड नमूने के साथ एक उदाहरण नोटबुक [यहाँ](07-python-agent-framework.ipynb) उपलब्ध है।

### पुनरावृत्त योजना

कुछ कार्यों के लिए आपसी संवाद या पुन: योजना आवश्यक होती है, जहाँ एक उप-कार्य का परिणाम अगले कार्य को प्रभावित करता है। उदाहरण के लिए, यदि एजेंट उड़ान बुकिंग करते समय अप्रत्याशित डेटा प्रारूप खोजता है, तो उसे होटल बुकिंग शुरू करने से पहले अपनी रणनीति को अनुकूलित करना पड़ सकता है।

इसके अतिरिक्त, उपयोगकर्ता प्रतिक्रिया (जैसे कोई व्यक्ति यह निर्णय लेता है कि उसे पहले की उड़ान पसंद है) आंशिक पुन: योजना को ट्रिगर कर सकती है। यह गतिशील, पुनरावृत्त दृष्टिकोण सुनिश्चित करता है कि अंतिम समाधान वास्तविक विश्व सीमाओं और बदलते उपयोगकर्ता प्राथमिकताओं के अनुरूप हो।

जैसे कि नमूना कोड

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. पिछले कोड की तरह ही और उपयोगकर्ता इतिहास, वर्तमान योजना पास करें

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
# .. पुनः योजना बनाएं और संबंधित एजेंटों को कार्य भेजें
```

अधिक व्यापक योजना के लिए कृपया Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">ब्लॉगपोस्ट</a> देखें, जो जटिल कार्यों को हल करने के लिए एक सामान्य मल्टी-एजेंट सिस्टम है।

## सारांश

इस लेख में हमने देखा कि कैसे हम एक ऐसा योजनाकार बना सकते हैं जो परिभाषित उपलब्ध एजेंटों को गतिशील रूप से चुन सकता है। योजनाकार का आउटपुट कार्यों को विभाजित करता है और एजेंटों को आवंटित करता है ताकि वे निष्पादित किए जा सकें। यह मान लिया गया है कि एजेंटों को आवश्यक कार्य करने के लिए आवश्यक फ़ंक्शन/उपकरण उपलब्ध हैं। एजेंटों के अलावा आप परावर्तन, सारांशकार और राउंड रॉबिन चैट जैसे अन्य पैटर्न भी शामिल कर सकते हैं ताकि और अनुकूलन किया जा सके।

## अतिरिक्त संसाधन

Magentic One - जटिल कार्यों को हल करने के लिए एक सामान्य मल्टी-एजेंट सिस्टम है और इसने कई चुनौतीपूर्ण एजेंटिक बेंचमार्क पर प्रभावशाली परिणाम प्राप्त किए हैं। संदर्भ: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>। इस कार्यान्वयन में, ऑर्केस्ट्रेटर कार्य-विशिष्ट योजनाएं बनाता है और इन कार्यों को उपलब्ध एजेंटों को सौंपता है। योजना बनाने के अलावा ऑर्केस्ट्रेटर एक ट्रैकिंग तंत्र भी उपयोग करता है जो कार्य की प्रगति की निगरानी करता है और आवश्यकतानुसार पुन: योजना बनाता है।

### योजना डिज़ाइन पैटर्न के बारे में और सवाल हैं?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) में शामिल हों ताकि अन्य शिक्षार्थियों से मिल सकें, ऑफिस ऑवर्स अटेंड कर सकें और अपने AI एजेंट्स से संबंधित प्रश्नों के उत्तर प्राप्त कर सकें।

## पिछला पाठ

[विश्वसनीय AI एजेंट बनाना](../06-building-trustworthy-agents/README.md)

## अगला पाठ

[मल्टी-एजेंट डिज़ाइन पैटर्न](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यह दस्तावेज़ एआई अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल भाषा में मूल दस्तावेज़ ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->