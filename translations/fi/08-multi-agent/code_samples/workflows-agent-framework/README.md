# Moniagenttisovellusten rakentaminen Microsoft Agent Framework Workflowlla

Tämä opas johdattaa sinut Microsoft Agent Frameworkin avulla rakennettujen moniagenttisovellusten ymmärtämiseen ja rakentamiseen. Tutkimme moniagenttijärjestelmien keskeiset käsitteet, sukellamme kehikon Workflow-komponentin arkkitehtuuriin ja käymme läpi käytännön esimerkkejä sekä Pythonilla että .NETillä eri työnkulkujen kuvioista.

## 1\. Moniagenttijärjestelmien ymmärtäminen

AI-agentti on järjestelmä, joka ylittää tavallisen suuren kielimallin (LLM) kyvyt. Se voi hahmottaa ympäristönsä, tehdä päätöksiä ja suorittaa toimia tavoitteiden saavuttamiseksi. Moniagenttijärjestelmä koostuu useista tällaisista agenteista, jotka tekevät yhteistyötä ratkaistakseen ongelman, jonka yksittäinen agentti ei pystyisi käsittelemään yksin.

### Tavalliset käyttötapaukset

  * **Monimutkainen ongelmanratkaisu**: Suuren tehtävän (esim. yrityksen laajuisen tapahtuman suunnittelu) jakaminen pienempiin alitehtäviin, joita hoitavat erikoistuneet agentit (esim. budjettiagentti, logistiikka-agentti, markkinointi-agentti).
  * **Virtuaaliset avustajat**: Pääavustaja-agentti delegoi tehtäviä kuten aikataulutus, tutkimus ja varaukset muille erikoistuneille agenteille.
  * **Automaattinen sisällöntuotanto**: Työnkulku, jossa yksi agentti luonnostelee sisällön, toinen tarkistaa sen tarkkuuden ja sävyn, ja kolmas julkaisee sen.

### Moniagenttimallit

Moniagenttijärjestelmät voidaan järjestää useissa malleissa, jotka määrittävät, miten ne ovat vuorovaikutuksessa:

  * **Peräkkäinen**: Agentit työskentelevät ennalta määritellyssä järjestyksessä, kuin kokoonpanolinjalla. Yhden agentin tulos toimii seuraavan syötteenä.
  * **Samanaikainen**: Agentit suorittavat rinnakkaisesti eri osia tehtävästä, ja niiden tulokset kootaan lopuksi.
  * **Ehdollinen**: Työnkulku seuraa eri polkuja agentin tuottaman tuloksen mukaan, kuten if-then-else-rakenteessa.

## 2\. Microsoft Agent Framework Workflow -arkkitehtuuri

Agent Frameworkin työnkulkujärjestelmä on kehittynyt orkestrointimoottori, joka hallitsee monimutkaisia vuorovaikutuksia useiden agenttien välillä. Se perustuu kaavioarkkitehtuuriin, joka käyttää [Pregel-tyylistä suoritusmallia](https://kowshik.github.io/JPregel/pregel_paper.pdf), jossa käsittely tapahtuu synkronoiduissa vaiheissa, joita kutsutaan "superstepiksi".

### Keskeiset komponentit

Arkkitehtuuri koostuu kolmesta pääosasta:

1.  **Suorittajat**: Nämä ovat perusyksiköitä prosessoinnissa. Esimerkeissämme `Agent` on eräänlainen suorittaja. Jokaisella suorittajalla voi olla useita viestinkäsittelijöitä, jotka kutsutaan automaattisesti vastaanotetun viestityypin mukaan.
2.  **Kaaret**: Ne määrittävät viestien kulkureitin suorittajien välillä. Kaariin voi liittää ehtoja, jotka mahdollistavat tiedon dynaamisen reitityksen työnkulun kaaviossa.
3.  **Työnkulku**: Tämä komponentti orkestroi koko prosessin halliten suorittajia, kaaria ja suorituksen kokonaisvirtaa. Se varmistaa, että viestejä käsitellään oikeassa järjestyksessä ja tuottaa tapahtumavirtoja havainnointia varten.

*Kaavio, joka kuvaa työnkulkujärjestelmän keskeiset komponentit.*

Tämä rakenne mahdollistaa vankkojen ja skaalautuvien sovellusten rakentamisen käyttämällä perusmalleja kuten peräkkäisiä ketjuja, fan-out/fan-in -periaatetta rinnakkaiseen käsittelyyn sekä switch-case-logiikkaa ehdollisissa virroissa.

## 3\. Käytännön esimerkit ja koodianalyysi

Tarkastellaan nyt, miten eri työnkulkuja toteutetaan käyttämällä kehikkoa. Tutkimme sekä Python- että .NET-koodia kutakin esimerkkiä varten.

### Tapaus 1: Perinteinen peräkkäinen työnkulku

Tämä on yksinkertaisin malli, jossa yhden agentin tulos välitetään suoraan toiselle. Tilanteessa hotellin `FrontDesk`-agentti antaa matkasuosituksen, jonka tarkistaa `Concierge`-agentti.

*Kaavio FrontDesk -\> Concierge -työnkulusta.*

#### Tilanteen tausta

Matkailija pyytää suositusta Pariisissa.

1.  `FrontDesk`-agentti, joka on suunniteltu lyhyeksi, ehdottaa Louvre-museon vierailua.
2.  `Concierge`-agentti, joka arvostaa aitoja kokemuksia, saa tämän ehdotuksen. Se tarkistaa suosituksen ja antaa palautetta, ehdottaen paikallisempaa, vähemmän turistikohdetta.

#### Python-toteutuksen analyysi

Python-esimerkissä määrittelemme ja luomme ensin kaksi agenttia, joilla on omat erityisohjeensa.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Määritä agenttien roolit ja ohjeet
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Luo agentti-instansseja
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Seuraavaksi `WorkflowBuilder`-luokkaa käytetään kaavion rakentamiseen. `front_desk_agent` asetetaan aloituspisteeksi, ja sen tuotoksen yhdistämiseksi `reviewer_agent`iin luodaan kaari.

```python
# 01.python-agent-framework-työnkulku-ghmalli-perus.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Lopuksi työnkulku suoritetaan käyttäjän alkuperäisellä kehotteella.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run suorittaa työnkulun; get_outputs() palauttaa output-executorin tuloksen.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) -toteutuksen analyysi

.NET-toteutus noudattaa hyvin samanlaista logiikkaa. Ensin määritellään vakioita agenttien nimille ja ohjeille.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agentit luodaan `AzureOpenAIClient`in (Responses API) avulla, ja sitten `WorkflowBuilder` määrittelee peräkkäisen työnkulun lisäämällä kaaren `frontDeskAgent`ista `reviewerAgent`iin.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetChatClient(deployment).AsAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetChatClient(deployment).AsAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

Työnkulku ajetaan käyttäjän viestillä, ja tulokset virtautetaan takaisin.

### Tapaus 2: Monivaiheinen peräkkäinen työnkulku

Tämä malli laajentaa perussekvenssiä lisäämällä useampia agentteja. Se sopii prosesseihin, jotka vaativat useita tarkistus- tai muokkausvaiheita.

#### Tilanteen tausta

Käyttäjä lähettää kuvan olohuoneesta ja pyytää kalustehintatarjousta.

1.  **Myynti-agentti**: Tunnistaa kuvan kalusteet ja luo listan.
2.  **Hinta-agentti**: Ottaa listan ja antaa yksityiskohtaisen hintajaon, sisältäen budjetti-, keskitason ja premium-vaihtoehdot.
3.  **Tarjous-agentti**: Saa hinnoitellun listan ja muotoilee sen viralliseksi tarjousehdotukseksi Markdown-muodossa.

*Kaavio Sales -\> Price -\> Quote -työnkulusta.*

#### Python-toteutuksen analyysi

Kolme agenttia määritellään, jokaisella oma erikoistunut rooli. Työnkulku rakentuu `add_edge`-metodin avulla ketjuna: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Luo kolme erikoistunutta agenttia
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Rakenna peräkkäinen työnkulku
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Syötteenä on `ChatMessage`, joka sisältää sekä tekstin että kuvan URI:n. Kehikko hoitaa jokaisen agentin tuotoksen siirron seuraavalle ketjussa, kunnes lopullinen tarjous luodaan.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Käyttäjän viesti sisältää sekä tekstiä että kuvan
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Suorita työnkulku
events = await workflow.run(message)
```

#### .NET (C\#) -toteutuksen analyysi

.NET-esimerkki jäljittelee Python-versiota. Kolme agenttia (`salesagent`, `priceagent`, `quoteagent`) luodaan, ja `WorkflowBuilder` yhdistää ne peräkkäin.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent priceagent  = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent quoteagent = azureClient.GetChatClient(deployment).AsAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

Käyttäjän viesti koostuu sekä kuvatiedoista (tavuina) että tekstikehotteesta. `InProcessExecution.RunStreamingAsync`-menetelmä käynnistää työnkulun, ja lopullinen tulos otetaan streamista.

### Tapaus 3: Samanaikainen työnkulku

Tätä mallia käytetään, kun tehtävät voidaan suorittaa samanaikaisesti ajansäästön vuoksi. Siihen liittyy "fan-out" useille agenteille ja "fan-in" tulosten kokoamiseksi.

#### Tilanteen tausta

Käyttäjä pyytää matkan suunnittelua Seattleen.

1.  **Välittäjä (Fan-Out)**: Käyttäjän pyyntö lähetetään kahdelle agentille samanaikaisesti.
2.  **Tutkija-agentti**: Tutkii nähtävyyksiä, säätä ja keskeisiä huomioita joulukuun matkaa Seattleen varten.
3.  **Suunnittelija-agentti**: Laatii itsenäisesti yksityiskohtaisen päiväkohtaisen matkasuunnitelman.
4.  **Kokoaja (Fan-In)**: Molempien agenttien tuotokset kerätään ja esitetään yhdessä lopputuloksena.

*Kaavio rinnakkaisesta Tutkija- ja Suunnittelija -työnkulusta.*

#### Python-toteutuksen analyysi

`ConcurrentBuilder` yksinkertaistaa tämän mallin luomista. Listaat vain osallistuvat agentit, ja rakentaja luo automaattisesti tarvittavan fan-out ja fan-in -logiikan.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder käsittelee fan-out/fan-in-logiikan
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Suorita työnkulku
events = await workflow.run("Plan a trip to Seattle in December")
```

Kehikko varmistaa, että `research_agent` ja `plan_agent` toimivat rinnakkain, ja niiden lopputulokset kerätään listaan.

#### .NET (C\#) -toteutuksen analyysi

.NETissä tämä malli vaatii eksplisiittisen määrittelyn. Mukautetut suorittajat (`ConcurrentStartExecutor` ja `ConcurrentAggregationExecutor`) luodaan fan-out ja fan-in -logiikan käsittelyä varten.

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

`WorkflowBuilder` käyttää sitten `AddFanOutEdge`- ja `AddFanInEdge`-metodeja rakentaakseen kaavion näiden mukautettujen suorittajien ja agenttien kanssa.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Tapaus 4: Ehdollinen työnkulku

Ehdolliset työnkulut sisältävät haarautuvan logiikan, jonka avulla järjestelmä voi kulkea eri polkuja väliinputkien perusteella.

#### Tilanteen tausta

Tämä työnkulku automatisoi teknisen oppaan luomisen ja julkaisun.

1.  **Evangelist-agentti**: Kirjoittaa luonnoksen oppaasta annetun rungon ja URL-osoitteiden perusteella.
2.  **Sisällön tarkistaja -agentti**: Tarkistaa luonnoksen. Se arvioi, ylittääkö sanamäärä 200 sanaa.
3.  **Ehdollinen haara**:
      * **Jos hyväksytty (`Yes`)**: Työnkulku jatkuu `Publisher-agentille`.
      * **Jos hylätty (`No`)**: Työnkulku pysähtyy ja ilmoittaa hylkäyssyyn.
4.  **Julkaisija-agentti**: Jos luonnos hyväksytään, tämä agentti tallentaa sisällön Markdown-tiedostona.

#### Python-toteutuksen analyysi

Tässä esimerkissä käytetään mukautettua funktiota `select_targets`, joka toteuttaa ehdollisen logiikan. Funktio annetaan `add_multi_selection_edge_group` -metodille ja ohjaa työnkulun tarkistajan tuloksen `review_result`-kentän perusteella.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Tämä funktio määrittää seuraavan vaiheen tarkastelutuloksen perusteella
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Jos hyväksytty, siirry 'save_draft' suoritettavaan tehtävään
        return [save_draft_id]
    else:
        # Jos hylätty, siirry 'handle_review' suoritettavaan tehtävään raportoidaksesi epäonnistumisen
        return [handle_review_id]

# Työnkulun rakentaja käyttää reititykseen valintafunktiota
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Monivalintareunus toteuttaa ehdollisen logiikan
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Mukautettuja suorittajia, kuten `to_reviewer_result`, käytetään agenttien JSON-tuotoksen jäsentämiseen ja vahvatyyppisten olioiden muodostamiseen, joita valintafunktio voi tarkastella.

#### .NET (C\#) -toteutuksen analyysi

.NET-versio käyttää samanlaista lähestymistapaa ehtofunktion kanssa. `Func<object?, bool>` määritellään tarkistamaan `ReviewResult`-oliosta `Result`-ominaisuus.

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

`AddEdge`-metodin `condition`-parametri mahdollistaa `WorkflowBuilder`ille haarautuvan polun luomisen. Työnkulku seuraa kaarta `publishExecutor`iin vain, jos ehtofunktio `GetCondition(expectedResult: "Yes")` palauttaa arvon true. Muuten se seuraa polkua `sendReviewerExecutor`iin.

## Yhteenveto

Microsoft Agent Framework Workflow tarjoaa vankan ja joustavan perustan monimutkaisten moniagenttijärjestelmien orkestrointiin. Hyödyntämällä sen kaaviopohjaista arkkitehtuuria ja keskeisiä komponentteja, kehittäjät voivat suunnitella ja toteuttaa monipuolisia työnkulkuja sekä Pythonilla että .NETillä. Olipa sovelluksesi tarpeena yksinkertainen peräkkäinen käsittely, rinnakkainen suoritus tai dynaaminen ehdollinen logiikka, kehikko tarjoaa työkalut tehokkaiden, skaalautuvien ja tyyppiturvallisten tekoälypohjaisten ratkaisujen rakentamiseen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->