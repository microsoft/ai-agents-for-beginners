# Microsoft Agent Frameworki uurimine

![Agent Framework](../../../translated_images/et/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Sissejuhatus

See õppetund käsitleb:

- Microsoft Agent Frameworki mõistmine: põhifunktsioonid ja väärtus  
- Microsoft Agent Frameworki võtmekontseptsioonide uurimine
- Täiustatud MAF mustrid: töövood, vahendustarkvara ja mälu

## Õpieesmärgid

Selle õppetunni lõpuks oskad:

- Luua tootmiskõlblikke tehisintellekti agente Microsoft Agent Frameworki abil
- Rakendada Microsoft Agent Frameworki põhifunktsioone oma agentuursete kasutusjuhtumite jaoks
- Kasutada täiustatud mustreid, sealhulgas töövoogusid, vahendustarkvara ja jälgitavust

## Koodinäited 

Microsoft Agent Frameworki (MAF) koodinäiteid leiate sellest varamuhoidlast failide `xx-python-agent-framework` ja `xx-dotnet-agent-framework` alt.

## Microsoft Agent Frameworki mõistmine

![Framework Intro](../../../translated_images/et/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) on Microsofti ühtne raamistik tehisintellekti agentide loomiseks. See pakub paindlikkust käsitleda laias valikus agentuurseid kasutusjuhtumeid nii tootmises kui uurimistöödes, sealhulgas:

- **Järjestikune agendi orkestreerimine** olukordades, kus on vaja samm-sammult töövooge.
- **Vastusaegne orkestreerimine** olukordades, kus agentidel on vaja ülesanded korraga lõpetada.
- **Grupivestluse orkestreerimine** olukordades, kus agentidel on võimalik üheskoos ühte ülesannet lahendada.
- **Ülesande üleandmise orkestreerimine** olukordades, kus agentide vahel antakse ülesande alaülesanded üle siis, kui need on lõpetatud.
- **Magnetiline orkestreerimine** olukordades, kus juhendaja agent loob ja muudab ülesannete nimekirja ning koordineerib subagentide tööd ülesande täitmiseks.

AI agentide tootmiseks sisaldab MAF lisafunktsioone nagu:

- **Jälgitavus** OpenTelemetry kasutamise kaudu, kus iga AI agendi tegevus, sealhulgas tööriistakutse, orkestreerimisetapid, järeldusvood ja jõudluse jälgimine Microsoft Foundry armatuurlaual, on jälgitav.
- **Turvalisus** agentide majutamisel Microsoft Foundrys, mis sisaldab turvakontrolle nagu rollipõhine juurdepääs, andmete privaatsus ja sisuturve.
- **Vastupidavus**, kuna agendi lõimed ja töövood saavad peatuda, jätkata ja taastuda vigadest, võimaldades pikemaajalisi protsesse.
- **Juhtimine** inimeste kaasamisega töövoogude toetamine, kus ülesanded märgitakse inimkinnitust nõudvaks.

Microsoft Agent Framework paneb rõhku ka omavahelise koostalitlusvõime saavutamisele:

- **Pilve-agnostikaks olemine** - agentidel on võimalik töötada konteinerites, kohapeal ja mitme erineva pilvesüsteemi vahel.
- **Pakkuja-agnostikaks olemine** - agente saab luua oma eelistatud SDK abil, sh Azure OpenAI ja OpenAI.
- **Avatud standardite integreerimine** - agentidel on võimalik kasutada protokolle nagu Agent-to-Agent (A2A) ja Model Context Protocol (MCP), et avastada ja kasutada teisi agente ja tööriistu.
- **Pluginate ja ühenduste kasutamine** - võimalik on ühendada andmete ja mälu teenustega nagu Microsoft Fabric, SharePoint, Pinecone ja Qdrant.

Vaatame, kuidas neid funktsioone rakendatakse Microsoft Agent Frameworki põhikontseptsioonide puhul.

## Microsoft Agent Frameworki võtmekontseptsioonid

### Agendid

![Agent Framework](../../../translated_images/et/agent-components.410a06daf87b4fef.webp)

**Agentide loomine**

Agendi loomine toimub, määrates järeldusteenuse (LLM pakkuja), 
juhised, mida AI agent peab järgima, ja määrates `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Ülaltoodud näites kasutatakse `Azure OpenAI`-d, kuid agente saab luua erinevate teenuste abil, sh `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` API-d

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

või [MiniMax](https://platform.minimaxi.com/), mis pakub OpenAI-kompatibelset API-d suure kontekstiga aknaga (kuni 204K tokenit):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

või kaugagendid, kasutades A2A protokolli:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Agentide käivitamine**

Agente käivitatakse `.run` või `.run_stream` meetoditega, kas mitte-voogedastuseks või voogedastuseks vastamiseks.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Iga agendi jooksul võivad olla ka valikud parameetrite kohandamiseks, nagu agendi kasutatavad `max_tokens`, `tools`, mida agent saab kutsuda, ja isegi kasutatav `model`.

See on kasulik juhtudel, kus ülesande täitmiseks on vaja kindlaid mudeleid või tööriistu.

**Tööriistad**

Tööriistad saab määratleda nii agendi määratlemisel:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Kui luuakse ChatAgent otse

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

kui ka agendi käivitamisel:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Tööriist, mis on mõeldud ainult selleks jooksuks )
```

**Agendi lõimed**

Agendi lõimesid kasutatakse mitmevooruliste vestluste käsitlemiseks. Lõimed saab luua kas:

- kasutades `get_new_thread()`, mis võimaldab lõimed salvestada aja jooksul
- lõime automaatse loomisega agendi käivitamisel, kus lõim kestab vaid selle käigu jooksul.

Lõime loomise kood näeb välja nii:

```python
# Loo uus lõim.
thread = agent.get_new_thread() # Käivita agent lõimega.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Lõime saab seejärel serialiseerida hilisemaks kasutamiseks:

```python
# Loo uus lõim.
thread = agent.get_new_thread() 

# Käivita agent koos lõimiga.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serialiseeri lõim salvestamiseks.

serialized_thread = await thread.serialize() 

# Deserialiseeri lõime olek pärast laadimist salvestusest.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agendi vahendustarkvara**

Agendid suhtlevad tööriistade ja LLM-idega, et täita kasutaja ülesandeid. Mõnel juhul soovime nende vahelist suhtlust jälgida või täiendavalt käivitada. Agendi vahendustarkvara võimaldab seda järgmiste abil:

*Funktsioonide vahendustarkvara*

See vahendustarkvara võimaldab meil käivitada toimingu agendi ja tema poolt kutsutava funktsiooni/tööriista vahel. Näide: logimine funktsiooni kutsel.

Koodis allpool määrab `next`, kas kutsutakse järgmine vahendustarkvara või tegelik funktsioon.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Eeltöötlus: Logi enne funktsiooni täitmist
    print(f"[Function] Calling {context.function.name}")

    # Jätka järgmise vahendustarkvara või funktsiooni täitmisega
    await next(context)

    # Järel-töötlus: Logi pärast funktsiooni täitmist
    print(f"[Function] {context.function.name} completed")
```

*Vestluse vahendustarkvara*

See vahendustarkvara võimaldab jälgida või täita toiminguid agendi ja LLM-i vaheliste päringute vahel.

See sisaldab olulist informatsiooni, nt AI teenusele saadetavad `messages`.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Eeltöötlemine: Logi enne tehisintellekti kutsumist
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Jätka järgmise vahendustaseme või tehisintellekti teenuse poole
    await next(context)

    # Järelprotsessimine: Logi pärast tehisintellekti vastust
    print("[Chat] AI response received")

```

**Agendi mälu**

Nagu õppetunnis `Agentic Memory` käsitleti, on mälu oluline element, mis võimaldab agentidel töötada erinevates kontekstides. MAF pakub mitut erinevat mälutüüpi:

*Rakenduse mälu*

See mälu on salvestatud lõimede ajal rakenduse jooksu ajal.

```python
# Loo uus lõim.
thread = agent.get_new_thread() # Käivita agent lõimega.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Püsivad sõnumid*

Seda mälu kasutatakse vestlusajaloo salvestamiseks erinevate sessioonide vahel. See määratletakse `chat_message_store_factory` abil:

```python
from agent_framework import ChatMessageStore

# Loo kohandatud sõnumite hoidla
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dünaamiline mälu*

See mälu lisatakse konteksti enne agentide käivitumist. Seda mälu saab hoida välisteenustes nagu mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Kasutades Mem0 arenenud mälu funktsionaalsuse jaoks
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

**Agendi jälgitavus**

Jälgitavus on oluline usaldusväärsete ja hooldatavate agentuursete süsteemide ehitamisel. MAF integreerub OpenTelemetry-ga, pakkudes jälgimist ja mõõdikuid parema nähtavuse saavutamiseks.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # tee midagi
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Töövood

MAF pakub töövoogusid, mis on eelmääratletud sammud ülesande täitmiseks ja mis sisaldavad AI agente nendes sammudes komponendina.

Töövood koosnevad erinevatest komponentidest, mis võimaldavad paremat juhtimisvoogu. Töövood võimaldavad ka **mitmeagendi orkestreerimist** ja **vaheetappide salvestamist** töövoo olekute säilitamiseks.

Töövoo põhikomponendid on:

**Täiturid**

Täiturid võtavad vastu sisendsõnumeid, teevad oma määratud ülesanded ja toodavad väljundisõnumi. See viib töövoogu suurema ülesande täitmise poole. Täiturid võivad olla kas AI agent või kohandatud loogika.

**Käärid**

Käärid määratlevad sõnumite voogu töövoos. Need võivad olla:

*Otsesed käärid* - lihtsad ühe-kaheni ühendused täiturite vahel:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Tingimuslikud käärid* - aktiveeruvad, kui teatud tingimus on täidetud. Näiteks, kui hotellitube pole saadaval, võib täitur soovitada teisi võimalusi.

*Lüliti-käsu (switch-case) käärid* - marsruutivad sõnumeid erinevatele täituritele vastavalt määratud tingimustele. Näiteks kui reisiklient on prioriteediga ligipääsuga, käsitletakse nende ülesanded teise töövoo kaudu.

*Fan-out käärid* - saadavad ühe sõnumi mitmele sihtmärgile.

*Fan-in käärid* - koguvad mitu sõnumit erinevatelt täituritelt ja saadavad üheks sihtmärgiks.

**Sündmused**

Paremaks jälgitavuseks töövoogudes pakub MAF sisseehitatud täitmissündmusi, sealhulgas:

- `WorkflowStartedEvent`  - tööhvoo täitmine algab
- `WorkflowOutputEvent` - töövoog toodab väljundi
- `WorkflowErrorEvent` - töövoog kohtab viga
- `ExecutorInvokeEvent`  - täitur alustab töötlemist
- `ExecutorCompleteEvent`  - täitur lõpetab töötlemise
- `RequestInfoEvent` - päring esitatakse

## Täiustatud MAF mustrid

Ülaltoodud sektsioonid käsitlevad Microsoft Agent Frameworki põhikontseptsioone. Kui loote keerukamaid agente, kaaluge järgmisi täiustatud mustreid:

- **Vahendustarkvara ahelad**: Keti moodi mitme vahendustarkvarahalduri ühendamine (logimine, autentimine, kiirusepiirangud), kasutades funktsioonide ja vestluste vahendustarkvara agendi käitumise peenhäälestamiseks.
- **Töövoo vaheetappide salvestamine**: Töövoo sündmuste ja serialiseerimise kasutamine pikaajaliste protsesside salvestamiseks ja jätkamiseks.
- **Dünaamiline tööriista valik**: Kombineerides RAG tööriistade kirjelduste ja MAF tööriistade registreerimisega, esitatakse päringu kohta ainult asjakohased tööriistad.
- **Mitmeagendi ülesande üleandmine**: Kasutades töövoo käärid ja tingimuslikku marsruutimist spetsialiseeritud agentide vaheliste ülesandeülesannete korraldamiseks.

## LangChain / LangGraph agentide majutamine Microsoft Foundrys

Microsoft Agent Framework on **raamistikuülene** — te ei ole piiratud ainult MAF-i kirjutatud agentidega. Kui teil on juba agent loodud **LangChain** või **LangGraph** abil, saate selle käitada kui **Microsoft Foundry majutatud agenti**, kus Foundry haldab käitamist, sessioone, skaleerimist, identiteeti ja protokolli lõpp-punkte, samal ajal kui teie agendi loogika jääb LangGraph-i.

Seda tehakse `langchain_azure_ai.agents.hosting` paketiga, mis ekspordib kompileeritud LangGraph graafi samade protokollide kaudu, mida Foundry majutatud agentide kasutab.

**1. Installi majutamise lisand:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` lisand installib Foundry protokolliteegid: `azure-ai-agentserver-responses` (OpenAI-kompatibelne `/responses` lõpp-punkt) ja `azure-ai-agentserver-invocations` (üldine `/invocations` lõpp-punkt).

**2. Valige majutamisprotokoll:**

| Protokoll | Host klass | Lõpp-punkt | Kasutamise olukord |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Soovite OpenAI-kompatibelset vestlust, voogedastust, vastuste ajalugu ja vestluse lõimimist — soovitatud vaikeseade vestlusagentidele. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Vajate kohandatud JSON-kujulist lõpp-punkti, webhook-laadset lõpp-punkti või mittevestluslikku töötlemist. |

Kuna **Responses API on Foundry agentide arenduse põhiliides**, alustage enamiku agentide puhul `ResponsesHostServer` kasutamisest.

**3. Konfigureerige keskkonnamuutujad** (`az login` esmalt, et `DefaultAzureCredential` saaks autentida):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Kui agent hiljem käivitatakse Foundry majutatud agendina, süstib platvorm automaatselt `FOUNDRY_PROJECT_ENDPOINT`.

**4. Eksponeerige LangGraph agent Responses protokolli kaudu:**

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

    # ChatOpenAI sihib siin Foundry projekti OpenAI-ühilduvat (Responses) lõpp-punkti.
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

Käivitage see lokaalselt käsuga `python main.py`, seejärel saatke responses-päring aadressile `http://localhost:8088/responses`.

**Peamised käitumised:**

- **Vestlused**: kliendid jätkavad vestlust, edastades `previous_response_id` või `conversation` ID. Kui teie graaf on koostatud LangGraphi vaheetapi hoidjaga, sidub Foundry vestluse oleku vaheetapiga (kasutage tootmises vastupidavat hoidjat; `MemorySaver` sobib kohaliku testimise jaoks).
- **Inimene ahelas**: kui teie graaf kasutab LangGraphi `interrupt()`, kuvab `ResponsesHostServer` ootel oleva katkestuse Responses `function_call` / `mcp_approval_request` elemendina, ning kliendid jätkavad sobiva `function_call_output` / `mcp_approval_response` vastusega.
- **Deploy Foundrysse**: kasutage Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (kohalik, nõuab Dockerit), ja seejärel `azd provision` ja `azd deploy`. Majutatud agendi juurutamiseks on vajalik **Foundry Project Manager** roll.

Selle näite töökorras versioon asub failis [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Täieliku juhendi (Invocations protokoll, kohandatud päringute skeemid ja tõrkeotsing) leiate siit: [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Koodinäited 

Microsoft Agent Frameworki koodinäiteid leiate sellest varamuhoidlast failide `xx-python-agent-framework` ja `xx-dotnet-agent-framework` alt.

## Kas teil on Microsoft Agent Frameworki kohta rohkem küsimusi?

Liituge [Microsoft Foundry Discordiga](https://discord.com/invite/ATgtXmAS5D), et kohtuda teiste õppijatega, osaleda kontoritundides ja saada vastused oma AI agentide küsimustele.
## Eelmine õppetund

[AI agentide mälu](../13-agent-memory/README.md)

## Järgmine õppetund

[Arvuti kasutamise agentide loomine (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->