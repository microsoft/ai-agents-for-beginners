# Microsoft Agent Framework tyrinėjimas

![Agent Framework](../../../translated_images/lt/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Įvadas

Šiame pamokoje aptarsime:

- Microsoft Agent Framework supratimas: pagrindinės ypatybės ir vertė  
- Microsoft Agent Framework pagrindinių koncepcijų tyrinėjimas
- Pažangūs MAF šablonai: darbo srautai, tarpiniai procesai ir atmintis

## Mokymosi tikslai

Baigus šią pamoką, jūs žinosite, kaip:

- Kurti gamybai pasiruošusius AI agentus naudojant Microsoft Agent Framework
- Taikyti pagrindines Microsoft Agent Framework funkcijas savo agentiniams naudojimo atvejams
- Naudoti pažangius šablonus, įskaitant darbo srautus, tarpinį programinį sluoksnį ir stebėjimą

## Kodo pavyzdžiai 

Microsoft Agent Framework (MAF) [kodo pavyzdžius](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) rasite šiame saugykloje faile `xx-python-agent-framework` ir `xx-dotnet-agent-framework`.

## Microsoft Agent Framework supratimas

![Framework Intro](../../../translated_images/lt/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) yra Microsoft vieningas pagrindas dirbtinio intelekto agentams kurti. Jis siūlo lankstumą spręsti įvairius agentinius naudojimo atvejus, kurie pasitaiko tiek gamyboje, tiek tyrimų aplinkoje, įskaitant:

- **Sekveninė agentų orkestracija** scenarijuose, kur reikia žingsnis po žingsnio vykdomų darbo procesų.
- **Konkuruojanti orkestracija** scenarijuose, kur agentai turi atlikti užduotis tuo pačiu metu.
- **Grupinių pokalbių orkestracija** scenarijuose, kur agentai gali bendradarbiauti vienos užduoties atlikimui.
- **Perdavimų orkestracija** scenarijuose, kur agentai perduoda užduotį vienas kitam užduočių vykdymo eigoje.
- **Magnetinė orkestracija** scenarijuose, kur vadybininkas-agentas kuria ir modifikuoja užduočių sąrašą bei koordinuoja subagentus užduočiai atlikti.

Kad būtų galima teikti AI agentus gamyboje, MAF taip pat apima šias funkcijas:

- **Stebėjimą (Observability)** naudojant OpenTelemetry, kur fiksuojamas kiekvienas AI agente veiksmas, įskaitant įrankių kvietimą, orkestracijos žingsnius, mąstymo srautus ir veiklos stebėjimą per Microsoft Foundry informacines lentas.
- **Saugumą** hostinant agentus tiesiogiai Microsoft Foundry, kuri apima saugumo kontrolę kaip vaidmenų pagrindu prieigos valdymą, privačių duomenų tvarkymą ir įmontuotą turinio saugą.
- **Patvarumą** — agentų gijos ir darbo srautai gali būti pristabdyti, atnaujinti ir atstatyti po klaidų, kas leidžia vykdyti ilgesnius procesus.
- **Valdymą (kontrolę)**, kai palaikomi žmogaus įsikišimo darbo srautai, kuriems užduotys žymimos kaip reikalaujančios žmogaus patvirtinimo.

Microsoft Agent Framework taip pat yra orientuotas į interoperabilumą:

- **Būti debesų nepriklausomu (Cloud-agnostic)** - agentai gali veikti konteineriuose, vietiniame IT tinkle ir skirtinguose debesyse.
- **Būti tiekėjo nepriklausomu (Provider-agnostic)** - agentai gali būti kuriami naudojant jūsų pageidaujamą SDK, pvz., Azure OpenAI ir OpenAI.
- **Integruoti atvirus standartus** - agentai gali naudoti protokolus, tokius kaip Agent-to-Agent (A2A) ir Model Context Protocol (MCP), kad rastų ir naudotų kitus agentus ir įrankius.
- **Įskiepius ir jungtis** - galima jungtis prie duomenų ir atminties paslaugų, tokių kaip Microsoft Fabric, SharePoint, Pinecone ir Qdrant.

Pažiūrėkime, kaip šios funkcijos taikomos kai kurioms pagrindinėms Microsoft Agent Framework koncepcijoms.

## Microsoft Agent Framework pagrindinės koncepcijos

### Agentai

![Agent Framework](../../../translated_images/lt/agent-components.410a06daf87b4fef.webp)

**Agentų kūrimas**

Agentų kūrimas vyksta apibrėžiant išvados paslaugą (LLM tiekėją), instrukcijų rinkinį AI agentui ir priskirtą `name`:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Aukščiau naudojamas `Azure OpenAI`, bet agentai gali būti kuriami naudojant įvairias paslaugas, įskaitant `Microsoft Foundry Agent Service`:

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

arba [MiniMax](https://platform.minimaxi.com/), kuris suteikia OpenAI suderinamą API su dideliais kontekstų langais (iki 204K žetonų):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

arba nuotolinius agentus naudojant A2A protokolą:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Agentų paleidimas**

Agentai paleidžiami naudojant `.run` arba `.run_stream` metodus, priklausomai nuo to, ar atsakymai būtų siunčiami vienu kartu ar srautu.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Kiekvienam agentui gali būti pritaikytos tokios parinktys kaip `max_tokens` (maksimalus žetonų skaičius), `tools` (įrankiai, kuriuos agentas gali naudoti), ir net pats `model` (modelis), naudojamas agentui.

Tai naudinga, kai užduočiai atlikti reikalingi specifiniai modeliai ar įrankiai.

**Įrankiai**

Įrankiai gali būti apibrėžiami tiek agentą kuriant:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Kuriant ChatAgent tiesiogiai

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

tiek paleidžiant agentą:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Įrankis suteiktas tik šiam paleidimui )
```

**Agentų gijos (Threads)**

Agentų gijos naudojamos daugeliui pokalbio posūkių valdyti. Gijos gali būti sukuriamos:

- Naudojant `get_new_thread()` funkciją, kuri leidžia giją išsaugoti ir naudoti vėliau
- Automatiškai kuriant giją paleidžiant agentą, kuri išlieka tik dabartinio paleidimo metu.

Gijos kūrimo pavyzdys:

```python
# Sukurti naują giją.
thread = agent.get_new_thread() # Vykdyti agentą su gija.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Vėliau gija gali būti seralizuojama vėlesniam saugojimui:

```python
# Sukurti naują giją.
thread = agent.get_new_thread() 

# Vykdyti agentą su gija.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serijalizuoti giją saugojimui.

serialized_thread = await thread.serialize() 

# Deserijalizuoti gijos būseną po įkėlimo iš saugyklos.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agentų tarpinis programinis sluoksnis (Middleware)**

Agentai sąveikauja su įrankiais ir LLM užduočių atlikimui. Tam tikrais atvejais norime vykdyti arba sekti veiksmus tarp šių sąveikų. Agentų tarpinis sluoksnis leidžia tai daryti per:

*Funkcinis tarpinis programinis sluoksnis*

Šis sluoksnis leidžia vykdyti veiksmą tarp agentų ir funkcijos/įrankio, kurį agentas kviečia. Pavyzdys – funkcijos kvietimo registravimas (logginimas).

Žemiau `next` nurodo, ar turi būti kviečiamas kitas tarpinio sluoksnio komponentas ar pati funkcija.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Išankstinis apdorojimas: Žurnalas prieš funkcijos vykdymą
    print(f"[Function] Calling {context.function.name}")

    # Tęsti prie kito tarpinio programos sluoksnio arba funkcijos vykdymo
    await next(context)

    # Vėlyvas apdorojimas: Žurnalas po funkcijos vykdymo
    print(f"[Function] {context.function.name} completed")
```

*Pokalbių tarpinis programinis sluoksnis*

Šis sluoksnis leidžia vykdyti arba registruoti veiksmus tarp agentų ir LLM užklausų.

Tai apima svarbią informaciją, pvz., `messages`, siunčiamas AI paslaugai.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Išankstinis apdorojimas: Įrašymas į žurnalą prieš AI kvietimą
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Tęsti kitam tarpininkui arba AI paslaugai
    await next(context)

    # Užbaigiamasis apdorojimas: Įrašymas į žurnalą po AI atsakymo
    print("[Chat] AI response received")

```

**Agentų atmintis**

Kaip parodyta `Agentic Memory` pamokoje, atmintis yra svarbus, kad agentas galėtų veikti skirtinguose kontekstuose. MAF siūlo keletą atminties tipų:

*Laikinoji atmintis (In-Memory Storage)*

Tai atmintis, saugoma gijose programos vykdymo metu.

```python
# Sukurkite naują giją.
thread = agent.get_new_thread() # Vykdykite agentą su gija.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Nuolatinės žinutės (Persistent Messages)*

Ši atmintis naudojama pokalbių istorijai skirtingose sesijose išlaikyti. Ji apibrėžiama per `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Sukurkite pasirinktinių žinučių saugyklą
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dinaminė atmintis (Dynamic Memory)*

Ši atmintis pridedama į kontekstą prieš paleidžiant agentus. Ji gali būti saugoma išorinėse paslaugose, pvz., mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Naudojant Mem0 pažangioms atminties galimybėms
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

**Agentų stebėjimas (Observability)**

Stebėjimas yra svarbus norint kurti patikimas ir lengvai prižiūrimas agentines sistemas. MAF integruojasi su OpenTelemetry, kad teiktų sekimą ir matuoklius geresniam stebėjimui.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # padaryti kažką
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Darbo srautai (Workflows)

MAF siūlo darbo srautus – iš anksto apibrėžtus žingsnius užduočiai atlikti, kur AI agentai yra sudedamosios dalys tų žingsnių viduje.

Darbo srautai susideda iš įvairių komponentų, kurie leidžia geriau valdyti eigos kontrolę. Darbo srautai taip pat leidžia **daugiagentės orkestracijos** ir **patikros taškų (checkpointing)** funkcijas būsenoms išsaugoti.

Pagrindiniai darbo srauto komponentai yra:

**Vykdytojai (Executors)**

Executoriai gauna įėjimo žinutes, atlieka priskirtas užduotis ir generuoja išvesties žinutes, taip stumdami darbo srautą link galutinės užduoties atlikimo. Executoriumi gali būti AI agentas arba pasirinktinė logika.

**Sujungimai (Edges)**

Sujungimai nurodo žinučių srautą darbo sraute. Tai gali būti:

*Tiesioginiai sujungimai (Direct Edges)* – paprasti vienas prie vieno jungimai tarp vykdytojų:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Sąlyginiai sujungimai (Conditional Edges)* – aktyvuojami, kai įvykdoma tam tikra sąlyga. Pvz., kai viešbučių kambariai nepasiekiami, vykdytojas gali pasiūlyti kitus variantus.

*Perjungimo sujungimai (Switch-case Edges)* – maršrutizuoja žinutes skirtingiems vykdytojams pagal apibrėžtas sąlygas. Pvz., jei keliautojas turi prioritetinę prieigą, jo užduotys bus tvarkomos kitu darbo srautu.

*Daugialypiai sujungimai išsklaidymui (Fan-out Edges)* – siunčia vieną žinutę keliems gavėjams.

*Daugialypiai sujungimai surinkimui (Fan-in Edges)* – surenka kelias žinutes iš skirtingų vykdytojų ir siunčia vienam gavėjui.

**Įvykiai (Events)**

Geresniam darbo srautų stebėjimui MAF siūlo įmontuotus vykdymo įvykius, įskaitant:

- `WorkflowStartedEvent`  - darbo srauto vykdymas prasideda
- `WorkflowOutputEvent` - darbo srautas generuoja išvestį
- `WorkflowErrorEvent` - darbo srautas susiduria su klaida
- `ExecutorInvokeEvent`  - vykdytojas pradeda apdorojimą
- `ExecutorCompleteEvent`  - vykdytojas baigia apdorojimą
- `RequestInfoEvent` - iškeliama užklausa

## Pažangūs MAF šablonai

Ankstesnėse sekcijose aptarėme pagrindines Microsoft Agent Framework koncepcijas. Kai kuriate sudėtingesnius agentus, verta atkreipti dėmesį į šiuos pažangius šablonus:

- **Tarpinio programinio sluoksnio komponavimas (Middleware Composition)**: sujunkite kelis tarpinio sluoksnio valdiklius (registravimą, autentifikavimą, užklausų limitavimą) naudojant funkcinius ir pokalbių tarpinio programinio sluoksnio metodus, siekiant tiksliai kontroliuoti agento elgesį.
- **Darbo srautų patikrų taškai (Workflow Checkpointing)**: naudokite darbo srauto įvykius ir seralizaciją, kad išsaugotumėte ir atnaujintumėte ilgai trunkančius agentų procesus.
- **Dinaminis įrankių pasirinkimas (Dynamic Tool Selection)**: derinkite RAG su įrankių aprašymais ir MAF įrankių registraciją, kad pateiktumėte tik aktualius įrankius pagal užklausą.
- **Daugiagentinis perdavimas (Multi-Agent Handoff)**: naudokite darbo srauto sujungimus ir sąlyginius maršrutus orkestruoti užduočių perdavimus tarp specializuotų agentų.

## LangChain / LangGraph agentų talpinimas Microsoft Foundry platformoje

Microsoft Agent Framework yra **naudojamas su kitais pagrindais** — nesate apriboti agentais, parašytais tik MAF. Jei jau turite agentą, sukurtą su **LangChain** arba **LangGraph**, galite jį paleisti kaip **Microsoft Foundry talpinamą agentą**, kad Foundry valdytų vykdymą, sesijas, mastelį, tapatybę ir protokolų galinius taškus, o jūsų agento logika liktų LangGraph.

Tai atliekama naudojant `langchain_azure_ai.agents.hosting` paketą, kuris pateikia kompiliuotą LangGraph diagramą per tuos pačius protokolus, kuriuos naudoja Foundry talpinami agentai.

**1. Įdiekite hosting papildinį:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Hosting papildinys įdiegia Foundry protokolo bibliotekas: `azure-ai-agentserver-responses` (OpenAI suderinamas `/responses` galinis taškas) ir `azure-ai-agentserver-invocations` (bendras `/invocations` galinis taškas).

**2. Pasirinkite talpinimo protokolą:**

| Protokolas | Host klasė | Galinis taškas | Naudojimo atvejis |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Norite OpenAI suderinamo pokalbio su srautu, atsakymų istorija ir pokalbių gijų — rekomenduojamas pokalbių agentams. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Reikia pasirinktinės JSON struktūros, webhook tipo galinio taško ar ne pokalbių apdorojimo. |

Kadangi **Responses API yra pagrindinis Foundry platformos agentų kūrimo API**, daugumai agentų pradėkite nuo `ResponsesHostServer`.

**3. Konfigūruokite aplinkos kintamuosius** (`az login` pirmiausia, kad `DefaultAzureCredential` galėtų autentifikuoti):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Kai agentas vėliau bus paleistas kaip talpinamas Foundry agentas, platforma automatiškai įterpia `FOUNDRY_PROJECT_ENDPOINT`.

**4. Atverkite LangGraph agentą per Responses protokolą:**

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

    # Čia ChatOpenAI taikosi į Foundry projekto OpenAI suderinamą (Responses) galinį tašką.
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

Paleiskite lokaliai su `python main.py`, tada išsiųskite Responses užklausą adresu `http://localhost:8088/responses`.

**Pagrindiniai elgesio bruožai:**

- **Pokalbiai**: klientai tęsia pokalbį perduodami `previous_response_id` arba `conversation` ID. Jei jūsų diagrama sukurta su LangGraph patikros tašku, Foundry susieja pokalbio būseną su patikros tašku (gamyboje naudokite patvarų patikros tašką; `MemorySaver` tinka vietiniam testavimui).
- **Žmogus procese (Human-in-the-loop)**: jei jūsų diagrama naudoja LangGraph `interrupt()`, `ResponsesHostServer` pateikia laukiančią pertrauką kaip Responses `function_call` / `mcp_approval_request` elementą, o klientai tęsia su atitinkamu `function_call_output` / `mcp_approval_response`.
- **Diegimas Foundry platformoje**: naudokite Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (vietinis, reikalauja Docker), tada `azd provision` ir `azd deploy`. Talpinamo agento diegimui reikalinga **Foundry projekto vadovo** rolė.

Šio pavyzdžio paleidžiamą versiją rasite faile [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Pilnas vadovas (Invocations protokolas, pasirinktinės užklausos schemos ir trikčių šalinimas) yra [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Kodo pavyzdžiai 

Microsoft Agent Framework kodo pavyzdžių rasite šioje saugykloje faile `xx-python-agent-framework` ir `xx-dotnet-agent-framework`.

## Daugiau klausimų apie Microsoft Agent Framework?

Prisijunkite prie [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), susitikite su kitais besimokančiais, dalyvaukite konsultacijų valandose ir gaukite atsakymus į savo AI agentų klausimus.
## Ankstesnė pamoka

[Atmintis AI agentams](../13-agent-memory/README.md)

## Kita pamoka

[Kompiuterio naudojimo agentų kūrimas (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->