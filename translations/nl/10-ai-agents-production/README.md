# AI-Agents in Productie: Observeerbaarheid & Evaluatie

[![AI Agents in Production](../../../translated_images/nl/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Naarmate AI-agents verschuiven van experimentele prototypes naar toepassingen in de echte wereld, wordt het belangrijk om hun gedrag te begrijpen, hun prestaties te bewaken en hun output systematisch te evalueren.

## Leerdoelen

Na het voltooien van deze les weet je hoe je/begrijp je:
- Kernconcepten van agent observeerbaarheid en evaluatie
- Technieken om de prestaties, kosten en effectiviteit van agents te verbeteren
- Wat en hoe je je AI-agents systematisch evalueert
- Hoe je kosten onder controle houdt bij het uitrollen van AI-agents in productie
- Hoe je agents die zijn gebouwd met Microsoft Agent Framework instrumenteert

Het doel is om je te voorzien van de kennis om je "black box" agents om te zetten in transparante, beheersbare en betrouwbare systemen.

_**Opmerking:** Het is belangrijk om AI-agents te implementeren die veilig en betrouwbaar zijn. Bekijk ook de les [Trustworthy AI Agents bouwen](../06-building-trustworthy-agents/README.md)._

## Traces en Spans

Observeerbaarheidstools zoals [Langfuse](https://langfuse.com/) of [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) stellen agentuitvoeringen meestal voor als traces en spans.

- **Trace** vertegenwoordigt een volledige agenttaak van begin tot eind (zoals het afhandelen van een gebruikersvraag).
- **Spans** zijn individuele stappen binnen de trace (zoals het aanroepen van een taalmodel of het ophalen van gegevens).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Zonder observeerbaarheid kan een AI-agent voelen als een "black box" - de interne staat en redenering zijn ondoorzichtig, waardoor het moeilijk is om problemen te diagnosticeren of prestaties te optimaliseren. Met observeerbaarheid worden agents "glass boxes", die transparantie bieden die cruciaal is voor het opbouwen van vertrouwen en het garanderen dat ze functioneren zoals bedoeld.

## Waarom Observeerbaarheid van Belang is in Productieomgevingen

Het overbrengen van AI-agents naar productieomgevingen brengt een nieuwe reeks uitdagingen en vereisten met zich mee. Observeerbaarheid is niet langer een "nice-to-have" maar een kritieke vaardigheid:

*   **Debuggen en Root-Cause Analyse**: Wanneer een agent faalt of een onverwachte output produceert, bieden observeerbaarheidstools de traces die nodig zijn om de bron van de fout te achterhalen. Dit is vooral belangrijk bij complexe agents die mogelijk meerdere LLM-aanroepen, toolinteracties en conditionele logica bevatten.
*   **Latentie en Kostenbeheer**: AI-agents vertrouwen vaak op LLMs en andere externe API's die per token of per oproep worden gefactureerd. Observeerbaarheid maakt nauwkeurige tracking van deze oproepen mogelijk, waardoor men operaties kan identificeren die te traag of te duur zijn. Dit stelt teams in staat prompts te optimaliseren, efficiëntere modellen te selecteren of workflows te herontwerpen om operationele kosten te beheersen en een goede gebruikerservaring te garanderen.
*   **Vertrouwen, Veiligheid en Naleving**: In veel toepassingen is het belangrijk om te zorgen dat agents veilig en ethisch gedrag vertonen. Observeerbaarheid levert een audittrail van agentacties en beslissingen. Dit kan gebruikt worden om problemen zoals promptinjectie, het genereren van schadelijke inhoud of het onjuist omgaan met persoonlijk identificeerbare informatie (PII) te detecteren en te mitigeren. Je kunt bijvoorbeeld traces bekijken om te begrijpen waarom een agent een bepaalde reactie gaf of een specifieke tool gebruikte.
*   **Continue Verbeteringsloops**: Observeerbaarheidsdata vormt de basis van een iteratief ontwikkelingsproces. Door te monitoren hoe agents presteren in de echte wereld, kunnen teams verbeterpunten identificeren, data verzamelen voor fijne afstemming van modellen en de impact van wijzigingen valideren. Dit creëert een feedbackloop waarbij inzichten uit online evaluatie productieinformatie bieden die offline experimentatie en verfijning voedt, wat leidt tot steeds betere agentprestaties.

## Belangrijke Metrics om te Volgen

Om agentgedrag te monitoren en te begrijpen, moeten verschillende metrics en signalen worden gevolgd. Hoewel de specifieke metrics kunnen variëren afhankelijk van het doel van de agent, zijn sommige universeel belangrijk.

Hier zijn enkele van de meest voorkomende metrics die observeerbaarheidstools volgen:

**Latentie:** Hoe snel reageert de agent? Lange wachttijden hebben een negatieve impact op de gebruikerservaring. Je moet de latentie meten voor taken en individuele stappen door agentuitvoeringen te traceren. Bijvoorbeeld, een agent die 20 seconden nodig heeft voor alle modelaanroepen kan worden versneld door een sneller model te gebruiken of door modelaanroepen parallel uit te voeren.

**Kosten:** Wat kost elke agentuitvoering? AI-agents zijn afhankelijk van LLM-aanroepen die per token worden gefactureerd of externe API's. Frequent gebruik van tools of meerdere prompts kan snel kosten doen stijgen. Bijvoorbeeld, als een agent een LLM vijf keer oproept voor een marginale kwaliteitsverbetering, moet je beoordelen of de kosten gerechtvaardigd zijn of dat je het aantal oproepen kunt verminderen of een goedkoper model kunt gebruiken. Real-time monitoring kan ook helpen onverwachte pieken te identificeren (bijv. bugs die overmatige API loops veroorzaken).

**Request Fouten:** Hoeveel verzoeken zijn mislukt bij de agent? Dit kan API-fouten of mislukte tooloproepen omvatten. Om je agent robuuster te maken tegen deze fouten in productie, kun je fallback-opties of retries instellen. Bijvoorbeeld, als LLM-provider A uitvalt, schakel je over naar LLM-provider B als backup.

**Gebruikersfeedback:** Het implementeren van directe gebruikersbeoordelingen levert waardevolle inzichten op. Dit kan expliciete beoordelingen omvatten (👍duim omhoog/👎omlaag, ⭐1-5 sterren) of tekstuele opmerkingen. Consistente negatieve feedback moet je waarschuwen omdat dit een teken is dat de agent niet naar behoren werkt.

**Impliciete Gebruikersfeedback:** Gebruikersgedrag levert indirecte feedback, zelfs zonder expliciete beoordelingen. Dit kan directe vraagherschikking, herhaalde queries of het klikken op een retry-knop omvatten. Bijvoorbeeld, als je ziet dat gebruikers herhaaldelijk dezelfde vraag stellen, is dit een teken dat de agent niet werkt zoals verwacht.

**Nauwkeurigheid:** Hoe vaak produceert de agent correcte of wenselijke resultaten? Definities van nauwkeurigheid variëren (bijv. correctheid van probleemoplossing, nauwkeurigheid van informatieophaling, gebruikersvoldoening). De eerste stap is om te definiëren wat succes voor jouw agent betekent. Je kunt nauwkeurigheid volgen via geautomatiseerde controles, evaluatiescores of taakvoltooiinglabels. Bijvoorbeeld, traces markeren als "geslaagd" of "mislukt".

**Geautomatiseerde Evaluatiemetrics:** Je kunt ook geautomatiseerde evaluaties instellen. Bijvoorbeeld, je kunt een LLM gebruiken om de output van de agent te scoren, b.v. of deze behulpzaam, accuraat of niet is. Er zijn ook verschillende open-source bibliotheken die helpen bij het scoren van verschillende aspecten van de agent. Bijvoorbeeld [RAGAS](https://docs.ragas.io/) voor RAG-agents of [LLM Guard](https://github.com/protectai/llm-guard) om schadelijke taal of promptinjectie te detecteren.

In de praktijk levert een combinatie van deze metrics de beste dekking van de gezondheid van een AI-agent. In het [voorbeeldnotebook](./code_samples/10-expense_claim-demo.ipynb) van dit hoofdstuk laten we je zien hoe deze metrics eruitzien in echte voorbeelden, maar eerst leren we hoe een typische evaluatieworkflow eruitziet.

## Instrueer je Agent

Om tracegegevens te verzamelen, moet je je code instrumenteren. Het doel is het agentenprogramma te instrumenteren zodat het traces en metrics genereert die kunnen worden vastgelegd, verwerkt en gevisualiseerd door een observeerbaarheidsplatform.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) is uitgegroeid tot een industrieel standaard voor LLM-observeerbaarheid. Het biedt een set API’s, SDK’s en tools voor het genereren, verzamelen en exporteren van telemetriedata.

Er zijn veel instrumentatielibraries die bestaande agentframeworks wrappen en het makkelijk maken om OpenTelemetry-spans naar een observeerbaarheidstool te exporteren. Microsoft Agent Framework integreert native met OpenTelemetry. Hieronder een voorbeeld van het instrumenteren van een MAF-agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agent execution is traced automatically
    pass
```

Het [voorbeeldnotebook](./code_samples/10-expense_claim-demo.ipynb) in dit hoofdstuk laat zien hoe je je MAF-agent instrumenteert.

**Handmatige Spancreatie:** Hoewel instrumentatielibraries een goede basis bieden, zijn er vaak situaties waar meer gedetailleerde of aangepaste informatie nodig is. Je kunt handmatig spans creëren om aangepaste applicatielogica toe te voegen. Bovenal kunnen automatisch of handmatig gemaakte spans worden verrijkt met aangepaste attributen (ook bekend als tags of metadata). Deze attributen kunnen bedrijfsspecifieke data, tussenliggende berekeningen of enige context omvatten die nuttig kan zijn voor debuggen of analyse, zoals `user_id`, `session_id`, of `model_version`.

Voorbeeld van handmatig traces en spans creëren met de [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agentevaluatie

Observeerbaarheid levert ons metrics, maar evaluatie is het proces waarin die data (en tests) geanalyseerd worden om te bepalen hoe goed een AI-agent presteert en hoe die kan worden verbeterd. Met andere woorden: zodra je die traces en metrics hebt, hoe gebruik je die dan om de agent te beoordelen en beslissingen te nemen?

Regelmatige evaluatie is belangrijk omdat AI-agents vaak niet-deterministisch zijn en kunnen evolueren (door updates of veranderend modelgedrag) – zonder evaluatie weet je niet of je “slimme agent” eigenlijk goed werkt of dat die is achteruitgegaan.

Er zijn twee categorieën evaluaties voor AI-agents: **online evaluatie** en **offline evaluatie**. Beide zijn waardevol en vullen elkaar aan. We beginnen meestal met offline evaluatie, omdat dit de minimaal noodzakelijke stap is voordat een agent wordt ingezet.

### Offline Evaluatie

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Dit houdt in dat de agent wordt geëvalueerd in een gecontroleerde omgeving, meestal met testdatasets, niet met live gebruikersvragen. Je gebruikt samengestelde datasets waarbij je weet wat de verwachte output of correct gedrag is, en draait de agent op die dataset.

Bijvoorbeeld, als je een agent hebt gebouwd voor wiskundige woordproblemen, dan zou je een [testdataset](https://huggingface.co/datasets/openai/gsm8k) kunnen hebben met 100 problemen met bekende antwoorden. Offline evaluatie wordt vaak gedaan tijdens de ontwikkeling (en kan onderdeel zijn van CI/CD-pijplijnen) om verbeteringen te checken of regressies te voorkomen. Het voordeel is dat het **herhaalbaar is en je duidelijke nauwkeurigheidsmetrics krijgt omdat je een grondwaarheid hebt**. Je kunt ook gebruikersvragen simuleren en de antwoorden van de agent meten tegen ideale antwoorden of geautomatiseerde metrics gebruiken, zoals hierboven beschreven.

De belangrijkste uitdaging bij offline evaluatie is ervoor te zorgen dat je testdataset uitgebreid en relevant blijft – de agent kan goed presteren op een vaste testset, maar zeer verschillende queries tegenkomen in productie. Daarom moet je testsets bijwerken met nieuwe randgevallen en voorbeelden die echte situaties weerspiegelen. Een mix van kleine “rooktesten” en grotere evaluatiesets is nuttig: kleine sets voor snelle controles en grotere sets voor bredere prestatiestatistieken.

### Online Evaluatie

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Dit verwijst naar het evalueren van de agent in een live, echte-wereldomgeving, dus tijdens daadwerkelijk gebruik in productie. Online evaluatie omvat het monitoren van de prestaties van de agent op echte gebruikersinteracties en het continu analyseren van resultaten.

Bijvoorbeeld, je kunt succespercentages, gebruikersvoldoenheidscores of andere metrics op live verkeer volgen. Het voordeel van online evaluatie is dat het **dingen vastlegt die je misschien niet in een labomgeving verwacht** – je kunt modeldrift over tijd waarnemen (als de effectiviteit van de agent afneemt doordat invoerpatronen veranderen) en onverwachte vragen of situaties detecteren die niet in je testdata voorkwamen. Het geeft een waarheidsgetrouw beeld van hoe de agent zich in het wild gedraagt.

Online evaluatie omvat vaak het verzamelen van impliciete en expliciete gebruikersfeedback, zoals besproken, en mogelijk het uitvoeren van schaduwtests of A/B-tests (waarbij een nieuwe versie van de agent parallel draait om te vergelijken met de oude). De uitdaging is dat het lastig kan zijn om betrouwbare labels of scores te krijgen voor live interacties – je vertrouwt mogelijk op gebruikersfeedback of downstream metrics (zoals of de gebruiker op het resultaat heeft geklikt).

### De twee combineren

Online en offline evaluaties sluiten elkaar niet uit; ze vullen elkaar juist aan. Inzichten uit online monitoring (bijv. nieuwe soorten gebruikersvragen waar de agent slecht op presteert) kunnen worden gebruikt om offline testdatasets aan te vullen en te verbeteren. Omgekeerd kunnen agents die goed presteren op offline tests vervolgens met meer vertrouwen online worden ingezet en gemonitord.

Veel teams hanteren in feite een loop:

_offline evalueren -> inzetten -> online monitoren -> nieuwe fouten verzamelen -> toevoegen aan offline dataset -> agent verfijnen -> herhalen_.

## Veelvoorkomende Problemen

Bij het inzetten van AI-agents in productie kom je wellicht diverse uitdagingen tegen. Hier zijn enkele veelvoorkomende problemen en hun mogelijke oplossingen:

| **Probleem**    | **Mogelijke Oplossing**   |
| ------------- | ------------------ |
| AI-agent voert taken niet consistent uit | - Verfijn de prompt die aan de AI-agent wordt gegeven; wees duidelijk over de doelstellingen.<br>- Identificeer waar het opdelen van taken in subtaken en deze laten afhandelen door meerdere agents kan helpen. |
| AI-agent loopt in continue loops vast | - Zorg voor duidelijke beëindigingsvoorwaarden zodat de agent weet wanneer hij het proces moet stoppen.<br>- Gebruik voor complexe taken die redeneren en plannen vereisen een groter model dat gespecialiseerd is in redeneertaken. |
| AI-agent tool-oproepen presteren niet goed | - Test en valideer de output van de tool buiten het agentsysteem.<br>- Verfijn de gedefinieerde parameters, prompts en benamingen van tools. |
| Multi-agent systeem presteert inconsistent | - Verfijn de prompts die aan elke agent worden gegeven zodat ze specifiek en van elkaar verschillend zijn.<br>- Bouw een hiërarchisch systeem met een "routerings-" of controller-agent die bepaalt welke agent de juiste is. |

Veel van deze problemen kunnen effectiever worden geïdentificeerd met observeerbaarheid in huis. De traces en metrics die we eerder bespraken helpen precies te lokaliseren waar in de agentworkflow problemen optreden, wat debuggen en optimaliseren veel efficiënter maakt.

## Kosten Beheren

Hier zijn enkele strategieën om de kosten van het inzetten van AI-agents in productie te beheren:

**Kleinere modellen gebruiken:** Kleine taalmodellen (SLM's) kunnen goed presteren bij bepaalde agentische use-cases en zullen de kosten aanzienlijk verlagen. Zoals eerder vermeld, is het bouwen van een evaluatiesysteem om de prestaties te bepalen en te vergelijken met grotere modellen de beste manier om te begrijpen hoe goed een SLM zal presteren in jouw use case. Overweeg om SLM's te gebruiken voor eenvoudigere taken zoals intentieclassificatie of parameterextractie, terwijl je grotere modellen reserveert voor complexere redenering.

**Een routermodel gebruiken:** Een vergelijkbare strategie is het gebruik van een diversiteit aan modellen en groottes. Je kunt een LLM/SLM of serverloze functie gebruiken om verzoeken op basis van complexiteit te routeren naar de best passende modellen. Dit helpt ook om kosten te verlagen en tegelijkertijd prestaties te garanderen voor de juiste taken. Bijvoorbeeld, routeer eenvoudige vragen naar kleinere, snellere modellen en gebruik dure grote modellen alleen voor complexe redeneertaken.

**Responses cachen:** Het identificeren van veelvoorkomende verzoeken en taken en het vooraf leveren van de antwoorden voordat ze door jouw agentische systeem gaan, is een goede manier om het volume van soortgelijke verzoeken te verminderen. Je kunt zelfs een flow implementeren om te bepalen hoe vergelijkbaar een verzoek is met jouw gecachte verzoeken met behulp van eenvoudigere AI-modellen. Deze strategie kan de kosten aanzienlijk verlagen voor veelgestelde vragen of veelvoorkomende workflows.

## Laten we zien hoe dit in de praktijk werkt

In de [voorbeeldnotebook van deze sectie](./code_samples/10-expense_claim-demo.ipynb), zien we voorbeelden van hoe we observability-tools kunnen gebruiken om onze agent te monitoren en evalueren.


### Meer vragen over AI-agenten in productie?

Sluit je aan bij de [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) om andere leerlingen te ontmoeten, deel te nemen aan kantooruren en je vragen over AI-agenten te laten beantwoorden.

## Vorige les

[Metacognitie ontwerp patroon](../09-metacognition/README.md)

## Volgende les

[Agentische protocollen](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->