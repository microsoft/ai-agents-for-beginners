# Microsoft Agent Framework tyrinėjimas

![Agent Framework](../../../translated_images/lt/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Įvadas

Šioje pamokoje aptarsime:

- Microsoft Agent Framework supratimą: pagrindines funkcijas ir vertę  
- Microsoft Agent Framework pagrindinių koncepcijų tyrinėjimą
- Pažangius MAF modelius: darbo eigos, tarpinę programinę įrangą ir atmintį

## Mokymosi Tikslai

Baigę šią pamoką žinosite, kaip:

- Kurti gamybai paruoštus dirbtinio intelekto agentus naudojant Microsoft Agent Framework
- Taikyti pagrindines Microsoft Agent Framework funkcijas jūsų agentinėms naudojimo situacijoms
- Naudoti pažangius modelius, įskaitant darbo eigas, tarpinę programinę įrangą ir stebėjimą

## Kodo Pavyzdžiai 

Kodo pavyzdžius Microsoft Agent Framework (MAF) rasite šiame saugykloje failese `xx-python-agent-framework` ir `xx-dotnet-agent-framework`.

## Microsoft Agent Framework supratimas

![Framework Intro](../../../translated_images/lt/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) yra „Microsoft“ vieningas dirbtinio intelekto agentų kūrimo karkasas. Jis siūlo lankstumą spręsti plačią agentinių naudojimo atvejų įvairovę, kuri pasitaiko tiek gamybos, tiek mokslinių tyrimų aplinkose:

- **Sekvencinė agentų orkestracija** scenarijuose, kur reikia eiliškų darbo eigos žingsnių.
- **Vienalaikė orkestracija** scenarijuose, kai agentai turi vienu metu atlikti užduotis.
- **Grupinio pokalbio orkestracija** scenarijuose, kai agentai gali bendradarbiauti atliekant vieną užduotį.
- **Užduočių perdavimo orkestracija** scenarijuose, kai agentai perduoda užduotį vienas kitam, baigus po užduotis.
- **Magnetinė orkestracija** scenarijuose, kai vadovaujantis agentas kuria ir keičia užduočių sąrašą bei koordinuoja pagalagentus tam, kad užbaigtų užduotį.

Siekiant pristatyti AI agentus gamybai, MAF taip pat apima funkcijas:

- **Stebėjimą** naudojant OpenTelemetry, kur stebima kiekviena AI agente atlikta veiksmas, įskaitant įrankių kvietimus, orkestravimo žingsnius, sprendimų srautus ir našumo stebėjimą per Microsoft Foundry informacines lentas.
- **Saugumą** – agentai yra palaikomi tiesiogiai Microsoft Foundry, kuri teikia saugumo kontrolę, tokią kaip, vaidmenų pagrindu prieigos valdymas, privačių duomenų tvarkymas ir integruotas turinio saugumas.
- **Tvirtumą**, nes agentų gijos ir darbo eigos gali būti pristabdytos, atnaujintos ir atkurtos iš klaidų, leidžiančios vykdyti ilgo laikotarpio procesus.
- **Valdymą** – palaikomos žmogiškojo valdymo darbo eigos, kai užduotys pažymimos kaip reikalaujančios žmogaus patvirtinimo.

Microsoft Agent Framework taip pat orientuotas į tarpusavio veikimą:

- **Būdamas debesų agnostiškas** – agentai gali veikti konteineriuose, vietoje ir keliuose skirtinguose debesyse.
- **Būdamas tiekėjų agnostiškas** – agentai gali būti kuriami naudojant jūsų pageidaujamą SDK, įskaitant Azure OpenAI ir OpenAI.
- **Integruojant atvirus standartus** – agentai gali naudoti protokolus, tokius kaip Agent-to-Agent (A2A) ir Model Context Protocol (MCP), kad atrastų ir naudotų kitus agentus bei įrankius.
- **Papildinius ir jungtis** – galima jungtis prie duomenų ir atminties paslaugų, tokių kaip Microsoft Fabric, SharePoint, Pinecone ir Qdrant.

Pažiūrėkime, kaip šios funkcijos taikomos pagrindinėms Microsoft Agent Framework koncepcijoms.

## Microsoft Agent Framework pagrindinės koncepcijos

### Agentai

![Agent Framework](../../../translated_images/lt/agent-components.410a06daf87b4fef.webp)

**Agentų kūrimas**

Agentų kūrimas vykdomas apibrėžiant išvedimo paslaugą (LLM tiekėją), 
instrukcijų rinkinį AI agentui vykdyti ir priskiriamą `pavadinimą`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Aukščiau naudojamas `Azure OpenAI`, bet agentai gali būti kuriami naudojant įvairias paslaugas, tarp jų ir `Microsoft Foundry Agent Service`:

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

arba [MiniMax](https://platform.minimaxi.com/), kuris siūlo OpenAI suderinamą API su dideliais konteksto langais (iki 204K žetonų):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

arba nuotolinius agentus, naudojant A2A protokolą:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Agentų paleidimas**

Agentai paleidžiami naudojant `.run` arba `.run_stream` metodus, skirta ne srautinėms arba srautinėms atsakų versijoms.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Kiekvienam agentui paleidžiant taip pat galima nurodyti parinktis, tokias kaip agento naudojamų `max_tokens`, agento galimų iškviesti `tools` ir net paties naudojamo `model`.

Tai naudinga atvejais, kai tam tikri modeliai ar įrankiai yra būtini vartotojo užduočiai atlikti.

**Įrankiai**

Įrankiai gali būti apibrėžiami tiek aprašant agentą:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Kai kuriamas ChatAgent tiesiogiai

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

tiek paleidžiant agentą:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Įrankis suteiktas tik šiam vykdymui )
```

**Agentų gijos**

Agentų gijos naudojamos daugiafunkcinių pokalbių valdymui. Gijos gali būti sukuriamos:

- Naudojant `get_new_thread()`, kas leidžia giją išsaugoti laikui bėgant
- Automatiškai sukuriant giją paleidžiant agentą, kuri egzistuoja tik pažangos metu

Gijos kūrimas atrodo taip:

```python
# Sukurkite naują giją.
thread = agent.get_new_thread() # Paleiskite agentą su šia gija.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Giją galima serializuoti ir išsaugoti ateičiai:

```python
# Sukurkite naują giją.
thread = agent.get_new_thread() 

# Vykdykite agentą su gija.

response = await agent.run("Hello, how are you?", thread=thread) 

# Seralizuokite giją saugojimui.

serialized_thread = await thread.serialize() 

# Deserializuokite gijos būseną po įkėlimo iš saugyklos.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agentų tarpinė programinė įranga**

Agentai sąveikauja su įrankiais ir LLM, kad atliktų vartotojo užduotis. Tam tikrais atvejais reikia vykdyti arba stebėti šias sąveikas. Agentų tarpinė programinė įranga leidžia tai padaryti per:

*Funkcinę tarpinę programinę įrangą*

Ši tarpinė programinė įranga leidžia vykdyti veiksmą tarp agento ir funkcijos/įrankio, kurį agentas kvies. Pavyzdys yra tokiu atveju, kai norima atlikti žurnalo įrašymą apie funkcijos kvietimą.

Žemiau pateiktame kode `next` nurodo, ar turi būti iškviečiama kita tarpinė programinė įranga, ar pati funkcija.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Išankstinis apdorojimas: žurnalas prieš funkcijos vykdymą
    print(f"[Function] Calling {context.function.name}")

    # Tęsti iki kito tarpinio programos sluoksnio arba funkcijos vykdymo
    await next(context)

    # Po apdorojimo: žurnalas po funkcijos vykdymo
    print(f"[Function] {context.function.name} completed")
```

*Pokalbių tarpinė programinė įranga*

Ši tarpinė programinė įranga leidžia vykdyti ar registruoti veiksmus tarp agento ir LLM užklausų.

Joje yra svarbi informacija, pavyzdžiui, `messages`, siunčiami AI paslaugai.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Išankstinis apdorojimas: Žurnalas prieš kviečiant DI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Tęsti kitam tarpinio sluoksnio arba DI paslaugai
    await next(context)

    # Po apdorojimo: Žurnalas po DI atsakymo
    print("[Chat] AI response received")

```

**Agentų atmintis**

Kaip aptarta pamokoje `Agentinė atmintis`, atmintis yra svarbus elementas leidžiantis agentui dirbti įvairiuose kontekstuose. MAF siūlo kelis atminties tipus:

*Atmintis atmintyje*

Tai atmintis saugoma gijų metu programos veikimo metu.

```python
# Sukurti naują giją.
thread = agent.get_new_thread() # Vykdyti agentą su gija.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Išliekantys pranešimai*

Ši atmintis naudojama saugoti pokalbio istoriją skirtingų sesijų metu. Ji aprašoma naudojant `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Sukurkite pasirinktinių pranešimų saugyklą
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dinaminė atmintis*

Ši atmintis pridedama prie konteksto prieš paleidžiant agentus. Ši atmintis gali būti saugoma išorinėse paslaugose, pavyzdžiui, mem0:

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

Stebėjimas yra svarbus kuriant patikimas ir prižiūrimas agentines sistemas. MAF integruojasi su OpenTelemetry, kad suteiktų sekimą ir matuoklius geresniam stebėjimui.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # padaryti ką nors
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Darbo eigos

MAF siūlo darbo eigas – iš anksto apibrėžtus žingsnius užduočiai atlikti, įtraukiant AI agentus kaip žingsnių komponentus.

Darbo eigos susideda iš įvairių komponentų, leidžiančių geriau valdyti srautus. Darbo eigos taip pat leidžia **daugiaagentinę orkestraciją** ir **punkto patikrinimą**, kad būtų išsaugotos darbo eigos būsenos.

Pagrindiniai darbo eigos komponentai yra:

**Vykdytojai**

Vykdytojai gauna įėjimo pranešimus, atlieka priskirtas užduotis ir sukuria išėjimo pranešimą. Tai juda darbo eigą link didesnės užduoties užbaigimo. Vykdytojai gali būti dirbtinio intelekto agentai arba pasirinktinė logika.

**Sąsajos (Edges)**

Sąsajos naudojamos apibrėžti pranešimų srautą darbo eigoje. Jos gali būti:

*Tiesioginės sąsajos* – Paprasti vienas prie vieno jungimai tarp vykdytojų:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Sąlyginės sąsajos* – Aktyvuojamos, kai pateikiama tam tikra sąlyga. Pavyzdžiui, kai viešbučių kambariai yra neprieinami, vykdytojas gali pasiūlyti kitas galimybes.

*Perjungimo sąsajos (Switch-case)* – Maršrutuoti pranešimus skirtingiems vykdytojams pagal apibrėžtas sąlygas. Pavyzdžiui, jei keliautojas turi prioritetinę prieigą, jo užduotys bus tvarkomos per kitą darbo eigą.

*Išsklaidymo sąsajos* – Siųsti vieną pranešimą keliems gavėjams.

*Suvartojimo sąsajos* – Surinkti kelis pranešimus iš skirtingų vykdytojų ir nusiųsti vienam gavėjui.

**Įvykiai**

Siekiant geresnio stebėjimo darbo eigose, MAF siūlo integruotus vykdymo įvykius, tokius kaip:

- `WorkflowStartedEvent`  – darbo eigos vykdymas prasideda
- `WorkflowOutputEvent` – darbo eiga generuoja išėjimą
- `WorkflowErrorEvent` – darbo eiga susiduria su klaida
- `ExecutorInvokeEvent`  – vykdytojas pradeda apdorojimą
- `ExecutorCompleteEvent`  – vykdytojas baigia apdorojimą
- `RequestInfoEvent` – pateikiama užklausa

## Pažangūs MAF modeliai

Aukščiau aptarti pagrindiniai Microsoft Agent Framework konceptai. Kuriant sudėtingesnius agentus, verta apsvarstyti šiuos pažangius modelius:

- **Tarpinės programinės įrangos derinys**: kelių tarpinės programinės įrangos tvarkyklių (žurnalo rašymas, autentifikacija, eismo ribojimas) sujungimas naudojant funkcijų ir pokalbių tarpinę programinę įrangą, siekiant detalaus agentų valdymo.
- **Darbo eigos punkto patikrinimas**: naudokite darbo eigos įvykius ir serializavimą išsaugoti ir atnaujinti ilgalaikius agentų procesus.
- **Dinaminis įrankių pasirinkimas**: derinkite RAG pagal įrankių aprašymus su MAF įrankių registracija, kad pristatytumėte tik aktualius įrankius užklausai.
- **Daugiaagentinis perdavimas**: naudokite darbo eigos sąsajas ir sąlyginius maršrutus orkestruoti perdavimus tarp specializuotų agentų.

## LangChain / LangGraph agentų talpinimas Microsoft Foundry

Microsoft Agent Framework yra **framework-interoperabilus** — jums nėra ribojimų naudoti tik MAF rašytus agentus. Jei jau turite agentą parašytą su **LangChain** arba **LangGraph**, galite paleisti jį kaip **Microsoft Foundry talpinamą agentą**, kad Foundry valdyti vykdymą, sesijas, mastelį, tapatybę ir protokolo galinius taškus, o jūsų agento logika liktų LangGraph.

Tai daroma naudojant `langchain_azure_ai.agents.hosting` paketą, kuris pateikia kompiliuotą LangGraph schemą per tuos pačius protokolus, kuriuos naudoja Foundry talpinami agentai.

**1. Įdiekite hosting papildinį:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Hosting papildinys įdiegia Foundry protokolo bibliotekas: `azure-ai-agentserver-responses` (OpenAI suderinamas `/responses` galinis taškas) ir `azure-ai-agentserver-invocations` (bendras `/invocations` galinis taškas).

**2. Pasirinkite hosting protokolą:**

| Protokolas | Host klasė | Galinis taškas | Naudokite kai |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Norite OpenAI suderinamo pokalbių, srautų, atsakymų istorijos ir pokalbio gijų – rekomenduojama daugumai pokalbių agentų. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Reikia pritaikytos JSON struktūros, webhook stiliaus galinio taško arba nesikalbinių procesų. |

Kadangi **Responses API yra pagrindinė agentų raidos API Foundry**, daugumai agentų pradėkite nuo `ResponsesHostServer`.

**3. Sukonfigūruokite aplinkos kintamuosius** (`az login`, kad `DefaultAzureCredential` galėtų autentifikuotis):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

Kai agentas vėliau paleidžiamas Foundry kaip talpinamas agentas, platforma automatiškai įterpia `FOUNDRY_PROJECT_ENDPOINT`.

**4. Pateikite LangGraph agentą per Responses protokolą:**

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

Vykdykite lokaliai su `python main.py`, tada nusiųskite Responses užklausą adresu `http://localhost:8088/responses`.

**Pagrindiniai elgesiai:**

- **Pokalbiai**: Klientai tęsia pokalbį perduodami `previous_response_id` arba `conversation` ID. Jei jūsų schema sukompiliuota su LangGraph punkto tikrinimo įrankiu, Foundry sieja pokalbio būseną su punktu (prodokcijoje naudokite tvirtą tikrinimo įrankį; `MemorySaver` tinka vietiniam testavimui).
- **Žmogus proceso viduryje**: Jei jūsų schema naudoja LangGraph `interrupt()`, `ResponsesHostServer` perteikia laukiančią pertrauką kaip Responses `function_call` / `mcp_approval_request` elementą, o klientai tęsia su atitinkamu `function_call_output` / `mcp_approval_response`.
- **Diegimas į Foundry**: Naudokite Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (vietinis, reikalauja Docker), tada `azd provision` ir `azd deploy`. Talpinamų agentų diegimui reikalinga **Foundry Project Manager** rolė.

Šio pavyzdžio veikianti versija yra [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Pilnai instrukcijai (Invocations protokolas, įprastinės schema, trikčių šalinimas) žr. [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Kodo Pavyzdžiai 

Kodo pavyzdžius Microsoft Agent Framework rasite šiame saugykloje failese `xx-python-agent-framework` ir `xx-dotnet-agent-framework`.

## Turite daugiau klausimų apie Microsoft Agent Framework?

Prisijunkite prie [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kad susitiktumėte su kitais besimokančiais, dalyvautumėte konsultacijose ir gautumėte atsakymus į savo AI agentų klausimus.
## Ankstesnė pamoka

[Atmintis dirbtinio intelekto agentams](../13-agent-memory/README.md)

## Tolimesnė pamoka

[Kompiuterio naudojimo agentų kūrimas (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->