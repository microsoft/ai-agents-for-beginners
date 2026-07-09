# Microsoft Agent Framework tyrinėjimas

![Agent Framework](../../../translated_images/lt/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Įvadas

Ši pamoka apims:

- Suprasti Microsoft Agent Framework: pagrindines funkcijas ir vertę  
- Tyrinėti Microsoft Agent Framework pagrindines sąvokas
- Pažangūs MAF modeliai: darbo srautai, tarpinė programinė įranga ir atmintis

## Mokymosi tikslai

Baigę šią pamoką mokėsite:

- Kurti gamybai paruoštus AI agentus naudojant Microsoft Agent Framework
- Taikyti pagrindines Microsoft Agent Framework funkcijas savo agentiniams naudojimo atvejams
- Naudoti pažangius modelius, įskaitant darbo srautus, tarpinę programinę įrangą ir stebėjimą

## Kodo pavyzdžiai 

Kodo pavyzdžius, skirtus [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework), galite rasti šiame saugykloje po `xx-python-agent-framework` ir `xx-dotnet-agent-framework` failais.

## Microsoft Agent Framework supratimas

![Framework Intro](../../../translated_images/lt/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) yra Microsoft vieningas pagrindas AI agentams kurti. Jis siūlo lankstumą spręsti įvairias agentinių naudojimo atvejus, pasitaikančius tiek gamybos, tiek tyrimų aplinkose, įskaitant:

- **Sekvencinė agentų orkestravimas** scenarijuose, kuriuose reikia žingsnis po žingsnio darbo srautų.
- **Konkuruojantis orkestravimas** scenarijuose, kai agentai turi atlikti užduotis tuo pačiu metu.
- **Grupinės pokalbių orkestravimas** scenarijuose, kai agentai gali bendradarbiauti vienoje užduotyje.
- **Perdavimų orkestravimas** scenarijuose, kai agentai perduoda užduotį vienas kitam atlikus tarpinius darbus.
- **Magnetinis orkestravimas** scenarijuose, kai valdymo agentas kuria ir keičia užduočių sąrašą bei koordinuoja padagents užduoties įgyvendinimui.

Siekiant pristatyti AI agentus gamyboje, MAF taip pat turi funkcijas:

- **Stebėjimui** naudojant OpenTelemetry, kur kiekvienas AI agento veiksmas, įskaitant įrankių kvietimą, orkestracijos žingsnius, samprotavimų srautus ir našumo stebėjimą per Microsoft Foundry valdymo skydelius, yra stebimas.
- **Saugumui**, talpinant agentus natūraliai Microsoft Foundry, kuris apima saugumo valdymą, pavyzdžiui, vaidmenimis pagrįstą prieigą, privačių duomenų tvarkymą ir integruotą turinio saugumą.
- **Atsparumui**, nes agentų gijos ir darbo srautai gali pristabdyti, atnaujinti ir atsigauti po klaidų, todėl palaikomas ilgesnis veikimo procesas.
- **Kontroliavimui**, nes palaikomi žmogiškos kontrolės darbo srautai, kuriuose užduotys žymimos kaip reikalaujančios žmogaus patvirtinimo.

Microsoft Agent Framework taip pat orientuojasi į sąveikumą:

- **Debesų nepriklausomumą** - agentai gali veikti konteineriuose, vietinėje aplinkoje ir keliuose skirtinguose debesyse.
- **Tiekėjo nepriklausomumą** - agentai gali būti sukurti per jūsų pageidaujamą SDK, įskaitant Azure OpenAI ir OpenAI
- **Atviro standarto integraciją** - agentai gali naudoti protokolus, tokius kaip Agent-to-Agent (A2A) ir Model Context Protocol (MCP), kad surastų ir naudotų kitus agentus bei įrankius.
- **Įskiepius ir jungtis** - galima jungtis prie duomenų ir atminties paslaugų, tokių kaip Microsoft Fabric, SharePoint, Pinecone ir Qdrant.

Pažiūrėkime, kaip šios funkcijos taikomos kai kurioms pagrindinėms Microsoft Agent Framework sąvokoms.

## Microsoft Agent Framework pagrindinės sąvokos

### Agentai

![Agent Framework](../../../translated_images/lt/agent-components.410a06daf87b4fef.webp)

**Agentų kūrimas**

Agentų kūrimas vykdomas apibrėžiant išvesties paslaugą (LLM teikėją), 
instrukcijų rinkinį AI agentui vykdyti ir priskirtą `vardą`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Aukščiau naudojama `Azure OpenAI`, bet agentai gali būti kuriami naudojant įvairias paslaugas, įskaitant `Microsoft Foundry Agent Service`:

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

arba [MiniMax](https://platform.minimaxi.com/), kuris teikia su OpenAI suderinamą API su dideliais konteksto langais (iki 204 tūkst. žetonų):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

arba nuotolinius agentus, naudojant A2A protokolą:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Agentų paleidimas**

Agentai paleidžiami naudojant `.run` arba `.run_stream` metodus, skirtingai, ar reikia ne srautinio, ar srautinio atsakymo.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Kiekvienam agento paleidimui galima pasirinkti ir pritaikyti parametrus, tokius kaip naudojamų `max_tokens`, tais įrankius (`tools`), kuriuos agentas gali kviesti, ir net patį agento naudojamą `modelį`.

Tai naudinga situacijose, kai užduočiai atlikti reikalingi specifiniai modeliai ar įrankiai.

**Įrankiai**

Įrankiai gali būti apibrėžiami tiek kuriant agentą:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Kai tiesiogiai kuriamas ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

ir taip pat paleidžiant agentą:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Įrankis skirtas naudoti tik šiam vykdymui )
```

**Agentų gijos**

Agentų gijomis tvarkomos daugkartinės pokalbių eilės. Gijos gali būti sukuriamos:

- Naudojant `get_new_thread()`, kuris leidžia giją išsaugoti laikui bėgant
- Automatiškai sukuriant giją paleidžiant agentą ir gija egzistuojanti tik per einamąjį paleidimą.

Siekiant sukurti giją, kodas atrodo taip:

```python
# Sukurkite naują giją.
thread = agent.get_new_thread() # Vykdykite agentą su gija.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Giją galima serializuoti ir išsaugoti vėlesniam naudojimui:

```python
# Sukurkite naują giją.
thread = agent.get_new_thread() 

# Paleiskite agentą su gija.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serializuokite giją saugojimui.

serialized_thread = await thread.serialize() 

# Deserializuokite gijos būseną po įkėlimo iš saugyklos.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agentų tarpinė programinė įranga**

Agentai sąveikauja su įrankiais ir LLM, kad atliktų naudotojo užduotis. Tam tikrose situacijose norime vykdyti arba sekti veiksmus tarp šių sąveikų. Agentų tarpinė programinė įranga leidžia tai padaryti per:

*Funkcinę tarpinę programinę įrangą*

Ši tarpinė programinė įranga leidžia vykdyti veiksmą tarp agento ir funkcijos/įrankio, kurį jis kvies. Pavyzdys, kada tai būtų naudinga, yra kai norima atlikti žurnalizavimą kviečiant funkciją.

Žemiau pateiktame kode `next` nusako, ar turėtų būti kviečiama kita tarpinė programinė įranga, ar pati funkcija.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Išankstinis apdorojimas: Įrašymas prieš funkcijos vykdymą
    print(f"[Function] Calling {context.function.name}")

    # Tęsti į kitą tarpinį programinį sluoksnį arba funkcijos vykdymą
    await next(context)

    # Po apdorojimo: Įrašymas po funkcijos vykdymo
    print(f"[Function] {context.function.name} completed")
```

*Pokalbių tarpinė programinė įranga*

Ši tarpinė programinė įranga leidžia vykdyti arba žurnaluoti veiksmus tarp agento ir LLM užklausų.

Joje yra svarbi informacija, pvz., `pranešimai` siunčiami AI paslaugai.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Išankstinis apdorojimas: žurnalas prieš kviečiant DI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Tęsti prie kito tarpinio programos sluoksnio arba DI paslaugos
    await next(context)

    # Po apdorojimo: žurnalas po DI atsakymo
    print("[Chat] AI response received")

```

**Agentų atmintis**

Kaip aptarta pamokoje `Agentic Memory`, atmintis yra svarbus elementas leidžiantis agentui veikti skirtinguose kontekstuose. MAF siūlo kelias atminties rūšis:

*Vidinė atmintis*

Tai atmintis, saugoma gijų metu programos vykdymo metu.

```python
# Sukurti naują giją.
thread = agent.get_new_thread() # Paleisti agentą su gija.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Pastovūs pranešimai*

Ši atmintis naudojama kalbos istorijai saugoti per skirtingas sesijas. Ji apibrėžiama naudojant `chat_message_store_factory`:

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

*Dinaminė atmintis*

Ši atmintis pridedama į kontekstą prieš paleidžiant agentus. Ši atmintis gali būti saugoma išorinėse paslaugose, tokiose kaip mem0:

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

**Agentų stebėjimas**


Stebėjimas yra svarbus kuriant patikimas ir lengvai prižiūrimas agentines sistemas. MAF integruojasi su OpenTelemetry, kad suteiktų sekimą ir skaitiklius geresniam stebėjimui.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # daryti kažką
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Darbo srautai

MAF siūlo darbo srautus, kurie yra iš anksto apibrėžti žingsniai užduočiai atlikti ir į kuriuos įtraukti AI agentai kaip komponentai šiuose žingsniuose.

Darbo srautai susideda iš skirtingų komponentų, kurie leidžia geresnę kontrolės eigą. Darbo srautai taip pat leidžia **daugiagentinę orkestraciją** ir **patikros taškų kūrimą**, kad būtų išsaugotos darbo srautų būsenos.

Pagrindiniai darbo srauto komponentai yra:

**Vykdytojai**

Vykdytojai gauna įvesties pranešimus, atlieka paskirtas užduotis ir tada sukuria išeities pranešimą. Tai stumia darbo srautą į priekį link didesnės užduoties užbaigimo. Vykdytojai gali būti arba AI agentai, arba pasirinktinė logika.

**Kraštai**

Kraštai naudojami apibrėžti pranešimų srautą darbo sraute. Tai gali būti:

*Tiesioginiai kraštai* – paprasti vienas prie vieno ryšiai tarp vykdytojų:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Sąlyginiai kraštai* – aktyvuojami po tam tikros sąlygos įvykdymo. Pavyzdžiui, kai viešbučių kambariai neprieinami, vykdytojas gali pasiūlyti kitus variantus.

*Perjungimo atvejis kraštai* – nukreipia pranešimus skirtingiems vykdytojams pagal apibrėžtas sąlygas. Pavyzdžiui, jei keliautojas turi prioritetinę prieigą, jų užduotys bus tvarkomos per kitą darbo srautą.

*Išsiuntimo kraštai* – siunčia vieną pranešimą keliems tikslams.

*Suvokimo kraštai* – surenka kelis pranešimus iš skirtingų vykdytojų ir siunčia vienam tikslui.

**Įvykiai**

Norint suteikti geresnį darbo srautų stebėjimą, MAF siūlo įmontuotus vykdymo įvykius, įskaitant:

- `WorkflowStartedEvent` - darbo srauto vykdymas prasideda
- `WorkflowOutputEvent` - darbo srautas sugeneruoja išeitį
- `WorkflowErrorEvent` - darbo srautas susiduria su klaida
- `ExecutorInvokeEvent` - vykdytojas pradeda apdorojimą
- `ExecutorCompleteEvent` - vykdytojas baigia apdorojimą
- `RequestInfoEvent` - išduodamas užklausimas

## Išplėstiniai MAF modeliai

Aukščiau aprašytos pagrindinės Microsoft Agent Framework sąvokos. Kai kuriate sudėtingesnius agentus, štai keletas pažangių modelių, kuriuos verta apsvarstyti:

- **Tarpinės programinės įrangos sudėtis**: susiekite kelis tarpinės programinės įrangos tvarkyklius (klausų registravimas, autentifikacija, greičio ribojimas) naudodami funkcijų ir pokalbių tarpinę programinę įrangą, kad gautumėte smulkų agento elgesio valdymą.
- **Darbo srauto patikros taškai**: naudokite darbo srautų įvykius ir serializavimą, kad išsaugotumėte ir atnaujintumėte ilgai trunkančius agento procesus.
- **Dinaminis įrankių pasirinkimas**: derinkite RAG pagal įrankių aprašus su MAF įrankių registracija, kad būtų pateikti tik aktualūs įrankiai kiekvienam užklausimui.
- **Daugiagentinis perdavimas**: naudokite darbo srautų kraštus ir sąlyginius nukreipimus, kad koordinuotumėte perdavimą tarp specializuotų agentų.

## LangChain / LangGraph agentų talpinimas Microsoft Foundry platformoje

Microsoft Agent Framework yra **framework-nesuderinamas** — nesate ribojami agentais, parašytais su MAF. Jei jau turite agentą, sukurtą su **LangChain** arba **LangGraph**, galite paleisti jį kaip **Microsoft Foundry talpinamą agentą**, todėl Foundry platforma valdo vykdymo laiką, sesijas, mastelį, tapatybę ir protokolo galinius taškus, o jūsų agento logika lieka LangGraph.

Tai atliekama naudojant `langchain_azure_ai.agents.hosting` paketą, kuris atskleidžia kompiliuotą LangGraph grafinį modelį per tuos pačius protokolus, kuriuos naudoja Foundry talpinami agentai.

**1. Įdiekite talpinimo papildinį:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` papildinys įdiegia Foundry protokolo bibliotekas: `azure-ai-agentserver-responses` (OpenAI suderinamas `/responses` galinis taškas) ir `azure-ai-agentserver-invocations` (bendras `/invocations` galinis taškas).

**2. Pasirinkite talpinimo protokolą:**

| Protokolas | Talpyklos klasė | Galinis taškas | Naudojimo atvejis |
|----------|-----------------|----------------|-------------------|
| **Responses** | `ResponsesHostServer` | `/responses` | Norite suderinamo su OpenAI pokalbio, srautinio perdavimo, atsakymų istorijos ir pokalbio susiuvimo – rekomenduojamas numatytasis variantas pokalbių agentams. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Reikia pasirinktinio JSON formato, webhook tipo galinio taško arba nesikalbančio apdorojimo. |

Kadangi **Responses API yra pagrindinis Foundry agentinio stiliaus kūrimo API**, daugumai agentų pradėkite nuo `ResponsesHostServer`.

**3. Konfigūruokite aplinkos kintamuosius** (`az login` pirmiausia, kad `DefaultAzureCredential` galėtų autentifikuoti):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

Kai agentas vėliau veiks kaip talpinamas agentas Foundry platformoje, platforma automatiškai įterps `FOUNDRY_PROJECT_ENDPOINT`.

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
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-4.1")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # Čia ChatOpenAI taikosi į Foundry projekto OpenAI suderinamą (Atsakymai) galinį tašką.
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

Paleiskite lokaliai su `python main.py`, tada siųskite Responses užklausą adresu `http://localhost:8088/responses`.

**Pagrindiniai elgesiai:**

- **Pokalbiai**: klientai tęsia pokalbį perduodami `previous_response_id` arba `conversation` ID. Jei jūsų grafas sukompiliuotas su LangGraph patikros tašku, Foundry pririša pokalbio būseną prie patikros taško (naudokite patvarų patikros tašką produkcijoje; `MemorySaver` tinka vietiniam testavimui).
- **Žmogus intervencijoje**: jei jūsų grafas naudoja LangGraph `interrupt()`, `ResponsesHostServer` rodo laukiančią pertrauką kaip Responses `function_call` / `mcp_approval_request` elementą, o klientai tęsia su atitinkamu `function_call_output` / `mcp_approval_response`.
- **Diegimas į Foundry**: naudokite Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokaliai, reikia Docker), tada `azd provision` ir `azd deploy`. Talpinamo agento diegimui reikalinga **Foundry Project Manager** rolė.

Veikianti šio pavyzdžio versija yra [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Pilną vadovą (Invocations protokolas, pasirinktinės užklausos schemos ir trikčių šalinimas) žr. [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Kodo Pavyzdžiai 

Microsoft Agent Framework kodo pavyzdžiai yra šiame saugykloje po `xx-python-agent-framework` ir `xx-dotnet-agent-framework` failais.

## Turite daugiau klausimų apie Microsoft Agent Framework?

Prisijunkite prie [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kad susitikti su kitais besimokančiais, dalyvauti darbo valandose ir gauti atsakymus į savo AI agentų klausimus.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->