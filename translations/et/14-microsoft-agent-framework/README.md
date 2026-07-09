# Microsofti Agendi Raamistiku Uurimine

![Agent Framework](../../../translated_images/et/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Sissejuhatus

Selles õppetükis käsitletakse:

- Microsoft Agent Frameworki mõistmine: peamised omadused ja väärtus  
- Microsoft Agent Frameworki võtmekontseptsioonide uurimine
- Täiustatud MAF mustrid: töövood, vahemoodulid ja mälu

## Õpieesmärgid

Pärast selle õppetüki läbimist teate, kuidas:

- Ehita tootmiskõlblikke AI-agente Microsoft Agent Frameworki abil
- Rakenda Microsoft Agent Frameworki põhifunktsioone oma agentide kasutusjuhtudel
- Kasuta täiustatud mustreid, sealhulgas töövooge, vahemooduleid ja jälgitavust

## Koodinäited 

Koodinäited [Microsoft Agent Frameworki (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) jaoks on selles hoidlas asuvates failides`xx-python-agent-framework` ja `xx-dotnet-agent-framework`.

## Microsoft Agent Frameworki Mõistmine

![Framework Intro](../../../translated_images/et/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) on Microsofti ühtne raamistik AI agentide loomiseks. See pakub paindlikkust, et lahendada paljusid agentide kasutusjuhtumeid nii tootmis- kui uurimiskeskkondades, sealhulgas:

- **Järjestikune agendi orkestreerimine** stsenaariumites, kus on vaja samm-sammult töövooge.
- **Sünkroonne orkestreerimine** stsenaariumites, kus agentidel tuleb ülesandeid samaaegselt täita.
- **Rühmavestluse orkestreerimine** stsenaariumites, kus agentidel on võimalus koos ühe ülesande kallal koostööd teha.
- **Üleandmise orkestreerimine** stsenaariumites, kus agentide vahel antakse ülesandeksimmut ülesandeid täites edasi.
- **Magnetiline orkestreerimine** stsenaariumites, kus juhitagendi ülesandeks on luua ja muuta ülesannete nimekirja ning koordineerida alagente ülesande täitmiseks.

AI agentide tootmiseks on MAFisse lisatud ka funktsioonid:

- **Jälgitavus** OpenTelemetry kasutamise kaudu, kus AI agendi iga toiming, sealhulgas tööriista väljakutse, orkestreerimise sammud, loogikavood ja jõudluse jälgimine Microsoft Foundry armatuurlaudadel.
- **Turvalisus** majutades agente natiivalt Microsoft Foundryl, mis sisaldab turvakontrolle, nagu rollipõhine ligipääs, privaatsete andmete käsitlemine ja sisuturve.
- **Vastupidavus** — Agendi lõimed ja töövood saavad peatuda, jätkata ja vigadest taastuda, võimaldades pikemaajalisi protsesse.
- **Järelevalve** — toetatakse inimliikmes olekut töövoogudes, kus ülesanded märgistatakse inimkinnitust vajavaks.

Microsoft Agent Framework on samuti keskendunud ühilduvusele järgmistega:

- **Pilveagnostilisus** — Agente saab käitada konteinerites, lokaalselt ja mitmes erinevas pilves.
- **Pakkuja-agnostilisus** — Agente saab luua oma eelistatud SDK kaudu, sealhulgas Azure OpenAI ja OpenAI.
- **Avatud standardite integreerimine** — Agendid saavad kasutada protokolle nagu Agent-to-Agent (A2A) ja Model Context Protocol (MCP), et avastada ja kasutada teisi agente ja tööriistu.
- **Laiendused ja ühendused** — Ühendused saab luua andme- ja mäluteenustega, nagu Microsoft Fabric, SharePoint, Pinecone ja Qdrant.

Vaatame, kuidas neid funktsioone rakendatakse Microsoft Agent Frameworki põhikontseptsioonides.

## Microsoft Agent Frameworki Põhikontseptsioonid

### Agendid

![Agent Framework](../../../translated_images/et/agent-components.410a06daf87b4fef.webp)

**Agentide Loomine**

Agendi loomine toimub, määratledes järeldusteenus (LLM pakkuja), 
juhiste komplekt AI agendi jaoks ja määratud `nimi`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Ülal kasutatud on `Azure OpenAI`, kuid agente saab luua mitmesuguste teenuste abil, sealhulgas `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` APId

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

või [MiniMax](https://platform.minimaxi.com/), mis pakub OpenAI-ga ühilduvat API-d suurte kontekstiakenatega (kuni 204K märki):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

või kaugagente, kasutades A2A protokolli:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Agentide Käivitamine**

Agente käitatakse meetoditega `.run` või `.run_stream` kas voogedastuseta või voogedastusega vastuste jaoks.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Iga agendi käivituse puhul saab valida valikuid, nagu agendi poolt kasutatavad `max_tokens`, tööriistad (`tools`), mida agent saab kutsuda, ja isegi kasutatav `mudel`.

See on kasulik juhtudel, kus konkreetseid mudeleid või tööriistu on vaja kasutaja ülesande täitmiseks.

**Tööriistad**

Tööriistu saab määrata nii agendi loomisel:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Kui luuakse ChatAgent otse

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

kui ka agendi käivitamisel:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Tööriist, mis on mõeldud ainult selle jooksu jaoks )
```

**Agendi Lõimed**

Agendi lõimesid kasutatakse mitmekordsete vestluste käsitlemiseks. Lõimesid saab luua kas:

- Kasutades `get_new_thread()`, mis võimaldab lõime ajas säilitada
- Lõime loomine automaatselt agendi käivitamisel ja lõime kestmine vaid praeguse käivituse jooksul.

Lõime loomise kood näeb välja järgmiselt:

```python
# Loo uus lõim.
thread = agent.get_new_thread() # Käivita agent koos lõimiga.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Lõime saab seejärel salvestada hilisemaks kasutamiseks serialiseerides:

```python
# Loo uus lõim.
thread = agent.get_new_thread() 

# Käivita agent lõimega.

response = await agent.run("Hello, how are you?", thread=thread) 

# Seriaalesta lõime salvestamiseks.

serialized_thread = await thread.serialize() 

# Deserializeeri lõime olek pärast laadimist salvestusest.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agendi Vahemoodulid**

Agendid suhtlevad tööriistade ja LLMidega, et täita kasutaja ülesandeid. Kindlates stsenaariumites tahame nende vahel käivitada või jälgida toiminguid. Agendi vahemoodulid võimaldavad seda teha järgmiste kaudu:

*Funktsioonide Vahemoodul*

See vahemoodul võimaldab meil sooritada toimingu agendi ja kutsutava funktsiooni/tööriista vahel. Näiteks võib seda kasutada funktsiooni kutsumise logimiseks.

Allolevas koodis määratleb `next`, kas järgmine vahemoodul või tegelik funktsioon tuleks kutsuda.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Eeltöötlus: Logi enne funktsiooni täitmist
    print(f"[Function] Calling {context.function.name}")

    # Jätka järgmise middleware'i või funktsiooni täitmisega
    await next(context)

    # Järelprotsess: Logi pärast funktsiooni täitmist
    print(f"[Function] {context.function.name} completed")
```

*Vestluse Vahemoodul*

See vahemoodul võimaldab sooritada või logida toimingut agendi ja LLMile saadetavate päringute vahel.

See sisaldab olulist infot, nagu AI teenusele saadetavad `sõnumid`.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Eeltöötlus: logi enne AI kutsumist
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Jätka järgmise middleware'i või AI teenusega
    await next(context)

    # Järelprotsess: logi pärast AI vastust
    print("[Chat] AI response received")

```

**Agendi Mälu**

Nagu õppetükis `Agentic Memory` käsitleti, on mälu oluline, et agent saaks tegutseda eri kontekstides. MAF pakub mitut tüüpi mälu:

*Mälu Rakenduses*

See mälu salvestatakse lõimedes rakenduse käivitamise ajal.

```python
# Loo uus lõim.
thread = agent.get_new_thread() # Käivita agent koos lõimiga.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Püsivad Sõnumid*

Seda mälu kasutatakse vestluse ajaloo salvestamiseks eri sessioonide vahel. See määratakse `chat_message_store_factory` abil:

```python
from agent_framework import ChatMessageStore

# Loo kohandatud sõnumite pood
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dünaamiline Mälu*

Seda mälu lisatakse konteksti enne agendi käivitamist. Seda mälu saab hoida välistes teenustes nagu mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Kasutades Mem0 täiustatud mälufunktsioonide jaoks
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

**Agendi Jälgitavus**


Vaadeldavus on oluline usaldusväärsete ja hooldatavate agentsete süsteemide loomisel. MAF integreerub OpenTelemetryga, et pakkuda jälgimist ja mõõdikuid parema vaadeldavuse saavutamiseks.

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

### Töölõigud

MAF pakub töölõike, mis on eelmääratletud sammud ülesande täitmiseks ja mis sisaldavad AI agente komponentidena nendes etappides.

Töölõigud koosnevad erinevatest komponentidest, mis võimaldavad paremat voolu kontrolli. Töölõigud võimaldavad ka **mitme-agendi orkestreerimist** ja **kontrollpunktide loomist** töövoo olekute salvestamiseks.

Töölõigu põhikomponendid on:

**Täideviijad**

Täideviijad võtavad vastu sisendsõnumeid, täidavad neile määratud ülesandeid ja seejärel genereerivad väljundsõnumi. See liigutab töölõiku edasi suurema ülesande täitmisel. Täideviijad võivad olla kas AI agent või kohandatud loogika.

**Suunad**

Suundi kasutatakse sõnumite voolu määramiseks töölõigus. Need võivad olla:

*Otsesuundade* - Lihtsad ühe-ühele ühendused täideviijate vahel:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Tingimuslikud suunad* - Aktiveeruvad pärast teatud tingimuse täitumist. Näiteks, kui hotellitube pole saadaval, võib täideviija soovitada teisi valikuid.

*Lüliti-jaotuse suunad* - Suunavad sõnumeid erinevatele täideviijatele määratletud tingimuste alusel. Näiteks kui reisiklientidel on prioriteetne ligipääs, käsitletakse nende ülesandeid läbi teise töölõigu.

*Lae-out suunad* - Saada üks sõnum mitmele sihtkohale.

*Lae-in suunad* - Kogu mitmeid sõnumeid erinevatelt täideviijatelt ja saada need ühele sihtkohale.

**Sündmused**

Parema vaadeldavuse pakkumiseks töölõikudes, pakub MAF sisseehitatud täitmise sündmusi, sealhulgas:

- `WorkflowStartedEvent`  - Töölõigu täitmine algab
- `WorkflowOutputEvent` - Töölõik genereerib väljundi
- `WorkflowErrorEvent` - Töölõigus esineb viga
- `ExecutorInvokeEvent`  - Täideviija alustab töötlemist
- `ExecutorCompleteEvent`  -  Täideviija lõpetab töötlemise
- `RequestInfoEvent` - Päring on esitatud

## Täiustatud MAF mustrid

Ülaltoodud osad käsitlevad Microsoft Agent Frameworki peamisi mõisteid. Kui ehitate keerukamaid agente, siis siin on mõned arendatud mustrid, mida kaaluda:

- **Vahevara kokkupanek**: Ketitage mitu vahevarahaldurit (logimine, autentimine, kiirusepiirang) funktsiooni- ja jututoa vahevara abil agentsi käitumise peenhäälestatud juhtimiseks.
- **Töölõigu kontrollpunktid**: Kasutage töölõigu sündmusi ja serialiseerimist pikaajaliste agendiprotsesside salvestamiseks ja jätkamiseks.
- **Dünaamiline tööriistade valik**: Ühendage RAG tööriistakirjelduste üle MAF tööriistade registreerimisega, et pakkuda ainult asjakohaseid tööriistu päringu kohta.
- **Mitme-agendi üleandmine**: Kasutage töölõigu suundi ja tingimuslikku marsruutimist spetsialiseeritud agentide vaheliste üleandmiste orkestreerimiseks.

## LangChain / LangGraph agentide majutamine Microsoft Foundryl

Microsoft Agent Framework on **raamistiku-deklareerivalt ühilduv** — te ei ole piiratud ainult MAFiga kirjutatud agentidega. Kui teil on juba agent loodud **LangChain** või **LangGraph** abil, saate selle käivitada kui **Microsoft Foundry hostitud agenti**, nii et Foundry haldab ajamist, sessioone, skaleerimist, identiteeti ja protokolli otspunktid teie eest, samal ajal kui teie agentloogika jääb LangGraphi.

Seda tehakse paketi `langchain_azure_ai.agents.hosting` abil, mis avaldab kompileeritud LangGraphi graafi samadel protokollidel, mida Foundry hostitud agendid kasutavad.

**1. Installi hosting lisa:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` lisa paigaldab Foundry protokolliraamatukogud: `azure-ai-agentserver-responses` (OpenAI-ga ühilduv `/responses` otspunkt) ja `azure-ai-agentserver-invocations` (generaalne `/invocations` otspunkt).

**2. Vali hosting protokoll:**

| Protokoll | Host klass | Otspunkt | Kasuta kui |
|----------|-----------|----------|------------|
| **Responses** | `ResponsesHostServer` | `/responses` | Soovite OpenAI-ga ühilduvat jutuvestlust, voogedastust, vastuse ajalugu ja vestluse lõimimist — soovitatud vaikimisi vestlusagentide puhul. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Vajate kohandatud JSON-kuju, webhook-tüüpi otspunkti või mitte-vestluslikku töötlemist. |

Kuna **Responses API on primaarne API Foundry agentstiilis arenduseks**, alustage enamiku agentide puhul `ResponsesHostServer`iga.

**3. Konfigureerige keskkonnamuutujad** (`az login` esmalt, et `DefaultAzureCredential` saaks autentida):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

Kui agent käivitatakse hiljem Foundry hostitud agendina, süstib platvorm automaatselt `FOUNDRY_PROJECT_ENDPOINT`.

**4. Avaldage LangGraph agent Responses protokolli kaudu:**

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

    # ChatOpenAI siin sihib Foundry projekti OpenAI-ga ühilduvat (Responses) lõpp-punkti.
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

Käivitage kohapeal käsuga `python main.py`, seejärel saatke Responses päring aadressile `http://localhost:8088/responses`.

**Põhikäitumised:**

- **Vestlused**: Kliendid jätkavad vestlust, edastades `previous_response_id` või `conversation` ID. Kui teie graaf on kompileeritud LangGraphi kontrollpunktiga, võtab Foundry vestluse oleku hoiukontrollpunkti külge (kasutage tootmises vastupidavat kontrollpunkti; `MemorySaver` sobib lokaalseks testimiseks).
- **Inimene silmuses**: Kui teie graaf kasutab LangGraphi `interrupt()`, kuvab `ResponsesHostServer` ootel katkestuse Responses `function_call` / `mcp_approval_request` üksusena ning kliendid jätkavad sobiva `function_call_output` / `mcp_approval_response` vastusega.
- **Deploy Foundrysse**: Kasutage Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (kohapealne, nõuab Dockerit), seejärel `azd provision` ja `azd deploy`. Hostitud agendi juurutamiseks on vajalik **Foundry Project Manage** roll.

Käitatav näiteversioon on saadaval aadressil [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Täieliku juhendi (Invocations protokoll, kohandatud päringu skeemid ja veaotsing) leiate siit: [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Koodinäited

Microsoft Agent Frameworki koodinäiteid leiate sellest hoidlast failide `xx-python-agent-framework` ja `xx-dotnet-agent-framework` alt.

## Kas on veel küsimusi Microsoft Agent Frameworki kohta?

Liituge [Microsoft Foundry Discordiga](https://discord.com/invite/ATgtXmAS5D), et kohtuda teiste õppijatega, osaleda kontoritundides ja saada oma AI agentide küsimustele vastuseid.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->