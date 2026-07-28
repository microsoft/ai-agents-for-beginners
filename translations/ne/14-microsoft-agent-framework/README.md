# माइक्रोसफ्ट एजेन्ट फ्रेमवर्क अन्वेषण गर्दै

![Agent Framework](../../../translated_images/ne/lesson-14-thumbnail.90df0065b9d234ee.webp)

### परिचय

यस पाठले समेट्नेछ:

- माइक्रोसफ्ट एजेन्ट फ्रेमवर्क बुझ्दै: प्रमुख विशेषताहरू र मूल्य  
- माइक्रोसफ्ट एजेन्ट फ्रेमवर्कका मुख्य अवधारणाहरू अन्वेषण गर्दै
- उन्नत MAF ढाँचा: कार्यप्रवाहहरू, मिडलवेयर, र स्मृति

## सिकाइ लक्ष्यहरू

यस पाठ समाप्त गरेपछि, तपाईं जान्नु हुनेछ:

- माइक्रोसफ्ट एजेन्ट फ्रेमवर्क प्रयोग गरेर उत्पादन तयार AI एजेन्टहरू बनाउने
- माइक्रोसफ्ट एजेन्ट फ्रेमवर्कका मुख्य विशेषताहरूलाई तपाईंको एजेन्टिक प्रयोग केसहरूमा लागू गर्ने
- कार्यप्रवाहहरू, मिडलवेयर, र अवलोकनशीलता सहित उन्नत ढाँचाहरू प्रयोग गर्ने

## कोड नमूनाहरू 

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) का कोड नमूनाहरू यस रिपोजिटोरीमा `xx-python-agent-framework` र `xx-dotnet-agent-framework` फाइलहरूमा भेट्न सकिन्छ।

## माइक्रोसफ्ट एजेन्ट फ्रेमवर्क बुझ्दै

![Framework Intro](../../../translated_images/ne/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) माइक्रोसफ्टको एउटै फ्रेमवर्क हो जुन AI एजेन्टहरू निर्माण गर्नका लागि बनेको छ। यसले उत्पादन र अनुसन्धान वातावरणहरूमा देखिएका विभिन्न एजेन्टिक प्रयोग केसहरूलाई सम्बोधन गर्ने लचिलोपन प्रस्ताव गर्दछ, जस्तै:

- **क्रमिक एजेन्ट अर्चेस्ट्रेशन** जहाँ चरण-द्वारा-चरण कार्यप्रवाहहरू आवश्यक हुन्छन्।
- **समकालीन अर्चेस्ट्रेशन** जहाँ एजेन्टहरूले एकै समयमा कार्यहरू पूरा गर्नुपर्छ।
- **समूह च्याट अर्चेस्ट्रेशन** जहाँ एजेन्टहरूले एउटै कार्यमा सँगै सहयोग गर्न सक्छन्।
- **ह्यान्डअफ अर्चेस्ट्रेशन** जहाँ एजेन्टहरूले उपकार्यहरू पूरा भएपछि कार्य एक-अर्कामा सुम्पिन्छन्।
- **म्याग्नेटिक अर्चेस्ट्रेशन** जहाँ व्यवस्थापक एजेन्टले कार्य सूची सिर्जना र संशोधन गर्छ र उपएजेन्टहरूको समन्वय गर्छ।

उत्पादनमा AI एजेन्टहरू प्रदान गर्न, MAF ले थप सुविधा पनि समावेश गरेको छ:

- **अवलोकनशीलता** OpenTelemetry को प्रयोगबाट जहाँ AI एजेन्टको प्रत्येक क्रिया जस्तै उपकरण कल, अर्चेस्ट्रेशन चरणहरू, सोच प्रक्रियाहरू र Microsoft Foundry ड्याशबोर्डमार्फत प्रदर्शन निगरानी हुन्छ।
- **सुरक्षा** एजेन्टहरू Microsoft Foundry मा नै होस्ट गरेर, जसमा भूमिका आधारित पहुँच, निजी डाटा व्यवस्थापन र निर्मित सामग्री सुरक्षा समावेश छन्।
- **टिकाउपन** एजेन्ट थ्रेडहरू र कार्यप्रवाहहरू रोक्न, पुनः सुरु गर्न र त्रुटिहरूबाट उपचार गर्न सकिन्छ जसले लामो समयसम्म चल्ने प्रक्रियालाई सक्षम बनाउँछ।
- **नियन्त्रण** मानव सहभागिताको आवश्यक भएको कार्यहरू चिन्ह लगाएर मानव अनुमोदनको समर्थन गरेको मानव इन द लूप कार्यप्रवाहहरू।

माइक्रोसफ्ट एजेन्ट फ्रेमवर्क अन्तर्सञ्चालनीय हुन पनि केन्द्रित छ:

- **क्लाउड-निरपेक्ष हुन** - एजेन्टहरू कन्टेनरमा, अन-प्रिम र धेरै भिन्न क्लाउडहरूमा चल्न सक्दछन्।
- **प्रदायक-निरपेक्ष हुन** - एजेन्टहरू तपाईंको रोजाइको SDK सहित Azure OpenAI र OpenAI मार्फत सिर्जना गर्न सकिन्छ।
- **खुला मानकहरू एकीकृत गर्दै** - एजेन्टहरूले Agent-to-Agent(A2A) र Model Context Protocol (MCP) जस्ता प्रोटोकलहरू उपयोग गरी अरू एजेन्ट र उपकरणहरू पत्ता लगाउन र प्रयोग गर्न सक्छन्।
- **प्लगइनहरू र कनेक्टरहरू** - Microsoft Fabric, SharePoint, Pinecone र Qdrant जस्ता डाटा र स्मृति सेवाहरूमा कनेक्शन गर्न सकिन्छ।

यी सुविधाहरूलाई माइक्रोसफ्ट एजेन्ट फ्रेमवर्कका केही मुख्य अवधारणाहरूमा कसरी लागू गरिन्छ हेरौँ।

## माइक्रोसफ्ट एजेन्ट फ्रेमवर्कका मुख्य अवधारणाहरू

### एजेन्टहरू

![Agent Framework](../../../translated_images/ne/agent-components.410a06daf87b4fef.webp)

**एजेन्ट सिर्जना गर्दै**

एजेन्ट सिर्जना LLM प्रदायकको रूपमा इनफरेन्स सेवा निर्धारण गरेर, AI एजेन्टले पालना गर्ने निर्देशनहरूको सेट सहित, र एक `name` तोकेर गरिन्छ:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

माथिको उदाहरण `Azure OpenAI` प्रयोग गरिरहेको छ, तर एजेन्टहरू विभिन्न सेवाहरू प्रयोग गरेर सिर्जना गर्न सकिन्छ जस्तै `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI को `Responses`, `ChatCompletion` API हरू

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

वा [MiniMax](https://platform.minimaxi.com/), जसले ठूलो सन्दर्भ विन्डोहरू (२०४K टोकन सम्म) सहित OpenAI-संग अनुकूल API प्रदान गर्दछ:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

वा A2A प्रोटोकल प्रयोग गरी दुर्गम एजेन्टहरू:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**एजेन्टहरू चलाउँदै**

एजेन्टहरू `.run` वा `.run_stream` मेथडहरू प्रयोग गरेर, निर्बाह वा स्ट्रिमिङ प्रतिक्रियाहरूका लागि चलाइन्छन्।

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

प्रत्येक एजेन्ट रनमा पनि विकल्पहरू हुन सक्छन् जसले एजेन्टद्वारा प्रयोग गरिने `max_tokens`, एजेन्टले कल गर्नसक्ने `tools`, र प्रयोग गरिने `model` सहितका प्यारामिटरहरू अनुकूलन गर्न सकिन्छ।

यसले तिनी केसहरूमा उपयोगी हुन्छ जहाँ प्रयोगकर्ताको कार्य पूरा गर्न विशेष मोडेलहरू वा उपकरणहरू आवश्यक पर्छ।

**उपकरणहरू**

उपकरणहरू एजेन्ट परिभाषित गर्दा:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# सिधा ChatAgent सिर्जना गर्दा

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

र एजेन्ट चलाउँदा पनि परिभाषित गर्न सकिन्छ:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # यो रनको लागि मात्र प्रदान गरिएको उपकरण )
```

**एजेन्ट थ्रेडहरू**

एजेन्ट थ्रेडहरू बहु-वार्ता संभाल्न प्रयोग गरिन्छ। थ्रेडहरू निम्न तरिकाले सिर्जना गर्न सकिन्छ:

- `get_new_thread()` प्रयोग गर्दा जसले थ्रेडलाई समयक्रममा बचत गर्न अनुमति दिन्छ
- एजेन्ट चलाउँदा स्वचालित रूपमा थ्रेड सिर्जना हुन्छ र त्यो थ्रेडले केवल वर्तमान चल्ने क्रममा बाँच्छ।

थ्रेड सिर्जना गर्न कोड यसरी देखिन्छ:

```python
# नयाँ थ्रेड सिर्जना गर्नुहोस्।
thread = agent.get_new_thread() # थ्रेडसँग एजेन्ट चलाउनुहोस्।
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

त्यसपछि तपाइँ थ्रेडलाई पछि प्रयोगको लागि स्टोर गर्न सक्नुहुन्छ:

```python
# नयाँ थ्रेड सिर्जना गर्नुहोस्।
thread = agent.get_new_thread() 

# थ्रेडसँग एजेन्ट चलाउनुहोस्।

response = await agent.run("Hello, how are you?", thread=thread) 

# भण्डारणको लागि थ्रेड सिरीयलाइज गर्नुहोस्।

serialized_thread = await thread.serialize() 

# भण्डारणबाट लोड पछि थ्रेड स्थिति डीसिरीयलाइज गर्नुहोस्।

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**एजेन्ट मिडलवेयर**

एजेन्टहरूले उपकरण र LLM सँग अन्तरक्रिया गरेर प्रयोगकर्ताका कार्यहरू पूरा गर्दछन्। केहि अवस्थामा हामी यी अन्तरक्रियाहरूको बीचमा केहि कार्य वा ट्र्याकिङ गर्न चाहन्छौं। एजेन्ट मिडलवेयरले निम्न मार्फत यसलाई सम्भव बनाउँछ:

*फङ्क्शन मिडलवेयर*

यस मिडलवेयरले एजेन्ट र फङ्क्शन/उपकरण बीचको कल बिचमा केही क्रिया चलाउन अनुमति दिन्छ। जस्तो कि तपाईं कलमा केहि लगिङ गर्न चाहनुहुन्छ भने यो उपयोगी हुन्छ।

तलको कोडमा `next` ले अर्को मिडलवेयर वा वास्तविक फङ्क्शन कल गर्नुपर्छ कि छैन निर्धारण गर्छ।

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # पूर्व-प्रक्रिया: कार्य निष्पादन अघि लग इन गर्नुहोस्
    print(f"[Function] Calling {context.function.name}")

    # अर्को मिडलवेयर वा कार्य निष्पादन जारी राख्नुहोस्
    await next(context)

    # पश्चात-प्रक्रिया: कार्य निष्पादन पछि लग इन गर्नुहोस्
    print(f"[Function] {context.function.name} completed")
```

*च्याट मिडलवेयर*

यो मिडलवेयरले एजेन्ट र LLM बीचका अनुरोधहरू बीचमा कुनै क्रिया चलाउन वा लग गर्न अनुमति दिन्छ।

यसमा AI सेवामा पठाइने `messages` जस्ता महत्वपूर्ण जानकारीहरू हुन्छन्।

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # पूर्व-संसोधन: AI कल पहिले लग इन गर्नुहोस्
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # अर्को मिडलवेयर वा AI सेवामा जारी राख्नुहोस्
    await next(context)

    # पश्च-संसोधन: AI प्रतिक्रिया पछि लग इन गर्नुहोस्
    print("[Chat] AI response received")

```

**एजेन्ट स्मृति**

`Agentic Memory` पाठमा जस्तै, स्मृति एजेन्टलाई फरक फरक सन्दर्भमा काम गर्ने सक्षम बनाउँछ। MAF ले विभिन्न प्रकारका स्मृतिहरू प्रस्ताव गर्दछ:

*इन-मेमोरी स्टोरेज*

यो स्मृति एप्लिकेशन रनटाइममा थ्रेडहरूमा भण्डारण हुन्छ।

```python
# नयाँ थ्रेड सिर्जना गर्नुहोस्।
thread = agent.get_new_thread() # थ्रेडसँग एजेन्ट चलाउनुहोस्।
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*टिकाउ सन्देशहरू*

यो स्मृति विभिन्न सेसनहरूमा संवाद इतिहास भण्डारण गर्दा प्रयोग हुन्छ। यो `chat_message_store_factory` प्रयोग गरेर परिभाषित गरिन्छ:

```python
from agent_framework import ChatMessageStore

# अनुकूलित सन्देश स्टोर सिर्जना गर्नुहोस्
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*डाइनामिक स्मृति*

यो स्मृति एजेन्टहरू चलाउनु अघि सन्दर्भमा थपिन्छ। यी स्मृतिहरू बाह्य सेवाहरूमा भण्डारण गर्न सकिन्छ जस्तै mem0:

```python
from agent_framework.mem0 import Mem0Provider

# उन्नत मेमोरी क्षमता को लागि Mem0 को प्रयोग गर्दै
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

**एजेन्ट अवलोकनशीलता**


एजेन्टिक प्रणालीहरूलाई भरपर्दो र मर्मतयोग्य बनाउन अवलोकनशीलता महत्वपूर्ण छ। MAF ले OpenTelemetry सँग एकीकृत भएर अवलोकनशीलतालाई सुधार गर्न ट्रेसिङ र मिटरहरू प्रदान गर्दछ।

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # केही गर्नुहोस्
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### कार्यप्रवाहहरू

MAF ले पूर्व-परिभाषित चरणहरू सहित कार्यप्रवाहहरू प्रस्ताव गर्दछ जसले एउटा कार्य पूरा गर्न र ती चरणहरूमा AI एजेन्टहरूलाई कम्पोनेंटको रूपमा समावेश गर्दछ।

कार्यप्रवाहहरू विभिन्न कम्पोनेंटहरूले बनेका हुन्छन् जसले नियन्त्रण प्रवाहलाई सुधार गर्छन्। कार्यप्रवाहहरूले **बहु-एजेन्ट संयोजन** र **चेकप्वाइन्टिङ** लाई पनि सक्षम बनाउँछन् जसले कार्यप्रवाह अवस्थाहरू बचत गर्छ।

कार्यप्रवाहका मुख्य कम्पोनेंटहरू हुन्:

**कार्यपालकहरू**

कार्यपालकहरूले इनपुट सन्देशहरू प्राप्त गर्छन्, आफ्नो असाइन गरिएको कार्यहरू पूरा गर्छन्, र पछि आउटपुट सन्देश उत्पादन गर्छन्। यसले कार्यप्रवाहलाई ठूलो कार्य पूरा गर्न तर्फ अगाडि बढाउँछ। कार्यपालकहरू AI एजेन्ट वा कस्टम तर्क हुन सक्छन्।

**एजहरू**

एजहरू कार्यप्रवाहमा सन्देशहरूको प्रवाह परिभाषित गर्न प्रयोग गरिन्छ। यी समावेश हुन सक्छन्:

*प्रत्यक्ष एजहरू* - कार्यपालकहरूबीच सादा एक-देखि-एक सम्बन्धहरू:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*सशर्त एजहरू* - निश्चित सर्त पूरा भएपछि सक्रिय। उदाहरणका लागि, जब होटल कोठाहरू उपलब्ध हुँदैनन्, तब कार्यपालकले अन्य विकल्पहरू सिफारिस गर्न सक्छ।

*स्विच-केस एजहरू* - वर्णन गरिएका सर्तहरूका आधारमा सन्देशहरू विभिन्न कार्यपालकहरूमा मार्गनिर्देशन। उदाहरणका लागि, यदि यात्रा ग्राहकसँग प्राथमिकता पहुँच छ भने, तिनीहरूको कार्यहरू अर्को कार्यप्रवाहबाट ह्यान्डल गरिन्छ।

*फ्यान-आउट एजहरू* - एक सन्देशलाई धेरै लक्ष्यहरूमा पठाउने।

*फ्यान-इन एजहरू* - विभिन्न कार्यपालकहरूबाट धेरै सन्देशहरू सङ्कलन गरी एक लक्ष्यमा पठाउने।

**घटनाहरू**

कार्यप्रवाहहरूमा राम्रो अवलोकनशीलता प्रदान गर्न MAF ले कार्यान्वयनका लागि निर्मित घटनाहरू प्रस्ताव गर्दछ जसमा समावेश छन्:

- `WorkflowStartedEvent`  - कार्यप्रवाह कार्यान्वयन सुरु हुन्छ
- `WorkflowOutputEvent` - कार्यप्रवाहले आउटपुट उत्पादन गर्छ
- `WorkflowErrorEvent` - कार्यप्रवाहले त्रुटि अनुभव गर्छ
- `ExecutorInvokeEvent`  - कार्यपालकले प्रक्रिया सुरु गर्छ
- `ExecutorCompleteEvent`  -  कार्यपालकले प्रक्रिया समाप्त गर्छ
- `RequestInfoEvent` - अनुरोध जारी गरिन्छ

## उन्नत MAF ढाँचा

माथिका भागहरूले Microsoft Agent Framework का मुख्य अवधारणाहरू समेटेका छन्। जटिल एजेन्टहरू निर्माण गर्दा विचार गर्नुपर्ने केही उन्नत ढाँचाहरू यसप्रकार छन्:

- **मिडलवेयर संयोजन**: मल्टिपल मिडलवेयर ह्यान्डलरहरू (लगिङ, प्रमाणीकरण, दर-सीमा) लाई श्रृंखला गरी एजेन्ट व्यवहारमाथि सूक्ष्म नियन्त्रणका लागि फंक्शन र च्याट मिडलवेयर प्रयोग गर्नुहोस्।
- **कार्यप्रवाह चेकप्वाइन्टिङ**: कार्यप्रवाह घटनाहरू र सिरियलाइजेसन प्रयोग गरी लामो समयसम्म चल्ने एजेन्ट प्रक्रियाहरू बचत र पुनः सुरु गर्नुहोस्।
- **डाइनामिक उपकरण चयन**: MAF को उपकरण दर्तासँग RAG को संयोजन गरेर प्रत्येक प्रश्नका लागि मात्र सान्दर्भिक उपकरणहरू प्रस्तुत गर्नुहोस्।
- **बहु-एजेन्ट हस्तान्तरण**: कार्यप्रवाह एजहरू र सशर्त रुटिङ प्रयोग गरी विशेषीकृत एजेन्टहरू बीच समन्वय गर्नुहोस्।

## Microsoft Foundry मा LangChain / LangGraph एजेन्टहरू होस्टिङ

Microsoft Agent Framework **फ्रेेमवर्क-अन्तरक्रियाशील** हो — तपाईं MAF का साथ लेखिएका एजेन्टहरूमा सीमित हुनुहुन्न। यदि तपाईंले पहिले नै **LangChain** वा **LangGraph** सँग एजेन्ट निर्माण गर्नुभएको छ भने, त्यसलाई **Microsoft Foundry होस्टेड एजेन्ट** को रूपमा चलाउन सक्नुहुन्छ जसले Foundry ले रनटाइम, सत्रहरू, स्केलेङ, पहिचान र प्रोटोकल अन्तबिन्दुहरू व्यवस्थापन गर्छ, जबकि तपाईंको एजेन्ट तर्क LangGraph मा रहन्छ।

यो `langchain_azure_ai.agents.hosting` प्याकेजसँग गरिन्छ, जुन Foundry होस्टेड एजेन्टहरूले प्रयोग गर्ने उही प्रोटोकलहरूमा कम्पाइल गरिएको LangGraph ग्राफलाई एक्सपोज गर्छ।

**१. होस्टिङ एक्स्ट्रा इन्स्टल गर्नुहोस्:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` एक्स्ट्राले Foundry प्रोटोकल पुस्तकालयहरू इन्स्टल गर्छ: `azure-ai-agentserver-responses` (OpenAI-अनुकूल `/responses` अन्तबिन्दु) र `azure-ai-agentserver-invocations` (सामान्य `/invocations` अन्तबिन्दु)।

**२. होस्टिङ प्रोटोकल छान्नुहोस्:**

| प्रोटोकल | होस्ट क्लास | अन्तबिन्दु | प्रयोग गर्ने बेला |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | तपाईंले OpenAI-अनुकूल च्याट, स्ट्रिमिङ, प्रतिक्रिया इतिहास, र संवाद थ्रेडिङ चाहनुहुन्छ — वार्तालाप एजेन्टहरूको लागि सिफारिस गरिएको पूर्वनिर्धारित। |
| **Invocations** | `InvocationsHostServer` | `/invocations` | तपाईंलाई कस्टम JSON संरचना, वेबहुक-शैली अन्तबिन्दु, वा गैर-वार्तालाप प्रक्रियाको आवश्यकता छ। |

किनकि **Responses API Foundry मा एजेन्ट-शैली विकासको प्रमुख API हो**, अधिकांश एजेन्टहरूका लागि `ResponsesHostServer` बाट सुरु गर्नुहोस्।

**३. वातावरण चरहरू कन्फिगर गर्नुहोस्** (`az login` पहिले गर्नुहोस् ताकि `DefaultAzureCredential` प्रमाणीकरण गर्न सकोस्):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

जब एजेन्ट पछि Foundry मा होस्टेड एजेन्टको रूपमा चल्छ, प्लेटफर्मले स्वतः `FOUNDRY_PROJECT_ENDPOINT` इन्जेक्ट गर्छ।

**४. Responses प्रोटोकलमा LangGraph एजेन्ट एक्सपोज गर्नुहोस्:**

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

    # ChatOpenAI यहाँ Foundry परियोजनाको OpenAI-समर्थित (Responses) अन्तिम बिन्दुलाई लक्षित गर्दछ।
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

स्थानीय रूपमा `python main.py` सँग चलाउनुहोस्, त्यसपछि `http://localhost:8088/responses` मा Responses अनुरोध पठाउनुहोस्।

**मुख्य व्यवहारहरू:**

- **वार्तालापहरू**: क्लाइन्टहरूले `previous_response_id` वा `conversation` ID पास गरेर कुरा जारी राख्छन्। यदि तपाईंको ग्राफ LangGraph चेकप्वाइन्टरसँग कम्पाइल गरिएको छ भने, Foundry ले वार्तालाप अवस्थालाई चेकप्वाइन्टसँग कुञ्जी गर्छ (उत्पादनमा टिकाऊ चेकप्वाइन्टर प्रयोग गर्नुहोस्; स्थानीय परीक्षणका लागि `MemorySaver` पर्याप्त छ)।
- **मानव-इन-द-लूप**: यदि तपाईंको ग्राफ LangGraph `interrupt()` प्रयोग गर्छ भने, `ResponsesHostServer` ले पेंडिङ रोकावटलाई Responses `function_call` / `mcp_approval_request` वस्तुका रूपमा देखाउँछ, र क्लाइन्टहरूले मेल खाने `function_call_output` / `mcp_approval_response` सँग पुन: सुरु गर्छन्।
- **Foundry मा डिप्लोय गर्नुहोस्**: Azure Developer CLI प्रयोग गर्नुहोस् — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (स्थानीय, Docker आवश्यक), पछि `azd provision` र `azd deploy`। होस्टेड-एजेन्ट डिप्लोयमेन्टका लागि **Foundry Project Manager** भूमिका आवश्यक छ।

यस उदाहरणको रन गर्न मिल्ने संस्करण [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) मा उपलब्ध छ। पूर्ण मार्गनिर्देशन (Invocations प्रोटोकल, कस्टम अनुरोध स्किमाहरू, र समस्या समाधान) को लागि [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) हेर्नुहोस्।

## कोड नमूनाहरू

Microsoft Agent Framework का लागि कोड नमूनाहरू यस रिपोजिटरीमा `xx-python-agent-framework` र `xx-dotnet-agent-framework` फाइलहरू अन्तर्गत भेट्न सकिन्छ।

## Microsoft Agent Framework सम्बन्धमा थप प्रश्नहरू छन्?

अन्य सिक्नेहरूसँग भेट्न, अफिस आवरमा सहभागी हुन र तपाईंका AI एजेन्ट प्रश्नहरूको उत्तर पाउन [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) मा सामेल हुनुहोस्।
## अघिल्लो पाठ

[AI एजेन्टहरूको मेमोरी](../13-agent-memory/README.md)

## अर्को पाठ

[कम्प्युटर प्रयोग एजेन्टहरू (CUA) बनाउने](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->