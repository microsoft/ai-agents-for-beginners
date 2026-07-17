# Raziščemo Microsoft Agent Framework

![Agent Framework](../../../translated_images/sl/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Uvod

Ta lekcija bo zajemala:

- Razumevanje Microsoft Agent Framework: Ključne funkcije in vrednost  
- Raziščemo ključne koncepte Microsoft Agent Framework
- Napredni MAF vzorci: delovni tokovi, middleware in pomnilnik

## Cilji učenja

Po zaključku te lekcije boste znali:

- Ustvariti produkcijsko pripravljene AI agente z uporabo Microsoft Agent Framework
- Uporabiti osnovne funkcije Microsoft Agent Framework za vaše agentne primere uporabe
- Uporabiti napredne vzorce, vključno z delovnimi tokovi, middleware in opazovanjem

## Vzorce kode 

Vzorci kode za [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) so na voljo v tem repozitoriju pod datotekami `xx-python-agent-framework` in `xx-dotnet-agent-framework`.

## Razumevanje Microsoft Agent Framework

![Framework Intro](../../../translated_images/sl/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) je Microsoftov enotni okvir za gradnjo AI agentov. Ponuja prilagodljivost za različne agentne primere uporabe, tako v produkcijskih kot raziskovalnih okoljih, vključno z:

- **Zaporedna orkestracija agentov** v primerih, kjer so potrebni postopni delovni tokovi.
- **Vzporedna orkestracija** v primerih, kjer agenti opravijo naloge istočasno.
- **Orkestracija skupinskega klepeta** v primerih, ko lahko agenti sodelujejo na eni nalogi.
- **Predaja nalog** v primerih, ko agenti predajajo nalogo drug drugemu, ko so podnaloge opravljene.
- **Magnetna orkestracija** v primerih, kjer vodja agent ustvarja in spreminja seznam nalog ter usklajuje podagente za dokončanje naloge.

Za zagotavljanje AI agentov v produkciji ima MAF vključenih tudi funkcije za:

- **Opazovanje** preko uporabe OpenTelemetry, kjer so zajete vse akcije AI agenta, vključno z uporabo orodij, koraki orkestracije, procesi razmišljanja in spremljanja učinkovitosti preko Microsoft Foundry nadzornih plošč.
- **Varnost** z gostovanjem agentov naravno na Microsoft Foundry, ki vključuje varnostne kontrole, kot so dostop, temelječ na vlogah, upravljanje zasebnih podatkov in vgrajena varnost vsebin.
- **Vzdržljivost** saj se lahko niti agentov in delovni tokovi ustavijo, nadaljujejo in obnovijo po napakah, kar omogoča daljše izvajanje procesov.
- **Nadzor**, saj so podprti delovni tokovi z vključenostjo človeka, kjer so naloge označene kot zahtevajo odobritev človeka.

Microsoft Agent Framework je tudi osredotočen na medsebojno delovanje z:

- **Biti neodvisen od oblaka** - Agentje lahko tečejo v vsebnikih, na kraju samem in preko več različnih oblakov.
- **Biti neodvisen od ponudnika** - Agentje so lahko ustvarjeni preko izbranega SDK, vključno z Azure OpenAI in OpenAI
- **Integracija odprtih standardov** - Agentje lahko uporabljajo protokole, kot so Agent-to-Agent (A2A) in Model Context Protocol (MCP), za odkrivanje in uporabo drugih agentov in orodij.
- **Vtičniki in priključki** - Možne so povezave s podatkovnimi in pomnilniškimi storitvami, kot so Microsoft Fabric, SharePoint, Pinecone in Qdrant.

Poglejmo, kako so te funkcije uporabljene pri nekaterih glavnih konceptih Microsoft Agent Framework.

## Ključni koncepti Microsoft Agent Framework

### Agenti

![Agent Framework](../../../translated_images/sl/agent-components.410a06daf87b4fef.webp)

**Ustvarjanje agentov**

Ustvarjanje agenta poteka z definiranjem storitve sklepanja (LLM ponudnik), 
nabora navodil, ki jih AI agent sledi, in dodeljenega `imena`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Zgornji primer uporablja `Azure OpenAI`, vendar lahko agente ustvarite z različnimi storitvami, vključno z `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI API-ji `Responses`, `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ali [MiniMax](https://platform.minimaxi.com/), ki nudi združljiv API z OpenAI z velikimi kontekstnimi okni (do 204K tokenov):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ali oddaljene agente z uporabo protokola A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Zagon agentov**

Agente zaženemo z metodama `.run` ali `.run_stream` za nestrimene ali strimene odzive.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Vsak zagon agenta lahko vključuje tudi možnosti za prilagoditev parametrov, kot so `max_tokens`, orodja `tools`, ki jih lahko agent kliče, in celo model `model`, ki ga agent uporablja.

To je uporabno, kadar so za opravljanje uporabniške naloge potrebni določeni modeli ali orodja.

**Orodja**

Orodja lahko definiramo tako pri definiranju agenta:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Ko ustvarjate ChatAgent neposredno

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

kot tudi pri zagonu agenta:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Orodje je na voljo samo za to izvedbo )
```

**Nitke agentov**

Nitke agentov se uporabljajo za večkratne pogovore (multi-turn). Nitke lahko ustvarimo bodisi z:

- Uporabo `get_new_thread()`, ki omogoča, da se nit shrani skozi čas
- Samodejnim ustvarjanjem nitke ob zagonu agenta, ki traja le med trenutnim zagonom.

Kodo za ustvarjanje nitke je videti takole:

```python
# Ustvari novo nit.
thread = agent.get_new_thread() # Zaženi agenta z nitjo.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Nato nitko lahko serializirate za shranjevanje in kasnejšo uporabo:

```python
# Ustvari novo nit.
thread = agent.get_new_thread() 

# Zaženi agenta z nitjo.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serializiraj nit za shranjevanje.

serialized_thread = await thread.serialize() 

# Deserializiraj stanje niti po nalaganju iz shrambe.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware agentov**

Agenti sodelujejo z orodji in LLM-ji za opravljanje uporabniških nalog. V določenih primerih želimo izvajati ali slediti tej interakciji med agentom in orodjem. Middleware agentov to omogoča z:

*Funkcijski middleware*

Ta middleware omogoča izvajanje akcije med agentom in klicanjem funkcije/orodja. Primer uporabe je beleženje klica funkcije.

V spodnji kodi `next` določa, ali naj se kliče naslednji middleware ali dejanska funkcija.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Predhodna obdelava: Beleženje pred izvajanjem funkcije
    print(f"[Function] Calling {context.function.name}")

    # Nadaljuj na naslednji vmesni programski opremi ali izvedbo funkcije
    await next(context)

    # Naknadna obdelava: Beleženje po izvajanju funkcije
    print(f"[Function] {context.function.name} completed")
```

*Chat middleware*

Ta middleware omogoča izvajanje ali beleženje akcije med agentom in zahtevami med LLM.

Vključuje pomembne informacije, kot so `messages`, ki se pošiljajo AI storitvi.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Predobdelava: Zabeleži pred klicem AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Nadaljuj do naslednjega vmesnega sloja ali AI storitve
    await next(context)

    # Poobdelava: Zabeleži po odgovoru AI
    print("[Chat] AI response received")

```

**Pomnilnik agentov**

Kot je bilo zajeto v lekciji `Agentic Memory`, je pomnilnik ključni element za omogočanje delovanja agenta v različnih kontekstih. MAF ponuja več vrst pomnilnikov:

*Shranjevanje v pomnilnik (In-Memory Storage)*

To je pomnilnik, shranjen v nitkah med izvajanjem aplikacije.

```python
# Ustvari novo nit.
thread = agent.get_new_thread() # Zaženi agenta z nitjo.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Trajni sporočila (Persistent Messages)*

Ta pomnilnik se uporablja za shranjevanje zgodovine pogovorov čez različne seje. Definiran je preko `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Ustvari prilagojeno shrambo sporočil
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dinamični pomnilnik (Dynamic Memory)*

Ta pomnilnik se doda kontekstu pred zagonom agentov. Te pomnilnike je mogoče shranjevati v zunanjih storitvah, kot je mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Uporaba Mem0 za napredne zmogljivosti pomnilnika
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

**Opazovanje agentov**

Opazovanje je pomembno za gradnjo zanesljivih in vzdržljivih agentnih sistemov. MAF se integrira z OpenTelemetry za zagotavljanje sledenja in meritev za boljšo opazovalnost.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # naredi nekaj
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Delovni tokovi

MAF nudi delovne tokove, ki so prednastavljeni koraki za dokončanje naloge in vključujejo AI agente kot komponente teh korakov.

Delovni tokovi so sestavljeni iz različnih komponent, ki omogočajo boljši nadzor nad tokom. Prav tako omogočajo **več-agentno orkestracijo** in **checkpointing** za shranjevanje stanja delovnega toka.

Osnovne komponente delovnega toka so:

**Izvajalci (Executors)**

Izvajalci prejmejo vhodna sporočila, opravijo dodeljene naloge in proizvedejo izhodno sporočilo. To premakne delovni tok naprej k dokončanju večje naloge. Izvajalci so lahko AI agenti ali prilagojena logika.

**Povezave (Edges)**

Povezave določajo tok sporočil v delovnem toku. Lahko so:

*Neposredne povezave* - Enostavne povezave ena na ena med izvajalci:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Pogojne povezave* - Aktivirajo se, ko je izpolnjen določen pogoj. Na primer, ko hotelske sobe niso na voljo, lahko izvajalec predlaga druge možnosti.

*Povezave s preklopi* - Usmerjajo sporočila do različnih izvajalcev glede na določene pogoje. Na primer, če ima potovalni kupec prednostni dostop in bodo njegove naloge obdelane v drugem delovnem toku.

*Razvejitev (Fan-out Edges)* - Pošlje eno sporočilo več naslovnikom.

*Združitev (Fan-in Edges)* - Zbere več sporočil od različnih izvajalcev in jih pošlje enemu naslovniku.

**Dogodki**

Za boljše opazovanje delovnih tokov MAF ponuja vgrajene dogodke za izvajanje, vključno z:

- `WorkflowStartedEvent`  - Začetek izvajanja delovnega toka
- `WorkflowOutputEvent` - Delovni tok proizvede izhod
- `WorkflowErrorEvent` - Delovni tok naleti na napako
- `ExecutorInvokeEvent`  - Izvajalec začne obdelavo
- `ExecutorCompleteEvent`  -  Izvajalec konča obdelavo
- `RequestInfoEvent` - Zahteva je izdana

## Napredni MAF vzorci

Zgornji oddelki pokrivajo ključne koncepte Microsoft Agent Framework. Ko gradite bolj zapletene agente, upoštevajte naslednje napredne vzorce:

- **Sestava middleware**: Povežite več middleware rokovalcev (beleženje, avtentikacija, omejevanje hitrosti) z uporabo funkcijskega in chat middleware za natančen nadzor nad vedenjem agenta.
- **Checkpointing delovnih tokov**: Uporabite dogodke delovnih tokov in serializacijo za shranjevanje in nadaljevanje daljših agentnih procesov.
- **Dinamični izbor orodij**: Združite RAG preko opisov orodij s registracijo orodij MAF za prikaz le relevantnih orodij za posamezen poizvedbo.
- **Več-agentna predaja**: Uporabite povezave delovnih tokov in pogojno usmerjanje za orkestracijo predaj med specializiranimi agenti.

## Gostovanje LangChain / LangGraph agentov na Microsoft Foundry

Microsoft Agent Framework je **sistem medsebojne združljivosti z ogrodji** — niste omejeni samo na agente, napisane z MAF. Če že imate agenta, zgrajenega z **LangChain** ali **LangGraph**, ga lahko zaženete kot **Najbolj gostovan agent Microsoft Foundry**, tako da Foundry upravlja čas izvajanja, seje, prilagajanje, identiteto in protokolne končne točke, medtem ko logika vašega agenta ostane v LangGraph.

To se izvaja z `langchain_azure_ai.agents.hosting` paketom, ki omogoča sestavljeni LangGraph graf preko istih protokolov, ki jih uporabljajo Foundry gostovani agenti.

**1. Namestite dodatni paket za gostovanje:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Paket `hosting` namesti Foundry protokolne knjižnice: `azure-ai-agentserver-responses` (združljiv `/responses` endpoint kot OpenAI) in `azure-ai-agentserver-invocations` (splošni `/invocations` endpoint).

**2. Izberite protokol gostovanja:**

| Protokol | Razred gostitelja | Končna točka | Uporaba |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Želite združljiv klepet OpenAI, streaming, zgodovino odzivov in povezanost pogovorov — priporočen privzeti način za pogovorne agente. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Potrebujete prilagojeno JSON obliko, webhook slog končne točke ali ne-pogovorno obdelavo. |

Ker je **Responses API primarni API za razvoj agentnega sloga v Foundry**, začnite s `ResponsesHostServer` za večino agentov.

**3. Konfigurirajte okoljske spremenljivke** (najprej `az login`, da se lahko `DefaultAzureCredential` avtenticira):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

Ko agent pozneje teče kot gostovani agent v Foundry, platforma samodejno vstavi `FOUNDRY_PROJECT_ENDPOINT`.

**4. Izpostavite LangGraph agenta preko Responses protokola:**

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

    # ChatOpenAI tukaj cilja na OpenAI-kompatibilno (Odgovori) končno točko projekta Foundry.
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

Zaženite lokalno z `python main.py`, nato pošljite zahtevo Responses na `http://localhost:8088/responses`.

**Ključna vedenja:**

- **Pogovori**: Stranke nadaljujejo pogovor tako, da prenesejo `previous_response_id` ali ID `conversation`. Če je vaš graf preveden s LangGraph checkpointerjem, Foundry poveže stanje pogovora s checkpointom (uporabite vzdržljiv checkpointer v produkciji; `MemorySaver` je ustrezno za lokalno testiranje).
- **Človek-v-zanki**: Če vaš graf uporablja LangGraph `interrupt()`, `ResponsesHostServer` prikaže čakajoči prekinitev kot `function_call` / `mcp_approval_request` v Responses, stranke pa nadaljujejo z ustreznim `function_call_output` / `mcp_approval_response`.
- **Implementacija v Foundry**: Uporabite Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokalno, zahteva Docker), nato `azd provision` in `azd deploy`. Za uvajanje gostovanih agentov je potrebna vloga **Foundry Project Manager**.

Izvedljiva različica tega primera je v [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Za celoten vodič (protokol Invocations, prilagojene sheme zahtevkov in odpravljanje težav), si oglejte [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Vzorce kode 

Vzorce kode za Microsoft Agent Framework lahko najdete v tem repozitoriju pod datotekami `xx-python-agent-framework` in `xx-dotnet-agent-framework`.

## Imate več vprašanj o Microsoft Agent Framework?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da spoznate druge učence, se udeležite uradnih ur in dobite odgovore na vaša vprašanja o AI agentih.
## Prejšnja lekcija

[Pomnilnik za AI agente](../13-agent-memory/README.md)

## Naslednja lekcija

[Gradnja agentov za uporabo računalnika (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->