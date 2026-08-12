# Kuchunguza Mfumo wa Wakala wa Microsoft

![Agent Framework](../../../translated_images/sw/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Utangulizi

Somo hili litashughulikia:

- Kuelewa Mfumo wa Wakala wa Microsoft: Vipengele Muhimu na Thamani  
- Kuchunguza Dhana Muhimu za Mfumo wa Wakala wa Microsoft
- Mifumo ya Juu ya MAF: Mifumo ya Kazi, Middleware, na Kumbukumbu

## Malengo ya Kujifunza

Baada ya kumaliza somo hili, utajua jinsi ya:

- Kuunda Wakala wa AI Tayari kwa Uzalishaji kwa kutumia Mfumo wa Wakala wa Microsoft
- Kutumia vipengele muhimu vya Mfumo wa Wakala wa Microsoft kwa Matumizi yako ya Wakala
- Kutumia mifumo ya juu ikijumuisha mifumo ya kazi, middleware, na uangalizi

## Sampuli za Msimbo 

Sampuli za msimbo kwa [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) zinaweza kupatikana katika hifadhidata hii chini ya faili za `xx-python-agent-framework` na `xx-dotnet-agent-framework`.

## Kuelewa Mfumo wa Wakala wa Microsoft

![Framework Intro](../../../translated_images/sw/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) ni mfumo uliounganishwa wa Microsoft wa kujenga mawakala wa AI. Unatoa uwezo wa kushughulikia aina mbalimbali za matumizi ya wakala yanayoonekana katika mazingira ya uzalishaji na utafiti ikiwa ni pamoja na:

- **Mpangilio wa Wakala mfululizo** katika hali ambapo mchakato wa hatua kwa hatua unahitajika.
- **Mpangilio wa Wakala kwa wakati mmoja** katika hali ambapo mawakala wanahitaji kukamilisha kazi kwa wakati mmoja.
- **Mpangilio wa Gumzo la Kikundi** katika hali ambapo mawakala wanaweza kushirikiana kwenye kazi moja.
- **Mpangilio wa Kuwahamisha Wakala** katika hali ambapo mawakala wanapakia kazi kwa mwingine wakati kazi ndogo zinakamilika.
- **Mpangilio wa Sumaku** katika hali ambapo wakala msimamizi huunda na kubadilisha orodha ya kazi na kushughulikia uratibu wa mawakala wadogo kumaliza kazi.

Ili kutoa Wakala wa AI katika Uzalishaji, MAF pia ina vipengele vya:

- **Uangalizi** kupitia matumizi ya OpenTelemetry ambapo kila hatua ya Wakala wa AI ikiwa ni pamoja na kuitishwa kwa zana, hatua za mpangilio, mifereji ya reasoning na ufuatiliaji wa utendaji kupitia dashibodi za Microsoft Foundry.
- **Usalama** kwa kuwa mwenyeji wa mawakala moja kwa moja kwenye Microsoft Foundry ambayo ina udhibiti wa usalama kama upatikanaji wa jukumu, usimamizi wa data binafsi na usalama wa maudhui uliojengewa ndani.
- **Uhimilivu** kwani nyuzi za Wakala na mifumo ya kazi zinaweza kusimamishwa, kuendelea na kupona kutoka kwa makosa ambayo huwezesha mchakato wa muda mrefu.
- **Udhibiti** kwani mifumo ya kazi yenye mpangilio wa binadamu inasaidiwa ambapo kazi zinatambulika kuwa zinahitaji idhini ya binadamu.

Mfumo wa Wakala wa Microsoft pia unaangazia uwezo wa kuingiliana kwa:

- **Kutoegemea Wingu** - Mawakala yanaweza kuendesha ndani ya kontena, mahali pa kazi na katika mawingu mbalimbali.
- **Kutoegemea Mtoaji** - Mawakala yanaweza kuundwa kupitia SDK unayopendelea ikijumuisha Azure OpenAI na OpenAI
- **Kuingiza Viwango Wazi** - Mawakala yanaweza kutumia itifaki kama Agent-to-Agent(A2A) na Model Context Protocol (MCP) kugundua na kutumia mawakala wengine na zana.
- **Viendelezi na Viunganishaji** - Uunganisho unaweza kufanyika kwa huduma za data na kumbukumbu kama Microsoft Fabric, SharePoint, Pinecone na Qdrant.

Hebu tuchunguze jinsi vipengele hivi vinavyotumika kwa baadhi ya dhana kuu za Mfumo wa Wakala wa Microsoft.

## Dhana Muhimu za Mfumo wa Wakala wa Microsoft

### Mawakala

![Agent Framework](../../../translated_images/sw/agent-components.410a06daf87b4fef.webp)

**Kuumba Mawakala**

Uundaji wa wakala hufanywa kwa kufafanua huduma ya inference (Mtoaji wa LLM), seti ya maagizo kwa Wakala wa AI kufuata, na `jina` lililowekwa:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Hapo juu inatumia `Azure OpenAI` lakini mawakala yanaweza kuundwa kwa kutumia aina mbalimbali za huduma ikiwemo `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Majibu`, API za `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

au [MiniMax](https://platform.minimaxi.com/), inayotoa API inayolingana na OpenAI yenye dirisha kubwa la muktadha (hadi vitokezo 204K):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

au mawakala wa mbali kwa kutumia itifaki ya A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Kuendesha Mawakala**

Mawakala huendeshwa kwa kutumia njia za `.run` au `.run_stream` kwa majibu yasiyo ya mtiririko au ya mtiririko.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Kila uendeshaji wa wakala pia unaweza kuwa na chaguzi za kubinafsisha vigezo kama `max_tokens` vinavyotumiwa na wakala, `tools` ambazo wakala anaweza kuitisha, na hata `model` yenyewe inayotumiwa kwa wakala.

Hii ni muhimu katika hali ambapo mifano au zana maalum zinahitajika kumaliza kazi ya mtumiaji.

**Zana**

Zana zinaweza kufafanuliwa wakati wa kuanzisha wakala:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Wakati wa kuunda ChatAgent moja kwa moja

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

na pia wakati wa kuendesha wakala:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Zana iliyotolewa kwa ajili ya kuendesha mara hii tu )
```

**Nyuzinyuzi za Wakala**

Nyuzinyuzi za wakala hutumika kushughulikia mazungumzo yenye mizunguko mingi. Nyuzinyuzi zinaweza kuundwa kwa njia ya:

- Kutumia `get_new_thread()` ambayo inaruhusu nyuzi kuhifadhiwa kwa muda mrefu
- Kuunda nyuzi moja moja moja moja moja kiotomatiki wakati wa kuendesha wakala na nyuzi hiyo kudumu tu wakati wa uendeshaji huo.

Kuunda nyuzi, msimbo unavyoonekana kama huu:

```python
# Unda thread mpya.
thread = agent.get_new_thread() # Endesha wakala kwa thread hiyo.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Baadaye unaweza kusambaza nyuzi hiyo ili ihifadhiwe kwa matumizi ya baadaye:

```python
# Unda thread mpya.
thread = agent.get_new_thread() 

# Endesha wakala na thread.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serialize thread kwa ajili ya kuhifadhi.

serialized_thread = await thread.serialize() 

# Deserialize hali ya thread baada ya kuipakia kutoka kwenye hifadhi.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware ya Wakala**

Mawakala hushirikiana na zana na LLM kukamilisha kazi za mtumiaji. Katika hali fulani, tunataka kutekeleza au kufuatilia kati ya mwingiliano huu. Middleware ya wakala inatuwezesha kufanya hivi kupitia:

*Middleware ya Kazi*

Middleware hii inaruhusu kutekeleza hatua kati ya wakala na kazi/zana anayoitisha. Mfano wa matumizi yake ni kufikia wakati wowote unataka kufanyika kurekodi kuitishwa kwa kazi.

Katika msimbo ulio chini `next` hutambua kama middleware inayofuata au kazi halisi inapaswa kuitwa.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Usindikaji wa awali: Andika kumbukumbu kabla ya utekelezaji wa kazi
    print(f"[Function] Calling {context.function.name}")

    # Endelea kwa katikati au utekelezaji wa kazi inayofuata
    await next(context)

    # Usindikaji wa baadae: Andika kumbukumbu baada ya utekelezaji wa kazi
    print(f"[Function] {context.function.name} completed")
```

*Middleware ya Gumzo*

Middleware hii inaruhusu kutekeleza au kurekodi hatua kati ya wakala na maombi kati ya LLM.

Hii ina habari muhimu kama `messages` zinazosambazwa kwa huduma ya AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Utangulizi: Andika kumbukumbu kabla ya simu ya AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Endelea kwa middleware au huduma ya AI inayofuata
    await next(context)

    # Baada ya usindikaji: Andika kumbukumbu baada ya jibu la AI
    print("[Chat] AI response received")

```

**Kumbukumbu ya Wakala**

Kama ilivyojadiliwa katika somo la `Agentic Memory`, kumbukumbu ni kipengele muhimu kwa kumwezesha wakala kufanya kazi katika muktadha mbalimbali. MAF hutoa aina mbalimbali za kumbukumbu:

*Uhifadhi wa Kumbukumbu Ndani*

Hii ni kumbukumbu inayo hifadhiwa ndani ya nyuzi wakati wa utekelezaji wa programu.

```python
# Unda thread mpya.
thread = agent.get_new_thread() # Endesha wakala na thread hiyo.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Ujumbe Endelevu*

Kumbukumbu hii hutumika kuhifadhi historia ya mazungumzo kati ya vikao tofauti. Hufafanuliwa kwa kutumia `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Unda duka maalum la ujumbe
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Kumbukumbu ya Muktadha (Dynamic)*

Kumbukumbu hii inaongezwa katika muktadha kabla mawakala kuendeshwa. Kumbukumbu hizi zinaweza kuhifadhiwa katika huduma za nje kama mem0:

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

**Uangalizi wa Wakala**

Uangalizi ni muhimu katika kujenga mifumo ya wakala yenye kuaminika na inayoweza kudumishwa. MAF ina ushirikiano na OpenTelemetry ili kutoa ufuatiliaji na mita kwa uangalizi bora.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # fanya kitu
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Mifumo ya Kazi

MAF hutoa mifumo ya kazi ambayo ni hatua zilizobainishwa kabla kukamilisha kazi na inajumuisha mawakala wa AI kama vipengele katika hatua hizo.

Mifumo ya kazi imetengenezwa kwa vipengele tofauti vinavyoruhusu mtiririko mzuri wa udhibiti. Mfumo huo pia unaruhusu **mpangilio wa wakala wengi** na **kuhifadhi hali** ili kuhifadhi hali za mfumo wa kazi.

Vipengele muhimu vya mfumo wa kazi ni:

**Watendakazi**

Watendakazi hupokea ujumbe wa ingizo, hufanya kazi zilizopangiwa, na kisha hutoa ujumbe wa matokeo. Hii husogeza mfumo wa kazi kuelekea kukamilisha kazi kubwa. Watendakazi wanaweza kuwa wakala wa AI au mantiki maalum.

**Mikondo**

Mikondo hutumika kufafanua mtiririko wa ujumbe katika mfumo wa kazi. Hii inaweza kuwa:

*Mikondo ya Moja kwa Moja* - Uunganisho rahisi wa moja kwa moja kati ya watendakazi:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Mikondo ya Masharti* - Inazinduliwa baada ya sharti fulani kutimizwa. Kwa mfano, wakati vyumba vya hoteli havipatikani, mtendakazi anaweza kupendekeza chaguzi nyingine.

*Mikondo ya Kuingia Kiwango* - Ielekeza ujumbe kwa watendakazi tofauti kwa misingi ya masharti yaliyowekwa. Kwa mfano, wakati mteja wa usafiri ana upatikanaji wa kipaumbele na kazi zao zitashughulikiwa kupitia mfumo mwingine wa kazi.

*Mikondo ya Kutoa kwa Wengi* - Tuma ujumbe mmoja kwa malengo mengi.

*Mikondo ya Kupokea kutoka kwa Wengi* - Kusanya ujumbe mwingi kutoka kwa watendakazi tofauti na kutuma kwa lengo moja.

**Matukio**

Ili kutoa uangalizi bora katika mifumo ya kazi, MAF hutoa matukio yaliyojengwa kwa ajili ya utekelezaji ikiwa ni pamoja na:

- `WorkflowStartedEvent`  - Utekelezaji wa mfumo wa kazi unaanza
- `WorkflowOutputEvent` - Mfumo wa kazi huzalisha matokeo
- `WorkflowErrorEvent` - Mfumo wa kazi unakutana na kosa
- `ExecutorInvokeEvent`  - Mtendakazi anaanza kusindika
- `ExecutorCompleteEvent`  -  Mtendakazi anakamilisha kusindika
- `RequestInfoEvent` - Ombi linafanyika

## Mifumo ya Juu ya MAF

Sehemu zilizo juu zinashughulikia dhana kuu za Mfumo wa Wakala wa Microsoft. Unapoendelea kuunda mawakala tata zaidi, hapa kuna mifumo ya juu ya kuzingatia:

- **Muundo wa Middleware**: Piga mnyororo wa vichakataji vya middleware nyingi (urekodi, uthibitishaji, ukomo wa viwango) kwa kutumia middleware ya kazi na gumzo kwa udhibiti wa kina wa tabia ya wakala.
- **Kuhifadhi Mfumo wa Kazi**: Tumia matukio ya mfumo wa kazi na serialization kuhifadhi na kuendelea na michakato ndefu ya wakala.
- **Uchaguzi wa Zana wa Kimsingi**: Changanya RAG juu ya maelezo ya zana na usajili wa zana za MAF kuonyesha zana zinazohitajika tu kwa kila swali.
- **Kuhamisha Wakala Wengi**: Tumia mikondo ya mfumo wa kazi na kuongoza kwa masharti kuratibu kuhamishwa kati ya mawakala maalum.

## Kuhosta Mawakala wa LangChain / LangGraph kwenye Microsoft Foundry

Mfumo wa Wakala wa Microsoft ni **mfumo unaoweza kuingiliana** — hutegemei mawakala yaliyotengenezwa tu na MAF. Ikiwa tayari una wakala aliyejengwa na **LangChain** au **LangGraph**, unaweza kuutumia kama **wakala anayehostwa na Microsoft Foundry** ili Foundry isimamishe wakati wa kukimbia, vikao, ugawaji, utambulisho, na vituo vya itifaki kwako, wakati mantiki ya wakala wako inabaki katika LangGraph.

Hii hufanywa kwa kifurushi cha `langchain_azure_ai.agents.hosting`, kinachoonyesha grafu ya LangGraph iliyokusanywa kupitia itifaki zile zile za wakala wanaohostwa na Foundry hutumia.

**1. Sakinisha ziada ya kuhudumia:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Ziada ya `hosting` inasimamia maktaba za itifaki za Foundry: `azure-ai-agentserver-responses` (mwisho wa OpenAI unaolingana `/responses`) na `azure-ai-agentserver-invocations` (mwisho wa jumla `/invocations`).

**2. Chagua itifaki ya kuhudumia:**

| Itifaki | Darasa la Mhosti | Mwisho wa Mkutano | Tumia wakati |
|----------|-----------|----------|----------|
| **Majibu** | `ResponsesHostServer` | `/responses` | Unataka gumzo la kuendana na OpenAI, mtiririko, historia ya majibu, na kuunganisha mazungumzo — chaguo la kawaida lililopendekezwa kwa mawakala wa mazungumzo. |
| **Makumbusho** | `InvocationsHostServer` | `/invocations` | Unahitaji muundo wa JSON maalum, mwisho wa webhook, au usindikaji usio wa mazungumzo. |

Kwa sababu **API ya Majibu ni API kuu kwa maendeleo ya mtindo wa wakala katika Foundry**, anza na `ResponsesHostServer` kwa mawakala wengi.

**3. Sanidi vigezo vya mazingira** (`az login` kwanza ili `DefaultAzureCredential` iweze kuthibitisha):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Wakati wakala baadaye anaendeshwa kama wakala anayehostwa katika Foundry, jukwaa litaingiza `FOUNDRY_PROJECT_ENDPOINT` moja kwa moja.

**4. Weka wakala wa LangGraph kupitia itifaki ya Majibu:**

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

    # ChatOpenAI hapa inalenga kwenye sehemu ya mradi wa Foundry inayolingana na OpenAI (Majibu).
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

Endesha kwa ndani kwa kutumia `python main.py`, kisha tuma ombi la Majibu kwa `http://localhost:8088/responses`.

**Tabia kuu:**

- **Mazungumzo**: Wateja wanaendelea na mazungumzo kwa kupitisha `previous_response_id` au kitambulisho cha `conversation`. Ikiwa grafu yako imekusanywa na checkpointer wa LangGraph, Foundry huhifadhi hali ya mazungumzo kwa checkpoint (tumia checkpointer ya kudumu katika uzalishaji; `MemorySaver` ni nzuri kwa majaribio ya ndani).
- **Binadamu katika mzunguko**: Ikiwa grafu yako inatumia LangGraph `interrupt()`, `ResponsesHostServer` huonyesha kikumbusho kilichosubiri kama kipengele cha `function_call` / `mcp_approval_request` cha Majibu, na wateja wanaendelea na `function_call_output` / `mcp_approval_response` inayolingana.
- **Weka katika Foundry**: Tumia Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (ndani, inahitaji Docker), kisha `azd provision` na `azd deploy`. Uwekaji wakala anayehostwa unahitaji jukumu la **Foundry Project Manager**.

Toleo linaloweza kuendeshwa la mfano huu lipo katika [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Kwa mwongozo kamili (itifaki ya Makumbusho, mifumo maalum ya maombi, na utatuzi wa matatizo), ona [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Sampuli za Msimbo 

Sampuli za msimbo kwa Mfumo wa Wakala wa Microsoft zinaweza kupatikana katika hifadhidata hii chini ya faili za `xx-python-agent-framework` na `xx-dotnet-agent-framework`.

## Je, Una Maswali Zaidi Kuhusu Mfumo wa Wakala wa Microsoft?

Jiunge na [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) kukutana na wanafunzi wengine, kuhudhuria saa za ofisi na kupata majibu ya maswali yako kuhusu Wakala wa AI.
## Somo Lililopita

[Kumbukumbu kwa Wakala wa AI](../13-agent-memory/README.md)

## Somo Lijalo

[Kuunda Mawakala wa Matumizi ya Kompyuta (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->