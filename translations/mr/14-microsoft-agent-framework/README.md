# Microsoft Agent Framework चा शोध

![एजंट फ्रेमवर्क](../../../translated_images/mr/lesson-14-thumbnail.90df0065b9d234ee.webp)

### परिचय

हा धडा खालील गोष्टी कव्हर करेल:

- Microsoft Agent Framework समजून घेणे: मुख्य वैशिष्ट्ये आणि मूल्य  
- Microsoft Agent Framework ची मुख्य संकल्पना एक्सप्लोर करणे
- प्रगत MAF पॅटर्न: वर्कफ्लोज, मिडलवेअर, आणि मेमरी

## शिकण्याचे उद्दिष्टे

हा धडा पूर्ण केल्यावर, आपण काय जाणून घेणार आहात:

- Microsoft Agent Framework वापरून प्रॉडक्शन रेडी AI एजंट कसे बनवायचे
- आपल्या Agentic उपयोग प्रकरणांसाठी Microsoft Agent Framework चे मुख्य वैशिष्ट्ये कसे लागू करायचे
- वर्कफ्लोज, मिडलवेअर आणि ऑब्झर्वेबिलिटीसह प्रगत पॅटर्न कसे वापरायचे

## कोड नमुने

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) साठीचे कोड नमुने या रिपॉझिटरीमध्ये `xx-python-agent-framework` आणि `xx-dotnet-agent-framework` फाइलांखाली आढळतील.

## Microsoft Agent Framework समजून घेणे

![फ्रेमवर्क परिचय](../../../translated_images/mr/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) हे AI एजंट तयार करण्यासाठी Microsoft चे एकसंध फ्रेमवर्क आहे. हे उत्पादन आणि संशोधन वातावरणात दिसणाऱ्या विविध agentic उपयोग प्रकरणांना सामोरे जाण्यासाठी लवचिकता देते, ज्यामध्ये समाविष्ट आहेत:

- **क्रमिक एजंट ऑर्केस्ट्रेशन** अशा परिस्थितींमध्ये जिथे पायरी-दर-पायरी वर्कफ्लो आवश्यक असतात.
- **समवर्ती ऑर्केस्ट्रेशन** अशा परिस्थितींमध्ये जिथे एजंटांना एकाच वेळी काम पूर्ण करावे लागते.
- **ग्रुप चॅट ऑर्केस्ट्रेशन** अशा परिस्थितींमध्ये जिथे एजंट एकत्र येऊन एका कामावर सहकार्य करतात.
- **हॅंडऑफ ऑर्केस्ट्रेशन** अशा परिस्थितींमध्ये जिथे एजंट उपकार्या पूर्ण झाल्याने एकमेकांना काम हस्तांतरित करतात.
- **मॅग्नेटिक ऑर्केस्ट्रेशन** अशा परिस्थितींमध्ये जिथे एक मॅनेजर एजंट कार्यांची यादी तयार करतो व बदलतो आणि उपएजंट्सच्या समन्वयाचा हातभार लावतो.

प्रॉडक्शनमध्ये AI एजंट वितरीत करण्यासाठी, MAF मध्ये खालील वैशिष्ट्ये समाविष्ट आहेत:

- **ऑब्झर्वेबिलिटी** OpenTelemetry चा वापर करून जिथे AI एजंटची प्रत्येक क्रिया — टूल कॉल, ऑर्केस्ट्रेशन पायऱ्या, निर्णय प्रवाह आणि Microsoft Foundry डॅशबोर्डमधून कामगिरीचे निरीक्षण — ट्रेस केली जाते.
- **सुरक्षा** एजंट Microsoft Foundry वर नैसर्गिकरित्या होस्ट केल्यामुळे भूमिका-आधारित परवानगी, खाजगी डेटा हाताळणी आणि अंगभूत कंटेंट सुरक्षा सारख्या सुरक्षा नियंत्रणांचा समावेश आहे.
- **दृढता (Durability)** एजंट थ्रेड्स आणि वर्कफ्लोज थांबवता, पुन्हा सुरू करता आणि त्रुटी पासून पुनर्प्राप्त करू शकतात ज्यामुळे दीर्घकालीन प्रक्रिया सक्षम होतात.
- **नियंत्रण** मानवी परवानगी आवश्यक असलेल्या कार्यांसाठी मानवी-इन-द-लूप वर्कफ्लो समर्थित आहेत.

Microsoft Agent Framework हा परस्पर-परिचालकीय (interoperable) असण्यावर देखील लक्ष केंद्रित करतो:

- **क्लाउड-निरपेक्ष (Cloud-agnostic)** - एजंट कंटेनर्समध्ये, ऑन-प्रेम किंवा विविध क्लाउडवर चालवता येतात.
- **प्रदाता-निरपेक्ष (Provider-agnostic)** - एजंट आपल्याप्रferred SDK वापरून तयार केले जाऊ शकतात जसे की Azure OpenAI आणि OpenAI
- **ओपन स्टँडर्ड्सचे एकीकरण** - Agent-to-Agent (A2A) आणि Model Context Protocol (MCP) सारखे प्रोटोकॉल इतर एजंट्स आणि टूल्स शोधण्यासाठी आणि वापरण्यासाठी वापरता येतात.
- **प्लगइन आणि कनेक्टर्स** - Microsoft Fabric, SharePoint, Pinecone आणि Qdrant सारख्या डेटा आणि मेमरी सेवांशी कनेक्शन केले जाऊ शकतात.

या वैशिष्ट्यांचा Microsoft Agent Framework च्या काही मुख्य संकल्पनांवर कसा वापर केला जातो ते पाहूया.

## Microsoft Agent Framework ची मुख्य संकल्पना

### एजंट्स

![एजंट घटक](../../../translated_images/mr/agent-components.410a06daf87b4fef.webp)

**एजंट तयार करणे**

एजंट तयार करणे हे inference सेवा (LLM Provider), AI एजंटने अनुसरण करण्यासाठी सूचना संच, आणि एक नियुक्त `name` परिभाषित करून केले जाते:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

वरील उदाहरण `Azure OpenAI` वापरत आहे परंतु एजंट विविध सेवांचा वापर करून तयार केले जाऊ शकतात जसे की `Microsoft Foundry Agent Service`:

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

किंवा A2A प्रोटोकॉल वापरून रिमोट एजंट्स:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**एजंट चालवणे**

एजंट्स `.run` किंवा `.run_stream` पद्धती वापरून चालवले जातात ज्यामध्ये नॉन-स्ट्रीमिंग किंवा स्ट्रीमिंग प्रतिसादांसाठी वापरले जाते.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

प्रत्येक एजंट रनमध्ये `max_tokens`, एजंट कॉल करू शकणारी `tools`, आणि अगदी एजंटसाठी वापरले जाणारे `model` सारखे पॅरामीटर्स सानुकूल करण्याचे पर्याय देखील असू शकतात.

हा उपयोगी असतो जेंव्हा विशिष्ट मॉडेल्स किंवा टूल्स वापरणे वापरकर्त्याच्या कामासाठी आवश्यक असते.

**टूल्स**

टूल्स एजंट परिभाषित करताना दोन्ही ठिकाणी परिभाषित केल्या जाऊ शकतात:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ChatAgent थेट तयार करताना

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

आणि एजंट चालवताना देखील:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # हे साधन फक्त या रनसाठी प्रदान केले आहे )
```

**एजंट थ्रेड्स**

एजंट थ्रेड्स बहु-फेऱ्यांच्या संभाषणांना हाताळण्यासाठी वापरल्या जातात. थ्रेड्स तयार करता येतात:

- `get_new_thread()` वापरून ज्यामुळे थ्रेड वेळोवेळी जतन केला जाऊ शकतो
- किंवा एजंट चालवताना थ्रेड आपोआप तयार होतो आणि तो केवळ वर्तमान रनदरम्यानच टिकतो.

थ्रेड तयार करण्याचा कोड असा दिसतो:

```python
# नवीन थ्रेड तयार करा.
thread = agent.get_new_thread() # एजंटला त्या थ्रेडसह चालवा.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

नंतर आपण नंतर वापरण्यासाठी थ्रेड सिरीयलाईज़ करू शकता:

```python
# नवीन थ्रेड तयार करा.
thread = agent.get_new_thread() 

# थ्रेडसह एजंट चालवा.

response = await agent.run("Hello, how are you?", thread=thread) 

# संग्रहणासाठी थ्रेड सीरिअलाइझ करा.

serialized_thread = await thread.serialize() 

# संग्रहणातून लोड केल्यानंतर थ्रेडची स्थिती डीसीरिअलाइझ करा.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**एजंट मिडलवेअर**

एजंट्स टूल्स आणि LLMs सह संवाद करून वापरकर्त्यांचे कार्य पूर्ण करतात. काही परिस्थितींमध्ये, या संवादांदरम्यान एखादी क्रिया कार्यान्वित करायची किंवा ट्रॅक करायची असते. एजंट मिडलवेअर आम्हाला हे करण्यास सक्षम करते:

*फंक्शन मिडलवेअर*

हे मिडलवेअर एजंट आणि कॉल केला जाणारा फंक्शन/टूल या दरम्यान एखादी क्रिया चालवण्याची परवानगी देते. उदाहरणार्थ, फंक्शन कॉलवर लॉगिंग करायचे असल्यास हे वापरले जाऊ शकते.

खालच्या कोडमध्ये `next` हे परिभाषित करते की पुढचे मिडलवेअर कॉल करायचे की प्रत्यक्ष फंक्शन.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # पूर्व-प्रक्रिया: फंक्शनच्या अंमलबजावणीपूर्वी लॉग करा
    print(f"[Function] Calling {context.function.name}")

    # पुढील मिडलवेअर किंवा फंक्शनच्या अंमलबजावणीकडे पुढे जा
    await next(context)

    # पश्च-प्रक्रिया: फंक्शनच्या अंमलबजावणी नंतर लॉग करा
    print(f"[Function] {context.function.name} completed")
```

*चॅट मिडलवेअर*

हे मिडलवेअर LLM आणि एजंटदरम्यानच्या विनंत्यांदरम्यान एखादी क्रिया चालवण्याची किंवा लॉग करण्याची परवानगी देते.

यात AI सेवेकडे पाठवलेल्या `messages` सारखी महत्त्वाची माहिती समाविष्ट असते.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # पूर्व-प्रक्रिया: AI कॉलच्या आधी नोंदी करा
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # पुढील मिडलवेअर किंवा AI सेवेकडे पुढे जा
    await next(context)

    # पोस्ट-प्रक्रिया: AI प्रतिसादानंतर नोंदी करा
    print("[Chat] AI response received")

```

**एजंट मेमरी**

`Agentic Memory` धड्यात चर्चा केलेप्रमाणे, मेमरी ही एजंटला विविध संदर्भांवर कार्य करण्यास सक्षम करण्यासाठी एक महत्त्वाचा घटक आहे. MAF मध्ये अनेक प्रकारच्या मेमरी उपलब्ध आहेत:

*इन-मेमरी स्टोरेज*

ही मेमरी अनुप्रयोग रनटाइम दरम्यान थ्रेड्समध्ये साठवली जाते.

```python
# नवीन थ्रेड तयार करा.
thread = agent.get_new_thread() # त्या थ्रेडसह एजंट चालवा.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*स्थायी संदेश (Persistent Messages)*

ही मेमरी वेगवेगळ्या सत्रांमध्ये संभाषण इतिहास साठवण्यासाठी वापरली जाते. हे `chat_message_store_factory` वापरून परिभाषित केले जाते:

```python
from agent_framework import ChatMessageStore

# सानुकूल संदेश साठवण तयार करा
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*डायनॅमिक मेमरी*

ही मेमरी एजंट सुरु होण्यापूर्वी संदर्भात जोडली जाते. या मेमरी बाह्य सेवांमध्ये जसे mem0 मध्ये साठवता येऊ शकतात:

```python
from agent_framework.mem0 import Mem0Provider

# उन्नत मेमरी क्षमतांसाठी Mem0 चा वापर
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

**एजंट ऑब्झर्वेबिलिटी**

ऑब्झर्वेबिलिटी विश्वसनीय आणि देखभालयोग्य agentic सिस्टीम्स तयार करण्यासाठी महत्त्वाची आहे. MAF OpenTelemetry सोबत एकत्रिकृत करते जेणेकरून चांगल्या ट्रेसिंग आणि मीटर्सद्वारे ऑब्झर्वेबिलिटी प्रदान करता येईल.

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

MAF वर्कफ्लोज ऑफर करते ज्यात पूर्वनिर्धारित पायऱ्या असतात ज्या एखादे कार्य पूर्ण करण्यासाठी आणि त्या पायऱ्यांमध्ये AI एजंट घटक समाविष्ट करतात.

वर्कफ्लोज वेगवेगळ्या घटकांनी बनलेले असतात जे नियंत्रण प्रवाह सुधारतात. वर्कफ्लोज **मल्टी-एजंट ऑर्केस्ट्रेशन** आणि वर्कफ्लो स्थिती जतन करण्यासाठी **चेकपॉइंटिंग** सक्षम करतात.

वर्कफ्लोचे मुख्य घटक म्हणजे:

**एक्झिक्युटर्स**

एक्झिक्युटर्स इनपुट संदेश प्राप्त करतात, त्यांच्या दिलेल्या कामे पार पाडतात, आणि नंतर आउटपुट संदेश तयार करतात. हे वर्कफ्लोला मोठे कार्य पूर्ण करण्याच्या दिशेने पुढे नेते. एक्झिक्युटर्स AI एजंट किंवा कस्टम लॉजिक असू शकतात.

**एज (Edges)**

एज वर्कफ्लोतील संदेशांचा प्रवाह परिभाषित करण्यासाठी वापरले जातात. हे प्रकारचे असू शकतात:

*डायरेक्ट एजेस* - एक्झिक्युटर्समधील सोपे एक-ते-एक कनेक्शन्स:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*कंडीशनल एजेस* - विशिष्ट अट पूर्ण झाल्यानंतर सक्रिय होतात. उदाहरणार्थ, जेव्हा हॉटेलच्या खोल्या उपलब्ध नसतात, तेव्हा एक्झिक्युटर इतर पर्याय सुचवू शकतो.

*स्विच-केस एजेस* - परिभाषित अटींनुसार संदेश वेगळ्या एक्झिक्युटर्सकडे रूट करतात. उदाहरणार्थ, जर प्रवासी ग्राहकाला प्राधान्य प्रवेश असेल तर त्यांची कामं दुसऱ्या वर्कफ्लोद्वारे हाताळली जाऊ शकतात.

*फॅन-आउट एजेस* - एका संदेशाला अनेक लक्ष्योंकडे पाठवतात.

*फॅन-इन एजेस* - वेगवेगळ्या एक्झिक्युटर्समधून अनेक संदेश गोळा करून एका लक्ष्याकडे पाठवतात.

**इव्हेंट्स**

वर्कफ्लोज मध्ये चांगली ऑब्झर्वेबिलिटी प्रदान करण्यासाठी, MAF एक्झिक्युशनसाठी अंगभूत इव्हेंट्स देते ज्यात समाविष्ट आहे:

- `WorkflowStartedEvent`  - वर्कफ्लो एक्झिक्युशन सुरू होते
- `WorkflowOutputEvent` - वर्कफ्लो आउटपुट तयार करते
- `WorkflowErrorEvent` - वर्कफ्लोला त्रुटी येते
- `ExecutorInvokeEvent`  - एक्झिक्युटर प्रक्रिया सुरू करतो
- `ExecutorCompleteEvent`  - एक्झिक्युटर प्रक्रिया पूर्ण करतो
- `RequestInfoEvent` - विनंती जारी केली जाते

## प्रगत MAF पॅटर्न

वरील विभाग Microsoft Agent Framework च्या मुख्य संकल्पनांवर प्रकाश टाकतात. जेव्हा आपण अधिक जटिल एजंट तयार करता, तेव्हा विचार करण्यासाठी काही प्रगत पॅटर्न:

- **मिडलवेअर संयोजन**: फंक्शन आणि चॅट मिडलवेअरचा वापर करून अनेक मिडलवेअर हँडलर्स (लॉगिंग, ऑथ, रेट-लिमिटिंग) साखळीबद्ध करा जेणेकरून एजंटच्या वर्तनावर सूक्ष्म नियंत्रण मिळेल.
- **वर्कफ्लो चेकपॉइंटिंग**: वर्कफ्लो इव्हेंट्स आणि सिरीयलाईझेशन वापरून दीर्घकालीन एजंट प्रक्रिये जतन आणि पुन्हा सुरू करा.
- **डायनॅमिक टूल निवड**: टूल वर्णनांवर RAG (Retrieval-Augmented Generation) संयोजित करून MAF च्या टूल रजिस्ट्रेशनसह फक्त संबंधित टूल्स प्रति क्वेरी सादर करा.
- **मल्टी-एजंट हँडऑफ**: विशेष एजंट्समधील हँडऑफ ऑर्केस्ट्रेट करण्यासाठी वर्कफ्लो एजेस आणि कंडीशनल राऊटिंग वापरा.

## कोड नमुने

Microsoft Agent Framework साठीचे कोड नमुने या रिपॉझिटरीमध्ये `xx-python-agent-framework` आणि `xx-dotnet-agent-framework` फाइलांखाली आढळतील.

## Microsoft Agent Framework बाबत आणखी प्रश्न आहेत का?

इतर शिकणाऱ्यांशी भेटण्यासाठी, ऑफिस अवर्समध्ये सहभागी होण्यासाठी आणि आपल्या AI Agents संबंधित प्रश्नांची उत्तरे मिळवण्यासाठी [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) मध्ये सामील व्हा.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
अस्वीकरण:
हे दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केले आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, परंतु कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत म्हणून मानले पाहिजे. महत्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजांसाठी किंवा चुकीच्या अर्थलागीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->