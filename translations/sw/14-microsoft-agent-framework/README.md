# Kuchunguza Mfumo wa Wakala wa Microsoft

![Agent Framework](../../../translated_images/sw/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Utangulizi

Somo hili litajumuisha:

- Kuelewa Mfumo wa Wakala wa Microsoft: Vipengele Muhimu na Thamani  
- Kuchunguza Dhana Muhimu za Mfumo wa Wakala wa Microsoft
- Mifumo ya Juu ya MAF: Mitiririko ya Kazi, Middleware, na Kumbukumbu

## Malengo ya Kujifunza

Baada ya kumaliza somo hili, utajua jinsi ya:

- Kujenga Wakala wa AI Tayari kwa Uzalishaji kwa kutumia Mfumo wa Wakala wa Microsoft
- Kutumia vipengele vya msingi vya Mfumo wa Wakala wa Microsoft kwa Matukio yako ya Matumizi ya Wakala
- Kutumia mifumo ya juu ikiwa ni pamoja na mitiririko ya kazi, middleware, na ufuatiliaji

## Sampuli za Msimbo

Sampuli za msimbo za [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) zinaweza kupatikana kwenye hifadhi hii chini ya faili za `xx-python-agent-framework` na `xx-dotnet-agent-framework`.

## Kuelewa Mfumo wa Wakala wa Microsoft

![Framework Intro](../../../translated_images/sw/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) ni mfumo wa muungano wa Microsoft kwa ajili ya kujenga mawakala wa AI. Inatoa urahisi wa kushughulikia aina mbalimbali za matukio ya matumizi ya wakala yanayoonekana katika mazingira ya uzalishaji na utafiti ikijumuisha:

- **Mwongozo wa mfululizo wa Wakala** katika hali ambapo mitiririko ya hatua kwa hatua inahitajika.
- **Mwongozo wa sambamba** katika hali ambapo mawakala wanahitaji kukamilisha kazi kwa wakati mmoja.
- **Mwongozo wa mazungumzo ya kikundi** katika hali ambapo mawakala wanaweza kushirikiana pamoja kwenye kazi moja.
- **Mwongozo wa Kuhamisha Kazi** katika hali ambapo mawakala wanapiga kazi kwa mchakato wa kupita kabisa kama kazi ndogo zinavyokamilika.
- **Mwongozo wa Kuingilia kwa Muhariri** katika hali ambapo wakala msimamizi anaunda na kubadilisha orodha ya kazi na kushughulikia ushirikiano wa mawakala kidogo kukamilisha kazi.

Ili kuwasilisha Wakala wa AI katika Uzalishaji, MAF pia ina vipengele vya:

- **Ufuatiliaji** kupitia matumizi ya OpenTelemetry ambapo kila hatua ya Wakala wa AI ikiwa ni pamoja na kuiita zana, hatua za mwongozo, mtiririko wa hoja na ufuatiliaji wa utendaji kupitia dashibodi za Microsoft Foundry.
- **Usalama** kwa kuwa mawakala wanahudumiwa moja kwa moja kwenye Microsoft Foundry ambayo inajumuisha controls za usalama kama upatikanaji wa kulingana na nafasi, usimamizi wa data binafsi na usalama wa maudhui uliomjengewa ndani.
- **Uthabiti** kama vijenzi vya Wakala na mitiririko ya kazi vinaweza kusitishwa, kuendelea na kurejeshwa kutokana na makosa yanayowezesha mchakato wa muda mrefu.
- **Udhibiti** kama mitiririko ya kazi ya mwanadamu ndani ya mzunguko inasaidiwa ambapo kazi zinatambulika kama zinahitaji idhini ya binadamu.

Mfumo wa Wakala wa Microsoft pia unazingatia ushirikiano kwa:

- **Kutokuwa tegemezi wa wingu moja** - Mawakala wanaweza kuendesha kwenye kontena, maeneo ya ndani na katika mawingu mbalimbali.
- **Kutokuwa tegemezi wa mtoa huduma** - Mawakala yanaweza kuundwa kupitia SDK unayopendelea ikiwa ni pamoja na Azure OpenAI na OpenAI
- **Kuunganisha Viwango Huru** - Mawakala yanaweza kutumia itifaki kama Agent-to-Agent (A2A) na Model Context Protocol (MCP) kugundua na kutumia mawakala na zana nyingine.
- **Viongezi na Vionganisho** - Uunganisho unaweza kufanywa kwa huduma za data na kumbukumbu kama Microsoft Fabric, SharePoint, Pinecone na Qdrant.

Tuchunguze jinsi vipengele hivi vinavyotumika kwa baadhi ya dhana muhimu za Mfumo wa Wakala wa Microsoft.

## Dhana Muhimu za Mfumo wa Wakala wa Microsoft

### Mawakala

![Agent Framework](../../../translated_images/sw/agent-components.410a06daf87b4fef.webp)

**Kuunda Mawakala**

Uundaji wa wakala hufanywa kwa kufafanua huduma ya ubashiri (Mtoa Huduma wa LLM), seti ya maelekezo kwa Wakala wa AI kufuata, na jina lililopewa `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Juu inatumia `Azure OpenAI` lakini mawakala wanaweza kuundwa kwa kutumia huduma mbalimbali ikiwa ni pamoja na `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, API za `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

au mawakala wa mbali kwa kutumia itifaki ya A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Kuendesha Mawakala**

Mawakala huendeshwa kwa kutumia mbinu `.run` au `.run_stream` kwa majibu yasiyo ya mfululizo au ya mfululizo.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Kila kuendesha wakala kunaweza pia kuwa na chaguzi za kubinafsisha vigezo kama `max_tokens` kinachotumika na wakala, `tools` ambazo wakala anaweza kuziita, na hata `model` yenyewe inayotumiwa kwa wakala.

Hii ni muhimu katika kesi ambapo mifano maalum au zana zinahitajika kukamilisha kazi ya mtumiaji.

**Zana**

Zana zinaweza kufafanuliwa wakati wa kufafanua wakala:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Wakati wa kuunda ChatAgent moja kwa moja

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

na pia wakati wa kuendesha wakala:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Chombo kilichotolewa kwa ajili ya mzunguko huu tu )
```

**Mishale ya Wakala**

Mishale ya Wakala hutumika kushughulikia mazungumzo ya mzunguko wa kadhaa. Mishale inaweza kuundwa kwa:

- Kutumia `get_new_thread()` ambayo inaruhusu mishale kuhifadhiwa kwa muda mrefu
- Kuunda mshale moja kwa moja wakati wa kuendesha wakala na mshale huo kudumu tu wakati wa kuendesha kwa sasa.

Kuunda mshale, msimbo unaonekana hivi:

```python
# Unda mfululizo mpya.
thread = agent.get_new_thread() # Endesha wakala na mfululizo huo.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Baadaye unaweza kusimamia mshale kuhifadhiwa kwa matumizi ya baadaye:

```python
# Unda thread mpya.
thread = agent.get_new_thread() 

# Endesha wakala pamoja na thread.

response = await agent.run("Hello, how are you?", thread=thread) 

# Fanyia serialization thread kwa ajili ya kuhifadhi.

serialized_thread = await thread.serialize() 

# Fanyia deserialization hali ya thread baada ya kupakia kutoka kuhifadhi.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware ya Wakala**

Mawakala hutoa mawasiliano na zana na LLM ili kukamilisha kazi za watumiaji. Katika hali zingine, tunataka kutekeleza au kufuatilia kati ya maingiliano haya. Middleware ya wakala inatuwezesha kufanya hivi kupitia:

*Middleware ya Kazi*

Middleware hii inatuwezesha kutekeleza hatua kati ya wakala na kazi/zaana inayoitwa. Mfano wa matumizi ni pale ambapo unaweza kutaka kufanya uandikishaji wa wito wa kazi.

Katika msimbo hapa chini `next` inaelezea kama middleware inayofuata au kazi halisi inapaswa kuitwa.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Uandaji wa awali: Ingia kumbukumbu kabla ya utekelezaji wa kazi
    print(f"[Function] Calling {context.function.name}")

    # Endelea kwa middleware inayofuata au utekelezaji wa kazi
    await next(context)

    # Uandaaji wa baadae: Ingia kumbukumbu baada ya utekelezaji wa kazi
    print(f"[Function] {context.function.name} completed")
```

*Middleware ya Mazungumzo*

Middleware hii inatuwezesha kutekeleza au kuandika hatua kati ya wakala na maombi kati ya LLM.

Hii ina taarifa muhimu kama vile `messages` zinazopeleka kwa huduma ya AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Usindikaji wa awali: Andika kipindi cha kabla ya simu ya AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Endelea kwa middleware inayofuata au huduma ya AI
    await next(context)

    # Usindikaji wa baada: Andika baada ya jibu la AI
    print("[Chat] AI response received")

```

**Kumbukumbu ya Wakala**

Kama ilivyofadhiliwa katika somo la `Kumbukumbu ya Wakala`, kumbukumbu ni kipengele muhimu kuwezesha wakala kufanya kazi katika muktadha tofauti. MAF inatoa aina mbalimbali za kumbukumbu:

*Hifadhi ya Kumbukumbu Ndani*

Hii ni kumbukumbu inayohifadhiwa katika mishale wakati wa utekelezaji wa programu.

```python
# Unda thread mpya.
thread = agent.get_new_thread() # Endesha wakala kwa thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Ujumbe Endelevu*

Kumbukumbu hii hutumika kuhifadhi historia ya mazungumzo kati ya vikao tofauti. Huainishwa kwa kutumia `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Unda hifadhi ya ujumbe maalum
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Kumbukumbu Inayobadilika*

Kumbukumbu hii huongezwa kwa muktadha kabla mawakala kuendeshwa. Kumbukumbu hizi zinaweza kuhifadhiwa katika huduma za nje kama mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Kutumia Mem0 kwa uwezo wa kumbukumbu wa hali ya juu
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

**Ufuatiliaji wa Wakala**

Ufuatiliaji ni muhimu kwa kujenga mifumo ya wakala inayotegemeka na inayoweza kudumishwa. MAF inaunganisha na OpenTelemetry kutoa ufuatiliaji na vipimo bora vya msingi.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # fanya jambo
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Mitiririko ya Kazi

MAF hutoa mitiririko ya kazi ambayo ni hatua zilizobainishwa awali za kukamilisha kazi na kuingiza mawakala wa AI kama vipengele katika hatua hizo.

Mitiririko ya kazi inaundwa na vipengele tofauti vinavyoruhusu kudhibiti mtiririko bora. Mitiririko ya kazi pia inaruhusu **mwelekeo wa mawakala wengi** na **kuhifadhi hali** ili kuhifadhi hali za mitiririko ya kazi.

Vipengele vya msingi vya mtiririko wa kazi ni:

**Watendaji**

Watendaji hupokea ujumbe wa kuingiza, kutekeleza kazi zao zilizopewa, na kisha kutoa ujumbe wa matokeo. Hii husogeza mtiririko wa kazi kuelekea kukamilisha kazi kubwa. Watendaji wanaweza kuwa wakala wa AI au mantiki maalum.

**Mikondo**

Mikondo hutumika kufafanua mtiririko wa ujumbe katika mtiririko wa kazi. Hii inaweza kuwa:

*Mikondo ya Moja kwa Moja* - Muunganisho rahisi ya mmoja kwa mmoja kati ya watendaji:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Mikondo ya Masharti* - Huamsha baada ya sharti fulani kutimizwa. Kwa mfano, wakati vyumba vya hoteli havipatikani, mtendaji anaweza kupendekeza chaguzi nyingine.

*Mikondo ya Switch-case* - Ruta ujumbe kwa watendaji tofauti kulingana na masharti yaliyowekwa. Kwa mfano, ikiwa mteja wa kusafiri ana upatikanaji wa kipaumbele na kazi zao zitatatuliwa kupitia mtiririko wa kazi mwingine.

*Mikondo ya Fan-out* - Tuma ujumbe mmoja kwa malengo mengi.

*Mikondo ya Fan-in* - Kusanya ujumbe mwingi kutoka kwa watendaji tofauti na utume kwa lengo moja.

**Matukio**

Ili kutoa ufuatiliaji bora katika mitiririko ya kazi, MAF hutoa matukio yaliyojengwa ya utekelezaji ikiwa ni pamoja na:

- `WorkflowStartedEvent`  - Utekelezaji wa mtiririko wa kazi unaanza
- `WorkflowOutputEvent` - Mtiririko wa kazi hutengeneza matokeo
- `WorkflowErrorEvent` - Mtiririko wa kazi unakumbana na kosa
- `ExecutorInvokeEvent`  - Mtendaji anaanza utekelezaji
- `ExecutorCompleteEvent`  -  Mtendaji anamaliza utekelezaji
- `RequestInfoEvent` - Ombi limefanywa

## Mifumo ya Juu ya MAF

Sehemu zilizo juu zinashughulikia dhana muhimu za Mfumo wa Wakala wa Microsoft. Unapoendelea kujenga mawakala tata, hapa kuna mifumo ya hali ya juu ya kuzingatia:

- **Muungano wa Middleware**: Fuata mfululizo wa wasimamizi wa middleware wengi (kama uandikishaji, uthibitishaji, ukomo wa viwango) kutumia middleware ya kazi na mazungumzo kwa udhibiti wa kina wa tabia ya wakala.
- **Uhifadhi wa Checkpoint wa Mitiririko ya Kazi**: Tumia matukio ya mitiririko ya kazi na serialization kuhifadhi na kuendelea na michakato ya wakala yenye muda mrefu.
- **Uchaguzi wa Zana Zinazobadilika**: Changanya RAG juu ya maelezo ya zana na usajili wa zana wa MAF ili kuonyesha zana zinazofaa tu kwa kila swali.
- **Uhamisho wa Wakala Wengi**: Tumia mikondo ya mitiririko ya kazi na ruta za masharti kuongoza uhamisho kati ya mawakala maalum.

## Sampuli za Msimbo

Sampuli za msimbo za Mfumo wa Wakala wa Microsoft zinaweza kupatikana kwenye hifadhi hii chini ya faili za `xx-python-agent-framework` na `xx-dotnet-agent-framework`.

## Una Maswali Zaidi Kuhusu Mfumo wa Wakala wa Microsoft?

Jiunge na [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) kukutana na wanafunzi wengine, kuhudhuria saa za ofisi na kupata majibu ya maswali yako kuhusu Wakala wa AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kivunjifu cha Dhamana**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kufikia usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kasoro. Hati asilia katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatubebei jukumu lolote kwa kutokuelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->