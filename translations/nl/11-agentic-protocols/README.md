# Agentische protocollen gebruiken (MCP, A2A en NLWeb)

[![Agentische protocollen](../../../translated_images/nl/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klik op de bovenstaande afbeelding om de video van deze les te bekijken)_

Naarmate het gebruik van AI-agents toeneemt, groeit ook de behoefte aan protocollen die standaardisatie, beveiliging en open innovatie ondersteunen. In deze les behandelen we drie protocollen die aan deze behoefte proberen te voldoen - Model Context Protocol (MCP), Agent to Agent (A2A) en Natural Language Web (NLWeb).

## Inleiding

In deze les behandelen we:

• Hoe **MCP** AI-agents in staat stelt externe tools en gegevens te benaderen om gebruikerstaken te voltooien.

• Hoe **A2A** communicatie en samenwerking tussen verschillende AI-agents mogelijk maakt.

• Hoe **NLWeb** natuurlijke taalinterfaces naar elke website brengt, waardoor AI-agents de inhoud kunnen ontdekken en ermee kunnen interageren.

## Leerdoelen

• **Identificeer** het hoofddoel en de voordelen van MCP, A2A en NLWeb in de context van AI-agents.

• **Leg uit** hoe elk protocol communicatie en interactie tussen LLM's, tools en andere agents faciliteert.

• **Herken** de verschillende rollen die elk protocol speelt bij het bouwen van complexe agentische systemen.

## Model Context Protocol

Het **Model Context Protocol (MCP)** is een open standaard die een gestandaardiseerde manier biedt voor applicaties om context en tools aan LLM's te leveren. Dit maakt een "universele adapter" mogelijk voor verschillende databronnen en tools waar AI-agents op een consistente manier mee kunnen verbinden.

Laten we kijken naar de componenten van MCP, de voordelen vergeleken met direct API-gebruik, en een voorbeeld van hoe AI-agents een MCP-server kunnen gebruiken.

### MCP Kerncomponenten

MCP werkt op een **client-serverarchitectuur** en de kerncomponenten zijn:

• **Hosts** zijn LLM-toepassingen (bijvoorbeeld een code-editor zoals VSCode) die de verbindingen met een MCP-server starten.

• **Clients** zijn componenten binnen de hostapplicatie die één-op-één verbindingen met servers onderhouden.

• **Servers** zijn lichtgewicht programma's die specifieke mogelijkheden blootstellen.

In het protocol zijn drie kernprimitieven opgenomen die de mogelijkheden van een MCP-server vormen:

• **Tools**: Dit zijn discrete acties of functies die een AI-agent kan aanroepen om een handeling uit te voeren. Bijvoorbeeld, een weerservice kan een "get weather"-tool aanbieden, of een e-commerce server kan een "purchase product"-tool aanbieden. MCP-servers adverteren de naam, beschrijving en input/output-schema van elke tool in hun capabilities-overzicht.

• **Resources**: Dit zijn alleen-lezen gegevensitems of documenten die een MCP-server kan leveren, en die clients op aanvraag kunnen ophalen. Voorbeelden zijn bestandsinhoud, databaserecords of logbestanden. Resources kunnen tekst zijn (zoals code of JSON) of binair (zoals afbeeldingen of PDF's).

• **Prompts**: Dit zijn vooraf gedefinieerde sjablonen die suggestieve prompts bieden en complexere workflows mogelijk maken.

### Voordelen van MCP

MCP biedt belangrijke voordelen voor AI-agents:

• **Dynamische Tool-ontdekking**: Agents kunnen dynamisch een lijst van beschikbare tools van een server ontvangen, samen met beschrijvingen van wat ze doen. Dit staat tegenover traditionele API's, die vaak statische codering voor integraties vereisen, wat betekent dat elke API-wijziging code-updates noodzakelijk maakt. MCP biedt een "één keer integreren"-aanpak, wat leidt tot grotere aanpasbaarheid.

• **Interoperabiliteit tussen LLM's**: MCP werkt met verschillende LLM's, wat flexibiliteit biedt om kernmodellen te wisselen om betere prestaties te evalueren.

• **Gestandaardiseerde beveiliging**: MCP bevat een standaard authenticatiemethode, wat de schaalbaarheid verbetert bij het toevoegen van toegang tot extra MCP-servers. Dit is eenvoudiger dan het beheren van verschillende sleutels en authenticatietypen voor diverse traditionele API's.

### MCP Voorbeeld

![MCP-diagram](../../../translated_images/nl/mcp-diagram.e4ca1cbd551444a1.webp)

Stel je voor dat een gebruiker een vlucht wil boeken met een AI-assistent die op MCP is gebaseerd.

1. **Verbinding**: De AI-assistent (de MCP-client) maakt verbinding met een MCP-server die door een luchtvaartmaatschappij wordt aangeboden.

2. **Tool-ontdekking**: De client vraagt de MCP-server van de luchtvaartmaatschappij: "Welke tools hebben jullie beschikbaar?" De server reageert met tools zoals "search flights" en "book flights".

3. **Tool-aanroep**: Je vraagt de AI-assistent: "Zoek alsjeblieft een vlucht van Portland naar Honolulu." De AI-assistent, gebruikmakend van zijn LLM, identificeert dat hij de "search flights"-tool moet aanroepen en geeft de relevante parameters (oorsprong, bestemming) door aan de MCP-server.

4. **Uitvoering en Antwoord**: De MCP-server, opererend als een wrapper, maakt de daadwerkelijke aanroep naar de interne boekings-API van de luchtvaartmaatschappij. Vervolgens ontvangt hij de vluchtinformatie (bijv. JSON-gegevens) en stuurt deze terug naar de AI-assistent.

5. **Verdere Interactie**: De AI-assistent presenteert de vluchtopties. Zodra je een vlucht selecteert, kan de assistent de "book flight"-tool op dezelfde MCP-server aanroepen om de boeking te voltooien.

## Agent-to-Agent Protocol (A2A)

Terwijl MCP zich richt op het verbinden van LLM's met tools, gaat het **Agent-to-Agent (A2A) protocol** een stap verder door communicatie en samenwerking tussen verschillende AI-agents mogelijk te maken. A2A verbindt AI-agents over verschillende organisaties, omgevingen en technologische stacks om samen een gedeelde taak te voltooien.

We bekijken de componenten en voordelen van A2A, samen met een voorbeeld van hoe het toegepast kan worden in onze reisapplicatie.

### A2A Kerncomponenten

A2A richt zich op het mogelijk maken van communicatie tussen agents en het laten samenwerken om een subtaken van de gebruiker te voltooien. Elk onderdeel van het protocol draagt hieraan bij:

#### Agent Card

Vergelijkbaar met hoe een MCP-server een lijst van tools deelt, heeft een Agent Card:
- De naam van de agent.
- Een **beschrijving van de algemene taken** die hij uitvoert.
- Een **lijst van specifieke vaardigheden** met beschrijvingen om andere agents (of zelfs menselijke gebruikers) te helpen begrijpen wanneer en waarom ze die agent zouden aanroepen.
- De **huidige Endpoint-URL** van de agent.
- De **versie** en **mogelijkheden** van de agent, zoals streaming responses en pushnotificaties.

#### Agent Executor

De Agent Executor is verantwoordelijk voor het **doorgeven van de context van de gebruikerschat aan de externe agent**, de externe agent heeft dit nodig om de taak te begrijpen die voltooid moet worden. In een A2A-server gebruikt een agent zijn eigen Large Language Model (LLM) om binnenkomende verzoeken te ontleden en taken uit te voeren met zijn eigen interne tools.

#### Artifact

Zodra een externe agent de gevraagde taak heeft voltooid, wordt het werkproduct gemaakt als een artifact. Een artifact **bevat het resultaat van het werk van de agent**, een **beschrijving van wat is voltooid**, en de **tekstuele context** die via het protocol is verzonden. Nadat het artifact is verzonden, wordt de verbinding met de externe agent gesloten totdat deze weer nodig is.

#### Event Queue

Deze component wordt gebruikt voor **het afhandelen van updates en het doorgeven van berichten**. Het is vooral belangrijk in productie voor agentische systemen om te voorkomen dat de verbinding tussen agents wordt gesloten voordat een taak is voltooid, vooral wanneer het voltooien van taken langere tijd kan duren.

### Voordelen van A2A

• **Verbeterde samenwerking**: Het stelt agents van verschillende leveranciers en platforms in staat om te interageren, context te delen en samen te werken, waardoor naadloze automatisering over traditioneel gescheiden systemen mogelijk wordt.

• **Flexibiliteit in modelselectie**: Elke A2A-agent kan beslissen welk LLM hij gebruikt om zijn verzoeken te bedienen, waardoor geoptimaliseerde of fijn afgestelde modellen per agent mogelijk zijn, in tegenstelling tot één enkele LLM-verbinding in sommige MCP-scenario's.

• **Ingebouwde authenticatie**: Authenticatie is direct in het A2A-protocol geïntegreerd, wat een robuust beveiligingskader voor agentinteracties biedt.

### A2A Voorbeeld

![A2A-diagram](../../../translated_images/nl/A2A-Diagram.8666928d648acc26.webp)

Laten we ons reisboekingsscenario uitbreiden, maar deze keer met A2A.

1. **Gebruikersverzoek aan Multi-Agent**: Een gebruiker interageert met een "Travel Agent" A2A-client/agent, bijvoorbeeld door te zeggen: "Boek alsjeblieft een gehele reis naar Honolulu voor volgende week, inclusief vluchten, een hotel en een huurauto".

2. **Orkestratie door Travel Agent**: De Travel Agent ontvangt dit complexe verzoek. Hij gebruikt zijn LLM om over de taak te redeneren en bepaalt dat hij met andere gespecialiseerde agents moet samenwerken.

3. **Inter-agent Communicatie**: De Travel Agent gebruikt vervolgens het A2A-protocol om verbinding te maken met downstream agents, zoals een "Airline Agent", een "Hotel Agent" en een "Car Rental Agent" die door verschillende bedrijven zijn gemaakt.

4. **Gedecentraliseerde Taakuitvoering**: De Travel Agent stuurt specifieke taken naar deze gespecialiseerde agents (bijv. "Find flights to Honolulu", "Book a hotel", "Rent a car"). Elk van deze gespecialiseerde agents, die hun eigen LLM's draaien en hun eigen tools gebruiken (die zelf MCP-servers kunnen zijn), voert zijn specifieke deel van de boeking uit.

5. **Geconsolideerd Antwoord**: Zodra alle downstream agents hun taken hebben voltooid, verzamelt de Travel Agent de resultaten (vluchtgegevens, hotelbevestiging, autohuurboeking) en stuurt een uitgebreid, chatstijlantwoord terug naar de gebruiker.

## Natural Language Web (NLWeb)

Websites zijn al lange tijd de primaire manier voor gebruikers om informatie en data op internet te benaderen.

Laten we kijken naar de verschillende componenten van NLWeb, de voordelen van NLWeb en een voorbeeld van hoe onze NLWeb werkt door naar onze reisapplicatie te kijken.

### Componenten van NLWeb

- **NLWeb-toepassing (kernservicedcode)**: Het systeem dat natuurlijke taalvragen verwerkt. Het verbindt de verschillende delen van het platform om antwoorden te creëren. Je kunt het zien als de **motor die de natuurlijke taalfunctionaliteit** van een website aandrijft.

- **NLWeb-protocol**: Dit is een **basisset regels voor natuurlijke taalinteractie** met een website. Het stuurt antwoorden terug in JSON-formaat (vaak met Schema.org). Het doel is om een eenvoudige basis te creëren voor het "AI-web", op dezelfde manier waarop HTML het mogelijk maakte documenten online te delen.

- **MCP-server (Model Context Protocol Endpoint)**: Elke NLWeb-configuratie fungeert ook als een **MCP-server**. Dit betekent dat het **tools (zoals een “ask”-methode) en data** kan delen met andere AI-systemen. In de praktijk maakt dit de inhoud en mogelijkheden van de website bruikbaar voor AI-agents, waardoor de site deel wordt van het bredere "agent-ecosysteem".

- **Embedding-modellen**: Deze modellen worden gebruikt om **website-inhoud om te zetten in numerieke representaties die vectors (embeddings) worden genoemd**. Deze vectors vangen betekenis op een manier waarop computers kunnen vergelijken en doorzoeken. Ze worden opgeslagen in een speciale database, en gebruikers kunnen kiezen welk embedding-model ze willen gebruiken.

- **Vector-database (ophaalmechanisme)**: Deze database **slaat de embeddings van de website-inhoud op**. Wanneer iemand een vraag stelt, controleert NLWeb de vectordatabase om snel de meest relevante informatie te vinden. Het geeft een snelle lijst met mogelijke antwoorden, gerangschikt op overeenstemming. NLWeb werkt met verschillende vectoropslagsystemen zoals Qdrant, Snowflake, Milvus, Azure AI Search en Elasticsearch.

### NLWeb aan de hand van een voorbeeld

![NLWeb](../../../translated_images/nl/nlweb-diagram.c1e2390b310e5fe4.webp)

Beschouw opnieuw onze reisboekingswebsite, maar deze keer aangedreven door NLWeb.

1. **Gegevensinvoer**: De bestaande productcatalogi van de reiswebsite (bijv. vluchtlijsten, hotelbeschrijvingen, reisaanbiedingen) worden geformatteerd met Schema.org of geladen via RSS-feeds. De tools van NLWeb nemen deze gestructureerde gegevens op, maken embeddings en slaan ze op in een lokale of externe vectordatabase.

2. **Natuurlijke Taalvraag (mens)**: Een gebruiker bezoekt de website en typt in plaats van door menu's te navigeren in een chatinterface: "Vind een gezinsvriendelijk hotel in Honolulu met een zwembad voor volgende week".

3. **NLWeb-verwerking**: De NLWeb-toepassing ontvangt deze vraag. Hij stuurt de vraag naar een LLM voor begrip en zoekt tegelijkertijd in zijn vectordatabase naar relevante hotelvermeldingen.

4. **Nauwkeurige resultaten**: De LLM helpt bij het interpreteren van de zoekresultaten uit de database, identificeert de beste overeenkomsten op basis van de criteria "gezinsvriendelijk", "zwembad" en "Honolulu", en formatteert vervolgens een antwoord in natuurlijke taal. Cruciaal is dat het antwoord verwijst naar daadwerkelijke hotels uit de catalogus van de website, waardoor verzonnen informatie wordt vermeden.

5. **AI-agentinteractie**: Omdat NLWeb fungeert als een MCP-server, kan een externe AI-reisagent ook verbinding maken met deze NLWeb-instance van de website. De AI-agent zou dan de `ask("Are there any vegan-friendly restaurants in the Honolulu area recommended by the hotel?")` MCP-methode kunnen gebruiken om de site direct te bevragen. De NLWeb-instance zou dit verwerken, gebruikmakend van zijn database met restaurantinformatie (indien geladen), en een gestructureerd JSON-antwoord retourneren.

### Nog meer vragen over MCP/A2A/NLWeb?

Word lid van de [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) om andere leerlingen te ontmoeten, deel te nemen aan spreekuren en je vragen over AI-agents beantwoord te krijgen.

## Bronnen

- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we naar nauwkeurigheid streven, houd er rekening mee dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal dient als de gezaghebbende bron. Voor kritieke informatie wordt een professionele menselijke vertaling aangeraden. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->