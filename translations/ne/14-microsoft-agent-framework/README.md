# माइक्रोसफ्ट एजेन्ट फ्रेमवर्क अन्वेषण गर्दै

![Agent Framework](../../../translated_images/ne/lesson-14-thumbnail.90df0065b9d234ee.webp)

### परिचय

यो पाठले कभर गर्नेछ:

- माइक्रोसफ्ट एजेन्ट फ्रेमवर्क बुझ्न: मुख्य विशेषताहरू र मूल्य  
- माइक्रोसफ्ट एजेन्ट फ्रेमवर्कका मुख्य अवधारणाहरू अन्वेषण गर्ने
- उन्नत MAF ढाँचाहरू: कार्यप्रवाहहरू, मध्यवर्ती, र मेमोरी

## सिकाइ लक्ष्यहरू

यो पाठ पूरा गरेपछि, तपाईं जान्ने हुनुहुनेछ कसरी:

- माइक्रोसफ्ट एजेन्ट फ्रेमवर्क प्रयोग गरेर उत्पादन तयार AI एजेन्टहरू निर्माण गर्ने
- माइक्रोसफ्ट एजेन्ट फ्रेमवर्कका मूल विशेषताहरूलाई तपाईंका एजेन्टिक उपयोग मामिलामा लागू गर्ने
- उन्नत ढाँचाहरू जस्तै कार्यप्रवाह, मध्यवर्ती, र अवलोकनीयता प्रयोग गर्ने

## कोड नमूना 

[माइक्रोसफ्ट एजेन्ट फ्रेमवर्क (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) को कोड नमूनाहरू यस रिपोजिटरीमा `xx-python-agent-framework` र `xx-dotnet-agent-framework` फाइलहरू अन्तर्गत फेला पार्न सकिन्छ।

## माइक्रोसफ्ट एजेन्ट फ्रेमवर्क बुझ्दै

![Framework Intro](../../../translated_images/ne/framework-intro.077af16617cf130c.webp)

[माइक्रोसफ्ट एजेन्ट फ्रेमवर्क (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) माइक्रोसफ्टको एकीकृत फ्रेमवर्क हो जुन AI एजेन्टहरू निर्माणका लागि हो। यसले उत्पादन र अनुसन्धान वातावरणहरूमा देखिने विभिन्न एजेन्टिक उपयोग मामिलाहरूलाई सम्बोधन गर्ने लचिलोपन प्रदान गर्दछ, जसमा समावेश छन्:

- **क्रमागत एजेन्ट अनस्ट्रेशन** जहाँ चरण-द्वारा-चरण कार्यप्रवाह आवश्यक हुन्छ।
- **समानान्तर अनस्ट्रेशन** जहाँ एजेन्टहरूले एकै समयमा कार्यहरू पूरा गर्नुपर्छ।
- **समूह संवाद अनस्ट्रेशन** जहाँ एजेन्टहरूले एउटै कार्यमा सँगै सहयोग गर्न सक्छन्।
- **ह्यान्डअफ अनस्ट्रेशन** जहाँ एजेन्टहरूले उप-कार्यहरू पूरा भएपछि एक अर्कालाई कार्य हस्तान्तरण गर्छन्।
- **म्याग्नेटिक अनस्ट्रेशन** जहाँ व्यवस्थापक एजेन्टले कार्य सूचि सिर्जना र संशोधन गर्छ र उप-एजेन्टहरूको समन्वय सम्हाल्छ।

उत्पादनमा AI एजेन्टहरू प्रदान गर्न, MAF मा यी सुविधाहरू पनि छन्:

- **अवलोकनीयता** OpenTelemetry को प्रयोग मार्फत जहाँ AI एजेन्टको प्रत्येक क्रियाकलाप जस्तै उपकरण आह्वान, अनस्ट्रेशन चरणहरू, तर्क प्रवाह र माइक्रोसफ्ट फाउन्ड्री ड्यासबोर्ड मार्फत प्रदर्शन अनुगमन हुन्छ।
- **सुरक्षा** एजेन्टहरूलाई माइक्रोसफ्ट फाउन्ड्रीमा मूल रूपमा होस्ट गरी जेठा पहुँच, निजी डाटा ह्यान्डलिंग र सामग्री सुरक्षा जस्ता सुरक्षा नियन्त्रणहरू समावेश गर्दछ।
- **टिकाउपन** एजेन्ट थ्रेडहरू र कार्यप्रवाहहरू रोक्न, पुनः सुरु गर्न र त्रुटिबाट फर्कन सक्छन् जसले लामो समय चल्ने प्रक्रियाहरू सक्षम गर्छ।
- **नियन्त्रण** मान्छेले हस्तक्षेप गर्ने कार्यप्रवाहहरू समर्थन गर्दछ जहाँ कार्यहरू मानवीय स्वीकृतिका लागि चिन्ह लगाइन्छ।

माइक्रोसफ्ट एजेन्ट फ्रेमवर्क अन्तरक्रियाशील बनाउन पनि केन्द्रित छ:

- **क्लाउड-एग्नोस्टिक** - एजेन्टहरू कन्टेनरहरू, अन-प्रीम र विभिन्न क्लाउडहरूमा चल्न सक्छन्।
- **प्रदायक-एग्नोस्टिक** - एजेन्टहरू तपाईँको रोजाइको SDK मार्फत सिर्जना गर्न सकिन्छ जस्तै Azure OpenAI र OpenAI।
- **खुला मानकहरूको एकीकरण** - एजेन्टहरूले Agent-to-Agent (A2A) र Model Context Protocol (MCP) जस्ता प्रोटोकलहरू प्रयोग गरी अन्य एजेन्टहरू र उपकरणहरू पत्ता लगाउन र प्रयोग गर्न सक्छन्।
- **प्लगइनहरू र कनेक्टरहरू** - माइक्रोसफ्ट फ्याब्रिक, शेयरपोइन्ट, पाइनकन र क्वेडरांट जस्ता डाटा र मेमोरी सेवाहरूमा जडान गर्न सकिन्छ।

अब माइक्रोसफ्ट एजेन्ट फ्रेमवर्कका केही मुख्य अवधारणाहरूमा यी सुविधाहरू कसरी लागू हुन्छन् हेर्छौं।

## माइक्रोसफ्ट एजेन्ट फ्रेमवर्कका मुख्य अवधारणाहरू

### एजेन्टहरू

![Agent Framework](../../../translated_images/ne/agent-components.410a06daf87b4fef.webp)


**एजेन्टहरू सिर्जना गर्दै**

एजेन्ट सिर्जना इन्फरेन्स सेवा (LLM प्रदायक), एआई एजेन्टले पछ्याउनुपर्ने निर्देशनहरूको सेट, र निर्दिष्ट गरिएको `name` द्वारा गरिन्छ:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

माथि `Azure OpenAI` प्रयोग गरिएको छ तर एजेन्टहरू विभिन्न सेवाहरू प्रयोग गरेर सिर्जना गर्न सकिन्छ जसमा `Microsoft Foundry Agent Service` पनि समावेश छ:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` API हरू

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

वा [MiniMax](https://platform.minimaxi.com/), जसले ठूलो सन्दर्भ विन्डोहरू (२०४K टोकन सम्म) को साथ OpenAI-संगत API उपलब्ध गराउँछ:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

वा A2A प्रोटोकल प्रयोग गरी रिमोट एजेन्टहरू:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**एजेन्टहरू सञ्चालन गर्दै**

एजेन्टहरू `.run` या `.run_stream` विधिहरू प्रयोग गरेर वा त नन-स्ट्रीमिंग वा स्ट्रिमिंग प्रतिक्रियाहरूका लागि सञ्चालन गरिन्छ।

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

हरेक एजेन्ट सञ्चालनमा एजेण्टले प्रयोग गर्ने `max_tokens`, एजेन्टले कल गर्न सक्ने `tools`, र यहाँसम्म कि एजेन्टको लागि प्रयोग हुने `model` जस्ता प्यारामिटरहरू पनि अनुकूलित गर्न विकल्पहरू हुनसक्छन्।

यो उपयोगी हुन्छ जहाँ विशिष्ट मोडेल वा उपकरणहरू प्रयोगकर्ता कार्य सम्पादन गर्न आवश्यक हुन्छन्।

**उपकरणहरू**

उपकरणहरू एजेन्टलाई परिभाषित गर्दा दुवै सेट गर्न सकिन्छ:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# च्याटएजेन्ट सिधै सिर्जना गर्दा

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

र एजेन्ट सञ्चालन गर्दा पनि:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # यो रनको लागि मात्र प्रदान गरिएको उपकरण )
```

**एजेन्ट थ्रेडहरू**

एजेन्ट थ्रेडहरू बहु-मोठा कुराकानीहरू सम्हाल्न प्रयोग गरिन्छ। थ्रेडहरू यसरी सिर्जना गर्न सकिन्छ:

- `get_new_thread()` प्रयोग गरी जसले थ्रेडलाई समयसँगै सुरक्षित गर्न सक्षम बनाउँछ
- एजेन्ट चलाउँदा स्वतः एक थ्रेड सिर्जना गर्ने र त्यहि रन अवधि भित्र मात्र थ्रेडको अस्तित्व रहने।

थ्रेड सिर्जना गर्न कोड यसरी देखिन्छ:

```python
# नयाँ थ्रेड बनाउनुहोस्।
thread = agent.get_new_thread() # थ्रेडसँग एजेन्ट चलाउनुहोस्।
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

त्यसपछि थ्रेडलाई भण्डारणका लागि सिरियालाइज गर्न सकिन्छ:

```python
# नयाँ थ्रेड सिर्जना गर्नुहोस्।
thread = agent.get_new_thread() 

# थ्रेडसँग एजेन्ट चलाउनुहोस्।

response = await agent.run("Hello, how are you?", thread=thread) 

# भण्डारणको लागि थ्रेडलाई सिरियलाइज गर्नुहोस्।

serialized_thread = await thread.serialize() 

# भण्डारणबाट लोड गरेपछि थ्रेडको अवस्था डीसिरियलाइज गर्नुहोस्।

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**एजेन्ट मिडलवेयर**

एजेन्टहरूले प्रयोगकर्ताका कार्यहरू पूरा गर्न उपकरणहरू र LLMs सँग अन्तरक्रिया गर्छन्। कतिपय अवस्थामा, यी अन्तरक्रियाहरू बीच कुनै क्रियान्वयन वा ट्र्याकिंग गर्न चाहिन्छ। एजेन्ट मिडलवेयरमार्फत हामी यो गर्न सक्छौं:

*फङ्क्शन मिडलवेयर*

यो मिडलवेयरले एजेन्ट र फङ्क्शन/टूल बिच कुनै क्रिया कार्यान्वयन गर्न अनुमति दिन्छ। यसको प्रयोगको उदाहरण फङ्क्शन कलमा केही लगिङ गर्न चाहिँदा हुन्छ।

तलको कोडमा `next` ले अर्को मिडलवेयर वा वास्तविक फङ्क्शन कल गर्नुपर्ने हो कि हो भनेर परिभाषित गर्छ।

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # पूर्व-प्रक्रिया: कार्य सञ्चालन अगाडि लग इन गर्नुहोस्
    print(f"[Function] Calling {context.function.name}")

    # अर्को मिडलवेयर वा कार्य सञ्चालनमा जारी राख्नुहोस्
    await next(context)

    # पश्च-प्रक्रिया: कार्य सञ्चालन पछि लग इन गर्नुहोस्
    print(f"[Function] {context.function.name} completed")
```

*च्याट मिडलवेयर*

यो मिडलवेयरले एजेन्ट र LLM बिचको अनुरोधहरूमा कुनै क्रिया सञ्चालन वा लगिङ गर्न अनुमति दिन्छ।

यसले AI सेवामा पठाईएका `messages` जस्ता महत्वपूर्ण जानकारी समावेश गर्दछ।

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # पूर्व-प्रक्रिया: AI कल अघि लग
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # अर्को मिडलवेयर वा AI सेवा तर्फ जारी राख्नुहोस्
    await next(context)

    # पछिल्लो-प्रक्रिया: AI प्रतिक्रिया पछि लग
    print("[Chat] AI response received")

```

**एजेन्ट मेमोरी**

`Agentic Memory` पाठमा चर्चा गरेजस्तै, मेमोरी एजेन्टलाई विभिन्न सन्दर्भहरूमा सञ्चालन गर्ने महत्वपूर्ण तत्व हो। MAF ले विभिन्न प्रकारका स्मृतिहरू प्रदान गर्दछ:

*इन-मेमोरी भण्डारण*

यो एप्लिकेसन रनटाइमको क्रममा थ्रेडहरूमा भण्डारण गरिएको मेमोरी हो।

```python
# नयाँ थ्रेड सिर्जना गर्नुहोस्।
thread = agent.get_new_thread() # थ्रेडसँग एजेन्ट चलाउनुहोस्।
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*पर्सिस्टेन्ट सन्देशहरू*

यो मेमोरी विभिन्न सत्रहरूमा कुराकानी इतिहास भण्डारण गर्न प्रयोग गरिन्छ। यसलाई `chat_message_store_factory` को उपयोगले परिभाषित गरिन्छ:

```python
from agent_framework import ChatMessageStore

# अनुकूल सन्देश सञ्झ्याल सिर्जना गर्नुहोस्
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*डायनामिक मेमोरी*


एजेन्टहरू चलाउनु अघि यो मेमोरी सन्दर्भमा थपिन्छ। यी मेमोरीहरू mem0 जस्ता बाह्य सेवाहरूमा संग्रहित गर्न सकिन्छ:

```python
from agent_framework.mem0 import Mem0Provider

# उन्नत स्मृति क्षमताहरूको लागि Mem0 प्रयोग गर्दै
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

अवलोकनशीलता भरपर्दो र मर्मतयोग्य एजेन्ट सिस्टमहरू निर्माण गर्न महत्वपूर्ण छ। MAF ले OpenTelemetry सँग एकीकरण गरी ट्रेसिङ र मिटरहरू प्रदान गर्छ जसले राम्रो अवलोकनशीलता हुनसक्छ।

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # केहि गर्नुहोस्
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### कार्यप्रवाहहरू

MAF ले पूर्व-परिभाषित कार्यप्रवाहहरू प्रस्ताव गर्छ जुन कार्य पूरा गर्न चरणहरू हुन् र ती चरणहरूमा AI एजेन्टहरू कम्पोनेन्टको रूपमा समावेश छन्।

कार्यप्रवाहहरू विभिन्न कम्पोनेन्टहरूबाट बनेका हुन्छन् जसले राम्रो नियन्त्रण प्रवाह अनुमति दिन्छ। कार्यप्रवाहहरूले **बहु-एजेन्ट समन्वय** र **चेकपोइन्टिङ** लाई सक्षम बनाउँछन् जसले कार्यप्रवाह अवस्थाहरू बचत गर्छ।

कार्यप्रवाहका मुख्य कम्पोनेन्टहरू हुन्:

**कार्यकारीहरू**

कार्यकारीहरूले इनपुट सन्देशहरू प्राप्त गर्छन्, कामहरू सम्पन्न गर्छन् र त्यसपछि आउटपुट सन्देश उत्पादन गर्छन्। यसले कार्यप्रवाहलाई ठूलो कार्य पूरा गर्ने दिशातर्फ अघि बढाउँछ। कार्यकारीहरू AI एजेन्ट वा कस्टम तर्क हुन सक्छन्।

**किनाराहरू**

किनाराहरू कार्यप्रवाहमा सन्देशहरूको प्रवाह परिभाषित गर्न प्रयोग हुन्छन्। यी हुनसक्छन्:

*प्रत्यक्ष किनाराहरू* - कार्यकारीहरू बीच साधारण एकदेखि एक जडानहरू:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*सर्तीय किनाराहरू* - निश्चित सर्त पूरा भएपछि सक्रिय हुन्छन्। उदाहरणको लागि, होटल कोठाहरू उपलब्ध नभएको बेला, एक कार्यकारीले अन्य विकल्पहरू सुझाव दिन सक्छ।

*स्विच-केस किनाराहरू* - परिभाषित अवस्थाहरू अनुसार सन्देशहरूलाई विभिन्न कार्यकारीहरूमा पठाउँछन्। उदाहरणको लागि, यदि यात्रु ग्राहकलाई प्राथमिकता पहुँच छ भने उनका कार्यहरू अर्को कार्यप्रवाहबाट सम्बोधन हुनेछ।

*फ्यान-आउट किनाराहरू* - एउटा सन्देश धेरै लक्ष्यहरूलाई पठाउनुहोस्।

*फ्यान-इन किनाराहरू* - विभिन्न कार्यकारीहरूबाट धेरै सन्देशहरू सङ्कलन गरी एउटै लक्ष्यमा पठाउनुहोस्।

**घटनाहरू**

कार्यप्रवाहहरूमा राम्रो अवलोकनशीलता प्रदान गर्न, MAF ले निम्न कार्यान्वयन घटनाहरूसमेत प्रस्ताव गर्दछ:

- `WorkflowStartedEvent`  - कार्यप्रवाह कार्यान्वयन सुरु हुन्छ
- `WorkflowOutputEvent` - कार्यप्रवाहले आउटपुट उत्पादन गर्छ
- `WorkflowErrorEvent` - कार्यप्रवाहमा त्रुटि आउँछ
- `ExecutorInvokeEvent`  - कार्यकारीले प्रक्रिया सुरू गर्छ
- `ExecutorCompleteEvent`  - कार्यकारीले प्रक्रिया समाप्त गर्छ
- `RequestInfoEvent` - अनुरोध जारी हुन्छ

## उन्नत MAF ढाँचाहरू

माथिका विभागहरूले माइक्रोसफ्ट एजेन्ट फ्रेमवर्कका मुख्य अवधारणाहरू समेटेका छन्। तपाईंले बढी जटिल एजेन्टहरू निर्माण गर्दा, यहाँ विचार गर्न सकिने केही उन्नत ढाँचाहरू छन्:

- **मिडलवेयर संयोजन**: एजेन्ट व्यवहारमाथि सूक्ष्म नियन्त्रणका लागि फंक्शन र च्याट मिडलवेयर प्रयोग गरी धेरै मिडलवेयर ह्यान्डलरहरू (लगिङ, प्रामाणिकरण, दर-सीमा) शृङ्खला गर्नुहोस्।
- **कार्यप्रवाह चेकपोइन्टिङ**: लामो समय चल्ने एजेन्ट प्रक्रियाहरू बचत र पुनः सुरु गर्न कार्यप्रवाह घटनाहरू र सिरियलाइजेशन प्रयोग गर्नुहोस्।
- **डायनामिक उपकरण चयन**: टूल वर्णनहरूमा RAG र MAF को उपकरण दर्ता संयोजन गरी प्रति प्रश्न मात्र सम्बन्धित उपकरणहरू देखाउनुहोस्।
- **बहु-एजेन्ट हस्तान्तरण**: विशेषज्ञ एजेन्टहरू बीच हस्तान्तरण समन्वय गर्न कार्यप्रवाह किनाराहरू र सर्तीय राउटिङ प्रयोग गर्नुहोस्।

## माइक्रोसफ्ट फाउन्ड्रीमा LangChain / LangGraph एजेन्टहरू होस्ट गर्नुहोस्

माइक्रोसफ्ट एजेन्ट फ्रेमवर्क **फ्रेमवर्क-अन्तरक्रियाशील** छ — तपाईं MAF सँग लेखिएका एजेन्टहरूमा मात्र सीमित हुनुहुन्न। यदि तपाईंले पहिले नै **LangChain** वा **LangGraph** सँग एजेन्ट निर्माण गर्नुभएको छ भने, तपाईं यसलाई **Microsoft Foundry होस्ट गरिएको एजेन्ट** को रूपमा चलाउन सक्नुहुन्छ ताकि फाउन्ड्रीले रनटाइम, सेसनहरू, स्केलिंग, पहिचान, र प्रोटोकल अन्तबिन्दुहरू व्यवस्थापन गरोस्, जबकि तपाईंको एजेन्ट तर्क LangGraph मा रहन्छ।

यो `langchain_azure_ai.agents.hosting` प्याकेजमार्फत गरिन्छ, जसले फाउन्ड्री होस्ट गरिएको एजेन्टहरूले प्रयोग गर्ने समान प्रोटोकलहरूमा संकलित LangGraph ग्राफ प्रकट गर्छ।

**१. होस्टिङ अतिरिक्त इन्स्टल गर्नुहोस्:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` अतिरिक्तले फाउन्ड्री प्रोटोकल पुस्तकालयहरू इन्स्टल गर्छ: `azure-ai-agentserver-responses` (OpenAI-अनुकूल `/responses` अन्तबिन्दु) र `azure-ai-agentserver-invocations` (सामान्य `/invocations` अन्तबिन्दु)।

**२. होस्टिङ प्रोटोकल छान्नुहोस्:**

| प्रोटोकल | होस्ट वर्ग | अन्तबिन्दु | प्रयोग गर्ने बेलामा |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | तपाईं OpenAI-अनुकूल च्याट, स्ट्रिमिङ, प्रतिक्रिया इतिहास, र संवाद थ्रेडिङ चाहनुहुन्छ — संवादात्मक एजेन्टहरूको लागि सिफारिस गरिएको पूर्वनिर्धारित। |
| **Invocations** | `InvocationsHostServer` | `/invocations` | तपाईंलाई कस्टम JSON रूप, वेबहुक शैलीको अन्तबिन्दु, वा गैर-सम्वादात्मक प्रक्रियाकरण चाहिन्छ। |

किनभने **Responses API फाउन्ड्रीमा एजेन्ट शैली विकासका लागि मुख्य API हो**, अधिकांश एजेन्टहरूको लागि `ResponsesHostServer` सँग सुरु गर्नुहोस्।

**३. वातावरण चरहरू कन्फिगर गर्नुहोस्** (`az login` पहिले ताकि `DefaultAzureCredential` प्रमाणीकरण गर्न सकोस्):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

पछि जब एजेन्ट फाउन्ड्रीमा होस्ट गरिएको एजेन्टको रूपमा चल्छ, प्लेटफर्मले `FOUNDRY_PROJECT_ENDPOINT` स्वचालित रूपमा इंजेक्ट गर्छ।

**४. Responses प्रोटोकलमा LangGraph एजेन्ट खुलाउनुहोस्:**

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

    # ChatOpenAI यहाँ Foundry परियोजनाको OpenAI-समर्थित (Responses) अन्त बिन्दुमा लक्षित छ।
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

यसलाई स्थानीय रुपमा `python main.py` सँग चलाउनुहोस्, त्यसपछि `http://localhost:8088/responses` मा Responses अनुरोध पठाउनुहोस्।

**प्रमुख व्यवहारहरू:**

- **संवादहरू**: ग्राहकहरूले `previous_response_id` वा `conversation` ID पास गरेर संवाद जारी राख्छन्। यदि तपाईंको ग्राफ LangGraph चेकपोइन्टरसँग कम्पाइल गरिएको छ भने, फाउन्ड्रीले संवाद अवस्थालाई चेकपोइन्टसँग कुञ्जी गर्दछ (उत्पादनमा टिकाउ चेकपोइन्टर प्रयोग गर्नुहोस्; स्थानीय परीक्षणका लागि `MemorySaver` ठीक छ)।
- **मानव-इन-द-लूप**: यदि तपाईंको ग्राफले LangGraph `interrupt()` प्रयोग गर्छ, `ResponsesHostServer` पेंडिङ इन्टरप्टलाई Responses `function_call` / `mcp_approval_request` वस्तुको रूपमा सतहमा ल्याउँछ, र ग्राहकहरू मिल्दोजुल्दो `function_call_output` / `mcp_approval_response` सँग पुन: सुरु गर्छन्।
- **फाउन्ड्रीमा परिनियोजन**: Azure Developer CLI प्रयोग गर्नुहोस् — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (स्थानीय, Docker आवश्यक), त्यसपछि `azd provision` र `azd deploy`। होस्ट गरिएको एजेन्ट परिनियोजनका लागि **Foundry Project Manager** भूमिका आवश्यक छ।

यस उदाहरणको चल्न योग्य संस्करण [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) मा छ। पूर्ण मार्गदर्शन (Invocations प्रोटोकल, कस्टम अनुरोध_SCHEMAहरू, र समस्यासंग समाधान) का लागि, [Foundry होस्ट गरिएको एजेन्टहरूका रूपमा LangGraph एजेन्टहरू होस्ट गर्नुहोस्](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) हेर्नुहोस्।

## कोड नमूना

माइक्रोसफ्ट एजेन्ट फ्रेमवर्कका कोड नमूनाहरू यस रिपोजिटरीमा `xx-python-agent-framework` र `xx-dotnet-agent-framework` फाइलहरूमा फेला पार्न सकिन्छ।

## माइक्रोसफ्ट एजेन्ट फ्रेमवर्क बारे थप प्रश्नहरू छन्?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) मा सामेल हुनुहोस् जहाँ अन्य सिक्नेहरूसँग भेटघाट गर्न, अफिस आवरहरूमा भाग लिन र तपाईंका AI एजेन्ट सम्बन्धी प्रश्नहरू समाधान गर्न सक्नुहुन्छ।
## अघिल्लो पाठ

[AI एजेन्टहरूको लागि मेमोरी](../13-agent-memory/README.md)

## अर्को पाठ


[कम्प्युटर प्रयोग गर्ने एजेन्टहरू (CUA) बनाउँदै](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->