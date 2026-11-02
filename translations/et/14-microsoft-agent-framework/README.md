# Microsoft Agent Frameworki uurimine

![Agent Framework](../../../translated_images/et/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Sissejuhatus

See õppetund käsitleb:

- Microsoft Agent Frameworki mõistmine: põhiomadused ja väärtus  
- Microsoft Agent Frameworki põhikontseptsioonide uurimine
- Täiustatud MAF-i mustrid: töövood, vahendustarkvara ja mälu

## Õpieesmärgid

Pärast selle õppetunni läbimist oskad sa:

- Luua tootmiskõlblikke tehisintellekti agente Microsoft Agent Frameworki abil
- Rakendada Microsoft Agent Frameworki põhifunktsioone oma agentide kasutusjuhtudel
- Kasutada täiustatud mustreid, sealhulgas töövooge, vahendustarkvara ja jälgitavust

## Koodinäited 

Microsoft Agent Frameworki ([MAF](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)) koodinäiteid leiate sellest hoidlast `xx-python-agent-framework` ja `xx-dotnet-agent-framework` failide alt.

## Microsoft Agent Frameworki mõistmine

![Framework Intro](../../../translated_images/et/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) on Microsofti ühtne raamistik tehisintellekti agentide loomiseks. See pakub paindlikkust lahendada erinevaid agentidega seotud kasutusjuhtumeid nii tootmiskeskkondades kui ka teadusuuringutes, sealhulgas:

- **Järjestikune agentide orkestreerimine** olukordades, kus on vaja samm-sammulisi töövooge.
- **Samasajaline orkestreerimine** olukordades, kus agendid peavad ülesandeid korraga täitma.
- **Rühmavestluse orkestreerimine** olukordades, kus agendid saavad koos ühe ülesande kallal teha koostööd.
- **Ülesannete üleandmise orkestreerimine** olukordades, kus agendid annavad ülesandeid üksteisele üle, kui alamtööülesanded on täidetud.
- **Magnetiline orkestreerimine** olukordades, kus juhtagent loob ja muudab ülesannete nimekirja ning koordineerib alamagentide tegevust ülesande täitmiseks.

AI agentide tootmiseks sisaldab MAF ka järgmisi funktsioone:

- **Jälgitavus** OpenTelemetry kasutamise kaudu, kus iga AI agendi tegevus, sealhulgas tööriistade kutsumine, orkestreerimise sammud, mõtlemisvood ja jõudlusmonitoring Microsoft Foundry juhtpaneelide kaudu, on jälgitav.
- **Turvalisus** hostides agendid natiivselt Microsoft Foundryl, mis sisaldab turvakontrolle nagu rollipõhine ligipääs, privaatsete andmete käitlemine ja sisemise sisu turvalisus.
- **Püsivus** kuna agendi lõimed ja töövood saavad peatuda, jätkata ja taastuda vigadest, võimaldades pikemaajalist protsessi.
- **Juhtimine** toetades inimeste osalusega töövooge, kus ülesanded märgitakse inimkinnitust vajavateks.

Microsoft Agent Framework keskendub ka ühilduvusele läbi:

- **Pilvekaugusest sõltumatus** - agendid saavad töötada konteinerites, kohapeal ja erinevates pilvkeskkondades.
- **Teenusepakkuja sõltumatus** - agendid luuakse eelistatud SDK-de kaudu, sealhulgas Azure OpenAI ja OpenAI.
- **Avatud standardite kasutamine** - agendid saavad kasutada protokolle nagu Agent-to-Agent (A2A) ja Mudeli kontekstiprotocol (MCP) teiste agentide ja tööriistade avastamiseks ja kasutamiseks.
- **Pluginate ja pistikprogrammide kasutamine** - ühendused on võimalikud andme- ja mäluteenustega nagu Microsoft Fabric, SharePoint, Pinecone ja Qdrant.

Vaatame, kuidas neid funktsioone rakendatakse mõnedele Microsoft Agent Frameworki põhikontseptsioonidele.

## Microsoft Agent Frameworki põhikontseptsioonid

### Agendid

![Agent Framework](../../../translated_images/et/agent-components.410a06daf87b4fef.webp)

**Agentide loomine**

Agendi loomine toimub defineerides järeldusteenus (LLM-i pakkuja), komplekt juhiseid, mida AI agent peab järgima, ja määramata `name`:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Ülal kasutasime `Azure OpenAI`, kuid agente saab luua mitmete teenuste abil, sh `Microsoft Foundry Agent Service`:

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

või [MiniMax](https://platform.minimaxi.com/), mis pakub OpenAI-ga ühilduvat API-d suure kontekstipikkusega (kuni 204K tokenit):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

või kaugtöölisi A2A protokolli kaudu:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Agentide käivitamine**

Agendid käivitatakse `.run` või `.run_stream` meetoditega, sõltuvalt sellest, kas vastused on voogedastatavad või mitte.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Iga agendi käivitamisel saab määrata valikuid, mis kohandavad parameetreid nagu agenti kasutatavad `max_tokens`, tööriistad (`tools`), mida agent saab kutsuda, ja isegi kasutatav `model`.

See on kasulik olukordades, kus konkreetseid mudeleid või tööriistu on vaja kasutaja ülesande täitmiseks.

**Tööriistad**

Tööriistu saab määratleda nii agendi loomisel:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Kui luuakse ChatAgenti otse

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

kui ka agendi käivitamisel:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Tööriist mõeldud ainult selleks käivitamiseks )
```

**Agendi lõimed**

Agendi lõimesid kasutatakse mitmevooruliste vestluste haldamiseks. Lõime saab luua kas:

- Kasutades `get_new_thread()`, mis võimaldab lõime kauem salvestada
- Lõime automaatselt luues agendi käivitamisel, kus lõime kestus on vaid põhitöö käigus.

Lõime loomiseks näeb kood välja selline:

```python
# Loo uus niit.
thread = agent.get_new_thread() # Käivita agent niidiga.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Saate lõime serialiseerida hilisemaks kasutamiseks:

```python
# Loo uus lõim.
thread = agent.get_new_thread() 

# Käivita agent lõimiga.

response = await agent.run("Hello, how are you?", thread=thread) 

# Sarjusta lõim hoiustamiseks.

serialized_thread = await thread.serialize() 

# Desarjusta lõime olek pärast hoiustamisest laadimist.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agendi vahendustarkvara**

Agendid suhtlevad tööriistade ja LLMidega, et täita kasutaja ülesandeid. Mõningates olukordades soovime nende vahelist suhtlust täiendavalt käsitleda või jälgida. Agendi vahendustarkvara võimaldab seda teostada:

*Funktsioonide vahendustarkvara*

See vahendustarkvara võimaldab sooritada tegevust agendi ja funktsiooni/tööriista vahel, mida agent kutsub. Näiteks võib siin teha logimist funktsioonikutsel.

Alltoodud koodis määrab `next`, kas tuleb kutsuda järgmine vahendustarkvara või tegelik funktsioon.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Eeltöötlus: Logi enne funktsiooni täitmist
    print(f"[Function] Calling {context.function.name}")

    # Jätka järgmise vahendustaseme või funktsiooni täitmisega
    await next(context)

    # Järel­töötlus: Logi pärast funktsiooni täitmist
    print(f"[Function] {context.function.name} completed")
```

*Vestluse vahendustarkvara*

See vahendustarkvara võimaldab täita või logida tegevusi agendi ja LLMi päringute vahel.

See sisaldab tähtsat infot, nagu `messages`, mis saadetakse AI teenusele.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Eeltöötlus: Logi enne AI käsku
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Jätka järgmise vahendustarkvara või AI teenuseni
    await next(context)

    # Järelprotsessimine: Logi pärast AI vastust
    print("[Chat] AI response received")

```

**Agendi mälu**

Nagu õppetunnis `Agentic Memory` käsitletud, on mälu oluline agentide funktsioneerimiseks eri kontekstides. MAF pakub mitut erinevat tüüpi mälu:

*Mälu rakenduse jooksul (In-Memory Storage)*

See on mälu, mis on salvestatud lõimedes rakenduse jooksu ajal.

```python
# Loo uus lõim.
thread = agent.get_new_thread() # Käivita agent lõimega.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Püsivad sõnumid*

Seda mälu kasutatakse, kui vestluste ajalugu tuleb säilitada erinevate sessioonide vahel. See määratakse `chat_message_store_factory` abil:

```python
from agent_framework import ChatMessageStore

# Loo kohandatud sõnumite salvestuskoht
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dünaamiline mälu*


See mälu lisatakse konteksti enne agentide käivitamist. Neid mälusid saab salvestada välisteenustesse, nagu mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Kasutades Mem0 täiustatud mäluvõimaluste jaoks
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

Jälgitavus on oluline usaldusväärsete ja hooldatavate agentide süsteemide loomiseks. MAF integreerub OpenTelemetryga, et pakkuda jälgimist ja mõõdikuid parema jälgitavuse tagamiseks.

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

MAF pakub töövooge, mis on eeldefineeritud sammud ülesande täitmiseks ja sisaldavad AI agente komponentidena nendes sammudes.

Töövood koosnevad erinevatest komponentidest, mis võimaldavad paremat voolu juhtimist. Töövood võimaldavad ka **mitme agendi orkestreerimist** ja **kontrollpunktide seadmist** töövoo olekute salvestamiseks.

Töövoo põhilised komponendid on:

**Täideviijad**

Täideviijad võtavad vastu sisendsõnumeid, täidavad neile määratud ülesandeid ja seejärel genereerivad väljundisõnumi. See liigutab töövoogu edasi suurema ülesande täitmise suunas. Täideviijad võivad olla kas AI agent või kohandatud loogika.

**Sõlmed**

Sõlmed määravad töövoo sõnumite voo. Need võivad olla:

*Otseteed* - Lihtsad ühe-ühele ühendused täideviijate vahel:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Tingimuslikud teed* - Aktiveeritakse pärast teatud tingimuse täitmist. Näiteks saab täideviija soovitada teisi võimalusi, kui hotellitube pole saadaval.

*Valiku-tingimusega teed* - Suunavad sõnumeid erinevatele täideviijatele määratletud tingimuste alusel. Näiteks kui reisiseltskonnal on prioriteetne juurdepääs, saavad nende ülesanded teha läbi teise töövoo.

*Mitme-väljundiga teed* - Saadavad ühe sõnumi mitmele sihtkohale.

*Mitme-sisendiga teed* - Koguvad mitmeid sõnumeid erinevatelt täideviijatelt ja saadavad ühe sihtkohta.

**Sündmused**

Parema töövoo jälgitavuse pakkumiseks pakub MAF sisseehitatud täitmissündmusi, sealhulgas:

- `WorkflowStartedEvent`  - Töövoo täideviimine algab
- `WorkflowOutputEvent` - Töövoog genereerib väljundi
- `WorkflowErrorEvent` - Töövoos tekib viga
- `ExecutorInvokeEvent`  - Täideviija alustab töötlemist
- `ExecutorCompleteEvent`  - Täideviija lõpetab töötlemise
- `RequestInfoEvent` - Esitatakse päring

## Täiustatud MAF mustrid

Ülaltoodud osad käsitlevad Microsofti agentide raamistikku peamisi kontseptsioone. Kui loote keerukamaid agente, siis siin on mõned täiustatud mustrid, mida kaaluda:

- **Vahevara koostamine**: Kettige mitu vahevara käitlejat (logimine, autentimine, kiirusepiirang) funktsiooni ja vestluse vahevara abil agendi käitumise detailseks kontrollimiseks.
- **Töövoo kontrollpunktid**: Kasutage töövoo sündmusi ja serialiseerimist pikaajaliste agentide protsesside salvestamiseks ja jätkamiseks.
- **Dünaamiline tööriista valik**: Kombineerige RAG tööriistade kirjeldustega MAF tööriistade registreerimisega, et näidata ainult päringu jaoks asjakohaseid tööriistu.
- **Mitme agendi üleviimine**: Kasutage töövoo sõlmi ja tingimuslikku marsruutimist spetsialiseeritud agentide vahelisteks üleviimisteks.

## LangChain / LangGraph agentide majutamine Microsoft Foundry's

Microsoft Agent Framework on **raamistikude vahel ühilduv** — te ei ole piiratud ainult MAF-ga kirjutatud agentidega. Kui teil on juba agent, mis on loodud **LangChain** või **LangGraph** abil, saate selle käivitada kui **Microsoft Foundry majutatud agenti**, nii et Foundry haldab teie eest käitusaega, sessioone, skaleerimist, identiteeti ja protokolli lõpp-punkte, samal ajal kui teie agendi loogika jääb LangGraph'i.

Seda tehakse `langchain_azure_ai.agents.hosting` paketiga, mis avaldab kompileeritud LangGraph graafi samade protokollide kaudu, mida Foundry majutatud agendid kasutavad.

**1. Installige majutamise lisa:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` lisa installib Foundry protokolli teegid: `azure-ai-agentserver-responses` (OpenAI-ga ühilduv `/responses` lõpp-punkt) ja `azure-ai-agentserver-invocations` (üldine `/invocations` lõpp-punkt).

**2. Valige majutamise protokoll:**

| Protokoll | Host klass | Lõpp-punkt | Kasuta kui |
|----------|------------|------------|-----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Soovite OpenAI-ga ühilduvat vestlust, voogedastust, vastuse ajalugu ja vestluse niidistamist — see on soovitatud vaikimisi valik vestlusagentidele. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Vajate kohandatud JSON struktuuri, webhook-tüüpi lõpp-punkti või mittevestluslikku töötlemist. |

Kuna **Responses API on peamine API agentide arendamiseks Foundrys**, alustage `ResponsesHostServer`-iga enamiku agentide puhul.

**3. Konfigureerige keskkonnamuutujad** (`az login` esmalt, et `DefaultAzureCredential` saaks autentida):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Kui agent töötab hiljem Foundry majutatud agendina, süstib platvorm automaatselt `FOUNDRY_PROJECT_ENDPOINT` väärtuse.

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
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-5-mini")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI siinkohal sihib Foundry projekti OpenAI-ühilduvat (Vastused) lõpp-punkti.
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

Käivitage see lokaalselt käsuga `python main.py`, seejärel saatke päring aadressile `http://localhost:8088/responses`.

**Põhikäitumised:**

- **Vestlused**: Kliendid jätkavad vestlust, edastades `previous_response_id` või `conversation` ID. Kui teie graaf on kompileeritud LangGraphi kontrollpunktijälgijaga, seob Foundry vestluse oleku kontrollpunktiga (kasutage tootmises vastupidavat kontrollpunktijat; kohaliku testi jaoks sobib `MemorySaver`).
- **Inimene tsüklis**: Kui teie graaf kasutab LangGraphi `interrupt()`-i, kuvab `ResponsesHostServer` ootel oleva katkestuse Responses `function_call` / `mcp_approval_request` elemendina ning kliendid jätkavad sobiva `function_call_output` / `mcp_approval_response` päringuga.
- **Deploy Foundrysse**: Kasutage Azure Developer CLI-d — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokaalne, nõuab Dockerit), seejärel `azd provision` ja `azd deploy`. Majutatud agendi juurutamine nõuab **Foundry projekti halduri** rolli.

Käideldav näidis asub aadressil [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Täieliku juhendi (Invocations protokoll, kohandatud päringu skeemid ja tõrkeotsing) leiate siit: [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Koodinäited

Microsoft Agent Frameworki koodinäited on leitavad sellest hoidlast failides `xx-python-agent-framework` ja `xx-dotnet-agent-framework`.

## Kas teil on Microsoft Agent Frameworki kohta rohkem küsimusi?

Liituge [Microsoft Foundry Discordiga](https://discord.com/invite/ATgtXmAS5D), et kohtuda teiste õppijatega, osaleda avatud uste tundides ja saada vastused AI agentide küsimustele.
## Eelmine õppetund

[Mälu AI agentidele](../13-agent-memory/README.md)

## Järgmine õppetund


[Arvutikasutusagentide (CUA) loomine](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->