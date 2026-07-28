# Gebruik van Agentic Protocols (MCP, A2A en NLWeb)

[![Agentic Protocols](../../../translated_images/nl/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

Naarmate het gebruik van AI-agenten toeneemt, groeit ook de behoefte aan protocollen die standaardisatie, beveiliging en ondersteuning voor open innovatie waarborgen. In deze les behandelen we 3 protocollen die aan deze behoefte voldoen - Model Context Protocol (MCP), Agent to Agent (A2A) en Natural Language Web (NLWeb).

## Introductie

In deze les behandelen we:

• Hoe **MCP** AI Agenten toegang geeft tot externe tools en data om gebruikersopdrachten uit te voeren.

• Hoe **A2A** communicatie en samenwerking tussen verschillende AI-agenten mogelijk maakt.

• Hoe **NLWeb** natuurlijke taalinterfaces aan elke website toevoegt zodat AI Agenten de inhoud kunnen ontdekken en ermee kunnen interactieren.

## Leerdoelen

• **Identificeren** van het hoofddoel en de voordelen van MCP, A2A en NLWeb in de context van AI-agenten.

• **Uitleggen** hoe elk protocol communicatie en interactie tussen LLMs, tools en andere agenten faciliteert.

• **Herkennen** van de verschillende rollen die elk protocol speelt bij het bouwen van complexe agentic systemen.

## Model Context Protocol

Het **Model Context Protocol (MCP)** is een open standaard die een gestandaardiseerde manier biedt voor applicaties om context en tools aan LLMs te leveren. Dit maakt een "universele adapter" mogelijk naar verschillende databronnen en tools waar AI-agenten op een consistente manier mee kunnen verbinden.

Laten we kijken naar de componenten van MCP, de voordelen ten opzichte van directe API-gebruik, en een voorbeeld van hoe AI-agenten een MCP-server kunnen gebruiken.

### Kerncomponenten van MCP

MCP werkt op basis van een **client-server architectuur** en de kerncomponenten zijn:

• **Hosts** zijn LLM-applicaties (bijvoorbeeld een code-editor zoals VSCode) die de verbindingen met een MCP Server starten.

• **Clients** zijn componenten binnen de hostapplicatie die één-op-één verbindingen met servers onderhouden.

• **Servers** zijn lichte programma's die specifieke functionaliteiten blootstellen.

In het protocol zijn drie kern-primitieven opgenomen die de mogelijkheden van een MCP Server vormen:

• **Tools**: Dit zijn discrete acties of functies die een AI-agent kan aanroepen om een taak uit te voeren. Bijvoorbeeld, een weerservice zou een "haal weer op" tool kunnen bieden, of een e-commerce server zou een "koop product" tool kunnen bieden. MCP-servers adverteren elke tool met naam, beschrijving en input/output schema in hun mogelijkhedenlijst.

• **Resources**: Dit zijn alleen-lezen data-items of documenten die een MCP-server kan leveren, en clients kunnen deze op verzoek ophalen. Voorbeelden zijn bestandsinhoud, database-records of logbestanden. Resources kunnen tekst zijn (zoals code of JSON) of binair (zoals afbeeldingen of PDF's).

• **Prompts**: Dit zijn vooraf gedefinieerde sjablonen die suggesties geven, waardoor complexere workflows mogelijk zijn.

### Voordelen van MCP

MCP biedt aanzienlijke voordelen voor AI-agenten:

• **Dynamische Tooldetectie**: Agenten kunnen dynamisch een lijst van beschikbare tools van een server ontvangen, samen met beschrijvingen van wat ze doen. Dit in tegenstelling tot traditionele API’s, die vaak statische codering voor integraties vereisen, wat betekent dat elke API-wijziging code-updates nodig maakt. MCP hanteert een "integreer één keer" aanpak, wat leidt tot meer aanpasbaarheid.

• **Interoperabiliteit over LLMs heen**: MCP werkt over verschillende LLMs heen en biedt flexibiliteit om kernmodellen te wisselen voor betere prestaties.

• **Gestandaardiseerde Beveiliging**: MCP bevat een standaard authenticatiemethode, wat de schaalbaarheid verbetert bij het toevoegen van toegang tot aanvullende MCP-servers. Dit is eenvoudiger dan het beheren van verschillende sleutels en authenticatietypes voor diverse traditionele API's.

### MCP Voorbeeld

![MCP Diagram](../../../translated_images/nl/mcp-diagram.e4ca1cbd551444a1.webp)

Stel je voor dat een gebruiker een vlucht wil boeken met behulp van een AI-assistent aangedreven door MCP.

1. **Verbinding**: De AI-assistent (de MCP-client) maakt verbinding met een MCP-server die door een luchtvaartmaatschappij wordt aangeboden.

2. **Tooldetectie**: De client vraagt aan de MCP-server van de luchtvaartmaatschappij: "Welke tools heb je beschikbaar?" De server antwoordt met tools zoals "vluchten zoeken" en "vluchten boeken".

3. **Tool-aanroep**: Je vraagt vervolgens aan de AI-assistent: "Zoek alsjeblieft een vlucht van Portland naar Honolulu." De AI-assistent gebruikt zijn LLM, identificeert dat het de tool "vluchten zoeken" moet aanroepen en stuurt de relevante parameters (vertrek, bestemming) naar de MCP-server.

4. **Uitvoering en Reactie**: De MCP-server, die fungeert als een tussenlaag, maakt de daadwerkelijke oproep naar de interne boekings-API van de luchtvaartmaatschappij. Daarna ontvangt het de vluchtinformatie (bijv. JSON-data) en stuurt die terug naar de AI-assistent.

5. **Verdere Interactie**: De AI-assistent presenteert de vluchtopties. Wanneer je een vlucht selecteert, kan de assistent vervolgens de "boeking vlucht" tool aanroepen op dezelfde MCP-server om de boeking te voltooien.

## Agent-to-Agent Protocol (A2A)

Terwijl MCP zich richt op het verbinden van LLMs met tools, gaat het **Agent-to-Agent (A2A) protocol** een stap verder door communicatie en samenwerking tussen verschillende AI-agenten mogelijk te maken. A2A verbindt AI-agenten over verschillende organisaties, omgevingen en technische platforms om een gedeelde taak te voltooien.

We bekijken de componenten en voordelen van A2A, samen met een voorbeeld van hoe het in onze reisapplicatie toegepast kan worden.

### Kerncomponenten van A2A

A2A richt zich op het mogelijk maken van communicatie tussen agenten en laat hen samenwerken om een subtaken van de gebruiker te voltooien. Elke component van het protocol draagt hieraan bij:

#### Agent Card

Net zoals een MCP-server een lijst van tools deelt, bevat een Agent Card:
- De Naam van de Agent.
- Een **beschrijving van de algemene taken** die het uitvoert.
- Een **lijst van specifieke vaardigheden** met beschrijvingen om andere agenten (of zelfs menselijke gebruikers) te helpen begrijpen wanneer en waarom ze die agent zouden willen aanroepen.
- De **huidige Endpoint URL** van de agent.
- De **versie** en **mogelijkheden** van de agent zoals streaming-reacties en pushmeldingen.

#### Agent Executor

De Agent Executor is verantwoordelijk voor het **doorgeven van de context van de gebruikerschat aan de externe agent**, die dit nodig heeft om de taak te begrijpen. In een A2A-server gebruikt een agent zijn eigen Large Language Model (LLM) om binnenkomende verzoeken te parseren en taken uit te voeren met zijn eigen interne tools.

#### Artifact

Zodra een externe agent de gevraagde taak heeft voltooid, wordt het resultaat als een artifact aangemaakt. Een artifact **bevat het resultaat van het werk van de agent**, een **beschrijving van wat er is voltooid**, en de **tekstuele context** die via het protocol wordt verzonden. Nadat het artifact is verzonden, wordt de verbinding met de externe agent gesloten totdat deze opnieuw nodig is.

#### Event Queue

Deze component wordt gebruikt voor **het afhandelen van updates en het doorgeven van berichten**. Dit is vooral belangrijk in productie voor agentische systemen om te voorkomen dat de verbinding tussen agenten wordt gesloten voordat een taak is voltooid, vooral wanneer taken meer tijd kunnen kosten.

### Voordelen van A2A

• **Verbeterde samenwerking**: Het maakt het mogelijk dat agenten van verschillende leveranciers en platforms met elkaar communiceren, context delen en samenwerken, wat naadloze automatisering tussen normaal gesproken afgescheiden systemen faciliteert.

• **Flexibiliteit bij modelkeuze**: Elke A2A-agent kan zelf beslissen welk LLM het gebruikt om verzoeken te verwerken, waardoor geoptimaliseerde of fijn afgestelde modellen per agent mogelijk zijn, in tegenstelling tot een enkele LLM-verbinding in sommige MCP-scenario's.

• **Geïntegreerde authenticatie**: Authenticatie is direct geïntegreerd in het A2A protocol, wat een robuust beveiligingskader voor agentinteracties biedt.

### A2A Voorbeeld

![A2A Diagram](../../../translated_images/nl/A2A-Diagram.8666928d648acc26.webp)

Laten we ons reisscenario uitbreiden, maar ditmaal gebruikmakend van A2A.

1. **Gebruikersverzoek aan Multi-Agent**: Een gebruiker interacteert met een "Travel Agent" A2A client/agent, bijvoorbeeld door te zeggen: "Boek alsjeblieft een volledige reis naar Honolulu voor volgende week, inclusief vluchten, een hotel en een huurauto".

2. **Orkestratie door Travel Agent**: De Travel Agent ontvangt dit complexe verzoek. Hij gebruikt zijn LLM om over de taak na te denken en bepaalt dat hij met andere gespecialiseerde agenten moet communiceren.

3. **Inter-Agent Communicatie**: De Travel Agent gebruikt vervolgens het A2A protocol om verbinding te maken met downstream agenten, zoals een "Airline Agent", een "Hotel Agent" en een "Car Rental Agent" die door verschillende bedrijven zijn gemaakt.

4. **Gedecentraliseerde Taakuitvoering**: De Travel Agent stuurt specifieke taken naar deze gespecialiseerde agenten (bijv. "Vind vluchten naar Honolulu", "Boek een hotel", "Huur een auto"). Elke gespecialiseerde agent, met zijn eigen LLMs en gebruikmakend van eigen tools (die zelf MCP-servers kunnen zijn), voert zijn specifieke deel van de boeking uit.

5. **Samengevoegde Reactie**: Zodra alle downstream agenten hun taken hebben afgerond, verzamelt de Travel Agent de resultaten (vluchtgegevens, hotelbevestiging, autohuurboeking) en stuurt een uitgebreide, chatstijl-reactie terug naar de gebruiker.

## Natural Language Web (NLWeb)

Websites zijn al lang de belangrijkste manier voor gebruikers om informatie en data over het internet te raadplegen.

Laten we de verschillende componenten van NLWeb bekijken, de voordelen van NLWeb en een voorbeeld van hoe onze NLWeb werkt door onze reisapplicatie te bekijken.

### Componenten van NLWeb

- **NLWeb Applicatie (Kern Service Code)**: Het systeem dat natuurlijke taalvragen verwerkt. Het verbindt de verschillende delen van het platform om antwoorden te creëren. Je kunt het zien als de **motor die de natuurlijke taal features van een website aandrijft**.

- **NLWeb Protocol**: Dit is een **basisset regels voor natuurlijke taal interactie** met een website. Het stuurt antwoorden terug in JSON-formaat (vaak gebruikmakend van Schema.org). Het doel is een eenvoudige basis te creëren voor het "AI Web," vergelijkbaar met hoe HTML het mogelijk maakte documenten online te delen.

- **MCP Server (Model Context Protocol Endpoint)**: Elke NLWeb-setup werkt ook als een **MCP server**. Dit betekent dat het **tools (zoals een “ask” methode) en data** kan delen met andere AI-systemen. In de praktijk maakt dit de inhoud en mogelijkheden van de website bruikbaar voor AI-agenten, waardoor de site deel wordt van het bredere “agent ecosysteem.”

- **Embedding Modellen**: Deze modellen worden gebruikt om **website-inhoud om te zetten in numerieke representaties genaamd vectoren** (embeddings). Deze vectoren vangen betekenis op op een manier die computers kunnen vergelijken en doorzoeken. Ze worden opgeslagen in een speciale database en gebruikers kunnen kiezen welk embedding model ze willen gebruiken.

- **Vector Database (Ophaalmechanisme)**: Deze database **slaat de embeddings van de website-inhoud op**. Wanneer iemand een vraag stelt, zoekt NLWeb in de vectordatabase snel de meest relevante informatie. Het geeft een snelle lijst mogelijke antwoorden, gerangschikt op overeenkomstigheid. NLWeb werkt met verschillende vectoropslagsystemen zoals Qdrant, Snowflake, Milvus, Azure AI Search en Elasticsearch.

### NLWeb door Voorbeeld

![NLWeb](../../../translated_images/nl/nlweb-diagram.c1e2390b310e5fe4.webp)

Neem opnieuw onze reisboekingswebsite, maar deze keer aangedreven door NLWeb.

1. **Data Inname**: De bestaande productcatalogi van de reiswebsite (bijv. vluchtlijsten, hotelbeschrijvingen, tourpakketten) zijn geformatteerd met Schema.org of geladen via RSS-feeds. De NLWeb-tools nemen deze gestructureerde data in, creëren embeddings en slaan deze op in een lokale of externe vectordatabase.

2. **Vraag in Natuurlijke Taal (Menselijk)**: Een gebruiker bezoekt de website en typt in plaats van menu’s te doorlopen in een chatinterface: "Vind een gezinsvriendelijk hotel in Honolulu met een zwembad voor volgende week".

3. **NLWeb Verwerking**: De NLWeb-applicatie ontvangt deze vraag. Het stuurt de vraag naar een LLM om het te begrijpen en zoekt tegelijkertijd in zijn vectordatabase naar relevante hotelvermeldingen.

4. **Nauwkeurige Resultaten**: De LLM helpt om de zoekresultaten uit de database te interpreteren, de beste overeenkomsten te identificeren op basis van criteria zoals "gezinsvriendelijk," "zwembad," en "Honolulu," en formatteert vervolgens een reactie in natuurlijke taal. Cruciaal is dat de reactie verwijst naar echte hotels uit de catalogus van de website, zonder verzonnen informatie.

5. **AI Agent Interactie**: Omdat NLWeb fungeert als een MCP-server, kan een externe AI-reisagent ook verbinding maken met deze NLWeb-instantie van de website. De AI-agent zou dan de `ask` MCP-methode kunnen gebruiken om de website direct te bevragen: `ask("Zijn er veganistische restaurants in de omgeving van Honolulu aanbevolen door het hotel?")`. De NLWeb-instantie zou dit verwerken, gebruikmakend van zijn database met restaurantinformatie (indien geladen), en een gestructureerde JSON-reactie retourneren.

### Meer Vragen over MCP/A2A/NLWeb?

Word lid van de [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) om andere lerenden te ontmoeten, kantooruren bij te wonen en je vragen over AI-agenten beantwoord te krijgen.

## Bronnen

- [MCP voor Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentatie](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

## Vorige Les

[AI Agents in Production](../10-ai-agents-production/README.md)

## Volgende Les

[Context Engineering voor AI Agents](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->