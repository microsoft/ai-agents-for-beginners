# Microsoft Agent Framework अन्वेषण

![Agent Framework](../../../translated_images/mr/lesson-14-thumbnail.90df0065b9d234ee.webp)

### परिचय

या धड्यात समाविष्ट आहे:

- Microsoft Agent Framework समजून घेणे: मुख्य वैशिष्ट्ये आणि मूल्य  
- Microsoft Agent Framework च्या मुख्य संकल्पनांचा शोध घेणे
- प्रगत MAF पॅटर्न: वर्कफ्लोज, मिडलवेअर, आणि मेमरी

## शिक्षण उद्दिष्टे

या धडा पूर्ण केल्यानंतर, तुम्हाला हे माहित असेल की:

- Microsoft Agent Framework वापरून उत्पादनासाठी तयार AI एजंट तयार करणे
- Microsoft Agent Framework चे मुख्य वैशिष्ट्ये एजंटिक वापराच्या केसवर लागू करणे
- वर्कफ्लोज, मिडलवेअर, आणि निरीक्षणसह प्रगत पॅटर्नचा वापर करणे

## कोड नमुने

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) साठी कोड नमुने या रिपॉझिटरीमध्ये `xx-python-agent-framework` आणि `xx-dotnet-agent-framework` फायलींमध्ये सापडतील.

## Microsoft Agent Framework समजून घेणे

![Framework Intro](../../../translated_images/mr/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) हा Microsoft चा एकत्रित फ्रेमवर्क आहे AI एजंट तयार करण्यासाठी. तो उत्पादन आणि संशोधन वातावरणातील एजंटिक वापरांच्या विविध प्रकाराना समर्थन देतो, ज्यामध्ये समाविष्ट आहेत:

- **क्रमशः एजंट ऑर्केस्ट्रेशन** ज्यामध्ये स्टेप-बाय-स्टेप वर्कफ्लो आवश्यक आहेत.
- **सामायिक ऑर्केस्ट्रेशन** ज्यामध्ये एजंटस एकाच वेळी कार्य पूर्ण करतात.
- **ग्रुप चॅट ऑर्केस्ट्रेशन** ज्यामध्ये एजंट एकत्र काम करू शकतात एका कार्यावर.
- **हँडऑफ ऑर्केस्ट्रेशन** ज्यामध्ये एजंट एकमेकांना कार्याचे उप-कार्य पूर्ण झाल्यावर सुपूर्द करतात.
- **मॅग्नेटिक ऑर्केस्ट्रेशन** ज्यामध्ये मॅनेजर एजंट कार्य सूची तयार करतो आणि बदलतो, तसेच उप-एजंट्सचे समन्वय करून कार्य पूर्ण करतो.

उत्पादनात AI एजंट वितरित करण्यासाठी, MAF मध्ये खालील वैशिष्ट्ये देखील आहेत:

- **निरीक्षणक्षमता** OpenTelemetry चा उपयोग करून जिथे AI एजंटची प्रत्येक क्रिया जसे टूल कॉल, ऑर्केस्ट्रेशन पावले, विचार प्रवाह, आणि Microsoft Foundry डॅशबोर्ड द्वारे कार्यप्रदर्शन निरीक्षण केले जाते.
- **सुरक्षा** Microsoft Foundry वर एजंट्सची स्थानिक होस्टिंग जी भूमिकाधारित प्रवेश, खाजगी डेटा हाताळणी आणि अंतर्भूत सामग्री सुरक्षा नियंत्रणे समाविष्ट करते.
- **टिकाऊपणा** कारण एजंट थ्रेड आणि वर्कफ्लोज थांबू, पुन्हा सुरु करू, आणि त्रुटींपासून पुनर्प्राप्त करू शकतात ज्यामुळे लांब प्रक्रिया चालू ठेवता येतात.
- **नियंत्रण** मानव सहभाग असलेले वर्कफ्लोज ज्यात कार्यांना मानवी मंजुरी आवश्यक असल्याचे चिन्हांकित केले जाते.

Microsoft Agent Framework सहसंबद्ध करण्यावर देखील लक्ष केंद्रित करते:

- **क्लाऊड-निरपेक्ष** - एजंट कंटेनर, ऑन-प्रिमाइसेस आणि विविध क्लाऊड्समध्ये चालू शकतात.
- **प्रदाता-निरपेक्ष** - एजंट्स तुम्ही पसंत केलेल्या SDK द्वारे तयार करू शकता ज्यात Azure OpenAI आणि OpenAI समाविष्ट आहेत.
- **खुल्या मानकांची समाकलन** - एजंट्स Agent-to-Agent (A2A) आणि Model Context Protocol (MCP) सारख्या प्रोटोकॉल वापरून इतर एजंट्स आणि टूल्स शोधू आणि वापरू शकतात.
- **प्लगइन्स आणि कनेक्टर्स** - Microsoft Fabric, SharePoint, Pinecone आणि Qdrant सारख्या डेटा आणि मेमरी सेवांशी कनेक्शन करता येते.

चला पाहूया Microsoft Agent Framework च्या काही मुख्य संकल्पनांवर ही वैशिष्ट्ये कशी लागू आहेत.

## Microsoft Agent Framework चे मुख्य संकल्पना

### एजंट्स

![Agent Framework](../../../translated_images/mr/agent-components.410a06daf87b4fef.webp)

**एजंट तयार करणे**

एजंट तयार करण्यासाठी इनफरन्स सेवा (LLM प्रदाता), AI एजंटचे पालन करण्यासाठी सूचनांचा संच, आणि दिलेला `name` निर्धारित केला जातो:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

वरील `Azure OpenAI` वापरून केले आहे पण एजंट विविध सेवांसह तयार केले जाऊ शकतात ज्यात `Microsoft Foundry Agent Service` सुद्धा समाविष्ट आहे:

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

किंवा [MiniMax](https://platform.minimaxi.com/), जे OpenAI-योग्य API प्रदान करते ज्यात मोठे संदर्भ विंडो (ते 204K टोकनपर्यंत) आहेत:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

किंवा A2A प्रोटोकॉल वापरून दूरच्या एजंट्स:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**एजंट चालवणे**

एजंट्स `.run` किंवा `.run_stream` पद्धती वापरून चालवले जातात, जे नॉन-स्ट्रिमिंग आणि स्ट्रिमिंग प्रतिसादांसाठी वापरले जातात.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

प्रत्येक एजंटचा रनमध्ये `max_tokens`, एजंट कॉल करू शकणारे `tools` आणि वापरले जाणारे `model` यांसारख्या पर्यायांसह सानुकूलना करता येते.

हे उपयोगी आहे जेव्हा विशिष्ट मॉडेल किंवा साधने वापरून वापरकर्त्याचे कार्य पूर्ण करणे आवश्यक असते.

**साधने**

साधने एजंट तयार करताना परिभाषित केली जाऊ शकतात:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ChatAgent थेट तयार करताना

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

आणि एजंट चालवताना:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # केवळ या चालवण्यासाठी उपलब्ध असलेले साधन )
```

**एजंट थ्रेड्स**

एजंट थ्रेड्स बहु-चर्चा संभाषण हाताळण्यासाठी वापरले जातात. थ्रेड्स तयार होतात:

- `get_new_thread()` वापरून जे थ्रेडला वेळेवर जतन करण्यास सक्षम करते
- एजंट चालवताना आपोआप थ्रेड तयार होते आणि तो केवळ चालू रन दरम्यान टिकतो.

थ्रेड तयार करण्याचा कोड असा दिसतो:

```python
# एक नवीन थ्रेड तयार करा.
thread = agent.get_new_thread() # थ्रेडसह एजंट चालवा.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

नंतर तुम्ही थ्रेडला संचयित करण्यासाठी सिरीयलाइज करू शकता:

```python
# नवीन थ्रेड तयार करा.
thread = agent.get_new_thread() 

# थ्रेडसह एजंट चालवा.

response = await agent.run("Hello, how are you?", thread=thread) 

# संचयनासाठी थ्रेड सिरियलाइज़ करा.

serialized_thread = await thread.serialize() 

# संचयनातून लोड केल्यानंतर थ्रेड स्थिती डीसीरियलाइझ करा.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**एजंट मिडलवेअर**

एजंट वापरकर्त्याचे कार्य पूर्ण करण्यासाठी साधने आणि LLMs शी संवाद साधतात. काही परिस्थितीत, आम्हाला या संवादामध्ये कोणती क्रिया करायची किंवा ट्रॅक करायची असते. एजंट मिडलवेअर याची परवानगी देते:

*फंक्शन मिडलवेअर*

या मिडलवेअरमुळे एजंट आणि फंक्शन/साधनामध्ये एक क्रिया चालवता येते, जसे की फंक्शन कॉलवर लॉगिंग करणे.

खालील कोडमध्ये `next` म्हणजे पुढील मिडलवेअर किंवा प्रत्यक्ष फंक्शन कॉल केले जाणार का हे सूचित करते.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # पूर्व-प्रक्रिया: फंक्शन कार्यान्वयनापूर्वी लॉग करा
    print(f"[Function] Calling {context.function.name}")

    # पुढील मिडलवेअर किंवा फंक्शन कार्यान्वयनाकडे पुढे जा
    await next(context)

    # पोस्ट-प्रक्रिया: फंक्शन कार्यान्वयनानंतर लॉग करा
    print(f"[Function] {context.function.name} completed")
```

*चॅट मिडलवेअर*

या मिडलवेअरमुळे एजंट आणि LLM मधील विनंत्या दरम्यान क्रिया चालवणे किंवा लॉग करणे शक्य होते.

यात AI सेवेला पाठवले जाणारे `messages` सारखी महत्त्वाची माहिती असते.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # पूर्व-प्रक्रिया: AI कॉलपूर्वी लॉग
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # पुढील मिडलवेअर किंवा AI सेवेकडे पुढे जा
    await next(context)

    # पश्च-प्रक्रिया: AI प्रतिसादानंतर लॉग
    print("[Chat] AI response received")

```

**एजंट मेमरी**

`Agentic Memory` धड्यात सांगितल्याप्रमाणे, मेमरी एजंटला वेगवेगळ्या संदर्भावर काम करण्यासाठी महत्त्वाची आहे. MAF मध्ये विविध प्रकारच्या मेमरी आहेत:

*इन-मेमरी स्टोरेज*

हि मेमरी थ्रेड्समध्ये अॅप्लिकेशनच्या रनटाइमच्या दरम्यान साठवलेली असते.

```python
# एक नवीन थ्रेड तयार करा.
thread = agent.get_new_thread() # थ्रेडसह एजंट चालवा.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*पर्सिस्टंट मेसेजेस*

वेगवेगळ्या सेशन्समध्ये संभाषण इतिहास साठवण्यासाठी ही मेमरी वापरली जाते. हे `chat_message_store_factory` वापरून परिभाषित केले जाते:

```python
from agent_framework import ChatMessageStore

# एक सानुकूल संदेश संच तयार करा
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*डायनॅमिक मेमरी*

एजंट्स चालण्यापूर्वी संदर्भामध्ये ही मेमरी जोडली जाते. ह्या मेमरी बाह्य सेवांमध्ये जसे mem0 मध्ये साठवता येऊ शकतात:

```python
from agent_framework.mem0 import Mem0Provider

# प्रगत मेमरी क्षमता साठी Mem0 चा वापर करत आहे
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

**एजंट निरीक्षणक्षमता**

विश्वसनीय आणि देखभालयोग्य एजंटिक सिस्टम तयार करण्यासाठी निरीक्षण महत्वाचे आहे. MAF OpenTelemetry सोबत एकत्रित होतो ज्यामुळे ट्रेसिंग आणि मीटर्सद्वारे चांगले निरीक्षण करता येते.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # काहीतरी करा
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### वर्कफ्लोज

MAF वर्कफ्लोज ऑफर करतो ज्या पूर्व-व्यवस्थित पावल्या आहेत एक कार्य पूर्ण करण्यासाठी आणि ज्यामध्ये AI एजंट्स त्या पावलांमध्ये घटक म्हणून असतात.

वर्कफ्लोज विविध घटकांनी बनलेले असतात जे उत्तम नियंत्रण प्रवाह सक्षम करतात. वर्कफ्लोज मल्टी-एजंट ऑर्केस्ट्रेशन आणि चेकपॉईंटिंग सक्षम करतात वर्कफ्लो स्थिती जतन करण्यासाठी.

वर्कफ्लोचे मुख्य घटक आहेत:

**एक्झिक्यूटर**

एक्झिक्यूटर इनपुट संदेश प्राप्त करतात, त्यांचे कार्य पार पाडतात, आणि नंतर आउटपुट संदेश तयार करतात. यामुळे वर्कफ्लो मोठ्या कार्याकडे पुढे जाते. एक्झिक्यूटर AI एजंट अथवा सानुकूल लॉजिक असू शकतो.

**एज**

एज वर्कफ्लोतील संदेशांचा प्रवाह परिभाषित करण्यासाठी वापरले जातात. हे असे असू शकतात:

*थेट एज* - एक्झिक्यूटर दरम्यान सोपे एक-टू-एक कनेक्शन:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*शर्तीवर आधारित एज* - विशिष्ट अट पूर्ण झाल्यावर सक्रिय होणारे. उदाहरणार्थ, जेव्हा हॉटेलचे खोल्या उपलब्ध नाहीत, तेव्हा एक्झिक्यूटर इतर पर्याय सुचवू शकतो.

*स्विच-केस एज* - परिभाषित अटींवर आधारित वेगवेगळ्या एक्झिक्यूटरकडे संदेश मार्गदर्शित करतात. उदाहरणार्थ, प्रवास ग्राहकाला प्राथमिकता प्रवेश असल्यास आणि त्यांच्या कार्यांवर वेगळ्या वर्कफ्लोने हाताळले जाईल.

*फॅन-आऊट एज* - एक संदेश अनेक लक्ष्यांना पाठवतो.

*फॅन-इन एज* - वेगवेगळ्या एक्झिक्यूटरकडून अनेक संदेश एकत्र करून एका लक्ष्याकडे पाठवतो.

**इव्हेंट्स**

वर्कफ्लोची चांगली निरीक्षणक्षमता प्रदान करण्यासाठी, MAF कार्यान्वयनासाठी अंगभूत इव्हेंट्स पुरवतो ज्यामध्ये समाविष्ट आहेत:

- `WorkflowStartedEvent`  - वर्कफ्लो कार्यान्वयन सुरू होते
- `WorkflowOutputEvent` - वर्कफ्लो आउटपुट तयार करतो
- `WorkflowErrorEvent` - वर्कफ्लोमध्ये त्रुटी येते
- `ExecutorInvokeEvent`  - एक्झिक्यूटर प्रक्रिया सुरू करतो
- `ExecutorCompleteEvent`  -  एक्झिक्यूटर प्रक्रिया पूर्ण करतो
- `RequestInfoEvent` - विनंती जारी केली जाते

## प्रगत MAF पॅटर्न

वर दिलेल्या विभागात Microsoft Agent Framework च्या मुख्य संकल्पना समजावून सांगितल्या आहेत. तुम्ही अधिक गुंतागुंतीचे एजंट तयार करत असाल, तर लक्षात घ्या काही प्रगत पॅटर्न:

- **मिडलवेअर संकलन**: फंक्शन आणि चॅट मिडलवेअर वापरून अनेक मिडलवेअर हँडलर्स (लॉगिंग, प्रमाणीकरण, दर-सीमा) साखळीबद्ध करून एजंट वर्तनावर सूक्ष्म नियंत्रण मिळवा.
- **वर्कफ्लो चेकपॉईंटिंग**: वर्कफ्लो इव्हेंट्स आणि सिरीयलायझेशन वापरून दीर्घकालीन एजंट प्रक्रियांचे जतन व पुनरारंभ करा.
- **डायनॅमिक टूल निवड**: टूल वर्णनेवर RAG सह MAF च्या टूल नोंदणीचा वापर करून प्रत्येक विचारलेल्या प्रश्नासाठी फक्त संबंधित टूल्स दाखवा.
- **मल्टी-एजंट हँडऑफ**: वर्कफ्लो एजेस आणि अटींवर आधारित राऊटिंग वापरून विशेषीकृत एजंट्समधील सुपूर्दीचे नियोजन करा.

## Microsoft Foundry वर LangChain / LangGraph एजंट होस्टिंग

Microsoft Agent Framework हा **फ्रेमवर्क-इंटरऑपरेबल** आहे — तुम्ही फक्त MAF वापरून लिहिलेले एजंट्सच नाही वापरू शकता. जर तुमच्याकडे आधीपासून **LangChain** किंवा **LangGraph** वापरून एजंट तयार असेल, तर तुम्ही तुम्हाला तो **Microsoft Foundry होस्टेड एजंट** म्हणून चालवू शकता ज्यामुळे Foundry रनटाइम, सेशन्स, स्केलिंग, आयडेंटिटी, आणि प्रोटोकॉल एन्डपॉइंट्स हँडल करते, तर तुमची एजंट लॉजिक LangGraph मध्ये राहते.

हे `langchain_azure_ai.agents.hosting` पॅकेजसोबत केले जाते, जे एक संकलित LangGraph ग्राफ त्याच प्रोटोकॉलवर देते जे Foundry होस्टेड एजंट वापरतात.

**1. होस्टिंग एक्स्ट्रा इन्स्टॉल करा:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` एक्स्ट्रा Foundry प्रोटोकॉल लायब्ररी इन्स्टॉल करते: `azure-ai-agentserver-responses` (OpenAI-योग्य `/responses` एन्डपॉइंट) आणि `azure-ai-agentserver-invocations` (सामान्य `/invocations` एन्डपॉइंट).

**2. होस्टिंग प्रोटोकॉल निवडा:**

| प्रोटोकॉल | होस्ट क्लास | एन्डपॉइंट | वापरा जेव्हा |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | तुम्हाला OpenAI-योग्य चॅट, स्ट्रिमिंग, प्रतिसाद इतिहास, आणि संभाषण थ्रेडिंग हवे असेल — संभाषण एजंटसाठी शिफारस केलेले डीफॉल्ट. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | तुम्हाला सानुकूल JSON संरचना, webhook-शैली एन्डपॉइंट, किंवा गैर-संभावंशीय प्रक्रिया हवी असेल. |

कारण **Responses API हा Foundry मध्ये एजंट-शैली विकासासाठी प्राथमिक API आहे**, बहुतेक एजंटसाठी `ResponsesHostServer` पासून सुरू करा.

**3. वातावरणीय चल सानुकूल करा** (`az login` आधी करा ज्यामुळे `DefaultAzureCredential` प्रमाणित होऊ शकेल):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

जेव्हा एजंट नंतर Foundry मध्ये होस्टेड एजंट म्हणून चालेल, तेव्हा प्लॅटफॉर्म आपोआप `FOUNDRY_PROJECT_ENDPOINT` इंजेक्ट करतो.

**4. Responses प्रोटोकॉलवर LangGraph एजंट प्रदर्शित करा:**

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

    # ChatOpenAI येथे Foundry प्रकल्पाच्या OpenAI-सुसंगत (प्रतिक्रियांचे) समाप्तीबिंदूवर लक्ष्य करते.
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

लोकलली `python main.py` ने चालवा, नंतर `http://localhost:8088/responses` वर Responses विनंती पाठवा.

**मुख्य वर्तन:**

- **संभाषणे**: क्लायंट `previous_response_id` किंवा `conversation` ID देऊन संभाषण सुरू ठेवतात. जर तुमचा ग्राफ LangGraph चेकपॉईंटरसह संकलित असेल, तर Foundry संभाषण स्थिती चेकपॉईंटशी जुळवतो (उत्पादनात टिकाऊ चेकपॉईंटर वापरा; स्थानिक चाचणीसाठी `MemorySaver` चालेल).
- **मानव-मध्ये-चक्र**: जर तुमचा ग्राफ LangGraph `interrupt()` वापरत असेल, तर `ResponsesHostServer` अपेक्षित इंटरप्शनला Responses `function_call` / `mcp_approval_request` आयटम म्हणून दर्शवतो, आणि क्लायंट जुळणारे `function_call_output` / `mcp_approval_response` सह पुन्हा सुरू होतो.
- **Foundry मध्ये तैनात करा**: Azure Developer CLI वापरा — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (स्थानिक, Docker आवश्यक), नंतर `azd provision` आणि `azd deploy`. होस्टेड एजंट तैनातीसाठी **Foundry प्रोजेक्ट मॅनेजर** भूमिका आवश्यक आहे.

या उदाहरणाचा चालणारा आवृत्ती [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) येथे आहे. पूर्ण मार्गदर्शनासाठी (Invocations प्रोटोकॉल, सानुकूल विनंती स्कीमा, आणि अडचणी सोडवणे) पाहा [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## कोड नमुने 

Microsoft Agent Framework साठी कोड नमुने या रिपॉझिटरीमध्ये `xx-python-agent-framework` आणि `xx-dotnet-agent-framework` फायलींमध्ये सापडतील.

## Microsoft Agent Framework विषयी अधिक प्रश्न आहेत का?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) मध्ये सामील व्हा, इतर शिकणाऱ्यांशी भेटा, ऑफिस ऑवर्स अटेंड करा आणि तुमचे AI एजंट प्रश्नांचे निराकरण करा.
## मागील धडा

[AI एजंटसाठी मेमरी](../13-agent-memory/README.md)

## पुढील धडा

[कॉम्प्युटर वापर एजंट्स तयार करणे (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->