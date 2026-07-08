# Microsoft Agent Frameworkin tutkiminen

![Agent Framework](../../../translated_images/fi/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Johdanto

Tämä oppitunti kattaa:

- Microsoft Agent Frameworkin ymmärtämisen: keskeiset ominaisuudet ja arvo  
- Microsoft Agent Frameworkin avainkäsitteiden tutkimisen
- Edistyneet MAF-mallit: työnkulut, middleware ja muisti

## Oppimistavoitteet

Oppitunnin suorittamisen jälkeen osaat:

- Rakentaa tuotantovalmiita tekoälyagentteja Microsoft Agent Frameworkilla
- Soveltaa Microsoft Agent Frameworkin keskeisiä ominaisuuksia agenttikäyttötapauksiin
- Käyttää edistyneitä malleja kuten työnkulkuja, middlewarea ja havaittavuutta

## Koodiesimerkit

[Microsoft Agent Frameworkin (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) koodiesimerkkejä löytyy tästä varastosta tiedostoista `xx-python-agent-framework` ja `xx-dotnet-agent-framework`.

## Microsoft Agent Frameworkin ymmärtäminen

![Framework Intro](../../../translated_images/fi/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) on Microsoftin yhtenäinen kehys tekoälyagenttien rakentamiseen. Se tarjoaa joustavuutta käsitellä laajaa valikoimaa agenttikäyttötapauksia sekä tuotanto- että tutkimusympäristöissä, mukaan lukien:

- **Järjestelmällinen agenttien orkestrointi** tilanteissa, joissa tarvitaan vaiheittaista työnkulkua.
- **Samaan aikaan tapahtuva orkestrointi** tilanteissa, joissa agenttien on suoritettava tehtäviä samanaikaisesti.
- **Ryhmäkeskustelun orkestrointi** tilanteissa, joissa agentit voivat tehdä yhteistyötä yhden tehtävän parissa.
- **Tehtävien luovutus** tilanteissa, joissa agentit siirtävät tehtävän toisilleen sitä mukaa kun alitehtävät valmistuvat.
- **Magnettinen orkestrointi** tilanteissa, joissa johtaja-agentti luo ja muokkaa tehtävälistaa ja hoitaa koordinaatiota alitehtävien suorittamiseksi.

Tuotantovalmistettujen tekoälyagenttien toimittamiseksi MAF sisältää myös ominaisuuksia, kuten:

- **Havaittavuus** OpenTelemetryn avulla, jossa tekoälyagentin jokainen toiminto, mukaan lukien työkalujen kutsuminen, orkestrointivaiheet, päättelyvirrat ja suorituskyvyn seuranta Microsoft Foundryn kojelaudoilla.
- **Turvallisuus** isännöimällä agentteja natiivisti Microsoft Foundryssa, johon sisältyy roolipohjainen pääsynvalvonta, yksityisten tietojen käsittely ja sisäänrakennettu sisältöturva.
- **Kestävyys** siten, että agenttien langat ja työnkulut voivat pysähtyä, jatkua ja palautua virheistä, mikä mahdollistaa pidempiaikaiset prosessit.
- **Hallinta** tukemalla ihmisen osallistumista työnkulkuihin, joissa tehtävät merkitään ihmisen hyväksyntää vaativiksi.

Microsoft Agent Framework keskittyy myös yhteentoimivuuteen:

- **Pilviriippumattomuus** - agentit voivat toimia konteissa, paikallisesti ja eri pilvialustoilla.
- **Tarjoajariippumattomuus** - agentteja voidaan luoda suosimallasi SDK:lla, mukaan lukien Azure OpenAI ja OpenAI.
- **Avoimien standardien integrointi** - agentit voivat käyttää protokollia kuten Agent-to-Agent (A2A) ja Model Context Protocol (MCP) löytääkseen ja käyttäessään muita agentteja ja työkaluja.
- **Lisäosat ja liittimet** - yhteydet voidaan muodostaa data- ja muistipalveluihin kuten Microsoft Fabric, SharePoint, Pinecone ja Qdrant.

Tarkastellaan miten näitä ominaisuuksia sovelletaan Microsoft Agent Frameworkin keskeisiin käsitteisiin.

## Microsoft Agent Frameworkin keskeiset käsitteet

### Agentit

![Agent Framework](../../../translated_images/fi/agent-components.410a06daf87b4fef.webp)

**Agenttien luominen**

Agentti luodaan määrittelemällä inferointipalvelu (LLM-tarjoaja), joukko ohjeita joita tekoälyagentin tulee noudattaa, sekä sille annetaan `nimi`:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Edellä käytetään `Azure OpenAI` -palvelua, mutta agentteja voidaan luoda myös erilaisilla palveluilla, kuten `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI:n `Responses`, `ChatCompletion`-rajapinnat

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

tai [MiniMax](https://platform.minimaxi.com/), joka tarjoaa OpenAI-yhteensopivan rajapinnan suurilla kontekstikehysyillä (jopa 204K tokenia):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

tai etäagentit käyttäen A2A-protokollaa:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Agenttien suoritus**

Agentteja suoritetaan käyttämällä `.run`tai `.run_stream`-metodeja ei-suoratoistoon tai suoratoistoon.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Jokaiselle agentin suoritukselle voidaan myös määrittää vaihtoehtoja, kuten agentin käyttämät `max_tokens`, agentin kutsumat `tools`-työkalut ja jopa agentin käyttämä `malli`.

Tämä on hyödyllistä tilanteissa, joissa tiettyjä malleja tai työkaluja tarvitaan käyttäjän tehtävän suorittamiseen.

**Työkalut**

Työkaluja voidaan määrittää sekä agenttia luotaessa:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Kun luot ChatAgentin suoraan

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

että agenttia suoritettaessa:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Työkalu tarjottu vain tätä ajoa varten )
```

**Agenttilangat**

Agenttilangat mahdollistavat monikierroksiset keskustelut. Langat voidaan luoda joko:

- Käyttämällä `get_new_thread()`, joka sallii langan tallentamisen ajan myötä
- Luomalla lanka automaattisesti agenttia suoritettaessa, jolloin lanka kestää vain kyseisen suorituksen ajan.

Langat luodaan koodilla seuraavasti:

```python
# Luo uusi säie.
thread = agent.get_new_thread() # Suorita agentti säikeellä.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Lanka voidaan sen jälkeen serialisoida myöhempää käyttöä varten:

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

Agentit käyttävät työkaluja ja LLM:iä käyttäjän tehtävien suorittamiseen. Tietyissä tilanteissa haluamme suorittaa tai seurata toimintoja näiden välisten vuorovaikutusten aikana. Agentin middleware mahdollistaa tämän seuraavasti:

*Funktiomiddleware*

Tämä middleware antaa meille mahdollisuuden suorittaa toiminto agentin ja hänen kutsumansa funktion/työkalun välillä. Esimerkki käytöstä on, kun haluat kirjata funktion kutsun lokiin.

Alla olevassa koodissa `next` määrittää, kutsutaanko seuraava middleware vai varsinainen funktio.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Esikäsittely: Kirjaa lokiin ennen funktion suorittamista
    print(f"[Function] Calling {context.function.name}")

    # Jatka seuraavaan middlewareen tai funktion suoritukseen
    await next(context)

    # Jälkikäsittely: Kirjaa lokiin funktion suorituksen jälkeen
    print(f"[Function] {context.function.name} completed")
```

*Chat-middleware*

Tämä middleware mahdollistaa toiminnon suorittamisen tai kirjaamisen agentin ja LLM:n välisissä pyynnöissä.

Tämä sisältää tärkeitä tietoja, kuten `messages` jotka lähetetään tekoälypalveluun.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Esikäsittely: Kirjaa lokiin ennen tekoälykutsua
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Jatka seuraavaan middlewareen tai tekoälypalveluun
    await next(context)

    # Jälkikäsittely: Kirjaa lokiin tekoälyn vastauksen jälkeen
    print("[Chat] AI response received")

```

**Agentin muisti**

Kuten `Agentic Memory` -oppitunnissa käsiteltiin, muisti on tärkeä osa agentin kykyä toimia eri konteksteissa. MAF tarjoaa useita erilaisia muistityyppejä:

*Muisti ohjelman ajon aikana*

Tämä on muisti, joka tallennetaan lankoihin sovelluksen käynnin aikana.

```python
# Luo uusi säie.
thread = agent.get_new_thread() # Suorita agentti säikeen kanssa.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Pysyvät viestit*

Tätä muistia käytetään keskusteluhistorian tallentamiseen eri istuntojen välillä. Se määritellään `chat_message_store_factory`-toiminnolla:

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

Tämä muisti lisätään kontekstiin ennen agenttien suorittamista. Näitä muistoja voidaan tallentaa ulkoisissa palveluissa kuten mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Käytetään Mem0:aa kehittyneisiin muistitoimintoihin
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


Havainnointikyky on tärkeää luotettavien ja ylläpidettävien agenttipohjaisten järjestelmien rakentamisessa. MAF integroituu OpenTelemetryyn tarjoten jäljitystä ja mittareita paremman havainnointikyvyn saavuttamiseksi.

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

Työnkulut koostuvat eri komponenteista, jotka mahdollistavat paremman kontrolloinnin työnkulussa. Työnkulut mahdollistavat myös **moniagenttien orkestroinnin** ja **tarkistuspisteiden tallennuksen** työnkulun tilojen säilyttämiseksi.

Työnkulun ydinkomponentit ovat:

**Suorittajat**

Suorittajat vastaanottavat syötemessuja, suorittavat heille annetut tehtävät ja tuottavat sitten tulostemessun. Tämä siirtää työnkulkua eteenpäin kohti suuremman tehtävän suorittamista. Suorittajat voivat olla joko tekoälyagentteja tai kustomoitua logiikkaa.

**Sillat**

Siltoja käytetään määrittämään viestien kulku työnkulussa. Näitä voivat olla:

*Suorat sillat* - Yksinkertaiset yhden suhde yhteen -yhteydet suorittajien välillä:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Ehdolliset sillat* - Aktivoituvat tietyn ehdon täyttyessä. Esimerkiksi, kun hotellihuoneet eivät ole saatavilla, suorittaja voi ehdottaa muita vaihtoehtoja.

*Kytkin-tapaussillat* - Reitittävät viestit eri suorittajille määriteltyjen ehtojen perusteella. Esimerkiksi, jos matkustajalla on etuoikeutettu pääsy, heidän tehtävänsä käsitellään toisen työnkulun kautta.

*Hajautussillat* - Lähettävät yhden viestin useille kohteille.

*Yhdistyssillat* - Keräävät useita viestejä eri suorittajilta ja lähettävät ne yhdelle kohteelle.

**Tapahtumat**

Tarjotakseen paremman havainnointikyvyn työnkulkuihin, MAF tarjoaa sisäänrakennettuja tapahtumia suorituksen aikana, mukaan lukien:

- `WorkflowStartedEvent`  - Työnkulun suoritus alkaa
- `WorkflowOutputEvent` - Työnkulku tuottaa tuloksen
- `WorkflowErrorEvent` - Työnkulku kohtaa virheen
- `ExecutorInvokeEvent`  - Suorittaja aloittaa käsittelyn
- `ExecutorCompleteEvent`  -  Suorittaja päättää käsittelyn
- `RequestInfoEvent` - Pyyntö lähetetään

## Edistyneet MAF-mallit

Edellä olevat osiot käsittelivät Microsoft Agent Frameworkin keskeisiä käsitteitä. Kun rakennat monimutkaisempia agenteja, tässä on joitakin edistyneitä malleja, joita kannattaa harkita:

- **Välikerrosyhdistelmät**: Ketjuta useita välikerroskäsittelijöitä (kirjautuminen, autentikointi, nopeudenrajoitus) käyttäen sekä toiminto- että keskusteluvälikerrosta tarkkaa hallintaa varten agentin käyttäytymisessä.
- **Työnkulun tarkistuspisteet**: Käytä työnkulun tapahtumia ja sarjallistamista pitkäkestoisten agenttiprosessien tallentamiseen ja jatkamiseen.
- **Dynaaminen työkalun valinta**: Yhdistä RAG työkalukuvauksiin MAF:n työkalujen rekisteröinnin kanssa, jotta näytetään vain asiakyselyyn liittyvät työkalut.
- **Moniagenttien siirrot**: Käytä työnkulun siltoja ja ehdollista reititystä orkestroidaksesi siirrot erikoistuneiden agenttien välillä.

## LangChain / LangGraph -agenttien hostaus Microsoft Foundryssa

Microsoft Agent Framework on **kehyksen välisesti yhteensopiva** — et ole rajoittunut vain MAF:lla kirjoitettuihin agenteihin. Jos sinulla on jo agentti rakennettu **LangChain**- tai **LangGraph**-työkaluilla, voit ajaa sen **Microsoft Foundryn ylläpitämänä agenttina**, jolloin Foundry hallinnoi ajonaikaa, istuntoja, skaalausta, tunnistautumista ja protokollapäätepisteitä puolestasi, samalla kun agentin logiikka pysyy LangGraphissa.

Tämä tehdään `langchain_azure_ai.agents.hosting`-paketilla, joka tarjoaa käännetyn LangGraph-verkon samaa protokollaa käyttäen, mitä Foundryn ylläpitämät agentit hyödyntävät.

**1. Asenna hosting-lisäosa:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` lisäosa asentaa Foundryn protokollakirjastot: `azure-ai-agentserver-responses` (OpenAI-yhteensopiva `/responses` päätepiste) ja `azure-ai-agentserver-invocations` (yleiskäyttöinen `/invocations` päätepiste).

**2. Valitse hosting-protokolla:**

| Protokolla | Host-luokka | Päätepiste | Käytetään kun |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Haluat OpenAI-yhteensopivan chatin, suoratoiston, vastaushistorian ja keskusteluketjutuksen — suositeltu oletus keskusteluagentteihin. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Tarvitset kustomoidun JSON-muodon, webhook-tyyppisen päätepisteen tai ei-keskustelevaa käsittelyä. |

Koska **Responses-rajapinta on ensisijainen rajapinta agenttipohjaiseen kehitykseen Foundryssa**, aloita useimmissa agenteissa `ResponsesHostServer`-luokalla.

**3. Määritä ympäristömuuttujat** (`az login` ensin, jotta `DefaultAzureCredential` voi todentaa):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

Kun agentti myöhemmin ajetaan ylläpidettynä agenttina Foundryssa, alusta lisää automaattisesti `FOUNDRY_PROJECT_ENDPOINT`-muuttujan.

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
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-4.1")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI tässä kohdistaa Foundry-projektin OpenAI-yhteensopivaan (Vastaukset) päätepisteeseen.
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

Aja se lokaalisti komennolla `python main.py`, sitten lähetä Responses-pyyntö osoitteeseen `http://localhost:8088/responses`.

**Keskeiset toiminnot:**

- **Keskustelut**: Asiakkaat jatkavat keskustelua välittämällä `previous_response_id` tai `conversation` ID:n. Jos verkko on käännetty LangGraphin tarkistuspisteen kanssa, Foundry yhdistää keskustelutilan tarkistuspisteeseen (käytä kestävää tarkistuspistettä tuotannossa; `MemorySaver` käy paikalliseen testaukseen).
- **Ihmisen osallistuminen**: Jos verkossa käytetään LangGraphin `interrupt()`-funktiota, `ResponsesHostServer` näyttää odottavan keskeytyksen Responsesin `function_call` / `mcp_approval_request` -kohteena, ja asiakkaat jatkavat vastaavalla `function_call_output` / `mcp_approval_response`.
- **Julkaisu Foundryssa**: Käytä Azure Developer CLI:tä — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokaali, vaatii Dockerin), sitten `azd provision` ja `azd deploy`. Ylläpidetyn agentin julkaisu vaatii **Foundry Project Manager** -roolin.

Suoritettava versio tästä esimerkistä löytyy tiedostosta [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Täydelliseen läpikäyntiin (Invocations-protokolla, kustomoidut pyyntörakenteet ja vianetsintä) katso [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Koodiesimerkit 

Microsoft Agent Frameworkin koodiesimerkkejä löytyy tästä repositoriosta tiedostoista `xx-python-agent-framework` ja `xx-dotnet-agent-framework`.

## Onko sinulla lisää kysymyksiä Microsoft Agent Frameworkista?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tavata muita oppijoita, osallistua aukioloaikoihin ja saada vastauksia tekoäly-agenttikysymyksiisi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->