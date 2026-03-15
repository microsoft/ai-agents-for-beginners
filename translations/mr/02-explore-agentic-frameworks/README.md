[![Exploring AI Agent Frameworks](../../../translated_images/mr/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(या धड्याचा व्हिडिओ पाहण्यासाठी वरील प्रतिमा क्लिक करा)_

# AI एजंट फ्रेमवर्क्स अन्वेषण करा

AI एजंट फ्रेमवर्क्स म्हणजे AI एजंट्सची निर्मिती, तैनात करणे आणि व्यवस्थापन सुलभ करण्यासाठी डिझाइन केलेले सॉफ्टवेअर प्लॅटफॉर्म आहेत. हे फ्रेमवर्क्स विकसकांना पूर्वनिर्मित घटक, सारांश, आणि साधने पुरवतात ज्यामुळे जटिल AI प्रणालींचा विकास सुलभ होतो.

हे फ्रेमवर्क्स विकसकांना त्यांच्या अनुप्रयोगांच्या अनन्य बाबींवर लक्ष केंद्रीत करण्यास मदत करतात जे AI एजंट विकासातील सामान्य आव्हानांसाठी मानकीकृत दृष्टिकोन पुरवतात. ते AI प्रणाली तयार करण्यात स्केलेबिलिटी, प्रवेशयोग्यता, आणि कार्यक्षमतेत वाढ करतात.

## प्रस्तावना

हा धडा खालील गोष्टींची माहिती देईल:

- AI एजंट फ्रेमवर्क्स काय आहेत आणि ते विकसकांना काय साध्य करण्यास सक्षम करतात?
- संघ या फ्रेमवर्क्सचा वापर कसा करून त्यांच्या एजंटच्या क्षमता पटकन प्रोटोटाइप, पुनरावृत्ती, आणि सुधारणा करू शकतात?
- Microsoft कडून तयार केलेल्या फ्रेमवर्क्स आणि साधनांमध्ये काय फरक आहे (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> आणि <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- माझ्या विद्यमान Azure पर्यावरणाच्या साधनांचा थेट समाकलन करता येईल का किंवा स्वतंत्र सोल्यूशन्सची गरज आहे का?
- Azure AI Agents सेवा काय आहे आणि ती मला कशी मदत करत आहे?

## शिकण्याचे उद्दिष्टे

या धड्याचे उद्दिष्टे आहेत की तुम्हाला समजावून देणे:

- AI विकासात AI एजंट फ्रेमवर्क्सची भूमिका.
- बुद्धिमान एजंट तयार करण्यासाठी AI एजंट फ्रेमवर्क्सचा कसा उपयोग करावा.
- AI एजंट फ्रेमवर्क्सद्वारे सक्षम केलेल्या मुख्य क्षमता.
- Microsoft Agent Framework आणि Azure AI Agent Service मधील फरक.

## AI एजंट फ्रेमवर्क्स काय आहेत आणि ते विकसकांना काय करण्यास सक्षम करतात?

पारंपरिक AI फ्रेमवर्क्स तुमच्या अॅप्समध्ये AI समाकलित करण्यात मदत करतात आणि या अॅप्सना खालील प्रकारे सुधारित करतात:

- **वैयक्तिकीकरण**: AI वापरकर्त्याच्या वर्तन आणि पसंतींचा विश्लेषण करून वैयक्तिकृत शिफारसी, सामग्री आणि अनुभव पुरवू शकतो.
उदाहरण: Netflix सारख्या स्ट्रिमिंग सेवांमध्ये AI वापरून दृश्य इतिहासावर आधारित चित्रपट आणि शो सुचवले जातात, ज्यामुळे वापरकर्त्यांचा सहभाग आणि समाधान वाढते.
- **स्वयंचलन आणि कार्यक्षमता**: AI पुनरावृत्तीच्या कामांना स्वयंचलित करू शकतो, कार्यप्रवाह सुलभ करू शकतो आणि कार्यक्षमतेत सुधारणा करू शकतो.
उदाहरण: ग्राहक सेवा अॅप्समध्ये AI-चालित चॅटबॉट्स सामान्य चौकशी हाताळतात, प्रतिसाद वेळ कमी करतात आणि मानवी एजंट्सना गुंतागुंतीच्या समस्यांवर लक्ष केंद्रित करण्यास मोकळे करतात.
- **सुधारित वापरकर्ता अनुभव**: AI वेगळ्या वैशिष्ट्यांनी वापरकर्ता अनुभव सुधारू शकतो जसे की आवाज ओळख, नैसर्गिक भाषा प्रक्रिया, आणि भविष्यसूचक मजकूर.
उदाहरण: Siri आणि Google Assistant सारखे आभासी सहाय्यक AI वापरून आवाज आदेश समजू शकतात आणि प्रतिसाद देतात, ज्यामुळे वापरकर्त्यांना त्यांच्या उपकरणांशी संवाद करणे सुलभ होते.

### हे सगळं छान वाटतयं, मग मग आपल्याला AI एजंट फ्रेमवर्कची का गरज आहे?

AI एजंट फ्रेमवर्क्स हे AI फ्रेमवर्क्सपेक्षा काही वेगळे आहेत. ते बुद्धिमान एजंट तयार करण्यास सक्षम करतात जे वापरकर्त्यांसोबत, इतर एजंट्ससोबत आणि पर्यावरणाशी संवाद साधून विशिष्ट उद्दिष्ट साध्य करतात. हे एजंट्स स्वायत्त वर्तन दाखवू शकतात, निर्णय घेऊ शकतात, आणि बदलत्या स्थितींनुसार जुळवून घेतात. चला AI एजंट फ्रेमवर्क्समुळे सक्षम होणाऱ्या काही मुख्य क्षमतांकडे पाहूया:

- **एजंट सहकार्य आणि समन्वय**: अनेक AI एजंट तयार करू शकतात जे एकत्र काम करतात, संवाद साधतात, आणि जटिल कामे सोडवण्यासाठी समन्वय करतात.
- **कार्य स्वयंचलन आणि व्यवस्थापन**: बहु-चरण कार्यप्रवाह स्वयंचलित करण्यासाठी, कार्य वाटप करण्यासाठी, आणि एजंट्समधील डायनॅमिक कार्य व्यवस्थापनासाठी प्रणाली पुरवतात.
- **सांदर्भिक समज आणि जुळवून घेणे**: एजंट्सना संदर्भ समजून घेण्याची, बदलत्या वातावरणाला जुळवून घेण्याची, आणि वास्तविक वेळेतील माहितीवर आधारित निर्णय घेण्याची क्षमता देतात.

थोडक्यात, एजंट तुम्हाला अधिक करण्यास सक्षम करतात, स्वयंचलन पुढच्या पातळीवर घेऊन जातात, आणि अधिक बुद्धिमान प्रणाली तयार करतात जी त्यांच्या वातावरणापासून शिकू आणि जुळवून घेऊ शकतात.

## एजंटच्या क्षमतांना जलद प्रोटोटाइप, पुनरावृत्ती आणि सुधारण्याचा कसा मार्ग आहे?

ही एक वेगवान बदलणारी क्षेत्र आहे, पण बर्‍याच AI एजंट फ्रेमवर्क्समध्ये काही सामान्य गोष्टी आहेत ज्या तुम्हाला जलद प्रोटोटाइप तयार करण्यास आणि पुनरावृत्ती करण्यास मदत करतात म्हणजेच मॉड्युलर घटक, सहकार्य साधने, आणि वास्तविक-वेळ शिकणे. चला यापैकी काहीकडे पाहूया:

- **मॉड्युलर घटक वापरा**: AI SDKs पूर्वनिर्मित घटक जसे की AI आणि मेमरी कनेक्टर्स, नैसर्गिक भाषा किंवा कोड प्लगइन्सद्वारे फंक्शन कॉलिंग, प्रॉम्प्ट टेम्पलेट्स, आणि बरेच काही ऑफर करतात.
- **सहकारी साधने वापरा**: विशिष्ट भूमिका आणि कार्यांसह एजंट डिझाईन करा ज्यामुळे ते सहकार्य करणाऱ्या कार्यप्रवाहांची चाचणी आणि सुधारणा करू शकतात.
- **वास्तविक-वेळ शिकणे**: फीडबॅक लूप्स स्थापित करा जिथे एजंट संवादांतून शिकतात आणि त्यांचे वर्तन गतिशीलपणे समायोजित करतात.

### मॉड्युलर घटक वापरा

Microsoft Agent Framework सारखे SDKs पूर्वनिर्मित घटक पुरवतात जसे की AI कनेक्टर्स, साधन व्याख्या, आणि एजंट व्यवस्थापन.

**संघ कसे वापरू शकतात**: संघ हे घटक जलद एकत्र करून कार्यक्षम प्रोटोटाइप तयार करू शकतात, ज्यामुळे प्रायोगिक व पुनरावृत्तीची प्रक्रिया जलद होते.

**प्रत्यक्ष कसे कार्य करते**: तुम्ही वापरकर्त्याच्या इनपुटमधून माहिती काढण्यासाठी पूर्वनिर्मित पार्सर, डेटा संग्रहित व पुनर्प्राप्त करण्यासाठी मेमरी मॉड्युल, आणि वापरकर्त्यांशी संवाद साधण्यासाठी प्रॉम्प्ट जनरेटर यांचा वापर करू शकता, आणि हे सगळे सुरुवातीपासून तयार करण्याची गरज नाही.

**कोड उदाहरण**. चला Microsoft Agent Framework शी `AzureAIProjectAgentProvider` वापरून वापरकर्त्याच्या इनपुटवर टूल कॉलिंगसह प्रतिसाद देण्याचा एक उदाहरण पाहूया:

``` python
# Microsoft Agent Framework Python उदाहरण

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# प्रवास बुक करण्यासाठी एक नमुना साधन फंक्शन परिभाषित करा
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # उदाहरण आउटपुट: आपली 1 जानेवारी, 2025 रोजी न्यूयॉर्कसाठी फ्लाइट यशस्वीरित्या बुक झाली आहे. सुरक्षित प्रवास! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

या उदाहरणातून तुम्हाला दिसेल की तुम्ही वापरकर्त्याच्या इनपुटमधून फ्लाइट बुकिंग विनंतीचा स्रोत, ठिकाण, आणि तारीख यासारखी महत्त्वाची माहिती काढण्यासाठी पूर्वनिर्मित पार्सर कसा वापरू शकता. हा मॉड्युलर दृष्टिकोन तुम्हाला उच्च-स्तरीय लॉजिकवर लक्ष देण्याची संधी देतो.

### सहकारी साधने वापरा

Microsoft Agent Framework सारखे फ्रेमवर्क्स अनेक एजंट्सना एकत्र काम करण्यास पुरवठा करतात.

**संघ कसे वापरू शकतात**: संघ विशिष्ट भूमिका आणि कार्यांसह एजंट डिझाईन करू शकतात, ज्यामुळे ते सहकार्य कार्यप्रवाहांची चाचणी व सुधारणा करू शकतात आणि संपूर्ण प्रणालीची कार्यक्षमता वाढवू शकतात.

**प्रत्यक्ष कसे कार्य करते**: तुम्ही एजंट्सचा एक संघ तयार करू शकता जिथे प्रत्येक एजंटची विशिष्ट कामगिरी असते, जसे डेटा पुनर्प्राप्ती, विश्लेषण, किंवा निर्णय घेणे. हे एजंट्स संवाद साधू शकतात आणि समान उद्दिष्ट साध्य करण्यासाठी माहिती शेअर करतात, जसे की वापरकर्त्याच्या प्रश्नाचे उत्तर देणे किंवा एखादे कार्य पूर्ण करणे.

**कोड उदाहरण (Microsoft Agent Framework)**:

```python
# Microsoft Agent Framework वापरून एकत्र काम करणारे अनेक एजंट तयार करणे

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# डेटा पुनर्प्राप्ती एजंट
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# डेटा विश्लेषण एजंट
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# एखाद्या कामावर एजंटांना क्रमाने चालवा
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

या पूर्वीच्या कोडमध्ये तुम्हाला दिसेल की अनेक एजंट्स एकत्र काम करून डेटा विश्लेषण करत आहेत. प्रत्येक एजंट विशिष्ट काम करतो आणि कार्याचा समन्वय साधून इच्छित निकाल प्राप्त केला जातो. विशेष भूमिका असलेले समर्पित एजंट तयार करून तुम्ही कार्यक्षमतेमध्ये आणि कामगिरीत सुधारणा करू शकता.

### वास्तविक-वेळ शिकणे

अत्याधुनिक फ्रेमवर्क्स वास्तविक-वेळ संदर्भ समज आणि जुळवून घेण्याच्या क्षमतांची पूर्तता करतात.

**संघ कसे वापरू शकतात**: संघ फीडबॅक लूप्स लागू करू शकतात जिथे एजंट संवादांतून शिकतात आणि त्यांचे वर्तन गतिशीलरीतीने बदलतात, ज्यामुळे क्षमता सातत्याने सुधारल्या जातात.

**प्रत्यक्ष कसे कार्य करते**: एजंट वापरकर्त्यांच्या अभिप्राय, पर्यावरणीय डेटा, आणि कार्य निकालाचा विश्लेषण करून त्यांच्या ज्ञानाच्या आधारात सुधारणा करतात, निर्णय घेण्यासाठीचे अल्गोरिदम समायोजित करतात, आणि कालांतराने कार्यक्षमता वाढवतात. ही पुनरावृत्ती शिकण्याची प्रक्रिया एजंट्सना बदलत्या परिस्थितींशी आणि वापरकर्त्यांच्या पसंतींशी जुळवून घेण्यास मदत करते, ज्यामुळे संपूर्ण प्रणाली अधिक परिणामकारक बनते.

## Microsoft Agent Framework आणि Azure AI Agent Service यामध्ये काय फरक आहे?

हे दृष्टिकोन कसे वेगळे आहेत याची तुलना करणे अनेक मार्गांनी करता येते, पण त्यांच्या डिझाइन, क्षमता, आणि लक्षित वापर प्रकरणांच्या दृष्टीने काही मुख्य फरक पाहूया:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework हा AI एजंट तयार करण्यासाठी एक सुलभ SDK आहे जो `AzureAIProjectAgentProvider` वापरतो. तो विकसकांना Azure OpenAI मॉडेल्सचा लाभ घेऊन टूल कॉलिंग, संभाषण व्यवस्थापन, आणि Azure ओळख नियंत्रणाद्वारे एंटरप्राइझ-ग्रेड सुरक्षा प्रदान करणारे एजंट तयार करण्याची परवानगी देतो.

**वापर प्रकरणे**: टूल वापर, बहु-चरण कार्यप्रवाह, आणि एंटरप्राइझ समाकलन परिदृश्यांसह उत्पादन-तयार AI एजंट तयार करणे.

Microsoft Agent Framework मधील महत्त्वाच्या मूलभूत संकल्पना:

- **एजंट्स**. एक एजंट `AzureAIProjectAgentProvider` द्वारे तयार केला जातो आणि नाव, सूचना, आणि साधनांनी कॉन्फिगर केला जातो. एजंट:

  - वापरकर्त्यांचे संदेश प्रक्रिया करतो आणि Azure OpenAI मॉडेल्स वापरून प्रतिसाद तयार करतो.
  - संभाषण संदर्भानुसार उपकरण स्वयंचलितपणे कॉल करतो.
  - अनेक संवादांमध्ये संभाषण स्थिती राखतो.

  एजंट तयार करण्यासाठी कोडचा एक तुकडा:

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **साधने**. फ्रेमवर्क एजंट्सना आपोआप कॉल करता येणाऱ्या Python फंक्शन्स म्हणून साधने व्याख्यायित करण्यास समर्थन करतो. साधने एजंट तयार करताना नोंदणी केली जातात:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **बहु-एजंट समन्वय**. तुम्ही वेगवेगळ्या विशेषतांसह अनेक एजंट तयार करू शकता आणि त्यांचे काम समन्वयित करू शकता:

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure ओळख समाकलन**. फ्रेमवर्क सुरक्षित, कीशिवाय प्रमाणीकरणासाठी `AzureCliCredential` (किंवा `DefaultAzureCredential`) वापरतो, ज्यामुळे API की थेट व्यवस्थापित करण्याची गरज नाही.

## Azure AI Agent Service

Azure AI Agent Service ही Microsoft Ignite 2024 मध्ये सादर केलेली नवीन सेवा आहे. ती अधिक लवचिक मॉडेल्ससह AI एजंटचा विकास आणि तैनात करण्याची अनुमती देते, उदा. Llama 3, Mistral, आणि Cohere सारख्या ओपन-सोर्स LLMs थेट कॉल करण्याची क्षमता.

Azure AI Agent Service मजबूत एंटरप्राइझ सुरक्षा प्रणाली आणि डेटा संग्रहण पद्धती पुरवते, ज्यामुळे ती एंटरप्राइझ अनुप्रयोगांसाठी योग्य ठरते.

ही सेवा Microsoft Agent Framework सह आउट-ऑफ-द-बॉक्स काम करते ज्याद्वारे एजंट तयार करणे आणि तैनात करणे शक्य आहे.

ही सेवा सध्या सार्वजनिक प्रीव्ह्यूमध्ये आहे आणि एजंट तयार करण्यासाठी Python आणि C# समर्थन करते.

Azure AI Agent Service Python SDK वापरून, आपण वापरकर्त्याने परिभाषित केलेले साधन असलेला एजंट तयार करू शकतो:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# साधनांची कार्ये परिभाषित करा
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
        model="gpt-4o-mini",
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

### मूलभूत संकल्पना

Azure AI Agent Service मध्ये खालील मुख्य संकल्पना आहेत:

- **एजंट**. Azure AI Agent Service Microsoft Foundry बरोबर समाकलित आहे. AI Foundry मध्ये, AI एजंट हा एक "स्मार्ट" मायक्रोसर्व्हिस आहे जो प्रश्नांची उत्तरे देऊ शकतो (RAG), क्रिया पार पाडू शकतो, किंवा कार्यप्रवाह पूर्णपणे स्वयंचलित करू शकतो. तो निर्मिती AI मॉडेल्सच्या शक्तीला साधने जोडून प्राप्त करतो ज्याद्वारे तो वास्तविक डेटा स्रोतांशी प्रवेश आणि संवाद साधू शकतो. येथे एजंटचे उदाहरण आहे:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    या उदाहरणात, एजंट `gpt-4o-mini` मॉडेलसह, नाव `my-agent`, आणि सूचना `You are helpful agent` सह तयार केला गेला आहे. एजंटला कोड इंटरप्रिटेशन कार्य पार पाडण्यासाठी साधने आणि संसाधने असलेली आहे.

- **थ्रेड आणि संदेश**. थ्रेड हाही एक महत्त्वाचा संकल्पना आहे. तो एजंट आणि वापरकर्त्यांमधील संवाद किंवा परस्परसंवाद दर्शवतो. थ्रेड्स वापरून संभाषणाची प्रगती ट्रॅक करता येते, संदर्भ माहिती संग्रहित करता येते, आणि संवादाची अवस्था व्यवस्थापित करता येते. येथे थ्रेडचे उदाहरण आहे:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    आधीच्या कोडमध्ये थ्रेड तयार केला जातो. नंतर, थ्रेडला संदेश पाठवले जातात. `create_and_process_run` कॉल करून, एजंटला थ्रेडवर काम करण्यास सांगितले जाते. शेवटी, संदेश घेऊन एजंटच्या प्रतिसादाची नोंद घेतली जाते. हे संदेश वापरकर्ता आणि एजंट यांच्यातील संभाषणाची प्रगती दर्शवतात. तसेच हे समजणे महत्त्वाचे आहे की संदेश वेगवेगळ्या प्रकारांचे असू शकतात उदा. मजकूर, प्रतिमा, किंवा फाइल, म्हणजे एजंटचे कार्य एखाद्या प्रतिमा किंवा मजकूर प्रतिसाद स्वरुपात आहे. विकसक म्हणून, नंतर तुम्ही या माहितीचा उपयोग प्रतिसाद अधिक प्रक्रिया करण्यासाठी किंवा वापरकर्त्यास सादर करण्यासाठी करू शकता.

- **Microsoft Agent Framework सह समाकलित**. Azure AI Agent Service Microsoft Agent Framework सोबत सुरळीत कार्य करते, म्हणजे तुम्ही `AzureAIProjectAgentProvider` वापरून एजंट तयार करू शकता आणि उत्पादनासाठी Agent Service मध्ये तैनात करू शकता.

**वापर प्रकरणे**: Azure AI Agent Service सुरक्षित, स्केलेबल, आणि लवचिक AI एजंट तैनात करण्यासाठी एंटरप्राइझ अनुप्रयोगांसाठी डिझाइन केलेली आहे.

## या दृष्टिकोनांमधील फरक काय आहे?

काही प्रमाणात यामध्ये ओव्हरलॅप आहे, पण डिझाइन, क्षमता, आणि वापर प्रकरणांच्या दृष्टीने काही महत्त्वाचे फरक आहेत:

- **Microsoft Agent Framework (MAF)**: AI एजंट तयार करण्यासाठी उत्पादन-तयार SDK आहे. टूल कॉलिंग, संभाषण व्यवस्थापन, आणि Azure ओळख समाकलनासाठी सुलभ API पुरवतो.
- **Azure AI Agent Service**: Azure Foundry मधील प्लॅटफॉर्म आणि तैनात करण्याची सेवा आहे. Azure OpenAI, Azure AI Search, Bing Search, आणि कोड कार्यान्वयन यांसारख्या सेवांशी अंतर्निर्मित कनेक्टिव्हिटी पुरवतो.

अजूनही नक्की काय निवडायचे हे ठरवू शकत नसल्यास?

### वापर प्रकरणे

चला काही सामान्य वापर प्रकरणे पाहू:

> प्रश्न: मी उत्पादन AI एजंट अनुप्रयोग तयार करत आहे आणि लवकर सुरुवात करू इच्छितो.
>

> उत्तर: Microsoft Agent Framework उत्तम पर्याय आहे. तो `AzureAIProjectAgentProvider` द्वारे साधे, Python-आधारित API पुरवतो ज्याद्वारे तुम्ही काही ओळींमध्ये एजंट्सचे साधने आणि सूचना परिभाषित करू शकता.

> प्रश्न: मला Azure एकत्रिकरणांबरोबर एंटरप्राइझ-ग्रेड तैनाती हवी आहे जसे की Search आणि कोड अंमलबजावणी.
>
> उत्तर: Azure AI Agent Service सर्वोत्तम आहे. ही एक प्लॅटफॉर्म सेवा आहे जी अनेक मॉडेल्स, Azure AI Search, Bing Search, आणि Azure Functions साठी अंतर्निर्मित क्षमता पुरवते. तुम्ही Foundry Portal मध्ये तुम्हाचे एजंट तयार आणि मोठ्या प्रमाणावर तैनात करू शकता.

> प्रश्न: मी अजूनही गोंधळलेलो आहे, मला कोणता एक पर्याय द्या.
>
> उत्तर: Microsoft Agent Framework वापरून तुमचे एजंट तयार करा आणि उत्पादनात तैनात करण्यासाठी नंतर Azure AI Agent Service वापरा. या पद्धतीने तुम्ही तुमच्या एजंट लॉजिकवर पटकन पुनरावृत्ती करू शकता आणि एंटरप्राइझ तैनातीसाठी स्पष्ट मार्ग ठेवू शकता.

चला महत्त्वाचे फरक सारणीमध्ये पाहूया:

| फ्रेमवर्क | लक्ष केंद्रित | मुख्य संकल्पना | वापर प्रकरणे |
| --- | --- | --- | --- |
| Microsoft Agent Framework | टूल कॉलिंगसह सुलभ एजंट SDK | एजंट्स, साधने, Azure ओळख | AI एजंट तयार करणे, टूल वापर, बहु-चरण कार्यप्रवाह |
| Azure AI Agent Service | लवचिक मॉडेल्स, एंटरप्राइझ सुरक्षा, कोड जनरेशन, टूल कॉलिंग | मॉड्युलरिटी, सहकार्य, प्रक्रिया आयोजन | सुरक्षित, स्केलेबल, आणि लवचिक AI एजंट तैनाती |

## माझ्या विद्यमान Azure पर्यावरणातील साधनांचा थेट समाकलन करू शकतो का किंवा मला स्वतंत्र सोल्यूशन्सची गरज आहे?
उत्तर होय आहे, आपण आपल्या विद्यमान Azure इकोसिस्टम टूल्स थेट Azure AI Agent Service शी एकत्रित करू शकता, विशेषतः, कारण हे अन्य Azure सेवांसह सहजपणे काम करण्यासाठी तयार केले गेले आहे. उदाहरणार्थ, आपण Bing, Azure AI Search, आणि Azure Functions एकत्रित करू शकता. Microsoft Foundry सह देखील सखोल एकत्रीकरण आहे.

Microsoft Agent Framework देखील `AzureAIProjectAgentProvider` आणि Azure ओळखीच्या माध्यमातून Azure सेवांसोबत एकत्रित होते, ज्यामुळे आपण आपल्या एजंट टूल्समधून थेट Azure सेवांना कॉल करू शकता.

## Sample Codes

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Got More Questions about AI Agent Frameworks?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) मध्ये सामील व्हा, इतर शिकणाऱ्यांशी भेटा, ऑफिस तासांत सहभागी व्हा आणि आपल्या AI Agents शी संबंधित प्रश्नांवर उत्तर मिळवा.

## References

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## Previous Lesson

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## Next Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अपूर्णता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वपूर्ण माहिती साठी व्यावसायिक मानवी भाषांतर करण्याचा सल्ला दिला जातो. या भाषांतराचा वापर केल्यामुळे झालेल्या कोणत्याही गैरसमजुती किंवा चुकांसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->