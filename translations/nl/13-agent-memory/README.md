# Geheugen voor AI-agenten 
[![Agent Memory](../../../translated_images/nl/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Wanneer we de unieke voordelen van het maken van AI-agenten bespreken, worden vooral twee dingen genoemd: het vermogen om tools aan te roepen om taken uit te voeren en het vermogen om in de loop van de tijd te verbeteren. Geheugen vormt de basis voor het creëren van zelfverbeterende agenten die betere ervaringen voor onze gebruikers kunnen creëren.

In deze les bekijken we wat geheugen betekent voor AI-agenten en hoe we het kunnen beheren en gebruiken ten voordele van onze applicaties.

## Introductie

Deze les behandelt:

• **Begrijpen van AI-agentgeheugen**: Wat geheugen is en waarom het essentieel is voor agenten.

• **Implementeren en opslaan van geheugen**: Praktische methoden om geheugenfunctionaliteit aan je AI-agenten toe te voegen, met focus op kortetermijn- en langetermijngeheugen.

• **AI-agenten zelfverbeterend maken**: Hoe geheugen agenten in staat stelt te leren van eerdere interacties en in de loop van de tijd te verbeteren.

## Beschikbare implementaties

Deze les bevat twee uitgebreide notebook-tutorials:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementeert geheugen met Mem0 en Azure AI Search met Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementeert gestructureerd geheugen met Cognee, bouwt automatisch een kennisgrafiek ondersteund door embeddings, visualiseert de grafiek en intelligente retrieval

## Leerdoelen

Na het voltooien van deze les weet je hoe je:

• **Verschillende soorten AI-agentgeheugen kunt onderscheiden**, waaronder werkgeheugen, kortetermijngeheugen en langetermijngeheugen, evenals gespecialiseerde vormen zoals persona- en episodisch geheugen.

• **Kortetermijn- en langetermijngeheugen voor AI-agenten kunt implementeren en beheren** met Microsoft Agent Framework, gebruikmakend van tools zoals Mem0, Cognee, Whiteboard-geheugen en integratie met Azure AI Search.

• **De principes achter zelfverbeterende AI-agenten begrijpt** en hoe robuuste geheugenbeheersystemen bijdragen aan continu leren en aanpassing.

## Begrijpen van AI-agentgeheugen

In de kern verwijst **geheugen voor AI-agenten naar de mechanismen die hen in staat stellen informatie te behouden en op te roepen**. Deze informatie kan specifieke details over een gesprek zijn, gebruikersvoorkeuren, eerdere acties of zelfs aangeleerde patronen.

Zonder geheugen zijn AI-toepassingen vaak stateless, wat betekent dat elke interactie opnieuw begint. Dit leidt tot een repetitieve en frustrerende gebruikerservaring waarbij de agent vorige context of voorkeuren "vergeet".

### Waarom is geheugen belangrijk?

De intelligentie van een agent is diep verbonden met zijn vermogen om eerdere informatie te herinneren en te gebruiken. Geheugen stelt agenten in staat om:

• **Reflectief te zijn**: Leren van eerdere acties en uitkomsten.

• **Interactief te zijn**: Context te behouden gedurende een lopend gesprek.

• **Proactief en reactief te zijn**: Behoeften te anticiperen of passend te reageren op basis van historische gegevens.

• **Autonoom te zijn**: Onafhankelijker te opereren door te putten uit opgeslagen kennis.

Het doel van het implementeren van geheugen is om agenten betrouwbaarder en capabeler te maken.

### Soorten geheugen

#### Werkgeheugen

Beschouw dit als een stuk kladpapier dat een agent gebruikt tijdens een enkele, lopende taak of denkproces. Het bevat directe informatie die nodig is om de volgende stap te berekenen.

Voor AI-agenten legt werkgeheugen vaak de meest relevante informatie van een gesprek vast, zelfs als de volledige chatgeschiedenis lang of ingekort is. Het richt zich op het extraheren van sleutel-elementen zoals vereisten, voorstellen, beslissingen en acties.

**Voorbeeld werkgeheugen**

In een reisboekingsagent kan werkgeheugen de huidige aanvraag van de gebruiker vastleggen, zoals "Ik wil een reis naar Parijs boeken". Deze specifieke vereiste wordt in de directe context van de agent gehouden om de huidige interactie te sturen.

#### Kortetermijngeheugen

Dit type geheugen bewaart informatie voor de duur van een enkel gesprek of sessie. Het is de context van de huidige chat, waardoor de agent kan terugverwijzen naar eerdere beurten in de dialoog.

**Voorbeeld kortetermijngeheugen**

Als een gebruiker vraagt: "Hoeveel zou een vlucht naar Parijs kosten?" en vervolgens vraagt: "En wat qua accommodatie daar?", zorgt kortetermijngeheugen ervoor dat de agent weet dat "daar" verwijst naar "Parijs" binnen hetzelfde gesprek.

#### Langetermijngeheugen

Dit is informatie die blijft bestaan over meerdere gesprekken of sessies heen. Het stelt agenten in staat gebruikersvoorkeuren, historische interacties of algemene kennis over langere perioden te onthouden. Dit is belangrijk voor personalisatie.

**Voorbeeld langetermijngeheugen**

Een langetermijngeheugen zou kunnen opslaan dat "Ben van skiën en buitenactiviteiten houdt, graag koffie met een bergzicht drinkt en geavanceerde pistes wil vermijden vanwege een eerdere blessure". Deze informatie, geleerd uit eerdere interacties, beïnvloedt aanbevelingen in toekomstige reisplanningssessies en maakt ze sterk gepersonaliseerd.

#### Persona-geheugen

Dit gespecialiseerde geheugentype helpt een agent een consistente "persoonlijkheid" of "persona" te ontwikkelen. Het stelt de agent in staat details over zichzelf of zijn bedoelde rol te onthouden, waardoor interacties vloeiender en gerichter worden.

**Voorbeeld persona-geheugen**
Als de reisagent is ontworpen als een "expert in ski-planning", kan persona-geheugen deze rol versterken en zijn antwoorden laten aansluiten bij de toon en kennis van een expert.

#### Workflow / Episodisch geheugen

Dit geheugen slaat de opeenvolging van stappen op die een agent neemt tijdens een complexe taak, inclusief successen en fouten. Het is alsof de agent specifieke "episodes" of ervaringen onthoudt om ervan te leren.

**Voorbeeld episodisch geheugen**

Als de agent heeft geprobeerd een specifieke vlucht te boeken maar dit faalde vanwege onbeschikbaarheid, kan episodisch geheugen deze fout registreren, waardoor de agent alternatieve vluchten kan proberen of de gebruiker bij een volgende poging beter geïnformeerd kan laten weten wat er misging.

#### Entiteitsgeheugen

Dit omvat het extraheren en onthouden van specifieke entiteiten (zoals mensen, plaatsen of dingen) en gebeurtenissen uit gesprekken. Het stelt de agent in staat een gestructureerd begrip op te bouwen van belangrijke elementen die besproken zijn.

**Voorbeeld entiteitsgeheugen**

Uit een gesprek over een vorige reis kan de agent "Parijs", "Eiffeltoren" en "diner bij restaurant Le Chat Noir" als entiteiten extraheren. In een toekomstige interactie kan de agent "Le Chat Noir" herinneren en aanbieden daar een nieuwe reservering te maken.

#### Gestructureerde RAG (Retrieval Augmented Generation)

Hoewel RAG een bredere techniek is, wordt "Gestructureerde RAG" benadrukt als een krachtige geheugentechnologie. Het extraheert dichte, gestructureerde informatie uit verschillende bronnen (gesprekken, e-mails, afbeeldingen) en gebruikt dit om precisie, recall en snelheid in reacties te verbeteren. In tegenstelling tot klassieke RAG die uitsluitend op semantische gelijkenis vertrouwt, werkt Gestructureerde RAG met de inherente structuur van informatie.

**Voorbeeld Gestructureerde RAG**

In plaats van alleen trefwoorden te matchen, zou Gestructureerde RAG vluchtgegevens (bestemming, datum, tijd, luchtvaartmaatschappij) uit een e-mail kunnen parsen en op een gestructureerde manier opslaan. Dit maakt nauwkeurige zoekvragen mogelijk zoals "Welke vlucht heb ik naar Parijs geboekt op dinsdag?"

## Implementeren en opslaan van geheugen

Het implementeren van geheugen voor AI-agenten omvat een systematisch proces van **geheugenbeheer**, dat bestaat uit het genereren, opslaan, ophalen, integreren, bijwerken en zelfs "vergeten" (of verwijderen) van informatie. Ophalen is een bijzonder cruciaal aspect.

### Gespecialiseerde geheugen-tools

#### Mem0

Een manier om agentgeheugen op te slaan en te beheren is het gebruik van gespecialiseerde tools zoals Mem0. Mem0 werkt als een persistent geheugenspoor, waarmee agenten relevante interacties kunnen herinneren, gebruikersvoorkeuren en feitelijke context kunnen opslaan, en kunnen leren van successen en fouten in de loop van de tijd. Het idee hier is dat stateless agenten stateful worden.

Het werkt via een **tweepasjes geheugenpijplijn: extractie en update**. Eerst worden berichten die aan de thread van een agent worden toegevoegd naar de Mem0-service gestuurd, die een Large Language Model (LLM) gebruikt om de gespreksgeschiedenis samen te vatten en nieuwe herinneringen te extraheren. Vervolgens bepaalt een door een LLM gedreven updatefase of deze herinneringen moeten worden toegevoegd, aangepast of verwijderd, en slaat ze ze op in een hybride datastore die vector-, graf- en key-value-databases kan omvatten. Dit systeem ondersteunt ook verschillende geheugentypes en kan grafgeheugen integreren voor het beheren van relaties tussen entiteiten.

#### Cognee

Een andere krachtige benadering is het gebruik van **Cognee**, een open-source semantisch geheugen voor AI-agenten dat gestructureerde en ongestructureerde gegevens transformeert in doorzoekbare kennisgrafieken ondersteund door embeddings. Cognee biedt een **dual-store architectuur** die vectorsimilariteitszoeken combineert met grafrelaties, waardoor agenten niet alleen begrijpen welke informatie vergelijkbaar is, maar ook hoe concepten zich tot elkaar verhouden.

Het blinkt uit in **hybride retrieval** die vectorsimilariteit, grafstructuur en LLM-redenering combineert - van ruwe chunk-lookup tot graf-bewuste vraagbeantwoording. Het systeem onderhoudt een **levend geheugen** dat evolueert en groeit terwijl het doorzoekbaar blijft als één verbonden grafiek, en ondersteunt zowel kortetermijnsessiecontext als langetermijnpersistent geheugen.

De Cognee-notebooktutorial ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstreert het bouwen van deze verenigde geheugenlaag, met praktische voorbeelden van het opnemen van diverse gegevensbronnen, het visualiseren van de kennisgrafiek en het queryen met verschillende zoekstrategieën die zijn afgestemd op specifieke agentbehoeften.

### Geheugen opslaan met RAG

Naast gespecialiseerde geheugentools zoals Mem0 , kun je robuuste zoekservices zoals **Azure AI Search als backend gebruiken voor het opslaan en ophalen van herinneringen**, vooral voor Gestructureerde RAG.

Dit stelt je in staat de antwoorden van je agent te onderbouwen met je eigen gegevens, wat zorgt voor relevantere en nauwkeurigere antwoorden. Azure AI Search kan worden gebruikt om gebruikersspecifieke reisherinneringen, productcatalogi of andere domeinspecifieke kennis op te slaan.

Azure AI Search ondersteunt mogelijkheden zoals **Gestructureerde RAG**, die uitblinkt in het extraheren en ophalen van dichte, gestructureerde informatie uit grote datasets zoals gesprekshistorieken, e-mails of zelfs afbeeldingen. Dit biedt "supermenselijke precisie en recall" vergeleken met traditionele tekstchunking- en embedding-benaderingen.

## AI-agenten zelfverbeterend maken

Een veelgebruikt patroon voor zelfverbeterende agenten omvat het introduceren van een **"kennisagent"**. Deze aparte agent observeert het hoofdgesprek tussen de gebruiker en de primaire agent. Zijn rol is om:

1. **Waardevolle informatie te identificeren**: Bepalen of een deel van het gesprek het waard is om op te slaan als algemene kennis of specifieke gebruikersvoorkeur.

2. **Te extraheren en samen te vatten**: De essentie van de les of voorkeur uit het gesprek distilleren.

3. **Op te slaan in een kennisbasis**: Deze geëxtraheerde informatie persistent maken, vaak in een vectordatabase, zodat het later kan worden opgehaald.

4. **Toekomstige queries aan te vullen**: Wanneer de gebruiker een nieuwe query start, haalt de kennisagent relevante opgeslagen informatie op en voegt deze toe aan de prompt van de gebruiker, waardoor de primaire agent cruciale context krijgt (vergelijkbaar met RAG).

### Optimalisaties voor geheugen

• **Latencybeheer**: Om te voorkomen dat gebruikersinteracties vertragen, kan aanvankelijk een goedkopere, snellere model worden gebruikt om snel te controleren of informatie waardevol is om op te slaan of op te halen, en alleen het complexere extractie-/ophaalproces aanspreken wanneer dat nodig is.

• **Onderhoud van de kennisbasis**: Voor een groeiende kennisbasis kan minder vaak gebruikte informatie naar "cold storage" worden verplaatst om kosten te beheersen.

## Nog meer vragen over agentgeheugen?

Doe mee met de [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) om andere leerlingen te ontmoeten, kantooruren bij te wonen en je vragen over AI-agenten beantwoord te krijgen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we naar nauwkeurigheid streven, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->