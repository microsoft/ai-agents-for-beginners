# AI-agents in productie: Observeerbaarheid & Evaluatie

[![AI-agents in productie](../../../translated_images/nl/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Naarmate AI-agents verschuiven van experimentele prototypes naar toepassingen in de echte wereld, wordt het vermogen om hun gedrag te begrijpen, hun prestaties te monitoren en hun output systematisch te evalueren belangrijk.

## Leerdoelen

Na het voltooien van deze les weet je hoe/begrijp je:
- Kernconcepten van agent-observeerbaarheid en evaluatie
- Technieken om de prestaties, kosten en effectiviteit van agents te verbeteren
- Wat en hoe je je AI-agents systematisch moet evalueren
- Hoe je kosten onder controle houdt bij het inzetten van AI-agents in productie
- Hoe je agents gebouwd met AutoGen instrumenteert

Het doel is je uit te rusten met de kennis om je "black box" agents te transformeren naar transparante, beheersbare en betrouwbare systemen.

_**Opmerking:** Het is belangrijk om AI-agents te implementeren die veilig en betrouwbaar zijn. Bekijk ook de les [Betrouwbare AI-agents bouwen](../06-building-trustworthy-agents/README.md)._

## Traces en Spans

Observeerbaarheidstools zoals [Langfuse](https://langfuse.com/) of [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) representeren agent-runs gewoonlijk als traces en spans.

- **Trace** vertegenwoordigt een volledige agenttaak van begin tot eind (zoals het afhandelen van een gebruikersquery).
- **Spans** zijn individuele stappen binnen de trace (zoals het aanroepen van een taalmodel of het ophalen van gegevens).

![Traceboom in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Zonder observeerbaarheid kan een AI-agent aanvoelen als een "zwarte doos" - de interne staat en redenering zijn ondoorzichtig, wat het moeilijk maakt om problemen te diagnosticeren of prestaties te optimaliseren. Met observeerbaarheid worden agents "doorzichtige systemen", die transparantie bieden die essentieel is voor het opbouwen van vertrouwen en ervoor zorgen dat ze werken zoals bedoeld.

## Waarom observeerbaarheid belangrijk is in productieomgevingen

Het overbrengen van AI-agents naar productieomgevingen brengt een nieuwe reeks uitdagingen en vereisten met zich mee. Observeerbaarheid is niet langer "leuk om te hebben" maar een kritische capaciteit:

*   **Debugging en root-cause analyse**: Wanneer een agent faalt of een onverwachte output produceert, bieden observeerbaarheidstools de traces die nodig zijn om de bron van de fout te achterhalen. Dit is vooral belangrijk bij complexe agents die meerdere LLM-aanroepen, toolinteracties en conditionele logica kunnen omvatten.
*   **Latentie- en kostenbeheer**: AI-agents vertrouwen vaak op LLMs en andere externe API's die per token of per oproep in rekening worden gebracht. Observeerbaarheid maakt het mogelijk deze oproepen nauwkeurig te volgen, waardoor je bedrijfsprocessen kunt identificeren die buitensporig traag of duur zijn. Dit stelt teams in staat prompts te optimaliseren, efficiëntere modellen te kiezen of workflows te herontwerpen om operationele kosten te beheersen en een goede gebruikerservaring te garanderen.
*   **Vertrouwen, veiligheid en naleving**: In veel toepassingen is het belangrijk om ervoor te zorgen dat agents veilig en ethisch handelen. Observeerbaarheid biedt een audittrail van agentacties en -beslissingen. Dit kan worden gebruikt om problemen zoals prompt-injectie, het genereren van schadelijke inhoud of het onjuist omgaan met persoonlijk identificeerbare informatie (PII) te detecteren en te mitigeren. Bijvoorbeeld, je kunt traces terugkijken om te begrijpen waarom een agent een bepaalde reactie gaf of een specifiek hulpmiddel gebruikte.
*   **Continue verbeteringslussen**: Observeerbaarheidsgegevens vormen de basis van een iteratief ontwikkelproces. Door te monitoren hoe agents presteren in de echte wereld, kunnen teams verbetergebieden identificeren, gegevens verzamelen voor het fijnregelen van modellen en de impact van veranderingen valideren. Dit creëert een feedbackloop waarbij inzichten uit online evaluatie in productie offline experimenten en verfijning informeren, wat leidt tot steeds betere agentprestaties.

## Belangrijke metrics om te volgen

Om het gedrag van agents te monitoren en te begrijpen, moet een reeks metrics en signalen worden bijgehouden. Hoewel de specifieke metrics kunnen variëren afhankelijk van het doel van de agent, zijn sommige universeel belangrijk.

Hier zijn enkele van de meest voorkomende metrics die observeerbaarheidstools monitoren:

**Latentie:** Hoe snel reageert de agent? Lange wachttijden beïnvloeden de gebruikerservaring negatief. Je zou latentie voor taken en individuele stappen moeten meten door agent-runs te traceren. Bijvoorbeeld, een agent die 20 seconden nodig heeft voor alle modelaanroepen kan worden versneld door een sneller model te gebruiken of modelaanroepen parallel uit te voeren.

**Kosten:** Wat zijn de kosten per agent-run? AI-agents vertrouwen op LLM-aanroepen die per token worden gefactureerd of op externe API's. Frequent gebruik van tools of meerdere prompts kan snel de kosten verhogen. Bijvoorbeeld, als een agent een LLM vijf keer aanroept voor marginaal betere kwaliteit, moet je beoordelen of de kosten gerechtvaardigd zijn of dat je het aantal oproepen kunt verminderen of een goedkoper model kunt gebruiken. Real-time monitoring kan ook helpen onverwachte pieken te identificeren (bijv. bugs die buitensporige API-lussen veroorzaken).

**Requestfouten:** Hoeveel verzoeken faalden? Dit kan API-fouten of mislukte tool-aanroepen omvatten. Om je agent robuuster te maken tegen deze fouten in productie, kun je valbacks of retries instellen. Bijv. als LLM-provider A down is, schakel je over naar LLM-provider B als back-up.

**Gebruikersfeedback:** Het implementeren van directe gebruikersevaluaties levert waardevolle inzichten op. Dit kan expliciete beoordelingen omvatten (👍thumbs-up/👎down, ⭐1-5 sterren) of tekstuele opmerkingen. Consistente negatieve feedback zou je moeten waarschuwen omdat dit een teken is dat de agent niet werkt zoals verwacht.

**Impliciete gebruikersfeedback:** Gebruikersgedrag levert indirecte feedback, zelfs zonder expliciete beoordelingen. Dit kan onmiddellijke herformuleringen van vragen, herhaalde queries of het klikken op een retry-knop omvatten. Bijv. als je ziet dat gebruikers herhaaldelijk dezelfde vraag stellen, is dat een teken dat de agent niet werkt zoals verwacht.

**Nauwkeurigheid:** Hoe vaak produceert de agent correcte of wenselijke outputs? Definities van nauwkeurigheid variëren (bijv. juistheid van probleemoplossing, nauwkeurigheid van informatieopvraging, gebruikerstevredenheid). De eerste stap is definiëren hoe succes eruitziet voor je agent. Je kunt nauwkeurigheid volgen via geautomatiseerde controles, evaluatiescores of taakvoltooiingslabels. Bijvoorbeeld door traces te markeren als "succeeded" of "failed".

**Geautomatiseerde evaluatiemetrics:** Je kunt ook geautomatiseerde evaluaties opzetten. Bijvoorbeeld, je kunt een LLM gebruiken om de output van de agent te scoren, bv. of deze behulpzaam, accuraat of niet is. Er zijn ook verschillende open source bibliotheken die je helpen om verschillende aspecten van de agent te scoren. Bijv. [RAGAS](https://docs.ragas.io/) voor RAG-agents of [LLM Guard](https://llm-guard.com/) om schadelijke taal of prompt-injectie te detecteren.

In de praktijk geeft een combinatie van deze metrics de beste dekking van de gezondheid van een AI-agent. In dit hoofdstuk [voorbeeldnotebook](./code_samples/10_autogen_evaluation.ipynb) laten we zien hoe deze metrics eruitzien in echte voorbeelden, maar eerst leren we hoe een typische evaluatieworkflow eruitziet.

## Instrumenteer je Agent

Om tracinggegevens te verzamelen, moet je je code instrumenteren. Het doel is de agentcode te instrumenteren zodat er traces en metrics worden uitgezonden die kunnen worden vastgelegd, verwerkt en gevisualiseerd door een observeerbaarheidsplatform.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) is uitgegroeid tot een industrienorm voor LLM-observeerbaarheid. Het biedt een set API's, SDK's en tools voor het genereren, verzamelen en exporteren van telemetriegegevens.

Er zijn veel instrumentatielibraries die bestaande agentframeworks wrappen en het gemakkelijk maken OpenTelemetry-spans naar een observeerbaarheidstool te exporteren. Hieronder staat een voorbeeld van het instrumenteren van een AutoGen-agent met de [OpenLit instrumentation library](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

Het [voorbeeldnotebook](./code_samples/10_autogen_evaluation.ipynb) in dit hoofdstuk zal demonstreren hoe je je AutoGen-agent instrumenteert.

**Handmatige spancreatie:** Hoewel instrumentatielibraries een goede basis bieden, zijn er vaak gevallen waarin meer gedetailleerde of aangepaste informatie nodig is. Je kunt handmatig spans aanmaken om aangepaste toepassingslogica toe te voegen. Belangrijker nog, je kunt automatisch of handmatig aangemaakte spans verrijken met aangepaste attributen (ook bekend als tags of metadata). Deze attributen kunnen bedrijfsspecifieke gegevens, tussenberekeningen of enige context omvatten die nuttig kan zijn voor debugging of analyse, zoals `user_id`, `session_id`, of `model_version`.

Voorbeeld van het handmatig aanmaken van traces en spans met de [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agent-evaluatie

Observeerbaarheid geeft ons metrics, maar evaluatie is het proces van het analyseren van die gegevens (en het uitvoeren van tests) om te bepalen hoe goed een AI-agent presteert en hoe deze kan worden verbeterd. Met andere woorden: zodra je die traces en metrics hebt, hoe gebruik je ze om de agent te beoordelen en beslissingen te nemen?

Regelmatige evaluatie is belangrijk omdat AI-agents vaak niet-deterministisch zijn en kunnen evolueren (door updates of veranderend modelgedrag) – zonder evaluatie weet je niet of je "slimme agent" daadwerkelijk zijn werk goed doet of dat hij is achteruitgegaan.

Er zijn twee categorieën van evaluaties voor AI-agents: **online evaluatie** en **offline evaluatie**. Beide zijn waardevol en vullen elkaar aan. Meestal beginnen we met offline evaluatie, omdat dit de minimale noodzakelijke stap is voordat je een agent inzet.

### Offline evaluatie

![Dataset-items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Dit houdt in dat je de agent evalueert in een gecontroleerde omgeving, typisch met behulp van testdatasets, niet met live gebruikersqueries. Je gebruikt samengestelde datasets waarbij je weet wat de verwachte output of correct gedrag is, en voert vervolgens je agent daarop uit.

Bijvoorbeeld, als je een agent voor wiskundige tekstproblemen hebt gebouwd, kun je een [testdataset](https://huggingface.co/datasets/gsm8k) van 100 problemen met bekende antwoorden hebben. Offline evaluatie wordt vaak gedaan tijdens ontwikkeling (en kan deel uitmaken van CI/CD-pijplijnen) om verbeteringen te controleren of achteruitgang te voorkomen. Het voordeel is dat het **herhaalbaar is en je duidelijke nauwkeurigheidsmetingen kunt krijgen omdat je grondwaarheid hebt**. Je kunt ook gebruikersqueries simuleren en de reacties van de agent meten ten opzichte van ideale antwoorden of geautomatiseerde metrics gebruiken zoals hierboven beschreven.

De belangrijkste uitdaging bij offline evaluatie is ervoor te zorgen dat je testdataset allesomvattend en relevant blijft – de agent kan goed presteren op een vaste testset maar in productie heel andere queries tegenkomen. Daarom moet je testsets bijwerken met nieuwe randgevallen en voorbeelden die echte scenario's weerspiegelen. Een mix van kleine "smoke test"-gevallen en grotere evaluatiesets is nuttig: kleine sets voor snelle controles en grotere voor bredere prestatiemetingen.

### Online evaluatie

![Overzicht observeerbaarheidsmetrics](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Dit verwijst naar het evalueren van de agent in een live, real-world omgeving, d.w.z. tijdens daadwerkelijk gebruik in productie. Online evaluatie omvat het monitoren van de prestaties van de agent op echte gebruikersinteracties en het continu analyseren van resultaten.

Bijvoorbeeld, je kunt succespercentages, gebruikerstevredenheidsscores of andere metrics op live verkeer bijhouden. Het voordeel van online evaluatie is dat het **dingen vastlegt die je in een laboratoriumomgeving misschien niet voorziet** – je kunt modeldrift in de loop van de tijd waarnemen (als de effectiviteit van de agent afneemt door veranderende inputpatronen) en onverwachte queries of situaties opvangen die niet in je testdata stonden. Het biedt een waarheidsgetrouw beeld van hoe de agent zich in het wild gedraagt.

Online evaluatie omvat vaak het verzamelen van impliciete en expliciete gebruikersfeedback, zoals besproken, en mogelijk het uitvoeren van shadow-tests of A/B-tests (waarbij een nieuwe versie van de agent parallel draait om te vergelijken met de oude). De uitdaging is dat het moeilijk kan zijn om betrouwbare labels of scores voor live-interacties te krijgen – je kunt vertrouwen op gebruikersfeedback of downstream-metrics (zoals of de gebruiker op het resultaat klikte).

### De twee combineren

Online en offline evaluaties sluiten elkaar niet uit; ze zijn zeer complementair. Inzichten uit online monitoring (bijv. nieuwe soorten gebruikersqueries waarbij de agent slecht presteert) kunnen worden gebruikt om offline testdatasets aan te vullen en te verbeteren. Omgekeerd kunnen agents die goed presteren in offline tests vervolgens met meer vertrouwen in productie worden uitgerold en online worden gemonitord.

Veel teams hanteren zelfs een lus:

_evalueer offline -> implementeer -> monitor online -> verzamel nieuwe foutgevallen -> voeg toe aan offline dataset -> verfijn agent -> herhaal_.

## Veelvoorkomende problemen

Wanneer je AI-agents in productie inzet, kun je verschillende uitdagingen tegenkomen. Hier zijn enkele veelvoorkomende problemen en mogelijke oplossingen:

| **Issue**    | **Potential Solution**   |
| ------------- | ------------------ |
| AI Agent not performing tasks consistently | - Verfijn de prompt die aan de AI-agent wordt gegeven; wees duidelijk over de doelstellingen.<br>- Identificeer waar het opdelen van taken in subtaken en het laten afhandelen door meerdere agents kan helpen. |
| AI Agent running into continuous loops  | - Zorg dat je duidelijke beëindigingsvoorwaarden hebt zodat de Agent weet wanneer het proces moet stoppen.<br>- Voor complexe taken die redeneren en plannen vereisen, gebruik een groter model dat gespecialiseerd is in redeneertaakten. |
| AI Agent tool calls are not performing well   | - Test en valideer de output van de tool buiten het agentsysteem.<br>- Verfijn de gedefinieerde parameters, prompts en naamgeving van tools.  |
| Multi-Agent system not performing consistently | - Verfijn de prompts die aan elke agent worden gegeven om ervoor te zorgen dat ze specifiek en onderscheidend zijn.<br>- Bouw een hiërarchisch systeem met behulp van een "routing" of controller-agent om te bepalen welke agent de juiste is. |

Veel van deze problemen kunnen effectiever worden geïdentificeerd met observeerbaarheid op zijn plaats. De traces en metrics die we eerder bespraken helpen precies te bepalen waar in de agent-workflow problemen optreden, waardoor debuggen en optimalisatie veel efficiënter wordt.

## Kosten beheren
Hier zijn enkele strategieën om de kosten van het inzetten van AI-agenten in productie te beheersen:

**Kleinere modellen gebruiken:** Kleine taalmodellen (SLMs) kunnen goed presteren bij bepaalde agentachtige gebruiksscenario's en zullen de kosten aanzienlijk verlagen. Zoals eerder vermeld, is het opzetten van een evaluatiesysteem om prestaties ten opzichte van grotere modellen te bepalen en te vergelijken de beste manier om te begrijpen hoe goed een SLM zal presteren voor jouw gebruiksscenario. Overweeg SLMs te gebruiken voor eenvoudigere taken zoals intentieclassificatie of parameterextractie, terwijl je grotere modellen reserveert voor complex redeneren.

**Een routermodel gebruiken:** Een vergelijkbare strategie is het gebruik van een diversiteit aan modellen en groottes. Je kunt een LLM/SLM of serverloze functie gebruiken om verzoeken op basis van complexiteit naar de meest geschikte modellen te routeren. Dit helpt ook om kosten te verlagen en tegelijk de prestaties voor de juiste taken te waarborgen. Bijvoorbeeld, stuur eenvoudige queries naar kleinere, snellere modellen, en gebruik dure grote modellen alleen voor complexe redeneertaken.

**Antwoorden cachen:** Het identificeren van veelvoorkomende verzoeken en taken en het vooraf leveren van de antwoorden voordat ze door je agentensysteem gaan, is een goede manier om het aantal soortgelijke verzoeken te verminderen. Je kunt zelfs een flow implementeren om te bepalen hoe vergelijkbaar een verzoek is met je gecachte verzoeken met behulp van meer basale AI-modellen. Deze strategie kan de kosten aanzienlijk verlagen voor veelgestelde vragen of veelvoorkomende workflows.

## Laten we kijken hoe dit in de praktijk werkt

In het [voorbeeldnotebook van deze sectie](./code_samples/10_autogen_evaluation.ipynb) zien we voorbeelden van hoe we observability-tools kunnen gebruiken om onze agent te monitoren en te evalueren.


### Heb je meer vragen over AI-agenten in productie?

Sluit je aan bij de [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) om andere leerenden te ontmoeten, deel te nemen aan spreekuren en antwoorden op je vragen over AI-agenten te krijgen.

## Vorige les

[Ontwerppatroon Metacognitie](../09-metacognition/README.md)

## Volgende les

[Agentische protocollen](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vrijwaring:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de brontaal moet als de gezaghebbende bron worden beschouwd. Voor kritieke informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->