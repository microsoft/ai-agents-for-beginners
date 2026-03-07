# Microsoft Agent Frameworki uurimine

![Agentide raamistik](../../../translated_images/et/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Sissejuhatus

See õppetund käsitleb:

- Microsoft Agent Frameworki mõistmine: põhifunktsioonid ja väärtus  
- Microsoft Agent Frameworki põhikontseptsioonide uurimine
- Täpsemad MAF-mustrid: töövood, vahendustarkvara ja mälu

## Õpieesmärgid

Pärast selle õppetunni läbimist oskate:

- Ehitada tootmiskõlblikke AI-agente, kasutades Microsoft Agent Frameworki
- Rakendada Microsoft Agent Frameworki põhifunktsioone oma agentsetes kasutusjuhtudes
- Kasutada edasijõudnud mustreid, sealhulgas töövoogusid, vahendustarkvara ja jälgitavust

## Koodinäited 

Koodinäiteid [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) jaoks leiate sellest hoidlast failidest `xx-python-agent-framework` ja `xx-dotnet-agent-framework`.

## Microsoft Agent Frameworki mõistmine

![Raamistiku ülevaade](../../../translated_images/et/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) on Microsofti ühtne raamistik AI-agentide loomisel. See pakub paindlikkust erinevate agentsete kasutusjuhtude lahendamiseks, mida kohtab nii tootmiskeskkonnas kui uurimistöös, sealhulgas:

- **Järjestikune agendi orkestreerimine** olukordades, kus on vaja samm-sammult töövooge.
- **Samaaegne orkestreerimine** olukordades, kus agentidel on vaja ülesandeid samaaegselt täita.
- **Rühmavestluse orkestreerimine** olukordades, kus agentid saavad üheskoos ühel ülesandel koostööd teha.
- **Üleandmise orkestreerimine** olukordades, kus agentid annavad ülesande osadena üksteisele üle, kui alamülesanded on lõpetatud.
- **Magnetiline orkestreerimine** olukordades, kus juhatajaagent loob ja muudab ülesannete nimekirja ning koordineerib abiagentide tööd ülesande täitmiseks.

AI-agentide juurutamiseks tootmiskeskkonda sisaldab MAF ka järgmisi funktsioone:

- **Jälgitavus** OpenTelemetry abil, kus iga AI-agendi tegevus — sh tööriistakutsed, orkestreerimisetapid, põhjendamisvood ja jõudluse jälgimine Microsoft Foundry armatuurlaatide kaudu.
- **Turvalisus** hostides agente natiivselt Microsoft Foundry's, mis sisaldab turvakontrolle nagu rollipõhine juurdepääs, privaatsete andmete käitlemine ja sisseehitatud sisuturve.
- **Püsivus** kuna agendi lõimed ja töövood võivad peatuda, jätkuda ja taastuda vigadest, mis võimaldab pikemaajalisi protsesse.
- **Kontroll** kuna inimeste kaasamise töövood on toetatud, kus ülesandeid märgitakse nõudvat inimkinnitust.

Microsoft Agent Framework on suunatud ka koostalitlusvõimele:

- **Pilveagnostiline** - agentid võivad töötada konteinerites, kohapeal ja mitmes erinevas pilves.
- **Teenusepakkujast sõltumatu** - agente saab luua eelistatud SDK kaudu, sh Azure OpenAI ja OpenAI
- **Avatud standardite integreerimine** - agentid saavad kasutada protokolle nagu Agent-to-Agent(A2A) ja Model Context Protocol (MCP), et avastada ja kasutada teisi agente ja tööriistu.
- **Pistikprogrammid ja ühendused** - ühendused saab luua andme- ja mäluteenustega nagu Microsoft Fabric, SharePoint, Pinecone ja Qdrant.

Vaatame, kuidas neid funktsioone rakendatakse Microsoft Agent Frameworki mõnele põhimõistele.

## Microsoft Agent Frameworki põhimõisted

### Agentid

![Agentide raamistik](../../../translated_images/et/agent-components.410a06daf87b4fef.webp)

**Agentide loomine**

Agendi loomine toimub, määrates ennustus-teenuse (LLM Provider), komplekti juhiste, mida AI-agent järgib, ja määratud `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Ülaltoodud kasutab `Azure OpenAI`, kuid agente saab luua mitmete teenuste abil, sealhulgas `Microsoft Foundry Agent Service`:

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

või kaugagente, kasutades A2A protokolli:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Agentide käivitamine**

Agente käitatakse, kasutades meetodeid `.run` või `.run_stream` vastavalt mittevoogedastuse või voogedastuse vastuste jaoks.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Igal agendi käivitusel võivad samuti olla valikud parameetrite kohandamiseks, nagu agendi poolt kasutatav `max_tokens`, `tools`, mida agent saab kutsuda, ja isegi `model`, mida agent kasutab.

See on kasulik juhtudel, kus ülesande täitmiseks on vajalikud konkreetsed mudelid või tööriistad.

**Tööriistad**

Tööriistad saab määratleda nii agendi defineerimisel:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Kui loote ChatAgenti otse

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

ning ka agendi käivitamisel:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Tööriist antud ainult selle jooksu jaoks )
```

**Agendi lõimed**

Agendi lõime kasutatakse mitmekäiguliste vestluste haldamiseks. Lõime saab luua kas:

- Kasutades `get_new_thread()`, mis võimaldab lõime aja jooksul salvestada
- Lõime automaatne loomine agendi käivitamisel, kus lõim kestab vaid selle jooksu jooksul.

Lõime loomiseks näeb kood välja järgmine:

```python
# Loo uus lõim.
thread = agent.get_new_thread() # Käivita agent koos lõimiga.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Seejärel saate lõime serialiseerida, et seda hiljem salvestada:

```python
# Loo uus lõim.
thread = agent.get_new_thread() 

# Käivita agent koos lõimiga.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serialiseeri lõim salvestamiseks.

serialized_thread = await thread.serialize() 

# Deserialiseeri lõimi olek pärast salvestusest laadimist.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agendi vahendustarkvara**

Agentid suhtlevad tööriistade ja LLM-idega, et täita kasutaja ülesandeid. Teatud olukordades tahame nende suhtluste vahel täita või jälgida tegevusi. Agendi vahendustarkvara võimaldab seda läbi:

*Funktsiooni vahendustarkvara*

See vahendustarkvara võimaldab meil täita tegevust agendi ja funktsiooni/tööriista (mida see kutsub) vahel. Näide kasutusest on olukord, kus soovite funktsioonikutsest logimist teha.

Allolevas koodis määrab `next`, kas tuleks kutsuda järgmine vahendustarkvara või tegelik funktsioon.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Eeltöötlus: Logi enne funktsiooni täitmist
    print(f"[Function] Calling {context.function.name}")

    # Jätka järgmise vahekihini või funktsiooni täitmiseni
    await next(context)

    # Pärasttöötlus: Logi pärast funktsiooni täitmist
    print(f"[Function] {context.function.name} completed")
```

*Vestluse vahendustarkvara*

See vahendustarkvara võimaldab meil täita või logida tegevust agendi ja päringute vahel LLM-ile.

See sisaldab olulist teavet, näiteks `messages`, mis saadetakse AI-teenusele.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Eeltöötlus: Logi enne tehisintellekti kõnet
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Jätka järgmise vahevara või tehisintellekti teenuse juurde
    await next(context)

    # Järeltöötlus: Logi pärast tehisintellekti vastust
    print("[Chat] AI response received")

```

**Agendi mälu**

Nagu on käsitletud õppetunnis `Agentic Memory`, on mälu oluline element, mis võimaldab agendil toimida erinevates kontekstides. MAF pakub mitut erinevat tüüpi mälusid:

*Mälusisene salvestus*

See on mälu, mis salvestatakse lõimedes rakenduse tööajal.

```python
# Loo uus lõim.
thread = agent.get_new_thread() # Käivita agent lõimiga.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Püsivad sõnumid*

Seda mälu kasutatakse vestluste ajaloo salvestamiseks erinevate seansside vahel. See määratletakse `chat_message_store_factory` abil:

```python
from agent_framework import ChatMessageStore

# Loo kohandatud sõnumihoidla
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dünaamiline mälu*

See mälu lisatakse konteksti enne agentide käivitamist. Neid mälusid saab salvestada välisteenustesse nagu mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Mem0 kasutamine edasijõudnud mäluvõimaluste jaoks
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

Jälgitavus on oluline usaldusväärsete ja hooldatavate agentsete süsteemide ehitamisel. MAF integreerub OpenTelemetryga, et pakkuda jälgimist ja meetreid parema jälgitavuse jaoks.

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

MAF pakub töövooge, mis on eelmääratletud sammud ülesande täitmiseks ja hõlmavad nendes sammudes AI-agente kui komponente.

Töövood koosnevad erinevatest komponentidest, mis võimaldavad paremat kontrollvoogu. Töövood võimaldavad ka **mitmeagendi orkestreerimist** ja **kontrollpunktimist** töövoo olekute salvestamiseks.

Töövoo põhikomponendid on:

**Täideviijad**

Täideviijad võtavad vastu sisendsõnumeid, täidavad neile määratud ülesandeid ja seejärel genereerivad väljund-sõnumi. See liigutab töövoogu edasi suurema ülesande täitmise suunas. Täideviijad võivad olla AI-agent või kohandatud loogika.

**Servad**

Servasid kasutatakse sõnumivoo määratlemiseks töövoos. Need võivad olla:

*Otsesed servad* - lihtsad üks-ühele ühendused täideviijate vahel:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Tingimuslikud servad* - aktiveeritakse pärast teatud tingimuse täitumist. Näiteks kui hotellitoad pole saadaval, saab täideviija soovitada muid võimalusi.

*Switch-case servad* - marsruutida sõnumeid erinevatele täideviijatele vastavalt määratletud tingimustele. Näiteks kui reisikliendil on prioriteetne juurdepääs ja nende ülesandeid töödeldakse läbi teise töövoo.

*Hargnemisservad* - saata üks sõnum mitmele sihtmärgile.

*Kogumisservad* - koguda mitu sõnumit erinevatelt täideviijatelt ja saata ühele sihtmärgile.

**Sündmused**

Parema jälgitavuse tagamiseks töövoogudes pakub MAF sisseehitatud täitmissündmusi, sh:

- `WorkflowStartedEvent`  - töövoo täitmine algab
- `WorkflowOutputEvent` - töövoog genereerib väljundi
- `WorkflowErrorEvent` - töövoos tekib viga
- `ExecutorInvokeEvent`  - täideviija alustab töötlemist
- `ExecutorCompleteEvent`  -  täideviija lõpetab töötlemise
- `RequestInfoEvent` - päring esitatakse

## Täpsemad MAF-mustrid

Ülaltoodud jaotised käsitlevad Microsoft Agent Frameworki põhikontseptsioone. Kui arendate keerukamaid agente, kaaluge järgmisi täpsemaid mustreid:

- **Vahendustarkvara koostamine**: aheldage mitu vahendustarkvara käitlejat (logimine, autentimine, piirkiirus) kasutades funktsiooni- ja vestlusvahendustarkvara peenhäälestatud kontrolli saavutamiseks agendi käitumise üle.
- **Töövoo kontrollpunktimine**: kasutage töövoo sündmusi ja serialiseerimist pikalt kestvate agendi protsesside salvestamiseks ja jätkamiseks.
- **Dünaamiline tööriistavalik**: kombineerige RAG tööriistakirjelduste üle MAF-i tööriista registreerimisega, et päringu kohta kuvada ainult asjakohased tööriistad.
- **Mitmeagendi üleandmine**: kasutage töövoo servasid ja tingimuslikku marsruutimist, et orkestreerida üleandmisi spetsialiseeritud agentide vahel.

## Koodinäited 

Koodinäited Microsoft Agent Frameworki jaoks asuvad selles hoidlas failides `xx-python-agent-framework` ja `xx-dotnet-agent-framework`.

## Kas teil on veel küsimusi Microsoft Agent Frameworki kohta?

Liituge [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)iga, et kohtuda teiste õppijatega, osaleda konsultatsioonitundides ja saada vastused oma AI-agentide küsimustele.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Lahtiütlus:
See dokument on tõlgitud tehisintellekti tõlketeenuse Co-op Translator (https://github.com/Azure/co-op-translator) abil. Kuigi me püüame tagada täpsust, pidage palun meeles, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokumenti selle algkeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste ega valede tõlgenduste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->