[![Exploring AI Agent Frameworks](../../../translated_images/mr/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(या धड्याचा व्हिडिओ पाहण्यासाठी वरच्या प्रतिमेवर क्लिक करा)_

# AI एजंट फ्रेमवर्क्सचा अभ्यास करा

AI एजंट फ्रेमवर्क्स हे सॉफ्टवेअर प्लॅटफॉर्म आहेत जे AI एजंट्स तयार करणे, तैनात करणे आणि व्यवस्थापित करणे सुलभ करतात. हे फ्रेमवर्क डेव्हलपर्सना तयार घटक, अमूर्तता आणि साधने प्रदान करतात जी गुंतागुंतीच्या AI प्रणालींच्या विकासाला सरलीकृत करतात.

हे फ्रेमवर्क AI एजंट विकासातील सामान्य आव्हानांसाठी प्रमाणबद्ध दृष्टिकोन देऊन डेव्हलपर्सना त्यांच्या अनुप्रयोगांच्या अद्वितीय पैलूंवर लक्ष केंद्रित करण्यास मदत करतात. ते AI सिस्टम्स तयार करताना स्केलेबिलिटी, प्रवेशयोग्यता आणि कार्यक्षमतेत वाढ करतात.

## परिचय

हा धडा खालील गोष्टींचा आढावा घेईल:

- AI एजंट फ्रेमवर्क्स म्हणजे काय आणि ते डेव्हलपर्सना काय साध्य करण्यास मदत करतात?
- टीम्स त्यांच्या एजंटच्या क्षमता पटकन प्रोटोटाइप, पुनरावृत्ती आणि सुधारण्यासाठी हे कसे वापरू शकतात?
- माइक्रोसॉफ्टने तयार केलेल्या फ्रेमवर्क्स आणि साधने यामधील फरक (Microsoft Foundry Agent Service आणि Microsoft Agent Framework)?
- माझे विद्यमान Azure इकोसिस्टम टूल्स थेट समाकलित करू शकतो का, की मला स्वतंत्र उपायांची आवश्यकता आहे?
- Microsoft Foundry Agent Service काय आहे आणि ते मला कसे मदत करत आहे?

## शिकण्याच्या उद्दिष्टे

या धड्याच्या उद्दिष्टांमध्ये समजून घेणे हे आहे:

- AI विकासात AI एजंट फ्रेमवर्क्सची भूमिका.
- बुद्धिमान एजंट्स तयार करण्यासाठी AI एजंट फ्रेमवर्क्सचा फायदा कसा घ्यायचा.
- AI एजंट फ्रेमवर्क्सद्वारे सक्षम केलेल्या मुख्य क्षमता.
- Microsoft Agent Framework आणि Microsoft Foundry Agent Service यामधील फरक.

## AI एजंट फ्रेमवर्क्स काय आहेत आणि ते डेव्हलपर्सना काय करायला तयार करतात?

पारंपारिक AI फ्रेमवर्क्स तुमच्या अनुप्रयोगांमध्ये AI समाकलित करण्यात आणि त्यांना खालील प्रकारे सुधारण्यात मदत करतात:

- **वैयक्तिकीकरण**: AI वापरकर्त्याच्या वागणूक आणि प्राधान्यांचा विश्लेषण करून वैयक्तिकृत शिफारसी, सामग्री आणि अनुभव प्रदान करू शकतो.
उदाहरण: Netflix सारख्या स्ट्रिमिंग सेवा AI वापरकर्त्यांच्या पाहण्याच्या इतिहासावर आधारित चित्रपट आणि शो शिफारस करतात, ज्यामुळे वापरकर्ता सहभाग आणि समाधानीपणा वाढतो.
- **स्वयंचलन आणि कार्यक्षमता**: AI पुनरावृत्ती होणारी कामे स्वयंचलित करू शकतो, कार्यप्रवाह सुलभ करू शकतो आणि ऑपरेशनल कार्यक्षमता सुधारू शकतो.
उदाहरण: ग्राहक सेवा अनुप्रयोग AI-चालित चॅटबॉट्स वापरून सामान्य चौकशी हाताळतात, प्रतिसाद वेळ कमी करतात आणि मानवी एजंट्सना अधिक गुंतागुंतीच्या समस्यांसाठी मोकळा ठेवतात.
- **सुधारित वापरकर्ता अनुभव**: AI स्मार्ट वैशिष्ट्ये जसे की व्हॉईस ओळख, नैसर्गिक भाषा प्रक्रिया आणि पूर्वानुमानित मजकूर प्रदान करून एकूण वापरकर्ता अनुभव सुधारू शकतो.
उदाहरण: Siri आणि Google Assistant सारखे वर्चुअल सहाय्यक AI वापरून वापरकर्त्यांच्या व्हॉईस कमांड समजून घेतात आणि प्रतिसाद देतात, ज्यामुळे उपकरणांशी संवाद सुलभ होतो.

### आवाज छान आहे, मग आपल्याला AI एजंट फ्रेमवर्क का हवा आहे?

AI एजंट फ्रेमवर्क्स केवळ AI फ्रेमवर्क्सपेक्षा अधिक काही आहेत. हे बुद्धिमान एजंट तयार करण्यासाठी बनवलेले आहेत जे वापरकर्ते, इतर एजंट्स आणि पर्यावरणाशी संवाद साधून विशिष्ट उद्दिष्टे साध्य करू शकतात. हे एजंट्स स्वायत्त वर्तन करू शकतात, निर्णय घेऊ शकतात आणि बदलत्या परिस्थितीशी जुळवून घेऊ शकतात. AI एजंट फ्रेमवर्क्सद्वारे सक्षम काही मुख्य क्षमता पाहूया:

- **एजंट सहकार्य आणि समन्वय**: एकापेक्षा जास्त AI एजंट तयार करण्यास सक्षम करा जे एकत्र काम करू शकतात, संवाद साधू शकतात आणि गुंतागुंतीच्या कामांमध्ये समन्वय करू शकतात.
- **कार्य स्वयंचलन आणि व्यवस्थापन**: बहु-टप्प्यांच्या कार्यप्रवाहांचे स्वयंचलन, कार्ये सौपणे, आणि एजंट्समधील डायनॅमिक कार्य व्यवस्थापनासाठी यंत्रणा प्रदान करा.
- **संदर्भात्मक समज आणि जुळवून घेणे**: एजंट्सना संदर्भ समजून घेण्याची, बदलत्या पर्यावरणाशी जुळणारी, आणि वास्तव वेळेतील माहितीच्या आधारे निर्णय घेण्याची क्षमता द्या.

याचा सारांश असा की, एजंट्स तुम्हाला अधिक करण्याची क्षमता देतात, स्वयंचलन पुढील स्तरावर नेऊ शकतात, आणि असे बुद्धिमान सिस्टम तयार करू शकतात जे पर्यावरणापासून शिकून जुळवून घेतात.

## एजंटच्या क्षमतांचा जलद प्रोटोटाइपिंग, पुनरावृत्ती आणि सुधारणा कशी करावी?

हा जलद बदलणारा क्षेत्र आहे, पण बहुतेक AI एजंट फ्रेमवर्क्समध्ये सामान्य काही गोष्टी आहेत ज्या तुम्हाला वेगाने प्रोटोटाइपिंग आणि पुनरावृत्ती करण्यात मदत करतात म्हणजे मॉड्युलर घटक, सहकारी साधने, आणि वास्तविक वेळेतील शिक्षण. चला त्यात बघूया:

- **मॉड्युलर घटक वापरा**: AI SDKs पूर्वनिर्मित घटक ऑफर करतात जसे AI आणि मेमरी कनेक्टर्स, नैसर्गिक भाषा किंवा कोड प्लगइन्सद्वारे फंक्शन कॉलिंग, प्रॉम्प्ट टेम्पलेट्स, आणि बरेच काही.
- **सहकारी साधनांचा वापर करा**: ठराविक भूमिका आणि कार्य असलेले एजंट तयार करा, जे सहकार्यात्मक कार्यप्रवाहांची चाचणी आणि सुधारणा करू शकतील.
- **वास्तविक-वेळेत शिका**: अभिप्राय लूप्स अंमलात आणा जिथे एजंट संवादांमधून शिकतात आणि त्यांचे वर्तन गतिशीलपणे समायोजित करतात.

### मॉड्युलर घटक वापरा

Microsoft Agent Framework सारखे SDKs पूर्वनिर्मित घटक जसे AI कनेक्टर्स, टूल डिफिनेशन्स, आणि एजंट व्यवस्थापन ऑफर करतात.

**टीम्स याचा कसा वापर करू शकतात**: टीम्स ही घटक जलद एकत्र करून कार्यशील प्रोटोटाइप तयार करू शकतात, ज्यामुळे प्रयोग आणि पुनरावृत्ती जलद होते.

**प्रत्यक्षात कसे काम करते**: तुम्ही वापरकर्त्याच्या इनपुटमधून माहिती काढण्यासाठी पूर्वनिर्मित पार्सर वापरू शकता, डेटा साठवण्यासाठी आणि मिळवण्यासाठी मेमरी मॉड्युल, आणि वापरकर्त्यांशी संवाद साधण्यासाठी प्रॉम्प्ट जनरेटर, हे सगळे काही शून्यातून तयार करण्याची गरज नाही.

**उदाहरण कोड**. Microsoft Agent Framework वापरून `FoundryChatClient` सह कसे वापर करायचे हे पाहू, जिथे मॉडेल वापरकर्त्याच्या इनपुटसाठी टूल कॉलिंगसह प्रतिसाद देते:

``` python
# Microsoft Agent Framework Python उदाहरण

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# प्रवासासाठी बुकिंग करण्यासाठी एक नमुना साधन कार्य定义 करा
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # उदाहरण आउटपुट: १ जानेवारी २०२५ रोजी तुमचा न्यू यॉर्क साठी फ्लाइट यशस्वीरीत्या बुक झाला आहे. सुरक्षित प्रवास! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

या उदाहरणातून आपण पाहू शकता की वापरकर्त्याच्या इनपुटमधून महत्त्वाची माहिती उकळण्यासाठी तुम्ही पूर्वनिर्मित पार्सर कसा वापरू शकता, जसे की फ्लाइट बुकिंग विनंतीसाठी उड्डाण स्थान, गंतव्य आणि तारीख. हा मॉड्युलर दृष्टिकोन तुम्हाला उच्च-स्तरीय लॉजिकवर लक्ष केंद्रित करायची मुभा देतो.

### सहकारी साधनांचा वापर करा

Microsoft Agent Framework सारखे फ्रेमवर्क्स अनेक एजंट्सना एकत्र काम करण्यास सुलभ करतात.

**टीम्स याचा कसा वापर करू शकतात**: टीम्स विशिष्ट भूमिका आणि कार्ये असलेले एजंट तयार करू शकतात, ज्यामुळे सहकार्यात्मक कार्यप्रवाहांची चाचणी आणि सुधारणा करणे शक्य होते आणि प्रणालीच्या एकूण कार्यक्षमतेत वाढ होते.

**प्रत्यक्षात कसे काम करते**: तुम्ही एजंट्सची टीम तयार करू शकता जिथे प्रत्येक एजंटचा एक विशेष कार्य असतो, जसे डेटा पुनर्प्राप्ती, विश्लेषण किंवा निर्णय घेणे. हे एजंट्स संवाद साधू शकतात आणि सामायिक माहिती वापरून वापरकर्त्याच्या क्वेरीला उत्तर देणे किंवा कार्य पूर्ण करणे यासारखे लक्ष्य साधू शकतात.

**उदाहरण कोड (Microsoft Agent Framework)**:

```python
# मायक्रोसॉफ्ट एजंट फ्रेमवर्क वापरून एकत्र काम करणारे अनेक एजंट तयार करणे

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# डेटा पुनर्प्राप्ती एजंट
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# डेटा विश्लेषण एजंट
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# एका कार्यावर एजंट्स अनुक्रमे चालवा
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

मागील कोडमध्ये तुम्हाला अनेक एजंट्स एकत्र काम करून डेटा विश्लेषण कसा करतात हे दिसेल. प्रत्येक एजंट विशिष्ट कार्य पार पाडतो, आणि कार्य एजंट्स समन्वयित करून अपेक्षित परिणाम साध्य करण्यासाठी पार पाडले जाते. विशेष भूमिका असलेले समर्पित एजंट तयार करून तुम्ही कार्य कार्यक्षमता आणि कामगिरी सुधारू शकता.

### वास्तविक-वेळेत शिका

प्रगत फ्रेमवर्क्स वास्तविक वेळेतील संदर्भ समज आणि जुळवून घेण्याच्या क्षमता प्रदान करतात.

**टीम्स याचा कसा वापर करू शकतात**: टीम्स अभिप्राय लूप्स अंमलात आणू शकतात जिथे एजंट संवादांमधून शिकतात आणि त्यांचे वर्तन गतिशीलरित्या समायोजित करतात, ज्यामुळे क्षमता सातत्याने सुधारतात.

**प्रत्यक्षात कसे काम करते**: एजंट वापरकर्ता अभिप्राय, पर्यावरणीय डेटा आणि कार्य परिणामांचे विश्लेषण करून त्यांचा ज्ञान आधार अद्यतनीत करतात, निर्णय घेण्याच्या अल्गोरिदम समायोजित करतात, आणि वेळेनुसार कामगिरी सुधारतात. या पुनरावृत्ती शिक्षण प्रक्रियेने एजंट्सना बदलत्या परिस्थिती आणि वापरकर्त्यांच्या प्राधान्यानुसार जुळवून घेण्याची परवानगी मिळते, ज्यामुळे प्रणालीची प्रभावीता वाढते.

## Microsoft Agent Framework आणि Microsoft Foundry Agent Service यामधील फरक काय आहेत?

या दृष्टिकोनांची तुलना करण्याचे अनेक मार्ग आहेत, पण त्यांच्या डिझाईन, क्षमता आणि लक्ष्य वापर केसच्या संदर्भात काही मुख्य फरक पाहूया:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework `FoundryChatClient` वापरून AI एजंट तयार करण्यासाठी एक सुसंगत SDK प्रदान करते. हे डेव्हलपर्सना Azure OpenAI मॉडेल्सशी संबद्ध एजंट तयार करण्यास सक्षम करते ज्यामध्ये अंगभूत टूल कॉलिंग, संभाषण व्यवस्थापन आणि Azure ओळखीद्वारे एंटरप्राइज-ग्रेड सुरक्षा आहे.

**वापर केस**: टूल वापर, बहु-टप्प्यांच्या कार्यप्रवाहांशी संबंधित, आणि एंटरप्राइज एकत्रीकरण दृष्टिकोनांसाठी उत्पादन-तयार AI एजंट तयार करणे.

Microsoft Agent Framework चे काही महत्त्वाचे मुख्य संकल्पना येथे आहेत:

- **एजंट्स**. एजंट `FoundryChatClient` द्वारे तयार केला जातो आणि नाव, सूचना, आणि टूल्ससह कॉन्फिगर केला जातो. एजंट हे करू शकतो:
  - **वापरकर्ता संदेश प्रक्रिया** आणि Azure OpenAI मॉडेल्स वापरून प्रतिसाद तयार करणे.
  - **टूल्स कॉल करणे** संभाषणाच्या संदर्भावर आधारित स्वयंचलितपणे.
  - **संभाषण स्थिती राखणे** अनेक संवादांमध्ये.

  एजंट कसा तयार करायचा हे दाखवणारा कोड स्निपेट:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **टूल्स**. फ्रेमवर्क Python फंक्शन्स म्हणून टूल्स परिभाषित करण्यास समर्थन देतो ज्यांना एजंट स्वयंचलितपणे कॉल करू शकतो. टूल्स एजंट तयार करताना नोंदवले जातात:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **बहु-एजंट समन्वय**. तुम्ही विविध विशेषतांसह अनेक एजंट तयार करू शकता आणि त्यांचे काम समन्वयित करू शकता:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure ओळख एकत्रीकरण**. फ्रेमवर्क सुरक्षित, कीशिवाय प्रमाणीकरणासाठी `AzureCliCredential` (किंवा `DefaultAzureCredential`) वापरतो, ज्यामुळे API की व्यवस्थापनाची गरज नाही.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service हा अलीकडील परिचय आहे, जो Microsoft Ignite 2024 मध्ये सादर करण्यात आला. हे AI एजंट्स विकसित करण्यासाठी आणि तैनात करण्यासाठी अधिक लवचीक मॉडेल्ससह, जसे थेट ओपन-सोर्स LLMs जसे Llama 3, Mistral, आणि Cohere यांना कॉल करण्याची परवानगी देते.

Microsoft Foundry Agent Service मजबूत एंटरप्राइज सुरक्षा यंत्रणा आणि डेटा संग्रहण पद्धती प्रदान करते, ज्यामुळे ते एंटरप्राइज अनुप्रयोगांसाठी योग्य आहे.

हे Microsoft Agent Framework सह आउट-ऑफ-द-बॉक्स काम करते एजंट्स तयार आणि तैनात करण्यासाठी.

हे सेवा सध्या Public Preview मध्ये आहे आणि एजंट तयार करण्यासाठी Python आणि C# यांना समर्थन देते.

Microsoft Foundry Agent Service Python SDK वापरून, वापरकर्ता-परिभाषित टूलसह एजंट तयार करू शकतो:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# टूल फंक्शन्स परिभाषित करा
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### मुख्य संकल्पना

Microsoft Foundry Agent Service खालील मुख्य संकल्पना आहे:

- **एजंट**. Microsoft Foundry Agent Service Microsoft Foundry मध्ये समाकलित आहे. Microsoft Foundry मध्ये, AI एजंट "स्मार्ट" मायक्रोसर्व्हिस म्हणून कार्य करतो, जो प्रश्नांची उत्तरे देऊ शकतो (RAG), क्रिया पार पाडू शकतो, किंवा पूर्ण कार्यप्रवाह स्वयंचलित करू शकतो. हे सर्जनशील AI मॉडेल्सची शक्ती आणि उपकरणे वापरून वास्तविक डेटा स्रोतांशी संवाद साधू शकतो. येथे एजंटचे उदाहरण:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    या उदाहरणात, `gpt-5-mini` मॉडेल, नाव `my-agent`, आणि सूचना `You are helpful agent` यासह एजंट तयार केला आहे. एजंटला कोड इंटरप्रिटेशन टास्कसाठी साधने आणि संसाधने दिली आहेत.

- **थ्रेड आणि संदेश**. थ्रेड ही दुसरी महत्त्वाची संकल्पना आहे. हे एजंट आणि वापरकर्त्यादरम्यान संवाद किंवा परस्परसंवाद दर्शवते. थ्रेडचा वापर संभाषण प्रगती, संदर्भ माहिती संग्रहित करण्यासाठी, आणि परस्परसंवाद स्थिती व्यवस्थापित करण्यासाठी होतो. थ्रेडचे उदाहरण:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # एजंटला थ्रेडवर काम करण्यास सांगा
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # एजंटच्या प्रतिसादासाठी सर्व संदेश काढा आणि लॉग करा
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    मागील कोडमध्ये थ्रेड तयार केला आहे. नंतर, थ्रेडला संदेश पाठवले जातात. `create_and_process_run` कॉल करून, एजंटला थ्रेडवर काम करण्यास सांगितले जाते. शेवटी, संदेश प्राप्त करून एजंटचा प्रतिसाद लॉग केला जातो. हे संदेश वापरकर्ता आणि एजंटमधील संभाषण प्रगती दर्शवतात. संदेश वेगवेगळ्या प्रकारांचे असू शकतात जसे मजकूर, प्रतिमा, किंवा फाइल, म्हणजे एजंटचे काम उदाहरणार्थ प्रतिमा किंवा मजकूर प्रतिसाद दिला आहे. तुम्ही विकासक म्हणून या माहितीलाच पुढील प्रक्रिया किंवा वापरकर्त्यास सादर करू शकता.

- **Microsoft Agent Framework शी समाकलित**. Microsoft Foundry Agent Service Microsoft Agent Framework सह सुरळीत काम करते, म्हणजे तुम्ही `FoundryChatClient` वापरून एजंट तयार करू शकता आणि Agent Service द्वारे उत्पादनात तैनात करू शकता.

**वापर केस**: Microsoft Foundry Agent Service सुरक्षित, स्केलेबल, आणि लवचीक AI एजंट तैनाती आवश्यक असलेल्या एंटरप्राइज अनुप्रयोगांसाठी डिझाइन केलेले आहे.

## या दृष्टिकोनांमधील फरक काय आहे?
 
असे वाटते की काही प्रमाणात ओव्हरलॅप आहे, पण त्यांच्या डिझाइन, क्षमता, आणि लक्ष्य वापर केसदृष्ट्या काही मुख्य फरक आहेत:
 
- **Microsoft Agent Framework (MAF)**: AI एजंट तयार करण्यासाठी उत्पादन-तयार SDK आहे. टूल कॉलिंग, संभाषण व्यवस्थापन, आणि Azure ओळख समाकलनासाठी एक सुसंगत API पुरवतो.
- **Microsoft Foundry Agent Service**: Microsoft Foundry मधील प्लॅटफॉर्म आणि तैनात सेवा आहे. Azure OpenAI, Azure AI Search, Bing Search आणि कोड अंमलबजावणी सारख्या सेवा यांच्यासोबत अंगभूत कनेक्टिव्हिटी देते.
 
अजूनही ठरवू शकत नाहीत कोणता निवडायचा?

### वापर केस
 
काही सामान्य वापर केस पाहून तुम्हाला मदत करू या:
 
> प्रश्न: मी उत्पादन AI एजंट अनुप्रयोग तयार करत आहे आणि लवकर सुरुवात करू इच्छितो
>

>उत्तर: Microsoft Agent Framework ही एक छान निवड आहे. ती `FoundryChatClient` द्वारे सोपी, Python-आधारित API देते जिच्याद्वारे तुम्ही काही ओळींमध्ये टूल्स आणि सूचना देऊन एजंट तयार करू शकता.

>प्रश्न: मला एंटरप्राइज-ग्रेड तैनाती हवीय ज्यात Azure एकत्रीकरण जसे Search आणि कोड अंमलबजावणी समाविष्ट आहेत
>
>उत्तर: Microsoft Foundry Agent Service उत्तम आहे. हे एक प्लॅटफॉर्म सेवा आहे जे अनेक मॉडेल्स, Azure AI Search, Bing Search आणि Azure Functionsसाठी अंगभूत क्षमता पुरवते. Foundry पोर्टलमध्ये एजंट तयार करणे आणि त्यांना प्रमाणात तैनात करणे सोपे करते.
 
> प्रश्न: मी अजूनही गोंधळात आहे, मला एक पर्याय सांग
>
> उत्तर: तुमचे एजंट तयार करण्यासाठी Microsoft Agent Framework वापरून सुरुवात करा, आणि उत्पादनात तैनात आणि प्रमाणात वाढवण्यासाठी Microsoft Foundry Agent Service वापरा. हा दृष्टिकोन तुम्हाला एजंट लॉजिकवर जलद पुनरावृत्ती करण्यास मुभा देतो आणि एंटरप्राइज तैनातीचा स्पष्ट मार्ग देतो.
 
मुख्य फरक सारांश म्हणून एका टेबलमध्ये देत आहोत:

| फ्रेमवर्क | लक्ष केंद्रित | मुख्य संकल्पना | वापर केस |
| --- | --- | --- | --- |
| Microsoft Agent Framework | टूल कॉलिंगसह सुसंगत एजंट SDK | एजंट्स, टूल्स, Azure ओळख | AI एजंट्स तयार करणे, टूल वापर, बहु-टप्पे कार्यप्रवाह |
| Microsoft Foundry Agent Service | लवचीक मॉडेल्स, एंटरप्राइज सुरक्षा, कोड जनरेशन, टूल कॉलिंग | मॉड्युलरिटी, सहकार्य, प्रक्रिया संयोजन | सुरक्षित, स्केलेबल, लवचीक AI एजंट तैनाती |

## माझे विद्यमान Azure इकोसिस्टम टूल्स थेट समाकलित करू शकतो का, की मला स्वतंत्र उपायांची गरज आहे?


होय, आपण आपले विद्यमान Azure परिसंस्था साधने Microsoft Foundry Agent Service सोबत थेट एकत्र करू शकता, विशेषतः हे इतर Azure सेवांसह सलगपणे कार्य करण्यासाठी तयार केलेले आहे. उदाहरणार्थ, आपण Bing, Azure AI Search, आणि Azure Functions एकत्र करू शकता. Microsoft Foundry सोबत देखील खोल एकत्रीकरण आहे.

Microsoft Agent Framework सुद्धा `FoundryChatClient` आणि Azure ओळखद्वारे Azure सेवांसोबत एकत्रित होते, जेणेकरून आपण आपल्या एजंट साधनांमधून थेट Azure सेवा कॉल करू शकता.

## नमुना कोडस्

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI Agent Frameworks बाबत अजून प्रश्न आहेत का?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) मध्ये सामील व्हा, इतर अभ्यासकांशी भेटा, ऑफिस तासात उपस्थित राहा आणि आपले AI Agents संबंधित प्रश्न सोडवा.

## संदर्भ

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## मागील धडा

[AI Agents आणि Agent वापर प्रकरणांची ओळख](../01-intro-to-ai-agents/README.md)

## पुढील धडा

[Agentic Design Patterns समजून घेणे](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->