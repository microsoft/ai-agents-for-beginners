# Moniagenttisovellusten rakentaminen Microsoft Agent Framework Workflow'n avulla

Tämä opas auttaa sinua ymmärtämään ja rakentamaan moniagenttisovelluksia Microsoft Agent Frameworkin avulla. Käymme läpi moniagenttijärjestelmien keskeiset käsitteet, tutustumme frameworkin Workflow-komponentin arkkitehtuuriin ja tarkastelemme käytännön esimerkkejä Pythonilla ja .NET:llä eri työnkulkujen malleista.

## 1\. Moniagenttijärjestelmien ymmärtäminen

AI-agentti on järjestelmä, joka ylittää tavallisen suuren kielimallin (LLM) kyvyt. Se voi havainnoida ympäristöään, tehdä päätöksiä ja toimia saavuttaakseen tiettyjä tavoitteita. Moniagenttijärjestelmässä useat agentit tekevät yhteistyötä ratkaistakseen ongelman, joka olisi vaikea tai mahdoton yksittäisen agentin käsitellä.

### Yleiset sovellusskenaariot

  * **Monimutkaisten ongelmien ratkaisu**: Suuren tehtävän (esim. yrityksen laajuisen tapahtuman suunnittelu) jakaminen pienempiin osatehtäviin, joita hoitavat erikoistuneet agentit (esim. budjettiagentti, logistiikka-agentti, markkinointiagentti).
  * **Virtuaaliassistentit**: Pääassistenttiagentti delegoi tehtäviä, kuten aikataulutusta, tutkimusta ja varaamista, muille erikoistuneille agenteille.
  * **Automaattinen sisällöntuotanto**: Työnkulku, jossa yksi agentti luonnostelee sisällön, toinen tarkistaa sen tarkkuuden ja sävyn, ja kolmas julkaisee sen.

### Moniagenttimallit

Moniagenttijärjestelmät voidaan järjestää useisiin malleihin, jotka määrittävät niiden vuorovaikutustavat:

  * **Peräkkäinen**: Agentit toimivat ennalta määritetyssä järjestyksessä, kuten kokoonpanolinjalla. Yhden agentin tuotos siirtyy seuraavan agentin syötteeksi.
  * **Rinnakkainen**: Agentit työskentelevät samanaikaisesti eri osatehtävien parissa, ja niiden tulokset yhdistetään lopuksi.
  * **Ehdollinen**: Työnkulku seuraa eri polkuja agentin tuottaman tuloksen perusteella, kuten if-then-else-lauseessa.

## 2\. Microsoft Agent Framework Workflow -arkkitehtuuri

Agent Frameworkin työnkulkujärjestelmä on edistynyt orkestrointimoottori, joka on suunniteltu hallitsemaan monimutkaisia vuorovaikutuksia useiden agenttien välillä. Se perustuu graafipohjaiseen arkkitehtuuriin, joka käyttää [Pregel-tyylistä suoritusmallia](https://kowshik.github.io/JPregel/pregel_paper.pdf), jossa käsittely tapahtuu synkronoiduissa vaiheissa, joita kutsutaan "superstepiksi".

### Keskeiset komponentit

Arkkitehtuuri koostuu kolmesta pääosasta:

1.  **Suorittimet**: Nämä ovat perustason käsittelyyksiköitä. Esimerkeissämme `Agent` on suorittimen tyyppi. Jokaisella suorittimella voi olla useita viestinkäsittelijöitä, jotka aktivoituvat automaattisesti vastaanotetun viestin tyypin perusteella.
2.  **Reunat**: Nämä määrittävät polun, jota viestit kulkevat suorittimien välillä. Reunoilla voi olla ehtoja, jotka mahdollistavat tiedon dynaamisen reitityksen työnkulun graafissa.
3.  **Työnkulku**: Tämä komponentti orkestroi koko prosessin, hallitsee suorittimia, reunoja ja koko suoritusvirtaa. Se varmistaa, että viestit käsitellään oikeassa järjestyksessä ja lähettää tapahtumia havainnointia varten.

*Kaavio, joka havainnollistaa työnkulkujärjestelmän keskeisiä komponentteja.*

Tämä rakenne mahdollistaa vankkojen ja skaalautuvien sovellusten rakentamisen perusmallien, kuten peräkkäisten ketjujen, rinnakkaisen käsittelyn fan-out/fan-in-mallien ja ehdollisten virtojen switch-case-logiikan avulla.

## 3\. Käytännön esimerkit ja koodianalyysi

Tarkastellaan nyt, kuinka eri työnkulun malleja toteutetaan frameworkin avulla. Käymme läpi Python- ja .NET-koodia jokaisessa esimerkissä.

### Tapaus 1: Perus peräkkäinen työnkulku

Tämä on yksinkertaisin malli, jossa yhden agentin tuotos siirtyy suoraan toiselle. Skenaariomme sisältää hotellin `FrontDesk`-agentin, joka tekee matkasuosituksen, jonka `Concierge`-agentti tarkistaa.

*Kaavio perus FrontDesk -> Concierge -työnkulusta.*

#### Skenaarion tausta

Matkustaja pyytää suositusta Pariisissa.

1.  `FrontDesk`-agentti, joka keskittyy ytimekkyyteen, ehdottaa vierailua Louvren museossa.
2.  `Concierge`-agentti, joka arvostaa autenttisia kokemuksia, vastaanottaa ehdotuksen. Se tarkistaa suosituksen ja antaa palautetta, ehdottaen paikallisempaa ja vähemmän turistista vaihtoehtoa.

#### Python-toteutuksen analyysi

Python-esimerkissä määritellään ja luodaan kaksi agenttia, joilla on erityiset ohjeet.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Define agent roles and instructions
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Create agent instances
reviewer_agent = chat_client.create_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.create_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Seuraavaksi `WorkflowBuilder`-työkalua käytetään graafin rakentamiseen. `front_desk_agent` asetetaan aloituspisteeksi, ja sen tuotos yhdistetään `reviewer_agent`-agenttiin.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Lopuksi työnkulku suoritetaan käyttäjän alkuperäisellä kehotteella.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C#) -toteutuksen analyysi

.NET-toteutus noudattaa hyvin samanlaista logiikkaa. Ensin määritellään agenttien nimet ja ohjeet.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agentit luodaan `OpenAIClient`-työkalulla, ja sitten `WorkflowBuilder` määrittää peräkkäisen virran lisäämällä reunan `frontDeskAgent`-agentista `reviewerAgent`-agenttiin.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

Työnkulku suoritetaan käyttäjän viestillä, ja tulokset striimataan takaisin.

### Tapaus 2: Monivaiheinen peräkkäinen työnkulku

Tämä malli laajentaa perusjärjestystä sisältämään enemmän agentteja. Se sopii prosesseihin, jotka vaativat useita tarkennus- tai muunnosvaiheita.

#### Skenaarion tausta

Käyttäjä antaa kuvan olohuoneesta ja pyytää huonekalutarjousta.

1.  **Sales-Agent**: Tunnistaa kuvassa olevat huonekalut ja luo listan.
2.  **Price-Agent**: Ottaa huonekalulistan ja antaa yksityiskohtaisen hintajaon, mukaan lukien budjetti-, keskitason ja premium-vaihtoehdot.
3.  **Quote-Agent**: Saa hinnoitellun listan ja muotoilee sen viralliseksi tarjousdokumentiksi Markdown-muodossa.

*Kaavio Sales -> Price -> Quote -työnkulusta.*

#### Python-toteutuksen analyysi

Kolme agenttia määritellään, jokaisella on erikoistunut rooli. Työnkulku rakennetaan `add_edge`-toiminnolla luomaan ketju: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Syöte on `ChatMessage`, joka sisältää sekä tekstin että kuvan URI:n. Framework huolehtii siitä, että jokaisen agentin tuotos siirtyy seuraavalle ketjussa, kunnes lopullinen tarjous on luotu.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# The user message contains both text and an image
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Run the workflow
async for event in workflow.run_stream(message):
    ...
```

#### .NET (C#) -toteutuksen analyysi

.NET-esimerkki peilaa Python-versiota. Kolme agenttia (`salesagent`, `priceagent`, `quoteagent`) luodaan. `WorkflowBuilder` yhdistää ne peräkkäin.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent priceagent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent quoteagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

Käyttäjän viesti koostuu sekä kuvadataa (tavuina) että tekstikehotteesta. `InProcessExecution.StreamAsync`-metodi käynnistää työnkulun, ja lopullinen tulos otetaan talteen striimistä.

### Tapaus 3: Rinnakkainen työnkulku

Tätä mallia käytetään, kun tehtävät voidaan suorittaa samanaikaisesti ajan säästämiseksi. Se sisältää "fan-out"-vaiheen useille agenteille ja "fan-in"-vaiheen tulosten yhdistämiseksi.

#### Skenaarion tausta

Käyttäjä pyytää suunnittelemaan matkan Seattleen.

1.  **Dispatcher (Fan-Out)**: Käyttäjän pyyntö lähetetään samanaikaisesti kahdelle agentille.
2.  **Researcher-Agent**: Tutkii nähtävyyksiä, säätä ja keskeisiä huomioita matkaa varten Seattleen joulukuussa.
3.  **Plan-Agent**: Laatii itsenäisesti yksityiskohtaisen päiväkohtaisen matkasuunnitelman.
4.  **Aggregator (Fan-In)**: Tutkijan ja suunnittelijan tuotokset kerätään ja esitetään yhdessä lopullisena tuloksena.

*Kaavio rinnakkaisesta Researcher ja Planner -työnkulusta.*

#### Python-toteutuksen analyysi

`ConcurrentBuilder` yksinkertaistaa tämän mallin luomista. Luettelo osallistuvista agenteista annetaan, ja builder luo automaattisesti tarvittavan fan-out- ja fan-in-logiikan.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework varmistaa, että `research_agent` ja `plan_agent` suorittavat tehtävänsä rinnakkain, ja niiden lopulliset tuotokset kerätään listaksi.

#### .NET (C#) -toteutuksen analyysi

.NET:ssä tämä malli vaatii tarkemman määrittelyn. Mukautetut suorittimet (`ConcurrentStartExecutor` ja `ConcurrentAggregationExecutor`) luodaan käsittelemään fan-out- ja fan-in-logiikkaa.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

// Custom executor to broadcast the message to all agents
public class ConcurrentStartExecutor() : ...
{
    public async ValueTask HandleAsync(string message, IWorkflowContext context)
    {
        // Send message to all connected agents
        await context.SendMessageAsync(new ChatMessage(ChatRole.User, message));
        // Send a token to start processing
        await context.SendMessageAsync(new TurnToken(emitEvents: true));
    }
}

// Custom executor to collect results
public class ConcurrentAggregationExecutor() : ...
{
    private readonly List<ChatMessage> _messages = [];
    public async ValueTask HandleAsync(ChatMessage message, IWorkflowContext context)
    {
        this._messages.Add(message);
        // Once both agents have responded, yield the final output
        if (this._messages.Count == 2)
        {
            ...
            await context.YieldOutputAsync(formattedMessages);
        }
    }
}
```

`WorkflowBuilder` käyttää `AddFanOutEdge`- ja `AddFanInEdge`-toimintoja graafin rakentamiseen näillä mukautetuilla suorittimilla ja agenteilla.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Tapaus 4: Ehdollinen työnkulku

Ehdolliset työnkulut tuovat mukaan haarautumislogiikan, joka mahdollistaa eri polkujen seuraamisen välitulosten perusteella.

#### Skenaarion tausta

Tämä työnkulku automatisoi teknisen oppaan luomisen ja julkaisemisen.

1.  **Evangelist-Agent**: Kirjoittaa oppaan luonnoksen annetun hahmotelman ja URL-osoitteiden perusteella.
2.  **ContentReviewer-Agent**: Tarkistaa luonnoksen. Se tarkistaa, onko sanamäärä yli 200 sanaa.
3.  **Ehdollinen haara**:
      * **Jos hyväksytty (`Yes`)**: Työnkulku etenee `Publisher-Agent`-agenttiin.
      * **Jos hylätty (`No`)**: Työnkulku pysähtyy ja antaa hylkäyksen syyn.
4.  **Publisher-Agent**: Jos luonnos hyväksytään, tämä agentti tallentaa sisällön Markdown-tiedostoon.

#### Python-toteutuksen analyysi

Tässä esimerkissä käytetään mukautettua funktiota, `select_targets`, ehdollisen logiikan toteuttamiseen. Tämä funktio annetaan `add_multi_selection_edge_group`-toiminnolle ja ohjaa työnkulun `review_result`-kentän perusteella, joka saadaan tarkistajan tuotoksesta.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# This function determines the next step based on the review result
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # If approved, proceed to the 'save_draft' executor
        return [save_draft_id]
    else:
        # If rejected, proceed to the 'handle_review' executor to report failure
        return [handle_review_id]

# The workflow builder uses the selection function for routing
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # The multi-selection edge implements the conditional logic
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Mukautettuja suorittimia, kuten `to_reviewer_result`, käytetään JSON-tuloksen jäsentämiseen agenteilta ja sen muuntamiseen vahvasti tyypitetyiksi objekteiksi, joita valintafunktio voi tarkastella.

#### .NET (C#) -toteutuksen analyysi

.NET-versio käyttää samanlaista lähestymistapaa ehtofunktion kanssa. `Func<object?, bool>` määritellään tarkistamaan `ReviewResult`-objektin `Result`-ominaisuus.

```csharp
// 04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb

// This function creates a lambda for the condition check
public Func<object?, bool> GetCondition(string expectedResult) =>
        reviewResult => reviewResult is ReviewResult review && review.Result == expectedResult;

// The workflow is built with conditional edges
var workflow = new WorkflowBuilder(draftExecutor)
            .AddEdge(draftExecutor, contentReviewerExecutor)
            // Add an edge to the publisher only if the review result is "Yes"
            .AddEdge(contentReviewerExecutor, publishExecutor, condition: GetCondition(expectedResult: "Yes"))
            // Add an edge to the reviewer feedback executor if the result is "No"
            .AddEdge(contentReviewerExecutor, sendReviewerExecutor, condition: GetCondition(expectedResult: "No"))
            .Build();
```

`AddEdge`-metodin `condition`-parametri mahdollistaa `WorkflowBuilder`-työkalun luomaan haarautuvan polun. Työnkulku seuraa reunaa `publishExecutor`-suorittimeen vain, jos ehto `GetCondition(expectedResult: "Yes")` palauttaa true. Muussa tapauksessa se seuraa polkua `sendReviewerExecutor`-suorittimeen.

## Yhteenveto

Microsoft Agent Framework Workflow tarjoaa vankan ja joustavan perustan monimutkaisten moniagenttijärjestelmien orkestrointiin. Sen graafipohjaisen arkkitehtuurin ja keskeisten komponenttien avulla kehittäjät voivat suunnitella ja toteuttaa kehittyneitä työnkulkuja sekä Pythonilla että .NET:llä. Olipa sovelluksesi tarpeena yksinkertainen peräkkäinen käsittely, rinnakkainen suoritus tai dynaaminen ehdollinen logiikka, framework tarjoaa työkalut tehokkaiden, skaalautuvien ja tyyppiturvallisten tekoälyratkaisujen rakentamiseen.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.