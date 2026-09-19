# Raziskovanje Microsoft Agent Framework

![Agent Framework](../../../translated_images/sl/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Uvod

Ta lekcija bo zajemala:

- Razumevanje Microsoft Agent Framework: Ključne funkcije in vrednost  
- Raziskovanje ključnih pojmov Microsoft Agent Framework
- Napredni MAF vzorci: delovni procesi, middleware in pomnilnik

## Cilji učenja

Po zaključku te lekcije boste znali:

- Graditi producentsko pripravljene AI agente z uporabo Microsoft Agent Framework
- Uporabiti osnovne funkcije Microsoft Agent Framework v vaših agentnih primerih uporabe
- Uporabiti napredne vzorce, vključno z delovnimi procesi, middleware in opazovanjem

## Primeri kode 

Primeri kode za [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) so na voljo v tem repozitoriju v datotekah `xx-python-agent-framework` in `xx-dotnet-agent-framework`.

## Razumevanje Microsoft Agent Framework

![Framework Intro](../../../translated_images/sl/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) je Microsoftov enoten okvir za gradnjo AI agentov. Nudil je prilagodljivost, da zadovolji široko paleto agentnih primerov uporabe, ki jih vidimo tako v proizvodnih kot raziskovalnih okoljih, vključno z:

- **Zaporedna orkestracija agentov** v scenarijih, kjer so potrebni korak-po-korak delovni procesi.
- **Sočasna orkestracija** v scenarijih, kjer agenti morajo opraviti naloge hkrati.
- **Orkestracija skupinskega klepeta** v scenarijih, kjer agenti sodelujejo skupaj pri eni nalogi.
- **Orkestracija predaje** v scenarijih, kjer agenti predajajo nalogo med seboj, ko so podnaloge zaključene.
- **Magnetna orkestracija** v scenarijih, kjer vodilni agent ustvari in spreminja seznam nalog ter upravlja koordinacijo podagentov za dokončanje naloge.

Za zagotavljanje AI agentov v produkciji ima MAF tudi vključene funkcije za:

- **Opazovanje** skozi uporabo OpenTelemetry, kjer je vsaka akcija AI agenta, vključno z uporabo orodij, koraki orkestracije, tokovi razmišljanja in spremljanje zmogljivosti skozi Microsoft Foundry nadzorne plošče.
- **Varnost** z gostovanjem agentov naravno na Microsoft Foundry, ki vključuje varnostne kontrole, kot so dostop na osnovi vlog, ravnanje z zasebnimi podatki in vgrajena varnost vsebine.
- **Vzdržljivost** saj se lahko niti in delovni procesi agentov začasno ustavijo, nadaljujejo in si opomorejo od napak, kar omogoča daljše delovanje postopkov.
- **Nadzor** saj so podprti delovni procesi z vključitvijo človeka, kjer so naloge označene kot zahtevajo odobritev človeka.

Microsoft Agent Framework je tudi osredotočen na interoperabilnost z:

- **Neodvisnostjo od oblaka** - Agenti lahko tečejo v vsebnikih, na lokaciji (on-premises) in preko različnih oblakov.
- **Neodvisnostjo od ponudnika** - Agenti se lahko ustvarijo preko vašega priljubljenega SDK, vključno z Azure OpenAI in OpenAI
- **Integracijo odprtih standardov** - Agenti lahko uporabljajo protokole, kot so Agent-to-Agent (A2A) in Model Context Protocol (MCP), za odkrivanje in uporabo drugih agentov ter orodij.
- **Vtičniki in konektorji** - Možne so povezave do podatkovnih in pomnilniških storitev, kot so Microsoft Fabric, SharePoint, Pinecone in Qdrant.

Poglejmo, kako so te funkcije uporabljene pri nekaterih osnovnih pojmih Microsoft Agent Framework.

## Ključni pojmi Microsoft Agent Framework

### Agenti

![Agent Framework](../../../translated_images/sl/agent-components.410a06daf87b4fef.webp)

**Ustvarjanje agentov**

Ustvarjanje agenta poteka z določitvijo storitve sklepanja (LLM Provider), 
niza navodil, ki jih mora AI agent slediti, in dodeljenega `imena`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Zgoraj se uporablja `Azure OpenAI`, vendar je mogoče agente ustvariti z uporabo različnih storitev, vključno z `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` API-ji

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ali [MiniMax](https://platform.minimaxi.com/), ki ponuja OpenAI-kompatibilen API z velikimi kontekstnimi okni (do 204K tokenov):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ali oddaljene agente s protokolom A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Zagon agentov**

Agenti se zaženejo z metodama `.run` ali `.run_stream` za ne-stremirane oziroma stremirane odzive.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Vsak zagon agenta lahko vsebuje tudi opcije za prilagajanje parametrov, kot so `max_tokens`, ki jih agent uporablja, `tools` (orodja), ki jih agent lahko poklič, in celo sam `model`, uporabljen za agenta.

To je uporabno v primerih, kjer so za zaključek uporabnikove naloge potrebni določeni modeli ali orodja.

**Orodja**

Orodja je mogoče definirati tako pri definiranju agenta:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Ko neposredno ustvarjate ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

in tudi pri zagonu agenta:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Orodje na voljo samo za to izvajanje )
```

**Niti agenta**

Niti agenta se uporabljajo za obravnavo pogovorov z več hodi. Niti je mogoče ustvariti na dva načina:

- Z uporabo `get_new_thread()`, ki omogoča, da se nit shrani skozi čas
- Z ustvarjanjem niti samodejno med zagonom agenta, pri čemer nit obstaja le med trenutnim zagonom.

Za ustvarjanje niti koda izgleda tako:

```python
# Ustvari novo nit.
thread = agent.get_new_thread() # Zaženi agent z nitjo.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Nato lahko nit serializirate za poznejšo uporabo:

```python
# Ustvari novo nit.
thread = agent.get_new_thread() 

# Zaženi agenta s to nitjo.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serializiraj nit za shranjevanje.

serialized_thread = await thread.serialize() 

# Deserializiraj stanje niti po nalaganju iz shrambe.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware agenta**

Agenti sodelujejo z orodji in LLM, da dokončajo uporabnikove naloge. V določenih scenarijih želimo izvajati ali spremljati vmesne interakcije. Middleware agenta to omogoča preko:

*Funkcijski middleware*

Ta middleware omogoča izvajanje dejanja med agentom in funkcijo/orodjem, ki ga agent kliče. Primer uporabe je, če želite zabeležiti klic funkcije.

V spodnji kodi `next` določa, ali je treba poklicati naslednji middleware ali dejansko funkcijo.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pred-obdelava: Zabeleži pred izvajanjem funkcije
    print(f"[Function] Calling {context.function.name}")

    # Nadaljuj na naslednjo vmesno programsko opremo ali izvedbo funkcije
    await next(context)

    # Po-obdelava: Zabeleži po izvajanju funkcije
    print(f"[Function] {context.function.name} completed")
```

*Chat middleware*

Ta middleware omogoča izvajanje ali beleženje dejanja med agentom in zahtevki med LLM.

Vsebuje pomembne informacije, kot so `messages`, ki se pošiljajo AI storitvi.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Predobdelava: Zabeleži pred klicem AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Nadaljuj na naslednji vmesnik ali AI storitev
    await next(context)

    # Obdelava po: Zabeleži po odgovoru AI
    print("[Chat] AI response received")

```

**Pomnilnik agenta**

Kot je obravnavano v lekciji `Agentic Memory`, je pomnilnik pomemben element za omogočanje delovanja agenta v različnih kontekstih. MAF ponuja več različnih vrst pomnilnika:

*Pomnilnik v teku (In-Memory Storage)*

Pomnilnik shranjen v nitih med izvajanjem aplikacije.

```python
# Ustvari novo nit.
thread = agent.get_new_thread() # Zaženi agenta z nitjo.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Vztrajna sporočila*

Ta pomnilnik se uporablja za shranjevanje zgodovine pogovorov med različnimi sejami. Določen je z `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Ustvari prilagojeno skladišče sporočil
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dinamični pomnilnik*

Ta pomnilnik se doda v kontekst pred zagonom agentov. Ti pomnilniki se lahko shranjujejo v zunanjih storitvah, kot je mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Uporaba Mem0 za napredne zmožnosti pomnilnika
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

**Opazovanje agenta**

Opazovanje je pomembno za gradnjo zanesljivih in vzdržljivih agentnih sistemov. MAF se povezuje z OpenTelemetry za zagotavljanje sledenja in meritev za boljšo opaznost.

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

### Delovni procesi

MAF ponuja delovne procese, ki so preddefinirani koraki za dokončanje naloge in vključujejo AI agente kot komponente v teh korakih.

Delovni procesi so sestavljeni iz različnih komponent, ki omogočajo boljši nadzor toka. Delovni procesi omogočajo tudi **večagentno orkestracijo** in **točkovanje zaustavitve** za shranjevanje stanj delovnega procesa.

Osnovne komponente delovnega procesa so:

**Izvajalci**

Izvajalci prejemajo vhodna sporočila, izvajajo dodeljene naloge in potom proizvedejo izhodno sporočilo. Tako delovni proces napreduje proti zaključku večje naloge. Izvajalci so lahko AI agenti ali lastna logika.

**Povezave**

Povezave se uporabljajo za definiranje toka sporočil v delovnem procesu. Lahko so:

*Neposredne povezave* - Enostavne povezave eden-na-eden med izvajalci:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Povezave s pogoji* - Aktivirane po izpolnitvi določenega pogoja. Na primer, ko sob ni na voljo, izvajalec lahko predlaga druge možnosti.

*Preklopne povezave* - Usmerjajo sporočila različnim izvajalcem glede na določene pogoje. Na primer, če ima potnik prednostni dostop, bodo njegove naloge obravnavane preko drugega delovnega procesa.

*Razširitvene povezave* - Pošljejo eno sporočilo več ciljem.

*Združevalne povezave* - Zberejo več sporočil iz različnih izvajalcev in pošljejo enemu cilju.

**Dogodki**

Za boljšo opaznost delovnih procesov MAF ponuja vgrajene dogodke izvajanja, vključno z:

- `WorkflowStartedEvent`  - Začetek izvajanja delovnega procesa
- `WorkflowOutputEvent` - Delovni proces ustvari izhod
- `WorkflowErrorEvent` - Delovni proces naleti na napako
- `ExecutorInvokeEvent`  - Izvajalec začne z obdelavo
- `ExecutorCompleteEvent`  -  Izvajalec zaključi obdelavo
- `RequestInfoEvent` - Podan je zahtevek

## Napredni MAF vzorci

Prejšnji odseki obravnavajo ključne pojme Microsoft Agent Framework. Ko gradite bolj zapletene agente, upoštevajte naslednje napredne vzorce:

- **Sestava middleware**: Zaporedno povezovanje več middleware komponent (beleženje, avtorizacija, omejevanje hitrosti) z uporabo funkcijskega in klepetalnega middleware za natančen nadzor vedenja agenta.
- **Točkovanje delovnih procesov**: Uporaba dogodkov delovnega procesa in serializacije za shranjevanje in nadaljevanje dolgoročno tekočih postopkov agentov.
- **Dinamična izbira orodij**: Združevanje RAG preko opisov orodij z MAF registracijo orodij za predstavitev le relevantnih orodij glede na poizvedbo.
- **Večagentna predaja**: Uporaba povezav delovnega procesa in pogojevnega usmerjanja za orkestracijo predaj med specializiranimi agenti.

## Gostovanje LangChain / LangGraph agentov na Microsoft Foundry

Microsoft Agent Framework je **okvirno interoperabilen** — niste omejeni na agente napisane z MAF. Če že imate agenta zgrajenega z **LangChain** ali **LangGraph**, ga lahko poganjate kot **Microsoft Foundry gostovanega agenta**, tako da Foundry upravlja izvajanje, seje, skaliranje, identiteto in protokolne končne točke, medtem ko vaša logika agentov ostane v LangGraph.

To se izvaja z `langchain_azure_ai.agents.hosting` paketom, ki razgrne sestavljen LangGraph graf prek enakih protokolov, kot jih uporabljajo Foundry gostovani agenti.

**1. Namestite hosting dodatek:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Dodatek `hosting` namesti Foundry protokolne knjižnice: `azure-ai-agentserver-responses` (OpenAI-kompatibilna `/responses` končna točka) in `azure-ai-agentserver-invocations` (splošna `/invocations` končna točka).

**2. Izberite gostovalni protokol:**

| Protokol | Gostiteljska razred | Končna točka | Uporaba |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Želite klepet, pretakanje, zgodovino odzivov in nitke pogovorov kompatibilne z OpenAI — priporočeno privzeto za pogovorne agente. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Potrebujete lastno JSON obliko, webhook-stil končno točko ali ne-pogovorno obdelavo. |

Ker je **Responses API glavna API za razvoj agentov v Foundry**, začnite z `ResponsesHostServer` za večino agentov.

**3. Konfigurirajte okoljske spremenljivke** (`az login` najprej, da se `DefaultAzureCredential` lahko avtorizira):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Ko agent kasneje teče kot gostovani agent v Foundry, platforma samodejno vbrizga `FOUNDRY_PROJECT_ENDPOINT`.

**4. Izpostavite LangGraph agenta prek protokola Responses:**

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

Zaženite ga lokalno z `python main.py`, nato pošljite zahtevek Responses na `http://localhost:8088/responses`.

**Ključna vedenja:**

- **Pogovori**: Stranke nadaljujejo pogovor z posredovanjem `previous_response_id` ali ID `conversation`. Če je vaš graf sestavljen z LangGraph checkpoint-erjem, Foundry poveže stanje pogovora s točko zaustavitve (uporabite trajni checkpoint-er v produkciji; `MemorySaver` je primeren za lokalno testiranje).
- **Človek v zanki**: Če vaš graf uporablja LangGraph `interrupt()`, `ResponsesHostServer` prikaže čakajočo prekinitev kot element Responses `function_call` / `mcp_approval_request`, stranke pa nadaljujejo z ujemajočim se `function_call_output` / `mcp_approval_response`.
- **Implementacija v Foundry**: Uporabite Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokalno, zahteva Docker), nato `azd provision` in `azd deploy`. Implementacija gostovanega agenta zahteva vlogo **Foundry Project Manager**.

Delujoča različica tega primera je na voljo v [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Za celoten vodnik (protokol Invocations, prilagojene sheme zahtevkov in odpravljanje težav) si oglejte [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Primeri kode 

Primeri kode za Microsoft Agent Framework so na voljo v tem repozitoriju v datotekah `xx-python-agent-framework` in `xx-dotnet-agent-framework`.

## Imate več vprašanj o Microsoft Agent Framework?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), da se povežete z drugimi učenci, obiskujete uradne ure in dobite odgovore na vprašanja o AI agentih.
## Prejšnja lekcija

[Pomnilnik za AI agente](../13-agent-memory/README.md)

## Naslednja lekcija

[Gradnja agentov za uporabo računalnika (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->