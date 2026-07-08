# Gebruik van Agentische Protocollen (MCP, A2A en NLWeb)

[![Agentic Protocols](../../../translated_images/nl/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

Naarmate het gebruik van AI-agenten toeneemt, groeit ook de behoefte aan protocollen die standaardisatie, beveiliging waarborgen en open innovatie ondersteunen. In deze les behandelen we 3 protocollen die in deze behoefte voorzien - Model Context Protocol (MCP), Agent to Agent (A2A) en Natural Language Web (NLWeb).

## Introductie

In deze les behandelen we:

• Hoe **MCP** AI-agenten in staat stelt externe tools en data te benaderen om gebruikersopdrachten te voltooien.

• Hoe **A2A** communicatie en samenwerking tussen verschillende AI-agenten mogelijk maakt.

• Hoe **NLWeb** natuurlijke taalinterfaces naar elke website brengt waardoor AI-agenten de inhoud kunnen ontdekken en ermee kunnen interacteren.

## Leerdoelen

• **Identificeren** van het hoofddoel en de voordelen van MCP, A2A en NLWeb in de context van AI-agenten.

• **Uitleggen** hoe elk protocol communicatie en interactie faciliteert tussen LLMs, tools en andere agenten.

• **Herkennen** van de onderscheiden rollen die elk protocol speelt bij het bouwen van complexe agentische systemen.

## Model Context Protocol

Het **Model Context Protocol (MCP)** is een open standaard die een gestandaardiseerde manier biedt voor applicaties om context en tools aan LLMs te leveren. Dit maakt een “universele adapter” mogelijk voor verschillende databronnen en tools waar AI-agenten op een consistente manier mee kunnen verbinden.

Laten we kijken naar de componenten van MCP, de voordelen ten opzichte van direct API-gebruik, en een voorbeeld van hoe AI-agenten een MCP-server zouden kunnen gebruiken.

### Kerncomponenten van MCP

MCP werkt op een **client-serverarchitectuur** en de kerncomponenten zijn:

• **Hosts** zijn LLM-applicaties (bijvoorbeeld een code-editor zoals VSCode) die de verbindingen met een MCP-server starten.

• **Clients** zijn componenten binnen de hostapplicatie die een-op-een verbindingen met servers onderhouden.

• **Servers** zijn lichte programma's die specifieke mogelijkheden aanbieden.

In het protocol zitten drie kernprimitieven die de mogelijkheden van een MCP-server vormen:

• **Tools**: Dit zijn discrete acties of functies die een AI-agent kan aanroepen om een actie uit te voeren. Bijvoorbeeld, een weerservice kan een "get weather"-tool aanbieden, of een e-commerce server kan een "purchase product"-tool aanleveren. MCP-servers adverteren elke tool met naam, beschrijving en input/output-schema in hun mogelijkhedenlijst.

• **Resources**: Dit zijn alleen-lezen data-items of documenten die een MCP-server kan aanbieden en die clients op aanvraag kunnen ophalen. Voorbeelden zijn bestandsinhoud, database-records of logbestanden. Resources kunnen tekst zijn (zoals code of JSON) of binair (zoals afbeeldingen of PDF’s).

• **Prompts**: Dit zijn vooraf gedefinieerde sjablonen die voorgestelde prompts bieden, waardoor complexere workflows mogelijk zijn.

### Voordelen van MCP

MCP biedt aanzienlijke voordelen voor AI-agenten:

• **Dynamische Toolontdekking**: Agents kunnen dynamisch een lijst ontvangen van beschikbare tools van een server samen met beschrijvingen van hun functies. Dit in tegenstelling tot traditionele API’s die vaak statische codering voor integraties vereisen, wat betekent dat elke API-wijziging code-updates vereist. MCP biedt een “integreer één keer”-benadering, wat leidt tot grotere aanpasbaarheid.

• **Interoperabiliteit tussen LLMs**: MCP werkt met verschillende LLMs, wat flexibiliteit biedt om kernmodellen te wisselen voor betere prestaties.

• **Gestandaardiseerde Beveiliging**: MCP bevat een standaard authenticatiemethode, wat de schaalbaarheid verbetert bij het toevoegen van toegang tot extra MCP-servers. Dit is eenvoudiger dan het beheren van verschillende sleutels en authenticatietypes voor diverse traditionele API’s.

### MCP Voorbeeld

![MCP Diagram](../../../translated_images/nl/mcp-diagram.e4ca1cbd551444a1.webp)

Stel je voor dat een gebruiker een vlucht wil boeken met een AI-assistent die MCP gebruikt.

1. **Verbinden**: De AI-assistent (de MCP-client) maakt verbinding met een MCP-server van een luchtvaartmaatschappij.

2. **Toolontdekking**: De client vraagt aan de MCP-server van de luchtvaartmaatschappij: “Welke tools zijn er beschikbaar?” De server reageert met tools zoals “search flights” en “book flights”.

3. **Tool-aanroep**: Je vraagt de AI-assistent: “Zoek een vlucht van Portland naar Honolulu.” De AI-assistent gebruikt zijn LLM om te identificeren dat het de tool “search flights” moet aanroepen en geeft de relevante parameters (vertrek en bestemming) door aan de MCP-server.

4. **Uitvoering en Reactie**: De MCP-server, die als wrapper fungeert, maakt de daadwerkelijke aanroep naar de interne boekings-API van de luchtvaartmaatschappij. Vervolgens ontvangt het de vluchtinformatie (bijvoorbeeld JSON-data) en geeft dat terug aan de AI-assistent.

5. **Verdere Interactie**: De AI-assistent toont de vluchtopties. Zodra je een vlucht selecteert, kan de assistent de tool “book flight” aanroepen op dezelfde MCP-server om de boeking af te ronden.

## Agent-to-Agent Protocol (A2A)

Terwijl MCP gericht is op het verbinden van LLMs met tools, gaat het **Agent-to-Agent (A2A) protocol** een stap verder door communicatie en samenwerking tussen verschillende AI-agenten mogelijk te maken. A2A verbindt AI-agenten van verschillende organisaties, omgevingen en technologiestacks om een gezamenlijke taak te voltooien.

We bekijken de componenten en voordelen van A2A, samen met een voorbeeld van hoe dit toegepast zou kunnen worden in onze reisapplicatie.

### Kerncomponenten van A2A

A2A richt zich op het mogelijk maken van communicatie tussen agenten en hen samen taken te laten voltooien. Elke component van het protocol draagt hieraan bij:

#### Agent Card

Net zoals een MCP-server een lijst met tools deelt, bevat een Agent Card:
- De naam van de agent.
- Een **beschrijving van de algemene taken** die hij uitvoert.
- Een **lijst van specifieke vaardigheden** met beschrijvingen om andere agenten (of zelfs menselijke gebruikers) te helpen begrijpen wanneer en waarom ze die agent zouden willen aanroepen.
- De **huidige Endpoint-URL** van de agent.
- De **versie** en **mogelijkheden** van de agent, zoals streaming van responsen en pushnotificaties.

#### Agent Executor

De Agent Executor is verantwoordelijk voor het **doorgeven van de context van de gebruikerschat aan de externe agent**, die deze nodig heeft om de taak te begrijpen. In een A2A-server gebruikt een agent zijn eigen Large Language Model (LLM) om binnenkomende verzoeken te verwerken en taken uit te voeren met zijn eigen interne tools.

#### Artifact

Zodra een externe agent de gevraagde taak heeft afgerond, wordt het werkproduct gecreëerd als een artifact. Een artifact **bevat het resultaat van het werk van de agent**, een **beschrijving van wat is voltooid**, en de **tekstuele context** die via het protocol wordt verzonden. Nadat het artifact is verzonden, wordt de verbinding met de externe agent gesloten tot het opnieuw nodig is.

#### Event Queue

Deze component wordt gebruikt voor **het afhandelen van updates en het doorgeven van berichten**. Dit is vooral belangrijk in productieomgevingen van agentische systemen om te voorkomen dat de verbinding tussen agenten wordt gesloten voordat een taak is voltooid, vooral wanneer de voltooiingstijd van taken langer kan duren.

### Voordelen van A2A

• **Versterkte Samenwerking**: Het maakt het mogelijk dat agenten van verschillende leveranciers en platforms communiceren, context delen en samenwerken, wat naadloze automatisering mogelijk maakt over traditioneel gescheiden systemen.

• **Flexibiliteit in Modelkeuze**: Elke A2A-agent kan zelf bepalen welke LLM hij gebruikt om zijn verzoeken te bedienen, waardoor geoptimaliseerde of fijn afgestelde modellen per agent mogelijk zijn, in tegenstelling tot een enkele LLM-verbinding in sommige MCP-scenario’s.

• **Ingebouwde Authenticatie**: Authenticatie is direct geïntegreerd in het A2A-protocol, wat een robuust securityframework biedt voor agentinteracties.

### A2A Voorbeeld

![A2A Diagram](../../../translated_images/nl/A2A-Diagram.8666928d648acc26.webp)

Laten we ons scenario voor reisboeking uitbreiden, maar deze keer gebruiken we A2A.

1. **Gebruikersverzoek aan Multi-Agent**: Een gebruiker communiceert met een "Travel Agent" A2A client/agent, bijvoorbeeld door te zeggen: "Boek alsjeblieft een hele reis naar Honolulu voor volgende week, inclusief vluchten, een hotel en een huurauto."

2. **Orkestratie door Travel Agent**: De Travel Agent ontvangt dit complexe verzoek. Hij gebruikt zijn LLM om over de taak na te denken en bepaalt dat hij moet communiceren met andere gespecialiseerde agenten.

3. **Inter-Agent Communicatie**: De Travel Agent gebruikt vervolgens het A2A-protocol om verbinding te maken met onderliggende agenten, zoals een "Airline Agent," een "Hotel Agent," en een "Car Rental Agent" van verschillende bedrijven.

4. **Gedecentraliseerde Taakuitvoering**: De Travel Agent stuurt specifieke taken naar deze gespecialiseerde agenten (bijv. "Vind vluchten naar Honolulu," "Boek een hotel," "Huur een auto"). Elk van deze gespecialiseerde agenten, draaiend met hun eigen LLMs en gebruikmakend van hun eigen tools (die zelf MCP-servers kunnen zijn), voert zijn specifieke deel van de boeking uit.

5. **Geconsolideerde Reactie**: Zodra alle onderliggende agenten hun taken hebben voltooid, brengt de Travel Agent de resultaten samen (vluchtgegevens, hotelbevestiging, autohuurreservering) en stuurt een uitgebreide chatstijl-reactie terug naar de gebruiker.

## Natural Language Web (NLWeb)

Websites zijn al lang de primaire manier voor gebruikers om informatie en data op het internet te benaderen.

Laten we de verschillende componenten van NLWeb bekijken, de voordelen van NLWeb en een voorbeeld hoe onze NLWeb werkt met onze reisapplicatie.

### Componenten van NLWeb

- **NLWeb Applicatie (Core Service Code)**: Het systeem dat natuurlijke taalvragen verwerkt. Het verbindt de verschillende delen van het platform om reacties te creëren. Je kunt het zien als de **motor die de natuurlijke taal-functies van een website aandrijft**.

- **NLWeb Protocol**: Dit is een **basisset regels voor natuurlijke taalinteractie** met een website. Het verzendt antwoorden in JSON-formaat (vaak gebruikmakend van Schema.org). Het doel is een eenvoudige basis te creëren voor het “AI Web,” net zoals HTML het delen van documenten online mogelijk maakte.

- **MCP Server (Model Context Protocol Endpoint)**: Elke NLWeb-opzet werkt ook als een **MCP-server**. Dit betekent dat het **tools (zoals een “ask”-methode) en data** kan delen met andere AI-systemen. In de praktijk maakt dit de inhoud en mogelijkheden van de website bruikbaar voor AI-agenten, waardoor de site onderdeel wordt van het bredere “agent-ecosysteem.”

- **Embedding Modellen**: Deze modellen worden gebruikt om **website-inhoud om te zetten in numerieke representaties die vectors worden genoemd** (embeddings). Deze vectors leggen betekenis vast op een manier die computers kunnen vergelijken en doorzoeken. Ze worden opgeslagen in een speciale database, en gebruikers kunnen kiezen welk embeddingmodel ze willen gebruiken.

- **Vector Database (Ophaalmechanisme)**: Deze database **slaat de embeddings van de website-inhoud op**. Wanneer iemand een vraag stelt, controleert NLWeb de vectordatabase om snel de meest relevante informatie te vinden. Het geeft een snelle lijst mogelijke antwoorden, gerangschikt op gelijkenis. NLWeb werkt met verschillende vectoropslagsystemen zoals Qdrant, Snowflake, Milvus, Azure AI Search en Elasticsearch.

### NLWeb aan de hand van een voorbeeld

![NLWeb](../../../translated_images/nl/nlweb-diagram.c1e2390b310e5fe4.webp)

Beschouw opnieuw onze reisboekingswebsite, maar deze keer aangedreven door NLWeb.

1. **Dataverwerking**: De bestaande productcatalogi van de reiswebsite (bijv. vluchtlijsten, hotelbeschrijvingen, tourpakketten) worden geformatteerd met Schema.org of geladen via RSS-feeds. De tools van NLWeb nemen deze gestructureerde data op, creëren embeddings en slaan ze op in een lokale of externe vectordatabase.

2. **Natuurlijke Taalvraag (Mens)**: Een gebruiker bezoekt de website en typt in een chatinterface: "Vind een gezinvriendelijk hotel in Honolulu met een zwembad voor volgende week."

3. **NLWeb Verwerking**: De NLWeb-applicatie ontvangt deze vraag. Het stuurt de vraag naar een LLM voor begrip en zoekt tegelijk in zijn vectordatabase naar relevante hotelvermeldingen.

4. **Nauwkeurige Resultaten**: De LLM helpt de zoekresultaten uit de database interpreteren, identificeert de beste overeenkomsten op basis van de criteria "gezinvriendelijk," "zwembad," en "Honolulu," en formatteert vervolgens een antwoord in natuurlijke taal. Cruciaal is dat het antwoord verwijst naar echte hotels uit de productcatalogus van de website, en geen gefantaseerde informatie bevat.

5. **Interactie met AI-agent**: Omdat NLWeb fungeert als een MCP-server, zou een externe AI-reisagent ook verbinding kunnen maken met deze NLWeb-instantie van de website. De AI-agent kan dan de `ask` MCP-methode gebruiken om de website direct te raadplegen: `ask("Zijn er veganistische restaurants in de buurt van Honolulu aanbevolen door het hotel?")`. De NLWeb-instantie verwerkt dit, maakt gebruik van zijn database met restaurantinformatie (indien geladen), en stuurt een gestructureerde JSON-reactie terug.

### Meer vragen over MCP/A2A/NLWeb?

Sluit je aan bij de [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) om andere lerenden te ontmoeten, deel te nemen aan office hours en je vragen over AI-agenten beantwoord te krijgen.

## Bronnen

- [MCP voor Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentatie](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->