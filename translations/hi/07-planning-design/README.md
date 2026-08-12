[![Planning Design Pattern](../../../translated_images/hi/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(इस पाठ का वीडियो देखने के लिए ऊपर की छवि पर क्लिक करें)_

# योजना डिजाइन

## परिचय

इस पाठ में निम्नलिखित विषय शामिल होंगे

* एक स्पष्ट समग्र लक्ष्य को परिभाषित करना और जटिल कार्य को प्रबंधनीय कार्यों में विभाजित करना।
* अधिक विश्वसनीय और मशीन-पाठ्य उत्तरों के लिए संरचित आउटपुट का उपयोग।
* गतिशील कार्यों और अप्रत्याशित इनपुट को संभालने के लिए एक घटना-चालित दृष्टिकोण लागू करना।

## सीखने के लक्ष्य

इस पाठ को पूरा करने के बाद, आपको निम्नलिखित समझ होगी:

* एक AI एजेंट के लिए समग्र लक्ष्य को पहचानना और सेट करना, जिससे यह स्पष्ट हो कि क्या प्राप्त करना है।
* जटिल कार्य को प्रबंधनीय उप-टास्क में विभाजित करना और उन्हें तार्किक अनुक्रम में व्यवस्थित करना।
* एजेंट्स को सही उपकरण (जैसे खोज उपकरण या डेटा एनालिटिक्स उपकरण) प्रदान करना, यह निर्णय लेना कि उन्हें कब और कैसे उपयोग किया जाए, और अप्रत्याशित परिस्थितियों को संभालना।
* उप-कार्य के परिणामों का मूल्यांकन करना, प्रदर्शन को मापना, और अंतिम आउटपुट में सुधार के लिए क्रियाओं को दोहराना।

## समग्र लक्ष्य को परिभाषित करना और एक कार्य को विभाजित करना

![Defining Goals and Tasks](../../../translated_images/hi/defining-goals-tasks.d70439e19e37c47a.webp)

अधिकांश वास्तविक विश्व के कार्य एक कदम में संभालने के लिए बहुत जटिल होते हैं। एक AI एजेंट को अपनी योजना और क्रियाओं का निर्देश देने के लिए एक संक्षिप्त उद्देश्य की आवश्यकता होती है। उदाहरण के लिए, लक्ष्य को देखें:

    "3-दिन की यात्रा कार्यक्रम बनाएं।"

जबकि इसे व्यक्त करना सरल है, इसे अभी भी सुधार की आवश्यकता है। जितना स्पष्ट लक्ष्य होगा, एजेंट (और किसी भी मानव सहयोगियों को) सही परिणाम प्राप्त करने के लिए उतना ही बेहतर ध्यान केंद्रित कर सकता है, जैसे कि फ्लाइट विकल्प, होटल की सिफारिशें, और गतिविधि सुझावों के साथ एक व्यापक यात्रा कार्यक्रम बनाना।

### कार्य विघटन

बड़े या जटिल कार्य छोटे, लक्ष्य-उन्मुख उप कार्यों में विभाजित करने पर अधिक प्रबंधनीय हो जाते हैं।
यात्रा कार्यक्रम के उदाहरण के लिए, आप लक्ष्य को इस तरह विभाजित कर सकते हैं:

* फ्लाइट बुकिंग
* होटल बुकिंग
* कार किराया
* वैयक्तिकीकरण

प्रत्येक उप-कार्य को समर्पित एजेंट्स या प्रक्रियाओं द्वारा संभाला जा सकता है। एक एजेंट सर्वोत्तम फ्लाइट डील खोजने में विशेषज्ञ हो सकता है, दूसरा होटल बुकिंग पर ध्यान केंद्रित कर सकता है, इत्यादि। एक समन्वयक या "डाउनस्ट्रीम" एजेंट तब इन परिणामों को एक सुसंगत यात्रा कार्यक्रम में अंतिम उपयोगकर्ता को प्रस्तुत कर सकता है।

यह मॉड्यूलर दृष्टिकोण क्रमिक सुधारों की अनुमति भी देता है। उदाहरण के लिए, आप खाद्य सुझावों या स्थानीय गतिविधि सिफारिशों के लिए विशेष एजेंट जोड़ सकते हैं और समय के साथ यात्रा कार्यक्रम को परिष्कृत कर सकते हैं।

### संरचित आउटपुट

बड़े भाषा मॉडल (LLMs) संरचित आउटपुट (जैसे JSON) उत्पन्न कर सकते हैं जो डाउनस्ट्रीम एजेंट्स या सेवाओं द्वारा पार्स और प्रोसेस करना आसान होता है। यह विशेष रूप से बहु-एजेंट संदर्भ में उपयोगी है, जहां हम योजना आउटपुट प्राप्त होने के बाद इन कार्यों को क्रियान्वित कर सकते हैं।

निम्नलिखित Python कोड स्निपेट एक सरल योजना एजेंट को दिखाता है जो एक लक्ष्य को उप-कार्य में विभाजित करता है और एक संरचित योजना उत्पन्न करता है:

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

# यात्रा उपकार्य मॉडल
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # हम एजेंट को कार्य सौंपना चाहते हैं

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

### मल्टी-एजेंट आयोजक के साथ योजना एजेंट

इस उदाहरण में, एक सेमांटिक राउटर एजेंट उपयोगकर्ता अनुरोध प्राप्त करता है (जैसे, "मुझे मेरी यात्रा के लिए होटल योजना चाहिए।").

योजना बनाने वाला फिर:

* होटल योजना प्राप्त करता है: योजना बनाने वाला उपयोगकर्ता के संदेश को स्वीकार करता है और सिस्टम प्रॉम्प्ट (जो उपलब्ध एजेंट विवरण शामिल करता है) के आधार पर एक संरचित यात्रा योजना उत्पन्न करता है।
* एजेंट्स और उनके उपकरणों की सूची बनाता है: एजेंट रजिस्टर में एजेंट्स की सूची होती है (जैसे फ्लाइट, होटल, कार किराया, और गतिविधियों के लिए) साथ ही वे कौन-कौन से फ़ंक्शन या उपकरण प्रदान करते हैं।
* योजना को संबंधित एजेंटों को मार्गदर्शित करता है: उप-टास्क की संख्या के आधार पर, योजना बनाने वाला संदेश को सीधे समर्पित एजेंट को भेजता है (एकल कार्य के लिए) या मल्टी-एजेंट सहयोग के लिए समूह चैट प्रबंधक के माध्यम से समन्वय करता है।
* परिणाम सारांशित करता है: अंत में, योजना बनाने वाला स्पष्टता के लिए उत्पन्न योजना का सारांश प्रस्तुत करता है।
निम्नलिखित Python कोड उदाहरण इन चरणों को दर्शाता है:

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

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# क्लाइंट बनाएं

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

वर्तमान कोड से प्राप्त आउटपुट इस प्रकार है, और आप इस संरचित आउटपुट का उपयोग `assigned_agent` को मार्गदर्शित करने और अंतिम उपयोगकर्ता को यात्रा योजना का सारांश प्रस्तुत करने के लिए कर सकते हैं।

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

पिछले कोड नमूने के साथ एक उदाहरण नोटबुक [यहाँ](./code_samples/07-python-agent-framework.ipynb) उपलब्ध है।

### पुनरावृत्त योजना बनाना

कुछ कार्यों को लगातार दोहराव या पुनः योजना बनाने की आवश्यकता होती है, जहां एक उप-कार्य का परिणाम अगले उप-कार्य को प्रभावित करता है। उदाहरण के लिए, यदि एजेंट फ्लाइट बुक करते समय अप्रत्याशित डेटा प्रारूप पाता है, तो उसे होटल बुकिंग पर जाने से पहले अपनी रणनीति को अनुकूलित करना पड़ सकता है।

इसके अतिरिक्त, उपयोगकर्ता प्रतिक्रिया (जैसे कोई मानव यह तय करता है कि उसे पहले फ्लाइट पसंद है) आंशिक पुनः योजना को ट्रिगर कर सकती है। यह गतिशील, पुनरावृत्त दृष्टिकोण अंतिम समाधान को वास्तविक विश्व की सीमाओं और बदलती उपयोगकर्ता प्राथमिकताओं के साथ संरेखित करता है।

जैसे नमूना कोड

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. पिछली कोड के समान और उपयोगकर्ता इतिहास, वर्तमान योजना पारित करें

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
# .. पुनः योजना बनाएं और कार्यों को संबंधित एजेंटों को भेजें
```

जटिल कार्यों को हल करने के लिए Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">ब्लॉगपोस्ट</a> देखें।

## सारांश

इस लेख में हमने देखा कि हम कैसे एक योजना बना सकते हैं जो गतिशील रूप से उपलब्ध एजेंट्स का चयन कर सके। योजना का आउटपुट कार्यों को विभाजित करता है और एजेंट्स को सौंपता है ताकि उन्हें निष्पादित किया जा सके। यह मान लिया जाता है कि एजेंट्स के पास आवश्यक कार्यों को करने के लिए आवश्यक फ़ंक्शंस/टूल्स तक पहुंच है। एजेंट्स के अलावा आप परावर्तन, सारांशक और राउंड रॉबिन चैट जैसे अन्य पैटर्न भी शामिल कर सकते हैं ताकि आगे अनुकूलन किया जा सके।

## अतिरिक्त संसाधन

Magnetic One - जटिल कार्यों को हल करने के लिए एक सामान्यीकृत बहु-एजेंट प्रणाली जो कई चुनौतीपूर्ण एजेंटिक बेंचमार्कों पर प्रभावशाली परिणाम प्राप्त कर चुकी है। संदर्भ: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. इस कार्यान्वयन में आयोजक कार्य विशिष्ट योजनाएं बनाता है और इन कार्यों को उपलब्ध एजेंटों को सौंपता है। योजना बनाने के अलावा आयोजक एक ट्रैकिंग तंत्र भी उपयोग करता है ताकि कार्य की प्रगति की निगरानी की जा सके और आवश्यकतानुसार पुनः योजना बनाई जा सके।

### योजना डिजाइन पैटर्न के बारे में और प्रश्न हैं?

अन्य शिक्षार्थियों से मिलने, कार्यालय समय में भाग लेने और अपने AI एजेंट्स से संबंधित प्रश्नों के उत्तर प्राप्त करने के लिए [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) में शामिल हों।

## पिछला पाठ

[विश्वसनीय AI एजेंट बनाना](../06-building-trustworthy-agents/README.md)

## अगला पाठ

[मल्टी-एजेंट डिजाइन पैटर्न](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->