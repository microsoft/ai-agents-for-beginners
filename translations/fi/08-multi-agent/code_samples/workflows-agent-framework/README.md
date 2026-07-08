# Moni-agenttisovellusten rakentaminen Microsoft Agent Framework Workflow'lla

Tämä opas ohjaa sinua ymmärtämään ja rakentamaan moni-agenttisovelluksia käyttäen Microsoft Agent Frameworkia. Tutkimme moni-agenttijärjestelmien keskeiset käsitteet, sukellamme frameworkin Workflow-komponentin arkkitehtuuriin ja käymme läpi käytännön esimerkkejä sekä Pythonilla että .NETillä eri työnkulkujen malleista.

## 1\. Moni-agenttijärjestelmien ymmärtäminen

AI-agentti on järjestelmä, joka ylittää tavallisen suuren kielimallin (LLM) kyvyt. Se voi havaita ympäristönsä, tehdä päätöksiä ja toimia saavuttaakseen tiettyjä tavoitteita. Moni-agenttijärjestelmä sisältää useita tällaisia agentteja, jotka tekevät yhteistyötä ratkaistakseen ongelman, joka olisi vaikea tai mahdoton yhdelle agentille yksin.

### Yleiset sovellusskenaariot

  * **Monimutkaisten ongelmien ratkaisu**: Suuren tehtävän (esim. yrityksen laajuisen tapahtuman suunnittelu) pilkkominen pienempiin osatehtäviin, joita käsittelevät erikoistuneet agentit (esim. budjettiasiantuntija, logistiikka-agentti, markkinointiasiantuntija).
  * **Virtuaaliassistentit**: Pääavustaja-agentti delegoi tehtäviä kuten aikataulutus, tutkimus ja varaukset muille erikoistuneille agenteille.
  * **Automaattinen sisällöntuotanto**: Työnkulku, jossa yksi agentti luonnostelee sisällön, toinen tarkistaa tarkkuuden ja sävyn, ja kolmas julkaisee sen.

### Moni-agenttimallit

Moni-agenttijärjestelmät voidaan järjestää useissa malleissa, jotka määräävät niiden vuorovaikutuksen tavan:

  * **Peräkkäinen**: Agentit toimivat ennalta määrätyssä järjestyksessä, kuten kokoonpanolinjalla. Yhden agentin tulos toimii seuraavan agentin syötteenä.
  * **Samaan aikaan**: Agentit työskentelevät rinnakkain eri osissa tehtävää, ja niiden tulokset yhdistetään lopussa.
  * **Ehtoperusteinen**: Työnkulku seuraa eri polkuja agentin tuloksen perusteella, kuten if-then-else-rakenteessa.

## 2\. Microsoft Agent Framework Workflow -arkkitehtuuri

Agent Frameworkin työnkulkujärjestelmä on edistynyt orkestrointimoottori, joka hallinnoi monimutkaisia vuorovaikutuksia useiden agenttien välillä. Se on rakennettu grafiikkapohjaisen arkkitehtuurin varaan, joka käyttää [Pregel-tyylistä suoritustapaa](https://kowshik.github.io/JPregel/pregel_paper.pdf), jossa käsittely tapahtuu synkronoiduissa vaiheissa, joita kutsutaan "supersteps".

### Keskeiset komponentit

Arkkitehtuuri koostuu kolmesta pääosasta:

1.  **Suorittajat**: Nämä ovat perusyksiköitä prosessoinnissa. Esimerkeissämme `Agent` on yksi suorittajatyyppi. Jokaisella suorittajalla voi olla useita viestinkäsittelijöitä, jotka kutsutaan automaattisesti vastaanotetun viestin tyypin mukaan.
2.  **Kaaret**: Määrittelevät viestien kulkureitin suorittajien välillä. Kaariin voi liittyä ehtoja, jotka mahdollistavat dynaamisen tiedon reitityksen työnkulkuverkossa.
3.  **Työnkulku**: Tämä komponentti orkestroi koko prosessin, halliten suorittajia, kaaria ja koko suorituksen virtausta. Se varmistaa, että viestit käsitellään oikeassa järjestyksessä ja lähettää tapahtumia tarkkailtavuuteen.

*Kaavio, joka havainnollistaa työnkulkujärjestelmän keskeisiä komponentteja.*

Tämä rakenne mahdollistaa vankkojen ja skaalautuvien sovellusten rakentamisen käyttämällä perusmalleja kuten peräkkäiset ketjut, fan-out/fan-in rinnakkaiskäsittely ja switch-case-logiikka ehdollisiin polkuihin.

## 3\. Käytännön esimerkit ja koodianalyysi

Tarkastellaan nyt, miten eri työnkulkunäytteitä toteutetaan käyttämällä frameworkia. Käymme läpi sekä Python- että .NET-koodin jokaista esimerkkiä varten.

### Tapaus 1: Perus peräkkäinen työnkulku

Tämä on kaikkein yksinkertaisin malli, jossa yhden agentin tulos siirretään suoraan toiselle. Skenaariossamme hotellin `FrontDesk`-agentti antaa matkasuosituksen, joka sitten tarkistetaan `Concierge`-agentin toimesta.

*Kaavio perustason FrontDesk -> Concierge -työnkulusta.*

#### Skenaarion tausta

Matkustaja pyytää suositusta Pariisissa.

1.  `FrontDesk`-agentti, joka on suunniteltu olosuhteiden mukaan tiiviiksi, ehdottaa vierailua Louvren museoon.
2.  `Concierge`-agentti, joka arvostaa aitoja kokemuksia, vastaanottaa ehdotuksen. Se arvioi suosituksen ja antaa palautetta, ehdottaen paikallisempaa ja vähemmän turistista vaihtoehtoa.

#### Python-toteutuksen analyysi

Python-esimerkissä määrittelemme ensin kaksi agenttia, joista jokaisella on omat ohjeistuksensa.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Määrittele agenttien roolit ja ohjeet
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Luo agenttien instanssit
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Seuraavaksi käytämme `WorkflowBuilder`ia rakentaaksemme verkon. `front_desk_agent` asetetaan aloituspisteeksi ja sen tuotoksen ja `reviewer_agent`-agentin välillä luodaan kaari.

```python
# 01.python-agent-framework-työnkulku-ghmalli-perus.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Lopuksi työnkulku suoritetaan alkuperäisellä käyttäjän kehotteella.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run suorittaa työnkulun; get_outputs() palauttaa ulostuloa suorittavan osan tuloksen.
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
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agentit luodaan käyttämällä `AzureOpenAIClient`ia (Vastaus-API), ja sitten `WorkflowBuilder` määrittää peräkkäisen työnkulun lisäämällä kaaren `frontDeskAgent`in ja `reviewerAgent`in välille.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

Työnkulku käynnistetään käyttäjän viestillä, ja tulokset striimataan takaisin.

### Tapaus 2: Monivaiheinen peräkkäinen työnkulku

Tämä malli laajentaa perussekvenssiä sisältämään enemmän agentteja. Se sopii prosesseihin, jotka tarvitsevat useita tarkastus- tai muuntovaiheita.

#### Skenaarion tausta

Käyttäjä antaa kuvan olohuoneesta ja pyytää kalustehintaa.

1.  **Myynti-agentti**: Tunnistaa kuvan kalusteet ja luo listan.
2.  **Hinta-agentti**: Ottaa listan ja antaa yksityiskohtaisen hintajaon, sisältäen edulliset, keskitason ja premium-vaihtoehdot.
3.  **Tarjous-agentti**: Vastaanottaa hinnoitellun listan ja muotoilee sen viralliseksi tarjousdokumentiksi Markdown-muodossa.

*Kaavio Myynti -> Hinta -> Tarjous -työnkulusta.*

#### Python-toteutuksen analyysi

Kolme agenttia määritellään, jokaisella erikoistunut rooli. Työnkulku rakennetaan käyttämällä `add_edge`-metodia ketjuttaen: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Luo kolme erikoistunutta agenttia
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Rakenna peräkkäinen työnkulku
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Syöte on `ChatMessage`, joka sisältää sekä tekstin että kuvan URI:n. Framework huolehtii siitä, että kunkin agentin tuotos välitetään seuraavalle peräkkäisesti, kunnes lopullinen tarjous on luotu.

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

.NET-esimerkki vastaa Python-versiota. Kolme agenttia (`salesagent`, `priceagent`, `quoteagent`) luodaan. `WorkflowBuilder` linkittää ne peräkkäin.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);
AIAgent priceagent  = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);
AIAgent quoteagent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

Käyttäjän viesti sisältää sekä kuvatiedot (tavujoukkoina) että tekstikehotteen. `InProcessExecution.StreamAsync`-menetelmä käynnistää työnkulun, ja lopputulos kaapataan striimistä.

### Tapaus 3: Rinnakkainen työnkulku

Tätä mallia käytetään, kun tehtäviä voidaan suorittaa samanaikaisesti ajan säästämiseksi. Se sisältää useaan agenttiin haarautumisen ("fan-out") ja tulosten kokoamisen yhteen ("fan-in").

#### Skenaarion tausta

Käyttäjä pyytää suunnittelemaan matkan Seattleen.

1.  **Lähettäjä (Fan-Out)**: Käyttäjän pyyntö lähetetään kahdelle agentille samaan aikaan.
2.  **Tutkija-agentti**: Tutkii nähtävyyksiä, säätä ja keskeisiä matkavinkkejä Seattlessa joulukuussa.
3.  **Suunnittelija-agentti**: Laatii yksityiskohtaisen päiväkohtaisten matkaohjelmien suunnitelman itsenäisesti.
4.  **Kokoaja (Fan-In)**: Molempien agenttien tuotokset kerätään ja esitetään yhdessä lopputuloksena.

*Kaavio rinnakkaisesta Tutkija- ja Suunnittelijatyönkulusta.*

#### Python-toteutuksen analyysi

`ConcurrentBuilder` yksinkertaistaa tämän mallin luontia. Luettelet vain osallistuvat agentit, ja rakentaja luo automaattisesti tarvittavan fan-out ja fan-in-logiikan.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder käsittelee fan-out/fan-in-logiikan
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Suorita työnkulku
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework varmistaa, että `research_agent` ja `plan_agent` suoritetaan rinnakkain, ja niiden lopulliset tulokset kerätään listaan.

#### .NET (C\#) -toteutuksen analyysi

.NETissä tämä malli vaatii eksplisiittisemmän määrittelyn. Räätälöityjä suorittajia (`ConcurrentStartExecutor` ja `ConcurrentAggregationExecutor`) luodaan käsittelemään fan-out ja fan-in-logiikkaa.

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

`WorkflowBuilder` käyttää sitten `AddFanOutEdge` ja `AddFanInEdge` -metodeja rakentaakseen verkon näiden räätälöityjen suorittajien ja agenttien avulla.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Tapaus 4: Ehtoinen työnkulku

Ehtoisissa työnkuluissa on haarautuva logiikka, mikä antaa järjestelmälle mahdollisuuden valita eri polkuja väliarvioiden perusteella.

#### Skenaarion tausta

Tämä työnkulku automatisoi teknisen opastuksen luonnin ja julkaisun.

1.  **Evankelista-agentti**: Kirjoittaa opastuksen luonnoksen annetun rungon ja URL-osoitteiden perusteella.
2.  **Sisällön tarkastaja -agentti**: Tarkistaa luonnoksen. Se tarkistaa onko sanamäärä yli 200 sanaa.
3.  **Ehtoharautus**:
      * **Jos hyväksytään (`Kyllä`)**: Työnkulku jatkuu `Publisher-Agent`ille.
      * **Jos hylätään (`Ei`)**: Työnkulku pysähtyy ja palauttaa hylkäyksen syyn.
4.  **Julkaisija-agentti**: Jos luonnos hyväksytään, tämä agentti tallentaa sisällön Markdown-tiedostoon.

#### Python-toteutuksen analyysi

Tämä esimerkki käyttää räätälöityä funktiota `select_targets` toteuttamaan ehdollisen logiikan. Tämä funktio annetaan `add_multi_selection_edge_group`-metodille ja ohjaa työnkulkua arvion `review_result`-kentän perusteella.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Tämä funktio päättää seuraavan vaiheen arviointituloksen perusteella
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Jos hyväksytään, siirry 'save_draft' suorittajaan
        return [save_draft_id]
    else:
        # Jos hylätään, siirry 'handle_review' suorittajaan raportoimaan epäonnistuminen
        return [handle_review_id]

# Työnkulun rakentaja käyttää valintafunktiota reititykseen
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Monivalintareuna toteuttaa ehdollisen logiikan
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Räätälöityjä suorittajia kuten `to_reviewer_result` käytetään jäsentämään JSON-tulokset agenteilta ja muuntamaan ne vahvasti tyypitetyiksi objekteiksi, joita valintafunktio voi tarkastella.

#### .NET (C\#) -toteutuksen analyysi

.NET-versio käyttää samankaltaista lähestymistapaa ehtofunktion kanssa. `Func<object?, bool>` määritellään tarkistamaan `ReviewResult`-objektin `Result`-ominaisuus.

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

`AddEdge`-metodin `condition`-parametri sallii `WorkflowBuilder`in luoda haarautuvan polun. Työnkulku seuraa kaarta `publishExecutor`iin vain, jos ehto `GetCondition(expectedResult: "Yes")` palauttaa tosi; muuten se seuraa polkua `sendReviewerExecutor`ille.

## Yhteenveto

Microsoft Agent Framework Workflow tarjoaa vahvan ja joustavan perustan monimutkaisten moni-agenttijärjestelmien orkestrointiin. Hyödyntämällä sen grafiikkapohjaista arkkitehtuuria ja keskeisiä komponentteja, kehittäjät voivat suunnitella ja toteuttaa kehittyneitä työnkulkuja sekä Pythonilla että .NETillä. Oli sovelluksesi tarpeena yksinkertainen peräkkäinen käsittely, rinnakkainen suoritus tai dynaaminen ehdollinen logiikka, framework tarjoaa työkalut rakentaa tehokkaita, skaalautuvia ja tyyppiturvallisia AI-pohjaisia ratkaisuja.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->