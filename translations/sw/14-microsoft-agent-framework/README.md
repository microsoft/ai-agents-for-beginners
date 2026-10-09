# Kuchunguza Mfumo wa Wakala wa Microsoft

![Agent Framework](../../../translated_images/sw/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Utangulizi

Somo hili litaangazia:

- Kuelewa Mfumo wa Wakala wa Microsoft: Sifa Muhimu na Thamani  
- Kuchunguza Misingi Muhimu ya Mfumo wa Wakala wa Microsoft
- Mifumo ya MAF ya Juu: Michakato ya Kazi, Middleware, na Kumbukumbu

## Malengo ya Kujifunza

Baada ya kumaliza somo hili, utajua jinsi ya:

- Kujenga Wakala wa AI Tayari kwa Uzalishaji kwa kutumia Mfumo wa Wakala wa Microsoft
- Kutumia sifa kuu za Mfumo wa Wakala wa Microsoft kwa Matumizi yako ya Wakili
- Kutumia mifumo ya juu ikiwa ni pamoja na michakato ya kazi, middleware, na ufuatiliaji

## Sampuli za Msimbo 

Sampuli za msimbo za [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) zinaweza kupatikana katika hifadhidata hii chini ya faili za `xx-python-agent-framework` na `xx-dotnet-agent-framework`.

## Kuelewa Mfumo wa Wakala wa Microsoft

![Framework Intro](../../../translated_images/sw/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) ni mfumo uliounganishwa wa Microsoft kwa ajili ya kujenga wakala wa AI. Inatoa unyumbufu wa kushughulikia aina mbalimbali za matumizi ya wakala unaoonekana katika mazingira ya uzalishaji na utafiti ikiwa ni pamoja na:

- **Utaratibu wa Wakala wa mfuatano** katika hali ambapo michakato ya hatua kwa hatua inahitajika.
- **Utaratibu wa Wakala kwa wakati mmoja** katika hali ambapo mawakala wanahitaji kukamilisha kazi kwa wakati mmoja.
- **Utaratibu wa Mazungumzo ya Kundi** katika hali ambapo mawakala wanaweza kushirikiana pamoja katika kazi moja.
- **Utaratibu wa Uhamisho** katika hali ambapo mawakala wanahamishia kazi kwa kila mmoja kadri kazi ndogo zinavyokamilika.
- **Utaratibu wa Miondoko** katika hali ambapo wakala wa meneja huunda na kubadilisha orodha ya kazi na kushughulikia uratibu wa mawakala mdogo kumaliza kazi.

Ili kutoa Wakala wa AI katika Uzalishaji, MAF pia ina sifa za:

- **Ufuatiliaji** kupitia matumizi ya OpenTelemetry ambapo kila kitendo cha Wakala wa AI ikiwa ni pamoja na kuitwa zana, hatua za utaratibu, mtiririko wa hoja na ufuatiliaji wa utendaji kupitia dashibodi za Microsoft Foundry.
- **Usalama** kwa kuwa mwenyeji wa mawakala asili kwenye Microsoft Foundry ambayo inajumuisha udhibiti wa usalama kama upatikanaji wa msingi wa nyaraka, usimamizi wa data binafsi na usalama wa maudhui uliopo ndani.
- **Uhimili** kwani mistari ya wakala na michakato ya kazi inaweza kusimama, kuendelea na kurekebisha makosa ambayo hutoa mchakato wa muda mrefu.
- **Udhibiti** kama michakato ya kazi yenye mtu binadamu katikati inasaidiwa ambapo kazi zinatumwa kama zinahitaji idhini ya binadamu.

Mfumo wa Wakala wa Microsoft pia unalenga kuwa na uingilivu kwa:

- **Kuwa huru kwa Wingu** - Wakala wanaweza kuendeshwa kwenye kontena, ndani ya ofisi na katika mawingu mengi tofauti.
- **Kuwa huru kwa Mtoa Huduma** - Wakala wanaweza kuundwa kupitia SDK unayopendelea ikiwa ni pamoja na Azure OpenAI na OpenAI
- **Kuingiza Viwango Huru** - Wakala wanaweza kutumia itifaki kama Agent-to-Agent(A2A) na Model Context Protocol (MCP) kugundua na kutumia mawakala na zana wengine.
- **Viambatanisho na Viano** - Muunganisho unaweza kufanywa kwa huduma za data na kumbukumbu kama Microsoft Fabric, SharePoint, Pinecone na Qdrant.

Tuchunguze jinsi sifa hizi zinavyotumika kwa baadhi ya dhana kuu za Mfumo wa Wakala wa Microsoft.

## Dhana Muhimu za Mfumo wa Wakala wa Microsoft

### Wakala

![Agent Framework](../../../translated_images/sw/agent-components.410a06daf87b4fef.webp)

**Kutengeneza Wakala**

Uundaji wa wakala hufanyika kwa kufafanua huduma ya utambuzi (Mtoa huduma wa LLM), seti ya maagizo kwa Wakala wa AI kufuata, na `jina` lililoteuliwa:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Hapo juu inatumia `Azure OpenAI` lakini mawakala wanaweza kuundwa kwa kutumia huduma mbalimbali ikiwa ni pamoja na `Microsoft Foundry Agent Service`:

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

au [MiniMax](https://platform.minimaxi.com/), ambayo hutoa API inayolingana na OpenAI na madirisha makubwa ya muktadha (hadi tokeni 204K):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

au mawakala wa mbali wakitumia itifaki ya A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Kuendesha Wakala**

Mawakala huendeshwa kwa kutumia njia `.run` au `.run_stream` kwa majibu yasiyo ya mtiririko au ya mtiririko.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Kila kuendesha wakala pia kunaweza kuwa na chaguzi za kubinafsisha vigezo kama `max_tokens` vinavyotumika na wakala, `tools` ambazo wakala anaweza kuitia simu, na hata `model` yenyewe inayotumika kwa wakala.

Hii ni muhimu katika kesi ambapo mifano maalum au zana zinahitajika kukamilisha kazi ya mtumiaji.

**Zana**

Zana zinaweza kufafanuliwa wakati wa kufafanua wakala:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Wakati wa kuunda ChatAgent moja kwa moja

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

na pia wakati wakala anapoendesha:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Chombo kilichotolewa kwa ajili ya kukimbia hii pekee )
```

**Mistari ya Wakala**

Mistari ya wakala hutumika kushughulikia mazungumzo ya mizunguko mingi. Mistari inaweza kuundwa kwa:

- Kutumia `get_new_thread()` ambayo huruhusu mstari kuhifadhiwa kwa muda mrefu
- Kuunda mstari moja moja wakati wa kuendesha wakala na mstari kupatikana tu wakati wa uendeshaji wa sasa.

Kuunda mstari, msimbo inaonekana hivi:

```python
# Unda thread mpya.
thread = agent.get_new_thread() # Endesha wakala kwa thread hiyo.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Kisha unaweza kuandaa mstari kuhifadhi kwa matumizi ya baadaye:

```python
# Unda kipaza sauti kipya.
thread = agent.get_new_thread() 

# Endesha wakala na kipaza sauti.

response = await agent.run("Hello, how are you?", thread=thread) 

# Fanya serialization ya kipaza sauti kwa kuhifadhi.

serialized_thread = await thread.serialize() 

# Fanya deserialization ya hali ya kipaza sauti baada ya kupakia kutoka kwenye hifadhi.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware ya Wakala**

Mawakala hushirikiana na zana na LLM ili kukamilisha kazi za mtumiaji. Katika hali fulani, tunataka kutekeleza au kufuatilia kati ya mwingiliano huu. Middleware ya wakala inatuwezesha kufanya hili kupitia:

*Middleware ya Kazi*

Middleware hii inaruhusu kutekeleza kitendo kati ya wakala na kazi/zaana inayoitwa. Mfano wa matumizi yake ni kutaka kufanya kurekodiwa kwa simu ya kazi.

Katika msimbo huu `next` huamua kama middleware inayofuata au kazi halisi itaitwa.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Utangulizi: Andika log kabla ya utekelezaji wa kazi
    print(f"[Function] Calling {context.function.name}")

    # Endelea kwa middleware inayofuata au utekelezaji wa kazi
    await next(context)

    # Ufuatiliaji wa baada: Andika log baada ya utekelezaji wa kazi
    print(f"[Function] {context.function.name} completed")
```

*Middleware ya Mazungumzo*

Middleware hii inaruhusu kutekeleza au kurekodi kitendo kati ya wakala na maombi kati ya LLM.

Hii ina taarifa muhimu kama `messages` zinazotumwa kwa huduma ya AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Usindikaji wa awali: Andika kumbukumbu kabla ya wito wa AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Endelea kwa middleware inayofuata au huduma ya AI
    await next(context)

    # Usindikaji wa baadaye: Andika kumbukumbu baada ya jibu la AI
    print("[Chat] AI response received")

```

**Kumbukumbu ya Wakala**

Kama ilivyoelezwa katika somo la `Agentic Memory`, kumbukumbu ni kipengele muhimu kwa kuwahimiza wakala kufanya kazi kwa muktadha tofauti. MAF inatoa aina kadhaa za kumbukumbu:

*Uhifadhi wa Kumbukumbu ya Ndani*

Hii ni kumbukumbu iliyohifadhiwa ndani ya mistari wakati wa kuendesha programu.

```python
# Unda uzi mpya.
thread = agent.get_new_thread() # Endesha wakala na uzi huo.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Ujumbe Endelevu*

Kumbukumbu hii hutumika kuhifadhi historia ya mazungumzo kati ya vikao tofauti. Imepangwa kwa kutumia `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Unda duka la ujumbe la kawaida
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Kumbukumbu ya Mabadiliko*

Kumbukumbu hii huongezwa kwenye muktadha kabla mawakala kuendeshwa. Kumbukumbu hizi zinaweza kuhifadhiwa kwa huduma za nje kama mem0:

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

Ufuatiliaji ni muhimu katika kujenga mifumo ya wakala inayoweza kuaminika na kudumishwa. MAF inaunganishwa na OpenTelemetry kutoa kufuatilia na mita kwa ufuatiliaji bora.

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

### Michakato ya Kazi

MAF hutoa michakato ya kazi ambayo ni hatua zilizoainishwa mapema za kumaliza kazi na kujumuisha mawakala wa AI kama vipengele katika hatua hizo.

Michakato ya kazi imeundwa na vipengele tofauti vinavyoruhusu mtiririko bora wa udhibiti. Michakato ya kazi pia inaruhusu **uratibu wa mawakala wengi** na **uhifadhi wa alama** kuhifadhi hali za michakato ya kazi.

Vipengele vikuu vya mchakato wa kazi ni:

**Watendaji**

Watendaji hupokea ujumbe wa ingizo, kutekeleza majukumu yao yaliyowekwa, na kisha kutoa ujumbe wa matokeo. Hii hupeleka mchakato wa kazi mbele kuelekea kukamilika kwa kazi kubwa. Watendaji wanaweza kuwa wakala wa AI au mantiki ya kawaida.

**Mikondo**

Mikondo hutumika kufafanua mtiririko wa ujumbe katika mchakato wa kazi. Hii inaweza kuwa:

*Mikondo ya Moja kwa Moja* - Muunganisho rahisi wa moja kwa moja kati ya watendaji:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Mikondo ya Masharti* - Hutumika baada ya sharti fulani kutimizwa. Kwa mfano, wakati vyumba vya hoteli havipo, mtendaji anaweza kupendekeza chaguzi nyingine.

*Mikondo ya Kesi ya Kubadili* - Ruta ujumbe kwa watendaji tofauti kulingana na masharti yaliyowekwa. Kwa mfano, ikiwa mteja wa usafiri ana upatikanaji wa kipaumbele na kazi zao zitatatuliwa kupitia mchakato mwingine wa kazi.

*Mikondo ya Kutuma Ujumbe nyingi* - Tuma ujumbe mmoja kwa malengo mengi.

*Mikondo ya Kupokea Ujumbe nyingi* - Kusanya ujumbe mbalimbali kutoka kwa watendaji tofauti na kutuma kwa lengo moja.

**Matukio**

Ili kutoa ufuatiliaji bora wa michakato ya kazi, MAF hutoa matukio yaliyojengwa kwa utekelezaji ikiwa ni pamoja na:

- `WorkflowStartedEvent`  - Kuanza utekelezaji wa mchakato wa kazi
- `WorkflowOutputEvent` - Mchakato wa kazi hutengeneza matokeo
- `WorkflowErrorEvent` - Mchakato wa kazi unakutana na kosa
- `ExecutorInvokeEvent`  - Mtendaji anaanza kusindika
- `ExecutorCompleteEvent`  -  Mtendaji anakamilisha kusindika
- `RequestInfoEvent` - Ombi limetumwa

## Mifumo ya Juu ya MAF

Sehemu zilizo juu zinaelezea dhana kuu za Mfumo wa Wakala wa Microsoft. Unapojenga mawakala magumu zaidi, hizi ni mifumo ya juu ya kuzingatia:

- **Muundo wa Middleware**: Unganisha watendaji wa middleware wengi (kurekodi, uthibitishaji, utawala wa viwango) kwa kutumia middleware ya kazi na mazungumzo kwa udhibiti mzuri wa tabia ya wakala.
- **Uhifadhi wa Alama ya Mchakato wa Kazi**: Tumia matukio ya mchakato wa kazi na serialization kuhifadhi na kuendelea na michakato ya wakala inayochukua muda mrefu.
- **Uchaguzi wa Zana za Dinamiki**: Changanya RAG juu ya maelezo ya zana na usajili wa zana wa MAF kuonyesha zana zinazohusiana tu kwa kila swali.
- **Uhamisho wa Wakala Wengi**: Tumia mikondo ya mchakato wa kazi na routing ya masharti kuratibu uhamisho kati ya mawakala maalum.

## Kuendesha Wakala wa LangChain / LangGraph kwenye Microsoft Foundry

Mfumo wa Wakala wa Microsoft ni **mfumo unaolingana na mifumo mingine** — haukubaliki kwa mawakala tu yaliyoandikwa kwa MAF. Ikiwa tayari una wakala aliyojengwa na **LangChain** au **LangGraph**, unaweza kuendesha kama **wakala mwenyeji wa Microsoft Foundry** ili Foundry idhibiti muda wa kuendesha, vikao, upanuzi, utambulisho, na mapokezi ya itifaki kwa niaba yako, wakati mantiki yako ya wakala inabaki katika LangGraph.

Hii hufanyika kwa kutumia kifurushi cha `langchain_azure_ai.agents.hosting`, kinachoonyesha grafu ya LangGraph iliyokusanywa juu ya itifaki sawa na wakala wenyeji wa Foundry hutumia.

**1. Sakinisha ziada ya kuhudumia:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Ziada ya `hosting` inasakinisha maktaba za itifaki za Foundry: `azure-ai-agentserver-responses` (mwisho wa OpenAI unaolingana wa `/responses`) na `azure-ai-agentserver-invocations` (mwisho wa jumla wa `/invocations`).

**2. Chagua itifaki ya kuhudumia:**

| Itifaki | Darasa la mwenyeji | Mwisho | Tumia wakati |
|----------|-----------|----------|----------|
| **Majibu** | `ResponsesHostServer` | `/responses` | Unataka mazungumzo yanayolingana na OpenAI, mtiririko, historia ya majibu, na ufuatiliaji wa mazungumzo — mshauri wa chaguo kwa kawaida kwa mawakala wa mazungumzo. |
| **Mifano** | `InvocationsHostServer` | `/invocations` | Unahitaji muundo wa JSON maalum, mwisho wa webhook au usindikaji usio wa mazungumzo. |

Kwa sababu **API ya Majibu ni API kuu kwa maendeleo ya aina ya wakala ndani ya Foundry**, anza na `ResponsesHostServer` kwa mawakala mengi.

**3. Sanidi vigezo vya mazingira** (`az login` kwanza ili `DefaultAzureCredential` iweze kuthibitisha):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Wakati wakala baadaye anaendesha kama wakala mwenyeji katika Foundry, jukwaa linaingiza `FOUNDRY_PROJECT_ENDPOINT` moja kwa moja.

**4. Weka wakala wa LangGraph juu ya itifaki ya Majibu:**

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

    # ChatOpenAI hapa inalenga kitovu cha mradi wa Foundry kinachotegemea OpenAI (Majibu).
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

Endesha hapo hapa ndani kwa kutumia `python main.py`, kisha tuma ombi la Majibu kwa `http://localhost:8088/responses`.

**Tabia kuu:**

- **Mazungumzo**: Wateja wanaendelea na mazungumzo kwa kupitisha `previous_response_id` au ID ya `conversation`. Ikiwa grafu yako imekusanywa na mhifadhi alama wa LangGraph, Foundry inahifadhi hali ya mazungumzo kwa alama (tumia mhifadhi alama aliyehimiliwa katika uzalishaji; `MemorySaver` ni sawa kwa majaribio ya ndani).
- **Mtu katikati ya mzunguko**: Ikiwa grafu yako inatumia LangGraph `interrupt()`, `ResponsesHostServer` inaonyesha faragha inayokusubiri kama kipengele cha Responses `function_call` / `mcp_approval_request`, na wateja wanaendelea na `function_call_output` / `mcp_approval_response` inayolingana.
- **Tekeleza katika Foundry**: Tumia Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (ndani, inahitaji Docker), kisha `azd provision` na `azd deploy`. Utekelezaji wa wakala mwenyeji unahitaji jukumu la **Msimamizi wa Mradi wa Foundry**.

Toleo linaloweza kuendeshwa la mfano huu linaishi katika [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Kwa mwongozo kamili (itifaki za Mifano, miundo ya maombi maalum, na utatuzi wa matatizo), angalia [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Sampuli za Msimbo 

Sampuli za msimbo za Mfumo wa Wakala wa Microsoft zinaweza kupatikana katika hifadhidata hii chini ya faili za `xx-python-agent-framework` na `xx-dotnet-agent-framework`.

## Una Maswali Zaidi Kuhusu Mfumo wa Wakala wa Microsoft?

Jiunge na [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) kukutana na wanafunzi wengine, kuhudhuria saa za ofisi na kupata majibu kwa maswali yako kuhusu Wakala wa AI.
## Somo lililopita

[Memory for AI Agents](../13-agent-memory/README.md)

## Somo linalofuata

[Building Computer Use Agents (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->