# Microsoft Agent Framework tyrinėjimas

![Agent Framework](../../../translated_images/lt/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Įvadas

Šioje pamokoje bus aptariama:

- Microsoft Agent Framework supratimas: pagrindinės savybės ir vertė  
- Pagrindinių Microsoft Agent Framework sąvokų tyrinėjimas
- Pažangūs MAF modeliai: darbų eiga, tarpinis programavimas ir atmintis

## Mokymosi tikslai

Baigus šią pamoką, žinosite, kaip:

- Kurti gamybai paruoštus DI agentus naudojant Microsoft Agent Framework
- Taikyti pagrindines Microsoft Agent Framework funkcijas savo agentiniams naudojimo atvejams
- Naudoti pažangius modelius, įskaitant darbų eigas, tarpinį programavimą ir stebėjimą

## Kodo pavyzdžiai 

Kodo pavyzdžius, skirtus [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok), rasite šiame saugykloje `xx-python-agent-framework` ir `xx-dotnet-agent-framework` failuose.

## Microsoft Agent Framework supratimas

![Framework Intro](../../../translated_images/lt/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) yra Microsoft vieningas karkasas DI agentams kurti. Jis suteikia lankstumą spręsti įvairius agentinius naudojimo atvejus, pastebimus tiek gamybos, tiek tyrimų aplinkose, įskaitant:

- **Sekvos agentų orkestracija** scenarijuose, kur reikia žingsnis po žingsnio darbų eigų.
- **Konkuruojanti orkestracija** scenarijuose, kai agentai turi užbaigti užduotis vienu metu.
- **Grupinio pokalbio orkestracija** scenarijuose, kai agentai gali bendradarbiauti spręsdami vieną užduotį.
- **Perdavimų orkestracija** scenarijuose, kai agentai perduoda užduotį vieni kitiems užduočių metu.
- **Magnetinė orkestracija** scenarijuose, kai valdymo agentas kuria ir keičia užduočių sąrašą bei koordinuoja pogrupius užduočiai užbaigti.

Kad būtų galima tiekti DI agentus gamyboje, MAF taip pat įtraukia funkcijas tokias kaip:

- **Stebimumas** naudojant OpenTelemetry, kur fiksuojamas kiekvienas DI agente atliekamas veiksmas įskaitant įrankių kvietimus, orkestracijos žingsnius, sprendimų srautus ir našumo stebėjimą Microsoft Foundry skydeliuose.
- **Saugumas** talpinant agentus natively Microsoft Foundry, kuri apima saugumo valdymą kaip vaidmenimis pagrįstą prieigą, privačių duomenų tvarkymą ir integruotą turinio saugumą.
- **Atsparumas** nes agentų gijos ir darbo eiga gali būti pristabdytos, tęsiamos ir atstatomos iš klaidų, leidžiant ilgesnį procesų vykdymą.
- **Valdymas** nes palaikomi žmogaus stebimi darbo eigų procesai, kur užduotys žymimos kaip reikalaujančios žmogaus patvirtinimo.

Microsoft Agent Framework taip pat orientuotas į interoperabilumą:

- **Debesims nepriklausoma** – agentai gali veikti konteineriuose, vietoje ir per skirtingas debesų platformas.
- **Tiekėjams nepriklausoma** – agentai gali būti kuriami naudojant jus dominančius SDK, įskaitant Azure OpenAI ir OpenAI.
- **Atvirų standartų integracija** – agentai gali naudoti protokolus, kaip Agent-to-Agent(A2A) ir Model Context Protocol (MCP), kad atrastų ir naudotų kitus agentus bei įrankius.
- **Papildiniai ir jungtys** – galima prisijungti prie duomenų ir atminties paslaugų, tokių kaip Microsoft Fabric, SharePoint, Pinecone ir Qdrant.

Pažiūrėkime, kaip šios funkcijos taikomos kai kurioms pagrindinėms Microsoft Agent Framework sąvokoms.

## Microsoft Agent Framework pagrindinės sąvokos

### Agentai

![Agent Framework](../../../translated_images/lt/agent-components.410a06daf87b4fef.webp)

**Agentų kūrimas**

Agentų kūrimas atliekamas apibrėžiant spėjimo paslaugą (LLM tiekėją), 
instrukcijų rinkinį, kurį DI agentas turi vykdyti, ir priskirtą `pavadinimą`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Aukščiau naudojamas `Azure OpenAI`, tačiau agentus galima kurti naudojant įvairias paslaugas, įskaitant `Microsoft Foundry Agent Service`:

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

arba nuotolinius agentus naudojant A2A protokolą:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Agentų paleidimas**

Agentai paleidžiami naudojant `.run` arba `.run_stream` metodus, priklausomai nuo to, ar reikia nepertraukiamos ar srautinės atsakymų transliacijos.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Kiekvienam agentei paleidimui gali būti pateikiamos parinktys parametrų tinkinimui, pvz., `max_tokens`, kuriuos naudoja agentas, `tools`, kuriuos agentas gali kviesti, ar net pats `modelis`, naudojamas agentui.

Tai naudinga situacijose, kai konkrečios modeliai ar įrankiai yra būtini vartotojo užduočiai atlikti.

**Įrankiai**

Įrankiai gali būti apibrėžti tiek kuriant agentą:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Kai kuriate ChatAgent tiesiogiai

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

tiek paleidžiant agentą:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Įrankis suteikiamas tik šiam paleidimui )
```

**Agentų gijos**

Agentų gijos naudojamos valdyti daugkartinius pokalbius. Gijos gali būti sukuriamos:

- naudojant `get_new_thread()`, kuri leidžia giją išsaugoti laikui bėgant
- automatiškai sukuriant giją paleidžiant agentą, kuri egzistuos tik šio paleidimo metu.

Gijos kūrimo kodas atrodo taip:

```python
# Sukurkite naują giją.
thread = agent.get_new_thread() # Vykdykite agentą su gija.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Tada giją galima serializuoti ir saugoti vėlesniam naudojimui:

```python
# Sukurkite naują srautą.
thread = agent.get_new_thread() 

# Paleiskite agentą su srautu.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serializuokite srautą saugojimui.

serialized_thread = await thread.serialize() 

# Deserializuokite srauto būseną po įkėlimo iš saugyklos.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agentų tarpinis programavimas**

Agentai sąveikauja su įrankiais ir LLM, kad užbaigtų vartotojų užduotis. Tam tikromis situacijomis norime vykdyti arba stebėti veiksmus tarp šių sąveikų. Agentų tarpinis programavimas leidžia tai atlikti per:

*Funkcinį tarpinį programavimą*

Šis tarpinis programavimas leidžia vykdyti veiksmą tarp agente ir funkcijos/įrankio, kurį jis kvies. Pavyzdys, kada tai naudinga – kai norite užfiksuoti funkcijos kvietimą.

Toliau pateiktame kode `next` nurodo, ar turi būti kviečiamas kitas tarpinis sluoksnis, ar pati funkcija.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Išankstinis apdorojimas: registruoti prieš funkcijos vykdymą
    print(f"[Function] Calling {context.function.name}")

    # Tęsti į kitą vidurinio sluoksnio komponentą arba funkcijos vykdymą
    await next(context)

    # Po apdorojimo: registruoti po funkcijos vykdymo
    print(f"[Function] {context.function.name} completed")
```

*Pokalybinis tarpinis programavimas*

Šis tarpinis programavimas leidžia vykdyti ar registruoti veiksmą tarp agente ir užklausų LLM.

Jame svarbi informacija, tokia kaip `messages`, siunčiami į DI paslaugą.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Išankstinis apdorojimas: žurnalas prieš AI kvietimą
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Tęsti prie kito tarpinio serverio arba AI paslaugos
    await next(context)

    # Vėlesnis apdorojimas: žurnalas po AI atsakymo
    print("[Chat] AI response received")

```

**Agentų atmintis**

Kaip aptarta pamokoje `Agentic Memory`, atmintis yra svarbus elementas leidžiantis agentui veikti per skirtingas kontekstus. MAF siūlo keletą skirtingų atminties tipų:

*Atmintinė operacijų metu*

Tai atmintis saugoma gijų metu programos vykdymo laiku.

```python
# Sukurti naują giją.
thread = agent.get_new_thread() # Vykdyti agentą su gija.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Nuolatiniai pranešimai*

Ši atmintis naudojama pokalbių istorijai saugoti per skirtingas sesijas. Ji apibrėžiama naudojant `chat_message_store_factory`:

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

Ši atmintis pridedama į kontekstą prieš paleidžiant agentus. Šia atmintį galima saugoti išorinėse paslaugose, tokiose kaip mem0:

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

**Agentų stebimumas**

Stebimumas yra svarbus patikimų ir prižiūrimų agentinių sistemų kūrimui. MAF integruoja OpenTelemetry, kad suteiktų atsekimą ir matuoklius geresniam stebimumui.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # padaryti kažką
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Darbų eigos

MAF siūlo darbų eigas, tai iš anksto apibrėžti žingsniai užduočiai užbaigti, įtraukiantys DI agentus kaip komponentus šiuose žingsniuose.

Darbų eigas sudaro skirtingi komponentai, leidžiantys geriau valdyti srautą. Darbų eigos taip pat leidžia **daugiagentų orkestraciją** ir **atkarpų įrašymą**, siekiant išsaugoti darbo darbo eigos būsenas.

Pagrindiniai darbo eigos komponentai yra:

**Vykdytojai**

Vykdytojai gauna įvesties žinutes, atlieka priskirtus darbus ir tuomet generuoja išvesties žinutes. Tai leidžia darbų eigai judėti link pagrindinės užduoties įvykdymo. Vykdytojai gali būti tiek DI agentai, tiek vartotojų logika.

**Kraštai**

Kraštai naudojami apibrėžti žinučių srautą darbo eigoje. Jie gali būti:

*Tiesioginiai kraštai* – paprasti vienas prie vieno ryšiai tarp vykdytojų:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Sąlyginiai kraštai* – aktyvuojami, kai įvykdoma tam tikra sąlyga. Pavyzdžiui, kai viešbučių kambarių nėra, vykdytojas gali pasiūlyti kitus variantus.

*Perjungimo atvejo kraštai* – nukreipia žinutes skirtingiems vykdytojams pagal nustatytas sąlygas. Pavyzdžiui, jei kelionės klientas turi pirmenybinę prieigą, jo užduotys bus vykdomos kitoje darbo eigoje.

*Išsišakojimo kraštai* – vieną žinutę siunčia keliems tikslams.

*Susijungimo kraštai* – surenka kelias žinutes iš skirtingų vykdytojų ir siunčia vienam tikslui.

**Įvykiai**

Siekiant geresnio stebimumo darbų eigose, MAF siūlo integruotus vykdymo įvykius, įskaitant:

- `WorkflowStartedEvent`  - prasideda darbo eigos vykdymas
- `WorkflowOutputEvent` - darbo eiga generuoja išvestį
- `WorkflowErrorEvent` - darbo eiga susiduria su klaida
- `ExecutorInvokeEvent`  - vykdytojas pradeda apdorojimą
- `ExecutorCompleteEvent`  -  vykdytojas baigia apdorojimą
- `RequestInfoEvent` - vykdoma užklausa

## Pažangūs MAF modeliai

Aukščiau aprašytos pagrindinės Microsoft Agent Framework sąvokos. Kuriant sudėtingesnius agentus, čia pateikiami kai kurie pažangūs modeliai, kuriuos verta apsvarstyti:

- **Tarpinių sluoksnių sudėtis**: susieti kelis tarpinio programavimo tvarkyklius (registravimą, autentifikavimą, greičio ribojimą) naudojant funkcijų ir pokalbių tarpinį programavimą, kad būtų galima tiksliau valdyti agentų elgseną.
- **Darbų eigų atkūrimas**: naudoti darbo eigos įvykius ir serializaciją ilgai trunkančioms agentų užduotims saugoti ir tęsti.
- **Dinaminis įrankių atrinkimas**: derinti RAG pagal įrankių aprašymus su MAF įrankių registracija, kad būtų pateikti tik aktualūs įrankiai kiekvienam užklausai.
- **Daugiagentų perdavimas**: naudoti darbo eigos kraštus ir sąlyginį maršrutavimą specializuotų agentų perdavimų orkestracijai.

## Kodo pavyzdžiai

Microsoft Agent Framework kodo pavyzdžius rasite šiame saugykloje `xx-python-agent-framework` ir `xx-dotnet-agent-framework` failuose.

## Ar turite daugiau klausimų apie Microsoft Agent Framework?

Prisijunkite prie [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kad susitiktumėte su kitais besimokančiais, dalyvautumėte valandose ir gautumėte atsakymus į savo DI agentų klausimus.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neatsakome už bet kokius nesusipratimus ar neteisingus interpretavimus, kilusius naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->