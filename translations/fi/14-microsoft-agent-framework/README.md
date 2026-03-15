# Microsoft Agent Frameworkin tutkiminen

![Agent Framework](../../../translated_images/fi/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Johdanto

Tässä oppitunnissa käsitellään:

- Microsoft Agent Frameworkin ymmärtäminen: Keskeiset ominaisuudet ja arvo  
- Microsoft Agent Frameworkin keskeisten käsitteiden tarkastelu
- Edistyneet MAF-mallit: työnkulut, middleware ja muisti

## Oppimistavoitteet

Oppitunnin suorittamisen jälkeen osaat:

- Rakentaa tuotantovalmiita tekoälyagentteja Microsoft Agent Frameworkin avulla
- Soveltaa Microsoft Agent Frameworkin ydintoimintoja agenttikäyttötapauksiisi
- Käyttää edistyneitä malleja, kuten työnkulkuja, middlewarea ja havainnointia

## Koodiesimerkit

[Microsoft Agent Frameworkin (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) koodiesimerkit löytyvät tästä arkistosta tiedostoista `xx-python-agent-framework` ja `xx-dotnet-agent-framework`.

## Microsoft Agent Frameworkin ymmärtäminen

![Framework Intro](../../../translated_images/fi/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) on Microsoftin yhtenäinen kehys tekoälyagenttien rakentamiseen. Se tarjoaa joustavuutta käsitellä monenlaisia agenttikäyttötapauksia sekä tuotanto- että tutkimusympäristöissä, mukaan lukien:

- **Peräkkäinen agenttien orkestrointi**, kun tarvitaan vaiheittaisia työnkulkuja.
- **Samanaikainen orkestrointi**, kun agenttien täytyy suorittaa tehtäviä samaan aikaan.
- **Ryhmäkeskustelun orkestrointi**, kun agentit voivat tehdä yhteistyötä yhden tehtävän parissa.
- **Tehtävän siirtojen orkestrointi**, kun agentit siirtävät tehtävän toisilleen, kun alitehtävät valmistuvat.
- **Magnetinen orkestrointi**, jossa johtava agentti luo ja muokkaa tehtävälistaa ja koordinoi avustavia agentteja tehtävän suorittamiseksi.

Tuotantovalmiiden tekoälyagenttien toimittamiseksi MAF sisältää myös ominaisuuksia kuten:

- **Havainnointi** OpenTelemetryn avulla, jossa jokainen tekoälyagentin toimenpide kuten työkalukutsu, orkestrointivaiheet, päättelyvirrat ja suorituskyvyn seuranta Microsoft Foundry -hallintapaneeleissa on seurattavissa.
- **Turvallisuus**: agentit isännöidään natiivisti Microsoft Foundryssa, joka sisältää turvallisuuskontrolleja kuten roolipohjaisen pääsynhallinnan, yksityisen datan käsittelyn ja sisäänrakennetun sisällön turvallisuuden.
- **Kestävyys**: agenttiketjut ja työnkulut voivat keskeytyä, jatkua ja toipua virheistä, mikä mahdollistaa pidemmät suoritukset.
- **Hallinta**: ihmisen osallistuminen työnkulkuun on tuettu, jolloin tehtävät voidaan merkitä ihmisen hyväksyntää vaativiksi.

Microsoft Agent Framework keskittyy myös yhteentoimivuuteen:

- **Pilvi-riippumattomuus** – agentit voivat toimia konttien sisällä, paikallisissa ympäristöissä ja useissa pilvissä.
- **Toimittajariippumattomuus** – agentit voidaan luoda suosimallasi SDK:lla, kuten Azure OpenAI:lla ja OpenAI:lla.
- **Avoimien standardien integrointi** – agentit voivat käyttää protokollia kuten Agent-to-Agent (A2A) ja Model Context Protocol (MCP) löytääkseen ja käyttääkseen muita agentteja ja työkaluja.
- **Plugin- ja liittimet** – yhteydet voidaan muodostaa datan ja muistin palveluihin kuten Microsoft Fabric, SharePoint, Pinecone ja Qdrant.

Katsotaan, miten näitä ominaisuuksia sovelletaan Microsoft Agent Frameworkin keskeisiin käsitteisiin.

## Microsoft Agent Frameworkin keskeiset käsitteet

### Agentit

![Agent Framework](../../../translated_images/fi/agent-components.410a06daf87b4fef.webp)

**Agenttien luominen**

Agentin luominen tapahtuu määrittelemällä päättelypalvelu (LLM-tarjoaja), joukko ohjeita, joita tekoälyagentin tulee noudattaa, ja nimi (`name`):

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```
  
Yllä käytetään `Azure OpenAI`:ta, mutta agentteja voidaan luoda monilla eri palveluilla, kuten `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```
  
OpenAI:n `Responses`, `ChatCompletion` API:t

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```
  
```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```
  
tai etäagentteja käyttäen A2A-protokollaa:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```
  
**Agenttien ajaminen**

Agenteja käytetään kutsumalla `.run`- tai `.run_stream`-metodeja, riippuen siitä, halutaanko ei-suoratoistavaa vai suoratoistavaa vastausta.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```
  
```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```
  
Jokaisella agenttikutsulla voi myös olla parametreja, kuten agentin käyttämä `max_tokens`, agentin käyttämät `tools` eli työkalut, tai jopa agentissa käytettävä `model`.

Tämä on hyödyllistä, kun tehtävään vaaditaan tiettyjä malleja tai työkaluja.

**Työkalut**

Työkaluja voidaan määritellä sekä agenttia luotaessa:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Kun luodaan ChatAgent suoraan

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```
  
että agenttia ajettaessa:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Työkalu, joka on tarjottu vain tätä ajoa varten )
```
  
**Agenttiketjut**

Agenttiketjuja käytetään monikierroksisten keskustelujen käsittelyyn. Ketju voidaan luoda:

- Käyttämällä `get_new_thread()`, jolloin ketju tallentuu ajan saatossa
- Luomalla ketju automaattisesti agentin suorittamisen aikana, jolloin ketju on voimassa vain kyseisen ajon ajan.

Ketjun luonti näyttää tältä:

```python
# Luo uusi säie.
thread = agent.get_new_thread() # Käynnistä agentti säikeen kanssa.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```
  
Ketjun voi sen jälkeen sarjoittaa tallennettavaksi myöhempää käyttöä varten:

```python
# Luo uusi säie.
thread = agent.get_new_thread() 

# Suorita agentti säikeellä.

response = await agent.run("Hello, how are you?", thread=thread) 

# Sarjoita säie tallennusta varten.

serialized_thread = await thread.serialize() 

# Desarjoita säikeen tila latauksen jälkeen.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```
  
**Agentin middleware**

Agentit tekevät vuorovaikutusta työkalujen ja LLM:ien kanssa käyttäjien tehtävien suorittamiseksi. Joissain tilanteissa haluamme suorittaa tai seurata näiden välistä toimintaa. Agentin middleware mahdollistaa tämän seuraavasti:

*Funktio-middleware*

Tämä middleware suorittaa toiminnon agentin ja kutsuttavan funktion/työkalun välillä. Esimerkkinä voisi olla lokitus funktion kutsusta.

Alla olevassa koodissa `next` määrittää, kutsutaanko seuraavaa middlewarea vai varsinaista funktiota.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Esikäsittely: Kirjaa lokiin ennen funktion suoritusta
    print(f"[Function] Calling {context.function.name}")

    # Jatka seuraavaan middlewareen tai funktion suoritukseen
    await next(context)

    # Jälkikäsittely: Kirjaa lokiin funktion suorituksen jälkeen
    print(f"[Function] {context.function.name} completed")
```
  
*Chatti-middleware*

Tämän middleware mahdollistaa toiminnon suorittamisen tai lokituksen agentin ja LLM:lle lähetettyjen pyyntöjen välillä.

Sisältää tärkeää tietoa, kuten AI-palvelulle lähetettävät `messages`.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Esikäsittely: Kirjaa lokiin ennen AI-kutsua
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Jatka seuraavaan middlewareen tai AI-palveluun
    await next(context)

    # Jälkikäsittely: Kirjaa lokiin AI-vastauksen jälkeen
    print("[Chat] AI response received")

```
  
**Agentin muisti**

Kuten `Agentic Memory` -oppitunnissa käsiteltiin, muisti on tärkeä osa agentin kykyä toimia eri konteksteissa. MAF tarjoaa useita muistityyppejä:

*Muisti sovelluksen ajon aikana*

Muisti, joka tallennetaan ketjuihin sovelluksen käynnin aikana.

```python
# Luo uusi säie.
thread = agent.get_new_thread() # Suorita agentti säikeellä.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```
  
*Pysyvät viestit*

Tätä muistia käytetään, kun halutaan tallentaa keskusteluhistoria eri istuntojen välillä. Määritellään käyttäen `chat_message_store_factory`:

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
  
*Dynaaminen muisti*

Tämä muisti lisätään kontekstiin ennen agenttien ajoa. Näitä muisteja voidaan tallentaa ulkoisiin palveluihin, kuten mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Käytetään Mem0:n kehittyneitä muistitoimintoja
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
  
**Agentin havainnointi**

Havainnointi on tärkeää luotettavien ja ylläpidettävien agenttijärjestelmien rakentamisessa. MAF integroituu OpenTelemetryyn tarjoamaan jäljitystä ja mittareita parempaa havainnointia varten.

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

Työnkulut koostuvat erilaisista komponenteista, jotka mahdollistavat paremman ohjauksen. Työnkulut mahdollistavat myös **moniagenttiorkestroinnin** ja **tarkistuspisteet**, joilla tallennetaan työnkulun tilat.

Työnkulun ydinkomponentit ovat:

**Suorittajat**

Suorittajat vastaanottavat syöteviestejä, suorittavat niille määritellyt tehtävät ja tuottavat tulosviestin. Tämä vie työnkulkua eteenpäin kohti suuremman tehtävän valmistumista. Suorittaja voi olla tekoälyagentti tai mukautettu logiikka.

**Kaarteet**

Kaarteilla määritellään viestien kulku työnkulussa. Ne voivat olla:

*Suorat kaarteet* – Yksinkertaiset yhdistykset suorittajien välillä yksi-yhteen:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```
  
*Ehdolliset kaarteet* – Aktivoituvat tietyn ehdon täyttyessä. Esimerkiksi, hotellihuoneiden ollessa loppu, suorittaja voi ehdottaa muita vaihtoehtoja.

*Valintaehdot (switch-case) -kaarteet* – Reitittävät viestit eri suorittajille määriteltyjen ehtojen perusteella. Esim. jos matkustajalla on prioriteettioikeus, hänen tehtävänsä käsitellään toisessa työnkulussa.

*Monikohdekarkaisu (fan-out) -kaarteet* – Lähettävät yhden viestin monille kohteille.

*Monilähtökarkaisu (fan-in) -kaarteet* – Keräävät useita viestejä eri suorittajilta ja lähettävät yhden viestin yhdelle kohteelle.

**Tapahtumat**

Työnkulkujen havainnollisuuden parantamiseksi MAF tarjoaa sisäänrakennettuja tapahtumia suoritusprosessiin, kuten:

- `WorkflowStartedEvent`  - Työnkulun suoritus alkaa
- `WorkflowOutputEvent` - Työnkulu tuottaa tuloksen
- `WorkflowErrorEvent` - Työnkulku kohtaa virheen
- `ExecutorInvokeEvent`  - Suorittaja aloittaa prosessoinnin
- `ExecutorCompleteEvent`  - Suorittaja lopettaa prosessoinnin
- `RequestInfoEvent` - Pyyntö lähetetään

## Edistyneet MAF-mallit

Yllä olevat osiot käsittelevät Microsoft Agent Frameworkin keskeisiä käsitteitä. Kun rakennat monimutkaisempia agenteja, tässä muutamia edistyneitä malleja harkittavaksi:

- **Middleware-yhdistelmät**: ketjuta useita middleware-käsittelijöitä (lokitus, autentikointi, nopeudenrajoitus) käyttämällä funktio- ja chatti-middlewarea tarkkaan kontrolliin agentin käytöksestä.
- **Työnkulun tarkistuspisteet**: käytä työnkulun tapahtumia ja sarjallistusta pitkien agenttiprosessien tallentamiseen ja jatkamiseen.
- **Dynaaminen työkalujen valinta**: yhdistä työkalumäärittelyjen RAG ja MAF:n työkalurekisteröinti esitelläksesi vain relevantit työkalut kuhunkin kyselyyn.
- **Moniagenttien tehtävien siirrot**: käytä työnkulun kaarteita ja ehdollista reititystä orkestroidaksesi tehtävien siirrot erikoistuneiden agenttien välillä.

## Koodiesimerkit

Microsoft Agent Frameworkin koodiesimerkit löytyvät tästä arkistosta tiedostoista `xx-python-agent-framework` ja `xx-dotnet-agent-framework`.

## Lisäkysymyksiä Microsoft Agent Frameworkista?

Liity [Microsoft Foundry Discordiin](https://aka.ms/ai-agents/discord) tapaamaan muita oppijoita, osallistumaan toimistoaikoihin ja saamaan vastauksia tekoälyagentteihin liittyviin kysymyksiisi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttäen tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaisen ihmiskääntäjän käyttöä. Emme ole vastuussa tästä käännöksestä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->