# मायक्रोसॉफ्ट एजंट फ्रेमवर्क एक्सप्लोर करणे

![Agent Framework](../../../translated_images/mr/lesson-14-thumbnail.90df0065b9d234ee.webp)

### परिचय

या धड्यात आपण यावर चर्चा करू:

- मायक्रोसॉफ्ट एजंट फ्रेमवर्क समजून घेणे: मुख्य वैशिष्ट्ये आणि महत्त्व  
- मायक्रोसॉफ्ट एजंट फ्रेमवर्क च्या मुख्य संकल्पनांचा शोध
- प्रगत MAF नमुने: कार्यप्रवाह, मिडलवेअर, आणि स्मृती

## शिक्षण उद्दिष्टे

हा धडा पूर्ण केल्यानंतर, तुम्हाला हे कसे करायचे हे माहीत होईल:

- मायक्रोसॉफ्ट एजंट फ्रेमवर्क वापरून उत्पादनासाठी तयार AI एजंट तयार करणे
- तुमच्या एजंट वापर प्रकरणांमध्ये मायक्रोसॉफ्ट एजंट फ्रेमवर्कची मुख्य वैशिष्ट्ये लागू करणे
- कार्यप्रवाह, मिडलवेअर, आणि निरीक्षणसारख्या प्रगत नमुनांचा वापर करणे

## कोड नमुने 

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) चे कोड नमुने तुम्हाला या संग्रहात `xx-python-agent-framework` आणि `xx-dotnet-agent-framework` फाइल्समध्ये सापडतील.

## मायक्रोसॉफ्ट एजंट फ्रेमवर्क समजून घेणे

![Framework Intro](../../../translated_images/mr/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) हा मायक्रोसॉफ्टचा AI एजंट तयार करण्यासाठी एकसंध फ्रेमवर्क आहे. यामुळे उत्पादन आणि संशोधन वातावरणातील विविध एजंट वापर प्रकरणांना सामोरे जाण्यासाठी लवचीकता मिळते जसे की:

- **अनुक्रमिक एजंट ऑर्केस्ट्रेशन** ज्याठिकाणी पायरी-दर-पायरी कार्यप्रवाह आवश्यक आहेत.
- **समकालीन ऑर्केस्ट्रेशन** ज्याठिकाणी एजंट एकाच वेळी कार्य पूर्ण करतात.
- **गट चैट ऑर्केस्ट्रेशन** ज्याठिकाणी एजंट एकत्रितपणे एका कार्यावर सहकार्य करतात.
- **हँडऑफ ऑर्केस्ट्रेशन** ज्याठिकाणी एजंट एकमेकांना उपकार्ये पूर्ण झाल्यावर कार्य हस्तांतरित करतात.
- **मॅग्नेटिक ऑर्केस्ट्रेशन** ज्याठिकाणी व्यवस्थापक एजंट कार्य सूची तयार आणि सुधारतो व उप-एजंट्सचे समन्वय करतो.

उत्पादनात AI एजंट प्रदान करण्यासाठी, MAF मध्ये खालील वैशिष्ट्ये देखील आहेत:

- **निरीक्षणयोग्यता** OpenTelemetry चा वापर करून ज्यात AI एजंटच्या प्रत्येक कृतीचा, उपकरण कॉल, ऑर्केस्ट्रेशन पायऱ्या, कारणीमंत्रणा प्रवाह आणि Microsoft Foundry डॅशबोर्डद्वारे कामगिरी निरीक्षण यांचा समावेश आहे.
- **सुरक्षा** Microsoft Foundry वर स्थानिकरित्या एजंट होस्ट करून, ज्यात भूमिका-आधारित प्रवेश, खाजगी डेटा हाताळणी आणि अंगभूत सामग्री सुरक्षा नियंत्रणांचा समावेश आहे.
- **टिकाऊपणा** कारण एजंट थ्रेड्स आणि कार्यप्रवाह थांबवू, पुन्हा सुरू करू आणि चुका दुरुस्त करू शकतात ज्यामुळे लांब प्रक्रिया शक्य होते.
- **नियंत्रण** ज्यात मानवी मंजुरीची गरज असलेल्या कार्यांसाठी मानवी-इन-द-लूप कार्यप्रवाहांना समर्थन दिले जाते.

मायक्रोसॉफ्ट एजंट फ्रेमवर्क इंटरऑपरेबल असण्यावर देखील लक्ष केंद्रीत करते:

- **क्लाउड-एग्नॉस्टिक** — एजंट कंटेनर्स, ऑन-प्रिमाइसेस आणि वेगवेगळ्या क्लाउडवर चालू शकतात.
- **प्रदाता-एग्नॉस्टिक** — Azure OpenAI आणि OpenAI सारख्या तुमच्या पसंतीच्या SDK द्वारे एजंट तयार करू शकता.
- **ओपन स्टँडर्ड्सचे एकीकरण** — Agent-to-Agent(A2A) आणि Model Context Protocol (MCP) सारखे प्रोटोकॉल वापरून इतर एजंट आणि उपकरणे शोधून त्यांचा वापर करू शकतात.
- **प्लगइन्स आणि कनेक्टर्स** — Microsoft Fabric, SharePoint, Pinecone आणि Qdrant सारख्या डेटा आणि स्मृती सेवा कनेक्ट करू शकतात.

चला पाहूया की हे वैशिष्ट्ये मायक्रोसॉफ्ट एजंट फ्रेमवर्कच्या काही मुख्य संकल्पनांवर कसे लागू होतात.

## मायक्रोसॉफ्ट एजंट फ्रेमवर्कच्या मुख्य संकल्पना

### एजंट्स

![Agent Framework](../../../translated_images/mr/agent-components.410a06daf87b4fef.webp)

**एजंट तयार करणे**

एजंट तयार करणे म्हणजे अनुमान सेवा (LLM प्रदाता), एआय एजंटसाठी अनुसरावयाच्या सूचनांचा संच आणि दिलेला `name` परिभाषित करणे.


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

वरील उदाहरणात `Azure OpenAI` वापरले आहे, पण एजंट विविध सेवा वापरून तयार करू शकता ज्यात `Microsoft Foundry Agent Service` देखील आहे:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` API

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

किंवा [MiniMax](https://platform.minimaxi.com/), जे OpenAI-सुसंगत API मोठ्या संदर्भ विंडोंसह (जोपर्यंत 204K टोकनपर्यंत) पुरवते:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

किंवा A2A प्रोटोकॉल वापरून दूरस्थ एजंट्स:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**एजंट चालवणे**

एजंट `.run` किंवा `.run_stream` मेथड्स वापरून नॉन-स्ट्रीमिंग किंवा स्ट्रीमिंग प्रतिसादांसाठी चालवले जातात.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

प्रत्येक एजंट रनसाठी पर्याय असू शकतात जसे की एजंट वापरत असलेल्या `max_tokens`, ज्याला एजंट कॉल करू शकतो असे `tools`, आणि अगदी एजंटसाठी वापरलेला `model`.

हे तेव्हा उपयुक्त असते जेव्हा वापरकर्त्याच्या कार्यासाठी विशिष्ट मॉडेल किंवा उपकरणे आवश्यक असतात.

**उपकरणे**

एजंट परिभाषित करताना उपकरणे देखील परिभाषित केली जाऊ शकतात:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ChatAgent थेट तयार करताना

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

आणि एजंट चालवताना देखील:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # फक्त या रनसाठी दिलेले साधन )
```

**एजंट थ्रेड्स**

एजंट थ्रेड्स बहु-फेर संवाद हाताळण्यासाठी वापरले जातात. थ्रेड तयार करणे खालीलपैकी एक पद्धतीने होते:

- `get_new_thread()` वापरून जे थ्रेड वेळोवेळी जतन होते
- एजंट चालवताना थ्रेड आपोआप तयार व्हावा आणि तो केवळ चालू रनदरम्यान टिकावा.

थ्रेड तयार करण्यासाठी कोड असे दिसतो:

```python
# एक नवीन थ्रेड तयार करा.
thread = agent.get_new_thread() # थ्रेडसह एजंट चालवा.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

नंतर हा थ्रेड नंतर वापरण्यासाठी सिरीयलाइज करू शकता:

```python
# नवीन थ्रेड तयार करा.
thread = agent.get_new_thread() 

# थ्रेडसह एजंट चालवा.

response = await agent.run("Hello, how are you?", thread=thread) 

# साठवणुकीसाठी थ्रेड सिरीयलाइझ करा.

serialized_thread = await thread.serialize() 

# साठवणुकीतून लोड केल्यानंतर थ्रेड स्थिती डीसीरियलाइझ करा.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**एजंट मिडलवेअर**

एजंट वापरकर्त्याचे कार्य पूर्ण करण्यासाठी उपकरणे आणि LLM सोबत संवाद साधतात. काही परिस्थितीत, या संवादात काही क्रिया करण्यासाठी किंवा ट्रॅक करण्यासाठी मिडलवेअर आवश्यक आहे. एजंट मिडलवेअर आम्हाला ते करण्यास अनुमती देते:

*फंक्शन मिडलवेअर*

या मिडलवेअरमुळे एजंट आणि फंक्शन/टूलमध्ये कॉल दरम्यान क्रिया करता येते. उदाहरणार्थ, फंक्शन कॉलवर लॉगिंग करणे.

खालील कोडमध्ये `next` हे परिभाषित करते की पुढील मिडलवेअर किंवा प्रत्यक्ष फंक्शन कॉल करायचा आहे की नाही.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # पूर्व-प्रक्रिया: फंक्शन अंमलबजावणीपूर्वी नोंद करा
    print(f"[Function] Calling {context.function.name}")

    # पुढील मिडलवेअर किंवा फंक्शन अंमलबजावणीसाठी सुरू ठेवा
    await next(context)

    # पश्चात-प्रक्रिया: फंक्शन अंमलबजावणीनंतर नोंद करा
    print(f"[Function] {context.function.name} completed")
```

*चॅट मिडलवेअर*

या मिडलवेअरमुळे एजंट आणि LLM दरम्यान विनंत्यांमध्ये क्रिया किंवा लॉगिंग करता येते.

यात `messages` सारखी महत्त्वाची माहिती असते जी AI सेवेवर पाठवली जात असते.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # पूर्व-प्रक्रिया: AI कॉलपूर्व लॉग
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # पुढील मिडलवेअर किंवा AI सेवेकडे चालू ठेवा
    await next(context)

    # पोस्ट-प्रक्रिया: AI प्रतिसादानंतर लॉग
    print("[Chat] AI response received")

```

**एजंट स्मृती**

`Agentic Memory` धड्यात नमूद केल्याप्रमाणे, स्मृती ही एजंटला वेगवेगळ्या संदर्भांवर काम करण्यास सक्षम बनवण्याचा एक महत्त्वाचा घटक आहे. MAF मध्ये अनेक प्रकारच्या स्मृती आहेत:

*इन-मेमरी स्टोरेज*

ही स्मृती थ्रेडमध्ये ऍप्लिकेशन रनटाइम दरम्यान संग्रहित होते.

```python
# नवीन थ्रेड तयार करा.
thread = agent.get_new_thread() # थ्रेडसह एजंट चालवा.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*स्थायी संदेश*

वेगवेगळ्या सत्रांमध्ये संवाद इतिहास संग्रहित करायला ही स्मृती वापरली जाते. ती `chat_message_store_factory` च्या साहाय्याने परिभाषित केली जाते:

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

*डायनॅमिक स्मृती*

एजंट चालवण्यापूर्वी हा स्मृती संदर्भात जोडली जाते. या स्मृती बाह्य सेवांमध्ये संग्रहित करता येतात जसे mem0:

```python
from agent_framework.mem0 import Mem0Provider

# प्रगत मेमरी क्षमतांसाठी Mem0 वापरून
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

**एजंट निरीक्षणयोग्यता**

निरीक्षणयोग्यता विश्वसनीय आणि देखभालयोग्य एजंट प्रणाली तयार करण्यासाठी महत्त्वाची आहे. MAF OpenTelemetry शी एकत्रित होते जेणेकरून चांगल्या निरीक्षणासाठी ट्रेसिंग आणि मीटर प्रदान केले जाऊ शकतील.

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

### कार्यप्रवाह

MAF कार्यप्रवाह प्रदान करते जे पूर्वनिर्धारित पायऱ्या आहेत जे कार्य पूर्ण करतात आणि त्यात AI एजंट घटक म्हणून असतात.

कार्यप्रवाह विविध घटकांनी बनलेले असतात जे चांगले नियंत्रण प्रवाह देते. कार्यप्रवाह **बहु-एजंट ऑर्केस्ट्रेशन** आणि **चेकपॉइंटिंग** वापर करून कार्यप्रवाह स्थिती जतन करणे याला सक्षम करतात.

कार्यप्रवाहाचे मुख्य घटक आहेत:

**कार्यकारी (Executors)**

कार्यकारी इनपुट संदेश प्राप्त करतात, त्यांचे कार्य पार पाडतात आणि नंतर आउटपुट संदेश तयार करतात. हे कार्यप्रवाहाला मोठे कार्य पूर्ण करण्याकडे अग्रसर करते. कार्यकारी AI एजंट किंवा सानुकूल लॉजिक असू शकते.

**कडे (Edges)**

कडे कार्यप्रवाहामध्ये संदेशांचा प्रवाह ठरवण्यासाठी वापरले जातात. हे असू शकतात:

*थेट कडे* - कार्याकारांमध्ये सोप्पे एक-एक कनेक्शन:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*अटींवर आधारित कडे* - विशिष्ट अट पूर्ण झाल्यावर सक्रिय होतात. उदाहरणार्थ, हॉटेलच्या खोल्या उपलब्ध नसल्यास कार्यकारी इतर पर्याय सुचवू शकतो.

*स्विच-केस कडे* - दिलेल्या अटींवर आधारित वेगळ्या कार्याकारांकडे संदेश पाठवतात. उदाहरणार्थ, प्रवास ग्राहकाला प्राधान्य प्रवेश असल्यास त्यांचे कार्य वेगळ्या कार्यप्रवाहातून हाताळले जाईल.

*फॅन-आऊट कडे* - एक संदेश अनेक लक्ष्यांकडे पाठवतात.

*फॅन-इन कडे* - अनेक कार्याकारांकडून संदेश गोळा करुन एका लक्ष्याकडे पाठवतात.

**ईव्हेंट्स**

कार्यप्रवाहांमध्ये चांगले निरीक्षण देण्यासाठी, MAF मध्ये कार्यान्वयनासाठी अंगभूत ईव्हेंट्स आहेत ज्यात समाविष्ट आहे:

- `WorkflowStartedEvent`  - कार्यप्रवाह प्रारंभ होतो
- `WorkflowOutputEvent` - कार्यप्रवाह आउटपुट तयार करतो
- `WorkflowErrorEvent` - कार्यप्रवाहामध्ये त्रुटी येते
- `ExecutorInvokeEvent`  - कार्यकारी प्रक्रिया सुरू करतो
- `ExecutorCompleteEvent`  - कार्यकारी प्रक्रिया पूर्ण करतो
- `RequestInfoEvent` - विनंती केली जाते

## प्रगत MAF नमुने

वर दिलेल्या विभागांमध्ये मायक्रोसॉफ्ट एजंट फ्रेमवर्कच्या मुख्य संकल्पना सांगितल्या आहेत. जसे आपण अधिक जटील एजंट तयार करता, येथे काही प्रगत नमुने विचारात घ्या:

- **मिडलवेअर संयोजन**: लॉगिंग, प्रमाणीकरण, दर मर्यादा असे अनेक मिडलवेअर हँडलर्स साखळीबद्ध करा ज्यामुळे एजंट वर्तनावर सूक्ष्म नियंत्रण मिळते.
- **कार्यप्रवाह चेकपॉइंटिंग**: कार्यप्रवाह ईव्हेंट्स आणि सिरीयलायझेशन वापरून दीर्घकालीन एजंट प्रक्रियेचे जतन आणि पुनरारंभ करा.
- **डायनॅमिक टूल निवड**: MAF च्या टूल नोंदणीसह टूल वर्णनांवर RAG चे संयोजन करा ज्यामुळे फक्त संबंधित टूल्स क्वेरीजसाठी सादर होतात.
- **बहु-एजंट हँडऑफ**: कार्यप्रवाह कडे आणि अटींवर आधारित रूटिंग वापरून विशेषीकृत एजंट्समधील हँडऑफसचे समन्वय करा.

## मायक्रोसॉफ्ट फाऊंड्रीवर LangChain / LangGraph एजंट होस्टिंग

मायक्रोसॉफ्ट एजंट फ्रेमवर्क **फ्रेमवर्क-इंटरऑपरेबल** आहे — तुम्ही MAF वापरून तयार केलेल्या एजंट्समध्ये मर्यादित नाही. जर तुमच्याकडे आधीच **LangChain** किंवा **LangGraph** वापरून एजंट तयार असेल, तर तुम्ही तो **मायक्रोसॉफ्ट फाऊंड्री होस्टेड एजंट** म्हणून चालवू शकता ज्यामुळे फाऊंड्री रनटाइम, सत्र, स्केलिंग, ओळख, आणि प्रोटोकॉल एंडपॉइंट्स व्यवस्थापित करते, आणि तुमच्या एजंट लॉजिक LangGraph मध्ये राहते.

हे करण्यात `langchain_azure_ai.agents.hosting` पॅकेज मदत करते, जे त्या प्रोटोकॉलवर एक संकलित LangGraph ग्राफ प्रकट करते ज्याचा उपयोग फाऊंड्री होस्टेड एजंट करतात.

**1. होस्टिंग एक्स्ट्रा इंस्टॉल करा:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` एक्स्ट्रा Foundry प्रोटोकॉल लायब्ररी इंस्टॉल करते: `azure-ai-agentserver-responses` (OpenAI-सुसंगत `/responses` एंडपॉइंट) आणि `azure-ai-agentserver-invocations` (सामान्य `/invocations` एंडपॉइंट).

**2. होस्टिंग प्रोटोकॉल निवडा:**

| प्रोटोकॉल | होस्ट क्लास | एंडपॉइंट | वापरण्याची वेळ |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | तुम्हाला OpenAI-सुसंगत चॅट, स्ट्रीमिंग, प्रतिसाद इतिहास, आणि संभाषण थ्रेडिंग हवे आहे — संभाषण एजंटसाठी शिफारस केलेली डीफॉल्ट. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | तुम्हाला कस्टम JSON फॉरमॅट, वेबहुक-शैली एंडपॉइंट, किंवा गैर-संभाषण प्रक्रिया हवी आहे. |

कारण **Responses API हा Foundry मध्ये एजंट-शैली विकासासाठी प्राथमिक API आहे**, बर्‍याच एजंटसाठी `ResponsesHostServer` पासून सुरू करा.

**3. पर्यावरण चल सेट करा** (`az login` आधी करा जेणेकरून `DefaultAzureCredential` प्रमाणीकृत करू शकेल):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

नंतर एजंट Foundry मध्ये होस्टेड एजंट म्हणून चालनार असताना, प्लॅटफॉर्म `FOUNDRY_PROJECT_ENDPOINT` आपोआप इंजेक्ट करतो.

**4. Responses प्रोटोकॉलवर LangGraph एजंट प्रकट करा:**

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

    # ChatOpenAI येथे Foundry प्रकल्पाच्या OpenAI-सुसंगत (प्रतिक्रिया) एंडपॉइंटवर लक्ष केंद्रित करते.
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

स्थानिकपणे `python main.py` सह चालवा, नंतर `http://localhost:8088/responses` वर Responses विनंती पाठवा.

**मुख्य वर्तन:**

- **संभाषणे**: ग्राहक `previous_response_id` किंवा `conversation` ID पाठवून संभाषण चालू ठेवतात. जर तुमचा ग्राफ LangGraph चेकपॉइंटर सह संकलित असेल, तर Foundry संभाषण स्थिती चेकपॉइंटशी जोडते (उत्पादनात टिकाऊ चेकपॉइंटर वापरा; स्थानिक चाचणीसाठी `MemorySaver` ठीक आहे).
- **मानवी-इन-द-लूप**: जर तुमचा ग्राफ LangGraph `interrupt()` वापरत असेल, तर `ResponsesHostServer` संभाव्य इंटरप्ट Responses `function_call` / `mcp_approval_request` आयटम म्हणून दर्शवितो, आणि ग्राहक तीच `function_call_output` / `mcp_approval_response` सह पुन्हा सुरू करतात.
- **Foundry मध्ये होस्ट करा**: Azure Developer CLI वापरा — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (स्थानिक, Docker आवश्यक आहे), नंतर `azd provision` आणि `azd deploy`. होस्टेड एजंट डिप्लॉयमेंटसाठी **Foundry प्रोजेक्ट मॅनेजर** भूमिका आवश्यक आहे.

या उदाहरणाचा चालवण्याजोगा आवृत्ती [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) मध्ये उपलब्ध आहे. पूर्ण मार्गदर्शनासाठी (Invocations प्रोटोकॉल, कस्टम विनंती स्कीमा, आणि त्रुटी निवारण), पाहा [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## कोड नमुने 

मायक्रोसॉफ्ट एजंट फ्रेमवर्कसाठी कोड नमुने तुम्हाला या संग्रहात `xx-python-agent-framework` आणि `xx-dotnet-agent-framework` फाइल्समध्ये सापडतील.

## मायक्रोसॉफ्ट एजंट फ्रेमवर्क विषयी अजून प्रश्न आहेत का?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) मध्ये सामील व्हा, अन्य शिकणाऱ्यांशी भेटा, ऑफिस तासांना उपस्थित राहा आणि तुमचे AI एजंट संबंधी प्रश्न विचारा.
## मागील धडा

[AI एजंटसाठी स्मृती](../13-agent-memory/README.md)

## पुढील धडा

[कंप्युटर वापर एजंट तयार करणे (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->