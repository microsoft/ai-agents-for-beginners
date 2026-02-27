# Microsoft Agent Frameworki uurimine

![Agendi raamistik](../../../translated_images/et/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Sissejuhatus

See õppetund käsitleb:

- Microsoft Agent Frameworki mõistmine: peamised omadused ja väärtus  
- Microsoft Agent Frameworki võtmekontseptsioonide uurimine
- Täiustatud MAF-mustrid: töövood, middleware ja mälu

## Õpieesmärgid

Pärast selle õppetunni läbimist oskad:

- Ehitada tootmiskõlbulikke tehisintellekti agente, kasutades Microsoft Agent Frameworki
- Rakendada Microsoft Agent Frameworki põhifunktsioone oma agentsetes kasutusjuhtumites
- Kasutada täiustatud mustreid, sealhulgas töövooge, middleware'i ja jälgitavust

## Koodinäited 

Koodinäited jaoks [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) leiad selles hoidlas failidest `xx-python-agent-framework` ja `xx-dotnet-agent-framework`.

## Microsoft Agent Frameworki mõistmine

![Raamistiku ülevaade](../../../translated_images/et/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) on Microsofti ühtne raamistik AI-agentide ehitamiseks. See pakub paindlikkust, et lahendada mitmesuguseid agentseid kasutusjuhtumeid nii tootmiskeskkonnas kui uurimistöös, sealhulgas:

- **Järjestikune agendi orkestreerimine** olukordades, kus on vaja samm-sammult töövooge.
- **Samaaegne orkestreerimine** olukordades, kus agendid peavad täitma ülesandeid samaaegselt.
- **Rühma-vestluse orkestreerimine** olukordades, kus agendid saavad ühist tööd teha ühe ülesande kallal.
- **Ülesande üleandmise orkestreerimine** olukordades, kus agendid annavad ülesandeid üksteisele alamülesannete täitmisel.
- **Magnetiline orkestreerimine** olukordades, kus halduragent loob ja muudab ülesannete nimekirja ning koordineerib subagentide tegevust ülesande lõpuleviimiseks.

AI-agentide tootmises kasutuselevõtuks sisaldab MAF ka funktsioone:

- **Jälgitavus** läbi OpenTelemetry kasutamise, kus iga AI-agendi tegevus, sealhulgas tööriistakutsete tegemine, orkestreerimise sammud, mõttekäigud ja jõudlusmonitooring Microsoft Foundry armatuurlaudadel, on jälgitav.
- **Turvalisus** hostides agente natiivselt Microsoft Foundryl, mis sisaldab turvakontrolle nagu rollipõhine juurdepääs, privaatse andmetöötluse ning sisseehitatud sisuohutuse.
- **Püsivus** kuna agendi lõimad ja töövood saavad peatuda, jätkuda ja taastuda vigadest, võimaldades pikemaajalisi protsesse.
- **Juhtimine** sest inimeste kaasamise töövood on toetatud, kus ülesanded märgitakse inimese kinnitust vajavaks.

Microsoft Agent Framework on suunatud ka koostalitlusele, pakkudes:

- **Pilvest sõltumatu** - Agendid saavad töötada konteinerites, kohapeal ja eri pilvekeskkondades.
- **Teenusepakkujast sõltumatu** - Agente saab luua sinu eelistatud SDK-de kaudu, sh Azure OpenAI ja OpenAI
- **Avatud standardite integreerimine** - Agendid saavad kasutada protokolle nagu Agent-to-Agent (A2A) ja Model Context Protocol (MCP), et leida ja kasutada teisi agente ja tööriistu.
- **Pluginad ja konnektorid** - Ühendusi saab luua andme- ja mäluteenustega nagu Microsoft Fabric, SharePoint, Pinecone ja Qdrant.

Vaatame, kuidas neid funktsioone rakendatakse mõne Microsoft Agent Frameworki põhikontseptsiooni puhul.

## Microsoft Agent Frameworki põhimõisted

### Agendid

![Agendi raamistik](../../../translated_images/et/agent-components.410a06daf87b4fef.webp)

**Agentide loomine**

Agendi loomine toimub järeldusteenuse (LLM Provider), komplekti juhistest, mida AI-agent järgib, ja määratud `name` määratlemise teel:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Ülaltoodud kasutab `Azure OpenAI`, kuid agente saab luua mitmesuguste teenuste abil, sealhulgas `Microsoft Foundry Agent Service`:

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

või kaugagendid, kasutades A2A-protokolli:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Agentide käivitamine**

Agendid käivitatakse, kasutades meetodeid `.run` või `.run_stream` mitte-voogu või voogu vastuste jaoks.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Iga agendi käivitamisel võivad olla ka valikud, et kohandada parameetreid, nagu agenti kasutatav `max_tokens`, agenti kutsutavad `tools` ja isegi agenti kasutatav `model`.

See on kasulik olukordades, kus ülesande täitmiseks on vaja konkreetseid mudeleid või tööriistu.

**Tööriistad**

Tööriistu saab määratleda nii agendi defineerimisel:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Kui ChatAgent luuakse otse

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

ning ka agendi käivitamisel:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Tööriist on antud ainult selle jooksu jaoks )
```

**Agendi lõimed**

Agendi lõime kasutatakse mitme vooruga vestluste käsitlemiseks. Lõime saab luua kas:

- Kasutades `get_new_thread()` , mis võimaldab lõime aja jooksul salvestada
- Lõime automaatne loomine agendi käivitamisel, kus lõim kestab ainult praeguse käivituse jooksul.

Lõime loomiseks näeb kood välja nõnda:

```python
# Loo uus lõim.
thread = agent.get_new_thread() # Käivita agent koos lõimiga.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Seejärel saab lõime serialiseerida hilisemaks kasutamiseks salvestamiseks:

```python
# Loo uus lõim.
thread = agent.get_new_thread() 

# Käivita agent lõimiga.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serialiseeri lõim salvestamiseks.

serialized_thread = await thread.serialize() 

# Deserialiseeri lõimi olek pärast laadimist salvestusest.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agendi middleware**

Agendid suhtlevad tööriistade ja LLM-idega kasutaja ülesannete täitmiseks. Teatud olukordades tahame nende interaktsioonide vahel täita või jälgida toiminguid. Agendi middleware võimaldab seda teha läbi:

*Funktsioonide middleware*

See middleware võimaldab meil täita toimingu agendi ja funktsiooni/tööriista vahel, mida see kutsub. Näide selle kasutamisest on olukord, kus soovid logida funktsioonikõnet.

Allolevas koodis määratleb `next`, kas kutsutakse järgmine middleware või tegelik funktsioon.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Eeltöötlus: Logi enne funktsiooni täitmist
    print(f"[Function] Calling {context.function.name}")

    # Jätka järgmise vahevara või funktsiooni täitmise juurde
    await next(context)

    # Järgtöötlus: Logi pärast funktsiooni täitmist
    print(f"[Function] {context.function.name} completed")
```

*Vestluse middleware*

See middleware võimaldab meil täita või logida toimingut agendi ja LLM-ile suunatavate päringute vahel.

See sisaldab olulist infot nagu `messages`, mis saadetakse AI-teenusele.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Eeltöötlus: Logi enne AI-kutset
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Jätka järgmise vahendustarkvara või AI-teenuse juurde
    await next(context)

    # Järeltöötlus: Logi pärast AI-vastust
    print("[Chat] AI response received")

```

**Agendi mälu**

Nagu õppetunnis `Agentic Memory` käsitletud, on mälu oluline komponent, mis võimaldab agendil toimida erinevates kontekstides. MAF pakub mitut erinevat mälutüüpi:

*Mälusisene salvestus*

See on mälu, mis salvestatakse lõimedes rakenduse tööaja jooksul.

```python
# Loo uus lõim.
thread = agent.get_new_thread() # Käivita agent koos lõimiga.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Püsivad sõnumid*

Seda mälu kasutatakse, kui vestluse ajalugu salvestatakse erinevate sessioonide vahel. See on määratletud kasutades `chat_message_store_factory` :

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

See mälu lisatakse konteksti enne agentide käivitamist. Need mälud võivad olla salvestatud välistesse teenustesse, nagu mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Mem0 kasutamine täiustatud mäluvõimaluste jaoks
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

Jälgitavus on oluline usaldusväärsete ja hooldatavate agentsüsteemide ehitamiseks. MAF integreerub OpenTelemetryga, et pakkuda jälgimist ja meetreid parema jälgitavuse jaoks.

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

MAF pakub töövooge, mis on eelmääratletud sammud ülesande lõpetamiseks ja mis sisaldavad AI-agente nende sammude komponendidena.

Töövood koosnevad erinevatest komponentidest, mis võimaldavad paremat voolu juhtimist. Töövood võimaldavad ka **mitme agendi orkestreerimist** ja **kontrollpunktimist**, et salvestada töövoo olekuid.

Töövoo põhikomponendid on:

**Täideviijad**

Täideviijad võtavad vastu sisendsõnumeid, täidavad neile määratud ülesandeid ja seejärel toodavad väljundsõnumi. See viib töövoogu edasi suurema ülesande lõpetamise suunas. Täideviijad võivad olla kas AI-agent või kohandatud loogika.

**Ühendused**

Ühendusi kasutatakse töövoos sõnumite voo määratlemiseks. Need võivad olla:

*Otsesed servad* - Lihtsad üks-ühele ühendused täideviijate vahel:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Tingimuslikud servad* - Aktiveeruvad pärast teatud tingimuse täitumist. Näiteks kui hotellitoad pole saadaval, võib täideviija soovitada muid valikuid.

*Switch-case servad* - Suunavad sõnumeid erinevatele täideviijatele vastavalt määratletud tingimustele. Näiteks kui reisikliendil on prioriteedijuurdepääs, siis tema ülesandeid käsitletakse teise töövoo kaudu.

*Fan-out servad* - Saadavad ühe sõnumi mitmele sihtmärgile.

*Fan-in servad* - Koguvad mitmeid sõnumeid erinevatelt täideviijatelt ja saadavad ühe sihtmärgile.

**Sündmused**

Parema jälgitavuse tagamiseks töövoogudes pakub MAF sisseehitatud sündmusi täitmise jaoks, sealhulgas:

- `WorkflowStartedEvent`  - Töövoo täitmine algab
- `WorkflowOutputEvent` - Töövoog toodab väljundi
- `WorkflowErrorEvent` - Töövooga tekib viga
- `ExecutorInvokeEvent`  - Täideviija alustab töötlemist
- `ExecutorCompleteEvent`  -  Täideviija lõpetab töötlemise
- `RequestInfoEvent` - Taotlus esitatakse

## Täiustatud MAF-mustrid

Ülaltoodud jaotised käsitlevad Microsoft Agent Frameworki põhikontseptsioone. Kui ehitad keerukamaid agente, siis siin on mõned täiustatud mustrid, mida kaaluda:

- **Middleware'i kompositsioon**: Keti mitut middleware-käitlejat (logimine, autentimine, taotluste piiramine) kasutades funktsiooni- ja vestluse middleware'i, et saavutada peenhäälestatud kontroll agendi käitumise üle.
- **Töövoo kontrollpunktimine**: Kasuta töövoo sündmusi ja serialiseerimist pikkade agentiprotsesside salvestamiseks ja jätkamiseks.
- **Dünaamiline tööriista valik**: Ühenda RAG tööriistakirjelduste üle koos MAF-i tööriistaregistreerimisega, et päringu kohta kuvada ainult asjakohased tööriistad.
- **Mitme agendi ülesande üleandmine**: Kasuta töövoo ühendusi ja tingimuslikku marsruutimist spetsialiseerunud agentide vaheliste üleandmiste orkestreerimiseks.

## Koodinäited 

Microsoft Agent Frameworki koodinäited leiad selles hoidlas failidest `xx-python-agent-framework` ja `xx-dotnet-agent-framework`.

## Kas sul on rohkem küsimusi Microsoft Agent Frameworki kohta?

Liitu [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) , et kohtuda teiste õppijatega, osaleda konsultatsioonitundides ja saada vastuseid oma AI-agentide küsimustele.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vastutusest loobumine:
See dokument on tõlgitud tehisintellektil põhineva tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi me püüame tagada täpsust, palun pidage meeles, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle algkeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta ühegi sellisest tõlkest tuleneva arusaamatuse ega valesti tõlgendamise eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->