[![Exploring AI Agent Frameworks](../../../translated_images/hi/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(इस पाठ का वीडियो देखने के लिए ऊपर की छवि पर क्लिक करें)_

# AI एजेंट फ्रेमवर्क एक्सप्लोर करें

AI एजेंट फ्रेमवर्क सॉफ़्टवेयर प्लेटफ़ॉर्म हैं जो AI एजेंट्स के निर्माण, तैनाती, और प्रबंधन को सरल बनाने के लिए डिज़ाइन किए गए हैं। ये फ्रेमवर्क डेवलपर्स को पूर्व-निर्मित घटक, अमूर्तताएं, और उपकरण प्रदान करते हैं जो जटिल AI सिस्टम के विकास को सुव्यवस्थित करते हैं।

ये फ्रेमवर्क डेवलपर्स को उनके अनुप्रयोगों के विशिष्ट पहलुओं पर ध्यान केंद्रित करने में मदद करते हैं, सामान्य AI एजेंट विकास की चुनौतियों के लिए मानकीकृत दृष्टिकोण प्रदान करके। वे AI सिस्टम के निर्माण में स्केलेबिलिटी, पहुंच, और दक्षता को बढ़ाते हैं।

## परिचय

इस पाठ में शामिल हैं:

- AI एजेंट फ्रेमवर्क क्या हैं और वे डेवलपर्स को क्या हासिल करने में सक्षम बनाते हैं?
- टीमें कैसे तेजी से प्रोटोटाइप, पुनरावृत्ति, और अपने एजेंट की क्षमताओं में सुधार कर सकती हैं?
- माइक्रोसॉफ्ट द्वारा बनाए गए फ्रेमवर्क और टूल्स के बीच क्या अंतर हैं (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> और <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- क्या मैं अपने मौजूदा Azure इकोसिस्टम टूल्स को सीधे एकीकृत कर सकता हूँ, या मुझे स्टैंडअलोन समाधान की आवश्यकता है?
- Microsoft Foundry Agent Service क्या है और यह मेरी कैसे मदद कर रहा है?

## सीखने के उद्देश्य

इस पाठ का उद्देश्य आपको समझने में मदद करना है:

- AI विकास में AI एजेंट फ्रेमवर्क की भूमिका।
- बुद्धिमान एजेंट बनाने के लिए AI एजेंट फ्रेमवर्क का उपयोग कैसे करें।
- AI एजेंट फ्रेमवर्क द्वारा सक्षम प्रमुख क्षमताएं।
- Microsoft Agent Framework और Microsoft Foundry Agent Service के बीच के अंतर।

## AI एजेंट फ्रेमवर्क क्या हैं और वे डेवलपर्स को क्या करने में सक्षम बनाते हैं?

पारंपरिक AI फ्रेमवर्क आपकी ऐप्स में AI को एकीकृत करने और इन ऐप्स को बेहतर बनाने में निम्नलिखित तरीकों से मदद कर सकते हैं:

- **व्यक्तिगतकरण**: AI उपयोगकर्ता व्यवहार और प्राथमिकताओं का विश्लेषण करके व्यक्तिगत सिफारिशें, सामग्री, और अनुभव प्रदान कर सकता है।
उदाहरण: Netflix जैसी स्ट्रीमिंग सेवाएं दृश्य इतिहास के आधार पर फिल्में और शो सुझाने के लिए AI का उपयोग करती हैं, जिससे उपयोगकर्ता की भागीदारी और संतुष्टि बढ़ती है।
- **स्वचालन और दक्षता**: AI दोहराए जाने वाले कार्यों को स्वचालित कर सकता है, कार्यप्रवाहों को सुव्यवस्थित कर सकता है, और संचालन दक्षता में सुधार कर सकता है।
उदाहरण: कस्टमर सर्विस ऐप्स AI-संचालित चैटबॉट्स का उपयोग सामान्य पूछताछ संभालने के लिए करती हैं, प्रतिक्रिया समय को कम करता है और जटिल मुद्दों के लिए मानव एजेंट को मुक्त करता है।
- **बेहतर उपयोगकर्ता अनुभव**: AI ऐसे बुद्धिमान फीचर्स प्रदान करता है जैसे आवाज़ मान्यता, प्राकृतिक भाषा प्रसंस्करण, और पूर्वानुमानित टेक्स्ट, जो समग्र उपयोगकर्ता अनुभव को बेहतर बनाते हैं।
उदाहरण: Siri और Google Assistant जैसे वर्चुअल असिस्टेंट AI का उपयोग करते हैं ताकि वे आवाज़ कमांड समझ सकें और प्रतिक्रिया दे सकें, जिससे उपयोगकर्ताओं के लिए उनके उपकरणों से बातचीत करना आसान हो जाता है।

### ये सब तो बहुत अच्छा लगता है, तो हमें AI एजेंट फ्रेमवर्क की क्यों ज़रूरत है?

AI एजेंट फ्रेमवर्क केवल AI फ्रेमवर्क से कहीं अधिक हैं। वे बुद्धिमान एजेंट बनाने के लिए डिज़ाइन किए गए हैं जो उपयोगकर्ताओं, अन्य एजेंटों, और पर्यावरण के साथ संवाद कर सकते हैं ताकि विशिष्ट लक्ष्यों को प्राप्त किया जा सके। ये एजेंट स्वायत्त व्यवहार दिखा सकते हैं, निर्णय ले सकते हैं, और परिवर्तित परिस्थितियों के अनुकूल हो सकते हैं। आइए AI एजेंट फ्रेमवर्क द्वारा सक्षम कुछ प्रमुख क्षमताओं पर नज़र डालते हैं:

- **एजेंट सहयोग और समन्वय**: कई AI एजेंट बनाने में सक्षम जो साथ मिलकर काम कर सकते हैं, संवाद कर सकते हैं, और जटिल कार्यों को हल कर सकते हैं।
- **कार्य स्वचालन और प्रबंधन**: बहु-चरण कार्यप्रवाहों को स्वचालित करने, कार्य सौंपने, और एजेंटों के बीच गतिशील कार्य प्रबंधन के लिए तंत्र प्रदान करें।
- **सांदर्भिक समझ और अनुकूलन**: एजेंटों को संदर्भ समझने, परिवर्तित पर्यावरण के अनुकूल होने, और वास्तविक समय की जानकारी के आधार पर निर्णय लेने की क्षमता प्रदान करें।

सारांश में, एजेंट आपको और अधिक करने देते हैं, स्वचालन को अगली स्तर पर ले जाते हैं, अधिक बुद्धिमान सिस्टम बनाते हैं जो उनके पर्यावरण से सीख सकते हैं और अनुकूलित हो सकते हैं।

## एजेंट की क्षमताओं को तेजी से प्रोटोटाइप, पुनरावृत्त करें और सुधारें कैसे?

यह एक तेजी से बदलता हुआ क्षेत्र है, लेकिन अधिकांश AI एजेंट फ्रेमवर्क में कुछ सामान्य बातें होती हैं जो आपको जल्दी प्रोटोटाइप और पुनरावृत्ति में मदद करती हैं जैसे मॉड्यूलर घटक, सहयोगी उपकरण, और वास्तविक समय सीखना। आइए इनके बारे में विस्तार से देखें:

- **मॉड्यूलर घटकों का उपयोग करें**: AI SDK पूर्व-निर्मित घटक प्रदान करते हैं जैसे AI और मेमोरी कनेक्टर, प्राकृतिक भाषा या कोड प्लगइन्स द्वारा फ़ंक्शन कॉलिंग, प्रॉम्प्ट टेम्पलेट्स, आदि।
- **सहयोगी उपकरणों का लाभ उठाएं**: विशिष्ट भूमिकाओं और कार्यों के साथ एजेंट डिज़ाइन करें, जिससे वे सहयोगी कार्यप्रवाहों का परीक्षण और सुधार कर सकें।
- **वास्तविक समय में सीखें**: ऐसे फीडबैक लूप्स लागू करें जहाँ एजेंट इंटरैक्शन से सीखते हैं और अपनी व्यवहार dynamically समायोजित करते हैं।

### मॉड्यूलर घटकों का उपयोग करें

Microsoft Agent Framework जैसे SDK पूर्व-निर्मित घटक प्रदान करते हैं जैसे AI कनेक्टर, टूल परिभाषाएं, और एजेंट प्रबंधन।

**टीमें कैसे उपयोग कर सकती हैं**: टीमें इन घटकों को जल्दी से इकट्ठा कर कार्यात्मक प्रोटोटाइप बना सकती हैं बिना शुरू से निर्माण करने के, जिससे त्वरित प्रयोग और पुनरावृत्ति संभव होती है।

**व्यावहारिक में कैसे काम करता है**: आप उपयोगकर्ता इनपुट से जानकारी निकालने के लिए पूर्व-निर्मित पार्सर, डेटा संग्रहीत और पुनः प्राप्त करने के लिए मेमोरी मॉड्यूल, और उपयोगकर्ताओं के साथ संवाद करने के लिए प्रॉम्प्ट जनरेटर का उपयोग कर सकते हैं, वह भी बिना इन घटकों को खरोंच से बनाए।

**उदाहरण कोड**. चलिए देखते हैं कि कैसे आप Microsoft Agent Framework को `FoundryChatClient` के साथ उपयोग करके मॉडल को टूल कॉलिंग के साथ उपयोगकर्ता इनपुट पर प्रतिक्रिया भेजने के लिए उपयोग कर सकते हैं:

``` python
# Microsoft एजेंट फ्रेमवर्क पायथन उदाहरण

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# यात्रा बुक करने के लिए एक नमूना टूल फ़ंक्शन परिभाषित करें
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
    # उदाहरण आउटपुट: आपकी 1 जनवरी 2025 को न्यूयॉर्क के लिए उड़ान सफलतापूर्वक बुक हो गई है। सुरक्षित यात्रा करें! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

इस उदाहरण से आप देख सकते हैं कि आप उपयोगकर्ता इनपुट से प्रमुख जानकारी जैसे उड़ान बुकिंग अनुरोध की उत्पत्ति, गंतव्य, और तिथि निकालने के लिए पूर्व-निर्मित पार्सर का कैसे उपयोग कर सकते हैं। यह मॉड्यूलर दृष्टिकोण आपको उच्च-स्तरीय तर्क पर ध्यान केंद्रित करने देता है।

### सहयोगी उपकरणों का लाभ उठाएं

Microsoft Agent Framework जैसे फ्रेमवर्क कई एजेंट बनाने में मदद करते हैं जो साथ मिलकर काम कर सकते हैं।

**टीमें कैसे उपयोग कर सकती हैं**: टीमें विशिष्ट भूमिकाओं और कार्यों के साथ एजेंट डिज़ाइन कर सकती हैं, जिससे वे सहयोगी कार्यप्रवाहों का परीक्षण और सुधार कर सकें और समग्र प्रणाली दक्षता बढ़ा सकें।

**व्यावहारिक में कैसे काम करता है**: आप एजेंटों की एक टीम बना सकते हैं जहाँ प्रत्येक एजेंट के पास विशिष्ट कार्य होती है, जैसे डेटा पुनः प्राप्ति, विश्लेषण, या निर्णय लेना। ये एजेंट एक साझा लक्ष्य प्राप्ति के लिए संवाद और सूचना साझा कर सकते हैं, जैसे उपयोगकर्ता प्रश्न का उत्तर देना या कार्य पूरा करना।

**उदाहरण कोड (Microsoft Agent Framework)**:

```python
# माइक्रोसॉफ्ट एजेंट फ्रेमवर्क का उपयोग करके साथ काम करने वाले कई एजेंट बनाना

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# डेटा पुनःप्राप्ति एजेंट
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# डेटा विश्लेषण एजेंट
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# एक कार्य पर अनुक्रम में एजेंट चलाना
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

पिछले कोड में आप देख सकते हैं कि कैसे एक कार्य बनाया गया है जिसमें कई एजेंट एक साथ काम करते हुए डेटा का विश्लेषण करते हैं। प्रत्येक एजेंट एक विशिष्ट कार्य करता है, और कार्य को एजेंटों के समन्वय द्वारा निष्पादित किया जाता है ताकि वांछित परिणाम हासिल हो सके। विशेषज्ञ भूमिकाओं के साथ समर्पित एजेंट बनाकर, आप कार्य दक्षता और प्रदर्शन में सुधार कर सकते हैं।

### वास्तविक समय में सीखें

उन्नत फ्रेमवर्क वास्तविक समय संदर्भ समझ और अनुकूलन की क्षमताएं प्रदान करते हैं।

**टीमें कैसे उपयोग कर सकती हैं**: टीमें फीडबैक लूप लागू कर सकती हैं जहाँ एजेंट इंटरैक्शन से सीखते हैं और अपनी व्यवहार dynamically समायोजित करते हैं, जिससे क्षमताओं में निरंतर सुधार और परिष्करण होता है।

**व्यावहारिक में कैसे काम करता है**: एजेंट उपयोगकर्ता फीडबैक, पर्यावरणीय डेटा, और कार्य परिणामों का विश्लेषण कर सकते हैं ताकि अपना ज्ञान आधार अपडेट करें, निर्णय लेने वाले एल्गोरिदम को समायोजित करें, और समय के साथ प्रदर्शन सुधारें। यह पुनरावृत्त सीखने की प्रक्रिया एजेंटों को बदलती परिस्थितियों और उपयोगकर्ता प्राथमिकताओं के अनुकूल होने में सक्षम बनाती है, जिससे समग्र सिस्टम की प्रभावशीलता बढ़ती है।

## Microsoft Agent Framework और Microsoft Foundry Agent Service में क्या अंतर हैं?

इन दृष्टिकोणों की तुलना करने के कई तरीके हैं, लेकिन आइए उनके डिज़ाइन, क्षमताओं, और लक्षित उपयोग मामलों के संदर्भ में कुछ प्रमुख अंतर देखें:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework `FoundryChatClient` का उपयोग करके AI एजेंट बनाने के लिए एक सरल SDK प्रदान करता है। यह डेवलपर्स को Azure OpenAI मॉडल के साथ अंतर्निहित टूल कॉलिंग, बातचीत प्रबंधन, और Azure पहचान द्वारा एंटरप्राइज़-ग्रेड सुरक्षा के साथ एजेंट बनाने में सक्षम बनाता है।

**उपयोग के मामले**: टूल उपयोग, बहु-चरण कार्यप्रवाह, और एंटरप्राइज़ एकीकरण परिदृश्यों के साथ उत्पादन-तैयार AI एजेंट बनाना।

Microsoft Agent Framework के कुछ महत्वपूर्ण मूलभूत अवधारणाएं:

- **एजेंट**। एक एजेंट `FoundryChatClient` के माध्यम से बनाया जाता है और नाम, निर्देश, और टूल्स के साथ कॉन्फ़िगर किया जाता है। एजेंट कर सकता है:
  - **उपयोगकर्ता संदेश संसाधित करें** और Azure OpenAI मॉडल का उपयोग करके प्रतिक्रियाएं उत्पन्न करें।
  - **बातचीत संदर्भ के आधार पर टूल्स को स्वचालित रूप से कॉल करें**।
  - **कई इंटरैक्शन के दौरान बातचीत की स्थिति बनाए रखें**।

  एजेंट बनाने का एक कोड स्निपेट यहां है:

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

- **टूल्स**। फ्रेमवर्क ऐसे टूल्स को परिभाषित करने का समर्थन करता है जो एजेंट स्वचालित रूप से कॉल कर सकता है। टूल्स एजेंट बनाते समय पंजीकृत होते हैं:

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

- **मल्टी-एजेंट समन्वय**। आप विभिन्न विशेषज्ञताओं के साथ कई एजेंट बना सकते हैं और उनके काम का समन्वय कर सकते हैं:

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

- **Azure पहचान एकीकरण**। फ्रेमवर्क API कुंजी प्रबंधन की आवश्यकता को खत्म करते हुए सुरक्षित, बिना कुंजी प्रमाणीकरण के लिए `AzureCliCredential` (या `DefaultAzureCredential`) का उपयोग करता है।

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service Microsoft Ignite 2024 में प्रस्तुत किया गया एक नया जोड़ है। यह AI एजेंट बनाने और तैनात करने की अनुमति देता है जो अधिक लचीले मॉडल का उपयोग करते हैं, जैसे सीधे ओपन-सोर्स LLMs जैसे Llama 3, Mistral, और Cohere को कॉल करना।

Microsoft Foundry Agent Service मजबूत एंटरप्राइज़ सुरक्षा तंत्र और डेटा भंडारण विधियां प्रदान करता है, जो इसे एंटरप्राइज़ एप्लिकेशन के लिए उपयुक्त बनाता है।

यह एजेंट बनाने और तैनाती के लिए Microsoft Agent Framework के साथ बाहर-बॉक्स काम करता है।

यह सेवा वर्तमान में सार्वजनिक पूर्वावलोकन में है और एजेंट निर्माण के लिए Python और C# को समर्थन करती है।

Microsoft Foundry Agent Service Python SDK का उपयोग करके, हम एक उपयोगकर्ता-परिभाषित टूल के साथ एजेंट बना सकते हैं:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# उपकरण कार्यों को परिभाषित करें
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

### मूलभूत अवधारणाएं

Microsoft Foundry Agent Service के निम्नलिखित मूलभूत अवधारणाएं हैं:

- **एजेंट**। Microsoft Foundry Agent Service Microsoft Foundry के साथ एकीकृत होता है। Microsoft Foundry के भीतर, एक AI एजेंट एक "स्मार्ट" माइक्रोसर्विस के रूप में कार्य करता है जिसका उपयोग प्रश्नों का उत्तर देने (RAG), क्रियाएँ करने, या पूरी तरह से कार्यप्रवाह स्वचालित करने के लिए किया जा सकता है। यह जनरेटिव AI मॉडल की शक्ति को ऐसे टूल्स के साथ जोड़कर करता है जो इसे वास्तविक दुनिया के डेटा स्रोतों तक पहुँचने और इंटरैक्ट करने की अनुमति देते हैं। यहां एक एजेंट का उदाहरण है:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    इस उदाहरण में, एक एजेंट `gpt-5-mini` मॉडल, नाम `my-agent`, और निर्देश `You are helpful agent` के साथ बनाया गया है। एजेंट कोड व्याख्या कार्यों को पूरा करने के लिए उपकरणों और संसाधनों से लैस है।

- **थ्रेड और संदेश**। थ्रेड एक और महत्वपूर्ण अवधारणा है। यह एजेंट और उपयोगकर्ता के बीच संवाद या इंटरैक्शन का प्रतिनिधित्व करता है। थ्रेड्स का उपयोग बातचीत की प्रगति को ट्रैक करने, संदर्भ सूचना स्टोर करने, और इंटरैक्शन की स्थिति प्रबंधित करने के लिए किया जा सकता है। यहां एक थ्रेड का उदाहरण है:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # एजेंट से थ्रेड पर काम करने के लिए कहें
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # एजेंट की प्रतिक्रिया देखने के लिए सभी संदेश प्राप्त करें और लॉग करें
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    पिछले कोड में, एक थ्रेड बनाया गया है। इसके बाद, थ्रेड को संदेश भेजा गया। `create_and_process_run` को कॉल करके, एजेंट को थ्रेड पर कार्य करने के लिए कहा गया। अंत में, संदेशों को लाया गया और एजेंट की प्रतिक्रिया देखने के लिए लॉग किया गया। ये संदेश उपयोगकर्ता और एजेंट के बीच बातचीत की प्रगति को दर्शाते हैं। यह भी महत्वपूर्ण है समझना कि संदेश विभिन्न प्रकार के हो सकते हैं जैसे टेक्स्ट, इमेज, या फ़ाइल, अर्थात् एजेंट के कार्य के परिणामस्वरूप, उदाहरण के लिए एक छवि या टेक्स्ट प्रतिक्रिया हो सकती है। एक डेवलपर के रूप में, आप इस जानकारी का उपयोग प्रतिक्रिया को आगे संसाधित करने या उपयोगकर्ता को प्रस्तुत करने के लिए कर सकते हैं।

- **Microsoft Agent Framework के साथ एकीकरण**। Microsoft Foundry Agent Service Microsoft Agent Framework के साथ सहजता से काम करता है, जिसका अर्थ है कि आप `FoundryChatClient` का उपयोग करके एजेंट बना सकते हैं और उत्पादन परिदृश्यों के लिए एजेंट सेवा के माध्यम से उन्हें तैनात कर सकते हैं।

**उपयोग के मामले**: Microsoft Foundry Agent Service उन एंटरप्राइज़ एप्लिकेशन के लिए डिज़ाइन किया गया है जिन्हें सुरक्षित, स्केलेबल, और लचीले AI एजेंट तैनाती की आवश्यकता होती है।

## इन दृष्टिकोणों में क्या अंतर है?
 
ऐसा लगता है कि ओवरलैप है, लेकिन उनके डिज़ाइन, क्षमताओं, और लक्षित उपयोग मामलों के संदर्भ में कुछ प्रमुख अंतर हैं:
 
- **Microsoft Agent Framework (MAF)**: AI एजेंट बनाने के लिए एक उत्पादन-तैयार SDK है। यह टूल कॉलिंग, बातचीत प्रबंधन, और Azure पहचान एकीकरण के साथ एजेंट बनाने के लिए एक सरल API प्रदान करता है।
- **Microsoft Foundry Agent Service**: Microsoft Foundry में एजेंट के लिए एक प्लेटफ़ॉर्म और तैनाती सेवा है। यह Azure OpenAI, Azure AI Search, Bing Search, और कोड निष्पादन जैसी सेवाओं के लिए अंतर्निहित कनेक्टिविटी प्रदान करता है।
 
अभी भी सुनिश्चित नहीं कि कौन सा चुनें?

### उपयोग के मामले
 
आइए कुछ सामान्य उपयोग मामलों के जरिए आपकी मदद करने की कोशिश करें:
 
> प्रश्न: मैं उत्पादन AI एजेंट एप्लिकेशन बना रहा हूँ और जल्दी शुरू करना चाहता हूँ
>

>उत्तर: Microsoft Agent Framework एक शानदार विकल्प है। यह `FoundryChatClient` के माध्यम से एक सरल, पाइथोनिक API प्रदान करता है जो आपको कुछ ही कोड लाइनों में टूल्स और निर्देशों के साथ एजेंट परिभाषित करने देता है।

>प्रश्न: मुझे Azure इंटिग्रेशन जैसे Search और कोड निष्पादन के साथ एंटरप्राइज़-ग्रेड तैनाती की जरूरत है
>
>उत्तर: Microsoft Foundry Agent Service सबसे उपयुक्त है। यह एक प्लेटफ़ॉर्म सेवा है जो कई मॉडलों, Azure AI Search, Bing Search और Azure Functions के लिए अंतर्निहित क्षमताएं प्रदान करती है। यह Foundry पोर्टल में आपके एजेंट बनाने और बड़े पैमाने पर तैनात करना आसान बनाती है।
 
> प्रश्न: मैं अभी भी भ्रमित हूँ, बस मुझे एक विकल्प दो
>
> उत्तर: अपने एजेंट बनाने के लिए Microsoft Agent Framework से शुरू करें, और फिर उत्पादन में तैनात और स्केल करने के लिए Microsoft Foundry Agent Service का उपयोग करें। यह तरीका आपको तेजी से एजेंट लॉजिक पर पुनरावृत्ति करने देता है जबकि एंटरप्राइज़ तैनाती के लिए स्पष्ट रास्ता भी प्रदान करता है।
 
आइए तालिका में प्रमुख अंतर संक्षेप करें:

| Framework | फोकस | मूल अवधारणाएं | उपयोग के मामले |
| --- | --- | --- | --- |
| Microsoft Agent Framework | टूल कॉलिंग के साथ सुव्यवस्थित एजेंट SDK | एजेंट, टूल, Azure पहचान | AI एजेंट बनाना, टूल उपयोग, बहु-चरण कार्यप्रवाह |
| Microsoft Foundry Agent Service | लचीले मॉडल, एंटरप्राइज़ सुरक्षा, कोड जनरेशन, टूल कॉलिंग | मॉड्यूलरिटी, सहयोग, प्रक्रिया प्रबंधन | सुरक्षित, स्केलेबल, और लचीली AI एजेंट तैनाती |

## क्या मैं अपने मौजूदा Azure इकोसिस्टम टूल्स को सीधे एकीकृत कर सकता हूँ, या मुझे स्टैंडअलोन समाधान की आवश्यकता है?


उत्तर है हाँ, आप अपने मौजूदा Azure इकोसिस्टम टूल्स को सीधे Microsoft Foundry Agent Service के साथ एकीकृत कर सकते हैं, खासकर क्योंकि इसे अन्य Azure सेवाओं के साथ सहजता से काम करने के लिए बनाया गया है। उदाहरण के लिए, आप Bing, Azure AI Search, और Azure Functions को एकीकृत कर सकते हैं। Microsoft Foundry के साथ भी गहरी एकीकरण है।

Microsoft Agent Framework भी `FoundryChatClient` और Azure पहचान के माध्यम से Azure सेवाओं के साथ एकीकृत होता है, जिससे आप अपने एजेंट टूल्स से सीधे Azure सेवाओं को कॉल कर सकते हैं।

## नमूना कोड

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI Agent Frameworks के बारे में और सवाल हैं?

अन्य शिक्षार्थियों से मिलने, ऑफिस आवर्स में भाग लेने और अपने AI Agents से जुड़े प्रश्नों के जवाब पाने के लिए [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) से जुड़ें।

## संदर्भ

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## पिछला पाठ

[AI Agents का परिचय और Agent उपयोग के मामले](../01-intro-to-ai-agents/README.md)

## अगला पाठ

[Agentic डिज़ाइन पैटर्न को समझना](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->