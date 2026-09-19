# माइक्रोसॉफ्ट एजेंट फ्रेमवर्क का अन्वेषण

![Agent Framework](../../../translated_images/hi/lesson-14-thumbnail.90df0065b9d234ee.webp)

### परिचय

यह पाठ निम्नलिखित को कवर करेगा:

- माइक्रोसॉफ्ट एजेंट फ्रेमवर्क को समझना: प्रमुख विशेषताएं और मूल्य  
- माइक्रोसॉफ्ट एजेंट फ्रेमवर्क के मुख्य अवधारणाओं का अन्वेषण
- उन्नत MAF पैटर्न: वर्कफ़्लोज़, मिडलवेयर, और मेमोरी

## सीखने के लक्ष्य

इस पाठ को पूरा करने के बाद, आप जानेंगे कि कैसे:

- माइक्रोसॉफ्ट एजेंट फ्रेमवर्क का उपयोग करके उत्पादन-तैयार एआई एजेंट बनाएँ
- अपने एजेंटिक उपयोग मामलों पर माइक्रोसॉफ्ट एजेंट फ्रेमवर्क की मुख्य विशेषताओं को लागू करें
- वर्कफ़्लोज़, मिडलवेयर, और ऑब्ज़र्वेबिलिटी सहित उन्नत पैटर्न का उपयोग करें

## कोड नमूने 

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) के कोड नमूने इस रिपॉजिटरी में `xx-python-agent-framework` और `xx-dotnet-agent-framework` फाइलों में पाए जा सकते हैं।

## माइक्रोसॉफ्ट एजेंट फ्रेमवर्क को समझना

![Framework Intro](../../../translated_images/hi/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) माइक्रोसॉफ्ट का AI एजेंट बनाने के लिए एक एकीकृत फ्रेमवर्क है। यह उत्पादन और अनुसंधान वातावरणों में देखे जाने वाले एजेंटिक उपयोग मामलों की व्यापक विविधता को संबोधित करने की लचीलापन प्रदान करता है, जिनमें शामिल हैं:

- **क्रमिक एजेंट ऑर्केस्ट्रेशन** ऐसे परिदृश्यों में जहां चरण-दर-चरण वर्कफ़्लोज़ की आवश्यकता होती है।
- **संकुल ऑर्केस्ट्रेशन** ऐसे परिदृश्यों में जहां एजेंटों को एक साथ कार्य पूरे करने होते हैं।
- **ग्रुप चैट ऑर्केस्ट्रेशन** ऐसे परिदृश्यों में जहां एजेंट एक साथ एक कार्य पर सहयोग कर सकते हैं।
- **हैंडऑफ ऑर्केस्ट्रेशन** ऐसे परिदृश्यों में जहां एजेंट एक-दूसरे को कार्य सौंपते हैं जैसे-जैसे उपकार्य पूरे होते हैं।
- **मैग्नेटिक ऑर्केस्ट्रेशन** ऐसे परिदृश्यों में जहां एक प्रबंधक एजेंट कार्य सूची बनाता और संशोधित करता है और उप-एजेंट्स के समन्वय को संभालता है ताकि कार्य पूरे हो सकें।

उत्पादन में एआई एजेंट प्रदान करने के लिए, MAF में निम्नलिखित सुविधाएँ भी शामिल हैं:

- **ऑब्ज़र्वेबिलिटी** OpenTelemetry के उपयोग के माध्यम से जहाँ AI एजेंट की हर क्रिया जैसे टूल का आह्वान, ऑर्केस्ट्रेशन चरण, कारण प्रवाह और प्रदर्शन निगरानी Microsoft Foundry डैशबोर्ड्स के माध्यम से होती है।
- **सुरक्षा** एजेंट्स को माइक्रोसॉफ्ट फाउंड्री पर नेटिव होस्ट करके जो कि भूमिका-आधारित पहुंच, निजी डेटा हैंडलिंग और अंतर्निर्मित सामग्री सुरक्षा जैसे सुरक्षा नियंत्रण शामिल करता है।
- **टिकाऊपन** क्योंकि एजेंट थ्रेड्स और वर्कफ़्लोज़ को रुका, फिर से चालू किया जा सकता है और त्रुटियों से पुनर्प्राप्त किया जा सकता है जिससे लंबी चलने वाली प्रक्रियाएँ संभव होती हैं।
- **नियंत्रण** जहां मानव अनुमोदन आवश्यक होता है, वहाँ मानव इंटरैक्शन वर्कफ़्लोज़ समर्थित हैं।

माइक्रोसॉफ्ट एजेंट फ्रेमवर्क का लक्ष्य इंटरऑपरेबल होना भी है:

- **क्लाउड-उदासीन होना** - एजेंट कंटेनरों, ऑन-प्रेम, और विभिन्न क्लाउड्स पर चल सकते हैं।
- **प्रदाता-उदासीन होना** - एजेंट आपके पसंदीदा SDK, जैसे Azure OpenAI और OpenAI के माध्यम से बनाए जा सकते हैं।
- **ओपन स्टैंडर्ड्स का एकीकरण** - एजेंट ऐसे प्रोटोकॉल का उपयोग कर सकते हैं जैसे Agent-to-Agent (A2A) और Model Context Protocol (MCP) अन्य एजेंट्स और टूल्स को खोजने और उपयोग करने के लिए।
- **प्लगइन्स और कनेक्टर्स** - डेटा और मेमोरी सेवाओं जैसे Microsoft Fabric, SharePoint, Pinecone, और Qdrant से कनेक्शन बनाए जा सकते हैं।

आइए देखें कि ये विशेषताएं माइक्रोसॉफ्ट एजेंट फ्रेमवर्क के कुछ मुख्य अवधारणाओं पर कैसे लागू होती हैं।

## माइक्रोसॉफ्ट एजेंट फ्रेमवर्क की मुख्य अवधारणाएँ

### एजेंट्स

![Agent Framework](../../../translated_images/hi/agent-components.410a06daf87b4fef.webp)

**एजेंट बनाना**

एजेंट निर्माण उस सर्विस (एलएलएम प्रोवाइडर) को परिभाषित करके किया जाता है जिसकी सहायता से AI एजेंट काम करेगा, एक
निर्देशों का सेट जिसे AI एजेंट को पालन करना होता है, और एक असाइन किया गया `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

उपरोक्त में `Azure OpenAI` का उपयोग हो रहा है लेकिन एजेंट विभिन्न सेवाओं के साथ बनाए जा सकते हैं जिनमें `Microsoft Foundry Agent Service` भी शामिल है:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` APIs

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

या [MiniMax](https://platform.minimaxi.com/), जो OpenAI-संगत API प्रदान करता है बड़ी संदर्भ विंडोज़ (204K टोकन्स तक) के साथ:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

या A2A प्रोटोकॉल का उपयोग करके रिमोट एजेंट्स:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**एजेंट चलाना**

एजेंट्स को `.run` या `.run_stream` मेथड का उपयोग करके चलाया जाता है, जो गैर-स्ट्रीमिंग या स्ट्रीमिंग प्रतिक्रियाओं के लिए होता है।

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

प्रत्येक एजेंट रन में विकल्प भी हो सकते हैं जैसे कि एजेंट द्वारा उपयोग किए गए `max_tokens`, एजेंट द्वारा कॉल किए जाने वाले `tools`, और यहां तक कि एजेंट के लिए उपयोग किया गया `model`।

यह उपयोगी होता है जब विशिष्ट मॉडल या टूल्स उपयोगकर्ता के कार्य को पूरा करने के लिए आवश्यक होते हैं।

**टूल्स**

टूल्स को एजेंट को परिभाषित करते समय भी निर्धारित किया जा सकता है:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# जब सीधे एक ChatAgent बनाया जा रहा हो

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

और एजेंट चलाते समय भी:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # इस रन के लिए केवल टूल प्रदान किया गया है )
```

**एजेंट थ्रेड्स**

एजेंट थ्रेड्स का उपयोग मल्टी-टर्न संवादों को हैंडल करने के लिए किया जाता है। थ्रेड्स को बनाने के दो तरीके हैं:

- `get_new_thread()` का उपयोग करना जो थ्रेड को समय के साथ सहेजने में सक्षम बनाता है
- एजेंट चलाते समय स्वचालित रूप से एक थ्रेड बनाना जो केवल वर्तमान रन के दौरान रहता है।

थ्रेड बनाने के लिए कोड ऐसा दिखता है:

```python
# एक नया थ्रेड बनाएं।
thread = agent.get_new_thread() # थ्रेड के साथ एजेंट चलाएं।
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

आप बाद में उपयोग के लिए थ्रेड को सीरियलाइज़ भी कर सकते हैं:

```python
# एक नया थ्रेड बनाएं।
thread = agent.get_new_thread() 

# थ्रेड के साथ एजेंट चलाएं।

response = await agent.run("Hello, how are you?", thread=thread) 

# संग्रहण के लिए थ्रेड को सीरियलाइज़ करें।

serialized_thread = await thread.serialize() 

# संग्रहण से लोड करने के बाद थ्रेड की स्थिति को डीसीरियलाइज़ करें।

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**एजेंट मिडलवेयर**

एजेंट टूल्स और LLM के साथ बातचीत करते हैं उपयोगकर्ता के कार्यों को पूरा करने के लिए। कुछ परिदृश्यों में, हम इन इंटरैक्शनों के बीच कुछ कार्रवाई करना या ट्रैक करना चाहते हैं। एजेंट मिडलवेयर हमें यह करने में सक्षम बनाता है:

*फंक्शन मिडलवेयर*

यह मिडलवेयर एजेंट और उस फंक्शन/टूल के बीच एक क्रिया निष्पादित करने की अनुमति देता है जिसे एजेंट कॉल करेगा। एक उदाहरण तब हो सकता है जब आप फंक्शन कॉल पर कुछ लॉगिंग करना चाहते हैं।

नीचे दिए गए कोड में `next` यह निर्धारित करता है कि अगला मिडलवेयर या वास्तविक फंक्शन कॉल किया जाना चाहिए।

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # प्री-प्रोसेसिंग: फ़ंक्शन निष्पादन से पहले लॉग करें
    print(f"[Function] Calling {context.function.name}")

    # अगले मिडलवेयर या फ़ंक्शन निष्पादन पर जारी रखें
    await next(context)

    # पोस्ट-प्रोसेसिंग: फ़ंक्शन निष्पादन के बाद लॉग करें
    print(f"[Function] {context.function.name} completed")
```

*चैट मिडलवेयर*

यह मिडलवेयर एजेंट और LLM के बीच अनुरोधों के बीच क्रिया निष्पादित करने या लॉग करने की अनुमति देता है।

इसमें महत्वपूर्ण जानकारी होती है जैसे वे `messages` जो AI सेवा को भेजे जा रहे होते हैं।

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # पूर्व-प्रक्रिया: AI कॉल से पहले लॉग
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # अगले मिडलवेयर या AI सेवा पर जारी रखें
    await next(context)

    # पश्च-प्रक्रिया: AI प्रतिक्रिया के बाद लॉग
    print("[Chat] AI response received")

```

**एजेंट मेमोरी**

जैसा कि `Agentic Memory` पाठ में कवर किया गया है, मेमोरी एजेंट को विभिन्न संदर्भों में काम करने के लिए सक्षम बनाने का एक महत्वपूर्ण तत्व है। MAF कई प्रकार की मेमोरी प्रदान करता है:

*इन-मेमोरी स्टोरेज*

यह मेमोरी एप्लीकेशन रनटाइम के दौरान थ्रेड्स में संग्रहीत होती है।

```python
# एक नई थ्रेड बनाएं।
thread = agent.get_new_thread() # थ्रेड के साथ एजेंट चलाएं।
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*पर्सिस्टेंट मैसेजेस*

यह मेमोरी विभिन्न सत्रों में संवाद इतिहास संग्रहीत करने के लिए उपयोग की जाती है। इसे `chat_message_store_factory` का उपयोग करके परिभाषित किया जाता है:

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

*डायनामिक मेमोरी*

यह मेमोरी एजेंट्स रन होने से पहले संदर्भ में जोड़ी जाती है। ये मेमोरीज़ बाहरी सेवाओं जैसे mem0 में संग्रहीत हो सकती हैं:

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

**एजेंट ऑब्ज़र्वेबिलिटी**

ऑब्ज़र्वेबिलिटी विश्वसनीय और रखरखाव योग्य एजेंटिक सिस्टम बनाने के लिए महत्वपूर्ण है। MAF OpenTelemetry के साथ एकीकृत होती है ताकि बेहतर ऑब्जर्वेबिलिटी के लिए ट्रेसिंग और मीटर्स प्रदान किया जा सके।

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # कुछ करो
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### वर्कफ़्लोज़

MAF वर्कफ़्लोज़ प्रदान करता है जो किसी कार्य को पूरा करने के लिए पूर्व-परिभाषित चरण होते हैं और उन चरणों में AI एजेंट्स को घटकों के रूप में शामिल करता है।

वर्कफ़्लोज़ विभिन्न घटकों से बने होते हैं जो बेहतर नियंत्रण प्रवाह की अनुमति देते हैं। वर्कफ़्लोज़ **मल्टी-एजेंट ऑर्केस्ट्रेशन** और **चेकपॉइंटिंग** की भी अनुमति देते हैं ताकि वर्कफ़्लो की स्थिति सहेजी जा सके।

वर्कफ़्लो के मुख्य घटक हैं:

**एग्जिक्यूटर्स**

एग्जिक्यूटर्स इनपुट संदेश प्राप्त करते हैं, अपने सौंपे हुए कार्य करते हैं, और फिर आउटपुट संदेश उत्पन्न करते हैं। यह वर्कफ़्लो को बड़े कार्य के पूर्ण होने की ओर आगे बढ़ाता है। एग्जिक्यूटर्स AI एजेंट या कस्टम लॉजिक हो सकते हैं।

**एजेस**

एजेस वर्कफ़्लो में संदेशों के प्रवाह को परिभाषित करने के लिए उपयोग होते हैं। ये हो सकते हैं:

*प्रत्यक्ष एजेस* - एग्जिक्यूटर्स के बीच सरल एक-दूसरे से जुड़ाव:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*शर्तीय एजेस* - जब कुछ विशेष शर्त पूरी हो जाती है तो सक्रिय होते हैं। उदाहरण के लिए, जब होटल के कमरे उपलब्ध नहीं होते, तो एक एग्जिक्यूटर अन्य विकल्प सुझा सकता है।

*स्विच-केस एजेस* - परिभाषित शर्तों के आधार पर संदेशों को विभिन्न एग्जिक्यूटर्स को मार्गदर्शित करना। उदाहरण के लिए, यदि यात्रा ग्राहक के पास प्राथमिकता वाली पहुँच है और उनके कार्य दूसरे वर्कफ़्लो के माध्यम से संभाले जाएंगे।

*फैन-आउट एजेस* - एक संदेश को कई लक्ष्यों को भेजना।

*फैन-इन एजेस* - विभिन्न एग्जिक्यूटर्स से कई संदेशों को इकट्ठा करना और एक लक्ष्य को भेजना।

**इवेंट्स**

वर्कफ़्लोज़ में बेहतर ऑब्ज़र्वेबिलिटी प्रदान करने के लिए, MAF निम्नलिखित एग्जिक्यूशन के लिए अंतर्निर्मित इवेंट्स प्रदान करता है:

- `WorkflowStartedEvent`  - वर्कफ़्लो एग्जिक्यूशन शुरू होता है
- `WorkflowOutputEvent` - वर्कफ़्लो आउटपुट उत्पन्न करता है
- `WorkflowErrorEvent` - वर्कफ़्लो में त्रुटि आती है
- `ExecutorInvokeEvent`  - एग्जिक्यूटर प्रोसेसिंग शुरू करता है
- `ExecutorCompleteEvent`  - एग्जिक्यूटर प्रोसेसिंग समाप्त करता है
- `RequestInfoEvent` - अनुरोध जारी किया जाता है

## उन्नत MAF पैटर्न

ऊपर के खंड माइक्रोसॉफ्ट एजेंट फ्रेमवर्क की मुख्य अवधारणाओं को कवर करते हैं। जब आप अधिक जटिल एजेंट बनाते हैं, तो यहाँ कुछ उन्नत पैटर्न हैं जिन पर विचार करना चाहिए:

- **मिडलवेयर संयोजन**: कई मिडलवेयर हैंडलर्स (लॉगिंग, ऑथ, रेट-लिमिटिंग) को फंक्शन और चैट मिडलवेयर के उपयोग से कड़ी बनाना ताकि एजेंट व्यवहार पर सूक्ष्म नियंत्रण संभव हो।
- **वर्कफ़्लो चेकपॉइंटिंग**: लंबी चलने वाली एजेंट प्रक्रियाओं को सहेजने और फिर से शुरू करने के लिए वर्कफ़्लो इवेंट्स और सीरियलाइज़ेशन का उपयोग करें।
- **डायनामिक टूल चयन**: टूल विवरणों पर RAG को MAF के टूल पंजीकरण के साथ संयोजित करें ताकि प्रति क्वेरी केवल प्रासंगिक टूल्स प्रस्तुत किए जा सकें।
- **मल्टी-एजेंट हैंडऑफ**: वर्कफ़्लो एजेस और शर्तीय रूटिंग का उपयोग करके विशेषज्ञ एजेंट्स के बीच हैंडऑफ का समन्वय करें।

## माइक्रोसॉफ्ट फाउंड्री पर LangChain / LangGraph एजेंट्स की होस्टिंग

माइक्रोसॉफ्ट एजेंट फ्रेमवर्क **फ्रेमवर्क-इंटरऑपरेबल** है — आप केवल MAF के साथ लिखे गए एजेंटों तक सीमित नहीं हैं। यदि आपके पास पहले से **LangChain** या **LangGraph** के साथ बनाया गया एजेंट है, तो आप इसे एक **Microsoft Foundry होस्टेड एजेंट** के रूप में चला सकते हैं ताकि Foundry रनटाइम, सत्र, स्केलिंग, पहचान, और प्रोटोकॉल एंडपॉइंट का प्रबंधन करे, जबकि आपकी एजेंट लॉजिक LangGraph में बनी रहे।

यह `langchain_azure_ai.agents.hosting` पैकेज के साथ किया जाता है, जो उसी प्रोटोकॉल पर संकलित LangGraph ग्राफ़ को उजागर करता है जिसका उपयोग Foundry होस्टेड एजेंट करते हैं।

**1. होस्टिंग एक्स्ट्रा इंस्टॉल करें:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` एक्स्ट्रा Foundry प्रोटोकॉल लाइब्रेरीज इंस्टॉल करता है: `azure-ai-agentserver-responses` (OpenAI-संगत `/responses` एंडपॉइंट) और `azure-ai-agentserver-invocations` (सामान्य `/invocations` एंडपॉइंट)।

**2. एक होस्टिंग प्रोटोकॉल चुनें:**

| प्रोटोकॉल | होस्ट क्लास | एंडपॉइंट | उपयोग कब करें |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | आप OpenAI-संगत चैट, स्ट्रीमिंग, प्रतिक्रिया इतिहास, और बातचीत थ्रेडिंग चाहते हैं — वार्तालाप एजेंटों के लिए अनुशंसित डिफ़ॉल्ट। |
| **Invocations** | `InvocationsHostServer` | `/invocations` | आपको कस्टम JSON प्रारूप, वेबहुक-शैली का एंडपॉइंट, या गैर-वार्तालाप प्रसंस्करण की आवश्यकता है। |

क्योंकि **Responses API Foundry में एजेंट-शैली विकास के लिए प्राथमिक API है**, अधिकांश एजेंटों के लिए `ResponsesHostServer` से शुरू करें।

**3. पर्यावरण चर कॉन्फ़िगर करें** (`az login` पहले चलाएं ताकि `DefaultAzureCredential` प्रमाणित कर सके):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

जब एजेंट बाद में Foundry में होस्टेड एजेंट के रूप में चलता है, तो प्लेटफ़ॉर्म स्वतः ही `FOUNDRY_PROJECT_ENDPOINT` इंजेक्ट करता है।

**4. Responses प्रोटोकॉल पर एक LangGraph एजेंट उजागर करें:**

```python
import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_azure_ai.agents.hosting import ResponsesHostServer

_AZURE_AI_SCOPE = "https://ai.azure.com/.default"


def build_chat_model() -> ChatOpenAI:
    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"].rstrip("/")
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-5-mini")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI यहाँ Foundry प्रोजेक्ट के OpenAI-संगत (Responses) एंडपॉइंट को लक्षित करता है।
    return ChatOpenAI(
        model=deployment,
        base_url=str(openai_client.base_url),
        api_key=token_provider,
    )


def main() -> None:
    graph = create_agent(build_chat_model(), tools=[])
    port = int(os.environ.get("PORT", "8088"))
    ResponsesHostServer(graph).run(port=port)


if __name__ == "__main__":
    main()
```

इसे स्थानीय रूप से `python main.py` के साथ चलाएं, फिर `http://localhost:8088/responses` पर Responses अनुरोध भेजें।

**मुख्य व्यवहार:**

- **बातचीतें**: क्लाइंट `previous_response_id` या `conversation` ID पास करके बातचीत जारी रखते हैं। यदि आपका ग्राफ LangGraph चेकपॉइंटर के साथ संकलित है, तो Foundry बातचीत की स्थिति को चेकपॉइंट के साथ कुंजीबद्ध करता है (उत्पादन में टिकाऊ चेकपॉइंटर का उपयोग करें; स्थानीय परीक्षण के लिए `MemorySaver` ठीक है)।
- **मानव-इन-द-लूप**: यदि आपका ग्राफ LangGraph `interrupt()` का उपयोग करता है, तो `ResponsesHostServer` लंबित इंटरप्ट को Responses `function_call` / `mcp_approval_request` आइटम के रूप में सतह पर लाता है, और क्लाइंट मिलते-जुलते `function_call_output` / `mcp_approval_response` के साथ फिर से शुरू होता है।
- **Foundry में तैनाती करें**: Azure Developer CLI का उपयोग करें — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (स्थानीय, डॉकर आवश्यक), फिर `azd provision` और `azd deploy`। होस्टेड-एजेंट तैनाती के लिए **Foundry प्रोजेक्ट मैनेजर** भूमिका आवश्यक है।

इस उदाहरण का चलने योग्य संस्करण [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) में उपलब्ध है। पूर्ण वॉकथ्रू (Invocations प्रोटोकॉल, कस्टम अनुरोध स्कीमास, और समस्या निवारण) के लिए, देखें [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)।

## कोड नमूने 

माइक्रोसॉफ्ट एजेंट फ्रेमवर्क के कोड नमूने इस रिपॉजिटरी में `xx-python-agent-framework` और `xx-dotnet-agent-framework` फाइलों में पाए जा सकते हैं।

## माइक्रोसॉफ्ट एजेंट फ्रेमवर्क के बारे में अधिक प्रश्न हैं?

अन्य शिक्षार्थियों से मिलने, कार्यालय समय में भाग लेने और अपने AI एजेंट्स के प्रश्नों का उत्तर पाने के लिए [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) में शामिल हों।
## पिछला पाठ

[AI एजेंट्स के लिए मेमोरी](../13-agent-memory/README.md)

## अगला पाठ

[कंप्यूटर उपयोग एजेंट्स का निर्माण (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->