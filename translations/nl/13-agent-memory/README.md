# Geheugen voor AI Agents  
[![Agent Memory](../../../translated_images/nl/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Wanneer we de unieke voordelen van het creëren van AI Agents bespreken, worden vooral twee dingen besproken: de mogelijkheid om tools aan te roepen om taken te voltooien en het vermogen om in de loop van de tijd te verbeteren. Geheugen vormt de basis voor het creëren van zelfverbeterende agents die betere ervaringen kunnen bieden aan onze gebruikers.

In deze les bekijken we wat geheugen is voor AI Agents en hoe we dit kunnen beheren en gebruiken ten voordele van onze applicaties.

## Introductie

Deze les behandelt:

• **Begrip van AI Agent Geheugen**: Wat geheugen is en waarom het essentieel is voor agents.

• **Implementatie en Opslag van Geheugen**: Praktische methoden om geheugenfunctionaliteit aan je AI agents toe te voegen, met focus op werkgeheugen en langetermijngeheugen.

• **AI Agents Zelfverbeterend Maken**: Hoe geheugen agents in staat stelt te leren van eerdere interacties en in de loop van tijd te verbeteren.

## Beschikbare Implementaties

Deze les bevat twee uitgebreide notebook tutorials:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementeert geheugen met Mem0 en Azure AI Search binnen Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementeert gestructureerd geheugen met Cognee, dat automatisch een kennisgrafiek bouwt op basis van embeddings, de grafiek visualiseert en intelligente retrieval mogelijk maakt

## Leerdoelen

Na het voltooien van deze les weet je hoe je:

• **Verschillende typen AI agent geheugen onderscheidt**, inclusief werkend geheugen, kortetermijngeheugen en langetermijngeheugen, evenals gespecialiseerde vormen zoals persona en episodisch geheugen.

• **Werkgeheugen en langetermijngeheugen voor AI agents implementeert en beheert** met Microsoft Agent Framework, gebruikmakend van tools als Mem0, Cognee, Whiteboard geheugen, en integratie met Azure AI Search.

• **De principes achter zelfverbeterende AI agents begrijpt** en hoe robuuste geheugenbeheer systemen bijdragen aan continue leren en aanpassing.

## Begrip van AI Agent Geheugen

In essentie verwijst **geheugen voor AI agents naar de mechanismen die ze in staat stellen om informatie te bewaren en terug te halen**. Deze informatie kan specifieke details over een gesprek zijn, gebruikersvoorkeuren, eerdere acties of zelfs aangeleerde patronen.

Zonder geheugen zijn AI-toepassingen vaak stateless, wat betekent dat elke interactie vanaf nul begint. Dit leidt tot een repetitieve en frustrerende gebruikerservaring waarbij de agent eerdere context of voorkeuren "vergeet".

### Waarom is geheugen belangrijk?

De intelligentie van een agent is sterk verbonden met het vermogen om eerdere informatie te herinneren en te benutten. Geheugen maakt agents:

• **Reflectief**: Leren van eerdere acties en uitkomsten.

• **Interactief**: Context behouden gedurende een lopend gesprek.

• **Proactief en Reactief**: Behoeften anticiperen of passend reageren op basis van historische gegevens.

• **Autonoom**: Zelfstandiger functioneren door terug te grijpen op opgeslagen kennis.

Het doel van het implementeren van geheugen is om agents betrouwbaarder en capabeler te maken.

### Typen geheugen

#### Werkgeheugen

Zie dit als een stuk kladpapier dat een agent gebruikt tijdens een enkele, doorlopende taak of denkproces. Het bevat directe informatie die nodig is om de volgende stap te berekenen.

Voor AI agents vangt werkgeheugen vaak de meest relevante informatie uit een gesprek op, zelfs als de volledige chatgeschiedenis lang of ingekort is. Het richt zich op het extraheren van kernpunten zoals vereisten, voorstellen, beslissingen en acties.

**Voorbeeld Werkgeheugen**

In een reisboekingsagent kan werkgeheugen de huidige aanvraag van de gebruiker bevatten, zoals "Ik wil een reis naar Parijs boeken". Dit specifieke verzoek wordt in de directe context van de agent vastgehouden om de huidige interactie te sturen.

#### Kortetermijngeheugen

Dit type geheugen bewaart informatie voor de duur van één gesprek of sessie. Het is de context van het huidige chatproces, waardoor de agent kan terugverwijzen naar eerdere beurtwisselingen in de dialoog.

In de [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK voorbeelden komt dit overeen met `AgentSession`, gemaakt met `agent.create_session()`. De sessie is het ingebouwde kortetermijngeheugen van het framework: het houdt gesprekcontext beschikbaar zolang dezelfde sessie wordt hergebruikt, maar die context wordt niet bewaard als de sessie eindigt of de applicatie herstart. Gebruik langetermijngeheugen voor feiten en voorkeuren die sessieoverschrijdend bewaard moeten blijven, meestal via een database, vectorindex of een andere duurzame opslag.

**Voorbeeld Kortetermijngeheugen**

Als een gebruiker vraagt: "Hoeveel kost een vlucht naar Parijs?" en daarna volgt met "En wat dacht je van accommodatie daar?", zorgt kortetermijngeheugen ervoor dat de agent weet dat "daar" verwijst naar "Parijs" binnen hetzelfde gesprek.

#### Langetermijngeheugen

Dit is informatie die behouden blijft over meerdere gesprekken of sessies heen. Het stelt agents in staat gebruikersvoorkeuren, historische interacties of algemene kennis over langere periodes te onthouden. Dit is belangrijk voor personalisatie.

**Voorbeeld Langetermijngeheugen**

Een langetermijngeheugen kan opslaan dat "Ben houdt van skiën en outdooractiviteiten, houdt van koffie met bergzicht en wil geavanceerde skipistes vermijden vanwege een eerdere blessure". Deze informatie, geleerd uit eerdere interacties, beïnvloedt aanbevelingen in toekomstige reisplanningssessies, wat ze sterk personaliseert.

#### Persona Geheugen

Dit gespecialiseerde type geheugen helpt een agent een consistente "persoonlijkheid" of "persona" te ontwikkelen. Het stelt de agent in staat details over zichzelf of haar rol te onthouden, waardoor interacties vloeiender en gerichter worden.

**Voorbeeld Persona Geheugen**  
Als de reisagent is ontworpen als een "expert ski-planner", kan persona geheugen deze rol versterken en de antwoorden laten aansluiten bij de toon en kennis van een expert.

#### Workflow/Episodisch Geheugen

Dit geheugen slaat de reeks stappen op die een agent tijdens een complexe taak onderneemt, inclusief successen en mislukkingen. Het is alsof het "episodes" of eerdere ervaringen onthoudt om daarvan te leren.

**Voorbeeld Episodisch Geheugen**

Als de agent probeerde een specifieke vlucht te boeken, maar dat mislukte wegens niet-beschikbaarheid, kan episodisch geheugen deze mislukking vastleggen. Dit stelt de agent in staat alternatieve vluchten te proberen of de gebruiker beter te informeren over het probleem bij een volgende poging.

#### Entiteit Geheugen

Dit betreft het extraheren en onthouden van specifieke entiteiten (zoals personen, plaatsen of zaken) en gebeurtenissen uit gesprekken. Het stelt de agent in staat een gestructureerd begrip op te bouwen van belangrijke besproken elementen.

**Voorbeeld Entiteit Geheugen**

Uit een gesprek over een vorige reis zou de agent "Parijs," "Eiffeltoren," en "diner bij restaurant Le Chat Noir" kunnen extraheren als entiteiten. Bij een volgende interactie kan de agent "Le Chat Noir" herinneren en aanbieden daar een nieuwe reservering te maken.

#### Gestructureerd RAG (Retrieval Augmented Generation)

Hoewel RAG een bredere techniek is, wordt "Gestructureerd RAG" benoemd als een krachtige geheugentechnologie. Het extraheert dichte, gestructureerde informatie uit diverse bronnen (gesprekken, e-mails, afbeeldingen) en gebruikt dit om precisie, recall en snelheid in antwoorden te verbeteren. In tegenstelling tot klassieke RAG die uitsluitend op semantische gelijkenis steunt, werkt Gestructureerd RAG met de inherente structuur van informatie.

**Voorbeeld Gestructureerd RAG**

In plaats van alleen trefwoorden te matchen, kan Gestructureerd RAG vluchtdetails (bestemming, datum, tijd, luchtvaartmaatschappij) uit een e-mail parsen en gestructureerd opslaan. Hierdoor zijn precieze vragen mogelijk zoals "Welke vlucht heb ik dinsdag naar Parijs geboekt?"

## Implementatie en Opslag van Geheugen

Het implementeren van geheugen voor AI agents omvat een systematisch proces van **geheugenbeheer**, dat genereren, opslaan, ophalen, integreren, bijwerken en zelfs "vergeten" (of verwijderen) van informatie inhoudt. Retrieval is een bijzonder cruciaal aspect.

### Gespecialiseerde Geheugentools

#### Mem0

Een manier om agentgeheugen te bewaren en beheren is via gespecialiseerde tools zoals Mem0. Mem0 fungeert als een persistent geheugenniveau, waardoor agents relevante interacties kunnen herinneren, gebruikersvoorkeuren en feitelijke context kunnen opslaan en leren van successen en mislukkingen in de loop van tijd. Het idee is dat stateless agents veranderen in stateful agents.

Het werkt via een **twee-fasen geheugenpijplijn: extractie en update**. Eerst worden berichten die aan een agentthread worden toegevoegd, naar de Mem0-service gestuurd, die met een Large Language Model (LLM) de gesprekgeschiedenis samenvat en nieuwe herinneringen extraheert. Daarna bepaalt een LLM-gestuurde updatefase of deze herinneringen moeten worden toegevoegd, gewijzigd of verwijderd en slaat ze op in een hybride datastore die vector-, grafen- en key-value databases kan omvatten. Dit systeem ondersteunt ook verschillende geheugentypen en kan grafengeheugen integreren om relaties tussen entiteiten te beheren.

#### Cognee

Een andere krachtige benadering is het gebruik van **Cognee**, een open-source semantisch geheugen voor AI agents dat gestructureerde en ongestructureerde data omzet in bevraagbare kennisgrafieken ondersteund door embeddings. Cognee biedt een **dual-store architectuur** die vectorgelijkeniszoeken combineert met grafrelaties, zodat agents niet alleen begrijpen welke informatie vergelijkbaar is, maar ook hoe concepten met elkaar verbonden zijn.

Het blinkt uit in **hybride retrieval** die vector gelijkenis, grafstructuur en LLM-redenering mengt – van ruwe chunk lookup tot grafbewuste vraagbeantwoording. Het systeem onderhoudt **levend geheugen** dat evolueert en groeit terwijl het bevraagbaar blijft als één verbonden grafiek, met ondersteuning voor zowel kortetermijnsessiecontext als langetermijnpersistent geheugen.

De Cognee notebook tutorial ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) toont het bouwen van deze verenigde geheugenlaag, met praktische voorbeelden van het inladen van diverse datasources, het visualiseren van de kennisgrafiek en queryen met verschillende zoekstrategieën afgestemd op specifieke agentbehoeften.

### Geheugen Opslaan met RAG

Naast gespecialiseerde geheugentools zoals Mem0, kun je robuuste zoekdiensten als **Azure AI Search gebruiken als backend voor opslag en ophalen van herinneringen**, vooral voor gestructureerd RAG.

Dit stelt je in staat om de antwoorden van je agent te onderbouwen met je eigen gegevens, en zorgt voor relevantere en nauwkeurigere antwoorden. Azure AI Search kan worden gebruikt om gebruiker-specifieke reisherinneringen, productcatalogi of andere domeinspecifieke kennis op te slaan.

Azure AI Search ondersteunt mogelijkheden zoals **Gestructureerd RAG**, dat uitblinkt in het extraheren en ophalen van dichte, gestructureerde informatie uit grote datasets zoals gesprekshistorie, e-mails of zelfs afbeeldingen. Dit levert "supermenselijke precisie en recall" vergeleken met traditionele tekstchunking en embedding methodes.

## AI Agents Zelfverbeterend Maken

Een veelvoorkomend patroon voor zelfverbeterende agents omvat het introduceren van een **"kennisagent"**. Deze aparte agent observeert het hoofdgesprek tussen de gebruiker en de primaire agent. Zijn rol is om:

1. **Waardevolle informatie identificeren**: Bepalen of een deel van het gesprek het waard is om opgeslagen te worden als algemene kennis of als specifieke gebruikersvoorkeur.

2. **Extraheren en samenvatten**: Het essentiële leerpunt of voorkeur uit het gesprek distilleren.

3. **Opslaan in een kennisbasis**: Deze geëxtraheerde informatie blijvend opslaan, vaak in een vectordatabase, zodat het later kan worden opgehaald.

4. **Toekomstige queries aanvullen**: Wanneer de gebruiker een nieuwe query initieert, haalt de kennisagent relevante opgeslagen informatie op en voegt deze toe aan de prompt van de gebruiker, waardoor cruciale context aan de primaire agent wordt geleverd (vergelijkbaar met RAG).

### Optimalisaties voor Geheugen

• **Latencybeheer**: Om te voorkomen dat gebruikersinteracties vertragen, kan aanvankelijk een goedkopere, snellere model gebruikt worden om snel te controleren of informatie het waard is om op te slaan of op te halen, waarbij het complexere extractie-/ophalingsproces alleen indien nodig wordt aangeroepen.

• **Onderhoud van de Kennisbasis**: Voor een groeiende kennisbasis kan minder vaak gebruikte informatie worden verplaatst naar "cold storage" om kosten te beheersen.

## Meer vragen over Agent Geheugen?

Word lid van de [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) om andere leerlingen te ontmoeten, om het kantooruren bij te wonen en om je vragen over AI Agents beantwoord te krijgen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->