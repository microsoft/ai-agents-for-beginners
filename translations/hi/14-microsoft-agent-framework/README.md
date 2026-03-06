# माइक्रोसॉफ्ट एजेंट फ्रेमवर्क का अन्वेषण

![Agent Framework](../../../translated_images/hi/lesson-14-thumbnail.90df0065b9d234ee.webp)

### परिचय

यह पाठ निम्नलिखित विषयों को कवर करेगा:

- माइक्रोसॉफ्ट एजेंट फ्रेमवर्क को समझना: मुख्य विशेषताएँ और मूल्य  
- माइक्रोसॉफ्ट एजेंट फ्रेमवर्क के प्रमुख संकल्पनाओं का अन्वेषण
- उन्नत MAF पैटर्न: वर्कफ़्लोज़, मिडलवेयर, और मेमोरी

## सीखने के लक्ष्य

यह पाठ पूरा करने के बाद, आप जानेंगे कि कैसे:

- माइक्रोसॉफ्ट एजेंट फ्रेमवर्क का उपयोग करके प्रोडक्शन रेडी AI एजेंट बनाएं
- माइक्रोसॉफ्ट एजेंट फ्रेमवर्क की मूल विशेषताओं को अपने एजेन्टिक उपयोग मामलों पर लागू करें
- उन्नत पैटर्न जैसे वर्कफ़्लोज़, मिडलवेयर, और ऑब्ज़रवेबिलिटी का उपयोग करें

## कोड उदाहरण

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) के लिए कोड उदाहरण इस रिपॉजिटरी में `xx-python-agent-framework` और `xx-dotnet-agent-framework` फाइलों के अंतर्गत उपलब्ध हैं।

## माइक्रोसॉफ्ट एजेंट फ्रेमवर्क को समझना

![Framework Intro](../../../translated_images/hi/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) माइक्रोसॉफ्ट का एक एकीकृत फ्रेमवर्क है जो AI एजेंट बनाने के लिए है। यह दोनों प्रोडक्शन और अनुसंधान वातावरणों में देखे जाने वाले एजेन्टिक उपयोग मामलों की विस्तृत विविधता को संबोधित करने की लचीलापन प्रदान करता है, जैसे:

- उन परिदृश्यों में जहां चरण-दर-चरण वर्कफ़्लोज़ की आवश्यकता होती है, **क्रमिक एजेंट ऑर्केस्ट्रेशन**।
- उन परिदृश्यों में जहां एजेंटों को एक साथ कार्य पूरे करने होते हैं, **सहमति ऑर्केस्ट्रेशन**।
- उन परिदृश्यों में जहां एजेंट एक साथ मिलकर एक कार्य करते हैं, **ग्रुप चैट ऑर्केस्ट्रेशन**।
- उन परिदृश्यों में जहां उप-कार्यों को पूरा करते हुए एजेंट एक दूसरे को कार्य सौंपते हैं, **हैंडऑफ ऑर्केस्ट्रेशन**।
- उन परिदृश्यों में जहां एक प्रबंधक एजेंट टास्क सूची बनाता है और संशोधित करता है और उप-एजेंट्स का समन्वय करता है, **मैग्नेटिक ऑर्केस्ट्रेशन**।

AI एजेंट प्रोडक्शन में प्रदान करने के लिए, MAF में निम्नलिखित विशेषताएं भी शामिल हैं:

- **ऑब्जरवेबिलिटी** OpenTelemetry के उपयोग के माध्यम से जहाँ AI एजेंट की हर क्रिया जैसे टूल आवाहन, ऑर्केस्ट्रेशन चरण, तर्क प्रवाह और Microsoft Foundry डैशबोर्ड के माध्यम से प्रदर्शन निगरानी होती है।
- **सुरक्षा** एजेंटों को Microsoft Foundry पर मूल रूप से होस्ट करके, जिसमें भूमिका-आधारित पहुंच, निजी डेटा प्रबंधन, और इन-बिल्ट कंटेंट सुरक्षा नियंत्रण शामिल हैं।
- **दृढ़ता** एजेंट थ्रेड्स और वर्कफ़्लोज़ को रोकने, फिर से शुरू करने और त्रुटियों से रिकवर करने में सक्षम बनाना, जो लंबे चलने वाली प्रक्रियाओं को संभव बनाता है।
- **नियंत्रण** जहां मानव इन-द-लूप वर्कफ़्लोज़ समर्थित हैं, जिसमें कार्यों को मानव अनुमोदन की आवश्यकता के रूप में चिह्नित किया जाता है।

माइक्रोसॉफ्ट एजेंट फ्रेमवर्क का उद्देश्य इंटरऑपरेबल होना भी है:

- **क्लाउड-एग्नोस्टिक होना** - एजेंट कंटेनरों, ऑन-प्रिमाइसेस और विभिन्न क्लाउड्स में चल सकते हैं।
- **प्रोवाइडर-एग्नोस्टिक होना** - एजेंट्स को Azure OpenAI, OpenAI सहित आपके पसंदीदा SDK के माध्यम से बनाया जा सकता है।
- **ओपन स्टैंडर्ड्स के साथ एकीकरण** - एजेंट्स Agent-to-Agent(A2A) और Model Context Protocol (MCP) जैसे प्रोटोकॉल का उपयोग करके अन्य एजेंट्स और टूल्स को खोज और उपयोग कर सकते हैं।
- **प्लगइन्स और कनेक्टर्स** - Microsoft Fabric, SharePoint, Pinecone और Qdrant जैसी डेटा और मेमोरी सेवाओं से कनेक्शन बनाया जा सकता है।

आइए देखें कि इन विशेषताओं को माइक्रोसॉफ्ट एजेंट फ्रेमवर्क के कुछ मूल संकल्पनाओं में कैसे लागू किया जाता है।

## माइक्रोसॉफ्ट एजेंट फ्रेमवर्क की प्रमुख संकल्पनाएँ

### एजेंट्स

![Agent Framework](../../../translated_images/hi/agent-components.410a06daf87b4fef.webp)

**एजेंट बनाना**

एजेंट निर्माण की प्रक्रिया में इंफरेंस सेवा (LLM प्रोवाइडर) को परिभाषित करना, AI एजेंट को पालन करने के लिए निर्देशों का एक सेट, और एक असाइन किया गया `name` शामिल है:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

ऊपर `Azure OpenAI` का उपयोग हो रहा है, लेकिन एजेंटों को विभिन्न सेवाओं का उपयोग करके बनाया जा सकता है, जिनमें `Microsoft Foundry Agent Service` भी शामिल है:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI के `Responses`, `ChatCompletion` API

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

या A2A प्रोटोकॉल का उपयोग करके रिमोट एजेंट्स:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**एजेंट चलाना**

एजेंट्स को `.run` या `.run_stream` मेथड्स का उपयोग करके चलाया जाता है, गैर-स्ट्रीमिंग या स्ट्रीमिंग प्रतिक्रियाओं के लिए।

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

प्रत्येक एजेंट रन के लिए विकल्प भी हो सकते हैं जिनसे पैरामीटर्स को कस्टमाइज़ किया जा सके जैसे कि एजेंट द्वारा उपयोग किए जाने वाले `max_tokens`, एजेंट द्वारा कॉल किए जाने वाले `tools`, और यहां तक कि एजेंट के लिए उपयोग किए जाने वाला `model` भी।

यह उन मामलों में उपयोगी होता है जहां उपयोगकर्ता के कार्य को पूरा करने के लिए विशिष्ट मॉडल या टूल्स की आवश्यकता होती है।

**टूल्स**

टूल्स को एजेंट को परिभाषित करते समय भी परिभाषित किया जा सकता है:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# जब सीधे एक ChatAgent बनाया जा रहा हो

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

और एजेंट को चलाते समय भी:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # इस रन के लिए केवल प्रदान किया गया उपकरण )
```

**एजेंट थ्रेड्स**

एजेंट थ्रेड्स मल्टी-टर्न वार्तालापों को संभालने के लिए उपयोग किए जाते हैं। थ्रेड्स को निम्नलिखित तरीकों से बनाया जा सकता है:

- `get_new_thread()` का उपयोग करके, जिससे थ्रेड समय के साथ सहेजा जा सके।
- एजेंट चलाते समय स्वचालित रूप से एक थ्रेड बनाना जो केवल वर्तमान रन के दौरान ही स्थायी रहे।

एक थ्रेड बनाने के लिए कोड इस प्रकार होगा:

```python
# एक नया थ्रेड बनाएं।
thread = agent.get_new_thread() # थ्रेड के साथ एजेंट चलाएं।
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

फिर आप थ्रेड को बाद में उपयोग के लिए सिरीयलाइज़ कर सकते हैं:

```python
# एक नया थ्रेड बनाएं।
thread = agent.get_new_thread() 

# थ्रेड के साथ एजेंट चलाएं।

response = await agent.run("Hello, how are you?", thread=thread) 

# संग्रहण के लिए थ्रेड को सीरियलाइज़ करें।

serialized_thread = await thread.serialize() 

# संग्रहण से लोड करने के बाद थ्रेड स्थिति को डीसीरियलाइज़ करें।

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**एजेंट मिडलवेयर**

एजेंट उपयोगकर्ता के कार्य पूरे करने के लिए टूल्स और LLM के साथ संवाद करते हैं। कुछ परिदृश्यों में, हम इन इंटरैक्शनों के बीच निष्पादन या ट्रैकिंग करना चाहते हैं। एजेंट मिडलवेयर हमें यह करने की अनुमति देता है:

*फंक्शन मिडलवेयर*

यह मिडलवेयर एजेंट और उस फंक्शन/टूल के बीच कोई क्रिया निष्पादित करने की अनुमति देता है जिसे यह कॉल कर रहा है। इसका उपयोग तब किया जाता है जब आप फंक्शन कॉल पर कुछ लॉगिंग करना चाहते हैं।

नीचे के कोड में `next` यह परिभाषित करता है कि अगला मिडलवेयर या वास्तविक फंक्शन कॉल करना चाहिए।

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # पूर्व-संसोधन: फ़ंक्शन निष्पादन से पहले लॉग करें
    print(f"[Function] Calling {context.function.name}")

    # अगली मिडलवेयर या फ़ंक्शन निष्पादन पर जारी रखें
    await next(context)

    # पश्च-संसोधन: फ़ंक्शन निष्पादन के बाद लॉग करें
    print(f"[Function] {context.function.name} completed")
```

*चैट मिडलवेयर*

यह मिडलवेयर एजेंट और LLM के बीच अनुरोधों पर कोई क्रिया निष्पादित करने या लॉगिंग करने की अनुमति देता है।

यह महत्वपूर्ण जानकारी जैसे कि AI सेवा को भेजे जा रहे `messages` को भी रखता है।

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # पूर्व-संसाधन: AI कॉल से पहले लॉग करें
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # अगले मिडलवेयर या AI सेवा पर जारी रखें
    await next(context)

    # पश्च-संसाधन: AI प्रतिक्रिया के बाद लॉग करें
    print("[Chat] AI response received")

```

**एजेंट मेमोरी**

`Agentic Memory` पाठ में कवर किए जाने के अनुसार, मेमोरी एजेंट को विभिन्न संदर्भों पर संचालित करने में सक्षम बनाता है। MAF विभिन्न प्रकार की मेमोरी प्रदान करता है:

*इन-मेमोरी स्टोरेज*

यह एप्लिकेशन रनटाइम के दौरान थ्रेड्स में संग्रहीत मेमोरी है।

```python
# एक नया थ्रेड बनाएँ।
thread = agent.get_new_thread() # थ्रेड के साथ एजेंट चलाएँ।
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*स्थायी संदेश*

यह मेमोरी विभिन्न सत्रों में वार्तालाप इतिहास संग्रहीत करने के लिए उपयोग की जाती है। इसे `chat_message_store_factory` का उपयोग करके परिभाषित किया जाता है:

```python
from agent_framework import ChatMessageStore

# एक कस्टम संदेश स्टोर बनाएं
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*डायनेमिक मेमोरी*

यह मेमोरी एजेंट्स के चलने से पहले संदर्भ में जोड़ी जाती है। ये मेमोरी बाहरी सेवाओं जैसे mem0 में संग्रहीत की जा सकती हैं:

```python
from agent_framework.mem0 import Mem0Provider

# उन्नत मेमोरी क्षमताओं के लिए Mem0 का उपयोग करना
memory_provider = Mem0Provider(
    api_key="your-mem0-api-key",
    user_id="user_123",
    application_id="my_app"
)

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a helpful assistant with memory.",
    context_providers=memory_provider
)

```

**एजेंट ऑब्जरवेबिलिटी**

विश्वसनीय और अनुरक्षित एजेंटिक सिस्टम बनाने के लिए ऑब्जरवेबिलिटी महत्वपूर्ण है। MAF बेहतर ऑब्जरवेबिलिटी के लिए OpenTelemetry के साथ एकीकरण करता है जो ट्रेसिंग और मीटर्स प्रदान करता है।

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # कुछ करें
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### वर्कफ़्लोज़

MAF वर्कफ़्लोज़ प्रदान करता है जो कार्य पूरा करने के लिए पूर्व-परिभाषित चरण होते हैं और उन चरणों में AI एजेंट्स घटकों के रूप में शामिल होते हैं।

वर्कफ़्लोज़ विभिन्न घटकों से बने होते हैं जो बेहतर नियंत्रण प्रवाह की अनुमति देते हैं। वर्कफ़्लोज़ **मल्टी-एजेंट ऑर्केस्ट्रेशन** और वर्कफ़्लो अवस्थाओं को सहेजने के लिए **चेकपॉइंटिंग** सक्षम करते हैं।

वर्कफ़्लो के मुख्य घटक हैं:

**एक्जीक्यूटर्स**

एक्जीक्यूटर्स इनपुट संदेश प्राप्त करते हैं, अपने निर्दिष्ट कार्य करते हैं, और फिर आउटपुट संदेश उत्पन्न करते हैं। यह बड़ा कार्य पूरा करने की दिशा में वर्कफ़्लो को आगे बढ़ाता है। एक्जीक्यूटर्स AI एजेंट या कस्टम लॉजिक हो सकते हैं।

**एजेस**

एजेस वर्कफ़्लो में संदेशों के प्रवाह को परिभाषित करने के लिए उपयोग होते हैं। ये हो सकते हैं:

*डायरेक्ट एजेस* - एक्जीक्यूटर्स के बीच सरल वन-टू-वन कनेक्शन:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*कंडीशनल एजेस* - किसी विशेष शर्त पूरी होने के बाद सक्रिय होते हैं। उदाहरण के लिए, जब होटल के कमरे उपलब्ध नहीं हैं, तो एक्जीक्यूटर अन्य विकल्प सुझा सकता है।

*स्विच-केस एजेस* - परिभाषित शर्तों के आधार पर संदेशों को विभिन्न एक्जीक्यूटर्स तक मार्ग देते हैं। उदाहरण के तौर पर, यदि यात्रा ग्राहक के पास प्रायरिटी एक्सेस है तो उनके कार्य अन्य वर्कफ़्लो के माध्यम से संभाले जाएंगे।

*फैन-आउट एजेस* - एक संदेश को कई लक्ष्यों को भेजें।

*फैन-इन एजेस* - विभिन्न एक्जीक्यूटर्स से कई संदेशों को एक लक्ष्य तक एकत्रित करें।

**इवेंट्स**

वर्कफ़्लोज़ में बेहतर ऑब्जरवेबिलिटी प्रदान करने के लिए, MAF निष्पादन के लिए इन-बिल्ट इवेंट्स प्रदान करता है, जिनमें शामिल हैं:

- `WorkflowStartedEvent` - वर्कफ़्लो निष्पादन शुरू होता है
- `WorkflowOutputEvent` - वर्कफ़्लो आउटपुट उत्पन्न करता है
- `WorkflowErrorEvent` - वर्कफ़्लो में त्रुटि आती है
- `ExecutorInvokeEvent` - एक्जीक्यूटर प्रोसेसिंग शुरू करता है
- `ExecutorCompleteEvent` - एक्जीक्यूटर प्रोसेसिंग समाप्त करता है
- `RequestInfoEvent` - एक अनुरोध जारी किया जाता है

## उन्नत MAF पैटर्न

ऊपर के अनुभाग माइक्रोसॉफ्ट एजेंट फ्रेमवर्क की प्रमुख संकल्पनाओं को कवर करते हैं। अधिक जटिल एजेंट्स बनाते समय, यहां कुछ उन्नत पैटर्न हैं जिन पर विचार करना चाहिए:

- **मिडलवेयर संयोजन**: एजेंट व्यवहार पर सूक्ष्म नियंत्रण के लिए फंक्शन और चैट मिडलवेयर का उपयोग करके कई मिडलवेयर हैंडलर्स (लॉगिंग, प्रमाणीकरण, रेट-लिमिटिंग) को चेन करें।
- **वर्कफ़्लो चेकपॉइंटिंग**: लंबे चलने वाले एजेंट प्रक्रियाओं को बचाने और फिर से शुरू करने के लिए वर्कफ़्लो इवेंट्स और सिरीयलाइज़ेशन का उपयोग करें।
- **डायनेमिक टूल चयन**: प्रति क्वेरी केवल प्रासंगिक टूल प्रस्तुत करने के लिए टूल विवरणों पर RAG के साथ MAF के टूल रजिस्ट्रेशन को मिलाएं।
- **मल्टी-एजेंट हैंडऑफ**: विशिष्ट एजेंट्स के बीच हैंडऑफ को ऑर्केस्ट्रेट करने के लिए वर्कफ़्लो एजेस और कंडीशनल रूटिंग का उपयोग करें।

## कोड उदाहरण

Microsoft Agent Framework के लिए कोड उदाहरण इस रिपॉजिटरी में `xx-python-agent-framework` और `xx-dotnet-agent-framework` फाइलों के अंतर्गत उपलब्ध हैं।

## माइक्रोसॉफ्ट एजेंट फ्रेमवर्क के बारे में और प्रश्न हैं?

अन्य शिक्षार्थियों से मिलने, ऑफिस आवर्स अटेंड करने और अपने AI एजेंट्स से जुड़े सवालों के उत्तर पाने के लिए [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) से जुड़ें।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनूदित किया गया है। हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में प्राधिकृत स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->