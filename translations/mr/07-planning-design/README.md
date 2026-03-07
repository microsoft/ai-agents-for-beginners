[![योजना डिझाइन पॅटर्न](../../../translated_images/mr/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(वरील प्रतिमा क्लिक करून या धड्याचे व्हिडिओ पहा)_

# नियोजन डिझाइन

## परिचय

हा धडा खालील गोष्टींचा समावेश करेल

* एक स्पष्ट एकूण उद्दिष्ट परिभाषित करणे आणि गुंतागुंतीच्या कार्याला हाताळण्यायोग्य उपकार्यात विभाजित करणे.
* अधिक विश्वसनीय आणि मशीन-वाचनीय प्रतिसादांसाठी संरचित आउटपुटचा लाभ घेणे.
* गतिशील कार्ये आणि अनपेक्षित इनपुट हाताळण्यासाठी इव्हेंट-चालित पद्धत लागू करणे.

## शिकण्याची उद्दिष्टे

हा धडा पूर्ण केल्यानंतर, आपण खालील बाबींची समज मिळवाल:

* एआय एजंटसाठी एकूण उद्दिष्ट ओळखणे आणि सेट करणे, जेणेकरून त्याला स्पष्टपणे कळेल काय साध्य करायचे आहे.
* गुंतागुंतीच्या कार्याला हाताळण्यायोग्य उपकार्यात विभाजित करणे आणि त्यांना तर्कसंगत क्रमात आयोजित करणे.
* एजंट्सना योग्य साधने (उदा., शोध साधने किंवा डेटा विश्लेषण साधने) प्रदान करणे, कोणत्या वेळी आणि कसे वापरायचे हे ठरवणे, आणि उद्भवणाऱ्या अनपेक्षित परिस्थिती हाताळणे.
* उपकार्यातील परिणामांचे मूल्यांकन करणे, कामगिरीचे मापन करणे, आणि अंतिम आउटपुट सुधारण्यासाठी कृतींमध्ये पुनरावृत्ती करणे.

## एकूण उद्दिष्ट परिभाषित करणे आणि कार्य विभाजित करणे

![उद्दिष्टे आणि कार्य परिभाषित करणे](../../../translated_images/mr/defining-goals-tasks.d70439e19e37c47a.webp)

अधिकांश वास्तविक जगातील कार्ये एका पावलात हाताळण्यास खूप गुंतागुंतीची असतात. एआय एजंटला त्याच्या नियोजन आणि कृती मार्गदर्शित करण्यासाठी संक्षिप्त उद्दिष्टाची गरज असते. उदाहरणार्थ, खालील उद्दिष्ट विचार करा:

    "3 दिवसांचे प्रवासाचे आराखडा तयार करा."

जरी हे विधान साधे वाटले तरी त्यात अजून सुधारणा आवश्यक असते. उद्दिष्ट जितके स्पष्ट असेल, तितके एजंट (आणि कोणतेही मानवी सहकारी) योग्य निकाल साध्य करण्यावर लक्ष केंद्रित करू शकतील, जसे की फ्लाइट पर्याय, हॉटेल शिफारसी आणि उपक्रमांच्या सूचना असलेला सर्वसमावेशक आराखडा तयार करणे.

### कार्य विभाजन

मोठी किंवा सखोल कार्ये छोटे, उद्दिष्टाभिमुख उपकार्यांमध्ये विभागली गेल्यावर अधिक हाताळण्यायोग्य बनतात.
प्रवासाच्या आराखड्याच्या उदाहरणासाठी, आपण उद्दिष्ट पुढीलप्रमाणे विभाजित करू शकता:

* फ्लाइट आरक्षण
* हॉटेल आरक्षण
* कार भाड्याने घेणे
* वैयक्तिकीकरण

प्रत्येक उपकार्य नंतर समर्पित एजंट्स किंवा प्रक्रियांद्वारे हाताळता येते. एक एजंट सर्वोत्तम फ्लाइट डील शोधण्यात विशेषज्ञ असू शकतो, दुसरा हॉटेल बुकिंगवर लक्ष केंद्रित करतो, आणि असे पुढे. एक समन्वयक किंवा “डाउनस्ट्रीम” एजंट नंतर या परिणामांना एकसंध आराखड्यात संकलित करून अंतिम वापरकर्त्यापर्यंत पोहोचवू शकतो.

हा मॉड्यूलर दृष्टिकोन तसेच क्रमिक सुधारणा करण्यासही परवानगी देतो. उदाहरणार्थ, आपण अन्नाच्या शिफारसींसाठी किंवा स्थानिक उपक्रम सुचविणाऱ्या विशेष एजंट्स जोडू शकता आणि कालानुक्रमे आराखडा अधिक परिपूर्ण करू शकता.

### संरचित आउटपुट

Large Language Models (LLMs) संरचित आउटपुट (उदा., JSON) तयार करू शकतात जे डाउनस्ट्रीम एजंट्स किंवा सेवांसाठी पार्स आणि प्रक्रिया करण्यास सोपे असते. हे विशेषतः बहु-एजंट संदर्भात उपयुक्त आहे, जिथे नियोजन आउटपुट प्राप्त झाल्यानंतर आपण हे कार्य अंमलात आणू शकतो.

The following Python snippet demonstrates a simple planning agent decomposing a goal into subtasks and generating a structured plan:

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

# प्रवास उपकार्य मॉडेल
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # आम्हाला हे कार्य एजंटला नियुक्त करायचे आहे

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

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

### मल्टी-एजंट ऑर्केस्ट्रेशनसह नियोजन एजंट

या उदाहरणात, एक Semantic Router Agent वापरकर्त्याचा विनंती प्राप्त करतो (उदा., "मला माझ्या प्रवासासाठी हॉटेल योजना हवी आहे.").

नियोजक नंतर:

* हॉटेल योजना प्राप्त करतो: नियोजक वापरकर्त्याचा संदेश घेतो आणि सिस्टम प्रॉम्प्टच्या (उपलब्ध एजंट तपशीलांसह) आधारे एक संरचित प्रवास आराखडा तयार करतो.
* एजंट आणि त्यांच्या साधनांची यादी करतो: एजंट रजिस्ट्रीमध्ये एजंटांची यादी असते (उदा., फ्लाइट, हॉटेल, कार भाड्याने घेणे, आणि उपक्रमांसाठी) तसेच ते कोणत्या फंक्शन्स किंवा साधने ऑफर करतात ते नमूद असते.
* आराखडा संबंधित एजंटकडे मार्गदर्शित करतो: उपकार्यांच्या संख्येनुसार, नियोजक संदेश थेट समर्पित एजंटकडे पाठवू शकतो (एकल-कार्य परिस्थितीसाठी) किंवा बहु-एजंट सहकार्याकरिता गट चॅट व्यवस्थापकाद्वारे समन्वय करू शकतो.
* परिणाम सारांशित करतो: शेवटी, नियोजक स्पष्टतेसाठी तयार केलेला आराखडा सारांशित करतो.
खालील Python कोड नमुना या टप्प्यांचे प्रदर्शन करतो:

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
    assigned_agent: AgentEnum # आम्हाला हे कार्य एजंटला नियुक्त करायचे आहे

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# क्लायंट तयार करा

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# वापरकर्त्याचा संदेश परिभाषित करा

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

# JSON म्हणून लोड केल्यानंतर प्रतिक्रियेची सामग्री छापा

pprint(json.loads(response_content))
```

खालील भाग मागील कोडचे आउटपुट आहे आणि आपण हा संरचित आउटपुट `assigned_agent` कडे मार्गदर्शित करण्यासाठी आणि अंतिम वापरकर्त्यास प्रवास आराखडा सारांशित करण्यासाठी वापरू शकता.

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

मागील कोड नमुन्यासह एक उदाहरण नोटबुक [इथे](07-python-agent-framework.ipynb) उपलब्ध आहे.

### पुनरावर्ती नियोजन

काही कार्यांना परस्पर संवाद किंवा पुन्हा नियोजनाची गरज असते, जिथे एका उपकार्याचा परिणाम पुढील उपकार्याला प्रभावित करतो. उदाहरणार्थ, जर एजंटाने उड्डाणे बुक करताना अनपेक्षित डेटा फॉरमॅट आढळला, तर अगोदरच ठरवलेली धोरणे बदलून हॉटेल बुकिंगकडे प्रस्थान करण्यापूर्वी त्याला अनुकूल करण्याची गरज असू शकते.

याशिवाय, वापरकर्त्याचे अभिप्राय (उदा., मानवी वापरकर्त्याने आधीच्या उड्डाणाला प्राधान्य देण्याचा निर्णय घेतल्यास) आंशिक पुनर्नियोजन ट्रिगर करू शकतो. ही गतिशील, पुनरावर्ती पद्धत अंतिम सोल्यूशन वास्तविक जगातील निर्बंध आणि बदलणाऱ्या वापरकर्त्यांच्या प्राधान्यांच्या अनुरूप राहून देते.

उदा. नमुना कोड

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. मागील कोडप्रमाणेच आणि वापरकर्त्याचा इतिहास व सध्याची योजना पुढे पाठवा

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
# .. पुन्हा योजना आखा आणि कार्ये संबंधित एजंटांना पाठवा
```

अधिक सर्वसमावेशक नियोजनासाठी आणि गुंतागुंतीच्या कार्यांसाठी उपाय शोधण्यासाठी Magentic One चा <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">ब्लॉगपोस्ट</a> पहा.

## सारांश

या लेखात आपण असा एक उदाहरण पाहिला आहे ज्यात आपण उपलब्ध एजंट्स डायनॅमिकली निवडणारा एक प्लॅनर तयार करू शकतो. नियोजकाचा आउटपुट कार्यांना विभाजित करतो आणि एजंट्सना कार्यसोपान असाइन करतो जेणेकरून ते अंमलात आणले जाऊ शकतील. असे गृहित धरले जाते की एजंट्सकडे त्या कार्यासाठी आवश्यक फंक्शन्स/साधनांचा प्रवेश आहे. एजंट्सच्या जोडण्याव्यतिरिक्त आपण अधिक सानुकूलता देण्यासाठी प्रतिबिंबन, सारांशकार, आणि राउंड रॉबिन चॅट सारख्या इतर पॅटर्न्स देखील समाविष्ट करू शकता.

## अतिरिक्त संसाधने

Magentic One - गुंतागुंतीच्या कार्यांसाठी समस्या सोडवणारी एक जनरलिस्ट मल्टी-एजंट सिस्टिम आहे आणि अनेक आव्हानात्मक एजंटिक बेंचमार्कवर प्रभावी निकाल मिळविला आहे. संदर्भ: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. या अंमलबजावणीत ऑर्केस्ट्रेटर कार्य-विशिष्ट आराखडे तयार करतो आणि उपलब्ध एजंट्सना ही कार्ये वाटप करतो. नियोजनाशिवाय, ऑर्केस्ट्रेटर कार्याची प्रगती मॉनिटर करण्यासाठी ट्रॅकिंग मेकॅनिझमचा वापरही करतो आणि आवश्यकतेनुसार पुनर्नियोजन करतो.

### नियोजन डिझाइन पॅटर्नबद्दल आणखी प्रश्न आहेत का?

इतर शिकणाऱ्यांशी भेटण्यासाठी, ऑफिस तासांना उपस्थित राहण्यासाठी आणि आपल्या AI एजंट्सच्या प्रश्नांची उत्तरे मिळवण्यासाठी [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) मध्ये सामील व्हा.

## मागील धडा

[विश्वसनीय AI एजंट तयार करणे](../06-building-trustworthy-agents/README.md)

## पुढील धडा

[मल्टी-एजंट डिझाइन पॅटर्न](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
अस्वीकरण:
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला गेला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, परंतु कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये त्रुटी किंवा चुकीचे अर्थ असू शकतात. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत म्हणून विचारात घेतला पाहिजे. महत्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवादाची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुतीसाठी किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->