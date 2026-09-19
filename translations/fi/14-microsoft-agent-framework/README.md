# Microsoft Agent Frameworkin tutkiminen

![Agent Framework](../../../translated_images/fi/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Johdanto

Tässä oppitunnissa käsitellään:

- Microsoft Agent Frameworkin ymmärtäminen: Keskeiset ominaisuudet ja arvo  
- Microsoft Agent Frameworkin keskeisten käsitteiden tutkiminen
- Kehittyneet MAF-mallit: työnkulut, middleware ja muisti

## Oppimistavoitteet

Oppitunnin suorittamisen jälkeen osaat:

- Rakentaa tuotantovalmiita tekoälyagentteja Microsoft Agent Frameworkilla
- Soveltaa Microsoft Agent Frameworkin ydintoimintoja omiin agenttipohjaisiin käyttötapauksiin
- Käyttää kehittyneitä malleja, kuten työnkulkuja, middlewarea ja havaittavuutta

## Koodiesimerkit 

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) -koodiesimerkkejä löytyy tästä arkistosta tiedostojen `xx-python-agent-framework` ja `xx-dotnet-agent-framework` alta.

## Microsoft Agent Frameworkin ymmärtäminen

![Framework Intro](../../../translated_images/fi/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) on Microsoftin yhtenäinen kehys tekoälyagenttien rakentamiseen. Se tarjoaa joustavuutta käsitellä laajaa kirjoa agenteille tyypillisiä käyttötapauksia niin tuotanto- kuin tutkimusympäristöissä, mukaan lukien:

- **Sarjallinen agenttien orkestrointi** tilanteissa, joissa tarvitaan vaiheittaisia työnkulkuja.
- **Samaan aikaan tapahtuva orkestrointi** tilanteissa, joissa agenttien on suoritettava tehtäviä samanaikaisesti.
- **Ryhmäkeskustelun orkestrointi** tilanteissa, joissa agentit voivat tehdä yhteistyötä yhdessä tehtävässä.
- **Tehtävien siirto** tilanteissa, joissa agentit luovuttavat tehtävän toisilleen, kun osatehtävät valmistuvat.
- **Magnettinen orkestrointi** tilanteissa, joissa hallinta-agentti luo ja muokkaa tehtävälistaa ja hoitaa ala-agenttien koordinoinnin tehtävän suorittamiseksi.

Tuotannossa toteutettavien tekoälyagenttien ansioksi MAF sisältää myös ominaisuuksia kuten:

- **Havaittavuus** OpenTelemetryn avulla, jossa jokainen tekoälyagentin toiminto, kuten työkalujen kutsut, orkestrointivaiheet, päättelyvirrat ja suorituskyvyn seuranta Microsoft Foundryn kojelaudoilla, on näkyvissä.
- **Turvallisuus** ajamalla agentit natiivisti Microsoft Foundryssa, johon kuuluu turvallisuusohjaukset, kuten roolipohjainen pääsy, yksityisten tietojen käsittely ja sisäänrakennettu sisällön turvallisuus.
- **Kestävyys**, koska agenttilangat ja työnkulut voivat keskeyttää, jatkaa ja palautua virheistä, mikä mahdollistaa pidempikestoiset prosessit.
- **Ohjaus**, koska ihmisen osallistumista työnkulkuun tuetaan, jolloin tehtävät merkitään ihmisen hyväksyntää vaativiksi.

Microsoft Agent Framework keskittyy myös yhteentoimivuuteen esimerkiksi:

- **Pilvipalveluista riippumattomuus** - Agentit voivat toimia säilöissä, paikallisissa ympäristöissä ja eri pilvipalveluissa.
- **Toimittajariippumattomuus** - Agentit voidaan luoda haluamallasi SDK:lla, mukaan lukien Azure OpenAI ja OpenAI.
- **Avoimien standardien integrointi** - Agentit voivat käyttää protokollia kuten Agent-to-Agent (A2A) ja Model Context Protocol (MCP) löytääkseen ja käyttäen muita agentteja ja työkaluja.
- **Laajennukset ja liittimet** - Yhteydet voivat olla tiedon ja muistin palveluihin, kuten Microsoft Fabric, SharePoint, Pinecone ja Qdrant.

Tarkastellaanpa, miten näitä ominaisuuksia sovelletaan Microsoft Agent Frameworkin keskeisiin käsitteisiin.

## Microsoft Agent Frameworkin keskeiset käsitteet

### Agentit

![Agent Framework](../../../translated_images/fi/agent-components.410a06daf87b4fef.webp)

**Agenttien luominen**

Agentin luominen tehdään määrittelemällä päättelypalvelu (LLM-toimittaja), joukko ohjeita tekoälyagentille noudatettavaksi ja nimetty `name`:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Yllä käytetään `Azure OpenAI`-palvelua, mutta agentteja voi luoda monilla eri palveluilla, mukaan lukien `Microsoft Foundry Agent Service`:

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

tai [MiniMax](https://platform.minimaxi.com/), joka tarjoaa OpenAI-yhteensopivan API:n suurilla konteksti-ikkunoilla (jopa 204 000 tokenia):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

tai etäagentit A2A-protokollaa käyttäen:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Agenttien suorittaminen**

Agentteja ajetaan `.run` tai `.run_stream` -menetelmillä, joko ei-suoratoistona tai suoratoistona vastauksia varten.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Jokaisessa agentin suorituksessa voi olla myös asetuksia parametrien, kuten agentin käyttämien `max_tokens`-, agentin kutsumien `tools`-työkalujen ja jopa käytetyn `model`-mallin mukauttamiseksi.

Tämä on hyödyllistä tapauksissa, joissa tehtävän suorittamiseen tarvitaan tiettyjä malleja tai työkaluja.

**Työkalut**

Työkaluja voidaan määritellä sekä agenttia luotaessa:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Kun luodaan ChatAgent suoraan

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

että agenttia ajettaessa:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Työkalu, joka on saatavilla vain tätä ajoa varten )
```

**Agenttilangat**

Agenttilankoja käytetään monisäikeisten keskustelujen käsittelemiseen. Langat voidaan luoda joko:

- Käyttämällä `get_new_thread()`, jolloin lanka voidaan tallentaa ajan myötä
- Luomalla lanka automaattisesti agenttia ajettaessa, jolloin lanka toimii vain kulloisenkin suorituksen ajan.

Langat luodaan seuraavasti:

```python
# Luo uusi säie.
thread = agent.get_new_thread() # Suorita agentti säikeen kanssa.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Langat voi sitten sarjoittaa tallennettavaksi myöhempää käyttöä varten:

```python
# Luo uusi säie.
thread = agent.get_new_thread() 

# Suorita agentti säikeellä.

response = await agent.run("Hello, how are you?", thread=thread) 

# Sarjoita säie tallennusta varten.

serialized_thread = await thread.serialize() 

# Purka säikeen tila lataamisen jälkeen tallennuksesta.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agentin middleware**

Agentit kommunikoivat työkalujen ja LLM:ien kanssa suorittaakseen käyttäjän tehtävät. Joissain tilanteissa haluamme suorittaa tai seurata tapahtumia näiden välissä. Agentin middleware mahdollistaa tämän esimerkiksi:

*Toimintomiddleware*

Tämä middleware mahdollistaa toiminnon suorittamisen agentin ja kutsuttavan funktion/työkalun välillä. Esimerkki käytöstä on lokituksen tekeminen funktiokutsun yhteydessä.

Alla olevassa koodissa `next` määrittelee, kutsutaanko seuraava middleware vai varsinainen funktio.

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

*Keskustelumiddleware*

Tämä middleware mahdollistaa toiminnon suorittamisen tai lokituksen agentin ja LLM:lle lähetettyjen pyyntöjen välillä.

Se sisältää tärkeitä tietoja, kuten AI-palvelulle lähetetyt `messages`.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Ennakkokäsittely: Kirjaa lokiin ennen tekoälykutsua
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Jatka seuraavaan väliohjelmistoon tai tekoälypalveluun
    await next(context)

    # Jälkikäsittely: Kirjaa lokiin tekoälyvastauksen jälkeen
    print("[Chat] AI response received")

```

**Agentin muisti**

Kuten `Agentic Memory` -oppitunnissa käsiteltiin, muisti on olennainen osa agentin toimintaa eri kontekstien välillä. MAF tarjoaa useita eri muistin tyyppejä:

*Muisti sovelluksen ajon aikana*

Tämä on muisti, joka tallennetaan langoissa sovelluksen ajon aikana.

```python
# Luo uusi säie.
thread = agent.get_new_thread() # Suorita agentti säikeen kanssa.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Pysyvät viestit*

Tätä muistia käytetään keskusteluhistorian tallentamiseen eri sessioiden välillä. Se määritellään `chat_message_store_factory`:lla:

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


Tämä muisti lisätään kontekstiin ennen agenttien suorittamista. Näitä muistoja voidaan tallentaa ulkoisiin palveluihin, kuten mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Mem0:n käyttäminen edistyneisiin muistitoimintoihin
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

**Agentin havaittavuus**

Havaittavuus on tärkeää luotettavien ja ylläpidettävien agenttipohjaisten järjestelmien rakentamisessa. MAF integroituu OpenTelemetryyn tarjotakseen jäljitystä ja mittareita paremman havaittavuuden saavuttamiseksi.

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

Työnkulut koostuvat eri komponenteista, jotka mahdollistavat paremman ohjausvirtauksen. Työnkulut mahdollistavat myös **moni-agenttien orkestroinnin** ja **tarkistuspisteiden käytön**, joiden avulla työnkulun tilat voidaan tallentaa.

Työnkulun peruskomponentit ovat:

**Suorittajat**

Suorittajat vastaanottavat syöteviestejä, suorittavat niille määritellyt tehtävät ja tuottavat sitten tulosviestin. Tämä vie työnkulkua eteenpäin kohti suuremman tehtävän valmistumista. Suorittajat voivat olla joko tekoälyagentteja tai mukautettua logiikkaa.

**Kärjet**

Kärkiä käytetään viestien virran määrittämiseen työnkulussa. Ne voivat olla:

*Suoria kärkiä* – Yksinkertaisia yhden ja yhden välistä yhteyksiä suorittajien välillä:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Ehtokärkiä* – Aktivoituvat, kun tietty ehto täyttyy. Esimerkiksi, kun hotellihuoneita ei ole saatavilla, suorittaja voi ehdottaa muita vaihtoehtoja.

*Kytkin-tilakärkiä* – Reitittää viestejä eri suorittajille määriteltyjen ehtojen perusteella. Esimerkiksi, jos matkustajalla on prioriteettikäyttöoikeus, hänen tehtävänsä käsitellään toisessa työnkulussa.

*Fan-out kärkiä* – Lähettää yhden viestin useille kohteille.

*Fan-in kärkiä* – Kerää useita viestejä eri suorittajilta ja lähettää ne yhdelle kohteelle.

**Tapahtumat**

Tarjotakseen paremman havaittavuuden työnkuluihin, MAF tarjoaa sisäänrakennettuja suoritus tapahtumia, mukaan lukien:

- `WorkflowStartedEvent`  - Työnkulun suoritus alkaa
- `WorkflowOutputEvent` - Työnkulku tuottaa tuloksen
- `WorkflowErrorEvent` - Työnkulku kohtaa virheen
- `ExecutorInvokeEvent`  - Suorittaja aloittaa käsittelyn
- `ExecutorCompleteEvent`  -  Suorittaja päättää käsittelyn
- `RequestInfoEvent` - Pyyntö tehdään

## Kehittyneet MAF-mallit

Edellä olevat osiot käsittelevät Microsoft Agent Frameworkin keskeisiä käsitteitä. Kun rakennat monimutkaisempia agentteja, tässä on joitakin kehittyneitä malleja harkittavaksi:

- **Väliohjelman koostaminen**: Ketjuta useita väliohjelmakäsittelijöitä (lokitus, tunnistus, nopeusrajoitus) käyttämällä funktio- ja chat-väliohjelmaa agentin toiminnan hienojakoiseen hallintaan.
- **Työnkulun tarkistuspisteet**: Käytä työnkulu tapahtumia ja sarjallistamista tallentaaksesi ja jatkaaksesi pitkään kestäviä agenttiprosesseja.
- **Dynaaminen työkalujen valinta**: Yhdistä RAG työkalukuvauksiin MAF:n työkalurekisteröinnin kanssa esitelläksesi vain asianmukaiset työkalut kuhunkin kyselyyn.
- **Moni-Agenttien siirto**: Käytä työnkulun kärkiä ja ehtoreititystä orkestroidaksesi siirrot erikoistuneiden agenttien välillä.

## LangChainin / LangGraph-agenttien isännöinti Microsoft Foundryssa

Microsoft Agent Framework on **kehys-yhteensopiva** — et ole rajoitettu käyttämään vain MAF:lla kirjoitettuja agentteja. Jos sinulla on jo agentti rakennettu **LangChainilla** tai **LangGraphilla**, voit käyttää sitä **Microsoft Foundryn isännöimänä agenttina**, jolloin Foundry hallinnoi ajonaikaa, istuntoja, skaalausta, identiteettiä ja protokollapisteitä puolestasi, kun taas agenttilogiikka pysyy LangGraphissa.

Tämä tehdään `langchain_azure_ai.agents.hosting` -paketilla, joka tarjoaa käännetyn LangGraph-kaavion samoilla protokollilla, joita Foundryn isännöimät agentit käyttävät.

**1. Asenna hosting-lisäosa:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting`-lisäosa asentaa Foundryn protokollakirjastot: `azure-ai-agentserver-responses` (OpenAI-yhteensopiva `/responses`-päätepiste) ja `azure-ai-agentserver-invocations` (geneerinen `/invocations`-päätepiste).

**2. Valitse hosting-protokolla:**

| Protokolla | Isäntäluokka | Päätepiste | Käytä, kun |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Haluat OpenAI-yhteensopivan chatin, suoratoiston, vastaushistorian ja keskusteluketjutuksen — suositeltu oletus keskusteluagentteja varten. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Tarvitset mukautetun JSON-muodon, webhook-tyyppisen päätepisteen tai ei-keskustelevaa käsittelyä. |

Koska **Responses API on ensisijainen API Foundryn agenttityyppiseen kehittämiseen**, aloita useimmille agenteille `ResponsesHostServer`-luokalla.

**3. Määritä ympäristömuuttujat** (`az login` ensin, jotta `DefaultAzureCredential` voi kirjautua sisään):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Kun agentti myöhemmin suoritetaan isännöitynä agenttina Foundryssa, alusta lisää `FOUNDRY_PROJECT_ENDPOINT` automaattisesti.

**4. Paljasta LangGraph-agentti Responses-protokollan kautta:**

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

    # ChatOpenAI tässä kohdistuu Foundryn projektin OpenAI-yhteensopivaan (Responses) päätepisteeseen.
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

Suorita paikallisesti komennolla `python main.py`, sitten lähetä Responses-pyyntö osoitteeseen `http://localhost:8088/responses`.

**Keskeiset käyttäytymistavat:**

- **Keskustelut**: Asiakkaat jatkavat keskustelua välittämällä `previous_response_id` tai `conversation`-tunnuksen. Jos kaaviosi on käännetty LangGraphin tarkistuspisteellä, Foundry yhdistää keskustelun tilan tarkistuspisteeseen (käytä tuotannossa kestävää tarkistuspistettä; `MemorySaver` sopii paikalliseen testaukseen).
- **Ihmisen osallistuminen**: Jos kaaviosi käyttää LangGraphin `interrupt()`-toimintoa, `ResponsesHostServer` näyttää odottavan keskeytyksen Responsesin `function_call` / `mcp_approval_request` -kohteena, ja asiakkaat jatkavat vastaavalla `function_call_output` / `mcp_approval_response` -vastauksella.
- **Julkaise Foundryyn**: Käytä Azure Developer CLI:tä — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (paikallinen, vaatii Dockerin), sitten `azd provision` ja `azd deploy`. Isännöidyn agentin käyttöönotto vaatii **Foundry Project Manager** -roolin.

Tämän esimerkin ajo kelpoinen versio löytyy tiedostosta [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Täydellisen läpikäynnin (Invocations-protokolla, mukautetut pyyntömalleja ja vianetsintä) löydät sivulta [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Koodiesimerkit

Microsoft Agent Frameworkin koodiesimerkkejä löytyy tästä arkistosta `xx-python-agent-framework`- ja `xx-dotnet-agent-framework`-tiedostoista.

## Lisää kysymyksiä Microsoft Agent Frameworkista?

Liity [Microsoft Foundryn Discordiin](https://discord.com/invite/ATgtXmAS5D) tavata muita oppijoita, osallistua toimistoaikoihin ja saada vastauksia AI Agents -kysymyksiisi.
## Edellinen oppitunti

[Muisti AI-agenteille](../13-agent-memory/README.md)

## Seuraava oppitunti


[Tietokoneen käyttösovellusten (CUA) rakentaminen](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->