# Microsoft Agent Frameworki avastamine

![Agent Framework](../../../translated_images/et/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Sissejuhatus

See õppetund käsitleb:

- Microsoft Agent Frameworki mõistmine: Põhifunktsioonid ja väärtus  
- Microsoft Agent Frameworki põhikontseptsioonide avastamine
- Täiustatud MAF mustrid: töövood, vahevara ja mälu

## Õpieesmärgid

Pärast selle õppetunni läbimist oskad:

- Ehita tootmiskõlblikke tehisintellekti agente Microsoft Agent Frameworki abil
- Rakenda Microsoft Agent Frameworki põhifunktsioone oma agentuursete kasutusjuhtumite jaoks
- Kasuta täiustatud mustreid, sealhulgas töövooge, vahevara ja jälgitavust

## Koodinäited 

Koodinäited [Microsoft Agent Frameworki (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) kohta leiad sellest hoidlast failide `xx-python-agent-framework` ja `xx-dotnet-agent-framework` alt.

## Microsoft Agent Frameworki mõistmine

![Framework Intro](../../../translated_images/et/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) on Microsofti ühtne raamistik tehisintellekti agentide ehitamiseks. See pakub paindlikkust erinevate agentuursete kasutusjuhtumite lahendamiseks nii tootmiskeskkonnas kui ka uurimistöös, sealhulgas:

- **Järjestikune agentide orkestreerimine** olukordades, kus on vajalikud samm-sammult töövood.
- **Samasajaline orkestreerimine** olukordades, kus agendid peavad ülesandeid samaaegselt täitma.
- **Grupi vestluse orkestreerimine** olukordades, kus agendid saavad koos ühe ülesande kallal koostööd teha.
- **Ülesande üleandmise orkestreerimine** olukordades, kus agendid annavad ülesande alamülesannetena üksteisele üle.
- **Magnetiline orkestreerimine** olukordades, kus juht-agent loob ja muudab ülesannete nimekirja ning koordineerib alamagentide tegevust ülesande täitmiseks.

Tootmiskeskkonna AI agentide tarnimiseks sisaldab MAF lisaks järgmisi funktsioone:

- **Jälgitavust** kasutades OpenTelemetryt, kus igasugune AI agendi tegevus, sealhulgas tööriistakutsete, orkestreerimise sammude, mõttekäikude ja jõudluse jälgimine Microsoft Foundry armatuurlaudade kaudu on nähtav.
- **Turvalisust** majutades agente natiivsete Microsoft Foundry keskkonnas, mis sisaldab turvakontrolli nagu rollipõhine ligipääs, privaatandmete käitlemine ja sisuturbe ehitamine.
- **Vastupidavust**, kuna agendi lõimed ja töövood võivad peatuda, jätkata ja taastuda vigadest, võimaldades pikemaid protsesse.
- **Juhtimist**, kuna inimesega kaasatud töövood toetavad ülesandeid, mis vajavad inimese kinnitust.

Microsoft Agent Framework keskendub ka ühilduvusele, võimaldades:

- **Pilvest sõltumatust** - Agendid saavad töötada konteinerites, kohapeal ja mitmes erinevas pilves.
- **Tarnija sõltumatust** - Agente saab luua eelistatud SDK-ga, sh Azure OpenAI ja OpenAI abil.
- **Avatud standardite integreerimist** - Agendid saavad kasutada protokolle nagu Agent-to-Agent (A2A) ja Model Context Protocol (MCP), et avastada ja kasutada teisi agente ning tööriistu.
- **Pluginad ja ühendused** - Ühendused võimaldavad andme- ja mäluteenuseid nagu Microsoft Fabric, SharePoint, Pinecone ja Qdrant.

Vaatame, kuidas neid funktsioone rakendatakse Microsoft Agent Frameworki mõningates põhikontseptsioonides.

## Microsoft Agent Frameworki põhikontseptsioonid

### Agendid

![Agent Framework](../../../translated_images/et/agent-components.410a06daf87b4fef.webp)

**Agentide loomine**

Agendi loomine toimub defineerides järeldamisteenus (LLM pakkuja), komplekt juhiseid AI agendile järgimiseks ja määrates `name`:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Ülaltoodud näide kasutab `Azure OpenAI`, kuid agente saab luua mitmete teenuste abil, sh `Microsoft Foundry Agent Service`:

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

või [MiniMax](https://platform.minimaxi.com/), mis pakub OpenAI-ga ühilduvat API-t suurte kontekstivõimalustega (kuni 204K tokenit):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

või kaugagendid kasutades A2A protokolli:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Agentide käivitamine**

Agente käitatakse `.run` või `.run_stream` meetoditega, vastavalt mittestriimiliste või voopõhiste vastuste puhul.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Iga agendi käivitamisel võib olla ka võimalusi kohandada parameetreid nagu agendi poolt kasutatavad `max_tokens`, agendi poolt kutsutavad `tools` ja isegi agendi jaoks kasutatav `model`.

See on kasulik juhtudel, kus konkreetseid mudeleid või tööriistu on vaja kasutaja ülesande täitmiseks.

**Tööriistad**

Tööriistu saab määratleda nii agendi loomisel:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ChatAgendi otsese loomise korral

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

kui ka agendi käivitamisel:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Tööriist, mis on mõeldud ainult selle käivituse jaoks )
```

**Agentide lõimed**

Agentide lõimedega hallatakse mitme vooruga vestlusi. Lõime saab luua kas:

- `get_new_thread()` abil, mis võimaldab lõime salvestada aja jooksul
- automaatse lõime loomisega agendi käivitamisel, kus lõime kestab ainult jooksva seansi jooksul.

Lõime loomiseks näeb kood välja selline:

```python
# Loo uus niit.
thread = agent.get_new_thread() # Käivita agent niidiga.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Lõime võib seejärel serialiseerida hilisemaks salvestamiseks:

```python
# Loo uus niit.
thread = agent.get_new_thread() 

# Käivita agent koos niidiga.

response = await agent.run("Hello, how are you?", thread=thread) 

# Sereali keera niit salvestamiseks.

serialized_thread = await thread.serialize() 

# Desereali keera niidi olek pärast laadimist salvestusest.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agendi vahevara**

Agendid suhtlevad tööriistade ja LLM-idega kasutaja ülesannete täitmiseks. Teatud olukordades soovime nende suhtluste vahepeal käivitada või jälgida tegevusi. Agendi vahevara võimaldab seda teha läbi:

*Funktsioonide vahevara*

See vahevara võimaldab käivitada tegevuse agendi ja funktsiooni/tööriista vahel, mida see kutsub. Näiteks võib see olla kasulik funktsiooni kõnede logimiseks.

Järgnev koodis määrab `next`, kas kutsutakse järgmine vahevara või tegelik funktsioon.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Eeltöötlus: Logi enne funktsiooni täitmist
    print(f"[Function] Calling {context.function.name}")

    # Jätka järgmise vahenduse või funktsiooni täitmisega
    await next(context)

    # Järelprotsess: Logi pärast funktsiooni täitmist
    print(f"[Function] {context.function.name} completed")
```

*Vestluse vahevara*

See vahevara võimaldab käivitada või logida tegevust agendi ja LLM vahelistes taotlustes.

See sisaldab olulist infot, nagu AI teenusele saadetavad `sõnumid`.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Eeltöötlus: Logi enne tehisintellekti kutset
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Jätka järgmise vahendustarkvara või tehisintellekti teenusega
    await next(context)

    # Järeltoiming: Logi pärast tehisintellekti vastust
    print("[Chat] AI response received")

```

**Agendi mälu**

Nagu on käsitletud õppetunnis `Agentic Memory`, on mälu oluline komponent, mis võimaldab agendil töötada erinevates kontekstides. MAF pakub mitut erinevat mälutüüpi:

*Mälu rakenduse sees*

See on mälu, mis salvestatakse lõimedes rakenduse tööajal.

```python
# Loo uus lõim.
thread = agent.get_new_thread() # Käivita agent koos lõimega.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Püsivad sõnumid*

Seda mälu kasutatakse vestluste ajaloo salvestamiseks erinevate sessioonide vahel. See on määratletud kasutades `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Loo kohandatud sõnumite salvestus
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dünaamiline mälu*

Seda mälu lisatakse konteksti enne agendi käivitamist. Seda võib hoida väliste teenuste nagu mem0 abil:

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

Jälgitavus on oluline usaldusväärsete ja hooldatavate agentuuri süsteemide loomiseks. MAF integreerub OpenTelemetryga, pakkudes jälgimist ja mõõdikuid parema jälgitavuse jaoks.

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

MAF pakub töövooge, mis on eelmääratletud sammud ülesande täitmiseks, kaasates AI agente nende sammude komponentidena.

Töövood koosnevad erinevatest komponentidest, mis võimaldavad paremat voolu juhtimist. Töövood võimaldavad ka **mitme agendi orkestreerimist** ja **läbipääsupunktide loomist** töövoogude olekute salvestamiseks.

Töövoo põhikomponendid on:

**Täideviijad**

Täideviijad saavad sisendsõnumeid, täidavad neile määratud ülesandeid ja toodavad väljundisõnumeid. See viib töövoo edasi suurema ülesande täitmise suunas. Täideviijad võivad olla kas AI agent või kohandatud loogika.

**Servad**

Servasid kasutatakse sõnumite voo määratlemiseks töövoos. Need võivad olla:

*Otseühendused* - Lihtsad ühelt täideviijalt teisele ühendused:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Tingimuslikud ühendused* - Aktiveeritakse, kui teatud tingimus on täidetud. Näiteks kui hotellitoad ei ole saadaval, saab täideviija soovitada muid võimalusi.

*Lüliti-juhtumi ühendused* - Suunavad sõnumeid erinevatele täideviijatele vastavalt määratletud tingimustele. Näiteks kui reisiklient on prioriteediga, käsitletakse tema ülesanded teise töövoo kaudu.

*Hulgisaadetised* - Saadab ühe sõnumi mitmele sihtmärgile.

*Hulgakogumised* - Kogub mitme täideviija sõnumeid ja saadab ühe sihtmärgi juurde.

**Sündmused**

Paremaks jälgitavuseks töövoogudel pakub MAF sisseehitatud sündmusi täitmise jaoks, sealhulgas:

- `WorkflowStartedEvent`  - töövoo täitmine algab
- `WorkflowOutputEvent` - töövoog genereerib väljundi
- `WorkflowErrorEvent` - töövoos tekib tõrge
- `ExecutorInvokeEvent`  - täideviija alustab töötlemist
- `ExecutorCompleteEvent`  - täideviija lõpetab töötlemise
- `RequestInfoEvent` - taotlus esitatakse

## Täiustatud MAF mustrid

Ülaltoodud osad käsitlevad Microsoft Agent Frameworki põhikontseptsioone. Kui ehitad keerukamaid agente, siis siin on mõned täiustatud mustrid, mida kaaluda:

- **Vahevara kokkupanek**: Kettita mitut vahevara käsitlejat (logimine, autentimine, kiirusepiirang) funktsiooni- ja vestlusvahevara abil täpsema kontrolli saamiseks agendi käitumise üle.
- **Töövoo läbipääsupunktid**: Kasuta töövoo sündmusi ja serialiseerimist pikkade agentide protsesside salvestamiseks ja jätkamiseks.
- **Dünaamiline tööriista valik**: Ühenda RAG tööriistakirjelduste üle MAF-i tööriistaregistreerimisega, et päringu kohta esitada vaid sobivad tööriistad.
- **Mitme agendi ülesande üleminek**: Kasuta töövoo servi ja tingimuslikku marsruutimist spetsialiseeritud agentide vahelisteks ülesannete üleandmisteks.

## LangChain / LangGraph agentide majutamine Microsoft Foundryl

Microsoft Agent Framework on **raamistikuülene** — sa ei ole piiratud ainult MAFis kirjutatud agentidega. Kui sul on juba agent ehitatud **LangChaini** või **LangGraphiga**, saad seda käitada kui **Microsoft Foundry majutatud agenti**, kus Foundry haldab jooksutamist, sessioone, skaleerimist, identiteeti ja protokolli lõpp-punkte, samal ajal kui sinu agendi loogika jääb LangGraphi.

Seda tehakse paketiga `langchain_azure_ai.agents.hosting`, mis eksponeerib koos kompileeritud LangGraph graafiku samadel protokollidel, mida Foundry majutatud agendid kasutavad.

**1. Paigalda hosting lisa:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` lisa paigaldab Foundry protokolliteegid: `azure-ai-agentserver-responses` (OpenAI-yhildub `/responses` lõpp-punkt) ja `azure-ai-agentserver-invocations` (üldine `/invocations` lõpp-punkt).

**2. Vali majutamisprotokoll:**

| Protokoll | Host klass | Lõpp-punkt | Kasuta kui |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Soovid OpenAI-yhildavat vestlust, striimimist, vastuste ajalugu ja vestluse lõimimist — see on soovitatud vaikimisi mitmepoolses vestluses. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Vajad kohandatud JSON-kuju, webhook-tüüpi lõpp-punkti või mittevestlusvoogudega töötlemist. |

Kuna **Responses API on Foundry peamine agentuuri-arenduse API**, alusta enamike agentide puhul `ResponsesHostServer`-iga.

**3. Konfigureeri keskkonnamuutujad** (`az login` esmalt, et `DefaultAzureCredential` saaks autentida):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

Kui agent hiljem käib Foundry majutatud agendina, süstib platvorm automaatselt `FOUNDRY_PROJECT_ENDPOINT`.

**4. Eksponeeri LangGraph agent Responses protokolli kaudu:**

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

    # ChatOpenAI sihib siin Foundry projekti OpenAI-ga ühilduvale (Responses) lõpp-punktile.
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

Käivita lokaalselt käsuga `python main.py`, seejärel saada Responses taotlus aadressile `http://localhost:8088/responses`.

**Peamised omadused:**

- **Vestlused**: Kliendid jätkavad vestlust, edastades `previous_response_id` või `conversation` ID. Kui su graafik on kompileeritud LangGraphi läbipääsupunktiga, võtab Foundry vestluse oleku salvestamiseks läbipääsupunkti võtme (kasuta tootmises vastupidavat läbipääsupunkti; `MemorySaver` sobib lokaalseks testimiseks).
- **Inimesega kaasatus**: Kui graafikus kasutatakse LangGraphi `interrupt()`, kuvab `ResponsesHostServer` ootel katkestuse Responsei `function_call` / `mcp_approval_request` kirjena ja kliendid jätkavad sobiva `function_call_output` / `mcp_approval_response` vastusega.
- **Deploy Foundry-sse**: Kasuta Azure Developer CLI-d — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokaalne, nõuab Dockerit), siis `azd provision` ja `azd deploy`. Majutatud agendi kasutuselevõtt nõuab **Foundry projektihalduri** rolli.

Jooksev näidis sellest asub failis [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Täieliku läbivaatuse jaoks (Invocations protokoll, kohandatud päringu skeemid ja veaotsing) vaata [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Koodinäited 

Microsoft Agent Frameworki koodinäited leiad sellest hoidlast failide `xx-python-agent-framework` ja `xx-dotnet-agent-framework` alt.

## Veel küsimusi Microsoft Agent Frameworki kohta?

Liitu [Microsoft Foundry Discordiga](https://discord.com/invite/ATgtXmAS5D), et kohtuda teiste õppijatega, osaleda vastuvõtutundides ja saada oma AI agentide küsimustele vastused.
## Eelmine õppetund

[AI agentide mälu](../13-agent-memory/README.md)

## Järgmine õppetund

[Arvuti kasutamise agentide loomine (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->