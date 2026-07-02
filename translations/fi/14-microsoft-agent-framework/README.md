# Microsoft Agent Frameworkin Tutkiminen

![Agent Framework](../../../translated_images/fi/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Johdanto

Tässä oppitunnissa käsitellään:

- Microsoft Agent Frameworkin ymmärtäminen: Keskeiset ominaisuudet ja arvo  
- Microsoft Agent Frameworkin keskeisten käsitteiden tutkiminen
- Edistyneet MAF-mallit: Työnkulut, Middleware ja Muisti

## Oppimistavoitteet

Tämän oppitunnin suorittamisen jälkeen osaat:

- Rakentaa tuotantovalmiita tekoälyagentteja Microsoft Agent Frameworkilla
- Soveltaa Microsoft Agent Frameworkin ydintoimintoja agenttikäyttötapauksiisi
- Käyttää edistyneitä malleja, mukaan lukien työnkulut, middleware ja havainnollisuus

## Koodiesimerkit

Microsoft Agent Frameworkin (MAF) koodiesimerkit löytyvät tästä repositoriosta tiedostoista `xx-python-agent-framework` ja `xx-dotnet-agent-framework`.

## Microsoft Agent Frameworkin Ymmärtäminen

![Framework Intro](../../../translated_images/fi/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) on Microsoftin yhtenäinen kehys tekoälyagenttien rakentamiseen. Se tarjoaa joustavuutta vastata moninaisiin agenttikäyttötapauksiin, joita esiintyy sekä tuotanto- että tutkimusympäristöissä, mukaan lukien:

- **Peräkkäinen agenttien orkestrointi** tilanteissa, joissa tarvitaan vaiheittaista työnkulkua.
- **Samanaikainen orkestrointi** tilanteissa, joissa agenttien pitää suorittaa tehtäviä samanaikaisesti.
- **Ryhmächatti-orkestrointi** tilanteissa, joissa agentit voivat työskennellä yhdessä saman tehtävän parissa.
- **Luovutus-orkestrointi** tilanteissa, joissa agentit siirtävät tehtävän toisilleen, kun alitehtävät valmistuvat.
- **Magnetinen orkestrointi** tilanteissa, joissa johtava agentti luo ja muokkaa tehtävälistaa sekä koordinoi ala-agenttien toimintaa tehtävän suorittamiseksi.

Tuotantovalmiiden tekoälyagenttien toimittamiseksi MAF sisältää myös ominaisuuksia:

- **Havainnollisuus** OpenTelemetryn avulla, jossa AI-agentin kaikki toiminnot, kuten työkalujen kutsuminen, orkestroinnin vaiheet, päättelyvirrat ja suorituskyvyn seuranta Microsoft Foundry -kojelautojen kautta, ovat nähtävissä.
- **Turvallisuus** isännöimällä agentteja natiivisti Microsoft Foundryssa, joka sisältää turvallisuusohjaukset kuten roolipohjaisen pääsynvalvonnan, yksityisen datan käsittelyn ja sisäänrakennetun sisällönturvan.
- **Kestävyys** sillä agenttien ketjut ja työnkulut voivat keskeytyä, jatkua ja toipua virheistä, mikä mahdollistaa pidempikestoiset prosessit.
- **Hallinta** ihmisen mukanaololla varsinkin työnkuluissa, joissa tehtävät merkitään vaativiksi ihmisen hyväksyntää.

Microsoft Agent Framework on myös suunniteltu yhteensopivaksi:

- **Pilviriippumattomaksi** - Agentit voivat toimia konteissa, paikallisissa ympäristöissä tai useissa eri pilvissä.
- **Tarjoajariippumattomaksi** - Agentteja voidaan luoda valitsemallasi SDK:lla, kuten Azure OpenAI:lla ja OpenAI:lla.
- **Avoimien standardien integroinnilla** - Agentit voivat hyödyntää protokollia kuten Agent-to-Agent (A2A) ja Model Context Protocol (MCP) löytääkseen ja käyttäen muita agentteja ja työkaluja.
- **Laajennuksilla ja liittimillä** - Yhteydet voidaan muodostaa tietopalveluihin ja muisteihin kuten Microsoft Fabric, SharePoint, Pinecone ja Qdrant.

Katsotaanpa, miten nämä ominaisuudet liitetään Microsoft Agent Frameworkin keskeisiin käsitteisiin.

## Microsoft Agent Frameworkin Keskeiset Käsitteet

### Agentit

![Agent Framework](../../../translated_images/fi/agent-components.410a06daf87b4fef.webp)

**Agenttien Luominen**

Agentin luominen tehdään määrittelemällä päättelypalvelu (LLM Provider), joukko ohjeita, joita tekoälyagentin tulee noudattaa, sekä annetulla `name`-nimellä:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Yllä on käytetty `Azure OpenAI`-palvelua, mutta agentteja voi luoda monilla eri palveluilla, mukaan lukien `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI:n `Responses`, `ChatCompletion` -rajapinnat

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

tai [MiniMax](https://platform.minimaxi.com/), joka tarjoaa OpenAI-yhteensopivan API:n suurilla konteksti-ikkunoilla (enintään 204K tokenia):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

tai etäagentit käyttämällä A2A-protokollaa:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Agenttien Suorittaminen**

Agentteja suoritetaan käyttämällä `.run` tai `.run_stream` -menetelmiä, joko ei-suoratoistettuihin tai suoratoistettuihin vastauksiin.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Jokaiselle agentin ajoille voidaan myös määrittää optioita, joilla mukautetaan parametreja kuten agentin käyttämää `max_tokens`-määrää, `tools`-työkaluja, joita agentti voi kutsua, ja jopa agentissa käytettävää `model`-mallia.

Tämä on hyödyllistä tapauksissa, joissa tehtävän suorittamiseen vaaditaan erityisiä malleja tai työkaluja.

**Työkalut**

Työkaluja voi määritellä sekä agenttia luotaessa:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Kun luodaan ChatAgent suoraan

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

että agenttia ajettaessa:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Työkalu tarjottu vain tätä suorituskerrosta varten )
```

**Agenttiketjut**

Agenttiketjuja käytetään käsittelemään monikeskusteluja. Ketjut voidaan luoda joko:

- Käyttämällä `get_new_thread()` -metodia, jonka avulla ketju voidaan tallentaa myöhempää käyttöä varten
- Luomalla ketju automaattisesti agenttia ajettaessa ja pitämällä ketju voimassa vain sen nykyisen ajon aikana.

Ketjun luominen näyttää koodissa tältä:

```python
# Luo uusi säie.
thread = agent.get_new_thread() # Suorita agentti säikeellä.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Voit sitten sarjoittaa ketjun tallennettavaksi myöhempää käyttöä varten:

```python
# Luo uusi säie.
thread = agent.get_new_thread() 

# Suorita agentti säikeen kanssa.

response = await agent.run("Hello, how are you?", thread=thread) 

# Sarjoita säie tallennusta varten.

serialized_thread = await thread.serialize() 

# Desarjoita säikeen tila latauksen jälkeen.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agentin Middleware**

Agentit ovat vuorovaikutuksessa työkalujen ja LLM:ien kanssa suorittaakseen käyttäjän tehtäviä. Tietyissä tilanteissa haluamme suorittaa tai seurata tapahtumia näiden vuorovaikutusten välillä. Agentin middleware mahdollistaa tämän seuraavasti:

*Funktioväliohjelmisto*

Tämä middleware sallii toiminnon suorittamisen agentin ja sen kutsuman funktion/työkalun välillä. Esimerkkinä on kirjaus funktion kutsusta.

Alla olevassa koodissa `next` määrittää, kutsutaanko seuraavaa middlewareä vai varsinaista funktiota.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Esikäsittely: Kirjaa lokiin ennen funktion suorittamista
    print(f"[Function] Calling {context.function.name}")

    # Jatka seuraavaan middlewareen tai funktion suorittamiseen
    await next(context)

    # Jälkikäsittely: Kirjaa lokiin funktion suorittamisen jälkeen
    print(f"[Function] {context.function.name} completed")
```

*Chat middleware*

Tämä middleware mahdollistaa toiminnon suorittamisen tai kirjaamisen agentin ja LLM:ään kohdistuvien pyyntöjen välillä.

Tähän sisältyy tärkeää tietoa, kuten AI-palveluun lähetettäviä `messages`-viestejä.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Esiprosessointi: Kirjaa lokiin ennen tekoälykutsua
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Jatka seuraavaan middlewareen tai tekoälypalveluun
    await next(context)

    # Jälkikäsittely: Kirjaa lokiin tekoälyvastauksen jälkeen
    print("[Chat] AI response received")

```

**Agentin Muisti**

Kuten oppitunnissa `Agentic Memory` käsiteltiin, muisti on tärkeä osa agentin toimintaa eri konteksteissä. MAF tarjoaa useita erilaisia muistityyppejä:

*Muisti sovellusmuistissa*

Tämä muisti säilyy ketjuissa sovellusajon aikana.

```python
# Luo uusi säie.
thread = agent.get_new_thread() # Suorita agentti säikeen kanssa.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Pysyvät Viestit*

Tätä muistia käytetään keskusteluhistorian tallentamiseen eri istuntojen välillä. Se määritellään käyttämällä `chat_message_store_factory` -parametria:

```python
from agent_framework import ChatMessageStore

# Luo mukautettu viestivarasto
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynaaminen Muisti*

Tämä muisti lisätään kontekstiin ennen agenttien ajoa. Näitä muisteja voidaan tallentaa ulkopuolisiin palveluihin kuten mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Käytetään Mem0:aa edistyneisiin muistitoimintoihin
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

**Agentin Havainnollisuus**

Havainnollisuus on tärkeää luotettavien ja ylläpidettävien agenttipohjaisten järjestelmien rakentamisessa. MAF integroituu OpenTelemetryyn tarjoten jäljityksen ja mittarit parempaa havainnollisuutta varten.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # tee jotain
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Työnkulut

MAF tarjoaa työnkulkuja, jotka ovat ennalta määriteltyjä vaiheita tehtävän suorittamiseksi ja sisältävät tekoälyagentteja osina näitä vaiheita.

Työnkulut koostuvat eri komponenteista, jotka mahdollistavat paremman ohjausvirran. Työnkulut tukevat myös **moni-agenttien orkestrointia** ja **tallennuspisteitä (checkpointing)** työnkulun tilojen tallentamiseksi.

Työnkulun ydinkomponentit ovat:

**Suorittajat**

Suorittajat vastaanottavat syötteitä, suorittavat annetut tehtävät ja tuottavat ulostulevan viestin. Tämä vie työnkulkua eteenpäin kohti suuremman tehtävän suorittamista. Suorittajat voivat olla tekoälyagentteja tai räätälöityä logiikkaa.

**Reunat**

Reunoilla määritellään työnkulun viestien virtaus. Ne voivat olla:

*Suorat reunat* - Yksinkertaisia yhdestä toiseen -yhdistyksiä suorittajien välillä:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Ehdolliset reunat* - Aktivoituvat, kun tietty ehto täyttyy. Esimerkiksi kun hotellihuoneita ei ole saatavilla, suorittaja voi ehdottaa muita vaihtoehtoja.

*Switch-case-reunat* - Reitittävät viestejä eri suorittajille määriteltyjen ehtojen perusteella. Esimerkiksi jos matkustajalla on prioriteettiasema, heidän tehtävänsä käsitellään toisessa työnkulussa.

*Fan-out-reunat* - Lähettävät yhden viestin useisiin kohteisiin.

*Fan-in-reunat* - Keräävät useita viestejä eri suorittajilta ja lähettävät yhdelle kohteelle.

**Tapahtumat**

Tarjotakseen parempaa havainnollisuutta työnkulkuihin MAF tarjoaa sisäänrakennettuja tapahtumia suoritukseen, kuten:

- `WorkflowStartedEvent` - Työnkulun suoritus alkaa
- `WorkflowOutputEvent` - Työnkulku tuottaa ulostulon
- `WorkflowErrorEvent` - Työnkulku kohtaa virheen
- `ExecutorInvokeEvent` - Suorittaja aloittaa käsittelyn
- `ExecutorCompleteEvent` - Suorittaja päättää käsittelyn
- `RequestInfoEvent` - Pyyntö lähetetään

## Edistyneet MAF-Mallit

Yllä olevissa osioissa käsiteltiin Microsoft Agent Frameworkin keskeiset käsitteet. Kun rakennat monimutkaisempia agentteja, kannattaa harkita seuraavia edistyneitä malleja:

- **Middleware-kompositio**: Useiden middleware-käsittelijöiden (kirjaus, todennus, nopeuden rajoitus) ketjuttaminen funktio- ja chat-middlewarellä hienojakoiseen agenteille annettavaan ohjaukseen.
- **Työnkulun tallennuspisteet (Checkpointing)**: Lisää työnkulun tapahtumia ja sarjoitusta tallentaaksesi ja jatkaaksesi pitkään käynnissä olevia agenttiprosesseja.
- **Dynaaminen työkalujen valinta**: Yhdistä RAG työkalukuvauksista MAF:n työkalurekisteröitymiseen esittääksesi vain kyseiseen kyselyyn relevantit työkalut.
- **Moni-agenttinen luovutus**: Käytä työnkulun reunoja ja ehdollista reititystä koordinoidaksesi tehtävien siirtoja erikoistuneiden agenttien välillä.

## Koodiesimerkit

Microsoft Agent Frameworkin koodiesimerkit löytyvät tästä repositoriosta tiedostoista `xx-python-agent-framework` ja `xx-dotnet-agent-framework`.

## Lisäkysymyksiä Microsoft Agent Frameworkista?

Liity [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) -kanavalle tapaamaan muita oppijoita, osallistumaan aukioloaikoihin ja saamaan vastauksia tekoälyagentteja koskeviin kysymyksiisi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->