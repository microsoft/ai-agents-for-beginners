# AI-agenten in productie: Observeerbaarheid & Evaluatie

[![AI Agents in Production](../../../translated_images/nl/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Naarmate AI-agenten van experimentele prototypes naar toepassingen in de echte wereld gaan, wordt het belangrijk om hun gedrag te begrijpen, hun prestaties te monitoren en hun outputs systematisch te evalueren.

## Leerdoelen

Na het voltooien van deze les weet je hoe/begrijp je:
- Kernconcepten van observeerbaarheid en evaluatie van agenten
- Technieken om de prestaties, kosten en effectiviteit van agenten te verbeteren
- Wat en hoe je je AI-agenten systematisch kunt evalueren
- Hoe je kosten kunt beheersen bij het uitrollen van AI-agenten in productie
- Hoe je agenten gebouwd met het Microsoft Agent Framework kunt instrumenteren

Het doel is je te voorzien van kennis om je "black box" agenten om te vormen tot transparante, beheersbare en betrouwbare systemen.

_**Opmerking:** Het is belangrijk AI-agenten veilig en betrouwbaar uit te rollen. Bekijk ook de les [Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)._

## Traces en Spans

Observeerbaarheidstools zoals [Langfuse](https://langfuse.com/) of [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) representeren runs van agenten meestal als traces en spans.

- **Trace** vertegenwoordigt een volledige agenttaak van begin tot eind (zoals het afhandelen van een gebruikersvraag).
- **Spans** zijn individuele stappen binnen de trace (zoals het aanroepen van een taalmodel of het ophalen van gegevens).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Zonder observeerbaarheid kan een AI-agent aanvoelen als een "black box" - zijn interne staat en redenering zijn ondoorzichtig, waardoor het moeilijk is problemen te diagnosticeren of prestaties te optimaliseren. Met observeerbaarheid worden agenten "glasdozen", die transparantie bieden die essentieel is om vertrouwen op te bouwen en ervoor te zorgen dat ze werken zoals bedoeld.

## Waarom observeerbaarheid belangrijk is in productieomgevingen

Het migreren van AI-agenten naar productieomgevingen brengt nieuwe uitdagingen en eisen met zich mee. Observeerbaarheid is geen "nice-to-have" meer maar een kritische vaardigheid:

*   **Debuggen en oorzaak-analyse:** Wanneer een agent faalt of een onverwachte output produceert, bieden observeerbaarheidstools de traces die nodig zijn om de bron van de fout te vinden. Dit is vooral belangrijk bij complexe agenten met meerdere LLM-aanroepen, toolinteracties en conditionele logica.
*   **Latentie- en kostenbeheer:** AI-agenten vertrouwen vaak op LLMs en andere externe API's die per token of per oproep worden gefactureerd. Observeerbaarheid maakt nauwkeurige tracking van deze oproepen mogelijk en helpt bij het identificeren van operaties die te traag of te duur zijn. Dit stelt teams in staat prompts te optimaliseren, efficiëntere modellen te selecteren of workflows opnieuw te ontwerpen om operationele kosten te beheersen en een goede gebruikerservaring te waarborgen.
*   **Vertrouwen, veiligheid en compliance:** In veel toepassingen is het belangrijk dat agenten zich veilig en ethisch gedragen. Observeerbaarheid biedt een audit trail van de acties en beslissingen van de agent. Dit kan worden gebruikt om problemen te detecteren en te beperken zoals promptinvoer, het genereren van schadelijke inhoud of het verkeerd omgaan met persoonsgebonden informatie (PII). Bijvoorbeeld, je kunt traces bekijken om te begrijpen waarom een agent een bepaalde reactie gaf of een specifieke tool gebruikte.
*   **Continue verbeteringslussen:** Observeerbaarheidsdata vormen de basis voor een iteratief ontwikkelproces. Door te monitoren hoe agenten presteren in de echte wereld, kunnen teams verbeterpunten identificeren, data verzamelen voor het fijn afstemmen van modellen en de impact van aanpassingen valideren. Dit creëert een feedbackloop waarbij inzichten uit productie-evaluaties offline experimenten en verfijning informeren, leidend tot steeds betere agentprestaties.

## Belangrijke statistieken om te volgen

Om het gedrag van agenten te monitoren en te begrijpen, moet een reeks statistieken en signalen worden gevolgd. Hoewel de specifieke metrics kunnen variëren afhankelijk van het doel van de agent, zijn sommige universeel belangrijk.

Hier zijn enkele van de meest voorkomende statistieken die observeerbaarheidstools monitoren:

**Latentie:** Hoe snel reageert de agent? Lange wachttijden hebben een negatieve impact op de gebruikerservaring. Je moet latentie meten voor taken en individuele stappen door agent-runs te tracen. Bijvoorbeeld, een agent die 20 seconden nodig heeft voor alle modelaanroepen kan versneld worden door een sneller model te gebruiken of modelaanroepen parallel uit te voeren.

**Kosten:** Wat zijn de kosten per agent-run? AI-agenten vertrouwen op LLM-aanroepen die per token worden gefactureerd of op externe API's. Frequente toolgebruik of meerdere prompts kunnen de kosten snel verhogen. Bijvoorbeeld, als een agent een LLM vijf keer aanroept voor een marginale kwaliteitsverbetering, moet je beoordelen of de kosten gerechtvaardigd zijn of dat je het aantal aanroepen kunt verminderen of een goedkoper model kunt gebruiken. Real-time monitoring helpt ook om onverwachte pieken (bijv. bugs die overmatige API-lussen veroorzaken) te identificeren.

**Aanvraagfouten:** Hoeveel aanvragen zijn mislukt? Dit kan API-fouten of mislukte toolaanroepen omvatten. Om je agent robuuster te maken tegen deze fouten in productie, kun je back-ups of retries instellen. Bijvoorbeeld als LLM-provider A uitvalt, schakel je over naar LLM-provider B als backup.

**Gebruikersfeedback:** Directe gebruikersbeoordelingen bieden waardevolle inzichten. Dit kan expliciete beoordelingen omvatten (👍duim omhoog/👎omlaag, ⭐1-5 sterren) of tekstuele opmerkingen. Consistente negatieve feedback moet je waarschuwen, want dit is een teken dat de agent niet werkt zoals verwacht.

**Impliciete gebruikersfeedback:** Gebruikersgedrag levert indirecte feedback op, zelfs zonder expliciete beoordelingen. Dit kan directe vraagherformuleringen, herhaalde vragen of het klikken op een herprobeerknop omvatten. Bijvoorbeeld, als je ziet dat gebruikers dezelfde vraag herhaaldelijk stellen, is dat een teken dat de agent niet werkt zoals verwacht.

**Nauwkeurigheid:** Hoe vaak produceert de agent correcte of gewenste outputs? Definities van nauwkeurigheid variëren (bijv. juistheid van probleemoplossing, nauwkeurigheid van informatieopvraag, gebruikerstevredenheid). De eerste stap is vaststellen wat succes voor jouw agent betekent. Je kunt nauwkeurigheid volgen via automatische controles, evaluatiescores of labels voor taakvoltooiing. Bijvoorbeeld door traces te markeren als "geslaagd" of "mislukt".

**Geautomatiseerde evaluatiemetrics:** Je kunt ook automatische evaluaties instellen. Bijvoorbeeld, je kunt een LLM gebruiken om de output van de agent te scoren, bijvoorbeeld of deze behulpzaam, nauwkeurig is of niet. Er zijn ook verschillende open source bibliotheken die je helpen om verschillende aspecten van de agent te scoren. Bijvoorbeeld [RAGAS](https://docs.ragas.io/) voor RAG-agenten of [LLM Guard](https://llm-guard.com/) om schadelijke taal of promptinvoer te detecteren.

In de praktijk geeft een combinatie van deze metrics de beste dekking van de gezondheid van een AI-agent. In het [voorbeeldnotebook](./code_samples/10-expense_claim-demo.ipynb) van dit hoofdstuk laten we je zien hoe deze statistieken eruit zien in echte voorbeelden, maar eerst leren we hoe een typische evaluatieworkflow eruitziet.

## Instrumenteer je agent

Om tracingdata te verzamelen, moet je je code instrumenteren. Het doel is de agentcode te instrumenteren zodat deze traces en metrics uitstoot die kunnen worden vastgelegd, verwerkt en gevisualiseerd door een observeerbaarheidsplatform.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) is uitgegroeid tot een industriestandaard voor LLM-observeerbaarheid. Het biedt een set API's, SDK's en tools voor het genereren, verzamelen en exporteren van telemetriedata.

Er zijn veel instrumentatielibraries die bestaande agentframeworks omsluiten en het makkelijk maken OpenTelemetry spans naar een observeerbaarheidstool te exporteren. Microsoft Agent Framework integreert natively met OpenTelemetry. Hieronder staat een voorbeeld van het instrumenteren van een MAF-agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agentuitvoering wordt automatisch gevolgd
    pass
```

Het [voorbeeldnotebook](./code_samples/10-expense_claim-demo.ipynb) in dit hoofdstuk demonstreert hoe je je MAF-agent instrumenteert.

**Handmatige spancreatie:** Hoewel instrumentatielibraries een goede basis bieden, zijn er vaak gevallen waarin meer gedetailleerde of aangepaste informatie nodig is. Je kunt spans handmatig creëren om aangepaste applicatielogica toe te voegen. Belangrijker, ze kunnen automatisch of handmatig gemaakte spans verrijken met eigen attributen (ook bekend als tags of metadata). Deze attributen kunnen bedrijfsspecifieke data, tussenberekeningen of elke context bevatten die nuttig kan zijn voor debugging of analyse, zoals `user_id`, `session_id` of `model_version`.

Voorbeeld van het handmatig creëren van traces en spans met de [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agent Evaluatie

Observeerbaarheid geeft ons statistieken, maar evaluatie is het proces van het analyseren van die data (en het uitvoeren van tests) om te bepalen hoe goed een AI-agent presteert en hoe die verbeterd kan worden. Met andere woorden, zodra je die traces en metrics hebt, hoe gebruik je die dan om de agent te beoordelen en beslissingen te nemen?

Regelmatige evaluatie is belangrijk omdat AI-agenten vaak niet-deterministisch zijn en kunnen evolueren (via updates of drift in modelgedrag) – zonder evaluatie zou je niet weten of je “slimme agent” zijn werk goed doet of juist achteruit is gegaan.

Er zijn twee categorieën evaluaties voor AI-agenten: **online evaluatie** en **offline evaluatie**. Beide zijn waardevol en vullen elkaar aan. We beginnen meestal met offline evaluatie, omdat dit de minimale noodzakelijke stap is voordat een agent wordt uitgerold.

### Offline Evaluatie

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Dit houdt in dat je de agent evalueert in een gecontroleerde omgeving, meestal met testdatasets, niet met live gebruikersvragen. Je gebruikt samengestelde datasets waarvan je weet wat de verwachte output of correct gedrag is, en vervolgens laat je je agent daarop draaien.

Bijvoorbeeld, als je een agent hebt gebouwd voor wiskundige tekstproblemen, heb je misschien een [testdataset](https://huggingface.co/datasets/gsm8k) van 100 problemen met bekende antwoorden. Offline evaluatie wordt vaak tijdens ontwikkeling gedaan (en kan onderdeel zijn van CI/CD-pijplijnen) om verbeteringen te controleren of regressies te voorkomen. Het voordeel is dat het **herhaalbaar is en je duidelijke nauwkeurigheidsstatistieken krijgt omdat de grondwaarheid bekend is**. Je kunt ook gebruikersvragen simuleren en de reacties van de agent meten tegen ideale antwoorden of automatische metrics gebruiken zoals hierboven beschreven.

De belangrijkste uitdaging bij offline evaluatie is ervoor te zorgen dat je testdataset volledig en relevant blijft – de agent kan goed presteren op een vaste testset, maar in productie heel andere vragen tegenkomen. Daarom moet je testsets updaten met nieuwe edge cases en voorbeelden die echte scenario’s weerspiegelen. Een mix van kleine “rooktest” cases en grotere evaluatiesets is nuttig: kleine sets voor snelle checks en grotere sets voor bredere prestatienormen.

### Online Evaluatie

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Dit verwijst naar het evalueren van de agent in een live, echte wereldomgeving, dus tijdens daadwerkelijk gebruik in productie. Online evaluatie houdt in dat je continu de prestaties bij echte gebruikersinteracties monitort en uitkomsten analyseert.

Bijvoorbeeld, je kunt succespercentages, gebruikersbeoordelingen of andere metrics op live verkeer bijhouden. Het voordeel van online evaluatie is dat het **dingen vastlegt die je in een laboratoriumomgeving misschien niet verwacht** – je kunt model drift over tijd waarnemen (als de effectiviteit van de agent afneemt als invoerpatronen veranderen) en onverwachte queries of situaties ontdekken die niet in je testdata zaten. Het geeft een waarheidsgetrouw beeld van hoe de agent in het wild functioneert.

Online evaluatie omvat vaak het verzamelen van impliciete en expliciete gebruikersfeedback, zoals besproken, en mogelijk het draaien van schaduwtests of A/B-tests (waarbij een nieuwe agentversie parallel draait om te vergelijken met de oude). De uitdaging is dat het lastig kan zijn betrouwbare labels of scores te verkrijgen voor live interacties – je kunt dan vertrouwen op gebruikersfeedback of downstream metrics (zoals of de gebruiker op het resultaat klikte).

### De twee combineren

Online en offline evaluaties sluiten elkaar niet uit; ze zijn juist sterk aanvullend. Inzichten uit online monitoring (bijvoorbeeld nieuwe soorten gebruikersvragen waarbij de agent slecht presteert) kunnen worden gebruikt om offline testdatasets uit te breiden en verbeteren. Omgekeerd kunnen agenten die offline goed presteren, daarna met meer vertrouwen online worden uitgerold en bewaakt.

Veel teams hanteren in feite een cyclus:

_offline evalueren -> uitrollen -> online monitoren -> nieuwe faalgevallen verzamelen -> toevoegen aan offline dataset -> agent verfijnen -> herhalen_.

## Veelvoorkomende problemen

Bij het uitrollen van AI-agenten in productie kun je verschillende uitdagingen tegenkomen. Hier zijn enkele veelvoorkomende problemen en mogelijke oplossingen:

| **Probleem**    | **Potentiële oplossing**   |
| ------------- | ------------------ |
| AI-agent voert taken niet consistent uit | - Verfijn de prompt die aan de AI-agent gegeven wordt; wees duidelijk over doelstellingen.<br>- Identificeer waar het opdelen van taken in subtaken en afhandelen door meerdere agenten kan helpen. |
| AI-agent raakt vast in continue lussen  | - Zorg voor duidelijke stopvoorwaarden zodat de agent weet wanneer het proces moet stoppen.<br>- Voor complexe taken die redeneren en plannen vereisen, gebruik een groter model dat gespecialiseerd is in redeneervaardigheden. |
| AI-agent toolaanroepen werken niet goed   | - Test en valideer de output van de tool buiten het agentsysteem.<br>- Verfijn de gedefinieerde parameters, prompts en benamingen van tools.  |
| Multi-agent systeem werkt niet consistent | - Verfijn de prompts voor elke agent zodat ze specifiek en onderscheidend zijn.<br>- Bouw een hiërarchisch systeem met een "routing" of controller-agent die bepaalt welke agent geschikt is. |

Veel van deze problemen kunnen effectiever worden geïdentificeerd als observeerbaarheid is geïmplementeerd. De traces en metrics die we eerder bespraken helpen precies te lokaliseren waar in de agentworkflow problemen optreden, waardoor debugging en optimalisatie veel efficiënter worden.

## Kosten beheren


Hier zijn enkele strategieën om de kosten van het inzetten van AI-agenten in productie te beheersen:

**Gebruik van Kleinere Modellen:** Kleine Taalmodellen (SLMs) kunnen goed presteren bij bepaalde agentuse-cases en zullen de kosten aanzienlijk verlagen. Zoals eerder vermeld, is het opzetten van een evaluatiesysteem om de prestaties te bepalen en te vergelijken met grotere modellen de beste manier om te begrijpen hoe goed een SLM zal presteren voor jouw use case. Overweeg het gebruik van SLMs voor eenvoudigere taken zoals intentieclassificatie of parameterextractie, terwijl je grotere modellen reserveert voor complexe redenering.

**Gebruik van een Routermodel:** Een soortgelijke strategie is het gebruik van een diversiteit aan modellen en groottes. Je kunt een LLM/SLM of serverless functie gebruiken om verzoeken op basis van complexiteit door te sturen naar de best passende modellen. Dit zal ook helpen om kosten te verlagen en tegelijkertijd prestaties op de juiste taken te garanderen. Bijvoorbeeld, stuur eenvoudige vragen naar kleinere, snellere modellen, en gebruik dure grote modellen alleen voor complexe redeneertaken.

**Caching van Reacties:** Veelvoorkomende verzoeken en taken identificeren en de antwoorden leveren voordat ze door je agentensysteem gaan, is een goede manier om het volume van soortgelijke verzoeken te verminderen. Je kunt zelfs een flow implementeren om te bepalen hoe vergelijkbaar een verzoek is met je gecachte verzoeken met behulp van meer basale AI-modellen. Deze strategie kan de kosten aanzienlijk verlagen voor veelgestelde vragen of gemeenschappelijke workflows.

## Laten we zien hoe dit in de praktijk werkt

In het [voorbeeldnotebook van deze sectie](./code_samples/10-expense_claim-demo.ipynb) zien we voorbeelden van hoe we observability tools kunnen gebruiken om onze agent te monitoren en te evalueren.


### Meer vragen over AI-agenten in productie?

Sluit je aan bij de [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) om andere leerlingen te ontmoeten, deel te nemen aan office hours en je vragen over AI-agenten beantwoord te krijgen.

## Vorige les

[Metacognition Design Pattern](../09-metacognition/README.md)

## Volgende les

[Agentic Protocols](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->