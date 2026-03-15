# Microsoft Agent Framework अन्वेषण गर्दै

![Agent Framework](../../../translated_images/ne/lesson-14-thumbnail.90df0065b9d234ee.webp)

### परिचय

यस पाठले समेट्नेछ:

- Microsoft Agent Framework को समझ: मुख्य विशेषताहरू र मूल्य  
- Microsoft Agent Framework का मुख्य अवधारणाहरू अन्वेषण गर्दै
- उन्नत MAF ढाँचाहरू: कार्यप्रवाह, मिडलवेयर, र स्मृति

## सिकाइ लक्ष्यहरू

यस पाठ पूरा गरेपछि, तपाईं जान्नुहुनेछ:

- Microsoft Agent Framework प्रयोग गरेर उत्पादन-तयार AI एजेन्टहरू बनाउने
- Microsoft Agent Framework का मूल सुविधाहरूलाई तपाईंको एजेन्टिक प्रयोग मामिलाहरूमा लागू गर्ने
- उन्नत ढाँचाहरू प्रयोग गर्ने जसमा कार्यप्रवाह, मिडलवेयर, र अवलोकनशक्ति छन्

## कोड नमूनाहरू 

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) का कोड नमूनाहरू यस भण्डारमा `xx-python-agent-framework` र `xx-dotnet-agent-framework` फाइलहरू अन्तर्गत फेला पार्न सकिन्छ।

## Microsoft Agent Framework को समझ

![Framework Intro](../../../translated_images/ne/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) माइक्रोसफ्टको एकीकृत फ्रेमवर्क हो AI एजेन्टहरू निर्माण गर्नको लागि। यसले उत्पादन र अनुसन्धान वातावरणहरूमा देखिएका विभिन्न प्रकारका एजेन्टिक प्रयोग मामिलाहरू समाधान गर्न लचिलोपन प्रदान गर्दछ, जस्तै:

- **क्रमिक एजेन्ट संयोजन** जहाँ चरण-द्वारा-चरण कार्यप्रवाहहरू आवश्यक पर्छन्।
- **समवर्ती संयोजन** जहाँ एजेन्टहरूले एउटै समयमा कार्य सम्पन्न गर्नुपर्छ।
- **समूह च्याट संयोजन** जहाँ एजेन्टहरूले एउटै कार्यमा सहकार्य गर्न सक्छन्।
- **ह्यान्डअफ संयोजन** जहाँ एजेन्टहरूले उपकार्यहरू सम्पन्न हुँदै गर्दा कार्य एकअर्कालाई हस्तान्तरण गर्छन्।
- **चुम्बकीय संयोजन** जहाँ प्रबन्धक एजेन्टले कार्य सूची सिर्जना र परिमार्जन गर्छ र उपएजेन्टहरूलाई समन्वय गर्छ।

AI एजेन्टहरू उत्पादनमा वितरण गर्न, MAF ले यसका लागि समावेश गरेको छ:

- **अवलोकनशक्ति**: OpenTelemetry मार्फत जहाँ AI एजेन्टका प्रत्येक क्रियाकलापहरू, उपकरण आह्वान, संयोजन चरणहरू, तार्किक प्रवाहहरू र प्रदर्शन नियन्त्रण Microsoft Foundry ड्यासबोर्डमार्फत नियाल्न सकिन्छ।
- **सुरक्षा**: एजेन्टहरू Microsoft Foundry मा स्वदेशी रूपमा होस्ट गरिन्छ, जसमा भूमिका आधारित पहुँच, निजी डेटा ह्यान्डलिङ्ग र सामग्री सुरक्षा नियंत्रणहरू समावेश छन्।
- **दृढता**: एजेन्ट थ्रेडहरू र कार्यप्रवाहहरूलाई रोक्न, पुनः सुरु गर्न र त्रुटिबाट पुनः प्राप्त गर्न मिल्छ, जसले लामो समयसम्म चल्ने प्रक्रिया सक्षम बनाउँछ।
- **नियन्त्रण**: मानव इन द लूप कार्यप्रवाहहरू समर्थन गरिन्छ जहाँ कार्यहरूलाई मानवीय स्वीकृतिको आवश्यक पर्ने रूपमा चिन्हित गरिन्छ।

Microsoft Agent Framework पनि अन्तर सञ्चालनशील हुन केन्द्रित छ:

- **क्लाउड-निर्पेक्ष** - एजेन्टहरू कन्टेनरहरूमा, सञ्चालन स्थलमा र विभिन्न क्लाउडहरूमा चल्न सक्छन्।
- **प्रदायक-निर्पेक्ष** - एजेन्टहरू तपाईंसँग मनपर्ने SDK मार्फत सिर्जना गर्न सकिन्छ, जस्तै Azure OpenAI र OpenAI।
- **खुला मानकहरू एकीकृत गर्दै** - एजेन्टहरूले Agent-to-Agent (A2A) र Model Context Protocol (MCP) जस्ता प्रोटोकलहरू उपयोग गरी अरू एजेन्ट र उपकरणहरू पत्ता लगाउन र प्रयोग गर्न सक्छन्।
- **प्लगइन र कनेक्टर्स** - Microsoft Fabric, SharePoint, Pinecone र Qdrant जस्ता डेटा र स्मृति सेवाहरूमा जडान गर्न सकिन्छ।

अब हेर्नुहोस् यी सुविधाहरू Microsoft Agent Framework का केहि मूल अवधारणाहरूमा कसरी प्रयोग गरिन्छ।

## Microsoft Agent Framework का मुख्य अवधारणाहरू

### एजेन्टहरू

![Agent Framework](../../../translated_images/ne/agent-components.410a06daf87b4fef.webp)

**एजेन्टहरू सिर्जना गर्दै**

एजेन्ट सिर्जना गर्ने प्रक्रिया अन्तर्गत inference सेवा (LLM प्रदायक), AI एजेन्टले पालना गर्नुपर्ने निर्देशनहरूको सेट, र नाम `name` निर्दिष्ट गरिन्छ:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

माथिको उदारहणमा `Azure OpenAI` प्रयोग भइरहेको छ तर एजेन्टहरू `Microsoft Foundry Agent Service` लगायत विभिन्न सेवाहरू प्रयोग गरेर पनि बनाउन सकिन्छ:

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

वा A2A प्रोटोकल प्रयोग गरी रिमोट एजेन्टहरू:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**एजेन्टहरू चलाउँदै**

एजेन्टहरू `.run` वा `.run_stream` विधिहरू प्रयोग गरी नन-स्ट्रीमिङ वा स्ट्रीमिङ प्रतिक्रियाहरूका लागि चलाइन्छ।

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

हरेक एजेन्ट चलाउँदा एजेन्टले प्रयोग गर्ने `max_tokens`, एजेन्टले कल गर्नसक्ने `tools`, र एजेन्टले प्रयोग गर्ने `model` जस्ता प्यारामिटरहरू अनुकूलन विकल्प हुन्छ।

यो विशेष मोडेलहरू वा उपकरणहरू कुनै प्रयोगकर्ताको कार्य पूरा गर्न आवश्यक पर्ने अवस्थामा उपयोगी हुन्छ।

**उपकरणहरू**

उपकरणहरू एजेन्ट परिभाषा गर्दा र एजेन्ट चलाउँदा दुवै समयमा परिभाषित गर्न सकिन्छ:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# सीधा रूपमा ChatAgent सिर्जना गर्दा

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # यो रनका लागि मात्र प्रदान गरिएको उपकरण )
```

**एजेन्ट थ्रेडहरू**

एजेन्ट थ्रेडहरू बहु-चरण संवाद ह्यान्डल गर्न प्रयोग गरिन्छ। थ्रेडहरू दुई तरिकाले बनाउन सकिन्छ:

- `get_new_thread()` प्रयोग गरेर, जसले थ्रेडलाई समयसँग बचत गर्न सक्षम बनाउँछ
- एजेन्ट चलाउँदा स्वतः थ्रेड सिर्जना गरी हालको चलाइमा मात्र थ्रेड टिकाइराख्ने

थ्रेड बनाउने कोड यस प्रकार देखिन्छ:

```python
# नयाँ थ्रेड सिर्जना गर्नुहोस्।
thread = agent.get_new_thread() # थ्रेडसँग एजेन्ट चलाउनुहोस्।
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

थ्रेडलाई पछि प्रयोग गर्न स्तरीकरण (serialize) गर्न सकिन्छ:

```python
# नयाँ थ्रेड सिर्जना गर्नुहोस्।
thread = agent.get_new_thread() 

# एजेन्टलाई थ्रेडसँग चलाउनुहोस्।

response = await agent.run("Hello, how are you?", thread=thread) 

# भण्डारणको लागि थ्रेडलाई सिरियलाइज गर्नुहोस्।

serialized_thread = await thread.serialize() 

# भण्डारणबाट लोड गरेपछि थ्रेडको अवस्था डिसिरियलाइज गर्नुहोस्।

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**एजेन्ट मिडलवेयर**

एजेन्टहरू उपकरण र LLM सँग अन्तरक्रिया गरेर प्रयोगकर्ताका कार्यहरू पूरा गर्छन्। केही अवस्थामा, यी अन्तरक्रियाहरूको बीचमा कार्यान्वयन वा ट्र्याकिङ गर्न चाहन्छौं। एजेन्ट मिडलवेयरले हामीलाई यस काम गर्न मद्दत गर्दछ:

*कार्य मिडलवेयर*

यो मिडलवेयरले एजेन्ट र कल गर्न लागेको कार्य/उपकरण बीच क्रिया सञ्चालन गर्न अनुमति दिन्छ। जस्तै, कार्य आह्वानमा लगिङ गर्न चाहिएको अवस्थामा।

नीचेको कोडमा `next` ले परिभाषित गर्छ कि अर्को मिडलवेयर हो या वास्तविक कार्य कल गरिनेछ।

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # पूर्व-प्रक्रिया: कार्यसम्पादन अघि लग इन गर्नुहोस्
    print(f"[Function] Calling {context.function.name}")

    # अर्को मिडलवेयर वा कार्यसम्पादनमा जारी राख्नुहोस्
    await next(context)

    # पोस्ट-प्रक्रिया: कार्यसम्पादन पछि लग इन गर्नुहोस्
    print(f"[Function] {context.function.name} completed")
```

*च्याट मिडलवेयर*

यो मिडलवेयरले एजेन्ट र LLM का अनुरोधहरू बीच क्रियापालन वा लगिङ गर्न अनुमति दिन्छ।

यसले AI सेवामा पठाइएका `messages` जस्ता महत्वपूर्ण जानकारी समावेश गर्दछ।

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # पूर्व-प्रक्रिया: AI कल अघि लग
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # अर्को मिडलवेयर वा AI सेवामा जारी राख्नुहोस्
    await next(context)

    # पश्च-प्रक्रिया: AI प्रतिक्रिया पछि लग गर्नुहोस्
    print("[Chat] AI response received")

```

**एजेन्ट स्मृति**

`Agentic Memory` पाठमा वर्णन गरिए अनुसार, स्मृति एजेन्टलाई विभिन्न सन्दर्भहरूमा सञ्चालन गर्न महत्त्वपूर्ण हुन्छ। MAF ले विभिन्न प्रकारका स्मृतिहरू प्रदान गर्दछ:

*इन-मेमोरी स्टोरेज*

यो स्मृति एप्लिकेशन रनटाइम अवधिमा थ्रेडहरूमा राखिन्छ।

```python
# नयाँ थ्रेड सिर्जना गर्नुहोस्।
thread = agent.get_new_thread() # थ्रेडसँग एजेन्ट चलाउनुहोस्।
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*लगातार सन्देशहरू (Persistent Messages)*

यो स्मृति विभिन्न सत्रहरूमा संवाद इतिहास भण्डारण गर्न प्रयोग हुन्छ। यसलाई `chat_message_store_factory` प्रयोग गरी परिभाषित गरिन्छ:

```python
from agent_framework import ChatMessageStore

# अनुकूल सन्देश भण्डार सिर्जना गर्नुहोस्
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*डायनामिक स्मृति*

यो स्मृति एजेन्टहरू चलाउनु अघि सन्दर्भमा थपिन्छ। यी स्मृतिहरू बाह्य सेवाहरूमा जस्तै mem0 मा संग्रहित गर्न सकिन्छ:

```python
from agent_framework.mem0 import Mem0Provider

# उन्नत मेमोरी क्षमताहरूको लागि Mem0 को प्रयोग गर्दै
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

**एजेन्ट अवलोकनशक्ति**

अवलोकनशक्ति भरपर्दो र कायम गर्न सकिने एजेन्ट प्रणाली निर्माणमा महत्त्वपूर्ण छ। MAF ले ट्रेसिङ र मिटरहरू उपलब्ध गराउन OpenTelemetryसँग एकीकरण गरेको छ।

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

MAF ले पूर्वनिर्धारित चरणहरू सहितको कार्यप्रवाहहरूसँग कार्य पूरा गर्न सहयोग गर्दछ जसमा AI एजेन्टहरू कम्पोनेन्टका रूपमा समावेश छन्।

कार्यप्रवाहहरूमा विभिन्न कम्पोनेन्टहरू हुन्छन् जुन राम्रो नियन्त्रण प्रवाह सुनिश्चित गर्दछ। कार्यप्रवाहहरूले **बहु-एजेन्ट संयोजन** र **चेकपॉइन्टिङ** पनि सक्षम पार्छन् जसले कार्यप्रवाहको अवस्था सुरक्षित राख्छ।

कार्यप्रवाहका मूल कम्पोनेन्टहरू हुन्:

**कार्यकारीहरू (Executors)**

कार्यकारीहरूले इनपुट सन्देशहरू प्राप्त गर्छन्, कार्य सम्पन्न गर्छन् र परिणाम सन्देश उत्पादन गर्छन्। यसले कार्यप्रवाहलाई ठूलो लक्ष्यतर्फ अगाडि बढाउँछ। कार्यकारीहरू AI एजेन्ट वा अनुकूलित तर्क हुन सक्छन्।

**एजहरू (Edges)**

एजहरू कार्यप्रवाहमा सन्देशहरूको प्रवाह परिभाषित गर्न प्रयोग हुन्छन्। ती निम्न अवस्थामा हुन सक्छन्:

*प्रत्यक्ष एजहरू* - कार्यकारीहरू बीच सरल एक-देखि-एक जडान:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*सशर्त एजहरू* - कुनै सर्त पूरा भएपछि सक्रिय। जस्तै, होटल कोठा उपलब्ध नभएमा, कार्यकारीले अन्य विकल्प सुझाउन सक्छ।

*स्विच-केस एजहरू* - परिभाषित सर्तहरूका आधारमा अलग कार्यकारीहरूमा सन्देशहरू मार्गनिर्देशन गर्छ। जस्तै, यात्रु ग्राहकसँग प्राथमिक पहुँच छ भने उनको कार्य अर्को कार्यप्रवाहमार्फत ह्यान्डल हुनेछ।

*फ्यान-आउट एजहरू* - एउटै सन्देशलाई धेरै लक्ष्यहरूमा पठाउँछन्।

*फ्यान-इन एजहरू* - विभिन्न कार्यकारीहरूबाट अनेक सन्देश सङ्कलन गरी एउटै लक्ष्यमा पठाउँछन्।

**घटनाहरू**

कार्यप्रवाहहरूको राम्रो अवलोकनशक्तिका लागि, MAF ले कार्यान्वयनका लागि निम्न घटनाहरू सिर्जना गर्छ:

- `WorkflowStartedEvent` - कार्यप्रवाह सुरु भयो
- `WorkflowOutputEvent` - कार्यप्रवाहले परिणाम उत्पादन गर्यो
- `WorkflowErrorEvent` - कार्यप्रवाहमा त्रुटि आयो
- `ExecutorInvokeEvent` - कार्यकारीले प्रोसेसिंग सुरु गर्यो
- `ExecutorCompleteEvent` - कार्यकारीले प्रोसेसिंग सम्पन्न गर्यो
- `RequestInfoEvent` - अनुरोध जारी गरियो

## उन्नत MAF ढाँचाहरू

माथिका खण्डहरूले Microsoft Agent Framework का मुख्य अवधारणाहरू समेट्छन्। अझ जटिल एजेन्टहरू बनाउँदै जाँदा यहाँ केही उन्नत ढाँचाहरू छन् जसलाई विचार गर्न सकिन्छ:

- **मिडलवेयर संयोजन**: कार्य र च्याट मिडलवेयर प्रयोग गरी लगिङ, प्रमाणीकरण, दर-सीमा नियन्त्रण जस्ता बहु मिडलवेयर ह्यान्डलरहरू चेन गरेर एजेन्ट व्यवहारमा सूक्ष्म नियन्त्रण पाउन।
- **कार्यप्रवाह चेकपॉइन्टिङ**: कार्यप्रवाह घटनाहरू र स्तरीकरण प्रयोग गरी लामो समयसम्म चल्ने एजेन्ट प्रक्रियाहरू सुरक्षित गर्ने र पुनः सुरु गर्ने।
- **डायनामिक उपकरण चयन**: उपकरण विवरणहरूमा RAG संयोजन गरी MAF को उपकरण दर्तासँग संयुक्त गरेर प्रत्येक प्रश्नका लागि मात्र सान्दर्भिक उपकरणहरू प्रस्तुत गर्ने।
- **बहु-एजेन्ट ह्यान्डअफ**: कार्यप्रवाह एजहरू र सशर्त मार्गनिर्देशन प्रयोग गरेर विशेषज्ञ एजेन्टहरूबीच ह्यान्डअफ संयोजन गर्ने।

## कोड नमूनाहरू 

Microsoft Agent Framework का कोड नमूनाहरू यस भण्डारमा `xx-python-agent-framework` र `xx-dotnet-agent-framework` फाइलहरूमा फेला पार्न सकिन्छ।

## Microsoft Agent Framework सम्बन्धी थप प्रश्नहरू छन्?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) मा सामेल हुनुहोस् अरू सिक्नेहरूसँग भेट्न, अफिस आवरहरूमा सहभागी हुन र तपाईंका AI एजेन्ट प्रश्नहरू समाधान गर्न।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यस दस्तावेजलाई AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) मार्फत अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं भने पनि, कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मातृ भाषामा नै अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट सृजित कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार हुन सक्दैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->