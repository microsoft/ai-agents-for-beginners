# AI-agents in productie: Observeerbaarheid & Evaluatie

[![AI-agents in productie](../../../translated_images/nl/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Naarmate AI-agents evolueren van experimentele prototypes naar toepassingen in de echte wereld, wordt het belangrijk om hun gedrag te begrijpen, hun prestaties te monitoren en hun uitkomsten systematisch te evalueren.

## Leerdoelen

Na het voltooien van deze les weet je hoe/begrijp je:
- Kernconcepten van observeerbaarheid en evaluatie van agents
- Technieken om de prestaties, kosten en effectiviteit van agents te verbeteren
- Wat en hoe je je AI-agents systematisch evalueert
- Hoe je kosten kunt beheersen bij het in productie nemen van AI-agents
- Hoe je agents kunt instrumenteren die zijn gebouwd met Microsoft Agent Framework

Het doel is je de kennis te geven om je "black box" agents te transformeren naar transparante, beheersbare en betrouwbare systemen.

_**Opmerking:** Het is belangrijk om AI-agents te implementeren die veilig en betrouwbaar zijn. Bekijk ook de les [Building Trustworthy AI Agents](./06-building-trustworthy-agents/README.md)._

## Traces en Spans

Observeerbaarheidstools zoals [Langfuse](https://langfuse.com/) of [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) stellen agent-runs meestal voor als traces en spans.

- **Trace** vertegenwoordigt een volledige agenttaak van begin tot eind (zoals het afhandelen van een gebruikersvraag).
- **Spans** zijn individuele stappen binnen de trace (zoals het aanroepen van een taalmodel of het ophalen van gegevens).

![Traceboom in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Zonder observeerbaarheid kan een AI-agent aanvoelen als een "black box" – de interne staat en redenering zijn ondoorzichtig, wat het moeilijk maakt om problemen te diagnosticeren of prestaties te optimaliseren. Met observeerbaarheid veranderen agents in "glass boxes" en bieden ze de transparantie die essentieel is voor het opbouwen van vertrouwen en ervoor te zorgen dat ze werken zoals bedoeld. 

## Waarom observeerbaarheid belangrijk is in productieomgevingen

Het overbrengen van AI-agents naar productieomgevingen brengt een nieuwe reeks uitdagingen en vereisten met zich mee. Observeerbaarheid is niet langer een "nice-to-have" maar een kritische capaciteit:

*   **Foutopsporing en oorzaakanalyse**: Wanneer een agent faalt of een onverwacht resultaat produceert, bieden observeerbaarheidstools de traces die nodig zijn om de bron van de fout te achterhalen. Dit is vooral belangrijk bij complexe agents die meerdere LLM-aanroepen, toolinteracties en conditionele logica kunnen omvatten.
*   **Latentie- en kostenbeheer**: AI-agents vertrouwen vaak op LLM's en andere externe API's die per token of per oproep worden gefactureerd. Observeerbaarheid maakt nauwkeurige tracking van deze oproepen mogelijk, zodat je operaties kunt identificeren die onnodig traag of duur zijn. Dit stelt teams in staat prompts te optimaliseren, efficiëntere modellen te kiezen of workflows te herontwerpen om operationele kosten te beheersen en een goede gebruikerservaring te waarborgen.
*   **Vertrouwen, veiligheid en naleving**: In veel toepassingen is het belangrijk te zorgen dat agents veilig en ethisch handelen. Observeerbaarheid levert een audittrail van agentacties en -beslissingen. Dit kan worden gebruikt om problemen zoals promptinjectie, het genereren van schadelijke inhoud of het onjuist omgaan met persoonsidentificeerbare informatie (PII) te detecteren en te mitigeren. Je kunt bijvoorbeeld traces bekijken om te begrijpen waarom een agent een bepaald antwoord gaf of een specifieke tool gebruikte.
*   **Continue verbeteringslussen**: Observeerbaarheidsdata vormt de basis voor een iteratief ontwikkelproces. Door te monitoren hoe agents presteren in de echte wereld, kunnen teams verbeterpunten identificeren, data verzamelen voor het fijnslijpen van modellen en de impact van wijzigingen valideren. Dit creëert een feedbackloop waarbij inzichten uit online evaluatie offline experimenten en verfijning informeren, wat leidt tot steeds betere agentprestaties.

## Belangrijke metrics om te volgen

Om het gedrag van agents te monitoren en te begrijpen, moet een reeks metrics en signalen worden bijgehouden. Hoewel de specifieke metrics kunnen variëren afhankelijk van het doel van de agent, zijn sommige universeel belangrijk.

Hier zijn enkele van de meest voorkomende metrics die observeerbaarheidstools monitoren:

**Latentie:** Hoe snel reageert de agent? Lange wachttijden hebben een negatieve invloed op de gebruikerservaring. Je zou latentie voor taken en individuele stappen moeten meten door agent-runs te traceren. Bijvoorbeeld, een agent die 20 seconden nodig heeft voor alle modelaanroepen kan worden versneld door een sneller model te gebruiken of modelaanroepen parallel uit te voeren.

**Kosten:** Wat zijn de kosten per agent-run? AI-agents vertrouwen op LLM-aanroepen die per token worden gefactureerd of op externe API's. Frequent gebruik van tools of meerdere prompts kan de kosten snel verhogen. Als een agent bijvoorbeeld een LLM vijf keer aanroept voor een marginale kwaliteitsverbetering, moet je beoordelen of die kosten gerechtvaardigd zijn of dat je het aantal oproepen kunt verminderen of een goedkoper model kunt gebruiken. Realtime monitoring kan ook onverwachte pieken identificeren (bijv. bugs die leiden tot excessieve API-lussen).

**Verzoekfouten:** Hoeveel verzoeken zijn er mislukt? Dit kan API-fouten of mislukte toolaanroepen omvatten. Om je agent robuuster te maken in productie, kun je dan fallback- of retry-mechanismen instellen. Bijv. als LLM-provider A uitvalt, schakel je over naar LLM-provider B als reserve.

**Gebruikersfeedback:** Het implementeren van directe gebruikersbeoordelingen levert waardevolle inzichten op. Dit kan expliciete beoordelingen omvatten (👍thumbs-up/👎down, ⭐1-5 sterren) of tekstuele opmerkingen. Aanhoudend negatieve feedback moet een waarschuwing zijn dat de agent niet werkt zoals verwacht. 

**Impliciete gebruikersfeedback:** Gebruikersgedrag biedt indirecte feedback, zelfs zonder expliciete beoordelingen. Dit kan onmiddellijke herformulering van vragen, herhaalde queries of het klikken op een retry-knop omvatten. Bijv. als je ziet dat gebruikers herhaaldelijk dezelfde vraag stellen, is dat een teken dat de agent niet functioneert zoals verwacht.

**Nauwkeurigheid:** Hoe vaak produceert de agent correcte of gewenste outputs? Definities van nauwkeurigheid variëren (bijv. correctheid van probleemoplossing, nauwkeurigheid van informatieopvraging, gebruikerstevredenheid). De eerste stap is te definiëren hoe succes eruitziet voor jouw agent. Je kunt nauwkeurigheid volgen via geautomatiseerde controles, evaluatiescores of taakvoltooiingslabels. Bijvoorbeeld, traces markeren als "geslaagd" of "mislukt". 

**Geautomatiseerde evaluatiemetrics:** Je kunt ook geautomatiseerde evaluaties opzetten. Bijvoorbeeld, je kunt een LLM gebruiken om de output van de agent te scoren, bijv. of deze behulpzaam of nauwkeurig is. Er zijn ook verschillende open-sourcebibliotheken die helpen verschillende aspecten van de agent te scoren, bijv. [RAGAS](https://docs.ragas.io/) voor RAG-agents of [LLM Guard](https://llm-guard.com/) om schadelijke taal of promptinjectie te detecteren. 

In de praktijk geeft een combinatie van deze metrics de beste dekking van de gezondheid van een AI-agent. In het [voorbeeldnotebook](./code_samples/10-expense_claim-demo.ipynb) van dit hoofdstuk laten we zien hoe deze metrics eruitzien in echte voorbeelden, maar eerst leren we hoe een typische evaluatieworkflow eruitziet.

## Instrumenteer je agent

Om tracegegevens te verzamelen, moet je je code instrumenteren. Het doel is de agentcode te instrumenteren zodat deze traces en metrics genereert die door een observeerbaarheidsplatform kunnen worden vastgelegd, verwerkt en gevisualiseerd.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) is uitgegroeid tot een industrieel standaard voor LLM-observeerbaarheid. Het biedt een set API's, SDK's en tools voor het genereren, verzamelen en exporteren van telemetriedata. 

Er zijn veel instrumentatielibraries die bestaande agentframeworks omhullen en het eenvoudig maken om OpenTelemetry-spans naar een observeerbaarheidstool te exporteren. Microsoft Agent Framework integreert native met OpenTelemetry. Hieronder een voorbeeld van het instrumenteren van een MAF-agent:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # De uitvoering van de agent wordt automatisch gevolgd
    pass
```

Het [voorbeeldnotebook](./code_samples/10-expense_claim-demo.ipynb) in dit hoofdstuk demonstreert hoe je je MAF-agent kunt instrumenteren.

**Handmatig aanmaken van spans:** Hoewel instrumentatielibraries een goede basis bieden, zijn er vaak gevallen waarin meer gedetailleerde of aangepaste informatie nodig is. Je kunt handmatig spans aanmaken om aangepaste applicatielogica toe te voegen. Belangrijker nog, je kunt automatisch of handmatig aangemaakte spans verrijken met aangepaste attributen (ook bekend als tags of metadata). Deze attributen kunnen bedrijfsspecifieke gegevens, tussentijdse berekeningen of elke context bevatten die nuttig kan zijn voor debugging of analyse, zoals `user_id`, `session_id` of `model_version`.

Example on creating traces and spans manually with the [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agent-evaluatie

Observeerbaarheid levert ons metrics, maar evaluatie is het proces van het analyseren van die data (en het uitvoeren van tests) om te bepalen hoe goed een AI-agent presteert en hoe deze kan worden verbeterd. Met andere woorden, zodra je die traces en metrics hebt, hoe gebruik je ze om de agent te beoordelen en beslissingen te nemen? 

Regelmatige evaluatie is belangrijk omdat AI-agents vaak niet-deterministisch zijn en kunnen evolueren (door updates of drift in modelgedrag) – zonder evaluatie zou je niet weten of je "slimme agent" zijn werk goed doet of is teruggevallen.

Er zijn twee categorieën evaluaties voor AI-agents: **online-evaluatie** en **offline-evaluatie**. Beide zijn waardevol en vullen elkaar aan. We beginnen meestal met offline-evaluatie, omdat dit de minimale noodzakelijke stap is voordat je een agent in productie neemt.

### Offline-evaluatie

![Datasetitems in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Dit houdt in dat je de agent in een gecontroleerde omgeving evalueert, doorgaans met testdatasets en niet met live gebruikersqueries. Je gebruikt samengestelde datasets waarbij je weet wat de verwachte output of het correcte gedrag is en voert je agent daarop uit. 

Als je bijvoorbeeld een agent hebt gebouwd voor wiskundige verhaaltjessommen, kun je een [testdataset](https://huggingface.co/datasets/gsm8k) hebben van 100 problemen met bekende antwoorden. Offline-evaluatie wordt vaak tijdens de ontwikkeling gedaan (en kan deel uitmaken van CI/CD-pijplijnen) om verbeteringen te controleren of regressies te voorkomen. Het voordeel is dat het **herhaalbaar is en je heldere nauwkeurigheidsmetrics kunt krijgen omdat je grondwaarheid hebt**. Je kunt ook gebruikersqueries simuleren en de reacties van de agent meten aan de hand van ideale antwoorden of geautomatiseerde metrics zoals hierboven beschreven. 

De belangrijkste uitdaging bij offline-evaluatie is ervoor te zorgen dat je testdataset volledig is en relevant blijft – de agent kan goed presteren op een vaste testset maar heel andere queries tegenkomen in productie. Daarom moet je testsets bijwerken met nieuwe randgevallen en voorbeelden die echte scenario's weerspiegelen​. Een mix van kleine "smoke-test" gevallen en grotere evaluatiesets is nuttig: kleine sets voor snelle controles en grotere voor bredere prestatiestatistieken​.

### Online-evaluatie 

![Overzicht van observeerbaarheidsmetrics](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Dit verwijst naar het evalueren van de agent in een live, echte omgeving, d.w.z. tijdens daadwerkelijk gebruik in productie. Online-evaluatie omvat het monitoren van de prestaties van de agent bij echte gebruikersinteracties en het continu analyseren van uitkomsten. 

Bijvoorbeeld, je kunt slagingspercentages, gebruikerstevredenheidsscores of andere metrics op live verkeer bijhouden. Het voordeel van online-evaluatie is dat het **dingen vastlegt die je mogelijk niet in een labsetting voorziet** – je kunt modeldrift in de loop van de tijd waarnemen (als de effectiviteit van de agent afneemt doordat invoerpatronen veranderen) en onverwachte queries of situaties opvangen die niet in je testdata stonden​. Het geeft een waarheidsgetrouw beeld van hoe de agent zich in het wild gedraagt. 

Online-evaluatie omvat vaak het verzamelen van impliciete en expliciete gebruikersfeedback, zoals eerder besproken, en het eventueel uitvoeren van shadow-tests of A/B-tests (waarbij een nieuwe versie van de agent parallel draait om te vergelijken met de oude). De uitdaging is dat het lastig kan zijn om betrouwbare labels of scores voor live-interacties te krijgen – je moet mogelijk vertrouwen op gebruikersfeedback of downstream-metrics (zoals heeft de gebruiker op het resultaat geklikt).

### Combineren van beide

Online- en offline-evaluaties sluiten elkaar niet uit; ze vullen elkaar juist goed aan. Inzichten uit online monitoring (bijv. nieuwe typen gebruikersqueries waarbij de agent slecht presteert) kunnen worden gebruikt om offline testdatasets aan te vullen en te verbeteren. Omgekeerd kunnen agents die goed presteren in offline-tests vervolgens met meer vertrouwen worden uitgerold en online worden gemonitord. 

Veel teams hanteren in feite een lus:

_evalueer offline -> implementeer -> monitor online -> verzamel nieuwe faalgevallen -> voeg toe aan offline dataset -> verfijn agent -> herhaal_.

## Veelvoorkomende problemen

Bij het uitrollen van AI-agents naar productie kun je verschillende uitdagingen tegenkomen. Hier zijn enkele veelvoorkomende problemen en mogelijke oplossingen:

| **Issue**    | **Potential Solution**   |
| ------------- | ------------------ |
| AI Agent not performing tasks consistently | - Verfijn de prompt die aan de AI-agent wordt gegeven; wees duidelijk over de doelstellingen.<br>- Identificeer waar het opsplitsen van taken in subtaken en het laten afhandelen door meerdere agents kan helpen. |
| AI Agent running into continuous loops  | - Zorg dat je duidelijke terminatievoorwaarden hebt zodat de Agent weet wanneer het proces moet stoppen.<br>- Voor complexe taken die redeneren en plannen vereisen, gebruik een groter model dat gespecialiseerd is in redeneertaken. |
| AI Agent tool calls are not performing well   | - Test en valideer de output van de tool buiten het agentsysteem.<br>- Verfijn de gedefinieerde parameters, prompts en de naamgeving van tools.  |
| Multi-Agent system not performing consistently | - Verfijn de prompts die aan elke agent worden gegeven zodat ze specifiek zijn en van elkaar te onderscheiden.<br>- Bouw een hiërarchisch systeem met een "routing" of controller-agent om te bepalen welke agent de juiste is. |

Veel van deze problemen kunnen effectiever worden geïdentificeerd met observeerbaarheid op zijn plaats. De traces en metrics die we eerder bespraken helpen precies te bepalen waar in de agentworkflow problemen optreden, waardoor debugging en optimalisatie veel efficiënter worden.

## Kosten beheren
Hier zijn enkele strategieën om de kosten van het inzetten van AI-agenten in productie te beheersen:

**Het gebruik van kleinere modellen:** Kleine taalmodellen (SLMs) kunnen goed presteren bij bepaalde agentische use-cases en zullen de kosten aanzienlijk verlagen. Zoals eerder vermeld, is het bouwen van een evaluatiesysteem om prestaties te bepalen en te vergelijken met grotere modellen de beste manier om te begrijpen hoe goed een SLM zal presteren voor jouw use-case. Overweeg SLMs te gebruiken voor eenvoudigere taken zoals intentieclassificatie of parameterextractie, en reserveer grotere modellen voor complexere redenering.

**Het gebruik van een routermodel:** Een vergelijkbare strategie is het gebruik van een diversiteit aan modellen en groottes. Je kunt een LLM/SLM of een serverless-functie gebruiken om verzoeken op basis van complexiteit naar de meest geschikte modellen te routeren. Dit helpt ook de kosten te verlagen en zorgt ervoor dat prestaties optimaal zijn voor de juiste taken. Route bijvoorbeeld eenvoudige vragen naar kleinere, snellere modellen, en gebruik dure grote modellen alleen voor complexe redeneringstaken.

**Caching van antwoorden:** Het identificeren van veelvoorkomende verzoeken en taken en het vooraf leveren van de antwoorden voordat ze door je agentische systeem gaan, is een goede manier om het volume van vergelijkbare verzoeken te verminderen. Je kunt zelfs een stroom implementeren om te bepalen hoe vergelijkbaar een verzoek is met je gecachte verzoeken met behulp van meer basale AI-modellen. Deze strategie kan de kosten aanzienlijk verlagen voor veelgestelde vragen of veelvoorkomende workflows.

## Laten we eens kijken hoe dit in de praktijk werkt

In de [voorbeeldnotebook van deze sectie](./code_samples/10-expense_claim-demo.ipynb) zullen we voorbeelden zien van hoe we observability-tools kunnen gebruiken om onze agent te monitoren en te evalueren.

### Meer vragen over AI-agenten in productie?

Sluit je aan bij de [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) om andere deelnemers te ontmoeten, spreekuren bij te wonen en antwoorden op je vragen over AI-agenten te krijgen.

## Previous Lesson

[Ontwerppatroon metacognitie](../09-metacognition/README.md)

## Next Lesson

[Agentische protocollen](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dit document is vertaald met behulp van de AI-vertalingsservice Co-op Translator (https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onjuistheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->