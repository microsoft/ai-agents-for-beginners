# माइक्रोसॉफ्ट एजेंट फ्रेमवर्क का अन्वेषण

![Agent Framework](../../../translated_images/hi/lesson-14-thumbnail.90df0065b9d234ee.webp)

### परिचय

इस पाठ में शामिल हैं:

- माइक्रोसॉफ्ट एजेंट फ्रेमवर्क की समझ: मुख्य विशेषताएं और मूल्य  
- माइक्रोसॉफ्ट एजेंट फ्रेमवर्क के मुख्य अवधारणाओं का अन्वेषण
- उन्नत MAF पैटर्न: वर्कफ़्लोज़, मिडलवेयर, और मेमोरी

## सीखने के लक्ष्य

इस पाठ को पूरा करने के बाद, आप जानेंगे कि कैसे:

- माइक्रोसॉफ्ट एजेंट फ्रेमवर्क का उपयोग करके प्रोडक्शन रेडी AI एजेंट बनाएं
- माइक्रोसॉफ्ट एजेंट फ्रेमवर्क की मुख्य विशेषताओं को अपने एजेंटिक उपयोग मामलों पर लागू करें
- वर्कफ़्लोज़, मिडलवेयर, और ऑब्ज़र्वबिलिटी सहित उन्नत पैटर्न का उपयोग करें

## कोड उदाहरण

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) के लिए कोड उदाहरण इस रिपॉजिटरी में `xx-python-agent-framework` और `xx-dotnet-agent-framework` फ़ाइलों के तहत पाए जा सकते हैं।

## माइक्रोसॉफ्ट एजेंट फ्रेमवर्क की समझ

![Framework Intro](../../../translated_images/hi/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) माइक्रोसॉफ्ट का एक एकीकृत फ्रेमवर्क है जो AI एजेंट बनाने के लिए है। यह उत्पादन और शोध परिवेश दोनों में देखे जाने वाले विभिन्न एजेंटिक उपयोग मामलों को संबोधित करने की लचीलापन प्रदान करता है, जिनमें शामिल हैं:

- **क्रमिक एजेंट आयोजन** उन परिदृश्यों में जहाँ कदम दर कदम वर्कफ़्लोज़ की आवश्यकता होती है।
- **समानांतर आयोजन** उन परिदृश्यों में जहाँ एजेंटों को एक साथ कार्य पूरा करना होता है।
- **समूह चैट आयोजन** उन परिदृश्यों में जहाँ एजेंट किसी एक कार्य पर साथ मिलकर काम कर सकते हैं।
- **हैंडऑफ आयोजन** उन परिदृश्यों में जहाँ एजेंट उप-कार्य पूरे होने पर कार्य को एक-दूसरे को सौंपते हैं।
- **मैग्नेटिक आयोजन** उन परिदृश्यों में जहाँ एक प्रबंधक एजेंट कार्य सूची बनाता और संशोधित करता है और उप-एजेंटों का समन्वय करता है कार्य पूरा करने के लिए।

प्रोडक्शन में AI एजेंट प्रदान करने के लिए, MAF में निम्नलिखित विशेषताएं भी शामिल हैं:

- **ऑब्ज़र्वबिलिटी** OpenTelemetry के उपयोग के माध्यम से जहां AI एजेंट की हर क्रिया जैसे टूल कॉल, आयोजन के चरण, तर्क प्रवाह और प्रदर्शन निगरानी Microsoft Foundry डैशबोर्ड के माध्यम से होती है।
- **सुरक्षा** एजेंटों को Microsoft Foundry पर स्वाभाविक रूप से होस्ट करके जिसमें सुरक्षा नियंत्रण जैसे भूमिका-आधारित पहुँच, निजी डेटा हैंडलिंग और अंतर्निर्मित सामग्री सुरक्षा शामिल है।
- **टिकाऊपन** क्योंकि एजेंट धागे और वर्कफ़्लोज़ को रोक, फिर शुरू और त्रुटियों से पुनर्प्राप्त कर सकते हैं, जो लंबी अवधि वाली प्रक्रियाओं को सक्षम बनाता है।
- **नियंत्रण** क्योंकि मानव इन द लूप वर्कफ़्लोज़ समर्थित हैं जहाँ कार्य मानवीय स्वीकृति की आवश्यकता के रूप में चिन्हित किए जाते हैं।

माइक्रोसॉफ्ट एजेंट फ्रेमवर्क का ध्यान अंतर-संचालनीय बनने पर भी है:

- **क्लाउड-एग्नोस्टिक होना** - एजेंट कंटेनरों, ऑन-प्रिमाइज़ और कई अलग-अलग क्लाउड्स में चल सकते हैं।
- **प्रदाता-एग्नोस्टिक होना** - एजेंट आपके पसंदीदा SDK के माध्यम से बनाए जा सकते हैं जिनमें Azure OpenAI और OpenAI शामिल हैं।
- **ओपन स्टैंडर्ड्स का एकीकरण** - एजेंट Agent-to-Agent (A2A) और Model Context Protocol (MCP) जैसे प्रोटोकॉल का उपयोग कर अन्य एजेंटों और टूल्स का पता लगा सकते हैं और उनका उपयोग कर सकते हैं।
- **प्लगइन्स और कनेक्टर्स** - Microsoft Fabric, SharePoint, Pinecone और Qdrant जैसे डेटा और मेमोरी सेवाओं से कनेक्शन बनाए जा सकते हैं।

आइए देखें कि ये विशेषताएं माइक्रोसॉफ्ट एजेंट फ्रेमवर्क के कुछ मुख्य अवधारणाओं पर कैसे लागू होती हैं।

## माइक्रोसॉफ्ट एजेंट फ्रेमवर्क के मुख्य अवधारणाएं

### एजेंट्स

![Agent Framework](../../../translated_images/hi/agent-components.410a06daf87b4fef.webp)

**एजेंट बनाना**

एजेंट निर्माण इनफेरेंस सेवा (LLM प्रदाता) को परिभाषित करके किया जाता है, 
AI एजेंट के लिए पालन करने के निर्देशों का एक सेट, और एक असाइन किया गया `name`:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

ऊपर `Azure OpenAI` का उपयोग किया जा रहा है लेकिन एजेंट विभिन्न सेवाओं का उपयोग करके बनाए जा सकते हैं जिनमें `Microsoft Foundry Agent Service` भी शामिल है:

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

या [MiniMax](https://platform.minimaxi.com/), जो OpenAI- संगत API बड़े संदर्भ विंडो के साथ प्रदान करता है (204K टोकन तक):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

या A2A प्रोटोकॉल का उपयोग करने वाले रिमोट एजेंट:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**एजेंट चलाना**

एजेंट को `.run` या `.run_stream` विधियों का उपयोग करके चलाया जाता है, जो गैर-स्ट्रीमिंग या स्ट्रीमिंग प्रतिक्रियाओं के लिए होते हैं।

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

प्रत्येक एजेंट रन में विकल्प भी हो सकते हैं, जैसे एजेंट द्वारा उपयोग किए जाने वाले `max_tokens`, जिन्हें एजेंट कॉल कर सकता है ऐसे `tools`, और यहां तक कि एजेंट के लिए उपयोग किए जाने वाले `model`।

यह तब उपयोगी होता है जब उपयोगकर्ता के कार्य को पूरा करने के लिए विशिष्ट मॉडल या टूल्स की आवश्यकता होती है।

**टूल्स**

टूल्स एजेंट परिभाषित करते समय भी परिभाषित किए जा सकते हैं:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# जब सीधे एक ChatAgent बनाया जा रहा हो

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

और एजेंट चलाते समय भी:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # इस रन के लिए केवल प्रदान किया गया टूल )
```

**एजेंट थ्रेड्स**

एजेंट थ्रेड्स का उपयोग बहु-चरणीय वार्तालापों को संभालने के लिए किया जाता है। थ्रेड्स को या तो इस प्रकार बनाया जा सकता है:

- `get_new_thread()` का उपयोग करके जो समय के साथ थ्रेड को सहेजने में सक्षम बनाता है
- एजेंट चलाते समय स्वचालित रूप से थ्रेड बनाकर और केवल वर्तमान रन के दौरान थ्रेड को सक्रिय रखकर।

थ्रेड बनाने के लिए कोड इस प्रकार दिखता है:

```python
# एक नया थ्रेड बनाएं।
thread = agent.get_new_thread() # थ्रेड के साथ एजेंट चलाएं।
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

आप बाद में उपयोग के लिए थ्रेड को सीरियलाइज़ कर सकते हैं:

```python
# एक नया धागा बनाएँ।
thread = agent.get_new_thread() 

# धागे के साथ एजेंट चलाएँ।

response = await agent.run("Hello, how are you?", thread=thread) 

# संग्रहण के लिए धागे को सीरियलाइज़ करें।

serialized_thread = await thread.serialize() 

# संग्रहण से लोड करने के बाद धागा स्थिति को डीसीरियलाइज़ करें।

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**एजेंट मिडलवेयर**

एजेंट टूल्स और LLMs के साथ बातचीत करता है उपयोगकर्ता के कार्य पूरी करने के लिए। कुछ स्थितियों में, हम इन अंत:क्रियाओं के बीच निष्पादित या ट्रैक करना चाहते हैं। एजेंट मिडलवेयर हमें यह करने में सक्षम बनाता है:

*फंक्शन मिडलवेयर*

यह मिडलवेयर हमें एजेंट और एक फंक्शन/टूल के बीच जो वह कॉल करेगा, के बीच एक क्रिया निष्पादित करने देता है। इसका उदाहरण तब होता है जब आप फंक्शन कॉल पर कुछ लॉगिंग करना चाहते हैं।

नीचे कोड में `next` परिभाषित करता है कि अगला मिडलवेयर या वास्तविक फंक्शन कॉल किया जाना चाहिए।

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # पूर्व-प्रसंस्करण: फ़ंक्शन निष्पादन से पहले लॉग करें
    print(f"[Function] Calling {context.function.name}")

    # अगले मिडलवेयर या फ़ंक्शन निष्पादन पर जारी रखें
    await next(context)

    # पश्च-प्रसंस्करण: फ़ंक्शन निष्पादन के बाद लॉग करें
    print(f"[Function] {context.function.name} completed")
```

*चैट मिडलवेयर*

यह मिडलवेयर एजेंट और LLM के बीच अनुरोधों के बीच एक क्रिया निष्पादित करने या लॉग करने देता है।

इसमें महत्वपूर्ण जानकारी होती है जैसे कि AI सेवा को भेजे जाने वाले `messages`।

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

    # पोस्ट-संसाधन: AI प्रतिक्रिया के बाद लॉग करें
    print("[Chat] AI response received")

```

**एजेंट मेमोरी**

जैसा कि `Agentic Memory` पाठ में बताया गया है, मेमोरी एजेंट को विभिन्न संदर्भों में काम करने में सक्षम बनाने का एक महत्वपूर्ण घटक है। MAF में कई प्रकार की मेमोरी हैं:

*इन-मेमोरी स्टोरेज*

यह मेमोरी एप्लिकेशन रनटाइम के दौरान थ्रेड्स में संग्रहीत होती है।

```python
# एक नया थ्रेड बनाएं।
thread = agent.get_new_thread() # थ्रेड के साथ एजेंट को चलाएं।
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*स्थायी संदेश*

यह मेमोरी विभिन्न सत्रों के बीच बातचीत के इतिहास को संग्रहीत करने के लिए उपयोग की जाती है। इसे `chat_message_store_factory` द्वारा परिभाषित किया गया है:

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

यह मेमोरी एजेंट चलाने से पहले संदर्भ में जोड़ी जाती है। ये मेमोरी mem0 जैसी बाहरी सेवाओं में संग्रहीत की जा सकती हैं:

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

**एजेंट ऑब्ज़रवबिलिटी**


अवलोकन विश्वसनीय और मेंटेन करने योग्य एजेंटिक सिस्टम बनाने के लिए महत्वपूर्ण है। MAF बेहतर अवलोकन के लिए ट्रेसिंग और मीटर प्रदान करने के लिए OpenTelemetry के साथ एकीकृत होता है।

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

### वर्कफ़्लो

MAF ऐसे वर्कफ़्लो प्रदान करता है जो एक कार्य पूरा करने के लिए पहले से परिभाषित चरण होते हैं और इन चरणों में AI एजेंट घटक के रूप में शामिल होते हैं।

वर्कफ़्लो विभिन्न घटकों से बने होते हैं जो बेहतर नियंत्रण प्रवाह की अनुमति देते हैं। वर्कफ़्लो **मल्टी-एजेंट ऑर्केस्ट्रेशन** और **चेकपॉइंटिंग** को भी सक्षम करते हैं ताकि वर्कफ़्लो स्थितियों को सहेजा जा सके।

एक वर्कफ़्लो के मुख्य घटक हैं:

**कार्य निष्पादक (Executors)**

कार्य निष्पादक इनपुट संदेश प्राप्त करते हैं, अपनी असाइन की गई कार्यों को पूरा करते हैं, और फिर एक आउटपुट संदेश उत्पन्न करते हैं। यह वर्कफ़्लो को बड़े कार्य की पूर्ति की ओर आगे बढ़ाता है। कार्य निष्पादक AI एजेंट या कस्टम लॉजिक हो सकते हैं।

**एजेस (Edges)**

एजेस का उपयोग वर्कफ़्लो में संदेश के प्रवाह को परिभाषित करने के लिए किया जाता है। ये हो सकते हैं:

*डाइरेक्ट एजेस* - कार्य निष्पादकों के बीच सरल एक-से-एक कनेक्शन:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*कंडीशनल एजेस* - जब कोई विशेष शर्त पूरी होती है तो सक्रिय होते हैं। उदाहरण के लिए, जब होटल के कमरे उपलब्ध नहीं होते, तो कार्य निष्पादक अन्य विकल्प सुझाव दे सकता है।

*स्विच-केस एजेस* - परिभाषित शर्तों के आधार पर संदेशों को विभिन्न कार्य निष्पादकों तक मार्गित करते हैं। उदाहरण के लिए, यदि यात्रा ग्राहक के पास प्राथमिकता पहुंच है और उनकी कार्यवाहक प्रक्रिया दूसरे वर्कफ़्लो के माध्यम से होगी।

*फैन-आउट एजेस* - एक संदेश को कई लक्ष्यों पर भेजना।

*फैन-इन एजेस* - विभिन्न कार्य निष्पादकों से कई संदेश एकत्र करना और एक लक्ष्य को भेजना।

**इवेंट्स (Events)**

वर्कफ़्लो में बेहतर अवलोकन प्रदान करने के लिए, MAF निष्पादन के लिए बिल्ट-इन इवेंट्स प्रदान करता है जिनमें शामिल हैं:

- `WorkflowStartedEvent` - वर्कफ़्लो निष्पादन शुरू होता है
- `WorkflowOutputEvent` - वर्कफ़्लो आउटपुट उत्पन्न करता है
- `WorkflowErrorEvent` - वर्कफ़्लो में त्रुटि होती है
- `ExecutorInvokeEvent` - कार्य निष्पादक प्रोसेसिंग शुरू करता है
- `ExecutorCompleteEvent` - कार्य निष्पादक प्रोसेसिंग समाप्त करता है
- `RequestInfoEvent` - अनुरोध जारी किया जाता है

## उन्नत MAF पैटर्न

ऊपर के अनुभाग Microsoft Agent Framework के मुख्य अवधारणाओं को कवर करते हैं। जैसे-जैसे आप अधिक जटिल एजेंट बनाते हैं, यहाँ कुछ उन्नत पैटर्न विचार करने के लिए हैं:

- **मिडलवेयर संयोजन**: एजेंट व्यवहार पर सूक्ष्म नियंत्रण के लिए फ़ंक्शन और चैट मिडलवेयर का उपयोग करके कई मिडलवेयर हैंडलरों (लॉगिंग, प्रमाणीकरण, दर-सीमा) की श्रृंखला बनाएं।
- **वर्कफ़्लो चेकपॉइंटिंग**: लंबे समय तक चलने वाली एजेंट प्रक्रियाओं को सहेजने और पुनः शुरू करने के लिए वर्कफ़्लो इवेंट और श्रृंखला उपयोग करें।
- **डायनामिक टूल चयन**: प्रति क्वेरी केवल प्रासंगिक टूल प्रस्तुत करने के लिए टूल विवरणों पर RAG को MAF के टूल पंजीकरण के साथ संयोजित करें।
- **मल्टी-एजेंट हैंडऑफ**: विशिष्ट एजेंटों के बीच हैंडऑफ को व्यवस्थित करने के लिए वर्कफ़्लो एजेस और कंडीशनल रूटिंग का उपयोग करें।

## Microsoft Foundry पर LangChain / LangGraph एजेंट होस्टिंग

Microsoft Agent Framework **फ्रेमवर्क-संगत** है — आप केवल MAF के साथ लिखे गए एजेंटों तक सीमित नहीं हैं। यदि आपके पास पहले से ही **LangChain** या **LangGraph** के साथ एक एजेंट है, तो आप इसे **Microsoft Foundry होस्टेड एजेंट** के रूप में चला सकते हैं ताकि Foundry रनटाइम, सत्र, स्केलिंग, पहचान, और प्रोटोकॉल एंडपॉइंट को प्रबंधित करे, जबकि आपका एजेंट लॉजिक LangGraph में रहता है।

यह `langchain_azure_ai.agents.hosting` पैकेज के साथ किया जाता है, जो उन्हीं प्रोटोकॉल के ऊपर एक संकलित LangGraph ग्राफ़ को उजागर करता है जिन्हें Foundry होस्टेड एजेंट उपयोग करते हैं।

**1. होस्टिंग एक्स्ट्रा इंस्टॉल करें:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` एक्स्ट्रा Foundry प्रोटोकॉल लाइब्रेरीज़ इंस्टॉल करता है: `azure-ai-agentserver-responses` (OpenAI-संगत `/responses` एंडपॉइंट) और `azure-ai-agentserver-invocations` (जनरल `/invocations` एंडपॉइंट)।

**2. होस्टिंग प्रोटोकॉल चुनें:**

| प्रोटोकॉल | होस्ट क्लास | एंडपॉइंट | कब उपयोग करें |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | आप OpenAI-संगत चैट, स्ट्रीमिंग, प्रतिक्रिया इतिहास, और संवाद थ्रेडिंग चाहते हैं — संवादात्मक एजेंटों के लिए अनुशंसित डिफ़ॉल्ट। |
| **Invocations** | `InvocationsHostServer` | `/invocations` | आपको एक कस्टम JSON प्रकार, वेबहुक-शैली एंडपॉइंट, या गैर-संवादात्मक प्रोसेसिंग चाहिए। |

चूंकि **Responses API Foundry में एजेंट-शैली विकास के लिए प्राथमिक API है**, इसलिए अधिकांश एजेंटों के लिए `ResponsesHostServer` से शुरू करें।

**3. पर्यावरण चर कॉन्फ़िगर करें** (`az login` पहले करें ताकि `DefaultAzureCredential` प्रमाणीकृत कर सके):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

जब एजेंट बाद में Foundry में होस्टेड एजेंट के रूप में चलता है, तो प्लेटफ़ॉर्म स्वचालित रूप से `FOUNDRY_PROJECT_ENDPOINT` इंजेक्ट करता है।

**4. Responses प्रोटोकॉल के ऊपर LangGraph एजेंट एक्सपोज़ करें:**

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

    # ChatOpenAI यहाँ Foundry परियोजना के OpenAI-संगत (प्रतिक्रियाएँ) एंडपॉइंट को लक्षित करता है।
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

इसे लोकली `python main.py` के साथ चलाएं, फिर एक Responses अनुरोध को `http://localhost:8088/responses` पर भेजें।

**मुख्य व्यवहार:**

- **संवाद (Conversations)**: क्लाइंट `previous_response_id` या `conversation` आईडी पास करके संवाद जारी रखते हैं। यदि आपका ग्राफ़ LangGraph चेकपॉइंटर के साथ संकलित है, तो Foundry संवाद स्थिति को चेकपॉइंट से जोड़ती है (उत्पादन में एक टिकाऊ चेकपॉइंटर का उपयोग करें; स्थानीय परीक्षण के लिए `MemorySaver` ठीक है)।
- **मानव-इन-द-लूप**: यदि आपका ग्राफ़ LangGraph `interrupt()` का उपयोग करता है, तो `ResponsesHostServer` लंबित interrupt को Responses `function_call` / `mcp_approval_request` आइटम के रूप में प्रस्तुत करता है, और क्लाइंट मेल खाते `function_call_output` / `mcp_approval_response` के साथ जारी रहते हैं।
- **Foundry पर तैनात करें**: Azure Developer CLI का उपयोग करें — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (स्थानीय, Docker आवश्यक), फिर `azd provision` और `azd deploy`। होस्टेड-एजेंट तैनाती के लिए **Foundry Project Manager** भूमिका आवश्यक है।

इस उदाहरण का चलाने योग्य संस्करण [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) में उपलब्ध है। पूरी वॉकथ्रू (Invocations प्रोटोकॉल, कस्टम अनुरोध स्कीमास, और समस्या निवारण) के लिए देखें [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)।

## कोड नमूने

Microsoft Agent Framework के कोड नमूने इस रिपॉजिटरी में `xx-python-agent-framework` और `xx-dotnet-agent-framework` फाइलों के तहत पाए जा सकते हैं।

## Microsoft Agent Framework के बारे में और प्रश्न हैं?

अन्य शिक्षार्थियों से मिलने, कार्यालय घंटे में शामिल होने और अपने AI एजेंट सवालों के उत्तर पाने के लिए [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) से जुड़ें।
## पिछला पाठ

[AI एजेंटों के लिए मेमोरी](../13-agent-memory/README.md)

## अगला पाठ

[कंप्यूटर उपयोग एजेंट (CUA) बनाना](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->