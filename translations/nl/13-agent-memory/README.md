# Geheugen voor AI Agenten 
[![Agent Memory](../../../translated_images/nl/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Bij het bespreken van de unieke voordelen van het creëren van AI Agenten, worden voornamelijk twee zaken besproken: het vermogen om tools aan te roepen om taken te voltooien en het vermogen om in de loop van de tijd te verbeteren. Geheugen ligt ten grondslag aan het creëren van een zelfverbeterende agent die betere ervaringen voor onze gebruikers kan creëren.

In deze les bekijken we wat geheugen is voor AI Agenten en hoe we het kunnen beheren en gebruiken ten voordele van onze toepassingen.

## Introductie

Deze les behandelt:

• **Begrip van AI Agent Geheugen**: Wat geheugen is en waarom het essentieel is voor agenten.

• **Implementeren en Opslaan van Geheugen**: Praktische methoden voor het toevoegen van geheugenmogelijkheden aan je AI agenten, met focus op kortetermijn- en langetermijngeheugen.

• **Zelfverbeterende AI Agenten Maken**: Hoe geheugen agenten in staat stelt te leren van eerdere interacties en in de loop van de tijd beter te worden.

## Beschikbare Implementaties

Deze les bevat twee uitgebreide notebook tutorials:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementeert geheugen met Mem0 en Azure AI Search met Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementeert gestructureerd geheugen met Cognee, automatisch opbouwen van knowledge graph gebaseerd op embeddings, visualisatie van grafiek, en intelligente opvraging

## Leerdoelen

Na het voltooien van deze les weet je hoe je:

• **Ondertussen verschillende typen AI agent geheugen kunt onderscheiden**, waaronder werkgeheugen, kortetermijngeheugen, langetermijngeheugen en gespecialiseerde vormen zoals persoonlijkheids- en episodisch geheugen.

• **Kortetermijn- en langetermijngeheugen voor AI agenten kunt implementeren en beheren** met het Microsoft Agent Framework, gebruikmakend van tools zoals Mem0, Cognee, Whiteboard geheugen, en integratie met Azure AI Search.

• **De principes achter zelfverbeterende AI agenten kunt begrijpen** en hoe robuuste geheugensystemen bijdragen aan continue leer- en aanpassingsprocessen.

## Begrip van AI Agent Geheugen

In de kern verwijst **geheugen voor AI agenten naar de mechanismen die hen in staat stellen informatie te behouden en terug te halen**. Deze informatie kan specifieke details over een gesprek zijn, gebruikersvoorkeuren, eerdere handelingen, of zelfs geleerde patronen.

Zonder geheugen zijn AI-toepassingen vaak stateloos, wat betekent dat elke interactie opnieuw begint. Dit leidt tot een repetitieve en frustrerende gebruikerservaring waarbij de agent de eerdere context of voorkeuren "vergeet".

### Waarom is Geheugen Belangrijk?

De intelligentie van een agent is diep verbonden met zijn vermogen om eerdere informatie te herinneren en te gebruiken. Geheugen maakt dat agenten:

• **Reflectief** zijn: Leren van eerdere handelingen en uitkomsten.

• **Interactief** zijn: De context van een lopend gesprek vasthouden.

• **Proactief en Reactief** zijn: Behoeften anticiperen of gepast reageren op basis van historische data.

• **Autonoom** zijn: Meer onafhankelijk opereren door gebruik te maken van opgeslagen kennis.

Het doel van het implementeren van geheugen is om agenten **betrouwbaarder en capabeler** te maken.

### Typen Geheugen

#### Werkgeheugen

Zie dit als een kladblokje dat een agent gebruikt tijdens een enkele, lopende taak of denkproces. Het houdt directe informatie vast die nodig is om de volgende stap te berekenen.

Voor AI agenten vangt werkgeheugen vaak de meest relevante informatie uit een gesprek op, zelfs als de volledige gespreksgeschiedenis lang of ingekort is. Het richt zich op het extraheren van kernpunten zoals vereisten, voorstellen, beslissingen en acties.

**Voorbeeld van Werkgeheugen**

In een reisboekingsagent kan werkgeheugen de huidige wens van de gebruiker vastleggen, zoals "Ik wil een reis naar Parijs boeken". Deze specifieke vereiste wordt vastgehouden in de directe context van de agent om de huidige interactie te begeleiden.

#### Kortetermijngeheugen

Dit type geheugen behoudt informatie gedurende een enkele conversatie of sessie. Het betreft de context van de huidige chat, waardoor de agent kan terugverwijzen naar eerdere beurten in het gesprek.

In de [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK voorbeelden correspondeert dit met `AgentSession`, aangemaakt met `agent.create_session()`. De sessie is het ingebouwde kortetermijngeheugen van het framework: het houdt de gesprekcontext beschikbaar zolang diezelfde sessie wordt hergebruikt, maar die context wordt niet bewaard wanneer de sessie eindigt of de applicatie opnieuw start. Gebruik langetermijngeheugen voor feiten en voorkeuren die sessies overstijgend moeten zijn, doorgaans via een database, vectorindex of een andere persistente opslag.

**Voorbeeld van Kortetermijngeheugen**

Als een gebruiker vraagt: "Hoeveel kost een vlucht naar Parijs?" en vervolgens "En de accommodatie daar?", zorgt het kortetermijngeheugen ervoor dat de agent weet dat "daar" verwijst naar "Parijs" binnen hetzelfde gesprek.

#### Langetermijngeheugen

Dit is informatie die behouden blijft over meerdere gesprekken of sessies. Het stelt agenten in staat gebruikersvoorkeuren, historische interacties of algemene kennis over langere perioden te onthouden. Dit is belangrijk voor personalisatie.

**Voorbeeld van Langetermijngeheugen**

Een langetermijngeheugen kan opslaan dat "Ben houdt van skiën en buitenactiviteiten, houdt van koffie met uitzicht op de bergen, en wil geavanceerde skipistes vermijden vanwege een eerdere blessure". Deze informatie, geleerd uit eerdere interacties, beïnvloedt aanbevelingen in toekomstige reisplanningssessies, waardoor deze sterk gepersonaliseerd worden.

#### Persoonlijkheidsgeheugen

Dit gespecialiseerde type geheugen helpt een agent een consistente "persoonlijkheid" of "persona" te ontwikkelen. Het stelt de agent in staat details over zichzelf of zijn bedoelde rol te onthouden, waardoor interacties vloeiender en gerichter zijn.

**Voorbeeld van Persoonlijkheidsgeheugen**
Als de reisagent is ontworpen als een "expert ski-planner," kan persoonlijkheidsgeheugen deze rol versterken, waardoor zijn antwoorden overeenkomen met de toon en kennis van een expert.

#### Workflow/Episodisch geheugen

Dit geheugen slaat de reeks stappen op die een agent onderneemt tijdens een complexe taak, inclusief successen en mislukkingen. Het is alsof het specifieke "episodes" of ervaringen herinnert om ervan te leren.

**Voorbeeld van Episodisch Geheugen**

Als de agent probeerde een specifieke vlucht te boeken maar dit faalde vanwege onbeschikbaarheid, kan episodisch geheugen deze mislukking registreren, waardoor de agent alternatieve vluchten kan proberen of de gebruiker beter kan informeren bij een volgende poging.

#### Entity-geheugen

Dit houdt in dat specifieke entiteiten (zoals personen, plaatsen of zaken) en gebeurtenissen uit gesprekken worden geëxtraheerd en onthouden. Het stelt de agent in staat een gestructureerd begrip van belangrijke elementen te bouwen.

**Voorbeeld van Entity-geheugen**

Uit een gesprek over een eerdere reis kan de agent "Parijs," "Eiffeltoren," en "diner bij Le Chat Noir restaurant" als entiteiten extraheren. Bij een toekomstige interactie zou de agent "Le Chat Noir" kunnen herinneren en een nieuwe reservering daar kunnen aanbieden.

#### Gestructureerde RAG (Retrieval Augmented Generation)

Terwijl RAG een bredere techniek is, wordt "Gestructureerde RAG" benadrukt als een krachtige geheugentechnologie. Het extraheert dichte, gestructureerde informatie uit diverse bronnen (gesprekken, e-mails, afbeeldingen) en gebruikt dit om precisie, terugroeping en snelheid van antwoorden te verbeteren. In tegenstelling tot klassieke RAG die uitsluitend op semantische gelijkenis vertrouwt, werkt Gestructureerde RAG met de inherente structuur van informatie.

**Voorbeeld van Gestructureerde RAG**

In plaats van alleen trefwoorden te matchen, kan Gestructureerde RAG vluchtgegevens (bestemming, datum, tijd, maatschappij) uit een e-mail parseren en gestructureerd opslaan. Dit maakt nauwkeurige vragen mogelijk zoals "Welke vlucht heb ik geboekt naar Parijs op dinsdag?"

## Implementeren en Opslaan van Geheugen

Het implementeren van geheugen voor AI agenten omvat een systematisch proces van **geheugenbeheer**, waaronder het genereren, opslaan, ophalen, integreren, bijwerken, en zelfs "vergeten" (of verwijderen) van informatie. Ophalen is een bijzonder cruciaal aspect.

### Gespecialiseerde Geheugentools

#### Mem0

Een manier om agentgeheugen op te slaan en te beheren is door gespecialiseerde tools zoals Mem0 te gebruiken. Mem0 werkt als een persistente geheugenslaag, waardoor agenten relevante interacties kunnen herinneren, gebruikersvoorkeuren en feitelijke context kunnen opslaan, en kunnen leren van successen en mislukkingen in de loop van de tijd. Het idee hier is dat stateloze agenten veranderen in statenvolle agenten.

Het werkt via een **tweepasige geheugen-pijplijn: extractie en update**. Eerst worden berichten die aan een agenten-thread zijn toegevoegd, naar de Mem0-service gestuurd, die een Large Language Model (LLM) gebruikt om de gespreksgeschiedenis samen te vatten en nieuwe herinneringen te extraheren. Vervolgens bepaalt een door LLM aangestuurde updatefase of deze herinneringen worden toegevoegd, gewijzigd, of verwijderd, en slaat ze op in een hybride datastore die vector-, grafiek- en key-value databases kan omvatten. Dit systeem ondersteunt ook verschillende geheugen typen en kan grafiekgeheugen integreren voor het beheren van relaties tussen entiteiten.

#### Cognee

Een andere krachtige aanpak is het gebruik van **Cognee**, een open-source semantisch geheugen voor AI agenten dat gestructureerde en ongestructureerde data omzet in doorzoekbare knowledge graphs ondersteund door embeddings. Cognee levert een **dual-store architectuur** die vector-zoekacties combineert met grafiekrelaties, waardoor agenten niet alleen begrijpen welke informatie gelijk is, maar ook hoe concepten aan elkaar gerelateerd zijn.

Het blinkt uit in **hybride opvraging** die vector gelijkenis, grafiekstructuur en LLM-redenering combineert – van ruwe chunk-lookup tot grafiekbewuste vraag-antwoord systemen. Het systeem onderhoudt een **levend geheugen** dat evolueert en groeit terwijl het doorzoekbaar blijft als één verbonden grafiek, en ondersteunt zowel kortetermijn-sessiecontext als langetermijn-persistent geheugen.

De Cognee notebook tutorial ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstreert het bouwen van deze uniforme geheugenslaag, met praktische voorbeelden van het inlezen van diverse gegevensbronnen, visualisatie van de knowledge graph, en opvraging met verschillende zoekstrategieën, afgestemd op specifieke agentbehoeften.

### Geheugen Opslaan met RAG

Naast gespecialiseerde geheugentools zoals Mem0, kun je robuuste zoekservices zoals **Azure AI Search als backend gebruiken voor het opslaan en ophalen van herinneringen**, vooral voor gestructureerde RAG.

Dit stelt je in staat de antwoorden van je agent te funderen met je eigen data, wat zorgt voor relevantere en nauwkeurigere antwoorden. Azure AI Search kan worden gebruikt om gebruikersspecifieke reisherinneringen, productcatalogi of andere domeinspecifieke kennis op te slaan.

Azure AI Search ondersteunt functies zoals **Gestructureerde RAG**, die uitblinkt in het extraheren en terugvinden van dicht, gestructureerd materiaal uit grote datasets zoals gespreksgeschiedenissen, e-mails, of zelfs afbeeldingen. Dit levert "bovennatuurlijke precisie en terugroeping" in vergelijking met traditionele tekstchunking en embedding benaderingen.

## AI Agenten Zelfverbeterend Maken

Een gangbaar patroon voor zelfverbeterende agenten is het introduceren van een **"kennisagent"**. Deze aparte agent observeert het hoofdgesprek tussen de gebruiker en de primaire agent. Zijn rol is:

1. **Waardevolle informatie identificeren**: Bepalen of een deel van het gesprek het waard is om opgeslagen te worden als algemene kennis of specifieke gebruikersvoorkeur.

2. **Extraheren en samenvatten**: Het essentiële leerpunt of voorkeur uit het gesprek distilleren.

3. **Opslaan in een kennisbasis**: Deze geëxtraheerde informatie persistent maken, vaak in een vectordatabase, zodat het later kan worden opgehaald.

4. **Toekomstige zoekopdrachten aanvullen**: Wanneer de gebruiker een nieuwe zoekopdracht start, haalt de kennisagent relevante opgeslagen informatie op en voegt die toe aan de prompt van de gebruiker, waardoor cruciale context aan de primaire agent wordt gegeven (vergelijkbaar met RAG).

### Optimalisaties voor Geheugen

• **Latentiebeheer**: Om vertragingen bij gebruikersinteracties te vermijden, kan aanvankelijk een goedkoper, sneller model worden gebruikt om snel te controleren of informatie waardevol is om op te slaan of op te halen, en alleen bij noodzaak het complexere extractie-/ophaalproces aanroepen.

• **Kennisbasisonderhoud**: Voor een groeiende kennisbasis kan minder gebruikte informatie naar "koude opslag" worden verplaatst om kosten te beheersen.

## Nog Meer Vragen Over Agent Geheugen?

Sluit je aan bij de [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) om andere leerlingen te ontmoeten, aanwezig te zijn bij spreekuren en je vragen over AI Agenten beantwoord te krijgen.
## Vorige Les

[Context Engineering voor AI Agenten](../12-context-engineering/README.md)

## Volgende Les

[Verkennen van Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->