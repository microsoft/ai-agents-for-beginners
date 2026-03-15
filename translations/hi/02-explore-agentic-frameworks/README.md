[![AI एजेंट फ्रेमवर्क्स का अन्वेषण](../../../translated_images/hi/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(ऊपर की छवि पर क्लिक करके इस पाठ का वीडियो देखें)_

# AI एजेंट फ्रेमवर्क्स का अन्वेषण

AI एजेंट फ्रेमवर्क ऐसे सॉफ़्टवेयर प्लेटफ़ॉर्म हैं जो AI एजेंट्स के निर्माण, तैनाती, और प्रबंधन को सरल बनाने के लिए डिज़ाइन किए गए हैं। ये फ्रेमवर्क डेवलपर्स को प्री-बिल्ट कॉम्पोनेंट्स, एब्स्ट्रैक्शन्स, और उपकरण प्रदान करते हैं जो जटिल AI सिस्टम के विकास को सुगम बनाते हैं।

ये फ्रेमवर्क सामान्य चुनौतियों के लिए मानकीकृत दृष्टिकोण प्रदान करके डेवलपर्स को उनके अनुप्रयोगों के अद्वितीय पहलुओं पर ध्यान केंद्रित करने में मदद करते हैं। वे AI सिस्टम बनाने में स्केलेबिलिटी, पहुँच, और दक्षता बढ़ाते हैं।

## परिचय 

यह पाठ निम्नलिखित को कवर करेगा:

- AI एजेंट फ्रेमवर्क क्या हैं और वे डेवलपर्स को क्या हासिल करने में सक्षम बनाते हैं?
- टीमें इनका उपयोग करके अपने एजेंट की क्षमताओं का शीघ्र प्रोटोटाइप, पुनरावृत्ति, और सुधार कैसे कर सकती हैं?
- Microsoft द्वारा बनाए गए फ्रेमवर्क और टूल्स के बीच क्या अंतर हैं (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> और <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- क्या मैं अपने मौजूदा Azure इकोसिस्टम टूल्स को सीधे एकीकृत कर सकता/सकती हूँ, या मुझे स्टैंडअलोन समाधान चाहिए होंगे?
- Azure AI Agents सेवा क्या है और यह मेरी कैसे मदद कर रही है?

## सीखने के लक्ष्य

इस पाठ के लक्ष्य आपको यह समझने में मदद करना हैं:

- AI विकास में AI एजेंट फ्रेमवर्क्स की भूमिका।
- बुद्धिमान एजेंट बनाने के लिए AI एजेंट फ्रेमवर्क्स का उपयोग कैसे करें।
- AI एजेंट फ्रेमवर्क्स द्वारा सक्षम की जाने वाली प्रमुख क्षमताएँ।
- Microsoft Agent Framework और Azure AI Agent Service के बीच क्या अंतर हैं।

## AI एजेंट फ्रेमवर्क्स क्या हैं और वे डेवलपर्स को क्या करने की अनुमति देते हैं?

पारंपरिक AI फ्रेमवर्क्स आपकी मदद कर सकते हैं कि आप AI को अपने ऐप्स में कैसे एकीकृत करें और इन ऐप्स को निम्नलिखित तरीकों से बेहतर बनाएं:

- **व्यक्तिकरण (Personalization)**: AI उपयोगकर्ता के व्यवहार और प्राथमिकताओं का विश्लेषण करके व्यक्तिगत सिफारिशें, सामग्री और अनुभव प्रदान कर सकता है।
Example: Netflix जैसे स्ट्रीमिंग सेवाएँ AI का उपयोग देखने के इतिहास के आधार पर फ़िल्में और शो सुझाने के लिए करती हैं, जो उपयोगकर्ता की भागीदारी और संतोष बढ़ाती हैं।
- **स्वचालन और दक्षता (Automation and Efficiency)**: AI दोहराए जाने वाले कामों को स्वचालित कर सकता है, वर्कफ़्लोज़ को सुव्यवस्थित कर सकता है, और संचालनात्मक दक्षता में सुधार कर सकता है।
Example: ग्राहक सेवा एप्लिकेशन सामान्य पूछताछ संभालने के लिए AI-समर्थित चैटबॉट्स का उपयोग करते हैं, जिससे प्रतिक्रिया समय कम होता है और मानव एजेंट अधिक जटिल मुद्दों के लिए मुक्त रहते हैं।
- **उन्नत उपयोगकर्ता अनुभव (Enhanced User Experience)**: AI आवाज़ पहचान, नेचुरल लैंग्वेज प्रोसेसिंग, और प्रेडिक्टिव टेक्स्ट जैसे बुद्धिमान फ़ीचर्स प्रदान कर उपयोगकर्ता अनुभव में सुधार कर सकता है।
Example: Siri और Google Assistant जैसे वर्चुअल असिस्टेंट्स AI का उपयोग करके वॉइस कमांड्स को समझते और उन पर प्रतिक्रिया देते हैं, जिससे उपयोगकर्ताओं के लिए अपने उपकरणों के साथ इंटरैक्ट करना आसान हो जाता है।

### यह सब तो अच्छा लग रहा है, तो हमें AI Agent Framework की आवश्यकता क्यों है?

AI एजेंट फ्रेमवर्क्स केवल AI फ्रेमवर्क्स से कहीं अधिक चीज़ का प्रतिनिधित्व करते हैं। इन्हें बुद्धिमान एजेंट्स बनाने के लिए डिज़ाइन किया गया है जो उपयोगकर्ताओं, अन्य एजेंट्स, और वातावरण के साथ इंटरैक्ट कर सकते हैं और विशिष्ट लक्ष्यों को हासिल कर सकते हैं। ये एजेंट स्वायत्त व्यवहार प्रदर्शित कर सकते हैं, निर्णय ले सकते हैं, और बदलती परिस्थितियों के अनुसार अनुकूलित हो सकते हैं। आइए AI एजेंट फ्रेमवर्क्स द्वारा सक्षम कुछ प्रमुख क्षमताओं को देखें:

- **एजेंट सहयोग और समन्वय (Agent Collaboration and Coordination)**: ऐसा निर्माण संभव बनाते हैं जहाँ कई AI एजेंट एक साथ काम कर सकें, संवाद कर सकें, और जटिल कार्यों को हल करने के लिए समन्वय कर सकें।
- **कार्य स्वचालन और प्रबंधन (Task Automation and Management)**: बहु-चरण वर्कफ़्लोज़, कार्य-डेलीगेशन, और एजेंटों के बीच डायनामिक कार्य प्रबंधन को स्वचालित करने के तंत्र प्रदान करते हैं।
- **पारिस्थितिक समझ और अनुकूलन (Contextual Understanding and Adaptation)**: एजेंट्स को संदर्भ समझने, बदलते पर्यावरण के अनुसार अनुकूलन करने, और वास्तविक-समय जानकारी के आधार पर निर्णय लेने में सक्षम बनाते हैं।

संक्षेप में, एजेंट आपको और अधिक करने की अनुमति देते हैं, स्वचालन को अगले स्तर पर ले जाते हैं, और ऐसे अधिक बुद्धिमान सिस्टम बनाते हैं जो अपने पर्यावरण से अनुकूलित और सीख सकते हैं।

## एजेंट की क्षमताओं का जल्दी प्रोटोटाइप, पुनरावृत्ति, और सुधार कैसे करें?

यह एक तेज़ी से बदलता परिदृश्य है, लेकिन अधिकांश AI एजेंट फ्रेमवर्क्स में कुछ सामान्य चीज़ें होती हैं जो आपको जल्दी प्रोटोटाइप और पुनरावृत्ति करने में मदद कर सकती हैं, जैसे मॉड्यूलर कॉम्पोनेंट्स, सहयोगी उपकरण, और रियल-टाइम लर्निंग। आइए इनमें गहराई से देखें:

- **मॉड्यूलर कॉम्पोनेंट्स का उपयोग करें**: AI SDKs प्री-बिल्ट कॉम्पोनेंट्स जैसे AI और Memory कनेक्टर्स, नेचुरल लैंग्वेज या कोड प्लगइन्स के माध्यम से फ़ंक्शन कॉलिंग, प्रॉम्प्ट टेम्पलेट्स, और अधिक प्रदान करते हैं।
- **सहयोगी उपकरणों का लाभ उठाएँ**: विशिष्ट भूमिकाओं और कार्यों के साथ एजेंट डिज़ाइन करें, जिससे वे सहयोगी वर्कफ़्लोज़ का परीक्षण और परिष्करण कर सकें।
- **रियल-टाइम में सीखें**: ऐसा फ़ीडबैक लूप लागू करें जहाँ एजेंट interactions से सीखते हैं और अपने व्यवहार को डायनामिक रूप से समायोजित करते हैं।

### मॉड्यूलर कॉम्पोनेंट्स का उपयोग करें

SDKs जैसे Microsoft Agent Framework प्री-बिल्ट कॉम्पोनेंट्स प्रदान करते हैं जैसे AI कनेक्टर्स, टूल परिभाषाएँ, और एजेंट प्रबंधन।

**टीमें इनका उपयोग कैसे कर सकती हैं**: टीमें इन कॉम्पोनेंट्स को जल्दी से संयोजित करके कार्यात्मक प्रोटोटाइप बना सकती हैं बिना शून्य से शुरू किए, जिससे त्वरित प्रयोग और पुनरावृत्ति संभव होती है।

**व्यवहार में यह कैसे काम करता है**: आप उपयोगकर्ता इनपुट से जानकारी निकालने के लिए एक प्री-बिल्ट पार्सर, डेटा संग्रह और पुनर्प्राप्ति के लिए एक मेमोरी मॉड्यूल, और उपयोगकर्ताओं के साथ इंटरैक्ट करने के लिए एक प्रॉम्प्ट जेनरेटर का उपयोग कर सकते हैं, और ये सब स्क्रैच से बनाने की आवश्यकता के बिना काम कर सकते हैं।

**Example code**. आइए एक उदाहरण देखें कि कैसे आप Microsoft Agent Framework का उपयोग `AzureAIProjectAgentProvider` के साथ करके मॉडल को उपयोगकर्ता इनपुट का उत्तर टूल कॉलिंग के साथ देने के लिए कर सकते हैं:

``` python
# Microsoft एजेंट फ्रेमवर्क पायथन उदाहरण

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# यात्रा बुक करने के लिए एक नमूना टूल फ़ंक्शन परिभाषित करें
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
    # उदाहरण आउटपुट: 1 जनवरी, 2025 को न्यू यॉर्क के लिए आपकी उड़ान सफलतापूर्वक बुक कर दी गई है। सुरक्षित यात्रा करें! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

इस उदाहरण से आप देख सकते हैं कि कैसे आप उपयोगकर्ता इनपुट से प्रमुख जानकारी जैसे उड़ान बुकिंग अनुरोध का मूलस्थान, गंतव्य, और तारीख निकालने के लिए एक प्री-बिल्ट पार्सर का लाभ उठा सकते हैं। यह मॉड्यूलर दृष्टिकोण आपको उच्च-स्तरीय लॉजिक पर ध्यान केंद्रित करने की अनुमति देता है।

### सहयोगी उपकरणों का लाभ उठाएँ

Microsoft Agent Framework जैसे फ़्रेमवर्क कई एजेंट बनाने की सुविधा प्रदान करते हैं जो एक साथ काम कर सकते हैं।

**टीमें इनका उपयोग कैसे कर सकती हैं**: टीमें विशिष्ट भूमिकाओं और कार्यों के साथ एजेंट डिज़ाइन कर सकती हैं, जिससे वे सहयोगी वर्कफ़्लोज़ का परीक्षण और परिष्करण कर सकें और समग्र सिस्टम दक्षता में सुधार कर सकें।

**व्यवहार में यह कैसे काम करता है**: आप एजेंटों की एक टीम बना सकते हैं जहाँ प्रत्येक एजेंट की विशिष्ट भूमिका होती है, जैसे डेटा पुनर्प्राप्ति, विश्लेषण, या निर्णय-निर्माण। ये एजेंट संवाद कर सकते हैं और सामान्य लक्ष्य हासिल करने के लिए जानकारी साझा कर सकते हैं, जैसे उपयोगकर्ता प्रश्न का उत्तर देना या किसी कार्य को पूरा करना।

**Example code (Microsoft Agent Framework)**:

```python
# Microsoft Agent Framework का उपयोग करके एक साथ काम करने वाले कई एजेंट बनाना

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# डेटा पुनःप्राप्ति एजेंट
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# डेटा विश्लेषण एजेंट
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# एक कार्य पर एजेंटों को अनुक्रम में चलाएं
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

ऊपर के कोड में आप देख सकते हैं कि कैसे आप एक ऐसा कार्य बना सकते हैं जिसमें कई एजेंट एक साथ काम करके डेटा का विश्लेषण करते हैं। प्रत्येक एजेंट एक विशिष्ट फ़ंक्शन निष्पादित करता है, और वांछित परिणाम प्राप्त करने के लिए एजेंटों का समन्वय करके कार्य निष्पादित होता है। विशेष भूमिकाओं के साथ समर्पित एजेंट बनाने से आप कार्य दक्षता और प्रदर्शन में सुधार कर सकते हैं।

### रियल-टाइम में सीखें

उन्नत फ्रेमवर्क रियल-टाइम संदर्भ समझ और अनुकूलन की क्षमताएँ प्रदान करते हैं।

**टीमें इनका उपयोग कैसे कर सकती हैं**: टीमें ऐसे फ़ीडबैक लूप लागू कर सकती हैं जहाँ एजेंट इंटरैक्शन से सीखते हैं और अपने व्यवहार को डायनामिक रूप से समायोजित करते हैं, जिससे क्षमताओं का निरंतर सुधार और परिष्करण होता है।

**व्यवहार में यह कैसे काम करता है**: एजेंट उपयोगकर्ता फ़ीडबैक, पर्यावरणीय डेटा, और कार्य परिणामों का विश्लेषण करके अपनी नॉलेज बेस अपडेट कर सकते हैं, निर्णय-निर्माण एल्गोरिदम समायोजित कर सकते हैं, और समय के साथ प्रदर्शन में सुधार कर सकते हैं। यह पुनरावृत्तिशील सीखने की प्रक्रिया एजेंटों को बदलती परिस्थितियों और उपयोगकर्ता प्राथमिकताओं के अनुसार अनुकूलित होने में सक्षम बनाती है, जिससे समग्र सिस्टम प्रभावशीलता बढ़ती है।

## Microsoft Agent Framework और Azure AI Agent Service के बीच क्या अंतर हैं?

इन दृष्टिकोणों की तुलना करने के कई तरीके हैं, लेकिन आइए उनके डिज़ाइन, क्षमताओं, और लक्षित उपयोग मामलों के संदर्भ में कुछ प्रमुख अंतर देखें:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework एक सुव्यवस्थित SDK प्रदान करता है ताकि `AzureAIProjectAgentProvider` का उपयोग करके AI एजेंट बनाए जा सकें। यह डेवलपर्स को Azure OpenAI मॉडल्स के साथ बिल्ट-इन टूल कॉलिंग, बातचीत प्रबंधन, और Azure identity के माध्यम से एंटरप्राइज-ग्रेड सुरक्षा का लाभ उठाने में सक्षम बनाता है।

**उपयोग के मामले**: टूल उपयोग, बहु-चरण वर्कफ़्लोज़, और एंटरप्राइज इंटीग्रेशन परिदृश्यों के साथ प्रोडक्शन-तैयार AI एजेंट बनाना।

यहाँ Microsoft Agent Framework के कुछ महत्वपूर्ण कोर कॉन्सेप्ट्स हैं:

- **Agents**. एक एजेंट `AzureAIProjectAgentProvider` के माध्यम से बनाया जाता है और एक नाम, निर्देश, और टूल्स के साथ कॉन्फ़िगर किया जाता है। एजेंट कर सकता है:
  - **Process user messages** और Azure OpenAI मॉडल्स का उपयोग करके प्रतिक्रियाएँ जेनरेट कर सकता है।
  - **Call tools** बातचीत के संदर्भ के आधार पर स्वतः टूल कॉल कर सकता है।
  - **Maintain conversation state** कई इंटरैक्शनों के दौरान बातचीत की स्थिति बनाए रख सकता है।

  यहाँ एक कोड स्निपेट है जो दिखाता है कि कैसे एक एजेंट बनाया जाता है:

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

- **Tools**. यह फ्रेमवर्क ऐसे टूल्स को परिभाषित करने का समर्थन करता है जिन्हें Python फ़ंक्शन्स के रूप में लागू किया जा सकता है जिन्हें एजेंट स्वचालित रूप से कॉल कर सकता है। एजेंट बनाते समय टूल्स रजिस्टर किए जाते हैं:

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

- **Multi-Agent Coordination**. आप विभिन्न विशेषज्ञताओं वाले कई एजेंट बना सकते हैं और उनके कार्यों का समन्वय कर सकते हैं:

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

- **Azure Identity Integration**. फ्रेमवर्क सुरक्षित, बिना-कुंजी प्रमाणीकरण के लिए `AzureCliCredential` (या `DefaultAzureCredential`) का उपयोग करता है, जिससे सीधे API कुंजियों का प्रबंधन करने की आवश्यकता समाप्त हो जाती है।

## Azure AI Agent Service

Azure AI Agent Service एक हालिया जोड़ है, जिसे Microsoft Ignite 2024 में पेश किया गया था। यह अधिक लचीले मॉडल्स के साथ AI एजेंट्स के विकास और तैनाती की अनुमति देता है, जैसे सीधे open-source LLMs को कॉल करना (उदा. Llama 3, Mistral, और Cohere)।

Azure AI Agent Service मजबूत एंटरप्राइज सुरक्षा तंत्र और डेटा भंडारण विधियाँ प्रदान करता है, जिससे यह एंटरप्राइज अनुप्रयोगों के लिए उपयुक्त है।

यह एजेंट्स बनाने और तैनात करने के लिए Microsoft Agent Framework के साथ आउट-ऑफ-द-बॉक्स काम करता है।

यह सेवा वर्तमान में Public Preview में है और एजेंट बनाने के लिए Python और C# का समर्थन करती है।

Azure AI Agent Service Python SDK का उपयोग करके, हम एक उपयोगकर्ता-निर्धारित टूल के साथ एक एजेंट बना सकते हैं:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# टूल फ़ंक्शंस परिभाषित करें
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

### मुख्य अवधारणाएँ

Azure AI Agent Service के निम्नलिखित मुख्य कॉन्सेप्ट्स हैं:

- **Agent**. Azure AI Agent Service Microsoft Foundry के साथ एकीकृत होता है। AI Foundry के भीतर, एक AI Agent एक "स्मार्ट" माइक्रोसर्विस के रूप में कार्य करता है जिसे प्रश्नों का उत्तर देने (RAG), क्रियाएँ करने, या वर्कफ़्लोज़ को पूर्णतया स्वचालित करने के लिए उपयोग किया जा सकता है। यह जनरेटिव AI मॉडल्स की शक्ति को उन टूल्स के साथ मिलाकर प्राप्त करता है जो इसे वास्तविक-विश्व डेटा स्रोतों तक पहुँचने और उनके साथ इंटरैक्ट करने की अनुमति देते हैं। यहाँ एक एजेंट का उदाहरण है:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    इस उदाहरण में, एक एजेंट मॉडल `gpt-4o-mini`, नाम `my-agent`, और निर्देश `You are helpful agent` के साथ बनाया गया है। एजेंट को कोड व्याख्या कार्यों को करने के लिए टूल्स और संसाधन प्रदान किए गए हैं।

- **Thread and messages**. थ्रेड एक और महत्वपूर्ण कॉन्सेप्ट है। यह एजेंट और उपयोगकर्ता के बीच एक बातचीत या इंटरैक्शन का प्रतिनिधित्व करता है। थ्रेड्स का उपयोग बातचीत की प्रगति को ट्रैक करने, संदर्भ जानकारी संग्रहीत करने, और इंटरैक्शन की स्थिति का प्रबंधन करने के लिए किया जा सकता है। यहाँ एक थ्रेड का उदाहरण है:

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

    पिछले कोड में, एक थ्रेड बनाया गया है। उसके बाद, थ्रेड को एक संदेश भेजा गया है। `create_and_process_run` कॉल करके, एजेंट को थ्रेड पर कार्य करने के लिए कहा जाता है। अंत में, एजेंट की प्रतिक्रिया देखने के लिए संदेशों को लाया और लॉग किया जाता है। ये संदेश उपयोगकर्ता और एजेंट के बीच बातचीत की प्रगति को दर्शाते हैं। यह भी समझना महत्वपूर्ण है कि संदेश विभिन्न प्रकार के हो सकते हैं जैसे टेक्स्ट, इमेज, या फ़ाइल; उदाहरण के लिए एजेंट का कार्य किसी इमेज या टेक्स्ट प्रतिक्रिया का परिणाम हो सकता है। एक डेवलपर के रूप में, आप फिर इस जानकारी का उपयोग प्रतिक्रिया को आगे प्रोसेस करने या उपयोगकर्ता को प्रस्तुत करने के लिए कर सकते हैं।

- **Integrates with the Microsoft Agent Framework**. Azure AI Agent Service Microsoft Agent Framework के साथ सहज रूप से काम करता है, जिसका अर्थ है कि आप `AzureAIProjectAgentProvider` का उपयोग करके एजेंट बना सकते हैं और उत्पादन परिदृश्यों के लिए उन्हें Agent Service के माध्यम से तैनात कर सकते हैं।

**उपयोग के मामले**: Azure AI Agent Service उन एंटरप्राइज अनुप्रयोगों के लिए डिज़ाइन किया गया है जिन्हें सुरक्षित, स्केलेबल, और लचीली AI एजेंट तैनाती की आवश्यकता होती है।

## इन दृष्टिकोणों के बीच क्या अंतर है?
 
यह लगता है कि इनमें ओवरलैप है, लेकिन उनके डिज़ाइन, क्षमताओं, और लक्षित उपयोग मामलों के संदर्भ में कुछ प्रमुख अंतर हैं:
 
- **Microsoft Agent Framework (MAF)**: AI एजेंट बनाने के लिए एक प्रोडक्शन-रेडी SDK है। यह टूल कॉलिंग, बातचीत प्रबंधन, और Azure identity इंटीग्रेशन के साथ एजेंट बनाने के लिए एक सुव्यवस्थित API प्रदान करता है।
- **Azure AI Agent Service**: Agents के लिए Azure Foundry में एक प्लेटफ़ॉर्म और तैनाती सेवा है। यह Azure OpenAI, Azure AI Search, Bing Search और कोड निष्पादन जैसे सेवाओं के लिए बिल्ट-इन कनेक्टिविटी प्रदान करती है।
 
अभी भी तय नहीं कर पाए कौन सा चुनना है?

### उपयोग के मामले
 
आइए कुछ सामान्य उपयोग मामलों के माध्यम से देखें कि क्या हम आपकी मदद कर सकते हैं:
 
> Q: I'm building production AI agent applications and want to get started quickly
>
>
>A: The Microsoft Agent Framework is a great choice. It provides a simple, Pythonic API via `AzureAIProjectAgentProvider` that lets you define agents with tools and instructions in just a few lines of code.

>Q: I need enterprise-grade deployment with Azure integrations like Search and code execution
>
> A: Azure AI Agent Service is the best fit. It's a platform service that provides built-in capabilities for multiple models, Azure AI Search, Bing Search and Azure Functions. It makes it easy to build your agents in the Foundry Portal and deploy them at scale.
 
> Q: I'm still confused, just give me one option
>
> A: Start with the Microsoft Agent Framework to build your agents, and then use Azure AI Agent Service when you need to deploy and scale them in production. This approach lets you iterate quickly on your agent logic while having a clear path to enterprise deployment.
 
आइए मुख्य अंतर का सार एक तालिका में संक्षेप करें:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| Microsoft Agent Framework | टूल कॉलिंग के साथ सुव्यवस्थित एजेंट SDK | Agents, Tools, Azure Identity | AI एजेंट बनाना, टूल उपयोग, बहु-चरण वर्कफ़्लोज़ |
| Azure AI Agent Service | लचीले मॉडल, एंटरप्राइज़ सुरक्षा, कोड जनरेशन, टूल कॉलिंग | Modularity, Collaboration, Process Orchestration | सुरक्षित, स्केलेबल, और लचीली AI एजेंट तैनाती |

## क्या मैं अपने मौजूदा Azure इकोसिस्टम टूल्स को सीधे एकीकृत कर सकता/सकती हूँ, या मुझे स्टैंडअलोन समाधान चाहिए होंगे?
उत्तर हाँ है — आप अपने मौजूदा Azure इकोसिस्टम टूल्स को सीधे Azure AI Agent Service के साथ एकीकृत कर सकते हैं, विशेष रूप से क्योंकि इसे अन्य Azure सेवाओं के साथ सहज रूप से काम करने के लिए बनाया गया है। उदाहरण के लिए आप Bing, Azure AI Search, और Azure Functions को एकीकृत कर सकते हैं। Microsoft Foundry के साथ भी गहरा एकीकरण मौजूद है।

Microsoft Agent Framework भी `AzureAIProjectAgentProvider` और Azure identity के माध्यम से Azure सेवाओं के साथ एकीकृत होता है, जिससे आप अपने एजेंट टूल्स से सीधे Azure सेवाओं को कॉल कर सकते हैं।

## नमूना कोड

- Python: [एजेंट फ्रेमवर्क](./code_samples/02-python-agent-framework.ipynb)
- .NET: [एजेंट फ्रेमवर्क](./code_samples/02-dotnet-agent-framework.md)

## क्या आपके पास AI एजेंट फ्रेमवर्क के बारे में और प्रश्न हैं?

अन्य शिक्षार्थियों से मिलने, कार्यालय घंटों में भाग लेने और अपने AI एजेंट्स के प्रश्नों के उत्तर प्राप्त करने के लिए [Microsoft Foundry डिस्कॉर्ड](https://aka.ms/ai-agents/discord) में शामिल हों।

## संदर्भ

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure एजेंट सेवा</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI प्रतिक्रियाएँ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI एजेंट सेवा</a>

## पिछला पाठ

[AI एजेंट्स और एजेंट उपयोग मामलों का परिचय](../01-intro-to-ai-agents/README.md)

## अगला पाठ

[एजेंटिक डिजाइन पैटर्न्स को समझना](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
अस्वीकरण:
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। हालांकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। हम इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए ज़िम्मेदार नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->