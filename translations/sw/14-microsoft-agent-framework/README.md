# Kuchunguza Mfumo wa Wakala wa Microsoft

![Mfumo wa Wakala](../../../translated_images/sw/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Utangulizi

Somo hili litajumuisha:

- Kuelewa Mfumo wa Wakala wa Microsoft: Vipengele Muhimu na Thamani  
- Kuchunguza Misingi Mikuu ya Mfumo wa Wakala wa Microsoft
- Mifumo ya MAF ya Juu: Mipangilio ya Kazi, Vipatanishi, na Kumbukumbu

## Malengo ya Kujifunza

Baada ya kumaliza somo hili, utajua jinsi ya:

- Kujenga Wakala wa AI Tayari kwa Uzalishaji kwa kutumia Mfumo wa Wakala wa Microsoft
- Kutumia vipengele kuu vya Mfumo wa Wakala wa Microsoft kwenye Matukio ya Matumizi ya Wakala
- Kutumia mifumo ya juu ikijumuisha mipangilio ya kazi, vipatanishi, na uangalizi

## Sampuli za Msimbo 

Sampuli za msimbo za [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) zinaweza kupatikana katika hifadhidata hii chini ya faili za `xx-python-agent-framework` na `xx-dotnet-agent-framework`.

## Kuelewa Mfumo wa Wakala wa Microsoft

![Utangulizi wa Mfumo](../../../translated_images/sw/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) ni mfumo umoja wa Microsoft kwa ajili ya kujenga wakala wa AI. Inatoa kubadilika kwa kushughulikia aina mbalimbali za matukio ya matumizi ya wakala yanayoonekana katika mazingira ya uzalishaji na utafiti yakiwemo:

- **Utawala wa Mchakato wa Wakala kwa Mpangilio** katika hali ambapo mchakato wa hatua kwa hatua unahitajika.
- **Utawala wa Mchakato kwa Wakati Mmoja** katika hali ambapo wakala wanahitaji kukamilisha kazi kwa pamoja.
- **Utawala wa Mazungumzo ya Kundi** katika hali ambapo wakala wanaweza kushirikiana pamoja kwenye kazi moja.
- **Utawala wa Kuwapasha Wakala Kazi** katika hali ambapo wakala wanapasa kazi kwa kila mmoja baada ya kazi ndogo kukamilika.
- **Utawala wa Kuvuta Kazi** katika hali ambapo wakala msimamizi huunda na kuhariri orodha ya kazi na kushughulikia uratibu wa wakala wadogo kukamilisha kazi.

Ili kutoa Wakala wa AI katika Uzalishaji, MAF pia ina vipengele vya:

- **Uangalizi** kupitia matumizi ya OpenTelemetry ambapo kila kitendo cha Wakili wa AI pamoja na kuitwa kwa zana, hatua za utawala, mwelekeo wa hoja na ufuatiliaji wa utendaji kupitia dashibodi za Microsoft Foundry.
- **Usalama** kwa kuwa mwenyeji wa wakala mojawapo kwenye Microsoft Foundry ambayo inajumuisha udhibiti wa usalama kama ufikiaji kwa msingi wa majukumu, usimamizi wa data binafsi na usalama wa maudhui uliopo.
- **Uimara** kwa kuwa nguzo na taratibu za wakala zinaweza kusitishwa, kuendelea na kupona kutokana na makosa ambayo huwezesha mchakato mrefu zaidi.
- **Udhibiti** kwa kuwa taratibu za binadamu mzunguko zinaungwa mkono ambapo kazi zinatambulika kuwa zinahitaji idhini ya binadamu.

Mfumo wa Wakala wa Microsoft pia umejikita katika kuwa na uwezo wa kuingiliana kwa:

- **Kuwa huru kwa Wingu** - Wakala wanaweza kuendeshwa ndani ya kontena, maeneo ya ndani na katika mawingu mbalimbali.
- **Kuwa huru kwa Mtoa Huduma** - Wakala wanaweza kuundwa kupitia SDK unayopendelea ikiwa ni pamoja na Azure OpenAI na OpenAI
- **Kuingiza Viwango Vya Wazi** - Wakala wanaweza kutumia itifaki kama Agent-to-Agent (A2A) na Model Context Protocol (MCP) kugundua na kutumia wakala na zana nyingine.
- **Viambatisho na Vihusiano** - Uhusiano unaweza kufanyika na huduma za data na kumbukumbu kama Microsoft Fabric, SharePoint, Pinecone na Qdrant.

Tuchunguze jinsi vipengele hivi vinavyotumika kwa baadhi ya misingi kuu ya Mfumo wa Wakala wa Microsoft.

## Misingi Muhimu ya Mfumo wa Wakala wa Microsoft

### Wakala

![Mfumo wa Wakala](../../../translated_images/sw/agent-components.410a06daf87b4fef.webp)

**Kuumba Wakala**

Uumbaji wa wakala hufanyika kwa kufafanua huduma ya tathmini (Mtoa Huduma wa LLM), seti ya maelekezo kwa Wakili wa AI kufuata, na jina lililopewa `name`:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Juu hutumia `Azure OpenAI` lakini wakala wanaweza kuundwa kwa kutumia huduma mbalimbali ikiwemo `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

APIs za OpenAI `Responses`, `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

au [MiniMax](https://platform.minimaxi.com/), ambayo hutoa API inayolingana na OpenAI yenye dirisha kubwa la muktadha (hadi tokeni 204K):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

au wakala wa mbali wakitumia itifaki ya A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Kuendesha Wakala**

Wakala wanaendeshwa kwa kutumia njia `.run` au `.run_stream` kwa majibu yasiyo na mfululizo au yenye mfululizo.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Kila kuendesha wakala kunaweza pia kuwa na chaguzi za kubinafsisha vigezo kama `max_tokens` vinavyotumiwa na wakala, `tools` ambazo wakala anaweza kuita, na hata `model` iliyotumiwa kwa wakala.

Hii ni muhimu katika hali ambapo mifano au zana maalum zinahitajika kukamilisha kazi ya mtumiaji.

**Zana**

Zana zinaweza kufafanuliwa wakati wa kuunda wakala:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Wakati wa kuunda ChatAgent moja kwa moja

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

na pia wakati wa kuendesha wakala:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Chombo kilichotolewa kwa ajili ya mzunguko huu pekee )
```

**Mizizi ya Wakala**

Mizizi ya Wakala hutumiwa kushughulikia mazungumzo ya mizunguko mingi. Mizizi inaweza kuundwa kwa:

- Kutumia `get_new_thread()` ambayo inaruhusu mizizi kuhifadhiwa kwa muda mrefu
- Kuunda mzizi kiotomati wakati unaendesha wakala na mzizi kuba tu katika kuendeshwa kwa sasa.

Kuunda mzizi, msimbo huonekana kama huu:

```python
# Unda thread mpya.
thread = agent.get_new_thread() # Endesha wakala kwa thread hiyo.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Baada yake unaweza kuweka mizizi kuwa serialized kuhifadhiwa kwa matumizi ya baadaye:

```python
# Unda kiini kipya.
thread = agent.get_new_thread() 

# Endesha wakala na kiini hicho.

response = await agent.run("Hello, how are you?", thread=thread) 

# Andika kiini kwa njia ya serialization kwa ajili ya kuhifadhi.

serialized_thread = await thread.serialize() 

# Soma hali ya kiini baada ya kupakia kutoka kwenye hifadhi.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Vipatanishi vya Wakala**

Wakala hushirikiana na zana na LLM kukamilisha kazi za mtumiaji. Katika hali fulani, tunataka kutekeleza au kufuatilia kati ya mwingiliano huu. Vipatanishi vya wakala vinatuwezesha kufanya hivi kupitia:

*Vipatanishi vya Kifunction*

Vipatanishi hivi huturuhusu kutekeleza kitendo kati ya wakala na function/zana ambayo wakala ataitegea. Mfano wa matumizi ni pale ambapo ungependa kufanya kumbukumbu kuhusu kuitwa kwa function.

Katika msimbo hapa chini `next` hutoa kama vipatanishi vinavyofuata au function halisi vinaweza kuitwa.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Utangulizi: Andika logi kabla ya utekelezaji wa kazi
    print(f"[Function] Calling {context.function.name}")

    # Endelea kwenye middleware inayofuata au utekelezaji wa kazi
    await next(context)

    # Baada ya usindikaji: Andika logi baada ya utekelezaji wa kazi
    print(f"[Function] {context.function.name} completed")
```

*Vipatanishi vya Mazungumzo*

Vipatanishi hivi huturuhusu kutekeleza au kuweka kumbukumbu kitendo kati ya wakala na maombi kati ya LLM.

Huu una taarifa muhimu kama `messages` zinazotumwa kwa huduma ya AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Kuhifadhi kumbukumbu kabla ya simu ya AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Endelea kwa middleware au huduma ya AI inayofuata
    await next(context)

    # Kuhifadhi kumbukumbu baada ya jibu la AI
    print("[Chat] AI response received")

```

**Kumbukumbu ya Wakala**

Kama ilivyoelezwa katika somo la `Agentic Memory`, kumbukumbu ni elementi muhimu kuwezesha wakala kufanya kazi katika muktadha tofauti. MAF inatoa aina tofauti za kumbukumbu:

*Uhifadhi wa Kumbukumbu Ndani*

Hii ni kumbukumbu inayohifadhiwa katika mizizi wakati wa uendeshaji wa programu.

```python
# Unda mzunguko mpya.
thread = agent.get_new_thread() # Endesha wakala na mzunguko huo.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Ujumbe wa Kudumu*

Kumbukumbu hii hutumiwa kuhifadhi historia za mazungumzo katika vikao tofauti. Inafafanuliwa kwa kutumia `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Unda duka la ujumbe maalum
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Kumbukumbu ya Mabadiliko*

Kumbukumbu hii inaongezwa kwa muktadha kabla wakala kuendeshwa. Kumbukumbu hizi zinaweza kuhifadhiwa katika huduma za nje kama mem0:

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

Uangalizi ni muhimu kwa kujenga mifumo ya kuaminika na inayoweza kudumishwa kwa wakala. MAF inaunganishwa na OpenTelemetry kutoa kufuatilia na mita kwa ajili ya uangalizi bora.

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

### Mipangilio ya Kazi

MAF hutoa mipangilio ya kazi ambayo ni hatua zilizopangwa tayari kukamilisha kazi na kujumuisha wakala wa AI kama vipengele katika hatua hizo.

Mipangilio ya kazi imetengenezwa kwa vipengele tofauti vinavyoruhusu mtiririko bora wa udhibiti. Mipangilio pia huwezesha **utawala wa wakala wengi** na **kurekodi mahali pa kusimamia** kuhifadhi hali za mchakato wa kazi.

Vipengele vikuu vya mchakato wa kazi ni:

**Watendaji**

Watendaji hupokea ujumbe wa ingizo, kutekeleza majukumu waliyopewa, kisha kutoa ujumbe wa matokeo. Hii husukuma mchakato wa kazi mbele kuelekea kukamilika kwa kazi kubwa. Watendaji wanaweza kuwa wakala wa AI au mantiki maalum.

**Mkupuo**

Mipakani hutumiwa kufafanua mtiririko wa ujumbe katika mchakato wa kazi. Hizi zinaweza kuwa:

*Mipakani ya Moja kwa Moja* - Uhusiano rahisi wa moja kwa moja kati ya watendaji:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Mipakani Sharti* - Inapoanzishwa baada ya sharti fulani kutimizwa. Kwa mfano, kama vyumba vya hoteli viko nje ya hisa, mtendaji anaweza kupendekeza chaguzi nyingine.

*Mipakani ya Mabadiliko* - Ruta ujumbe kwa watendaji tofauti kulingana na masharti yaliyofafanuliwa. Kwa mfano, kama mteja wa usafiri ana upatikanaji wa kipaumbele na majukumu yake yatahudumiwa kupitia mchakato mwingine wa kazi.

*Mipakani ya Kuwatuma Wengi* - Tuma ujumbe mmoja kwa malengo mengi.

*Mipakani ya Kukusanya Wengi* - Kusanya ujumbe kutoka kwa watendaji tofauti na kutumia kwa lengo moja.

**Matukio**

Ili kutoa uangalizi bora wa mipangilio ya kazi, MAF hutoa matukio yaliyojengwa kwa ajili ya utekelezaji ikiwa ni pamoja na:

- `WorkflowStartedEvent`  - Utekelezaji wa mchakato wa kazi unaanza
- `WorkflowOutputEvent` - Mchakato wa kazi hutengeneza matokeo
- `WorkflowErrorEvent` - Mchakato wa kazi unapata kosa
- `ExecutorInvokeEvent`  - Mtendaji huanza kusindika
- `ExecutorCompleteEvent`  -  Mtendaji anamaliza kusindika
- `RequestInfoEvent` - Ombi limewasilishwa

## Mifumo ya Juu ya MAF

Sehemu zilizotangulia zinaelezea misingi muhimu ya Mfumo wa Wakala wa Microsoft. Unapojenga wakala tata zaidi, hapa kuna mifumo ya juu ya kuzingatia:

- **Muundo wa Vipatanishi**: Unganisha vipatanishi vingi (kumbukumbu, uthibitishaji, kikomo cha kiwango) ukitumia vipatanishi vya function na mazungumzo kwa udhibiti mzuri wa tabia ya wakala.
- **Kurekodi Mahali pa Kusimamia kwa Mchakato wa Kazi**: Tumia matukio ya mchakato wa kazi na serialization kuhifadhi na kuendelea na michakato ya wakala inayochukua muda mrefu.
- **Uteuzi wa Zana la Kifaa-Cha-Mawazo**: Changanya RAG juu ya maelezo ya zana na usajili wa zana wa MAF kuonyesha zana zinazohitajika tu kwa kila kuuliza.
- **Kuwahamisha Wakala Wengi**: Tumia mipakani ya mchakato na njia za routing sharti kuandaa kuhamishwa kati ya wakala maalum.

## Kuendesha Wakala wa LangChain / LangGraph kwenye Microsoft Foundry

Mfumo wa Wakala wa Microsoft ni **mfumo unaoweza kuingiliana** — huna kikomo kwa wakala waliyoandikwa kwa MAF. Ikiwa tayari una wakala aliyejengwa na **LangChain** au **LangGraph**, unaweza kuendesha kama **wakala mwenyeji wa Microsoft Foundry** ili Foundry isimamia wakati wa utendakazi, vikao, upanuzi, utambulisho, na viungo vya itifaki kwa ajili yako, wakati mantiki ya wakala wako inabaki katika LangGraph.

Hii hufanyika kwa kifurushi cha `langchain_azure_ai.agents.hosting`, kinachofungua mchoro wa LangGraph uliotengenezwa kwa njia sawa za itifaki zinazotumiwa na wakala wenyeji wa Foundry.

**1. Sakinisha ziada ya mwenyeji:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Ziada ya `hosting` huweka maktaba za itifaki za Foundry: `azure-ai-agentserver-responses` (kiungo cha `/responses` kinacholingana na OpenAI) na `azure-ai-agentserver-invocations` (kiungo cha jumla cha `/invocations`).

**2. Chagua itifaki ya mwenyeji:**

| Itifaki | Darasa la mwenyeji | Kiungo | Tumia wakati |
|----------|-----------|----------|----------|
| **Majibu** | `ResponsesHostServer` | `/responses` | Unapotaka mazungumzo yanayolingana na OpenAI, mtiririko, historia ya majibu, na usimamizi wa mazungumzo — chaguo linalopendekezwa kwa wakala wa mazungumzo. |
| **Miito** | `InvocationsHostServer` | `/invocations` | Unapotaka muundo wa JSON maalum, kiungo cha mtindo wa webhook, au usindikaji usio wa mazungumzo. |

Kwa kuwa **APIs za Majibu ni API kuu kwa maendeleo ya aina ya wakala katika Foundry**, anza na `ResponsesHostServer` kwa wakala wengi.

**3. Sanidi vigezo vya mazingira** (`az login` kwanza ili `DefaultAzureCredential` iweze kuthibitisha):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Wakala atakapokuwa anapokelewa huko Foundry, jukwaa litatia automatik FOUDRY_PROJECT_ENDPOINT.

**4. Onyesha wakala wa LangGraph juu ya itifaki ya Majibu:**

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

    # ChatOpenAI hapa inalenga sehemu ya mradi wa Foundry inayolingana na OpenAI (Majibu).
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

Endesha ndani ya eneo lako na `python main.py`, kisha tuma ombi la Majibu kwa `http://localhost:8088/responses`.

**Tabia muhimu:**

- **Mazungumzo**: Wateja wanaendelea na mazungumzo kwa kupitisha `previous_response_id` au kitambulisho cha mazungumzo `conversation`. Ikiwa mchoro wako umeunganishwa na kiporekodi cha LangGraph, Foundry husawazisha hali ya mazungumzo kwa kiporekodi (tumia kiporekodi cha kudumu katika uzalishaji; `MemorySaver` ni nzuri kwa majaribio ya ndani).
- **Mtu katikati ya mzunguko**: Ikiwa mchoro wako unatumia LangGraph `interrupt()`, `ResponsesHostServer` huonesha mgongano uliosubiri kama kipengele cha `function_call` / `mcp_approval_request` cha Majibu, na wateja huendelea na `function_call_output` / `mcp_approval_response` vinavyofanana.
- **Tekeleza kwenye Foundry**: Tumia CLI ya Azure Developer — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokal, inahitaji Docker), kisha `azd provision` na `azd deploy`. Utekelezaji wa wakala mwenyeji unahitaji jukumu la **Msimamizi wa Mradi wa Foundry**.

Toleo linaloweza kuendeshwa la mfano huu linaishi katika [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Kwa mwongozo kamili (itifaki za Miito, muundo wa maombi maalum, na utatuzi wa matatizo), angalia [Kuendesha wakala wa LangGraph kama wakala wenyeji wa Foundry](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Sampuli za Msimbo 

Sampuli za msimbo za Mfumo wa Wakala wa Microsoft zinaweza kupatikana katika hifadhidata hii chini ya faili za `xx-python-agent-framework` na `xx-dotnet-agent-framework`.

## Je, una Maswali Zaidi Kuhusu Mfumo wa Wakala wa Microsoft?

Jiunge na [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) kukutana na wanaojifunza wengine, kuhudhuria wakati wa ofisi na kupata majibu ya maswali yako kuhusu Wakala wa AI.
## Somo lililopita

[Kumbukumbu kwa Wakala wa AI](../13-agent-memory/README.md)

## Somo lijalo

[Kujenga Wakala wa Matumizi ya Kompyuta (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->