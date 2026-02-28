[![AI एजंट फ्रेमवर्क्स एक्सप्लोर करणे](../../../translated_images/mr/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(या धड्याचा व्हिडिओ पाहण्यासाठी वरील प्रतिमेवर क्लिक करा)_

# AI एजंट फ्रेमवर्क्स एक्सप्लोर करा

AI एजंट फ्रेमवर्क्स म्हणजे असे सॉफ्टवेअर प्लॅटफॉर्म्स जे AI एजंट्सच्या निर्मिती, तैनाती आणि व्यवस्थापनास सुलभ करतात. हे फ्रेमवर्क्स डेव्हलपर्सना पूर्वनिर्मित घटक, अमूर्त मॉडेल्स आणि साधने प्रदान करतात जे क्लिष्ट AI प्रणालीच्या विकासाची साधना सुलभरित्या करतात.

हे फ्रेमवर्क्स डेव्हलपर्सना त्यांच्या अनुप्रयोगांच्या अनन्य बाबींवर लक्ष केंद्रित करण्यास मदत करतात, AI एजंट विकासातील सामान्य आव्हानांसाठी प्रमाणित पद्धती प्रदान करून. हे AI प्रणालीच्या स्केलेबिलिटी, प्रवेशयोग्यता आणि कार्यक्षमतेत सुधारणा करतात.

## परिचय 

हा धडा खालील गोष्टी सांभाळेल:

- AI एजंट फ्रेमवर्क्स काय आहेत आणि डेव्हलपर्सना काय साध्य करायला देते?
- टीम्स हे कसे जलद स्वरूप तयार करण्यासाठी, पुनरावृत्ती करण्यासाठी आणि त्यांचे एजंट क्षमतांनी कसे सुधारणा करु शकतात?
- Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> आणि <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) द्वारे तयार केलेल्या फ्रेमवर्क्स आणि साधनांमध्ये काय फरक आहे?
- मी माझ्या विद्यमान Azure परिसंस्थेतील साधने थेट एकत्र करू शकतो का, किंवा स्वतंत्र उपाययोजना गरजेच्या आहेत का?
- Azure AI Agents सेवा काय आहे आणि ती मला कशी मदत करत आहे?

## शिकण्याची उद्दिष्टे

या धड्याचा उद्देश तुम्हाला समजावून सांगणे आहे:

- AI विकासात AI एजंट फ्रेमवर्क्सची भूमिका.
- बुद्धिमान एजंट तयार करण्यासाठी AI एजंट फ्रेमवर्क्सचा उपयोग कसा करावा.
- AI एजंट फ्रेमवर्क्सद्वारे सक्षम केलेल्या मुख्य क्षमता.
- Microsoft Agent Framework आणि Azure AI Agent Service मधील फरक.

## AI एजंट फ्रेमवर्क्स काय आहेत आणि ते डेव्हलपर्सना काय साध्य करायला देते?

परंपरागत AI फ्रेमवर्क्स तुमच्या अॅप्समध्ये AI समाकलित करण्यास मदत करु शकतात आणि खालील प्रकारे या अॅप्स सुधारू शकतात:

- **व्यक्तिमत्वीकरण**: AI वापरकर्त्याच्या वर्तन आणि पसंतींचा विश्लेषण करु शकतो आणि वैयक्तिक शिफारसी, सामग्री आणि अनुभव प्रदान करतो.
उदाहरण: Netflix सारख्या स्ट्रीमिंग सेवा AI वापरकर्त्यांच्या पाहण्याच्या इतिहासावर आधारित चित्रपट आणि शो सुचवतात, ज्यामुळे वापरकर्त्यांचा सहभाग आणि समाधान वाढतो.
- **स्वयंचलन आणि कार्यक्षमतेत वाढ**: AI पुनरावृत्तीचे कार्य स्वयंचलित करु शकतो, कामकाज सुलभ करू शकतो आणि ऑपरेशनल कार्यक्षमता सुधारू शकतो.
उदाहरण: ग्राहक सेवा अॅप्स AI-चालित चॅटबॉटचा वापर करून सामान्य प्रश्नांना हाताळतात, प्रतिसाद वेळ कमी करतात आणि जास्त गुंतागुंतीच्या मुद्द्यांसाठी मानवी एजंटना मोकळ्या करतात.
- **संपूर्ण वापरकर्ता अनुभव सुधारणा**: AI आवाज ओळख, नैसर्गिक भाषा प्रक्रिया, आणि भाकीत ọrọ सारख्या बुद्धिमान वैशिष्ट्ये प्रदान करून एकूण वापरकर्ता अनुभव सुधारू शकतो.
उदाहरण: Siri आणि Google Assistant सारखे वर्चुअल सहाय्यक AI वापरून आवाज आदेश समजून घेतात आणि प्रतिसाद देतात, ज्यामुळे वापरकर्त्यांसाठी उपकरणांशी संवाद करणे सोपे होते.

### सारे छान वाटत आहे, मग आपल्याला AI एजंट फ्रेमवर्क का आवश्यक आहे?

AI एजंट फ्रेमवर्क्स हे फक्त AI फ्रेमवर्क्सपेक्षा काहीतरी वेगळे आहेत. ते बुद्धिमान एजंट्स तयार करण्यासाठी डिझाइन केले गेले आहेत, जे वापरकर्ते, इतर एजंट्स आणि पर्यावरणाशी संवाद साधू शकतात आणि ठराविक ध्येय साध्य करू शकतात. हे एजंट स्वायत्त वर्तन दाखवू शकतात, निर्णय घेऊ शकतात, आणि बदलत्या परिस्थितींशी जुळवून घेऊ शकतात. चला AI एजंट फ्रेमवर्क्सने सक्षम केलेल्या काही मुख्य क्षमतांकडे पाहू:

- **एजंट सहकार्य आणि समन्वय**: अनेक AI एजंट्स तयार करणे जे एकत्र काम करू शकतात, संवाद साधू शकतात आणि जटिल कार्ये सोडवण्यासाठी समन्वय करू शकतात.
- **कार्य स्वयंचलन आणि व्यवस्थापन**: बहु-चरण प्रक्रियेचे स्वयंचलन, कार्यांचे प्रतिनिधित्व, आणि एजंट्समधील गतिशील कार्य व्यवस्थापनासाठी यंत्रणा प्रदान करणे.
- **संदर्भात्मक समज आणि जुळणी**: एजंटना संदर्भ समजून घेण्याची, बदलत्या पर्यावरणाशी जुळवून घेण्याची, आणि वास्तविक वेळेतील माहितीवर आधारित निर्णय घेण्याची क्षमता प्रदान करणे.

सारांश म्हणजे, एजंट तुम्हाला अधिक करण्याची परवानगी देतात, स्वयंचलन पुढील स्तरावर नेण्याची, अधिक बुद्धिमान प्रणाली तयार करण्याची आणि त्यांचे पर्यावरणातून शिकण्याची क्षमता असलेली प्रणाली तयार करण्याची.

## एजंटच्या क्षमतांचा जलद प्रोटोटायपिंग, पुनरावृत्ती आणि सुधार कसा करावा?

हा एक वेगवान बदलणारा क्षेत्र आहे, पण बहुतेक AI एजंट फ्रेमवर्क्समध्ये काही सामान्य बाबी आहेत ज्या तुम्हाला जलद प्रोटोटाइपिंग आणि पुनरावृत्ती करायला मदत करतात, म्हणजे मॉड्यूलर घटक, सहकारी साधने, आणि वास्तविक वेळेतील शिक्षण. चला त्याचा सखोल अभ्यास करू:

- **मॉड्यूलर घटक वापरा**: AI SDK पूर्वनिर्मित घटक ऑफर करतात जसे AI आणि मेमरी कनेक्टर्स, नैसर्गिक भाषा किंवा कोड प्लगइन्स वापरून फंक्शन कॉलिंग, प्रॉम्प्ट टेम्पलेट्स, आणि बरेच काही.
- **सहकार्यात्मक साधने वापरा**: विशिष्ट भूमिका आणि कार्यांसह एजंट डिझाइन करा, ज्यामुळे ते सहकारी कार्यप्रवाहांची चाचणी आणि सुधारणा करु शकतील.
- **वास्तविक-वेळेत शिका**: अभिप्राय लूप्स अंमलात आणा जिथे एजंट संवादांमधून शिकतात आणि त्यांचे वर्तन गतिशीलपणे समायोजित करतात.

### मॉड्यूलर घटक वापरा

Microsoft Agent Framework सारख्या SDK पूर्वनिर्मित घटक जसे AI कनेक्टर्स, साधन व्याख्याने, आणि एजंट व्यवस्थापन ऑफर करतात.

**टीम्स याचा कसा उपयोग करू शकतात**: टीम्स या घटकांना जलद गोळा करून कार्यक्षम प्रोटोटाइप तयार करू शकतात, ज्यामुळे सुरुवातीपासून न करता जलद प्रयोग आणि पुनरावृत्ती शक्य होते.

**हे प्रत्यक्षात कसे कार्य करते**: तुम्ही वापरकर्ता इनपुटमधून माहिती काढण्यासाठी पूर्वनिर्मित पार्सर वापरू शकता, माहिती साठवण्यासाठी आणि पुनर्प्राप्तीसाठी मेमरी मॉड्यूल वापरू शकता, आणि वापरकर्त्यांशी संपर्क साधण्यासाठी प्रॉम्प्ट जनरेटर वापरू शकता, आणि सगळे हे घटक सुरुवातीपासून तयार करायची गरज नाही.

**उदाहरण कोड**. चला पाहूया Microsoft Agent Framework कसा वापरायचा `AzureAIProjectAgentProvider` वापरून वापरकर्त्याच्या इनपुटवर टूल कॉलिंगसह प्रतिक्रीया देण्यासाठी:

``` python
# Microsoft एजंट फ्रेमवर्क पायथन उदाहरण

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# प्रवास आरक्षण करण्यासाठी एक नमुना साधन फंक्शन परिभाषित करा
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
    # उदाहरण आउटपुट: 1 जानेवारी, 2025 रोजी न्यूयॉर्ककडे तुमची फ्लाइट यशस्वीरित्या बुक झाली आहे. शुभ प्रवास! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

तुम्हाला या उदाहरणातून दिसेल कसे तुम्ही वापरकर्ता इनपुटमधून महत्त्वाची माहिती काढण्यासाठी पूर्वनिर्मित पार्सरचा उपयोग करू शकता, जसे की उडाण बुकिंगच्या मूळ, गंतव्य आणि तारीख. हा मॉड्यूलर दृष्टिकोन तुम्हाला उच्च स्तराच्या लॉजिकवर लक्ष केंद्रित करण्यास अनुमती देतो.

### सहकार्यक्षमता साधने वापरा

Microsoft Agent Framework सारखे फ्रेमवर्क बहुतेक एजंट तयार करण्यास मदत करतात जे एकत्र काम करू शकतात.

**टीम्स याचा कसा उपयोग करू शकतात**: टीम्स विशिष्ट भूमिका आणि कार्यांसाठी एजंट डिझाइन करू शकतात, ज्यामुळे ते सहकारी कार्यप्रवाहांची चाचणी आणि सुधारणे करू शकतील आणि संपूर्ण प्रणाली कार्यक्षमता सुधारू शकते.

**हे प्रत्यक्षात कसे कार्य करते**: तुम्ही एजंट्सचा एक संघ तयार करू शकता ज्यामध्ये प्रत्येक एजंटला विशिष्ट कार्य असते, जसे डेटा प्राप्त करणे, विश्लेषण करणे, किंवा निर्णय घेणे. हे एजंट्स संवाद साधू शकतात आणि सामान्य ध्येय साध्य करण्यासाठी माहिती सामायिक करू शकतात, जसे वापरकर्त्याच्या प्रश्नाचे उत्तर देणे किंवा एखादे कार्य पूर्ण करणे.

**उदाहरण कोड (Microsoft Agent Framework)**:

```python
# मायक्रोसॉफ्ट एजंट फ्रेमवर्क वापरून एकत्र काम करणारे अनेक एजंट तयार करणे

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

# एखाद्या कार्यावर एजंट्सना अनुक्रमे चालवणे
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

यापूर्वीच्या कोडमध्ये तुम्हाला दिसेल कसे तुम्ही एक कार्य तयार करू शकता ज्यामध्ये अनेक एजंट्स एकत्र काम करतात डेटा विश्लेषणासाठी. प्रत्येक एजंट विशेष जबाबदारी पार पाडतो, आणि कार्य एजंट्सच्या समन्वयाने पार पाडले जाते जेणेकरून अपेक्षित परिणाम साध्य होईल. विशिष्ट भूमिका असलेल्या समर्पित एजंट्स तयार करून तुम्ही कार्याची कार्यक्षमता आणि कार्यप्रदर्शन सुधारू शकता.

### वास्तविक वेळेतील शिक्षण

सश्रृंखल फ्रेमवर्क वास्तविक वेळेतील संदर्भ समज आणि जुळणीसाठी क्षमता प्रदान करतात.

**टीम्स याचा कसा उपयोग करू शकतात**: टीम्स अभिप्राय लूप्सची अंमलबजावणी करू शकतात जिथे एजंट संवादांमधून शिकतात आणि त्यांचे वर्तन गतिशीलपणे सुधारतात, ज्यामुळे क्षमता सुरेख टप्प्याटप्प्याने विकास होते.

**हे प्रत्यक्षात कसे कार्य करते**: एजंट्स वापरकर्त्याचा अभिप्राय, पर्यावरणीय डेटा, आणि कार्य परिणामांचे विश्लेषण करु शकतात, त्यांचे ज्ञानसंग्रह अद्यतनित करू शकतात, निर्णय घेण्याच्या अल्गोरिदममध्ये सुधारणा करू शकतात, आणि कालांतराने कार्यक्षमतेत वाढ करतात. हा पुनरावृत्तीक्षम शिक्षण प्रक्रिया एजंट्सना बदलत्या परिस्थिती आणि वापरकर्ता पसंतींशी जुळवून घेण्यास अनुमती देते, परिणामी एकूण प्रणाली कार्यक्षमतेत वाढ होते.

## Microsoft Agent Framework आणि Azure AI Agent Service यामधील फरक काय?

या दृष्टिकोनांची तुलना करण्याचे अनेक मार्ग आहेत, पण त्यांचे डिझाइन, क्षमता आणि लक्ष्य वापराच्या बाबतीत काही महत्त्वाचे फरक आहेत:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework `AzureAIProjectAgentProvider` वापरून AI एजंट तयार करण्यासाठी एक सुलभ SDK प्रदान करतो. हे डेव्हलपर्सना Azure OpenAI मॉडेल्सचा उपयोग करणारे एजंट तयार करण्यास अनुमती देते जे टूल कॉलिंग, संभाषण व्यवस्थापन, आणि Azure ओळख प्रणालीद्वारे एंटरप्राइझ-ग्रेड सुरक्षा यांसह येतात.

**वापर प्रकरणे**: टूल वापर, बहु-चरण कार्यप्रवाह, आणि एंटरप्राइझ एकत्रीकरणासाठी उत्पादन-तयार AI एजंट तयार करणे.

Microsoft Agent Framework ची काही महत्त्वाची मूलभूत संकल्पना:

- **एजंट्स**. एजंट `AzureAIProjectAgentProvider` द्वारे तयार केला जातो आणि नाव, सूचना, आणि टूल्ससह सानुकूलित केला जातो. एजंट खालील करू शकतो:
  - **वापरकर्ता संदेश प्रक्रिया करणे** आणि Azure OpenAI मॉडेल्स वापरून प्रतिसाद तयार करणे.
  - **संवादाच्या संदर्भानुसार टूल्स कॉल करणे** स्वयंचलितपणे.
  - **अनेक संवादांमध्ये संभाषण स्थिती राखणे**.

  एजंट तयार करण्यासाठी कोडस्निपेट येथे आहे:

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

- **टूल्स**. फ्रेमवर्क Python फंक्शन्स म्हणून टूल्स परिभाषित करण्यास समर्थन देतो जे एजंट स्वयंचलितपणे कॉल करू शकतो. एजंट तयार करताना टूल्स नोंदणी केले जातात:

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

- **मल्टी-एजंट समन्वय**. तुम्ही विविध वैशिष्ठ्यांसह अनेक एजंट्स तयार करू शकता आणि त्यांचे कार्य समन्वयित करू शकता:

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

- **Azure ओळख समाकलन**. फ्रेमवर्क सुरक्षित, कीशिवाय प्रमाणीकरणासाठी `AzureCliCredential` (किंवा `DefaultAzureCredential`) वापरतो, ज्यामुळे API की व्यवस्थापनाची गरज नाही.

## Azure AI Agent Service

Azure AI Agent Service हा Microsoft Ignite 2024 मध्ये परिचित झालेले एक अधिक अलीकडील सेव आहे. हे अधिक लवचीक मॉडेल्ससह AI एजंट्स तयार करण्याची आणि तैनात करण्याची परवानगी देते, जसे की खुले स्रोत LLMs (उदा. Llama 3, Mistral, आणि Cohere) ला थेट कॉल करणे.

Azure AI Agent Service एंटरप्राइझ सुरक्षा यंत्रणा आणि डेटा संग्रह पद्धती प्रदान करते, ज्यामुळे ते एंटरप्राइझ अनुप्रयोगांसाठी योग्य ठरते.

हे Microsoft Agent Framework सह सहजतेने काम करते जे एजंट तयार करणे आणि तैनात करण्यासाठी वापरले जाते.

ही सेवा सध्या सार्वजनिक पूर्वावलोकनात आहे आणि Python व C# ला एजंट तयार करण्यासाठी समर्थन देते.

Azure AI Agent Service Python SDK वापरून, आपण एक एजंट वापरकर्ता-परिभाषित टूलसह तयार करू शकतो:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# उपकरणांच्या कार्यांची व्याख्या करा
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

### मुख्य संकल्पना

Azure AI Agent Service मध्ये खालील मुख्य संकल्पना आहेत:

- **एजंट**. Azure AI Agent Service Microsoft Foundry सह समाकलित आहे. AI Foundry अंतर्गत, AI एजंट हा एक "स्मार्ट" मायक्रोसर्व्हिस आहे जो प्रश्नांना उत्तर देण्यासाठी (RAG), क्रियाकलाप करणे, किंवा संपूर्णवर्कफ्लो स्वयंचलित करण्यासाठी वापरला जातो. हे जनरेटिव्ह AI मॉडेल्सची ताकद अशा साधनांसह एकत्र करून साध्य होते ज्याद्वारे तो वास्तविक जगातील डेटास्रोतांशी प्रवेश करू शकतो आणि संवाद साधू शकतो. येथे एक एजंटचे उदाहरण आहे:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    या उदाहरणात, `gpt-4o-mini` मॉडेलसह, `my-agent` नावाचा आणि `You are helpful agent` असा निर्देश असलेला एजंट तयार केला जातो. एजंटला कोड इंटरप्रिटेशन कार्य करण्यासाठी टूल्स आणि संसाधने दिली आहेत.

- **थ्रेड आणि संदेश**. थ्रेड ही एक महत्वाची संकल्पना आहे. हे एजंट आणि वापरकर्त्यादरम्यान संभाषण किंवा संवाद दर्शवते. थ्रेड्स वापरून संभाषणाची प्रगती ट्रॅक केली जाऊ शकते, संदर्भ माहिती साठवली जाऊ शकते, आणि संवाद स्थिती व्यवस्थापित केली जाऊ शकते. येथे थ्रेडचे उदाहरण आहे:

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

    मागील कोडमध्ये, थ्रेड तयार केला जातो. त्यानंतर, थ्रेडला संदेश पाठविला जातो. `create_and_process_run` कॉल करून, एजंटला थ्रेडवर कार्य करण्यास सांगितले जाते. शेवटी, संदेश घेतले जातात आणि एजंटच्या प्रतिसादासाठी लॉग केले जातात. संदेश संभाषणाची प्रगती दर्शवतात वापरकर्त्या आणि एजंट दरम्यान. हे समजणे महत्त्वाचे आहे की संदेश वेगवेगळ्या प्रकारांचे (म्हणजे मजकूर, प्रतिमा, किंवा फाईल) असू शकतात, म्हणजे एजंटचे कार्य एखादी प्रतिमा किंवा मजकूर प्रतिसाद निर्माण करत असते. डेव्हलपर म्हणून, तुम्ही नंतर या माहितीचा वापर प्रतिसाद पुढील प्रक्रिया करण्यासाठी किंवा वापरकर्त्यास सादर करण्यासाठी करू शकता.

- **Microsoft Agent Framework सह समाकलित**. Azure AI Agent Service Microsoft Agent Framework सह अखंड काम करते, म्हणजे तुम्ही `AzureAIProjectAgentProvider` वापरून एजंट तयार करू शकता आणि उत्पादन परिस्थितीसाठी Agent Service द्वारे त्यांची तैनात करू शकता.

**वापर प्रकरणे**: Azure AI Agent Service एंटरप्राइझ अनुप्रयोगांसाठी डिझाइन केले गेले आहे ज्यांना सुरक्षित, स्केलेबल आणि लवचीक AI एजंट तैनाती आवश्यक आहे.

## या दृष्टिकोनांमधील फरक काय?

काही अंशतः जुळते असे वाटते, पण त्यांच्या डिझाइन, क्षमता, आणि लक्ष्य वापराच्या दृष्टीने काही महत्त्वाचे फरक आहेत:

- **Microsoft Agent Framework (MAF)**: AI एजंट तयार करण्यासाठी तयार उत्पादन-योग्य SDK. टूल कॉलिंग, संभाषण व्यवस्थापन, आणि Azure ओळख समाकलनासाठी एक सुलभ API प्रदान करतो.
- **Azure AI Agent Service**: Azure Foundry मध्ये एजंटसाठी प्लॅटफॉर्म आणि तैनात सेवा. यात Azure OpenAI, Azure AI Search, Bing Search आणि कोड अंमलबजावणीसाठी बिल्ट-इन कनेक्टिव्हिटी आहे.

अजूनही काही शंका आहे का?

### वापर प्रकरणे

चला काही सामान्य वापर प्रकरणे पाहू आणि तुम्हाला मदत करू:

> Q: मी उत्पादन AI एजंट अनुप्रयोग तयार करीत आहे आणि लवकर सुरुवात करायची आहे
>

> A: Microsoft Agent Framework उत्कृष्ट निवड आहे. `AzureAIProjectAgentProvider` द्वारे एक सोपी, Python-आधारित API प्रदान केली जाते ज्यामुळे तुम्ही काही ओळींमध्ये टूल्स आणि सूचनांसह एजंट ठरवू शकता.

> Q: मला Azure एकत्रीकरणांसह (Search आणि कोड अंमलबजावणीसारख्या) एंटरप्राइझ-ग्रेड तैनाती हवी आहे
>
> A: Azure AI Agent Service सर्वोत्तम आहे. हे एक प्लॅटफॉर्म सेवा आहे ज्यामध्ये अनेक मॉडेल्स, Azure AI Search, Bing Search आणि Azure Functions चे बिल्ट-इन कौशल्य आहे. ते तुमचे एजंट Foundry पोर्टलमध्ये तयार करण्यास आणि मोठ्या प्रमाणात तैनात करण्यास सुलभ करते.

> Q: मला अजूनही गोंधळ आहे, फक्त एक पर्याय दे
>
> A: सुरुवातीला Microsoft Agent Framework वापरून एजंट तयार करा, आणि उत्पादनात तैनाती व प्रमाण वाढीसाठी नंतर Azure AI Agent Service वापरा. हा दृष्टिकोन तुम्हाला वेगाने तुमच्या एजंट लॉजिकवर पुनरावृत्ती करण्याची परवानगी देतो आणि एंटरप्राइझ तैनातीसाठी स्पष्ट मार्ग दाखवतो.

चला मुख्य फरक टेबलमध्ये सारांश पाहू:

| फ्रेमवर्क | लक्ष केंद्रित | मुख्य संकल्पना | वापर प्रकरणे |
| --- | --- | --- | --- |
| Microsoft Agent Framework | टूल कॉलिंगसह सुलभ एजंट SDK | एजंट्स, टूल्स, Azure ओळख | AI एजंट तयार करणे, टूल वापर, बहु-चरण कार्यप्रवाह |
| Azure AI Agent Service | लवचीक मॉडेल्स, एंटरप्राइझ सुरक्षा, कोड जनरेशन, टूल कॉलिंग | मॉड्यूलरिटी, सहकार्य, प्रक्रिया संघटन | सुरक्षित, स्केलेबल, आणि लवचीक AI एजंट तैनाती |

## मी माझ्या विद्यमान Azure परिसंस्थेतील साधने थेट एकत्र करू शकतो का, किंवा स्वतंत्र उपाययोजना गरजेच्या आहेत का?
उत्तर होय आहे, आपण आपल्या विद्यमान Azure इकोसिस्टम टूल्स थेट Azure AI Agent Service बरोबर एकत्रित करू शकता, विशेषत: कारण ते इतर Azure सेवांसोबत सुरळीत काम करण्यासाठी तयार करण्यात आले आहे. उदाहरणार्थ, आपण Bing, Azure AI Search आणि Azure Functions चे एकत्रीकरण करू शकता. Microsoft Foundry सह ही खोल एकत्रीकरण आहे.

Microsoft Agent Framework देखील `AzureAIProjectAgentProvider` आणि Azure ओळखीच्या माध्यमातून Azure सेवांसोबत एकत्रित होतो, ज्यामुळे आपण आपल्या एजंट टूल्समधून थेट Azure सेवांना कॉल करू शकता.

## नमुना कोड

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI Agent Frameworks विषयी अजून प्रश्न आहेत का?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) मध्ये सहभागी व्हा, इतर शिकणाऱ्यांशी भेटा, ऑफिस तासांना हजेरी लावा आणि आपले AI Agents प्रश्न सोडवा.

## संदर्भ

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## मागील धडा

[AI एजंट्स आणि एजंट वापर केस परिचय](../01-intro-to-ai-agents/README.md)

## पुढील धडा

[Agentic Design Patterns समजून घेणे](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**सर्वाधिकार सूचक**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील आहोत, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत सर्वाधिकार स्रोत म्हणून विचारला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतर करण्याची शिफारस केली जाते. या भाषांतराच्या वापरामुळे होणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->