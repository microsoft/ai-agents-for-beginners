# Microsoft Agent Frameworkin tutkiminen

![Agent Framework](../../../translated_images/fi/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Johdanto

Tässä oppitunnissa käsitellään:

- Microsoft Agent Frameworkin ymmärtäminen: keskeiset ominaisuudet ja arvo  
- Microsoft Agent Frameworkin keskeisten käsitteiden tutkiminen
- Edistyneet MAF-mallit: työnkulut, middleware ja muisti

## Oppimistavoitteet

Oppitunnin suorittamisen jälkeen osaat:

- Rakentaa tuotantovalmiita tekoälyagentteja Microsoft Agent Frameworkin avulla
- Soveltaa Microsoft Agent Frameworkin ydintoimintoja agenttipohjaisissa käyttötapauksissa
- Käyttää edistyneitä malleja, mukaan lukien työnkulut, middleware ja havainnoitavuus

## Koodiesimerkit 

Koodiesimerkit [Microsoft Agent Frameworkille (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) löytyvät tästä arkistosta tiedostojen `xx-python-agent-framework` ja `xx-dotnet-agent-framework` alta.

## Microsoft Agent Frameworkin ymmärtäminen

![Framework Intro](../../../translated_images/fi/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) on Microsoftin yhtenäinen kehys tekoälyagenttien rakentamiseen. Se tarjoaa joustavuuden vastata laajaan valikoimaan agenttipohjaisia käyttötapauksia, joita esiintyy sekä tuotanto- että tutkimusympäristöissä, kuten:

- **Peräkkäinen agenttien orkestrointi** tilanteissa, joissa tarvitaan vaiheittaisia työnkulkuja.
- **Samaan aikaan tapahtuva orkestrointi** tilanteissa, joissa agenttien on suoritettava tehtäviä samanaikaisesti.
- **Ryhmäkeskustelun orkestrointi** tilanteissa, joissa agentit voivat työskennellä yhdessä yhden tehtävän parissa.
- **Tehtävien luovutus orkestrointi** tilanteissa, joissa agentit siirtävät tehtävän toisilleen ala­tehtävien valmistuessa.
- **Magnetismin orkestrointi** tilanteissa, joissa johtava agentti luo ja muokkaa tehtävälistaa ja hoitaa ala-agenttien koordinoinnin tehtävän suorittamiseksi.

Tuotannon tekoälyagenttien toimittamiseksi MAF sisältää myös ominaisuuksia:

- **Havainnoitavuus** OpenTelemetryn avulla, jossa seurataan jokaista tekoälyagentin toimintoa, mukaan lukien työkalun kutsut, orkestroinnin vaiheet, päättelyprosessit sekä suorituskyvyn seuranta Microsoft Foundry -kojelautojen kautta.
- **Turvallisuus** sijoittamalla agentit natiivisti Microsoft Foundryyn, mikä sisältää roolipohjaisen pääsynvalvonnan, yksityisen tiedon käsittelyn ja sisäänrakennetun sisällön turvallisuuden.
- **Kestävyys** sillä agenttien säikeet ja työnkulut voivat keskeytyä, jatkua ja palautua virheistä, mikä mahdollistaa pidempään käynnissä olevan prosessin.
- **Hallinta** sillä ihmisen osallistuminen työnkulkuun on tuettu siten, että tehtävät merkitään ihmisen hyväksyntää vaativiksi.

Microsoft Agent Framework keskittyy myös yhteensopivuuteen:

- **Pilviteknologiasta riippumattomuuteen** - agentit voivat toimia konteissa, paikallisissa ympäristöissä ja useissa eri pilvissä.
- **Palveluntarjoajasta riippumattomuuteen** - agentit voidaan luoda suosimallasi SDK:lla, mukaan lukien Azure OpenAI ja OpenAI.
- **Avoimien standardien integrointiin** - agentit voivat käyttää protokollia kuten Agent-to-Agent (A2A) ja Model Context Protocol (MCP) löytääkseen ja käyttäessään muita agentteja ja työkaluja.
- **Laajennukset ja liittimet** - yhteydet voidaan muodostaa datapalveluihin ja muisteihin, kuten Microsoft Fabric, SharePoint, Pinecone ja Qdrant.

Tarkastellaan, miten näitä ominaisuuksia sovelletaan Microsoft Agent Frameworkin keskeisiin käsitteisiin.

## Microsoft Agent Frameworkin keskeiset käsitteet

### Agentit

![Agent Framework](../../../translated_images/fi/agent-components.410a06daf87b4fef.webp)

**Agenttien luominen**

Agentin luominen tapahtuu määrittelemällä päättelypalvelu (LLM-palveluntarjoaja), joukko ohjeita, joita tekoälyagentin tulee noudattaa, ja määritelty `nimi`:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Edellä käytetään `Azure OpenAI`:ta, mutta agentteja voidaan luoda monella eri palvelulla, mukaan lukien `Microsoft Foundry Agent Service`:

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

tai [MiniMax](https://platform.minimaxi.com/), joka tarjoaa OpenAI-yhteensopivan API:n laajoilla kontekstin ikkunoilla (jopa 204 000 tokenia):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

tai etäagentteja käyttäen A2A-protokollaa:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Agenttien suorittaminen**

Agenttien suorittaminen tapahtuu `.run` tai `.run_stream` -metodeilla, riippuen siitä, halutaanko ei-suoratoimista vai suoratoistovastausta.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Jokaisella agentin suorituksella voi olla myös asetuksia, jotka mukauttavat parametreja kuten agentin käyttämää `max_tokens`, työkalujen `tools` kutsumismahdollisuudet ja jopa itse `mallia` agentin käytettäväksi.

Tämä on hyödyllistä tapauksissa, joissa tiettyjä malleja tai työkaluja vaaditaan käyttäjän tehtävän suorittamiseen.

**Työkalut**

Työkaluja voidaan määritellä sekä agentin määrittelyn yhteydessä:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Kun luodaan ChatAgent suoraan

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

että agenttia suoritettaessa:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Työkalu, joka on saatavilla vain tätä ajoa varten )
```

**Agenttisäikeet**

Agenttisäikeitä käytetään käsittelemään moni-vaiheisia keskusteluja. Säikeitä voidaan luoda joko:

- Käyttämällä `get_new_thread()`-metodia, jolloin säie tallennetaan ajan myötä
- Luomalla säie automaattisesti agentin suorittamisen yhteydessä, jolloin säie on voimassa vain kyseisen suorituksen ajan.

Säikeen luominen näyttää koodissa tältä:

```python
# Luo uusi säie.
thread = agent.get_new_thread() # Suorita agentti säikeen kanssa.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Säikeen voi serialisoida tallennettavaksi myöhempää käyttöä varten:

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

**Agentin middleware**

Agentit vuorovaikuttavat työkalujen ja LLM:ien kanssa suorittaakseen käyttäjän tehtäviä. Tietyissä tilanteissa haluamme suorittaa tai seurata toimintaa näiden vuorovaikutusten välillä. Agentin middleware mahdollistaa tämän:

*Funktio-middleware*

Tämä middleware mahdollistaa toiminnon suorittamisen agentin ja kutsuttavan funktion/työkalun välillä. Esimerkkinä käytöstä voisi olla lokituksen tekeminen funktiokutsuille.

Alla olevassa koodissa `next` määrittelee, kutsutaanko seuraavaa middlewarea vai varsinaista funktiota.

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

*Chat-middleware*

Tämä middleware mahdollistaa toiminnon suorittamisen tai lokituksen agentin ja LLM:n pyyntöjen välillä.

Tämä sisältää tärkeää tietoa kuten AI-palvelulle lähetettävät `messages`.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Esikäsittely: Kirjaa lokiin ennen tekoälykutsua
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Jatka seuraavaan välikerrokseen tai tekoälypalveluun
    await next(context)

    # Jälkikäsittely: Kirjaa lokiin tekoälyn vastauksen jälkeen
    print("[Chat] AI response received")

```

**Agentin muisti**

Kuten opetuksessa `Agentic Memory` käsiteltiin, muisti on tärkeä osa agentin toimintaa eri konteksteissa. MAF tarjoaa useita erilaisia muisteja:

*Muisti sovelluksen ajon aikana*

Tämä on säikeiden aikana sovelluksen suoritusaikana tallennettu muisti.

```python
# Luo uusi säie.
thread = agent.get_new_thread() # Suorita agentti säikeen kanssa.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Pysyvät viestit*

Tätä muistia käytetään keskusteluhistorian tallentamiseen eri istuntojen välillä. Se määritellään käyttäen `chat_message_store_factory` -kenttää:

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

Tämä muisti lisätään kontekstiin ennen agenttien suorittamista. Näitä muisteja voidaan tallentaa ulkoisissa palveluissa, kuten mem0:ssa:

```python
from agent_framework.mem0 import Mem0Provider

# Käytetään Mem0:a edistyneisiin muistiominaisuuksiin
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

**Agentin havainnoitavuus**


Havainnointikyky on tärkeää luotettavien ja ylläpidettävien agenttipohjaisten järjestelmien rakentamisessa. MAF integroituu OpenTelemetryn kanssa tarjotakseen jäljitystä ja mittareita paremman havainnointikyvyn saavuttamiseksi.

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

MAF tarjoaa työnkulkuja, jotka ovat ennalta määriteltyjä vaiheita tehtävän suorittamiseksi ja sisältävät tekoälyagentteja komponentteina näissä vaiheissa.

Työnkulut koostuvat erilaisista komponenteista, jotka mahdollistavat paremman ohjausvirran. Työnkulut mahdollistavat myös **moni-agenttien orkestroinnin** ja **tarkistuspisteiden** käytön työnkulun tilan tallentamiseksi.

Työnkulun ydinkomponentit ovat:

**Suorittajat**

Suorittajat vastaanottavat syötemessagesseja, suorittavat niille määritellyt tehtävät ja tuottavat sitten lähtöviestin. Tämä vie työnkulkua eteenpäin kohti koko suuremman tehtävän suorittamista. Suorittajat voivat olla joko tekoälyagentteja tai räätälöityä logiikkaa.

**Kaaret**

Kaaria käytetään määrittelemään viestien kulku työnkulkussa. Näitä voivat olla:

*Suorat kaaret* - Yksinkertaiset yksi-yhteen yhteydet suorittajien välillä:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Ehdolliset kaaret* - Aktivoituvat tietyn ehdon täyttyessä. Esimerkiksi, kun hotellihuoneita ei ole saatavilla, suorittaja voi ehdottaa muita vaihtoehtoja.

*Valintakaaret* - Ohjaa viestit eri suorittajille määriteltyjen ehtojen perusteella. Esimerkiksi, jos matkustajalla on etuoikeutettu pääsy, heidän tehtävänsä hoidetaan toisen työnkulun kautta.

*Monisulkeutumis-kaaret* - Lähetä yksi viesti useaan kohteeseen.

*Monikokoontumis-kaaret* - Kerää useita viestejä eri suorittajilta ja lähetä yhdelle kohteelle.

**Tapahtumat**

Tarjotakseen paremman havainnointikyvyn työnkulkuihin, MAF tarjoaa sisäänrakennettuja tapahtumia suorituksesta, mukaan lukien:

- `WorkflowStartedEvent`  - Työnkulun suoritus alkaa
- `WorkflowOutputEvent` - Työnkulkutuottaa tuloksen
- `WorkflowErrorEvent` - Työnkulku kohtaa virheen
- `ExecutorInvokeEvent`  - Suorittaja aloittaa prosessoinnin
- `ExecutorCompleteEvent`  -  Suorittaja saa prosessoinnin päätökseen
- `RequestInfoEvent` - Pyyntö annetaan

## Edistyneet MAF-mallit

Yllä olevat osiot käsittelevät Microsoft Agent Frameworkin keskeisiä käsitteitä. Kun rakennat monimutkaisempia agentteja, tässä on joitain kehittyneitä malleja harkittavaksi:

- **Middleware-kompositio**: Ketjuta useita middleware-käsittelijöitä (lokitus, autentikointi, nopeussäädin) käyttämällä funktio- ja keskusteluvälikerroksia tarkkaan hallintaan agentin käyttäytymisestä.
- **Työnkulun tarkistuspisteet**: Käytä työnkulun tapahtumia ja sarjallistamista pitkien agenttiprosessien tallentamiseen ja jatkamiseen.
- **Dynaaminen työkalujen valinta**: Yhdistä RAG työkalukuvausten päälle ja MAF:n työkalurekisteröinti esittää vain kyselyyn relevantit työkalut.
- **Moni-agenttien siirrot**: Käytä työnkulun kaaria ja ehdollista reititystä erikoistuneiden agenttien välisiin siirtoihin.

## LangChain / LangGraph Agenttien isännöinti Microsoft Foundryssa

Microsoft Agent Framework on **kehys-yhteensopiva** — et ole rajoitettu vain MAF:lla rakennettuihin agentteihin. Jos sinulla on jo agentti rakennettuna **LangChain**illa tai **LangGraph**illa, voit ajaa sen **Microsoft Foundryn isännöimänä agenttina**, jolloin Foundry hallinnoi ajoaikaa, istuntoja, skaalausta, identiteettiä ja protokollapisteitä puolestasi, samalla kun agenttisi logiikka pysyy LangGraphissa.

Tämä tehdään `langchain_azure_ai.agents.hosting`-paketin avulla, joka tarjoaa käännetyn LangGraph-verkon samoilla protokollilla, joita Foundryn isännöidyt agentit käyttävät.

**1. Asenna hosting-lisäosa:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting`-lisäosa asentaa Foundryn protokollakirjastot: `azure-ai-agentserver-responses` (OpenAI-yhteensopiva `/responses`-päätepiste) ja `azure-ai-agentserver-invocations` (yleinen `/invocations`-päätepiste).

**2. Valitse hosting-protokolla:**

| Protokolla | Isäntäluokka | Päätepiste | Käytössä kun |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Haluat OpenAI-yhteensopivan chatin, suoratoiston, vastaushistorian ja keskusteluketjutuksen — suositeltu oletus keskusteluagentille. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Tarvitset räätälöidyn JSON-muodon, webhook-tyyppisen päätepisteen tai ei-keskustelullisen käsittelyn. |

Koska **Responses API on ensisijainen API agenttityyppiseen kehitykseen Foundryssa**, aloita useimpien agenttien osalta `ResponsesHostServer`-luokalla.

**3. Määritä ympäristömuuttujat** (`az login` ensin, jotta `DefaultAzureCredential` voi autentikoida):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Kun agentti myöhemmin ajetaan isännöitynä Foundryssa, alusta lisää `FOUNDRY_PROJECT_ENDPOINT` automaattisesti.

**4. Tarjoa LangGraph-agentti Responses-protokollan yli:**

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

Aja se paikallisesti komennolla `python main.py`, ja lähetä sitten Responses-pyyntö osoitteeseen `http://localhost:8088/responses`.

**Keskeiset käytökset:**

- **Keskustelut**: Asiakkaat jatkavat keskustelua välittämällä `previous_response_id` tai `conversation` tunnuksen. Jos verkko on käännetty LangGraphin tarkistuspiste-toiminnolla, Foundry avaimistaa keskustelutilan tarkistuspisteeseen (käytä kestävää tarkistuspistettä tuotannossa; `MemorySaver` sopii paikalliseen testaukseen).
- **Ihmisen osallistuminen**: Jos verkossa käytetään LangGraphin `interrupt()`-funktiota, `ResponsesHostServer` tuo odottavan keskeytyksen näkyviin Responses `function_call` / `mcp_approval_request` -kohteena, ja asiakkaat jatkavat vastaavalla `function_call_output` / `mcp_approval_response` -viestillä.
- **Ota käyttöön Foundryssa**: Käytä Azure Developer CLI -työkaluja — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (paikallinen, vaatii Dockerin), sitten `azd provision` ja `azd deploy`. Isännöidyn agentin käyttöönotto vaatii **Foundry Project Manager** -roolin.

Toimiva versio tästä esimerkistä löytyy [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) tiedostosta. Kattava läpikäynti (Invocations-protokolla, räätälöidyt pyyntölomakkeet ja vianmääritys) löytyy sivulta [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Koodiesimerkit 

Microsoft Agent Frameworkin koodiesimerkkejä löytyy tästä repositoriosta tiedostojen `xx-python-agent-framework` ja `xx-dotnet-agent-framework` alta.

## Lisäkysymyksiä Microsoft Agent Frameworkista?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tavata muita oppijoita, osallistua toimistoaikoihin ja saada vastauksia tekoälyagenttien kysymyksiisi.
## Edellinen Oppitunti

[Muisti tekoälyagenteille](../13-agent-memory/README.md)

## Seuraava Oppitunti

[Tietokoneen käytön agenttien rakentaminen (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->